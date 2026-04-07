# Formula 1 — Athlete Intelligence

Driver-level intelligence for Formula 1 predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** Constructor fan tokens ($FERRARI, $MCLAREN, etc.),
driver prediction markets, qualifying and race outcome markets.

---

## Overview

F1 driver intelligence is constructor-filtered — a driver's performance directly
affects their constructor's token value (DTM: Driver Token Multiplier). The single
most predictive driver variable is qualifying pace relative to teammate, not overall
race pace. Qualifying locks grid position; grid position determines race opportunity.

---

## Commands

| Command | Description |
|---|---|
| `get_qualifying_delta` | Driver's pace gap vs teammate in qualifying (primary signal) |
| `get_recent_form` | Last 5 races: finishes vs grid position (over/underperformance) |
| `get_wet_weather_rating` | Wet race specialist score — highly predictive in rain |
| `get_regulation_fit` | How well current car suits this driver's style |
| `get_athlete_signal_modifier` | Composite modifier combining all F1 driver factors |

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for F1. Combines qualifying pace, recent form, tyre management, and constructor status.

**Parameters:**
- `driver_id` (required) — driver identifier
- `race_id` (optional) — specific race; defaults to next scheduled

**Returns:**
```json
{
  "driver": "string",
  "constructor": "string",
  "qualifying_delta_vs_teammate": -0.15,
  "recent_form_delta": 1.05,
  "wet_weather_specialist": false,
  "regulation_fit_score": 0.85,
  "composite_modifier": 1.08,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Grid penalty applied", "Starting from P6 not P3"],
  "modifier_reason": "Faster than teammate in qualifying; strong recent results"
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Pole position, fastest in class, dry specialist in dry | ×1.20 |
| Front row start, recent podium form | ×1.10 |
| Neutral — mid-grid, average form | ×1.00 |
| Grid penalty applied (5+ places) | ×0.90 |
| Wet race when not a wet specialist | ×0.88 |
| Major mechanical failure in qualifying (starts from pit lane) | ×0.75 |
| Active injury / physical impairment | ×0.70 |

### Knockout conditions

| Condition | Floor modifier |
|---|---|
| Driver confirmed DNS (Did Not Start) | 0.55 |
| Starts from pit lane with major setup compromise | 0.70 |

---

## Integration example

### F1 pre-race weekend workflow

```
# Step 1: Load domain context
Load sports/formula1/sport-domain-formula1.md

# Step 2: After qualifying — this is the key intelligence moment
get_qualifying_delta driver=[DRIVER_ID] session=[QUALIFYING_ID]
get_recent_form driver=[DRIVER_ID] last_n=5

# Step 3: Check weather forecast for race day
Load core/core-weather-match-day.md
get_wet_weather_rating driver=[DRIVER_ID]  # if rain forecast

# Step 4: Get composite modifier
get_athlete_signal_modifier driver=[DRIVER_ID] race=[RACE_ID]

# Step 5: Decision logic
# If front row + dry conditions + recent form >= 1.05 → ENTER
# If grid penalty OR safety car likely (street circuit) → REDUCE
# Output: SportMind confidence schema
```

## Compatibility

**L1 domain:** `sports/formula1/sport-domain-formula1.md`
**L3 token:** `fan-token/formula1-token-intelligence/`
**L4 market:** `market/market-formula1.md`
**Weather:** `core/core-weather-match-day.md`


---

## Driver-Constructor pairing intelligence

In Formula 1, you cannot analyse a driver without their constructor.
A driver with a Tier 1 car is a different entity commercially and competitively
from the same driver in a Tier 3 car. The DTM (Driver Token Multiplier) is
always a driver-constructor combination, never a driver alone.

```
CONSTRUCTOR TIERS (updated at season start):
  Tier 1 — Champion-level hardware:
    Current constructors champion or within 50pts at season start
    Driver modifier: × 1.12 base (car advantage is structural)
    
  Tier 2 — Competitive midfield:
    Regularly scoring points; occasional podium threat
    Driver modifier: × 1.00 base
    
  Tier 3 — Lower midfield:
    Points occasional; primarily racing for development
    Driver modifier: × 0.92 base
    
  Tier 4 — Backmarker:
    Rarely scores points; development/funding priority
    Driver modifier: × 0.83 base

DRIVER-CONSTRUCTOR INTERACTION:
  Strong driver in weak car:
    Driver still matters — wheel-to-wheel racecraft + overtaking ability
    Apply: driver_skill_premium × 0.75 (talent partially overcomes hardware)
    
  Average driver in Tier 1 car:
    Hardware advantage reduces driver differentiation
    Apply: constructor_tier_modifier × 1.05 (car does most of the work)
    
  Elite driver in Tier 1 car:
    Maximum combined signal
    Apply: constructor_tier × driver_premium × 1.08

QUALIFYING TEAMMATE DELTA — primary individual signal:
  Faster than teammate in qualifying:
    > 0.3s faster: × 1.15 (dominant within team)
    0.1-0.3s faster: × 1.08
    Within 0.1s: × 1.02 (competitive equals)
    Slower: × 0.94 to × 0.87 (concerning)
    
  This delta is ALWAYS relative to the same constructor.
  A driver 0.3s faster than a Tier 4 teammate ≠ same signal as
  0.3s faster than a Tier 1 teammate.
```

## Circuit-specific intelligence

```
CIRCUIT ARCHETYPES AND DRIVER SIGNALS:

STREET CIRCUITS (Monaco, Singapore, Jeddah, Baku):
  Overtaking extremely difficult → qualifying is amplified
  Monaco: qualifying delta × 1.40 (if you start P1, you win)
  Safety car probability: elevated → volatile results
  Modifier: qualifying_delta × 1.30 for street circuits
  
  STREET CIRCUIT SPECIALIST:
    Driver with strong street circuit win record (Monaco esp.):
    Apply × 1.12 specialist bonus
    
POWER CIRCUITS (Monza, Spa, Silverstone):
  Engine/straight-line speed dominant
  Overtaking possible → race pace matters more than qualifying
  Modifier: qualifying_delta × 0.85 (less decisive on power circuits)
  
HIGH-DOWNFORCE CIRCUITS (Hungary, Suzuka):
  Aerodynamic efficiency dominant
  Tyre degradation matters — tyre management specialists advantaged
  Modifier: tyre_management_rating × 1.10
  
MIXED-PROFILE CIRCUITS (most of the calendar):
  Standard analysis; no circuit archetype modifier applied
  Use qualifying_delta as primary variable

WET RACE CIRCUIT CONSIDERATION:
  Some circuits are known for wet race probability:
  Spa, Suzuka, Interlagos — higher historical wet race frequency
  Pre-race weather check is mandatory for these circuits
```

## Season narrative intelligence

```
FORMULA 1 SEASON NARRATIVE ARC:

CONSTRUCTORS CHAMPIONSHIP:
  Teams trailing in CC with < 8 rounds left: maximum risk-taking stance
  Teams leading CC with comfortable margin: conservative risk strategy
  
  AGENT RULE: A constructor leading by >100 points with 5 races left
  will protect results — do not expect aggressive strategies.
  Apply × 0.92 to race-win probability for dominant leader preserving points.

DRIVERS CHAMPIONSHIP BATTLE:
  Two drivers within 25 points with 5 races left = maximum title narrative
  Title decider (final race, multiple outcomes possible): NCSI × 1.25
  
SPRINT RACE INTEGRATION (now part of 6 GP weekends):
  Sprint race Saturday: 40% weight signal (separate from Sunday GP)
  Sprint results can affect pit strategy confidence for Sunday
  Sprint crash → monitor driver fitness before Sunday race analysis
  
FINAL RACE OF SEASON (Abu Dhabi):
  Multiple championship outcomes possible until final lap:
  Apply narrative_active flag; standard signal weight elevated × 1.20
```

## Token intelligence for F1

```
F1 FAN TOKEN ECOSYSTEM:

Constructor tokens (Chiliz platform):
  Team performance drives token signal directly
  Constructor win → immediate positive HAS spike
  Constructor DNF/failure → negative signal (especially if star driver)
  
  ATM DRIVER MAPPING:
    Tier 1 driver (Verstappen, Hamilton tier): ATM 0.88-0.92
    DTM applied per race result: win × 1.15, podium × 1.05, DNF × 0.85
    
RACE WEEKEND TOKEN SIGNAL CALENDAR:
  Thursday (Practice 1-2): minimal signal
  Saturday Qualifying: FIRST MAJOR SIGNAL POINT of weekend
    Pole position: +3 to +8% token price movement
    Front row: +2 to +5%
    Disappointing qualifying: -2 to -6%
  Sunday Pre-race (2h): second major signal point
    Final grid after penalties confirmed: token movement
  Sunday Race result: peak signal
    Win: +8 to +20%
    DNF from leading position: -5 to -15%
    
CONSTRUCTOR SWITCH SIGNAL:
  Elite driver signed to new constructor:
    Signing constructor: +8 to +18% (elite talent arriving)
    Departing constructor: -5 to -12% (elite talent departing)
    
  Most significant constructor change: Verstappen announced retirement from RBR
  or equivalent — maximum disruption signal
```

## Integration: Full F1 race weekend workflow

```
Step 1: Load domain context
  Load sports/formula1/sport-domain-formula1.md
  Update constructor tiers if season has started (check standings)

Step 2: Circuit classification
  Street circuit? → qualifying_delta × 1.30 (amplify qualifying importance)
  Power circuit? → qualifying_delta × 0.85 (de-emphasise qualifying)
  Standard circuit? → standard qualifying_delta weight

Step 3: Weather forecast
  Rain probability > 40%? → hardware tier reset; wet specialist check
  get_wet_weather_rating for involved drivers
  
Step 4: Post-qualifying analysis (Saturday — most important window)
  get_qualifying_delta — who is fastest within each constructor?
  Grid penalties confirmed? → adjust expected starting positions
  
Step 5: Season narrative context
  Championship implications? → apply narrative_active if title at stake
  Sprint race this weekend? → check Saturday result before Sunday analysis
  
Step 6: Composite modifier
  get_athlete_signal_modifier (qualifying + circuit + weather + championship)
  
Step 7: Decision
  Pole + dry + no penalties + Tier 1 car: ENTER standard
  Wet race: reduce confidence by 1 tier regardless of qualifying
  Title decider: ENTER at 65% (high variance event)
```


*MIT License · SportMind · sportmind.dev*
