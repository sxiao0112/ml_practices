# Writing Style — ASD-STE100 + Readable Layout

All human-facing files (`reports/`, `README.md`, the final message to the user) MUST follow these rules.
Workbench files are agent-facing and are exempt, except for the paper entry format in `agent_prompt.md`.

Source: ASD-STE100 Simplified Technical English, Issue 9 (https://www.asd-ste100.org). The STE
dictionary of approved words is not freely available, so apply the writing rules below and prefer the
simplest common word. Paper titles, method names, model names, metrics and field terms are
**technical names** — keep them exactly as the authors wrote them.

## 1. Words

| Rule | Do | Do not |
|------|----|--------|
| Use simple, common words | "use", "start", "show", "help", "about" | "utilize", "commence", "demonstrate", "facilitate", "regarding" |
| One word = one meaning | "test" always means an experiment | "test" for both "experiment" and "check" |
| Keep one term for one thing in the whole report | "PSO" every time | "PSO", "particle swarms", "the swarm method" for the same thing |
| Max 3 nouns in a row | "the convergence proof for PSO" | "PSO convergence proof analysis results" |
| Do not use phrasal verbs | "find", "do", "examine" | "find out", "carry out", "look into" |
| Write the article ("the", "a") | "The paper shows a gain." | "Paper shows gain." |
| No contractions or slang | "does not" | "doesn't", "a ton of" |

## 2. Verbs

- Use the active voice. Write "Smith et al. (2023) show X", not "X is shown by Smith et al.".
- Use only simple tenses: present ("PSO converges"), past ("the authors tested"), future ("this will change").
- Do not use "-ing" verb forms as the main verb ("is increasing" → "increases").
- Do not turn verbs into nouns ("perform an analysis of" → "analyze").

## 3. Sentences

- **Descriptive sentences: max 25 words.** Instructions and recommendations: max 20 words.
- One idea per sentence. Split sentences that contain "and", "which" or ";" if they carry two ideas.
- Put the most important information first.
- Write instructions in the imperative: "Read Smith (2023) first." not "It is recommended that…".

## 4. Paragraphs

- One topic per paragraph. Start with the topic sentence.
- **Max 6 sentences per paragraph.** If you need more, use a list or a table.

## 5. Layout: tables and bullets

Prefer structure over prose. A reader must get the main result in 30 seconds.

| Use a… | When the content is… | Example |
|--------|---------------------|---------|
| **Table** | 3+ items that share the same attributes | Papers (title, year, venue, finding); method comparisons; streams and their status; contradictions (claim A vs claim B, evidence) |
| **Bullet list** | 3+ parallel points with no shared attributes | Key findings; gaps; limitations; reasons |
| **Numbered list** | Steps or a ranked order | Recommended reading order; next actions by priority |
| **Short paragraph** | Reasoning that connects facts ("X, because Y, so Z") | Why two streams disagree |

Table and list rules:
- Each bullet is one sentence or one sentence fragment. Max 2 lines.
- Start parallel bullets with the same part of speech (all nouns, or all verbs).
- Keep table cells short (max ~15 words). Put long explanations below the table.
- Give every table a short heading or lead-in sentence.
- Bold the 1–3 words that carry the key fact in a bullet, not whole sentences.

## 6. Confidence

Every major claim gets a confidence label: **High**, **Medium** or **Low**, plus the reason in a few words.
Put the label in a table column or at the end of the bullet: "PSO converges under condition C — **High** (proof + 3 replications)."

## Self-check before you save a report

- [ ] No sentence is longer than 25 words (20 for recommendations).
- [ ] No paragraph is longer than 6 sentences.
- [ ] All lists of papers, methods or comparisons are tables.
- [ ] Passive voice and "-ing" main verbs are removed where an active form exists.
- [ ] The same term names the same thing everywhere.
- [ ] Each major claim has a confidence label.
