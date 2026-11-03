# How consumers actually search with LLMs: experiments and field evidence

**Question:** How do LLM chatbots and AI search tools change consumer search effort, choices, purchases and satisfaction, compared with traditional search engines?

## Short answer
**Answer:** In lab and online experiments, LLM search makes people faster and reduces the number of queries. Accuracy matches traditional search when the LLM answer is right, but it drops when the answer is wrong. Field studies disagree on purchases and on whether chatbots replace Google use.

**Strength:** Low-Medium (11 studies, most with 90 to 1,526 participants, mostly U.S. samples, and several read only as abstracts or press summaries)
- **Holds when:** Users compare products or look up facts with one written answer → faster, fewer queries, higher satisfaction.
- **Does not hold when:** The LLM answer is wrong → users over-trust it and choose less accurately.
- **Mixed on purchases:** A reasoning assistant on a travel site cut hotel bookings 2.5%. Generative search on retail sites raised purchases.
- **Still unknown:** Whether faster search gives better long-run choices, and which consumers gain most.

## Background
Shopping and fact-finding used to start with a search engine and a list of links. Chatbots such as ChatGPT now give one written answer, often without links. This changes how much work a consumer does and how many sites they open. The answer matters for sellers, for publishers who depend on clicks, and for how much consumers trust AI advice.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model: a text model trained on very large text collections. |
| AI | Artificial intelligence. Here it means chatbots and AI search tools. |
| ChatGPT | OpenAI's chatbot. Its web-search feature is called ChatGPT Search. |
| Generative search | Search that writes a new answer from web sources, instead of a link list. |
| Randomized experiment | A test where some people are randomly given the tool and others are not. |
| Field experiment | A randomized test run on real users of a live website or app. |
| Lab or online experiment | A recruited-participant test with set tasks, usually paid. |
| MTurk | Amazon Mechanical Turk, an online platform for paid study participants. |
| Clickstream | A log of the pages a person opens and the links they click. |
| Comscore | A company that records web browsing from a panel of consenting households. |
| Overreliance | Trusting a wrong AI answer and acting on it without checking. |
| CHI | Human-computer interaction conference run by ACM. Peer reviewed. |
| ACM | Association for Computing Machinery, a computing society that runs conferences. |
| SSRN | Social Science Research Network, a site where economists post working papers. |
| CESifo | A German economics working paper series. |
| Management Science | A peer-reviewed business and economics journal. |
| Nuremberg Institute | Nuremberg Institute for Market Decisions, a German consumer research group. |
| Semrush | A search-marketing software company that publishes traffic studies. |

## Main approaches
The main ways researchers study this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Lab and online choice tasks | Give people a shopping or fact task with one tool, then measure time and accuracy. | Spatharioti 2023, Kaiser 2025, Xu 2023 | Emerging |
| Randomized field tests on live sites | Give some site users an AI tool at random, then track purchases. | Yan 2025, Zheng 2026, Fang 2026 | Emerging |
| Usage-log studies of substitution | Compare Google use before and after ChatGPT access, using panel data. | Shi 2026, Semrush 2025 | Contested |
| Stated-preference surveys | Ask people which tool they trust and why, after a task. | Nuremberg Institute 2025 | Emerging |

## What the evidence shows
### Finding 1: LLM search makes consumers faster and reduces queries.
- **Spatharioti 2023**: 90 MTurk workers compared vehicles in five tasks → LLM tool cut time from 3.4 to 1.6 minutes.
- **Spatharioti 2023**: Queries per task fell from 2.5 to 1.9 with the LLM tool.
- **Kaiser 2025**: 1,526 U.S. participants on practical searches → ChatGPT users were faster. The abstract gives no numbers.
- **Xu 2023**: ChatGPT users spent less time on all tasks in a small study.
- **Strength:** Medium — three studies agree on direction. Only one reports exact numbers and confidence ranges, from the full text.

### Finding 2: Accuracy is similar when the LLM is right and lower when it is wrong.
- **Spatharioti 2023**: On routine tasks, accuracy was 95.3% with the LLM and 92.3% with search. The gap was not significant.
- **Spatharioti 2023**: On one hard task, accuracy was 47% with the LLM and 93% with search. Users trusted wrong LLM answers.
- **Spatharioti 2023**: Color warnings on uncertain claims helped users. On one hard task, accuracy rose from 26% to 58% with warnings.
- **Strength:** Medium — the mechanism is clear, but the hard-task gap comes from one team and one task.

### Finding 3: Users rate chatbot search as more useful, yet many still prefer Google.
- **Xu 2023**: ChatGPT users rated usefulness, enjoyment, and satisfaction higher. Overall task performance did not differ.
- **Kaiser 2025**: ChatGPT users found the correct answer more often. Most still preferred Google, and preference depended on personality.
- **Nuremberg Institute 2025**: Participants kept Google for future searches, citing habit and trust.
- **Strength:** Medium — three studies agree. Satisfaction is self-reported, and not all studies give numbers.

### Finding 4: Field tests find purchase effects in both directions.
- **Yan 2025**: On a large travel site, a reasoning assistant cut hotel bookings 2.5%. Users searched less and clicked fewer hotels.
- **Zheng 2026**: Generative search raised purchases. Users browsed fewer products and focused on relevant merchants.
- **Fang 2026**: Randomized AI query refinement on a retailer raised purchase probability 1.2%. Treated users viewed fewer products before clicking.
- **Strength:** Low — three field tests on different sites and tools. Yan and Zheng were read only from summaries.

### Finding 5: Substitution is contested.
- **Shi 2026**: Comscore panel data show a 9.4% drop in weekly traditional search queries after wider ChatGPT Search access. The drop reached about 17% after 20 weeks.
- **Semrush 2025**: U.S. desktop users who adopted ChatGPT raised their Google sessions from 10.5 to 12.6 per week.
- **Strength:** Low — one working paper read through press coverage, and one industry report. The two disagree.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do AI tools raise purchases? | Zheng 2026 and Fang 2026: more purchases on retail sites | Yan 2025: 2.5% fewer hotel bookings on a travel site | Same site, same tool, purchases measured in both |
| Does ChatGPT replace Google use? | Shi 2026: 9.4% fewer traditional searches after rollout | Semrush 2025: Google sessions rose after adoption | Panel data with the same design and a longer window |
| Are LLM answers more accurate for consumers? | Nuremberg Institute 2025: 59% vs 39% correct theme-park choice | Spatharioti 2023: 47% vs 93% on one hard task | Pre-registered tests on several tasks with one accuracy scale |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Effects by consumer type (age, income, expertise) | Shows who gains and who loses from faster search | Kaiser 2025 (personality only) |
| Purchase effects of general chatbots such as ChatGPT | Most field tests use platform tools, not chatbots | Yan 2025 (travel assistant) |
| Effects beyond 20 weeks | Habits change slowly, and short windows miss this | Shi 2026 (20-week window) |
| Non-U.S. samples | Search habits and tools vary across countries | None found |
| Wrong-answer rates in real purchases | Harm from overreliance depends on how often the tool errs | Spatharioti 2023 (one hard task) |
| Quality of the final choice | Few studies track regret or satisfaction after buying | None found |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Spatharioti 2023 | **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** | 2023 | arXiv preprint (peer-reviewed as CHI 2025, with a different title) | full text (arXiv version) |
| Kaiser 2025 | **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** | 2025 | CHI (peer reviewed) | abstract |
| Xu 2023 | **ChatGPT vs. Google: A Comparative Study of Search Performance and User Experience** | 2023 | SSRN working paper | abstract |
| Yu 2026 | **Search or Chat? Comparing How We Learn About Debated Topics** | 2026 | arXiv preprint | abstract |
| Yan 2025 | **Reasoning AI, Consumer Search, and Purchase: Evidence from an Online Platform Field Experiment** | 2025 | SSRN working paper | search summary only |
| Zheng 2026 | **Generative Search: Evidence from a Large-Scale Field Experiment** | 2026 | Management Science (peer reviewed) | search summary only |
| Fang 2026 | **Generative AI and Sales Productivity: Field Experiments in Online Retail** | 2026 | CESifo working paper | search summary only |
| Shi 2026 | **Answering without Referring: How AI Search Rewrites the Web's Economic Bargain** | 2026 | arXiv preprint | press reports only |
| Huang 2026 | **Generative AI Search on Content Creation Platform: Evidence from a Large-Scale Field Experiment** | 2026 | SSRN working paper | title only |
| Nuremberg Institute 2025 | **ChatGPT vs. Google: How AI and Traditional Searches Compare in Consumer Decision-Making** | 2025 | NIM institute report | institute summary page |
| Krefeld-Schwalb 2025 | **Search in service of choice: An agenda for comparing, extending, and integrating consumer search models** | 2025 | International Journal of Research in Marketing | title and metadata only |
| Semrush 2025 | Title not found | 2025 | Semrush industry report | press summary only |

<details><summary>Original research question</summary>

What empirical evidence (lab experiments, randomized field experiments, surveys, clickstream/log data) exists on how consumers use LLM-based search (ChatGPT, Perplexity, Bing Chat, AI Overviews, shopping assistants) versus traditional search engines — in terms of search effort, time, number of queries, breadth of options considered, decision quality, purchase outcomes, and satisfaction? Include adoption and substitution patterns (e.g., ChatGPT reducing Google usage) and heterogeneity across consumers.

</details>
