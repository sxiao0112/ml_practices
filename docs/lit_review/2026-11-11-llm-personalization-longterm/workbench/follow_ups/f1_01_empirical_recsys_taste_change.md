# What causal field or quasi-experimental evidence exists on whether recommenders or personalization change users' long-run tastes or consumption diversity (e.g. Spotify diversity studies, Holtz et al. podcast experiment, Aridor et al. MovieLens filter-bubble deconstruction, Fleder & Hosanagar, Lee & Hosanagar, YouTube/Twitter audits, Meta 2020 election feed experiments, Ribeiro et al.)? Which way do effects go, how large, and how do these reconcile with theory predicting amplification? Resolve the tension between amplification theory and the mostly null or mixed field results.

## TL;DR
Answer: Few causal studies test taste change directly. The one randomized music study (Holtz et al., Spotify podcasts) finds personalization lowers individual diversity by 11.5% but raises aggregate diversity by 6%. Platform experiments on politics mostly find small attitude effects, with one 2026 X experiment showing a rightward shift when the algorithm is on.
Strength: Low
Direct causal evidence on long-run taste change is thin: about 6 randomized or counterfactual studies, mostly short (weeks), on one platform each. The within-user narrowing predicted by amplification theory appears in the music study, but relative to a popularity-based control, not to no recommendations. Null or small results on political attitudes come from short windows and one or two platforms.

## What Exists
### Sub-theme 1: Randomized field experiments on recommender-driven consumption diversity
- **The Engagement-Diversity Connection: Evidence from a Field Experiment on Spotify** (Holtz et al., 2020, ACM Conference on Economics and Computation; arXiv 2003.08203) — About 900,000 users in 17 countries got personalized podcast recommendations (treatment) or popularity-by-demographic recommendations (control). Treatment raised podcast streams by 28.90%, lowered individual diversity by 11.51%, and raised aggregate diversity by 5.96%.
  - Relevance: The only randomized music or podcast study found that directly measures within-user taste narrowing. Its control is popularity-based, not "no recommendations."
  - OpenAlex ID: W3011174874
  - Cited by: 108
- **How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment** (Lee & Hosanagar, 2019, Information Systems Research) — Randomized test on a North American retailer site with 1,138,238 users and 82,290 products. Collaborative filtering lowered aggregate sales diversity. Purchase-based recommenders moved sales more than view-based ones.
  - Relevance: Shows the aggregate-versus-individual split is a property of collaborative filtering, not only of podcasts. It tests sales, not user tastes, so it is a weaker match for taste change.
  - OpenAlex ID: W3124497955
  - Cited by: 213
- **Algorithmic Effects on the Diversity of Consumption on Spotify** (Anderson et al., 2020, WWW) — Large log study plus a randomized experiment. High consumption diversity is associated with better long-term metrics, and algorithmic listening is associated with lower diversity. Algorithmic recommendations work better for low-diversity users.
  - Relevance: Shows that algorithmic listening is associated with narrowing, but the association is not identified as causal. The randomized part tests recommendation effectiveness, not taste change.
  - OpenAlex ID: W3012950066
  - Cited by: 244
  - Note: Read from search snippets and a secondary summary. The PDF fetch failed, so the exact sample size and design are unverified.

### Sub-theme 2: Observational and audit studies of recommenders and tastes (MovieLens, YouTube, Spotify)
- **Exploring the filter bubble: the effect of using recommender systems on content diversity** (Nguyen et al., 2014, WWW) — On MovieLens, users who followed recommendations narrowed their rating diversity less than users who did not. Narrowing still occurred over time for both groups.
  - Relevance: The canonical MovieLens longitudinal study. It is observational, so selection into recommendations is a confound.
  - OpenAlex ID: W4299687421
  - Cited by: 651
- **Deconstructing the Filter Bubble: User Decision-Making and Recommender Systems** (Aridor, Gonçalves & Sikdar, 2020, RecSys) — A choice model in which consuming one item teaches the user about similar items, and risk aversion sharpens narrowing. Recommendations push users into new areas but make users alike.
  - Relevance: Gives the theory that explains Nguyen et al. without a causal estimate. This is a model paper, not a MovieLens causal study as the research prompt describes.
  - OpenAlex ID: not looked up
- **Auditing radicalization pathways on YouTube** (Ribeiro et al., 2020, FAT*) — Audit of 330,925 videos from 349 channels using untrained sock puppet accounts. Reports that some algorithmic pathways lead from moderate to extreme channels.
  - Relevance: Audit evidence for amplification. A later critique says untrained sock puppets understate pathways for trained users (Haroon et al., 2022).
  - OpenAlex ID: W2969399596
  - Cited by: 719
- **Examining the consumption of radical content on YouTube** (Hosseinmardi et al., 2021, PNAS) — Panel of over 300,000 Americans tracked on and off YouTube from 2016 to 2019. Off-platform tastes strongly match on-platform consumption.
  - Relevance: Attributes most radical consumption to user preference, which argues against a strong recommender effect. Observational, so it cannot rule out an effect.
  - OpenAlex ID: not looked up
- **Causally estimating the effect of YouTube's recommender system using counterfactual bots** (Hosseinmardi et al., 2024, PNAS) — Logged-in bots replay real users' histories and are compared with rule-based bots. Recommendations alone make consumption less partisan on average, most strongly for heavy partisan viewers.
  - Relevance: The strongest causal design in the YouTube audit literature. It reverses the direction of the 2020 audit result on average. Applies to the post-2019 algorithm, desktop only.
  - OpenAlex ID: W4391773993
  - Cited by: 66
- **Blockbuster Culture's Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity** (Fleder & Hosanagar, 2009, Management Science) — Argues that collaborative filters favor items with many past sales. Individual diversity can rise while aggregate sales diversity falls.
  - Relevance: The model-based origin of the individual-versus-aggregate split. The method was not checked beyond the abstract, so treat it as theory.
  - OpenAlex ID: W3122511740
  - Cited by: 776
- **Assessing the Impact of Music Recommendation Diversity on Listeners: A Longitudinal Study** (Porcaro et al., 2022, arXiv preprint) — 110 listeners in Southern Europe got daily electronic music recommendations at set diversity levels for 12 weeks. Diverse recommendations increased openness to the genre and reduced stereotypes.
  - Relevance: A longitudinal taste-change design with attitude outcomes. The abstract names no control group and gives no effect sizes.
  - OpenAlex ID: not looked up
- **The Daily Me Versus the Daily Others: How Do Recommendation Algorithms Change User Interests? Evidence from a Knowledge-Sharing Platform** (Liu & Cong, 2022, Journal of Marketing Research) — Social-follow recommendations concentrated social interests on popular users. Topic interests broadened.
  - Relevance: Shows that different recommender types move interests in different directions. The identification strategy was not verified.
  - OpenAlex ID: not looked up

### Sub-theme 3: Platform experiments on attitudes and polarization (Meta, X, YouTube)
- **How do social media feed algorithms affect attitudes and behavior in an election campaign?** (Guess et al., 2023, Science) — About 23,000 Facebook and 21,000 Instagram users got a chronological feed for about three months during the 2020 US election. Attitudes and polarization did not change. Time on platform and uncivil content fell, while untrustworthy content rose.
  - Relevance: The Meta 2020 experiment. It tests a feed switch and finds attitude nulls over a short window. Two platforms and one election limit generality.
  - OpenAlex ID: not looked up
- **Short-term exposure to filter-bubble recommendation systems has limited polarization effects: Naturalistic experiments on YouTube** (Liu et al., 2025, PNAS) — About 9,000 participants in four experiments. Researchers changed real recommendations in a YouTube-like platform for about 130,000 recommendations. Short-term exposure to partisan feeds did not measurably shift policy attitudes.
  - Relevance: Direct test of the filter-bubble mechanism on attitudes. Short exposure only. The authors say long-term effects and vulnerable groups remain untested.
  - OpenAlex ID: W4407695581
  - Cited by: 40
- **The political effects of X's feed algorithm** (Gauthier, Hodler, Widmer & Zhuravskaya, 2026, Nature) — About 5,000 active US users got algorithmic or chronological feeds for seven weeks in 2023. Switching the algorithm on shifted policy views toward conservative positions. Switching it off did not reverse the shift, and followed accounts persisted.
  - Relevance: The most direct recent evidence that a feed can move political views. Its asymmetry and persistence contrast with the Meta and YouTube nulls. One platform, one country, one summer.
  - OpenAlex ID: W7130386561
  - Cited by: 50
- **Engagement, user satisfaction, and the amplification of divisive content on social media** (Milli et al., 2025, PNAS Nexus) — Randomized comparison of Twitter's engagement ranking with a feed ranked by stated preferences. Stated-preference ranking showed less angry, partisan, and out-group hostile content.
  - Relevance: Shows ranking objective matters. The stated-preference arm may reinforce echo chambers, the authors note. Based on a secondary summary and the PMC listing.
  - OpenAlex ID: W4408138635
  - Cited by: 346
- **Algorithmic amplification of politics on Twitter** (Huszár et al., 2022, PNAS) — Uses a randomly assigned 1% holdout excluded from the personalized home timeline. Mainstream right-leaning accounts got more amplification than left-leaning accounts in six of seven countries.
  - Relevance: Provides a holdout design that measures amplification relative to a non-personalized baseline. Outcome is exposure, not taste. Authors are from the platform.
  - OpenAlex ID: not looked up

### Sub-theme 4: Theory and critiques of amplification
- **The Amplification Paradox in Recommender Systems** (Ribeiro, Veselovsky & West, 2023, ICWSM) — An agent-based simulation shows audits that ignore user preference overstate amplification. Users rarely pick niche extreme content when alternatives exist.
  - Relevance: Gives the strongest reconciling argument between amplification theory and null field results. It is a simulation, not evidence.
  - OpenAlex ID: not looked up
- **YouTube, The Great Radicalizer? Auditing and Mitigating Ideological Biases in YouTube Recommendations** (Haroon et al., 2022, arXiv preprint) — Critiques untrained sock puppets and argues trained sock puppets reveal larger ideological bias.
  - Relevance: Counter-evidence to the 2020 audit's low pathway rate. It supports the view that audit design drives the size of the effect.
  - OpenAlex ID: not looked up

## Reference Chain Discoveries
- Found via: OpenAlex citers of Holtz et al. (2020). Citers include Anderson et al. (2020) and a 2021 Spotify cross-country diversity study (W3186461074), not read.
- Found via: OpenAlex citers of Hosseinmardi et al. (2024). Gauthier et al. (2026), Liu et al. (2025), and Milli et al. (2025) came from here.
- Found via: OpenAlex references of Holtz et al. (2020). Lists Fleder & Hosanagar (2009), Nguyen et al. (2014), Anderson et al. (2020), and Lee & Hosanagar (2019).
- Found via: OpenAlex references of Hosseinmardi et al. (2024). Lists Ribeiro et al. (2020), Hosseinmardi et al. (2021), and Huszár-era audits.
- Found via: Anderson et al. (2020) search trail. Hansen et al. (2021, WSDM), "Shifting Consumption towards Diverse Content on Music Streaming Platforms," found but results not verified.
- Found via: "Dynamics of Exploration on Spotify" (2022, ICWSM, W4312554671). Found in citers of Holtz, abstract not read.

## What's Missing (Gaps)
- No randomized study of multi-year taste change in music or video. Longest found is 12 weeks (Porcaro et al.).
- No study estimates taste change against a true no-recommendation control. Holtz's control is popularity-based.
- No persistence test after a recommender is switched off, except Gauthier et al. on political follows.
- No field study of LLM-based personalization and taste change was found in these searches.
- No difference-in-differences study of streaming recommendation and taste was found. One search returned none.

## Contradictions or Tensions
- **Holtz vs. Nguyen (2014) on within-user narrowing.** Holtz finds individual diversity down 11.5% under personalization. Nguyen finds recommendation users narrowed less than non-users on MovieLens. The controls differ (popularity-based vs. none), and the outcomes differ (podcast streams vs. ratings).
- **Holtz on persistence.** One secondary summary says effects dissipated after the experiment. The Holtz abstract says persistence is not addressed. Treat the dissipation claim as unverified.
- **Gauthier et al. (2026) vs. Guess et al. (2023) and Liu et al. (2025).** Gauthier finds an attitude shift when X's algorithm is on. Meta and YouTube nulls find no attitude shift. Differences include platform, length (7 weeks vs. 3 months vs. days), and the counterfactual (algorithm vs. chronological, or manipulated recommendations).
- **Hosseinmardi (2024) vs. Ribeiro (2020).** Counterfactual bots find recommendations reduce partisanship on average. The sock puppet audit finds extremist pathways. Both use YouTube, but different periods and bot designs.
- **Ribeiro et al. (2023) vs. Huszár et al. (2022).** The simulation argues audits overstate amplification. The Twitter holdout finds real, consistent right-leaning amplification.
- **Amplification theory vs. field nulls.** Theory predicts feedback loops that narrow tastes. The field finds narrowing in one music study, small attitude effects in most political studies, and reversal on YouTube.

## Confidence
Confidence: Low
- What would raise confidence: A multi-year randomized test on music or video, with a no-recommendation control and a post-treatment follow-up.
- What would lower confidence: Full-text checks showing Holtz's or Anderson's effects are smaller, or that Liu & Cong's design is observational with no valid control.

Limits of this search: Most papers were read from abstracts, search snippets, or secondary summaries. The Anderson et al. PDF and the Lalmas WSDM PDF could not be fetched. The Spotify diversity literature was checked only through citers and search, not systematically.

## Search Log
### Round 1: Broad search
- Queries: "Holtz Aridor podcast recommender experiment consumption diversity field experiment"; "Aridor MovieLens filter bubble deconstruction recommender taste preferences"; "Spotify recommendations music diversity natural experiment users taste change"; "Meta 2020 election feed experiments Guess et al. Science political polarization algorithmic feed"; "Fleder Hosanagar recommender systems sales diversity; Lee Hosanagar 2019 YouTube recommendations consumption diversity"
- Papers found: about 12 relevant
- Key leads: Holtz et al. (2020); Lee & Hosanagar (2019); Hosseinmardi et al. (2024); Guess et al. (2023); Nguyen et al. (2014)
- Note: The Lee & Hosanagar 2019 YouTube attribution in the prompt is not supported. The 2019 Lee & Hosanagar paper is about retail sales. The YouTube-diversity work is Hosseinmardi and Ribeiro.
- Note: The prompt's "Aridor et al. MovieLens" describes a theory paper, not a MovieLens causal study.

### Round 2: Citation traversal
- Papers traversed: Holtz et al. (2020, OpenAlex W3011174874); Lee & Hosanagar (2019, W3124497955); Hosseinmardi et al. (2024, W4391773993)
- Citers resolved: 12 per paper (top by citation count). Relevant new citers: Gauthier et al. (2026), Milli et al. (2025), Liu et al. (2025), Liu & Cong (2022), Porcaro et al. (2022, not from citers; from search).
- Reference lists resolved: Holtz (41 references), Hosseinmardi (20 references). Lee & Hosanagar reference count (46) not resolved.
- 2-hop traversal: not done. The one-hop citers are mostly economics or marketing and audit papers. Few have more than 50 citations and direct relevance.

### Round 3: Reference section mining
- Full-text Related Work sections were not accessible. The Holtz abstract was read via WebFetch. The Anderson PDF fetch failed. The OpenAlex reference lists substituted.
- New papers from references: Fleder & Hosanagar (2009), Nguyen et al. (2014), Anderson et al. (2020), Ribeiro et al. (2020), Hosseinmardi et al. (2021)

### Round 4: Gap-filling
- Gaps targeted: Music or video taste-change designs with control groups; difference-in-differences; longitudinal designs
- Queries: "difference-in-differences recommender system causal effect music taste diversity users over time natural experiment streaming" (extended); "Shifting Consumption towards Diverse Content on Music Streaming Platforms WSDM 2021 Spotify randomized experiment results"
- New findings: Porcaro et al. (2022); Hansen et al. (2021, results not verified). No DiD music study found.

### Round 5: Adversarial check
- Gaps targeted: Critiques and nulls to the amplification claim
- Queries: "Short-term exposure to filter-bubble recommendation systems has limited polarization effects naturalistic experiments YouTube"; "Ribeiro 2020 Auditing radicalization pathways on YouTube critique sock puppet audit limitations recommendations"; "Hosseinmardi 2021 PNAS Examining the consumption of radical content on YouTube null effect supply demand users"; "Stray The Amplification Paradox in Recommender Systems 2023 engagement vs user preferences critique" (returned Ribeiro et al. 2023; the "Stray" name is not supported)
- New findings: Liu et al. (2025), Haroon et al. (2022), Ribeiro et al. (2023). Each is a null or counter-audit.

### Rounds 6+: Followed leads
- Followed: Gauthier et al. (2026) and Guess et al. (2023) for design details; Liu & Cong (2022) for the knowledge-sharing platform result; Milli et al. (2025) for the Twitter ranking result.
- New papers: none beyond those listed above.

### Convergence note
- Total unique relevant papers found: about 22 (16 with a full bullet entry above, plus reference-chain items)
- New papers in last round: 3 (Liu et al. 2025, Haroon et al. 2022, Ribeiro et al. 2023)
- Stopped because: Round 5 completed and sub-questions answered from abstracts and summaries. Full texts were not reachable for several key papers, so this search is bounded, not exhaustive. The stopping rule's "2 empty rounds" condition was not strictly met.
