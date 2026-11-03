# How well do LLM agents perform as delegated shoppers on behalf of consumers (agentic commerce)? Cover choice rationality and consistency (e.g., GARP tests, revealed preference), behavioral biases (position, anchoring, decoy effects), benchmarks for shopping agents (WebShop, ShoppingBench and successors), alignment of agent choices with the user's true preferences, and market-level effects when sellers and buyers both use AI agents (agent-to-agent negotiation, simulated marketplaces).

## TL;DR
Answer: LLM shopping agents make inconsistent choices that depend on the model, position, and framing. Position bias is the most reproducible effect, and anchoring can collapse simulated markets. Decoy-effect results conflict. Shopping benchmarks show low task success on realistic products.
Strength: Medium
Position and anchoring effects replicate across several 2025-2026 studies, but most are preprints or single-model audits. Conditions matter: results shift with model version, interface (text-only vs. visual), and prompt wording. Little evidence covers real purchases with real money or long-term user satisfaction.

## What Exists
### Sub-theme 1: Choice rationality and consistency (GARP, revealed preference)
- **The Emergence of Economic Rationality of GPT** (Chen, Liu, Shan, Zhong, 2023, PNAS) — GPT made budget allocations in risk, time, social and food domains and looked largely rational, scoring above human benchmarks in the literature. Scores were sensitive to language framing.
  - Relevance: Baseline evidence that LLMs pass revealed-preference style tests in simple allocation tasks. Its framing sensitivity is the first warning sign for shopping.
  - OpenAlex ID: W4389611357
  - Cited by: 167
  - Read: arXiv abstract (v3). Price-framing and discrete-choice results were not visible in the abstract.
- **Economic Rationality under Specialization: Evidence of Decision Bias in AI Agents** (Wen, 2025, arXiv preprint) — Agents given specialist roles (biotech expert, economist) violated GARP more often and showed lower CCEI than generalist GPT.
  - Relevance: Shows that persona or role prompts, which shopping agents often use, can reduce choice consistency.
  - OpenAlex ID: W4407012287
  - Cited by: 0
  - Read: OpenAlex abstract only.
- **Alignment Revisited: Are Large Language Models Consistent in Stated and Revealed Preferences?** (authors not verified, 2025, arXiv 2506.00751) — Small changes in prompt format flipped revealed choices in several models.
  - Relevance: Stated preferences (what the user says) may not predict agent choices. This matters for agents that act on stated needs.
  - Read: search snippet only.
- **What Do LLMs Want?** (Federal Reserve FEDS staff, 2026, FEDS working paper; authors not verified) — Prompt framing pushes models toward payoff-maximizing play. In a dynamic job-search task, preferences looked more fragile.
  - Relevance: Shows fragility grows in multi-step settings, which is closer to shopping than one-shot allocation.
  - Read: search snippet only.
- **Irrelevant Alternatives Bias Large Language Model Hiring Decisions** (Valkanova and Yordanov, 2024, Findings of EMNLP 2024; arXiv 2409.15299) — GPT-3.5 and GPT-4 showed a significant attraction (decoy) effect when acting as recruiters.
  - Relevance: Decoy evidence from a non-shopping setting. Shows the effect can appear in LLM choice tasks.
  - Read: search snippet only.
- **Framing Effects in Independent-Agent Large Language Models** (authors not verified, 2026, arXiv 2603.19282) — Logically equivalent prompts shifted choices in seven of eight model families (effect sizes about 0.18 to 0.90).
  - Relevance: Broad framing sensitivity across families. Unreplicated preprint.
  - Read: search snippet only.

### Sub-theme 2: Behavioral biases in shopping choices (position, anchoring, decoys, endorsements)
- **What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** (Allouah, Besbes, Figueroa, Kanoria, Kumar, 2025, arXiv preprint; a WWW 2026 version is listed in OpenAlex) — The ACES audit framework tests agent purchases across 8 product categories with 64 listings. Position effects were large and varied by model. Telling the agent to ignore position did not remove them.
  - Relevance: The most direct empirical study of shopping-agent choice. Covers position, endorsement tags, seller description changes, and model dependence.
  - OpenAlex IDs: W4417105883 (arXiv), W7152735904 (WWW 2026 listing), W4413020061 (SSRN 2025 earlier title)
  - Cited by: 0 (arXiv), 8 (WWW listing), 8 (SSRN listing)
  - Read: full text (HTML, first 100k characters) for numbers. Section 7.3 and the headless replication were not read.
  - Key numbers from the full text: top-row coefficient +1.22 (Claude Sonnet 4), +1.05 (GPT-4.1), -0.70 (GPT-5.1), +2.15 (Gemini 3.0 Pro Preview). An "Overall Pick" tag raised a 10% share to 19.9% to 42.6%, depending on model.
  - Seller effect: rewriting one product description raised share by 3.7 to 14.9 percentage points, depending on the buyer and seller model pair.
- **Small Bias, Large Failure: Anchoring Collapses a Market of Language-Model Agents** (Hantel, 2026, SSRN working paper, posted July 2026) — One anchoring sentence given only to sellers cut market efficiency from 96% to 15% in a five-seller market. A one-line debiasing instruction reversed the collapse.
  - Relevance: Shows anchoring compounds in multi-agent markets, even when the one-to-one bias is mild.
  - OpenAlex ID: W7171676768
  - Cited by: 0
  - Read: abstract from search snippet. Full text blocked (HTTP 403).
- **When Biased Agents Trade: Anchoring, Exploitation, and Market Failure in Agent-to-Agent Interactions** (Hantel, 2026, SSRN working paper) — Reports 8,415 interactions and anchoring as the bias that most damaged efficiency. Naming the bias in a warning recovered about 40% of the loss. Asking for step-by-step reasoning made anchoring worse.
  - Relevance: Same author as the market-collapse paper. Gives the mitigation evidence.
  - OpenAlex ID: W7171715124
  - Cited by: 0
  - Read: search snippet only. Full text blocked (HTTP 403). Figures are unverified.
- **How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations** (Takenami, Huang, Murawaki, Chu, 2025, EMNLP 2025 Findings; arXiv 2508.21137) — LLM sellers are affected by anchoring similarly to humans. Reasoning models are less susceptible.
  - Relevance: Peer-reviewed anchoring evidence in negotiation. Abstract only, so no effect sizes.
  - Read: arXiv abstract.
- **A Manager and an AI Walk into a Bar: Does ChatGPT Make Biased Decisions Like We Do?** (Chen, Kirshner, Ovchinnikov, 2025, venue not verified) — Tests ChatGPT for human-like decision biases in managerial settings.
  - Relevance: Cross-check for bias claims. Not read in full. Cross-stream reference.
  - OpenAlex ID: W4407010275
  - Cited by: 143
  - Read: title and OpenAlex metadata only.
- **Vertical tacit collusion in AI-mediated markets** (authors not verified, 2026, arXiv 2601.03061) — Cited by a second paper as reporting asymmetric decoy effects in instruction-tuned LLMs (Itzhak et al.).
  - Relevance: Points to decoy evidence that the search did not reach directly. Lead only.
  - Read: search snippet only.
- **A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents** (authors not verified, 2026, arXiv 2609.19843) — Reports that the decoy effect systematically shifts choices of GUI agents.
  - Relevance: Conflicts with the agent-decoy null result. Lead only.
  - Read: search snippet only.

### Sub-theme 3: Benchmarks for shopping agents (WebShop and successors)
- **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents** (Yao, Chen, Yang, Narasimhan, 2022, NeurIPS 2022; arXiv 2207.01206) — Simulated shop with 1.18 million products and 12,087 instructions. Best agent reached 29% task success. Human experts reached 59%.
  - Relevance: The reference benchmark. Its numbers set the baseline for later shopping benchmarks.
  - Read: search snippets quoting the paper.
- **ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents** (authors not verified, 2025, arXiv 2508.04266; AAAI 2026) — 3,310 user instructions across four intent types, over 2.5 million products. The best model (GPT-4.1) succeeded on under 50% of tasks.
  - Relevance: Successor to WebShop with harder, multi-constraint intents.
  - OpenAlex IDs: W7138412334 (AAAI 2026)
  - Cited by: 1
  - Read: search snippets only. Not fetched.
- **ShopperBench: A Benchmark for Personalized Shopping with Persona-Guided Simulation** (authors not verified, 2026, EACL 2026 industry track) — Builds on WebShop and tau2-Bench with user personas. Adds persona fidelity and path consistency metrics.
  - Relevance: Measures whether agents follow user preferences across a session. Scores not seen.
  - Read: search snippet only.
- **ShoppingComp: Are LLMs Really Ready for Your Shopping Cart?** (authors not verified, 2025, arXiv 2511.22978) — Open-web benchmark. In version 2, GPT-5.2 scored 17.76% answer F1 vs. 30.02% for human experts. Safety rubric pass rate was 35.42% vs. 77.08%.
  - Relevance: Shows large gaps on real products with safety and multi-constraint checks. Version numbers differ between v1 and v2.
  - Read: search snippets of v1 and v2 abstracts, not full text.
- **AgenticShop: Benchmarking Agentic Product Curation for Personalized Web Shopping** (authors not verified, 2026, arXiv 2602.12315) — Scores personalized product curation with checklists from user profiles and an LLM judge.
  - Relevance: Directly about preference alignment. Judge validated against human ratings according to the authors.
  - Read: search snippet only.
- **ShopSimulator** (authors not verified, 2026, arXiv 2601.18225) — Chinese shopping environment for RL-trained agents. Best models reached under 40% full success. Agents misuse personalization cues.
  - Relevance: Evidence that agents fail to use user preference signals.
  - Read: search snippet only.
- **Shopping Companion** (authors not verified, 2026, ACL Findings EMNLP 2026) — Long-horizon, preference-grounded tasks. Failures come from preference hallucination and weak attribute checks. GPT-5 succeeds under 70%.
  - Relevance: Names the two failure modes most relevant to preference alignment.
  - Read: search snippet only.

### Sub-theme 4: Agent-to-agent negotiation and simulated markets
- **The Automated but Risky Game: Modeling and Benchmarking Agent-to-Agent Negotiations and Transactions in Consumer Markets** (authors not verified, 2025, arXiv 2506.00073; NLLP 2025 workshop listed in OpenAlex) — LLM buyers and sellers negotiate over 50 real products. Weaker models closed below-cost or over-budget deals. Qwen2.5-7B had 11.8% out-of-budget deals.
  - Relevance: Direct evidence of money losses when both sides use agents. Seller model choice mattered more than buyer model choice.
  - OpenAlex IDs: W4415249953 (arXiv), W4416033579 (NLLP)
  - Cited by: 0 (arXiv), 2 (NLLP)
  - Read: arXiv v4 HTML for results table.
- **AgenticPay** (authors not verified, 2026, ICLR 2026 listing; arXiv 2602.06008) — Benchmark for multi-agent buyer-seller negotiation in natural language, from one-to-one to many-to-many markets.
  - Relevance: Covers market scale, which the Risky Game paper does not.
  - Read: ICLR listing and search snippets.
- **Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets** (Microsoft Research, 2025, arXiv 2510.25779; authors not verified) — Simulated consumer and business agents covering search, negotiation and transaction. Every model tested showed first-proposal bias. Performance dropped as market size grew.
  - Relevance: Shows the first-offer advantage at market scale. Relevant to position bias in markets.
  - Read: search snippets and project summary.
- **Strategic Tradeoffs Between Humans and AI in Multi-Agent Bargaining** (Qian, Zhu, Horton, 2026, OpenAlex W7133362381) — Humans (N=216), LLMs and Bayesian agents bargained. LLMs made concessionary offers that other LLMs accepted. Humans made fairness-based offers that were rejected more often.
  - Relevance: Shows that matching aggregate surplus can hide different strategies.
  - Cited by: 2
  - Read: OpenAlex abstract.
- **Agentic markets and learning** (authors not verified, 2026, arXiv 2603.25893) — Model of sequential search by consumers with agents. Cheaper search raises consumer surplus. More informative search can lower it.
  - Relevance: Theory of market effects. No LLM experiments.
  - Read: search snippet only.

### Sub-theme 5: Preference alignment and economic theory of agentic commerce
- **From Product Search to Preference Articulation: The Economics of Agentic Commerce** (Dong, Luo, Xu, 2026, arXiv 2608.08395, econ.TH) — Formal model. Manual search collapses beyond a complexity threshold. Agentic search avoids collapse. Consumers may adopt it late.
  - Relevance: Theory of why agents help with complex preferences. Gives testable predictions.
  - Read: arXiv abstract. Theoretical, no data.
- **The Evolution of Digital Search: From Blue Links to Delegated Decision-Making** (Rothschild, Immorlica, Lucier, Mobius, Slivkins, 2026, arXiv 2607.21459) — Perspective piece on welfare and competition when agents decide.
  - Relevance: Frames the question. Cross-stream with the search-engine stream.
  - Read: search snippet only.
- **AI shopping agents and the reallocation of consumer attention** (Zhao and Kang, 2026, OpenAlex W7224901915) — Models seller visibility and platform access in agentic commerce.
  - Relevance: Market-level effects. Cross-stream with the marketing stream.
  - Cited by: 0
  - Read: OpenAlex title only.

## Reference Chain Discoveries
- Found via: ACES audit (2508.02630) citers and references. Related-work list includes product-ranking and badge-effect studies. Those are cross-stream and were not traversed.
- Found via: Chen et al. (PNAS 2023) citers. Most are general LLM-as-subject papers. Only the Chen, Kirshner, Ovchinnikov paper and the Wen paper are specific to decision bias.
- Found via: Risky Game (2506.00073) citers. Two 2026 papers on agent trust and marketplaces. Not read.
- Found via: ShoppingBench (2508.04266) citers. No relevant papers beyond a tokenization-style conversational commerce paper.
- Found via: Search for decoy effects. Valkanova and Yordanov (2409.15299) and the Bi.team report (human participants using an LLM, not agent choices).

## What's Missing (Gaps)
- No study compares agent choices with a real user's own revealed preferences from past purchases. Most papers use synthetic or fixed utility functions.
- No study tests GARP or CCEI directly on shopping agents over repeated real-listing choices.
- Decoy-effect evidence on shopping agents conflicts. No preregistered test on the same products and models exists in the search results.
- Few studies measure real money outcomes for buyers. The Risky Game paper uses simulated budgets.
- Market-level studies mostly use simulated sellers. Real seller response to agent ranking rules is not measured.
- NBER and SSRN working papers on agent shopping were not found by the search tool. Their absence may be a search limit.

## Contradictions or Tensions
- **Decoy effect.** ACES (2508.02630) and the Hantel SSRN paper report agents ignore decoys in some settings. Valkanova and Yordanov (2409.15299) and a 2026 GUI-agent paper (2609.19843) report decoy effects. The settings differ: hiring, GUI, and shopping. Models and versions also differ.
- **Anchoring severity.** Hantel (SSRN, 2026) reports collapse from 96% to 15% efficiency under seller anchoring. Takenami et al. (2508.21137) report anchoring similar to humans and smaller in reasoning models. The market setting differs.
- **Chain-of-thought.** Hantel reports step-by-step reasoning makes anchoring worse. Takenami et al. report reasoning models resist anchoring better. These are different tasks and model families.
- **Rationality under specialization.** Chen et al. (2023) report largely rational GPT. Wen (2025) reports fewer GARP violations for generalist agents than specialist agents. Both concern decisions, but on different tasks.
- **Benchmark difficulty.** WebShop, ShoppingBench and ShoppingComp show low success rates. Magentic Marketplace shows strong performance under ideal search. Results depend on how hard the search task is.

## Confidence
Medium
- What would raise confidence: Full-text replication of the ACES position and decoy results across more models and an independent lab. Also a preregistered decoy test on shopping agents.
- What would lower confidence: Evidence that the position effect disappears under a realistic interface with images and full product pages. Evidence that model updates remove the anchoring collapse.

## Search Log
### Round 1: Broad search
- Queries: "LLM agents shopping choice rationality GARP revealed preference consumer"; "LLM shopping agent position bias anchoring decoy effect product choice"; "WebShop ShoppingBench benchmark shopping agents successors 2025"; "agent-to-agent negotiation LLM buyer seller agents marketplace simulation"; "agentic commerce AI agents preference alignment user true preferences SSRN NBER working paper"
- Papers found: about 45 unique results, of which about 20 relevant
- Key leads: 2508.02630 (ACES), 2506.00073 (Risky Game), Chen et al. PNAS 2023, ShoppingBench, Hantel SSRN

### Round 2: Citation traversal
- Papers traversed: ACES (2508.02630; 3 OpenAlex versions); Chen et al. PNAS 2023 (citers, top 10 by citations); Risky Game (both versions); ShoppingBench (citers)
- New papers from references: ACES references resolved to Bijmolt et al. (2005), Ursu (2018), and Chen, Kirshner, Ovchinnikov (2025). Only the last is relevant.
- New papers from citers: Wen (2025); Qian, Zhu, Horton (2026); Zhao and Kang (2026); Bichler (2026, "Agentic markets"); several 2026 agentic commerce reviews (not read)

### Round 3: Reference section mining
- Papers mined: ACES full text (HTML, first 100k characters, related-work list); Risky Game full text (results); Chen et al. (PNAS 2023) abstract
- Note: The Hantel SSRN full text was blocked (HTTP 403). Its figures come from snippets.
- New papers from references: Magentic Marketplace (2510.25779); Takenami et al. (2508.21137); WebShop (2207.01206); ShoppingComp numbers verified in v2

### Round 4: Gap-filling
- Gaps targeted: Shopping agents and preference alignment; decoy effects in LLMs; SSRN and NBER agent-market papers; benchmark successors to WebShop
- Queries: "Small Bias, Large Failure anchoring collapses a market of language-model agents"; "Magentic Marketplace simulated marketplace LLM agents first-proposal advantage"; "LLM decoy effect asymmetric dominance choice experiment language models arXiv 2025"; "WebShop Yao 2022 scalable real-world web interaction grounded language agents success rate human expert"; "ShoppingComp LLM shopping agents results accuracy open-world products evaluation"; "AI shopping agents consumer welfare delegated search economics model NBER SSRN 2026"; "LLM shopping agent user preference alignment personalized product choice evaluation study 2026"
- New findings: Hantel SSRN anchoring-collapse paper; Magentic Marketplace first-proposal bias; AgenticShop; ShopSimulator; Shopping Companion; theory papers (2608.08395, 2603.25893)

### Round 5: Adversarial check
- Gaps targeted: critiques and replication failures of LLM rationality and framing claims
- Queries: "LLM revealed preference rationality fragile prompt framing critique replication economic rationality GPT"
- New findings: Fed FEDS framing work; "Alignment Revisited" (2506.00751); Framing Effects in Independent-Agent LLMs (2603.19282). These show framing fragility but none directly replicates Chen et al. (2023).
- Contradictions surfaced: decoy effect disagreement (see above)

### Round 6+: Follow leads
- Searches for SSRN and NBER versions of agent-market papers returned no hits in the search tool. Preference-alignment leads were followed to AgenticShop, ShopSimulator, and Shopping Companion.
- New papers in this round: about 8, mostly 2026 preprints. Coverage is not complete.

### Convergence note
- Total unique relevant papers found: 28 (counted in the sub-themes above, including cross-stream entries)
- New papers in last round: about 8
- Stopped because: Practical budget reached. The last round still found new relevant papers, so the stopping rule was not met. Coverage of 2026 preprints is likely incomplete. NBER and SSRN coverage is weak in this tool.
