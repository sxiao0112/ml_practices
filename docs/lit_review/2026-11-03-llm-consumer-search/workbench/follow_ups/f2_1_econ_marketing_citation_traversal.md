# Starting from the key economics and marketing papers already found (e.g., Egan et al. 2026; Fradkin 2025; Kaiser and Schulze 2026 Marketing Science; Werner et al. 2024 steering; Qiu et al. 2025 Marketing Science; Fish et al. 2024 LLM collusion; the 2026 Weitzman-style AI-searcher theory papers; Padilla et al. 2026), run forward and backward citation traversal in OpenAlex and Google Scholar-style web search to find remaining econ, marketing and IS papers on LLMs and consumer search, competition, prices, product variety, or welfare. Then run an adversarial check: are there papers that find NO effect, or the opposite effect, of AI assistants on search, concentration or welfare?

## TL;DR
Answer: Traversal found 13 papers not yet in the workbench. Most are on algorithmic pricing, collusion and AI intermediaries in theory or simulation. Only one is a field experiment on an AI shopping assistant (Wang et al., ISR 2025). No paper found shows a clean null effect of AI search on concentration. The adversarial check did find results pointing the other way on collusion, steering and welfare.
Strength: Low
Traversal reached the seed papers' citers and references, but many citers are off-topic. Several new items have only OpenAlex metadata or search snippets. Full texts were not read for most of the new items.

## What Exists
### Sub-theme 1: Algorithmic recommendations, platform manipulation and competition (new)
- **Artificial Intelligence, Algorithmic Recommendations and Competition** (Calvano, Calzolari, Denicolò and Pastorello, 2023, CEPR Discussion Paper 18176) — Simulations show recommenders can raise concentration and prices, but also cut search costs. Overall consumer surplus is likely higher for reasonable parameters. Platform manipulation may intensify seller competition.
  - Relevance: Directly tests the concentration, price and welfare trade-off for recommender systems. A counterpoint to the view that recommendations harm consumers.
  - Read: abstract and VoxEU column summary via search. Full text behind a CEPR paywall.
  - OpenAlex ID: W4398627305 (supplementary appendix record; main record not located)
  - Note: a separate OpenAlex record, W4206561927 (2022, "Artificial Intelligence, Algorithmic Competition and Market Structures"), was seen but not checked. Its authorship is unverified, so it is not counted.
- **Algorithmic pricing: Implications for marketing strategy and regulation** (Spann, Bertini, Koenigsberg, Zeithammer and coauthors, 2025, International Journal of Research in Marketing) — Reviews how firms adopt pricing algorithms and the competition and price-discrimination concerns they raise. Includes a manager survey in the working-paper version.
  - Relevance: Marketing-journal review of algorithmic pricing. Not LLM-specific, but the mechanism applies to LLM price agents.
  - Read: search fragments of abstract. DOI 10.1016/j.ijresmar.2025.05.001.
  - OpenAlex ID: W4410889186
  - Cited by: 19 (OpenAlex)
- **The Coasean Singularity? Demand, Supply, and Market Design with AI Agents** (Shahidi, Rusak, Manning and Fradkin, 2025, NBER Working Paper 34468) — Argues AI agents cut search, communication and contracting costs. Also argues congestion and price obfuscation are new frictions. Calls welfare effects an empirical question.
  - Relevance: Framing paper for agent-mediated search and market design. Cited by Lucier et al. (2026) in the introduction.
  - Read: NBER and author-site summary via search. Full text not read.
  - OpenAlex ID: W4416085266
  - Cited by: 19 (OpenAlex)
- **Why Does AI Platform Competition Diverge? A Dynamic Analysis of Adoption, Recommendation Mechanisms, and Price Feedback** (authors not checked, 2026, OpenAlex record) — Models how AI platforms compete through adoption, recommendation design and price feedback.
  - Relevance: Platform competition model with recommendation mechanisms and prices. Theory only.
  - Read: OpenAlex title only.
  - OpenAlex ID: W7172488216
  - Cited by: 0
- **When do pricing algorithms intensify competition? A theory of online oligopoly** (authors not checked, 2026, OpenAlex record) — Theory of when pricing algorithms raise or lower competition in online oligopoly.
  - Relevance: Counterpoint on whether algorithms collude or compete. Theory only.
  - Read: OpenAlex title only.
  - OpenAlex ID: W7212143811
  - Cited by: 0

### Sub-theme 2: LLM price collusion and heterogeneity (new, adversarial)
- **On the Fragility of AI Agent Collusion** (Keppo, Li, Tsoukalas and Yuan, 2026, arXiv 2603.20281) — Argues LLM collusion weakens when agents differ. Patience gaps cut the price markup from about 22% to about 10%. Asymmetric data access cuts it to about 7%. Adding more LLMs or mixing in Q-learning agents breaks collusion, but model-size gaps do not.
  - Relevance: Direct adversarial result against the Fish et al. (2024) collusion finding. Shows the effect depends on agent heterogeneity. Stylized model plus experiments with open-source LLMs.
  - Read: arXiv abstract via fetch. Full text not read.
  - OpenAlex ID: not found
  - Note: the 22% and 10% and 7% figures come from the abstract summary. Their exact definitions are not verified.
- **AI Pricing, Agent Heterogeneity, and Collusion** (authors not checked, 2025, working paper) — Studies how heterogeneous pricing agents affect collusion. Title and event listing only.
  - Relevance: Second source on heterogeneity and collusion. Points the same way as Keppo et al. (2026). Not read.
  - Read: OpenAlex title and CUHK event page via search.
  - OpenAlex ID: W4413103613
  - Cited by: 0
- **AI-Powered Trading, Algorithmic Collusion, and Price Efficiency** (authors not checked, 2025, NBER working paper) — Studies collusion among AI trading algorithms and its effect on price efficiency. Finance setting, not consumer markets.
  - Relevance: Adjacent. Shows algorithmic collusion results outside retail. Not about consumer search.
  - Read: OpenAlex title only.
  - OpenAlex ID: W4412535963
  - Cited by: 37 (OpenAlex)
- **Playing repeated games with large language models** (authors not checked, 2025, Nature Human Behaviour) — Tests how LLMs behave in repeated strategic games, including cooperation.
  - Relevance: Adjacent. Lab evidence on LLM cooperation or collusion tendencies. Not about consumer search.
  - Read: OpenAlex title only.
  - OpenAlex ID: W4410251374
  - Cited by: 106 (OpenAlex)

### Sub-theme 3: AI assistants in shopping, sales and welfare (new, adversarial)
- **Artificial Intelligence (AI) Assistant in Online Shopping: A Randomized Field Experiment on a Livestream Selling Platform** (Wang, Huang, He and De, 2025, Information Systems Research) — A randomized field experiment on a livestream platform. The AI assistant raised sales by about 3.00% and cut return rates by about 12.55%. The effect was larger for high-uncertainty products.
  - Relevance: Only field experiment found on an AI shopping assistant with sales and returns outcomes. Positive effect, which runs against a no-effect or harm reading. Livestream setting, not an LLM search engine.
  - Read: search summary of abstract. Full text not read. An earlier SSRN version (2023) exists under "The Role of AI Assistants in Livestream Selling".
  - OpenAlex ID: W4408288065
  - Cited by: 58 (OpenAlex)
- **What Is Generative AI Worth?** (Brynjolfsson et al., 2026, Stanford Digital Economy Lab working paper) — Estimates consumer welfare gains from generative AI. Reports the mean willingness to accept rising from $98 in 2025 to $124.50 in 2026.
  - Relevance: Welfare counter-evidence against harm claims. General generative AI, not search-specific. Authors and figures from search summary only.
  - Read: search summary. Full text not read.
  - OpenAlex ID: not found

### Sub-theme 4: Agentic shoppers and delegated pricing (new)
- **Markdown Pricing When Shoppers Delegate to AI Agents** (Yuan and Yin, 2026, SSRN) — The OpenAlex title points to a seller pricing model when shoppers delegate to AI agents. A search result for a similar seller-strategy paper ("When Consumers Delegate") suggests the same research. That match is unconfirmed.
  - Relevance: Seller response to delegation, including pricing and visibility to agents. Theory.
  - Read: OpenAlex title only. Abstract not retrieved.
  - OpenAlex ID: W7220679498
  - Cited by: 0
- **LLM-Agent Interactions on Markets with Information Asymmetries** (Erlei and Meub, 2026, arXiv) — Studies LLM agents trading in markets where one side has more information.
  - Relevance: Adjacent. LLM agent market behavior under asymmetric information. Not consumer search.
  - Read: OpenAlex title and authors only.
  - OpenAlex ID: W7134931404
  - Cited by: 0

## Reference Chain Discoveries
[Papers found via citation traversal that weren't in initial searches]
- Found via: Calvano et al. (2023) main-paper search and the Calvano et al. (2020 AER) citers. The 2020 AER paper is already in the workbench and is also in Qiu et al.'s reference list.
- Found via: OpenAlex citers of Fish et al. (2024), W4393724845. Yields Spann et al. (2025), the 2025 heterogeneity and collusion items, and AI-Powered Trading.
- Found via: OpenAlex citers of Werner et al. (2024), W4403746738. Only one unrelated 2025 paper returned.
- Found via: OpenAlex citers of Qiu et al. (2025), W4410139673. Yields the two 2026 platform-competition theory papers.
- Found via: Lucier et al. (2026) introduction, read through the arXiv HTML. Names Shahidi et al. (2025). OpenAlex record then resolved it.
- Found via: Round 4 search on "AI agents price dispersion". Yields the Yuan and Yin record.
- Found via: Round 4 search on AI assistant field experiments. Yields the Wang et al. (2025) livestream study.
- Found via: Round 5 search on welfare harms of AI. Yields Brynjolfsson et al. (2026).
- Found via: Round 5 critique search on LLM collusion. Yields Keppo et al. (2026).

## What's Missing (Gaps)
- No econ or marketing paper found that tests LLM search engines with market-level concentration data.
- No field experiment found on an LLM search engine that measures prices or product variety. The livestream study is the nearest case.
- The Calvano et al. (2023) main paper is behind a paywall. Its full results were not read.
- Shahidi et al. (2025) and Lucier et al. (2026) are theory or framing. No empirical test of agent-mediated search on concentration was found.
- An LLM-vs-Qiu-style personalization study with real consumer search data was not found.
- Unverified industry claims (Vaer AI on retailer share in AI answers, and a Princeton and UW study on sponsored options in AI flight booking) were not counted. Neither was retrieved in full.
- Karle, Preuss and Reisinger (CESifo WP 12465, 2026) on platform recommendations and commissions surfaced in search only. Not found in OpenAlex, so not counted.

## Contradictions or Tensions
- Collusion: Fish et al. (2024) find LLM pricing agents reach supracompetitive prices. Keppo et al. (2026) find the effect shrinks under patience or data heterogeneity. Calvano et al. (2023) find pricing and recommendation effects depend on parameters.
- Recommenders and concentration: Calvano et al. (2023) find recommenders can raise concentration and prices. The same paper also finds consumer surplus likely rises for reasonable parameters.
- Manipulation: Calvano et al. (2023) argue platform manipulation may intensify competition and lower prices. The authors call it an exclusionary abuse, not an exploitative one.
- Sales effect of assistants: Wang et al. (2025) find a small sales gain and fewer returns. Brynjolfsson et al. (2026) find large consumer welfare gains. Both are positive, but in different settings.
- Delegation and pricing: Yuan and Yin (2026) model sellers reducing visibility and raising prices as shoppers delegate. This runs against a simple price-cutting story. The abstract was not read, so this is provisional.

## Confidence
Low
- What would raise confidence: Full text of Calvano et al. (2023) with its consumer surplus results, and a replication of Wang et al. (2025) on LLM search engines.
- What would lower confidence: Several new items are OpenAlex titles only. The Keppo et al. percentages come from an abstract summary and could change in the full paper.

## Search Log
### Round 1: Broad search
- Queries: LLM consumer search price competition welfare working paper 2026 SSRN; generative AI chatbot product choice concentration brands marketing science 2026; AI assistant shopping recommendations market concentration empirical NBER working paper; LLM search no effect OR null result consumer welfare AI assistant economics study.
- Papers found: about 25 candidate items across four queries. Most were industry reports or already in the workbench.
- Key leads: Lucier et al. (2026, arXiv 2603.25893, already in workbench); Calvano et al. (CEPR DP18176); Keppo et al. (2026); Karle et al. (CESifo, not verified).

### Round 2: Citation traversal
- Papers traversed: forward citers of Werner et al. (W4403746738), Fish et al. (W4393724845), Qiu et al. (W4410139673), Kaiser and Schulze (W7155099606), Fradkin (W4414631693), Egan et al. (W7223707194), Lucier et al. (W7143291850), Turegeldinova et al. (W4415449137).
- Backward references: Qiu et al. (25 references resolved in OpenAlex), Fish et al. (none listed), Lucier et al. (none listed), Werner et al. (none listed), Egan et al. (none listed).
- New papers from references: Calvano et al. (2020, already in workbench); older pricing-algorithm and search-theory papers (pre-2023, context only).
- New papers from citers: Spann et al. (2025); AI Pricing, Agent Heterogeneity, and Collusion (2025); two 2026 platform-competition theory papers; AI-Powered Trading (2025); Playing repeated games with LLMs (2025); Erlei and Meub (2026); Yuan and Yin (2026).

### Round 3: Reference section mining
- Papers mined: Lucier et al. (2026, arXiv 2603.25893), via arXiv HTML. Keppo et al. (2026, arXiv 2603.20281), via abstract.
- New papers from references: Shahidi et al. (2025, NBER 34468); Hadfield and Koh and Rothschild et al. (already in workbench). Choi et al. (2018), Immorlica et al. (2019), Kleinberg et al. (2016), Athey and Ellison (2011), Diamond (1971), Weitzman (1978/1979) are pre-2023 and counted as context only.
- New papers from citers: none beyond Round 2.

### Round 4: Gap-filling
- Gaps targeted: NET Institute audit of LLM product recommendations (already in workbench as An Empirical Audit of LLM Product Recommendations); Calvano DP18176 details; AI shopping assistant field experiments; LLM price dispersion; long-tail and variety; delegated pricing.
- Queries: NET audit first-position concentration; Calvano CEPR DP18176; Shahidi agentic commerce; AI shopping assistant randomized field experiment; AI shopping agents price dispersion; generative AI variety long tail.
- New findings: Shahidi et al. (2025, NBER 34468); Wang et al. (2025, ISR); Yuan and Yin (2026, title); Calvano VoxEU column. The NET audit was already in the workbench.

### Round 5: Adversarial check
- Gaps targeted: critiques of LLM collusion; null or negative results on AI search; welfare harm claims.
- Queries: LLM collusion fragility critique and replication; generative AI assistant consumer sales or welfare negative effect; AI assistant null result field experiment.
- New findings: Keppo et al. (2026, fragility); Brynjolfsson et al. (2026, welfare gains); Wang et al. (2025, positive field effect). No paper found with a clean null effect of AI search on concentration.

### Round 6: Systematic keyword sweep (OpenAlex, 2025-2026)
- Queries: ten keyword searches on LLM consumer search, AI shopping, agentic commerce, generative engine optimization, AI advertising, LLM pricing and collusion, answer engines, and ChatGPT shopping. Filtered to 2025-2026 and sorted by citation count.
- Hits: 204 unique items, most off-topic. Filtering unseen items by consumer and pricing terms left a short list. Only the items listed above were relevant enough to add.
- New findings: AI-Powered Trading (2025), Playing repeated games with LLMs (2025), The Coasean Singularity (already counted), Erlei and Meub (2026).

### Convergence note
- Total unique relevant papers found: 13 new in-range papers in this round. Of these, 2 are adjacent (finance collusion and LLM repeated games) and 2 are agent-market papers outside consumer search (Erlei and Meub, Yuan and Yin). Six have abstract or summary text (Calvano, Spann, Shahidi, Keppo, Wang, Brynjolfsson). The rest are OpenAlex titles or search snippets only.
- New papers in last round: 2 relevant (Erlei and Meub; AI-Powered Trading), both adjacent.
- Stopped because: Rounds 4 to 6 added few new consumer-search papers, and the keyword sweep returned mostly off-topic items. The eight-round cap was not reached.
