#!/usr/bin/env python3
"""Class/message family checks."""
import sys, pathlib, re, glob
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from check_corpus import check

def count_anchors(htm):
    return len(re.findall(r'(?i)<a name=', pathlib.Path(htm).read_text(errors="ignore")))

def main():
    # mObject.htm has 330 <A name> anchors (verified 2026-09-21) -> 330 message units.
    src = count_anchors("docs/original/mObject.htm")
    units = list(pathlib.Path("corpus/messages/mObject").glob("*.md"))
    assert len(units) == src, f"mObject messages: {len(units)} units vs {src} anchors"

    # Corpus-wide: every real message file (all m*.htm except mXRef.htm, the differently-shredded
    # index) contributes exactly one unit per <A name> anchor. This closes the brief's
    # believed-unchecked risk that only mObject follows the anchor-per-message structure, catching a
    # systematic shred failure in any of the other 26 files mechanically instead of by chance.
    msg_src = [f for f in glob.glob("docs/original/m*.htm") if "mXRef" not in f]
    total_anchors = sum(count_anchors(f) for f in msg_src)
    total_units = sum(
        1 for p in pathlib.Path("corpus/messages").rglob("*.md") if p.parent.name != "mXRef"
    )
    assert total_units == total_anchors, \
        f"message units {total_units} != source anchors {total_anchors} across {len(msg_src)} files"

    # A colon-bearing message name shredded to a safe filename but keeps its title.
    cs = pathlib.Path("corpus/messages/mObject/createSubclass.md")
    assert cs.exists(), "mObject#createSubclass unit missing"

    # clObject class unit exists.
    assert pathlib.Path("corpus/classes/clObject.md").exists(), "clObject class unit missing"

    rc = check("corpus/messages") or check("corpus/classes")
    print(f"mObject units={len(units)} (anchors={src}); total message units={total_units}")
    return rc

if __name__ == "__main__":
    sys.exit(main())
