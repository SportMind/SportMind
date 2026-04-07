# Rowing — Athlete Intelligence

Player-level intelligence for rowing predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** Olympic prediction markets; Boat Race (UK)

---

## Overview

Rowing athlete intelligence is dominated by ergometer (erg) split times for individual assessment and course conditions (wind, current, temperature) for race-day modifiers. Seat racing outcomes are the primary selection signal.

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

Master composite modifier for Rowing. Combines availability, form, and sport-specific variables.

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
  "modifier_reason": "Split time and course conditions is the primary driver"
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

### Rowing pre-event workflow

```
# Step 1: Load domain context
Load sports/rowing/sport-domain-rowing.md

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

**L1 domain:** `sports/rowing/sport-domain-rowing.md`
**L4 market:** `market/market-rowing.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_erg_score` | Ergometer time — primary fitness proxy | Yes |
| `get_regatta_record` | World Rowing Cup and Championship results | Yes |
| `get_boat_class_form` | Single/double/quad/eight — class-specific record | Yes |
| `get_conditions_modifier` | Wind/current/water conditions impact | Yes |
| `get_athlete_signal_modifier` | Composite rowing modifier | Yes |

---

## Ergometer and PB model

```
ROWING SIGNAL MODEL (similar to athletics — performance vs PB):

2km ergometer time is the universal fitness proxy.
On-water performance adds boat-class specific factors.

ERG SCORE MODEL:
  Within 1% of season best: peak form × 1.10
  Within 2%: good form × 1.04
  Within 4%: average × 1.00
  4%+ below: below form × 0.93

BOAT CLASS SPECIFICITY:
  Single scull: individual; pure performance signal
  Double/pair: chemistry matters; partnership history is a modifier
  Four/eight: crew cohesion; less individual signal; team-level analysis
  
  INDIVIDUAL EVENT MODIFIER (single/double): PB model applies directly
  CREW EVENT MODIFIER (eight+): apply 60% individual, 40% crew chemistry
```

## Henley and major regatta context

```
MAJOR REGATTAS:
  World Rowing Championships: peak annual event (Olympics in Olympic year)
  Henley Royal Regatta (UK): most prestigious invitation regatta
  World Rowing Cup: circuit; leading to championships
  
  HENLEY: challenge format; one-on-one knock-out; tactical racing
  Championships: heat-to-final; multiple races; fatigue accumulates
  
CONDITIONS SIGNAL:
  Head wind > 3 m/s: times significantly slower; specialist advantage smaller
  Tail wind > 2 m/s: fast conditions; PB proximity less diagnostic
  Crosswind: affects steering; more experienced steerers advantaged
  
  Olympics/World Championships hold races regardless of conditions (usually)
  Apply conditions_modifier when wind >3 m/s or current present
```

## Command reference / Modifier reference

### `get_athlete_signal_modifier`
```json
{
  "athlete": "string",
  "boat_class": "single|double|four|eight",
  "erg_modifier": 1.06,
  "conditions_modifier": 0.97,
  "composite_modifier": 1.02,
  "adjusted_direction": "NEUTRAL_POSITIVE",
  "key_risks": ["Head wind 4 m/s forecast — times 2-3% slower across board"],
  "modifier_reason": "Good erg form; conditions reduce reliability"
}
```

| Modifier | Source | Range |
|---|---|---|
| `erg_modifier` | `get_erg_score` | 0.93–1.10 |
| `regatta_record` | `get_regatta_record` | 0.90–1.10 |
| `conditions_modifier` | `get_conditions_modifier` | 0.88–1.05 |
| `composite_modifier` | Product of all | 0.80–1.20 |


*MIT License · SportMind · sportmind.dev*
