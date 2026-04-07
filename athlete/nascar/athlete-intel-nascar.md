# NASCAR — Athlete Intelligence

Player-level intelligence for nascar predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** NASCAR prediction markets; DFS platforms

---

## Overview

NASCAR athlete intelligence requires track-type matching. A superspeedway specialist is a different athlete to a short track specialist. Stage points accumulation strategy changes driver risk behaviour in the Championship 4 window.

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

Master composite modifier for NASCAR. Combines availability, form, and sport-specific variables.

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
  "modifier_reason": "Track type specialisation is the primary driver"
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

### NASCAR pre-event workflow

```
# Step 1: Load domain context
Load sports/nascar/sport-domain-nascar.md

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

**L1 domain:** `sports/nascar/sport-domain-nascar.md`
**L4 market:** `market/market-nascar.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_track_type_record` | Superspeedway/intermediate/short track/road course record | Yes |
| `get_stage_points_strategy` | Stage points position and playoff implications | Yes |
| `get_pit_crew_rating` | Pit stop speed and consistency — race-changing variable | Yes |
| `get_equipment_tier` | Car/engine package quality; manufacturer tier | Yes |
| `get_plate_racing_record` | Superspeedway pack racing specific stats | Yes |
| `get_athlete_signal_modifier` | Composite NASCAR modifier | Yes |

---

## Track type specialisation — the primary signal

```
NASCAR IS TRACK-TYPE SPECIFIC — more than any other motorsport:

A driver who excels at Daytona and Talladega superspeedways may struggle
at Bristol short track or Sonoma road course. Track matching is the
first analytical step before any form data.

TRACK TYPES:

SUPERSPEEDWAYS (Daytona, Talladega — 2.5+ mile ovals):
  Pack racing: 30-40 cars in tight formation; aerodynamics dominate
  Individual driving skill less important than position management and plate setup
  Crash risk: elevated significantly (multi-car accidents common)
  
  Superspeedway specialist modifier:
    Top-10 finish rate at superspeedways > 60%: × 1.12
    But crash risk reduces reliability: apply confidence_interval × 0.80
    
  KEY RULE: At superspeedways, equipment/car setup matters more than driver ability.
  Apply manufacturer_tier modifier as primary variable.
  
INTERMEDIATE TRACKS (Atlanta, Charlotte, Las Vegas — 1-2 mile ovals):
  Most common track type; most race experience available
  Driver consistency and tire management are key
  Primary signal: average finishing position at 1.5-mile ovals
  
  Modifier: average finish last 5 intermediate races vs season average
  Within 3 positions better than average: × 1.06
  3+ positions worse: × 0.93
  
SHORT TRACKS (Bristol, Martinsville, Richmond — under 1 mile):
  Highest contact frequency; most restarts
  Aggressive driving style advantaged; patience required
  Bristol Night Race: most intense NASCAR atmosphere
  
  Short track specialist (avg finish < 12 at short tracks): × 1.08
  
ROAD COURSES (Sonoma, Watkins Glen, Charlotte Roval):
  Least NASCAR-typical; road racing skills transfer from GT/sports car
  Road course ringers (drivers brought in for specific expertise): elevated
  Traditional oval racers: × 0.88 (skill set disadvantage)
  NASCAR drivers with road racing background: × 1.10
```

## Playoff and championship intelligence

```
NASCAR PLAYOFFS (Championship 4 model):

NASCAR uses an elimination playoff — poor performance eliminates teams.
This creates specific pressure signals unavailable in championship systems.

PLAYOFF ROUNDS:
  Round of 16 (4 races): three elimination spots per race if win; otherwise points
  Round of 12: same structure
  Round of 8: same structure
  Championship 4 (Phoenix): winner-take-all — only wins at Phoenix matter

ABOVE THE CUT LINE:
  Driver currently in playoff advancement position: × 1.05 (secured, managing)
  Driver on elimination bubble: × 1.12 (maximum desperation motivation)
  Driver eliminated or cannot advance: × 0.88 (reduced motivation)

STAGE POINTS STRATEGY:
  Modern NASCAR awards points for leading at Stage breaks (Laps ~25/60/final)
  Stage points can change championship math: drivers may race aggressively
  for stage points even if race win is unlikely
  
  Stage points leader at Stage 1: positive momentum signal for race winner prediction
  
REGULAR SEASON WIN = PLAYOFF BERTH:
  Winning a regular season race locks a driver into the playoffs
  A driver close to their first win is in maximum motivation state
  Apply: first_win_hunting × 1.10 for drivers without a 2026 win

MANUFACTURER TIER:
  Hendrick Motorsports, Joe Gibbs Racing: Tier 1 equipment
  Stewart-Haas (dissolved 2024), Chip Ganassi: varies
  
  Equipment tier modifier remains significant in NASCAR
  Tier 1 equipment with average driver vs Tier 3 with elite driver:
  Equipment wins ~60% of encounters — larger than MotoGP, smaller than F1
```

## ATM framework for NASCAR

```
NASCAR ATM TIERS:

Tier 1 — American icons (Dale Earnhardt Jr legacy; current: Kyle Larson, Denny Hamlin):
  ATM 0.72-0.80; recognised by all American sports fans
  Daytona 500 winner = permanent ATM uplift (+0.05 career)
  
Tier 2 — Multiple race winners:
  ATM 0.55-0.68; strong US market recognition
  
DAYTONA 500 SIGNAL:
  "The Super Bowl of NASCAR" — most watched race, February
  Winner's ATM: × 1.20 for full season (defending Daytona champion)
  Race signal weight: × 1.50 (vs standard NASCAR race × 1.00)
  
TOKEN MARKET:
  No NASCAR tokens currently active on Chiliz Chain
  Architecture ready for when launched
  Addressable market: US South + Midwest = strong potential fan token base
  NASCAR + DraftKings/FanDuel integration: digital-native fan base ready
```

## Integration: Full NASCAR pre-race workflow

```
Step 1: Load domain context
  Load sports/nascar/sport-domain-nascar.md

Step 2: TRACK TYPE CLASSIFICATION FIRST
  Superspeedway? Short track? Intermediate? Road course?
  Apply track-type-specific primary signal

Step 3: Equipment/manufacturer tier
  get_equipment_tier — Tier 1 or lower?
  Superspeedways: equipment > driver; Intermediates: more balanced

Step 4: Playoff context
  get_stage_points_strategy — is this driver fighting for points?
  Bubble driver: maximum motivation × 1.12

Step 5: Pit crew assessment
  get_pit_crew_rating — elite pit crew can gain 2-3 positions per race
  Sub-12 second average pit stop: × 1.05

Step 6: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`
```json
{
  "driver": "string",
  "track_type": "superspeedway|intermediate|short_track|road_course",
  "track_type_modifier": 1.08,
  "playoff_context_modifier": 1.12,
  "equipment_tier_modifier": 1.05,
  "pit_crew_modifier": 1.03,
  "composite_modifier": 1.15,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Superspeedway crash risk — confidence_interval widened"],
  "modifier_reason": "Short track specialist; playoff bubble motivation; Tier 1 equipment"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `track_type_modifier` | `get_track_type_record` | 0.88–1.12 |
| `playoff_modifier` | `get_stage_points_strategy` | 0.88–1.12 |
| `equipment_modifier` | `get_equipment_tier` | 0.90–1.10 |
| `pit_crew_modifier` | `get_pit_crew_rating` | 0.95–1.05 |
| `composite_modifier` | Product of all applicable | 0.75–1.30 |


*MIT License · SportMind · sportmind.dev*
