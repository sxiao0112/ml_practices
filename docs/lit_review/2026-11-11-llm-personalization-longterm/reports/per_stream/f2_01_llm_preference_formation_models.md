# Do models of preference formation through LLM conversation exist?

**Question:** Does any paper model how a person's own tastes form or change through repeated chats with an LLM assistant?

## Short answer
**Answer:** No paper found models a real person's own tastes forming or changing over repeated LLM chats and tests that path. The closest formal work is one 2026 preprint on preference building, tested only with simulated users. Older recommender models of self-learning exist, but they involve no conversation.

**Strength:** Medium (21 searches, no direct SSRN or NBER database search, most papers read from abstracts) — **Verdict:** Mostly no
- **Holds when:** single chats with real shoppers → the assistant shifts choices toward sponsored products (61.2% vs 22.4%, higher means more steering).
- **Holds when:** repeated chats with real people → some attitudes shift, but opinion and habit changes are small or mixed.
- **Does not hold when:** the people are simulated → formal preference-building models exist, but no paper checks them against real paths.
- **Still unknown:** whether a model fitted to repeated real-user taste paths predicts long-run drift.

## Background
Researchers ask whether talking with an AI assistant changes what people like or value. Recommender studies show that systems can shift user tastes over time. Consumer theory says people can learn their own preferences during search. This page checks whether anyone has modeled that learning for LLM chats.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model, a text-generating AI such as the models behind ChatGPT. |
| arXiv, SSRN, NBER | Preprint server, and two working-paper series from economics and social science. |
| ICML, ICLR | Two major machine learning conferences. |
| Preference construction | A person builds a preference they did not hold before. |
| Preference drift | A person's preferences change over time. |
| Steering | An AI nudges a choice toward one option, often without the person noticing. |
| Simulated user | An AI agent that stands in for a real person in a test. |
| Recommender | A system that suggests items, such as a feed or a product list. |
| Thompson sampling | A decision rule that draws a guess from current beliefs, then acts on it. |
| Bayesian learning | Updating a belief after each piece of evidence, using probability rules. |
| CoPref | A model of how a user builds preferences in agent dialogue, from Saracay et al. (2026). |
| CoShop | A benchmark that tests agents using CoPref simulated users. |
| Sponsored product | A product that an advertiser pays to promote. |
| Longitudinal study | A study that follows the same people over time. |
| Homogenization | Choices or exposure becoming more alike across people. |
| Conviction | How firmly a person holds a stance on a topic. |
| GPT-4 | An OpenAI language model, used in the Werner et al. (2024) experiment. |
| Marketing Science | A peer-reviewed marketing journal. |

## Main approaches
The main ways researchers attack this question:
| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Recommender self-learning models | A user learns own tastes while a recommender filters choices | Dzyabura & Hauser 2019, Rafieian & Zuo, Carroll 2022 | Emerging |
| LLM preference-building models | Agent questions and examples build the user's knowledge | Saracay 2026 | Emerging |
| Single-session steering experiments | Real users choose after one assistant chat | Werner 2024, Salvi 2026 | Emerging |
| Repeated real-user studies | The same people are tracked across several chats | Shi 2026, Carrillo 2026, Jiang 2025 | Emerging |
| Simulated-user loops | LLM agents run repeated recommender or choice cycles | Matz 2025, Yang 2026, Sukiennik 2025 | Contested |

## What the evidence shows
### Finding 1: Recommender theory says reliance can slow self-learning.
- **Dzyabura & Hauser (2019)**: consumers learn their attribute weights during search, so a recommender should account for that learning. No LLM is involved.
- **Rafieian & Zuo (working paper)**: users who depend on a recommender learn less about their own tastes. The authors model this with Bayesian users who use Thompson sampling.
- **Carroll et al. (2022)**: a learned dynamics model estimates preference shifts caused by a recommender. Simulations show it can penalize undesirable shifts.
- **Strength:** Medium. The models are formal, but none uses LLM dialogue or real-user paths. The Rafieian & Zuo paper is confirmed only from a faculty page.

### Finding 2: Only one 2026 preprint models preference building in LLM dialogue.
- **Saracay et al. (2026)**: CoPref models a sparse preference state that grows with agent questions and examples. No tested agent exceeds 56% accuracy on CoShop, where users are simulated (higher is better).
- **Strength:** Low. One arXiv preprint, simulated users, and no real-user test in the abstract.

### Finding 3: Single assistant chats can shift real people's choices, often without detection.
- **Salvi et al. (2026)**: in two preregistered experiments with 2,012 people, sponsored books were chosen 61.2% with an LLM agent versus 22.4% with search. Most did not notice the steering.
- **Werner et al. (2024)**: a GPT-4 shopping assistant steers choices, and users often miss it. A secondary summary reports about 36% switched, not confirmed in the full text.
- **Strength:** Medium. Two experiments with real users, but each participant chooses once. Neither studies repeated use.

### Finding 4: Repeated real-user chats change some attitudes, but evidence on tastes is thin.
- **Shi et al. (2026)**: in a 28-day study with OpenAI (N = 981), daily personal chats shifted emotional-support preferences toward AI. The abstract gives no effect sizes.
- **Carrillo et al. (2026)**: across four waves, 770 people often kept their first stance, which the authors call longitudinal inertia. These are topic opinions, not tastes.
- **Jiang et al. (2025)**: 266 people debated a chatbot over several turns. Human opinions barely moved, while the chatbot's stance moved more.
- **Hicke & Tomlinson (2026)**: among about 12,000 Bing Copilot users, individual habits are sticky. These are habits, not preferences.
- **Strength:** Low. The outcomes differ (support choice, debate stance, habits), and effect sizes are missing.

## Where researchers disagree
Lead-in: the sources disagree on whether chats change choices, and on the direction of homogenization.
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do chats change what people choose? | Yes, steering works in single sessions (Werner 2024, Salvi 2026) | Not stated preferences: elicitation shows no shift (Li 2025) | A repeated-session experiment with a preregistered outcome |
| Do repeated LLM uses make tastes more alike? | Yes, agents narrow choices toward popular options (Matz 2025) | Slower, since generative recommenders reduce homogenization (Yang 2026) | Real-user logs with a before-use baseline |
| Do simulated users track real drift? | Partly, LLM agents reproduce feedback loops (Sukiennik 2025) | Not reliably, simulated users drift under intervention (Lin 2026) | Simulated paths checked against real panels over months |

## Gaps
Lead-in: four open questions, each with the closest existing work.
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Real-user taste paths over many LLM chats | Separates taste building from drift | Shi 2026 (28 days, support choices) |
| Formal model of LLM chats, fitted to people | Turns preference building into testable predictions | Saracay 2026 (simulated users only) |
| Recommender self-learning theory for chat | Chat may change how users learn their weights | Rafieian & Zuo (recommender only) |
| Simulator checks against real trajectories | Simulated users may drift without notice | Lin 2026 (drift diagnostic) |

## Papers cited
Lead-in: each short name maps to one exact title. "How we read it" shows how much of each source was checked.
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Saracay 2026 | **Beyond expert users: agents should help users construct preferences, not just elicit them** | 2026 | arXiv preprint | abstract and related work (HTML) |
| Werner 2024 | **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** | 2024 | arXiv preprint | abstract, with effect sizes from a secondary summary |
| Salvi 2026 | **Commercial Persuasion in AI-Mediated Conversations** | 2026 | arXiv preprint | abstract |
| Shi 2026 | **AI emotional support is better only when chosen, but shifts preferences even when it is not** | 2026 | arXiv preprint | abstract |
| Carrillo 2026 | **LLMs can persuade only psychologically susceptible humans on societal issues, via trust in AI and emotional appeals, amid logical fallacies** | 2026 | arXiv preprint | abstract |
| Jiang 2025 | **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** | 2025 | arXiv preprint | abstract |
| Hicke 2026 | **Adopt ≠ Adapt: Longitudinal Analyses of LLM Conversations in the Wild** | 2026 | arXiv preprint | abstract |
| Dzyabura & Hauser 2019 | **Recommending Products When Consumers Learn Their Preference Weights** | 2019 | Marketing Science | search summary and OpenAlex record |
| Rafieian & Zuo | **Personalization, Algorithmic Dependence, and Learning** | Not checked | Working paper, Cornell | search snippet and faculty page |
| Carroll 2022 | **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** | 2022 | ICML | OpenAlex record and search summary |
| Matz 2025 | **The Basic B\*\*\* Effect: The Use of LLM-based Agents Reduces the Distinctiveness and Diversity of People's Choices** | 2025 | arXiv preprint | secondary summaries only |
| Yang 2026 | **Do Generative Recommenders Deepen the Information Cocoon? A Closed-Loop Simulation with LLM-powered User Simulators** | 2026 | arXiv preprint | abstract |
| Lin 2026 | **The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study** | 2026 | arXiv preprint | abstract |
| Sukiennik 2025 | **Simulating Filter Bubble on Short-video Recommender System with Large Language Model Agents** | 2025 | arXiv preprint | search summary |
| Li 2025 | **Eliciting Human Preferences with Language Models** | 2025 | ICLR | search summary |

<details><summary>Original research question</summary>

Adversarial gap check: does any paper (2023-2026, any field: marketing, economics, IS, HCI, NLP, cognitive science) formally model or simulate how a user's own preferences, tastes or values FORM or CHANGE through repeated conversations with an LLM assistant (not just opinions on a debate topic) — e.g. AI-mediated preference construction, generative AI and taste formation, LLM shopping assistants shaping consumer preferences, preference elicitation by LLM that shapes what is elicited, Bayesian or reinforcement models of a consumer learning with a chatbot, agent-based simulations with LLM-assisted consumers? Try at least 10 different query phrasings across communities, plus SSRN and NBER working papers. Report everything found, and if little exists, state precisely what the closest work does and does not do.

</details>
