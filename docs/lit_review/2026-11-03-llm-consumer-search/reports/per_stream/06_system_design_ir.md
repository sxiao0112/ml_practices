# Designing LLM systems for product and consumer search

**Question:** Which LLM design choices for product search have measured gains, and how large are those gains?

## Short answer
**Answer:** Three designs have company A/B test evidence. LLM query rewriting gives small sales gains on Taobao, with +1.57% sales on rare queries. Distilling an LLM relevance judge into a small ranker raised add-to-cart rates by 0.8% at Walmart. Generative retrieval with semantic IDs adds about 1% to 2% in several Chinese platform tests.

**Strength:** Medium (one full-text rewriting test and one full-text ranking test, with the other numbers from summaries)
- **Holds when:** Queries are rare or the traffic is long-tail → gains are larger, such as +1.57% sales versus +0.40% overall.
- **Does not hold when:** Queries are common and well served → the overall gain is small, about +0.4%.
- **Still unknown:** Whether clarifying questions or review-based answers help real shoppers in live traffic.

## Background
Shopping search has long relied on keyword matching. Keyword matching struggles when shoppers describe needs in plain language. LLMs can read such requests, rewrite them, ask follow-up questions and summarize products. This page covers which of these designs have shown real gains in company tests.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model, a text model trained on large text collections. |
| Query rewriting | Changing a shopper's search text into wording that the search index matches better. |
| Long-tail query | A rare search that few shoppers type, often with unusual words. |
| Clarifying question | A question the system asks to learn what the shopper wants. |
| Semantic ID | A short code that stands for a product, learned from its content. |
| Generative retrieval | A model that outputs product codes directly instead of scoring a list. |
| Distillation | Training a small model to copy the outputs of a large model. |
| Relevance judge | A model that scores how well a product matches a search. |
| Simulated user | A language model that plays a shopper to test a system. |
| A/B test | A live test that splits traffic between two versions and compares results. |
| GMV | Gross merchandise value, the total value of goods sold. |
| ATC | Add-to-cart, when a shopper places an item in the shopping cart. |
| HIT@10 | Hit rate at 10, the share of test searches where the right item appears in the top 10. |
| BERT-base | A small language model that reads a query and an item together to score a match. |
| GTE | A text embedding model that turns queries and items into vectors for dense retrieval. |
| NDCG | A ranking score that rewards placing good items near the top. |
| RAG | Retrieval-augmented generation, which adds retrieved documents to the prompt before answering. |
| Product QA | Answering shopper questions about a specific product. |
| BM25 | A classic keyword-matching method for search. |
| Dense retrieval | Matching queries and products as vectors in a shared space. |

## Main approaches
The table lists the main ways researchers approach this question. Each approach has a different level of evidence.

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| LLM query rewriting | An LLM rewrites the shopper's search into wording the index matches. | BEQUE (Taobao), IterQR (Meituan) | Emerging |
| Distilled relevance judge | A large LLM labels relevance, and a small model serves live traffic. | Walmart distillation | Emerging |
| Generative retrieval | A model outputs product codes directly as candidates. | TSGR, VARG, CQ-SID, ICEGR | Emerging |
| Clarifying questions | The system asks questions to narrow down the shopper's need. | ProductAgent, Zou 2020 | Contested |
| Simulated shoppers | An LLM plays the shopper to test the system. | ProductAgent, ConvApparel, CustomerSim | Contested |
| Review-grounded product QA | Retrieved reviews and specs feed an LLM answer. | RAGE, Flipkart PQA | Emerging |

## What the evidence shows
### Finding 1: LLM query rewriting gives small sales gains, mostly on rare queries.
- **BEQUE (Taobao, 2024)**: A fine-tuned Qwen 7B model rewrites queries, then learns from search feedback. The 14-day test raised sales 0.40% overall and 1.57% on long-tail queries.
- **IterQR (Meituan, 2025)**: Iterative LLM rewriting for delivery search. The abstract claims significant gains but gives no numbers.
- **Strength:** Medium. One full-text company test shows the effect. The second paper has no numbers.

### Finding 2: A distilled LLM relevance judge improves shopper engagement at Walmart.
- **Walmart distillation (Walmart, 2025)**: A Mistral-7B teacher trains a BERT-base student for relevance. A two-week tail-traffic test raised add-to-cart per session by 0.8%.
- **Walmart ranking study (Walmart, 2024)**: LLM features in ranking gave neutral sales and conversion results in online tests.
- **Strength:** Medium. One full-text test is positive and one is neutral. The paper does not flag which lifts are significant.

### Finding 3: Generative retrieval with semantic IDs adds about 1% to 2% in sales across several platforms.
- **TSGR (Taobao, 2026)**: Value-aware generative retrieval gave a 1.64% sales lift in an online test.
- **VARG (Tmall, 2026)**: Generated candidates enter the final ranker. A 14-day test on 20% of traffic gave a 1.45% sales lift.
- **CQ-SID (TmallAPP, 2026)**: Semantic cluster IDs add candidates to recall. A two-week test gave a 1.15% sales lift.
- **ICEGR (Baidu, 2026)**: End-to-end generative retrieval gave a 7.53% sales lift, the largest reported. This number is from a search summary.
- **Strength:** Low. Four company tests agree on small gains. Most numbers come from summaries, not full texts.

### Finding 4: Clarifying questions help in simulation, but real shoppers tire after about 11 questions.
- **ProductAgent (2025)**: An LLM agent asks questions and a simulator answers. Top-10 hit rate with BM25 reached 39.48 with GPT-4 in the conversational setting.
- **Zou 2020**: A live study asked shoppers yes or no questions. Shoppers answered about 11 questions on average before quitting.
- **Strength:** Low. The main result uses a simulator with no human check. The live study uses a small sample and reports numbers that vary by version.

### Finding 5: Simulated shoppers differ from real shoppers, so simulator results may mislead.
- **ConvApparel (2026)**: A dataset of human-AI shopping chats shows a significant realism gap for all simulators.
- **CustomerSim (2026)**: Retail simulators are fluent but less varied, and they drift from assigned personas.
- **Strength:** Medium. Two benchmark papers report the same weakness. Neither was read in full.

### Finding 6: Review-based answers have offline evidence only.
- **RAGE (2019)**: Retrieves review snippets, filters noise and generates an answer. It beats older methods on two offline datasets.
- **Flipkart PQA (2025)**: Uses RAG over specs, reviews and shopper context. It proposes an evaluation protocol, but its results were not read.
- **Strength:** Low. Every result is offline, and one result was not verified.

## Where researchers disagree
The table lists the main open disagreements. Each row names the test that would settle it.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do simulators predict real shoppers? | ProductAgent: simulator results show clear gains | ConvApparel, CustomerSim: simulators differ from humans | A live test with real shoppers |
| Does LLM relevance help sales? | Walmart distillation: add-to-cart gains | Walmart ranking study: sales neutral | A replicated test with all business metrics |
| Which retriever works in dialogue? | ProductAgent: BM25 beats dense retrieval in dialogue | ProductAgent: dense GTE wins in standard search | Tests on real shopper answers, not option picks |

## Gaps
The table lists open gaps. Each gap names the closest existing work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Live test of clarifying questions | Simulated gains may not hold for real shoppers | Zou 2020 (small live study only) |
| Live test of review-based product QA | Wrong answers can mislead buyers | Flipkart PQA (offline only) |
| Human check of shopper simulators | Simulators guide system design choices | ConvApparel (gap measured, no fix) |
| Full numbers for generative retrieval tests | Lifts from summaries cannot be checked | ICEGR (number from summary) |

Amazon reports that Rufus users are 60% more likely to buy. Amazon did not publish a controlled test or a method, so this claim is unverified.

## Papers cited
The table lists every paper named on this page. The last column shows how much of each paper was read.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| ProductAgent | **ProductAgent: Benchmarking Conversational Product Search Agent with Asking Clarification Questions** | 2025 | EMNLP 2025 Industry Track | full text |
| Zou 2020 | **An Empirical Study of Clarifying Question-Based Systems** | 2020 | CIKM 2020 | search summary and excerpts |
| ConvApparel | **ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders** | 2026 | EACL 2026 | abstract |
| CustomerSim | **CustomerSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators** | 2026 | NeurIPS 2026 (listed) | search summary |
| BEQUE | **Large Language Model based Long-tail Query Rewriting in Taobao Search** | 2024 | ACM (DOI 10.1145/3589335.3648298) | full text |
| IterQR | **IterQR: An Iterative Framework for LLM-based Query Rewrite in e-Commercial Search System** | 2025 | arXiv preprint | abstract |
| Walmart distillation | **Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models** | 2025 | arXiv preprint | full text |
| Walmart ranking study | **Towards More Relevant Product Search Ranking Via Large Language Models: An Empirical Study** | 2024 | arXiv preprint | abstract and snippet |
| TSGR | **TSGR: Taobao Search Generative Retrieval** | 2026 | arXiv preprint | search summary |
| VARG | **VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce Search** | 2026 | arXiv preprint | search summary |
| CQ-SID | **Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL** | 2026 | arXiv preprint | search summary |
| ICEGR | **ICEGR: An Intent-Coherent End-to-End Generative Retrieval** | 2026 | arXiv preprint (WSDM 2027 listed) | search summary |
| RAGE | **Review-Driven Answer Generation for Product-Related Questions in E-Commerce** | 2019 | arXiv preprint | abstract |
| Flipkart PQA | **Contextually Aware E-Commerce Product Question Answering using RAG** | 2025 | arXiv preprint | search snippet |

<details><summary>Original research question</summary>

What CS/IR research shows how to better design LLM-based systems for consumer and product search: conversational product search, clarifying questions and preference elicitation, retrieval-augmented generation over catalogs and reviews, LLM query understanding and rewriting in e-commerce, generative retrieval, product QA, comparison/summarization of options, and evaluation methods (offline metrics, simulated users, online A/B tests at companies like Amazon, Alibaba, Walmart, Instacart)? Which design choices have demonstrated gains and of what size?

</details>
