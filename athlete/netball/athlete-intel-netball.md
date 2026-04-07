# Netball — Athlete Intelligence

Player-level intelligence for netball predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** World Cup and Commonwealth Games prediction markets

---

## Overview

Netball athlete intelligence focuses on goal shooter accuracy (the primary scoring variable) and the centre-pass conversion rate (determines possession advantage). The Australian national system produces the deepest individual talent data.

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

Master composite modifier for Netball. Combines availability, form, and sport-specific variables.

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
  "modifier_reason": "Goal shooter accuracy and centre pass conversion is the primary driver"
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

### Netball pre-event workflow

```
# Step 1: Load domain context
Load sports/netball/sport-domain-netball.md

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

**L1 domain:** `sports/netball/sport-domain-netball.md`
**L4 market:** `market/market-netball.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_shooting_accuracy` | Goal-shooter accuracy %, super shot rate, shooting zone | Yes |
| `get_centre_court_form` | Centre/wing attack/wing defence — turnovers and feeds | Yes |
| `get_goalkeeper_intercept` | Goal keeper and goal defence intercept rate | Yes |
| `get_availability` | International window, injury, suspension | Yes |
| `get_athlete_signal_modifier` | Composite netball modifier | Yes |

---

## Shooting accuracy primacy

```
NETBALL SHOOTING — THE PRIMARY SCORING SIGNAL:

Goal Shooter (GS) and Goal Attack (GA) are the only players who can score.
Their accuracy determines matches. Elite combined shooting > 88%.

SHOOTING ACCURACY:
  > 92% combined (GS + GA): elite — × 1.12
  88-92%: good — × 1.05
  84-88%: average — × 1.00
  < 84%: below par — × 0.92

SUPER SHOT (SSN/international — 2-pointer from outer zone):
  Super shot conversions above 50%: × 1.06 for goal-scoring output
  Risk: missed super shots = 0 points; conservative teams may avoid

GOAL KEEPER / GOAL DEFENCE:
  Intercept rate (interceptions per possession): primary defensive signal
  Elite intercept rate > 2.5/match: × 1.08 defensive modifier
```

## Competition context

```
SUPER NETBALL (AUSTRALIA — top league):
  Best domestic competition globally; 8 franchises
  Season: May-September (Australian winter)
  Sunshine Coast Lightning, Melbourne Vixens: highest ATM clubs
  
NETBALL WORLD CUP:
  Every 4 years; Southern Hemisphere dominance (Australia, NZ, England)
  Australia × 1.30 home tournament; New Zealand × 1.25
  
ENGLAND NETBALL / VITALITY ROSES:
  Growing UK market; Commonwealth Games and World Cup elevated
  Tamsin Greenway era: built commercial profile in UK
  
ATM: Netball ATM strongest in Australia, New Zealand, England, Jamaica
```

## Command reference / Modifier reference

### `get_athlete_signal_modifier`
```json
{
  "player": "string",
  "position": "GS|GA|WA|C|WD|GD|GK",
  "shooting_modifier": 1.08,
  "availability_modifier": 1.00,
  "composite_modifier": 1.06,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["GA struggling on super shots this week"],
  "modifier_reason": "Elite shooting accuracy + full squad"
}
```

| Modifier | Source | Range |
|---|---|---|
| `shooting_modifier` | `get_shooting_accuracy` | 0.92–1.12 |
| `intercept_modifier` | `get_goalkeeper_intercept` | 0.95–1.08 |
| `availability_modifier` | `get_availability` | 0.88–1.00 |
| `composite_modifier` | Product of all | 0.82–1.20 |


*MIT License · SportMind · sportmind.dev*
