# Mixed Martial Arts (MMA) — Athlete Intelligence

Fighter-level intelligence for MMA events (UFC, PFL, Bellator). Covers striking, grappling, finishing tendencies, round-by-round profiles, fight camp signals, and physical matchup data. Used to adjust signal scores for fighter fan tokens if listed on Chiliz, and for sports betting signal enrichment.

**Applicable tokens:** Fighter tokens (if listed). Also used as enrichment layer for combat sports market signals.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_fighter_availability` | Camp status, weight cut, replacement flag, injury | Yes |
| `get_striking_profile` | Volume, accuracy, power, head/body/leg split | Yes |
| `get_grappling_profile` | Takedowns, submissions, control time, scrambles | Yes |
| `get_finishing_tendency` | KO/TKO %, submission %, decision %, by round | Yes |
| `get_round_profile` | Output by round — pace, fade, late surge | Yes |
| `get_fight_camp_signals` | Gym, coach, weight cut history, time off | Yes |
| `get_physical_matchup` | Reach, height, stance, age curve analysis | Yes |
| `get_style_matchup` | Striker vs wrestler, style clash historical data | Yes |
| `get_fighter_form_score` | Rolling form score over last N fights | Yes |

---

## Command reference

### `get_fighter_availability`

**Parameters:**
- `fighter_name` (required)
- `event_id` (optional)

**Returns:**
```json
{
  "fighter": "Islam Makhachev",
  "event": "UFC 315",
  "fight_date": "2026-05-02",
  "availability": {
    "status": "CONFIRMED",
    "is_late_replacement": false,
    "days_notice": 84,
    "weight_class": "Lightweight",
    "walking_weight_kg": 80,
    "fight_weight_kg": 70.3,
    "weight_cut_severity": "MODERATE",
    "weight_cut_history_issues": false,
    "last_fight_date": "2025-11-15",
    "days_off": 168,
    "injury_flags": [],
    "camp_status": "FULL_CAMP"
  },
  "signal_modifier": 1.05,
  "modifier_reason": "Full camp, no weight cut issues, adequate rest"
}
```

**Weight cut severity:** MINIMAL (<5kg), MODERATE (5–8kg), SEVERE (8–12kg), EXTREME (>12kg)

**Late replacement:** Any fight with <3 weeks notice. Apply -0.15 modifier minimum.

---

### `get_striking_profile`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: 5, max: 20)
- `opponent_tier` (optional) — `top5`, `top15`, `all`

**Returns:**
```json
{
  "fighter": "Alex Pereira",
  "striking_profile": {
    "sig_strikes_per_min": 5.82,
    "sig_strike_accuracy_pct": 54.0,
    "sig_strike_defence_pct": 61.0,
    "head_pct": 52.0,
    "body_pct": 28.0,
    "leg_pct": 20.0,
    "distance_pct": 68.0,
    "clinch_pct": 22.0,
    "ground_pct": 10.0,
    "knockdown_rate_per_100": 8.4,
    "avg_combo_length": 2.1,
    "jab_to_power_ratio": 0.38,
    "strike_defence_pct": 61.0,
    "absorbed_per_min": 3.12
  },
  "striking_score": 91,
  "striking_label": "ELITE",
  "ko_threat_rating": 95
}
```

---

### `get_grappling_profile`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: 5)

**Returns:**
```json
{
  "fighter": "Islam Makhachev",
  "grappling_profile": {
    "takedown_attempts_per_15": 6.8,
    "takedown_success_pct": 61.0,
    "takedown_defence_pct": 83.0,
    "submission_attempts_per_15": 2.4,
    "submission_win_rate": 0.36,
    "control_time_per_fight_min": 8.4,
    "guard_passes_per_fight": 3.1,
    "back_takes_per_fight": 1.8,
    "scramble_success_pct": 74.0,
    "preferred_submissions": ["arm bar", "rear naked choke", "D'arce"],
    "takedown_entries": ["double leg", "body lock", "ankle pick"],
    "cage_takedown_pct": 42.0
  },
  "grappling_score": 97,
  "grappling_label": "ELITE",
  "submission_threat_rating": 88,
  "td_defence_rating": 91
}
```

---

### `get_finishing_tendency`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: all pro fights)

**Returns:**
```json
{
  "fighter": "Alex Pereira",
  "record": "12-2",
  "finish_rate_pct": 83.0,
  "finish_breakdown": {
    "KO_TKO_pct": 75.0,
    "submission_pct": 8.0,
    "decision_pct": 17.0
  },
  "finish_by_round": {
    "round_1_pct": 42.0,
    "round_2_pct": 25.0,
    "round_3_pct": 16.0,
    "round_4_pct": 8.0,
    "round_5_pct": 9.0
  },
  "avg_fight_time_min": 8.4,
  "most_common_finish": "KO/TKO — head kick",
  "last_5_finishes": ["KO R1", "KO R2", "Decision", "KO R1", "TKO R3"],
  "finishing_score": 92,
  "signal_note": "High R1/R2 finish rate — price impact likely early in event"
}
```

---

### `get_round_profile`

Round-by-round output — identifies faders, slow starters, and late finishers.

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: 10)

**Returns:**
```json
{
  "fighter": "Dustin Poirier",
  "round_profile": {
    "round_1": { "sig_strikes_per_min": 6.2, "takedown_attempts": 0.8, "pace_index": 88 },
    "round_2": { "sig_strikes_per_min": 5.8, "takedown_attempts": 1.2, "pace_index": 82 },
    "round_3": { "sig_strikes_per_min": 4.9, "takedown_attempts": 0.6, "pace_index": 71 },
    "round_4": { "sig_strikes_per_min": 4.1, "takedown_attempts": 0.4, "pace_index": 62 },
    "round_5": { "sig_strikes_per_min": 3.8, "takedown_attempts": 0.3, "pace_index": 57 }
  },
  "pace_degradation_pct": 39.0,
  "profile_label": "EARLY_PRESSURE_FADER",
  "cardio_rating": 64,
  "signal_note": "Performance drops significantly after R2 — opponent with strong cardio has advantage in 5-round fights"
}
```

**Profile labels:** `IRON_CARDIO` (consistent), `SLOW_STARTER` (improves by R2), `EARLY_PRESSURE_FADER` (drops off), `LATE_SURGE` (strongest in late rounds)

---

### `get_fight_camp_signals`

**Parameters:**
- `fighter_name` (required)

**Returns:**
```json
{
  "fighter": "Sean O'Malley",
  "camp_signals": {
    "primary_gym": "MMA Lab",
    "camp_change_last_fight": false,
    "coach": "Tim Welch",
    "coach_quality_rating": 88,
    "sparring_partners_tier": "HIGH",
    "media_activity": "NORMAL",
    "public_controversy_flag": false,
    "weight_cut_plan": "STANDARD",
    "previous_weight_cut_issues": [
      { "event": "UFC 299", "issue": "Missed weight by 0.5lb", "severity": "MINOR" }
    ],
    "camp_length_days": 92,
    "time_off_between_fights_days": 201,
    "post_KO_loss_flag": false,
    "chin_durability_rating": 72,
    "knockdowns_received_career": 4
  },
  "camp_quality_score": 84,
  "signal_modifier": 1.02,
  "modifier_reason": "Stable camp, experienced coaching, no weight issues"
}
```

---

### `get_physical_matchup`

**Parameters:**
- `fighter_a` (required)
- `fighter_b` (required)

**Returns:**
```json
{
  "matchup": "Islam Makhachev vs Dustin Poirier",
  "physical_comparison": {
    "height_diff_cm": 2,
    "reach_diff_cm": -3,
    "reach_advantage": "POIRIER",
    "stance_matchup": "Orthodox vs Orthodox",
    "age_makhachev": 29,
    "age_poirier": 35,
    "age_curve_note": "Poirier past statistical prime for finishing ability (peaks 26–31)"
  },
  "historical_stance_matchup": {
    "orthodox_vs_orthodox_win_rate_favourite": 0.61
  },
  "physical_edge": "MAKHACHEV",
  "physical_edge_score": 68,
  "signal_modifier": 1.08
}
```

---

### `get_style_matchup`

Historical data on how style clashes resolve.

**Parameters:**
- `fighter_a` (required)
- `fighter_b` (required)
- `fights` (optional, default: 10 for each fighter)

**Returns:**
```json
{
  "matchup": "Alex Pereira vs Jiri Prochazka",
  "style_a": "STRIKER_POWER",
  "style_b": "STRIKER_BRAWLER",
  "style_clash": "STRIKER_VS_STRIKER",
  "historical_outcomes": {
    "striker_vs_striker_finish_rate_pct": 81.0,
    "avg_fight_time_min": 6.2,
    "ko_tko_pct": 73.0
  },
  "key_factors": [
    "Both fighters aggressive — likely no decision",
    "Pereira's accuracy advantage (54% vs 44%)",
    "Prochazka's unorthodox movement is historical equaliser",
    "Low probability of R4/R5 — expect early finish"
  ],
  "matchup_verdict": "PEREIRA_SLIGHT_EDGE",
  "confidence": 0.62,
  "signal_modifier": 1.10
}
```

---

### `get_fighter_form_score`

**Parameters:**
- `fighter_name` (required)
- `fights` (optional, default: 5)

**Returns:**
```json
{
  "fighter": "Islam Makhachev",
  "form_score": 94,
  "form_label": "DOMINANT",
  "last_5_fights": [
    { "opponent": "Arman Tsarukyan", "result": "W_UD", "performance_rating": 88 },
    { "opponent": "Dustin Poirier", "result": "W_SUB_R3", "performance_rating": 92 },
    { "opponent": "Alexander Volkanovski", "result": "W_UD", "performance_rating": 91 },
    { "opponent": "Alexander Volkanovski", "result": "W_KO_R1", "performance_rating": 96 },
    { "opponent": "Charles Oliveira", "result": "W_SUB_R2", "performance_rating": 94 }
  ],
  "win_streak": 12,
  "finish_streak": 2,
  "signal_modifier": 1.18,
  "modifier_reason": "Long win streak, recent finishes, consistent top-level performances"
}
```

---

## Injury intelligence

Full injury intelligence for mma is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-mma.md`
  
  Fight camp signals, weight cut as injury proxy, late replacement consequences, in-fight injury signals, career stage interaction.
  
  
  
  

Load these files alongside this skill for injury-aware agent reasoning.


---

## Integration example

### MMA pre-event workflow

```
# Step 1: Load domain context
Load sports/mma/sport-domain-mma.md

# Step 2: Check athlete availability and form
get_availability token=[MMA]
get_form_score token=[MMA]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[MMA]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.

## Modifier reference

| Condition | Modifier |
|---|---|
| All key players/athletes confirmed fit, top form | ×1.20 |
| Key player fit, good recent form | ×1.10 |
| Neutral — average form, full availability | ×1.00 |
| Minor concern — fatigue or unconfirmed lineup element | ×0.92 |
| Significant concern — key player doubt | ×0.82 |
| Key player ruled out — critical position | ×0.70 |

### Knockout conditions
| Condition | Floor modifier |
|---|---|
| Star player/athlete confirmed out | 0.70 |
| Multiple key positions unavailable | 0.65 |

*Ranges consistent with `core/core-athlete-modifier-system.md`*

