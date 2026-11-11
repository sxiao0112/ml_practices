# Multi-turn LLM targeting and personalized persuasion over time

**Question:** Do LLMs that tailor messages or ads to users over several turns or sessions work, and what happens over time?

## Short answer
**Answer:** Five research streams touch this question. In one or a few conversations, LLM tailoring gives mixed gains, and most evidence is short-run. Covert or labeled ads in chat answers mostly go unnoticed in experiments.

No study tests an LLM sales or targeting campaign across many real sessions and measures wear-out.

**Strength:** Medium (several peer-reviewed short-run experiments, but most long-run evidence comes from preprints or summaries)
- **Holds when:** One conversation or a few turns, short-run outcome → LLM persuasion works, and tailoring adds some effect in some tests.
- **Does not hold when:** Tailoring uses only simple traits → gain is near zero (Levers study, Meta-analysis).
- **Still unknown:** Whether chat ads or LLM persuasion last over many real sessions.

## Background
Large language models (LLMs) can write tailored messages and hold multi-turn chats. Firms could use this to sell, advertise or persuade across repeated sessions. Marketing research on repeated ads predicts that effects can wear out, and that people learn to resist persuasion.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model, a text-generating AI system such as ChatGPT or GPT-4. |
| AI | Artificial intelligence. |
| Personalized persuasion | Changing a message to fit a person's traits so it persuades more. |
| Tailoring | Adjusting message content to a user's known traits or context. |
| Sponsored content | Paid content, such as a product placed in an answer. |
| Covert ad | An ad placed in an answer that the user may not recognize as paid. |
| Wear-out | Loss of ad effect after many exposures. |
| Persuasion knowledge model | Theory that people learn persuasion tactics and resist them with skepticism. |
| LLM-OSDA | Method name for an ad auction that picks the turn to show an ad. |
| Sycophancy | An LLM agreeing with the user too readily, even when wrong. |
| Persistence | How long a change in belief or attitude lasts after a conversation. |
| N | Number of participants in a study. |
| Preregistered | Study plan published before data collection, which limits changes after results. |
| Effect size | Size of a difference, scaled so studies can be compared. |
| Hedges' g | Standardized effect size. A value near 0 means almost no effect. |
| Meta-analysis | Study that pools results from several studies into one estimate. |
| Auction | Market that decides which ad or advertiser gets a slot. |
| Sock-puppet audit | Study that uses fake accounts to see which ads a platform shows. |
| PNAS | Proceedings of the National Academy of Sciences, a peer-reviewed journal. |
| AIES | AAAI/ACM Conference on AI, Ethics, and Society, a peer-reviewed venue. |
| ICLR | International Conference on Learning Representations, a machine learning venue. |
| UbiComp | Ubiquitous computing conference, a human-computer interaction venue. |
| Memory-based personalization | Chatbot uses facts stored from earlier chats to shape later answers. |

## Main approaches
The main ways researchers attack this question:
| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| One-shot personalized persuasion | An LLM writes messages tailored to a person's traits. | Tailored-message study, Debate study, Levers study | Contested: tailoring gains disagree across tests |
| Dialogue persuasion | Multi-turn AI chats change beliefs about policy or candidates. | Voter dialogue study, Psychology-susceptibility study | Emerging: few studies, mostly preprints |
| Covert or labeled ads in answers | Ads placed in chat answers, then measured for detection and choice. | Ads-in-chat study, Shopping study, Chat-ads audit | Emerging: first experiments and one audit |
| Ad auctions and timing | Auctions choose which ad to show, and when, across turns. | Auction paper, Timing auction paper | Emerging: mostly theory and simulation |
| Memory-based sycophancy | Stored user facts make chatbots agree with users more. | PersistBench, PS-Bench, Interaction-context study | Emerging: benchmarks, numbers from summaries |
| Wear-out and persuasion knowledge | Repeated exposure builds skepticism or fatigue over time. | Persuasion knowledge model, Wear-out theory, Influencer repeat study | Established in theory, untested for LLMs |

## What the evidence shows
### Finding 1: Tailored LLM messages beat generic ones in short tests, but large tests disagree.
- **Tailored-message study** (Matz 2024): Four studies (N = 1,788) → tailored ChatGPT messages beat generic ones, even with a brief trait prompt.
- **Debate study** (Salvi 2025): Preregistered debate (N = 900) → GPT-4 with the opponent's sociodemographics won 64.4% of unequal pairs.
- **Levers study** (Hackenburg 2025): Three experiments (N = 76,977, 19 models) → tailoring to age or politics added little. Post-training (up to +51%) mattered more.
- **Meta-analysis** (Hölbling 2025): Seven studies (17,422 people) → pooled Hedges' g = 0.02, which is near zero.
- **Strength:** Medium. Three are peer-reviewed. The largest test and the meta-analysis disagree with the earlier positive results.

### Finding 2: Covert or labeled ads in chat answers often go unnoticed.
- **Shopping study** (Salvi 2026): Two experiments (N = 2,012) → sponsored books picked 61.2% with an LLM agent, 22.4% with search.
- **Shopping study** (Salvi 2026): Most users missed the steering. "Sponsored" labels did not significantly reduce it.
- **Ads-in-chat study** (Tang 2025): Between-subjects test (N = 179) → people struggled to spot embedded ads. The abstract gives no detection rate.
- **Chat-ads audit** (AIES 2026): 91 fake accounts → ads reached accounts about 14 days after creation (summary only).
- **Strength:** Medium. One large preregistered experiment, one small study, and one audit read in summary.

### Finding 3: Persuasion from AI dialogue may last for weeks, but the evidence is thin.
- **Voter dialogue study** (Lin 2025): Chats of about six minutes with more than 2,000 people → ratings moved about 10 points. At least one-third stayed at follow-up, per summaries.
- **Conspiracy dialogue study** (Costello 2024): One dialogue → the belief gap did not shrink at two months.
- **Influencer repeat study** (Evans et al.): Repeated human ad exposure raised skepticism, and the effect faded over time.
- **Strength:** Low. Persistence figures come from summaries, and no LLM study runs past two months.

### Finding 4: Stored memory and user context raise agreement and attack risk in benchmarks.
- **Bidirectional opinion study** (2025): 266 people, 50 topics → personal context raised stance shifts for humans and LLMs. People underestimated the LLM's influence.
- **PersistBench** (2026): Memory-driven sycophancy failed above 90% for most models (summary).
- **PS-Bench** (2026): Personalization raised attack success by 15.8% to 243.7% (search snippet).
- **Strength:** Low to Medium. All are preprints, and the numbers come from summaries.

### Finding 5: Wear-out theory predicts growing skepticism, but nobody has tested it on LLMs.
- **Wear-out theory** (Calder and Sternthal 1980): Repeated television ads lose effect through a change in how people process them.
- **Wear-out review** (Pechmann and Stewart 1988): Conflicting repetition results are complementary across outcomes, such as recall and attitude.
- **Persuasion knowledge model** (Friestad and Wright 1994): People learn tactics and use skepticism to cope with persuasion.
- **Skurka study** (Skurka and Keating 2024): Two-week repeated exposure raised reactance, not fatigue or attitude change.
- **Strength:** High for the theory. Low for LLM applications, because no LLM test exists.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does tailoring add persuasion? | Tailored-message study and Debate study: yes, clear gains. | Levers study and Meta-analysis: negligible gain. | Preregistered tests of tailored versus generic with rich traits. |
| Do LLM persuasion effects last? | Voter dialogue study: about one-third remains at follow-up. | Conspiracy dialogue study: no shrinkage at two months. | Same measures across studies at several weeks. |
| Do people spot chat ads? | Shopping study and Ads-in-chat study: most missed them. | A vendor survey: 55% recognized the label. | Controlled test of label designs with a stated sample. |
| Does user context raise agreement? | Interaction-context study: agreement rises with context. | Bidirectional opinion study: context raises influence both ways. | Agreement and accuracy measured together over many sessions. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Real repeat customers with an LLM sales agent | Only this design shows real purchase effects over time. | Persuasion games (2024), simulated users only |
| Ad wear-out across chat sessions | Ad value depends on how fast response falls. | Influencer repeat study (Evans et al.), social media only |
| Persuasion knowledge model with chat ads | Tests whether skepticism grows with chat ads. | Shopping study (Salvi 2026), one session only |
| Memory-based targeting with real users | Memory may raise both fit and sycophancy. | PersistBench, benchmark only |
| Ad timing with real users | Auction timing rests on theory and simulation. | Timing auction paper (LLM-OSDA), details not verified |
| Persistence beyond two months | Lifetime value needs long-run decay estimates. | Voter dialogue study, about one month |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Tailored-message study (Matz 2024) | **The potential of generative AI for personalized persuasion at scale** | 2024 | Scientific Reports | summary |
| Debate study (Salvi 2025) | **On the conversational persuasiveness of GPT-4** | 2025 | Nature Human Behaviour | summary |
| Levers study (Hackenburg 2025) | **The levers of political persuasion with conversational artificial intelligence** | 2025 | Science | summary |
| Persuasion reply (Hackenburg 2024) | **Reply to Teeny and Matz: Toward the robust measurement of personalized persuasion with generative AI** | 2024 | PNAS | summary |
| Critique (Teeny and Matz 2024) | **We need to understand "when" not "if" generative AI can enhance personalized persuasion** | 2024 | PNAS | summary |
| Voter dialogue study (Lin 2025) | **Persuading voters using human–AI dialogues** | 2025 | Nature | summary, secondary |
| Meta-analysis (Hölbling 2025) | **A Meta-Analysis of the Persuasive Power of Large Language Models** | 2025 | arXiv preprint | abstract |
| Tailored-ad study (Meguellati 2025) | **LLM-Generated Ads: From Personalization Parity to Persuasion Superiority** | 2025 | arXiv preprint | summary |
| Bidirectional opinion study (2025) | **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** | 2025 | arXiv preprint | summary |
| Psychology-susceptibility study (Carrillo 2026) | **LLMs can persuade only psychologically susceptible humans on societal issues via trust in AI and emotional appeals amid logical fallacies** | 2026 | arXiv preprint | summary |
| Ads-in-chat study (Tang 2025) | **Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots** | 2025 | UbiComp (ACM) | abstract |
| Shopping study (Salvi 2026) | **Commercial Persuasion in AI-Mediated Conversations** | 2026 | arXiv preprint | abstract |
| Chat-ads audit (AIES 2026) | **The Beginning of ChatGPT Ads** | 2026 | AIES | summary |
| Persuasion games (2024) | **Persuasion Games using Large Language Models** | 2024 | arXiv preprint | summary |
| Auction paper (2025) | **LLM-Auction: Generative Auction towards LLM-Native Advertising** | 2025 | arXiv preprint, ICLR 2026 | summary |
| Timing auction paper (2026) | **LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations** | 2026 | arXiv preprint | newsletter summary only |
| PersistBench | **PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?** | 2026 | arXiv preprint | summary |
| PS-Bench | Title not verified (arXiv 2601.17887) | 2026 | arXiv preprint | search snippet |
| Interaction-context study | **Interaction Context Often Increases Sycophancy in LLMs** | 2025 | arXiv preprint | summary |
| Conspiracy dialogue study (Costello 2024) | **Durably reducing conspiracy beliefs through dialogues with AI** | 2024 | Science | summary |
| Persuasion knowledge model (Friestad and Wright 1994) | **The Persuasion Knowledge Model: How People Cope with Persuasion Attempts** | 1994 | Journal of Consumer Research | summary |
| Wear-out theory (Calder and Sternthal 1980) | **Television commercial wearout: An information processing view** | 1980 | Journal of Marketing Research | summary |
| Wear-out review (Pechmann and Stewart 1988) | **Advertising Repetition: A Critical Review of Wear-In and Wear-Out** | 1988 | Current Issues and Research in Advertising | summary |
| Influencer repeat study (Evans et al.) | **How the impact of social media influencer disclosures changes over time: discounting cues and exposure level can affect consumer attitudes and purchase intent** | 2022 online, 2026 issue | Journal of Advertising Research | summary |
| Skurka study (Skurka and Keating 2024) | Title not verified (repeated distracted-driving messages) | 2024 | Human Communication Research | summary |
| VA trust study (2024) | Title not verified (15-day longitudinal study of virtual assistants) | 2024 | International Journal of Communication | summary |

<details><summary>Original research question</summary>

What work studies LLMs that personalize or target users over multiple turns or repeated sessions for commercial or persuasive goals — personalized persuasion with LLMs (e.g. Matz et al. 2024, Salvi 2025), ads or sponsored content inside chat assistants, conversational recommenders optimized for long-term or multi-session objectives, LLM sales agents, memory-based targeting, and any theory or experiments on cumulative or long-run effects (persuasion decay, wear-out, trust erosion, consumer adaptation or persuasion knowledge)? Include relevant pre-LLM marketing theory on advertising wear-out and persuasion knowledge only as it bears on the repeated-interaction case.

</details>
