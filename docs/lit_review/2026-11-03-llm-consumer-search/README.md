# Deep Literature Review: LLMs and Consumer Search

**Status:** Complete (2026-11-03). Three rounds of search, 13 search agents, and 1 synthesis agent.

**Questions:**
1. How do large language models (LLMs) change the way consumers search for products and information?
2. What research shows how to design or use LLMs for consumer search?

The review covers economics, marketing and computer science, including information retrieval and HCI (human-computer interaction).

## Start here
- [Synthesis](reports/synthesis.md): main findings, the design-lever table, and how the fields compare.
- [Open questions](reports/open_questions.md): what nobody has tested yet, most important first.
- [Per-stream reports](reports/per_stream/): one page for each search question.

## Main findings
## Summary

The review reached six main results. Each links to its section below.

- **Faster search**, but people follow wrong answers: **Medium**, three studies agree on direction ([details](reports/synthesis.md#finding-1-consumers-search-faster-with-llms-but-follow-wrong-answers))
- **Less regular web search** in desktop panels, with purchase effects unknown: **Low**, because the two panels share a data vendor ([details](reports/synthesis.md#finding-2-chatbots-cut-regular-web-search-but-purchase-effects-point-both-ways))
- **Fewer publisher clicks** after AI answers appear: **Medium**, because two field experiments agree on direction ([details](reports/synthesis.md#finding-3-ai-answers-send-fewer-clicks-to-publisher-sites))
- **Well-known brands** win many shopping picks, and list order and wording shift picks: **Medium**, because several audits agree, though most are preprints ([details](reports/synthesis.md#finding-4-shopping-picks-favor-well-known-brands-and-shift-with-list-order-and-wording))
- **Seller-written text** can raise a product's rank in AI answers: **Medium** for the attack, **Low** for defenses and labels ([details](reports/synthesis.md#finding-5-seller-written-text-can-steer-ai-picks-while-defenses-are-tested-only-in-labs))
- **Small sales gains**, mostly 1% to 3%, from LLM search parts: **Medium** for query rewriting, **Low** for generative retrieval ([details](reports/synthesis.md#finding-6-company-tests-show-small-sales-gains-from-llm-search-parts))


## Limits
- Most papers are 2024–2026 preprints. Agents read many of them at abstract level only.
- The searches on generative retrieval, simulated consumers and sponsored-answer labels did not converge. Treat those sections as partial.
- The "LLMs as simulated consumers" area is large. A separate review of it would be useful.
- Search agents ran on the Haiku model. A [citation check](#how-to-verify) is advised before you cite any number.

## How to verify
- Raw agent output with search logs: `workbench/agents/` and `workbench/follow_ups/`.
- Each decision and its reason: `workbench/orchestrator_log.md`. Live status: `state.md`.
- To fact-check the synthesis, run `/verify-citations` on `reports/synthesis.md`.
