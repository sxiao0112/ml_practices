# What does marketing and CS research find about which brands and products LLMs recommend to consumers: brand bias and popularity/incumbent bias, consistency of recommendations, sensitivity to prompt wording and consumer persona, vulnerability to manipulation (strategic text, prompt injection on product pages, fake reviews), sponsored or persuasive content in LLM answers, and implications for brand strategy and consumer trust?

## TL;DR
Answer: LLM product recommendations show strong concentration on a few incumbent brands in controlled audits, and popularity alone explains little of it. Recommendations shift with consumer persona, and single answers vary run to run. Strategic text in product pages can raise a product's recommendation rate, with the largest effects in attack-style tests and weaker effects once defenses or competition are added.
Strength: Medium
Most evidence is from 2024-2026 arXiv preprints, many read only at abstract level. Results depend on model, category and prompt design. No peer-reviewed study tests how consumers react to sponsored LLM answers, and no SSRN or NBER paper on this topic was found.

## What Exists
### Sub-theme 1: Brand bias, incumbent advantage and competition
- **Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems** (Chu and Hou, 2026, arXiv preprint 2606.17443) — In skincare tests with equal specs, well-known brands were recommended in all trials across three commercial LLMs. A competitor needed a rating edge of about 0.1 stars to break this.
  - Relevance: Direct evidence of incumbent bias and of how small consumer-facing advantages and authority-style claims shift it.
  - OpenAlex ID: W7164990044 (cited by 0 at lookup)
- **"Global is Good, Local is Bad?": Understanding Brand Bias in LLMs** (Kamruzzaman, Nguyen and Kim, 2024, EMNLP) — LLMs link global brands with positive attributes and recommend luxury gifts more to high-income countries. Local-brand preference appears only in some contexts.
  - Relevance: Shows brand bias along geography and origin, not only popularity.
  - OpenAlex ID: W4404792957 (cited by 4)
- **Auditing Preferences for Brands and Cultures in LLMs** (Rienecker, Mpofu, Goel, Datta, Zhao, Danielsson and Thorsen, 2026, arXiv preprint 2603.18300) — Gemini and GPT favored American entities across 10 topics and over 2,000 questions. DeepSeek showed weaker but still detectable geographic preference.
  - Relevance: Adds a persona-based design (ChoiceEval) and an economic-intermediary framing that matches the consumer question.
  - OpenAlex ID: not looked up. Read from search snippet only.
- **Who Owns the AI Recommendation? A Multi-Industry Empirical Map of Brand Category Ownership Across Large Language Models** (Żatuchin, 2026, Journal of Marketing Analytics, arXiv 2606.23057) — Across 50 brands in five industries and three models, mean Gini was 0.30. At least one brand appeared in 80% or more of answers for 204 of 250 queries.
  - Relevance: Quantifies how concentrated LLM brand choice is inside each category. Concentration is moderate in the Gini sense, but top-brand dominance is common.
  - OpenAlex ID: not looked up. Version 2 uses a corrected February analysis and a September replication (Spearman 0.994 across the two waves).
- **An Empirical Audit of LLM Product Recommendations** (Boffa, Farronato, Fedele, Levi and Mantovani, 2026, NET Institute Working Paper 26-09) — Across six LLMs and 100 categories, one product is listed first in more than three quarters of responses in 20 categories. Some models favor products from their own provider.
  - Relevance: Broadest multi-model audit found. Shows self-preferencing as a possible bias source.
  - OpenAlex ID: not looked up. Read from the working paper page.
- **Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations** (Malthouse, Lee, Yang, Pal and Feng, 2026, arXiv preprint 2609.16304) — Six LLMs in five categories often omit established brands. Prominence tracks search interest and online brand talk more than classic popularity.
  - Relevance: Argues that popularity is the wrong proxy and that marketplace visibility signals matter more.
  - OpenAlex ID: not looked up.
- **Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit** (Jack, Lehman, Maloney and Xu, 2026, arXiv preprint 2605.27439) — Across 533 brands in five prominence tiers, category leaders win 25 to 41% of the slots they reach. Specialist and regional brands never appear in 48 to 52% of runs.
  - Relevance: Gives tier-level numbers for how brand prominence maps to visibility.
  - OpenAlex ID: not looked up. Read from the abstract page.

### Sub-theme 2: Popularity bias
- **Large Language Models as Recommender Systems: A Study of Popularity Bias** (Lichtenberg, Buchholz and Schwöbel, 2024, Gen-IR workshop at SIGIR, arXiv 2406.01285) — On movie recommendation, an LLM recommender shows less popularity bias than traditional systems, even with no mitigation.
  - Relevance: The main counterpoint to the incumbent-bias papers. Domain is movies, not consumer products.
  - OpenAlex ID: not looked up. The abstract gives no effect sizes.
- **Exploring Diversity, Novelty, and Popularity Bias in ChatGPT's Recommendations** (Di Palma, Biancofiore, Anelli, Narducci and Di Noia, 2026, arXiv preprint 2601.01997) — Studies popularity bias in ChatGPT-3.5 and ChatGPT-4 across three datasets. The abstract reports no direction for the bias.
  - Relevance: Low. Confirms that popularity bias is measured but does not settle the question.
  - OpenAlex ID: not looked up.

### Sub-theme 3: Consistency and sensitivity to persona and wording
- **Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit** (Jack, Lehman, Maloney and Xu, 2026, arXiv preprint 2605.30207) — Adding a persona to the user message lowers recommendation-set overlap by 0.12 to 0.20 Jaccard. Category leaders stay about 80% consistent, while mid-market brands change by up to 75%.
  - Relevance: Most direct evidence on consumer persona sensitivity. Design: 2,000 runs, 10 personas, 8 prompts, 3 configurations.
  - OpenAlex ID: not looked up. The Anthropic cell has only four prompts, so its interval is wide.
- **The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing of Large Language Model Brand Recommendations** (Żatuchin, 2026, arXiv preprint 2609.04047) — Reanalyzes five audits (about 190,000 observations) and splits variance across sampling, prompt phrasing, run and model version. Version 2 says reliability depends on the question, so no fixed number of runs is advised.
  - Relevance: Shows that one answer is an unreliable measure of a brand's position.
  - OpenAlex ID: not looked up. Read from search snippets and a secondary summary.
- **Evaluating Position Bias in Large Language Model Recommendations** (authors not verified, 2025, arXiv preprint 2508.02020) — Candidate order alone changes LLM rankings. The paper proposes a prompting fix called RISE.
  - Relevance: Shows order sensitivity, a related consumer-facing effect. This paper is mainly a computer-science recommender result.
  - OpenAlex ID: not looked up. Read from search snippet only.

### Sub-theme 4: Manipulation of recommendations through strategic text and optimization
- **Manipulating Large Language Models to Increase Product Visibility** (Kumar and Lakkaraju, 2024, arXiv preprint 2404.07981) — Adding an optimized text sequence to a product page raised its rank in LLM recommendations. Tests used fictitious coffee machines, and the sequence was optimized with GCG.
  - Relevance: The origin paper for strategic-text manipulation of LLM product rankings. The evidence comes from a small, fictitious catalog.
  - OpenAlex ID: W4394782281 (cited by 2)
- **GEO: Generative Engine Optimization** (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan and Deshpande, 2023, KDD 2024, arXiv 2311.09735) — Nine content-rewrite methods raise a source's visibility in generative engine answers by up to 40%. Effects depend on the query domain.
  - Relevance: Defines the GEO framing. Its engines (2023 to 2024) may not match current systems.
  - OpenAlex ID: not looked up. Read from search snippets and an abstract summary.
- **E-GEO: A Testbed for Generative Engine Optimization in E-Commerce** (Bagga, Farias, Korkotashvili, Peng and Wu, 2025, arXiv preprint 2511.20867) — Builds 13,747 consumer queries, each with 10 Amazon listings. Authors report that under a simple in-prompt clause, optimization gains reflect real content improvement rather than manipulation.
  - Relevance: Largest e-commerce GEO testbed found. Defense result is reported in the abstract only.
  - OpenAlex ID: not looked up.
- **SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents** (Wen, Liu, Liu, Jiao, Yang, Wu and Tang, 2026, arXiv preprint 2606.28356) — Across 600 recommendation cases, GEO attacks raise the rate at which a flawed target enters the recommendation set by up to 83.2 points. Simple agent-side defenses cut this by up to 39.2 points but do not restore the no-attack level.
  - Relevance: Strongest evidence that defenses are incomplete. Model list not given in the abstract.
  - OpenAlex ID: not looked up.
- **Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents** (Wang, Li, Wu, Chen, Liu, Fok, Chen, Thing, Li, Tao and Zhang, 2026, arXiv preprint 2606.13385) — The StakeBench suite has 264 attack cases across 12 shopping categories and 3,168 attacked runs. The authors report that no attack objective is reliably resisted by current web agents.
  - Relevance: Covers prompt injection on shopping pages and visual cues such as fake badges. Abstract gives no per-attack success rates.
  - OpenAlex ID: not looked up.
- **LLM Whisperer: An Inconspicuous Attack to Bias LLM Responses** (Lin, Gerchanovsky, Akgul, Bauer, Fredrikson and Wang, 2025, CHI 2025, arXiv 2406.04755) — Swapping synonyms in a user's prompt raised the chance that the LLM mentions a target brand's concept by up to 78.3 points. A user study checks whether users notice.
  - Relevance: Shows wording-based manipulation that users may not notice. Earlier arXiv title was "Sales Whisperer."
  - OpenAlex ID: W4409735455 (cited by 10)

## Reference Chain Discoveries
Papers found through citation traversal or fetched pages, not in the first web searches:
- Found via: OpenAlex citers of Kumar and Lakkaraju (W4394782281), which returned no relevant 2024-2026 work beyond the two listed.
- Found via: OpenAlex citers of "Global is Good, Local is Bad?" (W4404792957), which returned LLM Whisperer (W4409735455) and "The synthesised consideration set" (W7225003177, 2026, not read).
- Found via: arXiv "Who Owns" paper context, which pointed to Dice Roll (2609.04047) and its companion arXiv 2609.05059 (title and findings not verified).
- Found via: Round 4 searches on fake reviews. Snippet-level leads only, authors not verified: "Ghostwriters of the Marketplace" (ICWSM 2026, 78k machine-written reviews); FraudSquad (arXiv 2510.01801); a Frankfurt 2026 thesis on German reviews.
- Found via: Round 4 search on prompt injection. Snippet-level leads only: arXiv 2603.15714 (public agent competition with a hidden developer note on a product page, which the agent ignored); arXiv 2509.25926 (type-directed privilege separation against review-based injection in WebShop).
- Found via: Round 4 search on sponsored answers. Snippet-level lead, authors not named: an experiment on AI sales assistants that found sponsorship disclosure lowers perceived integrity only in low-interactivity conditions.
- Found via: Round 4 search on sponsored ads. Adjacent, cross-stream: Reisenbichler, Reutterer and Schweidel, "Applying Large Language Models to Sponsored Search Advertising" (Marketing Science, 2026, snippet only). Shin et al. on targeted ads as implicit recommendations (theory, not LLM).
- Found via: Round 4 search on sponsored disclosure. Survey and vendor claims, not peer-reviewed: about 61% of consumers say they would trust a sponsored chatbot recommendation less. No source given.
- Found via: Round 5 search on position bias in brand matchups. Vendor study (Opascope, October 2026): first-named brand gets 54.7% of votes in 482 matchups. Not peer-reviewed.

## What's Missing (Gaps)
- No peer-reviewed or SSRN/NBER economics paper measures how consumers respond to labeled versus unlabeled sponsored LLM answers. The closest result is one retail-assistant experiment seen only in a snippet.
- No replication or independent critique of Kumar and Lakkaraju (2024) was found. The original result rests on fictitious coffee machines.
- Prompt wording, apart from persona, has no controlled study of brand recommendations in shopping assistants. The closest work is candidate-order bias and synonym-swap attacks.
- No study links an LLM's brand recommendations to actual purchases or market shares. All evidence stops at recommendation output.
- No study tests whether fake LLM-written reviews change LLM brand recommendations. Detection work exists, but its effect on the recommender is not measured.
- Few studies cover the same question across languages or markets. The Rienecker et al. and Kamruzzaman et al. papers are the exceptions.

## Contradictions or Tensions
- **Popularity bias.** Lichtenberg et al. (2024) find less popularity bias in an LLM movie recommender than in traditional ones. Malthouse et al. (2026), Jack et al. (2026) and Żatuchin (2026) find top brands dominate consumer product answers. The domains differ, and the measures differ too.
- **How much manipulation works.** Kumar and Lakkaraju (2024) and SafeGEO (2026) report large rank or inclusion gains from text optimization. E-GEO (2025) reports that a simple in-prompt clause makes gains look like real content improvement. SafeGEO reports defenses that still leave residual harm.
- **Incumbent advantage under competition.** Chu and Hou (2026) find a near-total incumbent monopoly with equal specs. The same paper finds that a small rating edge or authority-style claims break it. Jack et al. (2026) find leaders keep about 80% consistency across personas. Both can hold at once, since one result uses controlled specs and the other uses real retrieval.
- **Stability of answers.** Żatuchin (2026) reports high agreement on aggregate brand share across two waves (Spearman 0.994). The Dice Roll paper (2026) warns that a single answer is unreliable for any one question. These describe different units, aggregate shares versus single queries.
- **Version differences.** Żatuchin's "Who Owns" paper reports a mean Gini of 0.28 in one version and 0.30 in a later one. Use version 2.

## Confidence
Medium
- What would raise confidence: A replication of Kumar and Lakkaraju (2024) with real catalogs and current models, plus full-text checks of the Jack et al. (2026) and Chu and Hou (2026) papers.
- What would lower confidence: Evidence that persona and wording effects vanish once retrieval is fixed. Evidence that popularity bias is absent in consumer categories once brand awareness is controlled.
- Most evidence comes from arXiv preprints, many read only at abstract level. Several vendor and secondary sources are not used for claims.

## Search Log
### Round 1: Broad search
- Queries: "brand bias LLM product recommendations popularity incumbent bias arXiv 2025"; "generative engine optimization manipulation product recommendations LLM strategic text injection"; "LLM shopping assistant recommendations consistency prompt wording persona sensitivity study"; "marketing research ChatGPT brand recommendations SSRN NBER sponsored content LLM answers"; "prompt injection product page LLM agent shopping manipulation fake reviews study"
- Papers found: about 15 candidate results across five queries
- Key leads: Incumbent Advantage (2606.17443); "Global is Good" (2406.13997); E-GEO (2511.20867); Persona Conditioning (2605.30207); StakeBench (2606.13385)

### Round 2: Citation traversal
- Papers traversed: Kumar and Lakkaraju (2024) (OpenAlex W4394782281); "Global is Good" (OpenAlex W4404792957); Incumbent Advantage (OpenAlex W7164990044)
- New papers from references: None. OpenAlex returned empty reference lists for all three arXiv-linked records.
- New papers from citers: LLM Whisperer (W4409735455); "The synthesised consideration set" (W7225003177); "Auditing Preferences for Brands and Cultures" (W7139958388, found in OpenAlex, not read); "How Language Models Learn Taste" (W7223131426, not read).

### Round 3: Reference section mining (abstract pages used in place of full texts)
- Papers mined: Kumar and Lakkaraju (2024); Chu and Hou (2026); Kamruzzaman et al. (2024); Jack et al. persona (2026); Jack et al. 37,000-run audit (2026); E-GEO (2025); SafeGEO (2026); Malthouse et al. (2026)
- New papers from references: GEO (Aggarwal et al., 2023, KDD 2024) via search. Related work sections not available on abstract pages.
- New papers from citers: None beyond round 2.

### Round 4: Gap-filling
- Gaps targeted: sponsored LLM answers and consumer trust; fake reviews and LLM recommendations; consumer welfare; brand consistency across repeats; SSRN and NBER coverage.
- Queries: "LLM advertising sponsored recommendations conversational search consumer welfare economics paper 2026"; "LLM generated fake reviews consumer detection or manipulation product ratings study 2025 2026"; "consumer trust disclosure sponsored AI chatbot answers experiment labeled ads perceived trust"; "synthesised consideration set brand inclusion concentration large language model recommendations five industries"; "LLM recommendation brand position order bias ranking sensitivity to query paraphrase marketing journal"
- New findings: "Who Owns the AI Recommendation" (2606.23057); position bias studies (2508.02020); fake-review detection leads (snippet only); no SSRN or NBER LLM brand paper found.

### Round 5: Adversarial check
- Gaps targeted: critiques or replications of the main findings; counterpoints on popularity bias.
- Queries: "Kumar Lakkaraju strategic text sequence critique limitations product recommendation manipulation replication"; "LLM recommendation bias popularity long tail niche brands audit critique popularity bias LLM recommender 2026"; "LLM Whisperer inconspicuous attack bias LLM responses CHI 2025 brand product recommendation"
- New findings: No replication or critique of Kumar and Lakkaraju found. Lichtenberg et al. (2024) gives the counterpoint on popularity bias. Boffa et al. (2026) added as a multi-model audit. Di Palma et al. (2026) checked and found to report no direction.

### Round 6: Convergence check
- Gaps targeted: SSRN and firm-strategy work; repeated-query consistency; persona-consistency and cross-cultural preference audits.
- Queries: "SSRN working paper generative AI search brand visibility LLM recommendations firms strategy 2026"; "LLM product recommendation repeated queries variance consistency brands across runs arXiv 2026 audit"; "Auditing Preferences for Brands and Cultures in LLMs"
- New papers: Dice Roll Method (2609.04047); Auditing Preferences for Brands and Cultures (2603.18300); "Generative Engine Optimization at Scale" (Kumar, 2026, title only, not read). The SSRN query returned no SSRN paper.

### Convergence note
- Total unique relevant papers found: 17 (13 read at abstract level, 4 seen only in search snippets)
- New papers in last round: 2 (Dice Roll and the cross-cultural audit)
- Stopped because: Rounds 4 to 6 each still added papers, so the stopping rule was not met. I stopped after Round 6 by judgment. Later searches returned mostly vendor blogs, and the sub-questions on wording effects and sponsored-answer trust remain without direct evidence. The 8-round cap was not reached.
