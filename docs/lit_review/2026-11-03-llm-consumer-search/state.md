# Lit Review State — 2026-11-03

## Config
- Topic: Impact of LLMs on consumer search; designing/using LLMs for consumer search (econ, marketing, CS)
- Max rounds: 10
- Agent model: haiku
- Output: docs/lit_review/2026-11-03-llm-consumer-search

## Streams
| ID | Question (short) | Status | Rounds | Papers Found | Last Round New | Decision |
|----|-----------------|--------|--------|-------------|---------------|----------|
| 01 | Econ theory: search costs, competition, welfare | closed | 3 | 52 | 11 | CLOSE (diminishing returns) |
| 02 | Empirical consumer use of LLM search | closed | 2 | 17 | 6 | CLOSE (after f1_1) |
| 03 | Search engines, publishers, ads, GEO | closed | 1 | 14 | 14 | CLOSE (field part via f1_1) |
| 04 | Brand bias & manipulation in LLM recs | closed | 2 | 17 | - | CLOSE (ads/disclosure in f1_4) |
| 05 | LLM agents as shoppers | closed | 1 | 28 | 28 | CLOSE (remedies in f1_4) |
| 06 | System design for LLM product search | closed | 2 | 50 | 18 | CLOSE (after f1_3) |
| 07 | HCI: trust, reliance, interface | closed | 1 | 23 | 23 | CLOSE (interventions via f1_4) |

## Follow-ups
| ID | Parent | Question | Status | Round Launched | Papers Found |
|----|--------|----------|--------|---------------|-------------|
| f1_1 | 02,03 | Field evidence: substitution & purchases | closed | 1 | 6 new |
| f1_2 | 01,04 | SSRN/NBER/journal sweep econ+marketing | done | 1 | 19 new |
| f2_1 | 01,f1_2 | Econ/marketing citation traversal + adversarial | closed | 2 | 13 new (11 on-topic) |
| f2_2 | new | LLMs to model/simulate consumer search | closed | 2 | 40 new |
| f1_3 | 06 | Deployed assistants & generative retrieval | closed | 1 | 18 new |
| f1_4 | 04,05,07 | Consumer-aligned design interventions | closed | 1 | 22 new |

## Expansion Queue
| Priority | Question | Source | Status |
|----------|----------|--------|--------|

## Convergence Tracker
| Round | Agents Launched | New Papers (total across agents) | Streams Closed | Note |
|-------|----------------|----------------------------------|----------------|------|
| 0 | 7 | 147 (pre-dedup) | 2 | Initial launch |
| 1 | 4 | 65 | 5 | Follow-ups; econ still high new-rate |
| 2 | 2 | 53 (13+40) | all | Econ converging; simulated consumers is a new sub-field, scoped at 1 round |

## Budget
- Agents launched: 13
