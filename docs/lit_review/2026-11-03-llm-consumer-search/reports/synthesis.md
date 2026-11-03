# Synthesis: Impact of LLMs on consumer search, and how to design or use LLMs for consumer search

## Summary

The review reached six main results. Each links to its section below.

- **Faster search**, but people follow wrong answers: **Medium**, three studies agree on direction ([details](#finding-1-consumers-search-faster-with-llms-but-follow-wrong-answers))
- **Less regular web search** in desktop panels, with purchase effects unknown: **Low**, because the two panels share a data vendor ([details](#finding-2-chatbots-cut-regular-web-search-but-purchase-effects-point-both-ways))
- **Fewer publisher clicks** after AI answers appear: **Medium**, because two field experiments agree on direction ([details](#finding-3-ai-answers-send-fewer-clicks-to-publisher-sites))
- **Well-known brands** win many shopping picks, and list order and wording shift picks: **Medium**, because several audits agree, though most are preprints ([details](#finding-4-shopping-picks-favor-well-known-brands-and-shift-with-list-order-and-wording))
- **Seller-written text** can raise a product's rank in AI answers: **Medium** for the attack, **Low** for defenses and labels ([details](#finding-5-seller-written-text-can-steer-ai-picks-while-defenses-are-tested-only-in-labs))
- **Small sales gains**, mostly 1% to 3%, from LLM search parts: **Medium** for query rewriting, **Low** for generative retrieval ([details](#finding-6-company-tests-show-small-sales-gains-from-llm-search-parts))

## Background

This review asks how AI chatbots and AI search tools change what consumers find and buy. Shopping used to start with a search engine and a list of links. A chatbot now often gives one written answer, and that answer can decide which brands a shopper sees. The change matters for shoppers, for sellers, and for publishers who earn money from clicks.

Researchers study this change from several sides. Economists model search costs, prices and competition, while marketing researchers use field panels, surveys and brand audits. Computer scientists build search systems and test them in A/B tests, which split live users between a new system and an old one. Human-computer interaction studies measure trust and over-reliance, meaning people follow an AI answer even when it is wrong.

## Key terms

The table defines the terms that the report uses. Terms appear in the same plain form throughout.

| Term | Plain meaning |
|------|---------------|
| A/B test | Live test that splits users between a new system and the old one. |
| Add-to-cart | A shopper places an item in the shopping cart. |
| Anchoring | A judgment pulled toward an earlier number, such as a first price offer. |
| ACES audit | A 2025 audit method that tests which products shopping agents pick. |
| Attack success | Share of manipulated answers that work. Lower is safer. |
| Brand bias | Favoring well-known or established brands over smaller ones. |
| ChatGPT | OpenAI's chatbot. Its web search feature is called ChatGPT Search. |
| Clickstream panel | Logged web visits from a sample of users, collected by a tracking company. |
| Collusion | Sellers keep prices high together, often through pricing software, without an explicit agreement. |
| Consumer welfare | The value buyers gain after paying prices. |
| Control group | Users who do not get the new tool, used for comparison. |
| Distillation | Training a small model to copy the outputs of a larger model. |
| Encoder model | A small model that reads a query and a product together to score a match. |
| Field experiment | A randomized test run on real users of a live website or app. |
| Fiduciary duty | A legal duty to act in another person's best interest. |
| GEO (generative engine optimization) | Editing web pages so AI answer engines cite or recommend them. |
| GMV | Gross merchandise value: the total value of goods ordered on a platform. |
| Generative retrieval | A language model writes product codes directly instead of searching an index. |
| Hedge | Wording such as "not sure, but" that signals doubt about an answer. |
| Highlighting | Colored marks on answer text that flag likely errors. |
| Jaccard overlap | Share of items shared by two recommendation sets, from 0 (none) to 1 (identical). |
| Long-tail query | A rare search that few shoppers type, often with unusual words. |
| Mechanism design | Setting market rules, such as payments, so that self-interested parties act well. |
| NBER | National Bureau of Economic Research, which publishes economics working papers. |
| Over-reliance | Following an AI answer even when it is wrong. |
| Persona | A written profile, such as a budget shopper, added to a request to shape answers. |
| Persuasive intent | A chatbot that was told to persuade the user. |
| Position bias | Favoring items because of where they appear in a list. |
| Preprint | A paper posted online before peer review. |
| Preference elicitation | An agent asks questions to learn what the user wants. |
| Preregistered | A study plan filed before data collection, to limit selective reporting. |
| Prompt injection | Hidden instructions in web content that an AI agent may follow. |
| Publisher | A site that produces news, reviews or other written content. |
| Query rewriting | Changing a shopper's search text into wording that the index matches better. |
| Relevance judge | A model that scores how well a product matches a search. |
| Reranker | A model that reorders a short list of candidate products. |
| Semantic ID | A short code that stands for a product, built from its content. |
| Shopbot | Software that compares prices across online stores for a shopper. |
| Simulator | An LLM agent that acts as a user inside a simulated website or search engine. |
| Sponsored label | A tag that marks a paid placement in a product list or answer. |
| Staggered rollout | A feature released to different users on different dates, to compare timing effects. |
| Steering | An intermediary tilts recommendations toward some products or sellers. |
| Test-retest reliability | How consistent answers are when the same person answers twice. |
| VCR (verifiable-content rewards) | Payments to web authors for checkable facts in their text. |

## Findings

### Finding 1: Consumers search faster with LLMs but follow wrong answers

Faster answers save effort. A wrong answer can still lead a buyer to a poor choice.

- **Spatharioti 2023**: LLM search cut time per task from 3.4 to 1.6 minutes (lower is faster) in 90 online participants.
- **Spatharioti 2023**: On one hard task, accuracy was 47% with the LLM tool and 93% with web search (higher is better).
- **Xu 2023**: Chatbot users spent less time on all tasks in a small study, with no clear gain in task performance.
- **Si 2024**: LLM explanations sped up fact-checking, but users followed explanations that were convincingly wrong.
- **Kim 2025**: Explanations raised reliance on wrong answers as well as right ones.
- **Li and Aral 2025**: Visible links raised trust in a preregistered study of about 4,900 people, even when the links were wrong.
- **Ding 2025**: Random and relevant citations both raised trust in a study of about 300 people, and checking citations lowered trust.
- **Liu 2023**: About one in four citations in generative search answers did not support the sentence they were attached to.
- **Strength:** Medium. Speed and over-reliance agree across studies, but several results come from abstracts or summaries.
- **Limits:** Most studies used paid online participants, mainly in the U.S., and few measured real purchases.

### Finding 2: Chatbots cut regular web search but purchase effects point both ways

Less search does not show whether buyers buy more, pay less, or end up better off. Purchase and welfare evidence is thin, and the tests that exist conflict.

- **Padilla 2026**: Among 2,041 desktop users who adopted a chatbot, regular search fell 21.7% against their own past use.
- **Shi 2026**: Staggered ChatGPT Search access cut regular queries by 9.4% in a panel of about 45,000 households, and by 17% at week 20.
- **Ibrahim and Zaki 2026**: Public help-seeking on Reddit did not fall by more than 3.4% after ChatGPT, though Reddit posts are not searches.
- **Zheng 2026**: A randomized generative search tool on a large platform raised purchases and reduced product browsing.
- **Yan 2025**: A reasoning assistant on a large travel site cut hotel bookings by 2.5% against users without it.
- **Fang 2026**: Randomized query refinement on an online retailer raised purchase probability by 1.2%.
- **Kaiser 2026**: Among 973 retail sites, ChatGPT referrals converted below Google organic, email and affiliate traffic.
- **Lucier 2026**: In theory, cheaper AI search raises buyer surplus when shoppers pay to learn product fit, but more information can lower it.
- **Strength:** Low. The two substitution panels share a vendor, and purchase tests cover different platforms and tools.
- **Limits:** No study links the search drop to total spending, and no market data test the theory.

### Finding 3: AI answers send fewer clicks to publisher sites

Fewer clicks cut the traffic and ad revenue of the sites that write the content. This could weaken the content supply that AI answers draw on.

- **AI Overviews test (Agarwal 2026)**: Users who saw AI Overviews made 39.8% fewer outbound organic clicks than users who did not, among 1,065 Chrome users.
- **Referral field test (Wang 2026)**: Removing AI summaries raised clicks to publishers in a preregistered test with 1,100 Google users. The abstract gives no effect size.
- **Shi 2026**: Wider ChatGPT Search access cut traditional search use by 9.4%, with the largest referral losses in informational categories.
- **Traffic spread study (Gholami 2026)**: Traffic after LLM queries reached more sites than search traffic did, which counters a concentration story.
- **Industry data**: Press-reported click-through drops of 35% to 48% appear when AI summaries show, but these reports are not peer reviewed.
- **Strength:** Medium. Two experiments agree on direction, but both are drafts or preprints, and their sizes differ.
- **Limits:** Studies use U.S. users and mostly Google. Revenue from ads inside live AI answers is untested.

### Finding 4: Shopping picks favor well-known brands and shift with list order and wording

Brand bias decides which firms a shopper sees, so it affects competition for smaller brands. Other audits find weaker brand bias, so the size of the effect is unsettled.

- **Incumbent Advantage (Chu 2026)**: With equal specs, well-known skincare brands won every trial, and a rival needed about 0.1 more stars to break this pattern.
- **Who Owns (Żatuchin 2026)**: Across 50 brands and three models, one brand appeared in at least 80% of answers for 204 of 250 queries.
- **Empirical Audit (Boffa 2026)**: Across six models and 100 categories, one product was listed first in over three quarters of answers in 20 categories.
- **Persona Conditioning (Jack 2026)**: Adding a consumer persona lowered Jaccard overlap by 0.12 to 0.20 (0 is no overlap, 1 is identical).
- **ACES audit (Allouah 2025)**: Top-row placement raised one model's pick rate about 5-fold, and an instruction to ignore position did not remove the effect.
- **Counter-evidence**: Popularity Bias (Lichtenberg 2024) and Brand Retrieval (Malthouse 2026) find that popularity explains little of the pattern.
- **Strength:** Medium. Three audits agree on direction, but two are preprints and each uses its own product categories.
- **Limits:** The audits measure simulated picks, not purchases. Results vary by model, and the cause of the brand skew is unclear.

### Finding 5: Seller-written text can steer AI picks while defenses are tested only in labs

Text written to game AI rankings can move a product up. An AI answer may then reflect marketing rather than fit.

- **Manipulating LLMs (Kumar 2024)**: Optimized text added to a product page made a fictitious product the top recommendation.
- **SafeGEO (Wen 2026)**: Attacks raised flawed-product picks by up to 83.2 percentage points, and defenses cut that by up to 39.2.
- **GEO Defender (Li 2026)**: Average attack success fell from 50.32% to 6.20% across seven known attacks, in self-reported tests.
- **Counter-GEO-Bench (2026)**: Standard safety guard models cut attack success by at most 5.7% in relative terms.
- **StakeBench (Wang 2026)**: Current web agents did not reliably resist any attack type, across 264 attack cases and 3,168 runs.
- **Rauchfleisch 2026**: Disclosing persuasive instructions cut the attitude shift to 6.3 points, from about 12.6 with no notice on a 100-point scale. A plain AI notice did not change it.
- **Salvi 2026**: Under a persuasive chatbot, sponsored picks rose to 61.2%, against 22.4% in search, and a sponsored label did not stop this.
- **Strength:** Medium for the attack, since three studies agree on direction. Low for defenses and labels, because none measures purchases.
- **Limits:** Attacks used small or fictitious catalogs. No study tested adaptive attacks or real purchases.

### Finding 6: Company tests show small sales gains from LLM search parts

Company tests give the strongest evidence for specific design choices. Most of the gains are small, and simulated shoppers match only group patterns.

- **BEQUE (2024)**: A fine-tuned 7-billion-parameter model rewrites queries, raising sales 0.40% overall and 1.57% on long-tail queries in a 14-day test.
- **Walmart distillation (2025)**: A large language model taught a small encoder model to judge relevance, raising add-to-cart per session by 0.8% on tail traffic.
- **OneSearch (2025)**: A generator with a reranker raised orders 3.22%, while the generator alone lowered orders 0.69%.
- **Hi-Gen (Wu 2024)**: Extra candidates from a generator raised GMV 1.42% in a one-week test on 4% of users per arm.
- **WeGR (Tencent 2026)**: A two-month test raised orders 2.54% and cut GPU use 26.1%.
- **Alipay (Shen 2025)**: Distilled reasoning and a filter raised offline accuracy in fund search from 83.83% to 87.17%.
- **Maier 2025**: LLM answers reached about 90% of human test-retest reliability on purchase intent across 57 surveys.
- **Chen 2026**: No LLM beat the strongest baseline for individual survey answers, so individual-level use is weak.
- **Strength:** Medium for query rewriting and relevance judges, since each has one full-text test. Low for generative retrieval, which is mostly self-reported.
- **Limits:** Most gains come from Chinese platforms and Walmart. No paper reports how often generated product codes are invented.

## Where researchers disagree

The table shows where studies conflict and what would settle each conflict.

| Question | View A (short names) | View B (short names) | What would settle it | Status |
|----------|----------------------|----------------------|----------------------|--------|
| Does chatbot use cut regular web search? | Shi 2026 and Padilla 2026: 9% to 22% less regular search | Ibrahim and Zaki 2026: no decline above 3.4% on Reddit | A second panel with the same outcome definition | Open |
| Do AI tools raise purchases? | Zheng 2026 and Fang 2026: more purchases on retail sites | Yan 2025: 2.5% fewer hotel bookings on a travel site | Same tool and site, with purchases measured in both arms | Open |
| Do chatbot users decide better? | Kaiser 2025: chatbot users more often found correct answers | Spatharioti 2023: users followed wrong answers on one hard task | Purchase outcomes tracked after wrong answers | Open |
| Do explanations cut over-reliance? | Vasconcelos 2023: explanations help when they are cheap to read | Kim 2025: explanations raised reliance on right and wrong answers | A consumer test that varies explanation cost | Open |
| Do uncertainty cues help? | Kim 2024: "not sure" wording raised accuracy on medical questions | Li and Aral 2025: uncertainty highlights lowered trust | Hedges and highlights tested on the same tasks | Open |
| Do labels reduce persuasion? | Rauchfleisch 2026: disclosing persuasive intent halved the attitude shift | Salvi 2026: a sponsored label did not stop steering | A preregistered test with purchases as the outcome | Open |
| Are brand biases strong? | Incumbent Advantage (Chu 2026) and Who Owns (Żatuchin 2026): strong bias | Popularity Bias (Lichtenberg 2024): popularity explains little | A matched audit that controls for brand awareness | Open |
| Do defenses stop text attacks? | SafeGEO (Wen 2026): not fully | E-GEO (Bagga 2025): mostly | Adaptive attacks run against the same defense | Open |
| Do simulated shoppers predict real shoppers? | ProductAgent (2025): simulator results show clear gains | Chen 2026 and Tigre 2026: simulated panels miss individuals | A live test with real shoppers | Leaning B |
| Do LLM sellers collude on prices? | Fish 2024: simulated LLM sellers set above-competitive prices | Keppo 2026: differences between agents cut the markup from 22% to 10% | Real-market price data across sellers | Open |
| Do recommenders raise or lower prices? | Buyer-Optimal (Ichihashi 2025): a buyer-side recommender lowers prices | Tacit Collusion (Affonso 2026): agents may reach collusion-like prices | A model fit to real assistant rankings and price changes | Open |
| Do ads in answers pay off without hurting trust? | Summary auction (Dubey 2024): simulated auctions raise revenue | Talk Back study (Tang 2025): users rate ad answers lower | A field test with real ads and trust measures | Open |
| Does reasoning help against anchors? | Takenami (2025): reasoning models resist anchoring | Hantel (2026): step-by-step reasoning raises anchoring | Market tests comparing reasoning and non-reasoning modes | Open |
| Does AI concentrate sales on a few products? | Turegeldinova et al. (2025): yes, through homogenization | Raghavan (2026): no, competition keeps models diverse | Product share data before and after AI use | Open |

## Gaps

The table lists open gaps, the closest existing work, and how sure the review is that each gap is real.

| Gap | Why it matters | Closest existing work (short name) | Strength that the gap is real |
|-----|----------------|------------------------------------|-------------------------------|
| Purchase effect of the search drop | Shows whether substitution changes total spending | Zheng 2026 (platform tool, purchases) | High: no study links the drop to spending |
| Price dispersion under real assistant use | Dispersion is the main test of search-cost theory | Shopbot Prices (Tang 2010), pre-LLM data | High: no LLM market data found |
| Real sales concentration from AI picks | Shows whether a few sellers gain | Egan 2026 (AI subscriptions, not product sales) | Medium: audits show skew, but sales data are missing |
| Antitrust cases on AI shopping agents | Shows whether gatekeeper rules apply to agents | None found | Low: only legal commentary found |
| Rate of invented product codes | Shows how often users see wrong items | Alipay (Shen 2025), accuracy only | Medium: platforms report accuracy but not invented codes |
| Labels on sponsored answers and purchases | Sets disclosure rules | Rauchfleisch 2026 (attitudes only) | High: no purchase test found |
| Independent test of seller defenses | Current numbers are self-reported | SCI-Defense (Yu 2026) | Medium: only self-reported results exist |
| Live test of clarifying questions | Simulated gains may not hold for real shoppers | Zou 2020 (small live study) | Medium: one small live study exists |
| Human check of shopper simulators | Simulators guide design choices | ConvApparel (2026), gap measured without a fix | Medium: two benchmark papers report the gap |
| Effects by consumer group and beyond 20 weeks | Habits change slowly, and effects may differ by group | Kaiser 2025 (personality only) | Medium: few studies vary by consumer group |
| Long-run GEO effects on live engines | Gains may erode as sellers and engines adapt | GEO survey (Martinez 2026) | Medium: no stable effect found across platforms |

## How to design and use LLMs for consumer search

The table lists design levers with evidence from all streams, strongest first. Each lever names the setting where its effect was measured.

| Design lever | What it changes | Best evidence (short name) | Measured effect | Setting (lab / offline / live A/B) | Strength |
|--------------|-----------------|----------------------------|-----------------|------------------------------------|----------|
| Query rewriting by an LLM | Rewrites shopper search text into wording the index matches | BEQUE (2024) | Sales +0.40% overall, +1.57% on long-tail queries | Live A/B, 14 days | Medium |
| Distilled LLM relevance judge | A small model copies a large model's relevance labels | Walmart distillation (2025) | Add-to-cart per session +0.8% on tail traffic | Live A/B, 2 weeks | Medium |
| Disclosure of persuasive intent | Tells users that the chatbot was told to persuade | Rauchfleisch 2026 | Attitude shift 6.3 vs 12.6 points (lower is less persuaded) | Preregistered online study, 1,500 adults | Medium (attitudes only) |
| Visible source links | Attaches links to answer sentences | Li and Aral 2025 | Trust rose, even when the links were wrong | Preregistered survey, about 4,900 people | Medium (trust only) |
| Generator with a reranker | A generator writes item codes, and a reranker orders them | OneSearch (2025) | Orders +3.22% with reranker, -0.69% without | Live A/B | Low |
| Generator as extra candidates | Adds a generator's items to the candidate list | Hi-Gen (Wu 2024) | GMV +1.42% in a one-week test | Live A/B | Low |
| Hedged wording | Adds "not sure" phrasing to uncertain answers | Kim 2024 | Higher accuracy on medical questions, 404 people | Online experiment | Low (one study) |
| Warnings on uncertain claims | Colors claims by confidence level | Spatharioti 2023 | Hard-task accuracy 26% to 58% with warnings | Lab, one task | Low |
| Explanations | Gives reasons for each AI answer | Vasconcelos 2023 | Cut over-reliance only when reading was cheap | Simulated AI, lab | Low |
| Prompt warnings on bias | Warns the model about brand or popularity cues | BiasRecBench (2026) | Robustness up 3.5 to 12 points for GPT-4o | Benchmark | Low |
| Seller-text detector | Flags persuasive product text in ranking inputs | SCI-Defense (Yu 2026) | Catches 96.2% of review attacks at 1.2% false positives | Self-reported test | Low |
| Shuffled lists, merged rankings | Reorders items several times, then merges the rankings | Found in the Middle (Tang 2024) | Ranking scores up 7% to 18% on ranking tasks | Benchmark, not shopping | Low |
| Clarifying questions | Asks shoppers questions before ranking products | Zou 2020 | Shoppers answered about 11 questions before quitting | Small live study | Low |
| Simulated shoppers for testing | LLM shoppers stand in for real users in tests | BASES (2024) | Queries match 90.8% of terms, top clicks match 51% | Offline logs | Low |

Levers proposed but never measured on consumers:

- **Loyalty duties for shopping agents** (AI Agents and the Law (2025)): legal argument only, with no outcome measured.
- **Creator payments** for checkable facts (VCR mechanism (Xu 2026)): simulations only, and consumer welfare is not measured.
- **Ad and subscription models** for answer engines (Zhang 2026): theory only, with no consumer data.
- **Preference building** by shoppers in dialog (CoShop (Saracay 2026)): no agent exceeded 56% accuracy, and no welfare test exists.
- **Sponsored-answer labels tested on purchases**: attitude tests exist, but no study measures purchases.

## Economics vs. marketing vs. CS: what each field contributes

The table compares what each field asks and where its evidence is weakest.

| Field | Main questions asked | Typical evidence | Biggest blind spot |
|-------|----------------------|------------------|--------------------|
| Economics | How search costs, prices and competition change with AI agents | Theory models, simulated markets, and a few transaction datasets | No market-level sales data for LLM search |
| Marketing | Which brands get recommended, and how sellers and consumers respond | Field panels, brand-list audits, and online experiments | Most evidence comes from preprints and simulated shoppers |
| Computer science and information retrieval | How to design, rank and evaluate LLM search systems | Company A/B tests, benchmarks, and offline evaluations | Most gains are self-reported, and welfare is rarely measured |
| Human-computer interaction | When people trust or over-rely on AI answers | Lab and online experiments with paid participants | Few studies measure purchases or repeated use |

## Recommendations

1. Show visible sources and uncertainty cues, and measure decision accuracy, not only trust (Finding 1).
2. Test each shopping change with purchase outcomes before scaling it (Finding 2, purchase effect gap).
3. Add LLM parts as candidate sources or rerankers, not full replacements (Finding 6).
4. Audit brand lists across models and personas, and report the spread (Finding 4).
5. Screen seller-written product text, and test defenses against adaptive attacks (Finding 5).
6. Label sponsored content clearly, and measure whether labels change purchases (Finding 5, labels gap).
7. Check simulated shoppers against real behavior before using them to pick designs (human check gap).
8. Report full A/B results with significance, and both sales and relevance metrics (Finding 6).
9. Track purchases and returns, not only clicks or queries, in future studies (Findings 2 and 3).

## Appendix A: Streams at a glance

The table lists each stream with its question, its direct answer, and its strength. Papers counts include some duplicates across streams.

| Stream | Question (plain words) | Answer (max 20 words) | Strength | Papers |
|--------|------------------------|-----------------------|----------|--------|
| Economic theory of search costs | How do AI assistants change search costs, prices and welfare? | Theory says cheaper search can help buyers, but no market data test it. | Low | 17 |
| Consumer use of LLM search | How do chatbots change search effort, choices and purchases? | Searches are faster and fewer, but wrong answers get followed. Purchase effects conflict. | Low | 12 |
| Search engines, publishers and ads | Do AI answers cut clicks, and how do ads and GEO work? | Clicks fall in experiments. Ad auctions are theory only. GEO gains are controlled. | Medium | 14 |
| Brand bias and manipulation | Which brands do LLMs recommend, and how can sellers change picks? | Well-known brands win most answers. Seller text can raise a product's rank. | Medium | 16 |
| LLM agents as shoppers | Do shopping agents choose well, and how do they act against sellers? | List position and anchors shift picks. Anchors can collapse simulated markets. | Medium | 14 |
| System design for product search | Which design choices have measured gains? | Query rewriting and generative retrieval add small sales gains in company tests. | Medium | 14 |
| Trust and interface design | When do people trust or over-rely on AI answers? | Visible citations raise trust, even when wrong. Hedges help in one study. | Medium | 23 |
| Substitution and purchases in field data | Does chatbot use replace web search and change purchases? | Desktop search falls 9% to 22%. Purchase effects point both ways. | Low | 10 |
| Economics and marketing working papers | Which econ and marketing papers did computer science searches miss? | Demand and steering papers exist. Few use market data. | Medium | 21 |
| Deployed shopping assistants | Which deployed systems report online results? | Generative retrieval and rewriting report small gains. Assistants publish no numbers. | Medium | 18 |
| Designs that serve the consumer | Which methods make assistants act for shoppers, and were they tested? | Warnings, training and disclosure cut bias in tests. Few purchase tests exist. | Low | 18 |
| Economics and marketing citation trail | Do other econ papers find null or opposite effects? | Collusion depends on agent differences. One field trial shows sales gains. | Low | 12 |
| LLMs as simulated consumers | Can LLMs stand in for real consumers? | Aggregate patterns match. Individual and subgroup answers fit poorly. | Medium | 24 |

## Appendix B: Key papers

The first table lists the 20 papers that matter most, ranked by importance to the topic. The second table lists the other papers named in this report.

| # | Short name | Full title | Year | Venue | Why it matters |
|---|------------|------------|------|-------|----------------|
| 1 | Spatharioti 2023 | **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** | 2023 | arXiv preprint (CHI 2025 version has a different title) | Randomized test of LLM and web search for consumer choice. Errors are followed when the LLM is wrong. |
| 2 | Shi 2026 | **Answering without Referring: How AI Search Rewrites the Web's Economic Bargain** | 2026 | arXiv preprint | Staggered rollout shows 9.4% less traditional search. Read mostly through press reports. |
| 3 | Padilla 2026 | **The impact of LLM adoption on online user behavior** | 2026 | Working paper (AEA 2026 program) | Adopter comparison shows 21.7% less search. Full text not read. |
| 4 | Kaiser 2025 | **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** | 2025 | CHI | Large study of faster search and more correct answers, yet most users still prefer Google. |
| 5 | Yan 2025 | **Reasoning AI, Consumer Search, and Purchase: Evidence from an Online Platform Field Experiment** | 2025 | SSRN working paper | Field test showing 2.5% fewer hotel bookings with a reasoning assistant. |
| 6 | Zheng 2026 | **Generative Search: Evidence from a Large-Scale Field Experiment** | 2026 | Management Science | Field test showing more purchases with generative search. Read from a summary. |
| 7 | Agarwal 2026 | **Google AI Overviews and Publisher Traffic: Evidence from a Field Experiment** | 2026 | SSRN working paper | Randomized test showing about 40% fewer organic clicks when AI Overviews appear. |
| 8 | ACES audit (Allouah 2025) | **What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** | 2025 | arXiv preprint | Audit showing that list position and labels shift what shopping agents buy. |
| 9 | Incumbent Advantage (Chu 2026) | **Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems** | 2026 | arXiv preprint | Well-known brands win recommendation trials with equal specs. |
| 10 | Persona Conditioning (Jack 2026) | **Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial Chat: A Prominence-Stratified Cross-Provider Audit** | 2026 | arXiv preprint | Large audit showing that personas change which brands appear. |
| 11 | Li and Aral 2025 | **Human Trust in AI Search: A Large-Scale Experiment** | 2025 | arXiv preprint | Large preregistered study showing visible links raise trust even when wrong. |
| 12 | Kim 2024 | **"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust** | 2024 | arXiv preprint | Preregistered test showing hedged wording raised accuracy on medical questions. |
| 13 | Rauchfleisch 2026 | **Toward Meaningful Transparency for AI Chatbots: Disclosing Persuasive Intent Reduces Persuasion** | 2026 | arXiv preprint | Preregistered test with 1,500 adults on disclosing persuasive intent. Attitudes only. |
| 14 | Salvi 2026 | **Commercial Persuasion in AI-Mediated Conversations** | 2026 | arXiv preprint | Shows sponsored picks rise under a persuasive chatbot. Read from a summary. |
| 15 | Manipulating LLMs (Kumar 2024) | **Manipulating Large Language Models to Increase Product Visibility** | 2024 | arXiv preprint | Shows optimized product text can win the top recommendation. |
| 16 | Fish 2024 | **Algorithmic Collusion by Large Language Models** | 2024 | arXiv preprint | Simulated LLM pricing agents set prices above competitive levels. |
| 17 | Keppo 2026 | **On the Fragility of AI Agent Collusion** | 2026 | arXiv preprint | Shows collusion weakens when agents differ in patience or data. |
| 18 | Lucier 2026 | **Agentic Markets: Equilibrium Effects of Improving Consumer Search** | 2026 | arXiv preprint | Theory showing cheaper AI search can help or hurt buyers. |
| 19 | Egan 2026 | **Competition in Generative AI: Evidence from Consumer Demand** | 2026 | NBER Working Paper 35953 | Card data from 174 million consumers show strong price competition among AI services. |
| 20 | Chen 2026 | **When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses** | 2026 | arXiv preprint | Shows simulated respondents fail at the individual level. |

### Other papers named in this report

| # | Short name | Full title | Year | Venue | Why it matters |
|---|------------|------------|------|-------|----------------|
| 21 | Kaiser 2026 | **ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?** | 2026 | Marketing Science | Retail referral data show lower conversion than search. |
| 22 | Ibrahim and Zaki 2026 | **Informational Help-Seeking on Reddit Did Not Decline After ChatGPT** | 2026 | arXiv preprint | Counter-evidence on substitution, using posts rather than searches. |
| 23 | Fang 2026 | **Generative AI and Sales Productivity: Field Experiments in Online Retail** | 2026 | CESifo working paper | Randomized query refinement raised purchase probability 1.2%. |
| 24 | Xu 2023 | **ChatGPT vs. Google: A Comparative Study of Search Performance and User Experience** | 2023 | SSRN working paper | Small study of time and satisfaction with a chatbot. |
| 25 | Si 2024 | **Large Language Models Help Humans Verify Truthfulness -- Except When They Are Convincingly Wrong** | 2024 | NAACL | Explanations speed checking but mislead when they are wrong. |
| 26 | Kim 2025 | **Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies** | 2025 | CHI | Explanations raised reliance on both right and wrong answers. |
| 27 | Vasconcelos 2023 | **Explanations Can Reduce Overreliance on AI Systems During Decision-Making** | 2023 | CSCW | Explanations help only when reading them costs little. |
| 28 | Ding 2025 | **Citations and Trust in LLM Generated Responses** | 2025 | AAAI | Citations raised trust, including random citations. |
| 29 | Liu 2023 | **Evaluating Verifiability in Generative Search Engines** | 2023 | Findings of EMNLP | About one in four citations did not support its sentence. |
| 30 | Referral field test (Wang 2026) | **AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence** | 2026 | arXiv preprint | Removing AI summaries raised clicks to publishers. |
| 31 | Traffic spread study (Gholami 2026) | **Beyond Search** | 2026 | Georgetown KGI working paper | Traffic after LLM queries reaches more sites. Title taken from a file name, not verified. |
| 32 | Summary auction (Dubey 2024) | **Auctions with LLM Summaries** | 2024 | arXiv preprint | Simulated auction for ad content inside summaries. |
| 33 | Talk Back study (Tang 2025) | **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** | 2025 | ACM (venue not verified) | Users rated personalized ad answers lower. |
| 34 | Who Owns (Żatuchin 2026) | **Who Owns the AI Recommendation? A Multi-Industry Empirical Map of Brand Category Ownership Across Large Language Models** | 2026 | Journal of Marketing Analytics | Brand shares across 50 brands and three models. |
| 35 | Empirical Audit (Boffa 2026) | **An Empirical Audit of LLM Product Recommendations** | 2026 | NET Institute working paper | Six models and 100 categories show one product often listed first. |
| 36 | Popularity Bias (Lichtenberg 2024) | **Large Language Models as Recommender Systems: A Study of Popularity Bias** | 2024 | Gen-IR workshop at SIGIR | Finds less popularity bias than classic recommenders, in movies. |
| 37 | Brand Retrieval (Malthouse 2026) | **Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations** | 2026 | arXiv preprint | Established brands often omitted, and search interest predicts prominence. |
| 38 | SafeGEO (Wen 2026) | **SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents** | 2026 | arXiv preprint | Attacks raise flawed-product picks, and defenses cut the rise. |
| 39 | GEO Defender (Li 2026) | **When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization** | 2026 | arXiv preprint | Self-reported defense against seven known attacks. |
| 40 | Counter-GEO-Bench (2026) | **Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization** | 2026 | arXiv preprint | Standard guard models are weak against seller-written text. |
| 41 | StakeBench (Wang 2026) | **Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents** | 2026 | arXiv preprint | Current web agents did not reliably resist any attack type. |
| 42 | SCI-Defense (Yu 2026) | **SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines** | 2026 | arXiv preprint | Self-reported detector for seller-written persuasive text. |
| 43 | E-GEO (Bagga 2025) | **E-GEO: A Testbed for Generative Engine Optimization in E-Commerce** | 2025 | arXiv preprint | Testbed where defenses look mostly effective. |
| 44 | GEO survey (Martinez 2026) | **Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)** | 2026 | arXiv preprint | No technique has a stable cross-platform effect on visibility. |
| 45 | Buyer-Optimal (Ichihashi 2025) | **Buyer-Optimal Algorithmic Recommendations** | 2025 | ACM Conference on Economics and Computation | A recommender that serves buyers can lower prices. |
| 46 | Tacit Collusion (Affonso 2026) | **Vertical tacit collusion in AI-mediated markets** | 2026 | arXiv preprint | Agents may reach collusion-like prices without any agreement. |
| 47 | Takenami (2025) | **How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations** | 2025 | Findings of EMNLP 2025 | Reasoning models are less affected by anchors. |
| 48 | Hantel (2026) | **Small Bias, Large Failure: Anchoring Collapses a Market of Language-Model Agents** | 2026 | SSRN working paper | One anchoring sentence sharply cut market efficiency in simulation. |
| 49 | Turegeldinova et al. (2025) | **AI as a Centripetal Technology: Price Compression, Homogenization, and Entry** | 2025 | SSRN working paper | Theory of AI pulling products toward one template. |
| 50 | Raghavan (2026) | **Competition and Diversity in Generative AI** | 2026 | Management Science | Argues that competition keeps AI models diverse. |
| 51 | Maier 2025 | **LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings** | 2025 | arXiv preprint | About 90% of human test-retest reliability across 57 surveys. |
| 52 | Tigre 2026 | **When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels** | 2026 | arXiv preprint | Subgroup errors reach 10 to 30 points. |
| 53 | ProductAgent (2025) | **ProductAgent: Benchmarking Conversational Product Search Agent with Asking Clarification Questions** | 2025 | EMNLP 2025 Industry Track | Simulated gains from clarifying questions. |
| 54 | Zou 2020 | **An Empirical Study of Clarifying Question-Based Systems** | 2020 | CIKM 2020 | Live study in which shoppers answered about 11 questions. |
| 55 | ConvApparel (2026) | **ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders** | 2026 | EACL 2026 | Shows a realism gap for all simulators tested. |
| 56 | BASES (2024) | **BASES: Large-scale Web Search User Simulation with Large Language Model based Agents** | 2024 | arXiv preprint | Simulated queries and clicks match human logs in part. |
| 57 | BEQUE (2024) | **Large Language Model based Long-tail Query Rewriting in Taobao Search** | 2024 | ACM | Live test of LLM query rewriting on long-tail queries. |
| 58 | Walmart distillation (2025) | **Knowledge Distillation for Enhancing Walmart E-commerce Search Relevance Using Large Language Models** | 2025 | WWW 2025 Companion | Live test of a distilled LLM relevance judge. |
| 59 | OneSearch (2025) | **OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search** | 2025 | arXiv preprint | A reranker is needed to match the pipeline. |
| 60 | Hi-Gen (Wu 2024) | **Hi-Gen: Generative Retrieval For Large-Scale Personalized E-commerce Search** | 2024 | arXiv preprint | One-week live test of generator candidates. |
| 61 | WeGR (Tencent 2026) | **WeGR: unified generative retrieval for WeChat e-commerce search** | 2026 | arXiv preprint | Two-month live test. Title taken from a later check. |
| 62 | Alipay (Shen 2025) | **Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search** | 2025 | SIGIR 2025 | Reasoning distillation and a filter for fund search. |
| 63 | Shopbot Prices (Tang 2010) | **The impact of shopbot use on prices and price dispersion: Evidence from online book retailing** | 2010 | International Journal of Industrial Organization | Pre-LLM evidence on price dispersion, which is mixed. |
| 64 | AI Agents and the Law (2025) | **AI Agents and the Law** | 2025 | arXiv preprint | Legal argument on the loyalty of shopping agents. |
| 65 | VCR mechanism (Xu 2026) | **Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes** | 2026 | arXiv preprint | Simulated payments to content creators for checkable facts. |
| 66 | Zhang 2026 | **An Economic Framework for Generative Engines: Advertising or Subscription?** | 2026 | arXiv preprint | Theory of ads versus subscriptions in AI answers. |
| 67 | CoShop (Saracay 2026) | **Beyond expert users: agents should help users construct preferences, not just elicit them** | 2026 | arXiv preprint | Benchmark where no agent exceeded 56% accuracy. |
| 68 | Found in the Middle (Tang 2024) | **Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models** | 2024 | NAACL 2024 | Shuffling and merging improves ranking tasks. |
| 69 | BiasRecBench (2026) | **Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)** | 2026 | arXiv preprint | Benchmark of bias injection, where warnings partly help. |
| 70 | Semrush 2025 | Title not found | 2025 | Semrush industry report | Google sessions rose after ChatGPT adoption, which conflicts with substitution studies. |

## Appendix C: Method and limitations

- Streams: 7 initial streams and 6 follow-ups, 13 in total.
- Rounds: 3, one launch round and two follow-up rounds.
- Unique papers: about 190 after merging obvious duplicates by title. The list is not fully deduplicated.
- Search tools: OpenAlex, web search, arXiv pages, publisher pages (some blocked), and company blogs.
- How sources were read: about 17 full texts, about 60 abstracts, and the rest from search summaries, snippets, press reports or metadata. These counts are approximate.
- Limitations:
  - Several key numbers come from search summaries, not from the papers. Examples include Yan 2025 and Zheng 2026.
  - Most evidence comes from preprints, working papers, or company reports, and some of it has not been peer reviewed.
  - Two naming choices are judgment calls: Spatharioti 2023 and its 2025 conference version count as one study. The Egan 2026 author list differs by source.
  - Two 2026 papers by Wang use method names, so their short names do not clash.
  - The title of the traffic spread study came from a file name and was not verified.
  - Simulated and lab studies dominate, and few studies measure purchases.
  - Searches stopped at convergence or at the round limit. Generative retrieval, simulated consumers, and sponsored labels did not converge.
  - Evidence outside the United States is thin. The one non-U.S. synthetic panel found could not be verified.
  - Industry dashboards (Shopify, Similarweb, Adobe, Sensor Tower) are not counted as papers. Amazon's claim that Rufus users are 60% more likely to buy is unverified and not used.
