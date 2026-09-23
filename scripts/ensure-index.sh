#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
qmd collection list 2>/dev/null | grep -qw vision || qmd collection add "$ROOT/corpus" --name vision
qmd update
qmd embed
