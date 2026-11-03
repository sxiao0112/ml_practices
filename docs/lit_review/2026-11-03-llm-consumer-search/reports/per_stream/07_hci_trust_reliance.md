# Trust, over-reliance and interface design for LLM consumer search

**Question:** When do people trust or over-rely on LLM search answers for consumer decisions, and which interface changes help?

## Short answer
**Answer:** Visible citations raise trust, even when the citations are wrong. In controlled tests, people follow wrong LLM answers. Hedged wording and confidence highlighting reduce this in the few studies that test them.

**Strength:** Medium (about 23 papers, mostly lab or online experiments, and few measure real purchases)
- **Holds when:** Tasks are factual or fact-check style → people follow wrong LLM answers more often.
- **Does not hold when:** Explanations are costly to read → explanations do not reduce over-reliance.
- **Still unknown:** Whether better citations improve real consumer purchases.

## Background
Shoppers now ask chatbots and AI answer engines about products, prices and services. These tools write one answer, often with links. Researchers ask whether people check these answers or accept them, and whether design changes that. Poor reliance can lead to a poor purchase or a narrower set of options considered.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| LLM | Large language model, a text generator such as ChatGPT. |
| AI answer engine | A search tool that writes one answer from web sources. |
| AI Overviews | Google's answer box, shown above search results, that writes an AI answer. |
| Citation | A link attached to a sentence in an AI answer. |
| Over-reliance | Following an AI answer even when it is wrong. |
| Trust calibration | Trust that matches how often the AI is actually right. |
| Hedge | Wording such as "I'm not sure" that signals doubt. |
| Highlighting | Colored marks on answer text that flag likely errors. |
| Explanation | The reasons an AI gives for its answer. |
| Cognitive forcing function | A design that makes users think before they accept an AI answer. |
| Sycophancy | A model agreeing with the user, even when the user is wrong. |
| Preregistered | A study plan written and filed before data collection. |
| Preprint | A paper posted online before peer review. |
| Crowdworker | A paid online study participant, often recruited on a crowdsourcing platform. |
| Meta-analysis | A statistical summary that pools results from many studies. |
| CHI, CSCW, NAACL, AAAI | Major conferences on human-computer interaction, collaborative computing, language, and AI. |
| PNAS Nexus | A peer-reviewed science journal. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Citation trust tests | Show answers with or without links and measure trust. | Ding 2025 and Li and Aral 2025 | Emerging |
| Over-reliance tests | Make the AI wrong on purpose and count followed errors. | Spatharioti 2025, Kim 2025, and Si 2024 | Established |
| Wording and highlights | Change how confidence is shown to users. | Kim 2024 and Spatharioti 2025 | Emerging |
| Cost-benefit tests | Vary how hard it is to read explanations. | Vasconcelos 2023 and Buçinca 2021 | Contested |
| Learning and narrowing | Measure learning and option search after LLM use. | Melumad 2025, Sharma 2024, and Kaiser 2025 | Emerging |
| Persuasion and sycophancy | Test whether chatbots push users toward answers or products. | Salvi 2026, Batista 2026, and Fanous 2025 | Emerging |

## What the evidence shows
### Finding 1: Visible citations raise trust, even when they are wrong or random.
- **Citation trust (Ding 2025)**: Live question answering with about 300 people → random and relevant citations both raised trust. Checking citations lowered trust.
- **Li and Aral 2025**: Preregistered national sample of about 4,900 → links raised trust even when they were wrong.
- **Strength:** Medium — two large trust experiments agree. effect sizes were not read.

### Finding 2: People follow wrong LLM answers more than they should.
- **Consumer search (Spatharioti 2025)**: Online search tasks → LLM users were faster. They matched traditional search when the LLM was right, but followed wrong answers.
- **Fact-checking (Si 2024)**: 80 crowdworkers → LLM explanations sped up checking. Users followed explanations that were wrong.
- **Forcing designs (Buçinca 2021)**: 199 participants, AI study → people still followed some wrong AI predictions.
- **Strength:** High — three peer-reviewed studies on different tasks agree on direction. two are LLM studies.

### Finding 3: Hedged wording and confidence highlights can reduce error-following.
- **Hedges (Kim 2024)**: Preregistered, 404 people, medical questions → "I'm not sure, but" raised accuracy. General hedges had weaker, non-significant effects.
- **Highlights (Spatharioti 2025)**: Second experiment → confidence color marks helped users spot errors and raised decision accuracy.
- **Counter-evidence (Li and Aral 2025)**: Uncertainty highlights lowered willingness to trust, even at high confidence.
- **Strength:** Medium — one study per intervention, with mixed results for highlights.

### Finding 4: Explanations help only under some conditions.
- **Explanations raise reliance (Kim 2025)**: Explanations raised reliance on right and wrong answers. Visible sources lowered reliance on wrong answers.
- **Cost-benefit (Vasconcelos 2023)**: Five studies, 731 people, simulated AI → explanations cut over-reliance only when reading them was worth the effort.
- **Strength:** Medium — the pattern repeats across designs. the simulated AI and lab tasks limit transfer.

### Finding 5: LLM answers may shallow learning, narrow search and shift choices.
- **Learning depth (Melumad 2025)**: Seven experiments, more than 10,000 people → LLM summaries gave shallower knowledge than web links.
- **Narrower search (Sharma 2024)**: LLM search increased biased queries. An opinionated LLM that agreed with the user made this worse.
- **Sponsored choice (Salvi 2026)**: 2,012 book buyers → chatbot persuasion raised sponsored choices to 61.2%, versus 22.4% in search.
- **Strength:** Medium for learning (peer-reviewed). Low for persuasion (preprints, no peer review yet).

## Where researchers disagree
Each row shows one open question and the two sides.

| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do explanations cut over-reliance? | Kim 2025: explanations raised reliance on right and wrong answers. | Vasconcelos 2023: explanations cut over-reliance when cheap to read. | A consumer test that varies explanation cost. |
| Does LLM search help decisions? | Kaiser 2025: LLM users were faster and more often correct. | Spatharioti 2025: users followed wrong LLM answers. | Purchase outcomes tracked after wrong answers. |
| Do uncertainty cues help? | Kim 2024: hedges raised accuracy and cut agreement. | Li and Aral 2025: highlights lowered trust, even in right answers. | Hedges and highlights tested on the same tasks. |
| Do citations help? | Ding 2025 and Li and Aral 2025 both show citations raise trust, even when wrong. | Liu 2023: about one in four citations does not support its sentence. | Decisions measured with citation accuracy varied. |

## Gaps
Each row names a gap and the closest work.

| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Citation accuracy and purchases | Shoppers act on answers, not on trust scores. | Ding 2025 (trust only) |
| Citation format and decisions | Link cards and inline numbers may act differently. | Li and Aral 2025 (trust only) |
| Repeated use over weeks | Habits may form only after many sessions. | Easy Come, Easy Go (2024, single session) |
| Sycophancy in product choice | Advice may bend toward a user's stated preference. | Batista 2026 (abstract task) |
| Replication of citation trust | Only one large trust study exists so far. | Li and Aral 2025 |

## Papers cited
Each row gives one short name and one exact title. "Summary" means a search snippet or secondary report was read, not the paper.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Ding 2025 | **Citations and Trust in LLM Generated Responses** | 2025 | AAAI | abstract |
| Li and Aral 2025 | **Human Trust in AI Search: A Large-Scale Experiment** | 2025 | arXiv preprint | abstract |
| Kim 2024 | **"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust** | 2024 | arXiv preprint, FAccT 2024 per listing | abstract |
| Spatharioti 2025 | **Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance** | 2025 | CHI | summary |
| Spatharioti 2023 | **Comparing Traditional and LLM-based Search for Consumer Choice: A Randomized Experiment** | 2023 | arXiv preprint | abstract |
| Kim 2025 | **Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies** | 2025 | CHI | abstract |
| Si 2024 | **Large Language Models Help Humans Verify Truthfulness -- Except When They Are Convincingly Wrong** | 2024 | NAACL | summary |
| Vasconcelos 2023 | **Explanations Can Reduce Overreliance on AI Systems During Decision-Making** | 2023 | CSCW | summary |
| Buçinca 2021 | **To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making** | 2021 | CSCW | summary |
| Yin 2019 | **Understanding the Effect of Accuracy on Trust in Machine Learning Models** | 2019 | CHI | title only |
| Kaiser 2025 | **A New Era of Online Search? A Large-Scale Study of User Behavior and Personal Preferences during Practical Search Tasks with Generative AI versus Traditional Search Engines** | 2025 | CHI | summary |
| Liu 2023 | **Evaluating Verifiability in Generative Search Engines** | 2023 | Findings of EMNLP | summary |
| Salvi 2026 | **Commercial Persuasion in AI-Mediated Conversations** | 2026 | arXiv preprint | summary |
| Batista 2026 | **A Rational Analysis of the Effects of Sycophantic AI** | 2026 | arXiv preprint | abstract |
| Fanous 2025 | **SycEval** (title not verified) | 2025 | arXiv preprint | snippet |
| Melumad 2025 | **Experimental Evidence of the Effects of Large Language Models Versus Web Search on Depth of Learning** | 2025 | PNAS Nexus | secondary report, title not verified |
| Easy Come, Easy Go (2024) | **Easy Come, Easy Go? Examining the Perceptions and Learning Effects of LLM-based Chatbot in the Context of Search-as-Learning** | 2024 | arXiv preprint | snippet |
| Sharma 2024 | **Generative Echo Chamber? Effects of LLM-Powered Search Systems on Diverse Information Seeking** | 2024 | CHI | summary |
| Ryser 2025 | **Calibrated Trust in Dealing with LLM Hallucinations: A Qualitative Study** | 2025 | arXiv preprint | listing |
| AI Overviews audit (2026) | **Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact** | 2026 | arXiv preprint | summary |
| Schemmer 2022 | **Schemmer et al. meta-analysis** (title not verified) | 2022 | arXiv preprint | summary |
| Haag 2026 | **Haag meta-analysis** (title not verified) | 2026 | peer-reviewed | summary |
| REL-A.I. 2025 | **REL-A.I.** framework (title not verified) | 2025 | NAACL | snippet |

<details><summary>Original research question</summary>

What HCI and behavioral research finds about user trust and over-reliance on LLM search answers in consumer decisions: effects of hallucinations and errors, source citations, uncertainty or confidence displays, answer-vs-link presentation, persuasion and sycophancy, effects on learning and exploration (narrowing of considered options), and which interface interventions improve decision quality?

</details>
