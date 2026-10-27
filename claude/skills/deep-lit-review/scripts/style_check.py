#!/usr/bin/env python3
"""Mechanical style check for deep-lit-review reports (rules in templates/writing_style.md).

Usage:
    python3 style_check.py <report.md | reports_dir> [...]

Flags, per line:
    long-sentence   prose sentence > 25 words (> 20 in a Recommendations section)
    long-paragraph  paragraph > 4 sentences, or bullet > 2 sentences
    semicolon       ';' in prose or a table cell
    long-cell       table cell > 20 words (cells that are only a **bold title** are exempt)
    wide-table      table with > 6 columns
    long-bold       bold span of 6+ words outside a table (a full title used in prose)
    internal-ref    stream IDs (f1_02), round numbers, "our design"
    undefined-term  acronym not in the page's Key terms table and not defined as "TERM (...)"

Exit code 0 = clean, 1 = flagged lines, 2 = bad arguments. Stdlib only.
A clean result does not prove the page is readable; it only removes mechanical problems.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_SENTENCE = 25
MAX_RECOMMENDATION = 20
MAX_PARAGRAPH = 4
MAX_BULLET = 2
MAX_CELL = 20
MAX_COLUMNS = 6
LONG_BOLD = 6

# Terms a reader with basic ML knows, plus venues and sources that need no definition.
KNOWN = {
    "AI", "ML", "LLM", "LLMs", "GPU", "GPUs", "API", "APIs", "PDF", "URL", "HTML", "ID", "IDs", "US", "UK",
    "OK", "TL;DR", "NeurIPS", "ICML", "ICLR", "ACL", "EMNLP", "NAACL", "AAAI", "IJCAI", "CVPR", "TMLR",
    "COLM", "arXiv", "OpenReview", "OpenAlex", "LessWrong", "OpenAI", "DeepMind", "GitHub", "WebSearch",
    "WebFetch", "DOI", "RL", "KL", "QA", "OOD",
}
# All-caps emphasis words are not acronyms (STE also discourages them, but that is not this check).
EMPHASIS = {
    "YES", "NO", "NOT", "AND", "OR", "ONLY", "ALL", "NEVER", "MUST", "EXACTLY", "ALWAYS", "NONE", "ANY",
    "SAFETY", "BEHAVIOR", "POSITIVE", "NEGATIVE", "ALIGNED", "DESIRABLE", "CONFESSION", "MANDATORY",
}
# Model family names are self-explanatory enough (e.g. Qwen2.5-7B, GPT-4.1, DS-Llama-8B).
MODEL = re.compile(r"(GPT|Qwen|Llama|Claude|Gemini|Gemma|DeepSeek|Mistral|Mixtral|Phi|OLMo|DS)\b|\d+(\.\d+)?[BM]$")
ACRONYM = re.compile(r"(?<![\w/#.-])([A-Za-z]*[A-Z][a-z0-9]*[A-Z][A-Za-z0-9]*(?:[+-][A-Za-z0-9]+)*)(?![\w/])")
INTERNAL = [
    (re.compile(r"\bf\d+_\d+\b"), "stream ID"),
    (re.compile(r"\bround[- ]?\d\b", re.IGNORECASE), "round number"),
    (re.compile(r"\bour design\b", re.IGNORECASE), '"our design"'),
]
ABBREV = re.compile(r"\b(et al|e\.g|i\.e|vs|Fig|Figs|Eq|Tab|approx|cf|No)\.", re.IGNORECASE)
SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9*\[(\"'])")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)")


def plain(text: str) -> str:
    text = LINK.sub(r"\1", text)
    text = re.sub(r"`[^`]*`", "code", text)
    return text.replace("**", "").replace("__", "")


def sentences(text: str) -> list[str]:
    text = ABBREV.sub(lambda m: m.group(1) + "\x00", plain(text))
    text = re.sub(r"(\d)\.(\d)", "\\1\x00\\2", text)
    return [s.replace("\x00", ".") for s in SPLIT.split(text.strip()) if len(s.split()) >= 3]


def cells(line: str) -> list[str]:
    body = line.strip().strip("|")
    return [c.strip() for c in re.split(r"(?<!\\)\|", body)]


def is_rule(line: str) -> bool:
    return bool(re.fullmatch(r"\|?[\s:|-]+\|?", line.strip())) and "-" in line


def defined_terms(lines: list[str]) -> set[str]:
    """Terms from any table whose first header cell is 'Term', plus 'TERM (definition)' uses."""
    terms: set[str] = set()
    in_terms = False
    for line in lines:
        if line.lstrip().startswith("|"):
            row = cells(line)
            if row and row[0].lower() == "term":
                in_terms = True
                continue
            if in_terms and not is_rule(line) and row:
                for t in re.split(r"[,/]| or ", plain(row[0])):
                    t = re.sub(r"\s*\(.*?\)\s*", " ", t).strip()
                    if t:
                        terms.add(t.lower())
                        terms.update(a.lower() for a in ACRONYM.findall(t))
        else:
            in_terms = False
        for m in re.finditer(r"\b([A-Za-z][\w+.-]*[A-Z][\w+.-]*)\s+\(", plain(line)):
            terms.add(m.group(1).lower())
    return terms


def check(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8").splitlines()
    terms = defined_terms(raw)
    issues: list[str] = []
    seen_undefined: set[str] = set()
    in_fence = in_details = False
    section = ""
    para: list[tuple[int, str]] = []
    skip_table = False  # paper reference tables: titles and venues are exempt from term checks

    def flag(n: int, rule: str, msg: str) -> None:
        issues.append(f"{path}:{n}: [{rule}] {msg}")

    def flush() -> None:
        if not para:
            return
        text = " ".join(t for _, t in para)
        if len(sentences(text)) > MAX_PARAGRAPH:
            flag(para[0][0], "long-paragraph", f"{len(sentences(text))} sentences (max {MAX_PARAGRAPH})")
        para.clear()

    def terms_in(n: int, text: str) -> None:
        # drop bold spans long enough to be paper titles; pair ** left to right
        text = re.sub(r"\*\*(.+?)\*\*", lambda m: " " if len(m.group(1)) >= 20 else m.group(1), text)
        for tok in ACRONYM.findall(plain(text)):
            core = tok.rstrip("s") if tok.endswith("s") and tok[:-1].isupper() else tok
            if core in KNOWN or tok in KNOWN or tok in EMPHASIS or MODEL.search(core) or re.match(r"Ma?c[A-Z][a-z]", tok):
                continue
            if core.lower() in terms or tok.lower() in terms or core.lower() in seen_undefined:
                continue
            seen_undefined.add(core.lower())
            flag(n, "undefined-term", f"'{tok}' is not in Key terms and not defined on first use")

    for n, line in enumerate(raw, 1):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            flush()
            continue
        if in_fence:
            continue
        if s.startswith("<details"):
            in_details = True
        if in_details:
            in_details = "</details>" not in s
            continue
        h = HEADING.match(s)
        if h:
            flush()
            section = h.group(2).lower()
            continue
        if not s:
            flush()
            skip_table = False
            continue

        for rx, what in INTERNAL:
            if rx.search(plain(s)) and "appendix c" not in section and "method" not in section:
                flag(n, "internal-ref", f"{what}: '{rx.search(plain(s)).group(0)}'")

        if s.startswith("|"):
            flush()
            if is_rule(s):
                continue
            row = cells(s)
            low = [c.lower() for c in row]
            if any(c in ("full title", "paper", "title") for c in low) and not skip_table:
                skip_table = True
                if len(row) > MAX_COLUMNS:
                    flag(n, "wide-table", f"{len(row)} columns (max {MAX_COLUMNS})")
                continue
            if not skip_table and len(row) > MAX_COLUMNS:
                flag(n, "wide-table", f"{len(row)} columns (max {MAX_COLUMNS})")
            for c in row:
                if re.fullmatch(r"\*\*[^*]+\*\*", c):
                    continue
                words = len(plain(c).split())
                if words > MAX_CELL:
                    flag(n, "long-cell", f"{words} words (max {MAX_CELL}): '{plain(c)[:60]}...'")
                if ";" in plain(c):
                    flag(n, "semicolon", f"in table cell: '{plain(c)[:60]}'")
            if not skip_table:
                terms_in(n, s)
            continue

        skip_table = False
        terms_in(n, s)
        for m in re.finditer(r"\*\*([^*]+)\*\*", s):
            if len(m.group(1).split()) >= LONG_BOLD:
                flag(n, "long-bold", f"long bold in prose: '{m.group(1)[:60]}' (bold 1-3 words; name papers by short name)")
        if ";" in plain(s).replace("TL;DR", ""):
            flag(n, "semicolon", "in prose (write two sentences or a list)")

        bullet = re.match(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)", line)
        limit = MAX_RECOMMENDATION if "recommendation" in section else MAX_SENTENCE
        for sent in sentences(bullet.group(1) if bullet else s):
            if len(sent.split()) > limit:
                flag(n, "long-sentence", f"{len(sent.split())} words (max {limit}): '{sent[:60]}...'")
        if bullet:
            flush()
            if len(sentences(bullet.group(1))) > MAX_BULLET:
                flag(n, "long-paragraph", f"bullet has {len(sentences(bullet.group(1)))} sentences (max {MAX_BULLET})")
        else:
            para.append((n, s))
    flush()
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    files: list[Path] = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            files += sorted(p.rglob("*.md"))
        elif p.is_file():
            files.append(p)
        else:
            print(f"Not found: {p}", file=sys.stderr)
            return 2
    total = 0
    by_rule: dict[str, int] = {}
    for f in files:
        issues = check(f)
        total += len(issues)
        for i in issues:
            print(i)
            rule = i.split("[", 1)[1].split("]", 1)[0]
            by_rule[rule] = by_rule.get(rule, 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(by_rule.items(), key=lambda kv: -kv[1]))
    print(f"\n{len(files)} files, {total} flagged lines" + (f" ({summary})" if summary else ""))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
