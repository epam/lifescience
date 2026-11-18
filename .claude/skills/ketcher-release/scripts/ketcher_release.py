#!/usr/bin/env python3
"""Add Ketcher releases from GitHub (epam/ketcher) to the lifescience portal.

Generates/patches every file a Ketcher release touches:
  rst/ketcher/release-notes/ketcher-X.Y.Z.md        (new)
  rst/download/ketcher/ketcher-X.Y.Z.rst            (new)
  rst/download/ketcher.rst                          (Latest / Older toctrees)
  rst/ketcher/release-notes/index.rst               (toctree, ascending)
  rst/ketcher/demo/ketcher_remote.rst               (version, keeps BOM)
  rst/ketcher/demo/ketcher_standalone.rst           (version, keeps BOM)
  rst/themes/lifescience-theme/json-ld_ketcher.html (softwareVersion)
  rst/newsfeed.rst                                  (date-sorted news entries)

Requires the `gh` CLI (authenticated). Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

GH_REPO = "epam/ketcher"
SITE = "https://lifescience.opensource.epam.com"
NPM_PACKAGES = ["ketcher-core", "ketcher-react", "ketcher-standalone", "ketcher-macromolecules"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

NOTES_DIR = "rst/ketcher/release-notes"
DOWNLOAD_DIR = "rst/download/ketcher"
DOWNLOAD_INDEX = "rst/download/ketcher.rst"
NOTES_INDEX = "rst/ketcher/release-notes/index.rst"
DEMO_PAGES = ["rst/ketcher/demo/ketcher_remote.rst", "rst/ketcher/demo/ketcher_standalone.rst"]
JSON_LD = "rst/themes/lifescience-theme/json-ld_ketcher.html"
NEWSFEED = "rst/newsfeed.rst"

warnings: list[str] = []


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"WARNING: {msg}", file=sys.stderr)


# ---------------------------------------------------------------- versions

def vkey(v: str) -> tuple[int, ...]:
    return tuple(int(p) for p in v.split("."))


def is_plain_version(v: str) -> bool:
    return re.fullmatch(r"\d+\.\d+\.\d+", v) is not None


def is_patch(v: str) -> bool:
    return vkey(v)[2] != 0


@dataclass
class Release:
    version: str
    date: dt.date
    body: str


def gh_json(args: list[str]):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def published_versions(root: Path) -> list[str]:
    found = []
    for p in (root / NOTES_DIR).glob("ketcher-*.md"):
        v = p.stem[len("ketcher-"):]
        if is_plain_version(v):
            found.append(v)
    return sorted(found, key=vkey)


def pending_versions(root: Path, include_patches: bool) -> list[str]:
    releases = gh_json(["release", "list", "-R", GH_REPO, "-L", "100",
                        "--json", "tagName,isPrerelease,isDraft"])
    have = published_versions(root)
    latest = vkey(have[-1]) if have else (0, 0, 0)
    out = []
    for r in releases:
        v = r["tagName"].lstrip("v")
        if r["isPrerelease"] or r["isDraft"] or not is_plain_version(v):
            continue
        if is_patch(v) and not include_patches:
            continue
        if vkey(v) > latest and v not in have:
            out.append(v)
    return sorted(set(out), key=vkey)


def parse_name_date(name: str) -> dt.date | None:
    # Release names look like "Ketcher 3.10.0 February 27, 2026"
    m = re.search(r"(" + "|".join(MONTHS) + r")\s+(\d{1,2}),\s*(\d{4})", name)
    if not m:
        return None
    return dt.date(int(m.group(3)), MONTHS.index(m.group(1)) + 1, int(m.group(2)))


def fetch_release(version: str) -> Release:
    data = gh_json(["release", "view", f"v{version}", "-R", GH_REPO,
                    "--json", "name,body,publishedAt"])
    date = parse_name_date(data.get("name") or "")
    if date is None:
        date = dt.date.fromisoformat(data["publishedAt"][:10])
        warn(f"{version}: no date in release name {data.get('name')!r}; "
             f"using publishedAt {date.isoformat()} - confirm with the user")
    return Release(version, date, data.get("body") or "")


def fmt_date(d: dt.date) -> str:
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


# ---------------------------------------------------------------- renderers

ISSUE_RE = re.compile(r"(?<![\[\w/#])#(\d+)\b")


def render_notes_md(rel: Release) -> str:
    body = rel.body.replace("\r\n", "\n").replace("\r", "\n")
    lines = []
    for line in body.split("\n"):
        line = line.rstrip()
        line = re.sub(r"^(\s*)\* ", r"\1- ", line)
        if not line.lstrip().startswith("#"):  # leave markdown headings alone
            line = ISSUE_RE.sub(lambda m: f"[#{m.group(1)}](https://github.com/{GH_REPO}/issues/{m.group(1)})", line)
        lines.append(line)
    text = "\n".join(lines).strip("\n")
    check_body(rel, text)
    return f"\n# Ketcher {rel.version}\n\n{text}\n"


def check_body(rel: Release, text: str) -> None:
    v = rel.version
    if not text.strip():
        warn(f"{v}: GitHub release body is empty")
        return
    if "github.com/epam/ketcher/issues/" not in text:
        warn(f"{v}: no #NNNN issue references found - check the notes format")
    if "Additional notes" not in text or "Indigo" not in text:
        warn(f"{v}: no 'Additional notes' / Indigo version line - ask whether one should be added")
    known = {"What's Changed", "New features", "Bugfixes and improvements", "Additional notes:", "Additional notes"}
    for h in re.findall(r"^#+\s*(.+?)\s*$", text, re.M):
        if h not in known:
            warn(f"{v}: unusual section heading {h!r} - review the generated notes")


def render_download_rst(v: str) -> str:
    title = f"Ketcher {v}"
    npm = "\n".join(f"| `{p} <https://www.npmjs.com/package/{p}/v/{v}>`__" for p in NPM_PACKAGES)
    return (
        f"{title}\n{'-' * len(title)}\n\n"
        "Ketcher distributions\n^^^^^^^^^^^^^^^^^^^^^\n\n"
        f"`Ketcher {v} standalone <{SITE}/downloads/ketcher/ketcher-v{v}/ketcher-standalone-{v}.zip>`__\n\n"
        f"`Ketcher {v} remote <{SITE}/downloads/ketcher/ketcher-v{v}/ketcher-remote-{v}.zip>`__\n\n\n"
        "NPM packages\n^^^^^^^^^^^^\n\n"
        f"{npm}\n\n\n"
        "Source code\n^^^^^^^^^^^\n\n"
        f"`Source code on GitHub <https://github.com/{GH_REPO}/releases/tag/v{v}>`__\n"
    )


def render_news_entry(rel: Release) -> str:
    v = rel.version
    sub = "ketcher_" + v.replace(".", "_")
    title = f"Ketcher {v} released"
    return (
        f"{title}\n{'-' * len(title)}\n\n"
        f"*{fmt_date(rel.date)}*\n\n"
        f"We are glad to announce that a new stable version of Ketcher {v} is released.\n\n"
        f"* |{sub}_notes|\n\n"
        f"* |{sub}_downloads|\n\n"
        f".. |{sub}_notes| raw:: html\n\n"
        f"   <a href=\"ketcher/release-notes/ketcher-{v}.html\" target=\"_blank\">Release Notes</a>\n\n"
        f".. |{sub}_downloads| raw:: html\n\n"
        f"   <a href=\"download/ketcher.html\" target=\"_blank\">Downloads</a>\n\n"
    )


# ---------------------------------------------------------------- patchers

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")  # 'utf-8' keeps a BOM as


def update_download_index(text: str, versions: list[str]) -> str:
    entry = re.compile(r"^([ \t]+)ketcher/ketcher-(\d+\.\d+\.\d+)\.rst$", re.M)
    latest_m = entry.search(text)
    if not latest_m:
        raise SystemExit(f"{DOWNLOAD_INDEX}: cannot find the Latest release toctree entry")
    indent, old_latest = latest_m.group(1), latest_m.group(2)
    new_latest = max(versions + [old_latest], key=vkey)
    text = text[:latest_m.start(2)] + new_latest + text[latest_m.end(2):]
    older = sorted({old_latest, *versions} - {new_latest}, key=vkey, reverse=True)
    # first entry after the "Older releases" heading
    older_pos = text.index("Older releases")
    first_older = entry.search(text, older_pos)
    if not first_older:
        raise SystemExit(f"{DOWNLOAD_INDEX}: cannot find the Older releases toctree")
    block = "".join(f"{indent}ketcher/ketcher-{v}.rst\n" for v in older)
    return text[:first_older.start()] + block + text[first_older.start():]


def update_release_notes_index(text: str, versions: list[str]) -> str:
    entries = list(re.finditer(r"^([ \t]+)ketcher-[\w.]+\n", text, re.M))
    if not entries:
        raise SystemExit(f"{NOTES_INDEX}: cannot find toctree entries")
    last = entries[-1]
    indent = last.group(1)
    block = "".join(f"{indent}ketcher-{v}\n" for v in sorted(versions, key=vkey))
    return text[:last.end()] + block + text[last.end():]


def update_demo_page(text: str, version: str) -> str:
    new = re.sub(r"Ketcher \d+\.\d+\.\d+", f"Ketcher {version}", text)
    # keep the title underline at least as long as the title
    lines = new.split("\n")
    title_len = len(lines[0].lstrip("﻿"))
    if len(lines) > 1 and re.fullmatch(r"=+", lines[1]) and len(lines[1]) < title_len:
        lines[1] = "=" * title_len
    return "\n".join(lines)


def update_json_ld(text: str, version: str) -> str:
    new, n = re.subn(r'("softwareVersion":\s*")[^"]*(")', rf"\g<1>{version}\g<2>", text)
    if n != 1:
        raise SystemExit(f"{JSON_LD}: expected exactly one softwareVersion, found {n}")
    return new


NEWS_HEADER_RE = re.compile(r"^(?P<title>[^\n]+)\n-{3,}\n\n\*(?P<date>\d{1,2} \w+ \d{4})\*\n", re.M)


def parse_news_date(s: str) -> dt.date:
    d, m, y = s.split()
    return dt.date(int(y), MONTHS.index(m) + 1, int(d))


def insert_newsfeed_entries(text: str, releases: list[Release]) -> tuple[str, list[str]]:
    placements = []
    for rel in sorted(releases, key=lambda r: vkey(r.version)):
        entry = render_news_entry(rel)
        pos = None
        before = None
        for m in NEWS_HEADER_RE.finditer(text):
            if parse_news_date(m.group("date")) <= rel.date:
                pos, before = m.start(), m.group("title")
                break
        if pos is None:  # older than everything: append at the end
            text = text.rstrip("\n") + "\n\n" + entry
            placements.append(f"Ketcher {rel.version} ({fmt_date(rel.date)}) -> end of newsfeed")
        else:
            text = text[:pos] + entry + text[pos:]
            placements.append(f"Ketcher {rel.version} ({fmt_date(rel.date)}) -> before '{before}'")
    return text, placements


# ---------------------------------------------------------------- checks

def url_ok(url: str) -> bool:
    headers = {"User-Agent": "lifescience-portal-release-script"}
    for method in ("HEAD", "GET"):  # some hosts reject HEAD
        try:
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status == 200
        except urllib.error.HTTPError as e:
            if e.code not in (403, 405):
                return False
        except Exception:
            return False
    return False


def check_links(v: str) -> None:
    urls = [f"{SITE}/downloads/ketcher/ketcher-v{v}/ketcher-{k}-{v}.zip" for k in ("standalone", "remote")]
    urls += [f"https://registry.npmjs.org/{p}/{v}" for p in NPM_PACKAGES]
    for u in urls:
        if not url_ok(u):
            warn(f"{v}: not reachable (yet?): {u}")


# ---------------------------------------------------------------- main

def join_versions(vs: list[str]) -> str:
    tagged = [f"v{v}" for v in vs]
    return tagged[0] if len(tagged) == 1 else ", ".join(tagged[:-1]) + " and " + tagged[-1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--versions", nargs="+", help="explicit versions (default: all pending x.y.0 releases)")
    ap.add_argument("--include-patches", action="store_true", help="include x.y.N (N>0) releases when auto-detecting")
    ap.add_argument("--dry-run", action="store_true", help="show what would change, write nothing")
    ap.add_argument("--skip-link-check", action="store_true", help="do not probe download/npm URLs")
    ap.add_argument("--repo-root", default=".", help="portal repository root (default: cwd)")
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    if not (root / NEWSFEED).exists():
        print(f"error: {root} does not look like the lifescience portal repo", file=sys.stderr)
        return 2

    if args.versions:
        versions = sorted({v.lstrip("v") for v in args.versions}, key=vkey)
        bad = [v for v in versions if not is_plain_version(v)]
        if bad:
            print(f"error: not X.Y.Z versions: {bad}", file=sys.stderr)
            return 2
    else:
        versions = pending_versions(root, args.include_patches)
    if not versions:
        print("Nothing to do: the portal already has every published Ketcher release.")
        return 0

    for v in versions:
        for p in (root / NOTES_DIR / f"ketcher-{v}.md", root / DOWNLOAD_DIR / f"ketcher-{v}.rst"):
            if p.exists():
                print(f"error: {p.relative_to(root)} already exists; drop {v} from --versions", file=sys.stderr)
                return 2

    print(f"Versions: {', '.join(versions)}")
    releases = [fetch_release(v) for v in versions]
    newest = max(versions, key=vkey)

    outputs: dict[str, str] = {}
    for rel in releases:
        outputs[f"{NOTES_DIR}/ketcher-{rel.version}.md"] = render_notes_md(rel)
        outputs[f"{DOWNLOAD_DIR}/ketcher-{rel.version}.rst"] = render_download_rst(rel.version)
    outputs[DOWNLOAD_INDEX] = update_download_index(read(root / DOWNLOAD_INDEX), versions)
    outputs[NOTES_INDEX] = update_release_notes_index(read(root / NOTES_INDEX), versions)

    published = published_versions(root)
    if published and vkey(newest) < vkey(published[-1]):
        warn(f"{newest} is older than the portal's latest {published[-1]}; demo pages and JSON-LD left unchanged")
    else:
        for page in DEMO_PAGES:
            outputs[page] = update_demo_page(read(root / page), newest)
        outputs[JSON_LD] = update_json_ld(read(root / JSON_LD), newest)
    outputs[NEWSFEED], placements = insert_newsfeed_entries(read(root / NEWSFEED), releases)

    if not args.skip_link_check:
        for v in versions:
            check_links(v)

    print("\nNewsfeed placement:")
    for p in placements:
        print(f"  {p}")
    print("\nFiles:")
    for rel_path, content in outputs.items():
        path = root / rel_path
        status = "new" if not path.exists() else "modified"
        print(f"  {status:8} {rel_path}")
        if not args.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    short = [re.sub(r"\.0$", "", v) for v in versions]
    # long backlogs collapse to a range: ketcher-3.13-3.21-release-notes
    span = short if len(short) <= 3 else [short[0], short[-1]]
    branch = "ketcher-" + "-".join(span) + "-release-notes"
    print(f"\nSuggested branch: git checkout -b {branch} master")
    print(f"Suggested commit/PR title: Add release notes for Ketcher {join_versions(versions)}")
    if warnings:
        print(f"\n{len(warnings)} warning(s) - review before committing:")
        for w in warnings:
            print(f"  - {w}")
    if args.dry_run:
        print("\n(dry run: nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
