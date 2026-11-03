# What CS/IR research shows how to better design LLM-based systems for consumer and product search: conversational product search, clarifying questions and preference elicitation, retrieval-augmented generation over catalogs and reviews, LLM query understanding and rewriting in e-commerce, generative retrieval, product QA, comparison/summarization of options, and evaluation methods (offline metrics, simulated users, online A/B tests at companies like Amazon, Alibaba, Walmart, Instacart)? Which design choices have demonstrated gains and of what size?

## TL;DR
Answer: The strongest evidence covers three design choices. LLM query rewriting trained with search-system feedback gives small GMV gains on Taobao (+0.40% overall, +1.57% on long-tail queries). Distilling a large LLM relevance judge into a small ranker gives engagement gains at Walmart (+0.8% add-to-cart per session). Generative retrieval with semantic IDs gives 1-2% GMV gains in several Chinese platform A/B tests. Clarifying questions help offline, but a live study found users tire after about 11 questions. Product-review RAG has offline evidence only.
Strength: Medium
Lifts from company A/B tests are small and come from different platforms, metrics and durations, so they are not directly comparable. Most of the numbers below come from full text or abstracts. Several come only from search snippets and are marked as such.

## What Exists
### Sub-theme 1: Clarifying questions and preference elicitation
- **ProductAgent: Benchmarking Conversational Product Search Agent with Asking Clarification Questions** (authors not verified, 2025, EMNLP 2025 Industry Track) — An LLM agent asks clarifying questions and retrieves items. Full text read. An LLM user simulator answers using the ground-truth item. HIT@10 with BM25 on GPT-4 reaches 39.48 (conversational setting, Table 5).
  - Relevance: Closest match to conversational product search with clarifying questions. Evaluation relies only on the LLM simulator, with no human users.
  - OpenAlex ID: W4416037268
  - Cited by: 1
- **An Empirical Study of Clarifying Question-Based Systems** (Zou, Kanoulas, Liu, 2020, CIKM; arXiv 2008.00279 title, CIKM title may differ slightly) — An online study asked users yes/no clarifying questions to find a product. Users answered about 11 questions on average before quitting. About 12-17% of answers contradicted the target product description (version-dependent).
  - Relevance: Real users, not simulators. Shows fatigue limits on how many questions a system can ask.
  - Source read: search summary and PDF excerpts, not full text.
- **Learning to Ask: Question-based Sequential Bayesian Product Search** (authors not verified, year not verified, venue not verified) — Sequential Bayesian question selection for product search.
  - Relevance: Earlier question-selection method. Found in search only, not read.
- **Wizard of Shopping: Target-Oriented E-commerce Dialogue Generation with Decision Tree Branching** (authors not verified, 2025, ACL 2025) — A dialogue dataset for shopping assistants that ask clarifying questions.
  - Relevance: Training data for conversational product search. Found in search only, not read.
- **Flippi: End To End GenAI Assistant for E-Commerce** (authors not verified, 2025, arXiv 2507.05788) — An end-to-end LLM shopping assistant. The authors say targeted follow-up questions matter for a complete conversational experience.
  - Relevance: System-level design example. No ablation seen in the excerpt.

### Sub-theme 2: Simulated users and evaluation of conversational systems
- **ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders** (authors not verified, 2026, EACL 2026) — A dataset of human-AI shopping conversations. Abstract read. Reports a "significant realism gap" for all simulators, but no numbers in the abstract.
  - Relevance: Direct evidence that LLM simulators differ from human shoppers. Data-driven simulators beat a prompted baseline on unseen behaviors.
  - OpenAlex ID: not found
- **CustomerSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators** (authors not verified, 2026, NeurIPS 2026) — Retail simulators are fluent but show lower lexical diversity and drift from personas. Found in search, not read.
  - Relevance: Reports the same simulator weaknesses as ConvApparel, for retail.
- **Shoppers Also Asked: Generating Related Questions for E-commerce Search** (Kuzi, Chen, Malmasi, 2025, SIGIR eCom'25) — An LLM generates candidate related questions, then selects the best ones. Evaluated on TREC Product Search with LLM and human annotation. No online test seen.
  - Relevance: Shows an offline-evaluated design for question suggestions on results pages.
- **FABRIC: Fully-automated broad intent categorization in e-commerce** (Amazon, 2025, EMNLP 2025 Industry) — Builds evaluation labels for broad intent classification from clicks, relevance predictions and LLM judgments. Found in search, not read.
  - Relevance: Evaluation method for query intent, not a deployed classifier.

### Sub-theme 3: Retrieval-augmented generation over reviews and product QA
- **Learning to Trust: Dynamic Utilization of Retrieval-Augmented Generation for E-commerce Search Relevance** (authors not verified, 2026, ACM DOI 10.1145/3805712.3808439; arXiv 2510.11122) — RAG adds product context to a relevance model. Abstract read. Abstract reports "consistent lifts" in GSB and Item Goodrate without numbers. A search summary reports +10.37% GSB on question-style queries (from snippet, not confirmed in the abstract).
  - Relevance: Shows RAG as a relevance aid, not as answer generation. Gains are largest on noisy query slices.
  - OpenAlex ID: W7168349820
  - Cited by: 0
- **Contextually Aware E-Commerce Product Question Answering using RAG** (authors not verified, 2025, arXiv 2508.01990, Flipkart) — End-to-end RAG framework for product QA using specs, reviews and user context. Also proposes an evaluation protocol. Results not seen in snippet.
  - Relevance: Most direct RAG-over-catalog and reviews design. Evidence not verified.
- **Review-Driven Answer Generation for Product-Related Questions in E-Commerce** (Chen et al., 2019, venue not verified, arXiv 1905.01994, Alibaba) — RAGE retrieves review snippets, filters noise, then generates an answer. Reported as outperforming alternatives on two datasets. Offline only.
  - Relevance: Older baseline for review-grounded product QA.

### Sub-theme 4: Comparison and summarization of options
- **"This Suits You the Best": Query Focused Comparative Explainable Summarization** (authors not verified, 2025, arXiv 2507.04733) — Compares LLMs on query-focused summaries of products. Scored on seven quality dimensions. Offline only.
  - Relevance: Model choice for comparison summaries.
- **LLMs as Architects and Critics for Multi-Source Opinion Summarization** (Attri et al., 2025, arXiv 2507.04751) — Abstract not read. A search summary described metadata-enriched summaries with about 87% participant preference and Spearman 0.74 with human judges. These claims are unverified, and the match to this title is unconfirmed.
  - Relevance: Strongest engagement evidence for summaries, but a user study, not a storefront A/B test.
- Flippi (see Sub-theme 1, not a new paper): the compare flow produces pros, cons and a verdict sentence. No engagement test in excerpt.

### Sub-theme 5: LLM query understanding and rewriting
- **Large Language Model based Long-tail Query Rewriting in Taobao Search** (authors not verified, 2024, ACM DOI 10.1145/3589335.3648298, deployed on Taobao since October 2023; arXiv 2311.03758) — BEQUE. Fine-tunes Qwen 7B on rewrites, then aligns it with search-system feedback. Full text read. 14-day online A/B test: all queries GMV +0.40%, transactions +0.34%, UV +0.33%. Long-tail queries GMV +1.57%, transactions +2.52%, UV +2.32%. Offline hit rate 17.27 for proposed vs 12.95 for previous Taobao rewriter.
  - Relevance: Best-documented online LLM rewriting result. Gains small overall, concentrated in long-tail traffic.
  - OpenAlex ID: W4396843633
  - Cited by: 62
- **Enhancing E-Commerce Query Rewriting: A Large Language Model Approach with Domain-Specific Pre-Training and Reinforcement Learning** (authors not verified, 2024, venue not verified) — Domain pretraining plus RL for rewriting. Title only, not read.
  - OpenAlex ID: W4403577343
  - Cited by: 8
- **IterQR: An Iterative Framework for LLM-based Query Rewrite in e-Commercial Search System** (authors not verified, 2025, arXiv 2504.05309, Meituan) — Iterative rewriting with retrieval augmentation and online signals. Abstract read. Reports "significant improvement" on Meituan delivery search, without numbers.
  - Relevance: Rewriting for delivery search, not general e-commerce.
- **RL-based Query Rewriting with Distilled LLM for online E-Commerce Systems** (authors not verified, 2025, arXiv 2501.18056) — Distills an LLM rewriter into a smaller model trained with RL. Reports offline results on Amazon ESCI. Found in search, not read.
- **Relevance Matters: A Multi-Task and Multi-Stage Large Language Model Approach for E-commerce Query Rewriting** (authors not verified, 2026, arXiv 2603.02555) — Multi-task rewriting. Search snippet reports online A/B gains including more purchases per user, numbers not extracted.
- **Synthetic Data Powers Product Retrieval for Long-tail Knowledge-Intensive Queries in E-commerce Search** (authors not verified, 2026, arXiv 2602.23620, Taobao) — LLM pipeline routes long-tail knowledge-heavy queries. Search summary reports a 4-week online test on 10% of long-tail traffic, largest gain on negation-type queries. Numbers not seen.
- **Related Intent Generation for grocery search** (authors not verified, 2026, arXiv 2607.27172) — Closed LLMs generate intents offline, small models serve them. Offline evaluation only, per the snippet.
- Instacart intent engine (blog, November 2025, not a paper): industry write-up, not a paper. LLM category classification and rewrites for long-tail queries. No A/B result seen in excerpt. Not counted as a paper.

### Sub-theme 6: LLM relevance judges distilled into production rankers
- **Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models** (authors not verified, 2025, arXiv 2505.07105) — Teacher: Mistral-7B with LoRA. Student: BERT-base cross-encoder. Full text read. Offline: student +12.84% recall at 95% precision and +1.5% NDCG@5 versus the XEv1 baseline. Two-week A/B test (August 26 to September 9, 2024) on tail traffic: add-to-cart per session +0.8%, per visitor +1.2%, search abandonment -0.6%. Authors call the gains statistically significant, but the table does not mark which lifts are significant.
  - Relevance: Strongest deployed evidence for LLM-as-relevance-judge via distillation.
- **Towards More Relevant Product Search Ranking Via Large Language Models: An Empirical Study** (authors not verified, 2024, arXiv 2409.17460, Walmart) — LLM-based features in online A/B tests. Business metrics such as GMV and conversions were neutral. Abstract and snippet only.
  - Relevance: Shows relevance gains without engagement loss. Also shows no business-metric gain.

### Sub-theme 7: Generative retrieval with semantic IDs
- **GRAM: Generative Retrieval and Alignment Model: A New Paradigm for E-commerce Retrieval** (authors not verified, 2025, arXiv 2504.01403) — Aligns generative retrieval identifiers with query terms. Abstract read. Claims offline and online A/B gains, with no numbers in abstract. JD.com affiliation not confirmed.
  - Relevance: Addresses the query-ID mismatch in semantic-ID retrieval.
- **CAT-ID2: Category-Tree Integrated Document Identifier Learning for Generative Retrieval In E-commerce** (authors not verified, 2025, WSDM 2026, arXiv 2511.01461) — Adds category tree to semantic ID learning. Search snippet only.
- **Beyond Matching: Category-Guided Latent Intent Reasoning for Generative Retrieval in E-Commerce** (authors not verified, 2026, arXiv 2606.07075) — Targets the gap between attribute-heavy queries and abstract IDs. Search summary reports gains on Amazon ESCI (offline).
- **ICEGR: An Intent-Coherent End-to-End Generative Retrieval** (Baidu, 2026, WSDM 2027, arXiv 2608.29652) — Online A/B: CTR +3.52%, orders +15.96%, GMV +7.53% (from search summary, not verified).
- **TSGR: Taobao Search Generative Retrieval** (Taobao, 2026, arXiv 2607.18796) — Adds value awareness to items and candidate ranking. Online: IPV +0.43%, transactions +1.12%, GMV +1.64% (from search summary).
- **VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce Search** (Tmall, 2026, arXiv 2609.14493) — 14-day online test on 20% of search traffic: GMV +1.45% (from search summary).
- **Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL** (TmallAPP, 2026, arXiv 2605.14434) — Semantic cluster IDs as a recall supplement. Two-week online test: GMV +1.15%, UCTCVR +0.40% (from search summary).
- **Don't Rewrite the SID Map: Topology Preservation for Generative Retrieval in Dynamic E-Commerce Search** (TmallAPP, 2026, arXiv 2610.26105) — Studies ID drift when mappings update. Three-week online test: UCTCVR +0.29%, GMV +1.16% (from search summary).
- **GSID: Generative Semantic Indexing for E-Commerce Product Understanding** (Xianyu, 2025, arXiv 2509.23860) — Reports GMV +1% and transactions per user +0.3% for generative retrieval (from search summary).
- **Cross-stream, recommendation setting:** QuaSID (Kuaishou, arXiv 2603.00632) — semantic ID tokenizer for recommendation, not search. Not counted.

### Sub-theme 8: Deployed assistants and company claims
- Amazon Rufus (company posts and press, 2024 onward, not a paper): Company says customers who use Rufus are 60% more likely to complete a purchase. No controlled A/B design or method published. Not counted as a paper.

## Reference Chain Discoveries
- Found via: BEQUE (OpenAlex references). Query-rewriting lineage: QUEEN (Wang et al., 2021), Query Rewriting in TaoBao Search (2022), Query Rewriting via Cycle-Consistent Translation for E-Commerce Search (2021), Diversity driven Query Rewriting in Search Advertising (2021), Enhancing E-commerce Product Search through RL-Powered Query Reformulation (2023), Intent Term Weighting in E-commerce Queries (2019).
- Found via: BEQUE (OpenAlex references). Embedding retrieval in e-commerce: Embedding-based Product Retrieval in Taobao Search (2021), Embedding-based Retrieval in Facebook Search (2020), Towards Personalized and Semantic Retrieval (2020).
- Found via: BEQUE (OpenAlex references). Preference alignment and LLM methods named in the paper: Preference Rank Optimization (Song et al., 2023), DPO (Rafailov et al., 2023), query2doc (Wang et al., 2023), Learning to summarize from human feedback (2020).
- Found via: Learning to Trust (OpenAlex references). RAG and retrieval background: The Probabilistic Relevance Framework: BM25 and Beyond (2009), Adaptive-RAG (2024), RA-ISF (2024), Learning deep structured semantic models (2013).
- Found via: ProductAgent (related-work list in full text). Feng et al. 2023 (MAS2S), Lee et al. 2023 (CAMBIGNQ), Chang and Chen 2024 (SalesAgent), Vedula et al. 2024 (product clarification questions). Not read in full.
- Found via: ProductAgent citers (OpenAlex). ConServe: Traceable State- and Constraint-Aware Intelligent System for Multi-Turn Product Recommendation (2026). Not read.
- Found via: BEQUE citers (OpenAlex). Enhancing E-Commerce Query Rewriting with LLMs (2024) and Complicated Semantic Alignment for Long-Tail Query Rewriting in Taobao Search (2025, OpenAlex W4412877077). Title only.
- Found via: Round 4 gap search. An Empirical Study on Clarifying Question-Based Systems (Zou et al., 2020) and Walmart distillation paper.

## What's Missing (Gaps)
- No published online A/B test of RAG over reviews for product QA was found. All product-QA RAG evidence is offline.
- No live A/B test of attribute-based clarifying questions versus a control in e-commerce search was found. Google's conversational filtering docs describe the design but report no results.
- No live test of LLM comparison summaries measuring clicks or purchases was found. Evidence is offline or from small user studies.
- No benchmark combines conversational product search, preference elicitation, and calibrated LLM simulators with human validation. ProductAgent validates its simulator against nothing.
- Amazon Rufus has company-reported engagement claims only. No methods or controlled comparison were found.
- Walmart and Instacart: one Walmart deployment paper found. Instacart evidence is a blog post.

## Contradictions or Tensions
- Simulators versus humans: ProductAgent reports strong gains as the conversation grows, using an LLM simulator. ConvApparel and CustomerSim report that LLM simulators diverge from human shoppers. Zou et al. (2020) found users quit after about 11 questions. Simulated gains may overstate what real users accept.
- Dense versus sparse retrieval in conversational search: ProductAgent finds BM25 beats GTE and CoROM in conversational settings (HIT@10 39.48 vs 8.27 for GTE on GPT-4). In traditional setting, GTE wins (HIT@10 69.00 vs 34.80). The authors attribute this to option-choice answers favoring exact term matching.
- LLM reranking gains: a 2026 ICEB study found LLM reranking raised NDCG@5 from 0.922 to 0.961 over dense retrieval, with Hit@5 unchanged. Walmart's sponsored-search study found few-shot GPT-4 accuracy 63.02%, far below fine-tuned models. Gains depend on setup.
- Relevance versus engagement: Walmart's Towards More Relevant Product Search Ranking found neutral GMV and conversions. Walmart distillation found add-to-cart gains. Relevance gains do not always reach purchases.
- Generative retrieval gains: most Chinese platform A/B tests show GMV gains of 1-2%. ICEGR reports 7.53% GMV, the largest lift seen. Its number comes from a search summary, not a verified full text.

## Confidence
Medium
- What would raise confidence: Full-text reading of ICEGR, TSGR, VARG and CQ-SID tables to confirm GMV numbers and significance.
- What would raise confidence: Human-user replication of ProductAgent's clarifying-question gains, or a live A/B test of clarifying questions.
- What would lower confidence: A finding that the GMV gains in company tests come from traffic or metric changes rather than the design choice. Most tests lack public significance reporting.

## Search Log
### Round 1: Broad search
- Queries: conversational product search clarifying questions LLM e-commerce 2025; RAG product reviews QA e-commerce online A/B test; LLM query rewriting e-commerce online A/B Alibaba Amazon Walmart; generative retrieval product search semantic IDs e-commerce arXiv; simulated users LLM conversational product search preference elicitation benchmark
- Papers found: 5 usable leads from about 50 results
- Key leads: ProductAgent (2407.00942), BEQUE (2311.03758), Learning to Trust (2510.11122), GRAM (2504.01403), ConvApparel (2602.16938)

### Round 2: Citation traversal
- Papers traversed: ProductAgent (OpenAlex W4416037268, 0 references in OpenAlex), BEQUE (W4396843633, 18 references, 62 citations), Learning to Trust (W7168349820, 5 references)
- New papers from references: BEQUE references yielded query-rewriting lineage and embedding-retrieval papers. Learning to Trust references were BM25 and DSSM background only.
- New papers from citers: BEQUE citers were mostly general LLM surveys and recommender reviews, plus one e-commerce rewriting paper (2024, W4403577343). ProductAgent citers: one 2026 multi-turn recommender system (ConServe).

### Round 3: Reference section mining
- Papers mined: ProductAgent (full HTML at arxiv.org/html/2407.00942v1), BEQUE (full HTML at arxiv.org/html/2311.03758v3)
- Gaps targeted: exact results, simulator validation, related-work positioning
- New papers from related work: Feng et al. 2023 (MAS2S), Lee et al. 2023 (CAMBIGNQ), Chang and Chen 2024 (SalesAgent), Vedula et al. 2024, Li et al. 2022 (CLE-QR), Wang et al. 2021 (QUEEN). Not read in full.
- Note: abstract-only fetches returned no numbers. Full HTML fetches supplied numbers.

### Round 4: Gap-filling
- Gaps targeted: production LLM search evidence at Amazon, Walmart, Instacart; comparison summaries; clarifying questions online
- Queries: Amazon Rufus LLM online A/B test; LLM comparison summary e-commerce online experiment; Walmart or Instacart LLM relevance A/B 2025; clarifying questions e-commerce online A/B attribute questions
- New findings: Walmart distillation paper (2505.07105) with A/B test; Zou et al. (2020) online clarifying-question study; M-OS and "This Suits You the Best" summaries; Rufus claim (company only)

### Round 5: Adversarial check
- Gaps targeted: critiques of simulators, negative results, RAG hallucination
- Queries: LLM user simulator realism gap critique; LLM reranking e-commerce negative result; hallucination RAG product QA limitations
- New findings: ConvApparel realism gap (EACL 2026); CustomerSim (NeurIPS 2026) retail simulator weaknesses; ICEB 2026 reranking small gain; no e-commerce RAG hallucination paper found in 2025
- Walmart distillation numbers verified from full text (Round 5 fetch)

### Round 6: Lead following
- Papers checked: Learning to Trust abstract (no numbers in abstract, 8 authors); Zou et al. (2020) via search summary; IterQR abstract (no numbers)
- New papers: Zou et al. (2020) "An Empirical Study on Clarifying Question-Based Systems" (arXiv 2008.00279)

### Round 7: Verification and generative-retrieval gap
- Papers checked: GRAM abstract (no numbers in abstract); ConvApparel abstract (no dataset size or numbers)
- Queries: generative retrieval e-commerce semantic ID online A/B 2026
- New papers from this round: TSGR, VARG, CQ-SID (EG-GRPO), SID topology paper, GSID, ICEGR (all with online results from search summaries). Several are from 2026 and not read in full.
- New relevant papers this round: about 6

### Round 8: Final gap-filling (cap)
- Queries: LLM query understanding e-commerce production A/B 2025-2026; Amazon SIGIR eCom 2025 related question generation
- New papers: Taobao synthetic long-tail retrieval (2602.23620), grocery related intent generation (2607.27172), FABRIC (Amazon), Shoppers Also Asked (Kuzi et al.)
- New relevant papers this round: 4

### Convergence note
- Total unique relevant papers found: 32 (plus 1 cross-stream recommendation paper, not counted)
- New papers in last round: 4
- Stopped because: Hard cap of 8 internal rounds reached. Round 7 and Round 8 still added new relevant papers, so the search had not converged. Papers from generative retrieval and query rewriting remain under-sampled.
- Full-text reads: 3 (ProductAgent, BEQUE, Walmart distillation). Abstract reads: 5. Search-snippet only: the rest.
- Not performed: cross-check of 2026 arXiv numbers against full text for most generative-retrieval papers.
