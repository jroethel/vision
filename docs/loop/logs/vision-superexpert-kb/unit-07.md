# Unit 07: Summon - skill and staged launcher recipe

Plan: `docs/plans/2026-09-21.vision-superexpert-kb-plan.md`, Task 7.
Tracking issue #1.

## Deviation found and fixed before starting

My worktree branch (`worktree-agent-abd9fb59d5388b8f1`) was created off `master` (commit `2acb475`), not off `loop/vision-superexpert-kb-build` (commit `116a1a1` at the time I checked) as the task briefing stated.
`corpus/`, `docs/plans/2026-09-21.vision-superexpert-kb-plan.md`, and `scripts/ensure-index.sh` did not exist on that base, so the task was impossible as briefed.
Fix: `git reset --hard loop/vision-superexpert-kb-build` inside my own worktree only (never touched the main checkout, never switched branches there).
This discarded one unrelated uncommitted change in this worktree's copy of `application/production/scripts/ProcessUpdates.csh` (not an owned file, not part of this task).
An identical uncommitted diff still exists in the main checkout, untouched.
Verified after the reset: `docs/plans/`, `corpus/{feeds,reports,status,classes,messages,general}/`, and `scripts/ensure-index.sh` all present.

## Research before writing

- Read plan Task 7 interfaces section directly from the plan doc (not from memory).
- Counted corpus family units with `find corpus/<family> -name '*.md' | wc -l`: feeds 86, reports 408, status 9, classes 210, messages 3272, general 984, total 4969.
  `corpus/learnings/` does not exist yet (later task).
- Confirmed the name-mapping example: `corpus/feeds/pma-AnalystEst.md` frontmatter has `provenance: "docs/original/pma_AnalystEst.htm"` and a `nextQuarterEnd` field of type `Date`.
- Confirmed shred convention: `corpus/feeds/pma-AnalystEst.md` (first chunk) plus `corpus/feeds/pma-AnalystEst/3.md`, `.../4.md` (overflow).
  Also saw `corpus/general/invHolding/{2,3,4,5,6}.md`.
- Confirmed `corpus/messages/` is grouped by class dir (`mDate/asQuarterEnd.md`, `mNumber/quarterEnds.md`) plus `corpus/messages/mXRef/` chunked as `A-1.md`, `B-1.md`, etc. (55 files).
- Ran `qmd --help` and `qmd query --help` to get real flag syntax (`-c`, `--full-path`, structured `intent:/lex:/vec:/hyde:` query documents) rather than guessing.
- Ran a real structured query (`lex: nextQuarterEnd` + `vec: ...`) against the live `vision` collection: top hit was `corpus/feeds/pma-AnalystEst/3.md` at 93% score.
  Confirms the retrieval.md examples actually work, not just plausible syntax.
- For `reference/ground-truth.md`, verified live-source locations rather than assuming the plan's suggested `software/src/<version>/src/kernel/` path always applies:
  - Feed fields (e.g. `pma_AnalystEst`) are defined at the application layer, not in the C++ kernel: `grep -n "AnalystEst" application/localvision/bootstrap/protocol/originals/EXTiface.feeds` finds `AnalystEstimateRecord` at line 496.
  - `mDate`/`mNumber` quarter-end primitives are in `software/src/master/src/backend/PFdate.cpp` (`ByQuarterEndsIncrementDate` etc.), not `software/src/master/src/kernel/` - kernel/ holds different subsystems (e.g. `Vca_Registry_*`).
  - `software/testtools/ivr/` layout verified with `ls`: `order.ivr` and `INITpatch.ivr` at top level, `source/{benchmark,datafeed,ivr,misc,order.vis}`, `testkit/{doc,lib,scripts,test}`, and `testkit/scripts/{buildBaseline,checkProposed,diffProposed,diffProposedClasses,runAllTests}`.
  - Wrote `ground-truth.md` to say "verify with `ls` rather than assuming a fixed path" precisely because the plan's suggested kernel/ path turned out not to hold for messages, and doesn't apply at all for feed fields.

## Checks run

1. Skill-validity check (verbatim from the task): `skill valid` - pass.
2. Headless summon smoke (verbatim from the task), run from this worktree's root per the DEVIATION instruction (not `~/create/vision`):
   - Command: `claude -p "Using the vision-expert skill and qmd, which feed sets the field nextQuarterEnd and what is its type? Cite the corpus unit path, and state what must be checked before committing a schema or feed change based on this."`
   - One run needed, no retry.
   - Answer named `pma_AnalystEst`, type Date, cited `corpus/feeds/pma-AnalystEst/3.md` (an overflow chunk of the field-table doc, still under `corpus/`), and stated the corpus is unverified-as-of-retrieval and must be rechecked against live source or the ivr testkit before a schema/feed commit - and explicitly said it had not done that recheck.
   - All three grep conditions passed: `pma_AnalystEst`, `corpus`, and the ivr/live-source/verify pattern.

## Open questions

None blocking.
One note: the smoke answer cited the overflow chunk (`pma-AnalystEst/3.md`, which holds the field table) rather than the first-chunk file (`pma-AnalystEst.md`, which holds the frontmatter) - both are valid `corpus/` citations for this claim, and `reference/corpus-map.md` documents the shred convention so a reader can find the sibling first chunk if needed.

## Ground-truth fix (reopened after two failed validations)

Two downstream validations failed because `reference/ground-truth.md` labeled `asQuarterEnd`/`quarterEnds` as "Verified" in `software/src/master/src/backend/PFdate.cpp`, and `grep -rl asQuarterEnd software/src` finds nothing there.
The owner amended the plan's ground-truth rule: live source has two layers, the bootstrap protocol `application/localvision/bootstrap/protocol/originals/` defines messages (`*.bi`) and properties/feed fields (`*.idemo`, `EXTiface.feeds`), and `software/src/<version>/src/` holds only the C++ primitives those messages bind to.
Reconfirmed this session with `grep`/`sed`, none from memory: `Date.bi:231` defines `asQuarterEnd`, `Integer.bi:132` defines the `quarterEnds` message it calls, `PropertySetup.idemo:105` defines `nextQuarterEnd`, and `Offset.bi:105` binds primitive 317 (`ByQuarterEndsIncrementDate`) to `software/src/master/src/backend/PFdate.cpp:545` (`ByQuarterEndsDecrementDate` at line 579).
Also reconfirmed the pre-existing "Verified" claims: `EXTiface.feeds:496` (`AnalystEstimateRecord` reference), the ivr top-level layout (`order.ivr`, `INITpatch.ivr`), `source/{benchmark,datafeed,ivr,misc,order.vis}`, and `testkit/{doc,lib,scripts,test}` with `testkit/scripts/{buildBaseline,checkProposed,diffProposed,diffProposedClasses,runAllTests}`.
Rewrote `SKILL.md` and `reference/ground-truth.md` so Step 2 checks the bootstrap protocol first and the C++ primitives second, with every verified claim pointing at a location confirmed this session.
Also fixed a smaller inaccuracy in `SKILL.md` and `reference/corpus-map.md`: the real underscore feed name lives in a unit's `provenance` field, not `title`.
`title` is the document's own heading, confirmed against `corpus/feeds/pma-AnalystEst.md` frontmatter (`title: "Vision Upload Format: AnalystEst "`).
