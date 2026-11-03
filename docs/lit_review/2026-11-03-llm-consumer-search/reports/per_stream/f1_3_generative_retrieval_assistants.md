# Deployed LLM shopping assistants and generative retrieval: what works at scale

**Question:** Which large language model systems for product search run in production, and what do their online tests and cost or latency numbers show?

## Short answer
**Answer:** Generative retrieval with semantic IDs is the most tested deployed design. Platform A/B tests report order or sales gains of about 1-3%. Query rewriting and relevance distillation show similar small gains. Amazon Rufus describes its design but publishes no latency, cost or A/B numbers.

**Strength:** Medium (several companies run live tests, but most numbers are self-reported and only four papers were read in full)
- **Holds when:** the model adds a candidate channel or a reranker → orders +1.3% to +3.2% in platform tests.
- **Does not hold when:** a pure generator replaces the whole pipeline without a reranker → orders fall 0.69%.
- **Still unknown:** how often production models invent item codes. No paper reports this rate.
- **Still unknown:** whether conversational assistants raise sales. No controlled test is published.

## Background
Shopping sites now use large language models (LLMs) to understand queries and find products. This page asks which such systems run in production and what evidence they report. Most of the key evidence comes from online A/B tests, where live users see either the new system or the old one.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| A/B test | Live test that shows some users the new system and others the old one. |
| GMV | Gross merchandise value: total value of orders placed. |
| CTR | Click-through rate: share of shown results that get a click. |
| CVR | Conversion rate: share of clicks that end in a purchase. |
| SID (semantic ID) | Short code of a few tokens that names an item. Similar items get similar codes. |
| Generative retrieval | A language model writes item codes directly instead of searching an index. |
| Recall channel | One source of candidate items that feeds the ranking step. |
| Reranker | Model that re-orders a short candidate list by predicted relevance or purchase. |
| Distillation | Training a small model to copy the outputs of a larger model. |
| Query rewriting | Changing a user's search query into a clearer query before retrieval. |
| Long-tail query | Rare query with few past searches, where standard systems often fail. |
| Hallucination | Output that does not match the query or is not in the catalog. |
| RAG (retrieval-augmented generation) | The model answers from text it fetched from a database first. |
| Relevance judge | Model that scores how well an item matches a query. |
| Decision agent | Post-processing step that selects items from generated candidates. |
| OPEX | Operating expenditure: the running cost of a system per period. |
| Latency | Time one request takes to finish. |
| FP8 | 8-bit number format that speeds up model inference. |
| ACC | Accuracy: share of test cases the model gets right. |
| Dual-tower model | Two encoders, one for queries and one for items, scored by similarity. |
| Add-to-cart | Click that places an item in the shopping cart. |
| eCPM | Expected revenue per thousand ad impressions. |

## Main approaches
The main ways teams attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Generative retrieval with semantic IDs | A model writes item codes instead of an index lookup | OneSearch, Hi-Gen, HierGR, WeGR | Established |
| LLM relevance judges, distilled | A large model labels relevance and a small model serves | Walmart distillation, TaoSR1, Walmart dense retrieval | Established |
| LLM query rewriting | A model rewrites queries, tuned with search feedback | BEQUE, IterQR | Established |
| Reasoning distillation against hallucination | Teach the generator to reason, then filter its output | Alipay hallucination paper | Emerging |
| Conversational shopping assistants | A chat model answers from reviews and catalog data | Rufus blog, Retail-GPT | Emerging |

## What the evidence shows
### Finding 1: Generative retrieval adds about 1-3% in platform A/B tests.
- **OneSearch (Kuaishou team 2025)**: a pure generator replaced the mall search pipeline. Orders rose 3.22% with a reranker and fell 0.69% without one.
- **Hi-Gen (Wu 2024)**: a generator added items to recall. A one-week test on 4% of users per arm gave GMV +1.42%.
- **HierGR (Xia 2025)** and **SMGR (Meituan team 2026)**: food-delivery search. Orders rose 0.68% for complex intents, and revenue rose 1.12%.
- **WeGR (Tencent team 2026)**: a two-month test in Tencent's shopping search. Orders rose 2.54%, and GPU use fell 26.1%.
- **Strength:** Medium — several companies and live tests, but most tables give no significance marks.

### Finding 2: Reasoning distillation can cut irrelevant generated results.
Here, hallucination means generated results that do not match the query. The Alipay team distilled reasoning into the generator and added a decision agent.
- **Alipay hallucination paper (Shen 2025)**: offline accuracy rose from 83.83% to 87.17% in fund search.
- **Alipay hallucination paper (Shen 2025)**: online, trades rose 1.31% in fund search and 1.89% in insurance search.
- **Strength:** Medium — one company and a full-text read, but no before-and-after hallucination rate is reported.

### Finding 3: Distilled LLM judges help engagement, with small gains.
- **Walmart distillation (Walmart team 2025)**: a 7-billion-parameter LLM teacher trained a small BERT (encoder) model. Add-to-cart per session rose 0.8% on tail traffic.
- **Walmart dense retrieval (Rokon 2026)**: LLM labels matched trained humans 89.1% of the time. A two-week test raised ad spend 2.80%.
- **TaoSR1 (Taobao team 2025)**: a generative relevance model with FP8 and cached prompt prefixes. Latency fell from 800 ms to 286 ms (summary only).
- **Latent reasoning distillation (Qiu 2026)**: a small relevance model learns from chain-of-thought reasoning. Online gains are reported, but the abstract gives no numbers.
- **Strength:** Medium — large teams, but the latency figure comes from a secondary summary.

### Finding 4: LLM query rewriting adds small overall gains and larger gains on rare queries.
- **BEQUE (Taobao team 2024)**: a 7-billion-parameter model rewrites queries and is tuned on search feedback. GMV rose 0.40% overall and 1.57% on long-tail queries in a 14-day test.
- **IterQR (Meituan team 2025)**: rewrites feed an extra retrieval channel. An online gain is reported, but the number was not extracted.
- **Strength:** Medium — one full-text online result, and one study with no extracted numbers.

### Finding 5: Conversational assistants publish designs but few performance numbers.
- **Rufus blog (Amazon team, undated)**: a shopping-specific model, retrieval from reviews and catalog, and token streaming. No latency, cost or hallucination figure is given.
- **Instacart blog (Instacart team 2025)**: post-processing filters invented categories. No A/B result is given.
- **Workflow-graph agent (2025)**: authors not verified. A commerce messenger agent needs tool calls in its first turns to avoid made-up answers.
- **Retail-GPT (2024)**: authors not verified. It showed one significant hallucination in 80 tool-use tests, a small offline test.
- **Strength:** Low — company posts and small offline tests only.

## Where researchers disagree
The sources disagree on three points. Each row shows both views and the test that would settle it.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Can a pure generator replace the pipeline? | OneSearch reports a full replacement at lower running cost (OPEX) | The pure OneSearch variant lowers orders without a reranker | Replication with the same reranker and cost data |
| Do LLM judges match humans? | Zalando labels agree with humans about as often as humans agree | Zalando reports that LLM judges are often too strict | Human re-labeling of the same queries with agreement scores |
| Do relevance gains reach sales? | Walmart distillation: add-to-cart +0.8% on tail traffic | Etsy blog: engagement can fall while relevance rises | Joint reporting of relevance and purchases on the same test |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Rate of invented item codes in production | Shows how often users see wrong items | Alipay hallucination paper (accuracy only) |
| Latency and cost of assistants under live load | Decides whether assistants fit search budgets | Rufus blog (no numbers) |
| Live tests at Shopify, eBay or Etsy | Few public assistant tests exist outside China | Etsy relevance blog (no A/B result) |
| Independent replication of company gains | Most gains come from self-reported tests | OneSearch and WeGR (self-reported) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| OneSearch | **OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search** | 2025 | arXiv preprint | full text |
| Hi-Gen | **Hi-Gen: Generative Retrieval For Large-Scale Personalized E-commerce Search** | 2024 | arXiv preprint | summary of arXiv text |
| HierGR | **HierGR (exact title not verified)** | 2025 | ACL 2025 Industry Track | abstract snippet |
| SMGR | **Multimodal Generative Retrieval Model with Staged Pretraining for Food Delivery on Meituan** | 2026 | arXiv preprint | search summary |
| WeGR | **WeGR (exact title not verified)** | 2026 | arXiv preprint | summary |
| Alipay hallucination paper | **Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search** | 2025 | SIGIR 2025 | full text |
| Latent reasoning distillation | **Thinking Broad, Acting Fast: Latent Reasoning Distillation from Multi-Perspective Chain-of-Thought for E-Commerce Relevance** | 2026 | WWW 2026 Industry Track | abstract |
| TaoSR1 | **TaoSR1: The Thinking Model for E-commerce Relevance Search** | 2025 | arXiv preprint | summary |
| Walmart distillation | **Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models** | 2025 | WWW 2025 Companion | full text |
| Walmart dense retrieval | **Scaling Dense Retrieval with LLM-Annotated Training Data: Structured Mining and Progressive Curriculum for E-Commerce Sponsored Search** | 2026 | arXiv preprint | abstract |
| BEQUE | **Large Language Model based Long-tail Query Rewriting in Taobao Search** | 2024 | ACM (DOI listed) | full text |
| IterQR | **IterQR: An Iterative Framework for LLM-based Query Rewrite in e-Commercial Search System** | 2025 | arXiv preprint | abstract and search snippet |
| Rufus blog | **The technology behind Amazon's GenAI-powered shopping assistant, Rufus** | undated | Amazon Science blog | full blog post |
| Instacart blog | **Building The Intent Engine: How Instacart is Revamping Query Understanding with LLMs** | 2025 | Instacart tech blog | search summary |
| Retail-GPT | **Retail-GPT: leveraging Retrieval Augmented Generation (RAG) for building E-commerce Chat Assistants** | 2024 | arXiv preprint | summary |
| Workflow-graph agent | **A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs** | 2025 | arXiv preprint | summary |
| Zalando evaluation | **Retrieve, Annotate, Evaluate, Repeat: Leveraging Multimodal LLMs for Large-Scale Product Retrieval Evaluation** | 2024 | arXiv preprint | abstract and company blog |
| Etsy blog | **How Etsy Uses LLMs to Improve Search Relevance** | 2025 | Etsy Code as Craft blog | search summary |

<details><summary>Original research question</summary>

Complete the coverage of deployed LLM systems for product search: generative retrieval and semantic-ID methods, LLM query rewriting, and conversational shopping assistants deployed in production (Amazon Rufus, Instacart, Shopify, Walmart, Alibaba, JD, Meituan, Etsy, eBay, Zalando). What architectures, online A/B results and lessons (latency, hallucination, cost) are reported?

</details>
