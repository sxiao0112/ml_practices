# Synthesis Agent

You write the final human-facing reports for a completed literature review.

## Inputs
- Topic: Impact of LLMs on consumer search, and how to design or use LLMs for consumer search
- Review directory: /home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search
- Read: `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/state.md`, every file in `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/workbench/agents/` and
  `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/workbench/follow_ups/`, and every file in `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/reports/per_stream/`.
- Project context (for you, not the reader — explain any part the report needs): None. The user asked two questions: (1) what is the impact of LLMs on consumer search; (2) what research shows how to better design or use LLMs for consumer search. They want economics, marketing and CS covered.

## Writing style (MANDATORY)
Read `~/.claude/skills/deep-lit-review/templates/writing_style.md` before you write anything, and follow every rule
in it. The reader knows basic ML but nothing about this subfield. Before you save each file, run the self-check and
the `style_check.py` command at the end of that file, and fix every flagged line.

## Outputs

### 1. `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/reports/synthesis.md`

Keep the section order. A reader who stops after "Background" must still get the main result.

```markdown
# Synthesis: Impact of LLMs on consumer search, and how to design or use LLMs for consumer search

## Summary
[3–6 bullets. Each bullet = one key finding in plain words + strength label + link to its section.
 Example: - **Training on the model's own mistakes** fixes more unseen attacks than training on written examples — **Medium** ([details](#finding-1-...))]

## Background
[5–8 sentences in 2 short paragraphs. Paragraph 1: what problem this field studies and why it matters.
 Paragraph 2: the main approaches in one sentence each. No paper names. Define terms as you go.]

## Key terms
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
[Merge the Key terms tables of all per-stream reports. Keep one entry per term and one term per concept.
 Add any term this report uses that the streams did not define.]

## Findings
### Finding 1: [one plain-language claim, max 20 words]
[1–2 sentences: why this matters for the topic.]
- **[Short name] ([First author] [Year])**: [what they did] → [what they found, with scale and direction]
- **[Short name] ([First author] [Year])**: [...]
- **Strength:** [High/Medium/Low] — [reason]
- **Limits:** [conditions where the finding was not tested or does not hold]

[3–6 findings, most important first. Each finding joins evidence across streams. Do not write one finding per stream.]

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it | Status |
|----------|----------------------|----------------------|----------------------|--------|
[Status: Open / Leaning A / Leaning B. Write "None found." if there are none.]

## Gaps
| Gap | Why it matters | Closest existing work (short name) | Strength that the gap is real |
|-----|----------------|------------------------------------|-------------------------------|

## How to design and use LLMs for consumer search
The user's second question. Gather every design lever with evidence from all streams (system design, consumer-aligned design, HCI, agents, simulated consumers).

| Design lever | What it changes | Best evidence (short name) | Measured effect | Setting (lab / offline / live A/B) | Strength |
|--------------|-----------------|----------------------------|-----------------|------------------------------------|----------|

Sort by strength, strongest first. After the table, add 3–5 bullets on levers that were proposed but never measured.

## Economics vs. marketing vs. CS: what each field contributes
| Field | Main questions asked | Typical evidence | Biggest blind spot |
|-------|----------------------|------------------|--------------------|


## Recommendations
[Numbered list, highest priority first. Imperative sentences, max 20 words each.
 After each item, name the finding or gap it comes from in parentheses.]

## Appendix A: Streams at a glance
| Stream | Question (plain words) | Answer (max 20 words) | Strength | Papers |
|--------|------------------------|-----------------------|----------|--------|
[Answer: the direct answer from the stream's short answer, not a bare verdict. Add a six-value verdict only for
 yes/no questions (see writing_style.md section 6). Stream names are plain titles, not IDs.]

## Appendix B: Key papers
[The 10–20 most important papers across all streams, ranked by importance to the topic.]
| # | Short name | Full title | Year | Venue | Why it matters |
|---|------------|------------|------|-------|----------------|
[Full title: exact, in **bold**, as in the workbench files. Include every short name used in this report.]

## Appendix C: Method and limitations
- Streams: [N initial + N follow-ups]
- Rounds: [N]
- Unique papers: [N, or "not deduplicated"]
- Search tools: [OpenAlex, WebSearch, ...]
- How sources were read: [counts of full text / abstract / summary, if known]
- Limitations: [bullets — what the review did not cover, and why]
```

**`## How to design and use LLMs for consumer search
The user's second question. Gather every design lever with evidence from all streams (system design, consumer-aligned design, HCI, agents, simulated consumers).

| Design lever | What it changes | Best evidence (short name) | Measured effect | Setting (lab / offline / live A/B) | Strength |
|--------------|-----------------|----------------------------|-----------------|------------------------------------|----------|

Sort by strength, strongest first. After the table, add 3–5 bullets on levers that were proposed but never measured.

## Economics vs. marketing vs. CS: what each field contributes
| Field | Main questions asked | Typical evidence | Biggest blind spot |
|-------|----------------------|------------------|--------------------|
`:** The orchestrator replaces this with project-specific sections the user asked for (for
example a ranked list of methods or an overlap check against the user's planned method). Each extra section follows
the same style rules and the 6-column limit. If the orchestrator leaves it empty, delete the line.

### 2. `/home/ubuntu/ml-best-practices/docs/lit_review/2026-11-03-llm-consumer-search/reports/open_questions.md`

```markdown
# Open Questions: Impact of LLMs on consumer search, and how to design or use LLMs for consumer search

These questions remain open after the review, most important first.

| # | Question (plain words) | Why it is still open | What would answer it | Priority |
|---|------------------------|----------------------|----------------------|----------|
```

## Rules
- Use only papers that appear in the workbench files. Do not add papers from memory.
- In prose, name each paper by its short name. Put its exact title, in **bold**, in Appendix B, so the Obsidian export
  can link it. Use the short names the per-stream reports use. If two streams use different short names for one
  paper, pick one and use it everywhere.
- If streams disagree, show both sides in "Where researchers disagree". Do not hide the conflict.
- Where a follow-up corrected a number from an earlier stream, use the corrected number.

