---
title: Single-Day Experimental Medicine Studies — SoA Patterns and USDM Impact
kicker: protocol_phase_0 · report
footer: Phase 0 Experimental Medicine SoA · draft
---

# Single-Day Experimental Medicine Studies — SoA Patterns and USDM Impact

## Summary

This report examines one specific, under-represented type of clinical trial — the **single-day "experimental medicine" / Phase 0 study** — and asks what its Schedule of Activities (SoA) requires of the CDISC Unified Study Definitions Model (USDM).

It is a companion to the general [SoA and Footnote Patterns report](../../../protocol_soa_patterns/docs/reports/soa_patterns.html), which catalogued twelve SoA patterns and twenty-one footnote categories across 169 protocols and showed USDM carries them all. That scan is **thin on exactly this population**: short, intensive, dosing-anchored studies with little or no conventional visit structure. This report fills that gap — it characterises the SoAs of these studies and identifies any issue they raise for USDM **beyond** the existing pattern atlas.

The report is in three parts:

- **Part 1** defines the study type and fixes the terminology.
- **Part 2** presents the protocol set assembled for the analysis (sourced from ClinicalTrials.gov, real posted protocol documents only).
- **Part 3** characterises the SoAs and assesses the specific USDM impact.

> **Status: draft / in progress.** Part 1 is complete. Parts 2 and 3 are placeholders pending the protocol search (job 2) and SoA characterisation (job 3).

## Part 1 · What these studies are

### 1.1 Definition

A **Phase 0 / exploratory study** is a first-in-human trial that gives a *sub-therapeutic* exposure of a drug under a reduced preclinical package, purely to gather early PK, PD, mechanistic or imaging data — not to assess safety/tolerability or efficacy, and not intended to produce therapeutic benefit. The defining feature is the dose: low enough that risk is negligible, so the study sits *before* a conventional Phase 1.

The specific type of interest here is narrower than "Phase 0" in general. It is the **single-day experimental medicine** study: short (often a single day), small population, dosing-anchored schedule, and little or no conventional visit structure. This population is under-represented in existing protocol collections, which is why it warrants its own treatment.

The tightest well-defined sub-class is the **microdose study**: a dose below all of ≤ 100 µg total, ≤ 1/100th of the NOAEL, and ≤ 1/100th of the pharmacologically active dose (≤ 30 nmol for protein/biologic products). ICH M3(R2) sets out five example exploratory-trial approaches; the FDA Exploratory IND guidance (2006) created the "Phase 0" route in the US; EMA aligns with ICH.

A practical note that matters for searching: **ClinicalTrials.gov has no "Phase 0" value** — these register as **"Early Phase 1"**.

### 1.2 Terminology

The terms seen for this class of protocol, grouped by what they denote:

| Group | Terms |
|---|---|
| Umbrella / regulatory | Phase 0; exploratory clinical trial (ICH M3(R2)); exploratory IND / eIND (FDA); Early Phase 1 (ct.gov label); experimental medicine; first-in-human exploratory |
| Dose class | microdose / microdosing; sub-therapeutic; sub-pharmacological / sub-clinical; tracer dose |
| Methodology / readout | microtracer (¹⁴C); AMS (accelerator mass spectrometry); PET microdosing; LC-MS/MS bioanalysis; optical / fluorescence imaging microdose; radiolabelled microdose / dosimetry |
| Design variant | cassette / cocktail microdosing; Intra-Target Microdosing (ITM); microtracer absolute bioavailability; adaptive Phase 0/1 |

"EMP" — a term used informally for these studies — is **unconfirmed**; the field is "Experimental Medicine (EM)", so the best guess is "Experimental Medicine Protocol", but this is not verified.

**Excluded** (named to keep the search clean): conventional Phase 1 SAD/MAD; oncology "window-of-opportunity" studies that carry the Phase 0 label but are not sub-therapeutic; psychedelic "microdosing"; therapeutic-dose mass-balance / ADME.

## Part 2 · The protocol set

> *Placeholder — to be populated by the ClinicalTrials.gov search (job 2).*

Inclusion rule: registered as Early Phase 1 (or explicitly exploratory IND / Phase 0), sub-therapeutic with no therapeutic intent, single-day / short intensive design, **and a real protocol PDF posted on ClinicalTrials.gov**. The posted-PDF requirement is the binding constraint — most studies of this type never post one.

Currently in the corpus: NCT02901925 (ABY-029, fluorescence-guided microdose, recurrent glioma) and NCT01532024 (NAP, optical imaging probe, acute lung injury). Both are imaging microdose studies rather than classic AMS/PK microdosing.

## Part 3 · SoA characterisation and USDM impact

> *Placeholder — to be populated by the SoA characterisation (job 3).*

The baseline is the twelve-pattern atlas from the companion report, which USDM already covers (only two soft enhancement candidates: `state_preparation` and `activity_variant`). The relevant primitives for this study type are likely:

- **`pk_profile` (dense PK sampling, 68% in the general scan)** — hour/minute-resolution sampling around a dosing event, represented in USDM as a sub-timeline anchored on the dose.
- **Asynchronous timelines** and **cycles-as-decision-loop** — these represent periodic / continuous monitoring ("measure X every N minutes", continuous telemetry) as a separate timeline that cycles the activity with an exit condition on elapsed time. Not a gap.

The open question this report answers: do single-day / no-conventional-visit experimental medicine protocols introduce or stress any pattern **beyond** these twelve — in particular, is the collapse of the visit/Encounter axis (everything timed relative to dosing, within one encounter or a continuous stay) absorbed cleanly by USDM's Encounter-modality and main-timeline primitives, or does it expose a specific requirement?

## References

- Companion report: `protocol_soa_patterns/docs/reports/soa_patterns.html` — SoA and Footnote Patterns.
- Working definition and full terminology: `docs/phase0_definition_and_terms.md`.
- ICH M3(R2); FDA Exploratory IND Guidance (2006); EMA M3(R2); Phase-0 Microdosing Network.
