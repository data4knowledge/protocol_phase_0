# Protocol Phase 0 — Working Memory

Terse, dated log of decisions and state changes. Newest first.

## Canonical store: protocol_corpus

This project (protocol_phase_0) holds Phase 0 curation, analysis, and notes only.
The source of truth is the sibling repo ../protocol_corpus:
- Protocol data: protocol_corpus/protocols/<NCT>/source/ (PDF + ctgov.json)
- Registry: protocol_corpus/registry.yaml
- Pipeline: protocol_corpus/scripts/{fetch_ctgov_protocols,sync_registry,build_ground_truth}.py
- Secrets: protocol_corpus/.development_env (ANTHROPIC_API_KEY)

ALL fetch / sync / build_ground_truth commands below run from protocol_corpus, NOT here.

## 2026-06-23 — Onboarded two Phase 0 / microdose protocols

Added NCT02901925 and NCT01532024 to the corpus (Phase 0 microdose PK/PD hunt for Dave).

State now:
- Both have `source/<NCT>.pdf` (real Protocol/SAP PDF from CTG largeDocumentModule) + `source/ctgov.json`.
- Both registered in `registry.yaml` and enriched:
  - NCT02901925 — Dartmouth-Hitchcock, Glioma, common_name ABY-029 (ABY-029 microdose evaluation in recurrent glioma, n=14).
  - NCT01532024 — University of Edinburgh, Acute Lung Injury, common_name NAP (Neutrophil Activation Probe optical imaging in lungs, n=15).
- `sync_registry --mode validate` clean for both (the CORP0010/0001/0007/0019 drift lines are pre-existing, unrelated).

NOT done — pick up here:
- Ground truth not generated. Run from VSCode/terminal (AI-backed, needs ANTHROPIC_API_KEY in `.development_env` — do NOT run in Cowork):
  ```
  python scripts/build_ground_truth.py NCT02901925 --apply
  python scripts/build_ground_truth.py NCT01532024 --apply
  ```
- Open question Dave raised: both are imaging/optical-probe microdose studies, not classic oral-AMS PK microdosing. Kept for now. If corpus aim leans PK-centric, may swap — but almost nothing PK-oriented has a posted protocol PDF on CTG.

### CTG search recipe (the good one)

"Phase 0 / exploratory IND / microdose" maps to **Early Phase 1** on ClinicalTrials.gov (`aggFilters=phase:0`).

Find microdose Phase 0 studies that have a real protocol PDF:
```
https://clinicaltrials.gov/api/v2/studies?query.term=microdose%20OR%20microdosing%20OR%20%22sub-therapeutic%22&aggFilters=phase:0,docs:prot&countTotal=true&pageSize=60
```
Results (2026-06-23): ~462 Early Phase 1 with a protocol doc overall; only ~2 microdose-titled ones with an *actual* PDF — the two above. ~59 microdose Phase 0 exist total but most never post a protocol (Phase 0/imaging usually aren't FDAAA "applicable trials", so upload is voluntary).

CAVEAT: the `docs:prot` aggFilter is noisy — it also flags studies that merely *declare* a protocol in the IPD-sharing statement with nothing uploaded. Always confirm an actual PDF via the per-study `documentSection.largeDocumentModule.largeDocs` (field name is case-sensitive: `DocumentSection` works, `LargeDocumentModule` alone returns empty). CDN download pattern: `https://cdn.clinicaltrials.gov/large-docs/<last2 of NCT>/<NCT>/<filename>`.

### Cowork gotcha

`sync_registry.py --mode scan` and full `--mode enrich` time out at the 45s Cowork bash limit (they touch all ~235 entries / hit CTG per NCT). Use `--only NCT…` to scope. Deps to install in sandbox: `pip install --break-system-packages requests ruamel.yaml pyyaml pymupdf`.
