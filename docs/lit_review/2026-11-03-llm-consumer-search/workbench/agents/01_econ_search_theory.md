# What does economics (theory and empirics) say about how LLMs and AI assistants change consumer search costs, and the downstream effects on price dispersion, competition, market concentration, product variety, and consumer welfare? Include search-cost models (sequential/ordered search, Diamond paradox), delegated search to AI intermediaries, 'algorithmic consumers', steering/self-preferencing by AI intermediaries, and policy/antitrust analysis of AI assistants as gatekeepers.

## TL;DR
Answer: Economics has two thin layers. Theory papers (2026) model AI agents as cheaper Weitzman-style searchers and find cheaper search helps buyers, but more informative search can weaken seller competition. Older shopbot and Diamond-paradox work supplies the baseline. Empirical LLM-specific price-dispersion and concentration evidence is nearly absent. Steering and self-preferencing by AI intermediaries is argued in policy and law commentary and shown in consumer-choice experiments outside economics.
Verdict: omit (not a yes/no question)
Strength: Low
Conditions: Holds for stylized theory models with exogenous prices. Endogenous-price results are one model and one symmetric-market case. No peer-reviewed LLM-specific econ paper was found.

## What Exists

### Sub-theme 1: Classic search-cost and price-dispersion theory (baseline)
- **Persuasion Produces the (Diamond) Paradox** (Whitmeyer, 2020, arXiv preprint) — Shows information provision can restore the Diamond result that tiny search costs push prices to monopoly levels.
  - Relevance: Direct link to the Diamond paradox the question names. Adds product differentiation and imperfect information.
  - OpenAlex ID: W3107395031. Cited by: 3
- **Attraction versus Persuasion: Information Provision in Search Markets** (Au and Whitmeyer, 2022, Journal of Political Economy) — Title and metadata only; content not read. Topic inferred from title: information provision in search markets.
  - Relevance: Peer-reviewed extension of the same Diamond-type setting; shows firm incentives to inform.
  - OpenAlex ID: W4281382114. Cited by: 18
- **Competitive information disclosure in random search markets** (He and Li, 2023, Games and Economic Behavior) — Title and metadata only; content not read. Topic inferred from title.
  - Relevance: Shows disclosure choices depend on the search protocol, which matters if AI assistants change it.
  - OpenAlex ID: W3203112927. Cited by: 5
- **Persuaded Choice in Ordered Search** (Sato and Shirakawa, 2023, SSRN) — Title and metadata only; content not read. Topic inferred from title.
  - Relevance: Ordered (sequential) search is the protocol Weitzman-type AI agents follow.
  - OpenAlex ID: W4381955221. Cited by: 1
- **Limits of Disclosure in Search Markets** (Boleslavsky and Krasteva, 2025, SSRN) — Title and metadata only; content not read. Topic inferred from title.
  - Relevance: Recent counterpoint to the view that more information always helps buyers.
  - OpenAlex ID: W4410795904. Cited by: 0
- **Frictionless Commerce? A Comparison of Internet and Conventional Retailers** (Brynjolfsson and Smith, 2000, Management Science) — Compares online and offline prices; finds online prices 9-16% lower but dispersion still large among online sellers, with brand effects.
  - Relevance: Pre-LLM empirical benchmark for how lower search costs change prices and dispersion.
  - OpenAlex ID: W2154555821. Cited by: 2498
- **Shopbot Economics** (Kephart and Greenwald, 2002, Autonomous Agents and Multi-Agent Systems) — Models shopbots that compare prices for consumers and shows shopbots can price their own information.
  - Relevance: Early model of software agents as search intermediaries. Shopbots are the closest pre-LLM analogue to AI shopping assistants.
  - OpenAlex ID: W2914520853. Cited by: 79
- **The impact of shopbot use on prices and price dispersion: Evidence from online book retailing** (Tang, Smith and Montgomery, 2010, International Journal of Industrial Organization) — Empirical study of shopbot use and retail prices for books.
  - Relevance: The main empirical precedent for agent-driven search changing price dispersion. Found through citation traversal.
  - OpenAlex ID: W2115894736. Cited by: 87

### Sub-theme 2: Sequential and ordered search with delegated agents (2026 theory)
- **Agentic Markets: Equilibrium Effects of Improving Consumer Search** (Lucier, Immorlica, Mobius, Slivkins, Goldstein, Hofman, Jaffe and Rothschild, 2026, arXiv preprint 2603.25893) — Models consumers who pay to search for fit signals. Cheaper search raises consumer surplus. More informative search can lower it when the market learns less than consumers.
  - Relevance: Closest match to the question. Frames AI-assisted search as a Weitzman optimal-stopping problem. Endogenous-price result: more informative search can weaken competition.
  - Relevance on method: Purely theoretical. No empirical data. Consumers are Bayesian and follow Weitzman's index policy.
  - OpenAlex ID: W7143291850. Cited by: 0
- **From Product Search to Preference Articulation: The Economics of Agentic Commerce** (Dong, Luo and Xu, 2026, SSRN / arXiv 2608.08395) — Compares manual and agentic search when preferences are complex. Manual search fails beyond a complexity threshold. Agentic search keeps platform revenue positive.
  - Relevance: Directly models AI intermediaries and platform incentives. Predicts an adoption lag and an inverted fidelity allocation.
  - Relevance on method: Theory only. Abstract read; full text not read.
  - OpenAlex ID: W7201875729. Cited by: 0
- **The Evolution of Digital Search: From Blue Links to Delegated Decision-Making** (Rothschild, Immorlica, Lucier and Möbius, 2026, arXiv preprint 2607.21459) — Argues search moves from user-driven discovery to agent-mediated decisions. Discusses efficiency, competition and welfare.
  - Relevance: Framing paper for delegated search. Position piece rather than a model.
  - Relevance on method: Read from search snippet only.
  - OpenAlex ID: W7170434023. Cited by: 0
- **Delegation Rights: Property, Agency, and Investment Incentives in the Age of AI Agents** (authors not verified, 2026, arXiv preprint 2606.31935) — Welfare model with an AI-assisted commerce counterfactual.
  - Relevance: Illustrative model on delegation and property rights.
  - Relevance on method: Found in search results only. Authors and full text not verified.
  - OpenAlex ID: not checked.
- **Strategic Buying Agents** (Fu and Hu, 2026, arXiv preprint 2607.04708) — Theory of buyers who choose when to buy, tested on Amazon price histories. Finds language models are better at picking among pricing regimes than at buy-or-wait decisions.
  - Relevance: Shows LLM buyers do not reliably learn optimal stopping in price data. Stream-adjacent (delegated shoppers).
  - OpenAlex ID: W7167620503. Cited by: 0

### Sub-theme 3: Intermediary steering, recommendations and self-preferencing (theory)
- **Buyer-Optimal Algorithmic Recommendations** (Ichihashi and Smolin, 2025, ACM Conference on Economics and Computation, arXiv 2309.12122; earlier version 'Buyer-Optimal Algorithmic Consumption', 2023, SSRN) — A recommender that serves buyers skips high-price products. This raises buyer price sensitivity and pushes sellers to lower prices.
  - Relevance: Shows a buyer-side intermediary can lower prices by biasing recommendations. Also shows revealing buyer value leaves total payoffs unchanged.
  - OpenAlex IDs: W4411946093 (2025, ACM EC version); W4387732092 (2023, SSRN version). Cited by: 3 (SSRN version)
- **Vertical tacit collusion in AI-mediated markets** (Affonso, 2026, arXiv preprint 2601.03061) — Argues AI shopping agents and sellers can reach collusion-like outcomes without explicit agreement.
  - Relevance: Antitrust-relevant theory of harm for AI intermediaries. Argued, not tested empirically in the abstract read.
  - OpenAlex ID: W7118628059. Cited by: 0
- **An Economy of AI Agents** (Hadfield and Koh, 2025, arXiv preprint 2509.01063) — Survey-style paper. Lists three channels: steering recommendations, lower search costs that intensify competition, and distorted demand from agent purchases. Notes agents can collude in repeated pricing games.
  - Relevance: Good map of the economics literature on AI agents as market actors. Secondary source for Ichihashi and Smolin.
  - OpenAlex ID: W4416169532. Cited by: 0
- **Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms** (Ji, Xu and Feng, 2026, SSRN) — Studies how LLM platforms monetize through ads and subscriptions.
  - Relevance: Platform incentive to sell placement inside AI answers. Title only; abstract not read.
  - OpenAlex ID: W7223371335. Cited by: 0

### Sub-theme 4: Policy, antitrust and legal analysis of AI assistants as gatekeepers
- **Is Generative AI the Algorithmic Consumer We Are Waiting For?** (Gal and Zac, 2024, Network Law Review) — Argues LLMs could act as truncated algorithmic consumers that cut search and transaction costs. Warns that LLM answers can hide newcomers and that developers can self-prefer.
  - Relevance: Most direct conceptual link between LLMs and the algorithmic-consumer idea. Argumentative. Says no comparable consumer-market studies exist yet.
  - OpenAlex: not indexed.
- **Policy commentary on agentic AI and competition law** (Linklaters, Steptoe, UK CMA-related commentary, 2025-2026) — Describes self-preferencing, margin squeeze and tying as theories of harm for agents.
  - Relevance: Policy framing only. Mostly law-firm commentary, not enforcement decisions. Found via web search only. Exact titles not verified.

### Sub-theme 5: Evidence from consumer-choice experiments (adjacent stream, cross-stream)
- **What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** (Allouah, Besbes, Figueroa, Kanoria and Kumar, 2025, arXiv preprint 2508.02630; later version 2026 ACM) — Simulated shopping shows position bias, sensitivity to sponsored tags, and demand concentration on a few "modal" products. Read from search excerpts.
  - Relevance: Only evidence found on steering and concentration in AI shopping. Cross-stream (delegated shoppers).
  - OpenAlex IDs: W4413020061 (2025 version); W7152735904 (2026 ACM version). Cited by: 8
- **A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments** (Cherep, Ma and Xu, 2025, arXiv 2509.25609) — Tests 17 LLM agents on more than 80,000 shopping choices. Nudges shift choices even with identical products.
  - Relevance: Shows AI shoppers respond to steering cues. Cross-stream.
  - OpenAlex ID: W4415338268. Cited by: 0
- **AI agents are sensitive to nudges** (Cherep, Maes and Singh, 2026, PNAS) — Peer-reviewed version of the nudge findings.
  - Relevance: Peer-reviewed evidence for steering sensitivity. Cross-stream.
  - OpenAlex ID: W7164828231. Cited by: 0

### Sub-theme 6: Algorithmic pricing and collusion (adjacent, cross-stream)
- **Artificial Intelligence, Algorithmic Pricing, and Collusion** (Calvano, Calzolari, Denicolò and Pastorello, 2020, American Economic Review) — Simulations show pricing algorithms learn to sustain supracompetitive prices.
  - Relevance: Foundational for the concentration and collusion concern. Not about search, cross-stream.
  - OpenAlex ID: W2921123283. Cited by: 677

### Background cited in the sources (not separately searched)
- Diamond (1971), Stigler (1961), Weitzman (1979) are the standard search-theory references. Lucier et al. cite Weitzman (1978), Diamond (1971) and Athey and Ellison (2011). Not checked in OpenAlex in this run.

## Reference Chain Discoveries
- Found via: Shopbot Economics citers (OpenAlex): Tang, Smith and Montgomery (2010) on shopbot use and price dispersion.
- Found via: Whitmeyer (2020) citers: Au and Whitmeyer (2022), He and Li (2023), Sato and Shirakawa (2023), Boleslavsky and Krasteva (2025).
- Found via: Ichihashi and Smolin lead from Hadfield and Koh (2025) reference text: buyer-optimal recommendations (2023 SSRN, 2025 EC).
- Found via: Lucier et al. (2026) introduction and related work: Athey and Ellison (2011), Choi et al. (2018), Immorlica et al. (2019). Only text read, not verified in OpenAlex.
- Found via: Brynjolfsson and Smith (2000) lead from the shopbot price-dispersion search.
- Found via: Lucier et al. (2026) cited by Hadfield and Koh and Rothschild et al. (2025). Lucier has 0 OpenAlex citers as of this run.

## What's Missing (Gaps)
- No peer-reviewed economics paper tests how LLM assistants change price dispersion across sellers using real market data.
- No model combines an LLM assistant's own steering with seller response and endogenous prices in one framework, beyond Lucier et al. (2026) and Ichihashi and Smolin (2025).
- No empirical measure of AI-driven demand concentration on individual sellers outside simulated shopping (Allouah et al. 2025 is simulated).
- The Diamond paradox has not been applied to LLM-mediated search in any paper found.
- Antitrust analysis of AI assistants rests on commentary. No enforcement decision on shopping agents was found.
- Product variety effects of AI search (long-tail exposure) have no theory or data paper in this search.

## Contradictions or Tensions
- Cheaper search vs more informative search: Lucier et al. (2026) find cheaper search helps consumer surplus. They find more informative search can lower surplus through weaker seller competition. Shopbot and disclosure papers suggest information provision can restore high prices (Whitmeyer 2020). Also Boleslavsky and Krasteva (2025) argue disclosure has limits.
- Buyer-side vs seller-side steering: Ichihashi and Smolin (2025) show a buyer-optimal recommender lowers prices. Hadfield and Koh (2025) and Affonso (2026) raise the risk of steering toward higher prices or collusion. The two framings differ on whose interests the intermediary serves.
- Tang et al. (2010) find shopbot use affects dispersion in books. Brynjolfsson and Smith (2000) find online dispersion persists and brand effects dominate. These two empirical bodies point in different directions on whether lower search costs reduce dispersion.
- Gal and Zac (2024) argue LLM search reduces costs but concentrates attention. Allouah et al. (2025) find demand concentration in simulated shopping. Neither has market data.

## Confidence
Confidence: Low
- What would raise confidence: A peer-reviewed or NBER version of Lucier et al. (2026) with its full related work and calibration. Also a field study of LLM assistant use with price data.
- What would lower confidence: Evidence that Lucier et al.'s endogenous-price result depends on symmetric markets. Evidence that real assistants do not follow Weitzman-type search.

## Search Log
### Round 1: Broad search
- Queries: (1) large language models consumer search costs price dispersion economics theory; (2) AI assistant delegated search sequential search model consumer welfare working paper 2025; (3) generative AI shopping agents market concentration steering self-preferencing antitrust gatekeeper; (4) Diamond paradox LLM search costs algorithmic consumers economics paper
- Papers found: about 10 relevant candidates (several results were classic non-LLM search papers or law commentary)
- Key leads: Lucier et al. (2026); Dong, Luo and Xu (2026); Rothschild et al. (2026); Gal and Zac (2024); Whitmeyer (2020)

### Round 2: Citation traversal
- Papers traversed: Lucier et al. (2026) (OpenAlex references: 0, citers: 0); Whitmeyer (2020) (references: 2, citers: 3 relevant); Kephart and Greenwald shopbot paper (references: 26, citers: 10 listed, 2 relevant).
- New papers from references: Whitmeyer's 2 references were not resolved. Shopbot references not resolved (26 IDs, not traversed further because most are general multi-agent work).
- New papers from citers: Au and Whitmeyer (2022); He and Li (2023); Sato and Shirakawa (2023); Boleslavsky and Krasteva (2025); Tang, Smith and Montgomery (2010).
- Also looked up: Ichihashi and Smolin (2023 and 2025); Brynjolfsson and Smith (2000); Calvano et al. (2020).

### Round 3: Reference section mining
- Papers mined: Lucier et al. (2026) full HTML (first 100,000 characters; related work covered).
- Authors' positioning: Lucier et al. build on Weitzman (1978), Choi et al. (2018), Immorlica et al. (2019). They say Diamond (1971) shows costly search can drive surplus to zero.
- Not mined: Dong, Luo and Xu (2026) full text (only abstract was available). Gal and Zac (2024) full text (summary only).
- New papers from this round: Athey and Ellison (2011), Chen and He (2011), Aouad et al. (2025), Gibbard (2022), Immorlica et al. (2019), Choi et al. (2018), Kannan et al. (2018) (cited, not searched).

### Round 4: Gap-filling
- Gaps targeted: empirical LLM shopping evidence; sponsored/steering effects; LLM price dispersion.
- Queries: (1) AI shopping agents price dispersion empirical evidence LLM agents purchase choices prices 2025 2026; (2) "What is your AI agent buying" LLM shopping agent bias sponsored products position effects; (3) Ichihashi Smolin buyer-optimal recommendations search.
- New findings: Allouah et al. (2025); Cherep et al. (2025, 2026); Fu and Hu (2026); Ji, Xu and Feng (2026); Liu, Chen and Wang (2026, arXiv 2609.33289, stream 5 lead, not read). A news report (June 2026) on a Princeton/UW sponsored-option study was found but not verified. Not used in the report.

### Round 5: Adversarial check
- Queries: (1) critique limitations AI agents reduce search costs increase prices concentration theory negative result agentic commerce; (2) Brynjolfsson Smith frictionless commerce price dispersion.
- New findings: Lucier et al. (2026) negative result on information (endogenous prices). Hadfield and Koh (2025) list a collusion risk for AI agents. Brynjolfsson and Smith (2000) show online brand effects reduce competition in dispersion. No direct critique of Lucier et al. found.

### Round 6+: Follow leads
- Leads followed: Shopbot citers (Tang et al. 2010); Whitmeyer citers (three disclosure papers); Calvano et al. (2020) from collusion; Affonso (2026).
- New papers in last round: Brynjolfsson and Smith (2000); Calvano et al. (2020); Affonso (2026) abstract; Ichihashi and Smolin (2025). Each is relevant. Round 6 still produced new relevant papers.
- Not explored: Delegated Search Approximates Efficient Search (arXiv 1806.06933, snippet only); Monetizing Intelligence (title only); Learning to Sell (arXiv 2609.33289, title only).

### Convergence note
- Total unique relevant papers found: 22 in this file (including cross-stream items marked as such). The report cites 17 of them.
- New papers in last round: 4 (Brynjolfsson and Smith 2000; Calvano et al. 2020; Affonso 2026; Ichihashi and Smolin 2025)
- Stopped because: The round count reached 6 without an empty round. Remaining leads are title-only and stream-adjacent. Full-text reads of two 2026 economics papers were not possible from the tool output. Treat coverage as partial.
