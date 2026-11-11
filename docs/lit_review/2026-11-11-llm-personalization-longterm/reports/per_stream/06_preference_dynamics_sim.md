# Simulating user preference dynamics under AI influence

**Question:** How do simulations model user tastes or opinions changing under repeated recommender or AI exposure, and how are they checked against real people?

## Short answer
**Answer:** Three kinds of simulation work exist: explicit-rule models, LLM-agent user simulators, and LLM opinion networks. Explicit-rule models set how users drift, and LLM-agent simulators mostly keep tastes fixed. No study checks a simulated preference path against real users over time.

**Strength:** Medium (most core simulators read in full, but the real-user comparison rests on one cross-dataset result)
- **Holds when:** the recommender retrains on simulated clicks → recommendations narrow over rounds (Agent4Rec and Algorithmic Drift).
- **Does not hold when:** LLM agents judge facts → opinions move to scientific consensus, not to the persona's view (Chuang 2023).
- **Still unknown:** whether simulated drift rates match real platform users, since the one comparison used different datasets.

## Background
Recommender systems and AI chatbots can change what people like over time. Long studies on real people are slow and costly, so researchers often run simulated users instead. This page covers which simulators exist, how they update tastes, and whether anyone checks them against real people.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM-agent | A language model given a profile, memory and actions, acting as a simulated person. |
| User simulator | A program that stands in for real users to test a system. |
| ABM (agent-based model) | A simulation of many individual agents that follow simple rules over time. |
| Opinion dynamics | Models of how beliefs change through social contact. |
| Echo chamber | A group that mostly hears views it already holds. |
| Filter bubble | A feed that narrows what a user sees over time. |
| Information cocoon | A narrow loop of content, kept going by the recommender and the user. |
| Feedback loop | A system where the model's outputs shape its next training data. |
| Preference drift | A change in a user's tastes over time. |
| Persona | A fixed profile (age, traits, tastes) given to an LLM agent. |
| Persona collapse | Many distinct personas that behave in the same way. |
| Sycophancy | A model's tendency to agree with the person it talks to. |
| MovieLens-1M | A public dataset of movie ratings. |
| MIND | A public dataset of news clicks. |
| LoCoMo | A dataset of synthetic long-horizon user memory traces. |
| Accuracy (1:1 mix) | Share of correct like or dislike calls on a half-liked, half-disliked item set. Higher is better. |
| Jaccard overlap | Share of shared items between two sets. Drift here is one minus this overlap. |
| SFT and DPO | Training on example answers (SFT), then on preferred-versus-rejected answer pairs (DPO). |
| Biased assimilation | People accept content that fits their view and reject content that does not. |
| Choice model with inertia | Users pick from the recommender with a fixed chance and otherwise pick freely. |
| Homogenization | Many users come to behave or consume in the same way. |
| Stationary preferences | Preferences that do not change over time. |

## Main approaches
The main ways researchers attack this question:
| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Fixed-taste simulators | Tastes are set once, and only the recommender changes | Yao 2021, Agent4Rec | Established |
| LLM-agent user simulators | LLM agents with memory act as users in a recommender | RecAgent, SimUSER, UserMirrorer | Established |
| Explicit choice rules | Users follow the recommender with set probabilities and drift over time | Algorithmic Drift 2025 | Emerging |
| Agent-based longitudinal models | Many simple agents evolve over periods under a recommender | Zhang 2020, Adomavicius 2021 | Emerging |
| Biased-assimilation theory | Users move toward liked content and away from disliked content | Dean and Morgenstern 2022 | Emerging |
| LLM opinion networks | LLM agents exchange messages on a network and update opinions | Chuang 2023, Wang 2025 | Emerging |
| Human-AI co-evolution models | A statistical model fit to real platform data tracks cocoons | Piao 2023 | Emerging |

## What the evidence shows
### Finding 1: Simulated feedback loops narrow what users see, even with fixed tastes.
- **Yao 2021**: fixed-taste users on MovieLens-1M see popularity jump at step one. Popularity then falls on average (slope −0.028 for uniform users).
- **Agent4Rec (Zhang 2024)**: LLM agents with fixed tastes → recommendations grow more concentrated over iterations, with no numbers in the text.
- **Chaney 2018**: training on algorithm-exposed data → user behavior homogenizes without better utility.
- **Strength:** Medium — three groups agree on filter-bubble-like narrowing, but all runs are synthetic or offline with no real-user check.

### Finding 2: Explicit update rules make drift depend on how much users resist the recommender.
- **Algorithmic Drift (Coppolillo 2025)**: synthetic users with resistance and inertia → drift grows as resistance falls and inertia rises. Data are fully synthetic, with 2,000 users and 50 rounds.
- **Dean and Morgenstern 2022**: biased-assimilation model → personalized recommendations can collapse preferences, and randomization keeps them stationary. This is a theory result read from its summary.
- **Strength:** Medium — one simulation group and one theory paper, with no calibration on real data.

### Finding 3: LLM-agent simulators keep tastes fixed and validate on single decisions.
- **Agent4Rec (Zhang 2024)**: accuracy 0.69 on MovieLens-1M at a 1:1 mix (0 to 1, higher is better). Preferences are set once at the start.
- **SimUSER (Bougie 2025)**: accuracy 0.79 on MovieLens-1M, against 0.58 for RecAgent (self-reported in its own table).
- **UserMirrorer (2025)**: accuracy on real MIND clicks rises from 19.9 to 34.0 after SFT and DPO training. The simulator's state is not updated across interactions.
- **Strength:** Low to Medium — single-decision accuracy does not test long-run drift, and the numbers come from different protocols.

### Finding 4: LLM opinion simulations drift to scientific consensus, not to persona views.
- **Chuang 2023**: 10 GPT-3.5 agents over 100 steps → agents move to the scientific view on five topics. Confirmation-bias prompts raise diversity.
- **Wang 2025**: 50 GPT-4o-mini agents → echo chambers form on small-world and scale-free networks, not on random ones.
- **Strength:** Medium — two groups, small populations, one LLM each, and no human panel.

### Finding 5: Real users change their interests much faster than one synthetic dataset shows.
- **OmniBehavior (2026)**: daily interest drift is 0.63 for Kuaishou real users and 0.17 for LoCoMo, a synthetic long-memory dataset. Drift is one minus the Jaccard overlap of interest categories.
- **Strength:** Low — one comparison in a preprint, using two different datasets, so data differences may explain the gap.

## Where researchers disagree
The table shows the main open questions and what would settle each one.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do LLM agents reproduce echo chambers? | Yes on social networks (Wang 2025) | No, they converge to scientific consensus (Chuang 2023) | Matched runs on the same network with real users |
| Is single-decision accuracy enough? | Yes, it is the usual check (Agent4Rec, SimUSER) | No, drift needs trajectories (OmniBehavior) | Trajectory-level checks against real logs |
| Does the recommender or the user drive drift? | The recommender loop (Yao 2021, Agent4Rec) | The user's resistance and inertia (Algorithmic Drift) | Field data that separate exposure from user choice |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| No matched check of simulated preference paths against real panels | Drift results may reflect the simulator, not users | OmniBehavior 2026 (different datasets) |
| LLM-agent update rules are implicit or static | Results depend on a rule that most papers do not state | Agent4Rec, SimUSER |
| Persona collapse under repeated use is not measured | A narrow simulated population can distort feedback results | Chameleon's Limit 2026 (search summary) |
| Sycophancy effects on simulated taste change are untested | Agreeable simulators may overstate how easily users change | None directly, and Zhu 2024 covers leakage only |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| RecAgent | **User Behavior Simulation with Large Language Model-based Agents** | 2024 | ACM Transactions on Information Systems | search summary |
| Agent4Rec | **On Generative Agents in Recommendation** | 2024 | SIGIR 2024 | full text |
| SimUSER | **SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation** | 2025 | arXiv preprint | full text |
| UserMirrorer | **Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation** | 2025 | arXiv preprint | full text |
| Algorithmic Drift | **Algorithmic Drift: A simulation framework to study the effects of recommender systems on user preferences** | 2025 | Information Processing & Management | full text |
| Yao 2021 | **Measuring Recommender System Effects with Simulated Users** | 2021 | arXiv preprint | full text |
| Dean and Morgenstern 2022 | **Preference Dynamics Under Personalized Recommendations** | 2022 | ACM EC 2022 | search summary |
| Zhang 2020 | **Consumption and Performance: Understanding Longitudinal Dynamics of Recommender Systems via an Agent-Based Simulation Framework** | 2020 | Information Systems Research | title and metadata only |
| Adomavicius 2021 | **Understanding Longitudinal Dynamics of Recommender Systems with Agent-Based Modeling and Simulation** | 2021 | SimuRec workshop, RecSys 2021 | abstract |
| Chaney 2018 | **How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility** | 2018 | arXiv preprint | abstract |
| Chuang 2023 | **Simulating Opinion Dynamics with Networks of LLM-based Agents** | 2023 | arXiv preprint | full text |
| Wang 2025 | **Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks** | 2025 | COLING 2025 | full text |
| Piao 2023 | **Human–AI adaptive dynamics drives the emergence of information cocoons** | 2023 | Nature Machine Intelligence | abstract and secondary coverage |
| OmniBehavior 2026 | **Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces** | 2026 | arXiv preprint | full text, first 100,000 characters |
| Chameleon's Limit | **The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models** | 2026 | arXiv preprint | search summary |
| Zhu 2024 | **How Reliable is Your Simulator? Analysis on the Limitations of Current LLM-based User Simulators for Conversational Recommendation** | 2024 | arXiv preprint | search summary |

<details><summary>Original research question</summary>

What simulation work models how user preferences or opinions evolve under repeated exposure to recommenders or LLM assistants — agent-based models, opinion-dynamics simulations, LLM-agent user simulators (e.g. RecAgent, Agent4Rec, generative agents), long-horizon simulated users for personalization — what preference-update rules do they assume, how are simulations validated against real users, and what dynamics do they report?

</details>
