# Orchestrator Log

## Round 0 — 2026-11-03
- Launched 7 haiku agents (streams 01–07). Prompts filled from templates/agent_prompt.md; see workbench/prompts/.
- Context told agents to skip topics covered by prior reviews 2026-10-29-llm-crs-review and 2026-10-15-cost-aware-search.
- Policy/antitrust folded into stream 01 rather than a separate stream.
- Stream 05 returned: 28 papers; style check clean. Position bias replicates; decoy results conflict; benchmarks show low success.
- Stream 04 returned: 17 papers (13 abstract-only, 4 snippet-only). Incumbent-brand concentration; persona sensitivity; strategic text raises rec rate. Thin on consumer reaction to sponsored answers; no SSRN/NBER found — candidate DEEPEN.
- Stream 07 returned: 23 papers (4 summary-only). Citations raise trust even when wrong; hedging/highlighting help; shallower learning. Few purchase-quality outcomes; effect sizes mostly missing.
- Stream 02 returned: 11 studies. LLM search cuts time/queries; accuracy drops when LLM errs; field evidence on purchases/substitution conflicts. Thin — DEEPEN candidate on field/log data and substitution.
- Stream 03 returned: 14 papers (5 summary-only). Click drops 35-48%; LLM ad auctions theory/sim only; GEO up to +40% in benchmarks, unstable live.
- Stream 06 returned: 32 papers. Query rewriting +0.40% GMV Taobao; LLM-judge distillation +0.8% ATC Walmart; generative retrieval ~1-2% GMV; clarifying-question fatigue ~11 Qs. Hit cap while still finding — DEEPEN on generative retrieval / query rewriting.

## Round 0 review
- 01 (22, Low): DEEPEN — no empirical econ; no SSRN/NBER sweep → f1_2
- 02 (11, Low-Med): DEEPEN — field/log evidence and substitution conflict → f1_1
- 03 (14, Med): CLOSE — field traffic part folded into f1_1
- 04 (17, Med): DEEPEN — no SSRN/NBER → f1_2; interventions → f1_4
- 05 (28, Med): EXPAND — remedies for agent bias → f1_4
- 06 (32, Med): DEEPEN — hit round cap while finding new papers → f1_3
- 07 (23, Med): CLOSE — interventions folded into f1_4
- No contradictions between streams found at TL;DR level. f1_4 addresses the user's second question ("how to better design/use LLMs").
- f1_1 returned: 6 new. Comscore clickstream: search queries down 9-22% after ChatGPT adoption (2 non-independent studies); purchase effects conflict; Kaiser & Schulze 2026 Mkt Sci. CLOSE.
- f1_2 returned: 19 new (Egan 2026, Fradkin 2025, Fish 2024 LLM collusion, Qiu 2025 Mkt Sci, Werner 2024 steering). High new-paper rate → econ/marketing not converged; consider round-2 traversal.
- f1_4 returned: 22 new. Measured fixes: prompt warnings, debiased fine-tuning, persuasive-intent disclosure, defenses vs seller text. AI-identity notices and prompt-only position fixes did not work. No field evidence.
- f1_3 returned: 18 new. Generative retrieval 1-3% GMV lifts (Kuaishou, Alibaba, Meituan, Tencent); Alipay +1.3-2.1%; Rufus no numbers; no Shopify/eBay/Etsy papers.

## Round 1 review
- Total new: 65 (6+19+22+18). Not converged.
- CLOSE 02, 04, 05, 06, f1_1, f1_3, f1_4. Further generative-retrieval papers are marginal to the consumer-search question; incompleteness documented.
- Ads/sponsored content: f1_4 already covers Ads that Talk Back, Monetizing Intelligence, LLMAdBench, disclosure — no separate agent.
- Decoy-effect conflict in 05: low priority, left for synthesis to report as open.
- Round 2: f2_1 DEEPEN econ/marketing (19 new in f1_2 = highest rate); f2_2 EXPAND — LLMs as models of consumers (silicon samples), not covered by any stream, and part of "how to use LLMs for consumer search".
- f2_1 returned: 13 new (2 adjacent). Mostly algorithmic pricing/collusion theory; one field expt on AI shopping assistant (Wang et al. ISR 2025). No clean null on concentration; contrary results on collusion/steering/welfare. Many citers off-topic → diminishing returns. CLOSE.
- f2_2 returned: 40 new. Silicon samples fit aggregate purchase intent (~90% of human test-retest in one 57-survey study); weak individual/subgroup fit; search simulators lag on exploratory tasks.

## Round 2 review → STOP
- Core streams converged: econ new-paper rate fell 22→19→13 with off-topic citers; all core streams CLOSED.
- f2_2's 40 new papers reflect a large adjacent sub-field (LLMs as models of consumers), not unexplored core territory. Scope decision: cover it at one-round depth, flag as candidate for its own review. This overrides the "new direction in last round" late-stop rule, deliberately.
- Open, unresolved: decoy-effect conflict (05); purchase-outcome direction (f1_1). Reported as open in synthesis.
- Synthesis done (style clean). README written. Obsidian export: 236 unique papers.
