# What field and observational evidence (clickstream panels such as Comscore or Similarweb, browser logs, platform data, natural experiments such as Italy's 2023 ChatGPT ban, staggered rollouts of AI Overviews or Amazon Rufus, retailer referral data) shows whether LLM tools substitute for or complement traditional web search, and how they change real consumer purchase outcomes, conversion, basket composition, or spending?

## TL;DR
Answer: Desktop clickstream studies of ChatGPT adoption find fewer traditional search queries after adoption, about 9% to 22% lower, with the decline starting around month five. Field studies of purchases disagree in direction and do not isolate a link from search substitution to total spending. Industry dashboards report higher AI-referral conversion, but these are unreviewed and selection-prone.
Strength: Low-Medium for substitution, Low for purchase outcomes
Substitution rests on two Comscore-based studies that share a data vendor and a similar design, so they are not independent confirmations. Purchase results come from different platforms and tools, and none tests a general chatbot's effect on total spending.

## What Exists
### Sub-theme 1: Substitution from desktop clickstream and platform logs (new papers)
- **The impact of LLM adoption on online user behavior** (Padilla, Lam, Lambrecht and Hollenbeck, 2025, working paper; AEA 2026 program) — Comscore desktop panel, 2,041 users who adopted a chatbot in its first year. Traditional search fell 21.7% against each user's pre-adoption average, starting near week 20.
  - Relevance: Adoption-based design, a different comparison group from the rollout study. Largest search decline in the field literature. Calls to small sites fell 41.8%.
  - Read: secondary summary of the study plus conference program page. Full text not read.
  - Note: the workbench named a "Padilla et al. 2025" study without a title. This entry verifies it.
- **Informational Help-Seeking on Reddit Did Not Decline After ChatGPT** (Ibrahim and Zaki, 2026, arXiv 2609.12447) — Monthly posts from 26 informational and 90 hobby Reddit communities, six months before and after ChatGPT. Declines above 3.4% are ruled out, against 8% to 25% in earlier work.
  - Relevance: Counter-evidence on substitution, using public help-seeking as the outcome. Reddit posts are not search queries.
  - Read: abstract (via summary tool).
- **Disentangling Answer Engine Optimization from Platform Growth: A Log-Based Natural Experiment on ChatGPT Referral Traffic** (Watanabe and Nakayashiki, 2026, arXiv 2606.04362) — Treated YouTube Q&A pages versus untreated pages on one domain. ChatGPT referral level rose 1.82x (95% CI 1.31 to 2.54), placebo test p = 0.16.
  - Relevance: Shows how first-party logs can separate a site's own changes from platform growth. One domain, outcome is referral traffic, not purchases.
  - Read: abstract (via summary tool).
- **LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in passive behavioral logs** (Vargo, Rahman and Hopp, 2026, Journal of Marketing Analytics; OpenAlex W7162443840) — Detects LLM visits in passive event logs linked to a survey. One-month window.
  - Relevance: Measurement framework for LLM touchpoints in purchase journeys. The abstract reports a shift toward earlier, pre-intent discovery.
  - Read: abstract (partly retrieved). Direction and size of the main result not retrieved.
  - Cited by: 2 (OpenAlex)
- **The Unintended Consequences of Censoring Digital Technology - Evidence from Italy's ChatGPT Ban** (Kreitmeir and Raschky, 2023, OSF preprint; arXiv 2304.09339) — Italy's 2023 block. Italian developers' hourly output fell about 50% for two business days, then recovered. Synthetic control on daily Google search and Tor usage shows more circumvention tool use.
  - Relevance: The natural experiment the question names. Google search is used as a circumvention signal, not as a substitution measure. No purchase outcome.
  - Read: abstract.
  - Cited by: 15 (OpenAlex)

### Sub-theme 2: Purchase and conversion outcomes from retail referrals (new papers)
- **ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?** (Kaiser and Schulze, 2026, Marketing Science; OpenAlex W7155099606, DOI 10.1287/mksc.2025.0489) — Descriptive study of 973 e-commerce websites. Secondary reports say ChatGPT referrals convert below Google organic, email and affiliate traffic, with conversion and revenue per session rising over about 12 months.
  - Relevance: Retailer-side referral data on conversion, the outcome the question names. Descriptive, so no causal claim.
  - Read: abstract (OpenAlex) and secondary coverage. Full text blocked (HTTP 403).
  - Cited by: 2 (OpenAlex)
  - Note: a separate OpenAlex record (W7128379624) lists the same paper as a working paper.

### Sub-theme 3: Context from earlier streams (not counted)
Earlier findings already in the workbench: Shi et al. (9.4% fewer traditional queries after ChatGPT Search access), Yan et al. (2.5% fewer hotel bookings with a reasoning assistant), Zheng et al. (more purchases with generative search), and Fang et al. (1.2% higher purchase probability with query refinement).

### Sub-theme 4: Leads found but not read (not counted)
- **Competition in Generative AI: Evidence from Consumer Demand** (Egan and Russel, 2026, NBER working paper w35953) — metadata only. May use consumer demand data for AI products. Relevance unknown.
- **The Search Orientation Framework: How Consumers Start, Switch, and Stop in AI-Mediated Search** (Kyung, Longoni, Ding and Zhang, 2026, Current Opinion in Psychology) — conceptual review, metadata only.
- **The Rapid Adoption of Generative AI** (authors not checked, 2024, NBER w32966) — adoption survey, metadata only. Adoption context, not substitution.
- Industry, not counted: Shopify Q1 2026 (AI-referred sessions about 50% higher conversion than organic search), Similarweb (ChatGPT referral conversion 11.4% vs 5.3% organic), Adobe (AI-referred conversion above non-AI traffic), Sensor Tower (Rufus sessions 3.5x conversion on Black Friday 2025, correlational), Semrush (Google outbound share rising from about 14% to 21% in 2026).
- Unverified: a claimed field experiment on paid ChatGPT ads with 1,898 shops. Searches did not find the paper. Not counted.

## Reference Chain Discoveries
- Found via: OpenAlex citers of Consumer Responses to Generative AI Chatbots Versus Search Engines for Product Evaluation (W4410081533) — Vargo et al. (2026).
- Found via: OpenAlex citers of ChatGPT Referrals to E-Commerce Websites (W7155099606) — Kyung et al. (2026), plus an off-topic health chatbot paper.
- Found via: Reference mining of a secondary summary (UCLA Anderson Review) that names the Padilla et al. authors and sample — Padilla et al. (2026).
- Found via: Citers of Shi et al. (W7167813029) and Zheng et al. (W7214189263) — none returned in OpenAlex. Citation traversal was empty for both.
- Found via: Round of arXiv searches on staggered-adoption search decline — Ibrahim and Zaki (2026), Watanabe and Nakayashiki (2026).

## What's Missing (Gaps)
- Causal estimates of purchase effects from the ChatGPT rollout. No study links the search decline to total spending.
- Basket composition and average order value. No field study with these outcomes was found for general chatbots.
- Google AI Mode and Microsoft Copilot shopping. Searches found only vendor claims.
- Amazon Rufus rollout. No staggered-rollout study was found. Sensor Tower data are correlational.
- Shared-panel replication. Shi et al. and Padilla et al. use Comscore desktop panels, so they are not independent tests.
- Full text of the Marketing Science and Management Science papers. Publisher pages blocked automated access.

## Contradictions or Tensions
- Substitution direction: Padilla et al. and Shi et al. find fewer traditional queries. Ibrahim and Zaki find no decline in Reddit help-seeking, and Semrush finds Google sessions rising.
- Outcome choice: Padilla et al. measure search, Ibrahim and Zaki measure posts, and Watanabe and Nakayashiki measure referrals. These answer different questions.
- Conversion direction: Kaiser and Schulze find ChatGPT referrals convert below Google. Similarweb, Shopify and Adobe report higher AI-referral conversion. The industry figures are unreviewed and use different traffic definitions.
- Rufus lift: Sensor Tower reports 3.5x conversion. The source notes that high-intent shoppers may invoke Rufus, so the lift may not be causal.

## Confidence
Overall: Low-Medium for substitution, Low for purchase outcomes.
- What would raise confidence: Full text of Padilla et al. with the event-study figures. A second panel, outside Comscore, that finds the same decline. A staggered-rollout study linking search decline to purchases.
- What would lower confidence: A replication that finds no decline on desktop and mobile panels. Evidence that the 21.7% drop comes from a small set of heavy searchers.

## Search Log
### Round 1: Broad search
- Queries: "ChatGPT rollout Google search traffic clickstream natural experiment consumer purchases e-commerce 2025 2026"; "Italy ChatGPT ban 2023 natural experiment web traffic usage effects"; "Amazon Rufus staggered rollout conversion basket size field evidence"; "AI Overviews rollout staggered difference-in-differences online shopping purchases retailer referral traffic"; "Similarweb Comscore generative AI referral traffic retailers conversion LLM chatbot referrals e-commerce study"
- Papers found: 2 new (Kaiser and Schulze; Kreitmeir and Raschky). Other hits were industry or already known.
- Key leads: Kaiser and Schulze (retailer referral conversion); the Bocconi rollout study (already known).

### Round 2: Citation traversal
- Papers traversed: Consumer Responses to Generative AI Chatbots Versus Search Engines (W4410081533); ChatGPT Referrals to E-Commerce Websites (W7155099606); Shi et al. (W7167813029); Zheng et al. (W7214189263); Kreitmeir and Raschky (W4366688783, cited-by count only).
- New papers from references: none resolved. Reference list of W7155099606 was returned but not resolved.
- New papers from citers: Vargo et al. (2026); Kyung et al. (2026, lead only). Shi and Zheng returned no citers.

### Round 3: Reference section mining
- Papers mined: UCLA Anderson Review summary of the Padilla et al. study, which names the authors, data and sample. Paper full text not reachable.
- New papers: Padilla et al. (2026), verified this round.

### Round 4: Gap-filling
- Gaps targeted: staggered adoption and search decline; Rufus conversion and basket size; AI Overviews difference-in-differences; ChatGPT ad field experiment; Google AI Mode and Copilot shopping.
- Queries: "arXiv 2026 natural experiment LLM chatbot adoption online search queries decline Google difference-in-differences"; "Sensor Tower Rufus sessions conversion rate report 2025 AI shopping assistant Amazon purchases analysis"; "ChatGPT ads field experiment shops 1,898 paid visits revenue per visit working paper"; "Google AI Mode or Bing Copilot shopping conversion field data study consumers LLM referral vs organic search purchases 2026 paper".
- New findings: Ibrahim and Zaki (2026) and Watanabe and Nakayashiki (2026). No AI Overviews DiD study, no Rufus staggered-rollout study, and no ChatGPT ad field experiment found.

### Round 5: Adversarial check
- Gaps targeted: critiques of the search-decline and conversion results; contrary null results.
- Queries: no separate queries. Checked the results of the Sensor Tower and Google AI Mode searches for methodology caveats and conflicting figures.
- New findings: no new counted papers. The Drum's caution on Rufus selection, the Similarweb conversion figures, and the Reddit null all conflict with the other results.

### Convergence note
- Total unique relevant papers found: 17 (11 from earlier streams plus 6 new). Of the 6 new papers, one (Padilla et al.) was named in an earlier stream without a title.
- New papers in last round: 0 counted.
- Stopped because: The last round produced no new counted papers, and the remaining gaps returned only vendor material. The strict stopping rule was not fully met, since the fourth round still found two papers. Full texts of the two journal papers were blocked, so their findings rest on abstracts and secondary summaries.
