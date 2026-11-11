# Adversarial gap check: does any paper (2023-2026, any field: marketing, economics, IS, HCI, NLP, cognitive science) formally model or simulate how a user's own preferences, tastes or values FORM or CHANGE through repeated conversations with an LLM assistant (not just opinions on a debate topic) — e.g. AI-mediated preference construction, generative AI and taste formation, LLM shopping assistants shaping consumer preferences, preference elicitation by LLM that shapes what is elicited, Bayesian or reinforcement models of a consumer learning with a chatbot, agent-based simulations with LLM-assisted consumers? Try at least 10 different query phrasings across communities, plus SSRN and NBER working papers. Report everything found, and if little exists, state precisely what the closest work does and does not do.

## TL;DR
Answer: No paper found models a real user's own preferences forming or changing over repeated LLM conversations and then simulates or tests that path. The closest formal work is pre-LLM recommender theory (Dzyabura & Hauser 2019; Rafieian & Zuo) and one 2026 LLM preprint on preference construction (CoPref, Saracay et al.), which tests only simulated users.
Verdict: Mostly no
Strength: Medium
Holds for: formal models with real-user tests of single-session steering exist, and simulations of LLM-driven recommender loops exist. Does not hold for: a formal, multi-session, LLM-conversation model of the user's own taste that is validated on people. Search reach was limited: no direct SSRN or NBER database search, and most papers read by abstract only.

## What Exists

### Sub-theme 1: Formal models of users learning their own preferences (pre-LLM, recommender or search context)
- **Recommending Products When Consumers Learn Their Preference Weights** (Dzyabura & Hauser, 2019, Marketing Science) — consumers learn their attribute weights during search, so a static recommender can be suboptimal; a recommender can help that learning.
  - Relevance: closest marketing theory of a consumer learning own tastes from a recommender. No LLM, no conversation, no simulation of long-run paths.
  - OpenAlex ID: W2945152270
  - Cited by: 103
- **Personalization, Algorithmic Dependence, and Learning** (Rafieian & Zuo, Cornell, working paper) — users uncertain about tastes learn less about themselves when they depend on a recommender, creating a feedback loop.
  - Relevance: the closest formal model in the set. Bayesian users sample preferences by Thompson sampling. Recommender, not LLM dialogue. Context note says SSRN 5037671, which this search could not confirm.
  - OpenAlex ID: not found (not indexed in OpenAlex under this title or search terms)
- **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** (Carroll et al., 2022, ICML) — a learned dynamics model estimates how recommenders shift user preferences and penalizes undesirable shifts.
  - Relevance: simulation-based formal treatment of preference shift, but in a recommender bandit setting. Already in the review context, listed here only as the precedent.
  - OpenAlex ID: W4224979542
  - Cited by: 18
- **Influence of Recommender Systems on Users: A Dynamical Systems Analysis** (authors not checked, 2024, arXiv 2411.13883) — a stochastic approximation model of coupled evolution of population preferences and the learning algorithm.
  - Relevance: formal dynamical model of preference change under a recommender. Not LLM-based. Read from search summary only.
  - OpenAlex ID: not checked

### Sub-theme 2: LLM-based preference construction and preference state (2026 preprints, formal but simulated)
- **Beyond expert users: agents should help users construct preferences, not just elicit them** (Saracay, Schmidt, Guestrin, 2026, arXiv preprint) — CoPref models how users build preferences in response to agent dialog actions. CoShop benchmark: no agent exceeds 56% accuracy in five turns across five frontier models.
  - Relevance: closest match to "preference formation through LLM dialogue" as a formal model. Preference state starts sparse and grows monotonically, based on Search-Experience-Credence types. Users are simulated. No real-user validation shown in abstract.
  - OpenAlex ID: W7166830829
  - Cited by: 1
  - Full text read: partially (HTML, Related Work section)
- **BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation** (authors not checked, 2026, arXiv preprint, arXiv 2606.30850) — tests whether LLM belief trajectories track a closed-form Bayesian reference over multi-turn evidence.
  - Relevance: Bayesian update in LLM beliefs about a simulated user. Models the assistant's belief about the user, not the user's own preferences. Search summary only.
- **Bayesian Optimization with LLM-Based Acquisition Functions for Natural Language Preference Elicitation** (authors not checked, 2024, arXiv preprint; short name PEBOL) — maintains Bayesian beliefs over item utilities across dialogue turns.
  - Relevance: formal belief state in LLM dialogue. Treats user utilities as fixed. Search summary only.
- **CUPID** (COLM 2025, arXiv 2508.01674) — tests whether LLMs infer context-dependent user preferences from multi-turn feedback.
  - Relevance: already in review context. Confirms the inference side only, not preference change.

### Sub-theme 3: Real-user evidence that conversation shifts attitudes or choices (empirical, mostly no formal model)
- **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** (Werner, Soraperra, Calvano, Parkes, Rahwan, 2024, arXiv preprint) — a behavioral experiment finds conversational AI shifts consumer choices. Secondary summary reports 36% switch and 39% fail to notice steering (not verified in full text).
  - Relevance: real users, shopping context. Single-session choice. No formal model. Abstract gives no effect sizes.
  - OpenAlex ID: W4403746738
  - Cited by: 22
- **Commercial Persuasion in AI-Mediated Conversations** (Salvi, Cuevas, Ribeiro, 2026, arXiv preprint) — N = 2,012 in two preregistered experiments. Sponsored book selection rises from 22.4% to 61.2% with an LLM agent. Most users do not detect steering.
  - Relevance: real users, one choice per participant. Abstract describes single-session choice only.
  - OpenAlex ID: W7151421112
  - Cited by: 18
- **LLMs can persuade only psychologically susceptible humans on societal issues, via trust in AI and emotional appeals, amid logical fallacies** (Carrillo et al., 2026, arXiv preprint) — 770 participants, four-wave longitudinal design (about four conversations each). Convictions show longitudinal inertia.
  - Relevance: real repeated conversations with change measured over waves. Topic opinions, not tastes. No formal model; mixed-effects and explainable AI analysis.
- **Stayin' Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data** (Gebreegziabher et al., 2026, arXiv preprint; title as returned by the page, check it) — 8 participants, two-week deployment. Immediate and later preferences about LLM outputs differ.
  - Relevance: real repeated use, very small sample. Framework paper, not a model of preference formation.
- **AI emotional support is better only when chosen, but shifts preferences even when it is not** (Shi, Fang, Laban, Maes, Goldenberg, 2026, arXiv preprint) — three single-session experiments (N = 1,951) and a 28-day study with OpenAI (N = 981). Daily conversations shift support preferences toward AI when they turn personal.
  - Relevance: closest real-user evidence of repeated-use preference change. Domain is emotional support. No formal model. Effect sizes not in abstract.
- **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** (Jiang et al., 2025, arXiv preprint) — 266 participants, 50 controversial topics. Human opinions "barely shifted," while LLM stance moved more.
  - Relevance: multi-turn human-LLM opinion dynamics. Opinions on debate topics, which the question excludes. No formal dynamical model. Supports the "human side changes little" pattern.
- **Adopt ≠ Adapt: Longitudinal Analyses of LLM Conversations in the Wild** (Hicke & Tomlinson, 2026, arXiv preprint) — about 12,000 Bing Copilot users. Individual habits are "overwhelmingly sticky"; population trends shift.
  - Relevance: real longitudinal logs. Tasks and habits, not preferences. No model.

### Sub-theme 4: Agent-based and LLM-simulated consumers with preference change (simulation, mostly system-level)
- **The Basic B*** Effect: The Use of LLM-based Agents Reduces the Distinctiveness and Diversity of People's Choices** (Matz, Horton, Goethals, 2025, arXiv preprint) — 1,000 US social-media users, about 110,000 choices. Generic and personalized agents move choices toward popular options. Personalized agents narrow topical diversity more. Effect sizes (d = 0.21 and d = 0.08 for distinctiveness) come from secondary pages; check the paper.
  - Relevance: real behavior data with an LLM agent as the intervention. Choice-level homogenization, not a formal preference state.
  - OpenAlex ID: W4416713020
  - Cited by: 6
- **Do Generative Recommenders Deepen the Information Cocoon? A Closed-Loop Simulation with LLM-powered User Simulators** (Yang et al., 2026, arXiv preprint) — RecLoop runs LLM user agents through recommend-interact-retrain cycles. Generative recommenders slow cross-user homogenization.
  - Relevance: simulation of repeated loops with LLM users. Page does not say whether user tastes update; focus is system-level exposure.
- **Simulating Filter Bubble on Short-video Recommender System with Large Language Model Agents** (Sukiennik et al., 2025, arXiv 2504.08742) — LLM agents with personalities simulate user-recommender feedback. Demographics and category attraction increase homogenization.
  - Relevance: LLM agents in a feedback loop. Agent tastes are persona-fixed in the summary; preference update not confirmed.
- **Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces** (authors not checked, 2026, arXiv preprint, arXiv 2604.08362) — compares interest trajectories of real and synthetic users over three months.
  - Relevance: tests whether simulated users match real preference drift. Search snippet only.
- **PersonaAct: Simulating Short-Video Users with Personalized Agents** (authors not checked, 2026, arXiv preprint, arXiv 2601.22547) — reports diversity decline over sustained interaction on three platforms.
  - Relevance: a sustained-interaction diversity result. Search summary only.
- **The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study** (Lin, Yun, Matarić, Canny, Gretton, D'Amour, 2026, arXiv preprint, arXiv 2605.20767) — LLM-simulated users drift in latent attributes under intervention, which biases effect estimates. Proposes negative-control attributes as a diagnostic.
  - Relevance: shows that simulated users can change in ways that bias studies. Not a model of real preference formation.

## Reference Chain Discoveries
- Found via: CoPref (arXiv 2606.30863) Related Work. It cites a Search-Experience-Credence framework from information economics. It also cites Murakhovs'ka et al. (2023) on measuring how much an agent teaches the user. Not traversed further.
- Found via: OpenAlex citers of Werner et al. (W4403746738). Citers include Salvi et al., a 2026 review of manipulation and persuasion risks, and a 2026 International AI Safety Report. Review-level only, not read.
- Found via: OpenAlex search for "Eliciting Human Preferences with Language Models" (Li et al., W4387800384, 113 citations). Its result is the closest controlled test of whether LLM elicitation shifts stated preferences. Search summary reports no shift.

## What's Missing (Gaps)
- No real-user study tracks one person's stated taste across many LLM sessions with a formal model fitted to the path. Closest: Shi et al. (28 days, emotional support) and Carrillo et al. (four waves, opinions).
- No formal economic model combines LLM-mediated dialogue with a consumer who learns own preferences. Closest: Dzyabura & Hauser (no LLM), Rafieian & Zuo (recommender, not dialogue).
- No LLM-user simulation is validated against real preference trajectories over time. Closest: Lin et al. (drift as a bias source), 2604.08362 (lead only).
- No study separates preference construction (new attributes) from preference drift (changed weights) in LLM dialogue. CoPref names the first idea; no paper measures the second in people.
- Pre-LLM theory of endogenous preferences and recommender learning (Dzyabura & Hauser; Rafieian & Zuo) has not been adapted to LLM dialogue in any paper found.

## Contradictions or Tensions
- Steering versus no shift. Werner et al. (2024) and Salvi et al. (2026) find strong single-session steering. Li et al. (ICLR 2025) report no shift in stated preferences after LM elicitation. The tasks differ: product choice versus elicitation of stated preferences.
- Repeated use shifts or does not shift. Shi et al. (2026) report daily conversations shift emotional-support preferences toward AI. Hicke & Tomlinson (2026) report individual habits are sticky. Jiang et al. (2025) report human opinions barely move. Domains and measures differ.
- Homogenization versus diversity. Matz et al. (2025) find LLM agents reduce distinctiveness of choices. Yang et al. (2026) find generative recommenders slow cross-user homogenization. The first measures agent effects on people; the second measures a recommender design.
- Simulated users are unstable. Lin et al. (2026) show drift in simulated users. CoPref (2026) uses simulated users as the testbed without a real-user check in its abstract.

## Confidence
Confidence: Medium
- What would raise confidence: a direct SSRN or NBER search with terms "preference construction", "endogenous preferences", and "generative AI", and full text of CoPref, Shi et al., and Rafieian & Zuo.
- What would lower confidence: a full-text paper that models LLM-dialogue preference change formally and fits it to real users. Any such paper would overturn "Mostly no".
- Limits: 21 WebSearch queries across ML, NLP, HCI, marketing, and economics phrasings; no direct SSRN or NBER database access; most papers read by abstract or search summary only; Rafieian & Zuo not confirmed under its SSRN ID; effect sizes from secondary pages flagged in entries.

## Search Log
### Round 1: Broad search
- Queries:
  1. LLM assistant shapes user preferences over repeated conversations preference formation model
  2. AI-mediated preference construction generative AI taste formation consumers
  3. LLM shopping assistant shapes consumer preferences model 2025
  4. preference elicitation by large language model changes what users report their preferences to be
  5. Bayesian learning consumer chatbot recommendations own tastes dynamic model SSRN
  6. agent-based simulation LLM-powered consumer agents preference change over time
  7. NBER working paper generative AI consumer preferences endogenous taste change
  8. chatbot sycophancy changes user beliefs and preferences over multi-turn dialogue longitudinal study
  9. preference drift user learning from LLM interactions arXiv 2025 simulation
  10. endogenous preferences recommender system AI assistant consumer learning own preferences theory 2026
- Papers found: result links across the 10 queries (not counted one by one); about 12 relevant after screening.
- Key leads: CoPref (2606.30863), Werner et al. (2409.12143), Salvi et al. (2604.04263), Carrillo et al. (2604.16935), Gebreegziabher et al. (2605.04029), Lin et al. (2605.20767), Dzyabura & Hauser (2019), Rafieian & Zuo.

### Round 2: Citation traversal
- Papers traversed: CoPref (W7166830829; references, 26 cited works; citers: 1); Werner et al. (W4403746738; 22 citers, top 10 read); Li et al. elicitation (W4387800384; 113 citers, not traversed); Salvi et al. (W7151421112; ID confirmed). Also read abstracts of Carrillo, Gebreegziabher, Lin, Shi, Jiang, Hicke & Tomlinson, RecLoop.
- New papers from references: CoPref's Related Work cites Murakhovs'ka 2023, Kim 2026 (DiscoverLLM), Chen 2024 (ChatShop), Li 2024 (MediQ), Qian 2025 (UserBench), Wu 2025 (CollabLLM). All assume an expert user; none studies preference change.
- New papers from citers: Salvi et al. 2026 (cites Werner); Lies, damned lies, and language statistics (2026 review of persuasion risks, 48 citations); Large Language Models Persuade Without Planning Theory of Mind (2026, 3 citations). None models preference formation.
- Rafieian & Zuo: not in OpenAlex under the SSRN title. Found under the title "Personalization, Algorithmic Dependence, and Learning" via a faculty page.

### Round 3: Reference section mining and gap-filling
- Gaps targeted: whether CoPref's Related Work or citers contain a formal preference-change model; whether any NBER or SSRN paper covers LLM-driven taste change; whether a recommender model of own-preference learning has an LLM version.
- Queries:
  1. AI agents steer people toward popular mainstream options personalized agents less exploratory real-world choices study
  2. recommender system shapes user tastes dynamic model consumer preference learning economics theory Dzyabura recommending products when consumers learn their preference weights
  3. LLM simulated users fail to capture how human preferences change with repeated AI exposure critique
  4. "preference formation" large language model user simulator Bayesian belief update multi-turn consumer
  5. SSRN generative AI chatbot consumer learning preferences model dynamic game firms steer tastes 2025
  6. AI homogenization of user tastes over time simulation recommender LLM agents "taste" convergence study 2026
- New findings: Matz et al. (2025) on homogenization; BayesBench (belief trajectories); PEBOL; Dzyabura & Hauser confirmed (Marketing Science 2019); Carroll et al. (2022) and the 2024 dynamical-systems paper on recommender-induced preference shifts; RecLoop (2026). No SSRN or NBER paper matched the dynamic game with firms steering tastes.

### Round 4: Adversarial and verification
- Gaps targeted: negative results (no shift after repeated LLM use); verification of Rafieian & Zuo; critiques of simulated users.
- Queries:
  1. Rafieian Zuo "user learning" own tastes recommender Thompson sampling SSRN 5037671
  2. Matz Horton Goethals "The Basic B*** Effect" arXiv LLM agents distinctiveness choices
  3. LLM chatbot user study no change in user preferences after repeated interaction null result negative finding
  4. Sukiennik 2025 simulating filter bubble short-video recommender LLM agents user preference evolution
  5. Fang OpenAI MIT month-long randomized study ChatGPT use daily interaction effects psychosocial 2025 arXiv
- New findings: Shi et al. (2026, 28-day OpenAI study, emotional support preferences shift toward AI when personal); Jiang et al. (2025, opinions barely move); Hicke & Tomlinson (2026, sticky habits); Fang et al. (2025 MIT/OpenAI RCT, loneliness and dependence, not tastes; arXiv 2504.03888 seen only as a search result, not fetched).

### Round 5+: Convergence check
- Round 4 produced 2 new relevant papers (Shi et al. 2026; Matz et al. 2025 verified), and no new formal model. Round 3 produced 3 formal or simulation papers (Carroll 2022 and 2024 recommender dynamics; BayesBench). Stopped after the adversarial round because the last search returned no new formal LLM-dialogue model.

### Convergence note
- Total unique relevant papers found: 22 (13 with abstract or page read, 9 from search summaries only)
- New papers in last round: 2
- Stopped because: last round produced no new formal LLM-dialogue preference model, and the adversarial queries returned only real-user evidence already listed. Stopping rule satisfied by the Round 5 adversarial check plus at least 10 query phrasings.
