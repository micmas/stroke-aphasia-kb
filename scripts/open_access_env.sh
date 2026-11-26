#!/bin/bash
# Shared local launcher setup. Credentials stay with Wrangler or the environment.
oa_repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
oa_common="$(git -C "$oa_repo" rev-parse --path-format=absolute --git-common-dir)"
oa_primary_root="$(dirname "$oa_common")"
oa_python="${STROKE_KB_PYTHON:-}"
if [[ -z "$oa_python" ]]; then
  for oa_candidate in "$oa_repo/.venv/bin/python" "$oa_primary_root/.venv/bin/python"; do
    if [[ -x "$oa_candidate" ]]; then oa_python="$oa_candidate"; break; fi
  done
fi
if [[ -z "$oa_python" ]]; then
  echo 'Set up the project .venv first (see README.md), or set STROKE_KB_PYTHON.' >&2
  exit 1
fi
oa_account="${CLOUDFLARE_ACCOUNT_ID:-}"
if [[ -z "$oa_account" ]]; then
  oa_account="$("$oa_python" -c 'import json,sys; print(json.load(open(sys.argv[1]))["account_id"])' "$oa_repo/deployment/open-access.json")"
fi
oa_auth_args=(--account-id "$oa_account")
if [[ -z "${CLOUDFLARE_API_TOKEN:-}" ]]; then
  oa_wrangler="${STROKE_KB_WRANGLER:-}"
  if [[ -z "$oa_wrangler" ]]; then
    for oa_candidate in "$oa_repo/portal/node_modules/.bin/wrangler" "$oa_primary_root/portal/node_modules/.bin/wrangler"; do
      if [[ -x "$oa_candidate" ]]; then oa_wrangler="$oa_candidate"; break; fi
    done
  fi
  if [[ -z "$oa_wrangler" ]]; then oa_wrangler="$(command -v wrangler || true)"; fi
  if [[ -z "$oa_wrangler" ]]; then
    echo 'Install the portal dependencies (cd portal && npm ci), then sign in with Wrangler.' >&2
    exit 1
  fi
  oa_auth_args+=(--wrangler "$oa_wrangler")
fi
