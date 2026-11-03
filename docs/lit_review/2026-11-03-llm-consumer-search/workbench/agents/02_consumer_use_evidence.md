# What empirical evidence (lab experiments, randomized field experiments, surveys, clickstream/log data) exists on how consumers use LLM-based search (ChatGPT, Perplexity, Bing Chat, AI Overviews, shopping assistants) versus traditional search engines — in terms of search effort, time, number of queries, breadth of options considered, decision quality, purchase outcomes, and satisfaction? Include adoption and substitution patterns (e.g., ChatGPT reducing Google usage) and heterogeneity across consumers.

## TL;DR
Answer: Lab and online experiments mostly find that LLM search cuts task time and query counts and raises self-reported satisfaction. Decision accuracy matches traditional search when the LLM is right but drops when it errs, because users over-trust wrong answers. Field evidence on purchases and on substitution points in opposite directions.
Strength: Low-Medium
Most studies are small (90 to 1,526 participants), mostly U.S. samples, and several results come from abstracts or secondary reports. The answer holds for product-choice and information tasks with chatbots. Heterogeneity across consumers is barely studied.

## What Exists
### Sub-theme 1: Lab and online experiments on speed, queries, accuracy, satisfaction
- **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** (Spatharioti et al., 2023, arXiv) — 90 MTurk participants did five vehicle-comparison tasks. The LLM tool cut task time from 3.4 to 1.6 min (95% CI 2.8–4.1 vs 1.4–1.9) and queries from 2.5 to 1.9 per task. On routine tasks accuracy was 95.3% (LLM) vs 92.3% (search), not significant. On one hard task accuracy was 47% (LLM) vs 93% (search).
  - Relevance: Direct randomized test of LLM vs traditional search for consumer product choice. Experiment 2 (120 MTurk participants) shows color-coded warnings raised detection of wrong LLM answers.
  - OpenAlex ID: W4383860750
  - Cited by: 28 (OpenAlex)
  - Read: full text (arXiv v2 HTML). Per-condition sample sizes not reported.
- **Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance** (Spatharioti et al., 2025, CHI) — Peer-reviewed venue for the study above. Numbers below come from the arXiv version, not the CHI version.
  - Relevance: Same study, peer reviewed. Confirms the peer-reviewed status of the 2023 preprint.
  - OpenAlex ID: W4409767160 (DOI 10.1145/3706598.3714082)
  - Cited by: 33 (OpenAlex)
  - Read: metadata only (OpenAlex record).
- **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** (Kaiser et al., 2025, CHI) — N = 1,526, described as a representative U.S. sample. ChatGPT users were faster and more often found the correct solution. They relied less on primary web sources. Participants still expressed a subjective preference for Google, and ChatGPT preference depended on personality profile. No numbers on the abstract page.
  - Relevance: Largest peer-reviewed sample found for ChatGPT vs Google. Only paper found naming personality as a moderator.
  - OpenAlex ID: not resolved
  - Read: abstract only (NIM publication page). Assignment design not stated.
- **ChatGPT vs. Google: A Comparative Study of Search Performance and User Experience** (Xu et al., 2023, SSRN) — ChatGPT group spent less time on all tasks. No significant difference in overall task performance. Higher ratings for usefulness, enjoyment, and satisfaction. Authors warn of overreliance and misinformation. ChatGPT weaker on fact-checking.
  - Relevance: Early study of the same comparison. Satisfaction gain with no accuracy gain.
  - OpenAlex ID: W4383295164 (DOI 10.2139/ssrn.4498671; also arXiv 2307.01135)
  - Cited by: 67 (OpenAlex)
  - Read: abstract only (arXiv page). Sample size not stated on the page.
- **Search or Chat? Comparing How We Learn About Debated Topics** (Yu et al., 2026, arXiv) — N = 194 crowdsourced participants. No significant difference in learning gain or critical reflection between chat and search. Time and satisfaction not in the abstract. One search-result summary reported longer chatbot time (479 s vs 329 s). Not confirmed on the abstract page.
  - Relevance: Shows the satisfaction and time gains of chat may not carry over to learning outcomes.
  - OpenAlex ID: not resolved
  - Read: abstract only (arXiv 2608.14113, submitted 14 Aug 2026). Attitude strength and intellectual humility suggested as traits that matter more than the tool.

### Sub-theme 2: Field experiments on purchases and search intensity
- **Reasoning AI, Consumer Search, and Purchase: Evidence from an Online Platform Field Experiment** (Yan et al., 2025, SSRN) — authors Se Yan, Han Zhong, Zemin Zhong, Wenyu Zhou, Nitin Mehta. More than 510,000 users at a large online travel platform randomized to a reasoning or a non-reasoning assistant. Reasoning assistant cut hotel bookings by 2.5%. Users issued fewer queries, browsed fewer hotels, and clicked fewer hotels.
  - Relevance: Only field experiment found with a chatbot-style assistant and a purchase outcome. Shows a negative purchase effect.
  - OpenAlex ID: not found in OpenAlex. SSRN ID 5631050. Year inferred from SSRN number.
  - Read: search-result summary only. SSRN page returned HTTP 403.
- **Generative Search: Evidence from a Large-Scale Field Experiment** (Zheng et al., 2026, Management Science) — generative search significantly increased consumer purchases. It reduced exploratory browsing and clicking, and concentrated evaluation within relevant categories and merchants.
  - Relevance: Peer-reviewed field experiment on AI search and purchases. Platform tool, not a general chatbot.
  - OpenAlex ID: W7214189263 (DOI 10.1287/mnsc.2025.02458). Earlier SSRN version W4411337009 (2025, two authors listed).
  - Cited by: 0 (OpenAlex)
  - Read: search-result summary only. SSRN page returned HTTP 403.
- **Generative AI and Sales Productivity: Field Experiments in Online Retail** (Fang et al., 2026, CESifo) — earlier version titled "Generative AI and Firm Productivity" (SSRN 5584850, 2025). Randomized GenAI-based query refinement. Treated consumers viewed fewer products before clicking. Clicks rose 1.1%, spend 2.9%, and purchase probability 1.2%.
  - Relevance: Shows lower search intensity with higher purchases on a retail site.
  - OpenAlex ID: W4415262827 (earlier SSRN versions W4415256060, W4415426386)
  - Read: search-result summary only (arXiv 2510.12049 is the same paper per search results). Full text not read.
- **Generative AI Search on Content Creation Platform: Evidence from a Large-Scale Field Experiment** (Huang et al., 2026, SSRN) — authors Hongxian Huang, Jinglong Zhang, Jason Chan, Anindya Ghose. Found in OpenAlex search only.
  - Relevance: Another field experiment on AI search and consumer behavior, on a content platform.
  - OpenAlex ID: W7215111980 (DOI 10.2139/ssrn.7550003)
  - Read: title and metadata only. Findings not read.

### Sub-theme 3: Substitution and adoption from usage data
- **Answering without Referring: How AI Search Rewrites the Web's Economic Bargain** (Shi et al., 2026, arXiv / SSRN) — authors Qiaoni Shi, Kai Zhu, Kai Gu (Bocconi University). Uses Comscore desktop clickstream data (Oct 2024 to Jul 2025) and the staggered rollout of ChatGPT Search. Wider access linked to about 9.4% fewer weekly traditional search queries, rising to about 17% by week 20. Authors frame it as association.
  - Relevance: Best causal-style evidence on substitution found. Outcome is query volume, not purchases.
  - OpenAlex ID: W7167813029 (arXiv 2607.07652); W7170048783 (SSRN 7035298)
  - Read: secondary press reports only. Sources disagree on details (one account gives 4.9% rising to 8.2% for existing ChatGPT users).
- **Semrush clickstream study of ChatGPT adopters** (Semrush, 2025, industry report) — U.S. desktop users who started ChatGPT in Q1 2025. Google Search sessions rose from 10.5 to 12.6 per week after adoption, against a non-user control group. Opt-in panel, 90-day window. Counted as industry, not in the paper count.
  - Read: secondary summary only. Semrush primary report not read.

### Sub-theme 4: Stated preferences and tool choice
- **ChatGPT vs. Google: How AI and Traditional Searches Compare in Consumer Decision-Making** (Nuremberg Institute for Market Decisions with Vorarlberg University of Applied Sciences, 2025, not confirmed) — participants chose the best of three options in smartphone or theme park categories. ChatGPT users picked the correct theme park 59% of the time vs 39% for Google. ChatGPT users were faster. Most still preferred Google for future searches, citing habit and trust.
  - Relevance: Only study where ChatGPT improved accuracy on a consumer choice. Preference result matches Kaiser et al.
  - OpenAlex ID: not resolved. Authors and year not confirmed.
  - Read: NIM institute summary page only. Full paper not found.

### Sub-theme 5: Conceptual framing
- **Search in service of choice: An agenda for comparing, extending, and integrating consumer search models** (Krefeld-Schwalb et al., 2025, International Journal of Research in Marketing) — research agenda on comparing LLM-era search with existing consumer search models.
  - Relevance: Marketing framing paper. Could guide how to write up the field gap.
  - OpenAlex ID: W4413919948. Cited by: 1 (OpenAlex)
  - Read: metadata only.

## Reference Chain Discoveries
- Found via: OpenAlex citation traversal of Spatharioti et al. 2023 (W4383860750). Its 10 most-cited citers were all off-topic (LLM security, labor markets, RAG systems, education). OpenAlex lists no references for it, so backward traversal was not possible.
- Found via: OpenAlex citation traversal of Xu et al. 2023 (W4383295164). Citers were off-topic (higher education, LLM evaluation surveys).
- Found via: Reference mining of Spatharioti et al. 2023 related work. Named prior work covers search-behavior models (Bates 1989; Bennett et al. 2012; Ramos & Cota 2008) and LLM productivity field studies (Brynjolfsson et al. 2023; Dell'Acqua et al. 2023). Background only, not consumer-search evidence.
- Cross-stream leads, not counted: arXiv 2608.18352 (preregistered AI Overviews field experiment, N = 1,100, search-volume result not read). arXiv 2512.09483 (source coverage and citation bias, stream 03). arXiv 2504.06435 (human trust in AI search, stream 07). These were not read in full.
- Lead found, not read: "Consumer Responses to Generative AI Chatbots Versus Search Engines for Product Evaluation" (ResearchGate PDF). Authors and year not verified.

## What's Missing (Gaps)
- Heterogeneity: only personality (Kaiser et al.) and attitude strength (Yu et al.) appear as moderators. No study estimates effects by age, income, expertise, or product category with adequate power.
- Purchase outcomes for general chatbots such as ChatGPT. Field tests so far use platform-specific assistants (travel, retail, content platform).
- Long-run adoption beyond 20 weeks. Field windows run 90 days (Semrush) and 20 weeks (Shi et al.).
- Non-U.S. samples. All experiments found use U.S. participants or U.S. panels.
- Wrong-answer rates in real purchase tasks. Spatharioti et al. used one hard task. Overreliance cost depends on how often the tool errs.
- Welfare or decision-quality outcomes for high-stakes purchases. No study measures post-purchase regret or satisfaction with the choice.

## Contradictions or Tensions
- Purchases: Zheng et al. (2026) and Fang et al. (2026) find more purchases with AI search on retail platforms. Yan et al. (2025) find 2.5% fewer hotel bookings with a reasoning assistant. Different platforms, tools, and outcomes. Not directly comparable.
- Substitution: Shi et al. (2026) find about 9.4% fewer traditional search queries after rollout. Semrush (2025) finds Google sessions rising after adoption. Different designs (rollout vs self-selected adopters). Semrush is not peer reviewed.
- Accuracy: Spatharioti et al. (2023) find much lower accuracy with the LLM on one hard task (47% vs 93%). Nuremberg Institute (2025) find higher accuracy with ChatGPT (59% vs 39%). Different tasks and accuracy definitions.
- Learning: Yu et al. (2026) find no difference in learning gain. Xu et al. (2023) and Spatharioti et al. (2023) find higher satisfaction and faster work with the LLM. Satisfaction and speed do not map to learning.

## Confidence
Overall: Low-Medium.
- What would raise confidence: Full text of Kaiser et al. (CHI 2025) and Zheng et al. (Management Science 2026) to check the reported numbers. A preregistered multi-platform experiment with purchase outcomes. Full text of Shi et al. with its panel details.
- What would lower confidence: Replication of the 9.4% substitution estimate on another panel or device. Failure of Spatharioti's hard-task accuracy gap in a larger sample. Evidence that the Yan et al. booking drop is short-lived.

## Search Log
### Round 1: Broad search
- Queries: (1) randomized field experiment ChatGPT consumer search shopping behavior; (2) generative AI search versus traditional search engine lab experiment consumers decision quality; (3) ChatGPT substitution Google search traffic clickstream evidence; (4) LLM chatbot vs search engine user study number of queries time task completion satisfaction arXiv
- Papers found: 7 unique relevant studies (Spatharioti 2023, Xu 2023, Yu 2026, Yan SSRN, Zheng SSRN, Fang 2026, NIM theme park). Plus industry coverage (Semrush, Comscore).
- Key leads: Spatharioti 2023 (arXiv 2307.03744, randomized); Yan SSRN (travel field experiment); Comscore substitution study.

### Round 2: Citation traversal
- Papers traversed: Spatharioti 2023 (W4383860750), Xu 2023 (W4383295164). Also resolved NIM large-scale study (Kaiser et al.) via its publication page.
- New papers from references: none relevant (OpenAlex reference list empty for Spatharioti 2023).
- New papers from citers: none relevant. Only off-topic citers.
- New relevant papers this round: 2 (Kaiser et al. 2025 CHI; Shi et al. 2026 Bocconi, via press coverage of the Comscore study).
- Queries (targeted): "Comscore ChatGPT Search rollout staggered adoption"; "Nuremberg Institute ChatGPT Google theme park"; "arXiv generative AI search consumers search intensity field experiment LLM assistant e-commerce 2025".

### Round 3: Reference section mining
- Papers mined: Spatharioti et al. 2023 (related work, full HTML). SSRN pages for Yan et al. and Zheng et al. returned HTTP 403, so their full text was not read.
- New relevant papers: none. Related work names only older search-behavior and productivity studies.

### Round 4: Gap-filling
- Gaps targeted: heterogeneity across consumers; adoption and substitution; purchase outcomes for general chatbots; critique of the Semrush study.
- Queries: "generative AI search heterogeneity consumers" (OpenAlex); "large language model search engine use adoption survey consumers heterogeneity" (OpenAlex); "ChatGPT search access traditional search queries natural experiment" (OpenAlex); "conversational AI shopping assistant consumer decision experiment" (OpenAlex); "critique Semrush ChatGPT Google complementarity clickstream study methodology limitations"; "Bocconi working paper ChatGPT Search access Comscore" (identified Shi et al. title and authors).
- New relevant papers: 2 (Huang et al. 2026 SSRN; Krefeld-Schwalb et al. 2025 IJRM). Heterogeneity search found no consumer-specific paper.
- Semrush critique: no independent critique found. Limitations noted from the study's own write-up and commentary.

### Round 5: Adversarial check
- Targets: critiques of over-trust and overreliance findings; verification of the Yu et al. ID and Xu et al. record; author check for Fang et al., Shi et al., Zheng et al. in OpenAlex.
- Queries: "LLM chatbot search users over-reliance wrong answers worse decisions study critique generative search misinformation consumers" (WebSearch); OpenAlex author lookups for Fang, Shi, Zheng, Spatharioti CHI version.
- New findings: no new relevant consumer-search papers. Adversarial results (over-trust of fluent LLM answers; citation accuracy errors in news search) support Spatharioti et al. A widely cited 60% wrong-answer figure from a news citation test was judged too narrow for consumer decisions.
- Verified: Yu et al. ID (arXiv 2608.14113) and Xu et al. (SSRN and arXiv).

### Convergence note
- Total unique relevant studies: 11 (12 entries, since Spatharioti et al. appears as arXiv 2023 and CHI 2025 for one study).
- New relevant papers in last round: 0 (Round 5). In Round 4: 2.
- Stopped because: 5 rounds completed. Sub-questions have answers: adoption, substitution, speed, accuracy, satisfaction, purchases. Heterogeneity is answered as "little direct evidence." The stopping rule's strict condition (last two rounds with zero new papers) was not met, since Round 4 found 2. I stopped because search returns had dropped to near zero and the remaining heterogeneity gap is a literature gap, not a search gap.

## Paper list (for Obsidian export)
- **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** (Spatharioti et al., 2023, arXiv) — LLM tool halved task time and cut queries; hard-task accuracy much lower (47% vs 93%).
  - OpenAlex ID: W4383860750
  - Cited by: 28
- **Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance** (Spatharioti et al., 2025, CHI) — Peer-reviewed version of the study above.
  - OpenAlex ID: W4409767160
  - Cited by: 33
- **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** (Kaiser et al., 2025, CHI) — N = 1,526 U.S.; faster and more correct with ChatGPT; still prefer Google.
  - OpenAlex ID: not resolved
- **ChatGPT vs. Google: A Comparative Study of Search Performance and User Experience** (Xu et al., 2023, SSRN) — less time, similar performance, higher satisfaction with ChatGPT.
  - OpenAlex ID: W4383295164
  - Cited by: 67
- **Search or Chat? Comparing How We Learn About Debated Topics** (Yu et al., 2026, arXiv) — N = 194; no difference in learning gain.
  - OpenAlex ID: not resolved
- **Reasoning AI, Consumer Search, and Purchase: Evidence from an Online Platform Field Experiment** (Yan et al., 2025, SSRN) — 510,000+ travel users; reasoning assistant cut hotel bookings 2.5%.
  - OpenAlex ID: not found (SSRN 5631050)
- **Generative Search: Evidence from a Large-Scale Field Experiment** (Zheng et al., 2026, Management Science) — generative search raised purchases; reduced exploratory browsing.
  - OpenAlex ID: W7214189263
  - Cited by: 0
- **Generative AI and Sales Productivity: Field Experiments in Online Retail** (Fang et al., 2026, CESifo) — query refinement: fewer products viewed, 1.2% higher purchase probability.
  - OpenAlex ID: W4415262827
- **Generative AI Search on Content Creation Platform: Evidence from a Large-Scale Field Experiment** (Huang et al., 2026, SSRN) — title and metadata only.
  - OpenAlex ID: W7215111980
- **Answering without Referring: How AI Search Rewrites the Web's Economic Bargain** (Shi et al., 2026, arXiv) — Comscore panel; about 9.4% fewer traditional queries after ChatGPT Search access (association).
  - OpenAlex ID: W7167813029
- **ChatGPT vs. Google: How AI and Traditional Searches Compare in Consumer Decision-Making** (Nuremberg Institute for Market Decisions, 2025, not confirmed) — 59% vs 39% correct theme park choice with ChatGPT vs Google.
  - OpenAlex ID: not resolved
- **Search in service of choice: An agenda for comparing, extending, and integrating consumer search models** (Krefeld-Schwalb et al., 2025, International Journal of Research in Marketing) — research agenda; metadata only.
  - OpenAlex ID: W4413919948
  - Cited by: 1

Industry sources, not counted: Semrush clickstream study (2025). Similarweb reports 95% of ChatGPT users also use Google (no primary source read).
