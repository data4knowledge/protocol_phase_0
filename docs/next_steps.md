# Next Steps — Protocol Phase 0

The current plan. **Rewritten whole, never appended to.** If a line here is stale, replace it.
Where the project is going: `docs/aims.md`. What we decided and why: `docs/lessons_learned.md`.

*Rewritten 2026-09-21 after a two-month gap and the SAD/MAD scope expansion. The previous
version stacked four historical plans on top of each other; none is reproduced here.*

## Where this stands

Six issues are named and grounded (`docs/phase0_definition_and_terms.md`). Against the four
completion tests in `aims.md`:

| Issue | Grounded | Mapped to atlas | Traced vs DDF-RA | In report |
|---|---|---|---|---|
| 1 — interval / duration activities | yes | **no** | **no** | yes, marked open |
| 2 — dose-relative extended hours | yes | **no** | yes | yes |
| 3 — "P" predose anchor | yes | **no** | yes | yes |
| 4 — footnote-encoded semantics | yes | **no** | **no** | yes, marked open |
| 5 — parallel pre-dose timeline | yes | **no** | yes | yes |
| 6 — dose-escalation cohorts | yes | **no** | **no** | **no** |

**Nothing is mapped to the twelve-pattern atlas.** That column has been empty since the project
started, and the report is framed as the delta against that atlas. It is the largest gap — larger
than the DDF-RA trace.

The report (`docs/report/early_phase_soas.md`) carries the corrected 27-protocol count, a status
block naming the two gaps, and a Part-2 paragraph on the twelve SAD/MAD candidates. **Part 3 still
characterises five issues** — issue 6 is not written up there, and the summary still says "the five
issues below". Its version line reads v0.1.0 / 2 July, which no longer matches its content.

## The one thing to do next

**Re-quote issues 1–5 from NCT05469126's actual SoA — and expect it to be work, not a lookup.**

`sources/EMP Study.docx` is a scoping document. Several strings in
`phase0_definition_and_terms.md` and in the report were transcribed off its screenshots. Fine for
scoping; not fine as the evidence in a published report, and one of them does not hold together —
the issue-2 series reads `96 (D5)` then `120 (D26)`, which cannot both be measured from one dose.

**What is actually in the corpus for NCT05469126** (checked 2026-09-21, not assumed):

| | |
|---|---|
| ground truth | **1 SoA table, 2 activities, 2 timepoints** — a stub |
| `has_cci_redactions` | **true** |
| `validated.pages.soa` | **absent** — the 11–19 range is the page-finder's guess, not a reviewer's |
| text layer | the 74-page PDF yields ~5k characters; `source/soa.pdf` yields 206, all title page |

So the SoA pages are **images of a partly redacted table**, and none of the strings the report
quotes appear in any text layer. This is a vision read plus a human check, not a grep. Budget for
it accordingly, and finish by writing the reviewer's page range and timeline count back into the
corpus with `set_soa_pages.py` — that is the corpus's job and it makes the read reusable.

Give particular attention to the monitoring series that span visits and days — issues 1 and 5,
and the reason the project exists. Where CCI redaction removes a value, the structure is still
quotable and the number is not; say which.

## Then, in order

2. **Map the six issues to the twelve-pattern atlas.** Mount `protocol_soa_patterns`, read
   `protocol_soa_patterns/docs/reports/soa_patterns.html`, and put each issue in one of three
   boxes: existing pattern, partial match, or absent. The column has been empty since the project
   began and the report is framed as the delta against that atlas. Do it before the DDF-RA trace —
   tracing an issue the atlas already covers is wasted work.

3. **Read the SAD/MAD SoAs and settle issue 6.** The twelve candidates are in
   `docs/project_protocols.md`. Start with **NCT04586920** (SAD + MAD + DDI + food effect,
   n=104, reviewer count **6 timelines** — the richest) and **NCT04178733** (plain SAD, 2
   timelines — the simplest). *Note on NCT04586920: its `compare.yaml` reads `reference: 0,
   extracted: 6`, which looks like total disagreement and is not — `reference` there is the
   machine-drafted count, which the corpus warns is not the reference. The reviewer count is 6
   and the extractor found 6. Read the PDF anyway; the six tables are vision-drafted.* Read the actual SoA, not the summary. Confirm or kill each of
   issue 6's four parts: the cohort axis, sentinel dosing, the escalation gate, MAD
   repeat-dosing days. Promote what survives; delete what does not.

4. **Trace issues 1, 4 and 6 against DDF-RA.** Mount `DDF-RA`; trace against
   `Deliverables/API/USDM_API.json`, `CT/USDM_CT.xlsx`, `RULES/USDM_CORE_Rules.xlsx` (v4.0).
   Quote the class or rule id. **No verdict without one.**
   - **Issue 1** — is a collection *interval* first-class (activity duration, or paired
     bounding timings), distinct from a ± scheduling window? The long-standing candidate for
     the one genuine delta.
   - **Issue 4** — repeat counts (triplicate), conditional repeats ("repeat daily until
     resolution"), ordering among co-timed activities.
   - **Issue 6** — does the cohort/dose-level axis ride on arms / elements / study cells with
     one timeline, or does each dose level need its own `ScheduleTimeline`? Where does the
     escalation gate live?

5. **Fix the sponsor concentration.** Ten of the twelve SAD/MAD candidates are Eli Lilly, on an
   already Lilly-heavy list. **Use `scripts/search.py`** — that is what it is for. Swap its
   `DEFAULT_KEYWORDS` for the ascending-dose set ("single ascending dose", "multiple ascending
   dose", "first in human"), keep `phase="1"`, `funder="industry"` and `docs:prot`, and run it;
   it pages the full result set and writes a CSV. Onboard what it finds through
   `protocol_corpus/scripts/corpus.py`. Failing that, state the limitation in the report. Do not publish an issue-6 finding that is
   really one sponsor's template.

6. **Rewrite the report.** Six issues in Part 3, each with its atlas box and its traced verdict;
   bump the version and date off v0.1.0 / 2 July; add **NCT05262387** as the worked example for the *interaction* of issues
   1/2/4/5 — its assessment-day sub-timeline shows all four at once, and it is one of only two
   protocols here carrying a handcrafted USDM workbook. Then
   `python3 report_theme/build.py docs/report/early_phase_soas.md`.

7. **Make the closure pass.** `aims.md` says the issue list is closed only when a pass over the
   SoA of every protocol in the chosen list turns up no timing or repetition pattern not already
   on the list. Nothing above is that pass — step 3 reads the twelve candidates only. Until it is
   made the list stays open and the project cannot be done, so it belongs here rather than being
   assumed. Protocols with no SoA are recorded as "no SoA", not skipped.

## Drop candidates — your call

- **`docs/report/early_phase_soas.pdf`** — 2026-07-06, two revisions behind, and nothing in the
  repo produces it (`report_theme/build.py` emits HTML only). Regenerable-looking but not
  regenerable. Delete.

## Open decisions

- **Three chosen protocols sit outside the scope boundary `aims.md` states.** The boundary is
  intervention-anchored, sub-day relative timing. **NCT02901925** has no SoA at all
  (reviewer-confirmed 0 timelines), **NCT03861000** is visits-only, **NCT04057807** is narrative
  plus visits. Either the boundary is drawn wrong or those three do not belong in the chosen list.
  They may be worth keeping as the specimens of *absence* — that is an argument, not a decision.
  Yours to settle; do not quietly widen the boundary to fit them.
- **NCT04805983** (Yale, BMS-984923) — rejected in 2026-07 for being "SAD-like", which is no
  longer a reason. Never onboarded, so it is not in `protocol_corpus` at all. Onboard it, or
  leave it rejected on some other ground? Undecided.
- **The 17-protocol pharma Phase 1 set** (2026-06-29) — never folded in or ruled out. Its SAD
  members are no longer out of scope by class. Fold or drop.

## Carried loose ends — corpus-side, not this project's to fix

These belong in `protocol_corpus/docs/issues.md` if they still matter. **Check there before
re-reporting any of them.** All three notes predate `scripts/corpus.py` and the
`validated.pages` override, so the recorded commands are likely wrong now.

- **NCT03733990 — CLOSED here.** A reviewer has since stated `validated.pages.soa` = 20–32 and
  three tables are drafted, so the page-finder gap this project recorded is fixed. It is *also*
  row **N32** in the corpus register, but for a different defect — no timepoint spine, no
  reviewer count — which is still open there and is not ours.
- **Temp pids files — CLOSED.** `phase1_pids.txt` and friends are gone from the corpus root. The
  five `2026-09-*_ids.txt` files there now are a later session's and unrelated.
- **NCT06390098 — still open**, and it is the only one. No `validated.pages.soa`; its single
  drafted "Schedule of Activities" is near-empty off pages 44–53. **It has no row in the corpus
  register** — raise one there, then delete this section. This project's own rule is that corpus
  defects live in the corpus register, not in a second list here.
