# Handball — Athlete Intelligence

Player-level intelligence for handball predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** EHF handball prediction markets; PSG handball-adjacent signals

---

## Overview

Handball athlete intelligence centres on the goalkeeper — the single most important position in the sport. A goalkeeper with >35% save rate can override team-level signals. Centre-back creative play and wing speed are secondary variables.

---

## Commands

| Command | Description |
|---|---|
| `get_availability` | Player/athlete availability status |
| `get_form_score` | Recent performance score (last 5 events) |
| `get_sport_modifier` | Sport-specific key variable modifier |
| `get_athlete_signal_modifier` | Composite modifier — runs all sub-skills |

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for Handball. Combines availability, form, and sport-specific variables.

**Parameters:**
- `player_id` (required) — athlete identifier  
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{
  "athlete": "string",
  "availability": 1.0,
  "form_score": 0.85,
  "sport_specific_modifier": 1.05,
  "composite_modifier": 1.05,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["string"],
  "modifier_reason": "Goalkeeper save percentage is the primary driver"
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Peak fitness, top recent form, ideal conditions | ×1.20 |
| Fit, good form | ×1.10 |
| Neutral | ×1.00 |
| Minor fitness concern | ×0.90 |
| Significant fitness doubt | ×0.80 |
| Key athlete confirmed unavailable | ×0.70 |

---

## Integration example

### Handball pre-event workflow

```
# Step 1: Load domain context
Load sports/handball/sport-domain-handball.md

# Step 2: Athlete checks
get_availability athlete=[ATHLETE_ID]
get_form_score athlete=[ATHLETE_ID]
get_sport_modifier athlete=[ATHLETE_ID]

# Step 3: Get composite modifier
get_athlete_signal_modifier athlete=[ATHLETE_ID] event=[EVENT_ID]

# Step 4: Decision logic
# composite_modifier >= 1.10 AND signal >= 65 → ENTER
# composite_modifier < 1.00 OR injury_warning → WAIT or ABSTAIN
```

---

## Compatibility

**L1 domain:** `sports/handball/sport-domain-handball.md`
**L4 market:** `market/market-handball.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_goalkeeper_form` | Save rate, shot-stopping vs 7m, efficiency vs wings | Yes |
| `get_raider_profile` | For pivot/wing: breakthrough rate, positional scoring | Yes |
| `get_pivot_dominance` | Centre-back creativity, assists, breakthrough creation | Yes |
| `get_lineup_availability` | International window, injury, suspension status | Yes |
| `get_fatigue_profile` | EHF Champions League + domestic load management | Yes |
| `get_athlete_signal_modifier` | Composite handball modifier | Yes |

---

## Goalkeeper primacy model

```
HANDBALL GOALKEEPER — THE MOST IMPORTANT INDIVIDUAL IN THE SPORT:

A goalkeeper with a >35% save rate can override a team-level quality deficit.
Unlike football where goalkeepers prevent goals, handball goalkeepers save
approximately 30-35% of shots as the baseline. An elite goalkeeper saves 38-42%.

SAVE RATE THRESHOLDS:
  > 40% save rate: exceptional — modifier × 1.20 (team wins matches it should lose)
  37-40%:          elite — × 1.12
  34-37%:          above average — × 1.06
  31-34%:          average — × 1.00
  < 31%:           below average — × 0.92
  < 27%:           struggling — × 0.85 (significant vulnerability)

7-METRE SHOT STOPPING:
  7m penalties are essentially 1v1 contests between shooter and keeper
  Elite 7m stopper (>30% stopped): × 1.08 modifier
  Below average (<20% stopped): × 0.95

SHOT POSITION DIFFERENTIATION:
  Wing shots (acute angle): keepers generally perform better — less information signal
  Centre-back shots: hardest to stop; keeper performance here is the most diagnostic
  Pivot shots: 6-metre zone; requires physical positioning strength
  
  AGENT RULE: When evaluating a goalkeeper, weight centre-back shot efficiency
  most heavily. Wing shot save rates are less predictive.
```

## Positional framework

```
HANDBALL POSITIONS AND SIGNAL WEIGHT:

GOALKEEPER (GK):
  Signal weight: highest individual (as above)
  
CENTRE-BACK / PLAYMAKER (CB):
  Orchestrates attack; assist rate is primary signal
  Elite CB (10+ assists/game): × 1.10
  Creates breakthrough opportunities for wings and pivot
  
WINGS (LW/RW):
  Scoring specialists; wing goals come from fast breaks and line plays
  High scorer wing (8+ goals/game): × 1.06
  Fast break conversion rate: secondary signal
  
PIVOT / LINE PLAYER (P):
  Physical position in 6m zone; screen plays and close-range goals
  Dominant pivot (70%+ shooting efficiency at 6m): × 1.05
  
BACKCOURT SHOOTERS (LB/RB):
  Long-range shooting specialists
  Used more at elite level (Bundesliga, EHF) than lower leagues
  
SIGNAL HIERARCHY:
  GK form > CB creativity > Wing speed > Pivot dominance > Backcourt volume
```

## EHF Champions League context

```
EHF CHAMPIONS LEAGUE (Europe's highest handball competition):
  Final Four format (similar to basketball — one weekend, two semis + final)
  Highest-quality individual performances at this level
  
  FINAL FOUR signal multiplier: × 1.65 (elite weekend, marquee event)
  
BUNDESLIGA (Germany — best domestic league):
  Most competitive domestic league; player quality highest here
  Bundesliga form is strongest predictor for EHF performance
  
VELUX EHF CHAMPIONS LEAGUE GROUPS:
  16 teams; group phase matches weight: × 0.55
  Knockout phase: × 0.80-1.00
  
INTERNATIONAL WINDOWS:
  IHF World Championship, European Championship every 2 years
  Players released from clubs: congestion signal for clubs
  Apply: × 0.88 for clubs losing 3+ national team players
  
ATM TIERS FOR HANDBALL:
  Tier 1 — Icons: Mikkel Hansen era, current: star players with 5M+ reach
    ATM 0.70-0.78; globally recognised within handball community
  Tier 2 — National team captains, Champions League stars:
    ATM 0.55-0.68
  National ATM premium:
    Danish player in Denmark: × 1.30 (handball is national sport)
    German player in Bundesliga: × 1.20 (largest handball market)
    Croatian player at Croatia: × 1.25
```

## Integration: Full handball pre-match workflow

```
Step 1: Load domain context
  Load sports/handball/sport-domain-handball.md

Step 2: Goalkeeper check FIRST
  get_goalkeeper_form — save rate last 5 matches
  > 37%: positive signal; < 31%: vulnerability flag

Step 3: International window check
  get_lineup_availability — 3+ players on international duty?
  Apply × 0.88 for affected clubs

Step 4: Pivot/wing key player check
  get_raider_profile for star wing or pivot
  Form + availability

Step 5: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`
```json
{
  "player": "string",
  "position": "GK|CB|LW|RW|LB|RB|P",
  "save_rate_modifier": 1.12,
  "lineup_availability_modifier": 1.00,
  "form_modifier": 1.06,
  "composite_modifier": 1.10,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["International window — 2 key players away"],
  "modifier_reason": "Elite GK (38% save rate) + full squad available"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `goalkeeper_save_rate` | `get_goalkeeper_form` | 0.85–1.20 |
| `pivot_dominance` | `get_pivot_dominance` | 0.95–1.05 |
| `lineup_modifier` | `get_lineup_availability` | 0.88–1.00 |
| `fatigue_modifier` | `get_fatigue_profile` | 0.90–1.00 |
| `composite_modifier` | Product of all applicable | 0.78–1.25 |


*MIT License · SportMind · sportmind.dev*
