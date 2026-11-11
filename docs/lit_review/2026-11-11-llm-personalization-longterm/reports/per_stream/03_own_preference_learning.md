# How consumers learn their own preferences

**Question:** How do consumers learn or form their own tastes over time, and how do advisors or AI systems change that process?

## Short answer
**Answer:** Three model types describe how consumers learn their own tastes: Bayesian learning from use, preferences built at choice time, and habit formation. Recommenders and AI assistants move stated preferences in lab studies. Formal models show how this can lock in beliefs, but the AI evidence covers opinions more than product tastes.

**Strength:** Medium (learning models are well tested, but the AI evidence is small and mostly lab-based or preprint)
- **Holds when:** Recommendations show a rating or price in lab or online settings → ratings and willingness to pay move toward it.
- **Does not hold when:** Stated preferences are measured next to purchases → the aggregate learning effect shrinks a lot.
- **Still unknown:** Whether AI assistants shift consumers' product tastes over months of real use.

## Background
Consumers often cannot judge a product until they use it. Their tastes may also form or shift as they use products or hear advice. Recommenders and AI assistants change what consumers see, and so can change what they come to value. This matters for long-run personalization, because a system that shapes tastes also shapes the data it learns from.

Key terms used on this page:
| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Experience good | A product whose quality a buyer learns only by using it. |
| Bayesian learning | Updating beliefs after each new signal, using Bayes' rule. |
| Habit formation | Past use raises the taste for the same product over time. |
| State dependence | Past choice affects current choice, for example through habit. |
| Preference construction | Preferences are formed at choice time, not stored in advance. |
| Anchoring | An early number, such as a rating, pulls later judgments toward it. |
| Willingness to pay | The highest price a buyer would accept for an item. |
| Persuasion | A sender chooses what information a receiver sees, to shape beliefs. |
| Lock-in | A feedback loop that keeps beliefs or choices on one path. |
| Sycophancy | An AI model agrees with the user's views to please the user. |
| Structural model | A model that estimates the choice rule behind observed purchases. |
| Consumer panel | A fixed group of households whose purchases are tracked over time. |
| Reinforcement learning | Training a model from rewards gained through interaction. |
| Multi-turn | A conversation with several exchanges, not one prompt. |
| Simulated users | Software stand-ins for people, used to test a system before use. |
| MovieLens | An online movie-rating site used as a research testbed. |
| Trust region | A limit on how far a system may move users from their natural drift. |
| Preregistered | Study plan fixed and public before data collection starts. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Structural learning models | Consumers learn brand and attribute beliefs from use and ads. | Erdem and Keane (1996), Ching et al. (2013), Ackerberg (2003) | Established |
| Learning versus taste tests | Stated preferences separate learning from fixed tastes. | Shin et al. (2012), Heckman (1981) | Contested |
| Constructed preferences | Preferences are built during choice and depend on context. | Lichtenstein and Slovic (2006), Bettman et al. (1998), Atas et al. (2021) | Established |
| Recommender effects in the lab | A displayed prediction anchors ratings and willingness to pay. | Cosley et al. (2003), Adomavicius et al. (2013, 2018) | Emerging |
| Learning-aware recommenders | Recommend items that speed up the user's own learning. | Dzyabura and Hauser (2019), Kremer et al. (2014) | Emerging |
| Formal models of induced shift | Estimate and bound how a system moves user preferences. | Carroll et al. (2022, 2024), Qiu et al. (2025) | Emerging |
| LLM persuasion experiments | Measure how AI dialogue moves opinions and choices. | Jakesch et al. (2023), Salvi et al. (2025), Werner et al. (2024) | Emerging |

## What the evidence shows
### Finding 1: Consumers learn brand beliefs from use, but learning effects may be overstated.
- **Erdem and Keane (1996)**: Modeled brand choice with Bayesian updating from use and ad signals → fit scanner data better than ad hoc smoothing.
- **Ackerberg (2003)**: Yogurt panel with advertising → advertising mainly informed buyers, with smaller image effects.
- **Shin, Misra and Horsky (2012)**: Added survey-measured stated preferences to purchase data → the aggregate learning effect became much weaker.
- **Strength:** Medium. Many structural studies over decades, but separating learning from fixed tastes is disputed.

### Finding 2: Preferences are often built at choice time, so context changes them.
- **Lichtenstein and Slovic (2006)**: Reviewed many experiments → elicited preferences shift with how the choice is framed.
- **Bettman, Luce and Payne (1998)**: Choice strategies change with task and context → the same person can prefer different options.
- **Atas et al. (2021)**: Survey linking construction and cognitive biases to recommender design → anchoring and framing are named design risks.
- **Strength:** Medium. Lab consensus is strong, but few studies track long-run tastes in the field.

### Finding 3: In lab studies, a recommendation moves ratings and willingness to pay toward its value.
- **Cosley et al. (2003)**: MovieLens users rated toward a shown prediction, even when wrong → some detected manipulation.
- **Adomavicius et al. (2013)**: Three lab studies on television shows → the recommendation anchored the viewer's rating.
- **Adomavicius et al. (2018)**: Random song recommendations moved willingness to pay → the shift held after forced sampling.
- **Strength:** Medium. Three papers agree, but one research group ran them, all in the lab. A secondary summary reports 10 to 15 percent per star.

### Finding 4: Recommenders change how consumers search, and can speed or slow their learning.
- **Dellaert and Häubl (2012)**: Three studies → recommendations shift search toward choosing among products already seen.
- **Häubl and Trifts (2000)**: Controlled online store experiment → recommendation agents produced smaller, higher-quality consideration sets.
- **Dzyabura and Hauser (2019)**: Simulations and a limited empirical test → recommendations that account for weight learning help novices most.
- **Strength:** Medium. Controlled experiments support the search effects. The learning-aware design rests on simulations.

### Finding 5: Formal models show an advisor can induce preference shifts. Lock-in for tastes is not yet measured.
- **Carroll et al. (2022)**: Learned user-dynamics model, tested in simulation → penalizing shifts outside a trust region keeps engagement without manipulation.
- **Carroll et al. (2024)**: Dynamic reward model of changing preferences → each of eight alignment notions carries a risk.
- **Qiu et al. (2025)**: Bayesian feedback model with GPT usage data → predicts lock-in when a feedback strength passes a threshold.
- **Armstrong and Mindermann (2018)**: Formal proof → behavior alone cannot uniquely separate preferences from irrationality.
- **Strength:** Low. Theory and simulations only, and none is fitted to real consumer tastes.

### Finding 6: LLM assistants shift opinions in controlled studies. Evidence on product tastes is thin.
- **Jakesch et al. (2023)**: 1,506 people co-wrote with a biased assistant → their writing and later attitudes moved toward it, mostly unnoticed.
- **Salvi et al. (2025)**: Preregistered debates → personalized GPT-4 was more persuasive than humans in 64.4 percent of unequal pairs.
- **Hackenburg et al. (2025)**: 76,977 participants and 19 models → persuasion training raised persuasiveness by up to 51 percent and lowered accuracy.
- **Jiang et al. (2025, preprint)**: 266 people in multi-turn talks → human opinions barely moved, while model outputs did.
- **Werner et al. (2024, preprint)**: One session of product choice → the assistant's steering changed choices.
- **Strength:** Medium for opinions, from large controlled studies. Low for product tastes, from one session or a preprint.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Does learning drive brand choice? | Learning explains the dynamics: Erdem and Keane (1996), Ching et al. (2013). | Stated preferences show learning is overstated: Shin et al. (2012). | Panels with repeated belief and preference measures. |
| Do humans or AI move more? | Humans shift: Jakesch et al. (2023), Salvi et al. (2025). | Humans barely shift: Jiang et al. (2025, preprint). | Preregistered multi-turn study with matched controls and follow-up. |
| Is an induced shift harmful? | Natural drift is safe, excess is not: Carroll et al. (2022). | Any split of norms is an assumption: Armstrong and Mindermann (2018). | Measures of user welfare after the shifts. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| No real-use study of product tastes over months with an LLM. | Lock-in claims need long-run data. | Werner et al. (2024), one session. |
| Learning models not fitted to LLM dialogue data. | Would separate learning from steering. | Dzyabura and Hauser (2019). |
| No method to separate learning from preference change in logs. | Recommender logs mix both effects. | Shin et al. (2012), which uses survey data. |
| Lock-in studied for beliefs, not tastes. | Tastes matter most for welfare. | Qiu et al. (2025). |
| No welfare test of which shifts harm users. | Needed to set design rules. | Carroll et al. (2022). |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Erdem and Keane (1996) | **Decision-Making Under Uncertainty: Capturing Dynamic Brand Choice Processes in Turbulent Consumer Goods Markets** | 1996 | Marketing Science | Abstract and summary |
| Ching et al. (2013) | **Learning Models: An Assessment of Progress, Challenges, and New Developments** | 2013 | Marketing Science | Abstract and working-paper summary |
| Ackerberg (2003) | **Advertising, Learning, and Consumer Choice in Experience Good Markets: An Empirical Examination** | 2003 | International Economic Review | Abstract |
| Shin et al. (2012) | **Disentangling Preferences and Learning in Brand Choice Models** | 2012 | Marketing Science | Summary |
| Heckman (1981) | **Heterogeneity and State Dependence** | 1981 | Book chapter | Catalog record only |
| Lichtenstein and Slovic (2006) | **The Construction of Preference** | 2006 | Book, Cambridge University Press | Catalog record only |
| Bettman et al. (1998) | **Constructive Consumer Choice Processes** | 1998 | Journal of Consumer Research | Catalog record only |
| Atas et al. (2021) | **Towards psychology-aware preference construction in recommender systems: Overview and research issues** | 2021 | Journal of Intelligent Information Systems | Abstract |
| Cosley et al. (2003) | **Is seeing believing? How recommender system interfaces affect users' opinions** | 2003 | CHI conference | Summary |
| Adomavicius et al. (2013) | **Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects** | 2013 | Information Systems Research | Summary |
| Adomavicius et al. (2018) | **Effects of Online Recommendations on Consumers' Willingness to Pay** | 2018 | Information Systems Research | Summary |
| Dellaert and Häubl (2012) | **Searching in Choice Mode: Consumer Decision Processes in Product Search with Recommendations** | 2012 | Journal of Marketing Research | Summary |
| Häubl and Trifts (2000) | **Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids** | 2000 | Marketing Science | Summary |
| Dzyabura and Hauser (2019) | **Recommending Products When Consumers Learn Their Preference Weights** | 2019 | Marketing Science | Summary |
| Kremer et al. (2014) | **Implementing the "Wisdom of the Crowd"** | 2014 | Journal of Political Economy | Abstract |
| Carroll et al. (2022) | **Estimating and Penalizing Induced Preference Shifts in Recommender Systems** | 2022 | International Conference on Machine Learning | Landing page summary |
| Carroll et al. (2024) | **AI Alignment with Changing and Influenceable Reward Functions** | 2024 | International Conference on Machine Learning | Search summary |
| Qiu et al. (2025) | **The Lock-in Hypothesis: Stagnation by Algorithm** | 2025 | International Conference on Machine Learning | Search summary |
| Armstrong and Mindermann (2018) | **Occam's razor is insufficient to infer the preferences of irrational agents** | 2018 | Neural Information Processing Systems | Search summary |
| Jakesch et al. (2023) | **Co-Writing with Opinionated Language Models Affects Users' Views** | 2023 | CHI conference | Search and press summary |
| Salvi et al. (2025) | **On the conversational persuasiveness of GPT-4** | 2025 | Nature Human Behaviour | Search summary |
| Hackenburg et al. (2025) | **The levers of political persuasion with conversational artificial intelligence** | 2025 | Science | Search summary |
| Jiang et al. (2025) | **Beyond One-Way Influence: Bidirectional Opinion Dynamics in Multi-Turn Human-LLM Interactions** | 2025 | arXiv preprint | Search summary |
| Werner et al. (2024) | **Experimental Evidence That Conversational Artificial Intelligence Can Steer Consumer Behavior Without Detection** | 2024 | arXiv preprint | Search summary |

<details><summary>Original research question</summary>

What models describe how consumers learn or construct their OWN preferences over time (Bayesian learning about own tastes, experience goods, constructed/endogenous preferences, habit formation, acquired tastes, preference discovery), and which papers model how an external advisor, recommender or AI system changes that learning process (e.g. users' inference from recommendations, inversion problem between behavior and utility, learning-induced lock-in)? Include empirical evidence on preference malleability from recommendations.

</details>
