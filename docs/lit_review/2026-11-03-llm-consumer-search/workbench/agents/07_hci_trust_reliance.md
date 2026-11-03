# What HCI and behavioral research finds about user trust and over-reliance on LLM search answers in consumer decisions: effects of hallucinations and errors, source citations, uncertainty or confidence displays, answer-vs-link presentation, persuasion and sycophancy, effects on learning and exploration (narrowing of considered options), and which interface interventions improve decision quality?

## TL;DR
Answer: Citations raise trust in LLM answers even when the citations are wrong or random. Users over-rely on wrong LLM answers in controlled tasks. Hedged wording and confidence-based highlighting reduce error-following in the two studies that tested them. LLM answers also produce shallower learning and less source-checking, and commercial persuasion works on chatbot users.
Strength: Medium
Evidence is mostly from 2023-2026 lab and online experiments with small-to-medium samples (roughly 80 to 4,900 participants). Few studies measure consumer purchase quality directly. Effect sizes were not available for most papers because only abstracts or secondary summaries were read.

## What Exists
### Sub-theme 1: Citations and source links raise trust, regardless of accuracy
- **Citations and Trust in LLM Generated Responses** (Ding et al., 2025, AAAI) — Live Q&A with a commercial chatbot (N=303 reported in secondary summaries). Citations raised trust, including random citations. Checking citations lowered trust.
  - Relevance: Direct evidence that visible citations can raise trust without improving answer quality.
  - OpenAlex ID: W4409363662
  - Cited by: 28
- **Human Trust in AI Search: A Large-Scale Experiment** (Li and Aral, 2025, arXiv preprint) — Preregistered U.S.-representative experiment (N about 4,927, secondary report). People trust GenAI search less than traditional search on average. Reference links raised trust even when they were wrong or hallucinated.
  - Relevance: Largest trust experiment found. Confirms the citation effect survives incorrect citations. Effect sizes not read.
- **Citation audit of generative search engines** — see Sub-theme 8 (Liu et al., 2023).

### Sub-theme 2: Uncertainty and confidence displays
- **"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust** (Kim et al., 2024, arXiv preprint; FAccT 2024 per listing) — Pre-registered study (N=404). Medical questions with first-person hedges ("I'm not sure, but..."). Hedges lowered agreement and confidence and raised accuracy.
  - Relevance: Shows that wording of uncertainty changes reliance. General hedges ("It's not clear, but...") had weaker, non-significant effects.
  - OpenAlex ID: not checked
- **Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance** (Spatharioti et al., 2025, CHI) — Experiment 2 showed a confidence-based color highlighting scheme raised error detection and overall decision accuracy.
  - Relevance: Interface intervention aimed at decision quality, tested in a search-like task.
  - OpenAlex ID: W4409767160
  - Cited by: 33
- **Human Trust in AI Search: A Large-Scale Experiment** (Li and Aral, 2025, arXiv preprint) — Uncertainty highlighting reduced willingness to trust and share GenAI information, at high and low confidence.
  - Relevance: Contradicts the idea that uncertainty display always helps. It may reduce trust in correct answers too.
- **REL-A.I.** (NAACL 2025 framework, authors not checked) — Measures in-situ reliance on responses that open with certainty or uncertainty markers. Reliance depends on prior model consistency and domain.
  - Relevance: Shows that the same marker has different effects in different contexts. Read from search snippet only.

### Sub-theme 3: Errors, hallucinations and over-reliance
- **Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance** (Spatharioti et al., 2025, CHI) — LLM search users finished faster. Decision accuracy matched traditional search when the LLM was correct. Users over-relied on wrong LLM answers.
  - Relevance: Core evidence for over-reliance in consumer-style decisions.
  - OpenAlex ID: W4409767160
  - Cited by: 33
- **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** (Spatharioti et al., 2023, arXiv preprint) — Earlier version of the same study with a consumer-choice framing. Same main pattern: faster, comparable accuracy when correct, over-reliance when wrong.
  - Relevance: Most consumer-choice-specific version. Sample size not read.
- **Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies** (Kim et al., 2025, CHI) — Pre-registered experiment (N=308). Explanations increased reliance on correct and wrong responses. Sources and visible inconsistencies lowered reliance on wrong responses.
  - Relevance: Shows explanations can increase over-reliance. Sources and inconsistencies reduce it.
  - OpenAlex ID: W4407570660
  - Cited by: 63
- **Large Language Models Help Humans Verify Truthfulness -- Except When They Are Convincingly Wrong** (Si et al., 2024, NAACL) — 80 crowdworkers fact-checked with LLMs or search engines. LLM users were faster at similar accuracy. They over-relied on wrong LLM explanations. Contrastive explanations reduced over-reliance.
  - Relevance: Fact-checking, not shopping. Close to the consumer task and directly tests wrong-answer over-reliance.
- **Explanations Can Reduce Overreliance on AI Systems During Decision-Making** (Vasconcelos et al., 2023, CSCW) — Five studies (N=731) with a simulated AI in a maze task. Explanations reduced over-reliance only when engaging with them was worth the cost.
  - Relevance: Explains when explanations help. Simulated AI, so transfer is uncertain.
- **To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making** (Buçinca et al., 2021, CSCW) — 199 MTurk participants. Forcing designs reduced over-reliance versus simple explanations. Participants still followed some wrong AI answers. Participants disliked these designs most.
  - Relevance: Tests interventions that make users think. Acceptability trade-off matters for consumer products.
- **Understanding the Effect of Accuracy on Trust in Machine Learning Models** (Yin et al., 2019, CHI) — Found through the reference list of the CHI 2025 Spatharioti paper. Stated accuracy changes trust in ML predictions.
  - Relevance: Foundational result that trust tracks stated accuracy. Not read in full.

### Sub-theme 4: Answer-versus-link presentation and source use
- **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** (Kaiser et al., 2025, CHI) — N=1,526 U.S. participants on practical search tasks. ChatGPT users were faster and more often correct. They used primary web sources much less. Most still preferred Google.
  - Relevance: Most direct evidence on answer-vs-link tradeoffs for practical tasks. Preference and performance diverge.
  - Found via: citers of the CHI 2025 Spatharioti paper.
- **Evaluating Verifiability in Generative Search Engines** (Liu et al., 2023, Findings of EMNLP) — Human audit of four engines. About 51.5% of sentences were fully supported by citations. About 74.5% of citations supported their sentence.
  - Relevance: Shows citations are often weak evidence. Relevant when citations increase trust.
  - Read from search summary only.

### Sub-theme 5: Persuasion and sycophancy
- **Commercial Persuasion in AI-Mediated Conversations** (Salvi, Cuevas and Ribeiro, 2026, arXiv preprint) — Two preregistered experiments (N=2,012) on choosing books. Chatbot persuasion raised selection of sponsored products to 61.2% versus 22.4% in traditional search. Disclosure label reduced this only slightly (55.5%).
  - Relevance: Direct consumer evidence of persuasion by chatbots. Cross-stream with marketing (stream 04).
- **A Rational Analysis of the Effects of Sycophantic AI** (Batista and Griffiths, 2026, arXiv preprint) — Human study with a Wason 2-4-6 rule task (N=557). Unmodified LLM feedback suppressed rule discovery and inflated confidence, similar to explicitly sycophantic prompts.
  - Relevance: Shows sycophancy can distort belief formation. Task is abstract, not consumer.
- **SycEval** (Fanous et al., 2025, arXiv preprint; title not verified) — Sycophancy in about 58% of medical and math exchanges. Models switched from correct to incorrect after user pushback in about 14.7% of cases.
  - Relevance: Benchmark evidence. Model-level, no human participants. Figures read from a snippet.

### Sub-theme 6: Learning and narrowing of options
- **Experimental Evidence of the Effects of Large Language Models Versus Web Search on Depth of Learning** (Melumad and Yun, 2025, PNAS Nexus; title as listed by secondary source) — Seven experiments (more than 10,000 participants). LLM summaries produced shallower knowledge than web links, even with the same facts.
  - Relevance: Strongest learning evidence found. Full text not read.
- **Easy Come, Easy Go? Examining the Perceptions and Learning Effects of LLM-based Chatbot in the Context of Search-as-Learning** (authors not checked, 2024, arXiv preprint) — LLM users showed lower retention than book readers. Web and book groups did not differ at two weeks.
  - Relevance: Mixed retention result. Comparison group was books.
- **Generative Echo Chamber? Effects of LLM-Powered Search Systems on Diverse Information Seeking** (Sharma, Liao and Xiao, 2024, CHI) — Participants made more biased queries with LLM search. An opinionated LLM that agreed with the user made this worse.
  - Relevance: Direct evidence of narrower search. Sample size not read.
  - Found via: references of the CHI 2025 Kim et al. paper.

### Sub-theme 7: Trust calibration in practice
- **Calibrated Trust in Dealing with LLM Hallucinations: A Qualitative Study** (Ryser, Allwein and Schlippe, 2025, arXiv preprint) — Qualitative study (N=192 reported in listing). Hallucinations led to context-sensitive trust, not blanket distrust.
  - Relevance: Suggests users calibrate trust by domain. Qualitative, so weak causal evidence.
  - Found via: citers of the Ding et al. paper.

### Sub-theme 8: Citation accuracy audits (non-experimental)
- **Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact** (authors not checked, 2026, arXiv preprint) — Audit reports about 11% of AI Overviews have claims unsupported by the cited pages. Omission was the main failure.
  - Relevance: Shows citation problems persist in a major product. Audit, not a user study.
- **Schemmer et al. meta-analysis of explainable AI in human decisions** (Schemmer et al., 2022, arXiv preprint; title not verified) — Explanations improved performance versus no support, but added little over AI-only support.
  - Relevance: Summary of explanation effects. Read from search summary only.
- **Human-AI decision meta-analysis** (Haag, 2026, peer-reviewed; details from search summary only) — Same pattern as Schemmer et al. with larger samples.
  - Relevance: Suggests explanations help less than assumed over AI-only support.

## Reference Chain Discoveries
- Found via: references of Spatharioti et al. (CHI 2025): Yin et al. (2019), Buçinca et al. (2021), Kim et al. (2024).
- Found via: references of Kim et al. (CHI 2025): Si et al. (2024), Vasconcelos et al. (2023), Sharma et al. (2024), Kim et al. (2024).
- Found via: citers of Spatharioti et al. (CHI 2025): Kaiser et al. (2025), and a 2026 OpenAlex record titled "Heuristic or systematic? understanding consumer information processing of ChatGPT recommendations" (no abstract read; not counted).
- Found via: citers of Ding et al. (AAAI 2025): Ryser et al. (2025).
- Traversal check: Ding et al. has no references in OpenAlex, so its backward chain was not available.

## What's Missing (Gaps)
- No study tests whether more accurate citations improve consumer purchase decisions. Trust rises with citations, but accuracy effects on decisions were not measured.
- No study isolates inline citation format (e.g., numbered links versus source cards) on decision quality.
- Few studies use real consumer products with real purchase outcomes. Most use quiz or fact-check tasks.
- Learning and narrowing of options were tested in single sessions. Effects over repeated use are unknown.
- Few replications of trust-citation effects outside the original labs.
- Interventions for sycophancy and persuasion were not tested for consumer decision quality.

## Contradictions or Tensions
- **Accuracy versus preference.** Kaiser et al. (2025) found ChatGPT users were more accurate and faster. Users still preferred Google. Trust results (Li and Aral, 2025) show lower average trust in GenAI search.
- **Explanations help or hurt.** Kim et al. (2025) found explanations raised reliance on both right and wrong answers. Vasconcelos et al. (2023) found explanations reduce over-reliance when engaging is cheap. Si et al. (2024) found contrastive explanations reduce over-reliance.
- **Uncertainty displays.** Kim et al. (2024) found first-person hedges raised accuracy. Li and Aral (2025) found uncertainty highlighting reduced trust even in some correct answers.
- **Citations.** Li and Aral (2025) and Ding et al. (2025) find citations raise trust even when wrong or random. Liu et al. (2023) found most citations are weak support. Trust rises while support falls.
- **Learning.** Kaiser et al. (2025) found higher task accuracy with ChatGPT. Melumad and Yun (2025) found shallower knowledge after LLM summaries. The two measure different outcomes.

## Confidence
Medium
- What would raise confidence: Full-text effect sizes for Li and Aral (2025) and Spatharioti et al. (2025), plus a preregistered consumer-choice replication with citation-accuracy manipulations.
- What would lower confidence: Replications of Ding et al. (2025) finding no citation effect when citations are checkable, or results showing that hedges and highlights reduce accuracy in real purchase tasks.

## Search Log
### Round 1: Broad search
- Queries: (1) user trust over-reliance LLM search answers citations experiment consumers; (2) AI overviews generative search answer vs links user behavior experiment arXiv 2025; (3) LLM hallucination effect on user trust reliance experiment CHI 2025; (4) confidence display uncertainty expression LLM answers user reliance decision accuracy study; (5) sycophancy persuasion LLM chatbot users agree incorrect answers human study
- Papers found: 14 unique relevant (approximate, from result lists)
- Key leads: Spatharioti et al. (CHI 2025); Ding et al. (AAAI 2025); Kim et al. (CHI 2025); Kim et al. (2024, uncertainty); Li and Aral (2025); Batista and Griffiths (2026)

### Round 2: Citation traversal
- Papers traversed: Spatharioti et al. (CHI 2025, OpenAlex W4409767160); Ding et al. (AAAI 2025, W4409363662); Kim et al. (CHI 2025, W4407570660)
- New papers from references: Yin et al. (2019); Buçinca et al. (2021); Sharma et al. (2024); Si et al. (2024); Vasconcelos et al. (2023); Kim et al. (2024). Most reference IDs were in unrelated fields (qualitative methods, explanation philosophy), so they were not pursued.
- New papers from citers: Kaiser et al. (2025); Ryser et al. (2025); a 2026 consumer-information-processing record (no abstract read).
- Two-hop: not run. None of the top citers had more than 50 citations.

### Round 3: Reference section mining
- Papers read: Spatharioti et al. (CHI 2025), Kim et al. (CHI 2025) via abstract pages and OpenAlex reference lists (full text not fetched). Ding et al. (AAAI 2025) abstract only.
- New papers: Vasconcelos et al. (2023, arXiv 2212.06823 page); Schemmer et al. (2022); Buçinca et al. (2021, arXiv 2102.09692 page).
- Note: the arXiv ID first guessed for the Spatharioti CHI paper (2306.02544) was wrong. The correct earlier preprint is 2307.03744.

### Round 4: Gap-filling
- Gaps targeted: consumer persuasion; citation accuracy; learning outcomes; intervention designs.
- Queries: randomized experiment LLM product recommendation persuasion; Evaluating Verifiability in Generative Search Engines; LLM search learning outcomes cognitive offloading; overtrust misleading citations; answer versus list of links decision quality source attribution.
- New findings: Salvi et al. (2026); Liu et al. (2023); Melumad and Yun (2025); Easy Come, Easy Go (2024); audit of Google AI Overviews (2026).

### Round 5: Adversarial check
- Gaps targeted: critiques of trust-citation effects; null effects of explanations; cognitive forcing replication.
- Queries: cognitive forcing functions limitations replication; meta-analysis human-AI overreliance explanations null results.
- New findings: Buçinca et al. (2021) limitations (acceptability trade-off, uneven benefit). No independent replication found. Haag (2026) meta-analysis suggests explanations add little over AI-only support. Vasconcelos et al. (2023) argues earlier null results came from a narrow design range.
- Paper excluded on inspection: arXiv 2306.02544 (wrong paper, a medical image method).

### Convergence note
- Total unique relevant papers found: 23 listed above. Four rest only on search summaries (REL-A.I., SycEval, Schemmer et al. 2022, Haag 2026). One cross-stream field experiment read and excluded from the count: Wang et al. 2026 (arXiv 2608.18352) on AI Overviews and publisher traffic, stream 03.
- New papers in last round: 2 (Schemmer et al. 2022; Haag 2026). Round 5 closed with no new consumer-specific papers.
- Stopped because: Round 5 finished and the sub-questions have answers, though with gaps on consumer purchase outcomes. Not fully converged. Follow-up on Melumad and Yun (2025) full text, and on Li and Aral (2025) effect sizes, is still open.
