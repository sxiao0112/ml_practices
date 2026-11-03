# Brand visibility, bias and manipulation in LLM product recommendations

**Question:** Which brands do LLMs recommend to consumers, and how can sellers or attackers change those choices?

## Short answer
**Answer:** LLMs tend to recommend a few well-known brands in each product category. Changing the user's persona or wording can change which brands appear. Optimized text on a product page can raise that product's recommendation rate in attack-style tests.

**Strength:** Medium (most results are 2024 to 2026 preprints, and many were read only at abstract level)
- **Holds when:** Brands are compared on equal specs in one category → well-known brands win most answers.
- **Holds when:** A persona is added to the request → mid-market brands change most, and category leaders stay stable.
- **Does not hold when:** Brand awareness is controlled for → popularity explains little of the pattern in one audit.
- **Still unknown:** Whether sponsored or optimized answers change what consumers buy, or how they judge trust.

## Background
Shoppers now ask AI chatbots and answer engines which product to buy. The answer can decide which brands a shopper ever sees. Sellers have an incentive to shape these answers, and attackers can try to manipulate them.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model, an AI system trained on large amounts of text. |
| GEO (generative engine optimization) | Editing web content so AI answer engines mention or recommend it. |
| Incumbent bias | Tendency to recommend established brands over newer or smaller ones. |
| Popularity bias | Tendency to recommend the most popular items. |
| Persona | A described user profile, such as a budget shopper, added to the request. |
| Jaccard similarity | Overlap of two recommendation sets, from 0 (none) to 1 (identical). |
| Gini coefficient | Inequality measure from 0 (equal shares) to 1 (one brand takes all). |
| Strategic text sequence | Short optimized text added to a product page to raise its rank. |
| GCG | Greedy coordinate gradient, a search method that finds adversarial text automatically. |
| Prompt injection | Hidden instructions in web content that an AI agent reads and may follow. |
| Retrieval-augmented | The system fetches web pages before it writes an answer. |
| Preprint | A paper posted online before peer review. |
| CI | Confidence interval, the range that likely contains the true effect size. |
| SSRN | Social Science Research Network, an online archive of working papers. |
| NBER | National Bureau of Economic Research, which publishes economics working papers. |
| Synonym swap | Replacing words with near-equal words to change the answer. |
| Spearman correlation | Rank agreement between two sets of values, from -1 to 1. |
| Prominence tier | Brand group by market awareness, from category leader to regional player. |

## Main approaches
The main ways researchers attack this question:
| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Brand-share audits | Ask models for brand lists and count which brands appear | Incumbent Advantage (Chu 2026), Who Owns (Żatuchin 2026), Empirical Audit (Boffa 2026) | Emerging |
| Persona and repeat-run audits | Vary the persona or repeat the same request | Persona Conditioning (Jack 2026), Dice Roll (Żatuchin 2026) | Emerging |
| Popularity-bias studies | Test whether popular items dominate answers | Popularity Bias (Lichtenberg 2024), Brand Retrieval (Malthouse 2026) | Contested |
| Strategic text optimization | Edit product text to raise its rank | Manipulating LLMs (Kumar 2024), SafeGEO (Wen 2026), E-GEO (Bagga 2025) | Emerging |
| Prompt injection benchmarks | Hide instructions in product pages or reviews | StakeBench (Wang 2026) | Emerging |
| Wording-based bias | Swap synonyms in the user's request | LLM Whisperer (Lin 2025) | Emerging |

## What the evidence shows
### Finding 1: A few well-known brands win most answers in each category.
- **Incumbent Advantage (Chu 2026)**: Skincare brands with equal specs → well-known brands were recommended in every trial. A competitor needed about 0.1 more stars to break this.
- **Who Owns (Żatuchin 2026)**: 50 brands, five industries, three models → one brand appeared in at least 80% of answers for 204 of 250 queries.
- **Empirical Audit (Boffa 2026)**: Six models, 100 categories → one product was listed first in over three quarters of answers in 20 categories.
- **Strength:** Medium — three audits agree on direction, but two are preprints and each uses its own product categories.

### Finding 2: Popularity alone explains little of the pattern.
- **Brand Retrieval (Malthouse 2026)**: Six models, five categories → established brands were often omitted. Search interest predicted prominence better than popularity.
- **Popularity Bias (Lichtenberg 2024)**: Movie recommendations → the LLM showed less popularity bias than classic systems, with no fix applied.
- **Prominence Audit (Jack 2026)**: 37,000 runs, 533 brands → category leaders won 25 to 41% of the slots they reached.
- **Strength:** Low — the domains differ, and the popularity measures are not the same across papers.

### Finding 3: A consumer persona changes which brands appear, mainly for mid-market brands.
- **Persona Conditioning (Jack 2026)**: 2,000 runs, 10 personas, 8 prompts → adding a persona lowered recommendation-set overlap by 0.12 to 0.20 Jaccard.
- **Auditing Preferences (Rienecker 2026)**: Three models, over 2,000 questions → US models favored American brands, and the pattern held across personas.
- **Strength:** Medium for the persona effect, since one large design supports it. Low for the country pattern, since it was read from a summary.

### Finding 4: One answer is an unreliable measure of a brand's position.
- **Dice Roll (Żatuchin 2026)**: Reanalysis of five audits, about 190,000 observations → aggregate brand shares repeated across waves, but single answers to one question varied.
- **Strength:** Low — the two versions of the method paper give different run-count advice, and it was read only from a summary.

### Finding 5: Strategic text can raise a product's rank, and defenses leave residual risk.
- **Manipulating LLMs (Kumar 2024)**: Optimized text added to a product page → a fictitious product became the top recommendation.
- **E-GEO (Bagga 2025)**: 13,747 queries with 10 listings each → a simple in-prompt clause made gains look like real content improvement.
- **SafeGEO (Wen 2026)**: 600 cases → attacks raised the chance of a flawed product being recommended by up to 83.2 points. Defenses cut this by up to 39.2 points.
- **Strength:** Medium — three studies agree on direction, but tests use small or fictitious catalogs.

### Finding 6: Hidden instructions and wording tricks can steer shopping agents.
- **StakeBench (Wang 2026)**: 264 attack cases, 3,168 runs → no attack type was reliably resisted by current web agents.
- **LLM Whisperer (Lin 2025)**: Synonym swaps in the user's request → up to 78.3 points more mentions of a target concept.
- **Strength:** Medium for StakeBench. Low for LLM Whisperer, since it measures mentions, not purchases.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Is incumbent bias strong? | Strong: Incumbent Advantage (Chu 2026), Who Owns (Żatuchin 2026) | Weak: Popularity Bias (Lichtenberg 2024), Brand Retrieval (Malthouse 2026) | A matched audit that controls for brand awareness. |
| Do defenses stop text attacks? | Not fully: SafeGEO (Wen 2026) | Mostly: E-GEO (Bagga 2025) | Adaptive attacks run against the same in-prompt clause. |
| Are answers stable? | Aggregate shares stable: Who Owns (Żatuchin 2026) | Single answers vary: Dice Roll (Żatuchin 2026) | Repeated runs of the same query on one brand list. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Labeled versus unlabeled sponsored answers | Sets disclosure rules and tests the trust effect | One retail-assistant study (summary only) |
| Replicating the 2024 text attack on real catalogs | Shows whether the first result holds today | Manipulating LLMs (Kumar 2024) |
| Link from recommendations to purchases | Shows whether visibility changes sales | None found |
| Fake reviews and recommender effects | Fake reviews are cheap to write now | Ghostwriters corpus (2026, summary only) |
| Wording beyond persona and order | Users phrase requests in many ways | LLM Whisperer (Lin 2025) |
| SSRN and NBER work on LLM brand choice | Economic models of competition need market data | None found |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Incumbent Advantage (Chu 2026) | **Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems** | 2026 | arXiv preprint | abstract |
| Global is Good (Kamruzzaman 2024) | **"Global is Good, Local is Bad?": Understanding Brand Bias in LLMs** | 2024 | EMNLP 2024 | abstract |
| Auditing Preferences (Rienecker 2026) | **Auditing Preferences for Brands and Cultures in LLMs** | 2026 | arXiv preprint | summary |
| Who Owns (Żatuchin 2026) | **Who Owns the AI Recommendation? A Multi-Industry Empirical Map of Brand Category Ownership Across Large Language Models** | 2026 | Journal of Marketing Analytics | abstract |
| Empirical Audit (Boffa 2026) | **An Empirical Audit of LLM Product Recommendations** | 2026 | NET Institute working paper | abstract |
| Brand Retrieval (Malthouse 2026) | **Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations** | 2026 | arXiv preprint | abstract |
| Prominence Audit (Jack 2026) | **Prominence-Stratified Failure Modes in Retrieval-Augmented Commercial Recommendation: A 37,000-Run Audit** | 2026 | arXiv preprint | abstract |
| Popularity Bias (Lichtenberg 2024) | **Large Language Models as Recommender Systems: A Study of Popularity Bias** | 2024 | Gen-IR workshop at SIGIR | abstract |
| Persona Conditioning (Jack 2026) | **Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit** | 2026 | arXiv preprint | abstract |
| Dice Roll (Żatuchin 2026) | **The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing of Large Language Model Brand Recommendations** | 2026 | arXiv preprint | summary |
| Manipulating LLMs (Kumar 2024) | **Manipulating Large Language Models to Increase Product Visibility** | 2024 | arXiv preprint | abstract |
| GEO (Aggarwal 2024) | **GEO: Generative Engine Optimization** | 2024 | KDD 2024 | summary |
| E-GEO (Bagga 2025) | **E-GEO: A Testbed for Generative Engine Optimization in E-Commerce** | 2025 | arXiv preprint | abstract |
| SafeGEO (Wen 2026) | **SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents** | 2026 | arXiv preprint | abstract |
| StakeBench (Wang 2026) | **Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents** | 2026 | arXiv preprint | abstract |
| LLM Whisperer (Lin 2025) | **LLM Whisperer: An Inconspicuous Attack to Bias LLM Responses** | 2025 | CHI 2025 | summary |

<details><summary>Original research question</summary>

What does marketing and CS research find about which brands and products LLMs recommend to consumers: brand bias and popularity/incumbent bias, consistency of recommendations, sensitivity to prompt wording and consumer persona, vulnerability to manipulation (strategic text, prompt injection on product pages, fake reviews), sponsored or persuasive content in LLM answers, and implications for brand strategy and consumer trust?

</details>
