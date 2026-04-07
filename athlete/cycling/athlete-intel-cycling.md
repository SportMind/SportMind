# Cycling Athlete Intelligence — SportMind Skill

Player-level intelligence for cycling prediction markets and fan tokens.
Covers Grand Tour GC riders, Classics specialists, sprint and climber profiles.

**Applicable tokens / markets:** Individual rider tokens, Grand Tour stage and GC markets, Classics prediction markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_rider_form_score` | Recent race results, GC positions, stage wins | Yes |
| `get_rider_profile` | Classification specialist: climber, sprinter, time-trialist, puncheur, rouleur | Yes |
| `get_course_fit` | How well a rider's profile matches the upcoming race | Yes |
| `get_gc_standing` | Current GC position and time gaps in ongoing Grand Tour | Yes |
| `get_team_role` | Leader vs domestique status for this specific event | Yes |
| `get_injury_status` | Current crash reports, training updates | Yes |
| `get_athlete_signal_modifier` | Composite cycling modifier | Yes |

---

## Command reference

### `get_rider_profile`

**Parameters:**
- `rider_name` (required)

**Returns:**
```json
{
  "rider": "Tadej Pogačar",
  "profile": "GC_ALL_ROUNDER",
  "strengths": ["mountain climbing", "time trial", "attacking racing"],
  "weaknesses": ["team dependency limited", "sometimes over-attacks"],
  "specialist_events": ["Tour de France", "Giro d'Italia", "Il Lombardia"],
  "cobbles_rating": 62,
  "sprint_rating": 45,
  "climbing_rating": 98,
  "time_trial_rating": 94,
  "endurance_rating": 97
}
```

### `get_course_fit`

**Parameters:**
- `rider_name` (required)
- `race` (required) — race name e.g. `"Tour de France"`, `"Paris-Roubaix"`

**Returns:**
```json
{
  "rider": "Tadej Pogačar",
  "race": "Tour de France 2026",
  "course_fit_score": 96,
  "course_fit_label": "EXCEPTIONAL",
  "key_stages_favourable": ["Alpe d'Huez", "Col du Tourmalet", "ITT Stage 16"],
  "key_risks": ["Early cobble stage (Stage 5) — crash risk"],
  "course_fit_modifier": 1.20
}
```

### `get_gc_standing`

Live GC position during a Grand Tour.

**Parameters:**
- `rider_name` (required)
- `race` (required)

**Returns:**
```json
{
  "rider": "Tadej Pogačar",
  "race": "Tour de France 2026",
  "stage": 12,
  "gc_position": 1,
  "time_gap_to_2nd": "+1:24",
  "time_gap_to_3rd": "+3:45",
  "stages_remaining": 9,
  "gc_stage_types_remaining": ["mountain x3", "ITT x1", "sprint x2", "medium mountain x2"],
  "gc_status": "STRONG_LEADER",
  "gc_modifier": 1.22,
  "dnf_risk": "LOW"
}
```

### `get_team_role`

Determines if rider is leader or domestique — critical for signal validity.

**Parameters:**
- `rider_name` (required)
- `race` (required)

**Returns:**
```json
{
  "rider": "Wout van Aert",
  "race": "Tour de France 2026",
  "role": "SUPER_DOMESTIQUE",
  "team_leader": "Jonas Vingegaard",
  "own_objectives": ["Stage wins", "Green jersey points"],
  "rider_token_relevance": "MODERATE — will target stages but sacrifices GC ambitions",
  "role_modifier": 0.85
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `rider_name` (required)
- `race` (required)

**Returns:**
```json
{
  "rider": "Tadej Pogačar",
  "race": "Tour de France 2026",
  "base_signal_score": 74,
  "composite_modifier": 1.22,
  "adjusted_signal_score": 90,
  "modifier_breakdown": {
    "form": 1.18,
    "course_fit": 1.20,
    "gc_standing": 1.22,
    "team_role": 1.10,
    "injury_status": 1.00,
    "dnf_risk": 1.00
  },
  "confidence": 0.88,
  "recommendation": "STRONG BULLISH — clear leader, exceptional course fit, no injury flags",
  "key_risks": ["Cobble stage crash risk", "Weather on Alpe d'Huez stage"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| GC leader with 1:30+ gap after Alps | ×1.22 |
| Stage win specialist in correct race type | ×1.15 |
| EXCEPTIONAL course fit (>90 score) | ×1.20 |
| Confirmed team leader | ×1.10 |
| HOT form (2+ wins in last 4 races) | ×1.15 |
| Domestique role (not team leader) | ×0.85 |
| Poor course fit (<50 score) | ×0.82 |
| DNF risk HIGH (illness / crash damage) | ×0.72 |
| Confirmed DNF | 0.00 (exit immediately) |

*MIT License · SportMind · sportmind.dev*

---

## Injury intelligence

Full injury intelligence for cycling is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-cycling.md`
  
  
  
  
  
  Crash probability by stage type, Grand Tour cumulative fatigue curve, DNF prediction signals, GC leader vulnerability windows.

Load these files alongside this skill for injury-aware agent reasoning.


---

## Integration example

### Cycling pre-event workflow

```
# Step 1: Load domain context
Load sports/cycling/sport-domain-cycling.md

# Step 2: Check athlete availability and form
get_availability token=[CYCL]
get_form_score token=[CYCL]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[CYCL]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.
