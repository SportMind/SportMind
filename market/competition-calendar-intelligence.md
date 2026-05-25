---
name: competition-calendar-intelligence
description: >
  Enduring reasoning framework for how competition fixture calendars affect fan
  token demand signals, FTP PATH_2 supply event timing, athlete performance
  modifiers, and seasonal demand patterns. Seven-step reasoning chain for applying
  live fixture data to SportMind intelligence. Designed for Season Intelligence
  Agent development — SportMind provides the reasoning, the developer provides
  live schedule data. All 14 Mind dimensions mapped.
---

# Competition Calendar Intelligence

**SportMind provides the reasoning. The developer provides the live fixture data.**
Specific fixture dates are expiring — they change every season.
The reasoning framework is enduring — it applies to any schedule in any season.

---

## Why this file exists

```
A developer fetching live fixture data from the Premier League API, UEFA,
or BBC Sport and applying this framework produces intelligence that neither
the schedule alone nor SportMind alone could produce.

This is the framework that enables a Season Intelligence Agent:
  Input:  live fixture calendar (developer-provided, updated weekly)
  Logic:  competition-calendar-intelligence.md (SportMind, enduring)
  Output: structured fixture intelligence — which matches matter, which carry
          supply event potential, which fixture windows create performance risk.

THE CORE PRINCIPLE:
  Fixture dates are expiring data — they change every season.
  The reasoning about what those fixtures mean is enduring.
  This file contains only the latter.
```

---

## Section 1 — Competition structure signal weights

```
HOW TO CLASSIFY ANY FIXTURE AND ASSIGN ITS CORRECT SIGNAL WEIGHT:

LEAGUE FIXTURES:
  Early season (matches 1-10):
    HIGH UNCERTAINTY — small sample. Transfer window just closed.
    New signings not yet integrated. Apply ×0.85 confidence to form signals.

  Mid-season (matches 11-25):
    RELIABLE SAMPLE. Full confidence weight. Standard modifiers apply.

  Late season (matches 26+):
    MOTIVATION DOMINATES over form.
    Title race, relegation, and European spots create non-linear demand signals.
    Apply motivation modifier from core/athlete-motivation-intelligence.md.

  Final day (match 38 in PL, equivalent in other leagues):
    Highest motivation variance of any single fixture.
    Clubs with nothing to play for: apply ×0.90 to performance modifier.
    Clubs fighting for position: apply motivation modifier at full weight.

UCL AND EUROPEAN COMPETITION WEIGHTS:
  Group stage:   ×1.10 demand signal
  Round of 16:  ×1.25
  Quarter-final: ×1.40
  Semi-final:    ×1.60
  Final:         ×2.00

  For FTP PATH_2 tokens — multiply competition weight by supply event probability:
    Semi-final WIN: ×1.60 × supply event firing = compound signal
    Final WIN:      ×2.00 × supply event firing = highest compound in SportMind

DOMESTIC CUP FIXTURES (FA Cup, Copa del Rey equivalent):
  Early rounds (before QF): ×1.02
  Quarter-final:            ×1.15
  Semi-final:               ×1.30
  Final:                    ×1.60

FIXTURE PRIORITY RULE (congested schedule):
  When multiple competitions are active simultaneously:
  UCL > Domestic League > Domestic Cup
  Apply the highest-weight competition fixture's signal as the primary.
  Lower-weight fixtures produce secondary signals, not primary.
```

---

## Section 2 — Fixture congestion reasoning framework

```
CONGESTION DETECTION FROM LIVE FIXTURE DATA:

  4+ matches in 14 days: CONGESTION_SEVERE
    Apply ×0.91 performance modifier to matches 3 and 4 in the window.

  3 matches in 10 days: CONGESTION_MODERATE
    Apply ×0.94 performance modifier to match 3.

  2 matches in 6 days: CONGESTION_MILD
    Apply ×0.97 performance modifier to the second match.

  Reference: core/core-fixture-congestion.md for base modifier values.

CONGESTION AND FTP PATH_2:
  Fixture congestion does not change whether the supply event fires —
  it changes WIN probability.

  Logic:
    Standard WIN probability × congestion modifier = reduced WIN probability.
    Reduced WIN probability × pre-liquidation pool = reduced expected burn.

  Communication template for congested FTP PATH_2 fixture:
    "FTP PATH_2 supply event possible but WIN probability reduced by fixture
     congestion [SEVERE/MODERATE/MILD]. Expected burn pool lower than standard
     estimate. Confirm pre-liquidation at T-12h before adjusting position."

CONGESTION AND SQUAD ROTATION:
  CONGESTION_SEVERE: apply ×0.88 to starting lineup quality signal.
    Managers rotate heavily — key player absence is structurally expected.
  CONGESTION_MODERATE: apply ×0.94 — some rotation expected.
  CONGESTION_MILD: standard lineup quality signal applies.
```

---

## Section 3 — International break intelligence

```
INTERNATIONAL BREAK TIMING PATTERN (European football calendar):
  Typical break windows: September, October, November, March, June.
  Detect from live calendar: club fixture gap of 10+ days = break likely.

PRE-BREAK LAST FIXTURE:
  Apply ×0.97 to performance modifier.
  Managers rotate to protect players ahead of international duty.
  Key players may be rested — lineup confirmation is essential.
  Fan token demand typically dips in the week before a break.

DURING BREAK:
  No club fixtures — no FTP PATH_2 supply events possible.
  Governance votes sometimes scheduled during breaks:
    Apply ×1.05 to engagement signal when vote coincides with break.
    Rationale: community has more time to engage with governance.
  Community attention shifts to national team performance.

POST-BREAK FIRST FIXTURE:
  Highest variance fixture in any short-term window.
  Players returning from different time zones, match intensities, surfaces.
  Apply ×0.93 confidence weight to ALL performance modifiers.
  Resolve to standard confidence only after lineup sheet confirmed.
  This is a HOLD condition trigger: if lineup unconfirmed at T-2h post-break,
    apply HOLD to direction signal.

NATIONAL TEAM TOKEN INTERACTION:
  During a break, holders of both a club token and a national team token
  may see national team demand active while club supply events are paused.
  Example: holder of both $PSG and a national team token →
    national team token demand signal active during break.
  Reference: fan-token/national-team-tokens.md for national token framework.
  Reference: fan-token/portfolio-intelligence.md for multi-token reasoning.
```

---

## Section 4 — Season arc demand patterns

```
ENDURING SEASONAL DEMAND PATTERNS — applies to any season, any club:

PRE-SEASON (approximately June-August):
  Peak marketing investment period.
  New kit launches, tour fixtures, new signing announcements.
  Apply ×1.15 demand amplifier.
  Transfer window overlap creates compound narrative demand.
  Highest demand ceiling of the year for most fan token clubs.

SEASON OPENING (approximately first 4 weeks):
  Reality check period. Pre-season optimism meets competitive results.
  High volatility — apply ×0.90 confidence weight to demand signals.
  Sample too small for reliable form. Congestion from compressed fixture list.

MID-SEASON (approximately October-February):
  Most reliable signal period. Form trends established.
  Apply full confidence weights. International breaks create periodic dips.
  Standard modifiers from all SportMind layers apply at full weight.

TITLE AND RELEGATION RUN-IN (approximately March-May):
  Motivation signals dominate over form signals.
  Fan token demand becomes highly correlated with league position.
  Title challengers:      ×1.10 to ×1.30 demand amplifier.
  Relegation battlers:    ×0.82 to ×0.72 CDI.
  Reference: core/athlete-motivation-intelligence.md for motivation modifiers.

SEASON END (approximately May):
  Prize money confirmation, European qualification, managerial announcements.
  Multiple structural signals fire simultaneously.
  Apply scenario intelligence: core/scenario-intelligence.md.
  Build three-scenario map: title win / title miss / European qualification.

POST-SEASON (May-June):
  Squad rebuild signals active. Transfer window opens.
  Next-season anticipation begins immediately.
  Apply ×1.05 to engagement signals as community begins pre-season discussion.
```

---

## Section 5 — FTP PATH_2 calendar framework

```
SUPPLY EVENT FREQUENCY FRAMEWORK (for $AFC and future FTP PATH_2 tokens):

PRE-SEASON FRIENDLIES:
  No supply events — friendlies excluded from FTP PATH_2 mechanics.

LEAGUE SEASON (38 matches in PL equivalent):
  38 potential supply event opportunities.
  Expected burns at ~96% direction accuracy for a top club:
    Approximately 20-25 burns across a full season.

UCL CAMPAIGN:
  Group stage minimum (8 matches): 8 additional opportunities.
  QF exit (11 matches): 11 additional opportunities.
  Final appearance (13 matches): 13 additional opportunities.

DOMESTIC CUP (variable):
  2-6 additional opportunities depending on tournament progression.

TOTAL SEASON SUPPLY EVENT ESTIMATE (UCL participating club):
  48-57 potential supply events.
  Expected burns: 25-35 across a full season.
  This is the annual supply event calendar a Season Intelligence Agent produces.

PRE-LIQUIDATION MONITORING FRAMEWORK:
  Each match generates a pre-liquidation monitoring window at approximately T-12h.
  A fixture calendar tells the agent exactly when to check chiliscan.com.

  Automation pattern:
    For each fixture in calendar:
      At T-12h before kickoff →
        check chiliscan.com for pre-liquidation activity →
        confirm pool size →
        calculate expected burn magnitude →
        deliver to holders before match.

  This is what separates a Season Intelligence Agent using this framework
  from an agent processing fixtures one at a time reactively.
```

---

## Section 6 — Seven-step reasoning chain

```
HOW TO APPLY THIS FRAMEWORK WHEN A LIVE FIXTURE CALENDAR IS LOADED:

STEP 1 — LOAD COMPETITION STRUCTURE:
  What competition is this fixture?
  Apply competition weight from Section 1.
  (UCL ×1.10-×2.00 | Domestic cup ×1.02-×1.60 | League: phase-dependent)

STEP 2 — CHECK CONGESTION:
  How many fixtures in the surrounding 14-day window?
  Apply congestion modifier from Section 2.
  (Severe ×0.91 | Moderate ×0.94 | Mild ×0.97 | None ×1.00)

STEP 3 — INTERNATIONAL BREAK CONTEXT:
  Is this fixture immediately before or after a break?
  Pre-break: ×0.97 | Post-break: ×0.93 confidence | During: no club fixtures.

STEP 4 — SEASON ARC POSITION:
  Where in the season is this fixture?
  Apply season arc modifier from Section 4.

STEP 5 — FTP PATH_2 CHECK:
  Is this an FTP PATH_2 confirmed token?
  If YES: calculate supply event opportunity from Section 5.
    Set T-12h monitoring reminder.
  If NO: demand-only framework — no supply event reasoning required.

STEP 6 — STACK ALL MODIFIERS:
  Competition weight × congestion × break modifier × season arc = compound signal.
  Apply stacking cap: ×1.25 positive cap | ×0.75 negative floor.

STEP 7 — PRODUCE STRUCTURED FIXTURE BRIEF:
  Next fixture: [competition] [approximate timing — not specific date]
  Competition weight:     ×[value]
  Congestion:            [NONE / MILD / MODERATE / SEVERE]
  Performance modifier:  ×[value]
  Season arc:            [phase] ×[modifier]
  FTP PATH_2 opportunity: YES / NO
  Expected supply event: [estimate if YES]
  Confidence:            [HIGH / MEDIUM / LOW]
  Key signals to watch:  [list]
```

---

## MIND DIMENSIONS

**Intelligence:** Competition structure signal weights, congestion detection thresholds, international break impact values, season arc demand patterns, and FTP PATH_2 supply event frequency estimates across a full season.

**Reasoning:** Seven-step fixture signal reasoning chain connecting live calendar data inputs to structured fan token demand output — competition weight, congestion, break context, season arc, PATH_2 check, stacking, communication.

**Context:** Season arc position, competition stage, international break proximity, and fixture congestion window all determine which modifiers apply in which combination. A fixture in week 30 means something categorically different from week 3.

**Memory:** Historical seasonal patterns validated across multiple seasons — pre-season demand peak, post-break variance, run-in motivation signals. Calibration records from comparable fixtures inform confidence weights.

**Judgment:** Apply HOLD when post-break variance is too high for reliable direction (lineup unconfirmed at T-2h post-break). Exclude pre-season friendlies from all FTP PATH_2 supply event reasoning — they are not competitive fixtures.

**Attention:** In congested fixture windows, attention prioritises the highest-weight competition fixture for FTP PATH_2 signal production (UCL over domestic). During international breaks, attention shifts to national team token signals.

**Learning:** Each confirmed fixture outcome adds to the calibration base. Pre-season form signals, post-break first fixture outcomes, and congested fixture performance all have calibration records that improve the modifier values in this framework over time.

**Integration:** Fixture calendar intelligence integrates simultaneously with athlete availability (injury, rotation), macro environment (regime), fan token governance votes (timing), and seasonal demand patterns. All must be held together — not processed sequentially.

**Communication:** Structured fixture brief in plain language for holders. Technical modifier stack visible for developers. Section 6 Step 7 is the communication template — different depth for different audiences, same underlying framework.

**Calibration:** Confidence weights are explicitly applied per fixture type. Post-break ×0.93 confidence and early season ×0.85 should be validated against calibration records. If post-break fixtures are systematically more predictable than ×0.93 implies, upgrade the weight.

**Adaptation:** When fixtures are rescheduled (weather, VAR postponements, cup replays), the calendar framework adapts immediately. T-12h monitoring windows move with the fixture. Congestion calculations recalculate from the new date without requiring a calibration cycle.

**Verification:** Live fixture data must be verified against Tier 1 sources before any signal is produced. Premier League official, UEFA official, and club official channels are Tier 1. Third-party aggregators are Tier 2. Never produce a signal from unverified fixture data.

**Ethics:** Fixture-driven demand projections must not be presented as financial advice. Supply event estimates are probabilistic reasoning — not guaranteed outcomes. Holders who act on fixture intelligence do so with full understanding of the uncertainty embedded in every modifier.

**Transparency:** Every fixture signal shows its complete modifier stack: competition weight + congestion modifier + break context + season arc modifier = compound modifier. Section 6 is the transparency framework — every step is visible, auditable, and reproducible.

---

## Compatibility

**Fixture congestion base:**    `core/core-fixture-congestion.md`
**Athlete motivation:**         `core/athlete-motivation-intelligence.md`
**FTP PATH_2 mechanics:**       `fan-token/ftp-path2.md`
**Arsenal reference:**          `fan-token/arsenal.md`
**Scenario intelligence:**      `core/scenario-intelligence.md`
**National team tokens:**       `fan-token/national-team-tokens.md`
**Portfolio intelligence:**     `fan-token/portfolio-intelligence.md`
**Seasonal intelligence:**      `core/seasonal-intelligence.md`

---

*SportMind v3.97.86 · MIT License · sportmind.dev*
*SportMind provides the reasoning. The developer provides the live fixture data.*
*Seven-step reasoning chain. All 14 Mind dimensions mapped.*
