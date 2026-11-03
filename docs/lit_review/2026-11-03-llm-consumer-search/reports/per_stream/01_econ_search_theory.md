# How LLMs change search costs and market outcomes: economic theory and evidence

**Question:** How do LLM assistants change the cost of consumer search, and what follows for prices, competition, concentration, variety and welfare?

## Short answer
**Answer:** First, cheaper AI search helps buyers in theory. More informative search can weaken seller competition (Agentic Markets (Lucier 2026)). Second, a recommender built for buyers can lower prices (Buyer-Optimal (Ichihashi 2025)). Third, no study yet measures LLM effects on price dispersion or concentration with market data.

**Strength:** Low (two 2026 theory papers without peer review, one peer-reviewed recommender model, and no LLM market data)
- **Holds when:** Shoppers pay to learn product fit → cheaper search improves learning and consumer surplus.
- **Does not hold when:** Buyers learn more than the market does → more informative search can lower buyer surplus.
- **Still unknown:** Whether real AI assistants search the way these models assume, and how prices spread across sellers.

## Background
The question asks how AI assistants change the cost of finding products and prices. A shopper pays a cost to check each seller, and economists link this cost to prices and competition. The Diamond paradox says even a tiny search cost can push all sellers to monopoly prices. LLM assistants could lower search costs, or they could steer buyers toward some sellers.

Key terms used on this page:

| Term | Plain meaning |
|------|---------------|
| LLM | Large language model, the text engine behind chatbots and AI search. |
| AI assistant | Chatbot or AI search tool that answers questions and may recommend products. |
| Search cost | Time, money or effort a shopper spends to check one more option. |
| Price dispersion | How far apart prices are for the same product across sellers. |
| Diamond paradox | Tiny search costs can lead sellers to charge monopoly prices and leave buyers unsearched. |
| Weitzman search | Rule for which option to check next and when to stop checking. |
| Ordered search | Buyers check sellers in a set order and can stop early. |
| Shopbot | Software that compares prices across online stores for a shopper. |
| Consumer surplus | Value buyers gain beyond the price they pay. |
| Endogenous prices | Prices that sellers set in response to market conditions. |
| Information provision | Sellers or platforms decide what details buyers see before buying. |
| Steering | An intermediary tilts its recommendations toward some products. |
| Self-preferencing | A platform favors its own products over rival sellers. |
| Algorithmic consumer | Software that searches and buys for a person. |
| Algorithmic collusion | Pricing software that keeps prices high without any agreement between firms. |
| Gatekeeper | A firm that controls access to customers or key markets. |
| Antitrust | Competition law that polices monopoly power and unfair conduct. |
| Modal product | The product an AI agent picks most often across tests. |
| Sponsored tag | Label that marks a paid placement in a product list. |
| Position bias | Tendency to pick items shown in higher spots. |
| Nudge | Small change in layout or wording that shifts choices. |
| Bayesian | Updating beliefs with each new piece of evidence. |
| Simulation | Computer model that runs many virtual shoppers or sellers. |
| Preprint | Paper posted online before peer review. |
| Peer review | Checking by journal referees before publication. |
| SSRN | Social Science Research Network, a site for economics working papers. |
| arXiv | Online server for preprints in physics, computer science and economics. |
| ACM | Association for Computing Machinery, a computer science society that runs conferences. |

## Main approaches
Researchers attack this question in seven ways. The table lists each approach, its main papers and its status.

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Classic search theory | Costly search lets sellers keep prices high. | Diamond (1971), Diamond Persuasion (Whitmeyer 2020) | Established |
| Information design in search | Sellers choose what buyers learn before they search. | Attraction vs Persuasion (Au 2022), Disclosure Random Search (He 2023) | Emerging |
| Weitzman-style AI search | AI agents pay to learn product fit and search in order. | Agentic Markets (Lucier 2026), Agentic Commerce (Dong 2026), Digital Search (Rothschild 2026) | Emerging |
| Intermediary steering | Recommenders can favor buyers or sellers and move prices. | Buyer-Optimal (Ichihashi 2025), AI Economy (Hadfield 2025) | Emerging |
| Consumer-choice experiments | Simulated AI shoppers show steering and demand concentration. | AI Agent Buying (Allouah 2025), Nudge Study (Cherep 2025) | Emerging |
| Shopbot price data | Software search tools changed prices in real online markets. | Shopbot Prices (Tang 2010), Frictionless Commerce (Brynjolfsson 2000) | Contested |
| Algorithmic collusion | Pricing software can sustain high prices without agreement. | Algorithmic Collusion (Calvano 2020), Tacit Collusion (Affonso 2026) | Emerging |

## What the evidence shows
### Finding 1: Cheaper AI search can raise buyer surplus in theory.
- **Agentic Markets (Lucier 2026)**: Models shoppers who pay to learn fit → cheaper search improves learning and consumer surplus.
- **Agentic Commerce (Dong 2026)**: Models shoppers with complex preferences → agentic search avoids the match collapse that manual search suffers.
- **Strength:** Low — two theory papers from 2026, neither peer reviewed, and no market data.

### Finding 2: More informative search can lower buyer surplus.
- **Agentic Markets (Lucier 2026)**: Finds more informative search can cut surplus, because sellers compete less.
- **Diamond Persuasion (Whitmeyer 2020)**: Shows that information provided by firms can bring back the Diamond result of high prices.
- **Strength:** Low — the main claim comes from one theory model, and the Whitmeyer result is read from a search summary.

### Finding 3: Steering can lower prices when the intermediary serves buyers.
- **Buyer-Optimal (Ichihashi 2025)**: Models a recommender that serves buyers. It skips high-price items, which pushes sellers to cut prices.
- **AI Economy (Hadfield 2025)**: A survey lists steering, lower search costs and agent collusion as price channels.
- **Tacit Collusion (Affonso 2026)**: Argues that agents and sellers can reach collusion-like prices without any agreement.
- **Algorithmic Consumer (Gal 2024)**: Argues that LLM answers can hide newcomers and that developers can self-prefer.
- **Strength:** Medium for the buyer-side result (peer-reviewed model, but one model and no field test). Low for seller-side and policy claims (argument only, no enforcement case found).

### Finding 4: AI shoppers respond to steering cues, and their choices can concentrate.
- **AI Agent Buying (Allouah 2025)**: Simulated shoppers favor top positions and penalize sponsored tags. Choices concentrate on a few modal products.
- **Nudge Study (Cherep 2025)**: Tested 17 LLM agents on more than 80,000 choices. Nudges shifted picks even for identical products.
- **Strength:** Medium for the direction of the effect (many models and trials, one team). Low for market effects, since the work uses simulated shopping only.

### Finding 5: Shopbot evidence on price dispersion is mixed, and no LLM data exists.
- **Shopbot Prices (Tang 2010)**: Reports that price dispersion fell over the study period, per a search summary.
- **Frictionless Commerce (Brynjolfsson 2000)**: Finds online prices 9 to 16 percent lower, but price gaps among online sellers stay large.
- **Strength:** Low — the data are pre-LLM, and the two papers point in different directions on dispersion.

## Where researchers disagree
The sources disagree on two questions. The table lists each view and what would settle it.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does lower search cost reduce price dispersion? | Shopbot Prices (Tang 2010): dispersion fell in one study. | Frictionless Commerce (Brynjolfsson 2000): dispersion stays large online. | Price records from purchases made with and without an AI assistant, across many sellers. |
| Do intermediary recommendations lower or raise prices? | Buyer-Optimal (Ichihashi 2025): a buyer-side recommender lowers prices. | Tacit Collusion (Affonso 2026): agents and sellers may reach collusion-like prices. | A model fit to real assistant rankings and seller price changes. |

## Gaps
Five gaps limit what the theory can claim. Each row names the closest existing work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Price dispersion under real AI assistant use | Dispersion is the main test of search-cost theory. | Shopbot Prices (Tang 2010) |
| Assistant steering combined with seller pricing | Steering decides whether buyers or sellers gain. | Buyer-Optimal (Ichihashi 2025) |
| Diamond paradox applied to LLM search | Shows whether AI tools restore competition. | Diamond Persuasion (Whitmeyer 2020) |
| Market concentration among AI assistants | Shows whether a few assistants gain gatekeeper power. | AI Agent Buying (Allouah 2025), simulated only |
| Antitrust cases on AI shopping agents | Shows whether gatekeeper rules apply to agents. | None found. |

## Papers cited
Each short name appears once in the text above. The last column shows how much of each source we read.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Agentic Markets (Lucier 2026) | **Agentic Markets: Equilibrium Effects of Improving Consumer Search** | 2026 | arXiv preprint | Partial full text |
| Agentic Commerce (Dong 2026) | **From Product Search to Preference Articulation: The Economics of Agentic Commerce** | 2026 | SSRN | Abstract |
| Digital Search (Rothschild 2026) | **The Evolution of Digital Search: From Blue Links to Delegated Decision-Making** | 2026 | arXiv preprint | Search excerpt |
| Algorithmic Consumer (Gal 2024) | **Is Generative AI the Algorithmic Consumer We Are Waiting For?** | 2024 | Network Law Review | Summary of full text |
| Buyer-Optimal (Ichihashi 2025) | **Buyer-Optimal Algorithmic Recommendations** | 2025 | ACM Conference on Economics and Computation | Search excerpt |
| Diamond Persuasion (Whitmeyer 2020) | **Persuasion Produces the (Diamond) Paradox** | 2020 | arXiv preprint | Search excerpt |
| Diamond (1971) | **A Model of Price Adjustment** | 1971 | Journal of Economic Theory | Cited in another paper only |
| Attraction vs Persuasion (Au 2022) | **Attraction versus Persuasion: Information Provision in Search Markets** | 2022 | Journal of Political Economy | Title and metadata |
| Disclosure Random Search (He 2023) | **Competitive information disclosure in random search markets** | 2023 | Games and Economic Behavior | Title and metadata |
| Shopbot Economics (Kephart 2002) | **Shopbot Economics** | 2002 | Autonomous Agents and Multi-Agent Systems | Search excerpt |
| Shopbot Prices (Tang 2010) | **The impact of shopbot use on prices and price dispersion: Evidence from online book retailing** | 2010 | International Journal of Industrial Organization | Search excerpt |
| Frictionless Commerce (Brynjolfsson 2000) | **Frictionless Commerce? A Comparison of Internet and Conventional Retailers** | 2000 | Management Science | Search excerpt |
| AI Agent Buying (Allouah 2025) | **What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** | 2025 | arXiv preprint | Search excerpts of abstract and text |
| Nudge Study (Cherep 2025) | **A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments** | 2025 | arXiv preprint | Search excerpt |
| Algorithmic Collusion (Calvano 2020) | **Artificial Intelligence, Algorithmic Pricing, and Collusion** | 2020 | American Economic Review | Cited only, background |
| Tacit Collusion (Affonso 2026) | **Vertical tacit collusion in AI-mediated markets** | 2026 | arXiv preprint | Search excerpt |
| AI Economy (Hadfield 2025) | **An Economy of AI Agents** | 2025 | arXiv preprint | Search excerpts |

<details><summary>Original research question</summary>

What does economics (theory and empirics) say about how LLMs and AI assistants change consumer search costs, and the downstream effects on price dispersion, competition, market concentration, product variety, and consumer welfare? Include search-cost models (sequential/ordered search, Diamond paradox), delegated search to AI intermediaries, 'algorithmic consumers', steering/self-preferencing by AI intermediaries, and policy/antitrust analysis of AI assistants as gatekeepers.

</details>
