# Status Log — Protocol Phase 0

Log of actions undertaken. Newest first. Append a dated entry at the end of any session that changed state.

## 2026-06-25 (pm) — Job 2: found 6 broad-archetype candidates with real PDFs

- **Scope settled with Dave: BROAD** — single-day experimental-medicine archetype, any readout (not microdose-only).
- **Corrected a wrong lessons note:** real protocol PDFs are NOT rare in the Early Phase 1 universe. The 463 phase:0+docs:prot studies almost all carry a real `hasProtocol:true` PDF. The scarce thing is the *archetype*, not the PDF. The old "only ~2 with a PDF" finding was an artefact of the over-narrow `microdose` keyword.
- **`phase:0` is a junk filter for us** — "Early Phase 1" is a grab-bag (453-pt RCTs, vaccines, herbal medicine). Phase tag is unreliable; can't isolate the archetype by phase.
- **Working discriminator:** PET receptor-occupancy / radioligand-eval / pharmacological-challenge (fMRI/biomarker) studies in healthy or small-n, with a protocol PDF. The generic "single dose PD" set (134 hits) is mostly conventional SAD/MAD → excluded per rules.
- **6 candidates confirmed (real protocol PDF verified via largeDocs):**
  - NCT05725005 — ASN51 PET target occupancy, healthy n=12 (Asceneuron). Strong.
  - NCT03861000 — novel PDE4D PET radioligand eval, n=3 (NIMH). Strong; tracer = microdose, straddles narrow.
  - NCT03019289 — pridopidine sigma-1/D2 receptor occupancy, healthy+HD n=23 (Prilenia). Strong.
  - NCT04128683 — dopamine pharmacological-challenge fMRI (placebo/amisulpride/bromocriptine, drug 3h pre-scan), crossover n=31 (UCSD). Strong; cleanest dose-anchored SoA.
  - NCT03511105 — GSK2798745 segmental LPS alveolar-challenge model, healthy n=47 (GSK). Good mechanistic challenge.
  - NCT04805983 — BMS-984923 safety/PK + receptor occupancy, n=36 (Yale). Weakest — dose-escalation, SAD-like.
- **Not done:** onboarding to `protocol_corpus` (needs corpus repo mounted + pipeline run; ground truth outside Cowork). Awaiting Dave's keep/trim call.

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
