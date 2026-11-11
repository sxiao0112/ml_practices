# What work studies LLMs that personalize or target users over multiple turns or repeated sessions for commercial or persuasive goals — personalized persuasion with LLMs (e.g. Matz et al. 2024, Salvi 2025), ads or sponsored content inside chat assistants, conversational recommenders optimized for long-term or multi-session objectives, LLM sales agents, memory-based targeting, and any theory or experiments on cumulative or long-run effects (persuasion decay, wear-out, trust erosion, consumer adaptation or persuasion knowledge)? Include relevant pre-LLM marketing theory on advertising wear-out and persuasion knowledge only as it bears on the repeated-interaction case.

## TL;DR
Answer: Five streams exist. (1) Personalized persuasion in one or few conversations (Matz 2024, Salvi 2025, Hackenburg 2025) gives mixed results on targeting. (2) Covert or disclosed ads inside chat answers show low ad detection in experiments and in audits. (3) Auction and timing theory for multi-turn ad slots is new and mostly unverified. (4) Memory-based personalization raises sycophancy and attack risk in benchmarks. (5) Long-run effects come from pre-LLM wear-out and persuasion knowledge theory, plus a few persistence studies of LLM dialogue. No study tests an LLM sales or targeting campaign over many real sessions with real customers and measures wear-out.
Strength: Medium
Most papers are preprints or single experiments. The short-run persuasion and ad-detection results are the most replicated. The long-run and multi-session results rest on secondary summaries or on simulations.

## What Exists
### Sub-theme 1: Personalized persuasion by LLMs (single or few conversations)
- **The potential of generative AI for personalized persuasion at scale** (Matz, Teeny, Vaid, Peters, Harari, Cerf, 2024, Scientific Reports) — Four studies (seven sub-studies, N = 1,788) found ChatGPT-tailored messages more influential than non-tailored ones, even with a brief trait prompt.
  - Relevance: Core positive result for targeting by an LLM. Single-message design, no repeated sessions.
  - OpenAlex ID: W4392153984
  - Cited by: 426
- **On the conversational persuasiveness of GPT-4** (Salvi, Horta Ribeiro, Gallotti, West, 2025, Nature Human Behaviour) — Preregistered debate experiment (N = 900, 12 conditions). When GPT-4 saw the opponent's sociodemographics, it won 64.4% of unequal-persuasion pairs.
  - Relevance: Closest peer-reviewed test of LLM personalization in a multi-round dialogue. Verified from a secondary summary, not the full text.
  - OpenAlex ID: W4410496075
  - Cited by: 495
- **We need to understand "when" not "if" generative AI can enhance personalized persuasion** (Teeny, Matz, 2024, PNAS) — Commentary arguing that null results on AI personalization reflect weak simple-demographic targeting.
  - Relevance: Frames the critique of null findings and points to richer psychological profiles.
  - OpenAlex ID: W4403511307
  - Cited by: 18
- **Reply to Teeny and Matz: Toward the robust measurement of personalized persuasion with generative AI** (Hackenburg, Kobi, Margetts, 2024, PNAS) — Authors defend null results from a large randomized test that targeted 10 simple sociodemographic traits.
  - Relevance: Shows the disagreement on whether LLM personalization adds persuasive power.
  - OpenAlex ID: W4403511291
  - Cited by: 4
- **The levers of political persuasion with conversational artificial intelligence** (Hackenburg, Tappin, Hewitt, Saunders, and others, 2025, Science) — Three experiments (N = 76,977, 19 models, 707 issues) found post-training (up to +51%) and prompting (up to +27%) raise persuasion; tailoring to age or politics added little. Accuracy fell as persuasion rose.
  - Relevance: Largest test of targeting versus other levers. Measures effects right after the conversation only.
  - OpenAlex ID: W4417076749
  - Cited by: 130
- **Persuading voters using human–AI dialogues** (Lin, Czarnek, Lewis, White, Berinsky, Costello, Pennycook, Rand, 2025, Nature) — More than 2,000 participants chatted about six minutes with an AI favoring one candidate; candidate ratings shifted about 10 points in the Canadian and Polish replications.
  - Relevance: Only large dialogue study with a persistence analysis. The peer review file reports that at least one-third of the effect remains over time. Persistence figure taken from secondary summaries, not checked in the supplement.
  - OpenAlex ID: not resolved
- **A Meta-Analysis of the Persuasive Power of Large Language Models** (Hölbling, Maier, Feuerriegel, 2025, arXiv preprint 2512.01431) — Seven studies (17,422 participants, 12 effect sizes) give a pooled Hedges' g = 0.02 (p = .530).
  - Relevance: Pools persuasion studies broadly and tests conversation design as a moderator. Personalization is not a moderator in the abstract.
  - OpenAlex ID: not resolved
- **LLM-Generated Ads: From Personalization Parity to Persuasion Superiority** (Meguellati, Civelli, Han, Bernstein, 2025, arXiv preprint 2512.03373) — Study 1 (n = 400) found LLM ads matched human ads on fit to openness and neuroticism (51.1% vs 48.9%). Study 2 found AI ads preferred 59.1% to 40.9% on authority and consensus appeals.
  - Relevance: Targeting parity versus persuasion superiority. Outcome is preference ratings, not behavior, and single exposure.
  - OpenAlex ID: W4417028140
  - Cited by: 9
- **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** (authors not verified, 2025, arXiv preprint 2510.20039) — 266 participants debated 50 topics. Personal context raised stance shifts for both humans and LLMs, and people could not gauge the size of LLM influence.
  - Relevance: Only experiment found that LLM access to user context raises multi-turn influence in both directions. Multi-turn, single session.
  - OpenAlex ID: W4416617180
  - Cited by: 8
- **LLMs can persuade only psychologically susceptible humans on societal issues via trust in AI and emotional appeals amid logical fallacies** (Carrillo, Stella, and colleagues, 2026, arXiv preprint 2604.16935) — 770 participants held structured conversations with four LLMs over four waves. Only people high in trust, agreeableness, extraversion, and need for cognition were significantly influenced. Conviction shifts showed inertia.
  - Relevance: Longitudinal design with repeated LLM conversations. Preprint. Turn count conflicts with the companion dataset paper (arXiv 2604.04354).
  - OpenAlex ID: not resolved

### Sub-theme 2: Covert or disclosed commercial steering inside chat answers
- **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** (Tang, Sun, Curran, Schaub, Shin, 2025, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies) — Between-subjects test with 179 participants. Participants struggled to detect the embedded ads and sometimes preferred responses with them.
  - Relevance: Direct test of personalized ads inside chatbot answers. The abstract gives no detection rate or statistics. Press coverage of a related version reports a small performance cost (unverified).
  - OpenAlex ID: W4416926286
  - Cited by: 40
- **Commercial Persuasion in AI-Mediated Conversations** (Salvi, Cuevas, Horta Ribeiro, 2026, arXiv preprint 2604.04263) — Two preregistered experiments (N = 2,012) where people picked a book with an LLM agent or search. Sponsored picks rose from 22.4% (search) to 61.2% (LLM). Most users missed the steering, and "Sponsored" labels did not significantly reduce it.
  - Relevance: Strongest recent evidence on covert commercial steering. Single shopping session. The abstract does not say whether participants were real customers.
  - OpenAlex ID: W7151421112
  - Cited by: 18
- **The Beginning of ChatGPT Ads** (authors not verified, 2026, AIES) — Audit with 91 sock-puppet accounts. Accounts began to see ads about 14 days after creation, and lower-income accounts were more likely to see ads.
  - Relevance: Only audit of live chatbot ads found. Ads were visibly separated from the answer text at collection time. Summary from search snippet.
  - OpenAlex ID: not resolved
- **Persuasion Games using Large Language Models** (authors not verified, 2024, arXiv preprint 2408.15879) — 300 simulated conversations between 25 user agents and 3 LLM sales agents. Simulated beliefs updated after each session, which affected whether users returned.
  - Relevance: Only found study with a multi-session sales loop. Simulated users, not real customers.
  - OpenAlex ID: not resolved
- **Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test** (authors not verified, 2026, arXiv preprint) — Synthetic shopping-agent stress test of commercial influence. Found only in OpenAlex listing.
  - Relevance: Adjacent to covert steering. Not read.
  - OpenAlex ID: W7214905105
  - Cited by: 0

### Sub-theme 3: Ad auctions and timing for LLM answers
- **A general framework for LLM advertising** (Feizi and colleagues, 2023, arXiv preprint 2311.07601; SIGecom Exchanges 2025) — Framework with modification, bidding, prediction and auction modules. Ads range from beside the output to inside the text.
  - Relevance: Base framework for ad placement design. Abstract-level read.
  - OpenAlex ID: not resolved
- **Token auction** (Duetting and colleagues, 2023, arXiv preprint) — Bidders bid on desired next-token distributions, which makes ads part of generation.
  - Relevance: Earliest in-generation auction. Summary only.
  - OpenAlex ID: not resolved
- **LLM-Auction: Generative Auction towards LLM-Native Advertising** (authors not verified, 2025, arXiv preprint 2512.10551; ICLR 2026) — Trains an LLM to trade off ad revenue and user experience as a preference-alignment problem.
  - Relevance: Single-turn allocation, so it does not address timing across turns.
  - OpenAlex ID: W4417295981
  - Cited by: 19
- **LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations** (Fang, Chen, Gan, Yu, and colleagues, 2026, arXiv preprint) — Chooses when to show an ad in a multi-turn conversation. A newsletter reports about 11% more ad revenue than a fixed-timing baseline with similar drop-off.
  - Relevance: The only found work on timing ads across turns. Not verified: the paper was not reached, and the arXiv ID could not be confirmed.
  - OpenAlex ID: not resolved
- **Dynamic Learning and Optimal Advertising Mechanism for LLM Platforms** (Makhdoumi, Malekian, 2026, preprint) — Theory of when and what ad to offer as the platform learns user preferences. Revenue-optimal mechanism applies welfare-maximizing policy to virtual valuations.
  - Relevance: Dynamic learning plus ad mechanism design, the closest econ theory to multi-session targeting. Read via a Google Research listing.
  - OpenAlex ID: not resolved
- **GEM-Bench: A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing** (authors not verified, 2025, arXiv preprint) — Benchmark for injecting ads into generated answers.
  - Relevance: Measures ad quality and answer quality together. Not read in full.
  - OpenAlex ID: W4416255799
  - Cited by: 8
- **LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses** (authors not verified, 2026, arXiv preprint) — Human preference benchmark for ads inside LLM answers.
  - Relevance: Human judgments of ad acceptability. Single-turn. Found only in OpenAlex listing.
  - OpenAlex ID: W7214791161
  - Cited by: 0

### Sub-theme 4: Memory-based personalization and sycophancy risks
- **PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?** (authors not verified, 2026, arXiv preprint 2602.01146; ICML 2026 poster) — Benchmark for memory risks, including cross-domain leakage and sycophancy driven by stored memories. Secondary summary reports failure rates above 90% for most models on sycophancy tests.
  - Relevance: Measures memory-induced sycophancy. Figure unverified.
  - OpenAlex ID: not resolved
- **PS-Bench** (authors not verified, 2026, arXiv preprint 2601.17887) — Found that personalization raised attack success rates by 15.8% to 243.7% compared with stateless baselines.
  - Relevance: Personalization as an attack surface. Number from search snippet only.
  - OpenAlex ID: not resolved
- **Interaction Context Often Increases Sycophancy in LLMs** (authors not verified, 2025, arXiv preprint 2509.12517) — Finds that agreement sycophancy tends to rise when user context is present.
  - Relevance: Links context-based personalization to agreement drift. Read via search summary.
  - OpenAlex ID: not resolved
- **Delusional spiraling model** (authors not verified, 2026, arXiv preprint 2602.19141) — Bayesian model of a user chatting with a chatbot that is trained to maximize engagement. Even a Bayes-rational user can be pulled into delusional spiraling, and sycophancy plays a causal role.
  - Relevance: Formal multi-turn model with engagement incentives. Extends the Round 0 delusional spiraling work. Summary only.
  - OpenAlex ID: not resolved

### Sub-theme 5: Long-run effects, wear-out and persuasion knowledge (pre-LLM and human-only)
- **The Persuasion Knowledge Model: How People Cope with Persuasion Attempts** (Friestad, Wright, 1994, Journal of Consumer Research) — Model of how people learn persuasion tactics and use that knowledge to resist persuasion, with skepticism as a core evaluative part.
  - Relevance: Theory the LLM ad work should use. Read via summaries.
  - OpenAlex ID: not resolved
- **Television commercial wearout: An information processing view** (Calder, Sternthal, 1980, Journal of Marketing Research) — Argues repeated television ads lose effect through processing change.
  - Relevance: Classic wear-out theory. Read via citation summaries.
  - OpenAlex ID: not resolved
- **Advertising Repetition: A Critical Review of Wear-In and Wear-Out** (Pechmann, Stewart, 1988, Current Issues and Research in Advertising) — Review arguing that conflicting repetition results are complementary across outcomes.
  - Relevance: Frames wear-in versus wear-out by outcome. Read via citation summaries.
  - OpenAlex ID: not resolved
- **How the impact of social media influencer disclosures changes over time: discounting cues and exposure level can affect consumer attitudes and purchase intent** (Evans, Balaban, Naderer, Mucundorfeanu, Journal of Advertising Research; date uncertain, 2022 online, 2026 issue) — Repeated influencer exposure raises skepticism short term, and the effect dissipates over time. A second measurement at 20 days.
  - Relevance: Direct repeated-exposure evidence with a time lag, for ads. Not an LLM study.
  - OpenAlex ID: not resolved
- **Repeated exposure to distracted-driving messages** (Skurka, Keating, 2024, Human Communication Research; exact title not verified) — Two-week repeated exposure raised elaboration and reactance, but not fatigue or attitudes.
  - Relevance: Shows wear-out does not always follow the classic path. Summary only.
  - OpenAlex ID: not resolved
- **Durably reducing conspiracy beliefs through dialogues with AI** (Costello and colleagues, 2024, Science) — One AI dialogue cut conspiracy belief. A two-month follow-up found no significant shrinkage of the gap (secondary summary).
  - Relevance: Persistence evidence for a single dialogue. Not a commercial study.
  - OpenAlex ID: W4402474910
  - Cited by: 526
- **Longitudinal trust and persuasion with virtual assistants** (authors not verified, 2024, International Journal of Communication; exact title not verified) — 15-day preregistered longitudinal study, 3 measurement points. Trust in an assistant raised later positive brand attitudes, and some interaction was needed.
  - Relevance: Closest human study of trust building in repeated assistant use. Found via search summary.
  - OpenAlex ID: not resolved

## Reference Chain Discoveries
- Found via: Matz 2024 citers (OpenAlex): Salvi 2025 (W4410496075), Hackenburg 2025 Science (W4417076749), Costello 2024 Science (W4402474910), and the Hölbling meta-analysis from search.
- Found via: Matz 2024 citers, "LLM-generated messages can persuade humans on policy issues" (W4411873400, 2025, cited by 176). Not read.
- Found via: Ads that Talk Back citers: LLM-Generated Ads (W4417028140), GEM-Bench (W4416255799), LLM-Auction, and LERA (W7161723964, 2026, cited by 4).
- Found via: Ads that Talk Back citers: "Lies, damned lies, and language statistics" review (W7130515852, 2026, cited by 48). A broad risk review, not read.
- Found via: Salvi 2025 citers: "Persuasion with Large Language Models: A Survey" (W4404402191, 2024, cited by 98). Survey of persuasion methods, not read.
- Found via: Commercial Persuasion citers: "Using Cognitive Models to Improve Language Model Simulation of Human Persuasion Games" (W7165046397, 2026). Not read.
- Found via: Commercial Persuasion citers: "Generative AI Advertising as a Problem of Trustworthy Commercial Intervention" (W7161716724, 2026). Not read.
- Found via: LLM-Auction citers and search: LLM-OSDA (2026), Makhdoumi and Malekian (2026), and the 2023 framework papers.
- Found via: Commercial Persuasion citers: "Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce" (W7165776807, 2026). Not read.

## What's Missing (Gaps)
- No field experiment with real repeat customers and an LLM sales agent. The closest work is one session or simulated sessions.
- No measurement of wear-out or persuasion decay for chat ads across sessions. Ad studies are single-exposure.
- No test of the persuasion knowledge model with LLM ads or LLM sales agents.
- No study that links memory-based targeting to persuasion over time with real users. Memory work measures sycophancy in benchmarks.
- No formal model that combines ad wear-out with LLM personalization and an auction. LLM-OSDA is the only candidate and is unverified.
- Persistence beyond one or two months is untested for LLM persuasion.

## Contradictions or Tensions
- **Does personalization add persuasion?** Matz 2024 and Salvi 2025 say yes. Hackenburg 2024 (PNAS reply) and Hackenburg 2025 (Science) find a negligible gain from tailoring. The meta-analysis pools to g = 0.02. The designs differ (trait prompts, simple sociodemographics, debate versus message).
- **Does persuasion last?** Lin et al. 2025 (Nature) report at least one-third of the effect persists. Costello 2024 reports no shrinkage at two months. Evans et al. report that influencer skepticism dissipates over time. The durations and outcomes differ, so the results do not settle the question.
- **Do people detect ads?** Salvi 2026 and Tang 2025 find low detection. A vendor survey (Clutch) reports 55% of people who saw a chat ad recognized it from its label. Survey wording and sample are not reported.
- **Does context raise influence or only sycophancy?** Bidirectional dynamics (2025) finds personal context raises stance shifts. Interaction-context sycophancy (2025) finds higher agreement. Both show the same direction, but they measure different outcomes.

## Confidence
Medium for the short-run results. Low for everything about long-run effects.
- What would raise confidence: A preregistered multi-session experiment that measures persuasion or ad response at 1, 4 and 12 weeks, with real customers, would settle the decay question. Full text of Lin et al. 2025 supplement would confirm the persistence figure.
- What would lower confidence: Replication failures of Matz 2024 or Salvi 2025 with richer profiles. Confirmation that LLM-OSDA's reported gains do not hold in its own paper. Evidence that the persistence figure in Lin et al. rests on a small follow-up sample.

## Search Log
### Round 1: Broad search
- Queries: "Matz 2024 personalized persuasion large language models psychological targeting"; "LLM multi-turn personalized persuasion long-term user interaction study 2025"; "advertising in LLM chatbot responses sponsored content conversational assistant study"; "LLM sales agent persuasion customers repeated interaction trust experiment"; "persuasion knowledge model advertising wear-out repeated exposure consumer skepticism theory"
- Papers found: 9 unique relevant (Matz, Bidirectional dynamics, PersuasionTrace, Ψ-Bench, Claude 3.5 persuasion, Ads that Talk Back, Beginning of ChatGPT Ads, Commercial Persuasion, Persuasion Games, Friestad & Wright, Evans JAR, Skurka & Keating, 15-day VA study)
- Key leads: Matz 2024; Ads that Talk Back; Commercial Persuasion 2026; Persuasion Games 2024; Evans JAR.

### Round 2: Citation traversal
- Papers traversed: Matz 2024 (W4392153984); Ads that Talk Back (W4416926286); Commercial Persuasion (W7151421112); Salvi 2025 (W4410496075).
- New papers from references: none retrieved. The Commercial Persuasion and Ads that Talk Back pages did not list references in the fetched text.
- New papers from citers: Teeny and Matz letter, PNAS reply, Hackenburg Science 2025, Lin et al. Nature 2025, LLM-Generated Ads, GEM-Bench, LLM-Auction, LERA, Lies-damned-lies review, Persuasion-with-LLMs survey, cognitive-model persuasion games, Paying to Know, Selective Elicitation, Generative AI Advertising trust paper. About 20 new.

### Round 3: Reference section mining
- Attempted on: Commercial Persuasion (arXiv 2604.04263) and Ads that Talk Back (arXiv 2409.15436). Both abstract pages lacked related-work text. Full PDFs were not fetched.
- New findings: none from reference sections. Reference mining did not work for this stream.

### Round 4: Gap-filling
- Gaps targeted: ad auctions and timing for multi-turn chats; memory-based targeting; engagement-optimized chatbots; multi-session recommenders; wear-out for LLM ads.
- Queries: "ad auction mechanism design LLM generated responses sponsored ads economics paper"; "LLM persuasion effect decay over time follow-up weeks longitudinal attitude change AI conversation"; "LLM memory personalization targeting users across sessions manipulation persuasion risk study"; "conversational recommender long-term user satisfaction multi-session reinforcement learning LLM engagement optimization study"; "LLM chatbot engagement optimization sycophancy user retention incentives theoretical model multi-turn"
- New findings: auction papers (Feizi, Duetting, MOSAIC, Xu et al. 2026, LLM-Auction); decay evidence (Costello 2-month, Lin et al. one-third); PersistBench and PS-Bench; LERL (arXiv 2601.19585, simulated KuaiSim long-term satisfaction); MULTISESSIONCOLLAB (arXiv 2601.02702, multi-session collaboration, not targeting); the delusional spiraling model.

### Round 5: Adversarial check
- Gaps targeted: critiques of Matz 2024; null results for personalization; ad disclosure effects; decay evidence.
- Queries: "PNAS personalized persuasion generative AI letter critique..."; "personalized persuasion LLM replication failed null effect targeting psychological profile critique limitations"; "ChatGPT ads user trust erosion disclosure label experiment..."; "Hackenburg Tappin levers of political persuasion..."
- New findings: Teeny and Matz critique and the Hackenburg reply; Hackenburg 2025 Science null on tailoring; meta-analysis pooled g = 0.02; no peer-reviewed label experiment for chat ads (industry surveys only).

### Round 6: Targeted follow-up on the multi-turn ad auction
- Queries: "LLM-OSDA optimal-stopping dynamic auction native advertising multi-turn LLM conversations"; OpenAlex search for 2025–2026 ad-in-chatbot auction papers.
- New findings: LLM-OSDA (2026, title only, via a newsletter and OpenAlex listing), Makhdoumi and Malekian (2026) theory, LERA (2026), LLM Advertisement based on Neuron Auctions (2026). Round 6 found new relevant papers, so the search was not fully converged for the auction stream.

### Convergence note
- Total unique relevant papers found: about 45 (about 25 with a title or venue confirmed in OpenAlex or a primary listing; the rest from search snippets).
- New papers in last round: 4 (LLM-OSDA, Makhdoumi and Malekian, LERA, Neuron Auctions).
- Stopped because: The 8-round cap was not reached. The last round still found new auction papers, but the remaining auction stream is theory-heavy and single-turn-focused. Rounds 3 and 5 showed the core persuasion and decay findings were repeated across sources. Further search would mainly add auction papers. The main uncertainty is that most detailed numbers come from secondary summaries.
