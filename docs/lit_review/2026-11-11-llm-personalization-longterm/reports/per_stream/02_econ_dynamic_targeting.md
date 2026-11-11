# Economics of repeated targeting and personalization over time

**Question:** How do repeated targeting and personalization models affect consumer welfare, firm choices, and consumer responses over time?

## Short answer
**Answer:** The main models cover five types of repeated targeting: purchase-history pricing, learning-based pricing, dynamic persuasion, recommenders, and privacy choice. Most models show firms gain from repeated data use, but consumer welfare depends on commitment and competition. One model shows that consumer control over disclosure can guarantee gains for consumers.

**Strength:** Medium (mostly theory models, one field test at one firm, and no multi-period field study).
- **Holds when:** a firm prices on purchase history and consumers cannot control their data → firm profit rises and total consumer surplus falls (Dubé 2023).
- **Holds when:** consumers control their disclosure and sellers compete → consumers can gain (Ali 2023).
- **Does not hold when:** one person's data use exposes others → too much data is shared (Rhodes-Zhou 2024, Acemoglu 2022).
- **Still unknown:** consumer welfare over many purchases in a field test where tastes change.

## Background
Targeting models ask what a firm gains and loses when it learns from each purchase or interaction. Consumers can react by waiting, hiding data, or changing what they buy. These responses matter because repeated data use changes prices, product choice, and privacy over time.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Price discrimination | Charging different buyers different prices for the same product. |
| Behavior-based price discrimination | Charging prices that depend on a customer's past purchases. |
| Commitment | A firm can promise its future prices in advance. |
| Limited commitment | A firm cannot promise its future prices. |
| Ratchet effect | Buyers wait for lower later prices, because a current purchase shapes later offers. |
| Strategic consumer | A buyer who waits or hides information to get a better deal. |
| Consumer surplus | The buyer's gain: what they value minus what they pay. |
| Externality | An effect of one person's choice on others who do not choose. |
| Social learning | People learn from what other people chose or reported. |
| Markov perfect equilibrium | A stable outcome where each player's plan depends only on the current state. |
| Equilibrium refinement | A rule that removes implausible outcomes from a model. |
| Information design | Choosing what information to reveal, to shape other people's choices. |
| Bayesian persuasion | A sender picks signals that change a receiver's beliefs, to gain. |
| Dynamic persuasion | A sender reveals information over time to change a receiver's beliefs. |
| Recommender system | Software that suggests products or content to users. |
| Field test | A randomized test run in a real market with real customers. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Repeated price discrimination | Prices depend on past purchases, and buyers can wait | Dubé 2023, Villas-Boas 2004, Esteves 2017 | Contested |
| Learning-based pricing | Buyers and sellers learn product values through purchases | Bergemann-Välimäki 1996, Bergemann-Välimäki 2000, Papanastasiou-Savva 2017 | Established |
| Dynamic persuasion | A sender reveals signals over time to shape beliefs | Ely 2017, Che-Kim 2023, Orlov 2020 | Emerging |
| Information design theory | General theory of signals that change what agents choose | Kamenica-Gentzkow 2011, Bergemann-Morris 2019 | Established |
| Recommenders as information design | A platform chooses what to recommend to speed user learning | Che-Hörner 2018, Kremer 2014, Cao 2024 | Emerging |
| Consumer privacy choice | Sharing data affects others through firms' responses | Ichihashi 2020, Rhodes-Zhou 2024, Acemoglu 2022, Ali 2023 | Contested |
| Limits of discrimination | Extra customer data can split surplus only within limits | Bergemann-Brooks-Morris 2015 | Emerging |

## What the evidence shows
### Finding 1: Personalized prices raise firm profit, but total consumer surplus usually falls.
- **Dubé 2023**: a randomized price test at one large digital firm → personalization raised profit 19% over an optimized uniform price. Total consumer surplus fell 23%, though over 60% of consumers paid less.
- **Esteves 2017**: with imperfectly informed consumers, behavior-based discrimination raises industry profit and lowers consumer welfare.
- **Villas-Boas 2004**: a monopolist that recognizes past buyers ends up worse off than one that cannot. The abstract does not report consumer welfare.
- **Strength:** Medium. One field test at one firm, plus several peer-reviewed models with different consumer assumptions.

### Finding 2: Learning from purchases helps firms, and forward-looking buyers wait longer.
- **Bergemann-Välimäki 1996**: buyers learn product values by buying, and price competition splits the cost of learning. Every stable equilibrium is efficient.
- **Bergemann-Välimäki 2000**: public product performance plus strategic pricing gives too much experimentation in one market. The outcome nears efficiency as markets multiply.
- **Papanastasiou-Savva 2017**: social learning increases strategic waiting, but still raises expected firm profit. Committing to a full price path in advance is often a poor choice.
- **Banchio-Yang 2021**: with persistent buyer values and no commitment, seller revenue stays at or below the full-commitment benchmark. The abstract does not name the ratchet effect.
- **Chen 2024**: sampling the customers with the largest profit loss from estimation error gives 5% to 10% more profit, with up to 97% fewer samples.
- **Strength:** Medium. Theory models with explicit assumptions. The Chen 2024 numbers come from a working paper.

### Finding 3: Dynamic persuasion can fail, and small costs let a sender approach the best static outcome.
- **Che-Kim 2023**: a receiver who may stop listening can cause persuasion to collapse in equilibrium. For small persuasion costs, outcomes approach the sender-optimal benchmark.
- **Orlov 2020**: an agent who cannot commit releases information in small steps, which delays the principal's decision. A committed delayed release works better.
- **Ely 2017**: introduces timed messages from a principal who sees a process unfold. The optimal policies were not checked.
- **Strength:** Medium for Che-Kim 2023 and Orlov 2020, which are peer-reviewed with stated results. Low for Ely 2017, read from its abstract only.

### Finding 4: Recommenders can speed learning by over-recommending early, but engagement is not user welfare.
- **Che-Hörner 2018**: the optimal recommender over-recommends a product early, raises the rate over time, and stops once pessimistic.
- **Cao 2024**: a forward-looking recommender can hurt users under monopoly and help them under competition.
- **Kleinberg 2024**: engagement gains do not reliably raise user welfare when preferences are inconsistent.
- **Kremer 2014**: studies how disclosure design can make users learn from the crowd. The abstract was not read in full.
- **Strength:** Medium for Che-Hörner 2018, which is peer-reviewed with stated results.
- **Strength:** Medium for Cao 2024 and Kleinberg 2024, which rest on summaries. Low for Kremer 2014.

### Finding 5: Consumer control over data can help consumers, but data sharing often becomes excessive.
- **Ali 2023**: consumer control over disclosure guarantees gains for every buyer type, compared with perfect discrimination and no personalization. This depends on competition.
- **Ichihashi 2020**: a seller prefers to commit not to price on data, because this encourages disclosure. A consumer can gain by committing to withhold some data.
- **Rhodes-Zhou 2024**: data sharing imposes an outside effect on others, so too many consumers share. More competition can lower consumer surplus.
- **Acemoglu 2022**: others' sharing leaks information, so data is underpriced and collected too much. Competition does not fix this.
- **Hidir-Vellodi 2021**: the buyer-best segmentation reveals only part of a buyer's preferences, using wide pooled segments.
- **Strength:** Medium. Several peer-reviewed models disagree on the welfare sign. No field study of repeated privacy choice was found.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Can consumers gain from personalized prices? | Dubé 2023: firm-led personalization cuts total consumer surplus. | Ali 2023: consumer-controlled disclosure can guarantee gains. | A multi-period field test with consumer-controlled disclosure. |
| Should a firm avoid pricing on data? | Ichihashi 2020: a no-pricing commitment encourages disclosure. | Acemoglu 2022: data sharing is already excessive. | A model with both commitment and consumer control. |
| Do engagement-driven recommenders help users? | Che-Hörner 2018: early over-recommendation speeds learning for users. | Kleinberg 2024: engagement gains do not reliably raise user welfare. | A recommender test that measures long-run user utility. |
| Is learning-based pricing efficient? | Bergemann-Välimäki 1996: every stable equilibrium is efficient. | Bergemann-Välimäki 2000: one market shows too much experimentation. | A comparison of single and many markets in one model. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Multi-period welfare measured in a field | Long-run consumer surplus is unknown under repeated targeting | Dubé 2023 (one-shot) |
| Recommenders that also learn user preferences | Learning on both sides changes incentives | Che-Hörner 2018 (fixed preferences) |
| Consumer data manipulation in real markets | Lab evidence exists, but field effects are unknown | One lab study, title not retrieved |
| Preference change caused by recommendations | Changing tastes alter long-run welfare | Banchio-Yang 2021 (persistent values) |
| Dynamic persuasion with a receiver who learns the sender's bias | Trust in a seller may change over time | Che-Kim 2023 (no bias learning) |

## Papers cited
| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Dubé 2023 | **Personalized Pricing and Consumer Welfare** | 2023 | Journal of Political Economy | summary (search) |
| Villas-Boas 2004 | **Price Cycles in Markets with Customer Recognition** | 2004 | RAND Journal of Economics | abstract (search) |
| Esteves 2017 | **Behaviour-based price discrimination under advertising and imperfectly informed consumers** | 2017 | Information Economics and Policy | summary (search) |
| Fudenberg-Villas-Boas 2006 | **Behavior-Based Price Discrimination and Customer Recognition** | 2006 | Handbooks in Information Systems | metadata only |
| Acquisti-Varian 2005 | **Conditioning Prices on Purchase History** | 2005 | Marketing Science | metadata only |
| Bergemann-Välimäki 1996 | **Learning and Strategic Pricing** | 1996 | Econometrica | summary (search) |
| Bergemann-Välimäki 2000 | **Experimentation in Markets** | 2000 | Review of Economic Studies | summary (search) |
| Papanastasiou-Savva 2017 | **Dynamic Pricing in the Presence of Social Learning and Strategic Consumers** | 2017 | Management Science | abstract (search) |
| Banchio-Yang 2021 | **Dynamic Pricing with Limited Commitment** | 2021 | arXiv preprint | abstract (fetched) |
| Chen 2024 | **Policy-Aware Experimentation: Strategic Sampling for Optimized Targeting Policies** | 2024 | working paper | summary (search) |
| Ely 2017 | **Beeps** | 2017 | American Economic Review | abstract (search) |
| Kamenica-Gentzkow 2011 | **Bayesian Persuasion** | 2011 | American Economic Review | metadata only |
| Bergemann-Morris 2019 | **Information Design: A Unified Perspective** | 2019 | Journal of Economic Literature | metadata only |
| Renault 2017 | **Optimal Dynamic Information Provision** | 2017 | Games and Economic Behavior | metadata only |
| Orlov 2020 | **Persuading the Principal to Wait** | 2020 | Journal of Political Economy | abstract (search) |
| Che-Kim 2023 | **Keeping the Listener Engaged: A Dynamic Model of Bayesian Persuasion** | 2023 | Journal of Political Economy | abstract (search) |
| Escudé 2023 | **Slow persuasion** | 2023 | Theoretical Economics | metadata only |
| Che-Hörner 2018 | **Recommender Systems as Mechanisms for Social Learning** | 2018 | Quarterly Journal of Economics | abstract (search) |
| Kremer 2014 | **Implementing the Wisdom of the Crowd** | 2014 | Journal of Political Economy | metadata only |
| Cao 2024 | **How Does Competition Affect Exploration vs. Exploitation? A Tale of Two Recommendation Algorithms** | 2024 | Management Science | summary (search) |
| Kleinberg 2024 | **The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization** | 2024 | Management Science | summary (search) |
| Ichihashi 2020 | **Online Privacy and Information Disclosure by Consumers** | 2020 | American Economic Review | abstract (search) |
| Ali 2023 | **Voluntary Disclosure and Personalized Pricing** | 2023 | Review of Economic Studies | summary (search) |
| Rhodes-Zhou 2024 | **Personalization and Privacy Choice** | 2024 | working paper, forthcoming in RAND Journal of Economics | summary (search) |
| Acemoglu 2022 | **Too Much Data: Prices and Inefficiencies in Data Markets** | 2022 | American Economic Journal: Microeconomics | summary (search) |
| Hidir-Vellodi 2021 | **Privacy, Personalization, and Price Discrimination** | 2021 | Journal of the European Economic Association | summary (search) |
| Acquisti-Taylor-Wagman 2016 | **The Economics of Privacy** | 2016 | Journal of Economic Literature | summary (search) |
| Bergemann-Brooks-Morris 2015 | **The Limits of Price Discrimination** | 2015 | American Economic Review | summary (search) |

<details><summary>Original research question</summary>

What economic and marketing theory models multi-period or dynamic personalization/targeting — behavior-based price discrimination, dynamic persuasion and information design, the ratchet effect, data-driven targeting with learning on both sides, consumer privacy and strategic behavior over time, personalized recommendation as information design — and what do they imply for consumer welfare, firm incentives and consumer strategic responses in the long run?

</details>
