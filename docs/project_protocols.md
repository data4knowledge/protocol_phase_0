# Project Corpus

The protocols we used for the analysis. Two lists: chosen and rejected. If a protocol
isn't here, it wasn't considered. Sponsor/indication from `protocol_corpus/registry.yaml`;
descriptors from the read (see `lessons_learned.md` for the SoA-shape findings).

Scope boundary: `docs/aims.md`. A rejected protocol stays in `protocol_corpus`; rejection is
this project's judgement about the analysis, never a statement about the corpus.

## Chosen — 36

| NCT | Sponsor | Indication | What it is | SoA form | Timing anchor |
|---|---|---|---|---|---|
| NCT05469126 | Eli Lilly (Loxo) | Healthy | J2A-MC-GZGM — clarithromycin + LY3502970 DDI (the EMP "Example 2" screenshots) | grid | dose-relative |
| NCT05176314 | Eli Lilly (Loxo) | Healthy | pirtobrutinib + rosuvastatin DDI | grid | dose-relative |
| NCT06085482 | Eli Lilly | Healthy | LY3502970 Phase 1 | grid | dose-relative |
| NCT05444556 | Eli Lilly | Healthy | imlunestrant, female healthy participants (crossover) | grid | dose-relative |
| NCT01532024 | University of Edinburgh | Acute Lung Injury | NAP microdose | grid (reviewer: p14, 1 timeline) | dose/scan |
| NCT04128683 | University of California, San Diego | Anorexia Nervosa | dopamine pharmacological-challenge fMRI (amisulpride/bromocriptine, drug 3h pre-scan), crossover n=31 | grid | dose/scan |
| NCT05725005 | Asceneuron | Healthy | ASN51 PET target occupancy, n=12 | grid | dose/scan |
| NCT03019289 | Prilenia | Healthy / Huntington | pridopidine sigma-1/D2 receptor occupancy, n=23 | grid | dose/scan |
| NCT03511105 | GlaxoSmithKline | Healthy | GSK2798745 segmental LPS alveolar-challenge, n=47 | grid | challenge |
| NCT04202497 | Takeda | Healthy | LSD1 enzyme-occupancy PET, tracer microdose, n=7 | grid | dose/scan |
| NCT06390098 | Asceneuron | Healthy | ASN51 target-occupancy PET, n=3 | grid | dose/scan |
| NCT02551653 | GlaxoSmithKline | Pulmonary Hypertension | GSK2256098 biodistribution PET, microdose, n=10 | grid (T&E) | dose/scan |
| NCT04394845 | Genentech | Alzheimer | [18F]GTP1 biodistribution PET, n=6 | grid | dose/scan |
| NCT05128058 | Pfizer | Healthy | ritlecitinib target occupancy, n=16 | grid | dose |
| NCT03306589 | GlaxoSmithKline | Rheumatoid Arthritis | LPS / GM-CSF challenge, n=12 | grid | challenge |
| NCT04310423 | University of California, Los Angeles | Alcohol Use Disorder | endotoxin inflammatory challenge, n=76 | grid | dose/challenge |
| NCT03512171 | Vanderbilt University | Healthy Adults | fallypride + amphetamine challenge PET | narrative + scan list | dose/challenge |
| NCT04251221 | Yale University | Alcohol Drinking | PBR28 + alcohol challenge PET | narrative + scan list | challenge |
| NCT04236986 | Yale University | PTSD | PBR28 + LPS challenge PET | narrative + scan list | challenge |
| NCT04204993 | Imperial College London | Influenza A H3N2 | human influenza challenge, n=20 | narrative + grid | challenge (days) |
| NCT04234672 | Neurocrine Biosciences | Healthy | [14C]TAK-831 ABA + mass-balance, n=6 | grid + PK lists | dose |
| NCT03907540 | Kadmon | Autoimmune | [14C]-KD025 ABA + mass-balance, n=5 | grid + PK lists | dose |
| NCT04965389 | Bristol-Myers Squibb | Healthy | milvexian microtracer + food-effect, n=17 | grid (2) | dose |
| NCT05262387 | Eli Lilly | Diabetes Mellitus, Type 1 | LY900014 vs insulin lispro, exercise challenge in T1D patients, n=25 | grid (2: visits + assessment-day sub-timeline) | exercise challenge / meal |
| NCT04586920 | Eli Lilly | Healthy | **SAD + MAD + DDI + food effect, n=104** — the richest in the set | grid (6) | dose-relative / cohort |
| NCT04270370 | Eli Lilly | Healthy | SAD + MAD — LY3478045, n=72 | grid (3) | dose-relative / cohort |
| NCT04559568 | Eli Lilly | Healthy | SAD + MAD — LY3522348, n=65 | grid (2) | dose-relative / cohort |
| NCT06119529 | Eli Lilly | Healthy / Atopic Dermatitis | SAD + MAD — LY3872386, n=18 | grid (2) | dose-relative / cohort |
| NCT04178733 | Eli Lilly | Healthy | SAD — LY3493269, n=33 | grid (2) | dose-relative / cohort |
| NCT04230122 | Eli Lilly | Healthy | SAD — LY3478006, n=4 | grid (1) | dose-relative / cohort |
| NCT04411628 | Eli Lilly | COVID-19 | SAD, first-in-human, n=26 | grid (1) | dose-relative / cohort |
| NCT04498390 | Eli Lilly | Healthy | MAD — LY3493269, n=40 | grid (1) | dose-relative / cohort |
| NCT04682106 | Eli Lilly | Healthy | MAD — LY3493269 formulation, n=40 | grid (1) | dose-relative / cohort |
| NCT04604795 | GlaxoSmithKline | Celiac Disease | single + repeat dose escalation, n=65 | grid (2) | dose-relative / cohort |
| NCT04147715 | Shionogi | Healthy | SAD + food effect, n=98 | **none extracted** | dose-relative / cohort |
| NCT06181006 | Eli Lilly | Healthy | SAD — LOXO-305, n=24 | **none extracted** | dose-relative / cohort |

**Twelve of the 36 are ascending-dose (SAD / MAD), added 2026-09-21.** Already onboarded in
`protocol_corpus`, so no new ClinicalTrials.gov search was needed; four carry a
reviewer-confirmed timeline count (NCT04586920 = 6, NCT04178733 = 2, NCT04230122 = 1,
NCT04411628 = 1). They are the evidence for issue 6.

**Sponsor concentration is the standing weakness.** Ten of the twelve ascending-dose entries
are Eli Lilly, on a list that was already Lilly-heavy. Until that is fixed or stated, an
issue-6 finding reads as one sponsor's template rather than a property of the design —
`docs/next_steps.md` step 5.

---

## Rejected

| NCT | Sponsor | Indication | What it is | Why rejected |
|---|---|---|---|---|
| NCT02901925 | Dartmouth-Hitchcock | Glioma | ABY-029 fluorescent microdose imaging, n=14 | **Removed from the target set 2026-09-21 (Dave).** No SoA at all — reviewer-confirmed 0 timelines. Outside the scope boundary in `aims.md`: nothing is anchored on an intervention in sub-day units because there is no schedule to anchor. Stays in `protocol_corpus`. |
| NCT03861000 | NIMH | Depression | novel PDE4D PET radioligand eval, n=3 | **Removed from the target set 2026-09-21 (Dave).** Visits only, no SoA grid. Calendar-anchored, so outside the boundary. Its "Table 5" finding (participant time commitment is derivable, not a USDM gap) stands and is kept in `lessons_learned.md`. Stays in `protocol_corpus`. |
| NCT04057807 | Yale University | Alzheimer | PBR28 + LPS challenge PET | **Removed from the target set 2026-09-21 (Dave).** Narrative plus visits — the timing hangs off visit days, not off the challenge in sub-day units. Outside the boundary. Stays in `protocol_corpus`. |
| NCT04457778 | EMD Serono | Metastatic Solid Tumors | MAD, first-in-human, n=58 | Ascending dose in **patients** against response, cycle-based — the oncology-escalation exclusion in `aims.md`. Onboarded in the corpus; out of this analysis. |
| NCT03958630 | NIMH | Dementia | TSPO radioligand PET, n=13 | multi-year longitudinal diagnostic structure, not the single-day shape; kept in corpus, out of the analysis |
| NCT04805983 | Yale University | — | BMS-984923 safety/PK + receptor occupancy, n=36 | **REOPENED 2026-09-21.** Rejected as “SAD-like”, which is no longer a reason to reject. Never onboarded, so it is not in the corpus — onboarding is a decision, not a given. |
