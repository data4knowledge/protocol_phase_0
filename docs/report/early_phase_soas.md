---
title: Early Phase SoAs — Representation Issues for USDM
kicker: protocol_phase_0 · report
footer: Early Phase SoAs · draft
---

# Early Phase SoAs — Representation Issues for USDM

## Summary

Early-phase / experimental-medicine studies — short, small-population, intensively-sampled,
dosing-anchored trials — produce Schedules of Activities (SoAs) whose *cells* carry timing
structure that a plain activity×timepoint grid cannot hold. This report catalogues those
concrete representation issues and asks, for each, whether the CDISC Unified Study
Definitions Model (USDM) can carry it.

It is a companion to the general [SoA and Footnote Patterns report](../../../protocol_soa_patterns/docs/reports/soa_patterns.html),
which catalogued twelve SoA patterns and twenty-one footnote categories across 169 protocols
and showed USDM carries them all. That scan is **thin on exactly this population**, so this
report works the delta: the cell-level demands these early-phase tables make, evidenced by a
set of real protocols and, most directly, by the SoA screenshots in `sources/EMP Study.docx`.

The report has three parts: Part 1 fixes the study type and terminology (see the companion
note `docs/phase0_definition_and_terms.md`); Part 2 is the protocol set; Part 3 is the
issue-by-issue characterisation and USDM assessment.

> **Status: draft.** The five issues are characterised and grounded (Part 3). The USDM verdicts
> are marked either **traced** (settled against DDF-RA in prior work, cited) or **open**
> (needs a DDF-RA trace — the current next step). No USDM capability is asserted without a trace.

## Part 1 · What these studies are

A **Phase 0 / exploratory study** gives a sub-therapeutic exposure under a reduced preclinical
package to gather early PK, PD, mechanistic or imaging data — not safety/efficacy, not
therapeutic benefit. In practice the set used here is broader: **early-phase experimental
medicine**, which includes conventional Phase 1 clin-pharm PK/DDI studies. Those turn out to
be where the SoA representation issues are sharpest.

ClinicalTrials.gov has no "Phase 0" value — these register as **Early Phase 1**, and much
pharma early-phase work is simply labelled Phase 1. Full definition, thresholds and
terminology: `docs/phase0_definition_and_terms.md`.

## Part 2 · The protocol set

The corpus for the analysis is **26 protocols** sourced from ClinicalTrials.gov (real posted
protocol documents only). The full chosen/rejected list, with sponsor, indication, SoA form
and timing anchor, is `docs/project_protocols.md`. In shape it splits into:

- **Clin-pharm PK / DDI (Eli Lilly / Loxo)** — the four EMP protocols below; conventional
  crossover PK and drug-drug-interaction designs whose SoAs carry the cell-level structure
  this report is about.
- **PET receptor-occupancy / radioligand-tracer** studies (e.g. Asceneuron, Pfizer, Takeda,
  Genentech, GSK) — dose/scan-anchored, some microdose tracer.
- **Pharmacological- and infection-challenge** studies (LPS, endotoxin, alcohol, amphetamine,
  influenza) — assessments timed relative to a challenge administration.
- **Imaging microdose** studies (fluorescence / optical probes).

The four EMP protocols are the primary evidence set (from `sources/protocols.docx`), all Eli
Lilly / Loxo Phase 1 healthy-volunteer PK/DDI:

| NCT | Study | What it is |
|---|---|---|
| NCT05469126 | J2A-MC-GZGM | clarithromycin + LY3502970 DDI — **the source of the SoA screenshots** ("Example 2") |
| NCT05176314 | — | pirtobrutinib + rosuvastatin DDI |
| NCT06085482 | — | LY3502970 Phase 1 |
| NCT05444556 | — | imlunestrant, female healthy participants (crossover) |

## Part 3 · SoA representation issues and USDM impact

Each issue below is grounded in the GZGM (NCT05469126) SoA and the other EMP screenshots.
"USDM status" is **traced** (settled, cited) or **open** (needs a DDF-RA trace).

### Issue 1 — Interval / duration activities that cross day boundaries

**What the SoA shows.** A 24-hour urine collection recorded in 8-hour bins (4-hour in some
studies), the bins running across the study-day columns and merged to show it:

> `-24 to -16h, -16 to -8h, -8 to 0h, 0 to 8h, 8 to 16h, 16 to 24h` … `48 to 56h, 56 to 64h, 64 to 72h`

**What it demands.** Each bin is an activity with an explicit **start and end** — a duration,
not a point. A single logical activity spans several day columns, and the interval can
**begin before dosing** (`-24 to -16h`).

**USDM status: OPEN.** USDM timing is expressed primarily as point references (a Timing
relative to a reference event, with a window tolerance). Whether a collection *interval*
(start→end as the activity's own extent, distinct from a ± scheduling window) has a first-class
representation — or must be modelled as two bounding timings, or an activity duration — needs
tracing against the DDF-RA API and CORE rules. *This is the most likely genuine delta; do not
assert until traced.*

### Issue 2 — Dose-relative timing in extended-hour notation

**What the SoA shows.** PK sampling timed in running hours relative to the dose, past 24:

> `P, 0.5, 1, 2, 4, 6, 8, 12, 16` then `24 (D2), 36 (D2), 48 (D3) … 120 (D26), 168 (D28), 240 (D31)` — *"Times are relative to LY dosing"*

Dave's note asks the tool to accept `24:00 hr, 36:00 hr, 48:00 hr …` — hours that keep
counting rather than resetting to a day+clock.

**What it demands.** The primary coordinate is the **elapsed time from dosing**; the "(D2)…
(D31)" is the calendar day the offset happens to land on — a rendering, not the stored value.

**USDM status: traced — handled.** A discrete action timed off dosing is a scheduled activity
instance with a relative timing offset (see `lessons_learned.md`). The offset is an ISO 8601
duration (`PT24H`, `PT240H`), so extended hours are just a larger duration; day-in-parentheses
is a display convention over the same stored offset. The open part is presentational (can the
authoring tool *enter/show* `240:00 hr`), not a model gap.

### Issue 3 — "P": a predose anchor in individual cells

**What the SoA shows.** A literal `P` inside cells, per procedure, per period — `P` for the
Day-1 Medical Assessment and ECG, `P, 0.5, 1, 2 …` heading a PK series, `P (24 hr)` for a
coproporphyrin draw — re-anchoring in Period 2 of the crossover.

**What it demands.** A reusable relative anchor meaning "immediately before the dose in *this*
period", resolving to the correct dose administration in each period.

**USDM status: traced — handled (one point to confirm).** "Predose" is a Timing of type
*Before* relative to the dose administration; relative-timing anchors are the settled case.
The one thing worth confirming in the trace: in a multi-period crossover, that each period's
`P` references that period's dose-administration instance rather than a single global anchor.

### Issue 4 — Footnote-encoded scheduling semantics

**What the SoA shows.** Dave's note: *"Heavy usage of footnotes."* The cell shows only `Xᵇ`
or `Xᶜ`; the rule is in the footnote:

- **Windows** — *"within ± 1.5 hours of the scheduled time."*
- **Triplicate + borrowed timing** — *"measured in triplicate at predose and 12h, 24h, 48h, 72h and 96h to match PK collection timing"* (cell shows `Xᶜ`).
- **Conditional repeats** — injection-site assessment *"repeated daily until resolution"*; *"Failure to administer … will not result in a protocol deviation."*
- **Ordering** — *"If multiple procedures take place at the same time point, the order should be: ECG, vital signs, blood samples."*

**What it demands.** Timing, repetition count, conditionality and ordering — carried as prose,
not as a cell mark.

**USDM status: mixed.**

- *Windows* — **traced/handled**: timing-window tolerance is an existing primitive.
- *Triplicate / repeat counts* — **open**: whether a repeat count attaches to one activity or
  expands to N instances needs tracing.
- *Conditional repeats ("until resolution")* — **open**: needs decision/condition + exit-condition
  logic; trace required.
- *Co-timed ordering* — **open**: ordering *among activities sharing a timepoint* is subtler than
  the per-instance timeline ordering already known; trace required.

### Issue 5 — Parallel timelines that start before the dose

**What the SoA shows.** A sampling series running as its own timeline, beginning the day before
dosing and continuing across it — coproporphyrin `0, 0.5, 1, 2, 4, 6, 8, 12, 16 hr` on Day -1,
then `P (24 hr)` on Day 1 — plus the pre-dose urine bins from Issue 1.

**What it demands.** A **second timeline alongside** the main dose-anchored one, whose zero is
not the dose and which spans the dosing moment.

**USDM status: traced — likely handled (confirm).** Parallel / continuous monitoring is the
settled cyclic-sub-timeline-with-exit case (`lessons_learned.md`); a sub-timeline can anchor on
any reference event, so a pre-dose-anchored series that spans the dose should follow the same
shape. The new angle to confirm in the trace is only that the anchor precedes the main
timeline's anchor — probably fine, not asserted.

### Where this leaves USDM

Of the five, **two map onto already-traced relative-timing primitives** (Issues 2 and 3) and
**one onto the known sub-timeline pattern** (Issue 5). The genuine open questions — the
candidate deltas — are **Issue 1 (interval/duration activities with explicit start→end spanning
columns)** and **parts of Issue 4 (repeat counts, conditional "until resolution" repeats,
co-timed ordering)**. These are the items to trace against DDF-RA (API + CT + CORE rules) before
any verdict. This reopens, on firmer ground, the earlier "no USDM delta" conclusion, which was
reached on a narrower framing (challenge anchor + narrative round-trip only).

## References

- Companion report: `protocol_soa_patterns/docs/reports/soa_patterns.html` — SoA and Footnote Patterns.
- Study type, definition, terminology and the issue catalogue: `docs/phase0_definition_and_terms.md`.
- Protocol set (chosen / rejected): `docs/project_protocols.md`.
- Evidence: `sources/EMP Study.docx` (notes + SoA screenshots, incl. NCT05469126 / J2A-MC-GZGM).
- Prior USDM tracing and SoA-shape findings: `docs/lessons_learned.md`.
- ICH M3(R2); FDA Exploratory IND Guidance (2006); EMA M3(R2).
