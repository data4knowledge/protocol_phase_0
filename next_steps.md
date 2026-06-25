# Next Steps — Protocol Phase 0

The current plan. Single source of truth for "what now". Newest plan on top; rewrite as priorities change.

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
