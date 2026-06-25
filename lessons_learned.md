# Lessons Learned — Protocol Phase 0

Decisions and knowledge we don't want to lose. Append on new decisions/facts; remove only if wrong.

## Project scope & architecture

- **Project purpose (locked 2026-06-25):** characterise one under-represented trial type — single-day "experimental medicine" / Phase 0 studies — and find the specific issues their SoAs raise for USDM, vs the existing 12-pattern atlas. The general SoA→USDM mapping is already done elsewhere; this project only finds the **Phase-0 delta**.
- **Two layers, kept separate:** `protocol_corpus` is general purpose — any study with a posted protocol PDF, **sourced only from ClinicalTrials.gov**, no Phase 0 filter. This project (`protocol_phase_0`) pulls a Phase 0 subset by our definition.
- **The real target is SoA shape, not drug chemistry.** Microdose/PK is a well-defined subset, not the boundary. The archetype (from Dave): "Phase 0 / early phase / experimental medicine", often single-day, small population, many such trials run.

## USDM / SoA facts (Dave is the authority — trace before asserting)

- **Discrete point-in-time actions** (1h, 2h… off dosing): USDM handles cleanly — scheduled activity instance with a relative timing offset.
- **Parallel / continuous monitoring** ("measure X every N min", continuous ECG; shown as merged horizontal cells + footnote): USDM **handles this** — a separate timeline that cycles the activity with an **exit condition on elapsed time** (one timeline reference, not exploded instances). *Do NOT call this a gap — I did, and was wrong.*
- **The traditional "visit" largely doesn't apply** — single encounter / continuous stay, axis is time-relative-to-dosing, not visit days. Whether USDM absorbs this cleanly (Encounter-modality / main-timeline primitives) is the open job-3 question.
- **Prior art — `protocol_soa_patterns/docs/reports/soa_patterns.html`:** 12 SoA patterns + 21 footnote categories over 169 protocols / 1,759 footnotes, mapped to 11 USDM primitives. Thesis: USDM carries all patterns; only 2 soft enhancement candidates (`state_preparation`, `activity_variant`). The "dense PK sampling" pattern (`pk_profile`, 68%) = dose-anchored sub-timeline. This scan is **thin on single-day experimental-medicine protocols** — that gap is this project.
- **Behaviour rule:** never assert USDM/standards mechanics as fact without tracing the model or flagging it as a guess. Dave will catch it.

## Regulatory / definition facts

- **Microdose** = below all of: ≤100 µg total (≤500 µg / ≤5 doses repeat), ≤1/100 NOAEL, ≤1/100 PAD; ≤30 nmol for biologics.
- **ICH M3(R2):** 5 exploratory-trial approaches (1–2 microdose, 3–5 non-microdose sub-therapeutic). **FDA Exploratory IND (eIND)** guidance 2006 created the US "Phase 0" route. EMA aligns with ICH.
- **ClinicalTrials.gov has no Phase 0 value** — these register as **Early Phase 1**.
- **Exclude** (keep searches clean): conventional Phase 1 SAD/MAD; oncology window-of-opportunity (Phase 0 label but often not sub-therapeutic); psychedelic "microdosing"; therapeutic-dose mass-balance/ADME.

## CTG search recipe (the good one)

Find Phase 0 / microdose studies with a real protocol PDF:
```
https://clinicaltrials.gov/api/v2/studies?query.term=microdose%20OR%20microdosing%20OR%20%22sub-therapeutic%22&aggFilters=phase:0,docs:prot&countTotal=true&pageSize=60
```
- `docs:prot` is **noisy** — it flags studies that merely *declare* a protocol in the IPD statement. Always confirm an actual PDF via per-study `DocumentSection.largeDocumentModule.largeDocs` (field name case-sensitive: `DocumentSection` works; `LargeDocumentModule` alone returns empty).
- CDN download: `https://cdn.clinicaltrials.gov/large-docs/<last2 of NCT>/<NCT>/<filename>`.
- ~463 Early Phase 1 with a protocol doc overall. **CORRECTION (2026-06-25):** real PDFs are NOT rare — nearly all docs:prot studies carry a real `hasProtocol:true` largeDocs PDF. Only the *microdose-titled* subset was thin (2). The scarce thing is the **archetype**, not the PDF.
- **`phase:0` is a junk filter** for the archetype — "Early Phase 1" is a CTG grab-bag (453-pt RCTs, vaccines, herbal medicine). Drop it. Search by `query.term` for the archetype signature + `aggFilters=docs:prot,healthy:y`.
- **Working discriminator for the broad archetype:** PET "receptor occupancy" / radioligand evaluation / "pharmacological challenge" (fMRI/biomarker), healthy or small-n. The generic "single dose" + "pharmacodynamic" set (~134) is mostly conventional SAD/MAD → exclude.
- **PDF verification:** `filter.ids=` gets stripped by the fetch redirect — use the single-study endpoint `…/api/v2/studies/NCT?fields=NCTId,DesignModule,DocumentSection`. Bulk list pages cap around pageSize≈25 in this fetch tool (larger returns empty).

## Operational

- Canonical store: `protocol_corpus` — data in `protocols/<NCT>/source/` (PDF + ctgov.json), `registry.yaml`, pipeline scripts in `scripts/`. Run fetch/sync/build_ground_truth from there, not from this repo.
- `build_ground_truth.py` is AI-backed (needs ANTHROPIC_API_KEY in `protocol_corpus/.development_env`) — run from terminal/VSCode, **not in Cowork**.
- Cowork gotcha: `sync_registry.py --mode scan` / full `--mode enrich` time out at the 45s bash limit (touch all ~235 entries). Use `--only NCT…`. Sandbox deps: `pip install --break-system-packages requests ruamel.yaml pyyaml pymupdf`.
- Report build needs `pip install markdown`.

## Protocols in hand

- **NCT02901925** — ABY-029, fluorescence-guided microdose, recurrent glioma (Dartmouth-Hitchcock, n=14).
- **NCT01532024** — NAP, optical/neutrophil-activation imaging probe, acute lung injury (Univ. Edinburgh, n=15).
- Both are **imaging** microdose studies, not classic AMS/PK. Ground truth not yet generated (see next_steps / run outside Cowork).
