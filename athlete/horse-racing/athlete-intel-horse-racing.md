# Horse Racing Athlete Intelligence — SportMind Skill

Player-level intelligence for horse racing prediction markets.
The "athlete" in horse racing is the horse-jockey combination — inseparable for signal purposes.
Covers form, going preference, course record, trainer signals, and draw position.

**Applicable tokens / markets:** Horse racing prediction markets, ante-post tournament markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_horse_form` | Recent race results, speed figures, finishing positions | Yes |
| `get_going_preference` | Going type the horse performs best on | Yes |
| `get_course_distance_record` | Course and distance (C&D) history — strongest predictor | Yes |
| `get_draw_position_impact` | Stall draw advantage/disadvantage at specific course | Yes |
| `get_trainer_jockey_signals` | Trainer form at meeting, jockey booking significance | Yes |
| `get_equipment_changes` | Blinkers, tongue tie, first-time equipment signals | Yes |
| `get_athlete_signal_modifier` | Composite racing modifier | Yes |

---

## Command reference

### `get_horse_form`

**Parameters:**
- `horse_name` (required)
- `runs` (optional, default: 6)

**Returns:**
```json
{
  "horse": "Constitution Hill",
  "trainer": "Nicky Henderson",
  "jockey": "Nico de Boinville",
  "age": 8,
  "form_string": "11111F1",
  "recent_runs": [
    { "date": "2026-03-13", "race": "Champion Hurdle", "finish": 1, "sp": "1/4F", "going": "Good" },
    { "date": "2025-11-22", "race": "Fighting Fifth Hurdle", "finish": 1, "sp": "1/5F", "going": "Soft" }
  ],
  "rating": 176,
  "speed_figure_avg": 182,
  "form_score": 95,
  "form_label": "DOMINANT",
  "form_modifier": 1.20
}
```

### `get_going_preference`

**Parameters:**
- `horse_name` (required)

**Returns:**
```json
{
  "horse": "Constitution Hill",
  "going_preference": "Good_to_Soft",
  "performance_by_going": {
    "Firm": { "runs": 0, "wins": 0 },
    "Good_to_Firm": { "runs": 2, "wins": 1, "win_pct": 50 },
    "Good": { "runs": 4, "wins": 4, "win_pct": 100 },
    "Good_to_Soft": { "runs": 5, "wins": 5, "win_pct": 100 },
    "Soft": { "runs": 3, "wins": 2, "win_pct": 67 },
    "Heavy": { "runs": 1, "wins": 0, "win_pct": 0 }
  },
  "declared_going": "Good_to_Soft",
  "going_match": "OPTIMAL",
  "going_modifier": 1.10
}
```

### `get_course_distance_record`

The single most predictive variable in horse racing.

**Parameters:**
- `horse_name` (required)
- `course` (required)
- `distance` (optional)

**Returns:**
```json
{
  "horse": "Constitution Hill",
  "course": "Cheltenham",
  "distance": "2m",
  "course_distance_record": {
    "runs": 5,
    "wins": 4,
    "places": 1,
    "win_pct": 80,
    "best_time": "3m48.2s"
  },
  "cd_label": "PROVEN_CD_WINNER",
  "cd_modifier": 1.18,
  "note": "4 wins from 5 at Cheltenham over 2m — strongest possible course form signal"
}
```

### `get_trainer_jockey_signals`

**Parameters:**
- `trainer` (required)
- `meeting` (required) — e.g. `"Cheltenham Festival"`
- `jockey` (optional)

**Returns:**
```json
{
  "trainer": "Willie Mullins",
  "meeting": "Cheltenham Festival 2026",
  "trainer_stats_at_meeting": {
    "winners_this_festival": 8,
    "runners_this_festival": 24,
    "strike_rate": 0.333,
    "normal_strike_rate": 0.28
  },
  "festival_form_label": "HOT — above usual strike rate",
  "trainer_modifier": 1.12,
  "jockey": "Paul Townend",
  "jockey_retains_ride": true,
  "jockey_modifier": 1.05
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `horse_name` (required)
- `race` (required)

**Returns:**
```json
{
  "horse": "Constitution Hill",
  "race": "Champion Hurdle 2026",
  "base_signal_score": 72,
  "composite_modifier": 1.22,
  "adjusted_signal_score": 88,
  "modifier_breakdown": {
    "form": 1.20,
    "going_match": 1.10,
    "course_distance_record": 1.18,
    "trainer_form": 1.12,
    "jockey_booking": 1.05,
    "draw_position": 1.00
  },
  "confidence": 0.88,
  "recommendation": "STRONG BULLISH — dominant form, optimal going, proven at course and distance",
  "key_risks": ["Opponent Impaire Et Fier improving rapidly", "Going could dry overnight"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Proven C&D winner (3+ wins at course/distance) | ×1.18 |
| Optimal going match | ×1.10 |
| Trainer at festival in HOT form | ×1.12 |
| Dominant recent form (all-wins last 4) | ×1.20 |
| Retained leading jockey | ×1.05 |
| First time at course | ×0.90 |
| Going against preference (2+ categories wrong) | ×0.82 |
| Disadvantaged draw (Chester high draw) | ×0.80 |
| Non-runner (injury / going) | ×0.00 — immediate exit |

*MIT License · SportMind · sportmind.dev*

---

## Injury intelligence

Full injury intelligence for horse-racing is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-horse-racing.md`
  
  
  
  
  Pre-race vet signals, morning workout intelligence, paddock visual assessment, trainer language decoder, going conditions and injury interaction.
  

Load these files alongside this skill for injury-aware agent reasoning.


---

## Integration example

### Horse Racing pre-event workflow

```
# Step 1: Load domain context
Load sports/horse-racing/sport-domain-horse-racing.md

# Step 2: Check athlete availability and form
get_availability token=[HORS]
get_form_score token=[HORS]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[HORS]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.
