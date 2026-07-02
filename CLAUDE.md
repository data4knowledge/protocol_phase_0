# Protocol Phase 0 — Project Guide

Mount `/Users/daveih/Documents/github/protocol_phase_0` first (project rule). Canonical protocol data (PDFs, ctgov.json, registry) lives in the sibling repo `../protocol_corpus`; the SoA-pattern prior art lives in `../protocol_soa_patterns`. Mount those when a task touches them.

## What this project is

Take one under-represented trial type — **single-day "experimental medicine" / Phase 0 studies** — find enough real examples from ClinicalTrials.gov (posted protocol PDFs only), and identify the specific issues their Schedules of Activities raise for USDM, relative to the existing 12-pattern atlas in `protocol_soa_patterns`.

## Session protocol — run every session, on any machine

Project state is kept in three committed files so it travels with the repo:

- **`status.md`** — log of actions undertaken (newest first). Append a dated entry at the **end** of any session that changed state.
- **`next_steps.md`** — the current plan / what to do next. Keep it the single source of truth for "what now"; rewrite it as priorities change.
- **`lessons_learned.md`** — decisions and knowledge we don't want to lose. Append when a decision is made or a fact is established; only remove an entry if it turns out wrong.
- **`project_protocols.md`** — the project corpus: the single definitive list of protocols used for the analysis, split into chosen and rejected. Add any new protocol here when it's brought into the project.

**At session start:** read this file plus all three state files before assuming anything.
**At session end:** update the three files before finishing.

`memory.md` is a redirect to these files, kept so the generic "read the project's memory.md" convention still lands here.

## Report

Single living deliverable: `docs/report/early_phase_soas.md` (hand-edit) → build with
`python3 report_theme/build.py docs/report/early_phase_soas.md` → self-contained themed `early_phase_soas.html`.
Needs `pip install markdown`. One source file, one build call (not the soa_patterns multi-file assembler).
