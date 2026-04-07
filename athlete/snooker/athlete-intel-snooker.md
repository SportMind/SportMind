# Snooker Athlete Intelligence — SportMind Skill

Player-level intelligence for snooker fan tokens and prediction markets.

**Applicable tokens / markets:** Individual player tokens, World Championship markets, Triple Crown prediction markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_player_form_score` | Recent tournament results, ranking event wins | Yes |
| `get_crucible_record` | Venue-specific Crucible history — separate from general form | Yes |
| `get_world_ranking_status` | Current ranking, ranking trajectory, top-16 status | Yes |
| `get_break_building_stats` | Century break rate, maximum breaks, average break | Yes |
| `get_pressure_record` | Final frame win rate, deciding frame record | Yes |
| `get_athlete_signal_modifier` | Composite snooker modifier | Yes |

---

## Command reference

### `get_crucible_record`

**Parameters:**
- `player_name` (required)
- `years` (optional, default: all)

**Returns:**
```json
{
  "player": "Ronnie O'Sullivan",
  "crucible_record": {
    "appearances": 31,
    "wins": 7,
    "finals": 10,
    "semi_finals": 15,
    "first_round_exits": 4,
    "win_pct_of_matches_played": 0.74
  },
  "crucible_label": "SPECIALIST — elite Crucible record",
  "crucible_modifier": 1.22,
  "note": "7 World titles — highest in history. Crucible form consistently outperforms circuit form."
}
```

### `get_pressure_record`

**Parameters:**
- `player_name` (required)
- `tournaments` (optional, default: last 2 seasons)

**Returns:**
```json
{
  "player": "Judd Trump",
  "deciding_frame_record": {
    "played": 42,
    "won": 26,
    "win_pct": 0.619
  },
  "final_frame_clearance_rate": 0.68,
  "pressure_label": "STRONG — above average deciding frame record",
  "pressure_modifier": 1.08
}
```

### `get_break_building_stats`

**Parameters:**
- `player_name` (required)
- `season` (optional, default: current)

**Returns:**
```json
{
  "player": "Ronnie O'Sullivan",
  "centuries_this_season": 84,
  "maximums_career": 15,
  "avg_break": 42.8,
  "century_rate_per_frame": 0.31,
  "break_building_modifier": 1.08
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `player_name` (required)
- `tournament` (required)

**Returns:**
```json
{
  "player": "Ronnie O'Sullivan",
  "tournament": "World Championship 2026",
  "base_signal_score": 71,
  "composite_modifier": 1.18,
  "adjusted_signal_score": 84,
  "modifier_breakdown": {
    "form": 1.05,
    "crucible_record": 1.22,
    "ranking_status": 1.08,
    "break_building": 1.08,
    "pressure_record": 1.10
  },
  "confidence": 0.82,
  "recommendation": "BULLISH — Crucible specialist with elite record. Form secondary to venue history here.",
  "key_risks": ["Age 50+ — stamina over long matches", "Recent form inconsistent outside Crucible"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| 3+ World titles — proven Crucible specialist | ×1.22 |
| World number 1 ranking | ×1.12 |
| 80%+ deciding frame win rate | ×1.12 |
| Top-16 ranking (seeded at Crucible) | ×1.05 |
| Outside top-16 (plays qualifiers) | ×0.88 |
| First Crucible appearance | ×0.88 |
| Losing run (5+ matches without win) | ×0.82 |


---

## The Crucible — venue intelligence

```
WORLD SNOOKER CHAMPIONSHIP AT THE CRUCIBLE (Sheffield):

The Crucible (capacity 980) is the most intimate major sporting venue in the
world relative to the sport it hosts. The crowd is so close to the table that
psychological pressure is unique to this venue.

CRUCIBLE-SPECIFIC SIGNALS:
  Crucible experience: Players who have been to the later stages before
    have measurably better performance than their ranking suggests
    Apply: Crucible_experience modifier × 1.08 for veterans with 2+ SF appearances
    
  "Crucible curse": First-time winners often struggle in their second title defence
    Not statistically confirmed but widely documented — apply × 0.94 in second year
    
  Atmosphere response: Some players are elevated by the Crucible crowd;
    others are inhibited. Track per-player Crucible record vs ranking event record.
    If Crucible win% > ranking event win% by 10%+: Crucible_specialist modifier × 1.10
```

## Three-dart average model (adapted for snooker)

```
CENTURY BREAK RATE — PRIMARY SNOOKER SIGNAL:

Century breaks (100+ points in a single visit to the table) are the
snooker equivalent of basketball's net rating differential.
They measure quality of scoring when the player is at the table.

Century rate per frame:
  > 1.0 centuries per frame: elite form — × 1.12
  0.7-1.0: very good — × 1.06
  0.4-0.7: average — × 1.00
  < 0.4: below par — × 0.93

LONG MATCH ENDURANCE:
  World Championship is best-of-35 frames in the final (3 days).
  Players with strong late-session records: × 1.06
  Players who historically lose long matches: × 0.92
  
  Maximum break (147): career maximum breaks are an ATM signal
  Players with multiple 147s: media attention + commercial visibility
  ATM boost: +0.05 per career maximum break
```

## Competition calendar intelligence

```
SNOOKER TRIPLE CROWN:
  World Championship (April-May, Crucible)
  UK Championship (December, York)
  Masters (February, Alexandra Palace)
  
  Triple Crown winners in same season: enormous ATM event (very rare)
  Apply: narrative_active × 1.20 for any player in contention for all three

WORLD RANKINGS IMPACT:
  Snooker uses rolling 2-year ranking points
  World Championship is 10× more points than a regular event
  
  Ranking consequences:
  Top 16 qualification = direct seeding in all ranking events
  Dropping below 16 = qualification round required
  Below 64 = potential tour card loss
  
  AGENT RULE: Check ranking position and trajectory
  Player falling toward 16 boundary: motivation signal × 1.08 (must perform)
  Player safely in top 8 with big lead: comfort zone signal × 0.95

ATM TIERS FOR SNOOKER:
  Tier 1 — Global icons (Ronnie O'Sullivan, Mark Selby era):
    ATM 0.80-0.85; recognised beyond the sport; TV presenter-tier
  Tier 2 — Multiple World Champions:
    ATM 0.65-0.75; highly respected; strong UK market recognition
  Tier 3 — Top-16 regulars:
    ATM 0.45-0.60; known to snooker fans; commercial via sport-specific deals
```

## Integration: Full snooker pre-match workflow

```
Step 1: Load domain context
  Load sports/snooker/sport-domain-snooker.md

Step 2: Venue check
  World Championship at Crucible? → apply Crucible experience modifier
  
Step 3: Current form
  get_break_building_stats — century break rate last 5 events
  get_player_form_score — recent tournament results
  
Step 4: Pressure record
  get_pressure_record — final frame win rate for deciding frame situations
  
Step 5: Competition context
  Is this a ranking event? Triple Crown match? World Championship round?
  Apply appropriate competition weight
  
Step 6: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "player": "string",
  "century_rate_modifier": 1.06,
  "crucible_experience_modifier": 1.08,
  "pressure_record_modifier": 1.04,
  "composite_modifier": 1.10,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["World Championship Crucible curse (defending champion)"],
  "modifier_reason": "High century rate, Crucible experience, strong pressure record"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `century_rate_modifier` | `get_break_building_stats` | 0.93–1.12 |
| `crucible_experience_modifier` | `get_crucible_record` | 0.94–1.10 |
| `pressure_record_modifier` | `get_pressure_record` | 0.90–1.10 |
| `ranking_trajectory_modifier` | `get_world_ranking_status` | 0.92–1.08 |
| `composite_modifier` | Product of all applicable | 0.80–1.25 |


*MIT License · SportMind · sportmind.dev*
