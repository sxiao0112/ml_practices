# Formal models of users learning their preferences with an AI advisor

**Question:** Which formal models describe a user who learns her own preferences from an advisor, recommender or AI system, and what do they predict?

## Short answer
**Answer:** Five families of formal models fit this question. Strategic-user models predict that users who know their feedback shapes recommendations can widen preference gaps. Bayesian and deskilling models predict that heavy reliance on an advisor reduces a user's own learning. Elicitation studies show that the question format changes what a language model reports as a preference.

**Strength:** Medium (most formal results sit in working papers, and two key models were read only through abstracts)
- **Holds when:** the advisor learns from the user's own choices, and the user acts strategically → preference gaps can widen (Haupt 2023).
- **Does not hold when:** the AI tool is built to scaffold practice → unguarded use hurt later test scores, guarded use did not (Bastani 2025).
- **Still unknown:** whether these dynamics appear in real users' tastes measured over months.

## Background
Recommenders and AI chat tools now shape what people buy, read and believe. Many users do not know their own tastes in advance, so each suggestion can change them. Researchers ask whether this learning is accurate, and whether it leaves users better or worse off. The answer depends on who learns, who chooses the questions, and whether practice skill decays.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Cheap talk | Messages that cost the sender nothing, so the receiver must judge whether to trust them. |
| Strategic user | A user who changes behavior to shape what a recommender learns about her. |
| Cold start | The early phase, before a recommender has enough data about a new user. |
| Behavior-vs-utility inversion | Clicks and time spent can differ from what the user actually wants on reflection. |
| Inconsistent preferences | In-the-moment choices that differ from the user's reflective goals. |
| Content manifold | A space of content described by features, along which a platform can move. |
| Bayesian updating | Revising a belief with each new observation, using probability rules. |
| Thompson sampling | Choosing an option by drawing once from current beliefs about which option is best. |
| Exemplar model | A category-learning model that stores past examples and compares new ones to them. |
| Satiation | Liking for a product falls with repeated use, so the user switches. |
| Stated vs revealed preference | What a person says they prefer, compared with what they choose. |
| Deskilling | Loss of a skill that people stop practicing because a tool does the task. |
| Capability threshold | A skill level below which the skill falls quickly, in a model. |
| Rank correlation | A score from -1 to 1 for how well two rankings agree. Higher means more agreement. |
| PISA | An international school test of 15-year-olds, used here as calibration data. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Strategic users of recommenders | Users change feedback to steer future recommendations. | Haupt 2023, Schmit 2018 | Emerging |
| Behavior-vs-utility inversion | Clicks are a poor guide to what users want on reflection. | Kleinberg 2024, Kleinberg 2023 | Emerging |
| Repeated cheap talk and advisor learning | An advisor learns the user and may be biased. | Gramb 2022, Frug 2014 | Established |
| Bayesian self-learning under recommendations | Users learn their own tastes, and recommendations change what they see. | Rafieian 2024 | Emerging |
| Deskilling under AI reliance | Practice with AI builds less skill over time. | Bastani 2025, Park 2026, Caosun 2026 | Emerging |
| Preference elicitation | The question format changes the stated preference. | Mahajan 2026 | Emerging |
| Satiation and variety seeking | Liking drops with repeat use, which drives switching. | McAlister 1982, Kim 2002 | Established |

## What the evidence shows
### Finding 1: Strategic users can widen the preference gaps that recommenders see.
- **Haupt 2023**: a platform fixes a policy after a cold-start phase → users consume strategically, and preference differences widen in equilibrium.
- **Schmit 2018**: estimators that ignore the feedback loop are inconsistent → the platform's regret grows linearly (from a search excerpt).
- **Strength:** Medium. The model has clear equilibria, but no real-user test of it was found.

### Finding 2: Users who rely on a recommender may learn less about their own tastes.
- **Rafieian 2024**: users learn tastes by Bayesian updating and choose by Thompson sampling. With recommendations, they learn less about themselves (from a search excerpt).
- **Bahg 2021**: a curated sequence distorts category representations → learners become overconfident in simulations.
- **Strength:** Low to Medium. The Rafieian result rests on a search excerpt.
- **Limit:** The Bahg result is a conference abstract about categories, not preferences.

### Finding 3: AI use can reduce skill, and the design of the tool matters.
- **Bastani 2025**: about 1,000 high school students in a field experiment. Unrestricted AI helped during practice but lowered later unassisted scores.
- **Bastani 2025, guarded arm**: a tutor with learning-safe prompts largely avoided this loss.
- **Park 2026**: capability falls abruptly past a threshold of about 0.85 → fitted to PISA data from 15 countries.
- **Caosun 2026**: rational offloading can lower long-run productivity → strong AI substitution can create permanent skill gaps.
- **Strength:** High that unguarded use can harm one group of learners (peer-reviewed). Low for the threshold, which is a calibration fit in a preprint.

### Finding 4: The question format changes what a language model reports as a preference.
- **Mahajan 2026**: across 24 models, the stated-revealed rank correlation depends on the protocol. Allowing abstention in choices pushes it near zero or below.
- **Strength:** Medium. The study covers 24 models, but it is a preprint and measures model consistency, not a human's learning.

### Finding 5: An advisor that learns the user can help or exploit.
- **Gramb 2022**: an expert with a bonus for steering learns the consumer. In simple equilibria, learning helps both sides when it sharpens advice.
- **Strength:** Low. This is a working paper, and the lab test results were not retrieved.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do recommenders widen user tastes? | Strategic feedback widens gaps (Haupt 2023). | Some field studies find small or no short-term effects. | Panel data tracking the same users' tastes before and after recommendations. |
| Is reliance on AI rational? | Dependence can pay off over time (Rafieian 2024, Caosun 2026). | Unguarded use lowers later performance (Bastani 2025). | Follow-up tests of skill after the tool is removed, with varied designs. |
| Do skill losses jump at a threshold? | Capability collapses past a threshold (Park 2026). | Permanent group gaps, with no closed-form threshold stated (Caosun 2026). | Repeated skill measures across users with different AI exposure. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| One model with a self-learning user, LLM elicitation and skill decay | Each piece exists alone, so their interaction is untested. | Rafieian 2024, Park 2026 |
| An LLM advisor that chooses its own questions | The question choice can set what the user learns. | Mahajan 2026 (measurement only) |
| Validation on real longitudinal taste data | Predicted taste drift has no panel test yet. | Haupt 2023 (theory only) |
| A learning state for the user in advisor models | Cheap-talk models give the advisor a learning state, not the user. | Gramb 2022 |
| Satiation models linked to AI advisors | Satiation drives variety choice, with no AI link found. | McAlister 1982, Kim 2002 |

## Papers cited
The table lists papers with a confirmed exact title. Three other papers appear only in the text. They are the Frug (2014) expert-learning paper, the Valsecchi (2023) forecasting paper, and a 2026 Waseda advisor-guesser working paper. Their titles were not confirmed.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Haupt 2023 | **Recommending to Strategic Users** | 2023 | arXiv preprint | abstract |
| Kleinberg 2024 | **The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization** | 2024 | Management Science | abstract |
| Kleinberg 2023 | **The Inversion Problem: Why Algorithms Should Infer Mental State and Not Just Predict Behavior** | 2023 | Perspectives on Psychological Science | search excerpt |
| Schmit 2018 | **Human Interaction with Recommendation Systems** | 2018 | AISTATS | search excerpt |
| Eslami 2016 | **First I "like" it, then I hide it** | 2016 | CHI | title and metadata only |
| Rafieian 2024 | **Personalization, Algorithmic Dependence, and Learning** | 2024 | working paper, Cornell | search excerpt (PDF unreadable) |
| Gramb 2022 | **Anonymous or personal? A simple model of repeated personalized advice** | 2022 | Cologne working paper | search excerpt |
| Dzyabura 2019 | **Recommending Products When Consumers Learn Their Preference Weights** | 2019 | Marketing Science | metadata only (covered earlier) |
| Bahg 2021 | **How personalization guides (or distorts) learning: A model-based explanation** | 2021 | MathPsych/ICCM | conference abstract |
| Park 2026 | **The enrichment paradox: critical capability thresholds and irreversible dependency in human-AI symbiosis** | 2026 | arXiv preprint | abstract |
| Caosun 2026 | **The Augmentation Trap: AI Productivity and the Cost of Cognitive Offloading** | 2026 | arXiv preprint | abstract |
| Bastani 2025 | **Generative AI without guardrails can harm learning: Evidence from high school mathematics** | 2025 | PNAS | search excerpt and news coverage |
| Mahajan 2026 | **Mind the Gap: How Elicitation Protocols Shape the Stated-Revealed Preference Gap in Language Models** | 2026 | arXiv preprint | abstract |
| McAlister 1982 | **A Dynamic Attribute Satiation Model of Variety-Seeking Behavior** | 1982 | Journal of Consumer Research | reference list only |
| Kim 2002 | **Modeling Consumer Demand for Variety** | 2002 | Marketing Science | reference list only |

<details><summary>Original research question</summary>

What formal (economic, Bayesian, game-theoretic, cognitive) models describe a user who is uncertain about their OWN preferences and learns them over repeated interactions with an advisor, recommender or AI system — including repeated cheap talk or biased advisors, strategic users of recommenders (e.g. Haupt, Podimata), the behavior-vs-utility inversion problem (Kleinberg, Mullainathan, Raghavan), reliance and deskilling models where AI help reduces the user's own learning, LLM-based preference elicitation that may shape what it elicits, and variety-seeking/satiation models in marketing? List each model's primitives (state, update rule, advisor objective) and its long-run prediction, so a researcher can build a new model of preference learning under LLM influence.

</details>
