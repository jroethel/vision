"""Shared ingest utilities: Unit, budgets, slugs, frontmatter, the anchor
registry, link rewriting, pandoc conversion, and the HTML shredder."""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import subprocess
from dataclasses import dataclass
from datetime import date
from urllib.parse import unquote

BUDGET_CHARS = 8000
# Raw-HTML headroom per chunk for frontmatter plus pandoc expansion; the real
# ceiling is verified post-conversion in run.py (BUDGET line on failure).
_SHRED_HEADROOM = 1500


@dataclass
class Unit:
    source: str            # frozen-source path, e.g. "docs/original/mObject.htm"
    anchor: str | None     # source <a name> value, or None for whole-file units
    unit_type: str         # general | feed | report | status | class | message | learning
    title: str
    extra: dict            # family-specific frontmatter keys
    body_html: str         # HTML fragment for this unit, pre-conversion
    out_path: str          # corpus-relative output path


def token_estimate(text: str) -> int:
    return len(text) // 4


_slug_owner: dict[str, str] = {}


def slug(anchor: str) -> str:
    """Filesystem-safe stem: [A-Za-z0-9_] passes through, everything else -> '_'.
    Empty results and collisions get a short hex suffix of the original so
    distinct anchors never share a filename; the verbatim anchor always lives
    in the unit title and the anchor registry."""
    base = re.sub(r"[^A-Za-z0-9_]", "_", anchor)
    if not base or (_slug_owner.get(base) not in (None, anchor)):
        base += "_" + hashlib.md5(anchor.encode("utf-8")).hexdigest()[:6]
    _slug_owner[base] = anchor
    return base


def render_frontmatter(unit: Unit) -> str:
    provenance = f"{unit.source}#{unit.anchor}" if unit.anchor else unit.source
    fields = [
        ("provenance", provenance),
        ("unit_type", unit.unit_type),
        ("title", unit.title),
        ("ingested", date.today().isoformat()),
        *unit.extra.items(),
    ]
    lines = ["---"]
    for key, value in fields:
        lines.append(f"{key}: {json.dumps(value)}")  # JSON is a YAML subset
    return "\n".join(lines) + "\n---\n\n"


# Anchor registry: filename (lowercased; source hrefs vary in case) ->
# {anchor or None: corpus-relative out_path}.
_registry: dict[str, dict[str | None, str]] = {}
# Every link rewrite whose target was not registered: (current_out_path, url).
unresolved_links: list[tuple[str, str]] = []


def _reg_key(source_htm: str) -> str:
    return source_htm.rsplit("/", 1)[-1].lower()


def register_anchor(source_htm: str, anchor: str | None, out_path: str) -> None:
    _registry.setdefault(_reg_key(source_htm), {})[anchor] = out_path


def resolve_anchor(source_htm: str, anchor: str | None) -> str | None:
    return _registry.get(_reg_key(source_htm), {}).get(anchor)


_ID_TAG_RE = re.compile(
    r"<[a-zA-Z][^>]*\bid\s*=\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s>]+))",
    re.IGNORECASE,
)


def register_fragment_ids(source_htm: str, html: str,
                          chunks: list[tuple[str | None, str]],
                          out_paths: list[str]) -> None:
    """Register every id= fragment target in html to the chunk that contains
    it, so <file.htm>#<id> links resolve to the exact chunk even when the id
    sits mid-section (e.g. <p id="method">) rather than on an h1-h4/a-name
    boundary. Chunks are ordered slices of html, so containment is a span
    check; ids on boundary tags re-register to the same path (idempotent)."""
    spans = []
    pos = 0
    for _, chunk_html in chunks:
        start = html.find(chunk_html, pos)
        if start < 0:
            start = pos
        spans.append((start, start + len(chunk_html)))
        pos = start + len(chunk_html)
    for m in _ID_TAG_RE.finditer(html):
        frag_id = next((g for g in m.groups() if g is not None), None)
        if not frag_id:
            continue
        for i, (s, e) in enumerate(spans):
            if s <= m.start() < e:
                register_anchor(source_htm, frag_id, out_paths[i])
                break


# ](file.htm) and ](file.htm#anchor); pandoc percent-encodes spaces in fragments.
_LINK_RE = re.compile(r"\]\(([^)\s]*\.htm(?:#[^)]*)?)\)")


def rewrite_links(markdown: str, current_out_path: str) -> str:
    """Rewrite registered .htm links into corpus-relative links from
    current_out_path; unregistered targets are left as-is and recorded."""
    def sub(m: re.Match) -> str:
        url = m.group(1)
        file_htm, _, frag = url.partition("#")
        anchor = unquote(frag) if frag else None
        target = resolve_anchor(file_htm, anchor)
        if target is None:
            unresolved_links.append((current_out_path, url))
            return m.group(0)
        rel = posixpath.relpath(target, posixpath.dirname(current_out_path))
        return f"]({rel})"

    return _LINK_RE.sub(sub, markdown)


def pandoc_html_to_md(html_fragment: str) -> str:
    proc = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html_fragment,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed ({proc.returncode}): {proc.stderr.strip()}")
    return proc.stdout


# Section boundaries: <a name="..."> and <h1>-<h4> headings. A boundary
# carries its section anchor when the tag has one: the <a name> value, or the
# heading's id (ids are fragment targets in this corpus - source links like
# admTools.htm#Garbage Collection address <h2 id="..."> sections).
_BOUNDARY_RE = re.compile(
    r"<a\s+name\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))"
    r"|<h[1-4](?:\s[^>]*?\bid\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))|[\s>/])",
    re.IGNORECASE,
)


def _newline_offsets(html: str) -> list[int]:
    """Offsets just past newlines that lie outside any tag (never mid-tag)."""
    offsets = []
    in_tag = False
    for i, ch in enumerate(html):
        if ch == "<":
            in_tag = True
        elif ch == ">":
            in_tag = False
        elif ch == "\n" and not in_tag:
            offsets.append(i + 1)
    return offsets


def _split_window(segment: str, target: int) -> list[str]:
    """Split an over-budget segment at safe (outside-tag) newline offsets."""
    offsets = _newline_offsets(segment)
    pieces = []
    start = 0
    while start < len(segment):
        if len(segment) - start <= target:
            pieces.append(segment[start:])
            break
        limit = start + target
        within = [o for o in offsets if start < o <= limit]
        if within:
            cut = max(within)
        else:
            # No safe boundary in the window: take the next safe one past it
            # (slightly over target, still tag-safe), or a hard cut if the
            # segment has no safe boundary at all.
            after = [o for o in offsets if o > limit]
            cut = after[0] if after else limit
        pieces.append(segment[start:cut])
        start = cut
    return pieces


def _section_chunks(html: str, target: int) -> list[tuple[str | None, str]]:
    """Split at <h1>-<h4> and <a name> boundaries; over-budget sections are
    window-split at outside-tag newlines. A chunk's anchor is its boundary's
    <a name> value or heading id."""
    bounds = [(m.start(), next((g for g in m.groups() if g is not None), None))
              for m in _BOUNDARY_RE.finditer(html)]
    segments: list[tuple[str | None, int, int]] = []
    prev, prev_anchor = 0, None
    for start, anchor in bounds:
        if start > prev:
            segments.append((prev_anchor, prev, start))
        prev, prev_anchor = start, anchor
    if prev < len(html):
        segments.append((prev_anchor, prev, len(html)))
    segments = [s for s in segments if html[s[1]:s[2]].strip()]

    chunks: list[tuple[str | None, str]] = []
    for anchor, seg_start, seg_end in segments:
        segment = html[seg_start:seg_end]
        if len(segment) <= target:
            chunks.append((anchor, segment))
            continue
        for i, piece in enumerate(_split_window(segment, target)):
            chunks.append((anchor if i == 0 else None, piece))
    return chunks


# Frontmatter allowance for post-conversion budget verification; run.py's
# token check on the final text remains the authority.
_FM_ALLOWANCE = 500


def _fit(piece: str, anchor: str | None, budget_chars: int) -> list[tuple[str | None, str]]:
    """Verify post-conversion that this piece stays in budget; if pandoc
    expanded it past the ceiling (e.g. <hr> -> 72-char dash rules), re-split
    at a proportionally smaller target and re-verify."""
    markdown = pandoc_html_to_md(piece)
    if len(markdown) + _FM_ALLOWANCE <= budget_chars or len(piece) < 200:
        return [(anchor, piece)]
    target = max(400, int(len(piece) * (budget_chars - _FM_ALLOWANCE) / max(len(markdown), 1)))
    pieces = _split_window(piece, target)
    if len(pieces) == 1:
        mid = len(piece) // 2
        pieces = [piece[:mid], piece[mid:]]
    fitted: list[tuple[str | None, str]] = []
    for i, sub in enumerate(pieces):
        fitted.extend(_fit(sub, anchor if i == 0 else None, budget_chars))
    return fitted


def shred_html(html: str, budget_chars: int = BUDGET_CHARS) -> list[tuple[str | None, str]]:
    """Split a whole-file HTML fragment into chunks whose converted units stay
    within budget_chars. Splits at <h1>-<h4> and <a name> boundaries first; an
    over-budget section is split further at outside-tag newlines, and every
    chunk is verified post-conversion (re-split when pandoc expands it). Each
    chunk is returned as (anchor_or_None, chunk_html); anchor is the chunk's
    section anchor (<a name> value or heading id) when it began at a boundary
    that has one. A fragment under budget returns [(None, html)]."""
    target = budget_chars - _SHRED_HEADROOM
    if len(html) <= target:
        md = pandoc_html_to_md(html)
        if len(md) + _FM_ALLOWANCE <= budget_chars:
            return [(None, html)]
    return [c for anchor, piece in _section_chunks(html, target)
            for c in _fit(piece, anchor, budget_chars)]
