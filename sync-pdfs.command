#!/bin/bash
set -euo pipefail
oa_root="$(cd "$(dirname "$0")" && pwd)"
source "$oa_root/scripts/open_access_env.sh"
exec "$oa_python" -u "$oa_repo/scripts/sync_open_access.py" \
  "${oa_auth_args[@]}" --repo "${STROKE_KB_WORKING_REPO:-$oa_primary_root}" \
  --chapter all --execute "$@"
