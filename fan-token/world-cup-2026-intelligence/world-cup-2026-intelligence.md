---
name: world-cup-2026-intelligence
description: >
  FIFA World Cup 2026 fan token intelligence module. Use whenever an agent needs to
  reason about World Cup 2026 signal windows, national team token performance, club
  token spillover (NCSI), the 48-team format implications, US market unlock thesis,
  or any fan token decision during the June–July 2026 tournament period. Load alongside
  fan-token/football-token-intelligence/ and market/world-cup-2026.md. This is the
  deepest World Cup fan token skill in SportMind — provides tournament-phase signal
  architecture, NCSI amplification tables, host nation commercial signals, and the
  complete token calendar from draw to final.
---

# World Cup 2026 Fan Token Intelligence

**FIFA World Cup 2026 · USA / Canada / Mexico · 11 June – 19 July 2026**

The largest single commercial event in fan token history. 48 teams, 104 matches,
three host nations, and the first World Cup held in a country where the regulatory
environment for digital assets has been actively clarifying. Every Tier 1 football
fan token is affected. Eight national tokens are live for the first time at a
World Cup of this scale.

This skill is the fan token commercial intelligence layer for the tournament.
See `market/world-cup-2026.md` for tournament overview and format detail.
See `fan-token/football-token-intelligence/` for the underlying NCSI and ATM framework.

---

## Why World Cup 2026 is categorically different

```
PREVIOUS WORLD CUPS (Qatar 2022):
  32 teams · 64 matches · ~28 days · Middle East timezone (poor for Europe/Americas)
  Fan tokens: nascent ecosystem, 3 national tokens live
  Total viewer unique reach: ~5B

WORLD CUP 2026:
  48 teams · 104 matches · 39 days
  Three host nations (USA/Canada/Mexico) — Americas primetime
  Fan tokens: mature ecosystem, 8+ national tokens, 40+ club tokens active

  THE STRUCTURAL DIFFERENCES THAT CHANGE EVERYTHING:

  1. US TIMEZONE ADVANTAGE
     Group stage matches in American primetime reach:
     → 75M+ Latino football fans in USA (largest untapped token market)
     → Full Latin American market in afternoon hours
     → European market in evening (UCL slot equivalent)
     Combined reach window no previous World Cup has had

  2. 48-TEAM FORMAT — MORE SIGNAL WINDOWS
     32-team World Cup: each token has average 3-4 match exposures
     48-team World Cup: each token has average 4-5 match exposures
     More matches = more buy pressure windows = longer sustained HAS elevation

  3. HOST NATION COMMERCIAL SIGNAL
     USA, Canada, Mexico all have active football cultures + digital asset adoption
     US: ~35% crypto adoption rate; tournament as regulatory catalyst moment
     Mexico: Chivas ($CHVS) and Santos ($SAN) tokens — domestic club excitement

  4. NATIONAL TOKEN ECOSYSTEM MATURITY
     2022: $ARG was the primary national token
     2026: $ARG + multiple new national tokens expected in pre-tournament period
     National token holders are more globally distributed than club tokens
```

---

## Tournament signal calendar

```
PRE-TOURNAMENT WINDOWS:

T-180 days (December 2025 — Tournament Draw):
  SIGNAL TYPE: Draw anticipation + group reveal
  Impact: National token spike on draw day (+8–18%)
  Club tokens: spike for clubs with multiple players in same group
  Duration: 24–48h elevated HAS, then rapid decay
  Agent action: SHORT position window (24h max); draw-day signal only

T-90 days (March 2026 — Final Qualifying Rounds):
  SIGNAL TYPE: Qualification confirmation / elimination
  Impact: Confirming qualification: +5–12% national token
  Failing to qualify: -8–20% (e.g. Italy 2022-equivalent miss)
  Club tokens: moderate spillover from player qualifying campaigns

T-30 days (May 2026 — Squad Announcement Window):
  SIGNAL TYPE: Squad selection confirmation
  Impact: Key ATM players named in squad: +3–7% club token
  Key ATM players omitted through injury: -4–10% club token
  Duration: 72h elevated signal window

  HIGHEST-RISK OMISSIONS FOR CLUB TOKENS:
  Any Tier 1 ATM player (score >= 0.35) confirmed injured before tournament
  = Immediate club token DSM-equivalent signal (not disciplinary but same commercial impact)
  Apply x0.88 to club token commercial signal for duration of tournament

T-14 days (Pre-tournament warm-up matches):
  Minor signal. Do not treat as meaningful without specific context.
  Exception: injury in warm-up match = Category 1 breaking news protocol

---

GROUP STAGE WINDOWS (June 11 – July 2, 2026):

PER-MATCH SIGNAL:
  Win:  +3–8% national token; +1–3% club tokens for goal scorers
  Loss: -2–5% national token; neutral for club tokens unless star performs
  Draw: -1–3% national token (especially if elimination risk emerges)

GROUP STAGE OUTCOME TABLE:
  +++ (3 wins, goals by ATM players):       FTIS 95–100
  ++  (2W/1D, advancing comfortably):       FTIS 80–90
  +   (Advance on final matchday):          FTIS 65–75
  ~   (Advance as best third-place):        FTIS 55–65
  -   (Eliminated, competitive):            FTIS 30–45
  --- (Eliminated as heavy favourite):      FTIS 10–25

---

KNOCKOUT PHASE WINDOWS (July 4–19, 2026):

ROUND OF 32 (July 4–7):
  Signal magnitude: x1.4 vs group stage match
  Exit: -8–15% national token in 24h
  Advance: +5–10% national token

ROUND OF 16 (July 10–13):
  Signal magnitude: x1.6 vs group stage
  Exit: -10–20%
  Advance: +8–14%; narrative momentum compounds

QUARTER-FINALS (July 15–16):
  Signal magnitude: x1.9 vs group stage
  Exit: -12–25% national token
  Advance: +10–18%; club token NCSI at maximum

SEMI-FINALS (July 18):
  Signal magnitude: x2.2 vs group stage
  Finalist signal: +15–25% national token
  Losing semi: -8–15% (reaching semi is still strongly positive overall)

FINAL (July 19 — MetLife Stadium, New Jersey):
  WORLD CUP WINNER:
    National token: +25–60%
    Club tokens (star performer — Golden Boot/Ball): +12–22%
    Club tokens (key contributor 3+ G/A): +8–15%
    Club tokens (squad player): +3–7%

  RUNNER-UP:
    National token: +5–12%
    Normalisation: 7–10 days post-tournament
```

---

**Academic grounding: Saggu, Ante & Demir (2024), *Research in International Business and Finance* — documented anticipatory price gains in fan tokens before FIFA World Cup fixtures; event-driven losses post-elimination exceed advancement gains (asymmetry confirmed). This is the empirical basis for the pre-tournament amplifier and CALENDAR_COLLAPSE mechanics modelled below.**

## NCSI amplification at World Cup 2026

The National-Club Spillover Index operates at 3–4x normal strength during
a World Cup. This is the most important modifier in this skill.

```
NCSI WORLD CUP AMPLIFIER:
  Standard NCSI (domestic international break): x1.00
  Major tournament (Euros/Copa América):        x2.00–2.50
  World Cup (standard):                         x3.00
  World Cup 2026 (US hosted, expanded format):  x3.50–4.00

WHY HIGHER IN 2026:
  Larger audience → more new wallet creation
  US market exposure → new geographic holder demographics
  48-team format → longer duration → more sustained NCSI exposure
  Regulatory clarity signal → institutional participants more active

NCSI BY PLAYER TIER:

TIER 1 (ATM >= 0.35 — maximum club token impact):
  Club token impact per strong performance: +1.5–3.5%
  Tournament winner + Golden Boot: cumulative club token +18–28%

TIER 2 (ATM 0.20–0.34):
  Club token impact per match: +0.7–1.5%
  Tournament winner contribution: +6–12% club token

TIER 3 (ATM < 0.20):
  Club token impact per match: +0.2–0.5%
  Meaningful only if player wins Golden Boot against expectation

CLUB TOKEN VULNERABILITY:
  Clubs with zero World Cup starters = monitor for Phase 4 drift
  World Cup period = 6 weeks of no club football
  RISK: HAS may decline if no active ATM players in tournament
```

---

## Host nation commercial signals

```
USA HOST SIGNAL:
  First World Cup in the USA in the fan token era.

  US FAN TOKEN ADOPTION THESIS:
    New wallet creation rate will exceed any previous tournament
    Geographic holder diversification of all national tokens
    US media amplifies NCSI for tokens with US fanbase

  MONITORING SIGNAL:
    Track new US-located wallet creation via platform/chiliz-chain-address-intelligence.md
    Threshold: >500 new US wallets/week = adoption signal confirmed

  TOKENS MOST EXPOSED TO US MARKET UNLOCK:
    $ARG: Argentina — massive Latino-US following
    $MENGO: Flamengo — strong Brazilian diaspora in USA
    National tokens for Mexico, Brazil, Portugal

  REGULATORY CAVEAT:
    If SEC/CFTC provide utility token clarity before tournament → full US signal
    If regulation still unclear → conservative estimate applies
    Monitor: macro/macro-geopolitical.md for regulatory status

MEXICO HOST SIGNAL:
  $CHVS (Chivas/Guadalajara) — Group stage matches at Estadio Akron
  $SAN (Santos Laguna) — Training camp city proximity signal
  Apply x1.15 to $CHVS during Mexico group stage home matches
```

---

## Token World Cup 2026 exposure map

```
HIGHEST EXPOSURE — NATIONAL TOKEN:

$ARG — Argentina National Team
  Defending World Cup champion (Qatar 2022)
  Signal ceiling: MAXIMUM — winner scenario targets +40–60%
  Signal floor: Group stage exit -15–25%
  Special 2026 signal: if this is Messi's final World Cup, narrative ×1.25
  regardless of performance — sentimental holder base protects floor

HIGHEST EXPOSURE — CLUB TOKENS:

$PSG — French national team NCSI exposure
  If France wins: +8–14% PSG token

$BAR — Spain national team NCSI exposure
  If Spain wins: +6–12% BAR token

$CITY — Multi-national squad (England/Spain/Norway/Belgium/Portugal)
  Diversified NCSI; almost guaranteed uplift from 2-3 nations advancing
  Post-tournament risk: squad fatigue, monitor August fixtures

$ACM / $INTER / $JUV — Italian club tokens
  CRITICAL: Italy qualification status must be confirmed
  If Italy fails to qualify: zero World Cup exposure
  Monitor: Italy playoff results March 2026

$CHVS / $SAN — Mexico host nation exposure
  Direct local commercial signal from host matches

WATCH LIST (potential new national token launches):
  Brazil, France, Portugal, England, Germany, Spain
  Monitor: fantokens.com new listings Q1-Q2 2026
```

---

## PATH_2 interaction with World Cup 2026

The Fan Token Play PATH_2 mechanism (supply burn on WIN, supply neutral on LOSS)
operates unchanged during the World Cup. Tournament context amplifies the commercial
significance of each burn event — but the protocol mechanics are identical to
domestic fixtures. This section defines what changes and what does not.

```
WHAT DOES NOT CHANGE (protocol mechanics):
  Pre-liquidation at T-48h: 1/400th of supply → USDT (0.25%)
  WIN result: 95% of proceeds buyback and permanent burn
  LOSS result: supply returned to pre-liquidation level (no net change)
  DRAW result: treated as LOSS for supply mechanics

WHAT CHANGES (commercial significance):
  Audience multiplier: WC2026 group stage = CQS 1.35–1.40 (vs 1.00 standard)
  NCSI amplifier: x3.5 group stage → x4.0 final (vs x1.0 standard domestic)
  Each WIN burn event at the World Cup is commercially 3.5–4x more significant
  than a domestic WIN burn

PATH_2 + WORLD CUP — CUMULATIVE SUPPLY REDUCTION MODEL:

  If a PATH_2 club has multiple ATM players at WC2026:

  Best case (all nations advance to final):
    Club plays 38 domestic matches: ~14–16 wins (40% win rate)
    Each World Cup WIN adds burn events from NATIONAL NCSI uplift to HAS
    Net: supply reduction accelerates during tournament weeks

  Expected case (ATM nations eliminated QF/SF):
    4–5 World Cup burn events per ATM-nation-token interaction
    Supply reduction on track; tournament adds 6–8 week commercial uplift

  Worst case (ATM player eliminated group stage):
    3 tournament matches only
    CALENDAR_COLLAPSE signal applies: remainder of tournament = dead period
    PATH_2 WIN frequency drops to domestic only from this point

TOURNAMENT WIN IMPACT ON SUPPLY TRAJECTORY:
  If PATH_2 club's #1 ATM player wins World Cup:
    → NCSI persists 60 days post-tournament
    → Each subsequent club WIN burn event has elevated commercial weight
    → LTUI trajectory: STRONGLY POSITIVE through to October 2026

AGENT RULE — PROTOCOL EVENTS:
  T-48h pre-liquidation during World Cup = PROTOCOL_EVENT (never bearish)
  Apply same rule as domestic: pre-liquidation is confirmation of PATH_2 active
  Do NOT treat World Cup pre-liquidations differently to domestic ones
  The burn amount (0.25%) is unchanged regardless of commercial context

MONITORING:
  Chiliscan API: same endpoints as domestic supply verification
  Timing: T+30min minimum; T+6h definitive (same as domestic)
  WC2026 NOTE: match dates are fixed — schedule the verification cycles in advance
```

---

## National team token framework

National team tokens behave differently from club tokens in four structural ways.
Understanding these differences is essential for World Cup 2026 signal quality.

```
STRUCTURAL DIFFERENCE 1 — NO DOMESTIC COMPETITION SIGNALS
  Club tokens: weekly domestic matches sustain HAS year-round
  National tokens: activated only during tournaments and qualification
  Result: national token HAS baseline = low outside tournaments
  World Cup impact: HAS goes from near-dormant to maximum in days

STRUCTURAL DIFFERENCE 2 — NO FAN TOKEN PLAY PATH_2 (currently)
  PATH_2 confirmed: $AFC (club token), not national tokens
  National tokens have no WIN-linked supply reduction mechanism as of 2026
  All supply signals for national tokens are holder-driven (buy/sell pressure)
  NOT protocol-driven
  Monitor: fantokens.com for any national token PATH_2 announcements pre-tournament

STRUCTURAL DIFFERENCE 3 — CDI DECAY CURVE IS DIFFERENT
  Club token CDI: sustained by weekly matches + squad narrative
  National token CDI: tournament-only events → sharp spike / sharp decay
  Post-group-stage elimination: CDI -30 within 72h (CALENDAR_COLLAPSE equivalent)
  Post-final elimination: CDI -15 (still positive; tournament run creates lasting narrative)

  CDI WINDOW BY STAGE REACHED:
    Group stage exit:   CDI window = 18 days (group + 3 days post)
    Round of 32 exit:   CDI window = 28 days
    Round of 16 exit:   CDI window = 35 days
    Quarter-final exit: CDI window = 40 days
    Semi-final exit:    CDI window = 46 days
    Runner-up:          CDI window = 52 days
    Tournament winner:  CDI window = 75 days

STRUCTURAL DIFFERENCE 4 — HOLDER ARCHETYPE IS PRIMARILY SPECULATOR
  National tokens attract higher Speculator share than club tokens
  Speculators enter before group stage; exit within 48h of elimination
  Governors and Loyalists: smaller share for national tokens
  Implication: CHI is lower, MRS elevated risk during sell-off periods
  Apply HIGHER fraud detection sensitivity during post-elimination windows

NATIONAL TOKEN — ENTRY AND EXIT DISCIPLINE:
  ENTRY window: T-14 days to T-2h of first group match
  EXIT warning: any elimination result → IMMEDIATE reassessment
  Hard rule: NEVER enter national token 4h either side of elimination match
  (volatility exceeds signal quality regardless of SportMind score)

$ARG SPECIAL CASE — NARRATIVE AMPLIFIER:
  Argentina is the defending champion. If this is Messi's final World Cup:
  APPLY: narrative_amplifier = 1.25 to all signal outputs
  This amplifier reflects the unique sentimental holder base that
  protects the floor regardless of performance.
  CONDITION: activate only if confirmed by credible media T-30 days before tournament
  Do NOT apply pre-emptively from current session date
```

---

## CALENDAR_COLLAPSE — tournament elimination mechanics

CALENDAR_COLLAPSE is the fan token equivalent of a relegation event during
a World Cup. When a nation is eliminated, the remaining tournament becomes
a commercial dead period for that token.

```
CALENDAR_COLLAPSE TRIGGER CONDITIONS:
  Group stage exit:            CALENDAR_COLLAPSE_CONFIRMED on final group match
  Knockout round exit:         CALENDAR_COLLAPSE_CONFIRMED within 4h of match result
  Failure to qualify (pre-tournament): CALENDAR_COLLAPSE_CONFIRMED at draw allocation

CALENDAR_COLLAPSE EFFECTS BY TOKEN TYPE:

  NATIONAL TOKEN ($ARG, national tokens):
    Immediate: HAS decay begins within 6h of elimination
    24h: Speculator exit driving sell pressure
    72h: HAS stabilises at new (lower) baseline
    CDI: reset per stage-reached table above
    LTUI: tournament run creates lasting positive (better than no tournament)
    EXCEPTION: runners-up maintain elevated signal for 10–14 days post-final

  CLUB TOKEN with eliminated ATM players:
    Immediate: NCSI uplift ends — ATM modifier returns to standard domestic level
    No CALENDAR_COLLAPSE on club token from national elimination alone
    But: if 3+ ATM players eliminated = NCSI_SILENCE flag for remainder of tournament
    Club token continues on domestic cycle; World Cup narrative ends early

  CLUB TOKEN with PATH_2 active:
    Supply mechanics UNCHANGED — PATH_2 continues on domestic schedule
    No burn is missed because of national team elimination
    But: commercial weight of each subsequent WIN burn is reduced
    (CQS returns to domestic baseline ~1.00 from WC amplified level)

CALENDAR_COLLAPSE SIGNAL CHAIN:
  1. Elimination confirmed (full-time result)
  2. Raise CALENDAR_COLLAPSE flag for national token
  3. Apply CDI reset (stage-reached table)
  4. REMOVE NCSI amplifier from club token calculations
  5. Club token reverts to standard domestic ATM model
  6. National token: WAIT 72h before next entry signal assessment

AGENT HARD RULE:
  Never maintain ENTER signal on a national token after elimination
  Never blame "temporary dip" for elimination — it is structural
  CALENDAR_COLLAPSE is permanent for this tournament
```

---

## Post-tournament supply and signal reset

```
RESET TIMELINE (starting July 20, 2026):

WEEK 1 (July 20–26):
  National tokens: HAS normalisation; Speculators completing exit
  Club tokens: World Cup fatigue assessment begins
  PATH_2 club tokens: summer transfer window opens (July 1 overlaps tournament)
  World Cup performers = transfer targets; potential ATM change incoming

WEEK 2–4 (July 27 – August 16):
  Pre-season and domestic competition restart
  Key signal: how do ATM World Cup performers return to club form?
  August fixtures: apply TIS penalty for players with minimal recovery time
  Tournament winner players: high risk of INTERNATIONAL_RETURNEE_SHORT_PREP

30 DAYS POST-TOURNAMENT:
  Winner national token: NCSI still at x1.5 (decaying from peak)
  Finalist national token: NCSI at x1.2
  Semi-finalist: NCSI at x1.1
  Earlier exits: NCSI returned to x1.0

60 DAYS POST-TOURNAMENT (mid-September 2026):
  All tournament NCSI multipliers expired
  Return to standard domestic NCSI framework
  Exception: Golden Boot / Ball winner maintains personal NCSI at x1.3 until Jan 2027

TRANSFER WINDOW INTERSECTION:
  World Cup runs June 11 – July 19
  Summer window opens July 1 (overlaps last 3 weeks of tournament)
  Expected peak: August 15–31 (deadline pressure)
  Any ATM-tier World Cup standout = elevated transfer probability
  Apply: fan-token/star-departure-intelligence.md if transfer confirmed
  Apply: core/transfer-negotiation-intelligence.md for negotiation intelligence
  ALERT: PATH_2 clubs losing ATM-tier World Cup winner = double commercial event
    (NCSI winner + LTUI star departure simultaneously)

SEASON SUPPLY RECORD:
  Close the World Cup supply record after all PATH_2 events processed
  Log: total burns during tournament window
  Log: which matches had elevated CQS (>1.30)
  This data feeds into modifier-recalibration when the 150-record milestone is reached
```

---

## Agent reasoning protocol

```
PHASE 1 — Pre-tournament preparation (now through June 10, 2026):
  □ Identify NCSI Tier 1/2 players for each held token
  □ Map squad announcement dates per nation
  □ Track qualification status (especially Italy, conditional tokens)
  □ Monitor US regulatory environment
  □ Store World Cup token exposure map in Memory MCP
  □ Set watch: squad announcement days, tournament draw

PHASE 2 — Group stage (June 11 – July 2, 2026):
  □ Check match result for each relevant nation after every match
  □ Apply NCSI amplifier (x3.5) to standard NCSI calculations
  □ Monitor new wallet creation on Chiliz Chain
  □ Flag: any nation eliminated as heavy favourite

PHASE 3 — Knockout phase (July 4–19, 2026):
  □ Apply increasing NCSI amplifiers per round
  □ Monitor on-chain concentration after each knockout round
  □ Track smart wallet positioning around semi/final matches

PHASE 4 — Post-tournament (July 20 onwards):
  □ HAS normalisation window: 7–14 days
  □ Transfer window opens July 1 — World Cup performers = transfer targets
  □ NCSI persists 60 days for tournament winner squad members
  □ Monitor squad fatigue impact on August fixtures

HARD RULES:
  Never ENTER national token within 4h of an elimination match result
  (volatility too high for reliable entry signal)

  Always check macro_modifier first
  (crypto bear market applies x0.75 regardless of sporting signal)

  Use World Cup CDI, not standard CDI:
    Group stage performance: 4 days
    Knockout advancement: 8 days
    Winner: 45 days
```

---

## Pre-tournament protocol

**The signal window is open from T-30 days (May 12, 2026).**

The 53-day pre-tournament window requires a different operating mode from
tournament match-day signals. Squad announcements, injury news, NCSI awakening
for club tokens, national token activation, and US market first-mover signals
all operate on different timing and confidence rules than live match signals.

→ **Load `world-cup-2026-pre-tournament.md` from April 2026 through June 10.**
  This file covers the full countdown protocol, daily monitoring cycle,
  squad announcement impact table, MRS elevated vigilance rules, and the
  exact transition checkpoint to tournament mode on June 11.

---

## Load order for World Cup 2026 analysis

```
1. macro/macro-crypto-market-cycles.md           → macro modifier
2. macro/macro-geopolitical.md                   → US regulatory status
3. market/world-cup-2026.md                      → tournament overview
4. fan-token/world-cup-2026-intelligence/        → this file
5. fan-token/football-token-intelligence/        → NCSI/ATM framework
6. fan-token/fan-token-pulse/                    → on-chain baseline
7. platform/chiliz-chain-address-intelligence.md → wallet intelligence
8. platform/memory-integration.md               → NCSI tracking across tournament
```

---

*SportMind v3.71 · MIT License · sportmind.dev*
*Time-sensitive: FIFA World Cup 2026 runs June 11 – July 19, 2026*
*See: market/world-cup-2026.md · fan-token/football-token-intelligence/*
*core/core-narrative-momentum.md · fan-token/transfer-window-intelligence/*
