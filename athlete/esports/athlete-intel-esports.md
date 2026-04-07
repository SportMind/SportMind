# Esports — Athlete Intelligence

Player-level intelligence for esports fan tokens on Chiliz. Covers CS2, League of Legends, Dota 2, and Valorant. Directly applicable to **NAVI**, **OG**, and **DZG** tokens.

**Applicable tokens:** NAVI, OG, DZG (Dignitas), and any future esports tokens on Chiliz Chain.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_player_availability` | Roster status, stand-in flags, bootcamp, visa issues | Yes |
| `get_player_stats` | KDA, damage, rating, role-specific metrics | Yes |
| `get_role_performance` | Position/role mastery and meta alignment | Yes |
| `get_team_form` | Recent tournament results, map win rates | Yes |
| `get_meta_readiness` | Current patch alignment, agent/hero/champion pool | Yes |
| `get_head_to_head` | Team vs team and player vs player historical | Yes |
| `get_player_form_score` | Rolling form score over last N events | Yes |
| `get_draft_intelligence` | Pick/ban tendencies, bans-against data | Yes |

---

## Command reference

### `get_player_availability`

**Parameters:**
- `token` (required) — `NAVI`, `OG`, `DZG`
- `event_id` (optional)

**Returns:**
```json
{
  "token": "NAVI",
  "event": "IEM Katowice 2026",
  "roster_status": [
    {
      "name": "s1mple",
      "role": "AWP / Entry",
      "status": "ACTIVE",
      "is_stand_in": false,
      "visa_issues": false,
      "bootcamp_completed": true,
      "recent_break": false,
      "performance_contract_pressure": false
    },
    {
      "name": "b1t",
      "role": "Entry Fragger",
      "status": "ACTIVE",
      "is_stand_in": false,
      "visa_issues": false,
      "bootcamp_completed": true,
      "recent_break": false,
      "performance_contract_pressure": false
    }
  ],
  "stand_ins_count": 0,
  "roster_stability_score": 96,
  "signal_modifier": 1.10,
  "modifier_reason": "Full roster, completed bootcamp, no logistical issues"
}
```

**Stand-in flag:** Any stand-in apply -0.20 minimum modifier. Tier-1 stand-in reduces to -0.10.

---

### `get_player_stats`

**Parameters:**
- `token` (required)
- `player_name` (optional) — specific player or all roster
- `game` (optional) — `cs2`, `lol`, `dota2`, `valorant` (auto-detected from token if omitted)
- `events` (optional, default: 5)

**Returns for CS2:**
```json
{
  "token": "NAVI",
  "player": "s1mple",
  "game": "cs2",
  "last_5_events": {
    "rating_hltv": 1.38,
    "KDA": 1.82,
    "ADR": 94.2,
    "KAST_pct": 79.0,
    "HS_pct": 48.0,
    "opening_duel_win_pct": 61.0,
    "clutch_win_pct_1v1": 74.0,
    "clutch_win_pct_1v2": 38.0,
    "AWP_kills_per_map": 14.2,
    "first_kills_per_map": 4.8,
    "maps_played": 22,
    "overall_rating": 1.38
  },
  "form_score": 89,
  "form_label": "HOT",
  "signal_modifier": 1.15
}
```

**Returns for League of Legends:**
```json
{
  "token": "OG",
  "player": "Inspired",
  "game": "lol",
  "last_5_events": {
    "KDA": 5.8,
    "damage_per_min": 628,
    "CS_per_min": 5.2,
    "vision_score_per_min": 1.4,
    "first_blood_participation_pct": 68.0,
    "objective_control_pct": 72.0,
    "champion_pool_size": 12,
    "win_rate_on_meta_picks": 67.0,
    "solo_kill_rate": 2.1,
    "maps_played": 18
  },
  "form_score": 83,
  "form_label": "GOOD"
}
```

---

### `get_meta_readiness`

How well a team/player is aligned with the current game patch.

**Parameters:**
- `token` (required)
- `game` (optional)
- `patch` (optional — defaults to current live patch)

**Returns:**
```json
{
  "token": "NAVI",
  "game": "cs2",
  "current_patch": "1.39.6",
  "meta_readiness": {
    "utility_style_alignment": "HIGH",
    "aggression_meta_fit": "HIGH",
    "AWP_meta_strength": "STRONG",
    "map_pool_meta_fit": {
      "Mirage": "STRONG",
      "Inferno": "MODERATE",
      "Ancient": "WEAK",
      "Nuke": "STRONG",
      "Overpass": "MODERATE"
    },
    "scrim_win_rate_estimate": 0.64,
    "bootcamp_patch_preparation": true
  },
  "meta_readiness_score": 81,
  "signal_modifier": 1.08,
  "modifier_reason": "Team's style aligns with current patch — AWP-heavy meta favours NAVI"
}
```

---

### `get_draft_intelligence`

Pick/ban patterns and counter-draft data. Highest value in LoL, Dota2, Valorant.

**Parameters:**
- `token` (required)
- `opponent_token` (optional)
- `events` (optional, default: 10)

**Returns:**
```json
{
  "token": "OG",
  "game": "lol",
  "draft_patterns": {
    "most_picked_champions": ["Aatrox", "Azir", "Vi", "Tristana"],
    "most_banned_against_OG": ["Zed", "LeBlanc", "Katarina"],
    "first_pick_win_rate": 0.62,
    "second_pick_win_rate": 0.54,
    "comfort_picks": ["Faker-style Azir", "Twisted Fate"],
    "weak_side_adaptability": "HIGH",
    "blind_pick_comfort": "MODERATE"
  },
  "opponent_draft_tendencies": null,
  "draft_edge_score": 72,
  "signal_modifier": 1.05
}
```

---

### `get_head_to_head`

**Parameters:**
- `token` (required)
- `opponent_token` (required)
- `events` (optional, default: 10)
- `game` (optional)

**Returns:**
```json
{
  "token": "NAVI",
  "opponent": "OG",
  "game": "cs2",
  "h2h_record": { "NAVI_wins": 7, "OG_wins": 3, "maps_played": 26 },
  "map_h2h": {
    "Mirage": { "NAVI_wins": 5, "OG_wins": 1 },
    "Inferno": { "NAVI_wins": 3, "OG_wins": 2 },
    "Overpass": { "NAVI_wins": 2, "OG_wins": 1 }
  },
  "last_5_meetings": [
    { "event": "ESL One 2025", "winner": "NAVI", "score": "2-0" },
    { "event": "IEM 2025", "winner": "NAVI", "score": "2-1" },
    { "event": "BLAST 2024", "winner": "OG", "score": "2-1" },
    { "event": "IEM 2024", "winner": "NAVI", "score": "2-0" },
    { "event": "ESL 2024", "winner": "NAVI", "score": "2-1" }
  ],
  "h2h_win_rate_navi": 0.70,
  "signal_modifier": 1.12,
  "modifier_reason": "Strong H2H record — NAVI historically dominant vs OG"
}
```

---

### `get_player_form_score`

**Parameters:**
- `token` (required)
- `player_name` (required)
- `events` (optional, default: 5)

**Returns:**
```json
{
  "token": "NAVI",
  "player": "s1mple",
  "form_score": 91,
  "form_label": "HOT",
  "last_5_event_ratings": [1.41, 1.35, 1.38, 1.29, 1.44],
  "trend": "STABLE_HIGH",
  "mvp_awards_last_5": 2,
  "signal_modifier": 1.18,
  "modifier_reason": "Consistently above 1.35 rating — world-class form"
}
```

---

## Integration example

### Esports token pre-match workflow

```
# NAVI playing at major tournament
tokenintel_signals_active token=NAVI

get_player_availability token=NAVI event_id="IEM_KATOWICE_2026"
get_team_form token=NAVI events=5
get_meta_readiness token=NAVI
get_head_to_head token=NAVI opponent_token=OG
get_player_form_score token=NAVI player_name="s1mple" events=5

# Composite
get_athlete_signal_modifier token=NAVI

# Decision
# Full roster + hot form + meta aligned = apply 1.10-1.20 boost
# Stand-in detected = reduce confidence by 0.20
```

## Modifier reference

### Signal modifier table for esports

| Condition | Modifier |
|---|---|
| Full roster, bootcamp complete | 1.10 |
| Star player HOT form (rating >1.35) | 1.15 |
| Stand-in (any role) | 0.80 |
| Star player COLD form (rating <1.10) | 0.85 |
| Meta misaligned (patch counters team style) | 0.88 |
| Strong H2H advantage (>65% win rate) | 1.12 |
| Coach change this event | 0.92 |
| Travel / visa issues | 0.85 |
