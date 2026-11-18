---
name: ketcher-release
description: Use when a new Ketcher version is published on GitHub (epam/ketcher) and the lifescience portal needs its release notes, download page, demo pages, JSON-LD and newsfeed updated, or when asked to add, publish or backfill Ketcher release notes on the portal.
---

# Ketcher release → portal

## Overview

Each run adds 2 new files per Ketcher version and edits 6 shared files once. The changes are mechanical, so `scripts/ketcher_release.py` makes them, using the GitHub release (`gh release view`) as the only source of truth. Your part: choose the versions, review what it generates, and open the PR.

## What the script touches (per version X.Y.Z)

| File | Change |
|---|---|
| `rst/ketcher/release-notes/ketcher-X.Y.Z.md` | **new**: the GitHub release body, with a `# Ketcher X.Y.Z` heading, `-` bullets and `#NNNN` turned into issue links |
| `rst/download/ketcher/ketcher-X.Y.Z.rst` | **new**: links to the standalone/remote zips, 4 npm packages and the GitHub tag |
| `rst/download/ketcher.rst` | "Latest release" set to the newest version; the old latest and other new versions go to the top of "Older releases" |
| `rst/ketcher/release-notes/index.rst` | toctree entries added at the end, oldest first |
| `rst/ketcher/demo/ketcher_{remote,standalone}.rst` | version bumped to the newest (UTF-8 BOM kept) |
| `rst/themes/lifescience-theme/json-ld_ketcher.html` | `softwareVersion` set to the newest |
| `rst/newsfeed.rst` | one "Ketcher X.Y.Z released" entry each, **placed by date** among the Indigo entries |

The news date comes from the release **name** ("Ketcher 3.10.0 February 27, 2026"), not from `publishedAt`. Releases are often published in batches days after the date in their name. When dates tie, newer Ketcher versions go above older ones, and Ketcher goes above an Indigo entry from the same day.

## Workflow

Run all commands from the repo root. The script path is `.claude/skills/ketcher-release/scripts/ketcher_release.py`, and it always runs through `python3`.

1. **Start clean.** Run `git status` (it must be clean), then `git checkout master && git pull`.
2. **Preview.** Run `python3 .claude/skills/ketcher-release/scripts/ketcher_release.py --dry-run`. It lists the pending versions (every non-prerelease `x.y.0` newer than the portal's latest), where each news entry will go, and any warnings. The dry run performs the same release-body and link checks as a real run, so whatever warnings it shows are the ones you'll handle in step 4. `--skip-link-check` turns off the URL checks, for when you're offline. Show the version list to the user.
   - Patch releases (`x.y.N`, N>0) are left out because the portal hasn't published them since 3.0. Include them only if the user asks: use `--include-patches` or name them in `--versions`.
   - To backfill or pick specific versions, use `--versions 3.14.0 3.15.0`.
3. **Branch and generate.** Run the `git checkout -b … master` command the dry run printed. Branch names look like `ketcher-3.13-3.14-release-notes`, or a range such as `ketcher-3.13-3.21-release-notes` when there are more than 3 versions. Then run the script again without `--dry-run`, using the same arguments.
4. **Act on every warning:**
   - *No Indigo / "Additional notes" line*: ask the user whether to add one. Don't make up an Indigo version.
   - *Unusual section heading* or *no #NNNN references*: open the generated `.md` and check that the Markdown structure (headings and lists) is intact. The actual rendering is checked later by the PR's CI build.
   - *Date taken from publishedAt*: confirm the date with the user.
   - *Link not reachable*: the zips or npm packages aren't up yet. Tell the user before opening the PR, because the download page will 404 until they are.
5. **Review** `git diff --stat`: 2 new files per version plus the 6 shared files. Read through `rst/newsfeed.rst` near each inserted entry. Leave the upstream wording of the release notes alone: the portal mirrors GitHub, so typos get fixed upstream. If the notes cite an Indigo version newer than the portal's latest (`ls rst/indigo/release-notes`), keep the reference as it is and say in the PR body that the Indigo pages will follow.
6. **Commit and PR.** Commit and open the PR with the suggested title, e.g. `Add release notes for Ketcher v3.13.0, v3.14.0 and v3.15.0`. Then push with `git push -u origin <branch>` and run `gh pr create --base master`. The PR body lists the versions with their dates and any warnings you resolved. The `Build portal` GitHub Action then builds the site; local Sphinx isn't installed, and `sh build.sh` needs Docker.

## When the script refuses

- **"already exists"**: that version is already on the portal. Remove it from `--versions`.
- **"Nothing to do"**: the portal is up to date. Check `gh release list -R epam/ketcher` if the user expected a release; it may still be a pre-release or a draft.
- **A version older than the portal's latest**: the script leaves the demo pages and JSON-LD unchanged and warns about it. This is the expected result for a backfill.

## Out of scope

- Uploading the zips to `lifescience.opensource.epam.com/downloads/ketcher/`.
- Redeploying `/KetcherDemo` and `/KetcherDemoSA`.

Both are infrastructure steps outside this repo. Mention them in the PR if the link check warned.
