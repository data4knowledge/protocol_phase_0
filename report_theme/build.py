#!/usr/bin/env python3
"""Build a self-contained, d4k-themed HTML report from a markdown file.

The output is a single portable .html file: the theme CSS is inlined, so the
file can be moved, emailed or printed (A4) without any external assets.

Usage:
    python report_theme/build.py docs/report/foo.md
    python report_theme/build.py docs/report/foo.md -o docs/report/foo.html
    python report_theme/build.py docs/report/foo.md --kicker "protocol_complex · report"

Optional YAML-ish front matter (kept deliberately simple — no PyYAML needed):

    ---
    title: Complex Studies and Their Mapping into USDM
    kicker: protocol_complex · report
    footer: Complex Studies & USDM · draft
    date: 2026-06-03
    ---

Front matter is optional. Missing values are derived:
    title  -> front matter, else first H1, else file stem
    kicker -> front matter, else the containing git-repo folder name
    footer -> front matter "footer", else title; date is appended automatically
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency: pip install markdown")

HERE = Path(__file__).resolve().parent
CSS_PATH = HERE / "theme.css"
TEMPLATE_PATH = HERE / "template.html"

MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "footnotes",
    "attr_list",
    "sane_lists",
    "md_in_html",   # lets raw HTML blocks (inline SVG figures, callouts) pass through
    "toc",
]


def split_front_matter(text: str) -> tuple[dict, str]:
    """Return (meta, body). Front matter is an optional leading --- ... --- block."""
    meta: dict[str, str] = {}
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line and not line.lstrip().startswith("#"):
                    k, _, v = line.partition(":")
                    meta[k.strip().lower()] = v.strip()
            text = text[m.end():]
    return meta, text


def derive_title(meta: dict, body_md: str, md_path: Path) -> str:
    if meta.get("title"):
        return meta["title"]
    m = re.search(r"^#\s+(.+)$", body_md, re.MULTILINE)
    if m:
        # strip any trailing {#id} attr-list and inline emphasis markers
        return re.sub(r"\s*\{#[^}]+\}\s*$", "", m.group(1)).strip()
    return md_path.stem.replace("_", " ").title()


def derive_kicker(meta: dict, md_path: Path) -> str:
    if meta.get("kicker"):
        return meta["kicker"]
    # walk up to the nearest dir containing .git -> use its folder name
    for parent in md_path.resolve().parents:
        if (parent / ".git").exists():
            return f"{parent.name} · report"
    return "report"


def build(md_path: Path, out_path: Path | None, kicker_override: str | None) -> Path:
    raw = md_path.read_text(encoding="utf-8")
    meta, body_md = split_front_matter(raw)

    title = derive_title(meta, body_md, md_path)
    kicker = kicker_override or derive_kicker(meta, md_path)
    today = meta.get("date") or _dt.date.today().isoformat()
    footer_base = meta.get("footer") or title
    footer = f"{footer_base} · {today}"

    md = markdown.Markdown(extensions=MD_EXTENSIONS, output_format="html5")
    body_html = md.convert(body_md)

    css = CSS_PATH.read_text(encoding="utf-8")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    out_html = (
        template
        .replace("{{TITLE}}", html.escape(title))
        .replace("{{KICKER}}", html.escape(kicker))
        .replace("{{FOOTER}}", html.escape(footer))
        .replace("{{CSS}}", css)
        .replace("{{BODY}}", body_html)
    )

    if out_path is None:
        out_path = md_path.with_suffix(".html")
    out_path.write_text(out_html, encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build a d4k-themed HTML report from markdown.")
    p.add_argument("markdown", type=Path, help="Path to the source .md file")
    p.add_argument("-o", "--out", type=Path, default=None, help="Output .html path (default: alongside the .md)")
    p.add_argument("--kicker", default=None, help="Override the header kicker text")
    args = p.parse_args(argv)

    if not args.markdown.exists():
        p.error(f"file not found: {args.markdown}")

    out = build(args.markdown, args.out, args.kicker)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
