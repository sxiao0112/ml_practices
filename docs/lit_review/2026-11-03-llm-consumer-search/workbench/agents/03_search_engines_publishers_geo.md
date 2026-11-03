# How do LLM answer engines (Google AI Overviews, Bing Copilot, Perplexity, ChatGPT search) affect the search ecosystem: click-through and traffic to websites and publishers ('zero-click'), search advertising markets and ad placement in LLM answers, and the rise of generative engine optimization (GEO) — how sellers and content creators try to get cited or recommended by LLMs? Include economics of content provision, ad auctions for LLM outputs, and measurement studies.

## TL;DR
Answer: LLM answer engines reduce clicks to publisher sites, with click drops of 35% to 48% in several studies. Ad auctions for LLM answers exist only as theory and simulation. GEO rewrites raise visibility in answers by up to 40% in controlled benchmarks, but no reviewed technique shows a stable effect on live platforms.
Strength: Medium (click loss, two experimental designs plus industry data). Low for ad auctions and for GEO on live systems.
Traffic loss is the best-supported part. Ad and GEO claims rest on theory, simulations, or controlled tests. Industry click studies are not peer-reviewed.

## What Exists
### Sub-theme 1: Zero-click traffic and publisher referrals
- **AI Overviews field test** (Agarwal and Sen, 2026, SSRN) — Randomly hid AI Overviews for 1,065 Chrome users. Outbound organic clicks fell 39.8% and zero-click searches rose 34.5%. Read via search summary, not full text.
  - Relevance: Strongest causal evidence on clicks. Authors call results exploratory.
  - OpenAlex ID: W7149011595
  - Cited by: 3
- **AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence** (Wang, Gleason, Bart, Wilson and Metaxa, 2026, arXiv) — Preregistered field experiment, N=1,100 Google users. Removing AI Overviews and AI Mode raises click-through to publishers. Abstract gives no effect sizes.
  - Relevance: Second experiment supports the direction. Magnitude unknown from abstract.
  - OpenAlex ID: W7203917671
  - Cited by: 0
- **Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain** (Shi, Zhu and Gu, 2026, arXiv) — Comscore desktop clickstream. Wider ChatGPT Search access cuts traditional search use by 9.4%. ChatGPT sends outbound clicks in 5.2% of sessions. Largest losses in informational categories.
  - Relevance: Shows the substitution channel and category pattern from browsing logs.
  - OpenAlex ID: W7167813029
  - Cited by: 0
- **Beyond Search** (Gholami, Firullo, Cheyre and Acquisti, 2026, Georgetown KGI working paper) — LLM use mostly sits alongside search. Traffic after LLM queries spreads across more destinations. Read via search summary; title taken from the file name, not checked.
  - Relevance: Counter-view. Losses concentrate less than in other studies.
  - OpenAlex ID: not found
  - Cited by: not checked
- **Industry click studies** — Pew 2025, Ahrefs, Authoritas, Seer and SISTRIX. Click-through falls 35% to 48% when AI summaries appear, per press coverage. Not peer-reviewed. Excluded from paper count.
  - Relevance: Shows the size of click loss in practice. Google disputes the Pew sample.

### Sub-theme 2: Who loses traffic and how publishers respond
- **Strategic Response of News Publishers to Generative AI** (Zhao and Berman, 2025, arXiv) — Difference-in-differences on large publishers. Bot blocking via robots.txt reduces traffic. Publishers shift to content that is harder to copy.
  - Relevance: Shows the cost of blocking AI crawlers and a content response.
  - OpenAlex ID: W7118007976
  - Cited by: 0
- **Search Log note on smaller sites** — A 2026 AEA conference paper reports no drop for the most-visited sites and a marked drop for smaller sites. Title and full text not retrieved. Excluded from paper count.
  - Relevance: Supports size-based heterogeneity. Needs the title before citing.

### Sub-theme 3: Ad auctions and advertising inside LLM answers
- **Mechanism Design for Large Language Models** (Dütting, Mirrokni, Paes Leme, Xu and Zuo, 2024, WWW) — Token auction: bidders' LLMs each bid per token. Payments resemble Vickrey (second-price) rules. Prompt-tuned experiments on a public LLM show smooth shifts with bid share.
  - Relevance: Foundational theory of auctions inside generated text. No live deployment.
  - OpenAlex ID: W4396723524
  - Cited by: 23
  - Arxiv version: W4387806061 (cited by 0)
- **Auctions with LLM Summaries** (Dubey, Feng, Kidambi, Mehta and Wang, 2024, arXiv) — Factorized auction plus LLM module. Claims welfare-maximizing, incentive-compatible summaries. Supported by theory and synthetic experiments.
  - Relevance: Auctions for multi-ad summaries, closer to answer engines.
  - OpenAlex ID: W4394838760
  - Cited by: 0
- **Ad Auctions for LLMs via Retrieval Augmented Generation** (authors not checked, 2024, NeurIPS per DOI) — Places ads per text segment via retrieval. Repeated single-ad auctions raise more revenue. Multi-ad auctions raise output quality. Read via search summary.
  - Relevance: Revenue-quality trade-off in ad placement. Simulation-based.
  - OpenAlex ID: W4415798338
  - Cited by: 5
- **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** (authors not checked, 2025, ACM) — Participants rated ad versions lower across the questionnaire. Authors link this to wariness about sponsored results. Read via search summary.
  - Relevance: Only controlled user study of ads in chatbot answers found.
  - OpenAlex ID: W4416926286
  - Cited by: 12
- **Perplexity Publishers' Program** — Revenue sharing per cited ad answer. Perplexity reportedly winds down ads by end of 2026 citing trust. Press reports only. Excluded from paper count.

### Sub-theme 4: Generative engine optimization (GEO)
- **GEO: Generative Engine Optimization** (Aggarwal et al., 2024, KDD) — Nine rewriting methods on GEO-bench. Best methods raise position-adjusted word count by 41%. Cite Sources gains 115% at rank 5 but loses 30% at rank 1. Keyword stuffing gives little gain.
  - Relevance: Origin of GEO. Gains depend on initial rank and domain.
  - OpenAlex ID: W4401864200
  - Cited by: 63
  - Arxiv version: W4388788661 (cited by 4)
- **Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)** (Martinez, 2026, arXiv) — Survey of 45 studies. Topical relevance and position are the most reproducible levers. No reviewed technique shows a stable, longitudinal, cross-platform causal effect.
  - Relevance: Most direct critique of GEO gains. Says the GEO benchmark gains hold only when the source is already in context.
  - OpenAlex ID: W7169212596
  - Cited by: 0
- **Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots** (Wen, Zhang, Yuan, Chen, Zhang and Guo, 2026, arXiv, ICML 2026 position track) — Argues GEO can concentrate influence and hide commercial influence. Says offline setups diverge from deployed systems. No percentage given.
  - Relevance: Governance and disclosure angle. Positions GEO as a policy issue.
  - OpenAlex ID: not checked
  - Cited by: not checked

### Sub-theme 5: Citation patterns and source concentration
- **News Source Citing Patterns in AI Search Systems** (Yang, 2025, arXiv) — Analyzed about 366,000 citations from OpenAI, Perplexity and Google systems. About 9% cite news. News citations concentrate on few outlets. Cited news leans liberal.
  - Relevance: Shows which publishers gain AI citations. Bias size not given in abstract.
  - OpenAlex ID: W4416059753
  - Cited by: 0
- **Answer Bubbles: Information Exposure in AI-Mediated Search** (authors not checked, 2026, arXiv) — Perplexity gives at least one citation for 74.5% of queries. Google AI Overviews gives one for 57.8%. Read via search summary.
  - Relevance: Coverage difference across engines. Affects which publishers can be cited.
  - OpenAlex ID: not checked
  - Cited by: not checked

## Reference Chain Discoveries
- Found via: GEO related-work section — Kumar and Lakkaraju (2024), an adversarial product-visibility paper the GEO authors contrast with theirs. Not read.
- Found via: Mechanism Design citers (OpenAlex) — "Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms" (SSRN 2026, DOI 10.2139/ssrn.7662578). SSRN blocked automated fetch. Title only.
- Found via: Ad auction searches — "LERA: LLM-Enhanced RAG for Ad Auction in Generative Chatbots" (arXiv 2605.16474, 2026). Title only.
- Found via: Ad auction searches — "LLM Advertisement based on Neuron Auctions" (arXiv 2605.08326, 2026). Search summary only.
- Found via: Ad auction searches — "Truthful Aggregation of LLMs" (arXiv 2405.05905, 2024). Not read.
- Found via: GEO citers (OpenAlex) — "From Clicks to Citations: Generative AI Search, Zero-Click Behaviour, and the Rise of Generative Engine Optimization" (SSRN 2026, DOI 10.2139/ssrn.7517778). Title only.
- Found via: GEO critique search (OpenAlex) — "Retrieval Governs Synthesis: A Forensic Audit of Generative Engine Optimization (GEO) Benchmarks, Replication Failures, and Provenance in RAG Pipelines" (Zenodo 2026). Unreviewed. Not read; if its replication claims hold, they would lower GEO confidence.
- Found via: Padilla, Lam, Lambrecht and Hollenbeck (2025), reported by a journal-club summary, claiming adopters' search volume fell more than 20%. Not found in search or OpenAlex. Not counted.

## What's Missing (Gaps)
- Live auction data from deployed answer engines. Only theory and synthetic tests exist.
- Long-run GEO effects on live engines across platforms. The survey finds none reviewed.
- Causal estimates of publisher revenue loss from AI referrals, not just clicks.
- Non-US evidence. The field tests and clickstream studies use US users.
- Ad effects on user trust with real ad load and labeling. One controlled study found.
- Consumer-product GEO, where sellers compete for recommendations. Covered by other streams.

## Contradictions or Tensions
- Total traffic: Agarwal and Sen (2026) and Wang et al. (2026) find large click losses. Gholami et al. (2026) finds traffic spreads to more destinations. The AEA paper finds big sites unaffected. Different outcomes and samples explain part of this.
- GEO gains: Aggarwal et al. (2024) report up to 40% visibility gain. Martinez (2026) says the gain is conditional on the source already being in context and is not durable. Both could be true, but the GEO benchmark does not test deployed engines.
- Source concentration: Yang (2025) finds news citations concentrate on few outlets and lean liberal. The abstract does not quantify the bias.
- Industry vs academic click loss: Pew (2025) reports clicks of 8% vs 15% with and without summaries. Google disputes the sample. Academic designs use different populations.

## Confidence
High/Medium/Low
- Click loss from AI answers: Medium. Two experimental designs agree on direction, but both are preprints or drafts and the magnitude differs.
- Ad auctions in LLM answers: Low. Theory and simulations only, plus one user study.
- GEO on live platforms: Low. Controlled gains only, with a 2026 survey saying the effect is not shown stable.
- What would raise confidence: A published version of Agarwal and Sen (2026) with replication in another country. Effect sizes from Wang et al. (2026). A deployed-engine auction pilot with revenue data.
- What would lower confidence: Evidence that the click drops come mostly from low-value searches. Replication failures of the GEO benchmark claims (see the Zenodo audit above).

## Search Log
### Round 1: Broad search
- Queries: "generative engine optimization GEO paper visibility LLM answers Aggarwal 2024"; "Google AI Overviews click-through rate zero-click search publishers traffic study"; "advertising in LLM generated answers ad auction mechanism design sponsored content chatbot"; "LLM search engines reduce referral traffic to websites economics content providers SSRN NBER 2025"; "Perplexity ChatGPT search citation sources news publishers measurement study 2025 arXiv"
- Papers found: about 15 candidate sources, of which 8 academic and about 7 industry or press. Industry sources excluded from count.
- Key leads: GEO (Aggarwal 2024), Mechanism Design (Dütting 2024), Answering Without Referring (Shi 2026), Yang (2025), Pew (2025, industry).

### Round 2: Citation traversal
- Papers traversed: GEO (OpenAlex W4401864200), Mechanism Design (W4396723524), SSRN AI Overviews field experiment (W7149011595).
- New papers from references: GEO's six reference IDs resolved to titles. They are classic search and QA benchmarks (PageRank paper, Natural Questions, MS MARCO, ORCAS-I, hallucination survey, an SEO survey). None is a GEO or auction paper.
- New papers from citers: GEO citers (top 10 by citations) mostly marketing and education GEO papers, low relevance. Mechanism Design citers (top 10) mostly LLM mechanism-design papers, including Dubey 2024 indirectly. Field experiment citers: 3 unrelated papers.
- Hop 2 applied: none, because no 2-hop paper had over 50 citations and was directly relevant.

### Round 3: Reference section mining
- Papers mined: GEO (arXiv HTML v3, related work and per-method numbers), Mechanism Design (arXiv HTML, first 100,000 characters of 133,524; related work read).
- Authors' comments: GEO contrasts with Kumar and Lakkaraju (2024), calls traditional SEO inapplicable, and unifies evidence-based answer generation work. Mechanism Design contrasts with RLHF and robust mechanism design, and lists 3 follow-up works.

### Round 4: Gap-filling
- Gaps targeted: exact title and design of the SSRN field experiment; ad user-trust studies; publisher payment models; the Padilla et al. paper.
- Queries: "Padilla Lam Lambrecht Hollenbeck generative AI search traffic websites Stack Overflow adoption"; "Agarwal Sen randomized experiment Google AI Overviews outbound clicks zero-click redistribution of value"; "LLM answer engine advertising ad placement user trust experiment sponsored results in chatbot answers study"; "Perplexity publisher revenue sharing program content licensing deals generative AI economics paper"
- New findings: Agarwal and Sen title confirmed via OpenAlex (authors Agarwal and Sen). Ads that Talk Back (user-trust study) found. Padilla et al. paper not found in search or OpenAlex. Perplexity program found, press-only.

### Round 5: Adversarial check
- Gaps targeted: critiques of GEO gains; position papers on GEO risks.
- Queries: OpenAlex search "generative engine optimization critique limitations" (2025-2026 filter); WebFetch of the Martinez survey and Wen et al. position.
- New findings: Martinez (2026) survey critiques the 40% figure as conditional on the source already being in context. Wen et al. (2026) raise concentration and disclosure risks. Zenodo GEO benchmark audit found but unreviewed.

### Round 6: Follow citation leads on ad auctions and traffic
- Papers traversed: citers of Mechanism Design (arXiv and WWW IDs); Yang (2025) and Answer Bubbles IDs confirmed.
- New leads: "Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms" (SSRN 2026). Abstract not retrieved because SSRN blocks automated fetch. Title only.
- Dubey et al. 2024 abstract read.

### Convergence note
- Total unique relevant papers found: 14 (9 read at abstract or full-text level, 5 from search summaries only). Industry, press and unread leads are excluded from this count.
- New papers in last round: 1 (Monetizing Intelligence, unreadable). Round 5 added 2 readable critiques.
- Stopped because: The last round added no new readable papers. The eight-round hard cap was not reached. The Padilla paper remains unverified, and SSRN content is blocked, so ad-economics coverage is thin.
