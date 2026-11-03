# Effects on search engines, publishers, ads and generative engine optimization

**Question:** Do AI answer engines reduce clicks to websites, how do ads work inside LLM answers, and how do sellers try to get cited?

## Short answer
**Answer:** AI answer engines send fewer clicks to publisher sites. Several click studies report drops of 35% to 48%, though some find smaller or spread-out effects. Ad auctions for LLM answers exist only as theory and simulation. Controlled tests show that rewriting pages can raise their visibility in answers by up to 40%, but live effects are unproven.

**Strength:** Medium for click loss (two experimental designs, plus industry data). Low for ad auctions and for GEO (generative engine optimization) on live systems, which rest on theory or controlled tests.
- **Holds when:** Google shows an AI Overview → organic clicks fall about 40% in a randomized test with 1,065 users.
- **Does not hold when:** A site is among the most visited → traffic changes little, per one 2026 conference paper (summary only).
- **Does not hold when:** The source is missing from the context the engine reads → rewriting gives little gain (survey, 2026).
- **Still unknown:** How ads inside live AI answers change revenue and user trust.

## Background
Search engines list links, and users click them to read pages. AI answer engines write one reply instead, often with a few cited sources. This can cut the clicks that fund websites and the ads they show. Sellers and content creators now try to get their pages cited by these systems.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| AI answer engine | A chatbot or search tool that writes one answer and cites sources. |
| AI Overviews | Google's AI summary shown above its search results. |
| Zero-click search | A search where the user reads an answer and clicks no website. |
| Click-through rate | Share of users who click a link after seeing it. |
| Publisher | A site that produces news, reviews or other written content. |
| Generative engine optimization (GEO) | Methods that help a page get cited or shown in AI answers. |
| GEO-bench | A benchmark of queries and sources for testing GEO methods. |
| Ad auction | A market where advertisers bid for placement. |
| Token auction | An auction run one word piece at a time while the model writes. |
| RAG | Retrieval augmented generation: the model fetches documents, then writes from them. |
| Randomized field experiment | Real users are randomly given a feature or not, then outcomes are compared. |
| Difference-in-differences | Compares change over time between treated and untreated groups. |
| Bot blocking | A site tells AI crawlers, through robots.txt, not to read its pages. |
| Incentive compatible | Bidders gain nothing by reporting a false value. |
| Vickrey payment | A winner pays the second-highest bid, not its own bid. |
| Keyword stuffing | Repeating keywords to try to game how a page ranks. |
| SSRN | A working-paper server for economics and social science. Not peer-reviewed. |
| arXiv | A public preprint server. Papers here are not peer-reviewed. |
| KDD, WWW, ICML | Peer-reviewed conferences in data mining, the web, and machine learning. |

## Main approaches
The table lists the main ways researchers study this question.

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Field experiments | Randomly show or hide AI summaries, then measure clicks | AI Overviews test and Referral field test | Emerging |
| Browsing-log studies | Compare visits before and after access to a chatbot | Access study and Traffic spread study | Emerging |
| Publisher behavior | Track bot blocking and content changes | Publisher bot-blocking study | Emerging |
| Ad auction design | Design auctions that run inside generated text | Token auction, Summary auction and RAG ad auction | Emerging |
| Ad user studies | Show ads in chatbot answers and ask users | Talk Back study | Emerging |
| Citation audits | Count which outlets AI engines cite | Citation outlet study and Answer Bubbles study | Emerging |
| GEO benchmarks | Rewrite pages and measure visibility in answers | GEO benchmark | Contested |
| GEO critiques | Review GEO evidence and governance risks | GEO survey and GEO position paper | Emerging |

## What the evidence shows
### Finding 1: AI answers cut clicks to publisher sites.
- **AI Overviews test (Agarwal 2026)**: Randomly hid AI Overviews for 1,065 Chrome users → outbound organic clicks fell 39.8%, and zero-click searches rose 34.5%.
- **Referral field test (Wang 2026)**: Preregistered test with 1,100 Google users → removing AI summaries raised clicks to publishers. The abstract gives no effect size.
- **Industry data (Pew 2025, Ahrefs)**: Click-through drops of 35% to 48% when AI summaries appear → press-reported, not peer-reviewed.
- **Strength:** Medium. Two experimental designs agree on direction, but both are drafts or preprints, and their sizes differ.

### Finding 2: Losses are largest for informational queries and small sites.
- **Access study (Shi 2026)**: Wider ChatGPT Search access → traditional search use fell 9.4%. Largest referral losses fall on informational categories.
- **Traffic spread study (Gholami 2026)**: Traffic after LLM queries reaches more sites than search traffic does. This counters the concentration story.
- **Publisher bot-blocking study (Zhao 2025)**: Large publishers that block AI bots see less traffic. They shift toward content that is harder to copy.
- **Strength:** Low. Each pattern comes from one or two studies, and some rest on summaries.

### Finding 3: Ad auctions for LLM answers work in theory, not in live systems.
- **Token auction (Dütting 2024)**: Proposes a bid-per-token auction with second-price payments. Tests on a public LLM show output shifts smoothly with bid share.
- **Summary auction (Dubey 2024)**: Auctions ad content for one summary paragraph. Claims incentive compatibility, backed by theory and synthetic tests.
- **RAG ad auction (2024)**: Places ads per text segment. Repeated single-ad auctions raise more revenue, while multi-ad auctions raise answer quality.
- **Talk Back study (2025)**: Participants rated personalized ad answers lower across the questionnaire. Authors link this to wariness about sponsored results.
- **Strength:** Low. Theory and simulation, plus one user study read from a summary. Perplexity reportedly ended its ad placements, citing trust (press reports).

### Finding 4: GEO raises visibility in controlled tests, but the gain depends on rank and may not last.
- **GEO benchmark (Aggarwal 2024)**: Nine rewrite methods on GEO-bench → the best methods raise visibility up to 40%. Cite Sources gains 115% at rank 5 but loses 30% at rank 1.
- **GEO survey (Martinez 2026)**: A survey of 45 studies finds no technique with a stable, cross-platform effect on discoverability.
- **GEO position paper (Wen 2026)**: Argues GEO can concentrate influence and hide commercial influence. Calls for disclosure and audits.
- **Strength:** Medium for controlled gains (one benchmark, nine methods). Low for live effects, because the reviewed studies run in controlled settings.

### Finding 5: A few outlets get most AI news citations.
- **Citation outlet study (Yang 2025)**: Analyzed about 366,000 citations → news is about 9% of them, concentrated on few outlets, with a liberal lean.
- **Answer Bubbles study (2026)**: Perplexity cites at least one source for 74.5% of queries, and Google AI Overviews for 57.8%.
- **Strength:** Medium. The sample is large, but the first study has one author and the second is read from a summary.

## Where researchers disagree
The table shows where the evidence conflicts.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does AI search cut total publisher traffic? | Large click losses (AI Overviews test) | Traffic spreads to more sites (Traffic spread study) | Multi-platform panels tracking visits over time |
| Do GEO gains last? | Up to 40% gain in benchmarks (GEO benchmark) | No stable live effect (GEO survey) | Repeated audits of live engines over months |
| Do ads in answers help revenue without hurting trust? | Auctions raise revenue in simulation (Summary auction) | Users rate ad answers lower (Talk Back study) | Field test with real ads and trust measures |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Auction data from live answer engines | Theory cannot show real revenue or user cost | Token auction and Summary auction |
| Long-run GEO effects on live engines | Gains may erode as competitors respond | GEO survey |
| Causal revenue loss for publishers | Shows whether lost clicks reduce content supply | Publisher bot-blocking study |
| Evidence outside the United States | Field and log studies use US users | AI Overviews test |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| GEO benchmark (Aggarwal 2024) | **GEO: Generative Engine Optimization** | 2024 | KDD 2024 | abstract and related-work section |
| Token auction (Dütting 2024) | **Mechanism Design for Large Language Models** | 2024 | WWW 2024 | main sections |
| Summary auction (Dubey 2024) | **Auctions with LLM Summaries** | 2024 | arXiv preprint | abstract |
| RAG ad auction (2024) | **Ad Auctions for LLMs via Retrieval Augmented Generation** | 2024 | NeurIPS 2024 (not verified) | summary |
| Talk Back study (2025) | **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** | 2025 | ACM (not verified) | summary |
| Citation outlet study (Yang 2025) | **News Source Citing Patterns in AI Search Systems** | 2025 | arXiv preprint | abstract |
| AI Overviews test (Agarwal 2026) | **Google AI Overviews and Publisher Traffic: Evidence from a Field Experiment** | 2026 | SSRN working paper | summary |
| Referral field test (Wang 2026) | **AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence** | 2026 | arXiv preprint | abstract |
| Access study (Shi 2026) | **Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain** | 2026 | arXiv preprint | abstract |
| Traffic spread study (Gholami 2026) | **Beyond Search** | 2026 | Georgetown KGI working paper | summary (title from file name) |
| Publisher bot-blocking study (Zhao 2025) | **Strategic Response of News Publishers to Generative AI** | 2025 | arXiv preprint | abstract |
| GEO survey (Martinez 2026) | **Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)** | 2026 | arXiv preprint | abstract |
| GEO position paper (Wen 2026) | **Position: Generative Engine Optimization Creates Underexamined Risks, Governance Must Target Concentration, Disclosure, and Academic Blind Spots** | 2026 | ICML 2026 position track | abstract |
| Answer Bubbles study (2026) | **Answer Bubbles: Information Exposure in AI-Mediated Search** | 2026 | arXiv preprint | summary |

<details><summary>Original research question</summary>

How do LLM answer engines (Google AI Overviews, Bing Copilot, Perplexity, ChatGPT search) affect the search ecosystem: click-through and traffic to websites and publishers ('zero-click'), search advertising markets and ad placement in LLM answers, and the rise of generative engine optimization (GEO) — how sellers and content creators try to get cited or recommended by LLMs? Include economics of content provision, ad auctions for LLM outputs, and measurement studies.

</details>
