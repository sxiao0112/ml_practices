# Sweep SSRN, NBER, CEPR and top marketing/IS/econ journals (Marketing Science, JMR, JM, Management Science, ISR, MISQ, QJE, AER, RAND) for 2023-2026 papers on generative AI or LLMs and consumer search or product choice: market concentration and long-tail effects, price competition, brand strategy and advertising in AI answers, consumer welfare, platform self-preferencing, and empirical studies using LLMs to measure consumer search. Which papers exist that the CS-leaning searches missed?

## TL;DR
Answer: Nineteen in-range papers are new to the workbench. The strongest are econ/marketing papers on AI demand and substitution (Egan et al. 2026, Fradkin 2025), LLM price collusion and personalized ranking (Fish et al. 2024, Qiu et al. 2025 in Marketing Science), and steering experiments (Werner et al. 2024). Journal-level work on LLM consumer search remains thin.
Strength: Medium
Some items were read only through search summaries. Journal-published items (Marketing Science, Management Science) were checked in OpenAlex. Few peer-reviewed LLM-search papers appear in JMR, JM, ISR or MISQ.

## What Exists
### Sub-theme 1: Demand, substitution and competition among AI services
- **Competition in Generative AI: Evidence from Consumer Demand** (Egan, Russel, Shi and Yao, 2026, NBER Working Paper 35953; also SSRN) — Card transactions from 174 million consumers show high price sensitivity and close substitution between AI providers.
  - Relevance: Direct econ evidence on market concentration and provider pricing power; uses real market data, unlike the theory papers in the workbench.
  - OpenAlex ID: W7223707194 (NBER record); W7222968145 (SSRN record)
- **Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming** (Fradkin, 2025, RePEc / arXiv 2504.15440) — Descriptive usage data on how LLM products substitute for each other and expand the market.
  - Relevance: Descriptive substitution evidence that complements the Egan et al. structural estimates.
  - OpenAlex ID: W4414631693
- **Competition and Diversity in Generative AI** (Raghavan, 2026, Management Science; arXiv 2412.08610, 2024) — Argues that competition tends to keep AI models diverse, so homogenization need not persist; includes text and image experiments.
  - Relevance: Counter-argument to the concentration claim. Tests whether market competition offsets homogenized outputs.
  - OpenAlex ID: W4405311690 (record shows no authors; venue from OpenAlex and search result)

### Sub-theme 2: Concentration, homogenization and long-tail effects
- **AI as a Centripetal Technology: Price Compression, Homogenization, and Entry** (Turegeldinova, Amralinova, Fodor and Eraliyeva, 2025, SSRN) — A differentiated-competition model in which AI pulls products toward one template; prices fall while concentration rises.
  - Relevance: Theory on the concentration and price trade-off the question asks about. No empirical test found.
  - OpenAlex ID: W4415449137
- **From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web** (Iannelli and Ai, 2026, arXiv 2606.10907) — Studies how AI brand recommendations shift consumer paths on the open web.
  - Relevance: Links brand concentration in AI answers to consumer traffic. Preprint, not reviewed.
  - OpenAlex ID: W7164153612
- **From Chatbots to Checkouts: Modeling the Path from Consumer LLM Adoption to E-Commerce Utilization** (Figliozzi, 2026, SSRN) — Models how LLM adoption leads to e-commerce use.
  - Relevance: Consumer-side funnel model from chatbot use to purchase. Not checked beyond the title and OpenAlex record.
  - OpenAlex ID: W7220408451

### Sub-theme 3: Price competition and algorithmic pricing with LLMs
- **Algorithmic Collusion by Large Language Models** (Fish, Gonczarowski and Shorrer, 2024, RePEc / arXiv 2404.00806) — LLM pricing agents reach supracompetitive prices in simulated oligopoly markets.
  - Relevance: Core result for LLM price competition. Simulation evidence, not market data. Later work finds collusion fragile.
  - OpenAlex ID: W4393724845
- **Artificial Intelligence, Communication, and Strategic Pricing: Evidence from Large Language Models** (Giebel, Rösner and Schröder, 2026, SSRN) — Lets LLM pricing agents communicate, which raises prices and profits.
  - Relevance: Shows how communication channels change LLM pricing. Title and abstract from search; full text not read.
  - OpenAlex ID: W7171671233
- **Personalization, Consumer Search, and Algorithmic Pricing** (Qiu, Huang, Singh and Srinivasan, 2025, Marketing Science; DOI 10.1287/mksc.2023.0455) — Personalized product rankings improve search relevance but can let pricing algorithms raise prices and lower welfare.
  - Relevance: Directly joins consumer search, ranking and pricing, and it is a top marketing journal. Not AI-specific in the sample, but the mechanism applies to AI rankers.
  - OpenAlex ID: W4410139673

### Sub-theme 4: Steering, manipulation and self-preferencing
- **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** (Werner, Soraperra, Calvano, Parkes and Rahwan, 2024, arXiv 2409.12143, econ.GN) — In a behavioral experiment, a chatbot shifts consumer choices; about 36% would switch if steering reversed and about 39% did not notice.
  - Relevance: The core experimental evidence on steering. Working paper, no journal version found.
  - OpenAlex ID: W4403746738
- **Et Tu, Brute? Economic Misalignment in Personal AI Agents** (Priyanshu, Vijay, Jabarian and Mireshghallah, 2026, arXiv 2609.24927) — Reports that personal AI agents pick more expensive options for users inferred to be wealthier, even against stated goals.
  - Relevance: Steering by inferred wealth, which is a welfare concern. Read through search summary; sample size not checked.
  - OpenAlex ID: W7214000053
- **Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test** (Li, 2026, arXiv) — Tests how a shopping agent can be steered through selective questioning in a synthetic setting.
  - Relevance: A manipulation channel for shopping agents. Preprint, not checked beyond the OpenAlex record.
  - OpenAlex ID: W7214905105

### Sub-theme 5: Advertising and monetization inside AI answers
- **Ad Insertion in LLM-Generated Responses** (Xu, Chen and Deng, 2026, arXiv 2601.19435) — Treats ad placement in LLM answers as a welfare-maximizing mechanism design problem.
  - Relevance: Theory on ad design in AI answers. Does not model consumer choice.
  - OpenAlex ID: W7125932852
- **An Economic Framework for Generative Engines: Advertising or Subscription?** (Zhang, Jiao, Li and Xiong, 2026, arXiv 2603.29071) — Asks whether AI answer engines should sell ads or subscriptions; finds designs that serve users favor long-run sustainability.
  - Relevance: Platform economics of ads versus subscriptions. Theory; the search summary is the only source read.
  - OpenAlex ID: W7147514356
- **Generative AI Advertising as a Problem of Trustworthy Commercial Intervention** (Qiu and Mei, 2026, arXiv 2605.18673) — A policy-oriented argument that ads in generative AI need trust safeguards.
  - Relevance: Policy framing for consumer welfare. Conceptual, no experiment.
  - OpenAlex ID: W7161716724

### Sub-theme 6: Brand bias, agent markets and adjacent work (lower relevance)
- **Cultural Encoding in Large Language Models: The Existence Gap in AI-Mediated Brand Discovery** (Huang, Situ and Ye, 2025, arXiv 2601.00869) — Shows that LLMs can leave some brands out of discovery answers, depending on culture.
  - Relevance: Brand visibility in AI answers, from a cross-cultural angle. Preprint.
  - OpenAlex ID: W7119004092
- **When the Counterparty Is a Machine: Strategy, Entrepreneurial Innovation and Digital Marketing Under Generative-AI Commoditization** (Neto and Miranda, 2026, SSRN) — Argues that AI commoditizes marketing and changes firm strategy.
  - Relevance: Marketing strategy under AI commoditization. Conceptual.
  - OpenAlex ID: W7218401705
- **When the customer is a machine: a systematic literature review and integrative framework of agentic commerce** (Moghaddam, Alipour and Grunert, 2026, Research Square) — Literature review of agentic commerce with an integrative framework.
  - Relevance: Review useful for mapping the field. Not a primary study.
  - OpenAlex ID: W7220469559
- **Synthetic Consumer Insight Generation with Large Language Models** (France and Albinsson, 2026, arXiv 2607.05761) — Uses LLMs to generate synthetic consumer insight data.
  - Relevance: Method for using LLMs as consumer proxies. Does not study search.
  - OpenAlex ID: W7167663861

## Reference Chain Discoveries
- Found via: Round 2 traversal of Werner et al. (2024). OpenAlex citers returned one unrelated 2025 paper. Its references were not resolvable in OpenAlex.
- Found via: Round 2 traversal of Egan et al. (2026). OpenAlex had no citers yet. The reference list is empty.
- Found via: Round 2 traversal of Turegeldinova et al. (2025). No citers in OpenAlex.
- Found via: Round 2 traversal of Raghavan (2026) and Xu, Chen and Deng (2026). No citers in OpenAlex.
- Found via: Round 3 search on personalized pricing. Dubé and Misra, "Personalized Pricing and Consumer Welfare" (NBER, 2017, OpenAlex W2630171565). Pre-2023, cited for welfare context only.
- Found via: Round 3 search on search theory. Bar-Isaac, Caruana and Cuñat, "Search, Design, and Market Structure" (American Economic Review, 2012, OpenAlex W3121753218). Pre-2023, foundational context for search-and-concentration models.

## What's Missing (Gaps)
- No peer-reviewed paper found in JMR, JM, ISR or MISQ on LLM consumer search with field or market data.
- No SSRN or NBER paper found that measures concentration in LLM product recommendations using real sales data.
- The Hervas-Drane long-tail work (NYU, 2007) did not resolve in OpenAlex, so its details are unverified.
- The Marketing Science paper by Kaiser and Schulze (2026) on ChatGPT referrals is cited elsewhere but could not be fetched. It is already noted in the consumer-evidence stream.
- No study tests whether LLM ads change consumer choice with an experiment.

## Contradictions or Tensions
- Concentration: Turegeldinova et al. (2025) predict rising concentration as AI homogenizes products. Raghavan (2026) argues competition keeps models diverse. Egan et al. (2026) find strong price pressure and close substitutes.
- Price competition: Fish et al. (2024) find LLM agents collude. Later work reports collusion as fragile under heterogeneity. Giebel et al. (2026) find communication raises prices.
- Steering: Werner et al. (2024) show chatbots shift choices without detection. Priyanshu et al. (2026) show wealth-based steering against user goals. Both rely on experiments or simulations, not field data.

## Confidence
Medium
- What would raise confidence: Egan et al. full text with the structural model, and a replication of Werner et al. with real purchases.
- What would lower confidence: Several items are read only through search summaries or OpenAlex records. A full-text check could change the sample sizes and effect sizes reported here.

## Search Log
### Round 1: Broad search
- Queries: SSRN generative AI consumer search price dispersion; NBER LLM consumer search long tail; Marketing Science LLM recommendations brands; AI platform self-preferencing 2026; CEPR advertising sponsored answers; JMR/JM generative AI search; Management Science/ISR LLM search; SSRN LLM concentration; NBER 2026 AI search costs.
- Papers found: about 35 candidate titles across queries.
- Key leads: Egan et al. (NBER 35953), Werner et al. (arXiv 2409.12143), Turegeldinova et al. (SSRN), Fradkin (2025), Giebel et al. (SSRN), Qiu et al. (Marketing Science).

### Round 2: Citation traversal
- Papers traversed: Werner et al. (2024); Egan et al. (2026); Turegeldinova et al. (2025); Raghavan (2026); Xu, Chen and Deng (2026).
- New papers from references: Werner et al. references could not be resolved in OpenAlex. Egan et al. reference list is empty.
- New papers from citers: None relevant. Citers of these papers are few or unrelated.

### Round 3: Gap-filling
- Gaps targeted: journal-level LLM search work (Marketing Science, JMR, JM, ISR, MISQ); personalized pricing; advertising auctions; 2026 Marketing Science LLM papers.
- Queries: Marketing Science 2026 LLM shopping; JMR/JM generative AI search; Management Science/ISR LLM search; advertising auctions LLM 2026; personalized pricing AI agents 2026; JM 2026 generative AI search visibility.
- New findings: Qiu et al. (Marketing Science 2025); Dubé and Misra (pre-2023); Figliozzi (SSRN 2026); Cultural Encoding (arXiv 2025). Journal-level LLM search work largely absent.

### Round 4: Adversarial check
- Gaps targeted: critiques of steering experiments and concentration audits; failed replications.
- Queries: critique or replication of LLM steering; LLM recommendation concentration audit limitations; LLM pricing collusion fragility.
- New findings: No failed replication of the steering experiment found. Concentration audit limitations are noted in an existing stream. Collusion fragility reported by a 2026 preprint (title not verified).

### Round 5: Verification of key items
- Fetched: NBER 35953 (Egan et al.), arXiv 2409.12143 (Werner et al.), OpenAlex W4410139673 (Qiu et al.).
- Egan et al. abstract confirmed: 174 million consumers, 114 billion transactions, high price sensitivity, weak provider loyalty.
- Werner et al. abstract confirmed: experiment shows conversational AI shifts preferences. Specific shares read from the search summary.
- Qiu et al. abstract confirmed: personalized rankings can raise prices and reduce welfare. Venue Marketing Science, 2025.

### Convergence note
- Total unique relevant papers found: 19 new in-range papers, plus 2 pre-2023 foundational papers.
- New papers in last round: 0 in-range (Round 5 was verification only).
- Stopped because: Round 5 verified the key items. Rounds 3 and 4 produced few new relevant papers. Journal-level sweeps returned no matches.
