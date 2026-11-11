# Lit Review State — 2026-11-11

## Config
- Max rounds: 10
- Agent model: haiku
- Output: docs/lit_review/2026-11-11-llm-personalization-longterm

## Streams
| ID | Question (short) | Status | Rounds | Papers Found | Last Round New | Decision |
|----|-----------------|--------|--------|-------------|---------------|----------|
| 01 | Recommender feedback-loop theory | closed | 1 | 27 | 27 | RESOLVE vs field evidence → f1_01 |
| 02 | Economics of dynamic targeting | closed | 1 | 28 | 28 | CLOSE |
| 03 | Consumers learning own preferences | closed | 1 | 42 | 42 | DEEPEN → f1_02 |
| 04 | Bandits/RL with learning or changing users | closed | 1 | 21 | 21 | CLOSE |
| 05 | LLM-specific feedback-loop theory | closed | 1 | 25 | 25 | CLOSE |
| 06 | Simulations of preference dynamics | closed | 1 | 19 | 19 | EXPAND calibration → f1_03 |
| 07 | Evals of multi-turn/long-term LLM personalization | closed | 1 | 35 | 35 | CLOSE (multi-turn targeting → f1_04) |
| 08 | Alignment with changing/influenceable preferences | closed | 1 | 20 | 20 | CLOSE |

## Follow-ups
| ID | Parent | Question | Status | Round Launched | Papers Found |
|----|--------|----------|--------|---------------|-------------|
| f2_01 | f1_02/06 | Do models of preference formation through LLM chat exist? | closed | 2 | ~15 |
| f1_01 | 01 | Field evidence on recommender-induced taste change | closed | 1 | ~25 |
| f1_02 | 03 | Formal models of users learning own preferences with AI advisor | closed | 1 | ~25 |
| f1_03 | 06 | Estimating/validating preference dynamics from real data | closed | 1 | ~25 |
| f1_04 | 07/02 | Multi-turn LLM targeting and personalized persuasion | closed | 1 | ~25 |

## Expansion Queue
| Priority | Question | Source | Status |
|----------|----------|--------|--------|

## Convergence Tracker
| Round | Agents Launched | New Papers (total across agents) | Streams Closed | Note |
|-------|----------------|----------------------------------|----------------|------|
| 0 | 8 | ~217 (raw bullets, overlaps) | 5 | Initial launch |
| 1 | 4 | ~100 (raw) | 4 | Follow-ups: field evidence, user-learning models, calibration, LLM targeting |
| 2 | 1 | ~15 (raw) | 1 | Adversarial gap check f2_01: verdict Mostly no — gap confirmed |

## Budget
- Agents launched: 14 (13 search + 1 synthesis)

## Status
Converged after round 2. Synthesis complete.
