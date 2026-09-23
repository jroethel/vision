# Ground-truth recheck loop

Every corpus claim is unverified-as-of-retrieval: it reflects the frozen HTML docs as ingested on 2026-09-22, not the live system.
Live source and the ivr testkit are ground truth, and a retrieved schema or feed claim stays unverified-as-of-retrieval until checked against them before any feed or schema commit.
Run this loop before any feed or schema commit that relies on a corpus claim.

## Step 1: retrieve the unit and read its provenance

Fetch the unit with `qmd get` (see `reference/retrieval.md`).
Read its frontmatter: `provenance` (original HTML path, real underscore name), `unit_type`, and `ingested` (the as-of date, `2026-09-22` for this snapshot).

## Step 2: locate the live source for that claim

Live source has two layers.
The bootstrap protocol at `application/localvision/bootstrap/protocol/originals/` defines messages, properties, and feed fields.
`software/src/<version>/src/` holds only the C++ primitives those messages bind to, not the message definitions themselves.
Check the bootstrap protocol first, the C++ primitives second, or the ivr testkit before any feed or schema commit:

- **Messages** (`unit_type: message`, e.g. `mDate`, `mNumber`) are defined in the bootstrap protocol `*.bi` files.
  Verified: `asQuarterEnd` is defined at `Date.bi:231` (`defineMethod: [ | asQuarterEnd | ^self + 0 quarterEnds ] .`).
  Verified: the `quarterEnds` message it calls is defined at `Integer.bi:132`.
- **Properties and feed fields** (`unit_type: feed`, e.g. `pma_AnalystEst`) are defined in the bootstrap protocol `*.idemo` files and `EXTiface.feeds`.
  Verified: `nextQuarterEnd` is defined at `PropertySetup.idemo:105` (`AnalystEstimate	nextQuarterEnd	N	NA	Date`).
  Verified: `grep -n "AnalystEst" application/localvision/bootstrap/protocol/originals/EXTiface.feeds` finds the `AnalystEstimateRecord` reference at line 496.
- **Primitives a message binds to** are in `software/src/<version>/src/`.
  Verified: `Offset.bi:105` binds the `QuarterEnds increment:` primitive (317, `ByQuarterEndsIncrementDate`) to `software/src/master/src/backend/PFdate.cpp`, where the string literal appears at line 545, with `ByQuarterEndsDecrementDate` at line 579.
  `grep -rl asQuarterEnd software/src` finds nothing - the message itself lives only in the bootstrap protocol, never in `software/src/`.
  `software/src/` has three version trees: `8.0`, `8.1`, `master` - match the corpus claim's era to the right one if it matters.
- **Behavior claims** (does a message actually do what the doc says) are exercised by the ivr testkit at `software/testtools/ivr/`.
  Verified layout: `software/testtools/ivr/order.ivr` and `software/testtools/ivr/INITpatch.ivr` are top-level fixture scripts.
  `software/testtools/ivr/source/` holds `benchmark/`, `datafeed/`, `ivr/`, `misc/`, and `order.vis`.
  `software/testtools/ivr/testkit/` holds `doc/`, `lib/`, `scripts/`, and `test/` - `testkit/scripts/` holds `buildBaseline`, `checkProposed`, `diffProposed`, `diffProposedClasses`, `runAllTests`.

## Step 3: confirm the claim

Either read the live source at the location found in Step 2 and compare it to the corpus claim, or run the relevant ivr fixture (via `testkit/scripts/runAllTests` or a targeted fixture) and compare observed behavior to the corpus claim.
If the live source and the corpus disagree, the live source wins - the corpus is a frozen snapshot.

## Step 4: only then commit

A feed or schema commit is safe to make only after Step 3 confirms the claim against live source or a passing ivr run.
Never commit a schema or feed change on the strength of a corpus citation alone.
