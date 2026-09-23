"""Message family: each m*.htm (except mXRef.htm) shreds at its <A name>
boundaries into one message unit per anchor occurrence. The same message name
can recur inside a file (documented once per defining class, e.g. Boolean /
FALSE / TRUE), and names can differ only by case (isTrue vs isTRUE), which
collides on a case-insensitive filesystem; both cases get -2, -3... filename
suffixes while the first occurrence keeps the bare slug and the link-target
registration. mXRef.htm is the A-Z index: its letter sections are shredded
under budget with no anchor registration."""
import re

_ANCHOR_RE = re.compile(
    r"<a\s+name\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))", re.IGNORECASE)
_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def SELECTOR(path) -> bool:
    name = path.name
    return name.endswith(".htm") and name.startswith("m") \
        and not name.startswith("pma_")


def _body(path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = _FM_RE.match(text)
    return text[fm.end():] if fm else text


def _anchor_name(m) -> str:
    return next(g for g in m.groups() if g is not None)


def _message_units(path, common) -> list:
    units = []
    source = str(path)
    stem = path.stem
    cls = stem[1:]  # mObject.htm -> Object; file-based class mapping
    text = _body(path)
    matches = list(_ANCHOR_RE.finditer(text))
    used: set[str] = set()  # lowercased stems: case-insensitive filesystem
    for i, m in enumerate(matches):
        anchor = _anchor_name(m)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        base = common.slug(anchor)
        unit_stem, n = base, 1
        while unit_stem.lower() in used:
            n += 1
            unit_stem = f"{base}-{n}"
        used.add(unit_stem.lower())
        out_path = f"messages/{stem}/{unit_stem}.md"
        # First occurrence is the class's own definition and stays the link
        # target; inherited re-statements keep their own units without
        # overriding the registry entry.
        if common.resolve_anchor(source, anchor) is None:
            common.register_anchor(source, anchor, out_path)
        units.append(common.Unit(
            source=source,
            anchor=anchor,
            unit_type="message",
            title=anchor,
            extra={"class": cls},
            body_html=text[m.start():end],
            out_path=out_path,
        ))
    return units


def _xref_units(path, common) -> list:
    units = []
    source = str(path)
    text = _body(path)
    letters = list(_ANCHOR_RE.finditer(text))
    for i, m in enumerate(letters):
        letter = _anchor_name(m)
        end = letters[i + 1].start() if i + 1 < len(letters) else len(text)
        chunks = common.shred_html(text[m.start():end])
        for n, (_, chunk_html) in enumerate(chunks, 1):
            units.append(common.Unit(
                source=source,
                anchor=letter if n == 1 else None,
                unit_type="message",
                title=f"Message XRef: {letter}" if n == 1
                    else f"Message XRef: {letter} (part {n})",
                extra={},
                body_html=chunk_html,
                out_path=f"messages/mXRef/{letter}-{n}.md",
            ))
    return units


def extract(paths, common) -> list:
    units = []
    for path in paths:
        if path.stem == "mXRef":
            units.extend(_xref_units(path, common))
        else:
            units.extend(_message_units(path, common))
    return units
