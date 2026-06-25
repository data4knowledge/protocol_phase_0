# Next Steps — Protocol Phase 0

The current plan. Single source of truth for "what now". Newest plan on top; rewrite as priorities change.

## Now — Job 3 (characterise SoAs + USDM delta) + write the report

Protocol set is in hand: the original 5 + 11 new **IN** candidates (verdicts + findings in `docs/phase0_candidates_judged.md`). Search, ingest and judgement are done. What's left:

1. **Resolve the verdicts with Dave.** Confirm the 11 IN / 2 BORDERLINE / 3 OUT calls. OUT (NCT04234672, NCT03907540, NCT04965389) stay in corpus, out of the Phase-0 subset. Borderline (NCT03958630 longitudinal diagnostic; NCT04204993 multi-day influenza challenge) — include or set aside?
2. **Test the two USDM questions** (Dave is the authority — trace the model, don't assert):
   - Can USDM anchor a timeline on a **challenge-agent administration** as cleanly as on the study drug?
   - Does a **narrative-only (no-grid) schedule** round-trip into USDM SoA without inventing a table the protocol never had?
3. **Write Part 2** (the protocol set) and **Part 3** (SoA characterisation + USDM impact) of `docs/report/phase0_soa.md` from the three findings, then rebuild the HTML (`python3 report_theme/build.py docs/report/phase0_soa.md`).

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
