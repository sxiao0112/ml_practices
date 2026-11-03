# Designing LLM shopping help that serves the consumer

**Question:** Which methods make AI shopping and search assistants act for the shopper, and which of them were tested?

## Short answer
**Answer:** Several methods cut bias or manipulation by a measured amount in lab tests. These are prompt warnings, fine-tuning on example answers, disclosure of persuasive intent, and defenses against seller-written text. Fiduciary and market-design ideas have no measured consumer effects yet.

**Strength:** Low to Medium (most results come from single preprints, and several defense numbers are self-reported)
- **Holds when:** the bias is injected into lab product or paper picks → warnings and training recover about 3 to 15 points of accuracy.
- **Does not hold when:** the only disclosure says the bot is an AI → persuasion stays about the same (13.1 vs 12.6 points).
- **Still unknown:** whether labels or defenses change real purchases, prices or market shares.

## Background
Shoppers now ask chatbots and AI answer engines what to buy. These systems can favor certain brands, read seller text written to game rankings, or push sponsored items. Researchers ask which designs keep the answer on the shopper's side.

Key terms used on this page:

| Term | Plain meaning |
|------|---------------|
| LLM | Large language model, a text model such as ChatGPT. |
| Shopping agent | An AI that searches, compares and buys products for a user. |
| GEO (generative engine optimization) | Writing web text so that AI answers mention or rank it higher. |
| Position bias | Favoring an item because of where it appears in a list. |
| Brand or popularity bias | Favoring well-known brands or widely chosen items. |
| Anchoring | Judgments pulled toward a first number or offer the model saw. |
| Sponsored content | Paid placement, shown as an ad or inside an answer. |
| ASR (attack success rate) | Share of manipulated answers that work. Lower is safer. |
| False positive rate | Share of honest items wrongly flagged. Lower is better. |
| Robustness rate | Share of trials where the model still picks the right item. Higher is better. |
| Preference elicitation | An agent asks questions to learn what the user wants. |
| Delegation | The user lets an agent make the choice for them. |
| Principal-agent problem | An agent may serve another party's goals instead of the user's goals. |
| Fiduciary duty | A legal duty to act in another person's best interest. |
| Mechanism design | Choosing market rules so that self-interested parties behave well. |
| VCR (verifiable-content rewards) | Pays web authors for checkable facts in their text. |
| Permutation averaging | Shuffle the list order several times, then merge the rankings. |
| Fine-tuning | Training a model further on example answers. |
| Preregistered | A study plan filed before data collection, to limit selective reporting. |
| Attitude shift | Change in a 100-point rating after a chat. Higher means more persuaded. |
| Benchmark | A shared test set with a score for comparing systems. |
| Simulation | A model-based test with simulated users or sellers. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Prompt and training debiasing | Warn the model or train it on examples that resist bias. | BiasRecBench (2026), Prompt-based reranking (2025) | Contested |
| Order shuffling | Shuffle item order and merge several rankings. | Found in the Middle (Tang 2024) | Established for ranking tasks |
| Disclosure labels | Tell users when content is sponsored or when the bot is persuading. | Ads that Talk Back (Tang 2025), Persuasive intent (Rauchfleisch 2026) | Contested |
| Seller-manipulation defenses | Detect or rewrite text written to game AI rankings. | SCI-Defense (Yu 2026), GEO Defender (Li 2026) | Emerging |
| Preference elicitation | The agent asks questions to learn what the user wants. | CoShop (Saracay 2026) | Emerging |
| Fiduciary and legal framing | Treat the shopping agent as a loyal agent of the user. | AI Agents and the Law (2025), Fiduciary Illusion (Igaya 2026) | Emerging, no tests |
| Mechanism design | Set payment rules that reward checkable, truthful content. | VCR mechanism (Xu 2026) | Emerging, simulation only |

## What the evidence shows
### Finding 1: Prompt warnings and training cut shopping bias, but do not remove it.
- **BiasRecBench (2026)**: Injected authority, popularity and brand cues lowered accuracy by up to 38 points. A warning prompt raised GPT-4o robustness by 3.5 to 12 points.
- **BiasRecBench (2026)**: Fine-tuning on 50 debiased examples raised biased accuracy by 8 to 15 points on two 14B models.
- Found in the Middle (Tang 2024): Shuffling list order and merging rankings raised scores by about 7 to 18% on GPT-3.5. The tests were on ranking tasks, not shopping.
- **Prompt-based reranking (2025)**: Shuffling user history helped. Explicit "ignore position" instructions did not.
- **Strength:** Medium. Several models were tested, but the main shopping result is one new benchmark. Its text and tables disagree on some numbers.

### Finding 2: Naming the persuasive intent reduces influence. A plain AI label does not.
- **Persuasive intent (Rauchfleisch 2026)**: 1,500 UK adults chatted with a persuasive bot. An AI notice alone left the attitude shift at 13.1 points, against 12.6 with no notice.
- Persuasive intent (Rauchfleisch 2026), second arm: Disclosing the bot's persuasive instructions cut the attitude shift to 6.3 points.
- Ads that Talk Back (Tang 2025): 179 US users saw chatbot ads. Even with a "Sponsored" link, 49% did not notice the ad.
- **LLMAdBench (Ai 2026)**: More than 18,000 human judgments show that a sponsored label changes where people want ads placed. The abstract gives no effect size.
- **Context (Salvi 2026)**: Sponsored picks rose to 61.2% under a persuading chatbot, against 22.4% in search. The label condition did not stop the steering in the main results.
- **Strength:** Medium for attitudes, from one preregistered study. Low for purchases, because no study has tested labels on purchases.

### Finding 3: Lab defenses cut seller manipulation strongly. Standard safety filters cut it little.
- **SCI-Defense (Yu 2026)**: Catches 96.2% of review-style manipulation at a 1.2% false positive rate. Results are self-reported and not peer reviewed.
- **GEO Defender (Li 2026)**: Lowers average attack success from 50.32% to 6.20% over seven attacks. It keeps 94.12% of useful evidence use.
- **Counter-GEO-Bench (2026)**: Off-the-shelf guard models cut attack success by at most 5.7% relative. A simple baseline cut it by 47.6% relative.
- **Strength:** Low to Medium. The defenses are new, the numbers are self-reported, and they were tested only on known attacks.

### Finding 4: Shopping agents struggle to learn user preferences, and delegation leaks them.
- **CoShop (Saracay 2026)**: No agent passed 56% accuracy after five turns of dialog. One model asked a median of 9 clarifying questions.
- **Role coherence (Alavi 2026)**: A buyer agent leaks its willingness to pay through dialog. Sellers recovered it almost one-for-one.
- **ABxLab (Cherep 2025)**: 17 LLM agents in more than 80,000 shopping runs reacted more to prices, ratings and nudges than people do.
- **Strength:** Medium. These are benchmark and simulation results with no outcome data from real shoppers.

### Finding 5: Fiduciary and market-design ideas exist, but none has a measured consumer effect.
- AI Agents and the Law (2025): Argues that a shopping agent steering to a partner product breaches loyalty. This is a legal argument only.
- **Fiduciary Illusion (Igaya 2026)**: Argues that fiduciary labels do not stop machine-targeted marketing. Read from the metadata only.
- **VCR mechanism (Xu 2026)**: Pays creators for checkable content. Simulated defense utility beats the best baseline by about 12.1 points.
- **Strength:** Low. The work is legal, theoretical or simulated, and no study measures consumer welfare.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do labels help? | Intent disclosure halves persuasion (Rauchfleisch 2026). | Sponsored labels do not stop steering (Salvi 2026). | A preregistered test with purchases as the outcome. |
| Do prompt warnings help? | Warnings raise robustness (BiasRecBench 2026). | Bias instructions do not help rankers (Prompt-based reranking 2025). | Both prompts tested on the same models and tasks. |
| Should agents be loyal to users? | Breach of loyalty under agency law (AI Agents and the Law 2025). | Serve a plural set of interests (Governing AI Agents 2025). | Measured outcomes under each rule. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| No purchase-level test of disclosure labels. | Changed attitudes may not change what people buy. | Persuasive intent (Rauchfleisch 2026) |
| No independent test of seller defenses. | The current numbers are self-reported. | SCI-Defense (Yu 2026) |
| No test against adaptive attacks. | Attackers can rephrase text to avoid fixed defenses. | GEO Defender (Li 2026) |
| No measured fiduciary intervention. | Legal duties have no tested effect on shopping outcomes. | AI Agents and the Law (2025) |
| No real-market test of mechanisms. | Simulated sellers may respond differently. | VCR mechanism (Xu 2026) |
| No consumer-welfare test of preference elicitation. | Asking more questions may not improve picks. | CoShop (Saracay 2026) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| BiasRecBench | **Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)** | 2026 | arXiv preprint | summary of full text |
| Found in the Middle (Tang 2024) | **Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models** | 2024 | NAACL 2024 | abstract |
| Prompt-based reranking (2025) | **Prompt-Based LLMs for Position Bias-Aware Reranking in Personalized Recommendations** | 2025 | arXiv preprint | search summary |
| CoShop (Saracay 2026) | **Beyond expert users: agents should help users construct preferences, not just elicit them** | 2026 | arXiv preprint | search summary |
| Role coherence (Alavi 2026) | **When Agents Shop for You: Role Coherence in AI-Mediated Markets** | 2026 | arXiv preprint | search summary |
| ABxLab (Cherep 2025) | **A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments** | 2025 | ICLR 2026 | search summary |
| AI Agents and the Law (2025) | **AI Agents and the Law** | 2025 | arXiv preprint | search summary |
| Fiduciary Illusion (Igaya 2026) | **The Fiduciary Illusion: Anticipatory AI, Machine-Targeted Marketing, and the Right to Agency** | 2026 | SSRN | metadata only |
| Governing AI Agents (2025) | **Governing AI Agents** | 2025 | arXiv preprint | search summary |
| Ads that Talk Back (Tang 2025) | **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** | 2025 | IMWUT 2025 | summary of full text (partial) |
| Persuasive intent (Rauchfleisch 2026) | **Toward Meaningful Transparency for AI Chatbots: Disclosing Persuasive Intent Reduces Persuasion** | 2026 | arXiv preprint | abstract page |
| LLMAdBench (Ai 2026) | **LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses** | 2026 | arXiv preprint | abstract |
| Salvi 2026 | **Commercial Persuasion in AI-Mediated Conversations** | 2026 | arXiv preprint | search summary |
| LLM-generated ads (Meguellati 2025) | **LLM-Generated Ads: From Personalization Parity to Persuasion Superiority** | 2025 | arXiv preprint | abstract |
| SCI-Defense (Yu 2026) | **SCI-Defense: Detecting Persuasion-Structured Manipulation of LLM-Based Ranking in Generative Engines** | 2026 | arXiv preprint | abstract |
| GEO Defender (Li 2026) | **When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization** | 2026 | arXiv preprint | abstract |
| Counter-GEO-Bench (2026) | **Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization** | 2026 | arXiv preprint | abstract |
| VCR mechanism (Xu 2026) | **Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes** | 2026 | arXiv preprint | abstract |

<details><summary>Original research question</summary>

What research proposes and tests ways to make LLM search and shopping assistants act in the consumer's interest: debiasing agent choices (position, brand, anchoring), eliciting and representing user preferences for delegation, fiduciary or principal-agent alignment of AI shopping agents, disclosure and labeling of sponsored content in LLM answers, robustness to seller manipulation, and mechanism or market design for agent-mediated commerce? Which interventions have measured effects?

</details>
