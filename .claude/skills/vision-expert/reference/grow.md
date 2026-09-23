# Grow: session-end learning capture

Run this protocol at the end of any vision-expert session that surfaced knowledge the corpus lacked or got wrong.
The goal is to make the knowledge base grow from real question-answering, without letting unverified output leak into the corpus.

## What becomes a candidate

Distill only evidence-backed learnings into `learnings-queue/`, one markdown file per candidate.
Every candidate must carry a `verified_against` pointer to the live source that backs it: a `path:line` under `application/localvision/bootstrap/protocol/originals/` or `software/src/`, or an `ivr:<file>` pointer.
A learning you checked against live source this session qualifies; a retrieval-only inference does not, no matter how plausible (see `reference/ground-truth.md`).
Set `verified_on` to the date of the check, `role_tier` to the tier that matches the claim (see `reference/roles.md`), and `supersedes` when the learning corrects specific frozen-doc content.
The candidate format and the promotion checklist are documented in `learnings-queue/README.md`.

## Never write to the corpus directly

New learnings go to `learnings-queue/` only, never straight into `corpus/`.
The queue sits outside `corpus/` and is therefore never in the qmd `vision` collection, so an unreviewed candidate is never retrievable by retrieval.
Only promotion moves a learning into `corpus/learnings/` and makes it retrievable.

## Promotion is human-gated

Promotion runs only through `scripts/promote_learning.py`, which prints the candidate and requires an interactive y/N confirmation read from a TTY.
The gate fails closed on non-interactive stdin, so you (the session that drafted the candidate) cannot promote it yourself; a human reviews the rendered learning and confirms at the terminal.
`--assume-yes` is a test/CI-only override documented in `learnings-queue/README.md`; never use it for a real promotion.

## How promoted learnings are presented

A promoted learning keeps its `role_tier`, and the tiers in `reference/roles.md` govern how much weight it gets in an answer:

- `engineer` - usable directly, the recheck is cheap.
- `architect` - advisory, and any schema change it informs stays DBA-gated.
- `sysadmin` - lowest trust, present with explicit caution since the corpus has the weakest anchor for operational claims.

Cite a promoted learning by its `corpus/learnings/<slug>.md` path and name its tier when it carries weight in a recommendation.
