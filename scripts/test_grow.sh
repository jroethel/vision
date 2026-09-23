#!/usr/bin/env bash
set -euo pipefail
Q=learnings-queue
KW="ZZQMDGROWPROOF"
# Clean up test artifacts no matter where the script exits (an assertion under set -e aborts
# before the final cleanup step otherwise, leaving proof files that Step 5's commit could sweep in).
trap 'rm -f "$Q/proof-reviewed.md" "$Q/proof-unreviewed.md" corpus/learnings/proof-reviewed.md' EXIT

# 1. A reviewed candidate and an unreviewed candidate both sit in the queue.
cat > "$Q/proof-reviewed.md" <<EOF
---
type: learning
verified_against: software/testtools/ivr/order.ivr
verified_on: 2026-09-21
role_tier: engineer
---
Verified learning containing the token $KW for retrieval.
EOF
cat > "$Q/proof-unreviewed.md" <<EOF
---
type: learning
verified_against: software/testtools/ivr/order.ivr
verified_on: 2026-09-21
role_tier: engineer
---
Unreviewed candidate also containing $KW; must NOT be retrievable.
EOF

# 2. Before promotion, nothing with the token is retrievable (queue is not indexed).
#    Capture search output before grepping: `qmd ... | grep -q` under pipefail can EPIPE qmd and
#    flip the result. --full-path makes hits real paths (corpus/...) instead of qmd:// URIs.
bash scripts/index.sh >/dev/null
HITS="$(qmd search "$KW" -c vision -n 5 --full-path)"
if grep -q "$KW" <<<"$HITS"; then
  echo "FAIL: unreviewed queue content is retrievable"; exit 1
fi

# 3. Promote only the reviewed one (--assume-yes is the documented test/CI-only override for the
#    interactive gate); it becomes retrievable.
python3 scripts/promote_learning.py "$Q/proof-reviewed.md" --assume-yes
HITS="$(qmd search "$KW" -c vision -n 5 --full-path)"
if ! grep -q "corpus/learnings" <<<"$HITS"; then
  echo "FAIL: promoted learning not retrievable"; exit 1
fi

# 4. The unreviewed one is still not retrievable and still in the queue.
test -f "$Q/proof-unreviewed.md" || { echo "FAIL: unreviewed entry vanished"; exit 1; }

# 5. Happy-path cleanup, then re-index so the index does not reference the removed proof learning.
#    (The EXIT trap is the failure-path safety net; its rm -f is idempotent if we already cleaned.)
rm -f "$Q/proof-unreviewed.md" corpus/learnings/proof-reviewed.md
bash scripts/index.sh >/dev/null
echo "grow loop OK: reviewed promoted+retrievable, unreviewed never retrievable"
