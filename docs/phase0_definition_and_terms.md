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
being **J2A-MC-GZGM / NCT05469126**, the clarithromycin + LY3502970 DDI study). These SoAs
are not exotic science — they are ordinary clin-pharm PK/DDI tables — but the *cells* carry
timing structure that a naive activity×timepoint grid can't hold. Five patterns:

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
- **Procedure ordering:** *"If multiple procedures take place at the same time point, the following order should be used: ECG, vital signs, blood samples."*

None of that is representable by a tick in a cell; it is timing, repetition, conditionality
and ordering expressed as prose attached to the cell.

### 5. Parallel timelines that start before the dose

Some sampling runs as its own series **beginning the day before dosing** and continuing
across it — coproporphyrin sampled `0, 0.5, 1, 2, 4, 6, 8, 12, 16 hr` on Day -1, then
`P (24 hr)` on Day 1. Combined with the pre-dose urine bins (#1), the SoA has a **second
timeline alongside the main dose-anchored one, whose zero is not the dose** and which spans
the dosing moment. (This is the pre-dose-start angle of the already-known continuous /
parallel-monitoring case — see `lessons_learned.md`.)

### Why these are the target

Each is a demand on how the SoA *model* stores timing, not on the science. They are exactly
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
whose SoAs raise the issues above.

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

### Excluded (to keep searches clean)

Psychedelic "microdosing" (recreational); and — as a *study-type* boundary only —
therapeutic-dose mass-balance / ADME and oncology window-of-opportunity studies. Note the
project no longer excludes conventional clin-pharm DDI/PK: those are precisely where the SoA
representation issues show up.

### Two layers: corpus vs. project

- **Corpus (`protocol_corpus`)** — general purpose; any study with a real posted protocol
  PDF sourced only from ClinicalTrials.gov. No phase filter.
- **This project (`protocol_phase_0`)** — selects the early-phase subset used for the
  analysis. The chosen/rejected list is `docs/project_protocols.md`.

---
*Sources: `sources/EMP Study.docx` (notes + SoA screenshots, incl. NCT05469126 / J2A-MC-GZGM); ICH M3(R2); FDA Exploratory IND Guidance 2006; EMA M3(R2); Phase-0 Microdosing Network. SoA-shape and USDM-tracing findings: `docs/lessons_learned.md`.*
