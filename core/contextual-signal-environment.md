---
name: contextual-signal-environment
description: >
  The unified framework treating day of week, time of day, venue context,
  audience size, schedule density, and season position as a combined
  Contextual Signal Environment (CSE) that amplifies or dampens commercial
  signals. Produces a Context Quality Score (CQS: 0.60–1.40) applied as
  a multiplier to FTIS and CDI calculations. The six CSE dimensions:
  (1) Schedule slot — day + time + broadcast window value;
  (2) Venue commercial weight — capacity, occupancy, venue type;
  (3) Audience reach tier — broadcast/streaming viewership estimate;
  (4) Schedule density — match frequency effect on commercial windows;
  (5) Season position — where in the arc this match falls commercially;
  (6) Territory and timezone — active market windows at match time.
  Critical distinction: CQS affects the COMMERCIAL signal magnitude,
  not the on-pitch performance signal. A sold-out UCL final in prime
  time with 400M viewers does not make Arsenal more likely to win than
  a half-empty cup tie — but it amplifies the commercial consequence
  of every outcome event by a factor that agents must model correctly.
  Load alongside FTIS computation for any fan token analysis.
---

# Contextual Signal Environment — SportMind

**The on-pitch signal tells you what happened. The contextual signal
environment tells you how loudly the world heard it.**

A goal scored in a UCL final watched by 400 million people creates a
different fan token commercial event than the same goal in a League Cup
tie in front of 8,000 spectators. The SportMind core signal chain
(macro → competition tier → athlete → SMS) models the quality of the
on-pitch signal. The CSE framework models the commercial amplification
context in which that signal lands.

---

## The Context Quality Score (CQS)

```
CQS = weighted_average([
    schedule_slot_score       × 0.25,
    venue_commercial_weight   × 0.20,
    audience_reach_score      × 0.25,
    schedule_density_score    × 0.15,
    season_position_score     × 0.10,
    territory_window_score    × 0.05
])

CQS RANGE: 0.60 → 1.40
  1.40: Maximum context (UCL Final, primetime, sold-out, peak season)
  1.15: Strong context (UCL knockouts, prime Saturday slot, full stadium)
  1.00: Standard context (baseline — mid-table league match, afternoon)
  0.85: Reduced context (early kickoff, poor attendance, mid-season)
  0.60: Minimal context (dead rubber, pre-season, behind closed doors)

APPLICATION:
  FTIS_adjusted = FTIS_raw × CQS
  CDI_adjusted  = CDI_raw  × CQS
  HAS_baseline_adjusted = HAS_baseline × sqrt(CQS)  [square root dampens extreme swings]

IMPORTANT: CQS does NOT modify the on-pitch SMS.
  SMS models the probability of an outcome occurring.
  CQS models the commercial magnitude of that outcome when it occurs.
  Keep them strictly separate in the signal chain.
```

---

## Dimension 1 — Schedule slot score

```
FRAMEWORK: Day of week + kickoff time + broadcast window

SCORE BANDS (0.60 → 1.40):

PREMIUM SLOTS (1.20–1.40):
  Saturday 12:30pm–3pm (UK/Europe):     1.25
    → Peak domestic audience, full-day engagement, global morning window
    → Examples: Premier League Saturday lunchtime, La Liga afternoon
  Saturday evening (6pm–10pm local):    1.30
    → Prime viewing, high social activity, European + Americas overlap
  Sunday evening (5pm–9pm local):       1.25
    → Family viewing slot, high engagement depth
  Wednesday/Tuesday 8pm European:       1.35
    → UCL/EL prime window; European evening + Americas afternoon overlap
    → Global audience simultaneous: 500M+ potential for UCL
  US primetime (Sunday 4pm–9pm ET):     1.30
    → NFL window; NFL primetime games command ×1.15 (see nfl-token-intel)
  Indian primetime IPL (7:30pm IST):    1.35
    → 500M+ potential viewers; India market amplifier active

STANDARD SLOTS (0.90–1.15):
  Saturday 3pm (UK blackout period):    1.10
    → No UK TV broadcast; lower viewership but high stadium engagement
  Sunday afternoon (1pm–5pm local):     1.10
  Midweek league (7:45pm local):        1.00
  Saturday/Sunday 11am local:           0.95
  Friday evening:                       0.95
  Monday evening:                       0.90

REDUCED SLOTS (0.60–0.85):
  Saturday 12:30pm (reduced if poor competition context): 0.90
  Weekday afternoon (2pm):              0.80
  Early Saturday (10am–11am local):     0.75
  Pre-season friendly (any time):       0.65
  Reserve/youth team match:             0.60

BROADCAST SLOT AMPLIFIERS (add to base slot score):
  National exclusive TV broadcast:      +0.08
  Streaming-exclusive (Netflix/Amazon): +0.05
  Free-to-air (FTA) broadcast:          +0.10 (wider reach, lower depth)
  Pay-per-view premium event:           +0.12 (high intent, lower reach)
  No live broadcast (behind closed doors): -0.25

ANTI-STACKING: Total slot score capped at 1.40.
```

---

## Dimension 2 — Venue commercial weight

```
FRAMEWORK: Capacity + occupancy rate + venue type

CAPACITY TIERS:

  TIER A — Major venue (>60,000 capacity):
    Full capacity (>90% occupancy):      1.35
    Near-full (75–90%):                  1.20
    Half-full (50–75%):                  1.00
    Low attendance (<50%):               0.75
    Examples: Camp Nou, Wembley, Melbourne Cricket Ground, AT&T Stadium

  TIER B — Large venue (35,000–60,000):
    Full capacity (>90%):                1.25
    Near-full (75–90%):                  1.15
    Half-full (50–75%):                  0.95
    Low attendance (<50%):               0.70
    Examples: Emirates, Old Trafford, Madison Square Garden

  TIER C — Mid-size (15,000–35,000):
    Full:                                1.10
    Near-full:                           1.05
    Half-full:                           0.90
    Low:                                 0.65

  TIER D — Small (<15,000):
    Full:                                0.90
    Any:                                 0.70–0.85
    Examples: many lower-division grounds, small arena events

  SPECIAL VENUE MODIFIERS:
    Neutral venue (UCL Final, Super Bowl): +0.10
      → Neutral venue attracts neutral fans; broader audience composition
    Behind closed doors (COVID legacy, punishment):  override to 0.60
      → No crowd signal; social/broadcast only
    Home ground for mega-club (Anfield, San Siro atmosphere):  +0.05
      → Documented atmosphere premium on broadcast engagement

OCCUPANCY DETECTION:
  Agent rule: Use official announced attendance when available (T-1h).
  If unavailable: estimate from competition tier + opponent quality.
  UCL knockout sellout rate (top-8 clubs): 97%+ → assume full.
  Mid-table domestic cup: estimate 55–65% unless announced otherwise.
```

---

## Dimension 3 — Audience reach score

```
FRAMEWORK: Broadcast/streaming audience tier estimate

The audience reach score is the most commercially significant CSE dimension
because it determines how many potential new token holders can be reached
by a commercial outcome event.

GLOBAL TIER 1 (score: 1.40):
  Estimated viewership: 300M+
  Examples: UCL Final, World Cup Final, World Cup Semi-Final, Olympics Opening
  Token impact: Maximum CDI amplification; global new wallet acquisition possible

GLOBAL TIER 2 (score: 1.25):
  Estimated viewership: 100–300M
  Examples: UCL Quarter-Final/Semi-Final, World Cup Group, IPL evening India
  Token impact: High CDI; significant new holder acquisition in primary markets

MAJOR REGIONAL (score: 1.10):
  Estimated viewership: 20–100M
  Examples: Premier League Saturday prime, NFL Sunday, NBA Finals game
  Token impact: Strong CDI in primary market; limited global new acquisition

DOMESTIC PRIMARY (score: 1.00):
  Estimated viewership: 3–20M
  Examples: Standard Bundesliga, domestic cup semi-finals, domestic league prime
  Token impact: Standard CDI; primarily existing holders engaged

DOMESTIC SECONDARY (score: 0.85):
  Estimated viewership: 0.5–3M
  Examples: Lower-table fixtures, minor domestic cups
  Token impact: Below-average CDI

NICHE / EMERGING (score: 0.70):
  Estimated viewership: <500,000
  Examples: Conference League group stage, lower-division playoff
  Token impact: Minimal CDI amplification

AGENT RULE — AUDIENCE ESTIMATION:
  When broadcast figures are unavailable, use competition tier as proxy:
    UCL Final / World Cup Final:     → Global Tier 1
    UCL knockout / World Cup group:  → Global Tier 2
    Top-5 league (PL/La Liga/etc.):  → Major Regional (with broadcast slot)
    Standard domestic:               → Domestic Primary
  Note: India Rule (×1.40) applies when Indian audience is the primary market —
  this subsumes the audience reach score for IPL/India cricket events.
```

---

## Dimension 4 — Schedule density score

```
FRAMEWORK: Commercial window concentration and audience fatigue

This dimension is the inverse of fixture congestion — where congestion
models the PERFORMANCE impact on players, schedule density models the
COMMERCIAL impact on audience engagement and fan token behaviour.

CONCENTRATED WINDOWS (high commercial value):
  Unique midweek slot (UCL/EL only match that week):  1.20
    → Audience attention undivided; full social window
  Weekend with single high-profile match:             1.15
  International break window (no club fixtures):      1.10
    → Attention concentrated; international token amplification

STANDARD DENSITY (baseline):
  Standard fixture week (2–3 top matches in window):  1.00
  FA Cup / domestic cup alongside league:             0.97

SATURATED WINDOWS (reduced commercial value):
  Gameweek with 8+ Premier League fixtures:           0.90
    → Audience attention split; social volume diluted
  Christmas fixture pile-up (daily PL matches):       0.85
    → Market saturation; each individual match gets less attention
  World Cup group stage (4+ matches/day):             0.80
    → Even for major teams; fan exhaustion effect after day 5+
  Pre-season friendly period (multiple games daily):  0.65

FAN TOKEN SPECIFIC RULE:
  Multiple PATH_2 clubs playing simultaneously:
    Each club's token gets REDUCED HAS spike (attention split)
    Two clubs same night: each gets ×0.85 of normal solo spike
    Three clubs same night: each gets ×0.75
    Example: PSG + Arsenal + Bayern all playing Tuesday UCL →
    each $PSG, $AFC, $BAY token spike is dampened by the others
```

---

## Dimension 5 — Season position score

```
FRAMEWORK: Where in the season arc does this match fall commercially?

PEAK COMMERCIAL WINDOWS (1.20–1.40):
  Title decider (mathematically decisive match):      1.40
    → Highest single-match commercial event in domestic calendar
  Final gameweek with title/relegation still live:    1.35
  UCL/major tournament knockout (must-win):           1.25
  Final 5 league games with stakes alive:             1.20

ELEVATED COMMERCIAL WINDOWS (1.05–1.20):
  Season opener (new season narrative):               1.15
    → New signings, fresh optimism, highest pre-match sentiment
  Derby in top-4 run (both clubs competing):          1.10
  International window (nation's season peaks):       1.10
  Transfer deadline day adjacent (final 48h):         1.08
  Post-trophying season (defending champions):        1.05

STANDARD WINDOWS (0.90–1.05):
  Mid-season with live stakes (top-4 race):           1.00
  Standard competitive fixture:                       0.95
  Early season form-building:                         0.92

DEPRESSED COMMERCIAL WINDOWS (0.60–0.90):
  Post-elimination dead rubber:                       0.70
    → Club already relegated OR already won title with no threat
  Final gameweek with nothing at stake:               0.72
  Post-cup exit, no European spot in reach:           0.80
  Pre-season:                                         0.65
  Behind-closed-doors (any season position):          0.60

SEASON ARC AGENT RULES:
  Do not assume a mid-table club in December has nothing at stake.
  Check: are they within 6 points of European spot? → Apply ×1.05 minimum.
  Check: are they within 3 points of relegation zone? → Apply ×1.10 (fear amplifies engagement).
  Relegation battles generate HIGHER token engagement than comfortable mid-table.
```

---

## Dimension 6 — Territory and timezone window

```
FRAMEWORK: Which active market windows are open at match time?

Fan tokens are global assets. When a match takes place, the commercial
signal strength depends on which major crypto + sports markets are awake
and active to respond to outcome events.

TERRITORY WINDOWS:

  EUROPEAN EVENING (6pm–11pm CET):                   score: 1.20
    Europe (crypto-active, large fan token market)
    UK, Germany, Spain, France, Italy all active
    Americas coming online (EST afternoon)
    → Most valuable territory window for European club tokens

  AMERICAS AFTERNOON (12pm–6pm EST):                 score: 1.10
    US/Canada active (growing fan token market)
    European morning (some overlap)
    Latin America active (large football following)

  ASIA-PACIFIC EVENING (6pm–11pm SGT/JST):           score: 1.10
    Large crypto market (South Korea, Japan, Singapore)
    Important for cricket/IPL (India evening ≈ this window)
    Chelsea, Arsenal, Liverpool have significant Asian holder bases

  EUROPEAN MORNING (7am–12pm CET):                   score: 0.85
    Early UK kickoffs; limited active trading audience

  AMERICAS MORNING (6am–12pm EST):                   score: 0.75
    Limited active audience for European events
    NFL morning games see reduced international signal

  DEAD ZONE (3am–6am any primary market):            score: 0.70
    Some Asian/Pacific sports events fall here for European tokens

OVERLAP PREMIUM:
  European evening + Americas afternoon overlap (7–10pm CET):  +0.10
    → Both major markets active simultaneously — highest engagement window
    → UCL Wednesday 8pm (9pm in some EU markets) hits this window exactly

INDIA EXCEPTION:
  When India is the primary market (IPL, India cricket):
    India evening (7:30pm IST) = IST-adjusted window score
    Apply India Rule (×1.40) as override — subsumes territory dimension
```

---

## CQS worked examples

```
EXAMPLE 1 — UCL QUARTER-FINAL (Arsenal vs PSG, Wednesday 8pm, Emirates, full):
  Schedule slot:      Wednesday 8pm European prime     → 1.35
  Venue:              Tier B, >90% occupancy           → 1.25
  Audience reach:     Global Tier 2 (~150M viewers)    → 1.25
  Schedule density:   Midweek UCL only slot            → 1.20
  Season position:    UCL knockout — must-win stakes   → 1.25
  Territory window:   EU evening + US afternoon overlap → 1.30

  CQS = (1.35×0.25) + (1.25×0.20) + (1.25×0.25) + (1.20×0.15) + (1.25×0.10) + (1.30×0.05)
      = 0.338 + 0.250 + 0.313 + 0.180 + 0.125 + 0.065
      = CQS 1.27

  FTIS_raw = 82 → FTIS_adjusted = 82 × 1.27 = 104 (capped at 100 → maximum signal)

EXAMPLE 2 — LEAGUE CUP TIE (Arsenal vs Coventry, Tuesday 7:45pm, 70% attendance):
  Schedule slot:      Midweek league slot              → 1.00
  Venue:              Tier B, 70% occupancy            → 1.00
  Audience reach:     Domestic secondary (~1M viewers)  → 0.85
  Schedule density:   Alongside standard fixtures      → 0.97
  Season position:    Cup tie, Arsenal rotating squad  → 0.85
  Territory window:   EU evening (domestic only)       → 1.00

  CQS = (1.00×0.25) + (1.00×0.20) + (0.85×0.25) + (0.97×0.15) + (0.85×0.10) + (1.00×0.05)
      = 0.250 + 0.200 + 0.213 + 0.146 + 0.085 + 0.050
      = CQS 0.94

  FTIS_raw = 62 → FTIS_adjusted = 62 × 0.94 = 58

EXAMPLE 3 — DEAD RUBBER (Arsenal vs Brentford, final gameweek, already relegated opponent):
  CQS ≈ 0.73 (low slot, depleted attendance, no stakes, saturated final weekend)
  FTIS_raw = 45 → FTIS_adjusted = 45 × 0.73 = 33
  Agent action: ABSTAIN (insufficient commercial signal)
```

---

## Integration with SportMind signal chain

```
LOADING ORDER:
  Load CQS AFTER competition tier classification and BEFORE FTIS application.
  The competition tier determines base FTIS.
  CQS amplifies or dampens that base.

  Standard chain with CQS:
  1. Macro gate (macro_modifier)
  2. Competition tier (base FTIS)
  3. CQS calculation (contextual amplifier)
  4. FTIS_adjusted = FTIS_raw × CQS
  5. Athlete modifier (on-pitch signal)
  6. Confidence output

WHAT CQS DOES NOT MODIFY:
  → SMS score (on-pitch signal probability)
  → Athlete modifier values
  → Macro modifier
  → FTP PATH_2 burn mechanics (supply changes are fixed per result)

WHAT CQS DOES MODIFY:
  → FTIS (fan token intelligence signal — how commercially significant is this event)
  → CDI (commercial duration index — how long does the engagement arc last)
  → HAS spike baseline (how large is the initial holder activity surge)
  → New wallet acquisition rate (higher CQS = more new holders enter on outcome)

FTP PATH_2 NOTE:
  PATH_2 supply reduction is fixed per result (0.24% per WIN, supply-neutral per LOSS).
  CQS does not change the supply mechanics.
  CQS does change how many holders are watching and responding to that supply change.
  A WIN burn in a CQS 1.27 context generates more secondary market activity
  than a WIN burn in a CQS 0.94 context — same burn, different commercial echo.
```

---

## CQS output schema

```json
{
  "cqs_brief": {
    "match":          "Arsenal vs PSG",
    "assessed_at":    "2026-04-14T00:00:00Z"
  },

  "cqs_score":    1.27,
  "cqs_label":    "HIGH CONTEXT",

  "dimensions": {
    "schedule_slot":        1.35,
    "venue_weight":         1.25,
    "audience_reach":       1.25,
    "schedule_density":     1.20,
    "season_position":      1.25,
    "territory_window":     1.30
  },

  "adjustments": {
    "ftis_raw":      82,
    "ftis_adjusted": 100,
    "cdi_multiplier": 1.27,
    "has_adjustment": 1.13
  },

  "plain_english": "This is about as commercially significant a match as a fan token can be associated with. Wednesday UCL prime time, sold-out Emirates, global audience, peak knockout stakes, and both European and American markets active simultaneously. Every outcome event tonight will hit harder and last longer than a standard fixture.",

  "sportmind_version": "3.64.0"
}
```

---

*SportMind v3.64 · MIT License · sportmind.dev*
*See also: core/core-fixture-congestion.md (performance impact of schedule density)*
*market/broadcaster-media-intelligence.md · fan-token/fan-sentiment-intelligence/*
*fan-token/gamified-tokenomics-intelligence/ · core/temporal-awareness.md*
*core/match-condition-snapshot.md (include CQS in condition fingerprint)*
