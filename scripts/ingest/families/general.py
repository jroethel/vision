"""General-doc family: every docs/original/*.htm not claimed by a specific
family (i.e. not named pma_*, cl*, or m*). Over-budget docs are shredded via
common.shred_html, never dropped."""
import re

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def SELECTOR(path) -> bool:
    name = path.name
    return name.endswith(".htm") and not name.startswith(("pma_", "cl", "m"))


def extract(paths, common) -> list:
    units = []
    for path in paths:
        source = str(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        # Strip the source's Jekyll frontmatter block; keep its title.
        html, doc_title = text, ""
        fm = _FM_RE.match(text)
        if fm:
            html = text[fm.end():]
            t = _TITLE_RE.search(fm.group(1))
            if t:
                doc_title = t.group(1).strip().strip("\"'")
        doc_title = doc_title or path.stem

        chunks = common.shred_html(html)
        if not chunks:
            continue
        stem = path.stem
        common.register_anchor(source, None, f"general/{stem}.md")
        out_paths = []
        for i, (anchor, chunk_html) in enumerate(chunks, 1):
            out_path = f"general/{stem}.md" if i == 1 else f"general/{stem}/{i}.md"
            out_paths.append(out_path)
            if anchor:
                common.register_anchor(source, anchor, out_path)
            title = doc_title if i == 1 else f"{doc_title} (part {i})"
            units.append(common.Unit(
                source=source,
                anchor=anchor,
                unit_type="general",
                title=title,
                extra={},
                body_html=chunk_html,
                out_path=out_path,
            ))
        common.register_fragment_ids(source, html, chunks, out_paths)
    return units
