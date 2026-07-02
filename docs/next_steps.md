# Next Steps — Protocol Phase 0

The current plan. Single source of truth for "what now". Newest plan on top; rewrite as priorities change.

## NOW (2026-07-02) — map the EMP SoA-representation patterns to the atlas + USDM

Scope reframed by Dave (2026-07-02): this is the SAME Phase-0 piece, initially loosely specified. The deliverable is the **USDM delta for these concrete SoA-representation patterns** — NOT the single-day-archetype boundary. The prior "no USDM delta" conclusion was on too narrow a framing and is effectively reopened.

**Test set = the four in `sources/protocols.docx`, all already onboarded in `protocol_corpus`:**
NCT05469126 (=J2A-MC-GZGM, the EMP Example 2), NCT05176314, NCT06085482, NCT05444556.
Source docs: `sources/EMP Study.docx` (problem statement + SoA screenshots), `sources/protocols.docx` (the four IDs).

**Consolidated issue inventory — CONFIRM COMPLETE with Dave first (he may have a 6th):**
1. **Interval/window activities crossing day boundaries** — 24h urine in 8h bins (sometimes 4h): `0–8h, 8–16h, 16–24h`, cells merged across study-day columns. Activity with a duration (start→end), not a point.
2. **Dose-relative timing, extended-hour notation** — `24, 36, 48, 72, 96, 120, 168, 240h` rel. to dose as running hours, not day+clock. Extractor currently dumps these into free-text `conditions`.
3. **Predose "P" as a per-cell relative marker** — reusable "before the dose in this period" anchor.
4. **Footnote-encoded scheduling semantics** — windows (±1.5h), triplicate/repeat counts, conditional repeats ("if ISRs persist, repeat daily until resolution"), procedure ordering. Timing lives in the footnote, not the cell.
5. **Parallel timelines starting pre-dose** — continuous 24h monitoring of X that begins before dose and runs across it: a sub-timeline alongside the main dose-anchored timeline. (This is the general issue Dave named; relates to the already-logged continuous-monitoring case but the NEW angle is the pre-dose start.)

**Then, per pattern:**
a. Map to the 12-pattern atlas in `protocol_soa_patterns` (existing pattern / partial / absent). → **mount `protocol_soa_patterns` first.**
b. Assess USDM representability — TRACE against DDF-RA (API + CT + CORE rules), do not assert. Flag guesses. (Behaviour rule + no-unjustified-USDM-claims memory.)
c. Ground each claim in the actual protocol PDFs / ground truth, not the one-line summaries (that has burned me twice).

**Then write it up** into `docs/report/phase0_soa.md` and rebuild (`python3 report_theme/build.py docs/report/phase0_soa.md`). Only the delta — don't rebuild the general atlas.

Mounts needed next session: `protocol_soa_patterns` (atlas), `DDF-RA` (USDM tracing). Corpus + phase_0 already mount cleanly.

---


## Parallel thread (2026-06-29) — pharma Phase 1 experimental-medicine corpus

Separate from the Phase-0 Job-3 work below. Came out of "why no pharma Phase 0 protocols": pharma posts almost no early protocol PDFs, and their experimental-medicine work is labelled Phase 1. Pulled a 17-protocol industry Phase 1 set (posted protocols) into `protocol_corpus` to widen the corpus (NOT the Phase-0 subset).

State: 17 onboarded, registry enriched, ground truth built. SoA resolved on 14; finder patterns added for 3.

Remaining:
1. **NCT03733990** — SoA is caption-less image grids p21-32. Run (locally): `python3 scripts/extract_pdf_pages.py NCT03733990 --soa 21-32 && python3 scripts/build_ground_truth.py NCT03733990 --apply`.
2. **NCT04992442** — SoA redacted; DONE (validated signoff marks it intentionally empty; do not create a soa.pdf).
3. **Temp pids files** in corpus root (`phase1_pids.txt`, `phase1_new_pids.txt`, `soa_fix_pids.txt`) — delete once item 1 is done.
4. **Decide relationship to the report** — these 17 are pharma Phase 1, NOT the single-day Phase-0 archetype. Keep as corpus enrichment / contrast set, or pull any single-day ones into the Phase-0 subset? Open.

---


## Now — Job 3 (characterise SoAs + USDM delta) + write the report

Protocol set is in hand: the original 5 + 11 new **IN** candidates (verdicts + findings in `docs/phase0_candidates_judged.md`). Search, ingest and judgement are done. What's left:

1. ~~**Resolve the verdicts with Dave.**~~ **DONE (2026-06-25).** IN set = **12**: the 11 clean IN + **NCT04204993** (influenza challenge, included as the days-scale challenge edge case). **NCT03958630** (TSPO multi-year longitudinal) **set aside** — stays in corpus, out of Phase-0. OUT (NCT04234672, NCT03907540, NCT04965389) stay in corpus, out of subset.
2. ~~**Test the two USDM questions.**~~ **DONE (2026-06-25)** — traced against DDF-RA v4.0 (API + CT + CORE rules); full answers + rule IDs in `lessons_learned.md`. Headline: **Q1 (challenge anchor) = not a real question** — a timeline times events off other events; "study drug" vs "challenge" is a clinical label, not a modelling distinction. (CT does carry a "Challenge Agent" role C158128 as an optional label, nothing more. Also: NCT03306589's LPS is the study drug — bad example, don't repeat.) **Q2 (narrative round-trip) = YES, no delta** — SoA is a timing graph not a matrix; narrative supplies activities + timings = the graph's content; the timeline container (exit/anchor/ordering) is unconditional on every timeline so a gridded protocol needs it identically, hence not a Phase-0 delta. (Earlier "flow skeleton" framing was wrong; Dave corrected it.) **Validated with Dave.**
3. **PICK UP HERE — verify the pattern across all 12.** Both USDM questions closed as non-issues (see item 2). The whole archetype reduces to one claim: **every protocol is an intervention with timing measured from it (usually after; before when prepping).** That is ordinary timeline behaviour — no USDM problem. **But this is not yet verified against the actual protocols** — do NOT trust the `phase0_candidates_judged.md` one-liners (they already misled me: NCT03306589's LPS is the study drug, not a challenge). To verify: **mount `protocol_corpus`** and read each of the 12 extracted schedules, checking the timing anchor is an intervention — flag any anchored on something that ISN'T (a scan/sample that isn't an intervention, a calendar/visit day, or an event like a measurement threshold). Two to doubt up front: **NCT03861000** (no schedule grid at all — visits only, no timing) and **NCT04204993** (multi-day influenza confinement — timing may hang off study days, not one intervention).
4. **Then write Part 2** (the 12-protocol set) and **Part 3** (SoA characterisation). Given the above, the USDM section is now short: this archetype raises **no new USDM scheduling issue** — interventions with timing measured from them, which is what timelines do. Worked example optional. Rebuild HTML (`python3 report_theme/build.py docs/report/phase0_soa.md`). Reminder: only the Phase-0 delta vs the 12-pattern atlas — do NOT rebuild the general atlas.

### Cleanup / optional
- **NCT06390098** — real grid is "Schedule of Events" Table 1 (~p14-15) but the Tier-2 fallback mis-pointed; carve manually then rebuild:
  `python scripts/extract_pdf_pages.py NCT06390098 --soa 14-15 && python scripts/build_ground_truth.py NCT06390098 --apply`
- **Tier-2 finder fallback** can mis-target a narrative "Procedures and Assessments" section when the real grid is elsewhere (finder-None only, produces empty not wrong data). Refine if it recurs.

### Reference — settled this session
- Search filters: keyword union, `docs:prot`, NO `healthy:y`, all phases. Phase tag is useless (4 of 5 original kept are Phase 1, not Early Phase 1).
- `protocol_corpus` `search` extended: multi-`--term` union+dedupe, triage ranking, `--limit` after ranking, `--csv`. Quote phrases in `--term` or the net explodes (11,844 vs 161).
- SoA page-finder `_pages.py`: Tier-2 fallback added, regression-tested (0 existing results changed).
- Original kept 5: NCT04128683 · NCT05725005 · NCT03019289 · NCT03861000 (no SoA, documented) · NCT03511105. Dropped: NCT04805983.

Reminder for Part 3: only chase the Phase-0 delta vs the existing 12-pattern atlas — do **not** rebuild the general atlas.

## Open decisions to resolve

- **Scope: SETTLED — broad** (single-day experimental-medicine archetype, any readout). Confirmed against real candidates: occupancy/tracer PET, pharmacological + infection challenge, microdose imaging all kept; conventional clin-pharm (ABA/mass-balance/food-effect) excluded.
- **"EMP" meaning** — still unconfirmed (best guess Experimental Medicine Protocol). Watch for it verbatim in protocol PDFs.
