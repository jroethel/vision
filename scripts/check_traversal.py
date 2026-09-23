#!/usr/bin/env python3
"""Deep-link resolution: a known chain resolves; every clObject link (across the shredded clObject
units) resolves except where the frozen source links to a nonexistent anchor (dangling-at-source,
recorded not failed)."""
import re, sys, pathlib

CORPUS = pathlib.Path("corpus")
ORIG = pathlib.Path("docs/original")

def all_links(md_path):
    return re.findall(r"\]\(([^)]+)\)", md_path.read_text(encoding="utf-8"))

def resolve_md(from_path, target):
    p = (from_path.parent / target.split("#")[0]).resolve()
    return p.exists()

def source_anchor_exists(htm, anchor):
    f = ORIG / htm
    return f.exists() and re.search(r'(?i)<a name="%s"' % re.escape(anchor),
                                    f.read_text(errors="ignore")) is not None

def clobject_units():
    base = CORPUS / "classes" / "clObject.md"
    units = [base] if base.exists() else []
    d = CORPUS / "classes" / "clObject"
    if d.is_dir():
        units += sorted(d.glob("*.md"))
    return units

def main():
    units = clobject_units()
    assert units, "clObject unit(s) missing"

    # Chain: some clObject unit -> mObject#createSubclass, rewritten to a corpus .md path that
    # resolves relative to that unit's own directory (clObject shreds, so the link may be in any chunk).
    chain_ok = any(
        "messages/mObject/createSubclass" in t and resolve_md(u, t)
        for u in units for t in all_links(u)
    )
    assert chain_ok, "no clObject unit has a resolving rewritten link to mObject#createSubclass"

    fixable, dangling = [], []
    for u in units:
        for t in all_links(u):
            base = t.split("#")[0]
            if base.endswith(".md"):
                if not resolve_md(u, t):
                    fixable.append((u.name, t))  # a corpus .md link that does not resolve is always a bug
            elif base.endswith(".htm"):
                # residual (unregistered) source link: classify against the frozen source
                anchor = t.split("#", 1)[1] if "#" in t else ""
                (fixable if anchor and source_anchor_exists(base, anchor) else dangling).append((u.name, t))

    if dangling:
        print(f"known dangling-at-source (recorded, not a failure): {len(dangling)}")
        for u, d in dangling[:20]:
            print("  ", u, d)
    assert not fixable, f"clObject fixable unresolved links (anchor exists in source): {fixable}"

    print(f"traversal OK: chain resolves across {len(units)} clObject units; "
          f"{len(dangling)} dangling-at-source; no fixable drops")
    return 0

if __name__ == "__main__":
    sys.exit(main())
