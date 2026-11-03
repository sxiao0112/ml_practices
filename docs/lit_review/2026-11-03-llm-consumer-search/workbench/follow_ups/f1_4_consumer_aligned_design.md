# What research proposes and tests ways to make LLM search and shopping assistants act in the consumer's interest: debiasing agent choices (position, brand, anchoring), eliciting and representing user preferences for delegation, fiduciary or principal-agent alignment of AI shopping agents, disclosure and labeling of sponsored content in LLM answers, robustness to seller manipulation, and mechanism or market design for agent-mediated commerce? Which interventions have measured effects?

## TL;DR
Answer: Measured interventions so far are: (1) prompt warnings and fine-tuning on debiased examples, which cut bias in shopping-style choices by roughly 3 to 15 points; (2) disclosing persuasive intent, which halved an attitude shift in one preregistered study of 1,500 adults; (3) seller-manipulation detectors and rewrite defenses, which cut attack success in self-reported lab tests. Preference elicitation, fiduciary alignment and mechanism design have theory or benchmarks, but almost no measured consumer-facing effects.
Strength: Low to Medium
Most numbers come from single preprints, several self-reported by their authors. Effects hold for the tested models and tasks. Plain AI-identity notices and prompt-only position fixes did not reduce influence in the cases tested. Field or real-market evidence is absent.

## What Exists
### Sub-theme 1: Debiasing agent choices
- **Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)** (authors not verified, 2026, arXiv preprint 2603.17417) — Benchmark (BiasRecBench) with authority, popularity, brand and instruction-style injections. Authority bias cut accuracy up to 38 points. A system-prompt warning raised robustness by about 3.5 to 12 points for GPT-4o. Fine-tuning on 50 debiased examples raised biased accuracy by about 8 to 15 points on two 14B models.
  - Relevance: Direct measured debiasing effects for shopping-like picks, with prompt and training interventions. Text and tables disagree on some numbers.
  - OpenAlex ID: W7138946092
  - Cited by: 0
- **Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models** (Tang et al., 2024, NAACL). Shuffles list order in the prompt and merges the rankings. Abstract reports gains of about 7 to 18% for GPT-3.5 and 8 to 16% for LLaMA-2 70B.
  - Relevance: The standard fix for position bias in ranking. Tested on passage and list ranking, not on shopping.
  - Note: Body-text ranges differ from the abstract. Check the full PDF before quoting per-model numbers.
- **Prompt-Based LLMs for Position Bias-Aware Reranking in Personalized Recommendations** (authors not verified, 2025, arXiv preprint 2505.04948). Shuffling user history reduced position bias. Explicit instructions to reduce bias did not.
  - Relevance: Negative result for prompt-only debiasing of position effects. Read from search summary only.
- **Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations** (authors not verified, 2025, arXiv preprint 2502.01349). Reports that social-proof style cues in product text raise recommendation rates.
  - Relevance: Shows the product-text side of manipulation. Read from search summary only. No debiasing tested.

### Sub-theme 2: Eliciting preferences and delegation
- **Beyond expert users: agents should help users construct preferences, not just elicit them** (Saracay, Schmidt and Guestrin, 2026, arXiv preprint 2606.30863). Proposes CoPref, a model where users build preferences in dialog, and CoShop, a shopping benchmark. No agent exceeds 56% accuracy on CoShop after five turns. One model asks a median of 9 clarifying questions.
  - Relevance: Measures how poorly current shopping agents learn what users want.
  - OpenAlex ID: W7166830829
- **When Agents Shop for You: Role Coherence in AI-Mediated Markets** (Alavi and Nozari, 2026, arXiv preprint 2604.26220). A buyer agent given a consumer profile leaks willingness to pay in its dialog. Sellers recover it almost one-for-one. The authors argue prompts cannot fix this.
  - Relevance: Shows a delegation risk that falls on the consumer. Mitigation not measured.
  - OpenAlex ID: W7158731649
- **A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments** (Cherep, Ma, Xu, Shaked and Maes, 2025, ICLR 2026, arXiv 2509.25609). Runs 17 LLM agents through a web shop in more than 80,000 runs. Agents react more strongly than humans to prices, ratings and nudges.
  - Relevance: Large-scale measurement of agent sensitivity to the cues that sellers control.
  - OpenAlex ID: W4415338268
  - Already in workbench: 01_econ_search_theory.md (listed there with fewer author names). Not counted as new.

### Sub-theme 3: Fiduciary and principal-agent alignment
- **AI Agents and the Law** (authors not verified, 2025, arXiv preprint 2508.08544). Argues that a shopping agent steering a user to a deal-partner product breaches the duty of loyalty. Normative analysis only.
  - Relevance: Frames the loyalty question in agency-law terms. No measured effect.
- **The Fiduciary Illusion: Anticipatory AI, Machine-Targeted Marketing, and the Right to Agency** (Igaya, 2026, SSRN). Legal and conceptual argument about AI agents acting for a principal. Abstract read only.
  - Relevance: Argues fiduciary labels do not stop machine-targeted marketing. No measured effect.
  - OpenAlex ID: W7128051455
- **Governing AI Agents** (authors not verified, 2025, arXiv preprint 2501.07913). Argues agents should serve a plural set of interests, not one principal. Normative.
  - Relevance: Cuts against a strict fiduciary model of agent loyalty.
- **The Shopper Schism: Competing When AI Agents Become Your Customer** (authors not verified, 2026, Berkeley Center for Management Research working paper). Treats agency costs and opaque ranking as the main shopping-agent problem. Policy paper, no experiment.
  - Relevance: Frames market concentration as a risk to consumers. Grey literature.

### Sub-theme 4: Disclosure and labeling of sponsored content
- **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** (Tang, Sun, Curran, Schaub and Shin, 2025, IMWUT). Between-subjects experiment with 179 Prolific users. Even with a "Sponsored" label, 49% did not notice the ad. Labels did not lower trust, but ad conditions raised feelings of manipulation.
  - Relevance: Measures how little a sponsored label is noticed in chatbot answers.
  - OpenAlex ID: W4416926286
  - Cited by: 12
  - Note: The arXiv version (2409.15436) first appeared as "GenAI Advertising: Risks of Personalizing Ads with LLMs".
  - Already in workbench: 03_search_engines_publishers_geo.md. Not counted as new.
- **Toward Meaningful Transparency for AI Chatbots: Disclosing Persuasive Intent Reduces Persuasion** (Rauchfleisch and Jungherr, 2026, arXiv preprint 2608.11794). Preregistered study with 1,500 UK adults. A plain AI-identity notice did not change the attitude shift (13.1 vs 12.6 points in control). Disclosing the chatbot's persuasive instructions cut the shift to 6.3 points.
  - Relevance: The clearest measured disclosure effect. Covers attitudes, not purchases.
- **LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses** (Ai et al., 2026, arXiv preprint 2609.32533). More than 18,000 human judgments of where ads should sit. Sponsorship labels changed placement preferences. Effect size is not in the abstract.
  - Relevance: Shows that labels change what users prefer. Does not measure purchases.
  - OpenAlex ID: W7214791161
- **You probably wouldn't notice if an AI chatbot slipped ads into its responses** (Tang and Shin, 2026). Popular or short-form version of the Tang et al. ads study. Overlap with the 2025 paper is likely but not checked.
  - Relevance: Repeats the recognition finding for a broader audience.
  - OpenAlex ID: W7155522471
- **When AI ads backfire: Deconstructing consumer backlash to GenAI advertising** (Heimstad, Gaustad, Tafesse and Wien, 2026, Journal of Retailing and Consumer Services). Studies why consumers reject GenAI-made ads. Abstract read only.
  - Relevance: Shows backlash can follow disclosure of AI-made ads.
  - OpenAlex ID: W7204147563
- **LLM-Generated Ads: From Personalization Parity to Persuasion Superiority** (Meguellati, Civelli, Han, Bernstein, Sadiq and Demartini, 2025, arXiv preprint 2512.03373). In an 800-person study, AI ads were preferred 59.1% to 40.9% over human ads. Participants who knew the origin penalized AI ads by 21.2 points, post hoc.
  - Relevance: Shows persuasion strength. No labeling condition was tested.
  - OpenAlex ID: W4417028140
- **Designing Dialogic Disclaimers: Principles for Ethical Conversational Design in LLM Interfaces** (authors not verified, 2025). Design principles for disclaimers in chat interfaces. Title read from OpenAlex. Full text not read.
  - Relevance: Possible design guidance for labels. Effect not checked.
  - OpenAlex ID: W4412055639
- **A modular review of the evidence for harmful manipulation by large language models** (Bonnefon and Prunkl, 2026, Current Opinion in Psychology). Reviews evidence on how LLMs can manipulate users. Abstract read only.
  - Relevance: Background on the manipulation risk behind disclosure rules.
  - OpenAlex ID: W7221766882

### Sub-theme 5: Robustness to seller manipulation
- **SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines** (Yu, Jin, Zeng and Wang, 2026, arXiv preprint 2605.21948). Detector for persuasive text that promotes a product. Reports 96.2% of review attacks caught at a 1.2% false positive rate. Results are self-reported and not peer reviewed.
  - Relevance: Direct defense against seller-written manipulation in ranked answers.
  - OpenAlex ID: W7162076847
- **When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization** (Li, Shao, Lin and Guan, 2026, arXiv preprint 2609.02964). The GEO Defender reduces average attack success from 50.32% to 6.20% over seven attacks. It keeps 94.12% of benign evidence use. Self-reported.
  - Relevance: Shows a training-free and a trained defense. Tested against known attacks only.
  - OpenAlex ID: W7208727120
- **Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization** (authors not verified, 2026, arXiv preprint 2609.02316). Off-the-shelf guard models cut attack success by at most 5.7% relative. The authors' simple C-GEO Guard cut it by 47.6% relative with little loss in answer quality.
  - Relevance: Shows standard safety guards are weak against seller manipulation.

### Sub-theme 6: Mechanism and market design
- **Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes** (Xu, Guo and Xiong, 2026, arXiv preprint 2608.11390). Proposes paying content creators for verifiable factual rewrites (VCR). Simulations beat the strongest baseline by about 12.1 points in defense utility. Consumer welfare is not measured.
  - Relevance: Only mechanism proposal in the set with simulated results.
- **Do Matching Mechanisms Work with LLM Agents?** (authors not verified, 2026, arXiv preprint 2606.03030). Asks whether matching-market guarantees hold when LLM agents make the allocation choices. Argues that outcomes need not be stable or efficient. Theory and framing.
  - Relevance: Shows that mechanism guarantees may not carry over to LLM agents.
- **Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms** (Ji, Xu and Feng, 2026, SSRN). Models how LLM platforms choose between ads and subscriptions. Abstract read only.
  - Relevance: Theory of platform revenue choices. Consumer effects depend on details not read.
  - OpenAlex ID: W7223371335
  - Already in workbench: 01_econ_search_theory.md and 03_search_engines_publishers_geo.md (title only there). Not counted as new.

## Reference Chain Discoveries
- Found via: the 2025 "Ads that Talk Back" paper (OpenAlex citers). Surfaced the Tang and Shin 2026 paper, the AI-ads backfire paper, the dialogic disclaimers paper, the modular manipulation review and the fiduciary illusion paper.
- Found via: OpenAlex citers of the "Commercial Persuasion" (Salvi et al., 2026) paper. Returned two 2026 health-chatbot papers, not included.
- Found via: OpenAlex citers of the GEO paper (Aggarwal et al.). Returned a 2026 GEO nomenclature note and a Portuguese replication, not included.
- Found via: related-work search on the Trustable paper (2603.17417). Its related work names Bito et al. (2025) on position bias in recommenders, Wang et al. (2025) on judging bias and Li et al. (2025) on authority bias. Only the 2025 position-bias paper is new here, and its title was not verified.
- Found via: reference lists of the SCI-Defense and Trustable papers. OpenAlex lists no references for either, and the pages have no reference lists.

## What's Missing (Gaps)
- No study measures a fiduciary or loyalty intervention for shopping agents. Legal and normative work only.
- No field or real-market test of disclosure labels on purchases. All disclosure tests are lab or online panels.
- No study compares several debiasing methods on the same shopping task.
- Seller-defense results are self-reported. No independent replication or adaptive-attack test was found.
- No measured effect of preference elicitation on purchase quality for real consumers.

## Contradictions or Tensions
- **Disclosure works or not.** Rauchfleisch and Jungherr (2026) find intent disclosure halves persuasion. Salvi et al. (2026, known) report that a "Sponsored" label plus warning did not undo the steering effect in their main results. The first study tests persuasive intent. The second tests a product label.
- **Prompt warnings.** The Trustable paper finds system-prompt warnings help GPT-4o. The 2025 reranking paper finds explicit bias instructions do not help. The tasks differ, and the models differ.
- **Ranking fixes.** Permutation averaging improves ranking in general (Tang et al., 2024). A 2026 study finds shuffling alone does not fix shopping-agent position effects in some settings, per search snippet only.

## Confidence
Medium-Low
- What would raise confidence: A replication of the intent-disclosure result with purchases as the outcome. An independent test of SCI-Defense or GEO Defender against adaptive attacks.
- What would lower confidence: Independent tests showing the self-reported defense numbers fall on new attack types, or that disclosure effects vanish on purchases.

## Search Log
### Round 1: Broad search
- Queries: debiasing position and brand bias in shopping agents (2026); principal-agent and fiduciary alignment of shopping agents; sponsored-content disclosure in LLM answers; seller-manipulation defenses for generative engines; mechanism design for agent commerce.
- Papers found: about 50 links across five queries; 9 kept as leads.
- Key leads: Trustable paper (2603.17417); SCI-Defense (2605.21948); Ads that Talk Back (2409.15436); AI Agents and the Law (2508.08544); matching mechanisms paper (2606.03030).

### Round 2: Citation traversal
- Papers traversed: SCI-Defense, Trustable paper, Ads that Talk Back. OpenAlex lookups for all three, plus citers of Ads that Talk Back and of the GEO paper.
- New papers from references: None. OpenAlex lists no references for the 2026 arXiv items.
- New papers from citers: GEO Defender (2609.02964), LLM-Generated Ads (2512.03373), AI ads backfire, Monetizing Intelligence, LLMAdBench, fiduciary illusion, Tang and Shin 2026, modular manipulation review, dialogic disclaimers.

### Round 3: Reference section mining
- Papers traversed: Trustable paper (related work), Ads that Talk Back (related work), SCI-Defense (no related work section on the abstract page).
- New papers from references: Bito et al. (2025) position bias in recommenders, cited but not verified. No other new papers.

### Round 4: Gap-filling
- Gaps targeted: preference elicitation, delegation, shopping-agent sensitivity, label effects.
- Queries: clarifying questions and delegation; disclosure in user-aligned assistants; delegation and trust experiments.
- New findings: Beyond expert users (2606.30863), Role Coherence (2604.26220), ABxLab (2509.25609), Commercial Persuasion study 2 check (label effect not retrieved).

### Round 5: Adversarial check
- Gaps targeted: critiques of the sponsored-label result, adaptive attacks on GEO defenses, position-bias mitigation effect sizes.
- Queries: Commercial Persuasion replication and critique; GEO defense limits; permutation mitigation for shopping.
- New findings: Toward Meaningful Transparency (2608.11794), Counter-GEO-Bench (2609.02316), VCR mechanism (2608.11390), Found in the Middle (2310.07712), prompt-based reranking (2505.04948). No critique of the Salvi et al. result found.

### Round 6: Abstract checks
- Papers traversed: Toward Meaningful Transparency, VCR mechanism, Counter-GEO-Bench, LLMAdBench, LLM-Generated Ads, GEO Defender.
- New papers: none beyond those listed above. Permutation effect sizes checked against the ACL abstract.

### Convergence note
- Total unique relevant papers found: 25 listed in this follow-up. Of these, 22 are new and 3 were already in the workbench (ABxLab framework, Ads that Talk Back, Monetizing Intelligence).
- New papers in last round: 0 (round 6 added none), but round 5 added five.
- Stopped because: budget. Six rounds ran, under the eight-round cap. The last search round still surfaced new items, so convergence was not reached.
