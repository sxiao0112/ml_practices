# What theoretical models describe the long-run feedback loop between a personalization system (recommender, search ranker) and user preferences — e.g. preference amplification, filter bubbles, degenerate feedback loops, performative prediction, induced preference shift — and what do they predict about polarization, homogenization, welfare and convergence? Include key results (fixed points, conditions for drift) and which assumptions drive them.

## TL;DR
Answer: Four model families study this loop. (1) Preference-drift models: users drift toward what they are shown, and Kalimeris et al. (2021) find no fixed point, so concentration grows. Dean and Morgenstern (2022) show stationarity can be designed when preferences are known. (2) Degenerate-dynamics models: Jiang et al. (2019) give sufficient conditions for collapse to extremes. (3) Performative-prediction models: Perdomo et al. (2020) give convergence conditions for retraining when predictions shift outcomes. (4) Homogenization and welfare models: Chaney et al. (2018) simulate homogenization, and Kleinberg and Raghavan (2021) show monoculture can lower welfare.
Strength: Medium
Most results are simulations or stylized models with strong assumptions (drift direction, stochastic choice parameter, content richness). Few results are proofs about real platforms. The welfare claims for recommenders are mostly extrapolated from hiring or screening models.

## What Exists
### Sub-theme 1: Preference drift and amplification (user preferences move toward recommended content)
- **Preference Amplification in Recommender Systems** (Kalimeris, Bhagat, Kalyanaraman, Weinsberg, 2021, KDD)  — Matrix-factorization model with a softmax-like parameter beta. Users drift toward items the system scores highly. Authors report no fixed point exists under mild drift, so recommendations concentrate. Higher beta (less randomness) amplifies more. Mitigations: global removal of problematic items and personal downranking.
  - Relevance: The core model of "amplification" in the question. Fixed-point claim is from the Meta research blog summary; the full paper PDF was not readable.
  - OpenAlex ID: W3172701938
  - Cited by: 43
- **Preference Dynamics Under Personalized Recommendations** (Dean, Morgenstern, 2022, ACM EC)  — Users' tastes drift toward content they like and away from content they dislike (biased assimilation). Standard reward maximization is nearly trivial: simple algorithms get constant regret. Given known initial preferences, an algorithm keeps preferences approximately stationary when the content set is rich, with logarithmic regret. Randomization can also keep preferences stationary. Identifying initial preferences is harder because observation itself changes them.
  - Relevance: Shows the designer can prevent drift, not just measure it. Its stationarity result depends on known preferences and rich content.
  - OpenAlex ID: W4285088850 (arXiv 2205.13026)
  - Cited by: 37
- **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** (Carroll et al., 2022, ICML)  — Long-horizon recommenders can shift user preferences to become easier to satisfy. Proposes learning a user dynamics model from logs, then optimizing inside a trust region of "safe" shifts (natural drift without intervention). Simulations show the method keeps engagement while avoiding manipulative shifts. Simulations also show engagement-maximizing policies pull preferences toward a few attractor points.
  - Relevance: Frames induced preference shift as a design variable and offers an estimation and penalty method. Its evidence is simulation-based.
  - OpenAlex ID: W4224979542 (arXiv 2204.11966)
  - Cited by: 18
  - Related earlier version: **Estimating and Penalizing Preference Shift in Recommender Systems** (Carroll, Hadfield-Menell, Russell, 2021, RecSys), OpenAlex ID W3199782056, cited by 27. Not read.
- **Degenerate Feedback Loops in Recommender Systems** (Jiang, Chiappa, Lattimore, György, Kohli, 2019, AAAI/ACM AIES)  — Models user interests as a dynamical system with absorbing extremes ("degeneracy"). Gives sufficient conditions for degeneracy under deterministic and stochastic dynamics. An oracle recommender degenerates quickly. Continuous random exploration and a candidate pool growing at least linearly slow degeneracy.
  - Relevance: The closest formal model of "degenerate feedback loops" and of which design levers slow them.
  - OpenAlex ID: W2917760808 (arXiv 1902.10730)
  - Cited by: 272
- **The Amplification Paradox in Recommender Systems** (Ribeiro, Veselovsky, West, 2023, ICWSM)  — Agent-based model. Users who follow recommendations blindly drift toward niche extreme content, but rarely choose it when offered a choice. Net effect can be de-amplification. Argues audit studies alone cannot measure filter-bubble prevalence without modeling user choice.
  - Relevance: Adds a user-choice term that can cancel drift. Important counterpoint to amplification models. Based on the abstract and search summary; the model's assumptions about user utility drive the result.
  - OpenAlex ID: W4380302108
  - Cited by: 28

### Sub-theme 2: Performative prediction (the prediction changes the outcome it predicts)
- **Performative Prediction** (Perdomo, Zrnic, Mendler-Dünner, Hardt, 2020, ICML, PMLR 119)  — Defines performative predictions, which change the data distribution they forecast. Introduces "performative stability" as the equilibrium notion. Gives necessary and sufficient conditions for retraining to converge to a performatively stable point with near-minimal loss. Subsumes strategic classification.
  - Relevance: The general framework for "prediction changes the user." Recommenders are a natural case, but the paper does not model preference change directly.
  - OpenAlex ID: W3034367601
  - Cited by: 120
  - Note: the search result listed "Miller" as a co-author; OpenAlex and the PMLR abstract list Zrnic and Mendler-Dünner. The OpenAlex list is used here.
- **Stochastic Optimization for Performative Prediction** (Mendler-Dünner, Perdomo, Zrnic, Hardt, 2020, NeurIPS)  — Stochastic variant in which the distribution shifts with each deployed model. Not read in full; from search summary.
  - Relevance: Gives the algorithmic counterpart for repeated retraining.
  - OpenAlex ID: W3035048992
  - Cited by: 30
- **Performative Prediction: Past and Future** (Hardt, Mendler-Dünner, 2025, Statistical Science)  — Survey of the performative prediction literature. Not read in full; metadata from OpenAlex.
  - Relevance: Recent overview to check for the state of convergence results.
  - OpenAlex ID: W4414298153
  - Cited by: 73
- **Performative Recommendation: Diversifying Content via Strategic Incentives** (Eilat, Rosenfeld, 2023, ICML, PMLR 202)  — Treats recommendation as performative prediction where creators respond to the recommender. Adds a regularizer that anticipates creator adaptation and penalizes homogeneity. Analytic and semi-synthetic experiments show ignoring strategic creators leads to homogenization. From search summary; not read.
  - Relevance: Links the performative framework to homogenization. Creators, not users, are the responders here.
  - OpenAlex ID: not looked up

### Sub-theme 3: Homogenization and monoculture (many users or systems converge on the same content)
- **How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility** (Chaney, Stewart, Engelhardt, 2018, ACM RecSys)  — Simulation. Recommenders trained on their own confounded interaction data increase behavior homogenization at population and subgroup levels. Homogenization often lowers utility for users with minority tastes. Evaluating on confounded held-out data favors systems similar to the one that generated the data.
  - Relevance: The most cited simulation of homogenization from a feedback loop. Results are for one simulated setup. The T-RECS framework (arXiv 2107.08959) reruns this setup with 400 trials per model.
  - OpenAlex ID: W2765564115
  - Cited by: 419
- **Feedback Loop and Bias Amplification in Recommender Systems** (Mansoury, Abdollahpouri, Pechenizkiy, Mobasher, 2020, ACM CIKM)  — Studies bias amplification through repeated recommendation cycles on popularity-biased data. Not read in full; metadata and citation count from OpenAlex.
  - Relevance: Empirical companion to Chaney et al. on bias amplification.
  - OpenAlex ID: W3044938582
  - Cited by: 307
- **Algorithmic Monoculture and Social Welfare** (Kleinberg, Raghavan, 2021, PNAS)  — When many decision-makers use one algorithm, welfare can fall even if the algorithm is more accurate than each individual decision-maker. The model covers hiring and screening, not recommenders.
  - Relevance: The main welfare result for shared algorithms. Its mechanism is an analogy for recommenders, not a recommender model.
  - OpenAlex ID: W3164854573
  - Cited by: 248
- **Price of Anarchy of Algorithmic Monoculture** (Kleinberg, Sinanaj, Tardos, 2026, arXiv)  — Bounds the welfare loss from monoculture in a one-sided matching model. A secondary summary reports a tight price-of-anarchy bound of 2. Not verified against the paper.
  - Relevance: Gives a worst-case welfare bound for the monoculture model above.
  - OpenAlex ID: W7148275320
  - Cited by: 2

### Sub-theme 4: Welfare-optimal and creator-side models
- **Optimizing Long-term Social Welfare in Recommender Systems: A Constrained Matching Approach** (Mladenov, Creager, Ben-Porat, Swersky, Zemel, Boutilier, 2020, ICML, PMLR 119)  — Treats provider and user dynamics as an induced dynamical system. Picks among equilibria by solving a constrained matching problem. Myopic best-match recommendation performs poorly in a stylized model. Not read in full; from search summary.
  - Relevance: Shows welfare depends on which equilibrium the recommender selects.
  - OpenAlex ID: W3034922058
  - Cited by: 26
- **Modeling Content Creator Incentives on Algorithm-Curated Platforms** (Hron, Krauth, Jordan, Kilbertus, Dean, 2023, ICLR)  — Defines an "exposure game" where creators compete for limited user attention. Shows that algorithm design choices, such as non-negative factorization, change whether equilibria exist. Proposes such models for pre-deployment audits. Based on the arXiv abstract listing.
  - Relevance: Equilibrium-level model of supply-side feedback. Does not model user preference change.
  - OpenAlex ID: W4283689735 (arXiv 2206.13102)
  - Cited by: 38

### Sub-theme 5: Other feedback-loop models (lower confidence, from search summaries only)
- **The Feedback Loop Between Recommendation Systems and Reactive Users** (Mollabagher, Naghizadeh, 2025, arXiv 2504.07105)  — Engagement-maximizing recommender and users whose opinions react to content. Validated with numerical experiments. Not read.
  - OpenAlex ID: not looked up
- **Hidden Feedback Loops in Bandit Recommenders** (Khritankov, Pilkevich, 2021, arXiv 2109.05278)  — Multi-armed bandit recommender with noisy user interests. Feedback loops degrade recommendations to a small subset and reduce coverage and novelty. Not read.
  - OpenAlex ID: not looked up
- **Human–AI adaptive dynamics drives the emergence of information cocoons** (Piao, Liu, Zhang, Su, 2023, Nature Machine Intelligence)  — Human-AI co-adaptation model that produces information cocoons (narrow content exposure). Abstract not read; metadata from OpenAlex.
  - OpenAlex ID: W4387451903
  - Cited by: 108
- **Breaking Feedback Loops in Recommender Systems with Causal Inference** (Krauth, Wang, Jordan, 2025, ACM TORS)  — Causal correction for feedback loops in recommendation. Not read; metadata from OpenAlex.
  - OpenAlex ID: W4409963658
  - Cited by: 34

## Reference Chain Discoveries
- Found via: OpenAlex citers of Kalimeris et al. (2021): Dean and Morgenstern (2022, EC), Piao et al. (2023), and Ribeiro et al. (2023). Dean and Morgenstern was already in the search list.
- Found via: OpenAlex references of Kalimeris et al. (2021), which include Performative Prediction (W3035048992) and other performative work. The Mendler-Dünner et al. NeurIPS paper came from this list.
- Found via: OpenAlex citers of Performative Prediction (2020): Hardt and Mendler-Dünner (2025) survey, and Stochastic Optimization decision-dependent work (W3109064640, not read).
- Found via: OpenAlex citers of Chaney et al. (2018): Mansoury et al. (2020), a popularity-bias and feedback-loop cluster (not read).
- Found via: a direct search for monoculture work (not the Chaney reference list). Kleinberg and Raghavan (2021) and Kleinberg, Sinanaj and Tardos (2026) were found this way.
- Found via: Round 3 reference mining was not completed in full. The Related Work sections of Kalimeris et al. and Dean and Morgenstern were not fetched.

## What's Missing (Gaps)
- **No direct convergence theorem for the full loop with a learning user.** Dean and Morgenstern solve stationarity for known preferences. Kalimeris et al. show non-existence of fixed points for their drift model. No paper gives a general long-run convergence characterization for a learning recommender and a learning user.
- **Few welfare results for recommenders.** Kleinberg and Raghavan's welfare result is from hiring. The recommender welfare results (Mladenov et al. 2020; Eilat and Rosenfeld 2023) rely on creator or provider models, not user preference drift.
- **Model disagreement is not tested on real data.** Ribeiro et al. (2023) and Kalimeris et al. (2021) predict opposite effects of the same drift. No study compares the two on the same platform data.
- **Few results with LLM-style generative recommenders.** The models above assume a fixed item catalog and a matrix-factorization or bandit recommender. Generative systems that write content, or that shift a user's wording, are outside them.

## Contradictions or Tensions
- **Amplification vs. de-amplification.** Kalimeris et al. (2021) predict concentration with no fixed point. Ribeiro et al. (2023) predict de-amplification when users can choose. The difference is whether users follow recommendations blindly (Kalimeris) or choose freely (Ribeiro).
- **Stationarity is possible vs. drift is inevitable.** Dean and Morgenstern (2022) show a designed policy can keep preferences stationary, given known preferences and rich content. Kalimeris et al. (2021) show drift is not stopped by mild dynamics. The two results use different drift models and different knowledge assumptions.
- **Simulation homogenization vs. empirical nulls.** Chaney et al. (2018) and Piao et al. (2023) find homogenization in simulation. Guess, Malhotra and Pan (2023, Science) and Nyhan et al. (2023, Nature) found that changing Facebook feed ranking for three months did not significantly change issue polarization in the 2020 U.S. election study. Garcia's Nature commentary notes these are short, single-election studies. The search summaries here do not report the methods in detail.
- **Degeneracy is a user-side property.** Jiang et al. (2019) find that user dynamics drive degeneracy, and the recommender only speeds or slows it. This contrasts with Carroll et al. (2022), where the recommender's choice selects the induced shift.

## Confidence
Medium
- What would raise confidence: Reading the full text of Kalimeris et al. (2021) to check the non-existence-of-fixed-point theorem and its beta condition. A replication of Chaney et al. (2018) with a learning user. A paper testing Dean and Morgenstern (2022) stationarity under unknown preferences.
- What would lower confidence: A demonstration that the non-existence result depends on a specific drift form. A field result showing that user choice removes amplification at scale, as Ribeiro et al. (2023) argue for simulations.

## Search Log
### Round 1: Broad search
- Queries: (1) feedback loops recommender systems preference shift theoretical model dynamic; (2) performative prediction Perdomo Miller Zrnic Hardt 2020; (3) filter bubble recommender polarization model Dean Morgenstern Kleinberg Raghavan Mullainathan 2022; (4) Kleinberg Raghavan algorithmic monoculture homogenization recommender welfare; (5) induced preference shift recommender system user preferences learning dynamics fixed point
- Papers found: about 25 distinct hits across 5 queries; about 12 unique relevant papers.
- Key leads: Kalimeris et al. (2021); Dean and Morgenstern (2022); Perdomo et al. (2020); Carroll et al. (2022); Jiang et al. (2019).
- Note: Query 3 included a 2022 Dean/Morgenstern/Kleinberg/Raghavan/Mullainathan author list that did not match any found paper. The search found no such paper, so it is not included. Query 2 contained a wrong co-author name, which was corrected.

### Round 2: Citation traversal
- Papers traversed: Kalimeris et al. (2021, W3172701938); Perdomo et al. (2020, W3034367601); Chaney et al. (2018, W2765564115). Top 10 citers and 38 to 71 references were pulled for each.
- New papers from references: Mendler-Dünner et al. (2020, NeurIPS); Performative prediction references were mostly outside this review's scope.
- New papers from citers: Dean and Morgenstern (2022); Piao et al. (2023); Ribeiro et al. (2023); Hardt and Mendler-Dünner (2025); Mansoury et al. (2020); Hron et al. (2023) via a follow-up search.
- Also run: OpenAlex lookups for Jiang et al. (2019), Mladenov et al. (2020), Carroll et al. (2022), Krauth et al. (2025).

### Round 3: Reference section mining
- Planned for the top 2 papers. Full text of Kalimeris et al. was not readable (Meta PDF redirected, ACM DOI returned 403). The Meta research blog summary was read instead, which describes the same model and results. Dean and Morgenstern was read via arXiv abstract.
- Related Work sections were not mined. This is a known gap.
- New papers: none added from this step.

### Round 4: Gap-filling
- Gaps targeted: (a) recommender welfare with preference dynamics; (b) empirical tests of feed-based polarization; (c) recent (2024-2026) convergence or homogenization proofs.
- Queries: Mladenov et al. welfare query; Guess and Nyhan polarization query; 2024-2025 bandit and Bayesian convergence query.
- New findings: Mladenov et al. (2020); Guess et al. (2023); Nyhan et al. (2023) (title "Like-minded sources on Facebook are prevalent but not polarizing", Nature). No 2024-2025 convergence proof for a Bayesian or bandit user model was found. Closest 2025-2026 work: a confirmation-aware closed-loop model (arXiv 2508.11516) claims a convergence condition, not read.

### Round 5: Adversarial check
- Gaps targeted: critiques of amplification; null empirical results; contrasting models.
- Queries: Ribeiro et al. critique query; Guess and Nyhan critique query.
- New findings: Ribeiro et al. (2023) de-amplification argument. Garcia's Nature commentary argues the null result does not rule out feed algorithms as a cause. No methodological rebuttal of the Science or Nature studies was found.

### Round 6: Gap-filling, follow-up
- Gaps targeted: performative recommendation (creator-side); user-side welfare models.
- Queries: performative recommendation query; Hron et al. query; Krauth et al. query.
- New findings: Eilat and Rosenfeld (2023); Hron et al. (2023). The Narang et al. (2022) multiplayer performative prediction paper (W4223571424) is related but outside user-preference drift.
- Searches and OpenAlex lookups found no further unseen papers that bear directly on user-preference feedback theory.

### Convergence note
- Total unique relevant papers found: about 26 (about 20 with OpenAlex IDs, about 6 from search summaries only).
- New papers in last round: 2 relevant (Eilat and Rosenfeld 2023; Hron et al. 2023), both creator-side.
- Stopped because: rounds 5 and 6 added only creator-side or contrasting results and no new user-preference models. The stopping rule (two empty rounds) was not strictly met, since round 6 still added two creator-side papers. Stopped for time, not for saturation. Round 3 reference mining was not finished.
