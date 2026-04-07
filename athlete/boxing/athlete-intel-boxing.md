# Boxing Athlete Intelligence — SportMind Skill

Player-level intelligence for boxing prediction markets and fan tokens.
Heavily overlaps with `athlete/mma` — fight camp, weigh-in, and finishing tendency
logic is nearly identical. Key differences: title belt structure, division hierarchy, judging patterns.

**Applicable tokens / markets:** Fighter tokens, boxing prediction markets, title fight outcome markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_fighter_record` | Professional record, quality of opposition analysis | Yes |
| `get_physical_matchup` | Reach, height, stance, age curve | Yes |
| `get_weigh_in_status` | Official weigh-in result — binary risk check | Yes |
| `get_fight_camp_signals` | Gym, coach, sparring, injury rumours | Yes |
| `get_finishing_tendency` | KO%, decision%, style of victories | Yes |
| `get_belt_status` | Current titles held, mandatory defences due | Yes |
| `get_fighter_form_score` | Rolling form over last N fights | Yes |
| `get_athlete_signal_modifier` | Composite boxing modifier | Yes |

---

## Command reference

### `get_fighter_record`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: all pro fights)

**Returns:**
```json
{
  "fighter": "Anthony Joshua",
  "record": "28-4-0",
  "kos": 25,
  "ko_pct": 89.3,
  "opposition_quality": {
    "world_champions_faced": 6,
    "top_10_opponents": 12,
    "journeymen_pct": 15.4
  },
  "losses_analysis": [
    { "opponent": "Oleksandr Usyk", "method": "UD", "rematch": true },
    { "opponent": "Oleksandr Usyk", "method": "SD", "rematch": false }
  ],
  "record_modifier": 1.10
}
```

### `get_weigh_in_status`

**Parameters:**
- `fighter_name` (required)
- `event_name` (required)

**Returns:**
```json
{
  "fighter": "Tyson Fury",
  "event": "Fury vs Usyk II",
  "weight_limit_lbs": 265,
  "weight_made_lbs": 261.5,
  "result": "MADE_WEIGHT",
  "margin_lbs": 3.5,
  "previous_weight_issues": false,
  "weigh_in_modifier": 1.02,
  "note": "Made weight comfortably — no cut concerns going into fight"
}
```

### `get_finishing_tendency`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: last 15)

**Returns:**
```json
{
  "fighter": "Tyson Fury",
  "finish_rate_pct": 61.5,
  "ko_tko_pct": 61.5,
  "decision_pct": 38.5,
  "avg_rounds": 7.8,
  "late_stopper": true,
  "round_breakdown": {
    "rounds_1_3": 23.1,
    "rounds_4_6": 19.2,
    "rounds_7_9": 30.8,
    "rounds_10_12": 26.9
  },
  "finishing_modifier": 1.08,
  "note": "Fury finishes late — positions markets for late-round drama premium"
}
```

### `get_belt_status`

**Parameters:**
- `fighter_name` (required)

**Returns:**
```json
{
  "fighter": "Oleksandr Usyk",
  "belts_held": ["IBF", "WBA", "WBC", "WBO"],
  "status": "UNDISPUTED_HEAVYWEIGHT",
  "mandatory_defences_due": ["IBF mandatory: Daniel Dubois"],
  "unification_status": "FULL_UNDISPUTED",
  "belt_modifier": 1.25,
  "note": "Undisputed champion — loss is maximum negative catalyst. Highest token floor."
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `fighter_name` (required)
- `opponent_name` (optional)

**Returns:**
```json
{
  "fighter": "Tyson Fury",
  "opponent": "Oleksandr Usyk",
  "base_signal_score": 70,
  "composite_modifier": 1.12,
  "adjusted_signal_score": 78,
  "modifier_breakdown": {
    "record_quality": 1.10,
    "physical_matchup": 1.05,
    "weigh_in_status": 1.02,
    "camp_quality": 1.08,
    "finishing_tendency": 1.08,
    "form": 1.00
  },
  "confidence": 0.80,
  "recommendation": "BULLISH — strong heavyweight narrative, weigh-in confirmed, full camp completed",
  "key_risks": ["Usyk technical style historically problematic for big punchers", "Fight at neutral venue reduces home crowd advantage"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Undisputed champion (all 4 belts) | ×1.25 |
| Unified champion (2–3 belts) | ×1.15 |
| Single belt holder | ×1.05 |
| Made weight comfortably | ×1.02 |
| Full training camp, no injuries | ×1.05 |
| Strong KO% (>70%) | ×1.10 |
| Made weight barely (< 0.5lb margin) | ×0.90 |
| Missed weight by < 1lb (fight proceeds) | ×0.82 |
| Missed weight by > 1lb (title voided) | ×0.72 |
| Taking fight on short notice (< 6 weeks) | ×0.80 |
| Coming off KO loss | ×0.78 |
| Multiple consecutive losses | ×0.72 |
| Career-stage discount (36+ with KO losses) | ×0.75 |

*MIT License · SportMind · sportmind.dev*

---

## Injury intelligence

Full injury intelligence for boxing is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-boxing.md`
  
  
  
  Hand injury detection, cut risk assessment, chin durability history, fight camp secrecy decoder, weigh-in distress signals.
  
  

Load these files alongside this skill for injury-aware agent reasoning.


---

## Integration example

### Boxing pre-event workflow

```
# Step 1: Load domain context
Load sports/boxing/sport-domain-boxing.md

# Step 2: Check athlete availability and form
get_availability token=[BOXI]
get_form_score token=[BOXI]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[BOXI]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.
