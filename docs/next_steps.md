# Next Steps — Protocol Phase 0

The current plan. **Rewritten whole, never appended to.** If a line here is stale, replace it.
Where the project is going: `docs/aims.md`. What we decided and why: `docs/lessons_learned.md`.

*Rewritten 2026-09-21 after a two-month gap and the SAD/MAD scope expansion. The previous
version stacked four historical plans on top of each other; none is reproduced here.*

## Where this stands

Six issues are named and grounded (`docs/phase0_definition_and_terms.md`). Against the four
completion tests in `aims.md`:

| Issue | Grounded | Mapped to atlas | USDM mechanism from atlas | In report |
|---|---|---|---|---|
| 1 — interval / duration activities | **no** | **no** | **no** | yes, marked open |
| 2 — dose-relative extended hours | yes | **no** | **no** | yes |
| 3 — "P" predose anchor | yes | **no** | **no** | yes |
| 4 — footnote-encoded semantics | **no** | **no** | **no** | yes, marked open |
| 5 — parallel pre-dose timeline | yes | **no** | **no** | yes |
| 6 — dose-escalation cohorts | **no** | **no** | **no** | **no** |

**Nothing is mapped to the twelve-pattern atlas, which is now the only thing issues are traced
against** (Dave, 2026-09-21 — DDF-RA is out). Mapping and tracing are therefore one job: name
the pattern, take the USDM mechanism the atlas gives for it. That column has been empty since the
project started, and the report is framed as the delta against that atlas.

The report is **generated** from `docs/report_source.yaml` by `scripts/build_report.py`; the
markdown is overwritten and must not be hand-edited. The build prints the table above from the
source and refuses to print a traced verdict that names no atlas mechanism.

## The one thing to do next

**Settle where issues 1 and 4's evidence actually comes from.**

Issues 2, 3 and 5 are now quoted from NCT05469126's extracted SoA in `protocol_corpus`
(`unvalidated.content.soa[0].conditions`), which carries the real footnote text — eighteen
activities, twelve timepoints, eleven conditions. No vision read was needed; the earlier note in
this file claiming a two-row stub was a counting error and is retracted.

That read also **closed the issue-2 puzzle**. The series is two crossover periods, not one:
Period 1 doses Day 1, Period 2 doses Day 21, each restarting the clock, which is why `96 (D5)`
could sit beside `120 (D26)`. The pattern was right; the transcription had merged them.

**What it opened is worse.** Issue 1's urine bins and all four of issue 4's footnotes
(± 1.5 hours, triplicate, "until resolution", the ECG/vitals/bloods ordering) **do not appear in
NCT05469126's extracted SoA at all** — it has no urine collection among its eighteen activities,
and its eleven footnotes are different ones. Two explanations, and they lead different places:

1. **The screenshots are of another protocol.** `status.md` recorded image2/3 as GZGM, but that
   was itself a note. Then issues 1 and 4 are attributed to the wrong protocol in the report.
2. **The extractor missed them.** Then it is a corpus finding and belongs in that register, and
   the protocol PDF has to be opened after all.

Open the PDF for the SoA pages and settle which. These are the two issues most likely to be the
genuine delta, so their attribution is not a detail.

## Then, in order

2. **Map the six issues to the twelve-pattern atlas.** Mount `protocol_soa_patterns`, read
   `protocol_soa_patterns/docs/reports/soa_patterns.html`, and put each issue in one of three
   name: which of the twelve patterns it is, which of the twenty-one footnote categories it uses,
   and the USDM mechanism (A–K) the atlas gives for those. That is the whole trace — there is no
   second step against DDF-RA. An issue that turns out to be an existing pattern is not a delta
   and should leave the report.

3. **Read the SAD/MAD SoAs and settle issue 6.** Twelve of the 36 in
   `docs/project_protocols.md`. Start with **NCT04586920** (SAD + MAD + DDI + food effect,
   n=104, reviewer count **6 timelines** — the richest) and **NCT04178733** (plain SAD, 2
   timelines — the simplest). *Note on NCT04586920: its `compare.yaml` reads `reference: 0,
   extracted: 6`, which looks like total disagreement and is not — `reference` there is the
   machine-drafted count, which the corpus warns is not the reference. The reviewer count is 6
   and the extractor found 6. Read the PDF anyway; the six tables are vision-drafted.* Read the actual SoA, not the summary. Confirm or kill each of
   issue 6's four parts: the cohort axis, sentinel dosing, the escalation gate, MAD
   repeat-dosing days. Promote what survives; delete what does not.

4. **Resolve what the atlas does not cover.** After step 2, whatever has no pattern, no footnote
   category or no mechanism is the delta — and that, not a rule id, is the report's finding.
   Expect it to be narrow: `pk_profile` probably takes issue 2, `heavy_footnoting` plus
   `window_tolerance` / `conditional_branch` / `sample_ordering` probably take most of issue 4.
   The likely residue is issue 1's interval-with-an-end, a repeat-count category the atlas has
   no name for, and issue 6's cohort axis against `multi_track` — the rarest pattern in the scan
   at 1.0%, so thin coverage there is expected.

5. **Fix the sponsor concentration.** Ten of the twelve ascending-dose entries are Eli Lilly, on
   an already Lilly-heavy list — and they are now in the chosen list, so the skew is the set's,
   not a candidate pool's. **Use `scripts/search.py`** — that is what it is for. Swap its
   `DEFAULT_KEYWORDS` for the ascending-dose set ("single ascending dose", "multiple ascending
   dose", "first in human"), keep `phase="1"`, `funder="industry"` and `docs:prot`, and run it;
   it pages the full result set and writes a CSV. Onboard what it finds through
   `protocol_corpus/scripts/corpus.py`. Failing that, state the limitation in the report. Do not publish an issue-6 finding that is
   really one sponsor's template.

6. **Finish the report.** The structure is generated now, so this is filling the source, not
   rewriting prose: each issue's `atlas.patterns` / `atlas.footnotes` and a `trace` with real `refs`. The build will not
   print a traced verdict without them. Bump `meta.version`; add **NCT05262387** as the worked example for the *interaction* of issues
   1/2/4/5 — its assessment-day sub-timeline shows all four at once, and it is one of only two
   protocols here carrying a handcrafted USDM workbook. Edit `docs/report_source.yaml`, never the markdown, then
   `python3 scripts/build_report.py`.

7. **Make the closure pass.** `aims.md` says the issue list is closed only when a pass over the
   SoA of every protocol in the chosen list turns up no timing or repetition pattern not already
   on the list. Nothing above is that pass — step 1 reads one protocol, step 3 reads twelve. Until it is
   made the list stays open and the project cannot be done, so it belongs here rather than being
   assumed. Protocols with no SoA are recorded as "no SoA", not skipped.

## Open decisions

- **NCT04805983** (Yale, BMS-984923) — rejected in 2026-07 for being "SAD-like", which is no
  longer a reason. Never onboarded, so it is not in `protocol_corpus` at all. Onboard it, or
  leave it rejected on some other ground? Undecided.
- **The 17-protocol pharma Phase 1 set** (2026-06-29) — never folded in or ruled out, and **the
  list of ids exists nowhere in this repo**, so the decision cannot be taken from what is here.
  It came from a `search.py` run whose CSV was deleted. Either re-run the search and name them,
  or close the decision. Leaving it open costs more than either.

## Carried loose ends — one left

**NCT06390098** still has no `validated.pages.soa` in `protocol_corpus` and its single drafted
"Schedule of Activities" is near-empty off pages 44–53. It has **no row in the corpus register**.
Raise one there; it is not this project's to fix. NCT03733990 and the temp pids files are closed.
