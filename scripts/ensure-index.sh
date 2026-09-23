#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Capture first: piping into `grep -q` EPIPEs qmd when grep exits early, and pipefail then re-adds.
LIST="$(qmd collection list 2>/dev/null || true)"
grep -qw vision <<<"$LIST" || qmd collection add "$ROOT/corpus" --name vision
qmd update
qmd embed
