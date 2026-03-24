---
model: sonnet
description: Verify claims and citations in a research document using blind two-step checking. Use when the user wants to fact-check a synthesis doc, lit review, or any document with paper citations.
---

Hierarchical citation verification. You are the **top-level orchestrator** — you
do NOT read the document yourself. You delegate everything to sub-agents.

## Templates

All prompt templates are in `~/Mao/claude-toolkit/templates/verify-citations/`:

| File | Model | Purpose | Placeholders |
|------|-------|---------|-------------|
| `coordinator.txt` | sonnet | Section coordinator: extract citations, launch readers then checkers | `{file_path}`, `{start_line}`, `{end_line}`, `{reader_template_path}`, `{checker_template_path}` |
| `reader.txt` | haiku | Blind-fetch one source URL and summarize | `{url}`, `{url_fallback}` |
| `checker.txt` | haiku | Compare blind summary against claim | `{blind_summary}`, `{claim}` |
| `summarizer.txt` | haiku | Fetch and summarize one repo/dataset | `{url}` |
| `formatter.txt` | haiku | Condense raw summary to 1-2 sentences | `{raw_summary}` |

## Workflow

1. Launch a **sonnet splitter agent** that reads the target document, identifies
   sections containing citations, and returns a list of `(section_name, start_line, end_line)`.
   This keeps the document content out of your context.

2. For each section, read `coordinator.txt`, fill in the placeholders, and launch
   a **sonnet coordinator** Agent with the filled prompt. Run all in parallel as
   background agents.

3. Each coordinator:
   - Reads its section and extracts papers + claims
   - Reads `reader.txt`, fills in `{url}` per paper, launches haiku readers (parallel)
   - Waits for readers, then reads `checker.txt`, fills in `{blind_summary}` + `{claim}`, launches haiku checkers (parallel)
   - Compiles section report

4. Collect all coordinator reports and present consolidated summary:
   - Critical errors (wrong URLs, wrong authors, wrong numbers)
   - Precision issues (overstatements, imprecise descriptions)
   - Unverifiable from abstracts (flag for manual check or web search)

## For repo/dataset summarization

Same pattern: coordinator uses `summarizer.txt` → `formatter.txt` instead of
reader → checker. One coordinator for all repos+datasets.

## Known issues

- Haiku sub-agents may call Codex MCP despite instructions. Claude Code CLI
  does not support per-agent tool whitelists. Sonnet coordinators + templated
  prompts minimize this. If it persists, disable the Codex MCP server first.
- arxiv abstract pages often lack venue info. For venue checks, follow up with
  a separate round using WebSearch.
- Full paper text is at `arxiv.org/html/{id}v1` — use as `{url_fallback}`.
