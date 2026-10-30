#!/usr/bin/env python3
"""Commit a snapshot of the knowledge base and refresh every frozen copy of it.

The KB is read in three places that each hold a snapshot:

  explorer   export/stroke-aphasia-kb.json (approved findings) and
             export/stroke-aphasia-kb-drafts.json (approved + unreviewed drafts),
             the two versions the explorer's "Findings" switch shows; GitHub Pages
             regenerates both on every push, so pushing is what publishes them;
  webapp     the CALMaR webapp (neurodesk/webapps, apps/calmar) ships the same two
             exports as assets (aphasia-kb, aphasia-kb-drafts) through its
             scripts/sync_kb.py --both; the report offers both under
             "Knowledge-base evidence";
  notebook   the calmar repository pins this KB as its stroke-aphasia-kb/
             submodule; the notebook reads the files at that commit and chooses
             approved-only or approved + drafts with its `evidence` setting, so
             refreshing it means moving the submodule to this KB's HEAD.

Run it whenever you want the copies to catch up with the KB — it is never run
for you. It first commits the KB's own changes (entries, drafts, logs, register;
so every copy records a commit, not a dirty tree), then writes and commits the
explorer exports, the webapp assets (on the webapp's current branch, never on
main) and the calmar submodule pointer. Nothing is pushed: push the KB first,
then calmar and the webapp branch. --no-commit writes the copies and commits
nothing, to look before you snapshot.

    python scripts/snapshot.py                     # commit + refresh all three
    python scripts/snapshot.py --no-commit         # refresh only, commit nothing
    python scripts/snapshot.py --only explorer     # just the two explorer exports
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB = ROOT.parent
DRAFT_STATUSES = "approved,in_review,draft"
# What the KB's own commit sweeps in (everything else stays as it is).
KB_CONTENT = ["regions", "impairments", "therapies", "predictors", "reviews", "ingredients", "drafts",
              "citations.md", "logs", "screening", "atlas_mapping"]
TARGETS = ("explorer", "webapp", "notebook")


def run(cmd, cwd, check=True, quiet=False) -> subprocess.CompletedProcess:
    if not quiet:
        print("$ " + " ".join(str(c) for c in cmd) + (f"   (in {cwd})" if Path(cwd) != ROOT else ""))
    done = subprocess.run([str(c) for c in cmd], cwd=str(cwd), text=True, capture_output=quiet)
    if check and done.returncode:
        raise SystemExit(f"failed ({done.returncode}): {' '.join(str(c) for c in cmd)}"
                         + (f"\n{done.stderr}" if quiet and done.stderr else ""))
    return done


def git(repo, *args, check=True) -> str:
    return run(["git", "-C", repo, *args], cwd=repo, check=check, quiet=True).stdout.strip()


def commit(repo: Path, paths: list[str], message: str) -> str | None:
    """Stage `paths` and commit them if anything changed; returns the short hash or None."""
    existing = [p for p in paths if (repo / p).exists() or git(repo, "ls-files", "--", p, check=False)]
    if not existing:
        return None
    git(repo, "add", "-A", "--", *existing)
    if not git(repo, "diff", "--cached", "--name-only", "--", *existing):
        return None
    run(["git", "-C", repo, "commit", "-q", "-m", message, "--", *existing], cwd=repo)
    return git(repo, "rev-parse", "--short", "HEAD")


def counts(path: Path) -> str:
    v = json.loads(path.read_text(encoding="utf-8"))["version"]
    return f"{v['findings']} findings from {v['papers']} papers"


def refresh_kb_commit(args) -> None:
    dirty = git(ROOT, "status", "--porcelain", "--", *[p for p in KB_CONTENT if (ROOT / p).exists()])
    if not dirty:
        print("KB: no uncommitted changes in the entries, drafts, logs or register")
        return
    n = len(dirty.splitlines())
    if not args.commit:
        print(f"KB: {n} uncommitted file(s) — the snapshots will record a dirty tree (run without --no-commit to commit them first)")
        return
    h = commit(ROOT, KB_CONTENT, f"KB snapshot {date.today().isoformat()}: extraction, backfill and review results ({n} files)")
    print(f"KB: committed {n} file(s) as {h}")


def refresh_explorer(args) -> None:
    out = ROOT / "export"
    run([sys.executable, ROOT / "scripts" / "export_webapp.py", "--out", out / "stroke-aphasia-kb.json",
         "--fixtures", out, "--indent", "1"], cwd=ROOT)
    run([sys.executable, ROOT / "scripts" / "export_webapp.py", "--include", DRAFT_STATUSES,
         "--out", out / "stroke-aphasia-kb-drafts.json"], cwd=ROOT)
    print(f"explorer: approved {counts(out / 'stroke-aphasia-kb.json')} · "
          f"with drafts {counts(out / 'stroke-aphasia-kb-drafts.json')}")
    if args.commit:
        h = commit(ROOT, ["export"], f"Explorer exports {date.today().isoformat()}: approved and approved + drafts")
        print(f"explorer: {'committed ' + h if h else 'exports unchanged'}")


def refresh_webapp(args) -> None:
    app = Path(args.webapp).expanduser().resolve()
    sync = app / "scripts" / "sync_kb.py"
    if not sync.is_file():
        print(f"webapp: {sync} not found — skipped (pass --webapp <webapps>/apps/calmar)")
        return
    if "--both" not in sync.read_text(encoding="utf-8"):
        print(f"webapp: {sync} predates the two-version sync (--both) — check out the branch that has it; skipped")
        return
    repo = Path(git(app, "rev-parse", "--show-toplevel"))
    cmd = [sys.executable, sync, "--kb", ROOT, "--both"]
    if git(ROOT, "status", "--porcelain"):
        cmd.append("--allow-dirty")
    run(cmd, cwd=app)
    if args.commit:
        branch = git(repo, "branch", "--show-current")
        if branch in ("main", "master", ""):
            print(f"webapp: on {branch or 'a detached HEAD'} — not committing there; create a branch and commit "
                  "the assets and manifests yourself")
            return
        rel = app.relative_to(repo)
        paths = [f"{rel}/web/models/annotations/aphasia-kb.json", f"{rel}/web/models/annotations/aphasia-kb-drafts.json",
                 f"{rel}/tests/fixtures/kb-parity", f"{rel}/web/models/manifest.json", "packages/calmar/model.manifest.json"]
        kb_head = git(ROOT, "rev-parse", "--short", "HEAD")
        h = commit(repo, paths, f"calmar: knowledge base {kb_head} (approved and approved + drafts)")
        print(f"webapp: {'committed ' + h + ' on ' + branch if h else 'assets unchanged'}")


def refresh_notebook(args) -> None:
    calmar = Path(args.calmar).expanduser().resolve()
    sub = calmar / "stroke-aphasia-kb"
    if not (sub / ".git").exists():
        print(f"notebook: {sub} is not a checked-out submodule — skipped (git -C {calmar} submodule update --init)")
        return
    if git(sub, "status", "--porcelain", "--untracked-files=no"):
        print(f"notebook: {sub} has local edits — not moving it; the KB is edited only in {ROOT}")
        return
    head = git(ROOT, "rev-parse", "HEAD")
    if git(sub, "rev-parse", "HEAD") == head:
        print(f"notebook: calmar already pins {head[:7]}")
        return
    git(sub, "fetch", "-q", str(ROOT), "HEAD")
    git(sub, "checkout", "-q", "--detach", head)
    print(f"notebook: calmar's stroke-aphasia-kb/ now at {head[:7]} (the notebook's evidence setting picks approved or all)")
    if git(ROOT, "status", "--porcelain"):
        print("notebook: note — uncommitted KB changes are not in the submodule (run without --no-commit to include them)")
    if args.commit:
        h = commit(calmar, ["stroke-aphasia-kb"], f"stroke-aphasia-kb → {head[:7]}")
        print(f"notebook: {'committed ' + h + ' in calmar' if h else 'pointer unchanged'}")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__.split("\n\n", 1)[1])
    p.add_argument("--no-commit", dest="commit", action="store_false",
                   help="write the copies but commit nothing (default: commit the KB, then each copy; never pushes)")
    p.add_argument("--only", nargs="+", choices=TARGETS, help="refresh only these (default: all three)")
    p.add_argument("--webapp", default=str(GITHUB / "webapps" / "apps" / "calmar"), help="the webapp's apps/calmar folder")
    p.add_argument("--calmar", default=str(GITHUB / "calmar"), help="the calmar repository (holds the submodule)")
    args = p.parse_args(argv)
    targets = args.only or TARGETS
    refresh_kb_commit(args)
    if "explorer" in targets:
        refresh_explorer(args)
    if "webapp" in targets:
        refresh_webapp(args)
    if "notebook" in targets:
        refresh_notebook(args)
    if args.commit:
        print("\nNothing pushed. Push the KB first (the others point at its commits), then calmar and the webapp branch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
