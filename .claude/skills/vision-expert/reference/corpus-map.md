# Vision corpus map

The corpus lives at `corpus/` in the vision repo, built from the frozen HTML docs in `docs/original/`.
It is indexed in a machine-local qmd 2.5.3 collection named `vision`.
All units share `ingested: "2026-09-22"` in frontmatter - that is the as-of date for the whole corpus snapshot.

## Families and counts

Counts below are unit files (`*.md`), computed with `find corpus/<family> -name '*.md' | wc -l` against the corpus as of this build.

| Family            | Holds                                                    | Count |
|-------------------|-----------------------------------------------------------|------:|
| `corpus/feeds/`   | `pma_*` data-feed upload-format docs (fields, types)     |    86 |
| `corpus/reports/` | Report docs                                              |   408 |
| `corpus/status/`  | Status docs (the other `pma_*` data-feed family)         |     9 |
| `corpus/classes/` | `cl*` class docs (hierarchy, superclasses, properties)   |   210 |
| `corpus/messages/`| `m*` message docs, one per anchor, plus `mXRef`          |  3272 |
| `corpus/general/` | Everything else                                          |   984 |
| **Total**         |                                                           |  4969 |

`corpus/learnings/` does not exist yet in this snapshot; it is added by a later build task for promoted, human-reviewed learnings.

## Provenance and name mapping

Every unit's frontmatter carries:

- `provenance` - the original HTML source path under `docs/original/`, with the real (underscore) name, for example `"docs/original/pma_AnalystEst.htm"`.
  For message units the anchor is included, for example `"docs/original/mDate.htm#asQuarterEnd"`.
- `title` - the real Vision name as documented, for example `"Vision Upload Format: AnalystEst"`.
- `unit_type` - one of `feed`, `report`, `status`, `class`, `message`, `general`.
- `ingested` - the corpus build date, `"2026-09-22"`.

qmd corpus paths are qmd-native and never use underscores.
The source `pma_AnalystEst.htm` is indexed at `corpus/feeds/pma-AnalystEst.md` (dash).
When answering, always use the real underscore name from `title`/`provenance` (`pma_AnalystEst`) and cite the dash path (`corpus/feeds/pma-AnalystEst.md`) as the corpus location.
Never merge the two, and never present the dash form as the Vision name.

## Shred convention

Large docs are chunked so no single retrieval hit is unreadably long:

- First chunk: `<family>/<stem>.md` (e.g. `corpus/feeds/pma-AnalystEst.md`).
- Overflow chunks: `<family>/<stem>/<n>.md` (e.g. `corpus/feeds/pma-AnalystEst/3.md`, `corpus/general/invHolding/2.md`).

A single logical doc can therefore span multiple corpus files.
When a retrieval hit lands on an overflow chunk, check for a sibling first-chunk file at `<family>/<stem>.md` for the frontmatter (`provenance`, `title`, field tables).
Overflow chunks may not repeat it.

## Messages family layout

`corpus/messages/` is grouped by receiving class directory, one unit per message anchor:

- `corpus/messages/mDate/asQuarterEnd.md`, `corpus/messages/mNumber/quarterEnds.md`, etc. - one file per message, named after the message.
- `corpus/messages/mXRef/` - the message cross-reference index, chunked as `A-1.md`, `A-2.md`, `B-1.md`, etc. rather than by message name.
