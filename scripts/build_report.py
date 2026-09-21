#!/usr/bin/env python3
"""Generate docs/report/early_phase_soas.md from its structured source.

WHY THIS EXISTS
    The report used to be typed by hand. Every figure in it was a hand-maintained
    number, and they drifted — the protocol count said 26 while the protocol list
    said 27, the same footnote was quoted two different ways in two files, and an
    issue marked "traced" cited no rule id. None of that is a writing problem; it
    is what happens when prose and data live in the same hand-edited file.

    So the prose and the verdicts live in `docs/report_source.yaml`, the protocol
    set is read from `docs/project_protocols.md`, and this script assembles the
    markdown. **Do not hand-edit `docs/report/early_phase_soas.md` — it is
    overwritten.** Edit the YAML.

WHAT IT ENFORCES (from docs/aims.md, "What counts as done")
    An issue is finished only if it is grounded, mapped, traced and stated. This
    script cannot judge prose, but it can refuse to let the report claim more than
    the source supports.

    SIX conditions fail the build (exit non-zero, nothing written):

    1. `trace.status` is not one of traced / open / mixed.
    2. `trace.status: traced` with no `trace.refs`. The aims file defines traced as
       named against the SoA pattern atlas; a verdict naming nothing is an assertion,
       which is the failure mode this project keeps hitting.
    3. A `trace.refs` entry that is not an atlas mechanism (A-K).
    4. An `atlas.patterns` or `atlas.footnotes` name that is not in the atlas
       vocabulary held in the source, which is copied from
       `protocol_soa_patterns/docs/reports/soa_patterns.html`.
    5. An evidence `protocol` that is not in the chosen set.
    6. A malformed protocol table in `docs/project_protocols.md`.

    Two things are reported rather than enforced, because they are findings about the
    work and not errors in it:

    - Evidence carrying `verified: false` prints an "Unverified" callout beneath the
      quotation, in the report itself. A provenance warning that lives only in an
      internal document warns nobody.
    - An issue naming no atlas pattern or footnote category counts as not placed,
      prints as an open gap, and is counted in the status block.

    Counts - the protocol total, the grounded/mapped/traced tallies, the sponsor
    concentration - are computed here, never typed.

HOW TO RUN
    python3 scripts/build_report.py              # markdown + themed HTML
    python3 scripts/build_report.py --no-html    # markdown only
    python3 scripts/build_report.py --check      # validate, write nothing

    Dependencies are in requirements.txt: pyyaml here, markdown for the HTML step.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "report_source.yaml"
PROTOCOLS = ROOT / "docs" / "project_protocols.md"
OUT_MD = ROOT / "docs" / "report" / "early_phase_soas.md"



class BuildError(Exception):
    pass


# --------------------------------------------------------------------------- data


def read_protocol_set(path: Path) -> list[dict]:
    """Parse the Chosen table out of project_protocols.md.

    That table is the source of truth for the set; parsing it rather than
    duplicating it in the YAML is the whole point — two copies of a list are two
    lists, and they diverge.
    """
    text = path.read_text(encoding="utf-8")
    try:
        section = text[text.index("## Chosen"): text.index("## Rejected")]
    except ValueError as exc:
        raise BuildError(f"{path.name}: expected '## Chosen' and '## Rejected' headings") from exc

    rows = []
    for line in section.splitlines():
        if not re.match(r"\| NCT\d{8} \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            raise BuildError(f"{path.name}: row has {len(cells)} columns, expected 6:\n  {line}")
        rows.append(dict(zip(("nct", "sponsor", "indication", "what", "soa", "anchor"), cells)))

    if not rows:
        raise BuildError(f"{path.name}: no protocol rows found under '## Chosen'")
    seen = {r["nct"] for r in rows}
    if len(seen) != len(rows):
        raise BuildError(f"{path.name}: duplicate NCT ids in the chosen table")
    return rows


def sponsor_tally(rows: list[dict]) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for r in rows:
        name = re.sub(r"\s*\(.*\)", "", r["sponsor"]).strip()
        counts[name] = counts.get(name, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


# ---------------------------------------------------------------------- validation


def validate(src: dict, rows: list[dict]) -> list[dict]:
    """Hard failures raise. Otherwise return one status row per issue.

    The row is the four tests from `docs/aims.md`, so the build prints the state of
    the work rather than a list of complaints.
    """
    rowstats: list[dict] = []
    ids = {r["nct"] for r in rows}
    vocab = src["atlas"]

    for issue in src["issues"]:
        num = issue["number"]
        trace = issue.get("trace") or {}
        status = trace.get("status")
        if status not in {"traced", "open", "mixed"}:
            raise BuildError(f"issue {num}: trace.status is {status!r}, expected traced/open/mixed")
        if status == "traced" and not trace.get("refs"):
            raise BuildError(
                f"issue {num} claims trace.status: traced with no trace.refs.\n"
                f"  docs/aims.md defines traced as named against the SoA pattern atlas:\n"
                f"  the pattern it is, and the USDM mechanism (A-K) the atlas gives for it.\n"
                f"  Either add the mechanisms, or set status to open."
            )

        atlas = issue.get("atlas") or {}
        for field, allowed in (("patterns", vocab["patterns"]), ("footnotes", vocab["footnotes"])):
            for name in atlas.get(field) or []:
                if name not in allowed:
                    raise BuildError(
                        f"issue {num}: atlas.{field} names {name!r}, which is not in the atlas.\n"
                        f"  The vocabulary is in docs/report_source.yaml, copied from\n"
                        f"  protocol_soa_patterns/docs/reports/soa_patterns.html."
                    )
        placed = bool(atlas.get("patterns") or atlas.get("footnotes"))

        for ref in trace.get("refs") or []:
            if ref not in vocab["mechanisms"]:
                raise BuildError(
                    f"issue {num}: trace.refs names {ref!r}, which is not an atlas mechanism.\n"
                    f"  Valid: {', '.join(sorted(vocab['mechanisms']))}."
                )

        evidence = issue.get("evidence") or []
        for ev in evidence:
            nct = ev.get("protocol")
            if nct and nct not in ids:
                raise BuildError(
                    f"issue {num} cites {nct}, which is not in the chosen set.\n"
                    f"  Add it to docs/project_protocols.md or stop citing it."
                )

        rowstats.append({
            "number": num,
            "title": issue["title"],
            # aims test 1 is "evidenced in a named protocol's actual SoA". An issue
            # with no evidence at all is not grounded, so require evidence to exist
            # AND none of it to be flagged unverified.
            "grounded": bool(evidence) and not any(ev.get("verified") is False for ev in evidence),
            "mapped": placed,
            "traced": status == "traced",
        })
    return rowstats


def print_status(rowstats: list[dict], n_protocols: int) -> None:
    """One table, not a list of complaints.

    Each column is a test from `docs/aims.md`: grounded (evidence read from the
    protocol, not transcribed), mapped (placed against the twelve-pattern atlas),
    traced (the USDM mechanism the atlas gives for that pattern). An issue passes
    all three, or it is not finished.
    """
    def mark(ok: bool) -> str:
        return "  yes  " if ok else "  NO   "

    print(f"\n{n_protocols} protocols, {len(rowstats)} issues. Tests from docs/aims.md:\n")
    print("        grounded  mapped  traced   issue")
    for r in rowstats:
        print(f"  {r['number']}   {mark(r['grounded'])}{mark(r['mapped'])}{mark(r['traced'])}  {r['title'][:52]}")
    done = sum(1 for r in rowstats if r["grounded"] and r["mapped"] and r["traced"])
    print(f"\n  {done} of {len(rowstats)} issues pass all three.")
    if done < len(rowstats):
        print("  grounded NO = no evidence, or evidence flagged verified: false")
        print("  mapped   NO = no atlas pattern named in docs/report_source.yaml")
        print("  traced   NO = trace.status is open, i.e. no atlas mechanism (A-K) given")
    print()


# ----------------------------------------------------------------------- rendering


def render(src: dict, rows: list[dict]) -> str:
    meta = src["meta"]
    out: list[str] = []
    w = out.append

    w("---")
    w(f"title: {meta['title_long']}")
    w(f"kicker: {meta['kicker']}")
    w(f"footer: {meta['footer']}")
    w("---")
    w("")
    w('<div class="report-title">')
    w(f"  <h1>{meta['title']}</h1>")
    w(f'  <p class="subtitle">{meta["subtitle"]}</p>')
    w(f'  <p class="docmeta">Version: {meta["version"]} · {meta["date"]}</p>')
    w("</div>")
    w("")
    w("<!-- GENERATED by scripts/build_report.py from docs/report_source.yaml. Do not hand-edit. -->")
    w("")

    w("## Summary")
    w("")
    w(src["summary"].strip())
    w("")

    # status block — computed, never typed
    total = len(src["issues"])
    unmapped = sum(1 for i in src["issues"]
                   if not ((i["atlas"].get("patterns") or []) or (i["atlas"].get("footnotes") or [])))
    untraced = sum(1 for i in src["issues"] if i["trace"]["status"] != "traced")
    unverified = sum(
        1 for i in src["issues"] if any((e.get("verified") is False) for e in (i.get("evidence") or []))
    )
    w("> **Status.** Against the four tests in `docs/aims.md` — grounded, mapped, traced, stated —")
    w(f"> this report carries **{total} issues**, of which **{unmapped} are unmapped** against the")
    w(f"> twelve-pattern atlas and **{untraced} carry no USDM mechanism** from it."
      + (f" **{unverified}** rest on an" if unverified else ""))
    if unverified:
        w("> unverified transcription rather than on the protocol.")
    w(">")
    w("> Issues are traced against the SoA pattern atlas and nothing else: the pattern an issue")
    w("> is, and the USDM mechanism the atlas gives for it. The build refuses to print a traced")
    w("> verdict that names neither. Plan: `docs/next_steps.md`.")
    w("")

    w("## Part 1 · What these studies are")
    w("")
    w(src["part1"].strip())
    w("")

    w("## Part 2 · The protocol set")
    w("")
    w(f"The set is **{len(rows)} protocols** from ClinicalTrials.gov (real posted protocol documents")
    w("only), listed with sponsor, indication, SoA form and timing anchor in")
    w("`docs/project_protocols.md`. In shape it splits into:")
    w("")
    for cat in src["part2"]["categories"]:
        w(f"- **{cat['name']}** — {cat['note']}")
    w("")
    tally = sponsor_tally(rows)
    top, n = tally[0]
    w(f"**Sponsor concentration.** {n} of the {len(rows)} are {top}"
      f" ({n * 100 // len(rows)}% of the set), across {len(tally)} sponsors in total."
      " A finding drawn from a set this concentrated reads as one sponsor's template until that")
    w("is fixed or stated — `docs/next_steps.md` step 5.")
    w("")
    if src["part2"].get("note"):
        w(src["part2"]["note"].strip())
        w("")

    w("## Part 3 · SoA representation issues and USDM impact")
    w("")
    w(src["part3_intro"].strip())
    w("")

    for issue in src["issues"]:
        w(f"### Issue {issue['number']} — {issue['title']}")
        w("")
        for ev in issue.get("evidence") or []:
            if ev.get("lead"):
                w(f"**What the SoA shows.** {ev['lead'].strip()}")
                w("")
            if ev.get("quote"):
                for line in ev["quote"].strip().splitlines():
                    w(f"> {line}")
                w("")
            if ev.get("verified") is False:
                w(f"> **Unverified.** {ev.get('caveat', 'Not checked against the protocol.').strip()}")
                w("")
        w(f"**What it demands.** {issue['demands'].strip()}")
        w("")
        atlas = issue["atlas"]
        pats = atlas.get("patterns") or []
        fns = atlas.get("footnotes") or []
        if pats or fns:
            bits = []
            if pats:
                bits.append("pattern " + ", ".join(f"`{p}`" for p in pats))
            if fns:
                bits.append("footnote category " + ", ".join(f"`{f}`" for f in fns))
            line = "; ".join(bits)
        else:
            line = "**not yet placed**"
        w(f"**Atlas:** {line}." + (f" {atlas['note'].strip()}" if atlas.get("note") else ""))
        w("")
        trace = issue["trace"]
        head = {"traced": "traced", "open": "OPEN", "mixed": "mixed"}[trace["status"]]
        refs = (" (atlas mechanism " + ", ".join(trace["refs"]) + ")") if trace.get("refs") else ""
        w(f"**USDM status: {head}{refs}.** {trace['verdict'].strip()}")
        w("")

    w("### Where this leaves USDM")
    w("")
    w(src["conclusion"].strip())
    w("")

    w("## References")
    w("")
    for ref in src["references"]:
        w(f"- {ref}")
    w("")

    return "\n".join(out)


# ---------------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-html", action="store_true", help="write the markdown only")
    ap.add_argument("--check", action="store_true", help="validate and report, write nothing")
    args = ap.parse_args(argv)

    try:
        src = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
        rows = read_protocol_set(PROTOCOLS)
        rowstats = validate(src, rows)
    except BuildError as exc:
        print(f"BUILD FAILED\n{exc}", file=sys.stderr)
        return 1

    print_status(rowstats, len(rows))

    if args.check:
        print("check only — nothing written")
        return 0

    OUT_MD.write_text(render(src, rows) + "\n", encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")

    if not args.no_html:
        # The markdown is already on disk and is the deliverable this script owns.
        # A failure in the HTML step is a separate, recoverable problem — usually a
        # missing `markdown` package — so report it and exit non-zero without a
        # traceback, which says nothing the message above it did not.
        result = subprocess.run(
            [sys.executable, str(ROOT / "report_theme" / "build.py"), str(OUT_MD)],
            cwd=ROOT,
        )
        if result.returncode != 0:
            print(
                f"\nHTML step failed (exit {result.returncode}). The markdown was written.\n"
                f"  If the message above names a missing package, install it into this venv:\n"
                f"    pip install -r requirements.txt\n"
                f"  Then re-run, or build the HTML alone:\n"
                f"    python3 report_theme/build.py {OUT_MD.relative_to(ROOT)}",
                file=sys.stderr,
            )
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
