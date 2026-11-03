# Using LLMs to model and study consumer search

**Question:** Can LLMs stand in for real consumers in surveys, price tests and search studies, and where do they fail?

## Short answer
**Answer:** LLMs stand in for consumers as survey respondents, price testers, shoppers and search users. Aggregate patterns match human data best. Individual answers, subgroup differences and search-level choices match poorly.

**Strength:** Medium (a few research groups, mostly preprints, and no tests against real purchases).
- **Holds when:** Survey questions ask about purchase intent on a 5-point scale. Free-text answers reach about 90% of human test-retest reliability in one 57-survey study (Maier 2025).
- **Does not hold when:** Tests need individual answers or subgroup regression slopes. Individual fit is weak, and some subgroup slopes flip sign (Chen 2026 and Bisbee 2024).
- **Still unknown:** Whether simulated consumers predict real purchases, live click behavior, or real search and ranking choices.

## Background
Surveys and product tests cost time and money. Researchers ask whether LLMs can replace some respondents, shoppers or users. The question is how closely such stand-ins match real choices, and where they break. The answer affects pricing, interface design and search research.

Key terms used on this page:

| Term | Plain meaning |
|------|---------------|
| Silicon sample | Many LLM answers, each given a different persona, that mimic a human survey sample. |
| Persona | A written profile of a fictional respondent, with traits such as age, income and views. |
| Purchase intent | A respondent's stated likelihood of buying a product, usually on a 1 to 5 scale. |
| Likert scale | A rating scale, such as 1 (very unlikely) to 5 (very likely). |
| Test-retest reliability | How consistent answers are when the same respondent answers twice. |
| SSR | Semantic similarity rating: the LLM writes free text, which is mapped to a scale by meaning. |
| Willingness to pay | The highest price a buyer will pay for a product or feature. |
| BASES | A 2024 LLM simulator of web search users, tested on query and click data. |
| USimAgent | A 2025 LLM simulator of search users that models querying, clicking and stopping. |
| PAARS | A 2025 shopper simulator built from personas induced from shopping sessions. |
| NIM | Nuremberg Institute for Market Decisions, which publishes the review cited here. |
| Conjoint analysis | A survey where people choose between product profiles that mix several features. |
| Choice model | A model that predicts which option a person picks, based on option features. |
| Structural model | A model built on explicit economic assumptions, such as search costs, that explains choices. |
| Subgroup | A demographic group, such as an age band or income band. |
| Regression slope | The estimated change in an answer for a one-unit change in a trait. |
| Variance compression | Simulated answers bunch near the middle, so their spread is smaller than human spread. |
| Mode collapse | An LLM gives the same typical answer across repeated calls. |
| Positivity bias | A tendency to rate products or attitudes more favorably than true views. |
| Digital twin | An LLM persona built from one real person's answers to many questions. |
| A/B test | A randomized comparison of two versions of a page, product or offer. |
| Simulator | An LLM agent that acts as a user inside a simulated website or search engine. |
| Top-1 click agreement | How often the simulator's top click matches the human's top click. |
| Exploratory search task | A search where the user does not know the target at the start and learns as they go. |

## Main approaches
The table lists the main ways researchers attack this question. Status shows how settled each approach is.

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Silicon samples from demographics | Give an LLM a demographic backstory, then ask a survey question. | Argyle 2023, Dillion 2023 | Contested |
| Free-text rating (SSR) | The LLM writes a reaction, which is mapped to a scale. | Maier 2025, SSR fix 2026 | Emerging |
| LLM willingness to pay | The LLM answers choice tasks, then a choice model estimates willingness to pay. | Brand 2024, Brand 2025, Reusens 2026, Demand 2026 | Contested |
| Shopper and search simulators | Persona agents search, click and choose on a simulated site. | BASES 2024, USimAgent 2025, PAARS 2025, Customer-sim 2025 | Emerging |
| Digital twins for A/B tests | Persona agents, calibrated on real user data, predict test results. | Twin 2025, Persona A/B 2026, Flexible budget 2026 | Emerging |
| Validity audits | Compare simulated answers with human data for individuals and groups. | Bisbee 2024, Tigre 2026, Chen 2026 | Emerging |

## What the evidence shows
### Finding 1: Simulated answers match aggregate survey patterns in some product studies.
- **Maier 2025**: Across 57 personal-care surveys, free-text ratings reached about 90% of human test-retest reliability.
- **Argyle 2023**: GPT-3 given real respondents' backstories matched answer patterns of many U.S. subgroups.
- **Strength:** Medium. The strongest number comes from one team and one data set. Argyle's test used an older model.

### Finding 2: Individual answers match real people poorly.
- **Chen 2026**: Four models on U.S. and cross-cultural survey data. No model beats the strongest baseline for individuals.
- **Twin 2025**: A follow-up study of 19 tasks, reported in a secondary summary, found about 75% individual accuracy. Twins varied less than humans in 93.9% of cases.
- **Strength:** Medium. Two separate test sets agree, but most numbers come from abstracts.

### Finding 3: Subgroup differences and regression slopes get distorted.
- **Bisbee 2024**: Synthetic regression slopes often differ from real survey slopes. Some flip sign.
- **Wang 2025**: Fine-tuning on about 30 human observations improved spread but did not recover the original regression coefficients.
- **Tigre 2026**: Subgroup errors reached 10 to 30 points. A simple correction works only when missing answers are random.
- **Strength:** Medium. Three papers agree. The Bisbee finding comes from a search summary that names another author, so check it before citing.

### Finding 4: Stated willingness to pay has realistic size but shifts at the attribute level.
- **Brand 2024**: GPT-3.5 willingness-to-pay values had realistic size and followed economic patterns. The authors' slides cite about $3 for all 10,800 responses.
- **Reusens 2026**: Attribute-level willingness to pay deviated from human benchmarks and ran higher overall. Prompts shifted the values.
- **Demand 2026**: Demographics alone failed to recover preferences. The best prompt reversed the human ranking of attributes.
- **Strength:** Low. These results come from a conference abstract, a journal summary and a cost claim from slides.

### Finding 5: Search and shopper simulators match wording and some clicks, but fail on exploratory tasks.
- **BASES 2024**: Simulated queries overlapped 90.8% of terms with human queries. Top-1 click agreement was 51%.
- **Efficacy 2025**: In 32 real and 32 matched simulated sessions, simulations matched factual tasks. They underperformed on exploratory tasks.
- **Fulman 2025**: Simulated parking choices favored the first option shown, a sign of order effects.
- **Strength:** Low. Samples are small, the studies are few, and the tasks differ.

## Where researchers disagree
The table lists the main open disputes and what would settle each.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Is aggregate fit enough? | Maier 2025: about 90% reliability supports use. | Chen 2026 and Tigre 2026: aggregate fit hides individual errors. | Test on new products with real purchases. |
| Are simulated panels too positive? | NIM review: yes, positive attitudes are overstated. | Maier 2025: synthetic panels show less positivity bias. | Same items and same people, human and synthetic panels. |
| Do persona details matter? | Ma 2025: context about experiences improves fit. | Argyle 2023: demographic backstories alone capture subgroups. | Head-to-head test on the same respondents. |
| Can variance loss be fixed? | SSR fix 2026: a semantic rating method reduces the loss. | Instruction 2026: asking for the full distribution in one call works better. | Benchmark both on held-out human survey data. |

## Gaps
The table lists open questions and the closest existing work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Real purchases | Stated willingness to pay can differ from prices people actually pay. | Brand 2024 (hypothetical choices) |
| Live click data | Ranking changes need real users to confirm the simulator. | BASES 2024 (query and click match only) |
| Search-cost models | A structural model would link simulated choices to search costs and welfare. | Fulman 2025 (choice only) |
| Subgroup decisions | Segment targeting may pick the wrong segment. | Chen 2026 (simulated data only) |
| Non-U.S. consumers | Persona fit may not carry over to other countries. | Korea panel 2026 (one country) |

## Papers cited
The table lists every paper named above, with its exact title and how the agent read it.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Argyle 2023 | **Out of One, Many: Using Language Models to Simulate Human Samples** | 2023 | Political Analysis | summary |
| Brand 2024 | **Using GPT for Market Research** | 2024 | ACM Conference on Economics and Computation (EC '24) | summary |
| Brand 2025 | **Using LLMs for Market Research** | 2025 | Microsoft working paper | summary (title unverified) |
| Maier 2025 | **LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings** | 2025 | arXiv preprint | abstract |
| SSR fix 2026 | **Correcting Mode Collapse in Silicon Sampling with Semantic Similarity Rating** | 2026 | arXiv preprint | metadata only |
| Demand 2026 | **Can LLMs Serve as Synthetic Respondents for Consumer Demand Estimation?** | 2026 | NeurIPS | summary |
| Reusens 2026 | **Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices** | 2026 | Expert Systems with Applications | summary |
| Dillion 2023 | **Can AI language models replace human participants?** | 2023 | Trends in Cognitive Sciences | metadata only |
| Bisbee 2024 | **Synthetic Replacements for Human Survey Data? The Perils of Large Language Models** | 2024 | Political Analysis | metadata only, findings from a summary that names another author |
| Wang 2025 | **Can Finetuning LLMs on Small Human Samples Increase Heterogeneity, Alignment, and Belief-Action Coherence?** | 2025 | arXiv preprint | summary |
| Tigre 2026 | **When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels** | 2026 | arXiv preprint | abstract |
| Chen 2026 | **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses** | 2026 | arXiv preprint | summary |
| Ma 2025 | **Evaluating Silicon Sampling: LLM Accuracy in Simulating Public Opinion on Facial Recognition Technology** | 2025 | AHFE conference proceedings | summary |
| Twin 2025 | **Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions** | 2025 | Marketing Science | metadata, follow-up study from a secondary summary |
| Persona A/B 2026 | **Data-Driven Persona-Conditioned Agents for A/B Test Simulation** | 2026 | arXiv preprint | summary |
| Flexible budget 2026 | **Flexible but Fragile: Budgeted Human–Digital-Twin Allocation for A/B Tests** | 2026 | NeurIPS | summary |
| Instruction 2026 | **Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe** | 2026 | arXiv preprint | summary |
| NIM review | **Leaving Insight to Digital Twins? Promise, Progress and Limits of Synthetic Respondents** | year unverified | NIM Marketing Intelligence Review | secondary summary |
| BASES 2024 | **BASES: Large-scale Web Search User Simulation with Large Language Model based Agents** | 2024 | arXiv preprint | summary |
| Efficacy 2025 | **Evaluating the Efficacy of Simulated User Models in Interactive Information Retrieval: A User-Based Approach** | 2025 | Sindh University Research Journal | summary |
| USimAgent 2025 | **USimAgent: Large Language Models for Simulating Search Users** | 2025 | SIGIR | metadata and summary |
| PAARS 2025 | **PAARS** | 2025 | arXiv preprint | summary (full title unverified) |
| Customer-sim 2025 | **LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-based Shopping Assistants?** | 2025 | arXiv preprint | summary |
| Fulman 2025 | **Utilizing large language models to simulate parking search** | 2025 | Transportation Research Part A: Policy and Practice | summary |
| Korea panel 2026 | **Distributional Validity and Calibration of a Korean Synthetic Persona Panel for Digital and AI Service Use: A Secondary-Data Validation Against the Korea Media Panel Survey** | 2026 | arXiv preprint | search result only |

<details><summary>Original research question</summary>

How are LLMs used as research tools to model or simulate consumer search and choice: LLM-simulated consumers ('silicon samples') for market research and willingness-to-pay estimation, LLM agents as synthetic shoppers to test search interfaces or ranking, and LLM-based structural or behavioral models of search? How well do simulated consumers match real consumer search and choice data, and where do they fail?

</details>
