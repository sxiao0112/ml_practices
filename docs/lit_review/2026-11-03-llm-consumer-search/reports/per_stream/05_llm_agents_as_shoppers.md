# LLM agents as shoppers: rationality, biases and agent markets

**Question:** Do AI shopping agents choose well for their users, and how do they behave when sellers also use AI agents?

## Short answer
**Answer:** AI shopping agents pick products that shift with list position, price anchors and wording. Position bias is the most repeated finding. In simulated markets where buyer and seller agents negotiate, one anchor can make most deals fail.

**Strength:** Medium (several 2025 and 2026 studies agree on position and anchoring, but most are preprints or single-lab audits)
- **Holds when:** Products appear in a list and the agent picks one. Top-row placement raised one model's pick rate about 5-fold.
- **Does not hold when:** The model changes. GPT-5.1 favored the bottom row where Claude Sonnet 4 favored the top.
- **Still unknown:** Whether these biases hold on full shopping sites with real money at stake.

## Background
Shopping agents read product lists and choose items for a user. Companies now offer them in chat tools and browsers. Researchers ask whether these choices match the user's own preferences and stay consistent. They also ask what happens when seller agents answer buyer agents.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM agent | A large language model that takes actions, such as browsing or buying, for a user. |
| Revealed preference | A preference inferred from the choices a person or agent makes. |
| GARP | A test that checks whether choices contain contradictions, such as A chosen over B, then B over A. |
| CCEI | A score from 0 to 1 that measures how close choices come to passing GARP. Higher is more consistent. |
| Position bias | A tendency to pick items because of where they appear in a list. |
| Anchoring | A tendency to judge a price by an earlier number, such as a first offer. |
| Decoy effect | A tendency to prefer an option when a third, worse option makes it look better. |
| Framing | How the same choice is worded, which can change the answer. |
| Persona | A role given to an agent, such as "economist," that shapes its behavior. |
| Benchmark | A shared task set used to score and compare systems. |
| ACES audit | A 2025 audit framework that tests which products shopping agents pick. |
| WebShop | A 2022 benchmark where agents buy products from a simulated online shop. |
| ShoppingBench | A 2025 benchmark with harder shopping tasks and over 2.5 million products. |
| ShoppingComp | A 2025 benchmark that uses real web products and safety checks. |
| Task success rate | The share of tasks an agent completes correctly. Higher is better. |
| Agent-to-agent negotiation | Buyer and seller agents bargain over a price without a human in the loop. |
| Simulated marketplace | A computer model of buyers and sellers that tests how markets behave. |
| Market efficiency | The share of possible value that buyers and sellers capture in a market. Higher is better. |
| Preprint | A paper posted before peer review, such as on arXiv or SSRN. |
| SSRN | An online repository of economics and social science working papers. |
| NBER | The National Bureau of Economic Research, which also posts working papers. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Revealed-preference tests | Check whether agent choices follow consistent rules. | Chen et al. (2023), Wen (2025) | Contested |
| Bias audits of product lists | Change one feature, such as position, and track picks. | ACES audit (Allouah 2025) | Emerging |
| Anchoring and decoy experiments | Insert a price or extra option and measure the shift. | Hantel (2026), Valkanova (2024) | Contested |
| Negotiation and market simulations | Let buyer and seller agents deal, then count outcomes. | Risky Game (2025), Magentic Marketplace (2025) | Emerging |
| Shopping benchmarks | Score agents on fixed buying tasks. | WebShop (2022), ShoppingBench (2025) | Established |


## What the evidence shows

### Finding 1: Product position changes what agents buy.
- **ACES audit (Allouah 2025):** Tested 64 listings in 8 categories with six models → Top-row placement raised one model's pick rate about 5-fold. Other models showed weaker or reversed effects.
- **ACES audit (Allouah 2025):** Told the agent to ignore position → The effect stayed, so the instruction did not fix it.
- **Magentic Marketplace (2025):** Simulated agents across a full market → Every model showed a strong first-offer advantage.
- **Strength:** Medium. The effect appears across six models and two simulations, but the main audit is a single-lab preprint.

### Finding 2: Labels and seller wording change agent choices.
- **ACES audit (Allouah 2025):** Added an "Overall Pick" tag → Raised a product with a 10% share to 20% to 43%, depending on the model. Sponsored tags lowered share for all models.
- **ACES audit (Allouah 2025):** Seller agent rewrote one product description → Raised that product's share by 4 to 15 points in most model pairs.
- **Strength:** Medium. The result is large and significant, but it comes from one audit and one set of categories.

### Finding 3: Anchors can collapse simulated markets.
- **Hantel SSRN (2026a):** One anchoring sentence given only to sellers → Cut market efficiency from 96% to 15% in a five-seller market.
- **Hantel SSRN (2026b):** Naming the bias in a warning → Recovered about 40% of the loss. This is a search snippet, not a full text.
- **Takenami et al. (2025):** Seller agents in negotiation → Showed anchoring similar to humans. Reasoning models were less affected.
- **Strength:** Low to medium (one author's working papers, full text not available).

### Finding 4: Decoy effects appear in some tests and not in others.
- **Valkanova and Yordanov (2024):** GPT-3.5 and GPT-4 acted as recruiters → Showed a significant decoy effect, which a warning did not remove.
- ACES audit (Allouah 2025) and Hantel SSRN (2026b), shopping agents → Largely ignored decoy products.
- **Strength:** Low. The results conflict, and no matched shopping test exists in the sources found.

### Finding 5: Weaker agents lose money in agent-to-agent deals.
- **Risky Game (2025):** Buyer and seller agents bargained over 50 real products → Weaker models made more out-of-budget deals. Qwen2.5-7B made 11.8%, GPT-4.1 made 2.2% (lower is better).
- **Risky Game (2025):** Seller model choice mattered more than buyer model choice → A price-reduction gap of 14.9% versus 2.6%.
- **Strength:** Medium. The study covers many models and products, but it uses simulated budgets and a workshop venue.

### Finding 6: Rationality holds in simple tasks and breaks under framing.
- **Chen et al. (2023):** GPT made budget choices in four domains → Choices looked largely rational, above human scores in the literature. Language framing changed scores.
- **Wen (2025):** Agents with specialist personas → Violated GARP more often than generalist GPT.
- Fed FEDS (2026) and framing study (2026), logically equivalent prompts → Shifted choices in seven of eight model families.
- **Strength:** Medium for framing sensitivity. Low for GARP on shopping, because no study has run that test on shopping choices.

### Finding 7: Shopping benchmarks show low success on realistic tasks.
- **WebShop (2022):** Best agent with 1.18 million products → 29% task success. Human experts reached 59%.
- **ShoppingBench (2025):** 3,310 user instructions → Best model, GPT-4.1, succeeded on under 50% of tasks.
- **ShoppingComp (2025):** Real open-web products → GPT-5.2 scored 17.8% answer F1, versus 30.0% for human experts (version 2).
- **Strength:** Medium. The benchmarks use different scoring rules, and the ShoppingComp versions report different numbers.

## Where researchers disagree

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do agents fall for decoys? | Valkanova (2024): yes, in recruiter choices | ACES audit and Hantel (2026): largely no, in shopping | Matched decoy tests on the same products and models. |
| Does reasoning help against anchors? | Takenami (2025): reasoning models resist anchoring | Hantel (2026): step-by-step reasoning raises anchoring | Market tests comparing reasoning and non-reasoning modes. |
| Are LLM choices rational? | Chen (2023): largely rational, above human scores | Wen (2025) and framing studies: fragile | Repeated GARP tests on the same shopping choices. |

## Gaps

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Agent choices compared with the user's past purchases | Shows whether agents match what people want | AgenticShop (2026) uses profile checklists |
| GARP or CCEI on repeated shopping choices | Tests consistency where people spend money | Chen (2023) on budget tasks |
| Matched decoy tests on shopping agents | Current results conflict | ACES audit, Hantel (2026) |
| Real purchases with real money | Simulated budgets may hide true losses | Risky Game (2025) |
| Seller response to ranking rules | Shows whether markets reward gaming agents | ACES audit seller test |

## Papers cited

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| ACES audit | **What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** | 2025 | arXiv preprint | full text (first part) |
| Chen (2023) | **The Emergence of Economic Rationality of GPT** | 2023 | PNAS | abstract |
| Wen (2025) | **Economic Rationality under Specialization: Evidence of Decision Bias in AI Agents** | 2025 | arXiv preprint | abstract |
| Hantel (2026a) | **Small Bias, Large Failure: Anchoring Collapses a Market of Language-Model Agents** | 2026 | SSRN working paper | search snippet |
| Hantel (2026b) | **When Biased Agents Trade: Anchoring, Exploitation, and Market Failure in Agent-to-Agent Interactions** | 2026 | SSRN working paper | search snippet |
| Takenami (2025) | **How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations** | 2025 | EMNLP 2025 Findings | abstract |
| Valkanova (2024) | **Irrelevant Alternatives Bias Large Language Model Hiring Decisions** | 2024 | Findings of EMNLP 2024 | search snippet |
| Risky Game (2025) | **The Automated but Risky Game: Modeling and Benchmarking Agent-to-Agent Negotiations and Transactions in Consumer Markets** | 2025 | arXiv preprint | full text (results) |
| Magentic Marketplace (2025) | **Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets** | 2025 | arXiv preprint | search snippet |
| WebShop (2022) | **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents** | 2022 | NeurIPS 2022 | search snippet |
| ShoppingBench (2025) | **ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents** | 2025 | AAAI 2026 | search snippet |
| ShoppingComp (2025) | **ShoppingComp: Are LLMs Really Ready for Your Shopping Cart?** | 2025 | arXiv preprint | search snippet |
| Framing study (2026) | **Framing Effects in Independent-Agent Large Language Models** | 2026 | arXiv preprint | search snippet |
| Fed FEDS (2026) | **What Do LLMs Want?** | 2026 | Federal Reserve FEDS working paper | search snippet |

<details><summary>Original research question</summary>

How well do LLM agents perform as delegated shoppers on behalf of consumers (agentic commerce)? Cover choice rationality and consistency (e.g., GARP tests, revealed preference), behavioral biases (position, anchoring, decoy effects), benchmarks for shopping agents (WebShop, ShoppingBench and successors), alignment of agent choices with the user's true preferences, and market-level effects when sellers and buyers both use AI agents (agent-to-agent negotiation, simulated marketplaces).

</details>
