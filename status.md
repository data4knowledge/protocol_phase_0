# Status Log — Protocol Phase 0

Log of actions undertaken. Newest first. Append a dated entry at the end of any session that changed state.

## 2026-06-25 (eve, 7) — Both USDM questions closed as non-issues; pattern stated; session paused

- **Both USDM questions are non-issues.** Q1 (challenge anchor) was never a real question — a timeline times events off other events; "study drug" vs "challenge" is a clinical label, not a modelling one. Q2 (narrative round-trip) is no delta — USDM stores activities + times, not a table.
- **The archetype reduces to one claim (Dave):** every case is an **intervention with timing measured from it** — usually after, sometimes before (prep). That is ordinary timeline behaviour → no USDM problem.
- **NOT yet verified against the real protocols.** I twice trusted the `phase0_candidates_judged.md` one-liners and got burned (NCT03306589's LPS is the study drug, not a challenge). Open task = mount `protocol_corpus`, read all 12 extracted schedules, confirm each is intervention-anchored, flag any that aren't. Doubt up front: NCT03861000 (no grid), NCT04204993 (multi-day influenza).
- **Session paused by Dave** — pick up at next_steps item 3.

## 2026-06-25 (eve, 6) — Resolved verdicts; answered both USDM questions by tracing DDF-RA v4.0

- **Borderlines resolved (Dave):** IN set = **12** — the 11 clean IN + **NCT04204993** (influenza challenge, kept as the days-scale challenge edge case). **NCT03958630** (TSPO multi-year longitudinal) set aside; stays in corpus, out of Phase-0. 3 OUT unchanged.
- **Mounted `DDF-RA` and traced both Job-3 USDM questions** against `API/USDM_API.json` + `CT/USDM_CT.xlsx` + `RULES/USDM_CORE_Rules.xlsx` (v4.0). Full answers + rule IDs in `lessons_learned.md`.
  - **Q1 challenge anchor = not a real question** (Dave). A timeline times events off other events — that's what timelines do; "study drug" vs "challenge" is a clinical label, not a modelling one. CT carries a "Challenge Agent" role (C158128) as an optional label, nothing more. (NCT03306589's LPS is the study drug — my "3h post-LPS challenge" example was wrong, pulled from the summary table not the protocol.)
  - **Q2 narrative round-trip = YES, no delta** (corrected — first answer "flow skeleton delta" was wrong, Dave called it). SoA is a timing graph not a matrix; narrative supplies activities + timings = the graph's content. The timeline container (mainTimeline DDF00012, exit DDF00108/DDF00037, Fixed Reference anchor DDF00009, ordering DDF00008) is unconditional on EVERY timeline → a gridded protocol needs the identical scaffolding, so it's not invented from the narrative and not a Phase-0 delta. The ISO8601 "throughout" worry repeated the already-settled continuous-monitoring case (cycling sub-timeline + elapsed-time exit), not a gap.
- **Both USDM questions land on NO delta.** Net so far: the Phase-0 archetype's two candidate USDM frictions (challenge anchor, narrative-only schedule) both dissolve on tracing — USDM handles them with existing primitives + CT.
- **Next:** write Part 2 (the 12-protocol set) + Part 3 (SoA characterisation + USDM delta) of `docs/report/phase0_soa.md` and rebuild HTML.

## 2026-06-25 (eve, 5) — Corpus repo hygiene (sidecars/markers); lean cleanup reverted

- **Decision: keep ie/soa/schema.pdf sidecars AND `.*_pdf_autogen` markers tracked.** Dave uses the sidecars to navigate; untracking risks loss on clone/`git clean`. Markers must stay paired (sidecar with no marker reads as curated → build won't regenerate). See `lessons_learned.md` → Corpus repo hygiene.
- **What the markers are:** a note beside each auto-made sub-extract PDF storing its page range (duplicates `unvalidated.pages.<section>` — verified identical) plus the one bit it uniquely carries: autogen (overwrite OK) vs reviewer-curated (leave). Could be folded into the data model — logged in corpus `docs/next_steps.md` → Tidy-up backlog.
- **Lean-repo cleanup considered then REJECTED.** I had Dave run a `git rm --cached` over 1038 derived files; we then decided sidecars must stay. Left the repo half-done (1038 staged deletions + same 1038 now untracked = the "1K files" churn). Fix: **`git reset`** from corpus root (index-only, disk untouched) → restores all to tracked; only the 16 new protocols (97 files) remain as legit new content to commit. `.gitignore` already reverted; temp list files removed.

## 2026-06-25 (eve, 4) — Judged the 16; Job 3 characterisation begun

- **Read all 16** (4 from extracted SoA, 12 via subagents). Verdicts: **11 IN, 2 BORDERLINE, 3 OUT** — full table + reasons in `docs/phase0_candidates_judged.md`. Phase-0 set ~triples.
- **3 OUT** = ¹⁴C ABA/mass-balance + food-effect (conventional clin-pharm, excluded); the read decided them as the metadata-borderline cases predicted. They STAY in corpus, excluded from the Phase-0 subset.
- **Three Part-3 findings:** (1) SoA splits — half conventional grid, half NO table (narrative "Study Procedures" + scan-timing prose; this is why the finder found nothing); (2) a distinct **challenge-agent** timing anchor (LPS/alcohol/amphetamine/endotoxin/influenza — "3 h post-LPS"); (3) visit/Encounter axis collapses to dose/scan/challenge time.
- **Two USDM questions to test (Dave's call):** can USDM anchor a timeline on a challenge-agent admin like on study drug; does a narrative-only (no-grid) schedule round-trip into USDM SoA without inventing a table.
- **Cleanup deferred:** NCT06390098 manual `soa.pdf` carve (grid = "Schedule of Events" Table 1); consider refining the Tier-2 fallback (can mis-target a narrative "Procedures and Assessments" section when the grid is elsewhere — finder-None only, produces empty not wrong).

## 2026-06-25 (eve, 3) — Ingested 16 union candidates; SoA state mapped

- **Ran the ranked union search (Dave, terminal):** 161 union hits; all 5 corpus + dropped NCT04805983 surfaced and ranked sensibly (ranking validated). Quoting fix needed first (unquoted phrases → 11,844 junk; quoted → 161).
- **Ingested 16 new candidates** (`phase0_ingest_ids.txt`) into corpus: download-pdf + scan + build_ground_truth (vision). All 16 wrote OK.
- **SoA state of the 16:**
  - 4 clean SoAs extracted: NCT05128058 (2 tbl/29), NCT04394845 (1/17), NCT03306589 (1/26), NCT04965389 (2/36).
  - 2 finder MIS-TARGETS (Tier-2 fallback anchored a narrative "Procedures and Assessments" section; real grid elsewhere → vision returned empty): NCT06390098 (grid = "Schedule of Events"/Table 2), NCT03907540 (Quotient microtracer; grid past the narrative). Recoverable via manual soa.pdf.
  - 10 finder found NO schedule: NCT04202497, NCT03958630, NCT02551653, NCT03512171, NCT04251221, NCT04236986, NCT04057807, NCT04310423, NCT04204993, NCT04234672. Likely genuine no-conventional-grid (archetype thesis) but unconfirmed — needs reading.
- **Tooling note:** the Tier-2 SoA fallback can mis-target when a narrative "Procedures and Assessments" section exists separately from the grid (gated, finder-None only, produces empty not wrong data). Consider refining later.
- **Next = Job 3 read:** judge archetype fit + characterise SoA shape (grid / narrative / scan-timing list / none; dose- vs challenge- vs visit-anchored) per protocol.

## 2026-06-25 (eve, 2) — Extended corpus `search` for union candidate-finding

- **Settled the search-filter debate with data.** Pulled live CT.gov counts (docs:prot): current recipe + `healthy:y` = 29; drop `healthy:y` = 73; microdose/sub-therapeutic = 36; "experimental medicine" = 37; endotoxin/LPS challenge = 8; target/PET occupancy = 11; whole Early-Phase-1+PDF universe = 463. Two levers: drop `healthy:y` (patients are in-archetype) and broaden keywords beyond the PET-centric set.
- **Killed the phase filter.** Checked phases of the 5 kept: only NCT04128683 is EARLY_PHASE1; the other 4 are PHASE1 (one PHASE1+2). Early Phase 1 as a filter would lose 4 of 5. Phase tag fails both ways (noisy + under-inclusive). Use as a supplementary slice only, never the frame.
- **Layering locked (Dave):** corpus accepts any PDF — no archetype gate; Phase-0 usefulness is a project-layer judgement made by reading the SoA. Metadata = reading-order aid, not exclusion.
- **Extended `protocol_corpus/scripts/fetch_ctgov_protocols.py` `search`:** multi `--term` union+dedupe, server-side `docs:prot`, triage leaf-fields (phase/n/purpose/model/healthy), `_plausibility` ranking, `--limit` applied AFTER ranking, `--csv` output. Validated offline (parser, trim, scoring, union/dedupe/rank/cap/CSV all pass; archetype +11 vs Phase-3-1053pt −9). Live run is Dave's terminal — recipe in next_steps.

## 2026-06-25 (eve) — Fixed the SoA page-finder for the experimental-medicine archetype

- **Found why 4 of 5 SoAs were empty.** Ground truth for NCT04128683/NCT05725005/NCT03019289/NCT03861000 had `soa: []` with `extractors: []`. Cause traced to `protocol_corpus/scripts/extractors/_pages.py`: the page-finder returned `soa_pages=None` for all four. They don't use a "Schedule of <noun>" caption — the whole project thesis showing up in the data.
  - NCT04128683 → "Study Procedures Chart" (p6). NCT03019289 → "Table 1: Study Procedures and Assessments" (p59). NCT05725005 → caption-less timing grid (p51-53) under "Procedures and observations"; its only "Schedule of procedures" heading is on the TOC page (correctly filtered). NCT03861000 → **no SoA grid at all** (zero cell-marks); narrative visits + "Table 5: Number of visits".
- **Fix:** added a gated Tier-2 fallback (`SOA_FALLBACK_PATTERNS`) to `_pages.py`, consulted ONLY when the canonical SoA pass finds nothing. Patterns: Study Procedures Chart; Table/Appendix N: (Study) Procedures and Assessments; Procedures/Assessments by|per Visit; Procedures and observations.
- **Regression-proof by construction + tested.** Snapshotted finder output for all 222 protocols before/after. Result: 3 changed, all None→pages, **0 existing results altered**. The 3 are exactly NCT04128683 (p6-15), NCT03019289 (p58-67), NCT05725005 (p47-56) — spans cover each real table. NCT03861000 stays None (honest — no table to find).
- **Rebuild done (Dave, terminal).** `build_ground_truth.py --ids-from` rebuilt the 3. SoA now populated: NCT04128683 = 2 tables (Community + UCSD cohorts, 12/11 activities); NCT05725005 = "Schedule of Procedures", 31 activities/13 cols; NCT03019289 = "Study Procedures and Assessments", 29 activities/7 cols. All via `soa_vision_soa_v4` / claude-sonnet-4-6. Fix validated end-to-end.
- **NCT03861000 resolved: no SoA.** Reviewed its nearest artefact (Table 5, "Number of visits and time commitment of participants"): a cohort(Phase 1-4) × Visit#1-5 grid, each cell a bundle of discrete activities + an italicised participant time-commitment ("6 hours"). Not an SoA grid (no activity rows, no timing marks). Decision: keep `soa: []` in corpus, document Table 5 in the report as a specimen of visit-axis collapse. The time-commitment column is derivable from activity procedure durations → NOT a USDM delta (see lessons). All 5 SoAs now settled (4 populated, 1 documented-empty). Ready for Job 3.

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
