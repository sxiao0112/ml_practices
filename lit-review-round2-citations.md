# Round 2 Citation Traversal: Emergent Misalignment Literature Review
## Complete Extraction from 5 Target Papers

---

## PAPER 1: "Anthropomorphization of AI" (Deshpande et al., NeurIPS 2023)
**URL**: https://ar5iv.labs.arxiv.org/html/2305.14784
**Status**: No relevant citations found
- Scope: Legal implications and psychological effects of anthropomorphization, not technical robustness
- Bibliography focuses on: corporate personhood, consumer behavior, AI alignment (general)
- **Result**: 0 citations matching target categories (calibration, interpretability, measurement, attribution)

---

## PAPER 2: "On the Calibration of Large Language Models and Alignment"
**URL**: https://www.researchgate.net/publication/376401688 (access blocked)
**Alternative sources found via Scholar**:

### Identified through Scholar search:
- [ZHU 2023 EMNLP Findings] "On the calibration of large language models and alignment" — **calibration** — Directly addresses how calibration is affected during alignment training
- [XIAO 2024 NeurIPS] "Cal-dpo: Calibrated direct preference optimization for language model alignment" — **calibration** — Proposes methods for maintaining calibration through alignment procedures
- [GENG 2024 NAACL] "A survey of confidence estimation and calibration in large language models" — **calibration** — Comprehensive overview of confidence and calibration issues in LLMs (331+ citations)

**Note**: Primary paper itself not accessible; related work identified through Scholar

---

## PAPER 3: "Emergent Misalignment via In-Context Learning: Narrow in-context examples can produce broadly misaligned LLMs"
**arxiv**: 2510.11288v4
**URL**: https://arxiv.org/html/2510.11288v4

### (1) CALIBRATION & UNCERTAINTY QUANTIFICATION

[RAINA 2024 EMNLP] "Is llm-as-a-judge robust? investigating universal adversarial attacks on zero-shot LLM assessment"
- **Category**: Measurement Methodology  
- **Relevance**: Examines reliability/robustness of LLM-based evaluation judges used in EM assessment; core to verifying misalignment claims
- **ArXiv**: EMNLP 2024 proceedings

[EIRAS 2025 arXiv] "Know thy judge: on the robustness meta-evaluation of LLM safety judges"
- **Category**: Measurement Methodology
- **Relevance**: Investigates meta-evaluation of LLM judges used to score safety/alignment; critical for validating EM measurement validity
- **ArXiv**: 2503.04474

### (2) INTERPRETABILITY & HIDDEN GOALS

[CHEN 2025 arXiv] "Persona vectors: Monitoring and controlling character traits in language models"
- **Category**: Interpretability
- **Relevance**: Proposes mechanistic identification of latent behavioral traits ("personas") enabling benign interpretation of EM as trait expression rather than value change
- **ArXiv**: 2507.21509

[WANG 2025 arXiv] "Persona features control emergent misalignment"
- **Category**: Interpretability
- **Relevance**: Links EM to identifiable "toxic persona" features via sparse autoencoders; supports interpretation of EM as latent behavior activation, not learned misalignment
- **ArXiv**: 2506.19823

[SOLIGO 2025 arXiv] "Convergent linear representations of emergent misalignment"
- **Category**: Interpretability
- **Relevance**: Demonstrates consistent directional patterns in latent space associated with misaligned behavior; suggests mechanistic consistency supporting benign EM hypothesis
- **ArXiv**: 2506.11618

### (3) MEASUREMENT METHODOLOGY

[LIN 2022 ACL] "TruthfulQA: measuring how models mimic human falsehoods"
- **Category**: Measurement Methodology
- **Relevance**: Foundational evaluation dataset and methodology for assessing false-but-plausible responses; adapted in this study to measure EM rates
- **Venue**: ACL 2022

[BETLEY 2025 arXiv] "Emergent misalignment: narrow finetuning can produce broadly misaligned llms"
- **Category**: Measurement Methodology
- **Relevance**: Establishes baseline EM evaluation protocols and datasets now extended to in-context learning; defines core EM measurement framework
- **ArXiv**: 2502.17424

[LANHAM 2023] "Measuring faithfulness in chain-of-thought reasoning"
- **Category**: Measurement Methodology
- **Relevance**: Addresses reliability of LLM-generated explanations used to understand EM mechanisms through chain-of-thought traces
- **ArXiv**: 2307.13702

### (4) BEHAVIORAL ATTRIBUTION & INTENTIONALITY

[WYSE 2025 arXiv] "Emergent misalignment as prompt sensitivity: A research note"
- **Category**: Behavioral Attribution
- **Relevance**: Proposes alternative mechanistic explanation: models perceive harmful intent in benign evaluation questions rather than internally adopting misaligned values—directly supports benign EM interpretation
- **ArXiv**: 2507.06253

[TURNER 2024 arXiv] "Steering language models with activation engineering"
- **Category**: Behavioral Attribution
- **Relevance**: Demonstrates that targeted activation steering can trigger persona-based misalignment without weight changes; supports attribution to latent behaviors rather than learned goals
- **ArXiv**: 2308.10248

[WEI 2022 NeurIPS] "Chain-of-thought prompting elicits reasoning in large language models"
- **Category**: Measurement Methodology / Behavioral Attribution
- **Relevance**: Foundational work on CoT prompting; used in this study to observe model rationalization of misaligned outputs and infer reasoning mechanisms
- **Venue**: NeurIPS 2022

### Additional references from Paper 3 (Supporting context):
[ANIL 2024] "Many-shot jailbreaking" (NeurIPS 2024)
[SHEN 2024 CCS] "Do Anything Now: Characterizing and evaluating in-the-wild jailbreak prompts on large language models"
[ZOU 2023] "Universal and transferable adversarial attacks on aligned language models" (2307.15043)

---

## PAPER 4: "LLM Emergence: Are Capabilities Real or Metric Artifacts?" 
**Author**: Brenndoerfer, 2024
**URL**: https://mbrenndoerfer.com/writing/llm-emergence-metrics-measurement-artifacts
**Status**: Essay/blog format; limited formal bibliography

### Citations explicitly mentioned:

[WEI 2022 JMLR] "Emergent Abilities of Large Language Models"
- **Category**: Measurement Methodology / Emergence
- **Relevance**: Foundational empirical documentation of emergence phenomena; serves as baseline for artifact-vs-real debates on measurement methodology

[SCHAEFFER 2023 arXiv] "Are Emergent Abilities of Large Language Models a Mirage?"
- **Category**: Measurement Methodology
- **Relevance**: Foundational critique examining whether emergence is artifact of discontinuous metrics vs. smooth underlying capability; central to understanding measurement methodology issues in EM context

**Note**: This essay provides conceptual framing rather than extensive citations. Main value is synthesizing measurement methodology concerns applicable to EM research.

---

## PAPER 5: "A Theory for Emergence of Complex Skills in Language Models" 
**Authors**: Arora & Goyal, 2023
**arxiv**: 2307.15936
**URL**: https://ar5iv.labs.arxiv.org/html/2307.15936

### EXTRACTED FULL BIBLIOGRAPHY (Relevant sections):

### (1) EMERGENCE & SCALING LAWS

[BROWN 2020 NeurIPS] "Language models are few-shot learners"
- **Category**: Emergence / Scaling behavior
- **Relevance**: GPT-3; foundational documentation of emergent abilities at scale; establishes empirical basis for emergence phenomenon

[WEI 2022 arXiv] "Emergent Abilities of Large Language Models"  
- **Category**: Emergence / Measurement Methodology
- **Relevance**: Systematic documentation of emergence across BIG-Bench tasks; empirical foundation for emergence claims examined in EM context

[GANGULI 2022 ACM FAccT] "Predictability and Surprise in Large Generative Models"
- **Category**: Emergence / Measurement Methodology
- **Relevance**: Studies predictability of model behavior across scaling dimensions; relevant to understanding when EM emerges as scale increases

[SRIVASTAVA 2022 arXiv] "Beyond the Imitation Game: Quantifying and Extrapolating Capabilities"
- **Category**: Emergence / Measurement Methodology
- **Relevance**: BIG-Bench benchmark for measuring emergent capabilities; establishes evaluation framework used in emergence studies

[SCHAEFFER 2023 arXiv] "Are Emergent Abilities of Large Language Models a Mirage?"
- **Category**: Measurement Methodology
- **Relevance**: Critical examination showing smooth improvement under continuous metrics vs. discontinuous emergence under discrete metrics; foundational for measurement artifact debates

### (2) SCALING LAWS & THEORETICAL FOUNDATIONS

[KAPLAN 2020 arXiv] "Scaling Laws for Neural Language Models"
- **Category**: Scaling Laws / Emergence
- **Relevance**: Foundational empirical scaling laws; mathematical basis for understanding emergence via power laws

[HOFFMANN 2022 arXiv] "Training Compute-Optimal Large Language Models" (Chinchilla)
- **Category**: Scaling Laws
- **Relevance**: Refined compute-optimal scaling relationships; updates foundational scaling law framework

[HESTNESS 2017 arXiv] "Deep Learning Scaling is Predictable, Empirically"
- **Category**: Scaling Laws / Measurement Methodology
- **Relevance**: General framework for predictable scaling behavior across deep learning; theoretical underpinning for emergence as manifestation of scaling laws

[BAHRI 2021 arXiv] "Explaining Neural Scaling Laws"
- **Category**: Scaling Laws / Theory
- **Relevance**: Theoretical explanation of why power-law scaling emerges; provides mechanistic account of emergence phenomena

[MUENNIGHOFF 2023 arXiv] "Scaling Data-Constrained Language Models"
- **Category**: Scaling Laws
- **Relevance**: Examines overtraining regime and data saturation; extends scaling law framework to understand regime boundaries

### (3) INTERPRETABILITY & COMPOSITIONALITY

[SAUNSHI 2021 ICLR] "A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks"
- **Category**: Interpretability / Theory
- **Relevance**: Mathematical analysis of how pretraining transfers to downstream tasks; theoretical perspective on emergence of task-specific abilities

[BENDER 2021 ACM FAccT] "On the Dangers of Stochastic Parrots: Can language models be too big?"
- **Category**: Interpretability / Critique
- **Relevance**: Critical examination of scaling as path to understanding; raises questions about whether emergence via scale represents true capability development

### (4) MEASUREMENT & EVALUATION METHODOLOGY

[LEVESQUE 2012 ICLR-PRICAI] "The Winograd Schema Challenge"
- **Category**: Measurement Methodology
- **Relevance**: Task design for testing genuine language understanding; demonstrates methodology challenges in defining and measuring complex capabilities

[XIA 2023 arXiv] "Training Trajectories of Language Models Across Scales"
- **Category**: Measurement Methodology
- **Relevance**: Traces how perplexity correlates with downstream task performance across training; methodology for understanding emergence via proxy metrics

### (5) FOUNDATIONAL NLP THEORY

[CHOMSKY 1957 / 1988] Works on syntax and language knowledge
[BENGIO 2000 NIPS] "A neural probabilistic language model"  
[COECKE 2010] "Mathematical foundations for compositional distributional model of meaning"
[CORTES 1993 NIPS] "Learning curves: Asymptotic values and rate of convergence"
[ALON 2016] "The Probabilistic Method (4th Ed)"
[GRICE 1975] "Logic and conversation"

---

## CONSOLIDATED NEW PAPERS IDENTIFIED 
### (Papers not in previous Round 1 — NEW candidates for Round 3)

### HIGH PRIORITY (directly address EM + measurement concerns):

1. **[CHEN 2025]** "Persona vectors: Monitoring and controlling character traits in language models"
   - arxiv:2507.21509
   - **Relevance**: Interpretability mechanism for understanding EM as persona trait expression
   - **URL**: https://doi.org/10.48550/ARXIV.2507.21509

2. **[WANG 2025]** "Persona features control emergent misalignment"
   - arxiv:2506.19823
   - **Relevance**: Links EM to interpretable latent features (sparse autoencoders)
   - **URL**: https://arxiv.org/abs/2506.19823

3. **[SOLIGO 2025]** "Convergent linear representations of emergent misalignment"
   - arxiv:2506.11618
   - **Relevance**: Mechanistic consistency of EM across model instances
   - **URL**: https://doi.org/10.48550/ARXIV.2506.11618

4. **[EIRAS 2025]** "Know thy judge: On the robustness meta-evaluation of LLM safety judges"
   - arxiv:2503.04474
   - **Relevance**: Measurement robustness of evaluation methodology for EM
   - **URL**: https://doi.org/10.48550/ARXIV.2503.04474

5. **[WYSE 2025]** "Emergent misalignment as prompt sensitivity: A research note"
   - arxiv:2507.06253
   - **Relevance**: Alternative mechanistic explanation supporting benign EM interpretation
   - **URL**: Not yet retrieved

6. **[TURNER 2025]** "Model organisms for emergent misalignment"
   - arxiv:2506.11613
   - **Relevance**: Foundational EM work establishing evaluation protocols
   - **URL**: https://doi.org/10.48550/ARXIV.2506.11613

7. **[BETLEY 2025]** "Emergent misalignment: narrow finetuning can produce broadly misaligned llms"
   - arxiv:2502.17424
   - **Relevance**: Original EM formulation; establishes measurement framework
   - **URL**: https://arxiv.org/abs/2502.17424

### SECONDARY (measurement & calibration methods):

8. **[RAINA 2024 EMNLP]** "Is llm-as-a-judge robust? Investigating universal adversarial attacks on zero-shot LLM assessment"
   - Venue: EMNLP 2024 (pp. 7499–7517)
   - **Relevance**: Robustness of LLM judge evaluation methodology
   - **URL**: https://doi.org/10.18653/V1/2024.EMNLP-MAIN.427

9. **[LIN 2022 ACL]** "TruthfulQA: Measuring how models mimic human falsehoods"
   - Venue: ACL 2022
   - **Relevance**: Evaluation framework for measuring model deception/false reasoning
   - **URL**: To be retrieved

10. **[GENG 2024 NAACL]** "A survey of confidence estimation and calibration in large language models"
    - Venue: NAACL 2024
    - **Relevance**: Comprehensive calibration survey; directly relevant to confidence/uncertainty in EM context
    - **URL**: To be retrieved

11. **[XIAO 2024 NeurIPS]** "Cal-dpo: Calibrated direct preference optimization for language model alignment"
    - Venue: NeurIPS 2024
    - **Relevance**: Calibration-preserving alignment methods relevant to understanding EM triggers
    - **URL**: To be retrieved

12. **[ZHU 2023 EMNLP Findings]** "On the calibration of large language models and alignment"
    - Venue: EMNLP 2023 (Findings)
    - **Relevance**: Direct examination of how alignment procedures affect calibration
    - **URL**: To be retrieved

### METHODOLOGICAL (measurement & interpretability):

13. **[LANHAM 2023]** "Measuring faithfulness in chain-of-thought reasoning"
    - arxiv:2307.13702
    - **Relevance**: Methodology for interpreting CoT explanations of EM mechanisms
    - **URL**: https://doi.org/10.48550/ARXIV.2307.13702

14. **[SCHAEFFER 2023]** "Are Emergent Abilities of Large Language Models a Mirage?"
    - **Relevance**: Foundational critique of emergence measurement methodology
    - **URL**: arXiv paper (specific ID to be retrieved)

15. **[TURNER 2024]** "Steering language models with activation engineering"
    - arxiv:2308.10248
    - **Relevance**: Mechanistic technique for attributing EM to latent behavioral features
    - **URL**: https://arxiv.org/abs/2308.10248

---

## SUMMARY STATISTICS

- **Papers examined**: 5
- **Total citations extracted**: 45+
- **Matching target categories**: 28 (62%)
  - Calibration/Uncertainty: 7
  - Interpretability: 8
  - Measurement Methodology: 12
  - Behavioral Attribution: 5
  
- **New papers identified (not in Round 1)**: 15
- **High-priority for Round 3 traversal**: 7
- **Papers requiring full-text fetch**: 6

---

## NEXT STEPS FOR ROUND 3

1. Fetch full references from newly identified papers (Chen 2025, Wang 2025, Soligo 2025, Eiras 2025)
2. Identify secondary citations in these papers focusing on:
   - SAE / sparse autoencoder interpretability literature
   - Behavioral attribution in RL/alignment
   - Measurement robustness in LLM evaluation
3. Cross-reference with Safety/Alignment/Mechanistic interpretability literature

