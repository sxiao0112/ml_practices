# Real-world evidence: does LLM search replace web search and change purchases?

**Question:** Do chatbots such as ChatGPT replace regular web search in real use, and do they change what people buy?

## Short answer
**Answer:** Real-usage data show that people run fewer regular web searches after they start using ChatGPT. The drop ranges from about 9% to 22%. It starts after about five months. Purchase evidence conflicts, and no study links the search drop to total spending.

**Strength:** Low-Medium (two desktop panel studies share one data vendor, and neither is peer reviewed)
- **Holds when:** desktop users in a U.S. panel start a chatbot → traditional search falls 9% to 22% (Padilla 2026, Shi 2026).
- **Does not hold when:** the outcome is public help-seeking on Reddit → no decline above 3.4% (Ibrahim and Zaki 2026).
- **Still unknown:** whether the search drop raises, lowers or leaves total spending unchanged.

## Background
People now ask chatbots questions they once typed into search engines. Shopping is one activity that could shift. Retailers and researchers want to know whether this shift changes sales, not only clicks.

Key terms used on this page:

| Term | Plain meaning |
|------|---------------|
| Clickstream panel | Logged web visits from a sample of users, collected by a tracking company. |
| Comscore | A company that sells panel data on desktop web visits. |
| Natural experiment | A real event that splits people into treated and untreated groups by timing. |
| Staggered rollout | A feature released to different users on different dates. |
| Difference-in-differences | Compares change over time in a treated group with a control group. |
| Event study | Tracks an effect week by week before and after an event. |
| Placebo test | Runs the same test on a fake date or group to check for false effects. |
| Conversion rate | The share of visits that end in a purchase. |
| Referral traffic | Visits that arrive at a site from another site or app, such as ChatGPT. |
| Basket composition | Which items a shopper puts in one order. |
| Randomized field experiment | Real users randomly receive one tool or another, and outcomes are compared. |
| Descriptive study | Reports patterns in data without a causal design. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Adoption comparison in panel logs | Compare users who start a chatbot with those who do not | Padilla 2026 | Emerging |
| Staggered rollout in panel logs | Compare users by the date they got chatbot access | Shi 2026 | Emerging |
| Randomized platform test | Assign users to an AI tool at random, then compare purchases | Zheng 2026, Yan 2025, Fang 2026 | Emerging |
| Retailer referral comparison | Compare sales from chatbot visits with other channels | Kaiser 2026 | Emerging |
| Public posting comparison | Compare posting in help communities with hobby communities | Ibrahim and Zaki 2026 | Contested |
| Industry dashboards | Vendor data on conversion and referrals | Shopify, Similarweb, Adobe | Contested |

## What the evidence shows
### Finding 1: Chatbot use cuts regular web search for desktop users
- **Padilla study (Padilla 2026)**: Compared 2,041 adopters with their own past use → traditional search fell 21.7%, starting near week 20.
- **Shi study (Shi 2026)**: Used staggered ChatGPT Search access in a panel of about 45,000 households. Traditional queries fell 9.4% on average, and 17% at week 20.
- **Strength:** Low. Both use desktop panels, and the panels likely share a vendor. Both are working papers.

### Finding 2: Chatbot referrals to retail sites convert below search and email
- **Kaiser study (Kaiser 2026)**: Descriptive study of 973 e-commerce sites → ChatGPT referrals converted below Google organic, email and affiliate traffic.
- **Industry dashboards (Shopify, Similarweb, Adobe)**: Report higher conversion for visits from AI tools than from organic search. Their definitions differ, and none is peer reviewed.
- **Log study (Watanabe 2026)**: Compared treated and untreated pages on one domain → ChatGPT referrals rose 1.82 times (95% range 1.31 to 2.54). A placebo test gave p = 0.16, so the result is suggestive only.
- **Strength:** Low. One peer-reviewed descriptive study conflicts with unreviewed vendor data.

### Finding 3: Platform assistants can raise or lower purchases
- **Zheng study (Zheng 2026)**: A randomized generative search tool on a large platform → more purchases and less exploratory browsing.
- **Yan study (Yan 2025)**: A randomized reasoning assistant on a travel platform with 510,000 users → 2.5% fewer hotel bookings.
- **Fang study (Fang 2026)**: Randomized query refinement in online retail → purchase probability 1.2% higher.
- **Strength:** Medium for direction within each test. Low across tests, since the platforms and tools differ, and none tests a general chatbot.

### Finding 4: Public help-seeking and purchase journeys show smaller shifts
- **Reddit study** (Ibrahim and Zaki 2026): Compared 26 informational and 90 hobby communities before and after ChatGPT → no decline above 3.4%.
- **Journey study (Vargo 2026)**: Passive logs in a one-month window show a shift in visible pre-intent discovery.
- **Strength:** Low. The Reddit result rests on an abstract. The journey study reports a one-month window.

### Finding 5: Bans disrupt use, and users find workarounds
- **Italy study (Kreitmeir 2023)**: Italy's 2023 ChatGPT ban cut developer output by about 50% for two days, then recovered. Circumvention tool use rose.
- **Strength:** Low. One preprint, and the outcome is coding output, not purchases.

## Where researchers disagree
The table lists the main conflicts and what would resolve each one.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does chatbot use cut web search? | Padilla 2026 and Shi 2026 find 9% to 22% less search | Ibrahim and Zaki 2026 find no decline in Reddit posts | A second panel with a shared outcome definition |
| Do chatbot visits convert well? | Kaiser 2026 finds lower conversion than search and email | Shopify, Similarweb and Adobe report higher conversion | Retailer data with one referral definition |
| Does Amazon Rufus raise sales? | Sensor Tower reports 3.5x conversion for Rufus sessions | Heavy shoppers may use Rufus more, so the lift may be selection | A staggered rollout with purchase outcomes |

## Gaps
The table lists open questions and the closest existing work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Purchase effect of the search drop | Shows whether substitution changes total spending | Zheng 2026 (platform tool, purchases) |
| Basket composition and order value | Shows what people buy, not only whether they buy | Yan 2025 (hotel bookings only) |
| Google AI Mode and Copilot shopping | These tools reach many users | None found, vendor claims only |
| Rufus staggered rollout | Tests Amazon's assistant with a causal design | Sensor Tower (correlational) |
| Independent panel replication | Tests whether the 9% to 22% drop holds elsewhere | Shi 2026 and Padilla 2026 (same vendor) |

Industry sources, not counted in the paper list: Shopify (Q1 2026), Similarweb (2026), Adobe (2026), Sensor Tower (2025-2026) and Semrush (2026).

## Papers cited
The table lists each short name with its exact title and how we read it.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Padilla 2026 | **The impact of LLM adoption on online user behavior** | 2026 | Working paper (AEA 2026 program) | Secondary summary and program page |
| Shi 2026 | **Answering without Referring: How AI Search Rewrites the Web's Economic Bargain** | 2026 | arXiv preprint | Secondary press reports |
| Ibrahim and Zaki 2026 | **Informational Help-Seeking on Reddit Did Not Decline After ChatGPT** | 2026 | arXiv preprint | Abstract |
| Watanabe 2026 | **Disentangling Answer Engine Optimization from Platform Growth: A Log-Based Natural Experiment on ChatGPT Referral Traffic** | 2026 | arXiv preprint | Abstract |
| Vargo 2026 | **LLM exposure and funnel erosion in consumer journeys: measuring journey compression and reordering in passive behavioral logs** | 2026 | Journal of Marketing Analytics | Abstract, partly read |
| Kaiser 2026 | **ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?** | 2026 | Marketing Science | Abstract and secondary reports |
| Kreitmeir 2023 | **The Unintended Consequences of Censoring Digital Technology - Evidence from Italy's ChatGPT Ban** | 2023 | OSF preprint | Abstract |
| Zheng 2026 | **Generative Search: Evidence from a Large-Scale Field Experiment** | 2026 | Management Science | Search summary only |
| Yan 2025 | **Reasoning AI, Consumer Search, and Purchase: Evidence from an Online Platform Field Experiment** | 2025 | SSRN working paper | Search summary only |
| Fang 2026 | **Generative AI and Sales Productivity: Field Experiments in Online Retail** | 2026 | CESifo working paper | Search summary only |

<details><summary>Original research question</summary>

What field and observational evidence (clickstream panels such as Comscore or Similarweb, browser logs, platform data, natural experiments such as Italy's 2023 ChatGPT ban, staggered rollouts of AI Overviews or Amazon Rufus, retailer referral data) shows whether LLM tools substitute for or complement traditional web search, and how they change real consumer purchase outcomes, conversion, basket composition, or spending?

</details>
