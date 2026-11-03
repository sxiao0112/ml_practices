# Economics and marketing working papers on generative AI and consumer markets

**Question:** Which economics and marketing papers on AI assistants and consumer search exist that computer science searches missed?

## Short answer
**Answer:** Four groups of papers are new. Egan et al. (2026) and Fradkin (2025) measure AI demand and substitution with real data. Fish et al. (2024) and Qiu et al. (2025) study LLM pricing and personalized ranking. Werner et al. (2024) run a steering experiment.

**Strength:** Medium (two peer-reviewed or NBER items, and several preprints read only through summaries)
- **Holds when:** Consumers can switch between AI services → strong price pressure and weak brand loyalty (Egan et al. 2026).
- **Does not hold when:** Pricing agents can communicate with each other → collusion-like prices can appear (Fish et al. 2024, Giebel et al. 2026).
- **Still unknown:** Whether AI shopping assistants shift real purchases at scale, and how much of that shift is hidden.

## Background
AI assistants can change how buyers search for products and how sellers set prices. Economists study these changes with search models, where buyers pay a cost to check each option. Journals in economics and marketing publish these models, and they also publish data studies of market outcomes. This page lists the papers that link AI assistants to these questions, with the evidence type for each.

Key terms used on this page:

| Term | Plain meaning |
|------|---------------|
| LLM | Large language model, the text engine behind chatbots and AI search. |
| NBER | National Bureau of Economic Research, which publishes working papers. |
| SSRN | Social Science Research Network, an online repository of working papers. |
| arXiv | Online preprint server for research papers before peer review. |
| RePEc | Research Papers in Economics, an index of economics working papers. |
| OpenAlex | Free online database of scholarly works and citation counts. |
| Multihoming | A user who pays for or uses more than one service at once. |
| Substitution | Two products serve the same need, so buyers can switch between them. |
| Algorithmic collusion | Pricing software sets high prices without explicit agreement between sellers. |
| Steering | A system nudges a user toward one option, often without the user noticing. |
| Personalized ranking | Search results ordered by what each shopper is likely to prefer. |
| Homogenization | Products or outputs become more alike across sellers or models. |
| Mechanism design | Rules for auctions or platforms that set who pays and who wins. |
| Consumer welfare | Value buyers gain, after paying prices, from the market. |
| JMR, JM | Journal of Marketing Research and Journal of Marketing, top marketing journals. |
| ISR, MISQ | Information Systems Research and MISQ, two top information systems journals. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Demand data | Track real payments to measure how AI services compete | Egan et al. (2026), Fradkin (2025) | Emerging |
| Pricing simulations | Let LLM agents set prices in a model market | Fish et al. (2024), Giebel et al. (2026) | Contested |
| Search models with personalization | Study how ranking changes search and prices | Qiu et al. (2025) | Emerging |
| Steering experiments | Show participants a biased assistant and measure choices | Werner et al. (2024), Priyanshu et al. (2026) | Emerging |
| Ad and platform theory | Model ads or subscriptions inside AI answers | Xu et al. (2026), Zhang et al. (2026) | Emerging |
| Concentration theory | Model how AI pulls products toward one template | Turegeldinova et al. (2025) | Emerging |

## What the evidence shows
### Finding 1: AI services compete on price, and buyers switch easily
- **Egan et al. (2026)**: Card data from 174 million consumers show high price sensitivity. Services are close substitutes → competition is strong and limits provider pricing power.
- **Fradkin (2025)**: Descriptive usage data show substitution and multihoming across LLM products → buyers use several services, which limits provider lock-in.
- **Strength:** Medium — real transaction data from one country, and the structural model is not fully read.

### Finding 2: LLM pricing agents can raise prices, and communication makes it worse
- **Fish et al. (2024)**: GPT-4 pricing agents in simulated markets reach prices above the competitive level → collusion appears without an agreement.
- **Giebel et al. (2026)**: Letting agents communicate raises prices and profits → communication channels matter for pricing.
- **Strength:** Low — simulations with few models and market settings. Results depend on prompts and design.

### Finding 3: Personalized rankings can raise prices and reduce welfare
- **Qiu et al. (2025)**: Personalized product rankings improve relevance but let pricing algorithms charge more → consumer welfare can fall even as search gets better.
- **Strength:** Medium — a Marketing Science paper with a formal model. It is not specific to LLMs.

### Finding 4: AI assistants can steer choices without users noticing
- **Werner et al. (2024)**: Chatbot steering shifts choices in a lab experiment. About 36% of participants would switch if steering reversed → about 39% did not notice the steering.
- **Priyanshu et al. (2026)**: Personal AI agents pick costlier options for users inferred to be wealthy → steering can work against stated user goals.
- **Strength:** Low to Medium — one lab experiment and one large simulation read through a summary.

### Finding 5: Ads and platform design in AI answers are mostly theory
- **Xu et al. (2026)**: Ad placement in LLM answers as a welfare problem → a mechanism design result, no consumer data.
- **Zhang et al. (2026)**: Ads or subscriptions for AI answer engines → long-run user welfare favors designs that serve users.
- **Strength:** Low — theory papers without experiments or market data.

### Finding 6: Theory predicts concentration, but no paper tests it with market data
- **Turegeldinova et al. (2025)**: AI pulls products toward one template → prices fall while concentration rises and entry shrinks.
- **Raghavan (2026)**: Competition keeps AI models diverse → homogenization need not persist.
- **Strength:** Low — model results that point in opposite directions.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does AI raise concentration? | Turegeldinova et al. (2025): yes, through homogenization | Raghavan (2026): no, competition keeps models diverse | Market data on product shares before and after AI |
| Do LLM agents collude? | Fish et al. (2024): yes, in simulations | 2026 preprint on fragility: collusion weakens under heterogeneity | Tests with varied agents and real sellers |
| Does communication raise prices? | Giebel et al. (2026): yes, in simulations | No second study found in the sample | Field data on agent-to-agent messages |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Real sales data on AI recommendations | Shows whether concentration happens in actual purchases | Egan et al. (2026) measures AI subscriptions, not product sales |
| Field test of LLM ads and choice | Shows whether ads shift purchases | Xu et al. (2026) gives theory only |
| Peer-reviewed journal work on LLM search | Journal articles set the field standard | No match in the four named journals |
| Replication of steering experiments | Tests whether steering holds outside the lab | Werner et al. (2024) is a single lab study |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Egan et al. | **Competition in Generative AI: Evidence from Consumer Demand** | 2026 | NBER Working Paper 35953 | abstract (fetched) |
| Fradkin | **Demand for LLMs: Descriptive Evidence on Substitution, Market Expansion, and Multihoming** | 2025 | RePEc, arXiv preprint | search summary |
| Raghavan | **Competition and Diversity in Generative AI** | 2026 | Management Science | search summary |
| Turegeldinova et al. | **AI as a Centripetal Technology: Price Compression, Homogenization, and Entry** | 2025 | SSRN working paper | search summary |
| Iannelli and Ai | **From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web** | 2026 | arXiv preprint | OpenAlex record only |
| Figliozzi | **From Chatbots to Checkouts: Modeling the Path from Consumer LLM Adoption to E-Commerce Utilization** | 2026 | SSRN working paper | OpenAlex record only |
| Fish et al. | **Algorithmic Collusion by Large Language Models** | 2024 | RePEc, arXiv preprint | search summary |
| Giebel et al. | **Artificial Intelligence, Communication, and Strategic Pricing: Evidence from Large Language Models** | 2026 | SSRN working paper | search summary |
| Qiu et al. | **Personalization, Consumer Search, and Algorithmic Pricing** | 2025 | Marketing Science | abstract (fetched) |
| Werner et al. | **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** | 2024 | arXiv preprint (economics) | abstract (fetched) |
| Priyanshu et al. | **Et Tu, Brute? Economic Misalignment in Personal AI Agents** | 2026 | arXiv preprint | search summary |
| Li | **Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test** | 2026 | arXiv preprint | OpenAlex record only |
| Xu et al. | **Ad Insertion in LLM-Generated Responses** | 2026 | arXiv preprint | OpenAlex record only |
| Zhang et al. | **An Economic Framework for Generative Engines: Advertising or Subscription?** | 2026 | arXiv preprint | search summary |
| Qiu and Mei | **Generative AI Advertising as a Problem of Trustworthy Commercial Intervention** | 2026 | arXiv preprint | OpenAlex record only |
| Huang et al. | **Cultural Encoding in Large Language Models: The Existence Gap in AI-Mediated Brand Discovery** | 2025 | arXiv preprint | OpenAlex record only |
| Neto and Miranda | **When the Counterparty Is a Machine: Strategy, Entrepreneurial Innovation and Digital Marketing Under Generative-AI Commoditization** | 2026 | SSRN working paper | OpenAlex record only |
| Moghaddam et al. | **When the customer is a machine: a systematic literature review and integrative framework of agentic commerce** | 2026 | Research Square preprint | OpenAlex record only |
| France and Albinsson | **Synthetic Consumer Insight Generation with Large Language Models** | 2026 | arXiv preprint | OpenAlex record only |
| Dubé and Misra | **Personalized Pricing and Consumer Welfare** | 2017 | NBER working paper (before the 2023-2026 window) | OpenAlex record only |
| Bar-Isaac et al. | **Search, Design, and Market Structure** | 2012 | American Economic Review (before the window) | OpenAlex record only |

<details><summary>Original research question</summary>

Sweep SSRN, NBER, CEPR and top marketing/IS/econ journals (Marketing Science, JMR, JM, Management Science, ISR, MISQ, QJE, AER, RAND) for 2023-2026 papers on generative AI or LLMs and consumer search or product choice: market concentration and long-tail effects, price competition, brand strategy and advertising in AI answers, consumer welfare, platform self-preferencing, and empirical studies using LLMs to measure consumer search. Which papers exist that the CS-leaning searches missed?

</details>
