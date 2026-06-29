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
