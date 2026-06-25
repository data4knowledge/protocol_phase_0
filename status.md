# Status Log — Protocol Phase 0

Log of actions undertaken. Newest first. Append a dated entry at the end of any session that changed state.

## 2026-06-25 — Job 1 (definition) + report scaffold + project state files

- **Defined the study type and terminology.** Wrote `docs/phase0_definition_and_terms.md` covering definition, microdose thresholds, ICH M3(R2) 5 approaches, FDA eIND, CTG "Early Phase 1", full term list, exclusions. Verified regulatory facts via web.
- **Reframed the project** with Dave: target is the SoA-shape archetype (single-day experimental medicine), not microdose chemistry. Locked the project purpose. Established corpus-vs-project layering (corpus = any ct.gov protocol PDF; project = Phase 0 subset).
- **Corrected two of my own unjustified claims** (Dave pushed back): "dense SoA" was my inference not the spec (demoted to a job-3 hypothesis); USDM "has no clean representation" for periodic/continuous monitoring was wrong — USDM uses a cyclic sub-timeline with an elapsed-time exit. Captured the behaviour rule in `lessons_learned.md`.
- **Found prior art:** `protocol_soa_patterns/docs/reports/soa_patterns.html` already maps 12 SoA patterns to USDM (USDM covers all). Reframed job 3 to only chase the Phase-0 delta. Confirmed the 169-protocol scan is thin on this population.
- **Scaffolded the single project report:** `docs/report/phase0_soa.md` → themed `phase0_soa.html` via `report_theme/build.py`. Part 1 written; Parts 2 & 3 are placeholders. Build verified (theme inlined, tables render).
- **Set up portable project state:** created `status.md`, `next_steps.md`, `lessons_learned.md`; added session protocol to `CLAUDE.md`; reduced `memory.md` to a redirect.
- **Not done:** jobs 2 (find protocols) and 3 (characterise SoAs) — see `next_steps.md`.

## 2026-06-23 — Onboarded two Phase 0 / microdose protocols

- Added **NCT02901925** (ABY-029, glioma) and **NCT01532024** (NAP, acute lung injury) to `protocol_corpus`: real protocol PDF + ctgov.json, registered and enriched in `registry.yaml`, `sync_registry --mode validate` clean.
- Ground truth **not** generated (run outside Cowork — AI-backed, needs API key).
