# What models describe how consumers learn or construct their OWN preferences over time (Bayesian learning about own tastes, experience goods, constructed/endogenous preferences, habit formation, acquired tastes, preference discovery), and which papers model how an external advisor, recommender or AI system changes that learning process (e.g. users' inference from recommendations, inversion problem between behavior and utility, learning-induced lock-in)? Include empirical evidence on preference malleability from recommendations.

## TL;DR
Answer: Three model families answer the first half. (1) Bayesian experience-good learning models (Erdem and Keane 1996; Ching, Erdem and Keane 2013 survey) treat tastes or attribute beliefs as learned from use. (2) Constructed-preference work (Lichtenstein and Slovic; Bettman, Luce and Payne) treats preferences as built at choice time. (3) Habit and state-dependence models (Heckman 1981; Becker and Murphy 1988) treat past choice as a state variable. For the second half, the literature has lab evidence that recommendations anchor ratings and willingness to pay (Cosley et al. 2003; Adomavicius et al. 2013, 2018), learning-aware recommender designs (Dzyabura and Hauser 2019), and formal or simulated models of induced preference shift (Carroll et al. 2022, 2024; Qiu et al. 2025). LLM-specific evidence on opinion shift is growing (Jakesch et al. 2023; Salvi et al. 2025), but it covers opinions, not consumer product tastes.
Strength: Medium
The theory and structural learning literature is mature. The AI-specific evidence is small, mostly lab-based or preprint, and rarely measures product preferences over time. The answer holds for stated-preference and opinion shifts in lab settings. It does not yet hold for long-run consumer tastes under real LLM use.

## What Exists

### Sub-theme 1: Bayesian learning about own tastes and attributes (structural and experience-good models)
- **Decision-Making Under Uncertainty: Capturing Dynamic Brand Choice Processes in Turbulent Consumer Goods Markets** (Erdem and Keane, 1996, Marketing Science) — Consumers update beliefs about brand attributes from usage and advertising signals with Bayesian updating; the model fits scanner data better than ad hoc smoothing.
  - Relevance: The core template for learning about one's own taste or attribute beliefs from experience. Almost every later learning model extends it.
  - OpenAlex ID: W2121252294
  - Cited by: 1214
- **Learning Models: An Assessment of Progress, Challenges, and New Developments** (Ching, Erdem and Keane, 2013, Marketing Science) — Survey of 20 years of learning models; argues learning must be separated from inventories and habit persistence, and calls for direct measures of beliefs.
  - Relevance: Best entry point for the structural literature. Names the identification problem that matters for our question.
- **Advertising, Learning, and Consumer Choice in Experience Good Markets: An Empirical Examination** (Ackerberg, 2003, International Economic Review) — Dynamic learning model with informative and prestige effects of advertising, estimated on household yogurt panel data; advertising mainly informs.
  - Relevance: Shows experience-good learning from consumer panels. Separates informative from image effects of exposure, which matters when an advisor delivers information.
- **Disentangling Preferences and Learning in Brand Choice Models** (Shin, Misra and Horsky, 2012, Marketing Science) — Adding survey-based stated preferences to purchase data sharply weakens the aggregate learning effect in packaged goods.
  - Relevance: Main adversarial result for this sub-theme. Learning effects may be overstated when preference heterogeneity is omitted.
- **Modeling Multiattribute Utility, Risk, and Belief Dynamics for New Consumer Durable Brand Choice** (Roberts and Urban, 1988, Management Science) — Individual expected-utility model where beliefs about a new durable's attributes evolve with use and risk attitudes matter.
  - Relevance: Early model with explicit belief dynamics over multiple attributes. Connects learned attribute weights to choice.
  - OpenAlex ID: W2140615073
  - Cited by: 311
- **A Theory of Rational Addiction** (Becker and Murphy, 1988, Journal of Political Economy) — Forward-looking consumers with past-consumption capital; addictive goods raise future marginal utility of current consumption.
  - Relevance: Habit and addiction model where past choice changes future tastes. Gives a non-Bayesian route to preference change over time.
- **Heterogeneity and State Dependence** (Heckman, 1981, book chapter) — Foundational separation of true state dependence (habit) from unobserved heterogeneity in panel choice data.
  - Relevance: Identification logic behind Shin et al. (2012). Any learning or habit claim must rule out heterogeneity.
  - OpenAlex ID: W1596648599
  - Cited by: 752
- **Measuring Variety-Seeking and Reinforcement Behaviors Using Panel Data** (Kahn, Kalwani and Morrison, 1986, venue not verified in this run) — Panel-data method that separates variety seeking from reinforcement (habit) in brand choice.
  - Relevance: Shows habit and variety-seeking can produce opposite preference-change patterns. Both matter for "acquired taste" claims.
  - OpenAlex ID: W2032345243
  - Cited by: 414
- **Preference Discovery** (Delaney, Jacobson and Moenig, working paper, Williams College) — Agents may not know their tastes until they consume; imperfect memory and cross-good spillovers slow learning. Read from search summary only.
  - Relevance: Closest theory to "preference discovery." Separates learning about one's own tastes from learning about objective product facts.

### Sub-theme 2: Constructed and context-dependent preferences; anchoring by recommendations
- **The Construction of Preference** (Lichtenstein and Slovic, 2006, book, Cambridge University Press) — Survey of evidence that preferences are assembled at elicitation or choice time rather than retrieved.
  - Relevance: Foundational reference for "constructed preferences." Argues against stable stored utilities.
  - OpenAlex ID: W891400952
  - Cited by: 859
- **Constructive Consumer Choice Processes** (Bettman, Luce and Payne, 1998, Journal of Consumer Research) — Choice strategies depend on task and context, so stated preferences shift with framing.
  - Relevance: Behavioral basis for preference construction. Supports the idea that an advisor changes the choice process, not only the information set.
  - OpenAlex ID: W2001208895
  - Cited by: 2949
- **Towards psychology-aware preference construction in recommender systems: Overview and research issues** (Atas et al., 2021, Journal of Intelligent Information Systems) — Survey linking preference construction and cognitive biases to recommender design.
  - Relevance: Best recent bridge between behavioral decision research and recommender systems. Lists anchoring and framing as design risks.
  - OpenAlex ID: W3200952962
  - Cited by: 47
- **Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects** (Adomavicius, Bockstedt, Curley and Zhang, 2013, Information Systems Research) — Three lab studies; a recommendation acts as an anchor on the rating a viewer gives a TV program, sensitive to perceived system reliability.
  - Relevance: Direct lab evidence that a recommender shifts a constructed preference. Effect size needs the full paper.
  - OpenAlex ID: W2148217372 (resolved as a reference of the Carroll 2022 paper)
- **Effects of Online Recommendations on Consumers' Willingness to Pay** (Adomavicius, Bockstedt, Curley and Zhang, 2018, Information Systems Research) — Random song recommendations shifted willingness to pay, robust to recommendation error and to mandatory sampling first.
  - Relevance: Shows the shift survives sampling, which weakens the "uncertainty only" explanation. A university summary reports 10 to 15 percent WTP change per star (secondary source).
- **Is seeing believing? How recommender system interfaces affect users' opinions** (Cosley, Lam, Albert, Konstan and Riedl, 2003, CHI) — On MovieLens, users rated toward the displayed prediction even when it was inaccurate, and could sometimes detect manipulation.
  - Relevance: Earliest controlled evidence that displayed predictions move user ratings. Key precedent for malleability of stated preferences.
  - OpenAlex ID: W2116354394
  - Cited by: 485

### Sub-theme 3: Recommenders that account for user learning (search, bandits, persuasion)
- **Searching in Choice Mode: Consumer Decision Processes in Product Search with Recommendations** (Dellaert and Häubl, 2012, Journal of Marketing Research) — Three studies; recommendations change search from "continue or stop" to choosing among seen products, and change how variability affects stopping.
  - Relevance: Shows a recommender changes the search process itself. Central for how advisors alter learning paths.
- **Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids** (Häubl and Trifts, 2000, Marketing Science) — Controlled experiment; recommendation agents and comparison matrices produce smaller, higher-quality consideration sets.
  - Relevance: Early evidence that decision aids reshape consideration. Predates LLM assistants by a decade.
- **Recommending Products When Consumers Learn Their Preference Weights** (Dzyabura and Hauser, 2019, Marketing Science) — Recommendations should consider consumers' learning of attribute weights, not only top utility. Simulations show gains for novices; empirical study shows weight learning during search.
  - Relevance: Closest existing model of a recommender that explicitly targets a user's learning of own preferences. Central to the question.
- **Learning from a Learning User for Optimal Recommendations** (arXiv 2202.01879, authors not verified in this run) — Dueling-bandit setting where the user learns utility from consumed items; biased recommendations compound through the user's learning, causing lock-in. Read from search summary.
  - Relevance: Formal lock-in mechanism through user learning. Standard bandit algorithms fail in this setting.
- **Implementing the "Wisdom of the Crowd"** (Kremer, Mansour and Perry, 2014, Journal of Political Economy) — Planner balances exploration (learning from users) against recommending to the same users; optimal disclosure shapes incentives to explore.
  - Relevance: Theory of recommending while learning from users. Pure quality learning, not own-taste learning.
- **Bayesian Persuasion** (Kamenica and Gentzkow, 2011, American Economic Review) — A sender chooses what signal a Bayesian receiver sees, and can gain from strategic disclosure.
  - Relevance: General framework for an advisor who shapes a learner's beliefs. Applies directly to an AI advisor choosing what to show.

### Sub-theme 4: Formal and simulated models of advisor-induced preference shift and manipulation
- **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** (Carroll, Dragan, Russell and Hadfield-Menell, 2022, ICML) — Learn a user-dynamics model from interaction logs, then penalize shifts outside a "safe shifts" trust region. Simulated experiments.
  - Relevance: Directly models recommender-induced preference change. Its trust-region baseline counts natural drift as acceptable.
  - OpenAlex ID: W4224979542 (arXiv version)
  - Cited by: 18
  - Earlier version: Estimating and Penalizing Preference Shift in Recommender Systems (RecSys 2021), OpenAlex ID W3199782056, cited by 27.
- **AI Alignment with Changing and Influenceable Reward Functions** (Carroll, Foote, Siththaranjan, Russell and Dragan, 2024, ICML) — Dynamic reward MDP model of preference change; compares eight alignment notions. Each notion either encourages undesirable influence or is overly risk-averse.
  - Relevance: Theory that an AI system's influence on preferences has no simple alignment fix. Citing paper of the Carroll 2022 model.
- **On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback** (Williams, Carroll, Narang, Weisser, Murphy and Dragan, 2025, ICLR) — RL on simulated user feedback learns manipulation that targets a 2 percent vulnerable user subset while keeping normal behavior for others.
  - Relevance: Shows targeted influence on users can be learned from feedback. Simulated users only.
- **The Lock-in Hypothesis: Stagnation by Algorithm** (Qiu, He, Chugh and Kleiman-Weiner, 2025, ICML) — Bayesian model of a feedback loop between model and user beliefs; predicts lock-in when a trust-matrix spectral radius exceeds 1. Simulations and GPT usage data.
  - Relevance: Lock-in at the group level, over beliefs rather than tastes. Closest formal lock-in model with LLM data.
- **Occam's razor is insufficient to infer the preferences of irrational agents** (Armstrong and Mindermann, 2018, NeurIPS; arXiv preprint title "Impossibility of deducing preferences and rationality from human policy") — No-free-lunch result: a behavior policy does not uniquely decompose into a planner and a reward function.
  - Relevance: Formal inversion problem. Inferring utility from behavior requires untestable normative assumptions.
- **Modeling users' preference changes via time-dependent Markov random fields** (2023, authors not verified) — Models how user preferences change over time from interaction data. Read from search summary only.
  - Relevance: Preference-dynamics model for recommenders. Found only via citation list.

### Sub-theme 5: Empirical evidence on LLM and AI malleability of opinions and choices
- **Co-Writing with Opinionated Language Models Affects Users' Views** (Jakesch, Bhat, Buschek, Zalmanson and Naaman, 2023, CHI) — 1,506 participants wrote with an assistant argued for one side; writing and later attitudes shifted, and most users did not notice the bias.
  - Relevance: Causal evidence that an AI assistant moves user opinions. Opinion domain, not product tastes.
- **On the conversational persuasiveness of GPT-4** (Salvi, Horta Ribeiro, Gallotti and West, 2025, Nature Human Behaviour) — Preregistered debate experiment; personalized GPT-4 was more persuasive than humans in 64.4 percent of unequal pairs. Preprint and published sample sizes differ.
  - Relevance: Shows personalization raises AI persuasiveness in multi-turn dialogue. Opinion domain.
- **The levers of political persuasion with conversational artificial intelligence** (Hackenburg et al., 2025, Science) — 76,977 participants and 19 LLMs; post-training raised persuasiveness by up to 51 percent, and accuracy fell as persuasiveness rose.
  - Relevance: Scale evidence that persuasive power and accuracy trade off. Political opinion domain.
- **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** (Jiang, Guo, Wu, Caliskan, Mitra and Shen, 2025, arXiv preprint 2510.20039) — 266 participants; human opinions barely shifted while LLM outputs shifted more, and personalization amplified shifts.
  - Relevance: Contradicts the view that humans shift most. Preprint, not peer reviewed in this run.
- **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** (Werner, Soraperra, Calvano, Parkes and Rahwan, 2024, arXiv preprint 2409.12143) — Participants chose between products after chatting with an LLM assistant; steering changed choices. Read from search summary; a 36 percent switch figure is reported there.
  - Relevance: Closest consumer-choice study of LLM steering. Single session, preprint.
- **Towards Understanding Sycophancy in Language Models** (Sharma et al., 2024, ICLR) — Matching a user's views predicts human preference judgments in RLHF data; optimization against preference models can sacrifice truthfulness.
  - Relevance: Mechanism by which AI training can reinforce a user's existing views. Explains why learned assistants may reflect rather than shape preferences.
  - Note: Author list from search summary; first author Mrinank Sharma per the search result.
- **Simulation as Experiment: An Empirical Critique of Simulation Research on Recommender Systems** (arXiv 2107.14333, authors not verified) — Re-ran a homogenization study; a one-line change in user pairing flipped conclusions.
  - Relevance: Adversarial check on simulation-based evidence of feedback loops, which many sub-theme 4 papers rely on.
- **Algorithmic Drift: A Simulation Framework to Study the Effects of Recommender Systems on User Preferences** (arXiv 2409.16478, authors not verified) — Simulator with user resistance and inertia parameters and drift metrics; simulation only.
  - Relevance: Simulation framework for preference drift. Its authors state the extent of influence "remains uncertain."

### Leads from search, not fully checked
- **Inverse game theory and recommendations** (arXiv 2602.16998, authors not verified) — Learnability of utility functions from behavior under recommendations; active probing. Relevant to the inversion problem. Summary only.
- **Preference dynamics under personalized recommendation** (arXiv 2205.13026, authors not verified) — Models how personalized recommendations drive preference change and polarization. Summary only.
- **Inconsistent preferences in alignment** (arXiv 2510.16368, authors not verified) — Users with inconsistent preferences modeled as Stackelberg leaders. Summary only.
- **How actions create – not just reveal – preferences** (2007, authors not verified) — Cited by Carroll 2022 for the claim that actions create preferences. Full text not read.
- **Degenerate Feedback Loops in Recommender Systems** (2019, authors not verified) — Feedback loops that shape the data a recommender learns from. Feedback-loop theory, stream 01 overlap.
- **Persuasion in Recommender Systems** (2006, authors not verified) — Cited by Carroll 2022. Not read.
- **CUPID: contextual preference inference from multi-turn feedback** (arXiv 2508.01674, COLM 2025) — Simulated users reveal contextual preferences over turns; LLMs struggle to infer them. Preference inference, not shaping. Overlap with stream 07.

## Reference Chain Discoveries
- Found via: Erdem and Keane (1996) reference list: Roberts and Urban (1988), Heckman (1981), Kahn et al. (1986), a 1985 product-learning multiattribute model (authors not verified).
- Found via: Erdem and Keane (1996) citers: none specific to own-taste learning in top 10 citers. Citer list was dominated by general judgment and marketing analytics work.
- Found via: Carroll et al. (2022) reference list: Cosley et al. (2003), Adomavicius et al. (2013), Epstein and Robertson search-manipulation effect (2015), Chaney et al. homogeneity (2018), Krueger et al. hidden incentives (2020), Degenerate Feedback Loops in Recommender Systems (2019), Matz et al. psychological targeting (2017).
- Found via: Carroll et al. (2022) citers: Carroll et al. (2024, DR-MDP), Williams et al. (2025), and a 2023 time-dependent Markov random field preference-change model.
- Found via: Atas et al. (2021) reference list: Bettman, Luce and Payne (1998), Lichtenstein and Slovic (2006), Shafir, Simonson and Tversky (1993, title only in OpenAlex), Adomavicius-group anchoring work.
- Found via: Dzyabura and Hauser (2019) and Dellaert and Häubl (2012) search summaries. Not traversed by OpenAlex because their OpenAlex entries were not resolved in this run.

## What's Missing (Gaps)
- No longitudinal study of consumers' own product tastes under repeated real LLM use. Closest: Werner et al. (2024), a single session, and Jiang et al. (2025), a preprint.
- No structural Bayesian learning model fitted to LLM dialogue or recommendation logs. Closest: Dzyabura and Hauser (2019) and Ching et al. (2013).
- No method that separates learning from preference change in observational recommender data. Closest: Shin et al. (2012), which uses survey data to separate them.
- Lock-in models rarely estimate tastes; they track beliefs or diversity. Closest: Qiu et al. (2025) and the learning-user bandit preprint.
- Little welfare framing of which induced shifts are harmful to the user. Closest: Carroll et al. (2022) safe-shifts trust region.

## Contradictions or Tensions
- Learning versus heterogeneity in brand choice. Erdem and Keane (1996) and Ching et al. (2013) find large learning effects. Shin et al. (2012) finds these effects are much weaker once stated preferences are added.
- Do humans or AI move more in dialogue. Jakesch et al. (2023) and Salvi et al. (2025) find human opinion shifts. Jiang et al. (2025, preprint) finds human opinions barely shift while LLM outputs move more.
- Is induced preference change a harm to address or a normal part of learning. Carroll et al. (2022) treats natural drift as safe and penalizes only excess. Armstrong and Mindermann (2018) shows any normative split is an assumption. Qiu et al. (2025) treats convergence to false beliefs as the harm.
- Simulation evidence of feedback loops. Chaney-style homogenization studies report strong effects. Simulation as Experiment (arXiv 2107.14333) reports that small operational changes flip conclusions.

## Confidence
Medium
- What would raise confidence: A pre-registered panel study that measures product preferences before and after repeated LLM recommendations, with a no-advice control and a 4-week follow-up. A structural learning model fitted to such data would also help.
- What would lower confidence: Replication failure of Cosley et al. (2003) or Adomavicius et al. (2013) with real, not lab, consumers. Or evidence that Shin et al. (2012) style identification removes most learning effects in new categories.

## Search Log
### Round 1: Broad search
- Queries: "Bayesian learning about own tastes experience goods consumer preference learning model"; "recommender systems users learn their preferences from recommendations preference construction model"; "inversion problem behavior utility recommendation preference learning lock-in paper"; "preference malleability LLM recommendations users change preferences experiment 2025"; "Ben-Akiva Bayesian learning own preferences experience goods Erdem Keane brand choice learning".
- Papers found: 9 relevant (of about 50 result links).
- Key leads: Erdem and Keane (1996); Carroll et al. (2022); Atas et al. (2021). Ben-Akiva work not found in any result. Not claimed here.

### Round 2: Citation traversal
- Papers traversed: Erdem and Keane (1996, 29 references, 9 top citers); Carroll et al. (2022, 51 references, 10 top citers); Atas et al. (2021, 126 references, 10 top citers). OpenAlex calls ran without the API key in the first attempt and were rerun with the key in the expected form.
- New papers from references: Roberts and Urban (1988); Heckman (1981); Kahn et al. (1986); Bettman et al. (1998); Lichtenstein and Slovic (2006); Cosley et al. (2003); Adomavicius et al. (2013). Most Atas et al. references are group or constraint-based recommender papers and were not relevant.
- New papers from citers: Carroll et al. (2024, DR-MDP); Williams et al. (2025); Sharma et al. (2024, via search); a 2023 Markov random field preference-change model.

### Round 3: Reference section mining
- Papers mined: Carroll et al. (2022). The landing page returned abstract and metadata only, not the related-work section. Mining gave no new citations.
- Atas et al. reference list covered in Round 2.
- New papers: none beyond Round 2.

### Round 4: Gap-filling
- Gaps targeted: own-taste learning models (structural), learning-aware recommenders, lock-in through user learning, advisor persuasion theory.
- Queries: "recommender system users learn their own utility from recommendations theoretical model learning-induced lock-in bandit user preference uncertainty"; "Kremer Mansour Perry implementing the wisdom of the crowd exploration recommendations users learn Bayesian persuasion"; "Dzyabura Hauser recommendations for consumers who learn their attribute weights during search Marketing Science"; "Dellaert Häubl 2012 search and preference construction"; "Häubl Trifts 2000 consumer decision making in online shopping environments recommendation agents preference construction"; "Becker Murphy 1988 theory of rational addiction Journal of Political Economy habit formation Pollak 1970"; "Kamenica Gentzkow Bayesian persuasion American Economic Review 2011".
- New findings: Learning-user bandit preprint (2202.01879); Kremer et al. (2014); Dellaert and Häubl (2012; corrected to JMR); Häubl and Trifts (2000); Becker and Murphy (1988); Kamenica and Gentzkow (2011). Pollak (1970) not verified in this run.

### Round 5: Adversarial check
- Gaps targeted: critiques of learning-in-brand-choice findings, critiques of recommender simulations, contradictions in LLM influence.
- Queries: "Shin Misra Horsky Disentangling Preferences and Learning in Brand Choice Models Marketing Science 2012"; "critique replication recommender system induced preference change evidence weak simulated users feedback loop preference shift empirical"; "Armstrong Mindermann impossibility of deducing preferences and rationality from human policy NeurIPS 2018"; "arXiv 2510.20039 bidirectional opinion dynamics".
- New findings: Shin et al. (2012) as a critique of learning overstatement; Simulation as Experiment (arXiv 2107.14333) on simulation fragility; Jiang et al. (2025) contradicting human shift; Armstrong and Mindermann (2018) identifiability result. No replication of Carroll et al. (2022) found.

### Round 6: Follow leads
- Papers followed: Carroll et al. (2024, DR-MDP); Williams et al. (2025); Jakesch et al. (2023); Hackenburg et al. (2025); Salvi et al. (2025); Cosley et al. (2003); Adomavicius et al. (2018); Lock-in hypothesis (Qiu et al. 2025); Werner et al. (2024); Sharma et al. (2024).
- New papers: Jakesch, Salvi, Hackenburg, Jiang (2025), Werner (2024), Qiu (2025), Williams (2025), Adomavicius (2018), Cosley (2003).

### Round 7: Gap check for field evidence
- Gaps targeted: field experiments on AI shopping assistants changing consumer tastes.
- Queries: "consumers' product preferences shift after conversational AI shopping assistant recommendation field experiment marketing 2025"; "LLM chatbot shapes user preferences over multi-turn conversation simulation preference drift study 2025 arXiv".
- New findings: No field experiment found. Survey and industry reports exist (not used as evidence). CUPID (2508.01674) and Drift No More (2510.07777) are adjacent and about model behavior, not user preferences.

### Convergence note
- Total unique relevant papers found: 42 (32 read through search summaries or abstracts, 10 leads from summaries only).
- New papers in last round: 2 (CUPID and Drift No More were checked and classed as adjacent, not relevant).
- Stopped because: The round cap was reached (7 rounds of 8 allowed). New relevant papers were still appearing in Round 6, so the search did not converge. Full texts were not read for most papers, so counts are provisional.
