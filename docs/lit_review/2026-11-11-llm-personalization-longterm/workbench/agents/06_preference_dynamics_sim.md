# What simulation work models how user preferences or opinions evolve under repeated exposure to recommenders or LLM assistants — agent-based models, opinion-dynamics simulations, LLM-agent user simulators (e.g. RecAgent, Agent4Rec, generative agents), long-horizon simulated users for personalization — what preference-update rules do they assume, how are simulations validated against real users, and what dynamics do they report?

## TL;DR
Answer: Three families. (a) Pre-LLM agent-based and closed-loop models use explicit update rules: choice-plus-inertia models (Algorithmic Drift 2025), biased-assimilation models (Dean and Morgenstern 2022), and agent-based longitudinal models (Zhang et al. 2020). (b) LLM-agent user simulators (RecAgent, Agent4Rec, SimUSER, UserMirrorer) mostly fix preferences at initialization and do not update them across rounds. Their validation is offline accuracy on held-out ratings, not longitudinal behavior. (c) LLM opinion-dynamics simulations (Chuang 2023; Wang 2025 COLING; Y Social) update opinions through LLM reactions and validate against consensus or against math models, not human panels. No paper found validates a simulated preference trajectory against real users over time. One matched comparison exists on drift (OmniBehavior), but it compares two different datasets.
Strength: Medium
Preference-update rules are explicit in the synthetic and math models but absent or static in LLM-agent simulators. Results on dynamics mostly come from simulators with no real-user check, so conclusions about real drift are weak.

## What Exists
### Sub-theme 1: LLM-agent user simulators (profile, memory, action modules)
- **User Behavior Simulation with Large Language Model-based Agents** (Wang et al., 2024, ACM Transactions on Information Systems) — RecAgent: LLM agents with profile, memory and action modules simulate browsing, clicking and social chat in a recommender loop; authors show emergent information-cocoon and conformity case studies, no quantitative validation of preference change found in the arXiv text read at abstract level.
  - Relevance: the reference simulator the user named; defines the common agent architecture; preference update is implicit in memory, not an explicit rule.
  - OpenAlex ID: W4405643789
  - Cited by: 297
- **On Generative Agents in Recommendation** (Zhang et al., 2024, SIGIR) — Agent4Rec: 1,000 LLM agents (gpt-3.5-turbo) on MovieLens-1M, Steam, Amazon-Book; read full HTML. Preferences are fixed at initialization from 25 viewing-history items. Across rounds only the recommender is retrained on viewed and unviewed items. Offline 1:1 accuracy is 0.6912 (MovieLens), 0.7190 (Amazon-Book), 0.6892 (Steam). As the liked share falls to 1:9, MovieLens precision drops to 0.2139. Authors report agents give too few 1–2 ratings and pick a fixed number of items.
  - Relevance: the main LLM simulator for filter-bubble dynamics; its dynamics come from the recommender retraining loop, not from a changing user state.
  - OpenAlex ID: W4400525295
  - Cited by: 235
- **SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation** (Bougie and Watanabe, 2025, arXiv/ACM) — persona matching, episodic and knowledge-graph memory, chain-of-thought actions; read full HTML. On MovieLens 1:1 accuracy reports 0.7912, versus 0.6912 for Agent4Rec and 0.5807 for RecAgent (self-reported table). Adds a 55-test online A/B set for food recommendation. Preference drift is not measured directly; the exposure experiment shows agents rate over-represented genres higher after more than 20 pages.
  - Relevance: the only LLM simulator read that tests an over-exposure effect and uses a real A/B set for validation; the A/B set is not longitudinal.
  - OpenAlex ID: W4412886873
  - Cited by: 37
- **Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation** (authors not verified, 2025, arXiv 2508.18142) — UserMirrorer: fine-tunes a 3B model (SFT, then DPO) on decision processes distilled from a 32B model; read full HTML. Accuracy on MIND (real exposures) rises from 19.9 to 34.0. Simulator state is not updated across interactions; only the recommender is retrained on simulated feedback, improving recall in all reported settings.
  - Relevance: validates against real MIND exposures per decision, not per trajectory; it confirms the static-state pattern.
  - OpenAlex ID: W7166855044 (2026 record; arXiv 2025)
  - Cited by: 12
- **DyTA4Rec** (authors not verified, 2025, arXiv 2509.16895) — LLM agent with a "dynamic updater" for profile refinement; claims better individual and group alignment with real behavior. Only the abstract was read, with no dataset, metric or numbers.
  - Relevance: the only LLM simulator found that claims an explicit per-step profile update; the claim is unverified here.
  - OpenAlex ID: not resolved
- **Measuring Recommender System Effects with Simulated Users** (Yao, Halpern, Thain, Wang et al., 2021, arXiv 2101.04526; first title "Beyond Next Step Bias") — non-LLM simulated users with fixed selection and feedback models on MovieLens-1M (150 steps); read full HTML. No preference-update rule; the recommender re-fits on the growing trajectory. Mean popularity slope is −0.028 for uniform users and −0.099 for lazy users. The paper does not validate against real users and calls its test users deliberately simple.
  - Relevance: a clean reference for what a fixed-preference simulator produces; any drift it shows comes from the recommender.
  - OpenAlex ID: W3118999971
  - Cited by: 61

### Sub-theme 2: Explicit preference-update rules (non-LLM, closed-loop)
- **Algorithmic Drift: A simulation framework to study the effects of recommender systems on user preferences** (Coppolillo, Mungari, Ritacco, Fabbri et al., 2025, Information Processing & Management) — synthetic users choose with resistance γ, inertia δ and randomness η, and the recommender (RecVAE) re-trains on the history; read full HTML. Parameters are synthetic (2,000 users, 50 rounds, 100 steps); no real-data calibration. Drift grows as γ falls and δ rises. Randomness η does not change ADS.
  - Relevance: the most explicit preference-update rule found; it is a choice rule, not a belief update, and has no empirical anchor.
  - OpenAlex ID: W4408921326
  - Cited by: 16
- **Preference Dynamics Under Personalized Recommendations** (Dean and Morgenstern, 2022, ACM EC; arXiv 2205.13026) — biased-assimilation model: preferences move toward enjoyed content and away from disliked content. Personalization can collapse preferences to a subset of content; randomization keeps them stationary. Read at search-summary level only; theorems not checked.
  - Relevance: a formal, pre-LLM counterpart to simulated drift; overlaps with the economics stream.
  - OpenAlex ID: W4285088850
  - Cited by: 37
- **Consumption and Performance: Understanding Longitudinal Dynamics of Recommender Systems via an Agent-Based Simulation Framework** (Zhang, Adomavicius, Gupta, Ketter, 2020, Information Systems Research) — agent-based model of consumption and recommender performance over time; OpenAlex record only, not read.
  - Relevance: an agent-based longitudinal study of consumers that predates LLMs; its update rules were not checked.
  - OpenAlex ID: W2969575218
  - Cited by: 141
- **Understanding Longitudinal Dynamics of Recommender Systems with Agent-Based Modeling and Simulation** (Adomavicius, Jannach, Leitner, Zhang, 2021, SimuRec workshop at RecSys; arXiv 2108.11068) — proposes an ABM framework and research questions; abstract read only, no results.
  - Relevance: a framework and agenda paper; it states that static designs miss longitudinal effects.
  - OpenAlex ID: not resolved
- **How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility** (Chaney, Stewart, Engelhardt, 2018, RecSys; arXiv 1710.11214) — simulations show training on algorithm-exposed data homogenizes user behavior without raising utility; abstract read only, no numbers.
  - Relevance: the standard reference for simulated homogenization from a feedback loop.
  - OpenAlex ID: not resolved
- **Preference Amplification in Recommender Systems** (Kalimeris, Bhagat, Kalyanaraman, Weinsberg, 2021, KDD) — found as a citer of Chaney-type work; not read.
  - Relevance: likely overlaps with the feedback-loop stream; not verified.
  - OpenAlex ID: W3172701938
  - Cited by: 43

### Sub-theme 3: LLM opinion-dynamics simulations
- **Simulating Opinion Dynamics with Networks of LLM-based Agents** (Chuang, Goyal, Harlalka, Suresh et al., 2023, arXiv 2311.09618) — 10 LLM agents, 100 steps, GPT-3.5-turbo; opinions updated by a classifier reading each reply; read full HTML. Agents drift to scientific consensus regardless of persona (an "inherent truth bias"); confirmation-bias prompts raise diversity. Validation is against scientific consensus on five topics, not human data.
  - Relevance: shows LLM agents do not behave like classic opinion models; the update is the LLM itself.
  - OpenAlex ID: W4388787757
  - Cited by: 92
- **Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks** (Wang, Liu, Yang, Chen et al., 2025, COLING; arXiv 2409.19338) — 50 GPT-4o-mini agents on small-world, scale-free and random graphs; read full HTML. Echo chambers form on small-world and scale-free graphs and not on random graphs. Nudge effects are reported qualitatively only. No human validation; compared against BCM and FJ numerical baselines.
  - Relevance: the LLM analogue of recommender-driven polarization; the recommender links agents with belief gap of at most 2.
  - OpenAlex ID: W4403811759
  - Cited by: 22
- **Y Social: an LLM-powered Social Media Digital Twin** (Rossetti, Stella, Cazabet, Abramski et al., 2024) — simulator used in a calibration study on a 2022 Italian election (arXiv 2509.18985); read the calibration study's abstract and fetch. Agents are calibrated on real conversations; results are qualitative. Opinion dynamics look like math opinion models; changing parameters has no significant effect; LLM tone and toxicity are less varied than real data.
  - Relevance: a rare calibration against real conversations; calibration is on profiles, not on preference trajectories.
  - OpenAlex ID: W4401978508
  - Cited by: 81
- **Human–AI adaptive dynamics drives the emergence of information cocoons** (Piao, Liu, Zhang, Su et al., 2023, Nature Machine Intelligence) — statistical-physics model fit to two real platform datasets; positive feedback and similarity matching produce cocoons; negative feedback and self-exploration counteract them. Abstract and secondary coverage only (paywalled).
  - Relevance: the closest real-data-grounded dynamic model of user-recommender co-evolution.
  - OpenAlex ID: W4387451903
  - Cited by: 108

### Sub-theme 4: Validation and real-user comparisons
- **OmniBehavior / LoCoMo drift comparison** (authors not verified, 2026, arXiv 2604.08362) — defines daily interest drift as 1 − Jaccard of macro-categories across consecutive days; reports real users (200 Kuaishou users, 3 months) at 0.6311 and synthetic users (LoCoMo) at 0.1698; read full text up to 100,000 of 155,295 characters.
  - Relevance: the only drift measure compared against real users found; the datasets differ, so this is not a matched validation.
  - OpenAlex ID: not resolved
- **How Reliable is Your Simulator? Analysis on the Limitations of Current LLM-based User Simulators for Conversational Recommendation** (Zhu, Huang, Sang, 2024, arXiv 2403.16416) — finds data leakage in CRS simulators; search-summary only.
  - Relevance: a critique that simulator evaluation can inflate results.
  - OpenAlex ID: not resolved
- **The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models** (authors not verified, 2026, arXiv 2604.24698) — 10 LLMs; assigned distinct personas converge to a narrow behavior mode; search-summary only.
  - Relevance: a simulated population can look diverse on paper but behave alike.
  - OpenAlex ID: not resolved

## Reference Chain Discoveries
- Found via: OpenAlex citers of Chaney et al. (preference amplification): Dean and Morgenstern (2022), Piao et al. (2023), Chuang et al. (2023) citers, the "Human-AI" paper, and "Towards Psychologically-Grounded Dynamic Preference Models" (W4289785200, 2022, 22 cites; not read).
- Found via: citers of Chuang et al. (2023): "Y Social" (2024), "Systematic Biases in LLM Simulations of Debates" (W4404782785, 2024, 136 cites; not read).
- Found via: citers of Algorithmic Drift: "Validating generative agent-Based modeling in social media simulations through the lens of the friendship paradox" (W7125535193, 2026; not read), "The Diversity Paradox revisited: Systemic Effects of Feedback Loops in Recommender Systems" (W7130544004, 2026; not read).
- Found via: citers of Agent4Rec and RecAgent: "Agentic Feedback Loop Modeling Improves Recommendation and User Simulation" (W4412396342, 2025, 30 cites; not read), "Temporal-Aware User Behaviour Simulation with Large Language Models for Recommender Systems" (W4414745312, 2025; not read), "Do Generative Recommenders Deepen the Information Cocoon?" (arXiv 2606.17707, 2026; not read), "SimTok" (arXiv 2504.08742, 2025; not read).
- Found via: Round 4 search: "LifeSim" (arXiv 2603.12152, 2026) and "RealPref" (arXiv 2603.04191, 2026), long-horizon simulated users; search-summary only.
- Found via: citers of Piao et al. and Krauth, Wang, Jordan "Breaking Feedback Loops in Recommender Systems with Causal Inference" (W4409963658, 2025, 34 cites); outside this stream's lane.

## What's Missing (Gaps)
- No paper found compares a simulated preference trajectory against real users' trajectories over time. The closest is the cross-dataset drift comparison in OmniBehavior.
- Most LLM-agent simulators keep preferences static after initialization (Agent4Rec, SimUSER, UserMirrorer). The rule for how an LLM agent should update its preference after an exposure is not standardized.
- Opinion-dynamics LLM simulations are validated against consensus or math models, not human panels or field data.
- The sycophancy and optimism biases of LLM simulators (search summaries of 2403.09738 and 2606.20708) have not been linked to the simulated drift results in Agent4Rec or SimUSER.
- Adomavicius et al. (2021) proposes ABM research questions for recommender drift; no paper found answers them with real users.

## Contradictions or Tensions
- Persona-based LLM agents look more realistic than classic agents: SimUSER reports 0.7912 accuracy against 0.5807 for RecAgent, all self-reported. Algorithmic Drift and Agent4Rec report only synthetic or offline numbers. These are not on a common benchmark.
- Echo chambers: Wang et al. (2025 COLING) find them on small-world and scale-free graphs, but not on random graphs. Chuang et al. (2023) find LLM agents converge toward consensus unless biased by prompts. Both use LLM agents with different defaults (network, prompt bias).
- Drift size: OmniBehavior finds real users drift far more (0.63 vs 0.17 daily Jaccard drift). This comparison uses different datasets, so the gap may reflect the datasets and not the simulators.
- Filter-bubble severity: Agent4Rec reports filter-bubble-like centralization without numeric values in the text. Yao et al. (2021) find popularity declines for most users with fixed preferences. These point to different sources of dynamics (recommender retraining vs fixed selection).

## Confidence
Medium
- What would raise confidence: a matched study that runs an LLM-agent or ABM simulator on the same panel as real users and compares drift in both.
- What would lower confidence: finding that SimUSER's and Agent4Rec's accuracy numbers do not transfer across protocols, or that Algorithmic Drift's rule matches real data only under its synthetic generator.

## Search Log
### Round 1: Broad search
- Queries: RecAgent LLM user simulator; Agent4Rec generative agents preference evolution; opinion dynamics feedback loop polarization ABM; LLM agents long-horizon personalization drift validation; RecSim preference shift long-term engagement.
- Papers found: about 10 unique candidates.
- Key leads: RecAgent (2306.02552), Agent4Rec (2310.10108), Algorithmic Drift (2409.16478), Chuang 2023 (2311.09618), OmniBehavior (2604.08362), Y Social calibration (2509.18985).

### Round 2: Citation traversal
- Papers traversed (OpenAlex): RecAgent (W4405643789), Agent4Rec (W4400525295), Algorithmic Drift (W4408921326); also Chaney-type Preference Amplification (W3172701938), Chuang 2023 (W4388787757), Algorithmic Drift citers; simulation-filtered citers of RecAgent and Agent4Rec.
- New papers from references: Agent4Rec's references are mostly general recommender and LLM work (LightGCN-era baselines, tool-learning surveys); Algorithmic Drift's are mostly network science, filter-bubble and polarization classics.
- New papers from citers: as listed under Reference Chain Discoveries.

### Round 3: Reference mining (primary-source reads)
- Papers read: Agent4Rec (full HTML), Algorithmic Drift (full HTML), OmniBehavior (full text to 100,000 chars), Yao et al. (2021, full HTML), SimUSER (full HTML), UserMirrorer (full HTML), Chuang 2023 (full HTML), Wang 2025 COLING (full HTML), Y Social calibration (abstract), Chaney (abstract), DyTA4Rec (abstract), Adomavicius (abstract).
- Related Work sections were not mined as separate reads; method and validation sections were read instead.
- Note: a guessed arXiv ID for a "Sim2Real" user-simulation paper resolved to an unrelated paper and was dropped.

### Round 4: Gap-filling
- Gaps targeted: LLM opinion dynamics; information cocoons with real data; sycophancy and drift in user simulators; Dean and Morgenstern model; RecAgent validation.
- Queries: simulating opinion dynamics with LLM agents; Human-AI adaptive dynamics information cocoons; LLM user simulator sycophancy preference drift; Dean Morgenstern preference dynamics; RecAgent validation 2025.
- New findings: Piao et al. (NMI 2023) with real datasets; sycophancy inherited by simulators (search summaries); no RecAgent fidelity study found.

### Round 5: Adversarial check
- Gaps targeted: critiques of LLM user simulators; persona homogenization; field-validated drift.
- Queries: LLM user simulator critique and reliability; persona collapse and homogenization; preference change validated against field or longitudinal data.
- New findings: "How Reliable is Your Simulator?" (leakage); Chameleon's Limit (persona collapse); DyTA4Rec (claims alignment, no numbers read); LifeSim and RealPref (long-horizon benchmarks).

### Convergence note
- Total unique relevant papers found: about 22 (about 13 read at full text or full HTML, the rest at abstract or search-summary level).
- New papers in last round: about 4 (critique, persona collapse, DyTA4Rec, LifeSim).
- Stopped because: stopping rule clause (completed Round 5 with the field-validation sub-question still open). New relevant papers still appeared in Round 5, so the search has not converged. Several leads (Kalimeris 2021, Zhang 2020 ISR, Psychologically-Grounded Dynamic Preference Models, SimTok) were not read.
