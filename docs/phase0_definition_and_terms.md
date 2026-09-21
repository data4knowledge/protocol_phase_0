# Early Phase SoAs — the Issue, Definition & Terminology

What this project is now about, in one line: **the concrete Schedule-of-Activities (SoA)
representation problems that early-phase / experimental-medicine studies put on USDM** —
the complex cells, the merged cells, the sub-day dose-relative timing, the "P" predose
anchors, and the semantics buried in footnotes.

The study-type definition and terminology (microdose, Phase 0, Early Phase 1, etc.) is
still here as background, further down. But the driving question is no longer "what counts
as Phase 0" — it's "can USDM's SoA carry what these tables actually contain."

## The issue at hand

The evidence is `sources/EMP Study.docx` (Dave's notes + real SoA screenshots, the clearest
being **J2A-MC-GZGM / NCT05469126**, the clarithromycin + LY3502970 DDI study).

> **What that document is, and what it is not (clarified by Dave, 2026-09-21).**
> `EMP Study.docx` is a **scoping document** — notes plus SoA screenshots, written to frame the
> problem at the start. It is not protocol evidence and was never meant to be. The issue it was
> written to raise is **monitoring timelines that span visits and days**: a measurement series
> that runs as its own schedule across the study-day columns rather than sitting in one cell.
> That is issues 1 and 5 below, and it is the centre of the question.
>
> The practical consequence: several strings quoted below and in the report were transcribed off
> that document's *images* by an earlier session. As scoping notes that is fine. As quotations in
> a published report they carry the wrong provenance, and one of them is already inconsistent
> (see issue 2). **NCT05469126 is in `protocol_corpus` with its SoA carved — re-quote each issue
> from the protocol before the report is finished.**

These SoAs
are not exotic science — they are ordinary clin-pharm PK/DDI tables — but the *cells* carry
timing structure that a naive activity×timepoint grid can't hold. Six patterns — five
from the cell structure of clin-pharm tables, and a sixth from the cohort structure of
ascending-dose studies:

### 1. Interval / duration activities that cross day boundaries

A "24-hour urine collection" is not a point in time; it's a collection **over an interval**,
recorded in bins. In GZGM these bins are 8-hour (4-hour in some studies) and they run
straight across the study-day columns:

> `-24 to -16h, -16 to -8h, -8 to 0h, 0 to 8h, 8 to 16h, 16 to 24h` … then `48 to 56h, 56 to 64h, 64 to 72h`

Each bin is an activity with a **start and an end**, not a mark against a single timepoint.
The table merges cells across day columns to show it. Note two things: the interval can
**begin before dosing** (the `-24 to -16h` bins), and a single logical activity spans
several columns.

### 2. Dose-relative timing in extended-hour notation

PK sampling is timed in **running hours relative to the dose**, well past 24:

> `P, 0.5, 1, 2, 4, 6, 8, 12, 16` then `24 (D2), 36 (D2), 48 (D3), 72 (D4), 96 (D5)` … `120 (D26), 168 (D28), 240 (D31)` — *"Times are relative to LY dosing"*

**Unverified — the series above does not run continuously.** `96 (D5)` followed by `120 (D26)`
cannot both be measured from one dose; 120 h after a Day-1 dose is Day 6. The likeliest reading is
that this concatenates two periods of a crossover, the later hours running from a second dose
around Day 21 (120 h → D26, 168 h → D28, 240 h → D31, which is self-consistent). If so, the
transcription has merged two series and the "(Dn) is the calendar day the running hour falls on"
gloss is right per-period but wrong across the join. **Check against the PDF before quoting.**

The clock notation Dave calls out explicitly: it must accept `24:00 hr, 36:00 hr, 48:00 hr,
72:00 hr …` — i.e. hours that keep counting rather than resetting to a day+clock time. The
"(D2)"/"(D31)" in parentheses is the calendar day the running hour happens to fall on; the
**primary** coordinate is the elapsed hour from dosing, not the study day the column implies.

### 3. "P" — a predose anchor in individual cells

A literal `P` (predose) appears **inside cells**, per procedure, per period: `P` for the
Day-1 Medical Assessment and ECG, `P, 0.5, 1, 2 …` heading a PK series, `P (24 hr)` for a
coproporphyrin draw. It's a reusable relative anchor meaning "immediately before the dose in
*this* period" — and in a two-period crossover it re-anchors in Period 2. Dave's note:
*"need a 'P' for predose option for each cell."*

### 4. Footnote-encoded scheduling semantics

Dave's note: *"Heavy usage of footnotes."* The cell often carries only `Xᵇ` or `Xᶜ`; the
actual timing rule lives in the footnote. Observed in the screenshots:

- **Windows:** *"Day -1 vitals should be performed within ± 1.5 hours of the scheduled time."*
- **Triplicate + borrowed timing:** *"Supine BP and pulse rate … measured in triplicate at predose and 12h, 24h, 48h, 72h and 96h to match PK collection timing"* — the cell shows `Xᶜ`; the count and the times are in the note.
- **Conditional repeats:** injection-site assessment *"repeated daily until resolution"*, plus *"Failure to administer … will not result in a protocol deviation."*
- **Procedure ordering:** *"If multiple procedures take place at the same time point, the order should be: ECG, vital signs, blood samples."* — transcribed, not verified. The report quotes this footnote too; the two copies are identical today, and the duplication is what will let them drift again.

None of that is representable by a tick in a cell; it is timing, repetition, conditionality
and ordering expressed as prose attached to the cell.

### 5. Parallel timelines that start before the dose

Some sampling runs as its own series **beginning the day before dosing** and continuing
across it — coproporphyrin sampled `0, 0.5, 1, 2, 4, 6, 8, 12, 16 hr` on Day -1, then
`P (24 hr)` on Day 1. Combined with the pre-dose urine bins (#1), the SoA has a **second
timeline alongside the main dose-anchored one, whose zero is not the dose** and which spans
the dosing moment. (This is the pre-dose-start angle of the already-known continuous /
parallel-monitoring case — see `lessons_learned.md`.)

### 6. Dose-escalation cohorts — the same schedule, re-run per cohort

*Added 2026-09-21 when SAD and MAD studies were brought into scope (see below). This
issue is **grounded but not traced** — the USDM verdict is open.*

A Single Ascending Dose (SAD) or Multiple Ascending Dose (MAD) study prints **one** SoA
and runs it **many times**: cohort 1 at the lowest dose, cohort 2 at the next, and so on,
each cohort's schedule identical except for the dose administered and the calendar it runs
on. The table itself carries no cohort column — the cohort dimension lives in the design
narrative and in footnotes. Four things come with it:

- **The cohort axis.** The same activity×timepoint grid is instantiated per dose level.
  Whether that is one schedule parameterised by dose, or *n* schedules, is the question.
- **Sentinel dosing.** Within a cohort, a sentinel pair (typically one active, one placebo)
  is dosed first and the remainder follow only after a stated interval — a **within-cohort
  split with its own offset**, against a single printed row.
- **Escalation decision gates.** Dosing of cohort *n+1* is conditional on a safety review of
  cohort *n*, and timed relative to it ("not before N days after the last participant in the
  preceding cohort"). The gate is a condition on whether and when the next instance runs.
- **Repeat-dosing days (MAD).** Dosing runs Day 1…Day *N* with a full intensive PK profile on
  the first and last dosing days only, troughs in between, and the middle days collapsed into
  one spanning "daily" cell — issue 1's merged-cell problem, driven by repetition rather
  than by an interval.

**Evidence already in hand.** Twelve in-scope ascending-dose protocols are already onboarded in
`protocol_corpus` (listed in `docs/project_protocols.md`). Four carry a reviewer-confirmed
timeline count; **NCT04586920** (SAD + MAD, n=104) is counted at **6 timelines**, the highest
in the set. What drives that count is not yet established — it needs reading, not assuming.

**Open question, not a claim.** Does USDM carry the cohort dimension through arms / elements /
study-cell structure with one timeline, or does each dose level need its own `ScheduleTimeline`?
And where does the escalation gate live? Neither is traced. Do not state either way until it is.

### Why these are the target

Each is a demand on how the SoA *model* stores timing and repetition, not on the science. They are exactly
the cases the general 12-pattern atlas (`protocol_soa_patterns`) is thin on, because that
scan is light on short, dosing-anchored, footnote-heavy early-phase tables. Whether USDM
carries each cleanly is assessed in the report (`docs/report/early_phase_soas.md`) — traced
against DDF-RA, not asserted.

---

## Background — the study type

### Definition

A **Phase 0 / exploratory study** gives a *sub-therapeutic* exposure under a reduced
preclinical package, purely to gather early PK, PD, mechanistic or imaging data — not to
assess safety/tolerability or efficacy, and not for therapeutic benefit. In practice the
corpus for this project is broader than strict Phase 0: it is **early-phase experimental
medicine** — short, small-population, intensively-sampled, dosing-anchored studies,
including the conventional Phase 1 clin-pharm PK/DDI studies (the four Lilly/Loxo protocols)
whose SoAs raise the issues above, and — since 2026-09-21 — **first-in-human dose-escalation
studies (SAD and MAD)**.

#### SAD and MAD

- **SAD — Single Ascending Dose.** First-in-human, normally in healthy volunteers. Sequential
  cohorts each receive **one** dose, at a dose level escalated cohort by cohort, with sentinel
  dosing within the cohort and a safety review between cohorts. Intensive PK follows the single
  dose. Often carries an appended food-effect or crossover period.
- **MAD — Multiple Ascending Dose.** The same escalation structure, but each cohort receives
  **repeat** dosing over several days or weeks at its dose level. Intensive PK on the first and
  last dosing days, trough sampling between; steady-state assessment is the point.

Both were **previously excluded** from this project as "conventional Phase 1". That exclusion
is **reversed** — they are in scope, because their SoAs carry a structure the other families do
not: the cohort/dose-level axis of issue 6 above. The reversal and its reasoning are recorded in
`docs/lessons_learned.md`.

The tightest well-defined sub-class is the **microdose study**: below all of ≤ 100 µg total,
≤ 1/100th of the NOAEL, and ≤ 1/100th of the pharmacologically active dose (≤ 30 nmol for
biologics). ICH M3(R2) sets out five example exploratory-trial approaches; the FDA
Exploratory IND guidance (2006) created the US "Phase 0" route; EMA aligns with ICH.

Search fact that still matters: **ClinicalTrials.gov has no "Phase 0" value** — these
register as **Early Phase 1**, and much pharma early-phase work is labelled Phase 1.

### "EMP"

Used informally for these studies; **unconfirmed**. The field is "Experimental Medicine
(EM)", so best guess is "Experimental Medicine Protocol" — not verified.

### Terminology

| Group | Terms |
|---|---|
| Umbrella / regulatory | Phase 0; exploratory clinical trial (ICH M3(R2)); exploratory IND / eIND (FDA); Early Phase 1 (ct.gov label); experimental medicine; first-in-human exploratory |
| Dose class | microdose / microdosing; sub-therapeutic; sub-pharmacological / sub-clinical; tracer dose |
| Methodology / readout | microtracer (¹⁴C); AMS (accelerator mass spectrometry); PET microdosing; LC-MS/MS bioanalysis; optical / fluorescence imaging microdose; radiolabelled microdose / dosimetry |
| Design variant | cassette / cocktail microdosing; Intra-Target Microdosing (ITM); microtracer absolute bioavailability; adaptive Phase 0/1; DDI / clin-pharm crossover |
| Dose escalation | SAD (single ascending dose); MAD (multiple ascending dose); first-in-human (FIH); sentinel dosing; dose-escalation / safety review committee; starting dose; maximum tolerated dose (MTD); cohort |

### Excluded (to keep searches clean)

Psychedelic "microdosing" (recreational); and — as a *study-type* boundary only —
therapeutic-dose mass-balance / ADME and oncology window-of-opportunity studies.

Two former exclusions have been **reversed**, both for the same reason — the boundary is SoA
shape, not study purpose:

- **Conventional clin-pharm DDI / PK** (reversed 2026-07-02) — precisely where the cell-level
  representation issues show up.
- **SAD / MAD dose escalation** (reversed 2026-09-21) — brings the cohort/dose-level axis,
  sentinel dosing and escalation gates, none of which the other families exercise.

Oncology dose escalation stays out. It escalates in *patients* against response, and its
schedule problem is cycle-based repetition — a Phase 2/3 shape, not this one.

### Two layers: corpus vs. project

- **Corpus (`protocol_corpus`)** — general purpose; any study with a real posted protocol
  PDF sourced only from ClinicalTrials.gov. No phase filter.
- **This project (`protocol_phase_0`)** — selects the early-phase subset used for the
  analysis. The chosen/rejected list is `docs/project_protocols.md`.

---
*Sources: `sources/EMP Study.docx` (notes + SoA screenshots, incl. NCT05469126 / J2A-MC-GZGM); ICH M3(R2); FDA Exploratory IND Guidance 2006; EMA M3(R2); Phase-0 Microdosing Network. SoA-shape and USDM-tracing findings: `docs/lessons_learned.md`.*
