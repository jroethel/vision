#!/usr/bin/env python3
"""Promote a reviewed learning from learnings-queue/ into corpus/learnings/.

The interactive y/N confirmation is the human gate: it is read from a TTY and
fails closed under any non-interactive invocation (piped stdin, agent run),
so the automation that drafted a candidate cannot promote it.
--assume-yes exists solely for the automated grow test (scripts/test_grow.sh)
and CI; never use it for a real promotion.
"""

import json
import os
import re
import subprocess
import sys

ROLE_TIERS = ("engineer", "architect", "sysadmin")
REQUIRED_KEYS = ("verified_against", "role_tier")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def die(msg):
    print(f"promote_learning: {msg}", file=sys.stderr)
    sys.exit(1)


def parse_frontmatter(text):
    """Split a queue entry into an ordered (key, value) list and the body."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, None
    pairs = []
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        key, value = key.strip(), value.strip()
        if key:
            pairs.append((key, value))
    return pairs, text[match.end():]


def qmd_slug(stem):
    """Sanitize a filename stem qmd-native: [A-Za-z0-9-] only, no underscores."""
    return re.sub(r"[^A-Za-z0-9-]+", "-", stem).strip("-")


def main():
    assume_yes = "--assume-yes" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--assume-yes"]
    if len(args) != 1:
        die("usage: promote_learning.py <queue-entry> [--assume-yes]")
    entry = args[0]

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entry_path = os.path.abspath(entry)
    if not os.path.isfile(entry_path):
        die(f"queue entry not found: {entry}")

    with open(entry_path, encoding="utf-8") as f:
        text = f.read()
    pairs, body = parse_frontmatter(text)
    if pairs is None:
        die(f"{entry}: no frontmatter block found")
    keys = dict(pairs)

    for key in REQUIRED_KEYS:
        if not keys.get(key, "").strip():
            die(f"{entry}: required frontmatter key missing or empty: {key}")
    if keys["role_tier"] not in ROLE_TIERS:
        tiers = "|".join(ROLE_TIERS)
        die(f"{entry}: role_tier must be one of {tiers}, got: {keys['role_tier']}")

    print(text)

    if not assume_yes:
        if not sys.stdin.isatty():
            die("refusing to promote: stdin is not a TTY and --assume-yes was not given; "
                "a human must confirm at the terminal (this gate is what keeps the drafting "
                "automation from promoting its own candidate)")
        answer = input("Promote this learning into corpus/learnings/? [y/N] ").strip()
        if answer not in ("y", "yes"):
            die("not confirmed; nothing promoted")

    stem = os.path.splitext(os.path.basename(entry_path))[0]
    slug = qmd_slug(stem)
    if not slug:
        die(f"{entry}: stem sanitizes to an empty slug")
    target = os.path.join(root, "corpus", "learnings", f"{slug}.md")
    if os.path.exists(target):
        die(f"target already exists: {os.path.relpath(target, root)}")

    rel_entry = os.path.relpath(entry_path, root)
    lines = ["---"]
    lines.append(f"provenance: {json.dumps(rel_entry)}")
    lines.append(f"unit_type: {json.dumps('learning')}")
    for key, value in pairs:
        lines.append(f"{key}: {json.dumps(value)}")
    lines.append("---")
    with open(target, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n" + body)

    os.remove(entry_path)

    result = subprocess.run(["qmd", "update"], cwd=root)
    if result.returncode != 0:
        die(f"moved to {os.path.relpath(target, root)} but 'qmd update' failed "
            f"(exit {result.returncode}); run scripts/ensure-index.sh to re-index")


if __name__ == "__main__":
    main()
