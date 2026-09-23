"""Feed, report, and status family: docs/original/pma_*.htm.

Feed docs (first table header row starts with a `Field` column) carry two
representations of the same data: extra["fields"] for machine lookup and a
markdown table in the body for human reading. The source tables use 1990s
unclosed <td>/<th> tags that pandoc flattens into loose paragraphs, so the
table is rebuilt as clean closed-tag HTML before conversion. An "id of
existing X instance" description additionally links to the feed that defines
X (stored as {"ref": stem} in the field dict and as an inline
docs/original/<stem>.htm link that Phase B rewrites in-corpus).

Report docs (Position | Form Id | Description header) and the status doc
(pma_DataFeedStatus, neither shape) convert whole-file. Over-budget docs of
any kind are shredded via common.shred_html under the family convention:
first chunk <family>/<stem>.md, overflow <family>/<stem>/<n>.md."""
import html as htmlmod
import json
import re

ROW_RE = re.compile(r"<tr[^>]*>", re.I)
# Cells end at the next row/cell/table boundary tag; the source leaves
# <th>/<td> unclosed, and the last cell of a table would otherwise swallow
# everything to the end of the row chunk.
CELL_RE = re.compile(
    r"<(th|td)[^>]*>(.*?)(?=<t[dhr][\s>]|</t(?:able|r|d|h)>|$)", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
SOURCE_FM_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
SOURCE_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
# "The X feed is used to create and update <b>Entity</b> ... instances":
# the first such bold names the entity this feed defines.
_SUMMARY_ENTITY_RE = re.compile(
    r"(?:create|update|define|maintain|refresh)[^<]{0,80}?<b>([A-Za-z]+)</b>"
    r"[^<]{0,40}?(?:instance|record)", re.I)
_EXISTING_RE = re.compile(r"\bid of existing ([A-Za-z]+) instance")
_FEEDNAME_RE = re.compile(r"<b>\s*Data Feed:\s*</b>\s*<i>([^<]+)</i>", re.I)
_PROPERTY_RE = re.compile(r"^(.*?)\s*Property$", re.I)
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((docs/original/[^)\s]+\.htm)\)")


def SELECTOR(path) -> bool:
    return path.name.startswith("pma_")


def _clean(cell_html: str) -> str:
    return WS_RE.sub(" ", htmlmod.unescape(TAG_RE.sub(" ", cell_html))).strip()


def _esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _edit1(a: str, b: str) -> bool:
    """True when edit distance(a, b) <= 1 (source typos like Corrency)."""
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) <= 1
    if len(a) > len(b):
        a, b = b, a
    i = j = diff = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            diff += 1
            j += 1
            if diff > 1:
                return False
    return True


def _rows(body: str):
    """Yield (row_start_offset, cells) for every row with cells; cells are
    (tag, cleaned_text). Rows split at <tr>; cells at <th>/<td>."""
    starts = [m.start() for m in ROW_RE.finditer(body)] + [len(body)]
    for i in range(len(starts) - 1):
        chunk = body[starts[i]:starts[i + 1]]
        cells = [(m.group(1).lower(), _clean(m.group(2)))
                 for m in CELL_RE.finditer(chunk)]
        if cells:
            yield starts[i], cells


def _first_header_row(body: str):
    for row_start, cells in _rows(body):
        if all(tag == "th" for tag, _ in cells):
            return row_start, [text for _, text in cells]
    return None, None


def _classify(header_texts) -> str:
    lowered = [t.strip().lower() for t in header_texts]
    if lowered and lowered[0] == "field":
        return "feed"
    if "position" in lowered and "form id" in lowered:
        return "report"
    return "status"


def _header_entity(header_texts):
    """The grouped header's second column: '<FeedName> Property' -> name."""
    if len(header_texts) >= 4:
        m = _PROPERTY_RE.match(header_texts[1].strip())
        if m and m.group(1).strip():
            return m.group(1).strip()
    return None


def _table_span(body: str, header_start: int):
    """The <table>...</table> region around the fields table (feeds have no
    nested tables, so the first </table> after the header closes it)."""
    low = body.lower()
    tstart = low.rfind("<table", 0, header_start)
    tend = low.find("</table>", header_start)
    tend = tend + len("</table>") if tend != -1 else len(body)
    return tstart, tend


def _parse_fields(body: str, header_start: int, table_end: int):
    """Parse the TD rows of the fields table into field dicts, plus the
    group-marker rows between them, in document order."""
    fields, table_rows = [], []
    ncols = None
    for row_start, cells in _rows(body):
        if row_start < header_start:
            continue
        if row_start == header_start:
            ncols = len(cells)
            continue
        if row_start >= table_end:
            break
        tags = [tag for tag, _ in cells]
        texts = [text for _, text in cells]
        if all(tag == "th" for tag in tags):
            if texts and texts[0].strip():
                table_rows.append(("group", texts[0].strip()))
            continue
        if tags[0] != "td" or not texts[0].strip():
            continue
        if ncols == 4:
            field = dict(zip(("name", "property", "type", "desc"),
                             (texts + [""] * 4)[:4]))
        else:
            field = {"name": texts[0], "property": "",
                     "type": texts[1] if len(texts) > 1 else "",
                     "desc": texts[2] if len(texts) > 2 else ""}
        fields.append(field)
        table_rows.append(("field", field))
    return fields, table_rows


def _rebuild_table(header_texts, table_rows) -> str:
    """Closed-tag HTML table from parsed rows, emitted on ONE physical line:
    a newline between rows would let the shredder's window split cut the
    table in half, and pandoc flattens the orphaned rows into loose text."""
    has_property = len(header_texts) >= 4
    out = ["<table>"]
    out.append("<tr>" + "".join(f"<th>{_esc(h)}</th>" for h in header_texts)
               + "</tr>")
    for kind, payload in table_rows:
        if kind == "group":
            out.append(f'<tr><th align=center colspan={len(header_texts)}>'
                       f'{_esc(payload)}</th></tr>')
        else:
            field = payload
            cells = [_esc(field["name"])]
            if has_property:
                cells.append(_esc(field["property"]))
            cells.append(_esc(field["type"]))
            desc = field["desc"]
            if field.get("ref"):
                # desc carries a markdown link; give pandoc the HTML form
                cells.append(_MD_LINK_RE.sub(r'<a href="\2">\1</a>',
                                             _esc(desc)))
            else:
                cells.append(_esc(desc))
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells)
                       + "</tr>")
    out.append("</table>")
    return "".join(out)


def _apply_refs(fields, entity_map, own_stem):
    """Resolve 'id of existing X instance' rows: exact entity match, else a
    unique edit-distance-1 match (source typos), never the feed itself."""
    for field in fields:
        m = _EXISTING_RE.search(field["desc"])
        if not m:
            continue
        entity = m.group(1)
        stem = entity_map.get(entity)
        if stem is None:
            near = sorted(s for k, s in entity_map.items()
                          if _edit1(entity, k))
            if len(near) == 1:
                stem = near[0]
        if not stem or stem == own_stem:
            continue
        field["ref"] = stem
        head = field["desc"][:m.start(1)]
        tail = field["desc"][m.end(1):]
        field["desc"] = (f"{head}[{entity}](docs/original/{stem}.htm)"
                         f"{tail}")


def extract(paths, common) -> list:
    # Pass 1: read, strip the source's Jekyll frontmatter, classify.
    docs = []
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        html, doc_title = text, ""
        fm = SOURCE_FM_RE.match(text)
        if fm:
            html = text[fm.end():]
            t = SOURCE_TITLE_RE.search(fm.group(0))
            if t:
                doc_title = t.group(1).strip().strip("\"'")
        docs.append({
            "source": str(path),
            "stem": path.stem,
            "html": html,
            "title": doc_title or path.stem,
        })
    for doc in docs:
        doc["header_start"], doc["header"] = _first_header_row(doc["html"])
        doc["kind"] = _classify(doc["header"] or [])

    # Entity -> defining feed stem, from the feeds' own declarations: the
    # Summary's first "creates <b>X</b> instances" bold, then the grouped
    # header entity. On collision a *Master stem wins (it defines the
    # instances; the other feed only consumes them).
    entity_map = {}
    for doc in docs:
        if doc["kind"] != "feed":
            continue
        m = _SUMMARY_ENTITY_RE.search(doc["html"])
        candidates = [m.group(1)] if m else []
        header_entity = _header_entity(doc["header"] or [])
        if header_entity:
            candidates.append(header_entity)
        for entity in candidates:
            cur = entity_map.get(entity)
            if cur is None or (not cur.endswith("Master")
                               and doc["stem"].endswith("Master")):
                entity_map[entity] = doc["stem"]

    # Pass 2: build units.
    units = []
    for doc in docs:
        stem, kind = doc["stem"], doc["kind"]
        out_stem = common.safe_stem(stem)
        family = {"feed": "feeds", "report": "reports", "status": "status"}[kind]
        body_html = doc["html"]
        extra_first = {}

        if kind == "feed":
            tstart, tend = _table_span(body_html, doc["header_start"])
            fields, table_rows = _parse_fields(body_html, doc["header_start"],
                                               tend)
            _apply_refs(fields, entity_map, stem)
            name = _header_entity(doc["header"])
            if not name:
                m = _FEEDNAME_RE.search(body_html)
                name = m.group(1).strip() if m else stem
            # Replace the unclosed-tag source table (pandoc flattens it)
            # with a clean closed-tag rebuild carrying the same rows.
            body_html = (body_html[:tstart]
                         + _rebuild_table(doc["header"], table_rows)
                         + body_html[tend:])
            extra_first = {"entity": name, "fields": fields}

        # The first chunk carries the fields frontmatter, so shrink its
        # budget by that allowance (floor keeps the shredder sane).
        allowance = len(json.dumps(extra_first)) + 300
        chunks = common.shred_html(
            body_html, max(common.BUDGET_CHARS - allowance, 1200))
        if not chunks:
            continue

        out_first = f"{family}/{out_stem}.md"
        common.register_anchor(doc["source"], None, out_first)
        out_paths = []
        for i, (anchor, chunk_html) in enumerate(chunks, 1):
            out_path = out_first if i == 1 else f"{family}/{out_stem}/{i}.md"
            out_paths.append(out_path)
            if anchor:
                common.register_anchor(doc["source"], anchor, out_path)
            title = doc["title"] if i == 1 else f"{doc['title']} (part {i})"
            units.append(common.Unit(
                source=doc["source"],
                anchor=anchor,
                unit_type=kind,
                title=title,
                extra=extra_first if i == 1 else {},
                body_html=chunk_html,
                out_path=out_path,
            ))
        common.register_fragment_ids(doc["source"], body_html, chunks,
                                     out_paths)
    return units
