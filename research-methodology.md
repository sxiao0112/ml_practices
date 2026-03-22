# Research Methodology Practices

Lessons for conducting research with AI agents — literature review, critical analysis,
and research direction planning. Complements experiment-practices.md (running experiments)
and pipeline-architecture.md (code architecture).

---

## 1. Agent Instruction Iteration

When designing agent tasks (lit review, paper extraction, analysis), iterate the
instructions before scaling:

1. **Design** the schema/instructions
2. **Test on 1 example** where you already know the answer
3. **Compare** agent output to ground truth — identify systematic errors
4. **Fix instructions** to address each error type
5. **Re-test** on the same example until clean
6. **Test on 2-3 diverse examples** (different paper types, domains)
7. **Then batch** the remaining work

Common instruction failure modes:
- Agent guesses when it should say "not_reported"
- Agent interpolates ranges instead of listing exact values
- Agent confuses what the paper does vs what the paper studies
- Agent defaults to a value instead of searching the paper text
- Temporal reasoning errors (paper A can't build on paper B if B is newer)

Each failure mode becomes an explicit rule in the instructions. The instructions
grow by accumulating specific fixes — not by adding general advice.

**Anti-pattern:** Writing perfect-sounding instructions once and launching 30 agents.
The first agent reveals 5 systematic errors, but you've already wasted 29 runs.

## 2. Structured Paper Extraction: Link Claims to Experiments

When extracting technical details from papers, the fundamental unit is the
**experiment**, not the paper. A paper is a collection of claims, each supported
by specific experiments.

Structure:
```
claims:
  - claim: "X achieves Y"
    evidence: [experiment_ids]
    caveats: "only tested on Z"

experiments:
  - id: "e1"
    models: [exact names]
    intervention: {type, target, layers, hyperparams}
    dataset: {name, origin, size}
    evaluation: {method, judge, criteria}
    result: "specific number"
    figure: "Figure 4a"
```

This prevents the common failure of citing a paper's claim without knowing:
- Which models it was tested on (generalizability)
- What evaluation method was used (teacher-forcing inflation?)
- How many seeds/runs (reliability)
- What the exact decision criteria were (reproducibility)

A reusable YAML schema and agent instructions for this are in
[templates/methods-card/](templates/methods-card/).

## 3. External Adversarial Review

Before committing to a research direction, send your analysis to a different
model/perspective for critique. Use Codex MCP with GPT-5.4:

```
mcp__codex__codex with model="gpt-5.4"
```

### What to include in the prompt
- Full context from the lit review (key findings with arXiv IDs and evidential status)
- The specific proposal/analysis being critiqued
- Self-identified weaknesses (shows good faith, gets more targeted critique)
- Explicit questions that invite pushback

### Prompt patterns that work
- "Does experiment X actually provide evidence for hypothesis Y, or is it confounded by Z?"
- "Is my hierarchy ordering defensible? Which levels am I overconfident about?"
- "What experimental controls would make this decisive vs hand-wavy?"
- "What alternative directions would YOU suggest given this landscape?"

### Key lesson: sufficiency ≠ mediation
Showing that X produces Y (sufficiency) is NOT the same as showing that
interventions cause Y *through* X (mediation). Mediation requires:
1. Show T increases M (intervention activates candidate mediator)
2. Block M during T, show harmful effect disappears (necessity)
3. Show intended effect of T survives blocking M (specificity)
4. Apply M alone, show it partially recapitulates the harm (sufficiency)
5. Repeat across intervention types (generality)

This distinction is the #1 thing external critique catches that self-review
misses.

## 4. Evidential Hierarchy

When building arguments across papers, classify each finding by evidential
strength before using it as a premise:

| Level | Meaning | Trust |
|-------|---------|-------|
| Analytically proven | Formal mathematical proof | High — check assumptions |
| Demonstrated empirically | Tested across models/datasets with controls | Medium-high — check generalizability |
| Suggested | Single-setting observation or limited testing | Medium — needs replication |
| Proposed | Theoretical framework without validation | Low — treat as hypothesis |

Do not build load-bearing arguments on "suggested" findings. If your core
claim depends on a single-setting preprint, flag this explicitly.

Also track:
- **Peer review status**: Published (ICML, NeurIPS) > preprint > withdrawn
- **Replication**: Tested on N model families > single model
- **Evaluation method**: Open-ended generation > teacher-forcing (the latter
  inflates results by up to 2.5x in model editing)

## 5. Cross-Paper Contradiction Detection

When synthesizing across papers, explicitly check for contradictions. Common
types:

- **Scope mismatch**: Paper A shows X at one layer, paper B shows ¬X at all
  layers. Not a real contradiction — different scope.
- **Metric mismatch**: Paper A measures success on direct recall, paper B on
  downstream consequences. Both can be "right" simultaneously.
- **Level mismatch**: Paper A works in weight space, paper B in activation space.
  These can give different answers because they're different projections of the
  same phenomenon.
- **Genuine contradiction**: Paper A and B measure the same thing on the same
  level and disagree. Resolve by checking sample size, evaluation method,
  and model family.

The most productive contradictions are ones where two papers make the SAME
measurement but get different results — these reveal hidden confounds or
boundary conditions.

## 6. Cross-Literature Analysis Structure

When synthesizing across a large body of papers, use focused disputes rather
than grand narratives:

### Identify specific disputes
Find points where the literature actually disagrees. For each dispute:
- What's established (not in dispute)
- Competing explanations with best evidence for each
- What evidence would resolve it
- Current assessment

Grand "worldviews" (e.g., "it's all superposition" vs "it's all optimization")
create strawmen. Specific disputes (e.g., "is norm growth cause or symptom of
editing failure?") produce testable predictions.

### Build explanatory hierarchy
Classify findings by depth, but constrain by evidential strength:
- A weakly-evidenced finding should NOT anchor the hierarchy just because it
  sounds fundamental
- Each level should predict: "if this is the bottleneck, then intervention X
  should help and Y should not"
- Without falsifiable predictions, the hierarchy is taxonomy, not theory

### Check "unifications" rigorously
"Three views of one object" claims (e.g., weight-space subspace = activation-space
direction = loss-landscape attractor) require cross-space intervention transfer
to confirm. Co-occurrence is suggestive, not conclusive.

### Map contradictions carefully
Most apparent contradictions are scope/metric/level mismatches:
- Scope: Paper A tested layer 24, Paper B tested all layers
- Metric: Paper A measured direct recall, Paper B measured downstream consequences
- Level: Paper A analyzed weights, Paper B analyzed activations

Only flag as genuine when two papers measure the same thing at the same level
and disagree.

## 7. Separate Description from Explanation

When reviewing a field, keep three levels distinct:

1. **What happens** (established facts): "Sequential editing causes norm growth"
2. **How it happens** (mechanisms): "The L&E update rule has exponential growth"
3. **Why it happens** (root causes): "Feature superposition makes perturbation non-local"

Most papers establish level 1 (empirical observation), some establish level 2
(specific mechanism), and very few establish level 3 (root cause). Do not
upgrade a level-1 finding to level-3 status because it sounds like an
explanation.

Test: could the finding be a symptom of something deeper? If yes, it's not a
root cause. "Norm growth causes editing collapse" could be true, but norm
growth might itself be a symptom of a deeper geometric property. Classify
accordingly.
