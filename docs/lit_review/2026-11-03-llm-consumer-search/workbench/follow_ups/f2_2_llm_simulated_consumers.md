# How are LLMs used as research tools to model or simulate consumer search and choice: LLM-simulated consumers ('silicon samples') for market research and willingness-to-pay estimation, LLM agents as synthetic shoppers to test search interfaces or ranking, and LLM-based structural or behavioral models of search? How well do simulated consumers match real consumer search and choice data, and where do they fail?

## TL;DR
Answer: Four uses are in the literature. (1) "Silicon samples": LLMs given demographic or persona backstories answer surveys and willingness-to-pay (WTP) questions. (2) Simulated shoppers and search users that click, query and choose, used for benchmarks and interface tests. (3) Digital twins of individual customers, used to pre-test A/B experiments. (4) Early work on structural or choice-model estimation with LLM respondents. Aggregate fit is the best-supported result. The best case is purchase-intent distributions in personal-care surveys (about 90% of human test-retest reliability in one 57-survey study). Individual-level fit is weak, subgroup differences are flattened, and variance is compressed. Search and shopper simulators match query wording and some click patterns, but they lag on exploratory tasks and long trajectories.
Strength: Medium for aggregate survey and purchase-intent fit. Low for individual-level fit, WTP magnitudes, subgroup inference, and search or ranking evaluation.
Most of the strong numbers come from preprints and single-team papers, and many came from abstracts or search summaries rather than full text (see Search Log). Results depend on the model, the persona construction, the elicitation format (free text vs. direct score), and the domain. Independent replications are few.

## What Exists
### Sub-theme 1: Silicon samples for survey and purchase-intent research (foundations and critiques)
- **Out of One, Many: Using Language Models to Simulate Human Samples** (Argyle et al., 2023, Political Analysis) — Conditioned GPT-3 on sociodemographic backstories from real U.S. survey respondents; output distributions matched many human subgroups, which the authors call "algorithmic fidelity."
  - Relevance: Founding paper for the silicon-sample idea; the fidelity claim is the baseline that later work tests and often narrows.
  - OpenAlex ID: W4321455981
  - Cited by: 793
- **Using GPT for Market Research** (Brand et al., 2024, ACM Conference on Economics and Computation (EC '24); HBS Working Paper 23-062, 2023) — GPT-3.5 answering as a shopper gave WTP estimates of realistic magnitude that follow economic-theory patterns, via direct questions and conjoint-style attribute estimates; GPT conjoint ran 10,800 configurations for about $3.
  - Relevance: Direct WTP application; the conjoint set-up is the closest match to the question's willingness-to-pay part.
  - OpenAlex ID: W4405464828
  - Cited by: 11
- **Using LLMs for Market Research** (Brand et al., 2025, Microsoft working paper; title as given in search summary, not retrieved from source) — Same team; GPT-3.5 Turbo on conjoint studies of household products and computers. Reports replication of existing feature effects and WTP predictions for new features after demographic fine-tuning.
  - Relevance: Follow-up that tests whether the 2024 result extends with fine-tuning.
  - OpenAlex ID: not retrieved
- **LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings** (Maier et al., 2025, arXiv 2510.08338) — Tested semantic similarity rating (SSR), where the LLM writes a free-text answer that is mapped to a 5-point Likert scale by embedding similarity. Against 57 personal-care product surveys with 9,300 human responses, SSR reached about 90% of human test-retest reliability, and distributions had KS similarity above 0.85 (the paper's own figure; the Kolmogorov–Smirnov baseline for direct rating is reported as 0.26 in one secondary source).
  - Relevance: Strongest large-scale positive result for purchase-intent distributions. Single research group (PyMC Labs with a consumer-goods firm), so independence is limited.
  - OpenAlex ID: W4416384452
  - Cited by: 2
- **Correcting Mode Collapse in Silicon Sampling with Semantic Similarity Rating** (authors not retrieved, 2026, arXiv 2607.28550) — Title and arXiv ID from OpenAlex only. The search tool could not retrieve the paper, so the content is unverified; the title suggests a follow-up that targets the variance-compression failure of SSR-style methods.
  - Relevance: Possible fix for the variance-compression problem in silicon samples.
  - OpenAlex ID: W7171990420
  - Cited by: 0
- **Can LLMs Serve as Synthetic Respondents for Consumer Demand Estimation?** (authors not verified, 2026, NeurIPS 2026) — Discrete choice experiment with 18,144 observations. Demographics alone did not recover economically meaningful preferences; the best prompting strategy reversed the human ranking of attribute importance. The authors warn that LLM choice data can give misleading signals for business decisions even when prediction error looks acceptable.
  - Relevance: The most direct test of LLM respondents for WTP and demand estimation, and it is negative.
  - OpenAlex ID: not retrieved (conference page: neurips.cc/virtual/2026/169654)
  - Cited by: not retrieved
- **Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices** (Reusens, Goethals, Calders and Martens, 2026, Expert Systems with Applications; arXiv 2602.09802) — Ran multinomial logit on LLM travel-assistant choices to get implied WTP. Larger models gave meaningful WTP values, but attribute-level values deviated systematically from human benchmarks, and the derived values ran higher than the human reference. Persona prompts and information about past choices shift the results.
  - Relevance: Shows the structural-estimation (choice model) route to LLM WTP, and that the result depends on prompting.
  - OpenAlex ID: W7164556437 (journal listing per OpenAlex)
  - Cited by: 0
- **Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?** (Horton, Filippas and Manning, 2023, NBER Working Paper w31122) — Replicates classic behavioral-economics experiments with LLM agents. Qualitative results often match, with some differences. Each simulated agent is described as a flawed model that often gives unreasonable answers, and results need empirical confirmation.
  - Relevance: Economics framing for LLMs as simulated humans. Found via citation traversal of Argyle et al.
  - OpenAlex ID: W4363624465
  - Cited by: 329
- **Can AI language models replace human participants?** (Dillion, Tandon, Gu and Gray, 2023, Trends in Cognitive Sciences) — Position piece on when LLM "participants" can stand in for humans. Argues that cases where they can are narrow and need validation.
  - Relevance: Standard reference for the "replace humans?" debate. Found via citation traversal.
  - OpenAlex ID: W4376117416
  - Cited by: 408
- **Synthetic Replacements for Human Survey Data? The Perils of Large Language Models** (Bisbee et al., 2024, Political Analysis) — LLM-generated average opinions can look like population averages from the ANES, but regression coefficients linking respondent traits to opinions often differ from real survey estimates and sometimes flip sign. The authors judge the synthetic data unreliable for statistical inference.
  - Relevance: Key negative result for subgroup and regression-level inference. Found via two-hop traversal from Dillion et al.
  - Attribution caveat: a search summary described these exact findings as "Boelaert et al. (2024)". The title and content match this paper, but the author attribution is unconfirmed. Verify before citing.
  - OpenAlex ID: W4397011890
  - Cited by: 213
- **The threat of analytic flexibility in using large language models to simulate human data** (authors not verified, 2025, arXiv 2509.13397) — Argues that a small number of analytic choices (prompt, model, sample construction, scoring) can change how well silicon samples match human data. Seen only as a search summary.
  - Relevance: Method critique: results depend on researcher choices, so pre-registration of the set-up is needed.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Which Humans?** (Atari, Xue, Park and Blasi, 2023, preprint; venue not retrieved) — Argues that LLM "human" samples reflect a narrow population (WEIRD-like) and need to be checked against the population of interest.
  - Relevance: Population mismatch as a source of error. Found via two-hop traversal from Homo Silicus.
  - OpenAlex ID: W4386981810
  - Cited by: 151
- **Using large language models to generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines** (Sarstedt, Adler, Rau and Schmitt, 2024, Psychology and Marketing) — Review that places silicon samples in consumer and marketing research. Lists challenges (bias, validity, reporting) and gives guidelines for benchmarking against human data.
  - Relevance: Consumer-research framing and guidelines. Found via two-hop traversal from Dillion et al.
  - OpenAlex ID: W4391713857
  - Cited by: 149
- **Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information** (authors not verified, 2024, arXiv 2402.18144) — Group-level demographic information is used to simulate sub-population opinion distributions. Seen only as a search result.
  - Relevance: Early sub-population approach, which the later subgroup-flattening results test.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Simulating Survey Respondents with Large Language Models through Impulse Variables and Persona Conditioning** (authors not verified, 2023, SSRN 4595896) — Uses impulse variables and persona conditioning to simulate survey responses. Seen only as a metadata record.
  - Relevance: Working paper on persona construction for survey simulation.
  - OpenAlex ID: W4388430701
  - Cited by: 3
- **Tastes without distinction: silicon samples and the synthetic construction of tastes** (Ma et al., 2026, arXiv 2606.30085; first author as given in a secondary summary) — Tests LLM "silicon surrogates" against a cultural-participation survey and a single model family set. Reports systematic positive bias in liking, and loss of the relational structure of real taste patterns. One dataset and three model families.
  - Relevance: Shows distortion of structure in preference data, not just of averages.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Evaluating Silicon Sampling: LLM Accuracy in Simulating Public Opinion on Facial Recognition Technology** (Ma, 2025, AHFE International Conference proceedings) — Demographic-only personas gave poor individual-level accuracy (MAE 0.90–1.73, QWK near zero). Adding context about experiences and perceptions improved results markedly.
  - Relevance: Clear evidence that persona content matters beyond demographics.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Leaving Insight to Digital Twins? Promise, Progress and Limits of Synthetic Respondents** (authors not verified, year not verified, NIM Marketing Intelligence Review) — Practitioner review. Synthetic data overestimated positive attitudes and showed less variation across respondents than human data. Synthetic responses predicted individual answers better than chance and captured broad trends. Matched real choices about 79% of the time in one summary.
  - Relevance: Independent-ish evidence of positivity bias and variance compression; the 79% figure is from a secondary summary.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels** (Tigre and Souto, 2026, arXiv 2609.13148) — Splits synthetic-panel bias into covariate shift and concept shift. Aggregate validation can hide variance compression, sign-flipped coefficients, and subgroup errors of 10 to 30 points. Point correction works under missing-at-random nonresponse and fails under nonignorable nonresponse. Evaluated on ANES and Twin-2K-500 data.
  - Relevance: Gives a decision framework (trust, correct, or abandon) and shows that correction needs a complete invitation frame and a human calibration sample.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses** (Chen, Zhu and Zheng, 2026, arXiv 2607.26348) — Four models on General Social Survey (U.S.) and World Values Survey (cross-cultural) data. No LLM beats the strongest non-LLM baseline at the individual level; the cross-cultural gap is 11 to 22 points. On a segment-targeting task, models inflate between-segment gaps two to fourfold.
  - Relevance: Strongest recent evidence that individual-level fidelity fails, and that decisions made from segment gaps can point to the wrong segment.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Distributional Validity and Calibration of a Korean Synthetic Persona Panel for Digital and AI Service Use: A Secondary-Data Validation Against the Korea Media Panel Survey** (authors not verified, 2026, arXiv 2608.28615) — Validates a synthetic persona panel against a real national media panel. Seen only as a search result, so the findings are unverified.
  - Relevance: A second-country test of distributional validity.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Decoding Consumer Preferences Using Attention-Based Language Models** (authors not verified, 2025, arXiv 2507.17564) — Uses attention-based language models on consumer data to recover preferences. Seen only as a search result.
  - Relevance: Preference recovery from text, not from LLM-simulated respondents. Included because it is a structural-preference route.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **LLM Consumer Behavior Theory: Foundations of a Novel Research Field** (authors not verified, 2026, arXiv 2606.18005) — Frames consumers as preference structures that LLM agents imperfectly reflect; agent choices aggregate into market demand. Uses multinomial or mixed logit as the approximating utility model. Conceptual, not empirical.
  - Relevance: Theory link between LLM agent choice and structural demand.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe** (authors not verified, 2026, arXiv 2607.25292) — Argues each per-call output from an instruction-tuned model is a degenerate draw, which causes silicon-sample variance loss. Proposes asking for the response distribution in one call, which the authors report more than halves error against human survey data compared with persona aggregation.
  - Relevance: Mechanism for variance compression, with a proposed fix.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity** (Zhang et al., 2025, arXiv 2510.01171; ICML 2026 per search summary) — Attributes mode collapse to typicality bias in preference data. Proposes asking the model to verbalize a distribution of answers with probabilities.
  - Relevance: General method for the variance-compression problem, not tested here on consumer data.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Maintaining Stable Personas? Examining Temporal Stability in LLM-Based Human Simulation** (authors not retrieved, 2026, ACM, DOI 10.1145/3772363.3799334) — Tests whether LLM personas keep consistent answers over time. Seen as an OpenAlex record that cites the SSR paper.
  - Relevance: Test-retest stability of personas, which bounds how much any single persona can be trusted.
  - OpenAlex ID: W7153879242
  - Cited by: 4
- **Can Finetuning LLMs on Small Human Samples Increase Heterogeneity, Alignment, and Belief-Action Coherence?** (Wang et al., 2025, arXiv 2511.21218; first author from search summary) — Fine-tuning on about 30 human observations improved distributional alignment and heterogeneity. Even the best fine-tuned models did not reproduce the regression coefficients of the original behavioral study.
  - Relevance: Finetuning helps distributions but not regression-level inference. Direct test of the subgroup question.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **ChatGPT is not A Man but Das Man: Representativeness and Structural Consistency of Silicon Samples Generated by Large Language Models** (authors not verified, 2025, arXiv 2507.02919) — Tests whether silicon samples are representative of populations and internally consistent across questions. Seen only as a search result.
  - Relevance: Structural consistency across items, a separate failure mode from individual fit.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved

### Sub-theme 2: Digital twins and synthetic panels for A/B testing and pricing
- **Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions** (authors not retrieved in this session; Columbia DAP Lab team, 2025, Marketing Science 44(6)) — Representative U.S. sample (N = 2,058) with more than 500 questions in four waves, and public data. A follow-up mega-study of 19 preregistered studies reported about 75% average individual-level accuracy, but twins were less variable than humans in 93.9% of cases, and a "blue-shift" appeared with richer persona descriptions. The mega-study figures come from a secondary summary.
  - Relevance: Main public benchmark for twin fidelity; used by the Tigre and Souto and Chen et al. papers.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Data-Driven Persona-Conditioned Agents for A/B Test Simulation** (authors not verified, 2026, arXiv 2609.01038) — Builds persona agents from real user behavior to predict A/B results. On a benchmark of 40 A/B tests, directional accuracy was 0.75 to 0.90 depending on metric. Tests were on visual stimuli (ad designs and layouts) judged on click-through rate.
  - Relevance: Closest to the question's "test interfaces" use, but the 40-test benchmark is small and the tasks are visual, not search or ranking.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Flexible but Fragile: Budgeted Human–Digital-Twin Allocation for A/B Tests** (authors not verified, 2026, NeurIPS 2026) — Proposes splitting a fixed budget between human and digital-twin outcomes. The constrained policy beat the joint policy on holdout MSE in 51 of 60 configurations. Evaluated on WTP data.
  - Relevance: Practical design rule for using twins with a human budget.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved

### Sub-theme 3: LLM user simulators for search and ranking evaluation
- **USimAgent: Large Language Models for Simulating Search Users** (authors not verified, 2025, SIGIR) — LLM simulator that models querying, clicking and stopping over three-step rounds. Compared with query-reformulation methods and click models.
  - Relevance: Direct match for simulated search users; the question is whether it tracks real logs.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **BASES: Large-scale Web Search User Simulation with Large Language Model based Agents** (authors not verified, 2024, arXiv 2402.17505) — Reports 90.8% term overlap between LLM and human queries, and 51% top-1 click agreement with human clicks. The authors attribute part of the click mismatch to homogenized results and individual human bias.
  - Relevance: Quantitative fit to real query and click data, one of the few.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Sim4IA-Bench** (authors not verified, 2025, SIGIR Sim4IA micro-shared task) — Benchmark linking real search sessions with simulated next-query predictions; 70 sessions, with up to 62 simulator runs for each.
  - Relevance: Public resource for validating query-level simulators. Small.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Evaluating the Efficacy of Simulated User Models in Interactive Information Retrieval: A User-Based Approach** (authors not verified, 2025, Sindh University Research Journal) — Compared 32 real and 32 matched simulated sessions on the iSearch data. Simulated users approximated real performance on factual tasks but underperformed on exploratory and comparative tasks, especially in reformulation frequency and satisfaction.
  - Relevance: Shows the task boundary for search-user simulation. Small sample; journal venue is not a major IR venue.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Context-driven interactive query simulations** (authors not verified, 2023, arXiv 2312.09631) — Argues that user models ignore context and simulates context-driven reformulation, weighting the effort to gather information as well as information gain.
  - Relevance: Modeling the effort side of search, which most simulators omit.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Generative Agents: Interactive Simulacra of Human Behavior** (Park, O'Brien, Cai, Morris, Liang and Bernstein, 2023, UIST) — Persona-driven agents with memory and reflection in a simulated town. Foundational for LLM agents as human stand-ins, though not a consumer or search study.
  - Relevance: Foundational reference for agent-based simulation of human behavior. Found via two-hop traversal from Homo Silicus.
  - OpenAlex ID: W4387835442
  - Cited by: 2205

### Sub-theme 4: Synthetic shoppers and agents in shopping environments
- **PAARS** (authors not verified, 2025, arXiv 2503.24228; full title not retrieved) — Builds LLM shopper agents from personas induced from anonymised shopping sessions, with retail tools for search, view and purchase. Adds a behavioral alignment suite. Argues that survey and A/B tools need group-level similarity, not individual mimicry.
  - Relevance: Shopper simulator aimed at group-level similarity, which matches how the question frames fit.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-based Shopping Assistants?** (authors not verified, 2025, arXiv 2509.21501) — Two-stage pipeline comparing real customers with LLM counterparts on decisions, interaction behavior and evaluation results. Closest match to using synthetic shoppers to evaluate a shopping assistant.
  - Relevance: Direct test of a simulated-customer evaluation design.
  - OpenAlex ID: not retrieved
  - Cited by: not retrieved
- **Utilizing large language models to simulate parking search** (Fulman, Memduhoğlu and Zipf, 2025, Transportation Research Part A: Policy and Practice, 199) — GPT-4o mini acting as survey respondent in persona-based parking choices. Static choices favored cheaper and shorter options. Dynamic sequential choices under cruising-time uncertainty showed myopia and risk attitudes similar to human experiments. Order effects favored the first option shown. Authors frame LLMs as a pilot-testing complement, not a replacement.
  - Relevance: The closest published work to "simulated consumers for search" with a choice model. Transportation domain, not e-commerce. Abstract and summaries only.
  - OpenAlex ID: not retrieved (DOI 10.1016/j.tra.2025.104542)
  - Cited by: not retrieved

## Reference Chain Discoveries
- Found via: Argyle et al. (OpenAlex citers, top 12 by citation count). Yielded Horton et al. (Homo Silicus) and Dillion et al. (Can AI language models replace human participants?), both direct citers of Argyle et al.
- Found via: Dillion et al. two-hop (top 8 citers by citation count). Yielded Bisbee et al. (Synthetic Replacements), Which Humans? (Atari et al.), and Sarstedt et al. (2024).
- Found via: Horton et al. two-hop (top 8 citers by citation count). Yielded Generative Agents (Park et al.) and Dillion et al.
- Found via: Argyle et al. references (37 references, resolved; top 15 by citation count reviewed). These are foundational NLP and political-science references (e.g., GPT-3, T5, Stochastic Parrots). No new relevant item was found in the list, so no items are credited to it.
- Found via: Brand et al. citers (11 citers). Mostly unrelated applied papers. None kept.
- Found via: Maier et al. citers (2 citers). Yielded "Maintaining Stable Personas?" (2026).

## What's Missing (Gaps)
- No peer-reviewed study compares LLM-simulated WTP or purchase intent with real purchases or field A/B results in an e-commerce setting. The Maier et al. data are stated-intent surveys.
- No validated simulator of ranking effects on real click logs. BASES is the closest, and it reports 51% top-1 click agreement, which is not enough to validate a ranking experiment.
- No LLM-based structural estimation (for example, a Weitzman-style search model with LLM respondents) has been tested against real search data. The Reusens et al. paper estimates a multinomial logit on LLM choices, not a search model.
- Subgroup-level validity is tested in only a few papers (Bisbee et al., Wang et al., Chen et al.). No study tests whether subgroup-targeted interface decisions made from synthetic panels change when run on humans.
- Few studies cover non-U.S., non-English consumers, though Korean and cross-cultural work is starting.
- Several items reviewed here are only abstracts or search summaries. The full text of the NeurIPS 2026 demand paper, the Chen et al. benchmark, and the Tigre and Souto paper was not read.

## Contradictions or Tensions
- Positive fit vs. flattening. Maier et al. report realistic distributions (KS above 0.85) and reliability near 90% of human test-retest. A 2026 independent check (secondary summary, arXiv 2602.13862) and the NIM review both find variance compression and overestimation of positive attitudes. The difference may come from elicitation method (SSR free text vs. direct score) and from the Likert item set, but this has not been tested directly.
- Positivity bias direction. The NIM review says synthetic data overestimate positive attitudes. Maier et al. state that synthetic consumers show less positivity bias than human panels and wider spreads. These are different domains and measures.
- WTP magnitudes. Brand et al. (2024) report realistic WTP magnitudes. Reusens et al. (2026) find attribute-level WTP deviating systematically and running higher than human benchmarks. The NeurIPS 2026 paper finds that demographics alone fail, and that the best prompt reverses the human ranking of attributes. These are compatible only for aggregate magnitude, not for attribute ranking.
- Single-group vs. independent work. Most positive results come from one team (Maier et al.; Brand et al.), while critiques (Bisbee et al.; Chen et al.; Tigre and Souto) come from separate groups. The two sides also use different metrics, so a direct comparison is not possible.
- Search simulators. BASES reports 90.8% term overlap and 51% top-1 click agreement, which reads as good for queries and modest for clicks. The SURJ comparison finds close match on factual tasks and clear underperformance on exploratory ones. Both can be right, because they test different tasks.

## Confidence
Medium for the claim that LLM silicon samples reproduce aggregate survey and purchase-intent patterns in some domains. Low for individual-level fit, WTP magnitudes, subgroup inference, and search or ranking evaluation.
- What would raise confidence: an independent replication of the Maier et al. SSR result on a different product category and firm, with a pre-registered benchmark against real purchase or A/B data. For search, a validation of a LLM searcher against real click logs on a ranking change would count. For structural estimation, a result where LLM-respondent estimates match a structural model fit on real data.
- What would lower confidence: a replication where the free-text SSR advantage disappears when the same Likert items are asked directly, or a demonstration that the variance-compression or subgroup-flattening results hold across the newest model versions and prompts. The Tigre and Souto and Chen et al. papers, if confirmed in full text, would lower confidence in the individual-level claims.
- Note on sources: about half the specific numbers in this file come from abstracts or search summaries, not full texts. Items marked "not verified" lack author or venue confirmation.

## Search Log
### Round 1: Broad search
- Queries: "LLM silicon samples survey simulation consumer willingness to pay"; "LLM simulated consumers replicate survey responses market research silicon sampling"; "LLM agents synthetic shoppers test search interface ranking simulation arXiv 2025"; "large language models structural model discrete choice demand estimation consumer preferences"; "LLM user simulator consumer choice ranking evaluation click model simulated users e-commerce search 2025 2026"; follow-up title and author searches for Argyle et al., Maier et al. (SSR), Brand et al. (GPT market research), and an e-commerce ranking/click-model query.
- Papers found: about 25 distinct candidates in round 1 (including repeats across queries). About 20 of them were new to the workbench.
- Key leads: Argyle et al. 2023; Maier et al. 2025 (SSR); Brand, Israeli and Ngwe (GPT market research); the NeurIPS 2026 synthetic-respondent demand paper; Reusens et al. 2026 (WTP from subjective choices).

### Round 2: Citation traversal
- Papers traversed: Argyle et al. (W4321455981; 793 citations; top 12 citers and all 37 references resolved, top 15 by citations reviewed). Maier et al. (W4416384452; 2 citers). Brand et al. (W4405464828; 11 citers). Two-hop from Dillion et al. (W4376117416; 408 citations; top 8 citers) and Horton et al. (W4363624465; 329 citations; top 8 citers). Two-hop was not run on Argyle's other high-citation citers.
- New papers from references: none credited. Argyle's references are foundational NLP and political-science papers.
- New papers from citers: Bisbee et al. 2024 (Synthetic Replacements); Atari et al. (Which Humans?); Sarstedt et al. 2024; Park et al. 2023 (Generative Agents); Maintaining Stable Personas? (2026); Using LLMs for Market Research (Brand et al., 2025, found by title search, cross-checked against Brand et al. citers).

### Round 3: Reference section mining
- Papers traversed: Tigre and Souto (arXiv 2609.13148) and Maier et al. (arXiv 2510.08338), abstract pages only. The full related-work sections were not retrievable through the tool.
- Related-work commentary: not obtained. Authors' stated positioning comes from the abstracts only.
- New findings: none beyond the abstracts already recorded. Round 3 is incomplete for this reason.

### Round 4: Gap-filling
- Gaps targeted: (a) search-user simulation for interfaces; (b) LLM digital twins for A/B testing; (c) Twin-2K-500 and digital-twin benchmarks; (d) LLM structural search models; (e) subgroup validity of synthetic panels.
- Queries: "LLM simulated users search session query reformulation click behavior simulation information retrieval evaluation 2025"; "LLM digital twin customers A/B test prediction online experiment simulated users e-commerce"; "Twin-2K-500 dataset LLM digital twins 2,000 participants survey mega-study"; "LLM structural model of search costs consumer search theory estimation simulated consumers Weitzman"; "LLM simulated respondents fail to reproduce heterogeneity subgroup human choice data critique limitations"; "Chen Zhu Zheng When Synthetic Users Fail".
- New findings: about 11 new candidates (search simulators, A/B twins, Twin-2K, subgroup critiques). No LLM-based Weitzman-type structural search model was found; the structural search literature found (non-LLM) was not counted.

### Round 5: Adversarial check
- Gaps targeted: critiques and failed replications of silicon samples.
- Queries: "LLM persona simulated consumers overestimate purchase intent variance compression critique 2026"; "silicon sampling OR synthetic respondents failure mode critique marketing research 2025 2026 limitations"; "LLM survey simulation replication failed negative result silicon sample does not replicate experiment 2026"; "Correcting Mode Collapse in Silicon Sampling ...".
- New findings: about 3 new items (Das Man, Korean panel, Instruction-Tuned LMs) plus the variance-compression critiques. No clean failed replication of a specific survey was found.

### Round 6+: Not run
- Stopped after Round 5 because the sub-questions had answers (search-user, WTP, A/B and subgroup) and the stopping rule for Round 5 was met. Rounds 4 and 5 still produced new candidates, so the coverage is not converged. The remaining gaps are noted in "What's Missing."

### Convergence note
- Total unique relevant papers found: about 40 (new to this workbench) plus the overlap with existing workbench items (not counted here).
- New papers in last round: about 3 (Round 5).
- Stopped because: completed Round 5 and sub-questions have answers, and no further gap-filling round was scheduled. The result is not converged, because Round 5 still yielded new items.
