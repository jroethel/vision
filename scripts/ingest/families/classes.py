"""Class family: every cl*.htm converted via common.shred_html; the file-level
anchor lands on the first chunk's classes/<stem>.md so clX.htm links resolve."""
import re

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def SELECTOR(path) -> bool:
    name = path.name
    return name.endswith(".htm") and name.startswith("cl")


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
        common.register_anchor(source, None, f"classes/{stem}.md")
        out_paths = []
        for i, (anchor, chunk_html) in enumerate(chunks, 1):
            out_path = f"classes/{stem}.md" if i == 1 else f"classes/{stem}/{i}.md"
            out_paths.append(out_path)
            if anchor:
                common.register_anchor(source, anchor, out_path)
            title = doc_title if i == 1 else f"{doc_title} (part {i})"
            units.append(common.Unit(
                source=source,
                anchor=anchor,
                unit_type="class",
                title=title,
                extra={},
                body_html=chunk_html,
                out_path=out_path,
            ))
        common.register_fragment_ids(source, html, chunks, out_paths)
    return units
