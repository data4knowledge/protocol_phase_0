"""
search.py — the candidate finder for protocol_phase_0.

WHAT IT DOES
    Queries the ClinicalTrials.gov API v2 for trials matching a keyword scope plus
    server-side filters, pages through the ENTIRE result set via `nextPageToken`, and
    writes one row per trial to a CSV.

    It finds candidates. It does not download anything and does not touch the corpus.
    Onboarding a candidate — PDF, ctgov.json, registry entry, ground truth — is
    `protocol_corpus/scripts/corpus.py`, and that is the only thing that should do it.

HOW TO RUN
    python3 scripts/search.py                 # the default hunt (see below)
    python3 scripts/search.py "Oncology"      # same, narrowed by condition

    Writes `pharma_phase1_results.csv` in the current working directory. Needs
    `requests`; no API key.

THE DEFAULT HUNT
    phase:1, funderType:industry, docs:prot, statuses that tend to carry a posted
    document, and DEFAULT_KEYWORDS = "Phase 0" OR "Exploratory IND" OR "Microdose" OR
    "Experimental Medicine". That combination produced the 17-protocol industry
    Phase 1 set on 2026-06-29.

    To run a different hunt, change `DEFAULT_KEYWORDS` — do not write a second script.
    For the ascending-dose search in `docs/next_steps.md` step 5, that means
    "single ascending dose" OR "multiple ascending dose" OR "first in human",
    everything else unchanged.

    Quote multi-word phrases. Unquoted phrases are parsed as a bare OR of words and
    the net explodes — 11,844 hits against 161 on the run that taught us this.

OUTPUT COLUMNS
    NCT_ID, Title, Sponsor, Sponsor_Class, Phase, Has_Protocol_Doc,
    Planned_Enrollment, Allocation, URL

WHY THE FILTERS ARE WHAT THEY ARE
    phase       The `aggFilters` shorthand, 0-4. There is no PHASE0 value in the API;
                Phase 0 is EARLY_PHASE1, which `phase:0` selects. Do NOT frame a hunt
                on it — "Early Phase 1" is a CTG grab-bag (453-patient RCTs, vaccines,
                herbal medicine) and most early-phase pharma work is labelled Phase 1.
                Keywords do the scoping; the phase filter is a supplementary slice.
    funderType  industry | nih | other | fed. Posting a Phase 0/1 protocol is
                voluntary, so academia and NIH post and pharma posts close to nothing.
                Expect an academic skew on any hunt that does not force industry.
    docs:prot   Server-side "has a posted protocol document". NOISY — it also flags
                studies that merely declare a protocol in the IPD statement, which is
                why `Has_Protocol_Doc` is recomputed per study from
                `documentSection.largeDocumentModule.largeDocs`. Trust that column,
                not the filter.

    `documentSection` is a TOP-LEVEL sibling of `protocolSection`, not nested inside
    it. Reading `protocolSection.documentSection` silently yields nothing and looks
    like "no study has a PDF".

    Fuller notes: `docs/lessons_learned.md` section "CTG search recipe".
"""

import requests
import json
import csv
import sys

# Default keyword set: "experimental medicine" flavour (microdose / exploratory IND).
# This is what scopes Phase 1 down to the single-day / early-mechanistic studies we
# care about, rather than all of Phase 1.
DEFAULT_KEYWORDS = '"Phase 0" OR "Exploratory IND" OR "Microdose" OR "Experimental Medicine"'

# Statuses that tend to have a posted protocol PDF (not just RECRUITING).
DEFAULT_STATUSES = ["COMPLETED", "TERMINATED", "ACTIVE_NOT_RECRUITING",
                    "RECRUITING", "ENROLLING_BY_INVITATION"]


def search_trials(phase="1", funder="industry", condition=None,
                  keywords=DEFAULT_KEYWORDS, statuses=None,
                  with_docs_only=True, page_size=100, max_pages=None):
    """
    Query ClinicalTrials.gov API v2 and page through the full result set.

    API notes (v2):
      * There is no "PHASE0" value; Phase 0 is encoded as EARLY_PHASE1.
        Use aggFilters phase shorthands instead: phase:0,1,2,3,4.
      * Sponsor type is filtered with aggFilters funderType:industry|nih|other...
      * documentSection is a TOP-LEVEL sibling of protocolSection, not nested in it.

    phase           "0" | "1" | "2" | "3" | "4"  (aggFilters phase shorthand)
    funder          "industry" | "nih" | "other" | "fed" | None (no funder filter)
    condition       optional disease-area string (e.g. "Oncology")
    keywords        Essie query.term string; pass None/"" to disable keyword scoping
    statuses        list of overallStatus values; defaults to DEFAULT_STATUSES
    with_docs_only  if True, only return trials with a posted protocol/SAP PDF
                    (server-side via aggFilters docs:prot)
    page_size       results per request (max 1000)
    max_pages       stop after N pages (None = everything)
    """
    url = "https://clinicaltrials.gov/api/v2/studies"
    statuses = statuses or DEFAULT_STATUSES

    agg = [f"phase:{phase}"]
    if funder:
        agg.append(f"funderType:{funder}")
    if with_docs_only:
        agg.append("docs:prot")

    params = {
        "aggFilters": ",".join(agg),
        "filter.overallStatus": ",".join(statuses),
        "pageSize": page_size,
        "countTotal": "true",
    }
    if keywords:
        params["query.term"] = keywords
    if condition:
        params["query.cond"] = condition

    trials = []
    token = None
    pages = 0
    total = None

    print("Requesting data from ClinicalTrials.gov API...")
    print(f"  phase={phase} funder={funder} docs_only={with_docs_only} "
          f"keywords={'yes' if keywords else 'no'} condition={condition or '-'}")
    while True:
        if token:
            params["pageToken"] = token
        try:
            r = requests.get(url, params=params, timeout=30)
            r.raise_for_status()
            data = r.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            break

        if total is None:
            total = data.get("totalCount")
            if total is not None:
                print(f"API reports {total} total matching trials.")

        for item in data.get("studies", []):
            ps = item.get("protocolSection", {})
            ident = ps.get("identificationModule", {})
            nct_id = ident.get("nctId", "N/A")

            ls = ps.get("sponsorCollaboratorsModule", {}).get("leadSponsor", {})
            design = ps.get("designModule", {})

            docs = (item.get("documentSection", {})
                    .get("largeDocumentModule", {}).get("largeDocs", []))
            has_doc = any(d.get("hasProtocol") or
                          d.get("typeAbbrev") in ("Prot", "Prot_SAP") for d in docs)

            trials.append({
                "NCT_ID": nct_id,
                "Title": ident.get("briefTitle", "N/A"),
                "Sponsor": ls.get("name", "N/A"),
                "Sponsor_Class": ls.get("class", "N/A"),
                "Phase": "/".join(design.get("phases", []) or ["N/A"]),
                "Has_Protocol_Doc": has_doc,
                "Planned_Enrollment": design.get("enrollmentInfo", {}).get("count", "N/A"),
                "Allocation": design.get("designInfo", {}).get("allocation", "N/A"),
                "URL": f"https://clinicaltrials.gov/study/{nct_id}" if nct_id != "N/A" else "N/A",
            })

        pages += 1
        token = data.get("nextPageToken")
        if not token or (max_pages and pages >= max_pages):
            break

    print(f"Collected {len(trials)} trials across {pages} page(s).\n")
    return trials


def write_csv(trials, path):
    fields = ["NCT_ID", "Title", "Sponsor", "Sponsor_Class", "Phase",
              "Has_Protocol_Doc", "Planned_Enrollment", "Allocation", "URL"]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(trials)
    print(f"Wrote {len(trials)} rows to {path}")


# --- Execution Example ---
if __name__ == "__main__":
    # Default target: industry-sponsored Phase 1 experimental-medicine studies
    # that have a posted protocol PDF. Override condition via argv.
    condition = sys.argv[1] if len(sys.argv) > 1 else None
    trials = search_trials(phase="1", funder="industry",
                           condition=condition, with_docs_only=True)

    write_csv(trials, "pharma_phase1_results.csv")

    for t in trials:
        print(f"{t['NCT_ID']}  {t['Sponsor'][:35]:35}  |  {t['Title'][:55]}")
