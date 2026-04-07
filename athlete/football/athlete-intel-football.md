# Football / Soccer — Athlete Intelligence

Granular player-level intelligence for football fan tokens. Covers availability, form, positional output, goalkeeper metrics, set piece specialists, and head-to-head matchup data.

**Applicable tokens:** PSG, BAR, JUV, ACM, ATM, INTER, GAL, PORTO, NAP, BENFICA, SPURS, EFC, ASM, VCF, SEVILLA, RSO, LEV, BFC, UDI, SAM, ALA, AVL, AFC, GOZ, LEG, ITA

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_key_player_availability` | Availability status for all key players of a token's team | Yes |
| `get_player_form_score` | Rolling form score for a player over last N matches | Yes |
| `get_goalkeeper_rating` | GK-specific metrics: save %, post-shot xG, distribution | Yes |
| `get_attacking_output` | xG, xA, goals, assists, chances created per player | Yes |
| `get_defensive_rating` | Tackle %, aerial duels, interceptions, PPDA contribution | Yes |
| `get_set_piece_specialist` | Set piece roles, accuracy, expected goal contribution | Yes |
| `get_lineup_confirmation` | Confirmed XI status and source (official / press / rumour) | Yes |
| `get_head_to_head_matchup` | Individual player vs opponent player historical stats | Yes |
| `get_physical_load` | Fatigue index, minutes last 7 days, travel, international duty | Yes |
| `get_athlete_signal_modifier` | Composite athlete modifier for a token's current signal score | Yes |

---

## Command reference

### `get_key_player_availability`

Returns availability status for the top 5 key players on a team.

**Parameters:**
- `token` (required) — fan token symbol e.g. `BAR`, `PSG`
- `match_id` (optional) — specific upcoming match ID from `tokenintel_sports_calendar`

**Returns:**
```json
{
  "token": "BAR",
  "match": "Barcelona vs Atletico Madrid",
  "kickoff": "2026-04-05T20:00:00Z",
  "key_players": [
    {
      "name": "R. Lewandowski",
      "position": "ST",
      "status": "CONFIRMED",
      "fit_pct": 100,
      "source": "official_lineup",
      "last_match_minutes": 87,
      "notes": "Full training Thursday"
    },
    {
      "name": "P. Gavi",
      "position": "CM",
      "status": "DOUBT",
      "fit_pct": 65,
      "source": "press_conference",
      "notes": "Hamstring — manager said 50/50"
    },
    {
      "name": "F. De Jong",
      "position": "CM",
      "status": "OUT",
      "fit_pct": 0,
      "source": "official",
      "notes": "Ankle — 3 weeks"
    }
  ],
  "availability_score": 0.72,
  "signal_modifier": 0.83,
  "modifier_reason": "Two key midfielders unavailable/doubtful"
}
```

**Availability score:** 0.0–1.0. Above 0.85 = full strength. Below 0.65 = significant absences.

**Signal modifier:** Multiply against `tokenintel_signals_active` confidence score to get athlete-adjusted confidence.

---

### `get_player_form_score`

Rolling form score (0–100) for a specific player over last N matches.

**Parameters:**
- `token` (required) — fan token symbol
- `player_name` (required) — player name string
- `matches` (optional) — number of matches to average over (default: 5, max: 20)
- `competition` (optional) — filter by competition type: `all`, `league`, `ucl`, `domestic_cup`

**Returns:**
```json
{
  "player": "K. Mbappé",
  "token": "PSG",
  "form_score": 88,
  "form_label": "HOT",
  "last_5_matches": [
    { "opponent": "Lyon", "minutes": 90, "goals": 2, "assists": 1, "xG": 1.8, "xA": 0.9, "rating": 9.1 },
    { "opponent": "Nice", "minutes": 90, "goals": 1, "assists": 0, "xG": 0.9, "xA": 0.3, "rating": 7.4 },
    { "opponent": "Marseille", "minutes": 78, "goals": 0, "assists": 2, "xG": 0.6, "xA": 1.4, "rating": 7.8 },
    { "opponent": "Lens", "minutes": 90, "goals": 1, "assists": 1, "xG": 1.1, "xA": 0.7, "rating": 8.2 },
    { "opponent": "Monaco", "minutes": 90, "goals": 2, "assists": 0, "xG": 1.5, "xA": 0.2, "rating": 8.7 }
  ],
  "averages": {
    "goals_per_90": 1.2,
    "xG_per_90": 1.18,
    "xA_per_90": 0.7,
    "minutes_per_match": 87.6,
    "avg_rating": 8.24
  },
  "signal_boost": 1.20,
  "boost_reason": "Player scoring above xG expectation — hot form"
}
```

**Form labels:** COLD (0–39), POOR (40–54), AVERAGE (55–69), GOOD (70–84), HOT (85–100)

---

### `get_goalkeeper_rating`

Goalkeeper-specific deep metrics. Critical for defensive token signals — a backup GK is a -20% modifier.

**Parameters:**
- `token` (required)
- `matches` (optional, default: 10)

**Returns:**
```json
{
  "token": "JUV",
  "goalkeeper": {
    "name": "W. Szczesny",
    "status": "CONFIRMED_STARTER",
    "backup": "C. Perin",
    "last_10_matches": {
      "save_pct": 74.2,
      "post_shot_xG_conceded": 8.1,
      "actual_goals_conceded": 6,
      "xG_prevented": 2.1,
      "clean_sheets": 4,
      "high_danger_save_pct": 61.0,
      "distribution_accuracy_pct": 79.3,
      "sweeper_actions": 14,
      "penalty_saves": 1,
      "errors_leading_to_goal": 0
    },
    "gk_rating_score": 81,
    "is_starter": true,
    "backup_quality_delta": -18
  },
  "signal_modifier": 1.05,
  "modifier_reason": "Starting GK above average form, xG prevented positive"
}
```

**backup_quality_delta:** Points difference between starter and backup rating. -18 means backup is significantly weaker — if starter is ruled out, apply additional -0.18 modifier.

---

### `get_attacking_output`

xG, xA, chance creation and scoring rates for attacking players.

**Parameters:**
- `token` (required)
- `position` (optional) — filter: `ST`, `LW`, `RW`, `AM`, `all`
- `matches` (optional, default: 10)

**Returns:**
```json
{
  "token": "ACM",
  "attacking_players": [
    {
      "name": "R. Leão",
      "position": "LW",
      "status": "CONFIRMED",
      "xG_per_90": 0.42,
      "xA_per_90": 0.38,
      "goals_last_10": 5,
      "assists_last_10": 4,
      "big_chance_conversion_pct": 48.0,
      "shot_on_target_pct": 52.3,
      "dribble_success_pct": 61.0,
      "progressive_carries_per_90": 4.8,
      "penalty_area_touches_per_90": 6.2,
      "form_score": 79,
      "form_label": "GOOD"
    }
  ],
  "team_xG_per_90": 1.82,
  "team_goals_per_90": 1.60,
  "xG_overperformance": -0.22,
  "set_piece_xG_contribution_pct": 28.0,
  "signal_modifier": 1.08
}
```

---

### `get_defensive_rating`

Defensive player metrics. Used to assess clean sheet probability modifiers.

**Parameters:**
- `token` (required)
- `position` (optional) — `CB`, `LB`, `RB`, `CDM`, `all`
- `matches` (optional, default: 10)

**Returns:**
```json
{
  "token": "ATM",
  "defensive_players": [
    {
      "name": "J. Giménez",
      "position": "CB",
      "status": "CONFIRMED",
      "tackle_success_pct": 72.0,
      "aerial_duel_win_pct": 68.0,
      "interceptions_per_90": 2.1,
      "blocks_per_90": 1.4,
      "dribbled_past_per_90": 0.8,
      "ball_recoveries_per_90": 7.2,
      "PPDA_contribution": 9.4,
      "defensive_rating_score": 84
    }
  ],
  "team_defensive_rating": 78,
  "clean_sheet_probability_modifier": 1.12,
  "signal_modifier": 1.10,
  "modifier_reason": "Strong defensive unit at full strength — Atletico style"
}
```

---

### `get_set_piece_specialist`

Set piece roles, delivery accuracy, and xG contribution. Critical for teams where 30%+ of goals come from dead balls.

**Parameters:**
- `token` (required)
- `type` (optional) — `corners`, `free_kicks`, `penalties`, `all`

**Returns:**
```json
{
  "token": "PSG",
  "set_piece_specialists": {
    "corner_taker": { "name": "F. Ruiz", "delivery_accuracy_pct": 38.0, "xG_generated_per_corner": 0.09 },
    "free_kick_taker": { "name": "K. Mbappé", "free_kick_goals": 3, "free_kick_xG": 0.14, "on_target_pct": 45.0 },
    "penalty_taker": { "name": "K. Mbappé", "penalties_taken": 8, "scored": 7, "conversion_pct": 87.5 }
  },
  "set_piece_goals_pct": 31.0,
  "set_piece_xG_per_match": 0.52,
  "set_piece_dependency_rating": "HIGH",
  "signal_modifier": 1.05,
  "modifier_note": "If set piece taker is absent, apply additional -0.12 to modifier"
}
```

---

### `get_lineup_confirmation`

Real-time lineup confirmation status. The most important pre-match signal — fires at -1h.

**Parameters:**
- `token` (required)
- `match_id` (optional)

**Returns:**
```json
{
  "token": "SPURS",
  "match": "Tottenham vs Arsenal",
  "kickoff": "2026-04-06T16:30:00Z",
  "confirmation_status": "CONFIRMED",
  "confirmed_at": "2026-04-06T15:28:00Z",
  "source": "official_prematch",
  "minutes_before_kickoff": 62,
  "starting_xi": [
    { "name": "A. Forster", "position": "GK", "key_player": false },
    { "name": "P. Porro", "position": "RB", "key_player": false },
    { "name": "C. Romero", "position": "CB", "key_player": true },
    { "name": "M. van de Ven", "position": "CB", "key_player": true },
    { "name": "D. Udogie", "position": "LB", "key_player": false },
    { "name": "Y. Bissouma", "position": "CM", "key_player": false },
    { "name": "J. Maddison", "position": "AM", "key_player": true },
    { "name": "D. Kulusevski", "position": "RW", "key_player": true },
    { "name": "H. Son", "position": "LW", "key_player": true },
    { "name": "B. Johnson", "position": "ST", "key_player": true },
    { "name": "L. Bergvall", "position": "CM", "key_player": false }
  ],
  "key_players_starting": 5,
  "key_players_expected": 5,
  "availability_score": 1.0,
  "signal_modifier": 1.15,
  "modifier_reason": "Full strength lineup confirmed — maximum modifier"
}
```

**Confirmation statuses:** `UNCONFIRMED`, `RUMOURED`, `PRESS_HINT`, `PARTIALLY_CONFIRMED`, `CONFIRMED`

**Agent note:** Agents should wait for `CONFIRMED` status before applying maximum modifier. Use `PRESS_HINT` modifier (0.95) as interim.

---

### `get_head_to_head_matchup`

Individual player vs individual opponent player stats — the deepest signal layer.

**Parameters:**
- `token` (required) — attacking team token
- `player_name` (required)
- `opponent_token` (required) — defending team token
- `opponent_player` (optional) — specific defender to match against

**Returns:**
```json
{
  "matchup": "K. Mbappé vs A. Rudiger",
  "token": "PSG",
  "opponent_token": "GAL",
  "appearances_together": 6,
  "mbappé_stats_vs_rudiger": {
    "goals": 3,
    "assists": 1,
    "dribbles_attempted": 18,
    "dribbles_successful": 11,
    "dribble_success_pct": 61.1,
    "shots": 14,
    "shots_on_target": 9,
    "xG_in_matchup": 2.8,
    "times_fouled": 7
  },
  "rudiger_defensive_record_vs_mbappé": {
    "successful_tackles": 4,
    "aerial_duels_won": 3,
    "times_dribbled_past": 11
  },
  "matchup_verdict": "MBAPPÉ_EDGE",
  "advantage_score": 72,
  "signal_modifier": 1.18,
  "modifier_reason": "Strong historical advantage in this specific matchup"
}
```

---

### `get_physical_load`

Fatigue and load management signal. High minutes + international duty = degraded performance probability.

**Parameters:**
- `token` (required)
- `player_name` (optional) — specific player, or all key players if omitted

**Returns:**
```json
{
  "token": "BAR",
  "physical_load_summary": [
    {
      "name": "R. Lewandowski",
      "minutes_last_7_days": 180,
      "matches_last_14_days": 3,
      "international_duty": false,
      "travel_km_last_7_days": 2400,
      "fatigue_index": 0.72,
      "fatigue_label": "MODERATE",
      "performance_degradation_risk": "LOW"
    },
    {
      "name": "P. Gavi",
      "minutes_last_7_days": 270,
      "matches_last_14_days": 4,
      "international_duty": true,
      "travel_km_last_7_days": 8200,
      "fatigue_index": 0.91,
      "fatigue_label": "HIGH",
      "performance_degradation_risk": "HIGH"
    }
  ],
  "team_fatigue_index": 0.76,
  "signal_modifier": 0.92,
  "modifier_reason": "Key midfielder at high fatigue after international duty"
}
```

**Fatigue labels:** LOW (0.0–0.4), MODERATE (0.4–0.7), HIGH (0.7–0.85), CRITICAL (0.85–1.0)

---

### `get_athlete_signal_modifier`

Master composite modifier — combines all athlete signals into a single multiplier for the team signal score.

**Parameters:**
- `token` (required)
- `match_id` (optional) — defaults to next upcoming match

**Returns:**
```json
{
  "token": "BAR",
  "match": "Barcelona vs Atletico Madrid",
  "base_signal_score": 72,
  "athlete_modifier": 0.87,
  "adjusted_signal_score": 63,
  "adjusted_direction": "BULLISH",
  "modifier_breakdown": {
    "availability_modifier": 0.83,
    "form_modifier": 1.05,
    "goalkeeper_modifier": 1.02,
    "physical_load_modifier": 0.92,
    "set_piece_modifier": 1.00,
    "lineup_confirmation_modifier": 0.95
  },
  "key_risks": [
    "Gavi doubtful — key press trigger absent",
    "De Jong confirmed out — midfield depth reduced",
    "Lineup not yet confirmed — use interim modifier only"
  ],
  "signal_confidence": 0.78,
  "recommendation": "HOLD — wait for confirmed lineup before entry. Re-evaluate at -1h."
}
```

---

## Integration example

### Full pre-match athlete-aware workflow

```
# Step 1: Get base team signal
tokenintel_signals_active token=BAR

# Step 2: Check athlete layer
get_key_player_availability token=BAR
get_lineup_confirmation token=BAR
get_player_form_score token=BAR player_name="R. Lewandowski" matches=5
get_goalkeeper_rating token=BAR

# Step 3: Get composite modifier
get_athlete_signal_modifier token=BAR

# Step 4: Apply modifier and decide
# If adjusted_signal_score >= 65 AND lineup CONFIRMED → entry
# If lineup UNCONFIRMED → wait
# If adjusted_signal_score < 55 → skip regardless of team signal
```

### Autopilot integration

```json
{
  "template": "athlete_aware_matchday",
  "params": {
    "token": "BAR",
    "min_athlete_adjusted_score": 65,
    "require_lineup_confirmed": true,
    "min_key_player_availability": 0.80,
    "max_fatigue_index": 0.85,
    "form_window": 5
  }
}
```

---

## Injury intelligence

Full injury intelligence for football is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-football.md`
  Squad depth by position, set piece specialist loss, CB partnership disruption, manager language decoder, international duty injury, congested fixture risk.
  
  
  
  
  

Load these files alongside this skill for injury-aware agent reasoning.

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

