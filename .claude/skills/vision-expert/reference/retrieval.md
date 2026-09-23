# Retrieval craft for the vision corpus

Query the `vision` collection with qmd 2.5.3.
Never read `docs/original/` HTML directly - it is the frozen input, not the source of truth for retrieval.
The corpus in `corpus/` is the source of truth.

## Basic commands

- `qmd query -c vision "<question>"` - hybrid search with auto expansion and reranking.
  Use this by default.
- `qmd search -c vision "<question>"` - plain full-text BM25, no LLM expansion.
  Faster, use when you already know the exact term (a feed name, a message name, a class name).
- `qmd query -c vision --full-path "<question>"` - same as `qmd query`, but prints on-disk paths (`corpus/feeds/pma-AnalystEst.md`) instead of `qmd://` + docid.
  Prefer this when you need to cite a path.
- `qmd get <path or docid>` - fetch a full unit once you have its path or docid from a search hit.
- `qmd multi-get <pattern>` - batch-fetch several units by glob or comma-separated list.
  Patterns are collection-relative, not `corpus/`-relative (for example `messages/mDate/*.md`, not `corpus/messages/mDate/*.md`).

## Structured queries

For sharper recall, use a typed query document instead of a plain string.
Each line is `intent:`, `lex:`, `vec:`, or `hyde:`.
`intent:` is optional context, the rest are the actual query lines.

Field lookup (want the exact feed and field, favor lexical match on the field name):

```
qmd query -c vision $'intent: find the Vision feed that sets a given field\nlex: nextQuarterEnd\nvec: AnalystEst feed nextQuarterEnd field type'
```

Class hierarchy lookup (favor vector/semantic match on the concept):

```
qmd query -c vision $'intent: find a Vision class and its superclass\nlex: clCompany superclass\nvec: Company class hierarchy parent class'
```

Message lookup (message names are exact tokens, so lean lexical):

```
qmd query -c vision $'intent: find what a Vision message does\nlex: createSubclass:at:\nvec: create a subclass of an existing class'
```

Broad/fuzzy question (no exact term in hand, lean hyde):

```
qmd query -c vision $'hyde: The Vision feed that carries analyst estimate data defines a field for the next fiscal quarter end date.'
```

## Freshness fallback

If a query over the `vision` collection returns nothing, the machine-local index may be absent or stale - it is not proof the corpus lacks the answer.
Run `bash scripts/ensure-index.sh` once (idempotent: adds the collection if missing, then updates and embeds), then retry the same query before concluding the answer isn't in the corpus.
Never run `scripts/index.sh` - it drops the machine-global collection.

## Reading results

- Search hits show a `qmd://vision/<path>` (or `--full-path` on-disk path), a title, and a score.
  The path tells you the family (`feeds`, `reports`, `status`, `classes`, `messages`, `general`) and, via the dash-vs-underscore mapping in `reference/corpus-map.md`, the real Vision name.
- Pull the frontmatter (`provenance`, `title`, `ingested`) from the hit or a sibling first-chunk file to confirm the real name before answering.
- Treat every answer as unverified-as-of-retrieval.
  See `reference/ground-truth.md` before it informs any commit.
