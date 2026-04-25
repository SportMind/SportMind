# Academic References — SportMind

**The peer-reviewed evidence base underpinning SportMind's frameworks.**

This file is the canonical academic source registry for the library. Each paper
is listed with the SportMind files it validates and a note on its specific
contribution. New papers are registered here when integrated into the library.

For citation format within skill files, use the block-level pattern:
```
**Source: Author et al. (Year), Journal. Methodology and key finding.**
```

---

## How citations work in SportMind

Academic citations appear in SportMind skill files only where a specific
quantitative claim, framework structure, or empirical finding is drawn from
external peer-reviewed research. They do not appear on every paragraph —
most SportMind frameworks are the library's own constructs. Citations mark
the points where SportMind's reasoning is grounded in observed data.

The pattern: source attribution appears as a labelled block above the
section it validates. Agents loading skills treat cited claims as
empirically grounded; uncited claims are SportMind design decisions.

---

## Cluster 1 — Finance, Economics, Risk and Returns

**1. Scharnowski, M., Scharnowski, S., & Zimmermann, L. (2023)**
"Fan tokens: Sports and speculation on the blockchain."
*Journal of International Financial Markets, Institutions and Money*, 89, 101880.
— First major economic analysis of fan tokens as financial assets. Establishes
the dual nature (sports engagement + speculative asset). Foundation for
`fan-token/fan-token-why.md` treatment of the financial layer.

**2. Demir, E., Ersan, O., & Popesko, B. (2022)**
"Are Fan Tokens™ Fan Tokens?"
*Finance Research Letters*, 47, 102736.
— Match outcomes produce abnormal returns. UCL losses generate stronger negative
returns than wins generate positive returns. Empirical basis for the loss-effect
asymmetry in `core/post-match-signal-framework.md`.

**3. Ersan, O., Demir, E., & Assaf, A. (2022)**
"Connectedness among fan tokens and stocks of football clubs."
*Research in International Business and Finance*, 63, 101780.
— Documents the statistical connectedness between fan token prices and football
club equity prices. Empirical foundation for `market/sports-equity-intelligence.md`
cross-instrument signal framework.

**4. Vidal-Tomás, D. (2023)**
"Blockchain, sport and fan tokens."
*Journal of Economic Studies*, 51(1), 24–38.
— Performance analysis, bubble phenomenon, and Chiliz ecosystem dynamics.
Relevant to `fan-token/fan-token-exchange-intelligence.md` overheating signals.

**5. Mazur, M., & Vega, M. (2023)**
"Football and Cryptocurrencies."
*The Journal of Alternative Investments*, 26(1), 23–38.
— 150% average first-day returns at listing; long-run underperformance documented.
Direct empirical backing for the three-phase listing price pattern in
`fan-token/fan-token-exchange-intelligence.md` (New Listing Intelligence section).

**6. Ante, L., Schellinger, B., & Demir, E. (2024)**
"The impact of football games and sporting performance on intra-day fan token returns."
*Journal of Business Economics*, 94(5), 813–850.
— Intraday event study, 8 fan tokens, 325 matches. Loss-effect asymmetry quantified:
losses generate −0.8% during matches, −0.7% post-match; wins generate smaller
positive returns. PATH_2 supply-neutral ≠ sentiment-neutral. Draw disappointment
discount = 0.92. Cited in `core/post-match-signal-framework.md` and
`fan-token/fan-token-why.md`.

**7. Saggu, A., Ante, L., & Demir, E. (2024)**
"Anticipatory gains and event-driven losses in blockchain-based fan tokens:
Evidence from the FIFA World Cup."
*Research in International Business and Finance*, 70, 102333.
— Pre-tournament anticipatory price gains; losses after elimination larger
than wins from advancement. Empirical validation of the NCSI pre-tournament
amplifier and CALENDAR_COLLAPSE mechanics in `fan-token/world-cup-2026-intelligence/`
and the anticipatory gain model in `fan-token/fan-token-exchange-intelligence.md`.

**8. Assaf, A., Demir, E., & Ersan, O. (2024)**
"Detecting and date-stamping bubbles in fan tokens."
*International Review of Economics & Finance*, 92, 98–113.
— GSADF-based bubble detection methodology applied to fan tokens. Relevant to
exchange overheating signals in `fan-token/fan-token-exchange-intelligence.md`
and liquidity risk assessment in `fan-token/defi-liquidity-intelligence/`.

**9. Foglia, M., Maci, G., & Pacelli, V. (2024)**
"FinTech and fan tokens: Understanding the risks spillover of digital asset investment."
*Research in International Business and Finance*, 68.
— Risk spillover between fan tokens and broader crypto markets. Informs CHZ macro
state modelling in `market/sports-equity-intelligence.md`.

**10. Esparcia, C., & Díaz, A. (2024)**
"The football world upside down: Traditional equities as an alternative for
the new fan tokens? A portfolio optimization study."
*Research in International Business and Finance*, 71.
— Football equities and fan tokens as complementary portfolio instruments.
Cross-instrument portfolio perspective in `market/sports-equity-intelligence.md`.

**11. Shao, S-F., & Cheng, J. (2025)**
"Time-varying connectedness between sport cryptocurrency and listed European
football stocks: evidence from a LASSO-VAR approach."
*Applied Economics*.
— Time-varying (not static) connectedness confirmed. The equity-token signal
relationship changes across market regimes. Extends `market/sports-equity-intelligence.md`
signal type framework with regime-dependence caveat.

**12. Agnese, P., & Xiao, Y. (2025)**
"Tokenization in soccer leagues. Is fan engagement for real?"
*Research in International Business and Finance*, 76.
— Argues fan tokens are fan-driven, not primarily crypto-speculative. Governance
participation and club activity are the dominant price drivers in non-bubble
periods. Supports the geographic alignment signal in New Listing Intelligence.

**13. Lubian, D. (2023)**
"Exuberance, Asymmetric Volatility and Connectedness in Fan Tokens."
*Journal of Quantitative Finance and Economics*, 5(1), 73–92.
— Asymmetric volatility confirmed: downside volatility exceeds upside for fan
tokens. Reinforces loss-effect asymmetry and the EDLI risk model.

**14. Dedousi, O., & Fassas, A. (2025)**
"Herd behavior in digital asset markets: Evidence from fan tokens."
*Review of Behavioral Finance*, 17(3), 524–543.
— Herding behaviour confirmed in fan token markets, amplified during high-volume
sporting events. Relevant to post-listing normalisation dynamics and MRS
manipulation detection in `platform/fraud-signal-intelligence.md`.

**15. Alaminos, D. et al. (2025)**
"Deep Neural Networks and Fan Tokens' Pricing in Football Clubs."
*SAGE Journals*.
— Neural network price modelling of fan tokens. On-chain activity and club
social engagement are the most predictive features. Supports CHI as a primary
CDI driver in `fan-token/fan-holder-profile-intelligence.md`.

**16. Öget, E., Kanat, E., & Kaya, F. (2024)**
"The determinants of prices of fan tokens as a new sports finance tool."
*Ege Academic Review*, 24(2), 221–232.
— Sporting success and transaction volume are the dominant price determinants.
Match result → price relationship quantified. Cited alongside Demir et al. (2022)
for signal weight calibration.

**17. Kanat et al. (2024)**
Pooled Mean Group / ARDL study on determinants of fan token prices.
— Long-run cointegration between sporting success, transaction volume, and price
confirmed. Strengthens the Signal Modifiers chain in `core/sportmind-score.md`.

**18. Teker, T., & Konuşkan, A. (2022)**
"Association effect on fan token prices."
*International Journal of Business, Economics and Management Perspectives*, 6(2), 359–376.
— Club association and partnership announcements move fan token prices. Supports
the partnership signal model in `fan-token/fan-token-partnership-intelligence/`.

**22. (2026)**
"Higher moment risk transmission in token markets."
*Applied Economics*.
— Higher-order risk transmission between fan tokens. Extends the risk spillover
framework relevant to multi-token portfolio monitoring.

**23. (2026)**
"Dynamic quantile frequency connectedness and dependence between global football
club fan tokens, cryptocurrencies, and uncertainty indices."
*Empirical Economics* (Springer).
— Frequency-domain connectedness. Confirms CHZ as a macro layer that transmits
to individual tokens with different time horizons.

**24. (2026)**
"From the pitch to the market: what determines fan token prices dynamics and
trading activities?"
*Cogent Social Sciences / Tandfonline*.
— Most recent determinants study. On-pitch performance remains primary driver;
exchange infrastructure second.

---

## Cluster 2 — Consumer Behaviour, Fan Identity, Marketing

**25. Manoli, A. E., Dixon, K., & Antonopoulos, G. A. (2024)**
"Football Fan Tokens as a mode of 'serious leisure': unveiling the dual essence
of identity and investment."
*Leisure Studies*.
— 60-participant qualitative study, 10 focus groups. The identity-investment duality
is the empirical foundation for the Loyalist/Speculator/Governor/Amplifier archetype
framework in `fan-token/fan-holder-profile-intelligence.md`. The study Chiliz
publicly engaged with. Cited here and in the holder profile file.

**26. Vollero, A., Sardanelli, D., & Manoli, A. E. (2025)**
"Exploring the Influence of Football Fan Tokens on Engagement: A Study on Fans'
Meaning, Team Brand Identification, and Cocreation Mechanisms."
*Journal of International Marketing / SAGE*.
— Team brand identification moderates engagement. Co-creation (poll participation,
governance) is more engagement-sustaining than passive holding. Supports CHI
trajectory as the primary health signal in `fan-token/fan-holder-profile-intelligence.md`.

**27. Marques, F., Sousa, A., & Barbosa, B. (2026)**
"Factors influencing fan token purchase intent in sports fandom."
*International Journal of Sports Marketing and Sponsorship*, 27(6), 16–35.
— Purchase intent study. Club loyalty and perceived governance influence are the
two strongest predictors of token acquisition. Supports geographic alignment signal.

**28. Stegmann, P., Matyas, D., & Ströbel, T. (2023)**
"Hype or opportunity? Tokenization as engagement platform in sport marketing."
*International Journal of Sports Marketing and Sponsorship*, 24(4), 722–736.
— Engagement platform potential confirmed. Value depends on sustained club
commitment to token utility. Supports plateau warning signals in
`fan-token/fan-token-lifecycle/`.

**29. Chen, C. (2025)**
"Contesting fan tokens under crypto-capitalism: how sport NFT furthers the
hypercommodification of fandom."
*International Journal of Sports Marketing and Sponsorship*, 26(2), 254–272.
— Digital ethnography of Manchester City, Everton, and Crystal Palace fan token
holders. First qualitative study of Premier League fan token communities. Relevant
to CPFC and EFC holder profile intelligence and the PL gap discussion in
`market/market-football.md`.

**30. Baldi, G., Botti, A., & Carrubbo, L. (2023)**
"Sentiment and Deep Learning Content Analysis of a Digital Fan Token Platform:
An Exploratory Study."
*Springer RIIFORUM 2023*.
— Sentiment analysis of fan token platform content. Social sentiment predicts
short-term price moves. Supports the KOL influence model in
`fan-token/kol-influence-intelligence/`.

**33. Fındıklı, S., & Saygın, E. P. (2021)**
"Fan tokens in the context of consumer citizenship."
*Third Sector Social Economic Review*, 56(1), 57–71.
— Early framework paper positioning fan tokens as consumer citizenship tools.
Foundational for understanding the governance participation motivation in
`fan-token/sports-governance-intelligence/`.

---

## Cluster 3 — Blockchain, Information Systems, Frameworks

**34. Ante, L., Schellinger, B., & Wazinski, F.-P. (2023)**
"Enhancing Trust, Efficiency, and Empowerment in Sports: Developing a
Blockchain-Based Fan Token Framework."
*European Conference on Information Systems (ECIS 2023)*.
— The 3-layer framework (trust/efficiency, utility, financialization). The
structural model that informed SportMind's fan token lifecycle phase design.
Cited in `fan-token/fan-token-lifecycle/fan-token-lifecycle.md`.

**35. Ante, L., Saggu, A., Schellinger, B., & Wazinski, F.-P. (2024)**
"Voting participation and engagement in blockchain-based fan tokens."
*Electronic Markets*, 34(1).
— Analysis of 3,576 polls across fan token platforms. Average 4,003 participants
per poll. Governance participation data is the empirical backing for the CHI
governance signal in `fan-token/fan-holder-profile-intelligence.md` and
the agent notification sequences in `fan-token/sports-governance-intelligence/`.

**36. Schellinger, B., Ante, L., & Bauers, S. B. (2022)**
"Blockchain use cases and concepts in sports: A systematic review."
*ECIS 2022*.
— Systematic taxonomy of blockchain applications in sport. Foundation for the
scope delineation between fan tokens and other blockchain sports applications.

**37. Berkani, A. S. et al. (2024)**
"Blockchain use cases in the sports industry: A systematic review."
— Companion review to Schellinger et al. (2022). Confirms fan tokens as the
dominant active blockchain use case in sport.

---

## Cluster 4 — Systematic Reviews

**41. Zhou, X., Tao, Y., Huang, L., et al. (2026)**
"Cryptocurrency in sport: a thematic review."
*Frontiers in Psychiatry*.
— 30 peer-reviewed studies mapped across 5 thematic strands. The most recent
comprehensive synthesis. Used as a meta-source in `core/post-match-signal-framework.md`
and `fan-token/fan-token-why.md`. Confirms loss-effect asymmetry as the most
replicated finding in the field.

**42. Principe, V. A., de Souza Vale, R. G., & Nunes, R. D. A. M. (2024)**
"Blockchain and sports industry: a systematic literature review of Fan Tokens
and their implications."
*Retos: Nuevas Tendencias en Educación Física, Deporte y Recreación*, 60, 823–840.
— PRISMA-based systematic review. Confirms the dominance of finance/econometrics
research and the relative absence of US academic work.

**43. Ante, L. et al. (2024/2025)**
"Fungible and Non-Fungible Tokens in Sports."
Springer (book chapter systematic review).
— Comprehensive treatment distinguishing fan tokens from NFTs in sport.
Foundational for scope clarity in the library.

---

## Cluster 5 — Regulation, Gambling, Consumer Protection

**45. Lopez-Gonzalez, H., & Griffiths, M. D. (2023)**
"Gambling-like Features in Fan Tokens."
*Journal of Gambling Studies*, 39(4), 1579–1596.
— FC Barcelona case study. Identifies structural parallels between fan token
mechanics and gambling product features. Cited in `fan-token/fan-token-why.md`
as the regulatory risk that Fan Token Play PATH_2 was designed to address.

**46. Lopez-Gonzalez, H., & Petrotta, B. (2024)**
"Gambling-like digital assets and gambling severity: A correlational study with
U.S. sports bettors consuming cryptocurrencies, NFTs, and fan tokens."
*International Gambling Studies*.
— US-specific study. Relevant to US market regulatory context in
`macro/macro-regulatory-sportfi.md`. Confirms the harm-reduction argument for
the SEC/CFTC digital collectibles classification (March 2026).

**48. Bason, T., Petratos, P., Porreca, R., & Babu, M. M. (2023)**
Centre for Business in Society White Paper.
— Regulatory issues in fan tokens. Policy-level document relevant to
`macro/macro-regulatory-sportfi.md`.

---

## Field overview — key facts for agents

```
FIELD SIZE AND PACE:
  First peer-reviewed fan token paper: 2022
  Papers by end of 2025: ~30–35 English-language peer-reviewed studies
  Q1 2026 alone: 5+ new papers — field accelerating rapidly

MOST REPLICATED FINDING:
  Loss-effect asymmetry — confirmed across at least 6 independent studies.
  Losses generate materially larger negative returns than equivalent wins
  generate positive returns. This is the most robust empirical finding in
  the field and is directly incorporated into SportMind's signal chain.

DOMINANT RESEARCH METHOD:
  Finance/econometrics (~45% of papers) — event studies, GARCH models,
  connectedness frameworks (DCC-GARCH, LASSO-VAR, GSADF).

FASTEST-GROWING AREA:
  Consumer behaviour and marketing — qualitative studies of actual holders.
  This is where SportMind's holder archetype model finds its empirical grounding.

MOST CITED AUTHORS:
  Lennart Ante (Blockchain Research Lab, Germany)
  Ender Demir, Oguz Ersan, Aman Saggu, Benjamin Schellinger
  David Vidal-Tomás, Matthias & Stefan Scharnowski
  Argyro Manoli, Hibai Lopez-Gonzalez

KEY GAP IN LITERATURE:
  Very limited US academic work. Most research is European (Italy, Germany,
  Spain, UK, Portugal) and Turkish. Minimal academic work on tokenised
  sports finance / RWA — that space remains industry-driven.
  This is partly why SportMind's WC2026 and US market modules are built
  primarily from regulatory and industry sources rather than academic ones.

SPORTMIND COVERAGE NOTE:
  Every quantitative claim in this library that derives from academic research
  is traceable to a source in this file. Claims not sourced here are either
  SportMind design decisions or industry-observed data. The library never
  presents unsourced claims as empirically validated.
```

---

*Last updated: v3.83.0 — April 2026*
*52 papers registered. New papers: update this file and add citation block to relevant skill.*
