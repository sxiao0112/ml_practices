# How have researchers estimated user preference dynamics from longitudinal real data (structural estimation of taste evolution, preference drift detection in recommender logs, dynamic user embeddings, state-space or hidden Markov taste models, Kuaishou/Spotify/MovieLens trajectories) and how have user simulators (especially LLM-agent simulators with memory or evolving preferences) been validated against real longitudinal behavior? What methods and datasets would let one calibrate and validate a simulation of preference change under LLM influence?

## TL;DR
Answer: Three groups estimate taste change from real logs: structural panel models (state dependence, habit, migration natural experiments), learned recommender-log models (HMM change detection, temporal matrix factorization, learned preference-shift models), and field experiments on Spotify. LLM simulators with memory or evolving profiles are checked mostly against static or short-session accuracy, not against real individuals tracked over months. The closest longitudinal check is OmniBehavior (Kuaishou logs, 200 users, 3 months), which compares drift rates of real and LLM-simulated users.
Strength: Medium
No simulator found validates an individual's preference path over months against that person's real logs. The structural and field-experiment literature is strong on real data but does not simulate LLM-mediated change. The OmniBehavior drift numbers were read from a summarized fetch, not checked in the PDF.

## What Exists
### Sub-theme 1: Structural and natural-experiment estimation of taste change (panel and scanner data)
- **Habit Formation in Consumer Preferences: Evidence from Panel Data** (Dynan, 2000, American Economic Review) — tests habit persistence in PSID food panel data; finds no habit formation at the annual frequency.
  - Relevance: Shows a structural test of habit that can be run on panel logs; identifies a null result that a calibration target would need to respect.
  - OpenAlex ID: W2000321490
  - Cited by: 457
- **State dependence and alternative explanations for consumer inertia** (Dubé, Hitsch, Rossi, 2010, RAND Journal of Economics) — separates loyalty (state dependence) from heterogeneity in scanner panels; rules out search and learning explanations in their setting.
  - Relevance: Gives the identification logic (long panels plus exogenous switching shocks) a simulation calibration would need to match.
  - OpenAlex ID: W3125115177
  - Cited by: 397
- **The Evolution of Brand Preferences: Evidence from Consumer Migration** (Bronnenberg, Dubé, Gentzkow, 2012, American Economic Review) — uses moves between markets to show brand preferences form from life history and persist; heterogeneity explains about 40% of geographic share variation.
  - Relevance: A natural experiment on how a change of environment shifts preferences, with long persistence; a benchmark for how much drift should occur.
  - OpenAlex ID: W2045221586
  - Cited by: 376
  - Note: An NBER working paper version (W3122163161, 2010) also exists.
- **Environmental Changes and the Dynamics of Musical Identity** (Way, Gil, Anderson, Clauset, 2019, ICWSM) — Spotify listening for over 16 million users; relocation within the US changes tastes only slightly, and tastes stay closer to the past environment.
  - Relevance: Quasi-experimental music-taste data at scale; suggests slow taste change from environment shifts.
  - OpenAlex ID: W2935758972 (ICWSM record); arXiv record W2956141610 (arXiv 1904.04948)
  - Cited by: 13 (ICWSM record)
- Aguirregabiria and Carro (search snippet only, no IDs): fixed-effects dynamic discrete choice models with state dependence can be point-identified with panels as short as T = 4.
  - Relevance: Shows short panels may still identify average effects, which matters for logs with few periods per user.

### Sub-theme 2: Learned preference dynamics and drift detection from recommender logs
- **Detecting Changes in User Preferences using Hidden Markov Models for Sequential Recommendation Tasks** (Eskandanian, Mobasher, 2018, arXiv) — hidden Markov model (HMM) finds change points in music interaction sequences, judged against all-user behavior; change points feed a sequence-aware recommender.
  - Relevance: Direct HMM drift detection on real listening logs; the closest match to the "state-space taste" idea.
  - OpenAlex ID: W2892406399
  - Cited by: 15
- **Modeling the Dynamics of User Preferences for Sequence-Aware Recommendation Using Hidden Markov Models** (Eskandanian, Mobasher, 2019, arXiv) — follow-up; the HMM change detection reportedly beats standard baselines; recommender beats sequence-aware models.
  - Relevance: Same line of work with a recommender layer; full results not checked.
  - OpenAlex ID: W2945897885
  - Cited by: 4
- **Collaborative filtering with temporal dynamics** (Koren, 2009, KDD) — adds time-varying user biases and factors (timeSVD++) to matrix factorization; reports lower error on the Netflix Prize data.
  - Relevance: Standard dynamic user embedding baseline; shows temporal terms can matter more than model complexity.
  - OpenAlex ID: W2080320419 (KDD); CACM version W2057763140
  - Cited by: 1314 (KDD); 798 (CACM)
- **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** (Carroll, Dragan, Russell, Hadfield-Menell, 2022, ICML) — trains a predictive user model on interaction logs to estimate how a recommender would shift preferences; checks it in simulated experiments.
  - Relevance: The most direct "estimate then penalize" design for preference change; validation is in simulation only.
  - OpenAlex ID: W4224979542 (arXiv 2204.11966 per the fetched page)
  - Cited by: 18
  - Note: An earlier record with the same title (W3199782056, RecSys 2021 metadata, cited by 27) appears in OpenAlex.
- **The Value of Personalized Recommendations: Evidence from Netflix** (Zielnicki, Aridor, Bibaut, Tran, Chou, Kallus, 2025, arXiv) — discrete choice model with state dependence and low-rank taste; replacing the recommender with matrix factorization cuts engagement about 4%, popularity about 12%.
  - Relevance: Structural model fitted on streaming logs with a validation check from diversion ratios; abstract does not report preference evolution over time.
  - arXiv ID: 2511.07280 (Netflix data, not Kuaishou; an earlier search summary called it Kuaishou-agnostic and was wrong to imply otherwise)
  - OpenAlex ID: not looked up
- **The Engagement-Diversity Connection: Evidence from a Field Experiment on Spotify** (Holtz, Carterette, Chandar, Nazari, Cramer, Aral, 2020, ACM Conference on Economics and Computation) — about 900,000 users in 17 countries; personalized podcast recommendations raise streaming 28.90% over popularity-based ones; individual stream diversity falls.
  - Relevance: The only randomized real-world test of recommendation-induced consumption change found; includes spillover to unexposed app sections.
  - OpenAlex ID: W3011174874
  - Cited by: 108
  - arXiv ID: 2003.08203

### Sub-theme 3: LLM and agent simulators with memory or evolving preferences
- **Towards Real-world Human Behavior Simulation: Benchmarking Large Language Models on Long-horizon, Cross-scenario, Heterogeneous Behavior Traces** (Chen, Xu, Cao, Pan, Zhang, Hu, Du, Gao, Li, Lu, Sun, Han, Sun, Wu, Lin, 2026, arXiv; NeurIPS 2026 per the page) — OmniBehavior: Kuaishou logs for 200 representative users over Sep to Nov 2025, average 8,143 actions per user.
  - Relevance: The only found dataset with real long-horizon traces and a drift comparison against LLM users.
  - Reported in the fetched HTML: real users' daily interest drift (1 minus Jaccard) is 0.6311, synthetic LoCoMo users 0.1698; LLM users show abrupt shifts. Real users' first-vs-second-half intra-user distance ratio is about 0.29, LLM users about 0.7 to 0.87.
  - Metrics: F1 for binary actions, normalized MAE for watch duration, LLM-judged text fidelity; 6,000 prediction tasks.
  - Confidence in numbers: Medium. Read via a summarizing fetch of the HTML, not the PDF.
  - OpenAlex ID: W7152999892
  - Cited by: 16
- **Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data** (Lu et al., 2026, ACL) — ShopCART dataset of 31,865 shopping sessions and 230,965 actions; prompt-only LLMs reach 11.86% next-action accuracy; fine-tuned Qwen2.5-7B reaches 17.26%.
  - Relevance: Shows prompting alone fails to reproduce real action sequences; fine-tuning on logs helps. Session-level, not longitudinal.
  - OpenAlex ID: W4415318313
  - Cited by: 53
- **Beyond Offline A/B Testing: Context-Aware Agent Simulation for Recommender System Evaluation** (Bougie, Marconi, Ye, Watanabe, 2026, EMNLP) — ContextSim agents with episodic and emotional memory and a 30-day life simulation; MovieLens-1M preference accuracy 0.824 vs 0.791 for SimUSER.
  - Relevance: Memory-equipped simulator with some temporal checks, but no comparison of individual trajectories against real users over time.
  - OpenAlex ID: W7154244789
  - Cited by: 5
- **Temporal-Aware User Behaviour Simulation with Large Language Models for Recommender Systems** (Wanyan, Hettiachchi, Ma, Xu, Chan, 2025, arXiv) — DyTA4Rec: a dynamic profile updater and temporal prompting; abstract claims better alignment with real behavior; datasets and numbers not read.
  - Relevance: Evolving-profile simulator; the closest architecture to a calibrated drift model.
  - arXiv ID: 2509.16895
- **Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation** (Wei et al., 2026, ACL per the page; arXiv 2508.18142) — simulators fine-tuned on recommender feedback; alignment claimed; no drift validation reported.
  - Relevance: Shows the static-alignment standard that current simulators use.
  - arXiv ID: 2508.18142
- **HorizonBench: Long-Horizon Personalization with Evolving Preferences** (Li, Paranjape, Oktar, Ma, Zhou, Guan, Zhang, Park, Chen, Yang, Tsvetkov, Celikyilmaz, 2026, arXiv) — 360 synthetic users with six-month conversations; ground-truth preference changes built into the generator; best of 25 models scores 52.8%.
  - Relevance: Benchmark with known drift causes, but synthetic. Models keep the stale stated preference over a third of the time when wrong.
  - arXiv ID: 2604.17283
- **Measuring the Behavioral Fidelity of Long-Horizon Human Activity Simulations** (Cheng, Yang, Bas, Niinuma, Abe, Lindlbauer, 2026, EMNLP) — 43 hours of multi-camera office activity; statistical transition and time-of-day priors match real distributions best, but over-fragment routines.
  - Relevance: Long-horizon fidelity metrics for real traces; physical activity, not preferences.
  - OpenAlex ID: W7206211526
  - Cited by: 0
- **KuaiSim: A Comprehensive Simulator for Recommender Systems** (Zhao, Liu, Cai, Zhao, Liu, Zheng, Jiang, Gai, 2023, NeurIPS) — Kuaishou user simulator with response models pretrained on logs; cross-session retention task; no drift validation in the abstract.
  - Relevance: Kuaishou-based simulator; uses KuaiRand logs; calibration details not read.
  - OpenAlex ID: W7133187022
  - Cited by: 32
- **On Generative Agents in Recommendation** (authors not verified, 2024, SIGIR) — Agent4Rec, LLM agents with profiles, memories and actions on MovieLens-1M.
  - Relevance: The standard memory-agent recommender simulator; evaluated on static ratings.
  - OpenAlex ID: W4400525295
  - Cited by: 235
- **Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations** (Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant, 2026, ACL) — user study versus simulated users on tau-Bench retail tasks; simulators miscalibrate agent scores.
  - Relevance: Direct validation against human users, but single-task, not longitudinal.
  - OpenAlex ID: W7166876594
  - Cited by: 42
- **The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study** (Lin, Yun, Matarić, Canny, Gretton, D'Amour, 2026, arXiv) — persona-based simulated users drift under interventions, which biases treatment effects; proposes negative-control drift checks.
  - Relevance: Names the exact confound a simulation of LLM influence would face.
  - OpenAlex ID: W7162025110
  - Cited by: 7
- **Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation** (authors not verified, 2026, arXiv) — changing one persona attribute shifts unrelated attributes across eight LLMs.
  - Relevance: Shows personas cannot set one preference dimension alone; a calibration must check off-target drift.
  - OpenAlex ID: W7214764785
  - Cited by: 0
- **The Threat of Analytic Flexibility in Using Large Language Models to Simulate Human Data** (single author, 2026, venue not confirmed) — 252 silicon-sample configurations; fit to human data varies widely with choices of model and prompt.
  - Relevance: Shows validation results depend on analyst choices; a calibration must pre-register them.
  - OpenAlex ID: W4417080482
  - Cited by: 43

## Reference Chain Discoveries
- Found via: OmniBehavior citers (OpenAlex) — "Measuring the Behavioral Fidelity of Long-Horizon Human Activity Simulations", "LUNAR" (arXiv 2608.05246, app-log personalization benchmark; more context did not reliably help), "Towards Faithful Simulation of Human Shopping Behavior" (title not found; closest is Lu et al.).
- Found via: Carroll 2022 citers — "Preference Dynamics Under Personalized Recommendations" (2022, EC; covered in the earlier round, not re-read), "User Tampering in Reinforcement Learning Recommender Systems" (2023; covered in the earlier round).
- Found via: Koren 2009 citers — matrix factorization and factorization machine papers only; no drift-specific finding.
- Found via: Holtz 2020 citers — "Cultural Divergence in popular music" (2021, Humanities and Social Sciences Communications; cross-country diversity on Spotify, 84 citations); not read.
- Found via: Dubé et al. 2010 citers — "Power to Choose? An Analysis of Consumer Inertia in the Residential Electricity Market" (2017, 260 citations); not read.
- Found via: Search on critiques — "Limitations of Current LLM-based User Simulators in Conversational Recommendation" (Zhu et al., arXiv 2403.16416; audit finds target-item leakage in iEvaLM).
- Found via: Search on profile drift — DGDPO (arXiv 2508.12645; diagnose-and-treat profile refinement); search snippet only.
- Found via: Search on structural habit models — Aguirregabiria and Carro (dynamic discrete choice with short panels); search snippet only; Gordon and Sun (addictive stockpiling model on cigarette panels); search snippet only.
- Found via: Search on simulators with memory — AgenticLOCI (30-day synthetic longitudinal memory); search snippet only.
- Found via: Search on KuaiSim-type simulators — KuaiLive (live-streaming dataset, 21 days; search snippet only), KuaiRec and KuaiRand (short Kuaishou logs; referenced in snippets, not read).

## What's Missing (Gaps)
- No simulator found validates an individual user's preference path over months against that user's real logs. This is the core gap for calibrating LLM-driven change.
- Structural models (Dubé, Bronnenberg, Dynan) estimate taste change from real panels but are not used to drive or check LLM simulators.
- Drift has no shared definition. OmniBehavior uses daily 1 minus Jaccard; HorizonBench uses belief-update accuracy; Carroll 2022 uses a trust region. A calibration needs one agreed metric.
- Kuaishou open datasets span weeks (KuaiRec, KuaiRand, KuaiLive); only OmniBehavior spans three months. Multi-year panels are rare outside Spotify.
- No longitudinal dataset records exposure to LLM chat assistants alongside taste changes. Holtz-style randomized exposure exists for recommenders, not for LLM answers.
- No paper combines a state-space or HMM taste model with an LLM simulator and tests it on held-out real users.

## Contradictions or Tensions
- **Stable versus fast taste change.** Bronnenberg 2012 and Way 2019 find preferences persist for years and change slowly. OmniBehavior reports real daily drift of 0.63 by 1 minus Jaccard. Metrics differ, so the two numbers are not directly comparable.
- **Recommenders narrow taste or not.** Holtz 2020 finds personalization lowers individual diversity by 11.51 points but raises aggregate diversity. Zielnicki 2025 finds matrix-factorization and popularity recommenders reduce diversity. Carroll 2022 argues recommenders induce preference shifts by design; the empirical papers do not directly measure shifts in stated preferences.
- **Simulator alignment.** ContextSim (Bougie 2026) reports 0.824 accuracy on MovieLens-1M. OmniBehavior and Lu 2026 report poor next-action accuracy (11.86% prompt-only) on real logs. The tasks differ: one-rating accuracy versus next-action prediction.
- **Drift as a bias.** DyTA4Rec and Mirroring Users claim better alignment with real users, but do not test drift. Lin 2026 and Seshadri 2026 show that persona-driven drift biases results.

## Confidence
Medium
- Confidence that no simulator is validated over months against real users: High (eight search queries, citation traversal of top papers, abstract reads of 12 simulator papers).
- What would raise confidence: A full read of OmniBehavior's related work and drift section, plus the PDF of the Holtz 2020 paper, to check numbers.
- What would lower confidence: A 2026 paper that validates an LLM simulator against individual longitudinal logs and was not in the index used here. The search index may lag preprints from mid-2026.

## Search Log
### Round 1: Broad search
- Queries: (1) structural estimation taste evolution recommender longitudinal; (2) LLM agent user simulator evolving preferences memory validation; (3) preference drift detection recommender logs dynamic embeddings HMM; (4) Kuaishou interest drift dataset simulator calibration; (5) Spotify taste change natural experiment; (6) Dubé Hitsch Rossi state dependence scanner data; (7) LLM simulated users preference drift validation longitudinal; (8) OmniBehavior benchmark arXiv 2604.08362.
- Papers found: about 45 (all results, including duplicates); about 22 relevant.
- Key leads: OmniBehavior (2604.08362), Eskandanian & Mobasher HMM (1810.00272), Carroll 2022 (2204.11966), Dubé et al. 2010 (RAND), Way 2019 (1904.04948), Holtz 2020 (2003.08203).

### Round 2: Citation traversal
- Papers traversed: OmniBehavior (references: 21 resolved IDs listed; citers: 10 pulled); Eskandanian HMM 2018 (citers: 10); Dubé et al. 2010 (citers: 10); Carroll 2022 (citers: 8); Koren 2009 (citers: 8); Holtz 2020 (citers: 8); Lu 2026 (citers: 8).
- New papers from references: OmniBehavior references were not resolved to titles; not read.
- New papers from citers: LUNAR; Measuring Behavioral Fidelity; Illusion of Intervention; Persona Following; Lost in Simulation; Analytic Flexibility; Bronnenberg 2012 (via search); Dynan 2000 (via search); ContextSim (via search).

### Round 3: Reference section mining
- Papers mined: OmniBehavior (fetched arXiv HTML, dataset and drift sections read; related-work section not separately mined). Holtz 2020 and Carroll 2022 Related Work not read.
- Limitation: Related Work sections of the two most relevant papers were not mined, so this round is partial.
- New papers: none beyond round 2.

### Round 4: Gap-filling
- Gaps targeted: Structural habit identification; Koren-type dynamic embeddings; Kuaishou simulator calibration; memory-agent simulator longitudinal validation.
- Queries: (1) dynamic structural model habit formation identification panel taste evolution; (2) KuaiSim calibration against Kuaishou logs; (3) LLM agent evolving preferences memory MovieLens calibration 2026 (extended search); (4) Koren timeSVD temporal dynamics.
- New findings: Aguirregabiria & Carro; Gordon & Sun; KuaiSim abstract details (no calibration described); ContextSim; AgenticLOCI.

### Round 5: Adversarial check
- Gaps targeted: critiques of LLM simulators; failed validity claims.
- Queries: (1) LLM-simulated users not representative critique recommender evaluation; (2) Lu 2026 accuracy and fine-tuning check.
- New findings: Zhu et al. 2024 (iEvaLM leakage); Seshadri 2026 (miscalibrated against humans); Persona Following (cross-attribute influence); Analytic Flexibility (configuration sensitivity); Illusion of Intervention (drift confound).

### Round 6+: Not run
- Stopped after round 5 because the adversarial round was complete and each sub-question had an answer. Round 5 still returned new papers, so the search is not fully converged.

### Convergence note
- Total unique relevant papers found: about 27 (about 20 read through abstracts or fuller fetches; about 7 from search snippets only).
- New papers in last round: about 5 (adversarial round).
- Stopped because: round 5 completed and all sub-questions had answers. Convergence was not reached by the "last 2 rounds found zero new" rule, so coverage is best-effort.
