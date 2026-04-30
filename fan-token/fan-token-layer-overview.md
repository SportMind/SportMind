# Fan Token™ Intelligence — SportMind Layer 3

> AI-powered sports intelligence connecting on-chain fan token data, transfer markets,
> athlete social activity, on-pitch performance, off-pitch development, and commercial
> brand strategy into a unified, queryable layer for clubs, agents, athletes, and brands.

**Before loading any Layer 3 skill, read `fan-token/fan-token-why.md`.**
It explains why fan tokens exist as a category, what structural problems they solve
that the traditional sports model cannot, and where the trajectory leads. An agent
or developer who understands the thesis will reason differently about everything
the skills in this layer produce.

---

## The sixteen skills

```
GROUND TRUTH LAYERS
┌──────────────────────┐   ┌──────────────────────┐
│  fan-token-pulse     │   │  performance-on-pitch │
│  HAS · TVI · Geo     │   │  PI · Form · Metrics  │
└──────────┬───────────┘   └──────────┬────────────┘
           │                          │
INTELLIGENCE LAYERS
┌──────────────────────────────────────────────────────────┐
│ transfer-intelligence │ athlete-social-activity          │
│ TVS · APS · Loan      │ SHS · AGI · Sentiment · Voice    │
├───────────────────────┼──────────────────────────────────┤
│ performance-off-pitch │ athlete-social-lift               │
│ DTS · TAI · Rehab     │ AELS · Platform Lift             │
└───────────────────────┴──────────────────────────────────┘
           │                          │
SYNTHESIS LAYERS
┌──────────────────────┐   ┌──────────────────────┐
│  transfer-signal     │   │  brand-score          │
│  RCS · TSI · APS     │   │  ABS · Brief · Peers  │
└──────────────────────┘   └──────────┬────────────┘
                                      │
MONETISATION LAYER
┌──────────────────────────────────────────────────────────┐
│  sports-brand-sponsorship   │  sponsorship-match          │
│  Rate · Deal · ROI · Audit  │  AFS · Token activations    │
└─────────────────────────────┴────────────────────────────┘

SPORT-SPECIFIC BRIDGE SKILLS
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  football-   │ │  formula1-   │ │    mma-      │ │   esports-   │
│  token-intel │ │  token-intel │ │  token-intel │ │  token-intel │
│  FTIS·NCSI  │ │  FTIS·CTI   │ │  FighterTIS  │ │  OrgTIS·GRM  │
│  ATM·WC2026 │ │  DTM·Regs   │ │  FTM·CRI    │ │  PRS·RSI    │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘

TEMPORAL / LIFECYCLE LAYER
┌──────────────────────────────┐   ┌──────────────────────────────┐
│  fan-token-lifecycle         │   │  fan-token-partnership-intel  │
│  6 phases · CEX/DEX model   │   │  PHS · Due diligence          │
│  Non-contractual framework  │   │  Termination patterns · Cases │
│  Prediction market utility  │   │  Relaunch pathway · Community │
└──────────────────────────────┘   └──────────────────────────────┘
```

**Rule:** `fan-token-pulse` always runs first in any commercial chain.
`performance-on-pitch` always runs first in any performance chain.

---

## All core metrics

| Metric | Skill | Definition |
|--------|-------|------------|
| **HAS** | fan-token-pulse | Holder Activity Score |
| **TVI** | fan-token-pulse | Token Velocity Index |
| **PI** | performance-on-pitch | Performance Index — position-weighted quality |
| **DTS** | performance-off-pitch | Development Trajectory Score |
| **TAI** | performance-off-pitch | Training Adaptation Index |
| **PS** | performance-off-pitch | Professionalism Signal |
| **TVS** | transfer-intelligence | Transfer Viability Score |
| **DLVS** | transfer-intelligence | Development Loan Value Score |
| **SHS** | athlete-social-activity | Social Health Score |
| **AGI** | athlete-social-activity | Audience Growth Index |
| **AELS** | athlete-social-lift | Athlete Engagement Lift Score |
| **APS** | transfer-signal / transfer-intelligence | Athlete Portability Score |
| **ABS** | brand-score | Athlete Brand Score |
| **AFS** | sponsorship-match | Audience Fit Score |

---

## Skills at a glance

### Ground truth layers

**`fan-token-pulse`** — On-chain ground truth. Chiliz Chain + Socios Connect API + Kayen DEX. Produces HAS, TVI, geographic holder map, velocity classification. Required by all commercial chains.

**`performance-on-pitch`** — Match statistical intelligence. API-Football, FBref, StatsBomb. Position-weighted PI, form trajectory, xG/xA, progressive carries, pressures, physical profile, injury risk, scout report. Valuation multiplier for transfer-intelligence.

### Intelligence layers

**`transfer-intelligence`** — Full transfer lifecycle. Valuation vs. fee, contract risk (sell-on, release clause, buy-back), loan analysis (DLVS + return readiness), fan sentiment delta, post-transfer trajectory. Richer than transfer-signal.

**`athlete-social-activity`** — Comprehensive social intelligence. Content mix, brand voice profile, 90-day sentiment trend, influence network map, crisis early warning. Produces SHS + AGI. Broader than athlete-social-lift.

**`performance-off-pitch`** — Development intelligence. Training load, loan spell analysis, new club adaptation (TAI), youth pathway, rehabilitation phases, professionalism signals. Produces DTS, TAI, PS.

**`athlete-social-lift`** — Social-to-token correlation. Measures whether athlete posts move fan token holders. Produces AELS by platform and content type.

### Sport-specific bridge skills

**`football-token-intelligence`** — Football's dedicated fan token intelligence layer.
FTIS, NCSI (National-Club Spillover Index), ATM. Competition impact matrix, World Cup 2026 dual-token framework, friendly signal logic, multi-token fixtures.
→ `football-token-intelligence/football-token-intelligence.md`

**`formula1-token-intelligence`** — F1 constructor and driver token intelligence.
FTIS, Constructor Token Index (CTI), Driver Token Multiplier (DTM). Race-by-race FTIS, regulation cycle position, silly season transfer scoring, dual-championship-battle logic.
→ `formula1-token-intelligence/formula1-token-intelligence.md`

**`mma-token-intelligence`** — Fighter token intelligence for MMA.
FighterTIS, Fighter Token Multiplier (FTM), Career Risk Index (CRI). Fight week signal map, weigh-in binary risk assessment, post-fight trajectory by method of victory, existential risk framework.
→ `mma-token-intelligence/mma-token-intelligence.md`

**`esports-token-intelligence`** — Organisation token intelligence for esports.
OrgTIS, Game Roster Multiplier (GRM), Patch Risk Score (PRS), Roster Stability Index (RSI). Multi-game calendar, October-November stack window, game-by-game tournament tiers, relegation vs qualification distinction.
→ `esports-token-intelligence/esports-token-intelligence.md`

### Synthesis layers

**`transfer-signal`** — Token-native transfer intelligence. Rumour confidence scoring with source tier weighting (Romano = Tier 1), spike attribution, athlete portability to fan suites.

**`brand-score`** — Synthesis skill. Combines HAS + AELS + APS + REACH + SENTI into ABS. Exportable commercial brief with peer comparison and trend signal.

### Monetisation layer

**`sports-brand-sponsorship`** — Full commercial deal intelligence. Market rate benchmarking by tier and category, deal structure with KPIs and performance bonuses, portfolio conflict audit, ROI framework, token-native integration layer.

**`sponsorship-match`** — Audience-brand alignment from token data. AFS per brand category, geographic commercial priorities, token-native activation templates.

---

## Agent chain examples

**Full transfer decision:**
`performance-on-pitch → transfer-intelligence → fan-token-pulse (destination) → athlete-social-lift → brand-score`

**Loan spell review:**
`performance-on-pitch (at loan club) → performance-off-pitch → transfer-intelligence`

**Full commercial brief:**
`fan-token-pulse → performance-on-pitch → athlete-social-activity → athlete-social-lift → brand-score → sports-brand-sponsorship`

**Which squad player is highest commercial value:**
`fan-token-pulse → athlete-social-activity (squad) → athlete-social-lift (squad) → brand-score (ranked)`

**Token spike attribution:**
`fan-token-pulse → transfer-signal`

**Injury return readiness:**
`performance-off-pitch → performance-on-pitch (recent matches)`

**World Cup 2026 player brief:**
`fan-token-pulse (national token) → performance-on-pitch → athlete-social-activity → brand-score → sports-brand-sponsorship`

**Is this deal worth signing?:**
`performance-on-pitch → transfer-intelligence → fan-token-pulse (destination) → performance-off-pitch`

---

## Reference files

| File | Location | Purpose |
|------|----------|---------|
| Token registry | `fan-token-pulse/references/chiliz-token-registry.md` | CAP-20 addresses for 30+ clubs + national teams |
| API response shapes | `fan-token-pulse/references/chiliz-api-response-shapes.md` | Parsing guide + HAS JS implementation |
| Social API setup | `athlete-social-lift/references/social-platform-api-setup.md` | Platform auth and rate limits |
| Transfer source tiers | `transfer-signal/references/journalist-source-tiers.md` | Journalist credibility weights |
| League medians | `brand-score/references/social-following-league-medians.md` | Social following + HAS medians by league |
| Activation templates | `sponsorship-match/references/token-activation-templates.md` | Token-native campaign templates |
| Metric definitions | `performance-on-pitch/references/advanced-metric-definitions.md` | xG, xA, progressive carries, PSxG etc. |
| Adaptation timelines | `performance-off-pitch/references/transfer-adaptation-timelines.md` | Transfer type adaptation curves |
| Valuation benchmarks | `transfer-intelligence/references/transfer-fee-benchmarks.md` | Fee benchmarks by position/league/age |
| Contract templates | `transfer-intelligence/references/contract-clause-templates.md` | Clause types and risk frameworks |
| Deal benchmarks | `sports-brand-sponsorship/references/sponsorship-deal-benchmarks.md` | Disclosed sponsorship values by tier/category |
| Contract clauses | `sports-brand-sponsorship/references/endorsement-contract-clauses.md` | Endorsement clause library |

---

## Infrastructure

### Environment variables

```bash
SOCIOS_PARTNER_KEY=
CHILIZ_RPC_URL=https://rpc.ankr.com/chiliz
RAPIDAPI_KEY=
STATSBOMB_USER=
STATSBOMB_PASS=
X_BEARER_TOKEN=
INSTAGRAM_ACCESS_TOKEN=
TIKTOK_API_KEY=
YOUTUBE_API_KEY=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
BRANDWATCH_API_KEY=        # optional
SPARKTORO_API_KEY=         # optional
CLEARBIT_API_KEY=          # optional
```

---

## Status

Layer 3 is complete at v2.1.0 with 16 skills across six categories.
See `CHANGELOG.md` for full version history and `sportmind-overview.md` for
the complete library roadmap including v3.0 planned additions.

**Current skills:** fan-token-pulse, performance-on-pitch, performance-off-pitch,
athlete-social-lift, athlete-social-activity, transfer-signal, transfer-intelligence,
brand-score, sponsorship-match, sports-brand-sponsorship, football-token-intelligence,
formula1-token-intelligence, mma-token-intelligence, esports-token-intelligence,
fan-token-lifecycle, fan-token-partnership-intelligence

**Upcoming (v3.0):** ML-calibrated signal weights, real-time utility event monitoring,
skill registry API, multi-language support (Spanish, Portuguese, French, Arabic, Hindi)

---

*SportMind Layer 3 — the full picture of an athlete, from the blockchain to the boardroom.*

---

## Lifecycle and partnership intelligence — Layer 3 temporal framework

The skills above address the **active state** of a fan token. Two additional skills
address the **temporal dimension** — how a token's intelligence profile changes
across its full lifecycle:

### `fan-token/fan-token-lifecycle`
The complete lifecycle framework. Documents six phases from pre-launch through
post-partnership continuation. The central insight: fan tokens cannot be cancelled —
they are on-chain assets that transition from governance utility to predictive utility
when official partnership infrastructure ends.

Key concepts:
- Six-phase lifecycle model (pre-launch → active utility → plateau → non-contractual)
- Lifecycle-adjusted Layer 3 signal weights (which metrics apply at each phase)
- The non-contractual token principle: post-partnership on-chain persistence
- Prediction market as post-partnership utility form
- CEX/DEX trajectory model for non-contractual tokens
- On-chain holder data as persistent fan sentiment intelligence
- The open primitive model: third-party use cases without club approval

### `fan-token/fan-token-partnership-intelligence`
The partnership relationship framework. Documents new partnership signals,
health monitoring, termination events, and non-contractual token case studies.

Key concepts:
- Partnership quality assessment (due diligence before token launch)
- Partnership Health Score (PHS): five-indicator composite
- Tier 1–5 new partnership signal taxonomy with CHZ impact ranges
- Termination patterns: announced, silent lapse, forced, category exit
- Case studies: Type A (active partnerships under stress: $JUV, $ACM), Type B (uncertain status: $FAZE, ISL tokens), Type C (confirmed non-contractual: smaller club tokens)
- IMPORTANT: $JUV and $ACM are ACTIVE Socios/Chiliz partnerships — used as Type A behavioural case studies only
- The relaunch pathway: non-contractual to re-contractual
- Community empowerment: why non-contractual communities are intelligence assets

### The non-contractual token in prediction markets

A fan token that has lost official partnership utility is not worthless —
it is **utility-decoupled**. It continues to exist on-chain, continues to trade,
and continues to correlate with sporting performance. Prediction markets,
GameFi applications, and third-party developers can build on these tokens
without requiring official club approval. The prediction market form of
utility (price as aggregate sporting sentiment signal) may be more durable
than governance utility because it requires only: (1) the token continues
to trade, and (2) the club continues to play sport. Both outlast any
specific commercial partnership.
