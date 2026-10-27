# Writing Style — Readable for a Newcomer + ASD-STE100

All human-facing files (`reports/`, `README.md`, the final message to the user) MUST follow these rules.
This file is the only copy of the rules. Templates point here and do not repeat them.
Workbench files are agent-facing and are exempt, except for the paper entry format in `agent_prompt.md`.

## 0. The reader

Write for a reader who knows basic ML but nothing about this subfield.

| The reader knows | The reader does NOT know |
|------------------|--------------------------|
| Training, fine-tuning, loss, gradient, benchmark, accuracy, train/test split, LLM, prompt | The subfield's acronyms, methods, benchmarks, metrics, paper nicknames, or open debates |
| How to read a results table | What a score means on a benchmark they have not seen |
| — | Anything from the user's project or from this review's internal files |

Rules that follow from this:

1. **Define every term the reader does not know.** Put it in the page's **Key terms** table, or define it in the same
   sentence the first time ("SFT (supervised fine-tuning on example answers)"). This includes acronyms, method names,
   benchmark names, metric names, and subfield words such as "on-policy" or "prefill".
2. **Give every number its meaning.** State the scale and which direction is better, and name the comparison.
   Write "attack success 8% vs 22% without masking (lower is safer)", not "ASR 8.00 vs 22.40".
3. **Name papers by a short name in prose.** Use the method name or "First-author Year", e.g. "RECAP (Chen 2025)".
   Put the exact full title in **bold** in the **Papers cited** table, so each short name has one exact title.
   Do not use a full title as the subject of a sentence.
4. **Do not use internal references.** Do not write stream IDs ("f1_02"), round numbers, "our design" or file names in
   the text. Say what they mean ("a follow-up check of the key numbers", "the user's planned method: …").
5. **Explain before you compare.** Say what a method does in plain words before you rank it or quote its score.

## 1. Words (ASD-STE100)

Source: ASD-STE100 Simplified Technical English, Issue 9 (https://www.asd-ste100.org). The STE dictionary of approved
words is not freely available, so apply the writing rules below and prefer the simplest common word. Paper titles,
method names, model names, metrics and field terms are **technical names** — keep them exactly as the authors wrote
them, and define them (rule 0.1).

| Rule | Do | Do not |
|------|----|--------|
| Use simple, common words | "use", "start", "show", "help", "about" | "utilize", "commence", "demonstrate", "facilitate", "regarding" |
| One word = one meaning | "test" always means an experiment | "test" for both "experiment" and "check" |
| Keep one term for one thing in the whole report | "PSO" every time | "PSO", "particle swarms", "the swarm method" for the same thing |
| Max 3 nouns in a row | "the rate of false corrections on aligned starts" | "aligned-start false-correction rate" |
| Do not use phrasal verbs | "find", "do", "examine" | "find out", "carry out", "look into" |
| Write the article ("the", "a") | "The paper shows a gain." | "Paper shows gain." |
| No contractions or slang | "does not" | "doesn't", "a ton of" |

## 2. Verbs

- Use the active voice. Write "Smith et al. (2023) show X", not "X is shown by Smith et al.".
- Use only simple tenses: present ("PSO converges"), past ("the authors tested"), future ("this will change").
- Do not use "-ing" verb forms as the main verb ("is increasing" → "increases").
- Do not turn verbs into nouns ("perform an analysis of" → "analyze").

## 3. Sentences

- **Descriptive sentences: max 25 words.** Instructions and recommendations: max 20 words. A short paper name counts
  as its words. This is one more reason not to put full titles in prose.
- One idea per sentence. Split sentences that contain "and", "which" or ";" if they carry two ideas.
- **Do not use semicolons.** Write two sentences or a list.
- Put the most important information first.
- Write instructions in the imperative: "Read Smith (2023) first." not "It is recommended that…".

## 4. Paragraphs

- One topic per paragraph. Start with the topic sentence.
- **Max 4 sentences per paragraph.** If you need more, use a list or a table.

## 5. Layout: tables and bullets

Prefer structure over prose. A reader must get the main result in 30 seconds.

| Use a… | When the content is… | Example |
|--------|---------------------|---------|
| **Table** | 3+ items that share the same attributes | Papers; approaches; streams and their verdicts; disagreements (view A vs view B) |
| **Bullet list** | 3+ parallel points with no shared attributes | Conditions in a short answer; gaps; limitations |
| **Numbered list** | Steps or a ranked order | Reading order; next actions by priority |
| **Short paragraph** | Reasoning that connects facts ("X, because Y, so Z") | Why two papers disagree |

Table and list rules:
- **Table cells: max 20 words and one fact per cell.** No semicolons in cells. If a cell needs two facts, add a
  column or put the detail below the table.
- **Max 6 columns per table.** Split wider tables.
- Each bullet is one sentence or one sentence fragment. Max 2 lines.
- Start parallel bullets with the same part of speech (all nouns, or all verbs).
- Give every table a short lead-in sentence that says what the table shows.
- Bold the 1–3 words that carry the key fact in a bullet, not whole sentences.

## 6. Verdicts and confidence

**Verdict scale.** Most research questions do not have a yes/no answer. Use one of these six values, then explain
the conditions in bullets:

| Verdict | Use when |
|---------|----------|
| **Yes** | Direct, consistent evidence supports it |
| **Mostly yes** | Supported, with clear exceptions or limits |
| **Mixed** | It depends on conditions, or strong evidence points both ways |
| **Mostly no** | Not supported, with some exceptions |
| **No** | Direct evidence shows it is false |
| **No evidence** | Nobody has tested it directly (say what the closest work is) |

**Two separate labels.** Do not mix them:
- **Strength of evidence** (High / Medium / Low): how strong the result is. Give the reason in a few words: number of
  models, seeds, replications, peer review.
- **How we read it** (full text / abstract / summary): how much of the source the agent actually read. Put this in
  the **Papers cited** table only.

Every major claim gets a strength label and a short reason: "Masking helps — **Medium** (one model, one run)."

## Self-check before you save a report

- [ ] Every acronym, method, benchmark and metric is in **Key terms** or defined on first use.
- [ ] Every number has its scale, its direction (higher or lower is better), and its comparison.
- [ ] No full paper title is a sentence subject. Every short name appears in **Papers cited** with its exact title.
- [ ] No stream IDs, round numbers, file names or "our design" in the text.
- [ ] No sentence is longer than 25 words (20 for recommendations). No semicolons.
- [ ] No paragraph is longer than 4 sentences. No table cell is longer than 20 words. No table has more than 6 columns.
- [ ] Passive voice and "-ing" main verbs are removed where an active form exists.
- [ ] The same term names the same thing everywhere.
- [ ] Each major claim has a strength label and a reason.

Then run the checker and fix every flagged line:

```bash
python3 ~/.claude/skills/deep-lit-review/scripts/style_check.py <report file>
```

The checker finds only mechanical problems (length, semicolons, undefined acronyms, internal IDs, wide tables).
A clean result does not prove the page is readable. The checklist above still applies.
