# Protocol Phase 0 — Project Guide

Mount `/Users/daveih/Documents/github/protocol_phase_0` first (project rule). Canonical protocol data (PDFs, ctgov.json, registry) lives in the sibling repo `../protocol_corpus`; the SoA-pattern prior art lives in `../protocol_soa_patterns`. Mount those when a task touches them.

## What this project is

Take one under-represented family of trials — **early-phase experimental medicine**: clin-pharm PK/DDI, PET occupancy, challenge studies, and (since 2026-09-21) **SAD / MAD dose escalation** — find enough real examples from ClinicalTrials.gov (posted protocol PDFs only), and identify the specific issues their Schedules of Activities raise for USDM, relative to the existing 12-pattern atlas in `protocol_soa_patterns`.

**The destination, the scope boundary and what counts as done are in `docs/aims.md`. Read it first.**

## Session protocol — run every session, on any machine

Project state is kept in five committed files **under `docs/`** so it travels with the repo:

- **`docs/aims.md`** — where the project is going: the destination, what is in and out of scope, what counts as done, the standing boundaries. **Rate of change: yearly. Nothing dated belongs in it.** Change it only when the destination changes.
- **`docs/next_steps.md`** — the current plan. The single source of truth for "what now". **Rewritten whole, never appended to** — stacking plans is what made it unreadable by 2026-07.
- **`docs/lessons_learned.md`** — decisions and knowledge we don't want to lose. Append when a decision is made or a fact is established; annotate a reversed decision in place rather than deleting it. Only remove an entry if it turns out wrong.
- **`docs/phase0_definition_and_terms.md`** — what these studies are, the terminology, and the six SoA representation issues the project exists to answer. Background plus the issue inventory; changes when an issue is added, killed or promoted.
- **`docs/project_protocols.md`** — the project corpus: the definitive list of protocols used for the analysis — chosen, candidates, rejected. Changes rarely. Add any new protocol here when it's brought into the project.

**At session start:** read this file plus all five state files before assuming anything.
**At session end:** update whichever of them changed.

`docs/status.md` (the dated action log) was **deleted 2026-09-21** — the log restated what the other files already carried, and drifted from them. History is in git.

`memory.md` is a redirect to these files, kept so the generic "read the project's memory.md" convention still lands here.

## Standing rules

- **No USDM claim without a trace.** Trace it against DDF-RA and quote the class or rule id, or mark it a guess in the text. See `docs/aims.md` § Standing boundaries.
- **Read the protocol, not the summary table.** The descriptor tables in `docs/project_protocols.md` are a reading aid, not evidence.
- **This project never writes to `protocol_corpus`.** Corpus defects become rows in `protocol_corpus/docs/issues.md`, not local fixes. What changed there since 2026-07 is recorded in `docs/lessons_learned.md`.
- **Analyse, suggest, ask.** No change without approval. Never run git write operations.

## Tooling

Executable code lives in `scripts/`, as in the sibling repos. Documentation of what a
script does lives in its module docstring — read the top of the file before running it.

- **`scripts/search.py`** — **the candidate finder.** Queries ClinicalTrials.gov API v2
  with a keyword scope plus `aggFilters=phase:N,funderType:...,docs:prot`, pages the whole
  result set via `nextPageToken`, recomputes "has a real protocol PDF" per study from
  `documentSection.largeDocumentModule.largeDocs` (the `docs:prot` filter alone is noisy),
  and writes a CSV. `python3 scripts/search.py [condition]`. Needs `requests`.
  **Change `DEFAULT_KEYWORDS` for a new hunt rather than writing a second script**, and
  quote multi-word phrases or the result set explodes. Its docstring carries the full
  rationale for each filter; `docs/lessons_learned.md` § *CTG search recipe* has the
  API gotchas.

**This repo finds protocols; it does not onboard them.** PDF, `ctgov.json`, registry entry
and ground truth are all `protocol_corpus/scripts/corpus.py`. Nothing here writes to the
corpus.

- **`report_theme/build.py`** — builds the report (see below).

## Report

Single living deliverable: `docs/report/early_phase_soas.md` (hand-edit) → build with
`python3 report_theme/build.py docs/report/early_phase_soas.md` → self-contained themed `early_phase_soas.html`.
Needs `pip install markdown`. One source file, one build call (not the soa_patterns multi-file assembler).
