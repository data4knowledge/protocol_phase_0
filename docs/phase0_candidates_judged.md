# Phase-0 Candidate Judgement — union-search batch (2026-06-25)

16 candidates from the ranked union search were ingested into `protocol_corpus`
and read for archetype fit. Corpus keeps all 16 (a protocol is a protocol);
the Phase-0 project selects the **IN** set below. Verdicts come from reading the
protocols, not metadata.

## Verdicts

| NCT | What it is | n / pop | SoA form | Timing anchor | Verdict |
|---|---|---|---|---|---|
| NCT04202497 | LSD1 enzyme-occupancy PET, tracer microdose | 7 healthy | grid | dose/scan | IN |
| NCT06390098 | ASN51 target-occupancy PET | 3 healthy | grid* | dose/scan | IN |
| NCT02551653 | GSK2256098 biodistribution PET, microdose | 10 mixed | grid (T&E) | dose/scan | IN |
| NCT04394845 | [18F]GTP1 biodistribution PET | 6 healthy | grid | dose/scan | IN |
| NCT05128058 | Ritlecitinib target occupancy | 16 healthy | grid | dose | IN |
| NCT03306589 | LPS / GM-CSF challenge | 12 healthy | grid | challenge | IN |
| NCT04310423 | Endotoxin inflammatory challenge | 76 mixed | grid | dose/challenge | IN |
| NCT03512171 | Fallypride + amphetamine challenge PET | healthy | narrative + scan list | dose/challenge | IN |
| NCT04251221 | PBR28 + alcohol challenge PET | 50–100 | narrative + scan list | challenge | IN |
| NCT04236986 | PBR28 + LPS challenge PET (PTSD) | 80–160 | narrative + scan list | challenge | IN |
| NCT04057807 | PBR28 + LPS challenge PET (AD) | 16 | narrative + visits | challenge | IN |
| NCT03958630 | TSPO radioligand PET | 13 mixed | coarse grid | multi-year visits | BORDERLINE |
| NCT04204993 | Human influenza challenge | 20 healthy | narrative + grid | challenge (days) | BORDERLINE |
| NCT04234672 | [14C]TAK-831 ABA + mass-balance | 6 healthy | grid + PK lists | dose | OUT |
| NCT03907540 | [14C]-KD025 ABA + mass-balance | 5 healthy | grid + PK lists | dose | OUT |
| NCT04965389 | Milvexian microtracer + food-effect | 17 healthy | grid (2) | dose | OUT |

*NCT06390098's grid is real ("Schedule of Events", Table 1, ~p14-15); the Tier-2
finder fallback mis-pointed at a narrative section so its SoA built empty —
recoverable with a manual `soa.pdf` carve.

**Tally:** 11 IN, 2 BORDERLINE, 3 OUT.
- **BORDERLINE** reasons: NCT03958630 = archetype exposure but multi-year longitudinal diagnostic structure; NCT04204993 = right (infection-challenge) spirit but multi-day confinement, not single-day.
- **OUT** reasons: all three are conventional clinical pharmacology — ¹⁴C absolute-bioavailability + therapeutic-dose mass-balance/ADME (excluded), or formulation/food-effect. The microtracer is only the ABA component, not the study's purpose. (The read decided these, as predicted from metadata.)

## Findings for Part 3

1. **The SoA splits in two.** ~Half carry a conventional activity×timepoint grid; the other half — academic PET + challenge studies — have **no table at all**: a narrative "Study Procedures" section plus a scan-timing prose list. This is why the page-finder found nothing on them. A USDM SoA would have to represent a schedule the source protocol never drew as a grid.
2. **A distinct timing anchor: the challenge agent.** Alcohol, LPS, amphetamine, endotoxin, influenza — assessments are timed "3 h post-LPS" / "post-alcohol", relative to a challenge administration, not the study drug. Separate axis from dose-relative timing.
3. **The visit/Encounter axis collapses** (thesis confirmed): single scan-day / challenge-day studies; "when" = dose-time, scan-time, or challenge-time, not visit-day.

## USDM questions to test (Dave's call — not yet asserted)

- Can USDM anchor a timeline on a **challenge-agent administration** as cleanly as on the study drug?
- Does a protocol that presents its schedule **only as narrative prose** (no grid) round-trip into USDM's SoA structures without inventing a table the protocol never had?
