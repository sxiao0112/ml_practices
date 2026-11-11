# What formal (economic, Bayesian, game-theoretic, cognitive) models describe a user who is uncertain about their OWN preferences and learns them over repeated interactions with an advisor, recommender or AI system — including repeated cheap talk or biased advisors, strategic users of recommenders (e.g. Haupt, Podimata), the behavior-vs-utility inversion problem (Kleinberg, Mullainathan, Raghavan), reliance and deskilling models where AI help reduces the user's own learning, LLM-based preference elicitation that may shape what it elicits, and variety-seeking/satiation models in marketing? List each model's primitives (state, update rule, advisor objective) and its long-run prediction, so a researcher can build a new model of preference learning under LLM influence.

## TL;DR
Answer: Five model families touch this question. (1) Strategic-user and behavior-vs-utility models (Haupt et al. 2023; Kleinberg et al. 2022/2024) treat the platform as learning from biased or strategic signals. (2) Bayesian self-learning models (Rafieian and Zuo, working paper) let the user learn tastes through recommendations and show reduced self-learning. (3) Advisor-learning models (Gramb and Schottmüller; repeated cheap-talk papers) let the advisor learn the user. (4) Deskilling models (Park et al. 2026; Caosun and Aral 2026) let practice skill decay with AI reliance. (5) Elicitation and satiation work (Mahajan et al. 2026; McAlister 1982; Terui) covers how the question format and satiation shape stated preferences. No single paper combines a user who learns her own preferences, an LLM advisor that shapes elicitation, and a practice-skill decay term.
Strength: Medium
The theory is real but thin. Most formal results are in working papers, and two key papers (Rafieian and Zuo; Schmit and Riquelme) were read only through abstracts or search excerpts. The empirical deskilling result (Bastani et al. 2025, PNAS) is strong but comes from one school. It holds for a short, single-domain tutoring setting. It does not show that the preference-learning dynamics hold.

## What Exists
### Sub-theme 1: Strategic users and behavior-vs-utility inversion (recommenders)
- **Recommending to Strategic Users** (Haupt, Hadfield-Menell and Podimata, 2023, arXiv preprint 2302.06559) — Platform commits to a recommendation policy after a cold-start phase in which users consume content strategically. Equilibrium amplifies preference differences; minorities may avoid mainstream content. Three fixes are proposed (priors, disclosure, personalized-but-likeable first content).
  - Relevance: Core model of a user who knows her consumption shapes future recommendations. Primitives are a platform commitment, a cold-start phase, and strategic consumption. The update rule is not given in the abstract.
  - OpenAlex ID: W4320854936 (Cited by: 26). Indexed as RePEc working paper, 2023.
- **The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization** (Kleinberg, Mullainathan and Raghavan, 2024, Management Science; earlier EC 2022 version)
  - Model: platform maximizes user utility but observes only engagement. Content lies on a manifold parametrized by content features. A user has inconsistent preferences (in-the-moment choice diverges from reflective utility).
  - Result: whether higher engagement raises utility depends on the direction of movement across the manifold. The paper characterizes manifolds where raising engagement fails to raise utility.
  - Relevance: This is the formal version of the behavior-vs-utility problem. The advisor objective is utility, the observable is engagement, and the state is the user's reflective preference.
  - OpenAlex ID: W4388464161 (Cited by: 69, Management Science). EC 2022 version: W4285395868 (Cited by: 13).
- **The Inversion Problem: Why Algorithms Should Infer Mental State and Not Just Predict Behavior** (Kleinberg, Ludwig, Mullainathan and Raghavan, 2023, Perspectives on Psychological Science)
  - Conceptual argument: algorithms trained on behavior should infer the mental state that generates it. The paper is a position piece, not a formal model (from OpenAlex metadata and a search excerpt).
  - Relevance: Frames the advisor's task as inverting behavior to a latent preference.
  - OpenAlex ID: W4389609170 (Cited by: 35).
- **Human Interaction with Recommendation Systems** (Schmit and Riquelme, 2018, AISTATS; arXiv 1703.00535 as "On Bias and Exploration")
  - Model (from search excerpt only): agents combine the platform's aggregate score with private preferences. Naive estimators that ignore the feedback loop are inconsistent. Consistent estimators are efficient under myopia. Heterogeneous agents explore without incentives.
  - Relevance: Shows that ignoring user feedback loops biases the platform's learning. Says nothing about the user learning her own preferences.
  - OpenAlex ID: W2795541372 (Cited by: 25, arXiv listing).
- **First I "like" it, then I hide it** (Eslami, Karahalios, Sandvig, Vaccaro, Rickman, Hamilton and Kirlik, 2016, CHI) — Empirical study of users who adjust feed signals to steer recommendations. Title and metadata only; not read in full.
  - Relevance: Empirical support for strategic feedback. Found via the reference list of Haupt et al.
  - OpenAlex ID: W2405896853 (Cited by: 463).
- **Scoring Strategic Agents** (Ball, 2025, American Economic Journal: Microeconomics) — Reference of Haupt et al. (OpenAlex W2989070978, Cited by: 85). Not read; listed only as a lead on strategic scoring.

### Sub-theme 2: Bayesian self-learning under recommendations
- **Personalization, Algorithmic Dependence, and Learning** (Rafieian and Zuo, working paper, Cornell SC Johnson, 2024; SSRN 5037671)
  - From search excerpt (PDF not parsed; SSRN page blocked): users are unsure of tastes and update by Bayesian learning. Users decide by Thompson sampling. Users with unclear preferences do worse without recommendations, depend more on the system, and learn less about themselves over time. Dependence can be rational because the gain from the algorithm grows with time.
  - Relevance: Closest match to a user who learns her own preferences under an advisor. The update rule and the platform objective were not verified.
  - OpenAlex: not found in OpenAlex search.
- **Preference Dynamics Under Personalized Recommendations** (Dean and Morgenstern, 2022, ACM EC) — Covered in earlier rounds. Linked here only as the drift model that Round 0 already reviewed. OpenAlex ID: W4285088850 (Cited by: 37).
- **Recommending Products When Consumers Learn Their Preference Weights** (Dzyabura and Hauser, 2019, Marketing Science) — Covered in earlier rounds (own-taste learning). Linked here as the closest marketing model of a consumer learning weights. OpenAlex ID: W2945152270 (Cited by: 103).

### Sub-theme 3: Repeated cheap talk and biased or learning advisors
- **Anonymous or personal? A simple model of repeated personalized advice** (Gramb and Schottmüller, 2022, University of Cologne Working Paper 105)
  - Model (from search excerpt): an expert gives advice to a consumer repeatedly. The expert earns a bonus for steering the consumer, and learns the consumer over time. In simple equilibria, learning makes both sides better off when it sharpens the expert's guess. A lab experiment tests the predictions.
  - Relevance: Advisor learns the user, while the user does not learn her own preferences. The advisor objective includes a bias term.
  - Lab results were not retrieved.
- **Waseda advisor-guesser model** (Waseda working paper E2532, 2026; authors and title not confirmed) — Repeated game in which the advisor's bias is uncertain and evidence builds over time. A consistent recommendation can signal bias, while a changed one can signal limited knowledge. PDF returned HTTP 403; known only from a search excerpt.
- **Gradual learning by a biased expert** (Frug, 2014, Ben-Gurion University seminar paper; title not confirmed) — Expert learns gradually and strategically, extending Crawford and Sobel (1982). Known only from search excerpt.
- **Forecasts from an expert of unknown bias** (Valsecchi, 2023, FEEM working paper NDL2023-020; title not confirmed) — Repeated cheap talk with reputational concerns. Known only from search excerpt.
- **Advisor competence and bias** (KU Copenhagen Discussion Paper 16-10, 2016; title not confirmed) — Decision maker learns advisor type and may fire an advisor. Known only from search excerpt.
- Crawford and Sobel (1982) is the static baseline for cheap talk. Not fetched; cited from general knowledge.

### Sub-theme 4: Cognitive models of personalized learning
- **How personalization guides (or distorts) learning: A model-based explanation** (Bahg, Galdo, Day, Sloutsky and Turner, 2021, MathPsych/ICCM virtual conference)
  - Model: exemplar category learner with latent representations and attention weights, updated by gradient steps in the style of Kruschke (1992). Three sampling conditions: baseline, self-directed, and curated by an algorithm. Simulations show curated learners develop distorted representations and are overconfident on an independent dataset.
  - Relevance: Cognitive model where the sequence provider shapes what the learner samples. Learns categories, not preferences.
  - Conference abstract only (not the full paper).

### Sub-theme 5: Deskilling and reliance
- **The enrichment paradox: critical capability thresholds and irreversible dependency in human-AI symbiosis** (Park, Kim and Han, 2026, arXiv 2603.24391)
  - Model: two-variable dynamical system of capability H and delegation D. Three axioms: learning requires capability, practice builds it, disuse causes forgetting. Capability collapses past threshold K* ≈ 0.85. Reported fit to PISA data from 15 countries (102 points, R² = 0.946, 3 parameters).
  - Relevance: Direct model of skill decay under delegation. Preference learning is not modeled. Equations were not visible in the abstract page.
  - The threshold is a calibration fit in a preprint, so treat it as low confidence.
- **The Augmentation Trap: AI Productivity and the Cost of Cognitive Offloading** (Caosun and Aral, 2026, arXiv 2604.03501)
  - Model: a decision maker chooses offloading intensity over time. The productivity effect splits into an expertise-independent part and an expertise-dependent part. Results: rational adoption can lower long-run productivity; short-termist managers can make workers worse off; strong AI substitution produces permanent divergence between high- and low-skill workers.
  - Relevance: Same skill-decay logic as Park et al., with an explicit manager objective. Does not include preference learning.
- **Generative AI without guardrails can harm learning: Evidence from high school mathematics** (Bastani, Bastani, Sungu, Ge, Kabakcı and Mariman, 2025, PNAS)
  - Design: field experiment with about 1,000 high school students in Turkey. Unrestricted GPT Base helped during practice and hurt later unassisted performance. GPT Tutor, with learning-safe prompts, largely offset the harm. Magnitudes from secondary coverage (a 17% drop on later tests); check the paper.
  - Relevance: Strongest empirical evidence for AI reliance reducing the user's own competence. Single school and short curriculum.
  - OpenAlex ID: W4411627694 (Cited by: 965). A correction-search found no erratum.

### Sub-theme 6: LLM-based preference elicitation
- **Mind the Gap: How Elicitation Protocols Shape the Stated-Revealed Preference Gap in Language Models** (Mahajan, Kendiukhov, Hussain and Nottingham, 2026, arXiv 2601.21975)
  - Study: 24 language models. The rank correlation between stated and revealed preferences depends on the elicitation protocol. Allowing neutrality in stated preferences raises the correlation. Allowing abstention in revealed preferences pushes it to near zero or negative. Steering by stated preferences does not reliably help.
  - Relevance: Shows that the questioning format changes what an LLM records as a preference. This is measurement, not dynamics. It does not model a user's preference changing over time.
- **Rethinking the Expert User Paradigm** (2026; authors not confirmed) — Secondary alphaxiv summary only. COPREF model and COSHOP benchmark reportedly show LLM agents repeat preference questions. Not verified.

### Sub-theme 7: Variety-seeking and satiation in marketing
- **A Dynamic Attribute Satiation Model of Variety-Seeking Behavior** (McAlister, 1982, Journal of Consumer Research) — Foundational satiation model: attributes lose appeal with use, so consumers switch. Known from a reference list, not read.
- **Modeling Consumer Demand for Variety** (Kim, Allenby and Rossi, 2002, Marketing Science) — Horizontal variety seeking via diminishing marginal returns (satiation). Known from a reference list, not read.
- Terui threshold satiation model (Terui, year and venue not confirmed) — Preference factors shift only when a latent satiation variable crosses a threshold. Fits scanner and field-experiment panels. Known from a search summary only.

## Reference Chain Discoveries
- Found via: Haupt et al. (2023) references and citers. Eslami et al. 2016 (CHI), Ball 2025 (AEJ Micro), Schmit and Riquelme (2018), Dean and Morgenstern (2022, citers included Harm Mitigation under user preference dynamics, W4401863955, Cited by: 10, not read).
- Found via: Kleinberg et al. citers. "Engagement, user satisfaction, and the amplification of divisive content on social media" (W4408138635, 2025, Cited by: 346, not read). "AI Alignment with Changing and Influenceable Reward Functions" (W4399151482, 2024, Cited by: 41, not read). These bear on reward drift and are leads only.
- Found via: Bastani et al. (2025) citers. "AI makes you smarter but none the wiser" (W4415002361, 2025, Cited by: 149, not read). "Experimental evidence of the effects of large language models versus web search on depth of learning" (W4415615340, 2025, Cited by: 78, not read). "AI-induced never-skilling in medical education" (W7162142312, 2026, Cited by: 76, not read).
- Found via: Dzyabura and Hauser (2019) citers. Mostly marketing-AI reviews. No formal dynamic model found beyond those listed above.
- Found via: Schmit and Riquelme citers. "How algorithmic confounding in recommendation systems increases homogeneity and decreases utility" (W2765564115, 2018, Cited by: 419, Chaney et al.; covered in Round 0). "Bayesian Exploration with Heterogeneous Agents" (W2911712993, 2019, Cited by: 25, not read).

## What's Missing (Gaps)
- No model combines all three: a user who learns her own preferences, an advisor (an LLM) whose questions shape those preferences, and a practice term that decays skill. Caosun and Aral and Park et al. model skill but not preferences. Rafieian and Zuo model preferences and dependence but not elicitation.
- No model of an LLM advisor that chooses which questions to ask, with the user's posterior moving in response. The elicitation work (Mahajan et al.) is measurement only.
- Gramb and Schottmüller and the cheap-talk models give the advisor a learning objective, but none gives the user a self-learning state with an endogenous question menu.
- No formal model has been validated against longitudinal real-user taste data. Preference Dynamics (Dean and Morgenstern) and the Haupt model are theoretical.
- Variety-seeking models (McAlister; Kim, Allenby and Rossi; Terui) have not been linked to LLM advisors. They are not in the AI-advisor literature found here.

## Contradictions or Tensions
- **Strategic users widen differences vs. filter bubbles are mixed.** Haupt et al. predict that strategic consumption widens preference gaps. Search results report a MovieLens study where recommendations reduced filter-bubble behavior, and a YouTube experiment with no short-term attitude effect (authors not confirmed). The theory and the field evidence disagree on direction.
- **Rational dependence vs. harmful dependence.** Rafieian and Zuo show dependence can be rational because the algorithm's value rises over time. Bastani et al. (2025) show unguarded AI use harms later unassisted performance. The two can both hold: the harm depends on whether the tool is designed to scaffold practice.
- **Deskilling threshold vs. continuous decay.** Park et al. predict abrupt collapse past K* ≈ 0.85. Caosun and Aral predict permanent divergence under strong substitution. Neither has been tested with real preference data. The threshold is a calibration fit.
- **Engagement can match utility vs. can diverge.** Kleinberg et al. show engagement optimization is near-optimal on some manifolds and fails on others. Haupt et al. show strategic behavior distorts the signal. Both papers agree the platform cannot read utility directly.

## Confidence
Medium
- What would raise confidence: A full-text read of Rafieian and Zuo (equations, simulations, data) and Schmit and Riquelme (model and regret bounds). A longitudinal study that measures users' stated preferences before and after AI advice, with a replicated deskilling result beyond one school.
- What would lower confidence: Evidence that users' stated preferences do not move with recommendations in real data. A replication of Bastani et al. that finds no later-test harm once the tool is removed. Full-text checks showing the Park et al. threshold depends on the calibration.

## Search Log
### Round 1: Broad search
- Queries: "Haupt Podimata strategic users recommender system learning preferences"; "Kleinberg Mullainathan Raghavan inferring behavior-specific preferences utility inversion"; "repeated cheap talk biased advisor learning user preferences model"; "AI assistance deskilling model users learning reliance theoretical economics"; "LLM preference elicitation shapes user preferences constructed preferences model"; "variety seeking satiation dynamic model consumers learn preferences marketing"; "Bayesian learning of own preferences recommendation feedback loop users uncertain about tastes theoretical model".
- Papers found: about 20 candidates across the queries, of which 14 are relevant after screening.
- Key leads: Haupt et al. (2023); Kleinberg et al. (2022, 2024); Rafieian and Zuo; Gramb and Schottmüller; Park et al. (2026); Mahajan et al. (2026); McAlister (1982).

### Round 2: Citation traversal
- Papers traversed: Haupt et al. (references and citers); Kleinberg et al. "The Challenge of Understanding What Users Want" (citers; references returned no resolvable IDs); Dzyabura and Hauser (citers and references); Schmit and Riquelme (citers); Bastani et al. (citers).
- New papers from references: Eslami et al. (2016); Ball (2025); Schmit and Riquelme (2018); Dean and Morgenstern (2022, already covered); Haupt et al.'s other references.
- New papers from citers: Harm Mitigation under User Preference Dynamics; Engagement, user satisfaction, and the amplification of divisive content; AI makes you smarter but none the wiser; Experimental evidence of LLMs vs web search; AI-induced never-skilling in medical education; Bayesian Exploration with Heterogeneous Agents.

### Round 3: Reference section mining
- Papers mined: Haupt et al. (abstract and model summary, full text not parsed); Kleinberg et al. (abstract only; PDF fetch returned binary); Schmit and Riquelme (search excerpt).
- New papers from references: Waseda advisor-guesser model; Frug (2014); Valsecchi (2023); KU Copenhagen advisor competence paper (2016).
- Note: Rafieian and Zuo PDF was unreadable (binary). Its model is from a search excerpt only.

### Round 4: Gap-filling
- Gaps targeted: deskilling theory (no formal model with preferences); LLM elicitation dynamics; cognitive models of personalized learning; variety-seeking links to AI.
- Queries: "Rafieian Zuo 'Personalization, Algorithmic Dependence, and Learning' working paper"; "Gramb Schottmüller repeated personalized advice search engine learns consumer experiment"; "Bastani generative AI without guardrails can harm learning"; "variety seeking satiation dynamic model consumers learn preferences marketing".
- New findings: Park et al. (2026) and Caosun and Aral (2026) are formal skill-decay models. Bahg et al. (2021) gives a cognitive account. Mahajan et al. (2026) gives elicitation measurement. Bastani et al. (2025) gives the empirical deskilling result.
- Note: a WebFetch attempt on a made-up arXiv ID returned 404. No result was used.

### Round 5: Adversarial check
- Gaps targeted: critiques of strategic-user models; filter-bubble and taste-change evidence; corrections to the Bastani result.
- Queries: "recommender system does not change user preferences empirical evidence filter bubble taste change critique"; "Correction Bastani 'Generative AI without guardrails...' PNAS correction notice".
- New findings: Mixed filter-bubble evidence (see Contradictions). No correction notice found for Bastani et al. Waseda PDF returned HTTP 403. SSRN page for Rafieian and Zuo returned HTTP 403.

### Round 6: Gap-filling (LLM influence on user opinions)
- Gaps targeted: whether LLM advice changes user stated preferences directly.
- Queries: "LLM chatbot advice changes user opinions or preferences experiment persuasion sycophancy users shift stated preferences 2025".
- New findings: Opinion shifts from LLM dialogue are reported (2025 preprints; Nature and Science studies, December 2025, secondary coverage only). No study found that directly measures preference shifts from LLM elicitation. Not included as papers; noted as a gap.

### Convergence note
- Total unique relevant papers found: 19 (including Round 0 links that are only cited for context)
- New papers in last round: 0 included as papers (Round 6 produced secondary-coverage leads only)
- Stopped because: Rounds 5 and 6 produced no new included papers, and the core subfields (strategic recommenders, behavior-vs-utility, advisor learning, deskilling, elicitation, satiation) each had at least one formal or empirical anchor. Full-text access to two key models (Rafieian and Zuo; Schmit and Riquelme) was blocked, so the stop is not a full coverage claim.
