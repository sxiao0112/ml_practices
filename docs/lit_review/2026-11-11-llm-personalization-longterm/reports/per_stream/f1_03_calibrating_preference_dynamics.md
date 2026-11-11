# Estimating and validating preference dynamics from real data

**Question:** How is taste change measured from real data, and how are LLM user simulators checked against it? Which data could calibrate one?

## Short answer
**Answer:** Real data show taste change through structural panel models, learned log models, and field experiments. No LLM simulator has been checked against one person's real taste path over months. The best longitudinal check, OmniBehavior, finds simulated users drift far less than real users.

**Strength:** Medium (one three-month benchmark, drift numbers read from a summary, and no direct test found across about eight searches)
- **Holds when:** Long real panels with exogenous shocks → taste persistence and state dependence can be estimated (Dubé 2010).
- **Does not hold when:** Simulated users get only personas or single sessions → accuracy drops and drift is too low (Lu 2026, OmniBehavior).
- **Still unknown:** Whether an LLM simulator reproduces real taste change under LLM advice.

## Background
Simulated users test recommenders and LLM products before they reach real people. A simulated user should change its tastes the way real users do. Otherwise, tests of recommenders and LLM products can mislead. This page reviews how taste change is measured in real data and how simulators are checked.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Taste drift | Change in a person's preferences over time. |
| State dependence | Past choices make the same choice more likely now. |
| Habit formation | Consumption rises with past consumption of the same good. |
| Structural model | A model of choices that recovers the underlying preference parameters. |
| Hidden Markov model | A model where a hidden state changes over time and produces observed behavior. |
| Matrix factorization (MF) | Learns user and item vectors from ratings to predict new ratings. |
| Field experiment | A randomized test run on a live platform with real users. |
| User simulator | An LLM or other program that acts like a user in tests. |
| Persona | A text description of a simulated user's traits and preferences. |
| Jaccard drift | One minus the overlap between two sets of items on two days. |
| Negative control | An outcome that should not change, used to check for hidden shifts. |
| Diversity measure | A score for how spread out a user's consumption is across items. |
| MovieLens | A public movie-rating dataset used in recommender research. |
| Kuaishou | A Chinese short-video and live-streaming platform with public logs. |
| OmniBehavior | A 2026 benchmark of real Kuaishou logs for simulator tests. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Structural panel models | Model repeat purchases as choices that depend on past choices. | Dubé 2010, Dynan 2000 | Established |
| Migration natural experiments | Use moves between places to test how the environment shapes taste. | Bronnenberg 2012, Way 2019 | Established |
| Learned log models | Fit a hidden taste state or drifting embedding to user histories. | Eskandanian 2018, Koren 2009, Carroll 2022 | Emerging (hidden Markov, shift models) |
| Recommender field tests | Randomize recommendations and track consumption change. | Holtz 2020, Zielnicki 2025 | Emerging |
| LLM simulators with memory | Give an LLM a persona plus memory that updates over time. | Wanyan 2025, Bougie 2026 | Emerging |
| Simulator validation benchmarks | Compare simulated and real logs on actions or traces. | Chen 2026 (OmniBehavior), Lu 2026, Seshadri 2026 | Contested |

## What the evidence shows
### Finding 1: Real tastes persist for years and shift only a little after a move.
- **Brand migration (Bronnenberg 2012)**: Movers' brand choices track past regions → heterogeneity explains about 40% of share variation.
- **Music relocation (Way 2019)**: Spotify users who moved within the US → tastes stayed closer to the old environment.
- **Strength:** Medium. Two large panels in different categories, but no replication outside these data.

### Finding 2: Structural and learned models can separate taste change from habit, but need long panels.
- **Scanner-data state dependence (Dubé 2010)**: Household purchase panels with price shocks → loyalty to past brands is identified.
- **Panel habit test (Dynan 2000)**: Food panel data → no habit formation at annual frequency.
- **Music change points (Eskandanian 2018)**: Hidden Markov model on listening sequences → change points found, and recommendations beat baselines (reported in the 2019 follow-up).
- **Strength:** Medium. Each method has one or two datasets, and the hidden Markov model results are not checked against other data.

### Finding 3: Recommendations change what users consume and can narrow individual taste.
- **Podcast field test (Holtz 2020)**: 900,000 Spotify users → personalized picks raised streams 28.90% and cut individual diversity 11.51 points.
- **Netflix counterfactuals (Zielnicki 2025)**: Netflix viewing logs → alternative recommenders cut engagement 4% to 12% and lower diversity.
- **Strength:** High for the direction of the effect (randomized, large sample). Medium for the Netflix sizes (one platform, structural model).

### Finding 4: LLM simulators miss real long-horizon behavior and drift too little.
- **Kuaishou benchmark (Chen 2026)**: Logs for 200 users over three months → real daily drift 0.63, simulated 0.17 (1 minus Jaccard).
- **Action prediction (Lu 2026)**: About 31,865 shopping sessions → prompt-only LLMs predict 11.86% of next actions, and fine-tuning reaches 17.26%.
- **Strength:** Medium. One benchmark, with the drift values read from a summary of the full paper. The session result is consistent with it.

### Finding 5: Memory-based simulators are validated on accuracy, not on individual paths over time.
- **Context-aware agents (Bougie 2026)**: Memory and a 30-day life simulation → preference accuracy 0.824 on MovieLens-1M versus 0.791 for an older simulator. No individual path is tracked.
- **Evolving profiles (Wanyan 2025)**: Dynamic profile updates → the abstract claims better alignment with real behavior, with no numbers read.
- **Drift as bias (Lin 2026)**: Persona-based users shift under treatment → treatment effects can be biased, and a negative-control check can detect it.
- **Strength:** Low. No longitudinal test against real users, and some claims rest on abstracts only.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| How fast do real tastes change? | Slow and persistent (Bronnenberg 2012, Way 2019). | Fast in feeds: real daily drift 0.63 (Chen 2026). | One drift metric on panels with and without recommenders. |
| Do recommenders narrow taste? | Yes, individual diversity falls (Holtz 2020). | Current recommender keeps more diversity than MF (Zielnicki 2025). | Randomized test with one diversity measure on one platform. |
| Are LLM simulators valid? | Yes on rating accuracy (Bougie 2026, Wanyan 2025). | No on real actions and drift (Chen 2026, Seshadri 2026). | Held-out test of simulated paths against real users over months. |
| Can personas set one preference? | Yes, the target attribute moves (persona prompting). | No, other attributes shift too (Neutrality gap 2026). | Check selective control against real users' attributes. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Real users tracked for months, to test simulator drift | Only this tests whether simulated taste change is realistic. | Chen 2026 (200 users, three months) |
| Exposure to LLM answers in logs | Needed to estimate LLM influence on taste. | Holtz 2020 (recommender field test) |
| One shared drift metric | Papers cannot compare results without it. | Chen 2026 (1 minus Jaccard), Li 2026 |
| Structural model that drives a simulator | Would link estimated dynamics to simulated users. | Dubé 2010 (estimation only), Carroll 2022 |
| Long public logs | Kuaishou open logs mostly span weeks. | KuaiSim (Zhao 2023) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Dynan 2000 | **Habit Formation in Consumer Preferences: Evidence from Panel Data** | 2000 | American Economic Review | summary (search snippet) |
| Dubé 2010 | **State dependence and alternative explanations for consumer inertia** | 2010 | RAND Journal of Economics | summary (search snippet) |
| Bronnenberg 2012 | **The Evolution of Brand Preferences: Evidence from Consumer Migration** | 2012 | American Economic Review | summary (search snippet) |
| Way 2019 | **Environmental Changes and the Dynamics of Musical Identity** | 2019 | International AAAI Conference on Web and Social Media (arXiv preprint version) | abstract |
| Eskandanian 2018 | **Detecting Changes in User Preferences using Hidden Markov Models for Sequential Recommendation Tasks** | 2018 | arXiv preprint | summary (search snippet) |
| Eskandanian 2019 | **Modeling the Dynamics of User Preferences for Sequence-Aware Recommendation Using Hidden Markov Models** | 2019 | arXiv preprint | summary (search snippet) |
| Koren 2009 | **Collaborative filtering with temporal dynamics** | 2009 | ACM SIGKDD Conference | summary (search snippet) |
| Carroll 2022 | **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** | 2022 | International Conference on Machine Learning (proceedings) | summary of fetched page |
| Zielnicki 2025 | **The Value of Personalized Recommendations: Evidence from Netflix** | 2025 | arXiv preprint | abstract |
| Holtz 2020 | **The Engagement-Diversity Connection: Evidence from a Field Experiment on Spotify** | 2020 | ACM Conference on Economics and Computation | summary of search results |
| Chen 2026 | **Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces** | 2026 | arXiv preprint (accepted to NeurIPS 2026) | summary of fetched HTML |
| Lu 2026 | **Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data** | 2026 | ACL 2026 | summary of search results |
| Bougie 2026 | **Beyond Offline A/B Testing: Context-Aware Agent Simulation for Recommender System Evaluation** | 2026 | EMNLP 2026 | summary of fetched page |
| Wanyan 2025 | **Temporal-Aware User Behaviour Simulation with Large Language Models for Recommender Systems** | 2025 | arXiv preprint | abstract (summary of fetched page) |
| Li 2026 | **HorizonBench: Long-Horizon Personalization with Evolving Preferences** | 2026 | arXiv preprint | summary of fetched page |
| Lin 2026 | **The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study** | 2026 | arXiv preprint | summary of fetched page |
| Seshadri 2026 | **Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations** | 2026 | ACL 2026 | summary of search results |
| Neutrality gap 2026 | **Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation** | 2026 | arXiv preprint | search snippet |
| Zhao 2023 | **KuaiSim: A Comprehensive Simulator for Recommender Systems** | 2023 | NeurIPS 2023 | summary of fetched page |
| Cheng 2026 | **Measuring the Behavioral Fidelity of Long-Horizon Human Activity Simulations** | 2026 | EMNLP 2026 | summary of fetched page |

<details><summary>Original research question</summary>

How have researchers estimated user preference dynamics from longitudinal real data (structural estimation of taste evolution, preference drift detection in recommender logs, dynamic user embeddings, state-space or hidden Markov taste models, Kuaishou/Spotify/MovieLens trajectories) and how have user simulators (especially LLM-agent simulators with memory or evolving preferences) been validated against real longitudinal behavior? What methods and datasets would let one calibrate and validate a simulation of preference change under LLM influence?

</details>
