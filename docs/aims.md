# Aims — Protocol Phase 0

Where this project is going. **Rate of change: yearly.** Nothing dated belongs here.

The test for a line in this file: *would it still be true in a year?*
"Every issue carries a traced USDM verdict, not an asserted one" — yes.
"Issues 1 and 4 are still open" — no, that is state (`next_steps.md`).
"NCT05262387 is the worked example" — no, that is a choice about evidence.

## The destination

**A short, evidenced statement of what early-phase Schedules of Activities demand
of USDM, and whether USDM carries each demand.**

Not a survey of early-phase trials. Not a second SoA atlas. The general
SoA→USDM mapping already exists — `protocol_soa_patterns` catalogued twelve SoA
patterns and twenty-one footnote categories over 169 protocols and concluded USDM
carries them all. That scan is thin on short, dosing-anchored, footnote-heavy
early-phase tables. **This project works only that delta.**

The question that started it, and still the centre of it: **monitoring timelines that span
visits and days** — a measurement series running as its own schedule across the study-day
columns instead of sitting in one cell of the grid. Everything else in the issue list came out
of chasing that.

The output is one document: `docs/report/early_phase_soas.md`, built to HTML.

## What is in scope

**Early-phase experimental medicine.** The operative boundary is not a size or a duration.
Both were tried, and neither excludes anything: the set holds studies in the tens and in the
hundreds, and studies that run a day and studies that run weeks. It is this: **the SoA is anchored on an intervention and timed relative to it, in
sub-day units, rather than on a calendar of visits.** A protocol whose schedule reads
“Week 4, Week 8, Week 12” is out however small it is; one whose schedule reads
“predose, 0.5 h, 1 h, 24 h” is in however large.

Four families sit inside that boundary, all equally in:

1. **Clin-pharm PK / DDI** — crossover and drug-drug-interaction studies. Where
   the cell-level structure is sharpest.
2. **PET receptor-occupancy / radioligand-tracer** studies, including microdose tracers.
3. **Pharmacological- and infection-challenge** studies — LPS, endotoxin, alcohol,
   amphetamine, influenza, exercise.
4. **Dose-escalation first-in-human — SAD and MAD.** Sequential ascending-dose
   cohorts in healthy volunteers, single-dose or repeat-dose.

Strict Phase 0 / microdose is a *subset* of this, not the boundary. Neither drug chemistry
nor the registered phase label decides anything — both have been tried and both failed in
both directions.

**Study purpose is not irrelevant, and claiming otherwise would be dishonest.** Every
exclusion actually operated below is a purpose exclusion. The rule is narrower than “purpose
never matters”: purpose cannot put a protocol *in* that the timing boundary keeps out, and it
is used to keep protocols out only where the purpose reliably predicts a different SoA shape.
Where that prediction fails, the named exception wins — see the mass-balance exclusion below,
which carries three.

## What is out of scope

- **Calendar-anchored trials** — schedules built on visit days or weeks rather than on
  elapsed time from an intervention. Phase 2/3 and multi-year longitudinal designs.
  Their SoA problems are a different set and are already well covered.
- **Oncology dose escalation** — escalates in patients against response, and its schedule
  problem is cycle-based repetition, which is the calendar shape above.
- **Therapeutic-dose mass-balance / ADME and food-effect studies**, where the microtracer is
  only the ABA component and not the study purpose. **Three named exceptions are in the
  chosen list** — NCT04234672, NCT03907540 and NCT04965389 — kept for their table structure
  after a read. An exclusion with standing exceptions has to name them, or it is not a rule.
- Rebuilding or restating the twelve-pattern atlas. Cite it; do not reproduce it.
- Fixing the corpus pipeline. Extractor and page-finder defects belong to
  `protocol_corpus` and its issue register, not here.

## What counts as done

For **every** issue in the report, all four of these, or the issue is not finished:

| # | | |
|---|---|---|
| 1 | **Grounded** | evidenced in a named protocol's actual SoA — the PDF or the ground truth, never a one-line summary table |
| 2 | **Mapped** | placed against the twelve-pattern atlas: existing pattern, partial, or absent |
| 3 | **Traced** | the USDM verdict derived from DDF-RA — API, CT and CORE rules — with the class or rule id quoted |
| 4 | **Stated** | carried into the report with its verdict and its basis |

**And the issue list has to be closable, or “done” is unreachable by construction** — a new
issue can always be added, and one was added after the report had already been drafted. The list is closed when a pass over the SoA of
every protocol in the chosen list produces no timing or repetition pattern that is not already
on it. Until that pass has been made, the list is open and the project is not done, whatever
state the individual issues are in.

The project is done when the issue list is closed and the report holds no issue that fails any
of the four tests.

## Standing boundaries

**No USDM claim without a trace.** Every statement about what USDM can or cannot
represent is either traced against the model with the class or rule id quoted, or marked a
guess in the text. An untraced "X is a gap" is the failure mode this rule exists to stop, and
the project's record on it is bad — every such claim made so far has had to be retracted.
`lessons_learned.md` keeps the list.

**Read the protocol, not the summary.** Descriptor tables and one-line judgements
are a reading aid. Every claim about a protocol's SoA is made from the PDF or the
extracted ground truth.

**This project consumes `protocol_corpus`; it never writes to it.** Protocol data,
ground truth and the pipeline live there. Findings that are corpus defects become
rows in the corpus issue register, not local fixes.

**Two layers, kept separate.** `protocol_corpus` accepts any study with a real
posted ClinicalTrials.gov protocol PDF, with no archetype gate. This project selects
the early-phase subset used for the analysis; that selection is a judgement made by
reading, and it lives in `docs/project_protocols.md`.

**The corpus is the only source.** Real posted protocol documents from
ClinicalTrials.gov. No secondary summaries, no synthetic examples, no screenshots
without the protocol behind them.
