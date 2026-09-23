#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
qmd collection remove vision 2>/dev/null || true
qmd collection add "$ROOT/corpus" --name vision
qmd update
qmd embed
qmd collection show vision
