# Field evidence on whether recommenders change long-run tastes

**Question:** Do recommender systems change what people like or consume over time, and in which direction and by how much?

## Short answer
**Answer:** Only a few causal studies test this directly, and they disagree on direction. A personalized music recommender lowered each user's own variety by 11.5%. Platform experiments on political feeds mostly find small effects on attitudes.

**Strength:** Low (about six causal studies, mostly short, each on one platform)

- **Holds when:** Recommendations are personalized and compared with popularity-based suggestions. Individual variety falls, and total variety across users rises.
- **Does not hold when:** Feeds are switched for a few weeks or months. Political attitudes shift little in most trials.
- **Still unknown:** Whether within-user narrowing lasts for years, and how it compares with no recommendations at all.

## Background
Recommender systems pick items for each user based on past behavior. Researchers ask whether this narrows what people consume over time, creating a "filter bubble." Theory predicts that feedback loops should narrow tastes. Field tests check whether that happens, and by how much, on real platforms.

Key terms used on this page:

| Term | Plain meaning (max 20 words) |
|------|------------------------------|
| Recommender system | Software that picks items for each user based on past behavior. |
| YouTube | Video platform where many recommender audits have been run. |
| LLM-based personalization | Personalization by a large language model (LLM) chatbot. |
| Filter bubble | Narrowing of what a user sees or consumes, often caused by recommendations. |
| Individual diversity | How varied one user's consumption is across items or topics. |
| Aggregate diversity | How varied consumption is across all users taken together. |
| Randomized field experiment | Real users are randomly given one of several recommendation versions. |
| Holdout group | Users kept on a non-personalized version to measure the personalization effect. |
| Counterfactual bot | Automated account that follows a rule-based path to test what a recommender adds. |
| Sock puppet audit | Researcher-run fake account that watches videos to record what gets recommended. |
| Collaborative filtering | Method that recommends items liked by users with similar past behavior. |
| MovieLens | Public movie-rating dataset used to study recommenders. |
| Polarization | Gap between political groups in attitudes or partisan consumption. |
| Amplification | A recommender pushing some content more often than users would find it alone. |
| Difference-in-differences | Method that compares change over time between treated and untreated groups. |

## Main approaches
The main ways researchers attack this question:

| Approach | Core idea in plain words | Main papers (short names) | Status |
|----------|--------------------------|---------------------------|--------|
| Randomized platform experiment | Random users get different recommendations, and outcomes are compared. | Holtz 2020, Lee and Hosanagar 2019, Guess 2023 | Emerging |
| Platform experiment on feeds | Random users get a switched feed, such as chronological. | Guess 2023, Gauthier 2026, Milli 2025 | Contested |
| Controlled YouTube bot test | Logged-in bots replay real histories and compare with rule-based bots. | Hosseinmardi 2024 | Emerging |
| Sock puppet audit | Fake accounts record recommendations, with no real history. | Ribeiro 2020, Haroon 2022 | Contested |
| Log and panel data | Real behavior is tracked over time, without random assignment. | Anderson 2020, Nguyen 2014, Hosseinmardi 2021 | Established |
| Model or simulation | A formal model predicts how choices and feedback loops play out. | Fleder and Hosanagar 2009, Aridor 2020, Ribeiro 2023 | Established |

## What the evidence shows
### Finding 1: Personalization narrows one user's variety but widens variety across users.
- **Holtz 2020** (Holtz et al., 2020): About 900,000 Spotify users got podcast recommendations based on music history, or popular picks. Individual variety fell 11.51%, and total variety rose 5.96%.
- **Lee and Hosanagar 2019** (Lee and Hosanagar, 2019): A randomized test on a retail site with over 1.1 million users. Collaborative filtering lowered total sales variety.
- **Fleder and Hosanagar 2009** (Fleder and Hosanagar, 2009): A model shows individual variety can rise while total sales variety falls.
- **Strength:** Medium. Two randomized studies on two platforms agree on the split, but both are short and one is a model.

### Finding 2: Feed switches move attitudes little in short trials.
- **Guess 2023** (Guess et al., 2023): About 23,000 Facebook and 21,000 Instagram users got a chronological feed for about three months. Polarization and political knowledge did not change.
- **Liu 2025** (Liu et al., 2025): About 9,000 participants saw changed recommendations on a mock video platform. Short exposure did not measurably shift policy attitudes.
- **Strength:** Medium. Two large randomized trials agree on nulls, but both cover one election or one short window.

### Finding 3: Some trials find real shifts when the algorithm is on.
- **Gauthier 2026** (Gauthier et al., 2026): About 5,000 US X users got an algorithmic or chronological feed for seven weeks. Turning the algorithm on moved policy views rightward, and turning it off did not reverse this.
- **Milli 2025** (Milli et al., 2025): Ranking by stated preferences showed less angry and partisan content than engagement ranking.
- **Strength:** Low. One randomized study finds a shift, and the second tests ranking objectives, not taste.

### Finding 4: Audits disagree about size, and the design explains much of the gap.
- **Ribeiro 2020** (Ribeiro et al., 2020): Untrained sock puppets found some pathways from moderate to extreme channels.
- **Hosseinmardi 2024** (Hosseinmardi et al., 2024): Counterfactual bots show recommendations alone reduce partisan viewing on average.
- **Ribeiro 2023** (Ribeiro et al., 2023): A simulation shows audits that ignore user preferences overstate amplification.
- **Strength:** Medium. Several designs point the same way, but the causal bot study is the strongest.

## Where researchers disagree
| Question | View A (short names) | View B (short names) | What would settle it |
|----------|----------------------|----------------------|----------------------|
| Do recommenders narrow one user's tastes? | Holtz 2020 finds individual variety falls 11.5%. | Nguyen 2014 finds recommendation users narrow less than non-users. | A trial with a no-recommendation control and long follow-up. |
| Do feeds shift political attitudes? | Gauthier 2026 finds a rightward shift with the algorithm on. | Guess 2023 and Liu 2025 find no attitude change. | Replications on other platforms and longer windows. |
| Do audits overstate amplification? | Ribeiro 2020 finds extreme pathways. | Hosseinmardi 2024 and Ribeiro 2023 find smaller effects. | Trained-bot audits with matched controls on several platforms. |

## Gaps
| Gap | Why it matters | Closest existing work (short name) |
|-----|----------------|------------------------------------|
| Multi-year taste change in music or video | Short trials may miss slow narrowing. | Porcaro 2022 runs 12 weeks. |
| A true no-recommendation control | Popularity-based controls may hide the effect size. | Holtz 2020 uses popularity-based controls. |
| Persistence after a switch-off | Lasting effects drive long-run welfare. | Gauthier 2026 shows followed accounts persisted. |
| Personalization by LLM chatbots and taste | Large language model assistants may shape tastes faster. | None found in these searches. |

## Papers cited
Table lists each short name, its exact title, and how the summary was read.

| Short name | Full title | Year | Venue | How we read it |
|------------|------------|------|-------|----------------|
| Holtz 2020 | **The Engagement-Diversity Connection: Evidence from a Field Experiment on Spotify** | 2020 | ACM Conference on Economics and Computation, or arXiv preprint | abstract |
| Lee and Hosanagar 2019 | **How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment** | 2019 | Information Systems Research | abstract (search summary) |
| Anderson 2020 | **Algorithmic Effects on the Diversity of Consumption on Spotify** | 2020 | The Web Conference (WWW) | search summary |
| Nguyen 2014 | **Exploring the filter bubble: the effect of using recommender systems on content diversity** | 2014 | The Web Conference (WWW) | blog and search summary |
| Aridor 2020 | **Deconstructing the Filter Bubble: User Decision-Making and Recommender Systems** | 2020 | ACM Conference on Recommender Systems | search summary |
| Fleder and Hosanagar 2009 | **Blockbuster Culture's Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity** | 2009 | Management Science | search summary |
| Ribeiro 2020 | **Auditing radicalization pathways on YouTube** | 2020 | ACM Conference on Fairness, Accountability, and Transparency | secondary summary |
| Hosseinmardi 2021 | **Examining the consumption of radical content on YouTube** | 2021 | Proceedings of the National Academy of Sciences | search summary |
| Hosseinmardi 2024 | **Causally estimating the effect of YouTube's recommender system using counterfactual bots** | 2024 | Proceedings of the National Academy of Sciences | search summary |
| Porcaro 2022 | **Assessing the Impact of Music Recommendation Diversity on Listeners: A Longitudinal Study** | 2022 | arXiv preprint | abstract |
| Liu and Cong 2022 | **The Daily Me Versus the Daily Others: How Do Recommendation Algorithms Change User Interests? Evidence from a Knowledge-Sharing Platform** | 2022 | Journal of Marketing Research | search summary |
| Guess 2023 | **How do social media feed algorithms affect attitudes and behavior in an election campaign?** | 2023 | Science | secondary summary |
| Liu 2025 | **Short-term exposure to filter-bubble recommendation systems has limited polarization effects: Naturalistic experiments on YouTube** | 2025 | Proceedings of the National Academy of Sciences | secondary summary |
| Gauthier 2026 | **The political effects of X's feed algorithm** | 2026 | Nature | press and search summary |
| Milli 2025 | **Engagement, user satisfaction, and the amplification of divisive content on social media** | 2025 | PNAS Nexus | secondary summary |
| Huszár 2022 | **Algorithmic amplification of politics on Twitter** | 2022 | Proceedings of the National Academy of Sciences | search summary |
| Ribeiro 2023 | **The Amplification Paradox in Recommender Systems** | 2023 | ICWSM | search summary |
| Haroon 2022 | **YouTube, The Great Radicalizer? Auditing and Mitigating Ideological Biases in YouTube Recommendations** | 2022 | arXiv preprint | search summary |

<details><summary>Original research question</summary>

What causal field or quasi-experimental evidence exists on whether recommenders or personalization change users' long-run tastes or consumption diversity (e.g. Spotify diversity studies, Holtz et al. podcast experiment, Aridor et al. MovieLens filter-bubble deconstruction, Fleder & Hosanagar, Lee & Hosanagar, YouTube/Twitter audits, Meta 2020 election feed experiments, Ribeiro et al.)? Which way do effects go, how large, and how do these reconcile with theory predicting amplification? Resolve the tension between amplification theory and the mostly null or mixed field results.

</details>
