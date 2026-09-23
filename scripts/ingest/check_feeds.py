#!/usr/bin/env python3
"""Feed/report/status family checks."""
import sys, pathlib, glob
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from check_corpus import parse_frontmatter, check

def main():
    src_count = len(glob.glob("docs/original/pma_*.htm"))
    feeds = sorted(pathlib.Path("corpus/feeds").glob("*.md"))
    reports = sorted(pathlib.Path("corpus/reports").glob("*.md"))
    status = sorted(pathlib.Path("corpus/status").glob("*.md"))
    derived = len(feeds) + len(reports) + len(status)
    assert derived == src_count, f"pma_ count mismatch: {derived} derived vs {src_count} source"

    # nextQuarterEnd is defined by exactly one feed, pma_AnalystEst, type Date (verified 2026-09-21
    # by grep: `grep -l nextQuarterEnd docs/original/pma_*.htm` returns only pma_AnalystEst.htm).
    # Assert the type AT the field's own row, not "Date" anywhere in the body.
    est = pathlib.Path("corpus/feeds/pma-AnalystEst.md")  # qmd-native stem (source pma_AnalystEst.htm)
    assert est.exists(), "pma-AnalystEst feed unit missing"
    fm, body = parse_frontmatter(est.read_text(encoding="utf-8"))
    fields = {f["name"]: f["type"] for f in fm.get("fields", [])}
    assert fields.get("nextQuarterEnd") == "Date", \
        f"nextQuarterEnd not typed Date at its row in pma_AnalystEst: {fields.get('nextQuarterEnd')}"

    rc = check("corpus/feeds") or check("corpus/reports") or (check("corpus/status") if status else 0)
    print(f"feeds={len(feeds)} reports={len(reports)} status={len(status)} source_pma={src_count}")
    return rc

if __name__ == "__main__":
    sys.exit(main())
