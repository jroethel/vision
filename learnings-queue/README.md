# Learnings queue

Candidate learnings wait here for human review before promotion into the corpus.
This directory is never part of the qmd `vision` collection because it lives outside `corpus/`, so unreviewed candidates are never retrievable.
Only promoted learnings under `corpus/learnings/` are indexed and retrievable.

## Candidate format

A candidate is a markdown file in this directory with a `---`-delimited frontmatter block:

- `type: learning` - marks the file as a learning candidate.
- `verified_against` - a live-source `path:line` pointer under `application/localvision/bootstrap/protocol/originals/` or `software/src/`, or an `ivr:<file>` pointer, that the learning was checked against.
- `verified_on` - the date the check was performed.
- `role_tier` - one of `engineer`, `architect`, or `sysadmin` (see the trust tiers below).
- `supersedes` - optional, a `docs/original/...#anchor` pointer to frozen-doc content the learning corrects.

The body after the frontmatter is the learning text.

## Promotion checklist

A candidate is promoted only when all four hold:

1. `verified_against` is present and points at a real live-source location.
2. `role_tier` is set to one of the three tiers.
3. A human reviews the rendered learning and confirms interactively at the terminal.
4. `scripts/promote_learning.py` does the move into `corpus/learnings/` and runs `qmd update` so the learning becomes retrievable.

Run promotion as:

```bash
python3 scripts/promote_learning.py learnings-queue/<candidate>.md
```

The script prints the candidate, then requires a y/N answer read from a TTY.
It fails closed on any non-interactive stdin (piped input, agent invocation), so the automation that drafted a candidate cannot promote it.

## `--assume-yes` is test/CI only

`--assume-yes` skips the interactive confirmation and exists solely for the automated grow test (`scripts/test_grow.sh`) and CI.
Never use it for a real promotion; it bypasses the human gate that the whole loop exists to enforce.
Key validation is never skipped: a candidate missing `verified_against` or `role_tier`, or carrying an invalid tier, is refused even under `--assume-yes`.

## Trust tiers

Promoted learnings carry their `role_tier` into the corpus, and the tier governs how a learning is presented (see `reference/roles.md` in the vision-expert skill):

- `engineer` - usable directly, the underlying check is cheap to repeat.
- `architect` - advisory only, and any schema change it informs is DBA-gated.
- `sysadmin` - lowest trust, the corpus has the weakest anchor for operational claims.
