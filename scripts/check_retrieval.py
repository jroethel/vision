#!/usr/bin/env python3
"""Field -> feed retrieval check over the qmd 'vision' collection."""
import subprocess, sys

def qmd_search(query):
    out = subprocess.run(
        ["qmd", "search", query, "-c", "vision", "-n", "10", "--full-path"],
        capture_output=True, text=True, check=True,
    )
    return out.stdout

def main():
    # nextQuarterEnd is set by exactly one feed, pma_AnalystEst (verified 2026-09-21:
    # `grep -l nextQuarterEnd docs/original/pma_*.htm` returns only pma_AnalystEst.htm), so the
    # "which feed sets this field" promise is singular and this check is deterministic by design.
    hits = qmd_search("nextQuarterEnd")
    assert "pma-AnalystEst" in hits, f"nextQuarterEnd did not retrieve pma-AnalystEst:\n{hits}"
    assert "corpus/feeds" in hits, "retrieval hit lacks corpus provenance path"

    # A near-miss name that no feed defines must not surface a feed as a false positive.
    miss = qmd_search("nextQuarterEndingXyz")
    assert "corpus/feeds/pma-AnalystEst" not in miss, "near-miss produced false positive"

    print("retrieval OK: nextQuarterEnd -> pma_AnalystEst with provenance; near-miss clean")
    return 0

if __name__ == "__main__":
    sys.exit(main())
