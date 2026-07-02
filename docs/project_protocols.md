# Project Corpus

The protocols we used for the analysis. Two lists: chosen and rejected. If a protocol
isn't here, it wasn't considered. Sponsor/indication from `protocol_corpus/registry.yaml`;
descriptors from the read (see `lessons_learned.md` for the SoA-shape findings).

## Chosen

| NCT | Sponsor | Indication | What it is | SoA form | Timing anchor |
|---|---|---|---|---|---|
| NCT05469126 | Eli Lilly (Loxo) | Healthy | J2A-MC-GZGM — clarithromycin + LY3502970 DDI (the EMP "Example 2" screenshots) | grid | dose-relative |
| NCT05176314 | Eli Lilly (Loxo) | Healthy | pirtobrutinib + rosuvastatin DDI | grid | dose-relative |
| NCT06085482 | Eli Lilly | Healthy | LY3502970 Phase 1 | grid | dose-relative |
| NCT05444556 | Eli Lilly | Healthy | imlunestrant, female healthy participants (crossover) | grid | dose-relative |
| NCT02901925 | Dartmouth-Hitchcock | Glioma | ABY-029 fluorescent microdose imaging | none extracted | dose/scan |
| NCT01532024 | University of Edinburgh | Acute Lung Injury | NAP microdose | none extracted | dose/scan |
| NCT04128683 | University of California, San Diego | Anorexia Nervosa | dopamine pharmacological-challenge fMRI (amisulpride/bromocriptine, drug 3h pre-scan), crossover n=31 | grid | dose/scan |
| NCT05725005 | Asceneuron | Healthy | ASN51 PET target occupancy, n=12 | grid | dose/scan |
| NCT03019289 | Prilenia | Healthy / Huntington | pridopidine sigma-1/D2 receptor occupancy, n=23 | grid | dose/scan |
| NCT03861000 | NIMH | Depression | novel PDE4D PET radioligand eval, n=3 — no SoA grid (visits only) | none | visits |
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
| NCT04057807 | Yale University | Alzheimer | PBR28 + LPS challenge PET | narrative + visits | challenge |
| NCT04204993 | Imperial College London | Influenza A H3N2 | human influenza challenge, n=20 | narrative + grid | challenge (days) |
| NCT04234672 | Neurocrine Biosciences | Healthy | [14C]TAK-831 ABA + mass-balance, n=6 | grid + PK lists | dose |
| NCT03907540 | Kadmon | Autoimmune | [14C]-KD025 ABA + mass-balance, n=5 | grid + PK lists | dose |
| NCT04965389 | Bristol-Myers Squibb | Healthy | milvexian microtracer + food-effect, n=17 | grid (2) | dose |

## Rejected

| NCT | Sponsor | Indication | What it is | Why rejected |
|---|---|---|---|---|
| NCT03958630 | NIMH | Dementia | TSPO radioligand PET, n=13 | multi-year longitudinal diagnostic structure, not the single-day shape; kept in corpus, out of the analysis |
| NCT04805983 | Yale University | — | BMS-984923 safety/PK + receptor occupancy, n=36 | conventional dose-escalation (SAD-like); dropped before onboarding, not in the corpus |
