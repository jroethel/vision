---
name: vision-expert
description: Answers questions about the Vision DBMS data model - pma_ data feeds and their fields, entity classes and superclasses, class messages such as createSubclass:at:, and the Vision schema generally. Use for any question naming a Vision feed (pma_*), a feed field, a class (cl*), a superclass relationship, a message send, or "what does the Vision data model/schema look like".
---

# Vision expert

Retrieval-grounded answers over the Vision markdown knowledge base at `corpus/`, built from the frozen HTML docs in `docs/original/`.
The corpus is indexed in a machine-local qmd 2.5.3 collection named `vision`.

## Corpus map

- `corpus/feeds/` - the `pma_*` data-feed docs (upload format, fields, types).
- `corpus/reports/` - report docs.
- `corpus/status/` - status docs.
- `corpus/classes/` - `cl*` class docs (hierarchy, superclasses, properties).
- `corpus/messages/` - `m*` message docs, one unit per message anchor, grouped by class directory (for example `messages/mDate/asQuarterEnd.md`), plus `messages/mXRef`.
- `corpus/general/` - everything else.
- `corpus/learnings/` - promoted, human-reviewed learnings (added by a later build task, may not exist yet).

Large docs are shredded: the first chunk lives at `<family>/<stem>.md`, overflow chunks at `<family>/<stem>/<n>.md`.

**Name mapping (important):** qmd corpus paths are qmd-native and never use underscores, so the source `pma_AnalystEst.htm` is indexed at `corpus/feeds/pma-AnalystEst.md` (dash, not underscore).
The real Vision name is preserved in each unit's frontmatter as `title` and `provenance` (for example `provenance: "docs/original/pma_AnalystEst.htm"`).
Always answer with the real name (`pma_AnalystEst`) and cite the on-disk path (`corpus/feeds/pma-AnalystEst.md`) - never invent an underscore path, and never rename the real feed to match the path.

See `reference/corpus-map.md` for the fuller map: family counts, provenance scheme, and the `ingested` as-of date.

## Retrieval protocol

1. Query the `vision` collection, never grep or read `docs/original/` HTML directly:
   - `qmd query -c vision "<question>"` for hybrid search (recommended default).
   - `qmd search -c vision "<question>"` for plain full-text BM25.
   - Add `--full-path` to get real on-disk paths instead of `qmd://` + docid.
2. Fetch the full unit with `qmd get <path or docid>`, or read the hit's `--full-path` file directly.
3. If a query over `vision` returns nothing, run `scripts/ensure-index.sh` once (the machine-local index may be absent or stale) before concluding the corpus lacks the answer.

See `reference/retrieval.md` for structured `intent:/lex:/vec:/hyde:` query craft and worked examples.

## Heavy-sweep rule

Any multi-file sweep (scanning many corpus units, e.g. "list every feed with a Date field") runs in a subagent, so the verbose reads never fill the main context window.

## Ground-truth rule

Every schema or feed claim pulled from the corpus is **unverified-as-of-retrieval**.
Before committing any feed or schema change based on a corpus claim, recheck it against live source (`software/src/`) or the ivr testkit (`software/testtools/ivr/`).
See `reference/ground-truth.md` for the concrete recheck loop, and `reference/roles.md` for who is trusted to act on which kind of claim.
