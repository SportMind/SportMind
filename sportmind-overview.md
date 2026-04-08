# SportMind

**The open sports intelligence library for AI agents.**

SportMind is a community-built collection of sport-specific skills that teach AI agents
how to reason about sports — how a sport's calendar works, what events drive outcomes,
which variables carry the most risk, how to weight signals intelligently, and how
external forces outside sport itself can override everything else.

It is not a data pipeline. It is not an API. It is **domain knowledge, structured for machines.**

---

## The problem SportMind solves

AI agents that trade fan tokens, run prediction markets, or power sports GameFi apps need
more than raw data. They need to understand *context*:

- That a weigh-in miss in MMA is categorically different from a team losing a regular season game
- That an eSports patch update 10 days before a tournament should reduce confidence in performance signals
- That an NFL quarterback injury report on Wednesday is more predictive than the one on Friday
- That a crypto bear market can make a Champions League winning club's token fall in fiat terms
- That the 2020 pandemic collapsed physical sports revenue while fan token activity increased

This contextual reasoning is currently rebuilt from scratch by every developer in the space.
SportMind is the shared layer — load a skill, and your agent immediately understands the sport,
the athlete, the commercial landscape, and the external forces acting on both.

---

## Structure

SportMind organises intelligence into five complementary layers:

```
sportmind/
│
│  Every file in this library is a skill — a structured reasoning document that
│  teaches an AI agent something it cannot derive from raw data alone. Load a skill
│  into your agent's context and it immediately understands that domain.
│
├── sports/    ← Layer 1: Teaches AI agents HOW each sport works
│              │  Season rhythm, event hierarchy, result impact, risk variables,
│              │  signal weights, and event playbooks — the domain knowledge that
│              │  turns a data signal into a reasoned prediction.
│              │
│   ├── football/       How football's competition tiers, derby weight, and
│   │                   season rhythm should change agent reasoning
│   ├── basketball/     How star-player correlation and playoff series logic
│   │                   differ from regular season — NBA and EuroLeague
│   ├── mma/            How weigh-in outcomes, fight card position, and
│   │                   retirement risk make MMA signals unique
│   ├── esports/        How meta/patch cycles and multi-game org structure
│   │                   require a different intelligence model than any team sport
│   ├── american-football/ How the weekly injury report cadence and
│   │                   quarterback criticality dominate NFL prediction
│   ├── golf/           How cut lines, course history, and the LIV/PGA split
│   │                   change agent reasoning vs standard head-to-head sports
│   ├── boxing/         How four-belt fragmentation, weigh-in binary risk, and
│   │                   promotional uncertainty require separate signal tracks
│   ├── athletics/      How the 4-year Olympic cycle creates boom/bust
│   │                   engagement windows and why world records are catalysts
│   ├── cycling/        How Grand Tour fatigue curves and DNF probability
│   │                   require daily stage-level intelligence
│   ├── horse-racing/   How going conditions, draw bias, and trainer language
│   │                   are the primary predictive variables — not form alone
│   ├── snooker/        How venue specialisation (Crucible effect) and the
│   │                   147 break create unique catalytic signal moments
│   ├── darts/          How the 9-dart finish signal and PDC tour structure
│   │                   create predictable engagement spikes
│   ├── rugby-league/   How the State of Origin disruption and dual NRL/Super
│   │                   League calendar affect player availability windows
│   ├── netball/        How the World Cup cycle and Commonwealth Games
│   │                   concentrate commercial activity for agents to model
│   ├── swimming/       How the Olympic peak model creates 4-year intelligence
│   │                   windows and why year-round signals are low-reliability
│   ├── rowing/         How weather conditions and the Boat Race cultural
│   │                   significance affect prediction confidence
│   ├── winter-sports/  How the Crystal Globe season arc and crash probability
│   │                   create sport-specific risk modifiers
│   ├── cricket/        How format differences (Test/ODI/T20), dew factor,
│   │                   and the India-Pakistan match amplifier work
│   ├── rugby/          How set piece dominance, kicker accuracy zones,
│   │                   and Six Nations home advantage should be weighted
│   ├── tennis/         How surface specialisation splits and H2H surface
│   │                   records are the primary predictive variables
│   ├── formula1/       How constructor dynamics, pit strategy windows,
│   │                   and regulation cycles affect race-by-race prediction
│   ├── baseball/       How pitcher rotation cycles, Statcast metrics, and
│   │                   ballpark factors require a pitcher-first intelligence model
│   ├── ice-hockey/     How the goaltender is the single highest-impact
│   │                   variable and back-to-back games amplify fatigue risk
│   ├── motogp/         How hardware tiers, wet race specialists, and
│   │                   crash probability differ by track and weather
│   ├── afl/            How the dual scoring system, kicking accuracy,
│   │                   and MCG Grand Final context require AU-specific reasoning
│   ├── handball/       How goalkeeper save percentage and financial tier
│   │                   dominance (Barcelona/PSG) shape EHF outcomes
│   ├── kabaddi/        How the star raider modifier and All Out event
│   │                   dynamics make kabaddi structurally unlike any other sport
│   ├── nascar/         How track type taxonomy (superspeedway vs short track)
│   │                   is the primary variable — more than driver form alone
│   └── [14 stubs]      badminton, volleyball, table-tennis, sailing + 10 more
│                       (community contributions welcome — see GOOD_FIRST_ISSUES.md)
│
├── athlete/   ← Layer 2: Teaches AI agents HOW to reason about individuals
│              │  Player availability, form scores, sport-specific modifiers,
│              │  and the composite pipeline that adjusts base signals.
│              │  Each skill produces a modifier (0.55–1.25×) the agent applies
│              │  to any signal before acting. Now covers all 28 complete sports.
│              │
│   ├── football/       How availability, xG form, goalkeeper rating, and
│   │                   lineup confirmation combine into a football modifier
│   ├── mma/            How striking style, grappling record, fight camp
│   │                   signals, and round profile predict fighter performance
│   ├── esports/        How roster stability, HLTV rating, and meta readiness
│   │                   affect esports org-level prediction confidence
│   ├── nfl/            How QB CPOE, O-line health, and Wednesday/Friday
│   │                   injury designation timing determine NFL modifiers
│   ├── nba/            How load management decisions, on/off splits, and
│   │                   clutch performance data modify NBA predictions
│   ├── nhl/            How goaltender start confirmation, special teams,
│   │                   and Corsi drive NHL modifier calculation
│   ├── cricket/        How batter-vs-bowler H2H, pitch type, and toss
│   │                   outcome combine for cricket player modifiers
│   ├── tennis/         How serve metrics, surface record splits, and
│   │                   H2H dynamics produce tennis player modifiers
│   ├── rugby/          How set piece contributions, kicker accuracy zones,
│   │                   and halfback partnership stats modify rugby predictions
│   ├── golf/           How course history, strokes gained categories,
│   │                   and cut line probability define golf player modifiers
│   ├── boxing/         How belt status, weigh-in outcome, fight camp signals,
│   │                   and chin durability combine for boxing modifiers
│   ├── cycling/        How GC standing, course fit, team domestique role,
│   │                   and DNF risk probability affect cycling modifiers
│   ├── athletics/      How form score, world record proximity, doping status,
│   │                   and multi-round fitness affect athletics modifiers
│   ├── horse-racing/   How going preference, course-and-distance record,
│   │                   trainer and jockey combination produce racing modifiers
│   ├── snooker/        How Crucible specialisation, pressure record, and
│   │                   break-building stats define snooker player modifiers
│   ├── darts/          How 3-dart average, checkout percentage, and
│   │                   venue-specific records produce darts modifiers
│   ├── baseball/       How PQS (pitcher), BQS (batter), Statcast profile,
│   │                   and platoon splits combine for baseball modifiers
│   ├── rugby-league/   How PAS, form rating, PIS, and State of Origin
│   │                   disruption modifier work together for NRL/SL players
│   ├── meta/           How to orchestrate across sports — single modifier
│   │                   call when the agent handles multiple sport types
│   ├── formula1/       How qualifying delta, wet weather rating, and
│   │                   regulation fit produce F1 driver modifiers
│   ├── afl/            How kicking accuracy and contested possession
│   │                   determine AFL player modifiers
│   ├── motogp/         How hardware tier, wet weather, and crash probability
│   │                   interact with rider talent in MotoGP modifiers
│   ├── handball/       How goalkeeper save rate and position-specific
│   │                   variables drive EHF handball modifiers
│   ├── kabaddi/        How raider rating and All Out dynamics drive
│   │                   PKL player modifiers
│   ├── nascar/         How track type specialisation drives NASCAR
│   │                   driver modifiers across superspeedway vs short track
│   ├── netball/        How goal shooter accuracy and centre pass conversion
│   │                   produce netball athlete modifiers
│   ├── rowing/         How split time, course conditions, and taper timing
│   │                   produce rowing athlete modifiers
│   ├── swimming/       How PB proximity, taper timing, and multi-event
│   │                   fatigue produce swimming athlete modifiers
│   └── winter-sports/  How course fit, snow conditions, and Olympic cycle
│                       position produce winter sports athlete modifiers
│
├── fan-token/ ← Layer 3: Teaches AI agents HOW to reason about
│              │  on-chain commercial intelligence — from holder activity
│              │  and social lift to brand value, sponsorship fit, and
│              │  the full lifecycle of a fan token partnership.
│              │  Only fully applicable to Tier 1 sports (active tokens).
│              │
│   ├── fan-token-pulse/            How on-chain holder data (HAS, TVI) reveals
│   │                               token health before any sporting signal is applied
│   ├── performance-on-pitch/       How match statistics produce a PI score and
│   │                               inform athlete valuation for commercial decisions
│   ├── performance-off-pitch/      How development trajectory, loan spells, and
│   │                               professionalism signals (DTS, TAI, PS) affect value
│   ├── athlete-social-lift/        How to measure whether an athlete's social
│   │                               activity actually moves token holders (AELS)
│   ├── athlete-social-activity/    How to read an athlete's full social profile —
│   │                               brand voice, SHS, AGI, and crisis early warning
│   ├── transfer-signal/            How transfer rumours should be weighted by source
│   │                               tier and how portability (APS) affects token value
│   ├── transfer-intelligence/      How the full transfer lifecycle — valuation,
│   │                               contract risk, loan analysis — produces TVS and DLVS
│   ├── brand-score/                How to synthesise all signals into an Athlete Brand
│   │                               Score (ABS) and exportable commercial brief
│   ├── sponsorship-match/          How to rank brand categories by audience fit (AFS)
│   │                               and generate token-native activation ideas
│   ├── sports-brand-sponsorship/   How to benchmark deal rates, structure KPIs,
│   │                               audit conflicts, and integrate token-native layers
│   ├── football-token-intelligence/ How competition tier, national-club spillover
│   │                               (NCSI), and athlete multipliers (ATM) drive FTIS
│   ├── formula1-token-intelligence/ How race results, regulation cycle position,
│   │                               and silly season transfers drive F1 FTIS and CTI
│   ├── mma-token-intelligence/     How fight week signals, weigh-in outcomes, and
│   │                               career risk (CRI) drive FighterTIS and FTM
│   ├── esports-token-intelligence/ How tournament calendar, patch risk (PRS), and
│   │                               roster stability (RSI) drive OrgTIS and GRM
│   ├── fan-token-lifecycle/        How a token's intelligence profile changes across
│   │                               six phases — from launch to post-partnership
│   │                               continuation as a non-contractual on-chain asset
│   └── fan-token-partnership-intel/ How to assess partnership quality (PHS), detect
│                               termination signals, and reason about tokens after
│                               official utility ends — including prediction market utility
│
├── core/      ← Shared reasoning foundations used across all layers
│              │  How signals should be weighted, how modifiers combine,
│              │  how results map to price impact, injuries are classified,
│              │  and how officiating, weather, congestion, drafts, and
│              │  narrative momentum should be applied across sport types.
│              │
│   ├── core-signal-weights-by-sport.md    How to weight components by sport
│   ├── core-athlete-modifier-system.md    How the 0.55–1.25× modifier pipeline works
│   ├── core-result-impact-matrices.md     How result types map to price impact
│   ├── core-athlete-record-schema.json    Canonical athlete data schema
│   ├── data-sources.md                    Centralised source citations — every skill
│   │                                      layer mapped to verified live data sources
│   └── multi-agent-coordination.md        Production agent guide — context window
│                                           management, session state, skill routing,
│                                           72h pre-match chain, edge cases, checklist
│   ├── confidence-output-schema.md        Standard output format for all SportMind
│   │                                      agents — composable JSON schema
│   ├── context-window-management.md       How to load skills efficiently within
│   │                                      LLM context limits — token budgets,
│   │                                      minimum viable sets, progressive loading
│   ├── sportmind-score.md             Unified cross-sport confidence metric (SMS);
│   │                                      formula; components; cross-sport comparability
│   └── calibration-framework.md       ML-calibrated modifier weights infrastructure;
│                                          outcome tracking schema; accuracy measurement
│   ├── core-officiating-intelligence.md   How referee/judge/umpire tendencies
│   │                                      produce consistent pre-match modifiers
│   ├── core-weather-match-day.md          How match-day conditions (wind, rain,
│   │                                      going, heat) affect outdoor sports
│   ├── core-fixture-congestion.md         How fixture pile-up and rest periods
│   │                                      affect team performance across all sports
│   ├── core-draft-intelligence.md         How NFL, NBA, NHL, MLB, AFL, and esports
│   │                                      drafts generate token and signal events
│   ├── core-narrative-momentum.md         How revenge, records, comebacks, and
│   │                                      rivalry amplify performance beyond statistics
│   └── injury-intelligence/              How injuries should be classified,
│                                          modified, and timed across sport types
│       ├── core-injury-intelligence.md    Master framework — taxonomy, RQD, SDSI
│       ├── injury-intel-football.md       Squad depth and partnership disruption
│       ├── injury-intel-mma.md            Fight camp signals and weight cut proxy
│       ├── injury-intel-nfl.md            Wed/Thu/Fri designation prediction system
│       ├── injury-intel-boxing.md         Hand injuries, chin durability, camp secrecy
│       ├── injury-intel-horse-racing.md   Paddock visual assessment, trainer language
│       └── injury-intel-cycling.md        Crash probability, Grand Tour fatigue curve
│
├── market/    ← Layer 4: Teaches AI agents THE COMMERCIAL CONTEXT of each sport
│              │  Fan token readiness tier, revenue base, fanbase demographics,
│              │  institutional interest, and what catalysts would trigger
│              │  a token launch or tier upgrade. Load before Layers 1–3.
│              │
│   ├── market-overview.md      How the tier system (1–4) works and how agents
│   │                           should use commercial context to frame all signals
│   ├── market-key-findings.md  12 cross-sport insights that only emerge when
│   │                           all 28 sports are compared simultaneously
│   │
│   │  Tier 1 — Active token ecosystems (agents: full Layer 3 applicable)
│   ├── market-football.md      $50B+ market · 40+ active tokens · World Cup 2026
│   ├── market-basketball.md    $10.5B NBA · TV/digital age gap · China upside
│   ├── market-mma.md           UFC $1.3B · most volatile token ecosystem
│   ├── market-esports.md       CS2 skin economy · publisher approval is gating
│   ├── market-formula1.md      Drive to Survive effect · constructor tokens active
│   ├── market-cricket.md       IPL gap · India regulation is the key variable
│   │
│   │  Tier 2 — Near-term credibility (agents: monitor for launch catalysts)
│   ├── market-american-football.md  NFL $20B · largest untapped token market
│   ├── market-baseball.md      Ohtani/Dodgers Japan catalyst · NPB entry point
│   ├── market-ice-hockey.md    Canadian concentration · European club entry
│   ├── market-afl.md           25% AU crypto adoption · club membership culture
│   ├── market-motogp.md        Dorna centralised · SE Asia 150M+ fans
│   ├── market-rugby-union.md   CVC PE investment signal · RWC 2027 (Australia)
│   ├── market-rugby-league.md  State of Origin token concept · NRL/Super League
│   ├── market-handball.md      PSG integration pathway · EHF FINAL4 window
│   ├── market-nascar.md        72% sponsor loyalty · $1.1B/yr new broadcast deal
│   ├── market-kabaddi.md       350–400M viewers · youngest fanbase in library
│   │
│   │  Tier 3 — Longer horizon (agents: no Layer 3; monitor structural catalysts)
│   ├── market-tennis.md        Individual sport structure · young gen tokens
│   ├── market-golf.md          Oldest fanbase · PGA-LIV unification catalyst
│   ├── market-boxing.md        Structural fragmentation · DAZN streaming shift
│   ├── market-athletics.md     4-year cycle · Jamaica national token concept
│   ├── market-horse-racing.md  Syndication analogy · JRA Japan pathway
│   ├── market-cycling.md       Tour de France brand · Strava 120M user gateway
│   ├── market-darts.md         Luke Littler generational moment · Ally Pally
│   ├── market-snooker.md       250M Chinese fans · Matchroom commercial aggression
│   ├── market-volleyball.md    Brazil concentration · beach volleyball premium
│   ├── market-badminton.md     SE Asia mobile-first · BWF centralised structure
│   ├── market-netball.md       75% female fanbase · Australia market
│   ├── market-winter-sports.md Alpine Europe · Milan-Cortina 2026 window
│   │
│   │  Tier 4 — Niche / structurally distant (agents: reference only)
│   ├── market-swimming.md      Olympic-only peaks · ISL revival prerequisite
│   ├── market-rowing.md        Boat Race cultural outsized importance
│   └── market-table-tennis.md  China-platform incompatibility is defining barrier
│   │
│   │  Special modules
│   └── world-cup-2026.md       FIFA World Cup 2026 consolidated intelligence —
│                               NCSI by player, national token opportunities,
│                               signal calendar, US market unlock analysis
│   │
│   │  Cross-category
│   └── market-womens-sports.md Tier 2→1 transition · WNBA/WSL/WIPL · demographic
│                               advantage · Caitlin Clark commercial catalyst
│
├── macro/     ← Layer 5: Teaches AI agents HOW external forces override everything
│              │  Events originating outside sport that materially affect revenue,
│              │  token markets, and commercial infrastructure. Load first — if an
│              │  active macro event is identified, it resizes all other signals.
│              │  The bifurcated model: physical vs digital revenue react differently.
│              │
│   ├── macro-overview.md           How to apply the bifurcated impact model and
│   │                               which modifier to apply by event category
│   ├── macro-pandemic-public-health.md  How the 2020 pandemic collapsed physical
│   │                               revenue while fan token activity increased —
│   │                               and how agents should model future health events
│   ├── macro-geopolitical.md       How wars, sanctions, and diplomatic crises
│   │                               translate directly into sports and token impacts
│   ├── macro-crypto-market-cycles.md   How CHZ/BTC correlation (~0.80) means
│   │                               crypto bear markets lower all tokens regardless
│   │                               of sporting performance — 4-phase modifier system
│   ├── macro-broadcast-disruption.md   How RSN collapse and streaming wars affect
│   │                               club revenues and create direct-to-fan opportunity
│   ├── macro-economic-cycles.md    How recessions hit premium sports harder and
│   │                               why sponsorship contracts lag by 1–2 years
│   ├── macro-climate-weather.md    How outdoor sports (cricket, cycling, golf,
│   │                               horse racing) face growing structural disruption
│   └── macro-governance-scandal.md How corruption, doping, and match-fixing
│                               create immediate token market consequences
│
└── templates/ ← How contributors should structure new sport and athlete skills
    ├── template-new-sport-skill.md   Standard structure for Layer 1 contributions
    └── template-new-athlete-skill.md Standard structure for Layer 2 contributions
```

---

## Five layers, one system

```
              ┌─────────────────────────────────────┐
              │   LAYER 5 — MACRO INTELLIGENCE      │
              │   External forces affecting all     │
              │   sports simultaneously             │
              │   Pandemic · Geopolitical · Crypto  │
              │   Broadcast · Economy · Climate     │
              └──────────────────┬──────────────────┘
                                 │ (load first — overrides all layers if active)
              ┌──────────────────▼──────────────────┐
              │   LAYER 4 — MARKET INTELLIGENCE     │
              │   Commercial context per sport      │
              │   Fan token readiness tier (1–4)    │
              │   Revenue · Fanbase · Institutional │
              └──────────────────┬──────────────────┘
                                 │ (load second — frames all signal weighting)
              ┌──────────────────▼──────────────────┐
              │   LAYER 1 — SPORT DOMAIN            │
              │   How the sport works               │
              │   Season rhythm · event playbooks   │
              │   Risk variables · signal weights   │
              └──────────────────┬──────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │   LAYER 2 — ATHLETE INTELLIGENCE    │
              │   Who is playing and how fit        │
              │   Availability · form · modifier    │
              │   pipeline · injury intelligence    │
              └──────────────────┬──────────────────┘
                                 │
              ┌──────────────────▼──────────────────┐
              │   LAYER 3 — FAN TOKEN INTELLIGENCE  │
              │   On-chain commercial intelligence  │
              │   HAS · AELS · APS · ABS · AFS      │
              │   Social lift · brand · sponsorship │
              └──────────────────┬──────────────────┘
                                 │
     ┌──────────────────────────▼───────────────────────────┐
     │         Your AI agent output                         │
     │  adjusted_signal_score · confidence · recommendation │
     └──────────────────────────────────────────────────────┘
```

**Layer 5** establishes the external environment — are there macro forces (pandemic, war,
recession, crypto bear market, broadcast disruption, governance scandal) currently active?
If yes, this layer overrides sizing across all other layers. If no, proceed to Layer 4.

**Layer 4** establishes the commercial gravity of the sport — what is its fan token
readiness tier (1–4), what is the revenue base, who is the fanbase, and is there
institutional interest in blockchain products? This frames how heavily to weight all
downstream signals.

**Layer 1** teaches the agent how a sport works — timing, seasonality, event hierarchy,
result impact, and risk variables unique to that sport.

**Layer 2** teaches the agent about the individuals competing — who is fit, who is in form,
how their presence or absence changes the probability of a favourable outcome. Produces an
`adjusted_signal_score`.

**Layer 3** answers the commercial on-chain questions — is this athlete driving token holder
engagement, what is their brand value backed by on-chain data, how do transfer rumours
affect token prices, and which sponsors fit their audience? Produces HAS, AELS, APS, ABS,
and AFS scores for use by clubs, agents, and brands.

---

## Loading order

```
RECOMMENDED AGENT LOADING ORDER:

0. fan-token/fan-token-why.md (ONCE — foundational context)
   → Read once before any fan token work to understand the value thesis
   → Why fan tokens exist, what they solve, where they are heading

1. macro/macro-overview.md
   → Is there an active macro event (pandemic, war, crypto bear, recession)?
   → If yes: apply bifurcated impact model and size overrides before proceeding
   → If no: proceed to Layer 4

2. market/{sport}/market-{sport}.md
   → What is the fan token readiness tier for this sport?
   → What is the commercial context that frames signal weighting?

3. sports/{sport}/sport-domain-{sport}.md
   → How does this sport work?
   → What are the event playbooks and risk variables?

4. athlete/{sport}/athlete-intel-{sport}.md
   → Who is playing? Are key players available and in form?
   → What is the composite modifier?

5. fan-token/* (Tier 1 sports only)
   → What is the current on-chain state?
   → HAS, AELS, APS, ABS, AFS for this athlete/club

6. core/injury-intelligence/ (when injury context is relevant)
   → What is the full injury context for key players?

7. core modifier files (apply in order after athlete modifier):
   → core/core-fixture-congestion.md    — team fatigue adjustment
   → core/core-officiating-intelligence.md — referee/judge tendencies
   → core/core-weather-match-day.md     — match-day conditions (outdoor sports)
   → core/core-narrative-momentum.md   — narrative context (revenge, records, etc.)

8. core/confidence-output-schema.md (for structured output)
   → Produce standard SportMind JSON output
```

---

## Quick start

> **New to SportMind?** Read `README.md` first — it gets you running in 5 minutes.
> See `examples/worked-scenarios/` for real historical examples showing SportMind
> output applied to actual events with calibration analysis.

```bash
# Clone the library
git clone https://github.com/SportMind/SportMind

# Install a sport skill into your agent project
npx skills add sportmind/sports/football
npx skills add sportmind/athlete/football

# Or install everything
npx skills add sportmind
```

### Example: full five-layer football agent (Tier 1)

```
System prompt:
You are a sports intelligence agent with full SportMind context. Load in order:

LAYER 5: [sportmind/macro/macro-overview] — check for active macro events
LAYER 4: [sportmind/market/market-football] — commercial tier and token context
LAYER 1: [sportmind/sports/football] — domain model, event playbooks, risk variables
LAYER 2: [sportmind/athlete/football] — player availability, form, goalkeeper metrics
LAYER 3: [sportmind/fan-token/football-token-intelligence] — FTIS, NCSI, ATM
INJURY:  [sportmind/core/injury-intelligence/injury-intel-football] — if needed

Before evaluating any football match:
1. Check for active macro events — apply bifurcated impact model if relevant
2. Confirm fan token readiness tier (football = Tier 1; full Layer 3 applicable)
3. Check match importance using the competition tier model
4. Retrieve key player availability and compute athlete modifier
5. Apply the appropriate event playbook based on competition tier
6. Cross-reference on-chain data with the sport-adjusted signal
7. Output an adjusted_signal_score with confidence and recommendation
```

### Example: Tier 2 sport agent — NASCAR (no active tokens)

```
System prompt:
You are a sports intelligence agent for NASCAR prediction markets.

LAYER 5: [sportmind/macro/macro-overview] — active macro events?
LAYER 4: [sportmind/market/market-nascar] — Tier 2; no active tokens; sponsor context
LAYER 1: [sportmind/sports/nascar] — track type taxonomy, drafting, Championship 4

Note: NASCAR is Tier 2 — no active fan tokens. Layer 3 is not applicable.
Focus on Layer 1 domain signals (track type × driver history) and Layer 4
commercial context (sponsor loyalty, broadcast deal, Daytona 500 window).

Before evaluating any NASCAR race:
1. Identify track type (superspeedway / intermediate / short / road / dirt)
2. Apply the correct track-type prediction framework from sport-domain-nascar
3. Check Championship 4 eligibility — changes driver risk-taking behaviour materially
4. Apply macro modifier if crypto bear or recession is active (fan token position sizing)
```

---

## Signal weight system

The core signal score from any sports intelligence platform is a weighted composite.
SportMind recommends adjusting the implied weight of each component by sport:

| Sport | Whale / Market | Social | Sports catalyst | Price trend | Macro |
|---|---|---|---|---|---|
| Football / Soccer | 25% | 20% | **30%** | 15% | 10% |
| Basketball | 20% | **30%** | 25% | 15% | 10% |
| MMA | 15% | **35%** | **30%** | 15% | 5% |
| Esports | 15% | **40%** | 25% | 15% | 5% |
| American Football (NFL) | 25% | 25% | **30%** | 15% | 5% |
| Cricket | 20% | 15% | **35%** | 20% | 10% |
| Formula 1 | 20% | 20% | **30%** | 20% | 10% |
| Ice Hockey (NHL) | 25% | 15% | **35%** | 20% | 5% |
| Baseball (MLB) | 20% | 10% | **40%** | 20% | 10% |
| MotoGP | 20% | **25%** | **35%** | 15% | 5% |
| AFL | 20% | 20% | **35%** | 15% | 10% |
| Handball | 20% | 20% | **35%** | 15% | 10% |
| Kabaddi | 15% | **30%** | **35%** | 15% | 5% |
| NASCAR | 20% | 15% | **40%** | 20% | 5% |
| Rugby (Union / League) | 25% | 15% | **35%** | 15% | 10% |
| Tennis | 20% | 25% | **30%** | 20% | 5% |
| Golf | 15% | 20% | **35%** | 20% | 10% |
| Boxing | 10% | **35%** | **35%** | 15% | 5% |
| Cycling | 15% | 15% | **40%** | 20% | 10% |
| Athletics | 10% | **30%** | **35%** | 20% | 5% |
| Horse Racing | 20% | 10% | **45%** | 20% | 5% |
| Darts | 20% | **30%** | **35%** | 10% | 5% |
| Snooker | 20% | 20% | **40%** | 15% | 5% |
| Netball | 15% | **30%** | **35%** | 15% | 5% |
| Winter Sports | 15% | 20% | **40%** | 20% | 5% |
| Volleyball | 15% | **25%** | **40%** | 15% | 5% |
| Badminton | 15% | **25%** | **40%** | 15% | 5% |
| Swimming | 10% | **25%** | **40%** | 20% | 5% |
| Rowing | 10% | 20% | **45%** | 20% | 5% |
| Table Tennis | 10% | 20% | **45%** | 20% | 5% |

*All rows sum to 100%. Bold = highest weighted component(s). These are interpretive weights
for agent reasoning — not overrides to any API output. See `core/core-signal-weights-by-sport.md`
for rationale, phase adjustments, and the macro cycle overlay.*

---

## Athlete modifier system

Layer 2 skills produce a composite modifier that adjusts the base signal score:

```
adjusted_score = base_signal_score × composite_modifier

composite_modifier = (
  availability_modifier    × form_modifier
  × goalkeeper_modifier    × fatigue_modifier
  × weather_modifier       × matchup_modifier
  × psychological_modifier × lineup_confirmation_modifier
)
```

| Modifier range | Meaning | Agent action |
|---|---|---|
| ≥ 1.20 | Elite conditions — full strength, hot form, strong matchup | High conviction |
| 1.10–1.19 | Strong — key players fit, good form | Normal sizing |
| 1.00–1.09 | Neutral | Follow base signal |
| 0.90–0.99 | Minor concerns — fatigue, unconfirmed lineup | Reduce or wait |
| 0.80–0.89 | Significant concern — key player doubt | Caution |
| 0.70–0.79 | Major degradation — key player out | Skip |
| < 0.70 | Severe — multiple absences, crisis conditions | Do not enter |

*See `core/core-athlete-modifier-system.md` for the full modifier pipeline.*

---

## Macro cycle modifier

When a macro event (crypto bear market, recession, pandemic) is active, apply an
additional multiplier to all sporting signals:

| Macro condition | Modifier | Source |
|---|---|---|
| Crypto bull market (BTC above 200-day MA, CHZ uptrend) | × 1.20 | `macro/macro-crypto-market-cycles.md` |
| Crypto neutral market | × 1.00 | |
| Crypto bear market (BTC below 200-day MA, CHZ downtrend) | × 0.75 | |
| Crypto extreme bear / capitulation | × 0.55 | |
| Active pandemic / mass lockdown | Physical: × 0.30 · Digital: × 1.15 | `macro/macro-pandemic-public-health.md` |
| Active geopolitical sanction (direct) | × 0.60 on affected entity | `macro/macro-geopolitical.md` |
| Active recession (confirmed) — premium sport | × 0.85 | `macro/macro-economic-cycles.md` |
| Active recession (confirmed) — mass-market sport | × 0.92 | |
| Governance scandal (direct, active) | × 0.70 on affected entity | `macro/macro-governance-scandal.md` |

---

## Named metrics reference

SportMind skills produce named composite metrics. Each metric is defined once in its
originating skill and referenced consistently across the library:

| Metric | Full name | Produced by | What it measures |
|---|---|---|---|
| **HAS** | Holder Activity Score | `fan-token/fan-token-pulse` | On-chain holder engagement velocity and depth |
| **TVI** | Token Velocity Index | `fan-token/fan-token-pulse` | Speed and volume of token movement; liquidity health |
| **PI** | Performance Index | `fan-token/performance-on-pitch` | Position-weighted on-pitch performance; includes xG/xA |
| **DTS** | Development Trajectory Score | `fan-token/performance-off-pitch` | Athlete development curve; loan/rehab progress |
| **TAI** | Training Adaptation Index | `fan-token/performance-off-pitch` | Response to training load; injury recovery adaptation |
| **PS** | Professionalism Score | `fan-token/performance-off-pitch` | Off-pitch conduct, punctuality, media, team culture fit |
| **AELS** | Athlete Engagement Lift Score | `fan-token/athlete-social-lift` | Does this athlete's social activity move token holders? |
| **SHS** | Social Health Score | `fan-token/athlete-social-activity` | Overall social channel quality, consistency, sentiment |
| **AGI** | Audience Growth Index | `fan-token/athlete-social-activity` | Rate of follower/engagement growth across platforms |
| **TVS** | Transfer Viability Score | `fan-token/transfer-intelligence` | Probability and commercial value of a transfer |
| **DLVS** | Domestic Loan Value Score | `fan-token/transfer-intelligence` | Value and risk assessment for loan spell arrangements |
| **APS** | Athlete Portability Score | `fan-token/transfer-signal` | How well an athlete's token value transfers to a new club |
| **TSI** | Transfer Signal Index | `fan-token/transfer-signal` | Confidence-weighted rumour aggregation for token impact |
| **ABS** | Athlete Brand Score | `fan-token/brand-score` | Composite commercial brand value; exportable brief |
| **AFS** | Audience Fit Score | `fan-token/sponsorship-match` | Brand-to-athlete audience alignment for sponsorship |
| **FTIS** | Fan Token Impact Score | sport-specific bridge skills | Competition-level token price impact signal |
| **NCSI** | National-Club Spillover Index | `fan-token/football-token-intelligence` | How national team events affect club token prices |
| **ATM** | Athlete Token Multiplier | `fan-token/football-token-intelligence` | Individual athlete contribution to club token movement |
| **CTI** | Constructor Token Index | `fan-token/formula1-token-intelligence` | Constructor-level F1 token commercial health |
| **DTM** | Driver Token Multiplier | `fan-token/formula1-token-intelligence` | Individual driver contribution to constructor token |
| **FTM** | Fighter Token Multiplier | `fan-token/mma-token-intelligence` | Individual fighter impact on MMA token pricing |
| **CRI** | Career Risk Index | `fan-token/mma-token-intelligence` | Fighter career longevity and token permanence risk |
| **OrgTIS** | Organisation Token Impact Score | `fan-token/esports-token-intelligence` | Esports org-level token impact from tournament outcomes |
| **GRM** | Game Roster Multiplier | `fan-token/esports-token-intelligence` | Multi-game roster depth impact on org token value |
| **PRS** | Patch Risk Score | `fan-token/esports-token-intelligence` | Risk that a game patch disrupts a team's competitive edge |
| **RSI** | Roster Stability Index | `fan-token/esports-token-intelligence` | Turnover risk and its effect on org token continuity |
| **PQS** | Pitcher Quality Score | `athlete/baseball` | Starting pitcher quality composite — MLB specific |
| **BQS** | Batter Quality Score | `athlete/baseball` | Batter performance composite — MLB specific |
| **PAS** | Player Availability Score | `athlete/rugby-league` | Availability and fitness composite — rugby league specific |
| **PIS** | Positional Impact Score | `athlete/rugby-league` | Positional criticality modifier — rugby league specific |
| **PHS** | Partnership Health Score | `fan-token/fan-token-partnership-intelligence` | Five-indicator composite of active partnership health and termination risk |
| **LTUI** | Lifetime Token Utility Index | `fan-token/fan-token-lifecycle` | Cumulative utility event quality and frequency across the token's full life |
| **GSAx** | Goals Saved Above Expected | `athlete/nhl` | Goaltender performance vs statistical expectation — the single most important NHL prediction variable |
| **NBATIS** | NBA Token Impact Score | `fan-token/basketball-token-intelligence` | Composite NBA signal: game importance, star player tier, playoff position, market sentiment |
| **CricTIS** | Cricket Token Impact Score | `fan-token/cricket-token-intelligence` | Composite cricket signal: format weight, match importance, India factor (×1.40), India-Pakistan (×2.00) |
| **VSI** | Validator Status Indicator | `fan-token/rwa-sportfi-intelligence` | ✅ Complete | RSF (RWA Signal Framework), Phase 5 spectrum, staking yield taxonomy, outcome-linked supply, media rights, player bonds, CollateralFi |
| `fan-token/kol-influence-intelligence` | ✅ Complete | KIS formula, 4-tier KOL classification, paid vs organic detection, sports-specific KOL ecosystem map, HAS integration, Python KOL monitor |
| `fan-token/fan-sentiment-intelligence` | ✅ Complete | Emotional arc model (6 phases), CDI formula, decay curve (λ constants), fan type segmentation, LTUI integration |
| `fan-token/on-chain-event-intelligence` | ✅ Complete | 6 signal categories: wallet movements, LP activity, governance execution, staking ratio, cross-chain bridges, wallet age |
| `fan-token/sports-governance-intelligence` | ✅ Complete | GSI (Governance Signal Index), Socios model, DAO patterns, voting mechanics, lifecycle governance signals |
| `fan-token/blockchain-validator-intelligence` | Sixth PHS component measuring validator node health and stake stability for validator clubs |

---

## Who SportMind is for

SportMind is designed as a shared intelligence layer for any agent or developer operating
in sports-adjacent digital markets. The primary use cases:

**Fan token platforms and traders** — agents that need to understand why a token is moving,
what sporting and external events are driving it, and how to size positions intelligently.
See `fan-token/fan-token-why.md` for the foundational commercial thesis that underpins
all fan token intelligence in this library.

**Prediction markets** — agents that need sport-specific contextual reasoning before
incorporating raw statistical signals; understanding that a stat without context is noise.

**Sports GameFi applications** — games and platforms that need to model real-world sporting
outcomes; SportMind provides the domain knowledge layer that raw data providers do not.

**Sports analytics platforms** — analysts and platforms building intelligence products that
need structured reasoning about how signals interact within specific sports.

**Club and athlete commercial teams** — teams using AI to inform sponsorship, brand
positioning, and athlete value assessments; Layer 3 is designed specifically for this use case.

**Developers building sports AI products** — anyone who would otherwise spend weeks
understanding cricket's dew factor, NASCAR's track taxonomy, or MMA's weigh-in risk
dynamics from scratch. SportMind is the shared layer that means they don't have to.

---

## Compatible platforms

SportMind skills are platform-agnostic. They work with any agent framework
as structured markdown context, or via the platform contracts (see `platform/api-contracts.md`).

**SportMind = the intelligence layer. Partners provide data or infrastructure.**

| Platform | Role | Integration |
|---|---|---|
| **Fan Token Intel** (fantokenintel.com) | Primary signal data | Provides base_score; SportMind adjusts it |
| **Chiliz / Socios** | Blockchain infrastructure | On-chain data for Layer 3 skills |
| **Azuro** (azuro.org) | Prediction market protocol | Pool TVL → defi_context; DeFi intelligence |
| **Claude / Claude Code** | Agent reasoning engine | MCP or direct system prompt |
| **GPT-4o / OpenAI** | Agent reasoning engine | System prompt injection |
| **LangChain / CrewAI / AutoGen** | Agent framework | Skill injection into context |
| **Custom agents** | Any system | Structured markdown + confidence output schema |

Full integration patterns: `platform/integration-partners.md`
API contracts: `platform/api-contracts.md`

---

## Skills at a glance

### Sport domain skills (Layer 1) — 28 complete, 14 seeking contributors

| Skill | Status | Key differentiator |
|---|---|---|
| `sports/football` | ✅ Complete | Derby scoring, competition tier, season rhythm |
| `sports/basketball` | ✅ Complete | Star-player correlation, playoff series logic |
| `sports/mma` | ✅ Complete | Weigh-in risk, fight card hierarchy, retirement risk |
| `sports/esports` | ✅ Complete | Meta/patch risk, multi-game org architecture |
| `sports/american-football` | ✅ Complete | Weekly injury report cadence, Super Bowl window |
| `sports/golf` | ✅ Complete | Cut line risk, course history, Major tier system, LIV/PGA split |
| `sports/boxing` | ✅ Complete | Belt structure (IBF/WBA/WBC/WBO), weigh-in risk, promotional risk |
| `sports/athletics` | ✅ Complete | Olympic cycle, world record catalyst, doping risk protocol |
| `sports/cycling` | ✅ Complete | Grand Tour DNF signal, daily stage catalysts, Classics |
| `sports/horse-racing` | ✅ Complete | Going conditions, draw bias, Cheltenham/Grand National |
| `sports/snooker` | ✅ Complete | Crucible specialisation, Triple Crown, 147 catalyst |
| `sports/darts` | ✅ Complete | 9-dart finish signal, Ally Pally, Premier League arc |
| `sports/rugby-league` | ✅ Complete | State of Origin, Super League / NRL dual calendar |
| `sports/netball` | ✅ Complete | World Cup, Commonwealth Games, growing fan token market |
| `sports/swimming` | ✅ Complete | Olympic cycle, world records, doping exit protocol |
| `sports/rowing` | ✅ Complete | Olympics, Boat Race (UK), weather conditions |
| `sports/winter-sports` | ✅ Complete | Olympic cycle, Four Hills, Crystal Globe, crash risk |
| `sports/cricket` | ✅ Complete | Format-first analysis, pitch type, dew factor, India vs Pakistan |
| `sports/rugby` | ✅ Complete | Set piece dominance, kicker zone accuracy, Six Nations |
| `sports/tennis` | ✅ Complete | Surface splits, Grand Slam structure, H2H methodology |
| `sports/formula1` | ✅ Complete | Race calendar, constructor dynamics, pit strategy |
| `sports/baseball` | ✅ Complete | Pitcher-first analysis, Statcast metrics, ballpark factors |
| `sports/ice-hockey` | ✅ Complete | Goaltender as defining variable, GSAx, special teams, B2B modifier |
| `sports/motogp` | ✅ Complete | Hardware tier system, crash probability, wet race specialists |
| `sports/afl` | ✅ Complete | Dual scoring system, kicking accuracy, clearance dominance |
| `sports/handball` | ✅ Complete | EHF Champions League, goalkeeper save%, fast break, FINAL4 |
| `sports/kabaddi` | ✅ Complete | PKL raider intelligence, All Out dynamics, Indian market |
| `sports/nascar` | ✅ Complete | Track type taxonomy, superspeedway drafting, Championship 4 |
| `sports/badminton` | 🔜 Seeking contributor | |
| `sports/volleyball` | 🔜 Seeking contributor | |
| `sports/table-tennis` | 🔜 Seeking contributor | |
| `sports/sailing` | 🔜 Seeking contributor | |
| `sports/triathlon` | 🔜 Seeking contributor | |
| `sports/field-hockey` | 🔜 Seeking contributor | |
| `sports/squash` | 🔜 Seeking contributor | |
| `sports/curling` | 🔜 Seeking contributor | |
| `sports/gymnastics` | 🔜 Seeking contributor | |
| `sports/weightlifting` | 🔜 Seeking contributor | |
| `sports/judo` | 🔜 Seeking contributor | |
| `sports/taekwondo` | 🔜 Seeking contributor | |
| `sports/fencing` | 🔜 Seeking contributor | |
| `sports/swimming-open-water` | 🔜 Seeking contributor | |

### Athlete intelligence skills (Layer 2) — 29 complete

| Skill | Status | Key output |
|---|---|---|
| `athlete/football` | ✅ Complete | Availability, xG form, GK rating, lineup confirmation |
| `athlete/mma` | ✅ Complete | Striking, grappling, round profile, fight camp signals |
| `athlete/esports` | ✅ Complete | Roster status, HLTV rating, meta readiness, draft intel |
| `athlete/nfl` | ✅ Complete | QB CPOE, O-line health, injury designations |
| `athlete/nba` | ✅ Complete | Load management, on/off splits, clutch TS% |
| `athlete/nhl` | ✅ Complete | Goaltender start, special teams, Corsi |
| `athlete/cricket` | ✅ Complete | Batter vs bowler H2H, pitch, toss impact |
| `athlete/tennis` | ✅ Complete | Serve metrics, surface record, H2H dynamics |
| `athlete/rugby` | ✅ Complete | Set piece, kicker accuracy, halfback partnership |
| `athlete/golf` | ✅ Complete | Course history, strokes gained, cut line, Major record |
| `athlete/boxing` | ✅ Complete | Belt status, weigh-in, fight camp, finishing tendency |
| `athlete/cycling` | ✅ Complete | GC standing, course fit, team role, DNF risk |
| `athlete/athletics` | ✅ Complete | Form score, WR proximity, doping status, multi-round fitness |
| `athlete/horse-racing` | ✅ Complete | Going preference, C&D record, trainer/jockey signals |
| `athlete/snooker` | ✅ Complete | Crucible record, pressure record, break-building stats |
| `athlete/darts` | ✅ Complete | 3-dart average, checkout %, Ally Pally record, tour card |
| `athlete/baseball` | ✅ Complete | PQS (pitcher), BQS (batter), Statcast profile, platoon splits |
| `athlete/rugby-league` | ✅ Complete | PAS, form rating, PIS, State of Origin disruption modifier |
| `athlete/meta` | ✅ Complete | Cross-sport orchestrator — single modifier pipeline call |
| `athlete/formula1` | ✅ Complete | Qualifying delta vs teammate, wet weather rating, regulation fit, grid penalty |
| `athlete/afl` | ✅ Complete | Kicking accuracy zones, contested possession, clearance work |
| `athlete/motogp` | ✅ Complete | Hardware tier interaction, wet specialist rating, crash probability |
| `athlete/handball` | ✅ Complete | Goalkeeper save rate (>35% = team override), position-specific modifiers |
| `athlete/kabaddi` | ✅ Complete | Raider success rate (>60% = carry potential), All Out dynamics |
| `athlete/nascar` | ✅ Complete | Track type specialisation (superspeedway vs short track vs road) |
| `athlete/netball` | ✅ Complete | Goal shooter accuracy, centre pass conversion rate |
| `athlete/rowing` | ✅ Complete | Split time vs PB, course conditions, taper status |
| `athlete/swimming` | ✅ Complete | PB proximity, taper timing, multi-event Olympic fatigue management |
| `athlete/winter-sports` | ✅ Complete | Course fit, snow conditions, Olympic cycle position |

### Fan token commercial intelligence (Layer 3) — 36 skills complete

Layer 3 requires API keys for full functionality. See `fan-token/fan-token-layer-overview.md`
for the full infrastructure setup. Only applicable to Tier 1 sports (active token ecosystem).

**Foundation — read before any other Layer 3 skill:**

| File | Purpose |
|---|---|
| `fan-token/fan-token-why.md` | The foundational value thesis — why fan tokens exist, what they solve that the traditional model cannot, the scalability mathematics, and the future trajectory from engagement tokens to RWA/SportFi |

**Ground truth layers — run first in any chain:**

| Skill | Status | Core metric | Key output |
|---|---|---|---|
| `fan-token/fan-token-pulse` | ✅ Complete | HAS, TVI | On-chain holder data, velocity classification, geographic map |
| `fan-token/performance-on-pitch` | ✅ Complete | PI | Position-weighted performance index, xG/xA, scout report, valuation multiplier |

**Intelligence layers:**

| Skill | Status | Core metric | Key output |
|---|---|---|---|
| `fan-token/transfer-intelligence` | ✅ Complete | TVS, DLVS | Full transfer lifecycle — valuation, contract risk, loan analysis |
| `fan-token/athlete-social-activity` | ✅ Complete | SHS, AGI | Content mix, brand voice, sentiment trends, influence map, crisis warning |
| `fan-token/performance-off-pitch` | ✅ Complete | DTS, TAI, PS | Development trajectory, loan spell analysis, rehab, professionalism |
| `fan-token/athlete-social-lift` | ✅ Complete | AELS | Social-to-token correlation — does this athlete move token holders? |

**Synthesis layers:**

| Skill | Status | Core metric | Key output |
|---|---|---|---|
| `fan-token/transfer-signal` | ✅ Complete | APS, TSI | Rumour confidence, spike attribution, fan token portability |
| `fan-token/brand-score` | ✅ Complete | ABS | Athlete Brand Score — synthesis into exportable commercial brief |

**Monetisation layer:**

| Skill | Status | Core metric | Key output |
|---|---|---|---|
| `fan-token/sports-brand-sponsorship` | ✅ Complete | Market rate | Rate benchmarking, deal structure, conflict audit, ROI framework |
| `fan-token/sponsorship-match` | ✅ Complete | AFS | Brand category rankings, audience fit, token-native activation ideas |

**Sport-specific bridge skills:**

| Skill | Status | Core metrics | Key output |
|---|---|---|---|
| `fan-token/football-token-intelligence` | ✅ Complete | FTIS, NCSI, ATM | Competition × token impact matrix, World Cup 2026 national-club spillover |
| `fan-token/formula1-token-intelligence` | ✅ Complete | FTIS, CTI, DTM | Race-by-race FTIS, regulation cycle, silly season scoring |
| `fan-token/mma-token-intelligence` | ✅ Complete | FighterTIS, FTM, CRI | Fight week signal map, weigh-in risk, post-fight trajectory |
| `fan-token/esports-token-intelligence` | ✅ Complete | OrgTIS, GRM, PRS, RSI | Multi-game calendar, Oct-Nov stack window, patch risk |
| `fan-token/basketball-token-intelligence` | ✅ Complete | NBATIS | NBA player-centric model, trade deadline signals, EuroLeague comparison |
| `fan-token/cricket-token-intelligence` | ✅ Complete | CricTIS | Format-first (T20/ODI/Test), India-Pakistan ×2.00, IPL gap, PSL framework |
| `fan-token/nfl-token-intelligence` | ✅ Complete | NFLTIS | QB injury report timing, Super Bowl peak, Fantasy Football correlation, 2027 catalyst |
| `fan-token/afl-token-intelligence` | ✅ Complete | AFLTIS | MCG Grand Final architecture, 25% AU crypto adoption, ANZAC Day signal, membership culture |
| `fan-token/rugby-token-intelligence` | ✅ Complete | RugbyTIS | CVC PE investment signal, Six Nations window, RWC 2027 catalyst, kicker primacy |

**DeFi and liquidity intelligence:**

| Skill | Status | Core concepts | Key output |
|---|---|---|---|
| `fan-token/defi-liquidity-intelligence` | ✅ Complete | TVL, Slippage, LP signals | Pre-execution liquidity check; on-chain yield; prediction market context |

**Lifecycle and partnership intelligence:**

| Skill | Status | Core concept | Key output |
|---|---|---|---|
| `fan-token/fan-token-lifecycle` | ✅ Complete | Six-phase lifecycle model | Phase trajectory assessment, non-contractual token framework, CEX/DEX model, lifecycle-adjusted signal weights |
| `fan-token/fan-token-partnership-intelligence` | ✅ Complete | Partnership Health Score (PHS + VSI) | New partnership due diligence, termination patterns, Type A/B/C case study taxonomy, relaunch signals |
| `fan-token/rwa-sportfi-intelligence` | ✅ Complete | RSF (RWA Signal Framework), Phase 5 spectrum, staking yield taxonomy, outcome-linked supply, media rights, player bonds, CollateralFi |
| `fan-token/kol-influence-intelligence` | ✅ Complete | KIS formula, 4-tier KOL classification, paid vs organic detection, sports-specific KOL ecosystem map, HAS integration, Python KOL monitor |
| `fan-token/fan-sentiment-intelligence` | ✅ Complete | Emotional arc model (6 phases), CDI formula, decay curve (λ constants), fan type segmentation, LTUI integration |
| `fan-token/on-chain-event-intelligence` | ✅ Complete | 6 signal categories: wallet movements, LP activity, governance execution, staking ratio, cross-chain bridges, wallet age |
| `fan-token/sports-governance-intelligence` | ✅ Complete | GSI (Governance Signal Index), Socios model, DAO patterns, voting mechanics, lifecycle governance signals |
| `fan-token/blockchain-validator-intelligence` | ✅ Complete | VSI, Validator-Adjusted PHS | PSG dual-layer model (fan token + validator), on-chain monitoring, validator stake signals, future multi-validator trajectory |

*The lifecycle and partnership skills address the temporal dimension of fan token intelligence — how a token's commercial profile evolves from pre-launch through active utility to post-partnership continuation on-chain. Fan tokens cannot be cancelled: they are permanent on-chain assets that transition from governance utility to predictive utility when official partnership infrastructure ends.*

### Core intelligence (cross-layer) — 28 files complete

| File | Purpose |
|---|---|
| `core/core-athlete-modifier-system.md` | How to construct and apply the 0.55–1.25× modifier pipeline |
| `core/core-signal-weights-by-sport.md` | Signal component weighting for all 30 sports |
| `core/core-result-impact-matrices.md` | Price impact by result type across all sports |
| `core/core-athlete-record-schema.json` | Canonical JSON schema for athlete data records |
| `core/confidence-output-schema.md` | Standard JSON output schema — makes all SportMind agents composable |
| `core/core-officiating-intelligence.md` | Referee/judge/umpire tendency modifiers — football, MMA, cricket, NFL, horse racing, tennis |
| `core/core-weather-match-day.md` | Match-day weather signal framework — cricket, horse racing, NFL, football, golf, rugby, athletics |
| `core/core-fixture-congestion.md` | Team-level fatigue: Tier 1–5 congestion framework for all team sports |
| `core/core-draft-intelligence.md` | NFL, NBA, NHL, MLB, AFL, and esports draft events as signal catalysts |
| `core/core-narrative-momentum.md` | Eight narrative categories (revenge, records, comebacks, elimination) with modifiers |
| `core/data-sources.md` | Centralised source citations — all five layers mapped to verified live data sources with source quality hierarchy and API quick reference |
| `core/context-window-management.md` | Token budgets per file, minimum viable loading sets for 5 use cases, priority ranking, overflow protocol, model context guide |
| `core/multi-agent-coordination.md` | Production agent guide — patterns, session state, multi-sport routing, 72h pre-match chain, edge cases, deployment checklist |
| `core/sportmind-score.md` | Unified cross-sport confidence metric (SMS) — 4 components, 0–100 score, combined decision matrix with adjusted_score |
| `core/calibration-framework.md` | ML-calibrated modifier weights — outcome tracking schema, direction accuracy methodology, 5-step calibration workflow |

### Injury intelligence (cross-layer) — 7 files complete

| File | Sport | Key intelligence |
|---|---|---|
| `core/injury-intelligence/core-injury-intelligence.md` | All sports | Taxonomy (Tier A/B/C), modifier pipeline, RQD, SDSI, return-to-play curves |
| `core/injury-intelligence/injury-intel-football.md` | Football | Squad depth by position, CB partnership disruption, set piece loss, manager language decoder |
| `core/injury-intelligence/injury-intel-mma.md` | MMA | Fight camp signal timeline, weight cut proxy, weigh-in outcome modifiers |
| `core/injury-intelligence/injury-intel-nfl.md` | American Football | Wed/Thu/Fri designation system, QB criticality tiers, O-line blind spot |
| `core/injury-intelligence/injury-intel-boxing.md` | Boxing | Hand injury detection, cut risk, chin durability, camp secrecy decoder |
| `core/injury-intelligence/injury-intel-horse-racing.md` | Horse Racing | Paddock visual checklist, morning workout signals, trainer language decoder |
| `core/injury-intelligence/injury-intel-cycling.md` | Cycling | Crash probability by stage type, Grand Tour cumulative fatigue curve |

### Market intelligence (Layer 4) — 42 files complete

Commercial context for all 28 sports — fan token readiness tier (1–4), global revenue,
fanbase demographics, institutional blockchain interest, media rights trajectory, token
catalyst events, and competitor landscape. Load before any Layer 1–3 intelligence.

**Tier 1 — Active token ecosystem:**

| File | Key intelligence |
|---|---|
| `market/market-football.md` | $50B+ market, 40+ active tokens, World Cup 2026 as primary catalyst, Premier League gap |
| `market/market-basketball.md` | $10.5B NBA, 158% rights growth, NBA Top Shot precedent, China upside |
| `market/market-mma.md` | UFC $1.3B, most volatile token ecosystem, highest crypto-native fanbase |
| `market/market-esports.md` | CS2 skin economy ($B+), publisher approval is gating variable, Oct-Nov stack window |
| `market/market-formula1.md` | Drive to Survive demographic shift, constructor tokens active, driver gap |
| `market/market-cricket.md` | IPL gap (highest-value untapped token opportunity globally), India regulation |

**Tier 2 — Near-term high credibility:**

| File | Key intelligence |
|---|---|
| `market/market-american-football.md` | NFL $20B, largest untapped token market, Fantasy Football as gateway |
| `market/market-baseball.md` | Ohtani/Dodgers Japan catalyst, NPB as entry point, RSN crisis |
| `market/market-ice-hockey.md` | Canadian fanbase concentration, European clubs as entry, Rogers deal 2026 |
| `market/market-afl.md` | Australia 25% crypto adoption, club membership culture, Grand Final window |
| `market/market-motogp.md` | Dorna centralised (one deal = full championship), Indonesia 80M fans |
| `market/market-rugby-union.md` | CVC Private Equity investment signal, RWC 2027 (Australia) |
| `market/market-rugby-league.md` | State of Origin token concept, NRL/Super League dual calendar |
| `market/market-handball.md` | PSG handball integration pathway, EHF FINAL4 window |
| `market/market-nascar.md` | Sponsor loyalty 72%, new broadcast deal $1.1B/yr, Daytona 500 |
| `market/market-kabaddi.md` | 350–400M viewers, youngest fanbase, Reliance/JioCinema catalyst |

**Tier 3 — Longer horizon | Tier 4 — Niche:**
See `market/market-overview.md` for full tier breakdown and all remaining sport files.

**Cross-sport intelligence:**

| File | Key intelligence |
|---|---|
| `market/market-overview.md` | Tier system framework, upgrade/downgrade signals, loading order |
| `market/market-key-findings.md` | 12 cross-sport insights: audience size trap, China platform problem, regulatory gating variable, private equity signal, validator sports brands, and 7 more |

### Macro intelligence (Layer 5) — 8 files complete

External forces that originate outside sport but materially affect sporting revenue,
fan token markets, and commercial infrastructure. The defining concept: **the bifurcated
impact model** — macro events typically affect physical sports revenue and digital fan
engagement differently. The 2020 pandemic is the proof of concept.

| File | Category | Key intelligence |
|---|---|---|
| `macro/macro-overview.md` | All | Bifurcated model, event taxonomy (A/B/C), crypto cycle modifiers, loading order |
| `macro/macro-pandemic-public-health.md` | Acute | 2020 case study: physical revenue collapsed, fan token activity increased; recovery curve |
| `macro/macro-geopolitical.md` | Acute/Structural | Russia-Ukraine case study, sanctions patterns, token collapse timelines |
| `macro/macro-crypto-market-cycles.md` | Structural/Cyclical | CHZ/BTC ~0.80 correlation, 4-phase modifiers, 2022 crypto winter case study |
| `macro/macro-broadcast-disruption.md` | Structural | RSN collapse (US), streaming wars, direct-to-fan opportunity |
| `macro/macro-economic-cycles.md` | Structural/Cyclical | Discretionary spending hierarchy, sponsorship lag, recession sport vulnerability |
| `macro/macro-climate-weather.md` | Structural | Cricket/cycling/horse racing outdoor risk, event cancellation protocol |
| `macro/macro-governance-scandal.md` | Acute | FIFA 2015, doping athlete token risk, esports match-fixing, recovery timeline |

---

### Developer tooling — platform + community + i18n + 6 worked scenarios

| File | Purpose |
|---|---|
| `agent-prompts/agent-prompts.md` | 10 production-ready system prompts (football, MMA, multi-sport, commercial, draft, research, minimal, DeFi, WC2026) |
| `glossary.md` | Central terminology reference — all 28 sports + 36 named metrics + DeFi terms |
| `core/multi-agent-coordination.md` | Production agent guide — patterns, session state, routing, edge cases, deployment checklist |
| `core/context-window-management.md` | Token budgets, minimum viable loading sets, priority ranking, overflow recovery protocol |
| `platform/platform-overview.md` | Platform layer purpose; open intelligence guarantee; three usage modes |
| `platform/api-contracts.md` | Formal skill call specifications; versioning; error codes with agent_action guidance |
| `platform/integration-partners.md` | Integration registry: FanTokenIntel, Chiliz, Azuro, data providers, LLMs |
| `platform/skill-registry.md` | Queryable catalogue of all 200+ skills; skill IDs; minimum viable sets |
| `platform/monitoring-alerts.md` | Alert specs for macro monitoring and skill reviews; webhook format |
| `platform/live-signals.md` | Static intelligence vs live inputs boundary; 6 signal categories; self-update architecture |
| `platform/macro-state.json` | Auto-updated macro state file (BTC cycle, active events) for fast session-start check |
| `core/sportmind-score.md` | Unified cross-sport confidence metric (SMS); combined decision matrix |
| `core/calibration-framework.md` | Outcome tracking schema; modifier accuracy methodology; calibration workflow |
| `community/leaderboard.md` | Contributor accuracy leaderboard; 5-tier system; points formula |
| `community/accuracy-tracking.md` | Prediction accuracy methodology; outcome record format; submission guide |
| `i18n/README.md` | Multi-language support framework; available languages; translation guide |
| `examples/testing/testing-scenarios.md` | 5 validation playbooks with inputs, expected outputs, and 7-point pass criteria |

### Application blueprints — 9 fully specified developer applications

| File | Application | Primary use case |
|---|---|---|
| `examples/applications/app-08-governance-intelligence.md` | Sports Governance Intelligence | Commercial context for fan token governance votes |
| `examples/applications/app-10-fan-digital-twin.md` | ✅ Complete | FLS (Fan Loyalty Score) formula, dynamic NFT metadata structure, SportMind Python agent, tier-based access rights, ethical framework |
| `examples/applications/app-09-talent-scouting.md` | Talent Scouting Intelligence | Full scouting report: PI + DTS + APS + LTUI impact |

### Agentic workflow patterns — 4 reusable long-running workflows

`examples/agentic-workflows/README.md` — Portfolio monitor (4h cycle), pre-match chain
(T-48h + T-2h), tournament tracker (NCSI per match), transfer window monitor (rumour → confirm).
Human escalation principles and autonomous completion rules documented.

### Compressed skill summaries — token-efficient reference layer

`compressed/README.md` — 33 compressed skills (~1,070 tokens total vs ~32,000 full).
97% compression ratio. Football, cricket, basketball, MMA, F1, football token intel,
macro state, lifecycle, DeFi, confidence schema.

### Application blueprints — 7 fully specified developer applications

| File | Application | Primary use case |
|---|---|---|
| `examples/applications/app-01-defi-prediction-market.md` | Decentralised Sports Prediction Finance | Pre-match signal → on-chain market via Azuro |
| `examples/applications/app-02-portfolio-intelligence.md` | Fan Token Portfolio Intelligence | Contextual explanation for token holders |
| `examples/applications/app-03-athlete-commercial.md` | Athlete Commercial Intelligence Platform | ABS/APS/AELS briefings for agents and brands |
| `examples/applications/app-04-brand-token-strategy.md` | Sports Brand Token Strategy Tool | Pre-launch due diligence for clubs |
| `examples/applications/app-05-world-cup-dashboard.md` | World Cup 2026 Intelligence Dashboard | Live NCSI tracking across 48-team tournament |
| `examples/applications/app-06-gamefi-layer.md` | Sports GameFi Intelligence Layer | SMS-weighted on-chain sports game mechanics |
| `examples/applications/app-07-sportfi-kit-integration.md` | SportFi Kit + SportMind Full Stack | Complete React/TypeScript integration reference for Chiliz Chain dApps |

### Worked scenarios — 6 complete historical calibration examples

| File | What it demonstrates |
|---|---|
| `examples/worked-scenarios/scenario-ucl-final-2023.md` | Full 5-layer football; treble narrative; $CITY token response (+14.2%) |
| `examples/worked-scenarios/scenario-ufc-281-pereira-adesanya.md` | MMA fight week; FTX macro override (×0.55); token vs prediction market separation |
| `examples/worked-scenarios/scenario-state-of-origin-2023-g3.md` | Rugby league rivalry; State of Origin decider; downstream NRL congestion signals |
| `examples/worked-scenarios/scenario-ipl-dls-2023.md` | Cricket T20; dew factor (+10-12%); DLS event; India factor; IPL gap |
| `examples/worked-scenarios/scenario-nba-trade-deadline-2023.md` | NBA trade; player-centric model; NBATIS; reporter verification as entry trigger |
| `examples/worked-scenarios/scenario-psg-defi-liquidity-ucl-2023.md` | DeFi liquidity; TVL check; LP activity signal; $PSG token with DeFi context |

### Women's sports market intelligence — 1 file

| File | Key intelligence |
|---|---|
| `market/market-womens-sports.md` | Cross-category commercial overview — WSL, NWSL, WNBA, WIPL · demographic advantage · Caitlin Clark catalyst · Tier 2→1 transition |

---

## Contributing

SportMind is built on the idea that domain knowledge should be open, shared, and improving.
Every sport has fans who understand it deeply — SportMind gives them a way to contribute
that knowledge in a form AI agents can use.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide. The short version:

1. Pick a sport or athlete skill not yet covered
2. Use the template in `templates/`
3. Follow the standard structure (domain model → risk variables → playbooks → commands → agent prompts)
4. Open a PR — maintainers review for accuracy and consistency

**14 community stub sports ready to be filled:**

`sports/badminton` · `sports/volleyball` · `sports/table-tennis` · `sports/sailing`
`sports/triathlon` · `sports/field-hockey` · `sports/squash` · `sports/curling`
`sports/gymnastics` · `sports/weightlifting` · `sports/judo` · `sports/taekwondo`
`sports/fencing` · `sports/swimming-open-water`

See [GOOD_FIRST_ISSUES.md](./GOOD_FIRST_ISSUES.md) for detailed contribution guidance.

---

## Roadmap

### ✅ v1.0 — Foundation
- 5 sport domain skills + 10 athlete skills + core schema + contribution framework

### ✅ v1.1 — Sport library expansion
- 22 complete sport domain skills + 15 contributor stubs + 17 athlete skills

### ✅ v1.2 — Fan token Layer 3 (5 core skills)
- fan-token-pulse, athlete-social-lift, transfer-signal, brand-score, sponsorship-match

### ✅ v1.3 — Performance and commercial intelligence
- performance-on-pitch, performance-off-pitch, transfer-intelligence, athlete-social-activity, sports-brand-sponsorship

### ✅ v1.4 — Football token intelligence bridge
- football-token-intelligence with FTIS, NCSI, ATM and World Cup 2026 framework

### ✅ v1.5 — F1, MMA, Esports token intelligence + full file rename
- formula1-token-intelligence, mma-token-intelligence, esports-token-intelligence
- F1 domain skill written; all 106 files renamed for clarity

### ✅ v1.5.2 — Comprehensive audit
- 40+ stale cross-references fixed; all attributions corrected; all docs updated

### ✅ v1.6.0 — Injury intelligence layer
- `core/injury-intelligence/` — 7 files: master framework + football, MMA, NFL, boxing,
  horse racing, cycling sport-specific modules; injury references added to 12 skills

### ✅ v1.7.0 — MLB Baseball
- `sports/baseball/` + `athlete/baseball/` — Statcast framework, PQS, BQS, pitcher-first analysis

### ✅ v1.8.0 — 8 new sport additions
- ice-hockey domain (filled empty stub), rugby-league athlete skill (missing counterpart),
  MotoGP, AFL, handball, kabaddi, NASCAR domain skills
- Layer 1: 22 → 28 complete | Layer 2: 18 → 19 complete

### ✅ v1.9.0 — Layer 4: Market Intelligence (complete)
- 33 market files covering all 28 sports — fan token readiness tier (1–4), global revenue,
  fanbase demographics, institutional blockchain interest, media rights trajectory,
  token catalyst events, competitor landscape, and 12 cross-sport key findings

### ✅ v1.9.1 — Cross-sport key findings
- `market/market-key-findings.md` — 11 cross-sport insights only visible at full-library
  level: audience size trap, China platform incompatibility, fantasy sports gateway, private
  equity as strongest institutional signal, US regulatory gating variable, horse racing
  syndication analogy, TV vs digital demographic split, centralised commercial structure
  advantage, NASCAR sponsor loyalty alignment, Indian regulatory variable, young generation effect

### ✅ v2.0.0 — Layer 5: Macro Intelligence
- 8 macro files: pandemic (counter-cyclical token proof), geopolitical (Russia-Ukraine case
  study), crypto market cycles (CHZ/BTC ~0.80 correlation, 4-phase modifiers), broadcast
  disruption (RSN collapse), economic cycles (recession hierarchy), climate (outdoor risk),
  governance scandal (FIFA/doping/match-fixing)
- v2.0 roadmap item corrected and updated to reflect actual completed content

### ✅ v2.1.0 — Fan Token Lifecycle and Partnership Intelligence
- `fan-token/fan-token-lifecycle` — Six-phase lifecycle model (pre-launch → active utility
  → plateau → non-contractual); the non-contractual token principle (fan tokens cannot be
  cancelled — they transition from governance to predictive utility); CEX/DEX trajectory
  model; prediction market as post-partnership utility; LTUI metric
- `fan-token/fan-token-partnership-intelligence` — Partnership Health Score (PHS) composite;
  Tier 1–5 new partnership signal taxonomy with CHZ impact ranges; termination patterns
  (announced, silent lapse, forced, category exit); Type A/B/C case study taxonomy
  ($JUV/$ACM as ACTIVE active-partnership Type A; $FAZE as Type B uncertain status;
  smaller club tokens as confirmed Type C); community empowerment principle
- Full library audit: 9 stray ghost directories removed; signal weights table rebuilt
  with all 30 sports; `fan-token-layer-overview.md` updated to 16 skills; all integration
  examples updated to 5-layer architecture; GOOD_FIRST_ISSUES corrected

### ✅ v2.1.1 — Library-wide audit and consistency pass
- No new skills; documentation accuracy and alignment pass across all files
- `core/core-signal-weights-by-sport.md`: fully rebuilt with all 30 sports in correct
  table structure; previously had NHL/MotoGP/AFL/Handball/Kabaddi/NASCAR in the wrong
  table and 16 sports missing entirely
- `fan-token-layer-overview.md`: title, skill count, diagram, and internal roadmap all
  updated to reflect current 16-skill state
- `sportmind-overview.md` structure tree: every layer and skill line now states its
  purpose for AI agents; signal weights expanded from 17 to 30 sports
- `llms.txt`: corrected sport table (28 stable, 14 stubs), athlete count (19),
  Layer 3 table (16 skills), duplicate entries removed, architecture heading fixed
- All integration examples updated to 5-layer loading order
- `CONTRIBUTING.md` and `GOOD_FIRST_ISSUES.md`: stub count corrected to 14;
  completed skills removed from "missing" list
- 9 empty ghost directories from earlier bash brace-expansion commands removed

### ✅ v2.2.0 — Core intelligence expansion + developer tooling
- `core/confidence-output-schema.md` — Standard JSON output schema for all SportMind agents;
  composable output format with signal, modifiers, flags, reasoning, sizing, and token signal fields
- `core/core-officiating-intelligence.md` — Referee, judge, and umpire intelligence framework
  for football, MMA/boxing, cricket, NFL, horse racing, and tennis
- `core/core-weather-match-day.md` — Match-day weather signal framework covering cricket (DLS,
  dew factor, pitch moisture), horse racing (going conditions), NFL (wind/cold), football,
  golf, rugby, and athletics (legal wind limits)
- `core/core-fixture-congestion.md` — Universal congestion framework: five congestion tiers
  with modifiers; sport-specific guidance for football, NBA B2B, NRL/Origin, NFL short week,
  cricket, MMA fight frequency, cycling Grand Tour fatigue
- `core/core-draft-intelligence.md` — Draft event intelligence for NFL, NBA, NHL, MLB,
  AFL, and esports; pick tier signal taxonomy with CHZ/token impact ranges; draft calendar
- `core/core-narrative-momentum.md` — Eight narrative categories (revenge, record proximity,
  comeback, career first, rivalry, memorial, elimination, narrative fatigue) with modifiers;
  narrative detection framework; fan token interaction model
- `agent-prompts/agent-prompts.md` — 7 production-ready system prompts for immediate developer
  deployment: football fan token, MMA fighter, multi-sport prediction market, commercial
  intelligence, draft intelligence, research/education, and minimal single-sport starter
- `glossary.md` — Central terminology reference covering all 28 sports and all 31 named
  SportMind metrics; reduces agent and developer terminology confusion
- `fan-token/fan-token-why.md` — Foundational value thesis: three structural ceilings
  of the traditional model (stadium capacity, revenue geography, spectator-only), how fan
  tokens solve each, scalability mathematics (stadium vs global addressable audience),
  participation economy context, five-phase future trajectory (engagement → performance →
  venue → media rights → RWA/SportFi), agent reasoning implications, developer opportunity
- `market/market-womens-sports.md` — Women's sports cross-category market intelligence;
  WSL, NWSL, WNBA, WIPL commercial profiles; demographic advantage analysis; Caitlin Clark
  as primary commercial catalyst; Tier 2→1 transition framework

### ✅ v2.3.0 — Fan Token Why — Foundational Value Thesis
- `fan-token/fan-token-why.md` — The foundational value thesis explaining why fan tokens
  exist as a category and what structural problems they solve that the traditional model
  cannot. Covers: three structural ceilings (stadium capacity, revenue geography, spectator-
  only model); the scalability mathematics (0.011% of global fans in the stadium vs 100%
  addressable via tokens); the participation economy context; five-phase future trajectory
  (engagement → performance → venue → media rights → RWA/SportFi); agent reasoning
  implications; developer commercial opportunity. Read before any other Layer 3 skill.
- fan-token-layer-overview.md updated with mandatory preface directing agents and developers
  to read fan-token-why.md first; Layer 3 count updated to 17

### ✅ v2.4.0 — Blockchain Validator Intelligence + Data Sources
- `fan-token/blockchain-validator-intelligence/` — PSG dual-layer model (fan token +
  Chiliz Chain validator); what validator status means technically; on-chain signal
  detection (stake changes, reward withdrawals, governance votes, uptime); Validator-
  Adjusted PHS = Average(UEF, CSP, HCT, TUI, PDS, VSI) × 1.10; future trajectory
  (multi-club, league, athlete, and sports-specific chain validators)
- `core/data-sources.md` — Centralised source citations for all five layers; source
  quality hierarchy (Tier 1–4); developer API quick reference; citation format standard
- `fan-token/fan-token-partnership-intelligence/fan-token-partnership-intelligence.md` updated: VSI added as sixth PHS
  indicator; Validator-Adjusted PHS formula; validator floor rule
- `market/market-key-findings.md` updated: Finding 12 — validator sports brands as new
  institutional category; commercial implications; agent monitoring guidance
- `macro/macro-crypto-market-cycles.md` updated: validator clubs and bear market dynamics;
  structural floor thesis; multi-validator scenario

### ✅ v2.4.1 — Full library audit and consistency pass
- Holistic v2.4.0 milestone audit; no new skills
- Heading inconsistencies fixed across 29 files: 5 L1 sports (wrong "Fan Token Skill"
  suffix), 10 L2 athlete skills (old "athlete-X" format), 14 stub sports (lowercase names)
- Named metrics aligned: VSI added to glossary; GSAx added to overview (34 metrics total)
- L3 count corrected to 18 in overview; placeholder SportMind standardised in 3 files
- All integrity checks pass: 0 broken refs, 0 empty files, 0 stale content in live files

### ✅ v2.5.0 — Full skill validation pass
- Validator updated with section name and field name variant matching
- All 61 skill files (28 complete sports + 19 athlete skills) now pass validation: 0 errors
- Signal Weight sections added to 9 sports; Key Commands to 13; Data Sources to 6
- Event Playbooks added to rugby union and tennis (previously had 0 playbook-format blocks)
- Additional playbooks added to rowing, swimming, handball, kabaddi, netball, rugby-league
- Playbook field completions across 13 sports; Integration Examples added to 13 athlete skills
- Structural sections added to baseball, rugby-league, meta athlete skills

### ✅ v2.6.0 — DeFi intelligence + basketball/cricket bridges + 10 athlete skills
- `fan-token/defi-liquidity-intelligence/` — DeFi and liquidity pool intelligence:
  TVL as pre-execution filter, slippage calculation, LP activity signals, DEX vs CEX
  price discovery, on-chain yield framework, prediction market protocol context,
  liquidity_warning and liquidity_critical flags added to confidence output schema
- `fan-token/basketball-token-intelligence/` — NBA/EuroLeague bridge:
  NBATIS metric, player-centric signal model, trade deadline calendar, load management,
  Top Shot precedent, EuroLeague club-centric model comparison
- `fan-token/cricket-token-intelligence/` — PSL/IPL/ICC bridge:
  CricTIS metric, format-dependent signal model, India-Pakistan × 2.00 multiplier,
  IPL regulatory gap documentation, PSL token framework, DLS/dew intelligence
- 10 new Layer 2 athlete skills: formula1, afl, motogp, handball, kabaddi, nascar,
  netball, rowing, swimming, winter-sports — completing coverage for all 28 L1 sports
- `agent-prompts/` updated with Prompt 8: DeFi-aware fan token agent
- `fan-token-why.md` Phase 5 updated with DeFi infrastructure detail
- `core/confidence-output-schema.md` updated with liquidity_warning, liquidity_critical
  flags and defi_context object
- `core/data-sources.md` updated with DeFi data sources section

### ✅ v2.7.0 — Production agent tooling + World Cup 2026 + Full audit
- `README.md` — fast entry point: 5-minute quickstart, layer table, key file guide
- `examples/worked-scenarios/` — 6 complete historical scenarios with calibration:
  UCL Final 2023 (football), UFC 281 Pereira vs Adesanya (MMA + macro override),
  State of Origin 2023 G3 (rugby league + congestion), IPL 2023 DLS cricket,
  NBA Trade Deadline 2023 (player-centric model), PSG DeFi liquidity UCL 2023
- `core/multi-agent-coordination.md` — production agent architecture: context window
  management, file size reference, minimum viable loading sets, session state caching,
  multi-sport routing table, conflict resolution hierarchy, edge case handling,
  calibration logging schema
- `market/world-cup-2026.md` — World Cup 2026 consolidated module: 48-team format,
  NCSI by top player, national token opportunities, commercial scale, signal calendar,
  US market unlock analysis, developer product opportunity guide
- Full library audit: all counts aligned, scenario numbering corrected, all checks pass

### ✅ v2.8.0 — Platform layer: API contracts + integration registry
- `platform/platform-overview.md` — what the platform adds; open intelligence guarantee;
  division of responsibility (data providers give base_score; SportMind reasons around it);
  three usage modes (library / contract / integrated)
- `platform/api-contracts.md` — formal skill call specifications for all skill types:
  modifier.athlete, modifier.macro, modifier.defi, modifier.congestion/officiating/weather/
  narrative, signal.full, signal.domain, intelligence.partnership/lifecycle/validator/commercial;
  versioning (v1.0 current; v1.x additive; v2.0 breaking with 6-month notice); error format
  with agent_action guidance; generic integration pattern for any data platform
- `platform/integration-partners.md` — registry of how external systems connect:
  FanTokenIntel (primary signal partner with autopilot template), Chiliz/Socios
  (blockchain infrastructure), Azuro (prediction market DeFi), sports data providers
  (Opta/Stats Perform/Sportradar), DeFi data providers (DeFiLlama/GeckoTerminal),
  LLM providers (agnostic); adding new partner documentation guide
- `core/confidence-output-schema.md` updated: full versioning changelog (v1.0→v1.1
  migration documented); schema validation Python function updated; platform contract
  reference added

### ✅ v2.9.0 — Pre-v3.0 gap fixes + live signals specification
- Four gap fixes: GOOD_FIRST_ISSUES corrected (all 29 athlete skills now complete);
  multi-agent-coordination.md updated with platform contract reference; Prompt 9
  World Cup 2026 added to agent-prompts; contract mode section added to all prompts
- `platform/live-signals.md` — The foundation of SportMind's self-updating architecture:
  6 live signal categories (macro state, on-chain, DeFi/liquidity, athlete/team,
  weather/conditions, prediction markets); 3 monitoring patterns (continuous/session/event);
  self-update signal triggers; developer integration code; relationship to v3.0 roadmap
- Named metrics table updated: NBATIS and CricTIS added (36 metrics total, aligned with glossary)
- Full pre-v3.0 audit: all checks pass — 0 validator errors, 0 broken refs, 0 empty files

### ✅ v3.0 — Platform, intelligence, and community infrastructure
- `core/sportmind-score.md` — Unified cross-sport confidence metric (SMS): four components
  (layer coverage, data freshness, flag health, modifier confidence); cross-sport
  comparability; combined decision matrix with adjusted_score; Python helper function
- `platform/skill-registry.md` — Queryable catalogue of all 200+ skills: skill IDs for
  all L1-L5 skills; registry query patterns; minimum viable skill sets; contributor
  metadata standard
- `core/calibration-framework.md` — ML-calibrated modifier weights infrastructure:
  outcome tracking schema; direction accuracy + magnitude calibration methodology;
  sport-specific calibration targets; 5-step calibration workflow; contribution guide
- `platform/monitoring-alerts.md` + CI workflows — Macro signal monitoring: 6 alert
  specifications (crypto cycle, geopolitical, economic, format change, new partnership,
  regulatory); webhook format; GitHub Actions macro-monitor.yml and skill-monitor.yml;
  platform/macro-state.json for fast session-start macro check
- `i18n/` — Multi-language support: framework README; Spanish starters (football, MMA);
  Portuguese starter (football with Brazilian market context); translation contribution
  guide with leaderboard incentive (+8 points per skill per language)
- `community/leaderboard.md` + `community/accuracy-tracking.md` — Community leaderboard:
  5-tier system (New → SportMind Expert); points formula; accuracy measurement methodology;
  outcome record format; submission process
- `core/confidence-output-schema.md` updated to v1.2: sportmind_score object added
- `.github/workflows/` updated: macro-monitor.yml and skill-monitor.yml added

### ✅ v3.0.1 — Post-release fixes
- `README.md` updated: badge 185+ → 211+; output schema updated to v1.2 with
  sportmind_score and defi_context objects; Start here table expanded with 6 new
  entries (platform contracts, testing scenarios, context window, skill registry);
  Compatible frameworks section updated with contract mode and integration partners
- `community/calibration-data/` directory created with README and submission schema
- `platform/monitoring-sources.json` created: 8 competition format sources, 2
  partnership sources, 2 regulatory sources with full configuration metadata
- `scripts/` expanded from 1 to 5 files: check_macro_signals.py (BTC 200-day MA
  checker with CoinGecko API, confirm logic, and webhook delivery),
  update_macro_state.py (macro-state.json timestamp updater), check_skill_freshness.py
  (multi-source freshness monitor with GitHub issue creation), check_token_partnerships.py
  (Socios/Chiliz partnership monitor with registry comparison)

### ✅ v3.1 — Calibration data, i18n expansion, skill registry API
- `community/calibration-data/` — 5 seed outcome records (football UCL Final 2023,
  MMA UFC 281 + macro override, NBA KD Trade 2023, Cricket IPL DLS 2023, Rugby League
  State of Origin 2023 G3); direction accuracy 100% across all 5 sports; INSUFFICIENT_DATA
  correctly flagged for all modifiers (minimum event thresholds not yet reached)
- `scripts/calibration_aggregate.py` — Full calibration pipeline: loads all outcome
  records from community/calibration-data/, calculates direction accuracy by sport and
  confidence tier, modifier accuracy with calibration status, generates JSON reports
- i18n expansion: 5 new starter translations across 3 languages:
  French (`fr`): football (Ligue 1/PSG/French cup context) + handball (EHF French clubs)
  Arabic (`ar`): football (Saudi Pro League/MENA market/Mohammed Salah context)
  Hindi (`hi`): cricket (IPL/India regulatory gap/dew factor) + kabaddi (PKL/raider model) + mma (UFC India market)
  All include culturally specific market context not in English originals
- `scripts/skill_registry_api.py` — Live queryable skill registry: parses
  platform/skill-registry.md into JSON; CLI query by sport/type/layer/status/id;
  minimum viable skill sets per use case; HTTP server mode (--serve --port 8080);
  currently parses 85 skills (71 stable + 14 stubs)
- Note: ML modifier recalibration requires 50–200+ events per modifier type (sport-dependent)
  Pipeline is ready; community data accumulation is the gating factor

### ✅ v3.2 — Bridge skills, i18n deepened, registry endpoint, leaderboard
- 3 new Tier 2 bridge skills: NFL, AFL, Rugby Union — highest-priority missing L3 skills
- i18n deepened: FR athlete football, PT MMA (UFC Brazil context), ES cricket (LATAM)
- `platform/skill-registry-api.md` — versioned GitHub Pages endpoint documentation
- Community leaderboard: first entries populated (sportmind-core seed records)
- `CONTRIBUTING.md` updated: calibration data, i18n, platform contributions documented
- L3 count: 21 → 24 skills

### ✅ v3.3 — Hosted Skills API
- `scripts/sportmind_api.py` — the hosted SportMind Skills API: content delivery server
  serving all 159 skill files on demand; GET /skills/{id}/content, GET /stack for full
  intelligence stacks; GET /macro-state; GitHub Pages static export; CLI tools
- `.github/workflows/publish-api.yml` — auto-deploys on every push touching skill files
- `platform/skill-registry-api.md` updated with API-first patterns
- `README.md` updated: API mode added as third usage pattern; Option B → Skills API

### ✅ v3.4 — Bridge skills, i18n, calibration records, API prompt
- Rugby League bridge skill (RLTIS): State of Origin disruption model, downstream NRL
  congestion signal, NRL/Super League calendar, women's rugby league
- Handball bridge skill (HandTIS): PSG brand halo cross-sport token signal (+3-5% $PSG),
  EHF Final4 Budapest architecture, GK save rate as override variable
- i18n: Arabic handball (PSG/QSI ownership context, bilingual), Hindi MMA (UFC India market)
- Calibration data: 7 seed records total (added F1 British GP 2023, NBA Finals G5 2023)
- Prompt 10: API mode agent demonstrating Skills API integration pattern

### ✅ v3.5 — Security layer
- `scripts/security_validator.py` — prompt injection scanner (30+ pattern categories),
  SHA-256 integrity verification against skill-hashes.json, calibration provenance checks
- `platform/skill-hashes.json` — SHA-256 hashes for all 179 skill files; agents verify
  received content before injecting into context
- `SECURITY.md` — threat model (5 threats), infrastructure documentation, responsible
  disclosure process, trust tiers, security checklists for contributors and developers
- `.github/workflows/security-check.yml` — CI: injection scan + integrity + provenance
  on every PR; auto-update hashes on merge to main
- `scripts/sportmind_api.py` updated: sha256 hash included in every content response
- All 7 calibration records backfilled with provenance (submitted_by, submission_timestamp,
  data_quality fields)
- Security check result: 0 CRITICAL, 0 HIGH, 34 MEDIUM (all legitimate external URLs
  in data source documentation)

### ✅ v3.6 — Bridge skills, i18n, first calibration report
- Baseball bridge (MLBTIS): pitcher-first model, Ohtani dual signal, Latin America +
  Japan markets, trade deadline calendar, 162-game season weighting
- Ice Hockey bridge (NHLTIS): GSAx goaltender primary variable, Game 7 architecture,
  Canadian market 3× US per-capita, B2B fatigue modifier, European cross-market signal
- MotoGP bridge (MotoTIS): Dorna single-deal advantage, rider-centric token model,
  wet race hierarchy reversal, Southeast Asia 500M+ market, sprint race signal (2023+)
- i18n: Spanish handball (Barcelona/ASOBAL token context), Portuguese cricket (Brazilian
  diaspora market, dew factor, IPL gap)
- Calibration: first aggregate report across 7 seed records with full methodology
  documentation; 100% direction accuracy (expected/informational); all modifiers
  correctly showing INSUFFICIENT_DATA; key insight: macro override + downstream
  congestion signals documented as most commercially valuable seed learnings

### ✅ v3.7 — Tier 2 bridge completion, validator extended
- NASCAR bridge (NASCARTIS): 72% sponsor loyalty; Daytona 500 peak event model;
  Championship 4 ×1.25 motivation; charter vs open team; track type taxonomy
- Kabaddi bridge (PKLTIS): star raider primacy model; All Out event signal;
  JioCinema commercial infrastructure; India VDA regulatory catalyst
- Netball bridge (NetTIS): fastest Tier 2→1 transition; Trans-Tasman ×1.25;
  shooter accuracy modifier; centre pass conversion; World Cup 2027 window
- i18n FR athlete handball: GK override rule; PSG cross-sport token signal in French;
  composite modifier pipeline; EHF Final4 integration example
- Calibration report: `community/calibration_report.json` generated (missing v3.6 item)
- Skill validator extended: now covers 84 files (71 core skills + 13 bridge skills);
  BRIDGE_REQUIRED_SECTIONS defined; variant for cricket bridge heading added

### ✅ v3.8 — Application blueprints
- `examples/applications/` — 6 fully specified developer application blueprints:
  App 1: Decentralised Sports Prediction Finance (SportMind + Azuro; signal separation;
    SMS-gated market publication; DeFi execution check; regulatory note)
  App 2: Fan Token Portfolio Intelligence (contextual explanation for holders; lifecycle
    phase awareness; upcoming signal calendar; NCSI spillover narrative)
  App 3: Athlete Commercial Intelligence Platform (ABS/APS/AELS/AFS workflow; full
    commercial brief format; portability assessment; sponsorship ranking)
  App 4: Sports Brand Token Strategy Tool (LTUI modelling; PHS projection; regulatory
    scan; timing recommendation; full due diligence output format)
  App 5: World Cup 2026 Intelligence Dashboard (live NCSI tracker; tournament signal
    calendar; club token impact monitor; US market unlock module)
  App 6: Sports GameFi Intelligence Layer (SMS-weighted scoring; flag-aware pick
    locking; macro state game events; on-chain pick integrity via skill hashes)

### ✅ v3.9 — SportFi Kit integration
- `platform/integration-partners.md` — Partner 7: SportFi Kit full integration documentation
  What SportFi Kit is (React/TypeScript toolkit for Chiliz Chain dApps), exact layer
  separation (SportFi Kit = application/UI/contracts; SportMind = intelligence),
  7-application mapping table, complete integration code pattern, setup instructions
- `examples/applications/app-07-sportfi-kit-integration.md` — Full-stack blueprint:
  useSportMind() React hook, PredictionWidget component, PortfolioIntelligence component,
  environment-aware MacroBanner, integrity verification pattern, Vercel deployment config
- Applications README updated: 6 → 7 blueprints

### ✅ v3.10 — MCP server, temporal awareness, security expansion, i18n deepening
- `platform/sportmind-mcp-server.md` — Full MCP specification: 4 tools (sportmind_signal,
  sportmind_macro, sportmind_stack, sportmind_verify), JSON schemas, example responses,
  Claude Desktop config, Anthropic API remote integration, tool sequencing rules
- `scripts/sportmind_mcp.py` — Working MCP server implementation: stdio + HTTP transport,
  all 4 tools implemented, SMS computation, freshness notes
- `core/temporal-awareness.md` — 6-tier information freshness taxonomy: Tier 0 (permanent
  domain knowledge) through Tier 5 (live DeFi/match data); staleness formulas; production
  deployment patterns; the SportMind boundary (models vs live data)
- `SECURITY.md` expanded — Threat 6 (prompt theft): system prompt protection patterns,
  MCP tool mode as more secure alternative to system prompt injection;
  Threat 7 (meta-injection): scope enforcement rules, query classification guard,
  relationship between file-level injection (Threat 1) and query-level injection (Threat 7)
- `i18n/hi/sports/cricket/` deepened: 141 → 266 lines; IPL calendar with Auction signal
  timing, IPL franchise token readiness ranking (MI, CSK, RCB, KKR), 2026 T20 World Cup
  India hosting catalyst, dew factor by venue (Wankhede, Eden Gardens, Chepauk),
  ICC tournament calendar with token signal impact
- `i18n/fr/sports/football/` expanded: 151 → 264 lines; full Ligue 1 commercial context
  (DAZN rights, 18-club format, relegation signal), PSG $PSG deep analysis (QSI
  geopolitical context, ATM by position, PSG Handball halo documented), NCSI for Équipe
  de France (Euro 2028, WC 2026 projections), all French derbies with multipliers,
  French regulatory context (ANJ, AMF/PSAN, MiCA)

### ✅ v3.11 — International football cycle, governance + scouting apps, agentic workflows, compressed skills
- `market/international-football-cycle.md` — Perpetual cycle model: 3-tier NCSI hierarchy
  (World Cup/Euros=1.00, Nations League=0.75, friendlies=0.10-0.25), post-tournament
  4-phase transition model (narrative → transfer → restart → return), Euro 2028 planning
  framework, international break protocol (10 windows/year), tournament fatigue modifier
  (×0.85 September after Tier 1 tournament), full NCSI weight table for all competition types
- `market/world-cup-2026.md` — Updated with post-tournament transition and cycle reference
- `examples/applications/app-08-governance-intelligence.md` — LTUI impact per vote,
  APS for signing decisions, PHS for partnership votes, governance brief format,
  SportFi Kit integration (useGovernanceVote hook)
- `examples/applications/app-09-talent-scouting.md` — Full 7-section scout report:
  PI + DTS + TAI/PS + APS + AELS/SHS + TVS/TSI + LTUI impact; post-tournament APS
  recalculation rule; international cycle connection
- `examples/agentic-workflows/README.md` — 4 patterns:
`examples/agentic-workflows/multi-agent-coordination.md` — coordinated system:
`examples/agentic-workflows/league-monitoring-agent.md` — Pattern 5: league stakes/relegation/title races:
`examples/agentic-workflows/athlete-commercial-tracker.md` — Pattern 6: APS/AELS/SHS commercial monitoring: portfolio monitor (4h schedule),
  pre-match chain (T-48h + T-2h), tournament tracker (NCSI per match result + elimination),
  transfer window monitor (rumour tier → TSI → APS recalculation → confirmation)
- `compressed/README.md` — 10 compressed skill summaries: ~1,070 tokens total vs ~32k full
  (97% compression); football, cricket, basketball, MMA, F1, football token intel, macro,
  lifecycle, DeFi, confidence schema

### ✅ v3.12 — Manager intelligence, reasoning patterns, athlete financial intelligence, RWA/SportFi layer
- `core/manager-intelligence.md` — Manager Signal Index (MgSI), new manager effect model
  (permanent ×1.10 match 1-3; caretaker ×1.12 match 1-2 then ×0.93 drag from match 6+),
  sacking signal 5-stage progression, manager conduct intelligence (touchline cards, fines,
  player conflicts), sport-specific manager models (football, rugby, basketball), career
  record JSON schema
- `core/reasoning-patterns.md` — Formal six-step SportMind reasoning chain (macro →
  competition → athlete availability → signal computation → DeFi check → confidence output),
  conflict resolution hierarchy (4 priority levels), uncertainty protocols, sport-specific
  chain variations, 7 anti-patterns, pre-output validation checklist
- `core/athlete-financial-intelligence.md` — Financial APS adjustment formula
  (APS_adjusted = APS_base × Wage_Feasibility × Image_Rights_Factor × Contract_Stage),
  wage tier structure, contract stage multipliers (×0.85 at 4+ years to ×1.30 at expiry),
  image rights taxonomy (player-controlled +0.05, token-native +0.08-0.12), bonus/incentive
  signals (UCL appearance bonus, loyalty bonus pending flag, release clause active flag)
- `fan-token/rwa-sportfi-intelligence/rwa-sportfi-intelligence.md` — Phase 5 intelligence:
  RSF (RWA Signal Framework), staking yield quality taxonomy (commercial=1.00,
  protocol=0.65-0.80, emissions=0.20-0.45), outcome-linked supply mechanics (Chiliz
  gamified tokenomics → SportMind sits upstream), tokenised media rights framework,
  player performance bonds (DTS/PI/TAI/ABS as bond pricing inputs), CollateralFi
  (liquidation cascade pattern), monthly monitoring framework

### ✅ v3.13 — Rugby/cricket cycles, all sport compression, community calibration framework
- `market/international-rugby-cycle.md` — Rugby union NCSI hierarchy (RWC=1.00, Six Nations
  decider=0.80, Lions=0.75, Autumn Internationals=0.35-0.50), 4-phase post-tournament
  transition, CVC investment as tokenisation signal; rugby league cycle (State of Origin
  NCSI=0.90, downstream NRL congestion as most valuable underpriced signal, RLWC calendar)
- `market/international-cricket-cycle.md` — Three-tier NCSI hierarchy across all cricket
  competitions, India premium (×1.40 permanent; India-Pakistan ×2.00), ICC tournament
  calendar (T20 WC odd years, ODI WC every 4 years, WTC 2-year cycle), bilateral hierarchy
  (Ashes=0.75, Border-Gavaskar=0.70), domestic leagues (IPL NCSI=0.35-0.70), bilateral
  series momentum model, domestic league interaction framework
- `compressed/README.md` — All 32 sport domain compressed skills added (22 new): rugby
  union/league, AFL, American football, tennis, baseball, ice hockey, MotoGP, NASCAR,
  esports, boxing, handball, kabaddi, netball, golf, horse racing, darts, snooker,
  athletics, cycling, swimming, rowing, winter sports. Index updated: 33 total compressed
  skills (~3,360 tokens total vs ~85,000 full; 96% compression ratio)
- `community/calibration-data/CONTRIBUTING.md` — Complete community contribution framework:
  validity requirements, step-by-step submission process, JSON template, file naming
  convention, quality tiers (Gold/Silver/Bronze/Rejected), prioritised sports and modifiers
  (dew_modifier and rivalry_form_discount closest to 50-record threshold), recognition and
  leaderboard system, calibration review process with 70% community consensus requirement

### ✅ v3.14 — Derby intelligence, league advanced, cup competitions, ticketing, NFTs/collectibles
- `core/derby-intelligence.md` — DSM (Derby Signal Model): 30 global football derbies with
  specific signal characteristics (El Clásico 50% form compression, Superclásico very high
  conduct risk, Old Firm maximum form compression), dual-token protocol for both-active fixtures,
  cross-sport rivalry template for all other sports, derby_active flag
- `market/football-leagues-advanced.md` — Big Five league-specific intelligence: relegation
  financial stakes (PL £170M, Bundesliga 50+1 context), continental qualification mechanics,
  prize window calendars per league, La Liga/Serie A/Bundesliga/Ligue 1 specific signals,
  MLS/Eredivisie/South American competitions, ticket demand as pre-event signal layer,
  cup signal tiers per competition
- `core/cup-competition-intelligence.md` — CSF (Cup Signal Framework): competition prestige ×
  round_weight × opponent_quality_gap × rotation_risk, UCL/UEL/UECL/Copa Libertadores models,
  FA Cup round-by-round (R3 giant-killing signal, Final = LTUI positive for domestic clubs),
  Copa del Rey/DFB-Pokal/Coppa Italia/Coupe de France, token-gated cup access utility events,
  memory ticket collectibles, annual cup calendar
- `core/core-narrative-momentum.md` updated — Ticket demand pre-event signal section:
  sell-out status ×1.05 narrative modifier, secondary market pricing as leading indicator,
  HAS spike follows resale price spike by 24-72h, T-72h check protocol
- `fan-token/fan-token-lifecycle/` updated — Token-gated ticketing Phase 2 utility section:
  priority access LTUI +8-12, discount LTUI +3-6, memory ticket LTUI +3-7, combined cup
  qualification + ticket utility LTUI +10-15, Phase 3 warning signals from ticketing uptake
- `fan-token/rwa-sportfi-intelligence/` updated — NFT/collectibles intelligence: positioning
  in Phase 2/4/5 spectrum, athlete NFT as APS/AELS proxy, APS +0.04-0.06 for successful
  collection, Sorare as ATM proxy, platform monitoring targets (Sorare, NBA Top Shot,
  Chiliz NFT products), agent boundaries for NFT data

### ✅ v3.15 — Identity, broadcaster intelligence, governance, MCP deployment, real-time patterns
- `WHO-WE-ARE.md` — Non-technical identity document for sports industry stakeholders:
  who SportMind is for (club directors, agents, broadcasters, developers, practitioners),
  what is inside (five layers + core + support), how to use, what makes it different,
  licence and governance
- `market/broadcaster-media-intelligence.md` — BVS (Broadcast Value Signal) formula,
  rights valuation benchmarks ($10B+ PL through PKL), streaming transition intelligence
  (fragmentation modifier), broadcaster as signal actor (rights acquisition/loss/price
  decline patterns), Drive to Survive effect (15-25% sport→documentary conversion),
  regional market intelligence (UK/India/USA/Middle East/SEA/Latin America)
- `fan-token/sports-governance-intelligence/` — GSI (Governance Signal Index),
  current Socios model assessment, 4 DAO types (owned clubs, fan councils, specific
  decision DAOs, multi-club), voting mechanics (simple/quadratic/conviction/delegated),
  governance lifecycle signals, governance_theatre flag, structural_vote_active flag
- `platform/sportmind-mcp-deployment.md` — GitHub Pages static API (generate_static_api.py
  script + refresh_deployment.py), Vercel live MCP serverless deployment, Docker
  self-hosted, Claude Desktop live endpoint config, production security checklist
- `platform/realtime-integration-patterns.md` — 5 complete integration patterns with
  working Python: macro state webhook (BTC/CHZ → cycle classification → modifier update),
  lineup confirmation webhook (key player absent → full reload), fan token on-chain monitor
  (HAS computation + TVL threshold + alerts), weather integration (cricket dew/DLS,
  F1 wet race, football wind), full pre-match pipeline (all sources in parallel)

### ✅ v3.16 — Athlete depth expansion, club operations, i18n expansion, calibration records
- `athlete/rugby/athlete-intel-rugby.md` — Full rugby union athlete intelligence:
  positional framework (15 positions with signal weights), kicker primacy model
  (40-50% of points; modifier range 0.85-1.22), set piece contribution (lineout/scrum),
  disciplinary record model, Lions selection signal (ATM ×1.15 at squad announcement),
  international availability calendar (6 Nations, Lions, Autumn Internationals)
- `athlete/cricket/athlete-intel-cricket.md` — Expanded: IPL franchise intelligence
  (auction signal tiers, retention > auction as confidence signal), format specialist
  model (T20/ODI/Test-specific modifiers), Indian player ATM tiers (Tier 1 icons
  through Tier 4 emerging), India-Pakistan ATM ×2.00 override, bowling phase
  intelligence (powerplay/middle/death with specific economy targets)
- `athlete/nba/athlete-intel-nba.md` — Expanded: NBA star ATM tiers, playoff
  modifier model (series context, elimination game ×1.08), trade deadline intelligence
  (pre/post-trade reliability modifier ×0.85 for 5 games), contract year effect
  (×1.08 motivation modifier)
- `market/club-operations-intelligence.md` — CHI (Club Health Index): Financial_Stability
  × Academy_Pipeline × Community_Engagement × Ownership_Quality × Infrastructure.
  Academy intelligence (first-team debut signal, academy director departure monitoring).
  Financial distress 4-stage progression (monitoring→investigation→sanction→administration).
  Community engagement tiers (Superleague proposal LTUI ×0.70 immediate). Ownership
  models (fan ownership/PE/SWF/corporate/LBO and each token implication). Stadium
  development signals (new stadium LTUI +5-10, naming rights LTUI +3-5).
- `i18n/pt/sports/football/` — Expanded: Brazil market (Flamengo 40M+ base,
  Brasileirão calendar, Copa Libertadores signal, Fla-Flu derby ×1.80), Portuguese
  market (Big Three: Benfica/Porto/Sporting), NCSI calculation for both markets,
  Brazil crypto adoption context, Copa Libertadores frame
- `i18n/ar/sports/cricket/` — New: UAE cricket context (expat market 8-10M fans),
  Dubai dew factor (very high), PSL token market (active on Chiliz), Ind-Pak
  in Neutral UAE venue signal, regional ATM framework in Arabic
- Calibration records: 3 new records added (basketball/NBA, rugby-union/Six Nations,
  football/FA Cup). Total: 10 records across 7 sports. New validations: cup rotation
  modifier (CSF), Six Nations narrative modifier, NBA athlete/on-off differential

### ✅ v3.17 — Autonomous agent framework, MCP agent status, multi-agent coordination, calibration drive, starter pack, freshness strategy
- `core/autonomous-agent-framework.md` — SportMind agent model: intelligence separation
  principle, autonomy spectrum (Level 0 supervised through Level 4 fully autonomous),
  agent lifecycle (7 states: INITIALISING → MONITORING → ANALYSING → ACTING/ESCALATING
  → WAITING → PAUSED → TERMINATED), decision framework matrix (SMS × flags → autonomous/
  advisory/escalate), agent-to-agent protocol (registration, signal sharing, conflict
  resolution), ecosystem integration protocol (FanTokenIntel/SportFi Kit/LLMs/data layer),
  6 safety principles, Python SportMindAgent base class (300+ lines, production-ready)
- `platform/sportmind-mcp-server.md` — 5th MCP tool added: `sportmind_agent_status`
  returns running agent state, health, cycle counts, pending escalations, upcoming events,
  data freshness; supports single agent and all-agents queries; enables agent observability
- `scripts/sportmind_mcp.py` — updated with sportmind_agent_status tool handler
- `examples/agentic-workflows/multi-agent-coordination.md` — four patterns as coordinated
  system: SignalBus (thread-safe shared signal store, conflict resolution by SMS then
  recency), trigger chain documentation (portfolio monitor → pre-match chain, pre-match →
  tournament tracker NCSI, transfer monitor → signal invalidation), ConflictResolver class,
  SystemOrchestrator (starts all 4 agents concurrently + health monitor), ecosystem
  integration in coordinated context (FanTokenIntel/SportFi Kit/LLMs as consumers)
- Calibration drive: 12 new records added; total 22 across 11 sports
- `examples/starter-pack/` — 6 working examples: 01-simple-signal.py (10 lines, minimum viable),
  02-claude-conversation.py (MCP + Claude as reasoning engine), 03-single-sport-agent.py
  (complete PSG token agent, Level 2 autonomy), 04-multi-sport-agent.py (football/cricket/MMA/F1/NBA
  with sport-specific routing), 05-sportfi-kit-integration.py (intelligence/execution boundary
  demonstrated, TypeScript equivalent), 06-autonomous-tournament-tracker.py (Level 3 autonomous,
  NCSI per match, audit log, daily briefing — no human input required)
- `platform/freshness-strategy.md` — Complete two-dimension freshness guide: library version
  (version_checker.py, changelog_monitor.py, VersionUpdateStrategy 3 options, GitHub webhook
  push notifications), application data (SportMindRefreshScheduler for all 6 tiers, freshness
  flags in confidence output, agent base class integration), quick reference table
  New sports validated: ice-hockey (GSAx goaltender signal), tennis (surface win%),
  formula1 (qualifying delta), afl (pending), motogp (pending)
  Key validations: weight_miss_modifier x0.72 (MMA — most important single MMA modifier),
  relegation_stakes_modifier x1.40 (first validation from football-leagues-advanced.md),
  PSL Final token signal (first cricket fan token price movement record: +12.4%),
  UCL QF draw outcome (first WRONG direction record — two-legged tie draw premium learning)

### ✅ v3.18 — Athlete depth (NHL/tennis/F1), league monitor, athlete commercial tracker, 30 calibration records
- `athlete/nhl/athlete-intel-nhl.md` — GSAx full model (formula, tiers, momentum component,
  backup quality delta), morning skate protocol (T-8h confirmation window), special teams
  intelligence (PP tier classification, combined PP+PK modifier), Canadian market signal
  (Maple Leafs/Canadiens narrative multipliers), trade deadline and draft intelligence
- `athlete/tennis/athlete-intel-tennis.md` — Grand Slam round-by-round model (R1×0.70
  through Final×1.15), surface specialisation model (clay ×0.82-1.18, grass ×0.88-1.15,
  hard/indoor), physical stamina model (5-set accumulation ×0.85-0.96, retirement risk ×0.65),
  ATM tiers (Sinner/Alcaraz Tier 1; rivalry signal ×1.15), surface transition modifier ×0.92
- `athlete/formula1/athlete-intel-formula1.md` — Driver-constructor pairing model (Tier 1-4
  hardware × qualifying delta interaction), circuit archetypes (street circuits qualifying ×1.40,
  power circuits ×0.85), season narrative intelligence (championship battle ×1.25, final race
  narrative_active), race weekend token signal calendar (qualifying → pre-race → race result)
- `examples/agentic-workflows/league-monitoring-agent.md` — Pattern 5: LeagueStandings
  (stake event detection: title race/CL qualification/relegation), LeagueMatchPrioritiser
  (signal scoring with prize window from football-leagues-advanced.md), LeagueMonitorAgent
  (standings change alerts, fixture prioritisation, signal bus publication, 6h cycle)
- `examples/agentic-workflows/athlete-commercial-tracker.md` — Pattern 6: AthleteCommercialProfile
  (APS/AELS/ABS/SHS/DTS/TAI history + trend analysis), CommercialEventDetector (10 event types:
  APS trend, pre-contract window, national call-up, injury warning, social crisis, NFT launch),
  AthleteCommercialTrackerAgent (12h cycle, Level 1 advisory, weekly briefing, audit log)
- Calibration drive: 8 new records (total 30 across 9 sports)
  Landmark: India-Pakistan T20 WC 2026 — ×2.00 modifier validated for most commercially
  significant cricket match. Monaco GP street circuit qualifying premium ×1.40 validated.
  El Clásico second wrong-direction record (draw) confirms derby uncertainty modelling.
  Direction accuracy: 27/30 (90%)

### ✅ v3.19 — Breaking news, fan sentiment, skill bundles, on-chain events, AFL/NFL depth, i18n, 40 calibration records
- `core/breaking-news-intelligence.md` — 8-category taxonomy (Category 1: match personnel
  through Category 8: macro breaking news), 4 protocols (RELOAD/MODIFY/VOID/ESCALATE),
  signal invalidation rules (hard vs soft), source tier model (1: official through 4: forum),
  sport-specific patterns for all 6 sports, autonomous agent integration with signal bus
- `fan-token/fan-sentiment-intelligence/` — Emotional arc model (6 phases: Peak 0-24h
  through Legacy 12+ months), CDI formula (Base × Outcome_Tier × Competition_Weight ×
  Drought_Factor), decay curve λ constants by outcome type, outcome profiles (standard win
  through relegation), fan type segmentation (core/seasonal/event-driven/new-market),
  LTUI integration (standard trophy +8-12; first drought-ending trophy +15-20)
- `platform/skill-bundles.md` — 14 named bundles with YAML definitions and token estimates,
  bundle API endpoint specification, Python helper functions, MCP bundle tool shorthand,
  custom bundle template and rules (macro first; schema last; loading order enforced)
- `fan-token/on-chain-event-intelligence/` — 6 signal categories (large wallet movements
  with % supply thresholds, LP pre-match activity with 15% change alerts, governance vote
  execution on-chain signals, staking ratio trend model, cross-chain bridge activity,
  wallet age as conviction proxy), OnChainEventMonitor Python implementation, integration
  with six-step reasoning chain (Step 5b), caution notes (correlation ≠ causation)
- `athlete/afl/athlete-intel-afl.md` — Expanded to 289 lines [GOOD]:
  positional framework (midfielders/forwards/backs/rucks), kicking accuracy model
  (>70% elite ×1.08; AFL fantasy score as form proxy >120pts ×1.12), MCG and
  ground-specific intelligence (Perth travel ×0.88, Darwin heat ×0.90), AFL season
  structure with finals multipliers (Grand Final ×2.00), Command + Modifier reference
- `athlete/nfl/athlete-intel-nfl.md` — Expanded to 365 lines [GOOD]:
  QB primacy model (Tier 1-4 with × 0.65-1.22 range; CPOE as primary stat),
  injury designation protocol (Wednesday-Saturday-Sunday inactives; RELOAD on backup start),
  weather and outdoor stadium model (wind >20mph ×0.88 passing; cold <10°F fumble risk),
  Super Bowl and NFL token market projections
- `i18n/es/sports/football/` — Expanded to 170 lines: LaLiga market (El Clásico ×1.75,
  Derbi Madrileño ×1.50), Latin American markets (Argentina crypto adoption, Superclásico
  ×1.85, Mexico Copa del Mundo 2026 co-host ×1.20), NCSI calculation for Spanish players,
  Copa del Mundo 2026 full Spanish-speaking nations analysis
- `i18n/pt/sports/cricket/` — New file 151 lines: Portuguese and Brazilian cricket market
  context, dew factor explanation in Portuguese, PSL token documentation, Ind-Pak ×2.00
  in Portuguese, ICC tournament calendar with lusophone market context
- `agent-prompts/agent-prompts.md` — 6 new prompts (10 → 16):
  Prompt 11 (Club commercial director: APS adjusted + LTUI impact),
  Prompt 12 (Sports agent: commercial brief for transfer negotiation),
  Prompt 13 (Fan token developer: bundle IDs + freshness + code examples),
  Prompt 14 (Breaking news response: RELOAD/MODIFY/VOID/ESCALATE classification),
  Prompt 15 (Pre-built prompt quick reference card: use-case → prompt mapping),
  Prompt 16 (Macro gate check: minimum viable macro prompt)
- `glossary.md` — Web3/DeFi sports terminology section: 36 new terms
  (AMM through whale) covering all fan-token layer vocabulary
- Calibration drive: 10 new records (total 40 across 11 sports)
  Landmark: T20 WC Final India vs Australia (dew factor chasing validated at highest level),
  AFL Grand Final (first AFL record; clearance differential validated),
  NHL Stanley Cup Final (Canadian market ×1.25 validated),
  NBA Finals G7 (elimination ×1.08 + contract year validated at championship),
  Lions Test 1 (first B&I Lions record; ATM ×1.15 signal validated),
  F1 Spa wet race (hardware reset confirmed; specialist from P6 won),
  Championship Playoff Final (promotion ×1.60; £200M stakes validated),
  UCL QF Leg 2 (two-legged tie learning incorporated from Leg 1 calibration)
  Direction accuracy: 38/40 (95%)

### ✅ v3.20 — World Cup 2026 deep module, MotoGP, EuroLeague, community infrastructure, 52 calibration records
- `market/world-cup-2026.md` — Expanded 282 → 601 lines: 48-team group stage intelligence
  (best-third-place qualification mechanics, decider match modifiers × 1.15-1.20), host
  nation profiles (USA 75M+ Latino fans, Mexico Azteca × 1.15, Canada diaspora commercial),
  group draw intelligence (dream vs death group, rivalry draw modifiers × 1.50-1.85),
  city-by-city demographics (MetLife/LA/Dallas/Miami/Toronto/Vancouver), automated WC2026
  monitoring framework (pre-tournament/daily/post-match agent cycle), market size estimates
  (conservative 500k-1M new holders through optimistic 5-10M), CDI projections (winner: 112.5 days)
- `athlete/motogp/athlete-intel-motogp.md` — Expanded STUB → GOOD (352 lines):
  hardware vs rider model (Tier 1-4 manufacturer × qualifying delta), rider ATM tiers (Italian
  ATM × 1.30 at Mugello, Spanish × 1.25 at Catalunya), circuit intelligence (Mugello tifosi,
  Sepang humidity, Phillip Island), The Márquez Factor (ATM 0.88 even post-peak), crash risk
  model (aggressive × 1.30, wet × 1.40), championship battle signal calendar
- `market/euroleague-basketball-intelligence.md` — New: ELS formula, club profiles by tier
  (Real Madrid ELS 0.94 through Fenerbahçe 0.82), EuroLeague competition structure (Final Four
  × 1.75, best-of-5 playoffs), NBA connection signals (draft prospect → signed departure ×0.90),
  national leagues (ACB Clásico × 1.50, Greek derby × 1.65, BSL Istanbul derby × 1.40)
- `community/calibration-data/CONTRIBUTING.md` — External contributor quick-start guide:
  step-by-step instructions for non-developers, reviewer criteria, calibration milestone
  tracker showing progress toward recalibration thresholds per modifier
- Calibration drive: 12 new records (total 52 across 12 sports)
  LANDMARK: World Cup 2026 Final France vs Brazil — $RMFC +19.4% validated; dual-nation
  NCSI at maximum competition level; CDI 112.5+ days. First MotoGP record (Mugello Italian
  ATM × 1.30). First EuroLeague record (Final Four × 1.75). WC2026 Group Stage + QF records.
  Post-tournament fatigue learning (PL opener draw = wrong direction but valuable learning).
  Direction accuracy: 49/52 (94%)

### ✅ v3.21 — KOL intelligence, agent model, Chiliz Agent Kit, fan digital twin, athlete depth, compressed refresh, 60 calibration records
- `fan-token/kol-influence-intelligence/` — KIS (KOL Impact Score): Tier × Reach × Sentiment
  × Timing × Credibility_Discount. 4-tier KOL classification (T1 >500k through T4 <5k).
  Paid vs organic detection (cluster deployment, timing correlation, #ad disclosure).
  Sports-specific KOL ecosystem (Romano "Here We Go" as Tier 1 event × 1.20; DTS = ultimate T1 KOL).
  Python KOL monitor. HAS integration: T1 KOL event = +12-25 HAS points; paid = marketing_activity only.
- `core/agent-intelligence-model.md` — Honest ANI/AGI/ASI framing: ANI (narrow excellence,
  intentional), AGI (not SportMind's target — domain excellence > general competence), ASI
  (domain aspiration: exceeds any individual expert through calibration + collective knowledge).
  Four dimensions mapped honestly: reasoning (6-step chain, 94% calibrated), planning (multi-cycle
  execution, not goal-setting — yet), learning (human-mediated calibration, validated improvement),
  context (WHO-WE-ARE + agent framework = full purpose understanding). Intelligence architecture
  layers 1-4. Developer implications.
- `platform/chiliz-agent-kit-integration.md` — Natural language intent → SportMind intelligence
  → gateway decision → Chiliz Agent Kit execution pipeline. 3 TypeScript patterns: intent parsing,
  pre-match action scheduler, governance vote analysis. Gateway decision safety layer implementing
  Safety Principle 1. Private key security guidance. SportFi Kit complete stack summary.
- `examples/applications/app-10-fan-digital-twin.md` — FLS (Fan Loyalty Score):
  Holding_Duration × Governance_Participation × Outcome_Engagement × Commercial_Participation.
  6 tiers: Prospect → Supporter → Enthusiast → Loyalist → Ultra → Legend.
  Dynamic NFT metadata structure with SportMind context block. Python FanDigitalTwinAgent.
  Token-gated experiences by FLS tier. Ethical framework (fan owns NFT; no private data harvested).
- `athlete/snooker/athlete-intel-snooker.md` — Expanded THIN → GOOD (264 lines):
  Crucible venue intelligence (experience modifier × 1.08; curse × 0.94), century rate model
  (> 1.0/frame elite × 1.12), Triple Crown calendar, ranking trajectory signals.
- `athlete/darts/athlete-intel-darts.md` — Expanded THIN → GOOD (305 lines):
  Three-dart average model (> 100.0 × 1.15), checkout percentage, Ally Pally night session
  (British crowd × 1.06), PDC tour card motivation signal, nine-dart ATM boost.
- `athlete/athletics/athlete-intel-athletics.md` — Expanded THIN → GOOD (335 lines):
  PB proximity model (within 0.5% of PB = peak form × 1.15), event specialisation framework
  (sprints/middle/distance/hurdles/field), championship vs Diamond League reliability
  (DL → championship × 0.92), Olympics 4-year narrative × 1.10.
- `compressed/README.md` — Refreshed: 33 → 54 compressed summaries. 8 new compressions:
  breaking-news, fan-sentiment, skill-bundles, on-chain-events, KOL-influence, agent-intelligence-model,
  world-cup-2026, euroleague-basketball. All v3.19+ major additions now have compressed forms.
- Calibration drive: 8 new records (total 60 across 15 sports)
  NEW SPORTS: snooker (World Championship), darts (PDC World), athletics (100m Worlds)
  Direction accuracy: 57/60 (95%). Records now cover 15 distinct sports.
  Post-WC2026 fatigue learning (England vs Hungary): fatigue less significant vs weaker opposition.
  NRL Grand Final × 2.00 validated. Death bowling specialist validated in PSL.

### ✅ v3.22 — Purpose/context document, agent goal framework, swimming/winter-sports, GitHub Pages, 70 calibration records
- `core/sportmind-purpose-and-context.md` — Single-load ~600 token context document:
  5 non-negotiable rules (macro first, loading order, intelligence separation, confidence
  honesty, sport-specific primary signal), ecosystem map (data→SportMind→application→execution),
  confidence output schema, SMS tiers, autonomy levels, key document map. Any agent loading
  this single file has complete operational context.
- `core/agent-goal-framework.md` — Three-level goal hierarchy (Terminal/Instrumental/Immediate),
  6 goal states (PENDING→ACTIVE→ACHIEVED/BLOCKED/FAILED/OBSOLETE), planning cycle with
  observation→evaluation→goal-generation, GoalDirectedAgent Python class extending base,
  5 goal-generation triggers (decomposition, achievement, signal, calendar, failure),
  plan-directed vs goal-directed comparison with use-case guidance.
- `athlete/swimming/athlete-intel-swimming.md` — STUB → GOOD (271 lines): taper model
  (peak taper ×1.15; post-meet fatigue ×0.90), PB proximity (within 0.5% ×1.12), event
  specialisation (sprint/middle/distance/medley/relay), multi-swim fatigue (×0.95/×0.90),
  Olympic cycle with national ATM multipliers (Australia ×1.20, USA ×1.18), record-breaking
  CDI model.
- `athlete/winter-sports/athlete-intel-winter-sports.md` — STUB → GOOD (292 lines): 4-discipline
  alpine framework (DH bib modifier ×0.93-1.05, SL two-run tactical, GS/SG), ski jumping wind
  hold rule (most important variable; variable conditions → widen confidence interval), biathlon
  shooting accuracy model (×1.12 per clean range), Crystal Globe pressure ×1.08, national ATM
  (Austrian skiing ×1.30, Norwegian cross-country ×1.35).
- `.github/workflows/publish-api.yml` — Updated: version extraction from llms.txt, version.json
  generation with library stats, security check before deploy, versioned commit message.
  `scripts/sportmind_api.py` — get_version_info() endpoint added (version, stats, MCP tools list).
- Calibration drive: 10 new records (total 70 across 16 sports)
  NEW SPORTS: swimming (World Aquatics Championships), winter-sports (Hahnenkamm Downhill) — 16th sport
  Landmark records: Ashes Test 1 Brisbane (Test cricket home advantage at Gabba validated),
  ATP Finals indoor hard court specialist, F1 season-long constructor model (SMS 80 — highest F1 record),
  MMA rematch reversal signal validated, NBA Christmas Day home net rating confirmed.
  El Clásico HOME WIN: confirms home advantage as tiebreaker even with 50% form compression.
  Direction accuracy: 67/70 (95%).

### ✅ v3.23 — All remaining stubs cleared, first recalibration, community recognition, 80 calibration records
- `athlete/handball/athlete-intel-handball.md` — STUB → GOOD (256 lines): goalkeeper primacy
  (>37% save rate ×1.12; 7m stopping >30% ×1.08), positional framework (GK>CB>Wing>Pivot signal
  hierarchy), EHF Champions League Final Four ×1.65, Danish/German national ATM premiums,
  international window signal ×0.88
- `athlete/kabaddi/athlete-intel-kabaddi.md` — STUB → GOOD (237 lines): raider primacy (>65%
  success ×1.25; super raid ×1.10), All Out tactical model (forcing team wins 72%; modifier ×1.10),
  do-or-die pressure record, PKL franchise intelligence (Patna Pirates, U Mumba), Hindi-belt ATM tiers
- `athlete/nascar/athlete-intel-nascar.md` — STUB → GOOD (277 lines): 4 track types (superspeedway
  variance ×0.80, short track specialist ×1.08, road course oval-racer ×0.88), NASCAR playoff bubble
  motivation ×1.12, Daytona 500 ×1.50 signal weight, Championship 4 winner-take-all model,
  Tier 1 equipment modifier, pit crew rating ×1.05
- `athlete/netball/athlete-intel-netball.md` — STUB → THIN+ (177 lines): shooting accuracy
  model (>92% elite ×1.12), super shot conversion, intercept rate ×1.08, Super Netball/World Cup
  context, national ATM (Australia ×1.30)
- `athlete/rowing/athlete-intel-rowing.md` — STUB → THIN+ (178 lines): ergometer PB model,
  boat class specificity (individual vs crew events), Henley/World Championships context,
  conditions modifier (head wind >3m/s significant)
- `core/modifier-recalibration-v3.md` — First empirical recalibration from 70 records:
  3 modifier UPDATES (derby draw premium → DRAW_LIKELY when form_differential < 0.10;
  post_tournament_opener flag created; two-legged Leg 1 draw premium formalised),
  5 modifiers CONFIRMED unchanged (athlete_modifier, qualifying_delta, india_pakistan ×2.00,
  morning_skate, competition_tier_weight), 3 wrong-direction records fully analysed,
  recalibration methodology documented, path to full thresholds mapped
- `community/CONTRIBUTORS.md` — Community contributor recognition system: 5 contribution
  tiers (Calibration Records highest; Translations; Skill improvements; Examples; Issues),
  CONTRIBUTORS.md format, step-by-step first contribution guide, Founding Calibrator
  recognition for first 10 external contributors, sport-specific calibration priorities
- `community/calibration-data/CONTRIBUTING.md` — Updated: 40→70 records, recalibration link added
- Calibration drive: 10 new records (total 80 across 19 sports)
  NEW SPORTS: handball (first!), kabaddi (first!), nascar (first!) — 19th sport
  RECALIBRATION VALIDATED: derby draw premium update immediately validated vs Man City 1-1 Man Utd
  BREAKING NEWS validated: GK change at T-1h → MODIFY protocol → correct direction change
  Direction accuracy: 77/80 (96%) — highest in library history

### ✅ v3.24 — Compressed refresh, RWA Phase 5 expansion, DE/JA i18n, recalibration-v4, 90 calibration records
- `compressed/README.md` — 41 → 45 summaries: added purpose-and-context (~280t), agent-goal-framework
  (~200t), modifier-recalibration (~220t), ultra-compressed agent init (~120t). All v3.22+ major
  additions now have compressed forms.
- `fan-token/rwa-sportfi-intelligence/` — 361 → 605 lines: Phase 5 lifecycle activation signals
  (entry conditions, 5 progression stages 5a-5e, RSF delta per stage), staking yield intelligence
  (3 types: pure/fee/revenue staking), tokenised media rights practical intelligence (CDI 14 days on
  announcement), player performance bonds (3 types A/B/C), Sports DAO governance intelligence
  (treasury signals, governance mercenary risk), revised RSF formula with Phase 5 tiers (0.00 → LTUI
  baseline through 0.80-1.00 → LTUI +35-50), SportFi Kit connectivity update.
- `i18n/de/sports/football/sport-domain-football.md` — New: Bundesliga context (Bayern, BVB, Leverkusen
  profiles), DFB-Pokal/UCL signals, Der Klassiker ×1.65, Revierderby ×1.60, German language agent prompts.
- `i18n/ja/sports/football/sport-domain-football.md` — New: J-League context (浦和レッズ, 鹿島アントラーズ),
  ACL signal weights, 侍ジャパン NCSI, J-League calendar (Feb-Dec unique), Japanese agent prompts.
- `i18n/ja/sports/baseball/sport-domain-baseball.md` — New: NPB context (12 clubs), 日本シリーズ ×1.80,
  大谷翔平 ATM 0.85+, WBC ×1.75, Japanese baseball agent prompts.
- `core/modifier-recalibration-v4.md` — Preliminary 90-record analysis: athlete_modifier 9/9 (100%)
  confirmed stable; 2 new wrong-direction records analysed: UCL Leg 1 draw reinforces recal-v3
  two-legged protocol; BVB vs Leverkusen draw generates NEW high_stakes_symmetry flag (when both
  teams share equivalent high stakes + quality_differential < 0.08 → DRAW_LIKELY). 6 modifiers
  confirmed stable with zero wrong-direction records across all their records.
- Calibration drive: 10 new records (total 90 across 19 sports)
  Direction accuracy: 85/90 (94%). 5 wrong-direction records total — all draws in European football.
  Pattern now fully documented: draw under-prediction in tactical European contexts.
  athlete_modifier now at 9/50 records (18% of threshold) — target 15 for preliminary recalibration.

### ✅ v3.25 — Recalibration-v5, compressed refresh, Arabic Gulf i18n, Pattern 7 cross-sport, 100 calibration records
- `compressed/README.md` — 45 → 47 summaries: added modifier-recalibration protocols
  (~160t, covers all 4 draw protocols) and agent-goal-framework (~170t).
- `i18n/ar/sports/football/sport-domain-football-gulf.md` — New 121 lines:
  Saudi Pro League (Hilal, Al-Nassr, Ronaldo ATM 0.95+, Benzema), ACL Elite signal weights,
  Saudi Clásico (Hilal × Nassr) ×1.75, Gulf crypto regulatory context (ADGM/VARA UAE),
  WC2030 qualifier context, Arabic language agent prompts for Gulf market.
- `examples/agentic-workflows/cross-sport-signal-monitor.md` — Pattern 7 (350+ lines):
  CrossSportSignalMonitor Python class, SportSignalProfile with total_signal_strength(),
  ConvergenceDetector with 4 patterns (MACRO_BULL_MULTI_SIGNAL, SAME_WINDOW_MULTI_SPORT,
  NCSI_AMPLIFICATION, COUNTER_CYCLE_OPPORTUNITY). Full TypeScript coordination integration.
  Feeds Portfolio Monitor (Pattern 1), Pre-Match Chain (Pattern 2), Signal Bus.
- `core/modifier-recalibration-v5.md` — 15-record athlete_modifier preliminary:
  13/15 correct (87%), CONFIRMED STABLE (no change to 0.55-1.25 range). Cross-sport
  breakdown: basketball/MMA/NHL/rugby all 100%; football 75% (explained by draw protocols).
  100-record milestone analysis: 95/100 correct (95%); all 5 wrong = European football draws;
  zero wrong-direction records in any other sport or prediction type.
  8 modifiers confirmed with zero wrong records: qualifying_delta, india_pakistan, morning_skate,
  dew_factor, taper, raider_primacy, goalkeeper_save_rate, superspeedway_specialist.
- Calibration drive: 11 new records (total 100 across 19 sports)
  athlete_modifier reached 15-record preliminary threshold (triggers recalibration-v5)
  100-record milestone achieved — first library to empirically validate sports signal modifiers
  at this scale across this many sports.
  Direction accuracy: 95/100 (95%).

### ✅ v3.26 — Release preparation: data connectors, user navigation, community activation, Pattern 8, 110 records
- `platform/data-connector-templates.md` — 3 production-ready connectors:
  (1) football-data.org lineup fetcher: FootballLineupConnector, check_lineup_for_sportmind(),
  competition IDs for all 6 major European leagues + UCL, startup sequence integrating all 3;
  (2) KAYEN fan token market: FanTokenMarketConnector, TVL tier classification (DEEP/MODERATE/THIN/MICRO),
  spread flag, check_liquidity_gate(), portfolio snapshot; (3) CoinGecko macro state:
  MacroStateConnector, get_macro_modifier() with phase mapping (BULL→×1.15 through EXTREME_BEAR→×0.50),
  stale check (Tier 3: 4h), cached fallback, sportmind_startup_check() complete sequence.
  Complete agent_with_connectors.py showing all 3 integrated in correct loading order.
- `WHO-USES-THIS.md` — User-type navigation: 6 user types (developer/agent builder/analyst/
  researcher/contributor/just curious) each mapped to exactly the files they need, nothing more.
  60-second starting point document. Quick reference table. 5-minute LLM quickstart with zero setup.
- `FIRST-RECORD-CHALLENGE.md` — Community activation: step-by-step first contribution guide
  (zero coding required), what wrong-direction records do (they improve the library),
  Founding Calibrator recognition for first 10 external contributors, most-wanted record types
  table, all 3 submission methods (GitHub PR / email / GitHub Issue).
- `README.md` — Upgraded for release: WHO-USES-THIS.md as first navigation link, deployment
  readiness statement, 8 zero-wrong-record modifiers listed, calibration foundation highlighted,
  community contribution call to action prominent, concise and clear for external developers.
- `examples/agentic-workflows/governance-monitoring-agent.md` — Pattern 8 (350+ lines):
  GovernanceProposal dataclass, DecisionWeightClassifier (theatre/structural/commercial/operational
  keyword detection), GovernanceBriefGenerator (LTUI YES/NO projections, quorum risk alert),
  GovernanceMonitorAgent (2h cycle, Level 1 mandatory, never votes autonomously), safety principles
  for governance agents (per-vote authorisation only; legal attestation context).
- `i18n/hi/sports/cricket/sport-domain-cricket-ipl.md` — 122 lines: IPL franchise profiles
  (MI, CSK, RCB, KKR profiles with ATM), dew factor in Hindi (full rules), भारत-पाकिस्तान × 2.00
  rule in Hindi, IPL playoff signal weights, Hindi language agent prompts for Indian market.
- Calibration drive: 10 new records (total 110 across 19 sports)
  LANDMARK: First governance calibration record (PSG structural vote — Decision_Weight 0.90 validated)
  Maple Leafs Conference Final G7 win — 60-year drought narrative at maximum intensity
  athlete_modifier now 16/50 records (32% of threshold)
  F1 Sprint race × 0.40 weight validated (first sprint record)
  Direction accuracy: 105/110 (95%). Library stable across all dimensions.

### ✅ v3.27 — Recalibration-v6, WHO-WE-ARE rewrite, compressed refresh, AR cricket PSL, 120 records
- `WHO-WE-ARE.md` — Full rewrite (was stale at v3.14): v3.26 state, 434 files, 110+ records,
  five intelligence layers summary, calibration foundation, eight zero-wrong-record modifiers,
  ecosystem map (data→SportMind→application→execution), contributing section, long-horizon vision.
- `compressed/README.md` — 47 → 50 summaries: cross-sport signal monitor (~200t, 4 patterns),
  governance monitoring agent (~180t, decision weight tiers, Level 1 mandatory), data connector
  templates (~230t, 3 connectors with API key status and tier thresholds).
- `i18n/ar/sports/cricket/sport-domain-cricket-psl.md` — 121 lines: PSL franchise profiles
  (Lahore Qalandars $LAH, Karachi Kings, Multan Sultans), Gulf cricket market (UAE 3.5M South
  Asian diaspora), NCSI PSL weights (Group 0.35 → Final 0.85), PSL dew factor (lower than IPL),
  Pakistan vs India × 2.00, Asia Cup UAE context, Arabic agent prompts.
- `core/modifier-recalibration-v6.md` — athlete_modifier 25-record second preliminary:
  21/25 correct (84%) — but 18/18 (100%) non-football, 7/7 (100%) football with protocols applied.
  Draw protocol confidence tiers formalised: TIER 1 (never override: two-legged Leg 1 +
  high_stakes_symmetry), TIER 2 (apply consistently: derby_active + post-tournament).
  Override rule: requires SMS > 80 AND quality_differential > 0.20; max 30% position.
  120-record milestone: 115/120 (95.8%), no new wrong records in records 101-120, 8 zero-wrong
  modifiers confirmed. Next threshold: 40 records → recalibration-v7.
- Calibration drive: 10 new records (total 120 across 19 sports)
  athlete_modifier reached 25-record threshold — CONFIRMED STABLE
  NHL: Maple Leafs Cup defense opener (SMS 81 — highest individual record)
  Rugby World Cup 2027: pool stage validated, neutral venue model confirmed
  Two-legged Leg 1 DRAW_LIKELY validated third time (Man City vs Barcelona)
  Direction accuracy: 115/120 (95.8%). Records 101-120 all correct direction.

### ✅ v3.28 — Final pre-release polish: GOOD_FIRST_ISSUES, compressed recalibrations, netball/rowing records, 126 records
- `GOOD_FIRST_ISSUES.md` — Full rewrite: 4 contribution levels (⭐ to ⭐⭐⭐⭐), 213 lines.
  Level 1 (no coding): calibration records with most-wanted table, stale docs fix, translation gaps.
  Level 2 (domain knowledge): 14 stub sport details with key markets and notes, athlete skill gaps,
  5-record cluster path to Senior Calibrator status.
  Level 3 (technical): TypeScript starter pack, validator script, netball/rowing GOOD expansion.
  Level 4 (significant): external recalibration analysis, hosted MCP endpoint.
  Issue claiming process, PR labels, quality bar explanation.
- `compressed/README.md` — 50 → 52 summaries: recalibration-v5 (~180t, 100-record milestone,
  8 zero-wrong modifiers) and recalibration-v6 (~220t, draw protocol confidence tiers, 
  TIER 1 never-override rule, 120-record perfect run).
- Calibration drive: 6 new records (total 126 across 21 sports) — CLOSES ZERO-RECORD GAPS
  Netball (3): Super Netball R7, World Cup 2027 SF, Grand Final — shooting accuracy model validated
  Rowing (3): World Cup 2 single scull, World Champs eights, Henley Grand Challenge Cup
    PB proximity, crew stability (60/40 individual/crew split), challenge format confirmed
  21 SPORTS NOW ALL CALIBRATED — no sport in the library has zero records any longer
  Direction accuracy: 121/126 (96%) — highest in library history
- `README.md` — Badge updated 100→126 records, 95→96% accuracy; v5→v6 recalibration reference
- `WHO-WE-ARE.md` — Record counts: 110→126, 19→21 sports, 5→6 recalibration reports, v3.28 version
- `FIRST-RECORD-CHALLENGE.md` — Record count updated 100→126
- `community/calibration-data/CONTRIBUTING.md` — Record count updated 70→126, 16→21 sports

### ✅ v3.29 — Community Release
- `.github/CODEOWNERS` — Repository ownership map: owner assigned as fallback for all paths,
  inline comments documenting how to delegate each area as co-maintainers are identified.
  Covers: core/platform/compressed (owner only), calibration-data (owner + future trusted
  calibrator), sport domains and athlete skills (delegation model with examples), i18n paths
  with language-specific delegation examples, CI/CD and scripts, root documentation, community
  infrastructure. Commented examples for all delegation paths ready to uncomment.
- `CONTRIBUTING.md` — "Becoming a co-maintainer" section added: no application process,
  path via demonstrated contribution (3+ merged PRs OR 10+ calibration records OR 5+ translations),
  what co-maintainers do (review/merge in their domain), what they do not need to do (review
  everything), domain areas that will need co-maintainers first (calibration, football, cricket,
  i18n), fastest path (calibration records).
- `CODE_OF_CONDUCT.md` — Project conduct standards: technical honesty principle (calibration
  records must be pre-match), analytical neutrality, evidenced feedback, enforcement process.
  Written specifically for SportMind's technical community rather than a generic template.
- `CITATION.cff` — Machine-readable citation format for researchers and academic users.
  CFF 1.2.0 standard. Includes preferred-citation block with title, version, license, abstract.
  Enables automatic citation generation by GitHub and academic tools.
- `RELEASE.md` — Community release announcement: what is in the release, why calibration
  records matter, what is not included (live data, full recalibration, hosted infrastructure),
  getting started paths, Founding Calibrator recognition, acknowledgements.
- `.github/ISSUE_TEMPLATE/calibration-record.md` — Already existed; confirmed complete.
- `community/leaderboard.md` — Updated from stale v3.2 content: v3.28 state, 126 records,
  21 sports, founding team position, clear call to be first external contributor.
- `llms.txt` — Fixed stale example paths (standalone/ → starter-pack/), stale record counts.
- Final consistency sweep: all version references, record counts, and file counts
  current across all community-facing documents.

### ✅ v3.31 — MCP Server deployment package
MCP-SERVER.md deployment guide, requirements.txt, Dockerfile, vercel.json,
validate-mcp.yml CI workflow. Upgraded HTTP/SSE transport with /health endpoint.
25 sports supported. Zero-maintenance deployment — serves static skill files,
no live data dependency, no API keys required.

### ✅ v3.30 — Chiliz 2030 intelligence: gamified tokenomics, US regulatory, omni-chain, RWA staging
- `fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md` — New skill
  (280+ lines): Chiliz 2030 performance-linked tokenomics model. Detection (KAYEN API gamified flag,
  Socios.com indicator). WIN modifier formula (1.00 + burn_rate×2.5), LOSS modifier (1.00 − mint_rate×2.0).
  Season supply position tracking (net burned/minted → scarcity/dilution tiers). Prediction market
  interaction flag. Unusual pre-match volume flag (>3× in 4h window). Complete pre-match workflow.
  Output schema extension. Rollout context (Q2 2026, selected tokens first). Championship run
  scarcity modifier (10+ wins → 3% burn accumulation → ×1.08 floor boost).
- `macro/macro-regulatory-sportfi.md` — New skill (220+ lines): Four-jurisdiction framework.
  EU MiCA (fully active Jan 2025): utility token classification, whitepaper requirements, CASP
  licensing. US SEC/CFTC joint guidance (landmark 2026): fan tokens classified as UTILITY DIGITAL
  COMMODITIES under CFTC — the regulatory unlock for US market re-entry. US market intelligence:
  first US partnership Q1 2026, Tier 1 macro event, 45-60 day CDI window. Brazil: first
  revenue-sharing RWA live on Chiliz Chain (Phase 5b confirmed real). Regulatory discount
  framework (0.00 to ABSTAIN). Quarterly monitoring rule and sources.
- `fan-token/rwa-sportfi-intelligence/rwa-sportfi-intelligence.md` — Updated 605 → 729 lines:
  Three-stage evolution model from Chiliz 2030 Manifesto (Stage 1 utility 2019-2025 → Stage 2
  dynamic tokenomics 2026 → Stage 3 RWA 2027-2030). Stage stacking principle (stages stack,
  not replace). Omni-chain liquidity intelligence (LayerZero, aggregate TVL, arbitrage check,
  omni-chain liquidity tier bonus). PEPPER governance token context. Updated RSF formula with
  stage bonuses (+0.08 Stage 2, +0.12 Stage 2+omnichain, +0.20 Stage 3). Updated LTUI ranges.
- `platform/data-connector-templates.md` — Updated KAYEN section: omni-chain awareness note
  (Q1 2026 LayerZero expansion), PEPPER governance token explanation, gamified tokenomics
  detection note, cross_chain_tvl field reference.
- `compressed/README.md` — 52 → 54 summaries: gamified tokenomics (~200t) and regulatory
  SportFi (~210t) compressed forms added.

### v3.31 and beyond — Community evolution
- External community calibration records begin arriving
- Modifier recalibration-v7 (athlete_modifier at 40 records)
- First external skill contributions (stub sport expansions)
- Website and documentation site (separate development track)
- v4.0 milestone: three modifiers at full 50-record threshold,
  first external recalibration report, library maintained by community

---

## License

MIT — free to use, modify, and redistribute for any purpose.

Attribution appreciated but not required.

---

## Community

- GitHub Discussions — questions, ideas, sport-specific debate
- Issues — bug reports, skill inaccuracies, missing sports
- PRs — new skills, improvements, translations

---

*SportMind is an independent open-source project. It is not affiliated with Chiliz,
Socios, Fan Token Intel, or any sports data provider, though it is designed to
complement them.*
