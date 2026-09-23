# Ground-truth recheck loop

Every corpus claim is unverified-as-of-retrieval: it reflects the frozen HTML docs as ingested on 2026-09-22, not the live system.
Run this loop before any feed or schema commit that relies on a corpus claim.

## Step 1: retrieve the unit and read its provenance

Fetch the unit with `qmd get` (see `reference/retrieval.md`).
Read its frontmatter: `provenance` (original HTML path, real underscore name), `unit_type`, and `ingested` (the as-of date, `2026-09-22` for this snapshot).

## Step 2: locate the live source for that claim

Where "live source" is depends on what kind of unit it is - verify with `ls` rather than assuming a fixed path, because the layout differs by unit type:

- **Feed fields** (`unit_type: feed`, e.g. `pma_AnalystEst`) are defined in the application-layer bootstrap protocol, not the C++ kernel.
  Check `application/localvision/bootstrap/protocol/originals/` - `EXTiface.feeds`, `EntityExtenderSetup.idemo`, `PropertySetup.idemo`, and `ClassSetup.idemo` are the files that define feed records and their fields.
  Verified: `grep -n "AnalystEst" application/localvision/bootstrap/protocol/originals/EXTiface.feeds` finds the `AnalystEstimateRecord` reference at line 496.
- **Class and message definitions** (`unit_type: class` or `message`, e.g. `mDate`, `mNumber`) map to `software/src/<version>/src/`, but not always `kernel/` specifically - verify which subsystem with `ls software/src/<version>/src/` and grep before citing a path.
  Verified: `mDate`/`mNumber` quarter-end primitives (`asQuarterEnd`, `quarterEnds`) are implemented in `software/src/master/src/backend/PFdate.cpp` (string literals `ByQuarterEndsIncrementDate`, `ByQuarterEndsDecrementDate`), not in `software/src/master/src/kernel/`.
  `software/src/` has three version trees: `8.0`, `8.1`, `master` - match the corpus claim's era to the right one if it matters.
- **Behavior claims** (does a message actually do what the doc says) are exercised by the ivr testkit at `software/testtools/ivr/`.
  Verified layout: `software/testtools/ivr/order.ivr` and `software/testtools/ivr/INITpatch.ivr` are top-level fixture scripts; `software/testtools/ivr/source/` holds `doc/`, `lib/`, `scripts/`, `test/`; `software/testtools/ivr/testkit/scripts/` holds `buildBaseline`, `checkProposed`, `diffProposed`, `diffProposedClasses`, `runAllTests`.

## Step 3: confirm the claim

Either read the live source at the location found in Step 2 and compare it to the corpus claim, or run the relevant ivr fixture (via `testkit/scripts/runAllTests` or a targeted fixture) and compare observed behavior to the corpus claim.
If the live source and the corpus disagree, the live source wins - the corpus is a frozen snapshot.

## Step 4: only then commit

A feed or schema commit is safe to make only after Step 3 confirms the claim against live source or a passing ivr run.
Never commit a schema or feed change on the strength of a corpus citation alone.
