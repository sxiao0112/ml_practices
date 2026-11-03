# Complete the coverage of deployed LLM systems for product search: generative retrieval and semantic-ID methods, LLM query rewriting, and conversational shopping assistants deployed in production (Amazon Rufus, Instacart, Shopify, Walmart, Alibaba, JD, Meituan, Etsy, eBay, Zalando). What architectures, online A/B results and lessons (latency, hallucination, cost) are reported?

## TL;DR
Answer: Most deployed evidence comes from Chinese platforms and Walmart. Generative retrieval with semantic IDs (Kuaishou OneSearch, Alibaba Hi-Gen, Meituan HierGR and SMGR, Tencent WeGR) reports online order or GMV lifts of about 1-3%. Alipay reports that reasoning distillation plus a decision agent cuts irrelevant generated results, with +1.31% to +2.07% trade lifts. Amazon Rufus publishes an architecture but no latency, cost, hallucination or A/B numbers. No Shopify, eBay or Etsy paper with online LLM results was found. Instacart and Etsy describe deployed LLM systems only in engineering blogs.
Strength: Medium
Most platform numbers are self-reported. Only a few are read from full text (OneSearch, Alipay, Walmart distillation, Walmart dense retrieval). The rest come from abstracts or search summaries and are marked as such. Lifts from different platforms, metrics and durations are not directly comparable.

## What Exists
### Sub-theme 1: Generative retrieval with semantic IDs in production search
- **OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search** (Kuaishou team, 2025, arXiv preprint; ICML 2026 proceedings) — A single encoder-decoder replaces the multi-stage search pipeline on Kuaishou mall search. The best variant, with a reward-model reranker, gives order volume +3.22%, buyer volume +2.40%, PV CVR +1.78% (higher is better) versus the pipeline. The pure generative variant is negative on orders (-0.69%).
  - Relevance: Full-text read. Clearest deployed end-to-end design, with a cost claim (OPEX 24.60% of pipeline, versions differ).
  - Relevance: Test duration not stated. The paper does not discuss hallucination or invalid-ID rates.
  - OpenAlex ID: W4417094648
  - Cited by: 1
- **OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework** (Chen et al., 2026, arXiv 2603.24422, Kuaishou) — Adds query-understanding reasoning distilled into the generator without extra inference cost. A third-party summary reports item CTR +3.98%, buyer CVR +3.05%, order volume +2.11%.
  - Relevance: Follow-up to OneSearch. Online numbers come from a summary, not the paper's table, so they are unverified.
  - OpenAlex ID: W7140663666
  - Cited by: 0
- **Hi-Gen: Generative Retrieval For Large-Scale Personalized E-commerce Search** (Wu et al., 2024, arXiv 2404.15675, Alibaba) — Hierarchical encoder-decoder generates document IDs for extra recall. One-week live test with 4% of users per arm: GMV +1.42%, PayCount +0.92%, CVR +1.51%, CTR +0.83%.
  - Relevance: Read from arXiv search summaries. The paper also reports a +0.56% latency change in its table, despite claiming no added latency.
  - OpenAlex ID: W4395483237
  - Cited by: 2
- **HierGR (Xia et al., 2025, ACL Industry Track)** — Generative retrieval for food-delivery search at Meituan. Reported online order gain of +0.68% for complex search intents.
  - Relevance: Abstract-level snippet only. Latency handled by a query cache and pairing with an online dense retriever.
- **Multimodal Generative Retrieval Model with Staged Pretraining for Food Delivery on Meituan** (Meituan team, 2026, arXiv 2602.06654, called SMGR here) — Multimodal generative retrieval with staged pretraining. One-week test on 10% of Meituan traffic against a dual-tower baseline: revenue +1.12%, CTR +1.02%, clicks +0.72%, CPC +0.19%.
  - Relevance: Search-summary reading. CPC direction (higher or lower is better) depends on the advertiser's objective.
- **Generative Retrieval with Preference Optimization for E-commerce Search** (Li et al., 2024, arXiv 2407.19829, reported as JD.com work) — Generative retrieval trained with preference optimization for e-commerce search.
  - Relevance: Title and secondary-source affiliation only. Online results not read.
  - OpenAlex ID: W4402963795
  - Cited by: 1
- **WeGR: unified generative retrieval for WeChat e-commerce search** (Tencent team, 2026, arXiv 2610.16979) — Codebook tokenizer (CoCo-VAE) plus a second component (DHPO) for WeChat e-commerce search. Two-month online A/B: orders +2.539%, CTR +1.508%, CVR +1.381%. CPU use -25.5%, GPU use -26.1%.
  - Relevance: Summary reading (alphaxiv). The authors note the test compares whole systems, so component gains cannot be separated.
- **TSGR: Taobao Search Generative Retrieval** — already in the workbench (06 file). Not counted.

### Sub-theme 2: LLM relevance judges and distillation into production rankers
- **Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search** (Shen et al., 2025, SIGIR, arXiv 2503.21098) — Generative retrieval for Alipay fund and insurance search. Reasoning from a larger LLM is distilled into the generator, and a decision agent filters the output. Offline ACC: fund 83.83% to 87.17%, insurance 85.83% to 90.05%. Online (fund overall): Click_PV +2.84%, Trade_Count +1.31%, Trade_UV +0.99%.
  - Relevance: Full-text read (HTML). Hallucination is defined as generated documents irrelevant to the query. The paper gives no before-and-after rate.
  - Relevance: Latency of the decision agent and test length not stated. Significance is stated in text, not per cell.
  - OpenAlex ID: W4412394915
  - Cited by: 4
- **Thinking Broad, Acting Fast: Latent Reasoning Distillation from Multi-Perspective Chain-of-Thought for E-Commerce Relevance** (Qiu et al., 2026, arXiv 2601.21611, WWW 2026 industry track) — Distills chain-of-thought reasoning into a small relevance model with a latent reasoning extractor. Online A/B on an e-commerce search advertising platform.
  - Relevance: Abstract read. Abstract gives no metric names or percentages.
  - OpenAlex ID: W7126163891
  - Cited by: 0
- **TaoSR1: The Thinking Model for E-commerce Relevance Search** (Taobao and Tmall team, 2025, arXiv 2508.12365) — Generative LLM relevance model trained with chain-of-thought, DPO and GRPO. Serving latency falls from about 800 ms to 286 ms with FP8, prefix caching and batching.
  - Relevance: Latency figures from secondary summaries. Full paper not read. Online gains beat BERT baselines per summary.
- **Explainable LLM-driven Multi-dimensional Distillation for E-Commerce Relevance Learning** (Zhao et al., 2025, arXiv 2411.13045, Taobao and Tmall) — Distills an explainable LLM relevance model into online models, with online experiments on search ads.
  - Relevance: Title and summary only. Numbers not read.
  - OpenAlex ID: W4410636343
  - Cited by: 1
- **Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models** (Walmart team, 2025, arXiv 2505.07105) — A 7B LLM teacher trains a BERT-base student. Two-week A/B on tail traffic: add-to-cart per session +0.8%, search abandonment -0.6%. Already in workbench (06 file). Not counted.
- **Retrieval-GRPO: A Multi-Objective Reinforcement Learning Framework for Dense Retrieval in Taobao Search** (Liu et al., 2025, arXiv 2511.13885) — Dense retriever trained with RL rewards that include LLM relevance scores. Authors say it is deployed on Taobao.
  - Relevance: Dense retrieval, not generative. Included because the reward comes from an LLM. Summary reading only; metrics not read.

### Sub-theme 3: LLM query rewriting and understanding in production
- **Large Language Model based Long-tail Query Rewriting in Taobao Search** (BEQUE) — already in workbench. Not counted.
- **IterQR: An Iterative Framework for LLM-based Query Rewrite in e-Commercial Search System** — already in workbench. Its Meituan delivery A/B is used as a retrieval channel. Lift not extracted. Not counted.
- **Relevance Matters: A Multi-Task and Multi-Stage Large Language Model Approach for E-commerce Query Rewriting** — already in workbench. Not counted.
- **Instacart "Building The Intent Engine" (engineering blog, 2025)** — Not a paper. LLM re-ranks candidate categories with store context. Post-processing guardrails filter hallucinated categories. No A/B numbers in the post.

### Sub-theme 4: Conversational shopping assistants and hallucination control
- **Amazon Rufus engineering blog (Amazon Science, 2024-2025)** — Not a paper. Describes a shopping-specific LLM, retrieval from reviews and catalog, token streaming, and model choice for cost and latency. Gives no latency, cost, hallucination or A/B numbers.
- **Retail-GPT: leveraging Retrieval Augmented Generation (RAG) for building E-commerce Chat Assistants** (authors not verified, 2024, arXiv 2408.08925) — RAG-based e-commerce chat assistant. Tool-invocation test reports 1 significant hallucination in 80 instances.
  - Relevance: Offline test, small sample. Summary reading.
- **Production-Grade Conversational Agents with Workflow Graphs** (authors not verified, 2025, arXiv 2505.23006) — Case study of a commerce messenger agent. Reports that the first turns need external tool calls to avoid hallucination.
  - Relevance: Summary reading. No A/B result.
- **Hallucination Detection in LLM-enriched Product Listings** (authors not verified, 2024, ECNLP workshop) — Two-phase detector for hallucinated attributes in LLM-written product listings. Recall-first phase then precision-first phase.
  - Relevance: Catalog hallucination, not search answers. Snippet only.

### Sub-theme 5: LLM relevance evaluation at retailers
- **Retrieve, Annotate, Evaluate, Repeat: Leveraging Multimodal LLMs for Large-Scale Product Retrieval Evaluation** (Hosseini and Kober, 2024, arXiv 2409.11860, Zalando) — Multimodal LLM writes per-query annotation guidelines and labels results. Human-LLM agreement is reported as on par with human-human agreement.
  - Relevance: Abstract and blog read. Accepted at ECIR 2025 per a secondary source, unverified. Speed and cost claims come from news summaries.
- **Enhancement of E-commerce Sponsored Search Relevancy with LLM** (Walmart AdTech authors, 2024 workshop, posted to arXiv 2607.03886) — LoRA fine-tuned Llama 2 7B classifies query-ad pairs as relevant, partly relevant or irrelevant.
  - Relevance: Abstract read. No online test found. A third-party accuracy figure (89.43%) is not confirmed.
- **Scaling Dense Retrieval with LLM-Annotated Training Data: Structured Mining and Progressive Curriculum for E-Commerce Sponsored Search** (Rokon et al., 2026, arXiv 2606.23911, Walmart) — LLM labels with 89.1% agreement with trained human annotators. Two-week online A/B: ad spend +2.80%, CTR +1.4%, eCPM +2.8%, click conversion +2.9%.
  - Relevance: Abstract read. Gives no latency or serving cost. Traffic is tens of millions of requests per arm.

## Reference Chain Discoveries
- Found via: OneSearch OpenAlex record (no references resolved). OneSearch-V2 and the Kuaishou OneSug family are linked. OneSug (AAAI 2026, query suggestion) found by title only, not read.
- Found via: Alipay hallucination paper references (OpenAlex). Multiview Identifiers Enhanced Generative Retrieval (2023, 37 citations) and a knowledge-graph QA paper (2024). Background only.
- Found via: Alipay hallucination paper citers (OpenAlex). Persona-design study of AI shopping agents (2026, W7167931870). Belongs to the agents stream; not counted.
- Found via: Walmart sponsored-search search results. Dense-retrieval paper 2606.23911 cited alongside Walmart distillation.

## What's Missing (Gaps)
- No online A/B result for an LLM shopping assistant from Shopify, eBay or Etsy was found in papers.
- Amazon Rufus publishes an architecture but no latency, cost or hallucination figures in any paper or blog found.
- Instacart and Etsy describe LLM deployments only in engineering blogs. No paper with A/B numbers was found.
- No production paper reports a rate of invalid or hallucinated IDs. Alipay reports only accuracy and no before-and-after hallucination rate.
- Most generative-retrieval A/B tests come from Chinese platforms. Few use the same metrics or durations.

## Contradictions or Tensions
- End-to-end versus hybrid generative retrieval: OneSearch's pure generative variant lowers orders (-0.69%). Adding a reward reranker turns orders positive (+3.22%). The paper's reranker is needed to match the pipeline.
- Latency versus relevance: TaoSR1 cuts relevance-model latency with FP8 and caching (800 ms to 286 ms). Hi-Gen reports a +0.56% latency change despite claiming none.
- Relevance versus engagement: Etsy reports engagement can fall while semantic relevance rises (summary of the Code as Craft post, not read). Walmart distillation reports add-to-cart gains.
- Size of gains: most platform generative-retrieval lifts are 1-3% in orders or GMV. ICEGR reports 7.53% GMV and WeGR reports 2.5% orders. Summary numbers differ in size and source.

## Confidence
Medium
- What would raise confidence: Full-text reading of OneSearch-V2, ICEGR, WeGR and TaoSR1 to confirm online tables and significance.
- What would raise confidence: A full-text read of the Meituan SMGR and HierGR papers to check traffic and duration.
- What would lower confidence: Evidence that the platform gains come from traffic or metric changes rather than the design. Most tests report no significance levels.

## Search Log
### Round 1: Broad web search
- Queries: Amazon Rufus architecture latency cost lessons; generative retrieval semantic ID e-commerce online A/B JD.com; LLM query rewriting e-commerce online A/B Meituan JD Etsy eBay; conversational shopping assistant hallucination latency Instacart Shopify Zalando; Alibaba LLM e-commerce semantic ID 2026; Walmart Meituan LLM product search hallucination 2026
- Papers found: about 20 usable leads
- Key leads: OneSearch (2509.03236), Alipay hallucination (2503.21098), Hi-Gen, Walmart Sponsored Search, IterQR (Meituan), GenRec (JD, recommendation)

### Round 2: Citation traversal (OpenAlex)
- Papers traversed: OneSearch (W4417094648; 0 references resolved, 1 citer), Alipay hallucination (W4412394915; 3 references, 4 citers), IterQR (W4416526818; 0 references, 0 citers)
- New papers from references: Multiview Identifiers Enhanced Generative Retrieval (2023); knowledge-graph QA retrieval (2024); boosting LLM relevance modeling with distribution-aware learning (2024)
- New papers from citers: Persona design in AI shopping agents (2026), a Tip-of-the-Tongue search analysis (2026). Both are outside this stream.
- Lookups by arXiv ID: Hi-Gen (W4395483237), GenR-PO (W4402963795), OneSearch-V2 (W7140663666), ELLM-MKD (W4410636343), latent reasoning distillation (W7126163891)

### Round 3: Reference section mining (full text)
- Papers mined: OneSearch (arXiv HTML v1, Tables 8 and text), Alipay hallucination (arXiv HTML v3, Tables 1 and 2), Walmart dense retrieval (abstract), latent reasoning distillation (abstract), Rufus engineering blog (full post), Zalando LLM-judge (abstract)
- Gaps targeted: exact online tables, hallucination definition, cost and latency numbers
- New findings: OneSearch OPEX and FLOPs utilization claims. Alipay offline accuracy and online trade lifts. Rufus post has no numeric results. Latent reasoning abstract has no numbers.

### Round 4: Gap-filling
- Gaps targeted: Kuaishou and Alibaba generative search follow-ups; Meituan delivery search; Instacart, Etsy, eBay, Zalando, Shopify; Alipay GR; Walmart LLM relevance
- Queries: OneSearch Kuaishou A/B; GenRec JD App; Instacart LLM query understanding; Etsy or eBay LLM search; Zalando or Shopify shopping assistant; LLMGR Alipay; Retrieval-GRPO Taobao; MMQ semantic IDs; Hi-Gen; Meituan generative retrieval; WeGR; TaoSR1; Enhancement of Sponsored Search Relevancy
- New findings: Most of the 18 counted papers came from this round and Round 1. Non-paper sources: Instacart, Etsy, Rufus blogs. eBay and Shopify: nothing. LLMGR: no arXiv record found. GenRec (2604.14878) is recommendation, excluded.

### Round 5: Adversarial check
- Gaps targeted: negative results, failed deployments, rewrite-induced hallucination, semantic-ID drift
- Queries: generative retrieval semantic ID failed online test; LLM query rewriting negative A/B; LLM relevance latency distillation Taobao
- New findings: No e-commerce negative online result found. Semantic-ID drift study (2610.26105, already in workbench) reports large HitRate drops at small beam sizes. QueryBandits (2508.16697) shows static rewrites increase hallucination regret in a non-e-commerce setting. Not counted.

### Round 6: Lead following and verification
- Papers checked: Retrieval-GRPO (2511.13885), MMQ (2508.15281, recommendation tokenizer, excluded), Walmart sponsored search (2607.03886), Zalando (2409.11860), Meituan SMGR and HierGR
- New findings: Retrieval-GRPO counted (dense retrieval, summary reading). MMQ excluded as recommendation. OneSug and Explicit Semantic Generative Retrieval kept as unverified leads, not counted.

### Convergence note
- Total unique relevant papers found: 18 new papers counted in this file, plus several already in the workbench that were re-found (not counted)
- New papers in last round: 1 (Retrieval-GRPO)
- Stopped because: Six rounds completed. Remaining leads (OneSug, Explicit Semantic Generative Retrieval, LLMGR, Beyond Keywords talk) are unverified or not papers. Stopped before the 8-round cap. Coverage of Alibaba and Tencent generative retrieval is not exhausted.

### Unverified leads (not counted)
- OneSug: E-commerce query suggestion (AAAI 2026, OpenAlex W7137881052). Title only.
- Explicit Semantic Generative Retrieval (Alibaba International, 2025). Title only.
- Beyond Keywords: Impact of LLM-Powered Search in Online Marketplaces (Gallino, 2026). Talk abstract only, no paper. Randomized field experiment, about 1.2 million sessions. Abstract claims purchased items priced 1.4-1.7% higher and faster conversion (not verified).
- LLMGR (Alipay, CIKM 2024). No arXiv record found.
- GenRec (JD App, arXiv 2604.14878). Recommendation, excluded from count.
- MMQ (2508.15281) and RecGPT-V3 (Taobao). Recommendation, excluded.
