#!/usr/bin/env python3
"""Ingest orchestrator. Phase A: partition docs/original/*.htm by family
SELECTOR and extract units (populating the anchor registry). Phase B: convert
each unit's HTML with pandoc, prepend frontmatter, rewrite links, enforce the
token budget, and write corpus/<out_path>."""
import argparse
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import common  # noqa: E402

FAMILIES_DIR = HERE / "families"


def load_families() -> dict:
    families = {}
    for path in sorted(FAMILIES_DIR.glob("*.py")):
        if path.name == "__init__.py":
            continue
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        families[path.stem] = module
    return families


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append",
                        help="limit the run to this family (repeatable)")
    args = parser.parse_args(argv)

    families = load_families()
    limit_to = sorted(set(args.only)) if args.only else None
    selected = limit_to if limit_to is not None else sorted(families)
    unknown = [name for name in selected if name not in families]
    if unknown:
        parser.error(f"unknown family: {', '.join(unknown)}")

    # Partition: first family whose SELECTOR claims the doc; unclaimed -> general.
    # The general sweep-up applies to full runs only: an --only build keeps each
    # family to the docs its own SELECTOR claims, so --only general yields
    # exactly the non-pma_/cl/m docs even while other families don't exist yet.
    docs = sorted(pathlib.Path("docs/original").glob("*.htm"))
    assigned = {name: [] for name in families}
    for doc in docs:
        for name in sorted(families):
            if families[name].SELECTOR(doc):
                assigned[name].append(doc)
                break
        else:
            if limit_to is None:
                assigned["general"].append(doc)

    # Phase A: extract units and populate the anchor registry.
    units = []
    for name in selected:
        claimed = assigned[name]
        made = families[name].extract(claimed, common)
        units.extend(made)
        print(f"family {name}: {len(claimed)} docs -> {len(made)} units")

    # Phase B: convert, budget-check, rewrite links, write.
    failed = written = 0
    for unit in units:
        try:
            markdown = common.pandoc_html_to_md(unit.body_html)
        except RuntimeError as exc:
            print(f"PANDOC {unit.out_path} {exc}", file=sys.stderr)
            failed += 1
            continue
        text = common.render_frontmatter(unit) + markdown
        text = common.rewrite_links(text, unit.out_path)
        if common.token_estimate(text) > 2000:
            print(f"BUDGET {unit.out_path} {len(text)}", file=sys.stderr)
            failed += 1
            continue
        dest = pathlib.Path("corpus") / unit.out_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        written += 1

    print(f"{written} units written, {failed} failed, "
          f"{len(common.unresolved_links)} unresolved links left as-is")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
