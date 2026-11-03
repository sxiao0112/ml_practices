# Economics and marketing: citation trail and stress test

**Question:** Which other economics, marketing and information systems papers study AI assistants and consumer search, prices, variety or welfare? Do any find no or opposite effects?

## Short answer
**Answer:** Thirteen papers are new to this review. Most study algorithmic pricing, collusion and AI intermediaries in models or simulations. Only one is a field experiment on an AI shopping assistant, and it finds sales rose 3.00% against a control group.

**Strength:** Low (few field studies, and most new items were read only as abstracts or titles)
- **Holds when:** AI price agents are alike in a repeated market → simulated prices rise above competitive levels (Fish 2024).
- **Does not hold when:** agents differ in patience → Keppo 2026 cuts the markup above competitive prices from 22% to 10%.
- **Still unknown:** whether AI assistants change prices, variety or welfare in real markets with sales records.

## Background
Many buyers now ask AI chatbots for product advice before they buy. Economists ask whether this lowers the effort of comparing options, changes prices, or concentrates sales on a few sellers. The answer depends on who sets the prices and whether buyers trust the advice.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| AI assistant | A chatbot or agent that answers questions or acts for a user. |
| Consumer search | The effort a buyer spends comparing options before buying. |
| Agentic commerce | Shopping in which an AI agent searches and buys for the user. |
| Algorithmic pricing | Software that sets or adjusts prices automatically from market data. |
| Collusion | Sellers keep prices high together without an explicit agreement. |
| Supracompetitive price | A price above the level that competition would produce. |
| Recommender system | Software that ranks or suggests products to a buyer. |
| Steering | An intermediary shifts buyer choices toward chosen sellers or products. |
| Heterogeneity | Differences between agents, such as patience or data access. |
| Q-learning | A trial-and-error learning method used by some pricing software. |
| Simulation | A computer model where agents act, used when real data are missing. |
| Field experiment | Real customers randomly assigned to a treatment or a control group. |
| Randomized trial | A field experiment where chance decides who gets the treatment. |
| Weitzman-style search model | Theory where buyers pay to inspect options and stop by a rule. |
| Willingness to accept | The payment a user would take to give up a product. |
| Citation traversal | Following a paper's references backward and its citing papers forward. |
| Working paper | A paper shared before peer review, on NBER, SSRN or arXiv. |
| NBER | National Bureau of Economic Research, a US economics research network. |
| SSRN | Social Science Research Network, a preprint server for economics and business. |
| arXiv | An open preprint server for computer science, economics and statistics. |
| CEPR | Centre for Economic Policy Research, a European economics network. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Pricing simulations | Software sellers set prices in a repeated market. | Fish 2024, Keppo 2026, Calvano 2020 | Contested |
| Recommender models | Models how rankings and suggestions change competition. | Calvano 2023, Shahidi 2025 | Emerging |
| Search theory | Models buyers who pay to inspect options and stop by a rule. | Lucier 2026, Yuan and Yin 2026 | Emerging |
| Shopping field experiment | Real shoppers randomly get an AI assistant or not. | Wang 2025 | Emerging |
| Choice experiments | Tests whether chatbot wording shifts buyer choices. | Werner 2024 | Emerging |
| Welfare estimates | Measures how much buyers value generative AI. | Brynjolfsson 2026 | Emerging |

## What the evidence shows
### Finding 1: Pricing agents can collude, but differences between agents weaken it.
- **Fish (Fish et al. 2024)**: LLM pricing agents in a simulated market → prices rose above competitive levels.
- **Keppo (Keppo et al. 2026)**: A stylized model and open-source LLM agents → patience gaps cut the markup from 22% to 10%.
- **Strength:** Medium for direction, because both papers agree on heterogeneity. Low for size, because both are simulations or preprints.

### Finding 2: Recommenders can raise prices and concentration, yet may still help buyers.
- **Calvano (Calvano et al. 2023)**: Simulated recommender systems → concentration and prices can rise. Consumer surplus is likely higher for reasonable settings.
- **Lucier (Lucier et al. 2026)**: Theory of search with AI helpers → cheaper search raises buyer surplus. More informative search can lower it.
- **Strength:** Low, because both are theory or simulation, with no market sales data.

### Finding 3: One randomized trial finds an AI shopping assistant raised sales and cut returns.
- **Wang (Wang et al. 2025)**: Randomized trial on a livestream selling platform → sales rose 3.00% and return rates fell 12.55%.
- **Strength:** Medium for this setting, because it is a peer-reviewed randomized trial. Low for chatbots, because the setting differs.

### Finding 4: One study estimates large buyer gains from generative AI.
- **Brynjolfsson (Brynjolfsson et al. 2026)**: Estimate of user value for generative AI → willingness to accept rose from $98 to $124.50.
- **Strength:** Low, because it is a working paper on generative AI in general and read only from a summary.

### Finding 5: Chatbots can steer choices without the buyer noticing.
- **Werner (Werner et al. 2024)**: Behavioral experiment with a conversational AI → choices shifted, and about 39% of participants did not notice.
- **Strength:** Low, because it is one experiment, read from the abstract, with no journal version found.

## Where researchers disagree
The table lists the main disagreements. Each row names the test that would settle it.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do pricing agents collude? | Fish 2024: simulated LLM sellers reach above-competitive prices. | Keppo 2026: differences between agents shrink collusion sharply. | Real-market price data across sellers with different tools. |
| Do recommenders hurt buyers? | Calvano 2023: concentration and prices can rise with recommenders. | Lucier 2026: more information can lower buyer surplus. | Field measures of buyer surplus under AI recommendations. |
| Is AI steering harmful? | Werner 2024: undetected steering shifts buyer choices. | Calvano 2023: manipulation may intensify competition and lower prices. | Trials that measure prices paid under steered recommendations. |

## Gaps
The table lists what no paper has tested, and the nearest existing work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Sales concentration when AI helps buyers, using market data | Concentration drives the welfare question. | Egan 2026 (card data, no search) |
| Field tests of chatbot search with prices | Field results test whether models match real buyers. | Wang 2025 (livestream, not a chatbot) |
| Variety and long-tail effects of AI search | Variety decides whether small sellers gain. | Qiu 2025 (personalized ranking, no AI) |
| Real-world collusion by AI sellers | Simulations may overstate or miss collusion. | Keppo 2026 (simulation) |
| Buyer welfare of chatbot search | Welfare drives policy on AI intermediaries. | Calvano 2023 (simulation) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Fish | **Algorithmic Collusion by Large Language Models** | 2024 | arXiv preprint | summary |
| Keppo | **On the Fragility of AI Agent Collusion** | 2026 | arXiv preprint | abstract |
| Calvano 2020 | **Artificial Intelligence, Algorithmic Pricing, and Collusion** | 2020 | American Economic Review | summary |
| Calvano 2023 | **Artificial Intelligence, Algorithmic Recommendations and Competition** | 2023 | CEPR Discussion Paper 18176 | summary (full text paywalled) |
| Spann | **Algorithmic pricing: Implications for marketing strategy and regulation** | 2025 | International Journal of Research in Marketing | search fragments |
| Shahidi | **The Coasean Singularity? Demand, Supply, and Market Design with AI Agents** | 2025 | NBER Working Paper 34468 | summary |
| Lucier | **Agentic Markets: Equilibrium Effects of Improving Consumer Search** | 2026 | arXiv preprint | summary and introduction |
| Yuan and Yin | **Markdown Pricing When Shoppers Delegate to AI Agents** | 2026 | SSRN working paper | title only |
| Wang | **Artificial Intelligence (AI) Assistant in Online Shopping: A Randomized Field Experiment on a Livestream Selling Platform** | 2025 | Information Systems Research | search summary |
| Brynjolfsson | **What Is Generative AI Worth?** | 2026 | Stanford Digital Economy Lab working paper | search summary |
| Werner | **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** | 2024 | arXiv preprint | abstract |
| Egan | **Competition in Generative AI: Evidence from Consumer Demand** | 2026 | NBER Working Paper 35953 | abstract |

<details><summary>Original research question</summary>

Starting from the key economics and marketing papers already found (e.g., Egan et al. 2026; Fradkin 2025; Kaiser and Schulze 2026 Marketing Science; Werner et al. 2024 steering; Qiu et al. 2025 Marketing Science; Fish et al. 2024 LLM collusion; the 2026 Weitzman-style AI-searcher theory papers; Padilla et al. 2026), run forward and backward citation traversal in OpenAlex and Google Scholar-style web search to find remaining econ, marketing and IS papers on LLMs and consumer search, competition, prices, product variety, or welfare. Then run an adversarial check: are there papers that find NO effect, or the opposite effect, of AI assistants on search, concentration or welfare?

</details>
