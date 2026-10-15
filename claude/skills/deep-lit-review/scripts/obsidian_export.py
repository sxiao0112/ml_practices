#!/usr/bin/env python3
"""Export a deep-lit-review output directory as an Obsidian vault.

Usage:
    python3 obsidian_export.py <review_output_dir> [--vault-root DIR | --vault-dir DIR]

By default every review goes into one shared vault, so a single Obsidian vault (and a single
Syncthing folder) holds all reviews:
    ~/lit-review-vault/                 (--vault-root; env LIT_REVIEW_VAULT)
        Index.md                        list of all reviews
        <review_dir name>/              this review, containing:
    Home.md       — map of content: topic, streams, reports, paper index
    Papers/       — one note per unique paper, with YAML frontmatter
                    (authors, year, venue, openalex, cited_by, streams) and
                    backlinks to every stream that mentions it
    Streams/      — one note per workbench agent / follow-up file
    Reports/      — synthesis, open questions, per-stream reports
    Log/          — state.md and orchestrator_log.md

Paper titles in streams and reports become [[wikilinks]], so Obsidian's graph
view, backlinks pane and (optionally) Dataview queries work out of the box.

Papers are parsed from bold-title lines in the workbench files, e.g.
    - **Paper Title** (Authors, 2024, Venue) — finding
      - OpenAlex ID: W123456
      - Cited by: 42

Re-running is safe: generated notes are overwritten, but anything you write
below a "## My notes" heading in any note is preserved. Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

MY_NOTES = "## My notes"
GENERATED_BY = "deep-lit-review"
DEFAULT_VAULT_ROOT = Path("~/lit-review-vault")
LINK_ROOT = (
    ""  # vault-relative folder of this review, e.g. "my-review/"; set in export()
)

PAPER_LINE = re.compile(
    r"^\s*(?:[-*]\s+)?\*\*(?P<title>[^*]+?)\*\*\s*"
    r"\((?P<meta>[^()]*(?:\([^()]*\)[^()]*)*)\)\s*"
    r"(?:[—–:-]+\s*(?P<finding>.*))?$"
)
YEAR = re.compile(r"\b(19|20)\d{2}\b")
YEAR_RANGE = re.compile(r"\b(?:19|20)\d{2}(?:\s*(?:[-–&/]|and)\s*(?:19|20)\d{2})*\b")
OPENALEX_ID = re.compile(r"\bW\d{6,}\b")
CITED_BY = re.compile(
    r"(?:cited by|citations?)\D{0,15}?([\d,]{1,9})|([\d,]{1,9})\s+citations",
    re.IGNORECASE,
)
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s)\]>,;]+)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
PLACEHOLDER_AUTHORS = {
    "authors",
    "authors unknown",
    "multiple authors",
    "various",
    "unknown",
    "n/a",
    "",
}


@dataclass
class Mention:
    stream: str  # stream note name
    section: str  # sub-theme heading the paper appeared under
    finding: str
    details: list[str]


@dataclass
class Paper:
    title: str
    authors: str = ""
    year: int | None = None
    venue: str = ""
    openalex: str = ""
    doi: str = ""
    cited_by: int | None = None
    mentions: list[Mention] = field(default_factory=list)
    note_name: str = ""


# ---------------------------------------------------------------- helpers


def safe_name(text: str, limit: int = 120) -> str:
    """Make text usable as an Obsidian note name / filename."""
    text = re.sub(r'[\\/:*?"<>|#^\[\]]', " ", text)
    text = re.sub(r"\s+", " ", text).strip().strip(".")
    return text[:limit].rstrip() or "Untitled"


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())


def yaml_value(value) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(yaml_value(v) for v in value) + "]"
    if value is None:
        return "null"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)  # JSON strings are valid YAML


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if value in (None, "", []):
            continue
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append(f"generated_by: {GENERATED_BY}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def write_note(path: Path, body: str) -> None:
    """Write a generated note, keeping the user's '## My notes' section."""
    preserved = f"{MY_NOTES}\n\n"
    if path.exists():
        old = path.read_text(encoding="utf-8")
        idx = old.find(MY_NOTES)
        if idx != -1:
            preserved = old[idx:]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        body.rstrip() + "\n\n" + preserved.rstrip() + "\n", encoding="utf-8"
    )


def first_heading(text: str) -> str:
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            return m.group(2).strip()
    return ""


def section(text: str, name: str) -> str:
    """Return the body of the first '## name' section (case-insensitive prefix)."""
    out, inside = [], False
    for line in text.splitlines():
        m = HEADING.match(line)
        if m and len(m.group(1)) <= 2:
            if inside:
                break
            inside = m.group(2).strip().lower().startswith(name.lower())
            continue
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def parse_meta(meta: str) -> tuple[str, int | None, str]:
    year_m = YEAR.search(meta)
    if not year_m:
        return "", None, ""
    authors = meta[: year_m.start()].strip(" ,;")
    if authors.lower() in PLACEHOLDER_AUTHORS:
        authors = ""
    range_m = YEAR_RANGE.search(meta, year_m.start())
    venue = meta[range_m.end() :].strip(" ,;") if range_m else ""
    return authors, int(year_m.group(0)), venue


# ---------------------------------------------------------------- parsing


def parse_papers(text: str, stream: str) -> list[Paper]:
    papers: list[Paper] = []
    lines = text.splitlines()
    current_section = ""
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        h = HEADING.match(line)
        if h and not in_fence:
            current_section = h.group(2).strip()
        m = None if in_fence else PAPER_LINE.match(line)
        title = m.group("title").strip() if m else ""
        if not m or title.startswith("[") or len(title) < 8:
            i += 1
            continue
        authors, year, venue = parse_meta(m.group("meta"))
        if year is None:  # bold text in parens without a year is not a citation
            i += 1
            continue
        details: list[str] = []
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                if details:
                    break
                j += 1
                continue
            if HEADING.match(nxt) or PAPER_LINE.match(nxt):
                break
            details.append(nxt.strip().lstrip("-* ").strip())
            j += 1
        blob = " ".join([m.group(0)] + details)
        oa = OPENALEX_ID.search(blob)
        doi = DOI.search(blob)
        cites = [
            int((a or b).replace(",", ""))
            for a, b in CITED_BY.findall(blob)
            if (a or b).replace(",", "")
        ]
        papers.append(
            Paper(
                title=title.rstrip(" .:"),
                authors=authors,
                year=year,
                venue=venue,
                openalex=oa.group(0) if oa else "",
                doi=doi.group(1).rstrip(".") if doi else "",
                cited_by=max(cites) if cites else None,
                mentions=[
                    Mention(
                        stream,
                        current_section,
                        (m.group("finding") or "").strip(),
                        details,
                    )
                ],
            )
        )
        i = j
    return papers


def merge(papers: list[Paper]) -> list[Paper]:
    by_key: dict[str, Paper] = {}
    oa_to_key: dict[str, str] = {}
    for p in papers:
        key = oa_to_key.get(p.openalex) if p.openalex else None
        key = key or norm_title(p.title)
        if key not in by_key:
            by_key[key] = p
        else:
            q = by_key[key]
            q.authors = q.authors or p.authors
            q.year = q.year or p.year
            q.venue = q.venue or p.venue
            q.openalex = q.openalex or p.openalex
            q.doi = q.doi or p.doi
            if p.cited_by is not None:
                q.cited_by = max(q.cited_by or 0, p.cited_by)
            q.mentions.extend(p.mentions)
        if by_key[key].openalex:
            oa_to_key[by_key[key].openalex] = key
    merged = list(by_key.values())
    used: set[str] = set()
    for p in sorted(merged, key=lambda p: (-(p.cited_by or 0), p.title)):
        name = safe_name(p.title)
        if name.lower() in used:
            name = safe_name(f"{p.title} ({p.year})") if p.year else name
        n = 2
        base = name
        while name.lower() in used:
            name = f"{base} {n}"
            n += 1
        used.add(name.lower())
        p.note_name = name
    return merged


# ---------------------------------------------------------------- linkify


class Linker:
    """Turn paper titles in markdown into [[wikilinks]] to paper notes."""

    def __init__(self, papers: list[Paper]):
        self.target: dict[str, str] = {}
        for p in papers:
            self.target.setdefault(p.title.lower(), f"{LINK_ROOT}Papers/{p.note_name}")
        titles = sorted({p.title for p in papers}, key=len, reverse=True)
        alt = "|".join(re.escape(t) for t in titles) or r"(?!x)x"
        long_titles = [t for t in titles if len(t.split()) >= 5]
        long_alt = "|".join(re.escape(t) for t in long_titles) or r"(?!x)x"
        self.bold = re.compile(r"\*\*(" + alt + r")\*\*", re.IGNORECASE)
        # Long titles are distinctive enough to link anywhere; short ones only when bolded
        # or alone in a table cell, so "Particle Swarm Optimization" in prose stays prose.
        self.plain = re.compile(
            r"(?<![\[\w])(" + long_alt + r")(?![\w\]])", re.IGNORECASE
        )
        self.cell = re.compile(r"(\|\s*)(" + alt + r")(\s*\|)", re.IGNORECASE)

    def link(self, title: str, in_table: bool) -> str:
        target = self.target.get(title.lower())
        if not target:
            return title
        sep = "\\|" if in_table else "|"
        return f"[[{target}{sep}{title}]]"

    def __call__(self, text: str) -> str:
        out, in_fence = [], False
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence or HEADING.match(line):
                out.append(line)
                continue
            table = line.lstrip().startswith("|")
            line = self.bold.sub(
                lambda m, t=table: f"**{self.link(m.group(1), t)}**", line
            )
            if table:
                line = self.cell.sub(
                    lambda m: m.group(1) + self.link(m.group(2), True) + m.group(3),
                    line,
                )
            # only link plain mentions outside existing links
            parts = re.split(r"(\[\[.*?\]\])", line)
            parts = [
                p
                if p.startswith("[[")
                else self.plain.sub(lambda m, t=table: self.link(m.group(1), t), p)
                for p in parts
            ]
            out.append("".join(parts))
        return "\n".join(out)


# ---------------------------------------------------------------- render


def pretty(stem: str) -> str:
    return safe_name(stem.replace("_", " ").strip())


def stream_note_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    title = first_heading(text)
    label = f"{path.stem.split('_', 1)[0]} {title}" if title else pretty(path.stem)
    return safe_name(label, 100)


def paper_body(p: Paper) -> str:
    fm = {
        "title": p.title,
        "authors": p.authors,
        "year": p.year,
        "venue": p.venue,
        "openalex": f"https://openalex.org/{p.openalex}" if p.openalex else "",
        "doi": f"https://doi.org/{p.doi}" if p.doi else "",
        "cited_by": p.cited_by,
        "streams": sorted(
            {f"[[{LINK_ROOT}Streams/{m.stream}|{m.stream}]]" for m in p.mentions}
        ),
        "tags": ["paper"],
    }
    lines = [frontmatter(fm) + f"# {p.title}", ""]
    meta = " · ".join(x for x in [p.authors, str(p.year or ""), p.venue] if x)
    if meta:
        lines += [meta, ""]
    links = []
    if p.openalex:
        links.append(f"[OpenAlex](https://openalex.org/{p.openalex})")
    if p.doi:
        links.append(f"[DOI](https://doi.org/{p.doi})")
    q = re.sub(r"\s+", "+", p.title)
    links.append(f"[Google Scholar](https://scholar.google.com/scholar?q={q})")
    lines += [" · ".join(links), "", "## Mentioned in", ""]
    for m in p.mentions:
        where = f"[[{LINK_ROOT}Streams/{m.stream}|{m.stream}]]" + (
            f" › {m.section}" if m.section else ""
        )
        lines.append(f"### {where}")
        if m.finding:
            lines.append(m.finding)
        lines += [f"- {d}" for d in m.details]
        lines.append("")
    return "\n".join(lines)


def stream_body(
    name: str, src: Path, papers: list[Paper], linker: Linker, kind: str
) -> str:
    text = src.read_text(encoding="utf-8")
    mine = sorted(
        (p for p in papers if any(m.stream == name for m in p.mentions)),
        key=lambda p: (-(p.cited_by or 0), p.title),
    )
    fm = {
        "title": first_heading(text) or name,
        "kind": kind,
        "source": str(src),
        "paper_count": len(mine),
        "tags": ["stream"],
    }
    tldr = re.sub(r"(?:\n\s*(?:-{3,}|\*{3,})\s*)+$", "", section(text, "TL;DR")).strip()
    head = [frontmatter(fm)]
    if tldr:
        head += ["> [!summary] TL;DR", *[f"> {l}" for l in tldr.splitlines()], ""]
    head += [f"## Papers ({len(mine)})", ""]
    head += [
        f"- [[{LINK_ROOT}Papers/{p.note_name}|{p.title}]]"
        + (f" ({p.year})" if p.year else "")
        + (f" — {p.cited_by} cites" if p.cited_by else "")
        for p in mine
    ]
    head += ["", "---", ""]
    return "\n".join(head) + linker(strip_frontmatter(text))


def report_body(src: Path, linker: Linker, tag: str) -> str:
    text = src.read_text(encoding="utf-8")
    fm = {
        "title": first_heading(text) or pretty(src.stem),
        "source": str(src),
        "tags": [tag],
    }
    return frontmatter(fm) + linker(strip_frontmatter(text))


def home_body(
    topic: str,
    streams: list[str],
    reports: list[str],
    logs: list[str],
    papers: list[Paper],
) -> str:
    lines = [
        frontmatter({"title": topic, "tags": ["lit-review", "moc"]}) + f"# {topic}",
        "",
    ]
    lines += [f"{len(streams)} streams · {len(papers)} unique papers", ""]
    if reports:
        lines += [
            "## Reports",
            "",
            *[f"- [[{LINK_ROOT}Reports/{r}|{r}]]" for r in reports],
            "",
        ]
    lines += [
        "## Streams",
        "",
        *[f"- [[{LINK_ROOT}Streams/{s}|{s}]]" for s in streams],
        "",
    ]
    if logs:
        lines += [
            "## Orchestration",
            "",
            *[f"- [[{LINK_ROOT}Log/{l}|{l}]]" for l in logs],
            "",
        ]
    lines += [
        "## Papers",
        "",
        "Sorted by citation count. With the Dataview plugin you can query these notes directly, e.g.:",
        "",
        "```dataview",
        f'TABLE year, venue, cited_by, streams FROM "{LINK_ROOT}Papers" SORT cited_by DESC',
        "```",
        "",
        "| Paper | Year | Venue | Cited by | Streams |",
        "|---|---|---|---|---|",
    ]
    for p in sorted(papers, key=lambda p: (-(p.cited_by or 0), p.title)):
        streams_s = ", ".join(
            sorted(
                {
                    f"[[{LINK_ROOT}Streams/{m.stream}\\|{m.stream.split(' ', 1)[0]}]]"
                    for m in p.mentions
                }
            )
        )
        venue = p.venue.replace("|", "/")
        lines.append(
            f"| [[{LINK_ROOT}Papers/{p.note_name}\\|{p.title}]] | {p.year or ''} | {venue} | {p.cited_by or ''} | {streams_s} |"
        )
    return "\n".join(lines)


GRAPH_JSON = {
    "colorGroups": [
        {"query": "path:Papers", "color": {"a": 1, "rgb": 5431473}},
        {"query": "path:Streams", "color": {"a": 1, "rgb": 14701138}},
        {"query": "path:Reports", "color": {"a": 1, "rgb": 11657298}},
    ]
}


def export(review_dir: Path, vault: Path, vault_root: Path) -> None:
    global LINK_ROOT
    rel = vault.relative_to(vault_root).as_posix()
    LINK_ROOT = "" if rel == "." else rel + "/"
    wb = review_dir / "workbench"
    stream_files = sorted((wb / "agents").glob("*.md")) + sorted(
        (wb / "follow_ups").glob("*.md")
    )
    if not stream_files:
        sys.exit(f"No workbench files found under {wb}/agents or {wb}/follow_ups")

    stream_names: list[tuple[Path, str, str]] = []
    all_papers: list[Paper] = []
    for f in stream_files:
        name = stream_note_name(f)
        kind = "follow-up" if f.parent.name == "follow_ups" else "agent"
        stream_names.append((f, name, kind))
        all_papers.extend(parse_papers(f.read_text(encoding="utf-8"), name))
    papers = merge(all_papers)
    linker = Linker(papers)

    for p in papers:
        write_note(vault / "Papers" / f"{p.note_name}.md", paper_body(p))
    for f, name, kind in stream_names:
        write_note(
            vault / "Streams" / f"{name}.md", stream_body(name, f, papers, linker, kind)
        )

    reports: list[str] = []
    rdir = review_dir / "reports"
    report_files = [rdir / "synthesis.md", rdir / "open_questions.md"] + sorted(
        (rdir / "per_stream").glob("*.md")
    )
    for f in report_files:
        if f.exists():
            name = (
                pretty(f.stem).title()
                if f.parent == rdir
                else f"Stream report - {pretty(f.stem)}"
            )
            write_note(
                vault / "Reports" / f"{name}.md", report_body(f, linker, "report")
            )
            reports.append(name)

    logs: list[str] = []
    for f, name in [
        (review_dir / "state.md", "State"),
        (wb / "orchestrator_log.md", "Orchestrator log"),
    ]:
        if f.exists():
            write_note(vault / "Log" / f"{name}.md", report_body(f, linker, "log"))
            logs.append(name)

    topic = ""
    for f in (review_dir / "README.md", review_dir / "state.md"):
        if f.exists():
            text = f.read_text(encoding="utf-8")
            m = re.search(r"^- Topic:\s*(.+)$", text, re.MULTILINE)
            topic = m.group(1).strip() if m else first_heading(text)
            if topic:
                break
    topic = topic or review_dir.name
    write_note(
        vault / "Home.md",
        home_body(topic, [n for _, n, _ in stream_names], reports, logs, papers),
    )

    graph = vault_root / ".obsidian" / "graph.json"
    if not graph.exists():
        graph.parent.mkdir(parents=True, exist_ok=True)
        graph.write_text(json.dumps(GRAPH_JSON, indent=2) + "\n", encoding="utf-8")

    print(f"Obsidian vault: {vault}")
    print(
        f"  {len(papers)} papers ({len(all_papers)} mentions), {len(stream_names)} streams, {len(reports)} reports"
    )
    print("  Open the vault folder in Obsidian ('Open folder as vault'), then start from Index.md or Home.md")


def write_index(vault_root: Path) -> None:
    reviews = sorted(h.parent for h in vault_root.glob("*/Home.md"))
    lines = [
        frontmatter({"title": "Literature reviews", "tags": ["moc"]})
        + "# Literature reviews",
        "",
    ]
    lines += ["| Review | Topic | Papers |", "|---|---|---|"]
    for r in reviews:
        text = (r / "Home.md").read_text(encoding="utf-8")
        topic = first_heading(strip_frontmatter(text))
        count = len(list((r / "Papers").glob("*.md")))
        lines.append(
            f"| [[{r.name}/Home\\|{r.name}]] | {topic.replace('|', '/')} | {count} |"
        )
    write_note(vault_root / "Index.md", "\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("review_dir", type=Path, help="deep-lit-review output directory")
    where = ap.add_mutually_exclusive_group()
    where.add_argument(
        "--vault-root",
        type=Path,
        help="shared vault (default: $LIT_REVIEW_VAULT or ~/lit-review-vault)",
    )
    where.add_argument(
        "--vault-dir", type=Path, help="write a standalone vault to exactly this folder"
    )
    args = ap.parse_args()
    review_dir = args.review_dir.expanduser().resolve()
    if not review_dir.is_dir():
        sys.exit(f"Not a directory: {review_dir}")
    if args.vault_dir:
        vault = args.vault_dir.expanduser().resolve()
        export(review_dir, vault, vault)
        return
    root = args.vault_root or Path(
        os.environ.get("LIT_REVIEW_VAULT", DEFAULT_VAULT_ROOT)
    )
    root = root.expanduser().resolve()
    export(review_dir, root / review_dir.name, root)
    write_index(root)


if __name__ == "__main__":
    main()
