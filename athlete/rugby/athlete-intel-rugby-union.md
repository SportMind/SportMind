# Rugby Union — Athlete Intelligence

Player-level intelligence for rugby union and league fan tokens. Covers set piece dominance, kicker accuracy, breakdown specialists, and halfback partnership metrics.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_set_piece_dominance` | Lineout %, scrum success, maul metres | Yes |
| `get_kicker_accuracy` | Conversion %, penalty %, zone performance | Yes |
| `get_breakdown_metrics` | Turnovers won, ruck success, dominant tackles | Yes |
| `get_halfback_partnership` | 9/10 combination stats and win rate | Yes |
| `get_player_availability` | Injury, suspension, rotation plans | Yes |
| `get_physical_metrics` | Carries, metres, offloads, tackles | Yes |
| `get_athlete_signal_modifier` | Composite rugby modifier | Yes |

---

## Key metrics

### `get_set_piece_dominance`
```json
{
  "token": "RUGBY_TOKEN",
  "set_piece": {
    "lineout_win_pct_own_ball": 88.0,
    "lineout_steal_pct": 12.0,
    "scrum_success_own_ball": 94.0,
    "scrum_penalty_concession_per_match": 0.8,
    "maul_metres_per_match": 34.0,
    "hooker_throw_accuracy_pct": 91.0,
    "key_locks_available": true
  },
  "set_piece_score": 86,
  "signal_modifier": 1.10
}
```

### `get_kicker_accuracy`
```json
{
  "player": "Finn Russell",
  "kicking_metrics": {
    "conversion_pct": 84.0,
    "penalty_goal_pct": 78.0,
    "zone_performance": {
      "central_0_22m": 97.0,
      "wide_22_35m": 72.0,
      "central_35_50m": 68.0,
      "wide_35_50m": 44.0
    },
    "crosswind_performance": "MODERATE",
    "clutch_kicks_last_5_games": { "attempts": 8, "scored": 6 },
    "kicking_form_score": 81
  },
  "signal_modifier": 1.06
}
```

### `get_halfback_partnership`
```json
{
  "scrum_half": "Ben Youngs",
  "fly_half": "Finn Russell",
  "appearances_together": 18,
  "team_win_rate_together": 0.72,
  "service_time_avg_sec": 2.8,
  "box_kick_pct": 28.0,
  "flat_ball_pct": 58.0,
  "partnership_chemistry_score": 84,
  "signal_modifier": 1.08
}
```

---

## Rugby modifier table

| Condition | Modifier |
|---|---|
| Set piece dominant, all props available | 1.10 |
| First-choice kicker confirmed | 1.06 |
| Key prop injured (scrum weakness) | 0.88 |
| Fly-half doubtful or out | 0.85 |
| Established 9/10 partnership split | 0.90 |
| Wet conditions (kicking team disadvantage) | 0.92 |


---

## Modifier reference

| Condition | Modifier |
|---|---|
| Full XV confirmed, kicker fit, top form | ×1.20 |
| Key players fit, strong set piece confirmed | ×1.10 |
| Neutral — standard availability | ×1.00 |
| Kicker concern or one forward absence | ×0.90 |
| Starting kicker out OR hooker out (lineout loss) | ×0.82 |
| Multiple front row absences | ×0.70 |

*Ranges consistent with `core/core-athlete-modifier-system.md`*


## Integration example

### Rugby Union pre-event workflow

```
# Step 1: Load domain context
Load sports/rugby/sport-domain-rugby.md

# Step 2: Check athlete availability and form
get_availability token=[RUGB]
get_form_score token=[RUGB]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[RUGB]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier. Combines all sport-specific sub-components into one multiplier.

**Parameters:**
- `player_id` (required) — player or team identifier
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{{
  "player": "string",
  "availability": 1.0,
  "form_modifier": 1.05,
  "sport_specific_modifier": 1.02,
  "composite_modifier": 1.07,
  "adjusted_direction": "POSITIVE",
  "confidence": 0.85,
  "key_risks": ["string"],
  "modifier_reason": "string"
}}
```

