# Phase 0 / Microdose Protocols — Definition & Terminology

Job 1 of the Phase 0 corpus work. Purpose: pin down what we mean by "these protocols" so the CTG search (job 2) and SoA characterisation (job 3) hunt for the right thing.

## Project purpose (locked 2026-06-25)

Take **one specific, under-represented trial type — single-day "experimental medicine" / Phase 0 studies** — find enough real examples (the general corpus and the `protocol_soa_patterns` 169-protocol scan are **thin on exactly this population**), and identify the **specific issues their SoAs raise for USDM**, relative to the existing 12-pattern atlas. Job 2 (pull more from ct.gov) is needed precisely because these are under-represented today.

## What we're actually after (the real spec)

The driving interest is **assessing impact on the USDM Schedule of Activities (SoA)** — what this class of protocol *requires* of the SoA model. So the operative definition is about **SoA shape**, not drug chemistry. The microdose/PK material below is a useful subset, not the boundary.

The target archetype, **as actually described by Dave** (spec is deliberately loose):

- **"Phase 0" / "early phase" / "experimental medicine"** studies.
- Often run on a **single day** (or very short).
- **Small population.**
- **"Lot of studies done"** — i.e. many such trials are run.
- Referred to as **"EMP"** — meaning unconfirmed. Best guess "Experimental Medicine Protocol" (the field is "Experimental Medicine / EM"); could be sponsor-specific. **TO CONFIRM.**
- Aim: assess **impact on USDM SoAs** and any particular requirements.

**Hypotheses (mine, NOT Dave's spec — to test in job 3, not selection criteria):**

- These have **dense, sub-day SoAs** (many procedures, fine timing in minutes/hours, tight repeats, single encounter). This is my prior from how single-day early-phase PK studies usually look — unverified, and won't hold for all of them.
- The single-day / sub-day timing is the part most likely to stress the USDM SoA model.

Job 3 is where we confirm or kill these against real protocols.

## Prior art: protocol_soa_patterns report (READ THIS FIRST for job 3)

Reference: `protocol_soa_patterns/docs/reports/soa_patterns.html` (Dave, 2026-06-25). Much of "characterise SoAs + USDM impact" is **already done** here:

- Scan of **169 protocols with SoAs** + **1,759 footnotes** (147 protocols). Same corpus ecosystem.
- Catalogues **12 SoA patterns** and **21 footnote categories**, mapped to **11 USDM primitives**. Thesis (demonstrated): **USDM already carries every pattern.** Only **2 soft enhancement candidates** — `state_preparation` (e.g. fasting) and `activity_variant` — both workable today, neither blocking.
- Relevant to our archetype:
  - **`pk_profile` — dense PK sampling, 68%** = my "dense SoA" hypothesis, but properly measured. Hour/minute-resolution sampling round a dosing event. USDM: **sub-timeline anchored on the dose** (primitives B Sub-timeline at Activity, C Sub-timeline at SAI, G Timing windows).
  - **Asynchronous timelines (D)** + **Cycles as decision-loop (F)** = the periodic/continuous-monitoring case (DIH correction above). Confirmed handled.

**Implication for this project:** don't re-characterise the general SoA→USDM mapping — it exists. The genuine open Phase-0 question is narrower: do **single-day / no-visit "experimental medicine"** protocols introduce or stress any pattern **beyond these 12**, or is the "visit doesn't apply" case already absorbed by the Encounter-modality (H) / main-timeline (A) primitives? Job 3 = test that delta, not rebuild the atlas.

## USDM SoA characterisation targets (from Dave's domain knowledge)

These are the SoA features that matter for USDM impact — the "particular requirements" to assess in job 3. From Dave, 2026-06-25:

1. **Discrete timed actions** — point-in-time activities (1hr, 2hr, …), timed off a reference (typically dosing). *USDM read (tentative): handled cleanly — each is a scheduled activity instance with a relative timing offset.*

2. **Parallel / continuous monitoring** — an activity running *across* a span, not at a point: "measure X every N minutes", continuous ECG/telemetry, etc. In the SoA table this shows as **merged horizontal cells spanning the time columns, usually with a footnote**. *USDM representation (per Dave): a **separate timeline** that cycles the activity, with an **exit condition** firing when the elapsed time is reached. So it's one timeline reference from the main SoA, looping to a time-based exit — not exploded point instances. Continuous telemetry is the same shape with the cycle = sampling interval. USDM handles this; not a gap.*

3. **The traditional "visit" doesn't apply** — no sequence of Encounters; one encounter (or a continuous stay), everything timed relative to dosing rather than visit days. *USDM read (tentative, confirm with Dave): the Encounter axis that normally structures an SoA largely collapses; the organising axis becomes relative time, not visit.*

For job 3: characterise how each protocol's SoA actually uses these patterns, and check the USDM representations hold up against the real documents rather than asserting. Note (DIH correction, 2026-06-25): do **not** claim USDM gaps without tracing the model — the cyclic-sub-timeline-with-exit handles periodic/continuous monitoring.

## Working definition (microdose sub-class)

A **Phase 0 / exploratory study** is a first-in-human trial that gives a *sub-therapeutic* exposure of a drug under a reduced preclinical package, purely to gather early PK, PD, mechanistic or imaging data — **not** to assess safety/tolerability or efficacy, and **not** intended to produce therapeutic benefit. The defining feature is the dose: low enough that the risk is negligible, so it sits *before* a conventional Phase 1.

The tightest sub-class is the **microdose study**.

## The numbers (microdose thresholds)

A dose is a **microdose** if it is below *all* of:

- **≤ 100 µg total** (and, in the repeat version, ≤ 100 µg per administration, ≤ 5 administrations, ≤ 500 µg total), AND
- **≤ 1/100th of the NOAEL** (No Observed Adverse Effect Level), AND
- **≤ 1/100th of the pharmacologically active dose (PAD)**.
- For **protein/biologic products: ≤ 30 nmol** total.

Anything sub-therapeutic but above the microdose ceiling is a *non-microdose exploratory* study (ICH approaches 3–5 below) — still Phase 0 in spirit, not a microdose.

## Regulatory frame

**ICH M3(R2)** (effective Dec 2009) defines **5 example approaches** to exploratory clinical trials. Condensed:

1. Microdose, single dose — ≤100 µg, ≤1/100 NOAEL & PAD.
2. Microdose, repeat — ≤100 µg/day, ≤5 doses, ≤500 µg total.
3. Single sub-therapeutic → therapeutic-range dose.
4. ≤14-day repeat dose, no therapeutic-range intent, starting sub-therapeutic.
5. ≤14-day repeat dose into therapeutic range.

Approaches 1–2 are microdosing; 3–5 are larger sub-therapeutic/therapeutic exploratory designs with progressively heavier tox packages. None aim at MTD.

**FDA Exploratory IND (eIND) Guidance, 2006** — created the "Phase 0" / exploratory IND route in the US; reduced preclinical requirements in exchange for limited, sub-therapeutic, no-therapeutic-intent dosing.

**EMA** — aligned with ICH M3(R2); same microdose definition.

**ClinicalTrials.gov** — there is **no "Phase 0" value**. These register as **"Early Phase 1"** (`aggFilters=phase:0` in the API). This is the single most important search fact: confirmed in prior corpus work.

## Full term list

Terms you'll see for this protocol class, grouped by what they actually denote.

**Umbrella / regulatory labels**

- Phase 0 trial / Phase '0' study
- Exploratory clinical trial (ICH M3(R2) language)
- Exploratory IND study / eIND study (FDA)
- Early Phase 1 (ClinicalTrials.gov registry label)
- First-in-human exploratory study

**Dose-class terms**

- Microdose / microdosing study / human microdosing
- Sub-therapeutic dose study
- Sub-pharmacological / sub-clinical dose
- Tracer dose study

**Methodology / readout terms** (how the tiny signal is detected)

- Microtracer study (esp. ¹⁴C microtracer)
- AMS — Accelerator Mass Spectrometry
- PET microdosing / molecular imaging microdose (¹¹C, ¹⁸F tracers)
- LC-MS/MS ultra-sensitive bioanalysis
- Optical / fluorescence imaging microdose (e.g. the two corpus protocols)
- Radiolabelled microdose / dosimetry study

**Design variants**

- Cassette microdosing / cocktail microdosing (several compounds in one sub-therapeutic dose)
- Intra-Target Microdosing (ITM) — local microdose into ~1% of a tissue/organ to reach locally active concentrations while staying systemically a microdose
- Microtracer absolute bioavailability (AB) study — oral therapeutic dose + IV ¹⁴C microtracer
- Adaptive Phase 0 / Phase 1 (rolling design)
- Proof-of-mechanism (early) — sometimes used loosely for Phase 0

**Bodies / sources**

- Phase-0 Microdosing Network (phase-0microdosing.org)

## Related-but-distinct (exclude these)

Worth naming explicitly so the search doesn't drag them in:

- **Conventional Phase 1 / FIH SAD-MTD** — therapeutic-range, dose-escalation, safety-focused. Not Phase 0.
- **"Phase 0" in oncology window-of-opportunity sense** — pharmacodynamic studies in patients pre-surgery; *sometimes* microdose, often not. Judge by dose, not the label.
- **Psychedelic "microdosing"** — recreational/wellness use of sub-perceptual doses. Completely different thing; will pollute keyword searches for "microdose".
- **Bioequivalence / mass-balance ADME** at therapeutic dose — uses ¹⁴C but is *not* a microdose.

## Two layers: corpus vs. this project

These are separate, deliberately:

- **Corpus (`protocol_corpus`)** is general purpose. Any study is valid game if it has a **real posted protocol PDF**, sourced **only from ClinicalTrials.gov**. No Phase 0 filter applies at this layer.
- **This project (`protocol_phase_0`)** *pulls a subset* from the corpus matching our Phase 0 selection definition (below). So job 2 is two steps: (a) find ct.gov studies with protocol PDFs and add them to the corpus, then (b) select those matching our definition into this project.

### Selection definition for this project — TO CONFIRM

The candidate selection rule is **AMS PK microdosing** (or whatever definition we derive). Open question: narrow vs. broad — see the note below, this is the decision to settle before job 2.

Hard constraint regardless: protocols only come from **ClinicalTrials.gov**, and only if a **real protocol PDF is posted** (the limiting factor — most Phase 0 studies never post one).

## Note on the two protocols already in the corpus

Both are **imaging microdose** studies, not classic oral-AMS PK microdosing:

- **NCT02901925** — ABY-029, fluorescence-guided microdose in recurrent glioma.
- **NCT01532024** — NAP, optical/neutrophil-activation imaging probe in acute lung injury (an ITM-style lung study).

Decision for job 2 (project selection, not corpus): narrow to **classic AMS/PK microdosing**, or broad **any sub-therapeutic exploratory** (PK + imaging)? This matters because under a strict AMS-PK rule, **neither existing protocol qualifies** — both are imaging microdose. Trade-off: AMS-PK is the cleanest, most homogeneous class for SoA characterisation, but almost nothing PK-centric posts a protocol PDF, so the pulled set will be tiny. Broad keeps the two we have and yields more protocols, at the cost of a more heterogeneous set.

---
*Sources: ICH M3(R2); FDA Exploratory IND Guidance 2006; EMA M3(R2); TRACER CRO M3(R2) approaches summary; Burt et al., Phase 0/microdosing reviews; Phase-0 Microdosing Network.*
