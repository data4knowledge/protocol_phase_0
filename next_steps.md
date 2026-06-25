# Next Steps — Protocol Phase 0

The current plan. Single source of truth for "what now". Newest plan on top; rewrite as priorities change.

## Now

**Job 2 — find more protocols (the point of the project).**
Search ClinicalTrials.gov for single-day "experimental medicine" / Phase 0 studies that have a **real posted protocol PDF**. Add them to `protocol_corpus`, then select the matching subset into this project. Use the CTG recipe in `lessons_learned.md`.

- "Phase 0 / exploratory IND / microdose" registers as **Early Phase 1** (`aggFilters=phase:0`).
- Confirm an actual PDF via per-study `DocumentSection.largeDocumentModule.largeDocs` — the `docs:prot` aggFilter is noisy.
- Triage on the documents: dose is sub-therapeutic / no therapeutic intent; design is short / single-day; small population.

**Job 3 — characterise the SoAs + USDM delta.**
For the protocols found, characterise the SoA and test the one open question: do single-day / no-conventional-visit studies add or stress any pattern **beyond** the 12-pattern atlas — especially the collapse of the visit/Encounter axis (everything timed relative to dosing). Do **not** rebuild the general atlas; only the Phase-0 delta.

**Fill the report.** Populate Parts 2 (protocol set) and 3 (SoA characterisation + USDM impact) of `docs/report/phase0_soa.md`, rebuild the HTML.

## Open decisions to resolve

- **Scope when the set is in hand:** narrow (classic AMS/PK microdosing) vs broad (any sub-therapeutic exploratory, keeps the two imaging protocols). Dave leans toward the single-day experimental-medicine archetype regardless of readout. Settle against the real candidates.
- **"EMP" meaning** — unconfirmed (best guess Experimental Medicine Protocol). Watch for it appearing verbatim in protocol PDFs.
