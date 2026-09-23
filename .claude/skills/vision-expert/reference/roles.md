# Trust tiers by role

Corpus answers are unverified-as-of-retrieval (see `reference/ground-truth.md`).
How much weight to put on an unverified answer, and how much rechecking to insist on before acting, depends on who is asking and what they are asking for.

## Engineer - cheap and code-anchored

An engineer question ("what does this message do", "what type is this field", "which feed sets X") is cheap to verify: the corpus claim is a short hop from a live-source grep or an ivr fixture run.
Answer directly from retrieval, then point at the specific `software/src/` location or ivr fixture that would confirm it.
Treat engineer-facing answers as low-risk to give fast, because the recheck loop in `reference/ground-truth.md` is itself cheap for this kind of question.

## Architect - advisory only

An architect question ("should this class inherit from X", "does this feed design fit the schema", "what's the impact of adding a field") gets an advisory answer, not a directive one.
Schema commits are DBA-only.
A corpus-grounded answer can shape the recommendation, but the answer must say plainly that the actual schema change is out of scope for this skill and belongs to whoever owns the DBA path, after the ground-truth recheck.
Never present an architect-level answer as pre-approved for a schema commit.

## Sysadmin - weakest anchor, parked

A sysadmin question (deployment, process control, environment/ops concerns) has the weakest anchor in this corpus - the corpus documents the data model and feed/class/message schema, not operational runbooks.
Treat sysadmin questions as parked: say what the corpus does and does not cover, do not stretch a schema-doc citation to answer an ops question, and point at `application/production/` or the relevant ops docs instead of guessing from corpus retrieval.
