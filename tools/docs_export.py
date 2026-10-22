#!/usr/bin/env python3
# =============================================================================
#  docs_export.py — turns docs/*.md into an ingest bundle for the web renderer
#
#  WHY THIS EXISTS. The public site is rendered by the web renderer, not by
#  MkDocs. the web renderer needs three things that plain markdown files do not
#  carry: the ORDER of the pages, their SECTION and their TITLE — plus
#  links rewritten from `foo.md` to a slug the web can resolve.
#
#  The order comes from the `nav:` in mkdocs.yml, so there is ONE list to
#  maintain, not two. A page in docs/ that is missing from the nav (or the
#  other way round) is an error here — silently dropping a page from the
#  customer site is exactly the failure nobody notices.
#
#  A section of a page can still be kept back from the web:
#
#      <!-- internal -->
#      ... never leaves the repository ...
#      <!-- /internal -->
#
#  Unbalanced markers are a hard error, never a silent half-strip.
#
#  Output:
#      export/manifest.json    ordered tree: section, title, slug, file
#      export/<slug>.md        YAML front matter + body, links rewritten
#      export/<path>           every non-markdown file under docs/ (the
#                              clip and its poster), at the SAME relative
#                              path the pages reference
#
#  Usage:
#      python tools/docs_export.py                    # DRY RUN, prints the plan
#      python tools/docs_export.py --apply            # writes export/
#      python tools/docs_export.py --apply --link-base /docs/
#
#  WHEN IT FAILS AND WHAT STAYS: every page is read, stripped and checked
#  BEFORE anything is written, so a failing check leaves the previous
#  export untouched and consistent. With --apply the target is cleared of
#  *.md first (a page deleted here must disappear there too) — after all
#  checks have passed. Needs: pip install pyyaml
#
#  WHAT THIS CANNOT SEE. This script gets export/ right and
#  stops there — the INGEST on the other side keeps its own state. When a
#  page moves (Examples became a section) or gets ingested twice, Drupal
#  keeps the old node and gives the new one a `-0` alias, so the live
#  sidebar shows the same title twice: /docs/tutorial + /docs/tutorial-0,
#  and /docs/examples-0. Nothing here and nothing in manifest.json shows
#  it — both are correct. After any page move or rename, LOOK at the live
#  sidebar and delete the orphan node in the web renderer.
# =============================================================================
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from share_header import share_lines, take_header  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Never on the public web. Not hypothetical: the licensing chapter in the
# product repository documents how licences are ISSUED, and that text
# must not reappear here through a copy-paste a year from now.
FORBIDDEN = [
    "inovaea-keys",
    "licgen",
    "private key",
    "license_key.inc",
]

INT_OPEN = "<!-- internal -->"
INT_CLOSE = "<!-- /internal -->"

LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+?)\.md(#[^)\s]*)?\)")
# a picture alone on its line (no attribute list after it) - centred on
# export, see the loop in main()
IMG_LINE_RE = re.compile(r"^(!\[[^\]]*\]\([^)\s]+\))[ \t]*$", re.M)


def load_nav():
    """(section, title, filename) in nav order, taken from mkdocs.yml."""
    cfg = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    out = []

    def walk(items, section):
        for it in items:
            for title, val in it.items():
                if isinstance(val, str):
                    out.append((section, title, val))
                else:
                    walk(val, title)

    walk(cfg["nav"], "")
    return out


def strip_internal(text: str, name: str) -> str:
    out, pos = [], 0
    while True:
        a = text.find(INT_OPEN, pos)
        if a < 0:
            out.append(text[pos:])
            return "".join(out)
        b = text.find(INT_CLOSE, a)
        if b < 0:
            sys.exit(f"ERROR {name}: '{INT_OPEN}' without a closing "
                     f"'{INT_CLOSE}' — refusing to export half a page")
        out.append(text[pos:a])
        pos = b + len(INT_CLOSE)
        if text[pos:pos + 1] == "\n":
            pos += 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="really write (default is a dry run)")
    ap.add_argument("--out", default=str(ROOT / "export"),
                    help="target folder (default export/)")
    ap.add_argument("--link-base", default="/docs/",
                    help="prefix for rewritten links (default /docs/ — "
                         "the site base is fixed; '' breaks every "
                         "cross-section link)")
    args = ap.parse_args()
    out = Path(args.out).resolve()

    # MSYS/Git-Bash rewrites a leading "/" argument into a Windows path,
    # so `--link-base /docs/` arrived here as
    # "C:/Program Files/Git/docs/" and every cross-link in the bundle
    # pointed into a Git installation. It published cleanly and looked
    # fine in the diff — the kind of corruption you only find by reading
    # the result back. Refuse it
    # instead: a link base is a URL path or nothing.
    lb = args.link_base
    if lb and not (lb.startswith("/") or lb.startswith("http")):
        sys.exit(f"ERROR: --link-base '{lb}' is not a URL path. If you "
                 f"are in Git Bash, MSYS rewrote it — run this from "
                 f"PowerShell, or prefix the command with "
                 f"MSYS2_ARG_CONV_EXCL='*'.")

    nav = load_nav()
    slugs = {f: f[:-3] for _, _, f in nav}

    # Where each page LIVES on the web: a page inside a section sits
    # under its section's LANDING slug (/docs/buses/modbus); the
    # landing itself and navless pages sit flat (/docs/buses,
    # /docs/quickstart). The old rewrite emitted bare flat slugs and
    # the browser resolved them RELATIVE to wherever the reader stood —
    # /docs/limits from the index, /docs/buses/peripherals-and-services
    # from a bus page — a systematic 404 an audit caught on
    # four pages before calling it a generator bug (it was).
    landing = {}
    for section, title, fname in nav:
        if section and title == section:
            landing[section] = slugs[fname]
    url_of = {}
    for section, title, fname in nav:
        slug = slugs[fname]
        if not section or landing.get(section) == slug:
            url_of[slug] = slug
        else:
            url_of[slug] = f"{landing.get(section, section)}/{slug}"

    on_disk = {f.name for f in DOCS.glob("*.md")}
    missing = [f for _, _, f in nav if f not in on_disk]
    extra = sorted(on_disk - set(slugs))
    if missing:
        sys.exit(f"ERROR: in the nav but not in docs/: {', '.join(missing)}")
    if extra:
        sys.exit(f"ERROR: in docs/ but not in the nav: {', '.join(extra)}. "
                 f"Add it to mkdocs.yml or delete it — a page nobody can "
                 f"reach is a page nobody reads.")

    pages, warns = [], []
    for section, title, fname in nav:
        raw = (DOCS / fname).read_text(encoding="utf-8")
        share, raw = take_header(raw, fname, DOCS)
        body = strip_internal(raw, fname)
        low = body.lower()
        for bad in FORBIDDEN:
            if bad.lower() in low:
                sys.exit(f"ERROR {fname}: contains '{bad}' — that does not "
                         f"belong on the public web. Wrap it in "
                         f"{INT_OPEN} … {INT_CLOSE} or remove it.")

        def fix_link(m):
            target, anchor = m.group(2), m.group(3) or ""
            if target + ".md" not in slugs:
                warns.append(f"{fname}: link to '{target}.md' is not a page "
                             f"— reduced to plain text")
                return m.group(1)
            # ONE URL FORM: the canonical address ENDS
            # with a slash — the sitemap, the canonical tag and the site's
            # own redirect all say so. Emitting the bare form made every
            # cross-link in the documentation spend a 301, and Search
            # Console filed 16 pages under "Page with redirect". The slash
            # goes BEFORE the anchor, or the fragment lands on the wrong
            # side of the redirect.
            return (f"[{m.group(1)}]"
                    f"({args.link_base}{url_of[target]}/{anchor})")

        body = LINK_RE.sub(fix_link, body)

        # EVERY picture standing on its own line is centred - the site's `.sb-center`
        # class (display:block; margin-inline:auto). A line that already
        # carries an attribute list keeps it; an inline picture inside
        # a sentence is left alone.
        body = IMG_LINE_RE.sub(lambda m: m.group(1) + "{: .sb-center}", body)

        slug  = slugs[fname]
        order = len(pages) + 1
        # THE SECTION IS A FOLDER: their
        # navigation tree follows directories, where a section is a real
        # page with a real address rather than a label. A `section:`
        # string names no page, so honouring it would have meant them
        # inventing a parent record per section — one line here is the
        # cheaper half of that trade. The front matter keeps `section:`
        # anyway: it costs nothing and says what the folder means.
        #
        # AND THE FOLDER NEEDS AN INDEX PAGE: their tree
        # nests a page under the INDEX PAGE of its directory. A folder
        # without one has nothing to nest under, so every page fell to
        # the top level and the public menu rendered as one flat list —
        # exactly what the section folders were meant to prevent. The
        # page whose nav TITLE equals its section name is that section's
        # landing page and becomes the folder's index.md.
        is_landing = bool(section) and title == section
        rel   = (f"{section}/index.md" if is_landing
                 else f"{section}/{slug}.md" if section
                 else f"{slug}.md")
        front = ("---\n"
                 f"title: {json.dumps(title, ensure_ascii=False)}\n"
                 f"slug: {slug}\n"
                 f"section: {json.dumps(section, ensure_ascii=False)}\n"
                 f"order: {order}\n"
                 # the same number under the name their engine reads
                 # natively — one of us translating it beats both of us
                 # remembering that the two mean the same thing
                 f"sidebar_position: {order}\n"
                 + share_lines(share) +
                 "generator: tools/docs_export.py\n"
                 "---\n\n")
        pages.append({"slug": slug, "title": title, "section": section,
                      "order": order, "file": rel,
                      "bytes": len(body.encode("utf-8")),
                      "_text": front + body})

    # Every section MUST have exactly one landing page (a page titled
    # like the section, first in it) — without one the web menu cannot
    # group the section's pages and the whole navigation collapses into
    # a flat list. That is a fault this tool refuses, not a style choice.
    by_sec = {}
    for p in pages:
        if p["section"]:
            by_sec.setdefault(p["section"], []).append(p)
    for sec, ps in by_sec.items():
        landings = [p for p in ps if p["file"].endswith("/index.md")]
        if len(landings) != 1:
            sys.exit(f"ERROR: section '{sec}' has {len(landings)} landing "
                     f"pages (need exactly 1: a page titled '{sec}'), "
                     f"or the web menu shows its pages ungrouped")
        if ps[0] is not landings[0]:
            sys.exit(f"ERROR: the landing page of '{sec}' must be FIRST "
                     f"in its section in mkdocs.yml")

    # Assets: everything under docs/ that is not a page. They keep their
    # relative path, because that is what the pages already reference
    # (<video src="video/…">) — rewriting media paths would mean parsing
    # raw HTML, and this way there is nothing to get wrong.
    assets = sorted(f.relative_to(DOCS).as_posix()
                    for f in DOCS.rglob("*")
                    if f.is_file() and f.suffix.lower() != ".md")

    print(f"pages   : {len(pages)}")
    print(f"assets  : {len(assets)}")
    print(f"content : {sum(p['bytes'] for p in pages)/1024:.1f} kB")
    cur = None
    for p in pages:
        if p["section"] != cur:
            cur = p["section"]
            print(f"  [{cur or '(root)'}]")
        print(f"    {p['slug']:<28} {p['title']}")
    for w in warns:
        print(f"WARN {w}")

    if not args.apply:
        print(f"\nDRY RUN — nothing written. --apply writes to {out}")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    # RECURSIVE clear: a page that moves to another section must not stay
    # behind in the old folder, where the next import would meet two
    # records claiming the same slug
    for old in out.rglob("*.md"):
        old.unlink()
    for p in pages:
        dst = out / p["file"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(p.pop("_text"), encoding="utf-8")
    # an asset DELETED from docs/ must leave export/ too - the .md files
    # are wiped and rewritten above, the assets were only ever copied, so
    # 51 pictures of ST code lived on in the bundle after the pages
    # stopped naming them. Stale bytes in a bundle are the
    # "abandoned location" trap in its smallest form.
    keep = {(out / rel) for rel in assets}
    for old_asset in out.rglob("*"):
        if old_asset.is_file() and old_asset.suffix.lower() != ".md"                 and old_asset.name != "manifest.json"                 and old_asset not in keep:
            old_asset.unlink()
    for rel in assets:
        dst = out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DOCS / rel, dst)

    # A section that was renamed (or translated) leaves its old folder
    # behind, empty. An empty directory in a bundle is a section in their
    # navigation tree — so prune, deepest first.
    for d in sorted((p for p in out.rglob("*") if p.is_dir()),
                    key=lambda p: len(p.parts), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()

    (out / "manifest.json").write_text(
        json.dumps({"site": "ctrl32", "language": "en",
                    "generator": "tools/docs_export.py",
                    "sections": list(dict.fromkeys(p["section"]
                                                   for p in pages)),
                    "pages": pages, "assets": assets},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"\nwritten to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
