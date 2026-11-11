# What economic and marketing theory models multi-period or dynamic personalization/targeting — behavior-based price discrimination, dynamic persuasion and information design, the ratchet effect, data-driven targeting with learning on both sides, consumer privacy and strategic behavior over time, personalized recommendation as information design — and what do they imply for consumer welfare, firm incentives and consumer strategic responses in the long run?

## TL;DR
Answer: Dynamic targeting theory covers six strands: repeated price discrimination on purchase history, learning-based pricing and experimentation, dynamic persuasion, recommenders as information design, consumer privacy choice, and market-level limits on discrimination. Across strands, firms usually gain from dynamic data use, while consumer welfare depends on commitment, competition and whether consumers anticipate the firm's use of data.
Strength: Medium
Theory-heavy. One large field test (Dubé 2023, one firm, one experiment) is the only empirical welfare measurement found. No multi-period field study of repeated targeting was found. The ratchet effect is discussed only through a secondary summary of Banchio and Yang (2021) and was not confirmed in the abstract.

## What Exists

### Sub-theme 1: Repeated price discrimination on purchase history (behavior-based price discrimination)
- **Personalized Pricing and Consumer Welfare** (Dubé and Misra, 2023, Journal of Political Economy) — randomized price test at one large digital firm: personalization raised profit 19% over an optimized uniform price, while total consumer surplus fell 23%, though over 60% of consumers paid less.
  - Relevance: the only welfare split measured in the field; one-shot pricing, not multi-period.
  - OpenAlex ID: W2630171565 (NBER working-paper record)
  - Cited by: 63
- **Behavior-Based Price Discrimination and Customer Recognition** (Fudenberg and Villas-Boas, 2006, Handbook chapter) — survey of repeated-sales pricing with recognized customers; abstract and metadata only.
  - Relevance: standard theory reference for behavior-based price discrimination.
  - OpenAlex ID: W2499718117
  - Cited by: 237
- **Price Cycles in Markets with Customer Recognition** (Villas-Boas, 2004, RAND Journal of Economics) — a monopolist that recognizes past buyers ends up worse off than without recognition; prices to new customers cycle.
  - Relevance: profit result for the firm; the consumer welfare result is not in the abstract.
- **Conditioning Prices on Purchase History** (Acquisti and Varian, 2005, Marketing Science) — standard reference on pricing that uses purchase records; abstract not read.
  - Relevance: foundational model for the purchase-history channel.
  - OpenAlex ID: W3122338044
  - Cited by: 694
- **Behaviour-based price discrimination under advertising and imperfectly informed consumers** (Esteves and Cerqueira, 2017, Information Economics and Policy) — with imperfectly informed consumers, behavior-based discrimination raises industry profit and lowers consumer welfare.
  - Relevance: reverses the usual full-information conclusion that consumers can gain; title taken from a repository record, not checked against the journal page.

### Sub-theme 2: Learning-based pricing and experimentation with learning on both sides
- **Learning and Strategic Pricing** (Bergemann and Välimäki, 1996, Econometrica) — a buyer learns sellers' product values by buying; price competition splits the cost of learning; every Markov perfect equilibrium is efficient.
  - Relevance: the classic two-sided learning result; the consumer and seller share the learning cost through prices.
- **Experimentation in Markets** (Bergemann and Välimäki, 2000, Review of Economic Studies) — a new product of unknown quality with public performance data; buyers' informational externality plus strategic pricing gives excessive experimentation in one market, and efficiency as markets multiply.
  - Relevance: direct link between consumer learning externalities and firm pricing over time.
- **Dynamic Pricing in the Presence of Social Learning and Strategic Consumers** (Papanastasiou and Savva, 2017, Management Science) — social learning intensifies strategic waiting, yet raises expected firm profit; committing to a full price path in advance is often a poor choice.
  - Relevance: forward-looking consumers plus learning from others; direct test of the "consumers wait" channel.
  - OpenAlex ID: W2306295924
  - Cited by: 311
- **Dynamic Pricing with Limited Commitment** (Banchio and Yang, 2021, arXiv preprint) — with persistent private values and a D1-style refinement, seller revenue is no higher than under full commitment, whatever the persistence. The ratchet effect is not named in the abstract.
  - Relevance: the closest direct statement on the ratchet effect; the earlier search snippet overstated it as "removes the gains", which the abstract does not say.
  - OpenAlex ID: W4287327788
  - Cited by: 2
- **Policy-Aware Experimentation: Strategic Sampling for Optimized Targeting Policies** (Chen, Ascarza and Netzer, 2024, working paper) — sample customers with the largest expected profit loss from estimation error; reports 5% to 10% profit gain and up to 97% fewer samples in two applications. Later version titled Policy-Aware Sampling: Prioritizing Consequential Customers for Optimized Targeting Policies. Summary only.
  - Relevance: learning on the firm side to choose targeting policies; not a consumer-learning model.

### Sub-theme 3: Dynamic persuasion and information design over time
- **Beeps** (Ely, 2017, American Economic Review) — a principal who sees a stochastic process sends messages over time to an agent; the paper introduces dynamic persuasion mechanisms. Abstract read via search summary; main optimal-policy results not confirmed.
  - Relevance: the base dynamic persuasion model with timed signals.
  - OpenAlex ID: W4235023701
  - Cited by: 196
- **Bayesian Persuasion** (Kamenica and Gentzkow, 2011, American Economic Review) — static benchmark in which the sender chooses signals to maximize her own payoff.
  - Relevance: benchmark that all dynamic versions extend.
  - OpenAlex ID: W4255572092
  - Cited by: 1975
- **Information Design: A Unified Perspective** (Bergemann and Morris, 2019, Journal of Economic Literature) — review of information design; metadata only.
  - Relevance: general framework for designing what agents learn.
  - OpenAlex ID: W3121860146
  - Cited by: 593
- **Optimal Dynamic Information Provision** (Renault, Solan and Vieille, 2017, Games and Economic Behavior) — characterizes optimal dynamic information provision; metadata only, results not read.
  - Relevance: dynamic information design with a changing state.
  - OpenAlex ID: W1596703369
  - Cited by: 111
- **Persuading the Principal to Wait** (Orlov, Skrzypacz and Zryumov, 2020, Journal of Political Economy) — a biased agent who cannot commit releases information in small steps to delay the principal's action; committing to a delayed full release is optimal.
  - Relevance: consumer or agent delay as a strategic response to information flow.
  - OpenAlex ID: W3122680755
  - Cited by: 98
- **Keeping the Listener Engaged: A Dynamic Model of Bayesian Persuasion** (Che, Kim and Mierendorff, 2023, Journal of Political Economy) — persuasion can collapse in a Markov perfect equilibrium; for small persuasion costs, sender-optimal outcomes are approached; attention is the key constraint.
  - Relevance: dynamic persuasion with a receiver who may stop listening; the key constraint is attention.
  - OpenAlex ID: W4308886374
  - Cited by: 36
- **Slow persuasion** (Escudé and Sinander, 2023, Theoretical Economics) — dynamic information design; metadata only.
  - Relevance: dynamic persuasion pace; results not read.
  - OpenAlex ID: W4319991391
  - Cited by: 12

### Sub-theme 4: Recommenders as information design and learning
- **Recommender Systems as Mechanisms for Social Learning** (Che and Hörner, 2018, Quarterly Journal of Economics) — the optimal recommender over-recommends a product early to speed exploration; frequency rises over time and stops once the designer is pessimistic.
  - Relevance: direct model of personalized recommendation as information design with dynamics.
  - OpenAlex ID: W2779126177
  - Cited by: 173
- **Implementing the Wisdom of the Crowd** (Kremer, Mansour and Perry, 2014, Journal of Political Economy) — how to make crowd-sourced learning incentive compatible through disclosure design; abstract not read.
  - Relevance: information-design baseline for review-based recommendation.
  - OpenAlex ID: W2149247676
  - Cited by: 260
- **How Does Competition Affect Exploration vs. Exploitation? A Tale of Two Recommendation Algorithms** (Cao, Ma, Ning and Sun, 2024, Management Science) — a forward-looking recommender can hurt users under monopoly and help under competition; competing firms can face a prisoner's dilemma in investment. Summary only.
  - Relevance: multi-period recommender with user learning; welfare sign depends on market structure.
- **The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization** (Kleinberg, Mullainathan and Raghavan, 2024, Management Science) — engagement gains do not reliably mean user welfare gains when preferences are inconsistent. Venue and year taken from a search summary; arXiv version dated 2022.
  - Relevance: adversarial to the view that engagement-optimal recommenders serve users.

### Sub-theme 5: Consumer privacy and strategic data sharing over time
- **Online Privacy and Information Disclosure by Consumers** (Ichihashi, 2020, American Economic Review) — a seller learns preferences from disclosure and prices on them; the seller prefers to commit not to price on data, which encourages disclosure; the equilibrium is typically inefficient.
  - Relevance: consumer strategic disclosure in a multi-product seller setting; a precommitment to withhold data can hurt the consumer.
  - OpenAlex ID: W2949225670
  - Cited by: 225
- **Voluntary Disclosure and Personalized Pricing** (Ali, Lewis and Vasserman, 2023, Review of Economic Studies) — consumer control over disclosure can guarantee gains for every type relative to perfect discrimination and to no personalization; depends on competition and disclosure technology.
  - Relevance: the strongest positive result for consumers under strategic disclosure.
- **Personalization and Privacy Choice** (Rhodes and Zhou, 2024, working paper, forthcoming in RAND Journal of Economics) — sharing data imposes a negative externality on others through firms' product-market responses; too many consumers share data; more competition can lower consumer surplus.
  - Relevance: direct model of consumer privacy externalities in personalized recommendations, prices and product design.
  - OpenAlex ID: W4394863397
  - Cited by: 7
- **Too Much Data: Prices and Inefficiencies in Data Markets** (Acemoglu, Makhdoumi, Malekian and Ozdaglar, 2022, American Economic Journal: Microeconomics) — data is underpriced because others' sharing leaks information; competition does not fix excessive sharing.
  - Relevance: market-level result that data sharing is excessive; contrasts with the view that markets collect too little data.
  - OpenAlex ID: W3127984278
  - Cited by: 220
- **Privacy, Personalization, and Price Discrimination** (Hidir and Vellodi, 2021, Journal of the European Economic Association) — the buyer-optimal incentive-compatible segmentation is partially revealing and built from pooled segments.
  - Relevance: consumer-optimal disclosure design under personalized pricing.
- **The Economics of Privacy** (Acquisti, Taylor and Wagman, 2016, Journal of Economic Literature) — review; privacy protection can raise or lower welfare depending on context; consumers often lack full information about data use.
  - Relevance: review anchor for the privacy strand.

### Sub-theme 6: Market-level limits of price discrimination
- **The Limits of Price Discrimination** (Bergemann, Brooks and Morris, 2015, American Economic Review) — any split of surplus between consumers and the seller is achievable through segmentation, within bounds: seller profit at least the uniform-monopoly profit, total surplus at most the efficient surplus.
  - Relevance: shows what extra customer information can and cannot do for surplus extraction.

## Reference Chain Discoveries
- Found via: citers of Beeps (Ely 2017) — Bergemann and Morris 2019; Renault, Solan and Vieille 2017; Orlov, Skrzypacz and Zryumov 2020; Che and Hörner 2018.
- Found via: references of Che and Hörner 2018 — Kamenica and Gentzkow 2011.
- Found via: citers of Ichihashi 2020 — Acemoglu et al. 2022 (Too Much Data); Bergemann, Bonatti and Gan 2019 (The Economics of Social Data) and Bergemann and Bonatti 2019 (Markets for Information) appeared but were not used.
- Found via: first OpenAlex title lookups — Kremer et al. 2014; Acquisti and Varian 2005; Fudenberg and Villas-Boas 2006; Banchio and Yang 2021; Rhodes and Zhou 2024.
- Found via: Round 1 search results — Papanastasiou and Savva 2017; Villas-Boas 2004; Esteves and Cerqueira 2017.
- Found via: Round 4 searches — Ali, Lewis and Vasserman 2023; Acquisti, Taylor and Wagman 2016; Bergemann, Brooks and Morris 2015.
- Found via: Round 6 search on privacy and personalized pricing — Hidir and Vellodi 2021.
- Found via: Round 7 search on experimentation in markets — Bergemann and Välimäki 2000.
- Found via: Round 8 search on recommendation algorithms — Cao et al. 2024; Chen et al. 2024 (title checked in a second search).
- Lab evidence on consumers who manipulate their survey data for a pricing model (Bó, Chen and Hakimov, 2024, Games and Economic Behavior) surfaced in a search summary. Exact title not retrieved, so it is not listed as a paper.

## What's Missing (Gaps)
- No model combines repeated personalized recommendation, learning on both sides, and dynamic persuasion. Closest: Che and Hörner 2018 plus Ely 2017.
- Dubé and Misra 2023 is one-shot. No multi-period field measurement of consumer surplus under repeated targeting was found.
- Consumer strategic data manipulation under real repeated pricing has lab evidence only; no field study found.
- Most dynamic models fix consumer preferences (Papanastasiou and Savva 2017; Banchio and Yang 2021 use persistent values). Models where recommendations shift preferences were not found in this stream.
- Long-run welfare for LLM-style interaction is outside this stream and was not found in theory papers here.

## Contradictions or Tensions
- Welfare of personalized pricing: Dubé and Misra (2023) find total consumer surplus falls 23% under firm-led personalization, while Ali et al. (2023) find consumer-controlled disclosure guarantees gains. Different regimes (firm pricing versus consumer control), not a direct contradiction.
- Behavior-based price discrimination with imperfectly informed consumers (Esteves and Cerqueira 2017) hurts consumers, while the full-information literature summary suggests consumers can gain. Not checked against the original full-information papers.
- Recognition and firm profit: Villas-Boas (2004) finds recognition hurts a monopolist, while Papanastasiou and Savva (2017) find social learning raises firm profit. Different models, so the two results do not directly conflict.
- Recommender value: Che and Hörner (2018) show over-recommendation improves exploration, while Kleinberg et al. (2024) warn that engagement optimization does not reliably raise user welfare. They use different welfare objectives.
- Data sharing: Ichihashi (2020) shows a seller's commitment not to price on data encourages disclosure, while Acemoglu et al. (2022) and Rhodes and Zhou (2024) argue sharing is excessive. The welfare direction of more data differs by model.

## Confidence
Medium
- What would raise confidence: full text of Dubé and Misra (2023) and Villas-Boas (2004) for consumer welfare results; full text of Renault et al. (2017) and Orlov et al. (2020) to check dynamic persuasion results; a multi-period field measurement of repeated targeting.
- What would lower confidence: several entries rest on abstracts or search summaries (Esteves and Cerqueira 2017, Ali et al. 2023, Cao et al. 2024, Kleinberg et al. 2024), and the Banchio and Yang ratchet claim is narrower than the earlier snippet.

## Search Log
### Round 1: Broad search
- Queries: dynamic behavior-based price discrimination consumer welfare repeated purchases; dynamic persuasion information design Bayesian persuasion over time learning; ratchet effect dynamic pricing consumer strategic waiting; data-driven targeting learning on both sides; personalized recommendation as information design strategic consumers privacy.
- Papers found: roughly 40 result links across five queries; about 10 judged relevant and followed up.
- Key leads: Ely 2017 (Beeps); Rhodes and Zhou 2024; Banchio and Yang 2021; Esteves and Cerqueira 2017; Papanastasiou and Savva 2017.

### Round 2: Citation traversal
- Papers traversed: Beeps (Ely 2017), Che and Hörner 2018, Ichihashi 2020 (citers and references of Che and Hörner 2018 only; references not pulled for the others).
- New papers from references: Kamenica and Gentzkow 2011 (Bayesian Persuasion). Other references of Che and Hörner were older bandit, herding or review-fraud papers and were not added.
- New papers from citers: Bergemann and Morris 2019; Renault et al. 2017; Orlov et al. 2020; Acemoglu et al. 2022; Bergemann and Bonatti 2019; Bergemann, Bonatti and Gan 2019 (not used).
- Also looked up by title in OpenAlex: Acquisti and Varian 2005; Fudenberg and Villas-Boas 2006; Kremer et al. 2014; Banchio and Yang 2021; Rhodes and Zhou 2024.

### Round 3: Reference section mining
- Attempted: arXiv abstract for Banchio and Yang (read); Pisa working paper (binary PDF, unreadable); AEA page for Beeps (404). Related-work sections were not reached for the two most relevant papers.
- New papers: none from this round.

### Round 4: Gap-filling
- Gaps targeted: consumer disclosure, the dynamic persuasion results, limits of discrimination, learning-and-pricing foundations, the privacy review.
- Queries: Ali, Lewis and Vasserman; Dubé and Misra; Papanastasiou and Savva; Bergemann and Välimäki 1996; Acquisti, Taylor and Wagman 2016; Ichihashi 2020; Orlov et al. 2020; Bergemann, Brooks and Morris 2015; Che and Hörner 2018; Esteves and Cerqueira 2017.
- New findings: Ali et al. 2023 (consumer control); Bergemann-Välimäki 1996; Acquisti-Taylor-Wagman 2016; Bergemann-Brooks-Morris 2015; Esteves-Cerqueira 2017.

### Round 5: Adversarial check
- Gaps targeted: whether dynamic targeting can help consumers; critiques of persuasion and recommender results.
- Queries: Villas-Boas 2004 customer recognition welfare; Che, Kim and Mierendorff 2023; recommender misalignment and engagement.
- New findings: Villas-Boas 2004 (profit result, welfare not in abstract); Che-Kim-Mierendorff 2023 (persuasion can collapse); Kleinberg et al. 2024 (engagement not user welfare); Cao et al. 2024 surfaced later.

### Round 6: Follow leads
- Gaps targeted: data-market externality, personalized price and privacy papers, consumer manipulation.
- Queries: Acemoglu et al. 2022; Hidir and Vellodi 2021; consumer data obfuscation under behavior-based pricing.
- New findings: Acemoglu et al. 2022 (too much data); Hidir and Vellodi 2021; lab evidence on manipulation (title not retrieved).

### Round 7: Follow leads
- Gaps targeted: two-sided experimentation literature; dynamic targeting with learning.
- Queries: Bergemann and Välimäki 2000 (experimentation in markets); dynamic targeting with consumer learning 2023-2024.
- New findings: Bergemann and Välimäki 2000; a lead to Cao et al. 2024 and Chen et al. 2024.

### Round 8: Follow leads (last allowed round)
- Gaps targeted: exact titles and venues for Cao et al. and Chen et al.
- Queries: Cao, Ma forward-looking recommendation; Chen, Ascarza, Netzer policy-aware experimentation.
- New findings: Cao et al. 2024 (Management Science); Chen et al. 2024 (working paper, two titles).

### Convergence note
- Total unique relevant papers found: 28 (listed above; Bó, Chen and Hakimov 2024 excluded, title not retrieved).
- New papers in last round: 2 (Cao et al. 2024; Chen et al. 2024). Round 7 added 1.
- Stopped because: hit the 8-round hard cap. The last two rounds still added new papers, so the search did not converge; gaps remain on multi-period field evidence and consumer manipulation.
