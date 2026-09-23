#!/usr/bin/env python3
"""Assert corpus-wide invariants over a corpus directory (or subdirectory)."""
import sys, pathlib, json

_INVALID = object()  # marks a frontmatter value that is not valid JSON/YAML-safe

def parse_frontmatter(text):
    """Values are emitted as json.dumps(...); parse them back and flag any that
    do not round-trip. A key line is 'key: <json-value>'; the key has no colon,
    so the first colon is always the separator even when the value contains ':'."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            v = v.strip()
            try:
                fm[k.strip()] = json.loads(v) if v else ""
            except json.JSONDecodeError:
                fm[k.strip()] = _INVALID
    return fm, text[end + 5:]

def check(root):
    root = pathlib.Path(root)
    units = sorted(root.rglob("*.md"))
    assert units, f"no units found under {root}"
    errors = []
    for u in units:
        text = u.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{u}: no frontmatter")
            continue
        if any(v is _INVALID for v in fm.values()):
            errors.append(f"{u}: frontmatter value is not valid JSON (unescaped scalar?)")
        if not fm.get("provenance"):
            errors.append(f"{u}: missing provenance")
        if not fm.get("unit_type"):
            errors.append(f"{u}: missing unit_type")
        if len(text) // 4 > 2000:
            errors.append(f"{u}: over budget ({len(text)} chars)")
    for e in errors:
        print("FAIL", e)
    print(f"checked {len(units)} units, {len(errors)} errors")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(check(sys.argv[1] if len(sys.argv) > 1 else "corpus"))
