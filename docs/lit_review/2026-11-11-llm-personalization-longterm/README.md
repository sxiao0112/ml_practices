# Deep Literature Review: Long-Term Effects of LLM Personalization

**Status:** Complete (2026-11-11). Three rounds of search, 13 search agents, and 1 synthesis agent.

**Questions:**
1. Which theoretical models describe dynamic learning, feedback loops, and repeated personalization or targeting? This includes models from before LLMs.
2. How can we model how users learn or form their own preferences under LLM influence, and how can we simulate it?
3. Which existing studies evaluate the multi-turn or long-term effects of LLM personalization?

The review covers economics, marketing, recommender systems, online learning, AI alignment, NLP and HCI (human-computer interaction).

## Start here
- [Synthesis](reports/synthesis.md): six main findings, a building-blocks table for a preference-learning model, and a toolkit table of simulators, benchmarks and field designs.
- [Open questions](reports/open_questions.md): what nobody has tested yet, most important first.
- [Per-stream reports](reports/per_stream/): one page for each search question.

## Main findings
- **Feedback loops** narrow tastes in models, but real platforms show small or mixed effects. **Medium** for models, **Low** for field tests ([details](reports/synthesis.md#finding-1-feedback-loops-narrow-tastes-in-models-but-real-platforms-show-small-or-mixed-effects))
- **Chatbots agree more** as chats grow longer, and they often miss changed preferences. **Medium** ([details](reports/synthesis.md#finding-2-chatbots-agree-more-as-chats-grow-longer-and-they-often-miss-changed-preferences))
- **Chat steering** works in one session, and users often miss it. **Medium**, because no test uses repeated sessions ([details](reports/synthesis.md#finding-3-chat-steering-works-in-one-session-and-often-goes-unnoticed-while-tailoring-adds-little))
- **No study tracks** chatbot-driven taste change over months. **Low** ([details](reports/synthesis.md#finding-4-advice-moves-stated-preferences-but-no-study-tracks-chatbot-driven-taste-paths-over-months))
- **Approval training** can reward influence on the user. **Medium**, theory only ([details](reports/synthesis.md#finding-5-rewarding-user-approval-can-reward-influence-and-the-formal-fixes-trade-off))
- **Simulated users** are not checked against real taste paths over time. **Low** ([details](reports/synthesis.md#finding-6-simulated-users-drift-less-than-real-users-so-simulators-need-trajectory-checks))

## Main gap
No paper models a user who learns her own preferences through repeated LLM chats and then tests that path on real users. A check with 21 searches confirmed this. The closest work is Rafieian and Zuo (an unverified working paper, recommender only), Dzyabura and Hauser 2019 (recommender only), and CoPref/CoShop 2026 (a preprint with simulated users only).

## Limits
- Most papers are 2024–2026 preprints. Agents read most of them at abstract level only.
- Rafieian and Zuo is not indexed in OpenAlex. Check it before you cite it.
- Search agents ran on the Haiku model. Run a citation check before you cite any number.

## How to verify
- Raw agent output with search logs: `workbench/agents/` and `workbench/follow_ups/`.
- Each decision and its reason: `workbench/orchestrator_log.md`. Live status: `state.md`.
- To fact-check the synthesis, run `/verify-citations` on `reports/synthesis.md`.
