#!/bin/bash
set -euo pipefail
oa_root="$(cd "$(dirname "$0")" && pwd)"
source "$oa_root/scripts/open_access_env.sh"
exec "$oa_python" -u "$oa_repo/scripts/collect_open_access.py" \
  "${oa_auth_args[@]}" --chapter all --max-records 50000 --minutes 1440 "$@"
