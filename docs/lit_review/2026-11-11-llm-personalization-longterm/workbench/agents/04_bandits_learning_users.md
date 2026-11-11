# What online-learning / bandit / reinforcement-learning work studies personalization when the user's preferences evolve or the user is also learning — e.g. bandits with satiation or boredom, rising/rotting bandits, recommending to learning or strategic users, two-sided learning, users who explore, long-term-value RL in recommenders (e.g. YouTube REINFORCE, long-term engagement objectives) — and what regret or welfare results and failure modes (manipulation of preferences, myopia) do they find?

## TL;DR
Answer: Five strands. (1) Satiation and boredom bandits, where pulling an arm lowers its later reward and rest restores it (Leqi et al. 2021; Laforgue et al. 2021; Warlop et al. 2018). (2) Rising and rotting rested bandits, where rewards change with pulls (Fiandri et al. 2024). (3) Learning users, whose utility estimates improve from experience (Yao et al. 2022, two papers). (4) Preference-shaping models, where consumption moves tastes (Dean and Morgenstern 2022; Nadkarni et al. 2024; Zhou et al. 2021; Lankireddy et al. 2024). (5) Long-horizon RL recommenders and their manipulation risks (Chen et al. 2019; Maystre et al. 2023; Carroll et al. 2022; Evans and Kasirzadeh 2021).
Strength: Medium
Theory-heavy and mostly simulated. Few papers test preference change on real user data. Regret results depend strongly on the assumed dynamics model. Most strands assume the platform knows the dynamics or can estimate them.

## What Exists
### Sub-theme 1: Satiation, boredom and rested bandits (reward falls with repeated pulls)
- **Rebounding Bandits for Modeling Satiation Effects** (Leqi, Kilinc-Karzan, Lipton, Montgomery, 2021, NeurIPS; arXiv 2020) — Arm reward falls with consecutive pulls and recovers when unused. Greedy is optimal only for identical deterministic dynamics. Proposes Explore-Estimate-Plan for unknown stochastic dynamics. No regret bound or real-data test in the abstract.
  - Relevance: Direct model of satiation with planning requirement. Shows myopic (greedy) play fails in general.
  - OpenAlex ID: W3104509044
  - Cited by: 11
- **A Last Switch Dependent Analysis of Satiation and Seasonality in Bandits** (Laforgue, Clerici, Cesa-Bianchi, Gilad-Bachrach, 2021, arXiv) — Reward depends on time since the arm last switched. Captures progressive satiation and seasonality. Proves a regret bound against the NP-hard optimal non-stationary policy. Preliminary experiments only.
  - Relevance: Generalizes satiation to delayed, seasonal effects. Relevant to taste recovery over time.
  - OpenAlex ID: W3208492374
  - Cited by: 5
- **Fighting Boredom in Recommender Systems with Linear Reinforcement Learning** (Warlop, Lazaric, Mary, 2018, NeurIPS) — Recommendations change tastes. Models this as an MDP with linear reward dependence on recent actions. LinUCRL gets a regret bound independent of the number of states. Tests on synthetic and real-data environments.
  - Relevance: Earliest RL treatment of boredom in recommenders found in this search. Shows exploration must account for taste change.
  - OpenAlex ID: not resolved in this run
- **Modeling Attrition in Recommender Systems with Departing Bandits** (Ben-Porat, Cohen, Leqi, Lipton, Mansour, 2022, AAAI) — Users leave when dissatisfied, so the policy controls session length. Unknown user types. One type: UCB-type policy is optimal. Two types: Õ(√T) regret.
  - Relevance: Adds user departure (attrition) as a welfare channel. Connects satisfaction to retention.
  - OpenAlex ID: W4283812815
  - Cited by: 9

### Sub-theme 2: Rising and rotting bandits (arm reward changes with use)
- **Rising Rested Bandits: Lower Bounds and Efficient Algorithms** (Fiandri, Metelli, Trovò, 2024, arXiv) — Arm rewards are rested and non-decreasing and concave. Gives regret lower bounds and the R-ed-UCB algorithm, with Õ(T^{2/3}) regret under conditions. Tests on synthetic tasks and one real dataset (model selection).
  - Relevance: Rising case of the rested family, the mirror image of satiation. Splitting pulls evenly across identical rising arms can give linear regret (per search snippets of the Amichay thesis).
  - OpenAlex ID: not resolved in this run
- Search snippets also report a worst-case lower bound for infinite-armed rotting bandits (Kim, Vojnović, Yun), and a sliding-window algorithm with Õ(K^{1/3}T^{2/3}) regret (Levine et al.). Not read in full. Treat as leads only.

### Sub-theme 3: Learning users (the user's utility is learned during the interaction)
- **Learning from a Learning User for Optimal Recommendations** (Yao, Li, Nekipelov, Wang, Xu, 2022, ICML; arXiv 2202.01879) — Users learn item utilities from experience, so feedback is non-stationary. The RAES algorithm uses comparative feedback from two-item slates. Regret degrades gracefully with user learning rate and becomes linear if user learning never converges. Synthetic data only.
  - Relevance: Two-sided learning in its clearest form. Shows regret depends on how fast the user learns.
  - OpenAlex ID: W4226116300
  - Cited by: 1
- **Learning the Optimal Recommendation from Explorative Users** (Yao, Li, Nekipelov, Wang, Xu, 2022, AAAI; arXiv 2110.03068) — Companion paper from the same group on users who explore. Search snippet only. Did not read the full text.
  - Relevance: Covers the "users who explore" case directly.
  - OpenAlex ID: W3204296881
  - Cited by: 5
- **Optimal recommendation to users that react: Online learning for a class of POMDPs** (2016, CDC) — Lead found in OpenAlex. Authors and content not checked.
  - OpenAlex ID: W2331759129
  - Cited by: 21

### Sub-theme 4: Preference dynamics and preference shaping (recommendations move tastes)
- **Preference Dynamics Under Personalized Recommendations** (Dean, Morgenstern, 2022, EC) — Users move toward content they enjoy and away from content they dislike. Constant regret is easy to achieve, so the real goal is approximate stationarity of preferences. Personalization can collapse preferences, while randomized recommendations keep them stable. No experiments in the abstract.
  - Relevance: Key theory paper on regret being trivial while welfare is not. Builds on biased-assimilation opinion dynamics (Hazla et al. 2019; Gaitonde et al. 2021).
  - OpenAlex ID: W4285088850
  - Cited by: 37
- **Influencing Bandits: Arm Selection for Preference Shaping** (Nadkarni, Manjunath, Moharir, 2024, arXiv) — Observed rewards reinforce population preferences. Goal is to shape preferences toward a target arm, not to maximize reward. Explore-then-Commit and Thompson sampling give logarithmic regret in the known-horizon case. Experiments unclear from abstract.
  - Relevance: Makes the platform's objective preference shaping. Shows the manipulation-as-goal case.
  - OpenAlex ID: not resolved in this run
- **Influence of Recommender Systems on Users: A Dynamical Systems Analysis** (Lankireddy, Nair, Manjunath, 2024, arXiv) — Contextual linear bandit coupled with preference drift toward recommended items. Mean dynamics approximated by a deterministic system via stochastic approximation. Claims exploitation can polarize preferences. Theory only.
  - Relevance: Shows the exploration-exploitation trade-off itself shapes long-run preferences.
  - OpenAlex ID: not resolved in this run
- **Incentivized Bandit Learning with Self-Reinforcing User Preferences** (Zhou, Liu, Dong, Deng, 2021, ICML) — Platform must pay users to pull arms. Popular arms attract like-minded users. Two policies give O(log T) regret with O(log T) payment. No incentivized policy gets sublinear regret and sublinear payment under super-polynomial feedback growth.
  - Relevance: Welfare cost of influence is quantified as payments. Clear impossibility result.
  - OpenAlex ID: not resolved in this run
- **Harm Mitigation in Recommender Systems under User Preference Dynamics** (Chee, Kalyanaraman, Ernala, Weinsberg, Dean, Ioannidis, 2024, KDD; arXiv 2406.09882) — Trades off click-through rate against harmful content under preference dynamics. Finds stationary points and algorithms for optimal policies at stationarity. Semi-synthetic movie data. A harm penalty alone may do nothing if dynamics are ignored.
  - Relevance: Shows that ignoring dynamics can make standard harm penalties ineffective.
  - OpenAlex ID: W4401863955
  - Cited by: 10

### Sub-theme 5: Long-horizon and long-term-value RL in recommenders, with manipulation risks
- **Top-K Off-Policy Correction for a REINFORCE Recommender System** (Chen, Beutel, Covington, Jain, Belletti, Chi, 2019, WSDM as reported in search; arXiv 2018) — Production YouTube REINFORCE with millions of actions. Off-policy correction for logged feedback. Top-K correction for multi-item slates. Live results reported in a secondary source only: about 0.85% ViewTime gain at K=16 (not verified on the paper).
  - Relevance: Industrial case of RL recommenders optimizing long-run engagement signals. The paper itself does not frame preference change.
  - OpenAlex ID: W2902572901
  - Cited by: 434
- **Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective** (Maystre, Russo, Zhao, 2023, arXiv; v3 2024) — Podcast recommender for listening journeys spanning months. Reports substantial long-term gains in A/B tests versus short-term proxy metrics (no effect size in abstract). Offline data reduction up to 120,000x claimed, described as illustrative.
  - Relevance: Industrial evidence for the long-horizon side. The myopic baseline is called "short-term proxy metrics."
  - OpenAlex ID: not resolved in this run
- **Improving Long-Term Metrics in Recommendation Systems using Short-Horizon Reinforcement Learning** (Mazoure, Mineiro, Srinath, Sharifi Sedeh, Precup, Swaminathan, 2021, arXiv) — Session-based SHPI adds a termination bonus to approximate cross-session drift. Beats matrix factorization, myopic bandits and RL baselines across four tasks. Effect sizes not in abstract.
  - Relevance: Gives a middle path: long-term value without full RL.
  - OpenAlex ID: not resolved in this run
- **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** (Carroll, Hadfield-Menell, Russell, Dragan, 2022, ICML; earlier RecSys 2021 version under the title "Estimating and Penalizing Preference Shift in Recommender Systems") — Long-horizon recommenders have incentives to manipulate users. Learns a user-dynamics model and penalizes shifts outside a trust region of "natural" shifts (random recommender baseline). Simulated results: manipulation avoided with engagement kept. Notes that myopic recommenders also produce undesired shifts.
  - Relevance: Central paper on manipulation as a failure mode of long-horizon optimization, and of myopic optimization.
  - OpenAlex ID: not resolved in this run (arXiv 2204.11966)
- **User Tampering in Reinforcement Learning Recommender Systems** (Evans, Kasirzadeh, 2021 FAccTRec; AIES 2023) — Causal argument that RL recommenders can shape user views to raise later engagement. Simulated political-content case: a Q-learning agent polarizes users early to succeed later. Argues RL-only media recommenders are unsafe or commercially unviable.
  - Relevance: Names user tampering as a failure mode. Simulation is one toy environment.
  - arXiv: 2109.04083
- **Degenerate Feedback Loops in Recommender Systems** (Jiang, Chiappa, Lattimore, György, Kohli, 2019, AIES) — Models interest as a dynamical system. Gives conditions under which interest degenerates to extremes, with deterministic and stochastic dynamics. Separates echo chamber from filter bubble effects.
  - Relevance: Formal base for feedback-loop collapse in recommenders.
  - OpenAlex ID: W2917760808
  - Cited by: 272
- **Feedback Loop and Bias Amplification in Recommender Systems** (Mansoury et al., 2020, CIKM) — Simulated loop amplifies popularity bias over iterations across UserKNN, BPR and MostPopular. Impact is stronger for minority-group users.
  - Relevance: Welfare inequality across groups under a feedback loop. Simulation only.
  - OpenAlex ID: W3044938582
  - Cited by: 307
- **AI Alignment with Changing and Influenceable Reward Functions** (Carroll, Foote, Siththaranjan, Russell, Dragan, 2024, ICML) — DR-MDP framework. Argues static-preference alignment rewards influencing users. Overlaps with the alignment stream. Not recommender-specific in the snippet.
  - OpenAlex ID: W4399151482
  - Cited by: 41

## Reference Chain Discoveries
- Found via: Preference Dynamics (Dean and Morgenstern 2022) references: Rebounding Bandits (already found), Preference Amplification in Recommender Systems (2021, cites 43), Estimating and Penalizing Preference Shift (2021, cites 27), User Tampering (already found), Fighting Boredom (already found), A Theory of Chosen Preferences (2019, cites 87), The Challenge of Understanding What Users Want (Stray et al. area, 2023, cites 69), Hidden Incentives for Auto-Induced Distributional Shift (2020, cites 63), Degenerate Feedback Loops (already found), Feedback Loop and Bias Amplification (already found), Top-K Off-Policy Correction (already found), Performative Prediction (2020, cites 120; adjacent to stream 01), Decision-Dependent Risk Minimization in Geometrically Decaying Dynamic Environments (2022, cites 9).
- Found via: Citers of Rebounding Bandits: Modeling Attrition (already found), A Last Switch Dependent Analysis (already found), A Field Test of Bandit Algorithms for Recommendations (2023, cites 7), Combinatorial Blocking Bandits with Stochastic Delays (2021, cites 6), State-Separated SARSA: Recovering Rewards (2026, cites 2), Learning the Optimal Control for Evolving Systems with Converging Dynamics (2024, cites 1).
- Found via: Citers of Preference Dynamics: Harm Mitigation (already found), The Impact of Recommendation Systems on Opinion Dynamics (2023, cites 10), User Welfare Optimization with Competing Content Creators (2024, cites 15), Incentivizing High-Quality Content in Online Recommender Systems (2023, cites 17), Mapping the Design Space of Teachable Social Media Feed Experiences (2024, cites 34), Leveraging LLMs for Collective Decision-Making (2025, cites 27; LLM-related, stream 05 overlap).
- Found via: Citers of Learning from a Learning User: Personalized Algorithms and the Virtue of Learning Things the Hard Way (2024, cites 1). Not read.
- Found via: Round 4 search "is long-term optimization worth it": Reassessing the Effectiveness of Reinforcement Learning in Sequential Recommendation (authors not checked; snippet says a tuned original baseline outperforms prior RL variants).
- Found via: Round 1 search on Algorithmic Drift: Coppolillo et al. (2024), stochastic simulation with drift metrics. Snippet only; not read.

## What's Missing (Gaps)
- No paper combines a satiation model, a learning user, and a long-horizon RL objective with regret and welfare results in one setting. The closest pairs are Dean and Morgenstern (dynamics, welfare) and Yao et al. (learning users, regret).
- Few regret results cover preference shift with real user data. Most evidence is synthetic or semi-synthetic (Chee et al. 2024 is a partial exception).
- No head-to-head test of myopic versus long-horizon recommenders on preference shift with the same user model. Carroll et al. (2022) gives partial simulated evidence only.
- Welfare results for two-sided learning are sparse. Yao et al. (2022) cover the platform's regret, not the user's welfare.
- Satiation models are mostly for bandit arms (content), not for user taste states learned across many users.

## Contradictions or Tensions
- Regret versus welfare: Dean and Morgenstern (2022) say constant regret is easy. Stationarity is the hard target. Standard regret does not measure user harm. Chee et al. (2024) and Carroll et al. (2022) agree that welfare needs its own objective.
- Myopia: Carroll et al. (2022) say myopic recommenders also shift preferences. Maystre et al. (2023) and Mazoure et al. (2021) argue that long-horizon optimization helps. Spotify's own earlier draft concedes a myopic strategy may be nearly optimal (search snippet). Evidence on whether long-term objectives help is mixed.
- Direction of polarization: Lankireddy et al. (2024) say exploitation polarizes. Dean and Morgenstern (2022) say personalization collapses preferences, and randomized recommendations keep them stationary. These are consistent but use different mechanisms.
- Learning versus drift: Yao et al. (2022) treat user change as learning that converges. Dean and Morgenstern (2022) treat it as drift toward consumed content. Regret conclusions differ: linear regret if learning never converges, versus constant regret for drift.
- Long-term RL gains: Chen et al. (2019) and Maystre et al. (2023) report industry gains. Reassessment work (snippet) suggests tuned baselines can match RL variants. Industry claims are not independently replicated.

## Confidence
Medium
- What would raise confidence: A replicated regret and welfare result on real user data with a measured preference-shift outcome (e.g., Chee et al. 2024 extended to real logs). Full text of Yao et al. (2022) and Nadkarni et al. (2024) with stated bounds and experiments.
- What would lower confidence: Evidence that the satiation or learning models fit real users poorly. A strong tuned myopic baseline that matches long-term RL on preference metrics.

Caveats on this run: Most entries come from abstracts, search snippets or the summarizer, not full texts. Authors and venues for Modeling Attrition, Top-K Off-Policy Correction and Degenerate Feedback Loops were checked against snippets, not full papers. The Carroll 2022 ICML version and the RecSys 2021 version are treated as one paper line. Round 2 traversal covered the three seed papers and Dean and Morgenstern's reference list. Two-hop traversal was not run because no directly relevant paper had more than 50 citations.

## Search Log
### Round 1: Broad search
- Queries: (1) bandits satiation boredom preferences decline with repeated recommendations; (2) rising and rotting bandits regret; (3) recommending to learning users, two-sided learning; (4) strategic users, manipulation, myopic, long-term welfare; (5) YouTube REINFORCE long-term satisfaction; (6) Dean Morgenstern preference dynamics; (7) bandit preference shaping regret; (8) Kleinberg Raghavan monoculture; (9) Mansoury feedback loop preference drift; (10) long-term value RL RecSim.
- Papers found: about 45 candidate hits across 10 queries; 14 judged relevant after reading snippets.
- Key leads: Rebounding Bandits (satiation), Learning from a Learning User (learning users), Preference Dynamics (preference dynamics). Other leads: Top-K REINFORCE, Mansoury 2020, Fighting Boredom.

### Round 2: Citation traversal
- Papers traversed: Rebounding Bandits (W3104509044), Learning from a Learning User (W4226116300), Preference Dynamics (W4285088850), with their citers (top 10 by citations each) and the reference list of Preference Dynamics (35 references resolved to titles).
- New papers from references: Preference Amplification in Recommender Systems; Estimating and Penalizing Preference Shift; A Theory of Chosen Preferences; The Challenge of Understanding What Users Want; User Tampering; Hidden Incentives for Auto-Induced Distributional Shift; Degenerate Feedback Loops; Feedback Loop and Bias Amplification; Performative Prediction; Fighting Boredom; Top-K REINFORCE.
- New papers from citers: Last Switch Dependent Analysis; Modeling Attrition; Harm Mitigation; Influencing Bandits (via search); Opinion-dynamics impact paper (2023); User Welfare Optimization with Competing Content Creators (2024); AI Alignment with Changing and Influenceable Reward Functions (2024).

### Round 3: Reference section mining
- Papers: abstracts fetched for Rebounding Bandits, Learning from a Learning User, Preference Dynamics, Last Switch Dependent Analysis, Rising Rested Bandits, Influencing Bandits, Lankireddy et al., Optimizing Audio Recommendations, Improving Long-Term Metrics, Chen et al. (YouTube). Full related-work sections not fetched.
- New findings: Yao et al. (2022) has a companion AAAI paper; Carroll et al. (2022) has an earlier RecSys 2021 version; Chee et al. (2024) authorship confirmed via search.

### Round 4: Gap-filling
- Gaps targeted: boredom in RL recommenders; preference-shift estimation; long-horizon RL recommender evidence; incentivized bandits with self-reinforcing preferences; Modeling Attrition authorship.
- Queries: Fighting Boredom authorship; Carroll 2024 ICML; Carroll 2022 preference shift; long-term engagement RL 2024-2025; Zhou 2021 incentivized bandits; Modeling Attrition authorship.
- New findings: Zhou et al. (2021) two policies with O(log T) regret. Carroll 2022 gives a penalty method. No 2024-2025 paper found that directly compares myopic and long-horizon preference shaping.

### Round 5: Adversarial check
- Queries: critique of long-term optimization versus myopic baselines; user tampering critiques; limits of Carroll et al. penalty.
- New findings: Snippets report a tuned baseline matching RL variants in sequential recommendation (reassessment work), and a Spotify draft conceding a myopic strategy may be nearly optimal. Neither was read in full.

### Round 6+: Follow leads
- Leads followed: Rising Rested Bandits (abstract fetched), Harm Mitigation (search), Lankireddy et al. (abstract fetched). The 2-hop traversal was skipped for papers under 50 citations.
- Dead end: Algorithmic Drift (Coppolillo et al. 2024) snippet only; full text not read. A fetch of an unrelated arXiv URL returned 404 and was not used.

### Convergence note
- Total unique relevant papers found: about 24 (listed above with resolved or unresolved IDs).
- New papers in last round: 3 (Reassessment work, Spotify draft concession, Algorithmic Drift).
- Stopped because: Last two rounds found few new papers on the core question. Remaining new hits were on adjacent topics (monoculture, RL critiques) and were not relevant enough to pursue further. Hard cap not reached.
