# Theory of recommender feedback loops and preference shift

**Question:** Which theory models explain how recommenders and user preferences shape each other over time, and what do these models predict?

## Short answer
**Answer:** Four model families describe this loop. Preference-drift models show that recommended content can pull tastes toward itself. Kalimeris et al. (2021) find that the concentration keeps growing and never settles.

**Strength:** Medium (most results come from simulations or stylized models, and few have been tested on real platforms)
- **Holds when:** users follow recommendations and drift toward them → concentration grows, with no fixed point (Kalimeris 2021).
- **Does not hold when:** users choose freely and rarely pick extreme niche items → the drift can reverse (Ribeiro 2023).
- **Still unknown:** whether these loops appear at scale on real platforms with learning users. Large feed experiments found small or null polarization effects (Guess 2023 and Nyhan 2023).

## Background
A recommender chooses what a user sees. What a user sees can change what that user later wants. Over time, this can narrow tastes, split groups apart, or make many users look alike. Researchers have built models to predict these outcomes because they affect platform design and public policy.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Feedback loop | A cycle where a system's output changes the data that train its next output. |
| Preference drift | A slow change in what a user likes, caused by what the user sees. |
| Fixed point | A state that stays the same after one more round of the loop. |
| Amplification | A growing concentration of recommended content around one topic or type. |
| Filter bubble | A narrow set of content a user sees, which limits exposure to other views. |
| Degenerate loop | A feedback loop that drives user interests to an extreme and keeps them there. |
| Performative prediction | A prediction that changes the outcome it forecasts, so the data shift after deployment. |
| Induced preference shift | A change in user preferences that the recommender causes on purpose or as a side effect. |
| Stationarity | A condition where a user's preferences stay roughly unchanged over time. |
| Regret | The gap between the reward a policy earns and the reward of the best policy. |
| Homogenization | Users or outputs become more alike over time. |
| Monoculture | Many decision-makers use the same algorithm, so their decisions become similar. |
| Matrix factorization | A method that scores user-item pairs with low-rank user and item vectors. |
| Softmax parameter (beta) | A setting that controls how often the top-scored item is picked. Higher beta means less randomness. |
| Attractor | A state that many trajectories move toward and stay near. |
| Confounding | A bias where past recommendations shape the data used to learn user tastes. |
| Creator | A content producer who competes for user attention on a platform. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Preference drift | Users move toward items they are shown, and the system follows | Kalimeris 2021, Dean 2022, Carroll 2022 | Emerging (few papers, recent) |
| Degenerate dynamics | User interests move to extremes under a feedback loop | Jiang 2019 | Emerging (few papers, recent) |
| Performative prediction | A deployed model changes the data it learns from | Perdomo 2020, Mendler-Dünner 2020, Hardt 2025 | Established (replicated, several groups) |
| Homogenization in simulation | Recommenders trained on their own output make users more alike | Chaney 2018 and Mansoury 2020 | Established (replicated, several groups) |
| Monoculture and welfare | Shared algorithms can lower total welfare | Kleinberg 2021 | Established (replicated, several groups) |
| Creator equilibria | Creators compete for attention under a ranking rule | Hron 2023 and Eilat 2023 | Emerging (few papers, recent) |

## What the evidence shows
### Finding 1: Recommended content can pull user tastes toward itself.
- **Kalimeris 2021**: Matrix-factorization model where users drift toward recommended items, and the authors report no fixed point under mild drift. Higher beta, meaning less randomness, amplifies more.
- **Dean 2022**: Biased-assimilation model, where tastes move toward liked content. Standard reward maximization is nearly trivial, and simple policies have constant regret.
- **Carroll 2022**: Simulated long-horizon recommenders → engagement-maximizing policies pull preferences toward a few attractor points.
- **Strength:** Medium. The models are stylized and the key fixed-point result is from a research-blog summary of the full paper. The Dean and Morgenstern and Carroll results come from abstracts and simulations.

### Finding 2: A designer can hold tastes steady if the designer knows them.
- **Dean 2022**: With known starting tastes and a rich content set, a policy keeps tastes roughly stationary. Its regret grows only logarithmically with time.
- **Randomization**: Random recommendations also keep tastes stationary (Dean 2022).
- **Carroll 2022**: A user model learned from logs predicts how a new recommender shifts tastes. The authors penalize shifts outside a trust region of natural drift.
- **Strength:** Medium. The Dean and Morgenstern result is a proof under stated conditions. The Carroll result is shown in simulation only.

### Finding 3: Feedback loops can narrow user interests and lower utility for minority tastes.
- **Jiang 2019**: Dynamical model of user interests → sufficient conditions make the system degenerate. Continuous random exploration and a candidate pool that grows at least linearly slow degeneration.
- **Chaney 2018**: Simulated recommender trained on its own confounded data → behavior homogenizes, and users with minority tastes lose utility.
- **Strength:** Medium. Both results depend on the simulated setup. The T-RECS framework reran the Chaney setup with 400 trials per model, and the homogenization result held.

### Finding 4: Performative prediction gives conditions for retraining to converge.
- **Perdomo 2020**: Gives necessary and sufficient conditions for repeated retraining to reach a performatively stable point with near-minimal loss. The framework subsumes strategic classification.
- **Mendler-Dünner 2020**: Stochastic optimization version, where each deployed model shifts the data distribution.
- **Strength:** High for the theory (peer-reviewed proofs). Low for recommenders, because the framework models a predictor that changes outcomes, not a user who learns tastes.

### Finding 5: Shared algorithms can lower welfare even when each is accurate.
- **Kleinberg 2021**: When many decision-makers use one accurate algorithm, total welfare can fall. The authors model hiring and screening, not recommenders.
- **Strength:** High for the result in its setting (peer-reviewed, Proceedings of the National Academy of Sciences). Low for recommenders, because the mechanism is only an analogy there.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does a recommender amplify tastes? | Kalimeris 2021: drift grows and never settles | Ribeiro 2023: users who choose freely pull back | Logs with user choice and measured taste drift |
| Do feed changes shift polarization? | Guess 2023 and Nyhan 2023: little or no effect in three months | Garcia commentary: short, single-election studies cannot rule out a cause | Longer, multi-platform experiments with taste measures |
| Is stationarity practical? | Dean 2022: yes, if starting tastes are known | Carroll 2022: learn the dynamics from logs instead | A test with unknown tastes and real logs |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| No convergence result with a learning user and a learning system | Predicts long-run tastes and polarization | Dean 2022 (known tastes) and Kalimeris 2021 (no fixed point) |
| Recommender welfare under user drift | Welfare claims rest on hiring or creator models | Kleinberg 2021 (hiring) and Mladenov 2020 (provider model) |
| A direct test of amplification against de-amplification | The two sides predict opposite effects | Kalimeris 2021 vs Ribeiro 2023 |
| Generative systems that write content | Current models assume a fixed item catalog | Hron 2023 (fixed catalog, creators) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Kalimeris 2021 | **Preference Amplification in Recommender Systems** | 2021 | KDD | summary (Meta research blog) |
| Dean 2022 | **Preference Dynamics Under Personalized Recommendations** | 2022 | EC | abstract |
| Carroll 2022 | **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** | 2022 | ICML | abstract |
| Jiang 2019 | **Degenerate Feedback Loops in Recommender Systems** | 2019 | AIES | summary (search excerpts) |
| Perdomo 2020 | **Performative Prediction** | 2020 | ICML | abstract |
| Mendler-Dünner 2020 | **Stochastic Optimization for Performative Prediction** | 2020 | NeurIPS | metadata only |
| Hardt 2025 | **Performative Prediction: Past and Future** | 2025 | Statistical Science | metadata only |
| Chaney 2018 | **How algorithmic confounding in recommendation systems increases homogeneity and decreases utility** | 2018 | RecSys | summary (search excerpts) |
| Mansoury 2020 | **Feedback Loop and Bias Amplification in Recommender Systems** | 2020 | CIKM | metadata only |
| Kleinberg 2021 | **Algorithmic monoculture and social welfare** | 2021 | Proceedings of the National Academy of Sciences | summary (search excerpts) |
| Ribeiro 2023 | **The Amplification Paradox in Recommender Systems** | 2023 | ICWSM | abstract and summary |
| Guess 2023 | **How do social media feed algorithms affect attitudes and behavior in an election campaign?** | 2023 | Science | summary (search excerpts) |
| Nyhan 2023 | **Like-minded sources on Facebook are prevalent but not polarizing** | 2023 | Nature | metadata only |
| Mladenov 2020 | **Optimizing Long-term Social Welfare in Recommender Systems: A Constrained Matching Approach** | 2020 | ICML | summary (search excerpts) |
| Hron 2023 | **Modeling Content Creator Incentives on Algorithm-Curated Platforms** | 2023 | ICLR | summary (arXiv listing) |
| Eilat 2023 | **Performative Recommendation: Diversifying Content via Strategic Incentives** | 2023 | ICML | summary (search excerpts) |
| Piao 2023 | **Human–AI adaptive dynamics drives the emergence of information cocoons** | 2023 | Nature Machine Intelligence | metadata only |

<details><summary>Original research question</summary>

What theoretical models describe the long-run feedback loop between a personalization system (recommender, search ranker) and user preferences — e.g. preference amplification, filter bubbles, degenerate feedback loops, performative prediction, induced preference shift — and what do they predict about polarization, homogenization, welfare and convergence? Include key results (fixed points, conditions for drift) and which assumptions drive them.

</details>
