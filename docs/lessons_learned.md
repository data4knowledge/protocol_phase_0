# Lessons Learned — Protocol Phase 0

Decisions and knowledge we don't want to lose. Append on new decisions/facts; remove only if wrong.

## Project scope & architecture

- **Issues are traced against the SoA pattern atlas, and nothing else (Dave, 2026-09-21).**
  `protocol_soa_patterns/docs/reports/soa_patterns.html` is the reference: **12 patterns**
  (`normal`, `pk_profile`, `cycles`, `extension_period`, `subsidiary_tables`, `multi_track`,
  `heavy_footnoting`, `conditional_branches`, `ae_row`, `unscheduled_visits`,
  `early_termination`, `decentralised`), **21 footnote categories**, and **11 USDM mechanisms
  A–K**. An issue is traced when it is named against that vocabulary — which pattern it is, and
  which mechanism the atlas gives for it. **Mapping and tracing are therefore one job, not two.**
  *This replaces tracing against DDF-RA.* That was never a decision: it was how the 2026-06-25
  session happened to answer two questions, `lessons_learned` recorded it with "Dave to
  validate", `next_steps` carried it forward as an instruction, and on 2026-09-21 I promoted it
  into `aims.md` and then into a hard build check without asking. The June DDF-RA answers below
  stay as history; they are not the standard. **Consequence, recorded honestly:** issues 2, 3 and
  5 had been marked "traced" on DDF-RA reasoning, and under the atlas standard none of the six is
  traced. The vocabulary is copied into `docs/report_source.yaml` and `scripts/build_report.py`
  rejects a name that is not in it.

- **Scope NARROWED (Dave, 2026-09-21) — three protocols removed from the target set.**
  **NCT02901925** (no SoA at all, reviewer-confirmed 0 timelines), **NCT03861000** (visits only,
  no grid) and **NCT04057807** (narrative plus visits) are out of the analysis. All three fail the
  boundary in `aims.md`: their timing hangs off visit days or off nothing, not off an intervention
  in sub-day units. Chosen goes **27 → 24**; the 36 active protocols are those 24 plus the 12
  SAD/MAD candidates. **They stay in `protocol_corpus`** — rejection here is a judgement about
  this analysis, never about the corpus. Two findings made on them survive and are kept: the
  NCT03861000 "Table 5" result (participant time commitment is derivable, not a USDM gap) and the
  observation that roughly half the early-phase population carries no SoA grid at all. **Note what
  this costs:** the set no longer contains a documented specimen of schedule *absence*, so if the
  report wants to say anything about narrative-only protocols it must say where the evidence came
  from.

- **Scope EXPANDED (Dave, 2026-09-21) — SAD and MAD are IN.** Single and Multiple Ascending Dose studies join the existing early-phase / experimental-medicine definition. **This reverses a recorded exclusion** — "conventional Phase 1 SAD/MAD" was listed under *Exclude* in this file, and NCT04805983 was rejected in `project_protocols.md` for being "SAD-like". Both reversed; the old lines are annotated in place, not deleted. **Why it is worth it:** not more evidence for the existing five issues, but a sixth structure they do not exercise — the **cohort / dose-level axis** (one printed SoA instantiated per ascending cohort), **sentinel dosing** (a within-cohort split with its own offset), **escalation decision gates** (cohort *n+1* conditional on the safety review of cohort *n*), and **MAD repeat-dosing days** (intensive PK on first and last dosing day, middle days collapsed into a spanning cell). Written up as issue 6 in `phase0_definition_and_terms.md`. **The USDM verdict on issue 6 is OPEN — not traced, do not assert it.** **Oncology dose escalation stays out** (escalates in patients against response, cycle-based — a Phase 2/3 shape). **Evidence needed no new search:** twelve in-scope ascending-dose protocols were already onboarded in `protocol_corpus`; four carry a reviewer-confirmed timeline count. **Folded into the chosen list on 2026-09-21 (Dave)**, taking it to 36. **Known weakness: ten of the twelve are Eli Lilly**, on top of an already Lilly-heavy chosen list — the set needs non-Lilly SAD/MAD before any issue-6 finding is publishable, or it reads as one sponsor's house style.
- **Scope REFRAMED (Dave, 2026-07-02) — still the same project, was loosely specified.** The real deliverable is the **USDM delta for concrete SoA-representation patterns**, evidenced by four Lilly/Loxo Phase-1 clin-pharm protocols — NCT05469126, NCT05176314, NCT06085482, NCT05444556 — plus a scoping document (`sources/EMP Study.docx`). *(`sources/protocols.docx` named those four and is no longer in `sources/`; ids inlined 2026-09-21 so the reference stops dangling.)*. The five patterns: (1) interval activities crossing day boundaries (8h urine bins), (2) dose-relative extended-hour timing (24–240h), (3) predose "P" per-cell marker, (4) footnote-encoded semantics (windows, repeats, conditionals, ordering), (5) parallel timeline starting pre-dose. **This reopens the earlier "no USDM delta" conclusion** — that was reached on too narrow a framing (challenge-anchor + narrative round-trip only). The single-day-archetype boundary is NO LONGER the frame; do not exclude these four for being conventional clin-pharm DDI/PK.
- **Project purpose (original, locked 2026-06-25 — superseded by the 2026-07-02 reframe above):** characterise one under-represented trial type — single-day "experimental medicine" / Phase 0 studies — and find the specific issues their SoAs raise for USDM, vs the existing 12-pattern atlas. The general SoA→USDM mapping is already done elsewhere; this project only finds the **Phase-0 delta**.
- **Two layers, kept separate:** `protocol_corpus` is general purpose — any study with a posted protocol PDF, **sourced only from ClinicalTrials.gov**, no Phase 0 filter. This project (`protocol_phase_0`) pulls a Phase 0 subset by our definition.
- **The real target is SoA shape, not drug chemistry.** Microdose/PK is a well-defined subset, not the boundary. The archetype (from Dave): "Phase 0 / early phase / experimental medicine", often single-day, small population, many such trials run.

- **Corpus grew to 27 (2026-07-26): NCT05262387** — exercise-challenge T1D study, the first
  entry that is (a) in patients rather than healthy volunteers and (b) anchored on a physical
  challenge rather than a dose or scan. Its assessment-day sub-timeline exercises issues 1, 2, 4
  and 5 simultaneously, so it is the natural worked example when the report needs one protocol
  that shows the interaction of the patterns rather than one pattern each. Heavily CCI-redacted —
  usable for structure, not for timing values.

## USDM / SoA facts (Dave is the authority — trace before asserting)

- **Discrete point-in-time actions** (1h, 2h… off dosing): USDM handles cleanly — scheduled activity instance with a relative timing offset.
- **Parallel / continuous monitoring** ("measure X every N min", continuous ECG; shown as merged horizontal cells + footnote): USDM **handles this** — a separate timeline that cycles the activity with an **exit condition on elapsed time** (one timeline reference, not exploded instances). *Do NOT call this a gap — I did, and was wrong.*
- **The traditional "visit" largely doesn't apply** — single encounter / continuous stay, axis is time-relative-to-dosing, not visit days. Whether USDM absorbs this cleanly (Encounter-modality / main-timeline primitives) is the open job-3 question.
- **Prior art — `protocol_soa_patterns/docs/reports/soa_patterns.html`:** 12 SoA patterns + 21 footnote categories over 169 protocols / 1,759 footnotes, mapped to 11 USDM primitives. Thesis: USDM carries all patterns; only 2 soft enhancement candidates (`state_preparation`, `activity_variant`). The "dense PK sampling" pattern (`pk_profile`, 68%) = dose-anchored sub-timeline. This scan is **thin on single-day experimental-medicine protocols** — that gap is this project.
- **Participant time commitment / burden is NOT a USDM gap (Dave, 2026-06-25).** NCT03861000's "Table 5" shows a "(6 hours)" per visit labelled "time commitment of participants". This is derivable — generated by summing the procedure durations off the activities in that visit — so it's a computed view, not a primitive USDM must store. Do not log it as a candidate delta. (Killed my earlier "duration-on-encounter" hypothesis, which wrongly read it as a scheduling/encounter duration.)
- **Behaviour rule:** never assert USDM/standards mechanics as fact without tracing the model or flagging it as a guess. Dave will catch it.

### Two Job-3 USDM questions — ANSWERED by tracing DDF-RA v4.0 (2026-06-25)

Traced against `DDF-RA/Deliverables`: `API/USDM_API.json` (class+cardinality), `CT/USDM_CT.xlsx` (codelists), `RULES/USDM_CORE_Rules.xlsx` (CORE conformance, v4.0 column). Not asserted from memory — Dave to validate.

- **Q1 — challenge-agent anchor: NOT A REAL QUESTION (Dave, 2026-06-25).** A timeline positions events relative to other events — that is what a timeline is. There is no privileged anchor in USDM; you time things off whichever event you pick. "Study drug" vs "challenge" is a clinical label, not a modelling distinction. So "can USDM anchor on the challenge as well as the drug" was never a question — yes, trivially, the same way a calendar holds any appointment. (I also misused NCT03306589 as a challenge example off the one-line summary table — in that protocol LPS IS the study drug, so its timing is ordinary dose-anchored. Lesson: read the protocol before naming it; the judged-table one-liners are not enough.) The only thing on the model side worth a footnote: USDM CT carries a `StudyIntervention.role` term "Challenge Agent" (C158128) if you want to *label* a provocation as such — a terminology nicety, not a scheduling capability. Whether any of our 12 even uses a challenge distinct from the study drug needs confirming by reading, not asserted.
- **Q2 — narrative-only round-trip: YES, round-trips cleanly, NO delta.** (Earlier "flow skeleton delta" was WRONG — Dave called it, 2026-06-25.) USDM's SoA is a **timing graph, not a matrix**; the grid is only a rendering. A narrative supplies activities + relative timings = exactly the graph's content, so the absence of a printed table is irrelevant — USDM never consumed a table. `Encounter`/`epoch` optional (epoch only a WARNING, DDF00080) → no fabricated visits/columns. **The structural container is NOT a delta:** mainTimeline (DDF00012), ≥1 exit (DDF00108) + instance pointing to it (DDF00037), ≥1 Fixed Reference anchor (DDF00009), per-instance default-condition/exit linkage (DDF00008) are **unconditional on every `ScheduleTimeline`** — a gridded protocol needs the identical scaffolding; the modeller supplies it equally either way. Not invented *from* the narrative, not specific to it. **The ISO8601 / "periodically/throughout" point repeated the already-settled continuous-monitoring case** (separate cycling sub-timeline with elapsed-time exit) — handled, NOT a gap; same error already logged above. Net: narrative form is not disadvantaged vs grid form. Q2 = no delta, like Q1.

## SoA-shape findings (Phase-0 archetype — from the 16-protocol read, 2026-06-25)

- **Two SoA shapes in the archetype.** ~Half carry a conventional activity×timepoint grid; the other half (academic PET + challenge studies) have **no SoA table at all** — a narrative "Study Procedures" section plus a scan-timing prose list. The page-finder finding nothing on these is the signal, not a bug. Open USDM question: does a narrative-only schedule round-trip into USDM SoA without inventing a table the protocol never had?
- **Challenge-agent timing anchor.** Distinct axis: assessments timed relative to a challenge administration (LPS, alcohol, amphetamine, endotoxin, influenza — "3 h post-LPS"), not the study drug. Open USDM question: can USDM anchor a timeline on the challenge agent as cleanly as on the study drug? (Both flagged for Dave; not asserted.)
- **Archetype boundary the read enforces (metadata can't):** ¹⁴C absolute-bioavailability + therapeutic-dose mass-balance/ADME, and formulation/food-effect studies are OUT even when they contain an IV microtracer — the microtracer is only the ABA component, not the study purpose. Confirmed on NCT04234672, NCT03907540, NCT04965389. **— REVERSED on those three (Dave, 2026-07-02): all three were moved OUT→IN under the SoA-shape reframe and are in the chosen list. The boundary above still stands as a rule; these three are the stated exceptions, kept for their table structure. Annotated 2026-09-21 after a review caught the contradiction.**
- **The chosen/rejected protocol list lives in** `docs/project_protocols.md` (the project corpus).

## Corpus repo hygiene (decided 2026-06-25)

- **KEEP the ie/soa/schema.pdf sidecars tracked** — Dave uses them as reviewer-navigation aids; untracking risks loss on fresh clone / `git clean`. Do NOT gitignore or `git rm --cached` them.
- **The `.*_pdf_autogen` markers stay tracked too** — they must travel paired with their sidecar (a sidecar with no marker reads as reviewer-curated → build freezes it, never regenerates). Markers showing in GitHub Desktop after an ingest are just normal new content.
- A "lean repo" pass was considered and **rejected** for this reason. `git rm --cached` only untracks (disk files untouched) — but untracked ≠ safe here.

## Regulatory / definition facts

- **Microdose** = below all of: ≤100 µg total (≤500 µg / ≤5 doses repeat), ≤1/100 NOAEL, ≤1/100 PAD; ≤30 nmol for biologics.
- **ICH M3(R2):** 5 exploratory-trial approaches (1–2 microdose, 3–5 non-microdose sub-therapeutic). **FDA Exploratory IND (eIND)** guidance 2006 created the US "Phase 0" route. EMA aligns with ICH.
- **ClinicalTrials.gov has no Phase 0 value** — these register as **Early Phase 1**.
- **Exclude** (keep searches clean): ~~conventional Phase 1 SAD/MAD~~ **— REVERSED 2026-09-21, SAD/MAD are now IN SCOPE (see Project scope above)**; oncology window-of-opportunity (Phase 0 label but often not sub-therapeutic); psychedelic "microdosing"; therapeutic-dose mass-balance/ADME.

## CTG search recipe (the good one)

**Implemented in `scripts/search.py`** — that script encodes everything below and is the
thing to run. Moved there from the repo root on 2026-09-21; its module docstring explains
each filter. The notes here are the reasoning behind it, kept because the reasoning is what
gets forgotten.

Find Phase 0 / microdose studies with a real protocol PDF:
```
https://clinicaltrials.gov/api/v2/studies?query.term=microdose%20OR%20microdosing%20OR%20%22sub-therapeutic%22&aggFilters=phase:0,docs:prot&countTotal=true&pageSize=60
```
- `docs:prot` is **noisy** — it flags studies that merely *declare* a protocol in the IPD statement. Always confirm an actual PDF via per-study `DocumentSection.largeDocumentModule.largeDocs` (field name case-sensitive: `DocumentSection` works; `LargeDocumentModule` alone returns empty).
- CDN download: `https://cdn.clinicaltrials.gov/large-docs/<last2 of NCT>/<NCT>/<filename>`.
- ~463 Early Phase 1 with a protocol doc overall. **CORRECTION (2026-06-25):** real PDFs are NOT rare — nearly all docs:prot studies carry a real `hasProtocol:true` largeDocs PDF. Only the *microdose-titled* subset was thin (2). The scarce thing is the **archetype**, not the PDF.
- **`phase:0` is a junk filter** for the archetype — "Early Phase 1" is a CTG grab-bag (453-pt RCTs, vaccines, herbal medicine). Drop it. Search by `query.term` for the archetype signature + `aggFilters=docs:prot,healthy:y`.
- **Working discriminator for the broad archetype:** PET "receptor occupancy" / radioligand evaluation / "pharmacological challenge" (fMRI/biomarker), healthy or small-n. The generic "single dose" + "pharmacodynamic" set (~134) is mostly conventional SAD/MAD — which was an exclusion until 2026-09-21 and is **no longer one**. That set is now a candidate pool, not noise; re-run it if the twelve corpus SAD/MAD protocols prove too Lilly-concentrated.
- **PDF verification:** `filter.ids=` gets stripped by the fetch redirect — use the single-study endpoint `…/api/v2/studies/NCT?fields=NCTId,DesignModule,DocumentSection`. Bulk list pages cap around pageSize≈25 in this fetch tool (larger returns empty).

## SoA page-finder (corpus pipeline)

- **The SoA extractor only runs when it has pages.** `protocol_corpus/scripts/extractors/soa.py` input priority: (1) `source/soa.pdf` sidecar if present → rasterise all; (2) else page-finder `soa_pages`; (3) neither → empty scaffold, `extractors: []`, no error. An empty `soa: []` with `extractors: []` means the finder found nothing, NOT that vision failed.
- **`schema.pdf`/`soa.pdf`/`ie.pdf` sidecars** are auto-carved by `build_ground_truth.py` (`_autogen_section_pdfs`) from page-finder ranges, or via `--sub-extracts-only` (no API spend). `extract_pdf_pages.py` carves `--ie`/`--soa` manually (no `--schema`).
- **Single-day experimental-medicine protocols often have no canonical SoA caption.** Observed captions instead: "Study Procedures Chart", "Table N: Study Procedures and Assessments", caption-less timing grids, or no SoA table at all (narrative visits). This is the project thesis, visible in the page-finder's misses.
- **Fix added 2026-06-25:** `SOA_FALLBACK_PATTERNS` in `_pages.py`, a Tier-2 pass gated behind the canonical pass being empty — so it can only turn None→hit, never alter a resolved protocol. Regression contract: any change to a currently-non-None `soa_pages` is a regression. Test by snapshotting `find_section_pages().soa_pages` over all protocols before/after and diffing.

## Operational

- Canonical store: `protocol_corpus` — data in `protocols/<NCT>/source/` (PDF + ctgov.json), `registry.yaml`, pipeline scripts in `scripts/`. Run fetch/sync/build_ground_truth from there, not from this repo.
- `build_ground_truth.py` is AI-backed (needs ANTHROPIC_API_KEY in `protocol_corpus/.development_env`) — run from terminal/VSCode, **not in Cowork**.
- Cowork gotcha: `sync_registry.py --mode scan` / full `--mode enrich` time out at the 45s bash limit (touch all ~235 entries). Use `--only NCT…`. Sandbox deps: `pip install --break-system-packages requests ruamel.yaml pyyaml pymupdf`.
- Report build needs `pip install markdown`.

## Protocols in hand

- **NCT02901925** — ABY-029, fluorescence-guided microdose, recurrent glioma (Dartmouth-Hitchcock, n=14).
- **NCT01532024** — NAP, optical/neutrophil-activation imaging probe, acute lung injury (Univ. Edinburgh, n=15).
- Both are **imaging** microdose studies, not classic AMS/PK. Ground truth not yet generated (see next_steps / run outside Cowork).

## Pharma Phase 1 / experimental-medicine search & onboarding (2026-06-29)

- **CT.gov v2 API gotchas (cost real time this session):**
  - There is **no `PHASE0`** value. Phase 0 == `EARLY_PHASE1`. Filter phase with `aggFilters=phase:0|1|2|3|4` (NOT `filter.phases`, which is not a real param).
  - Sponsor type: `aggFilters=funderType:industry|nih|other|fed`. Posted protocol PDF: `aggFilters=docs:prot`. These compose: `phase:1,funderType:industry,docs:prot`.
  - `documentSection` is a **top-level sibling of `protocolSection`**, not nested inside it. Reading `protocolSection.documentSection` silently yields nothing (cost a "0 protocols have PDFs" false alarm).
  - Multi-value `filter.overallStatus` is comma-separated.
- **Why pharma is near-absent from posted Phase 0/1 protocols:** posting is voluntary (Phase 0/1 are not "applicable clinical trials" under FDAAA), so academia/NIH post and pharma posts the legal minimum (~nothing). Pharma DOES run the studies; they're just labelled Phase 1 and the protocols aren't posted. The doc-bearing set skews academic/NCI by construction.
- **The 17 pharma Phase 1 set** is corpus enrichment (ABA/mass-balance, microtracer, PET occupancy, SAD). **Partly superseded 2026-09-21:** the SAD members are no longer out of scope by class. Still: don't fold anything into the project subset without reading it.

## SoA page-finder — more (2026-06-29)

- **pymupdf-missing is a SILENT trap.** `_pages.find_section_pages` guards `if fitz is None: return empty`. With no pymupdf installed, EVERY section returns empty for EVERY protocol, **instantly**, and the SoA extractor then writes `soa: []` with no error — indistinguishable from "vision failed". If a whole batch comes back with empty SoA in ~0.3s/protocol, suspect the dep, not the patterns. (This was the entire cause of the empties in the Cowork sandbox; `pip install --break-system-packages pymupdf` fixes it. On Dave's machine pymupdf is present, so his runs were fine.)
- **4 SoA caption patterns added to `_pages.py` for the pharma Phase 1 style** (verified hits, no regression):
  1. broadened `_SOA_KEYWORDS`: optional `(?:study\s+)?` after "schedule of" + singular-tolerant nouns (`assessments?`, `events?`, `procedures?`, …) → catches "Schedule of Study Procedures" (NCT03811834) and singular forms.
  2. new: `study plan and timing of procedures` (NCT03463525, AstraZeneca).
  3. new: `study events? flow ?chart` (NCT03311841, Merck).
- **Two SoA shapes patterns can't reach** (no anchorable heading text): caption-less image grids (NCT03733990 → manual `soa.pdf` via `extract_pdf_pages.py --soa`) and fully **redacted** SoAs (NCT04992442 → see below).

## Redacted / unavailable SoA — convention (2026-06-29)

- **No dedicated field existed; use the `validated` block** (it survives re-extraction; `unvalidated.*` is rewritten every run). Mark the section reviewer-signed-empty with a reason:
  ```yaml
  validated:
    content: { soa: [] }
    signoff:
      soa: { by: dih, date: 2026-06-29, note: "SoA redacted in source — ...; intentionally empty; do not create source/soa.pdf." }
  ```
- Safe because `soa: []` validates (it's the not-applicable state) and `signoff` has **no strict schema** (consumers only check truthiness + `.keys()`), so the extra `note` key is tolerated. Audits keying off `validated.signoff.soa` see it resolved, not a finder gap.
- The per-table `has_cci_redactions` flag is for redactions *inside* an otherwise-extracted table — does NOT apply when the whole SoA is redacted (no table objects exist).

## What changed in `protocol_corpus` (noted 2026-09-21)

This project last touched the corpus on 2026-07-26. It has moved a long way since, and
several things this project relied on are now named differently or superseded. Verified
against the repo on 2026-09-21, not read off its documents.

- **The corpus roughly doubled.** ~533 protocol directories on disk; the corpus set lists
  **506** NCT ids, and its `CLAUDE.md` now states 531 protocols (506 NCT + 25 CORP) + 1 template.
  Any note in this repo quoting the old "234 protocols" is stale.

- **`scripts/corpus.py` IS the pipeline now.** One command, seven stages (fetch →
  ground-truth → workbook → fill → roundtrip → extract → compare), driven by `<IDS>` /
  `--target-set` / `--all` / `--remaining`. `run_pipeline.py` is retired to `scripts/archive/`.
  **Do not hand-assemble `fetch_ctgov_protocols.py` + `sync_registry.py` +
  `build_ground_truth.py` into a sequence** — the stages do work a hand-run misses. The
  onboarding commands recorded in this project's older notes predate it.

- **Three named sets, nested, and a figure without a set name is not a result.**
  `protocol_corpus/docs/sets/inner_set.txt` (**T1, 15** — protocols carrying a handcrafted workbook, used by
  `usdm_training`; the only set with content ground truth, so gate 2 and above are measured
  here), `protocol_corpus/docs/sets/measured_set.txt` (**T2, 104** — every protocol with a reviewer-confirmed
  timeline count, frozen 2026-09-19; gate 1 is measured here), `protocol_corpus/docs/sets/corpus_set.txt`
  (**T3, 506** — every NCT protocol). **T1 ⊂ T2 ⊂ T3 is the intent, and does not hold today** —
  NCT04677179, NCT05089734 and NCT06142383 are in the inner set with no reviewer count. Tracked
  as `N34` in the corpus register; do not re-report it. Inner-set membership is likewise the
  *aim*, not the state: the set file says "carry, **or are meant to carry**" a workbook.
  The T1/T2/T3 labels were *reused* on
  2026-09-21 — an older note using them means a disjoint partition, not this nesting.
  **Retired names, and using one is a finding:** "full set", "test set", "measurement set",
  "baseline cohort", "target set", "the 104", "the 15".
  *Caution: these files were renamed from `full_set` / `test_set` at 12:49 on 2026-09-21,
  mid-session. The corpus moves on Dave's other machine without this repo hearing about it —
  read the set files before quoting them, never this note.*

- **`protocol_corpus/docs/issues.md` is the one register.** Open defects AND open decisions, one list.
  Numbering: bare number = a GitHub issue in the named repo, `N`-prefix = local placeholder.
  A finding this project makes about the corpus becomes a row there — not a local fix here,
  and not a second register.

- **`protocol_corpus/docs/plan.md` is gone** (deleted 2026-09-20), along with its `known_fixes`, `pipeline`,
  `baseline_cohort`, `soa_curation_lessons` and `multi_design_protocols` documents. Content went to that repo's own `aims.md`, `programme.md`, `issues.md`, `next_steps.md`,
  `measurement_plan.md` and `README.md`. **Any pointer in this project to `protocol_corpus/docs/plan.md` is dead.**

- **`validated.soa_timelines` exists and is the reviewer's count of SCHEDULES, not printed
  tables.** `{count, cci, by, date, note}` in `ground_truth.yaml`, set with
  `scripts/set_soa_pages.py set <ID> <range> --timelines N`. Four headed tables that are one
  schedule split into parts count as **1**. This did not exist when this project last looked, and
  it is the single most useful new signal here: **13 of the protocols this project references now
  carry a reviewer-confirmed timeline count**, so claims about how many schedules a protocol has
  no longer have to be eyeballed. `validated.pages.<section>` likewise now overrides the
  page-finder — the reviewer states the real range, and it drives the sub-extracts and the
  vision drafters.

- **PDF page numbers, never printed page numbers.** Corpus-wide convention: every page number
  anywhere — `validated.pages`, notes, issue rows, conversation — is the PDF page (1-indexed
  from the PDF's first page), not the number in the protocol's footer, which a cover sheet
  commonly shifts. The `source/{ie,soa}.pdf` sub-extracts carry a generated title page, so
  sub-extract page *k+1* is the *k*th page of the range. Translate before quoting.

- **`protocol_corpus/docs/working/timeline_disagreements.md`** is the live sheet of reference-vs-extracted
  timeline-count deltas. Relevant here: several early-phase protocols sit in it, and a
  disagreement on one of ours is evidence about the SoA's structure, not just a pipeline defect.

### Where this project's protocols now stand in the corpus

The file names 42 NCT ids: **36 chosen + 6 rejected**. Of the 36 chosen:

- **All 36 are in the corpus.** Across the whole file only **NCT04805983** is not — reopened on
  2026-09-21 but never onboarded, so it has no PDF, no ground truth and no registry entry, and it
  sits in the rejected list. Bringing it in is a decision, not a formality.
- **12 carry a reviewer-confirmed timeline count** and are in the frozen **measured set** (T2).
  (It was 13 until NCT02901925 left the target set on 2026-09-21.)
- **2 carry a handcrafted USDM workbook**, and both — **NCT06085482** and **NCT05262387** — are
  in the **inner set** (T1, 15 protocols). Those two are the only protocols here with
  content ground truth, which makes them the right place to ground any USDM claim that needs
  more than structure.

## Session lessons — 2026-09-21

The repo has no session log by design (the dated action log, formerly `status.md` under `docs/`,
was deleted this day; `CLAUDE.md` says why). These are the durable items — what would change how
the next session behaves. State is in `next_steps.md`; the destination is in `aims.md`.

**Sibling repos touched:** `protocol_corpus` and `protocol_soa_patterns`, both **read only** —
nothing was written to either. The only outstanding item owed to a sibling is a register row for
NCT06390098 in `protocol_corpus/docs/issues.md`.

- **`sources/EMP Study.docx` is a SCOPING document, not evidence (Dave).** Notes plus SoA
  screenshots, written to frame the problem at the start. **The issue it was written to raise is
  monitoring timelines that span visits and days** — a measurement series running as its own
  schedule across the study-day columns instead of sitting in one cell. That is issues 1 and 5 and
  it is the centre of the question; the other four came out of chasing it. Consequence: strings
  quoted from its *images* are scoping notes, and were never protocol evidence. Do not cite them
  in the report as though they were.

- **NCT05469126's ground truth carries the evidence — and a counting bug nearly cost a day.**
  Its extracted SoA holds **18 activities, 12 timepoints and 11 conditions**, and the conditions
  carry the real footnote text, including the full PK series for both crossover periods. Issues 2,
  3 and 5 were re-quoted straight from it. **Earlier the same day I recorded it as "1 table, 2
  activities, 2 timepoints — a stub", labelled "checked, not assumed", in two documents, and
  built a plan around budgeting for a vision read.** The cause: `activities` is
  `{found: bool, items: [...]}`, and I called `len()` on the dict, which is 2. **Count
  `[...]['items']`, never the wrapper** — the shape is in
  `protocol_corpus/docs/spec/ground_truth_shape.md`, and a suspiciously round "2 activities, 2
  timepoints" should have been the tell.

- **The issue-2 series is two crossover periods, not one — settled from the ground truth.**
  Period 1 doses Day 1 (`P … 96 (D5)`), Period 2 doses Day 21 (`P … 120 (D26), 168 (D28),
  240 (D31)`), each restarting the clock. The screenshot transcription had merged them, which is
  why `96 (D5)` appeared to sit beside `120 (D26)`. The *pattern* the issue claims — running
  hours past 24 with the calendar day in parentheses — was right throughout.

- **Issues 1 and 4's evidence is not in NCT05469126.** No urine collection among its eighteen
  activities; none of "± 1.5 hours", "triplicate", "until resolution" or the ECG/vitals/bloods
  ordering among its eleven footnotes. Either the scoping screenshots are of a different protocol,
  or the extractor missed them — the first makes the report's attribution wrong, the second makes
  it a corpus defect. **Unresolved, and these are the two issues most likely to be the real
  delta.** Ranked first in `next_steps.md`.

- **`protocol_corpus` moves under this project mid-session.** Its set files were renamed
  `full_set`/`test_set` → `measured_set`/`inner_set` at **12:49 on 2026-09-21**, between two reads
  in the same session, from Dave's other machine. A note in this repo about the corpus is a
  snapshot with a short life. **Read the corpus files; never quote this repo's notes about them.**

- **Don't argue a scope boundary from facts the project has flagged as unusable.** `aims.md`
  briefly justified its boundary with "n=104 running to Day 31" — where n=104 is a candidate not
  yet read and "Day 31" comes from the transcription the project itself marks as not holding
  together. A rule propped up by its own open questions is circular. Fixed the same day; worth
  remembering because it read as perfectly reasonable when written.

- **A completion test that nothing closes is unreachable.** `aims.md` originally said the project
  was done when no issue failed the four tests — with nothing closing the issue *set*, so "done"
  was reachable by declaring the list closed. There is now a closure rule (a pass over the SoA of
  every chosen protocol turning up no new pattern) and a ranked item that performs it. Any future
  completion test needs the same treatment: ask what makes the list stop growing.

- **An exclusion with exceptions has to name them.** `lessons_learned` recorded NCT04234672,
  NCT03907540 and NCT04965389 as OUT on the mass-balance boundary; Dave had moved all three IN on
  2026-07-02 and the lesson was never annotated, so the two documents contradicted each other for
  eleven weeks without anyone noticing. Annotate a reversal where the original rule sits.

- **`search.py` → `scripts/search.py`** (2026-09-21), matching the sibling repos, with a module
  docstring carrying what it does, how to run it, and why each filter is what it is. It is the
  **candidate finder**; onboarding is `protocol_corpus/scripts/corpus.py` and nothing here writes
  to the corpus. An earlier judgement in this session that the script was dead and should be
  deleted was wrong on both counts — it defaults to `phase="1"`, so the "`phase:0` is a junk
  filter" lesson never applied to it.

- **The `review-focus` skill is now general**, over any repo carrying aims / next_steps /
  lessons_learned, with per-repo specifics in `references/<repo>.md` (only `protocol_corpus` has
  one). Two review passes over this repo on 2026-09-21 found ~25 real defects, most of them
  introduced the same day by the session that was tidying it. **Running the review after an edit
  session is worth more than running it before one.**

- **The report is generated now, and that is the structural change of the day.**
  `docs/report_source.yaml` holds the prose, evidence, atlas placements and verdicts;
  `scripts/build_report.py` parses the protocol set out of `docs/project_protocols.md` and
  assembles `docs/report/early_phase_soas.md`, then chains to `report_theme/build.py`.
  **The markdown is overwritten — never hand-edit it.** Six conditions fail the build, the useful
  two being a `traced` verdict with no atlas mechanism, and any atlas name outside the vocabulary.
  Every count in the report is computed. It exists because the hand-typed version drifted: 26 vs
  27 protocols, one footnote quoted two ways in two files, three issues marked traced citing
  nothing.

- **`search.py` → `scripts/search.py`, and `requirements.txt` added** (pyyaml, markdown,
  requests). An earlier judgement in this session that `search.py` was dead and should be deleted
  was wrong twice over — it defaults to `phase="1"`, so the "`phase:0` is a junk filter" lesson
  never applied to it, and it is the only candidate-finding tool the project has.

- **Run the review after an edit session, not before one.** Three review passes over this repo on
  2026-09-21 found roughly thirty-five real defects, and the large majority were introduced the
  same day by the sessions that were tidying it — including the NCT05469126 counting bug above,
  which was recorded in two documents as a verified fact and drove the ranked next step for
  several hours. A reviewer that only reads what a session wrote about itself finds nothing.

