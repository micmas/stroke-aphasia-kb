#!/usr/bin/env bash
# Move the knowledge base out of calmar/aphasia-kb into this repository with
# its git history, rename aphasia-kb → stroke-aphasia-kb everywhere, and
# replace the folder in calmar with a submodule at stroke-aphasia-kb/.
#
#   tools/migrate-from-calmar.sh [--execute] [--phase kb|calmar|all] [--calmar DIR] [--remote URL]
#
# Dry run by default: prints every step and the files whose text would change.
# --execute performs them. Nothing is pushed by the script. Phase "kb" (steps
# 1–4) builds this repository; you then push it; phase "calmar" (step 5)
# needs the pushed remote because it clones it as a submodule, and lands
# calmar's changes on a new branch (stroke-aphasia-kb-submodule) for review.
#
# Run this only when no one is writing entries in calmar/aphasia-kb — it
# refuses to start if either working tree has uncommitted changes.
#
# What it does
#   1. calmar:  git subtree split --prefix=aphasia-kb → branch kb-history
#   2. here:    merge kb-history (unrelated histories). README.md conflicts by
#               design: the KB's README wins; this repo's assembly README is
#               dropped (its content lives in EXPLORER.md).
#   3. here:    rename the folder name in text: aphasia-kb → stroke-aphasia-kb
#               (python module names aphasia_kb / aphasia_rules are NOT renamed)
#   4. here:    regenerate export/ from the moved entries, run npm test, commit
#   5. calmar:  new branch; git rm -r aphasia-kb; git submodule add <remote>
#               stroke-aphasia-kb; same text rename in calmar's own files;
#               commit. You then run the calmar tests and push both repos.
set -euo pipefail

EXECUTE=0
PHASE=all
CALMAR=""
REMOTE="https://github.com/micmas/stroke-aphasia-kb.git"
while [ $# -gt 0 ]; do
  case "$1" in
    --execute) EXECUTE=1 ;;
    --calmar) CALMAR="$2"; shift ;;
    --phase) PHASE="$2"; shift ;;
    --remote) REMOTE="$2"; shift ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

KB="$(cd "$(dirname "$0")/.." && pwd)"
CALMAR="${CALMAR:-$KB/../calmar}"
CALMAR="$(cd "$CALMAR" && pwd)"
SPLIT_BRANCH=kb-history
CALMAR_BRANCH=stroke-aphasia-kb-submodule

say() { printf '\n\033[1m%s\033[0m\n' "$*"; }
run() { if [ "$EXECUTE" = 1 ]; then echo "+ $*"; "$@"; else echo "  (dry) $*"; fi; }

# Text files whose content mentions the old folder name. The regex leaves an
# existing "stroke-aphasia-kb" alone, so re-running is harmless.
rename_in() {  # rename_in DIR [exclude-prefix...]
  local dir="$1"; shift
  local excludes=(); for e in "$@"; do excludes+=(-not -path "$dir/$e/*"); done
  find "$dir" -type f \( -name '*.md' -o -name '*.py' -o -name '*.txt' -o -name '*.yaml' -o -name '*.yml' \
       -o -name '*.ipynb' -o -name '*.cff' -o -name '*.sh' -o -name '*.json' -o -name '*.js' -o -name '*.cfg' -o -name '*.toml' -o -name '.gitignore' \) \
       -not -path '*/.git/*' -not -path '*/.venv/*' -not -path '*/node_modules/*' -not -path '*/__pycache__/*' "${excludes[@]}" \
       -print0 | xargs -0 grep -l -E '(^|[^-])aphasia-kb' 2>/dev/null || true
}
apply_rename() {  # apply_rename FILE...
  [ $# -eq 0 ] && return 0
  if [ "$EXECUTE" = 1 ]; then
    perl -pi -e 's/(?<!stroke-)aphasia-kb/stroke-aphasia-kb/g' "$@"
  fi
}

say "Preconditions"
echo "  knowledge base repo: $KB"
echo "  calmar repo:         $CALMAR"
echo "  remote for submodule: $REMOTE"
[ -d "$CALMAR/aphasia-kb" ] || { echo "no aphasia-kb/ in $CALMAR" >&2; exit 1; }
[ -d "$CALMAR/.git" ] || { echo "$CALMAR is not a git repository" >&2; exit 1; }
[ -d "$KB/.git" ] || { echo "$KB is not a git repository" >&2; exit 1; }
if [ -n "$(git -C "$CALMAR" status --porcelain)" ]; then
  echo "calmar has uncommitted changes — commit or stash them first (entries being written?)" >&2
  git -C "$CALMAR" status --short | head -20 >&2
  [ "$EXECUTE" = 1 ] && exit 1
fi
if [ -n "$(git -C "$KB" status --porcelain)" ]; then
  echo "$KB has uncommitted changes — commit them first" >&2
  [ "$EXECUTE" = 1 ] && exit 1
fi
if [ "$PHASE" != calmar ] && git -C "$KB" ls-files --error-unmatch schema.md >/dev/null 2>&1; then
  echo "schema.md is already tracked here: the KB seems to have been moved already (use --phase calmar)" >&2
  [ "$EXECUTE" = 1 ] && exit 1
fi
command -v perl >/dev/null || { echo "perl is required for the rename" >&2; exit 1; }

if [ "$PHASE" = kb ] || [ "$PHASE" = all ]; then
say "1. Split aphasia-kb/ out of calmar with its history"
run git -C "$CALMAR" subtree split --prefix=aphasia-kb -b "$SPLIT_BRANCH"
if [ "$EXECUTE" = 1 ]; then
  echo "  $(git -C "$CALMAR" rev-list --count "$SPLIT_BRANCH") commits on $SPLIT_BRANCH"
fi

say "2. Merge that history into this repository"
run git -C "$KB" fetch "$CALMAR" "$SPLIT_BRANCH"
if [ "$EXECUTE" = 1 ]; then
  if ! git -C "$KB" merge --allow-unrelated-histories --no-commit --no-ff FETCH_HEAD; then
    conflicts="$(git -C "$KB" diff --name-only --diff-filter=U)"
    echo "  conflicts: $conflicts"
    for f in $conflicts; do
      case "$f" in
        README.md) git -C "$KB" checkout --theirs -- README.md; git -C "$KB" add README.md; echo "  README.md: kept the KB's";;
        *) echo "unexpected conflict in $f — resolve by hand, then: git commit" >&2; exit 1;;
      esac
    done
  fi
  git -C "$KB" commit -q -m "Move the knowledge base here from calmar/aphasia-kb (history preserved)" \
    -m "git subtree split --prefix=aphasia-kb of micmas/calmar $(git -C "$CALMAR" rev-parse --short HEAD), merged with --allow-unrelated-histories."
else
  echo "  (dry) git merge --allow-unrelated-histories FETCH_HEAD   # README.md: the KB's wins"
fi

say "3. Rename aphasia-kb → stroke-aphasia-kb in this repository's text"
files="$(rename_in "$KB" export)"
echo "$files" | sed 's/^/  /' | grep . || echo "  (none)"
# shellcheck disable=SC2086
apply_rename $files
if [ "$EXECUTE" = 1 ] && [ -n "$files" ]; then
  git -C "$KB" add -A
  git -C "$KB" commit -q -m "Rename aphasia-kb → stroke-aphasia-kb in documentation and scripts"
fi

say "4. Regenerate the export from the moved entries and test the port"
run bash -c "cd '$KB' && python3 export_webapp.py --out export/stroke-aphasia-kb.json --fixtures export --indent 1 && npm test"
if [ "$EXECUTE" = 1 ]; then
  git -C "$KB" add export && git -C "$KB" commit -q -m "Export regenerated from the moved entries" || true
fi

fi  # phase kb

if [ "$PHASE" = calmar ] || [ "$PHASE" = all ]; then
if [ "$EXECUTE" = 1 ]; then
  local_head="$(git -C "$KB" rev-parse HEAD)"
  remote_head="$(git ls-remote "$REMOTE" HEAD 2>/dev/null | cut -f1 || true)"
  if [ "$local_head" != "$remote_head" ]; then
    cat <<MSG

  This repository's HEAD ($local_head) is not what $REMOTE serves.
  Push it first (git -C "$KB" push origin main), then re-run:
    tools/migrate-from-calmar.sh --execute --phase calmar
MSG
    exit 0
  fi
fi
say "5. Replace the folder in calmar with a submodule (on branch $CALMAR_BRANCH)"
run git -C "$CALMAR" checkout -b "$CALMAR_BRANCH"
run git -C "$CALMAR" rm -r -q aphasia-kb
run git -C "$CALMAR" submodule add "$REMOTE" stroke-aphasia-kb
echo "  files in calmar whose text changes:"
cfiles="$(rename_in "$CALMAR" aphasia-kb stroke-aphasia-kb)"
echo "$cfiles" | sed 's/^/    /' | grep . || echo "    (none)"
# shellcheck disable=SC2086
apply_rename $cfiles
if [ "$EXECUTE" = 1 ]; then
  git -C "$CALMAR" add -A
  git -C "$CALMAR" commit -q -m "Knowledge base moved to micmas/stroke-aphasia-kb; consumed as a submodule" \
    -m "aphasia-kb/ → submodule stroke-aphasia-kb/ (its history is in that repository). Path references renamed."
fi

fi  # phase calmar

say "Done"
if [ "$EXECUTE" = 1 ]; then
  cat <<MSG
  Next, by hand:
    cd $KB    && git log --oneline | head -5 && git push origin main
    cd $CALMAR && source .venv/bin/activate && python -m pytest tests -q -x
                  git push -u origin $CALMAR_BRANCH   # then open the pull request
  Clone instructions become: git clone --recurse-submodules https://github.com/micmas/calmar.git
  Branch $SPLIT_BRANCH in calmar can be deleted once the merge is pushed.
MSG
else
  echo "  Dry run only. Re-run with --execute when no entries are being written."
fi
