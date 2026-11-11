# Online learning when users also learn or change

**Question:** Which bandit and reinforcement learning work models users whose tastes change or who learn, and what does it find about regret, welfare and manipulation?

## Short answer
**Answer:** Five strands study this, from satiation bandits to long-horizon reinforcement learning (RL). Satiation and boredom bandits model taste loss, and rising and rotting bandits model rewards that change with use. Learning-user, preference-shaping and long-horizon models study users who change while being recommended to. Regret is often easy to keep low, but user welfare and manipulation are harder to control.

**Strength:** Medium (mostly theory and simulations, with few tests on real user data)
- **Holds when:** The user's taste model is known or learnable → simple policies keep regret low (Dean 2022, Zhou 2021).
- **Does not hold when:** Tastes drift toward what is recommended → welfare and stationarity need explicit design (Dean 2022, Carroll 2022).
- **Still unknown:** Whether the satiation and learning models fit real users well, measured on real logs.

## Background
Most online learning theory assumes that a user's reward for an item stays fixed. Recommenders break this assumption. Repeated exposure can tire users, and early use can teach users what they like. The field asks how such changes affect regret, the standard measure of lost reward, and user welfare.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Bandit | A decision problem where each action gives an uncertain reward, and the learner must balance trying and using. |
| Regret | Reward lost compared with always picking the best action in hindsight. |
| Satiation | Reward for an item falls after repeated consumption. |
| Rested bandit | A bandit whose arm rewards change only when the arm is pulled. |
| Rising or rotting bandit | A rested bandit whose rewards increase (rising) or decrease (rotting) with pulls. |
| Preference shaping | Actions that move user tastes toward some target content or opinion. |
| Stationarity | A state where user preferences stop changing over time. |
| Welfare | Long-run benefit to users, which can differ from engagement or reward. |
| MDP | Markov decision process, a model of states, actions and rewards over time. |
| RL | Reinforcement learning, learning a policy from rewards through interaction. |
| Long-horizon RL | RL that optimizes total reward over many sessions, not one step. |
| Myopic | Optimizing only the next reward, with no regard for later effects. |
| REINFORCE | A policy-gradient RL method that adjusts action probabilities by reward. |
| Off-policy correction | A fix for learning from logs made by an older policy. |
| UCB | Upper confidence bound, an exploration rule that favors uncertain actions. |
| Thompson sampling | An exploration rule that samples a plausible model and acts on it. |
| Explore-then-commit | Explore for a fixed period, then keep the best action found. |
| CTR | Click-through rate, the share of shown items that get clicked. |
| Polarization | Users' tastes split toward opposite extremes. |
| Feedback loop | A system where its outputs change the data that trains it. |
| NP-hard | Computationally intractable in general, so exact solutions are impractical. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Satiation bandits | Repeated pulls lower reward, rest restores it | Leqi 2021, Laforgue 2021, Warlop 2018 | Emerging |
| Departing users | Dissatisfied users leave, so policy controls session length | Ben-Porat 2022 | Emerging |
| Rising and rotting bandits | Rewards rise or fall with use, regret bounds differ | Fiandri 2024 | Emerging |
| Learning users | Users learn their own utilities from experience | Yao 2022a, Yao 2022b | Emerging |
| Preference dynamics | Consumed content moves tastes toward or away from it | Dean 2022, Lankireddy 2024 | Emerging |
| Preference shaping | The platform aims to move tastes to a target | Nadkarni 2024, Zhou 2021 | Emerging |
| Long-horizon RL | RL optimizes long-run engagement in industry systems | Chen 2019, Maystre 2023, Mazoure 2021 | Contested |
| Shift penalties | Penalize recommendations that move tastes too far | Carroll 2022, Chee 2024 | Emerging |

## What the evidence shows
### Finding 1: Repeated use lowers reward, so greedy play can fail.
- **Leqi 2021** (Leqi et al., 2021): Reward falls with pulls and recovers at rest → greedy play is optimal only for identical, deterministic arms.
- **Warlop 2018** (Warlop et al., 2018): Boredom as a Markov decision process → a regret bound that ignores the number of states.
- **Laforgue 2021** (Laforgue et al., 2021): Reward depends on time since last switch → regret bound against an intractable optimal policy.
- **Strength:** Medium. Theory with proofs, a few synthetic experiments. No replication on real logs.

### Finding 2: Rising rewards can make naive learning fail.
- **Fiandri 2024** (Fiandri et al., 2024): Rewards increase with pulls → lower bounds, and an algorithm with about T^(2/3) regret under conditions.
- Search snippets report that even identical rising arms can cause linear regret with even splitting. The source was not read in full.
- **Strength:** Medium. One preprint with lower bounds and a proposed algorithm. Results depend on stated conditions.

### Finding 3: When users learn, regret depends on how fast they learn.
- **Yao 2022a** (Yao et al., 2022): Users learn utilities from experience → regret grows as user learning slows, and becomes linear if learning never converges.
- **Yao 2022b** (Yao et al., 2022): A companion paper on users who explore. Read from its search snippet only.
- **Strength:** Medium. Synthetic experiments only. The bounds were not read directly.

### Finding 4: Regret is easy to keep low, but welfare is harder.
- **Dean 2022** (Dean and Morgenstern, 2022): Preferences move toward consumed content → simple policies keep regret constant, but stationarity needs design.
- **Nadkarni 2024** (Nadkarni et al., 2024): Rewards reinforce tastes → logarithmic regret for shaping toward a target arm.
- **Zhou 2021** (Zhou et al., 2021): Platform pays users to pull arms → logarithmic regret and payment. Sublinear regret and payment are impossible in some cases.
- **Lankireddy 2024** (Lankireddy et al., 2024): Exploiting more polarizes tastes → theory only, no experiments.
- **Strength:** Medium. Several theory papers agree on the direction. None measure welfare on real users.

### Finding 5: Long-horizon RL is used in industry, and manipulation is a known risk.
- **Chen 2019** (Chen et al., 2019): Production REINFORCE with off-policy correction for slates → live gains reported in a secondary source only.
- **Maystre 2023** (Maystre et al., 2023): Podcast recommender for long journeys → A/B gains reported, no effect size in the abstract.
- **Mazoure 2021** (Mazoure et al., 2021): Short-horizon RL with a termination bonus → beats myopic baselines on four tasks.
- **Carroll 2022** (Carroll et al., 2022): Learned user model plus a trust region on shifts → avoids manipulation in simulation. Notes that myopic recommenders also shift preferences.
- **Evans 2021** (Evans and Kasirzadeh, 2021): Simulated Q-learning agent polarizes users early → argues that media recommenders built only with RL are unsafe or unviable.
- **Strength:** Low to Medium. Industry claims are not replicated independently, and simulations are toy environments.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does long-term optimization help users? | Maystre 2023 and Mazoure 2021 report gains | Snippets say tuned myopic baselines can be nearly optimal | Same-metric comparison on real logs with tuned baselines |
| Is user change learning or drift? | Yao 2022a: change is learning that converges | Dean 2022: change is drift toward consumed content | Real data showing which model fits user trajectories |
| Does exploitation polarize users? | Lankireddy 2024: yes, exploitation polarizes | Dean 2022: personalization collapses, randomization does not | Experiments comparing policies on the same user model |
| Is a penalty enough? | Carroll 2022: a shift penalty helps in simulation | Chee 2024: harm penalties do nothing if dynamics are ignored | Tests of penalties with a fitted dynamics model |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Satiation, learning users and long-run RL in one model | Real users do all three, so a combined model could shift conclusions | Dean 2022 (dynamics), Yao 2022a (learning) |
| Real-data tests of preference change | Simulated tastes may not match real drift | Chee 2024 (semi-synthetic movies) |
| Myopic versus long-horizon policies on taste change | Tells whether long-term objectives are worth their risk | Carroll 2022 (simulation only) |
| Welfare results for two-sided learning | Regret measures the platform, not the user | Yao 2022a (platform regret only) |
| Satiation models for user states, not content arms | Users, not items, are what tire | Leqi 2021 (arms only) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Leqi 2021 | **Rebounding Bandits for Modeling Satiation Effects** | 2021 | NeurIPS | abstract (summarized) |
| Laforgue 2021 | **A Last Switch Dependent Analysis of Satiation and Seasonality in Bandits** | 2021 | arXiv preprint | abstract (summarized) |
| Warlop 2018 | **Fighting Boredom in Recommender Systems with Linear Reinforcement Learning** | 2018 | NeurIPS | search snippet |
| Ben-Porat 2022 | **Modeling Attrition in Recommender Systems with Departing Bandits** | 2022 | AAAI | search snippet |
| Fiandri 2024 | **Rising Rested Bandits: Lower Bounds and Efficient Algorithms** | 2024 | arXiv preprint | abstract (summarized) |
| Yao 2022a | **Learning from a Learning User for Optimal Recommendations** | 2022 | ICML | abstract (summarized) |
| Yao 2022b | **Learning the Optimal Recommendation from Explorative Users** | 2022 | AAAI | search snippet |
| Dean 2022 | **Preference Dynamics Under Personalized Recommendations** | 2022 | EC | abstract (summarized) |
| Nadkarni 2024 | **Influencing Bandits: Arm Selection for Preference Shaping** | 2024 | arXiv preprint | abstract (summarized) |
| Lankireddy 2024 | **Influence of Recommender Systems on Users: A Dynamical Systems Analysis** | 2024 | arXiv preprint | abstract (summarized) |
| Zhou 2021 | **Incentivized Bandit Learning with Self-Reinforcing User Preferences** | 2021 | ICML | search snippet and abstract |
| Chee 2024 | **Harm Mitigation in Recommender Systems under User Preference Dynamics** | 2024 | KDD | search snippet |
| Chen 2019 | **Top-K Off-Policy Correction for a REINFORCE Recommender System** | 2019 | arXiv preprint (WSDM reported) | abstract (summarized) |
| Maystre 2023 | **Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective** | 2023 | arXiv preprint | abstract (summarized) |
| Mazoure 2021 | **Improving Long-Term Metrics in Recommendation Systems using Short-Horizon Reinforcement Learning** | 2021 | arXiv preprint | abstract (summarized) |
| Carroll 2022 | **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** | 2022 | ICML | search snippet |
| Evans 2021 | **User Tampering in Reinforcement Learning Recommender Systems** | 2021 | FAccTRec workshop, AIES 2023 | search snippet |
| Jiang 2019 | **Degenerate Feedback Loops in Recommender Systems** | 2019 | AIES | search snippet |
| Mansoury 2020 | **Feedback Loop and Bias Amplification in Recommender Systems** | 2020 | CIKM | search snippet |
| Carroll 2024 | **AI Alignment with Changing and Influenceable Reward Functions** | 2024 | ICML | search snippet |

<details><summary>Original research question</summary>

What online-learning / bandit / reinforcement-learning work studies personalization when the user's preferences evolve or the user is also learning — e.g. bandits with satiation or boredom, rising/rotting bandits, recommending to learning or strategic users, two-sided learning, users who explore, long-term-value RL in recommenders (e.g. YouTube REINFORCE, long-term engagement objectives) — and what regret or welfare results and failure modes (manipulation of preferences, myopia) do they find?

</details>
