# Tennis — Athlete Intelligence

Player-level intelligence for tennis. Covers serve/return metrics, surface performance, physical stamina, head-to-head dynamics, and recent form. Applicable to any player tokens on Chiliz.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_serve_metrics` | 1st serve %, ace rate, double faults, speed | Yes |
| `get_return_game` | Return points won, break points, return depth | Yes |
| `get_surface_record` | Win % by surface, conditions, indoor/outdoor | Yes |
| `get_physical_stamina` | Match duration, 5-set record, recent schedule density | Yes |
| `get_head_to_head` | Direct H2H, surface split, style matchup | Yes |
| `get_player_form_score` | Rolling form over last N tournaments | Yes |
| `get_athlete_signal_modifier` | Composite tennis modifier | Yes |

---

## Key metrics

### `get_serve_metrics`
```json
{
  "player": "Jannik Sinner",
  "surface": "clay",
  "serve_metrics": {
    "first_serve_in_pct": 64.0,
    "ace_rate_per_game": 1.4,
    "double_fault_rate_per_game": 0.6,
    "first_serve_points_won_pct": 78.0,
    "second_serve_points_won_pct": 56.0,
    "serve_speed_1st_avg_kph": 204,
    "serve_speed_2nd_avg_kph": 166,
    "break_point_save_pct": 67.0
  },
  "serve_rating": 88,
  "signal_modifier": 1.08
}
```

### `get_surface_record`
```json
{
  "player": "Rafael Nadal",
  "surface_records": {
    "clay": { "win_pct": 91.7, "titles": 14, "form_last_season": "STRONG" },
    "hard": { "win_pct": 83.2, "titles": 22, "form_last_season": "MODERATE" },
    "grass": { "win_pct": 76.3, "titles": 2, "form_last_season": "WEAK" }
  },
  "current_surface": "clay",
  "surface_modifier": 1.18,
  "signal_modifier": 1.18
}
```

### `get_head_to_head`
```json
{
  "player_a": "Jannik Sinner",
  "player_b": "Carlos Alcaraz",
  "h2h_record": { "sinner_wins": 5, "alcaraz_wins": 7 },
  "h2h_by_surface": {
    "clay": { "sinner": 2, "alcaraz": 4 },
    "hard": { "sinner": 3, "alcaraz": 3 }
  },
  "current_surface": "clay",
  "h2h_surface_verdict": "ALCARAZ_EDGE",
  "signal_modifier_sinner": 0.93,
  "signal_modifier_alcaraz": 1.07
}
```

---

## Tennis modifier table

| Condition | Modifier |
|---|---|
| Player on preferred surface, top form | 1.18 |
| Player on least preferred surface | 0.85 |
| 5-set match in last 48 hours | 0.88 |
| Strong H2H advantage (>65% on current surface) | 1.12 |
| Player returning from injury (first event back) | 0.85 |
| Indoor specialist on outdoor clay | 0.90 |


---

## Modifier reference

| Condition | Modifier |
|---|---|
| Player fully fit, on form, surface specialist | ×1.20 |
| Player fit, good surface record | ×1.10 |
| Neutral — average form, correct surface | ×1.00 |
| Fatigue from 5-set previous round | ×0.90 |
| Injury reported — playing through | ×0.80 |
| Mid-match retirement risk flagged | ×0.65 |

*Ranges consistent with `core/core-athlete-modifier-system.md`*


## Integration example

### Tennis pre-event workflow

```
# Step 1: Load domain context
Load sports/tennis/sport-domain-tennis.md

# Step 2: Check athlete availability and form
get_availability token=[TENN]
get_form_score token=[TENN]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[TENN]

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

---

## Grand Slam round-by-round intelligence

The four Grand Slams are the highest-signal tennis events. Each round has
a distinct signal profile because the format changes the competitive dynamics:
best-of-5 sets for men (all rounds), best-of-3 for women (all rounds except
the final, which is best-of-3 — correction: women play best-of-3 throughout).

```
GRAND SLAM ROUND SIGNAL MODEL:

ROUND 1 (128 to 64):
  Top-32 seeds vs unseeded/lower-ranked opponents
  Expected outcomes: heavily seeded team wins >85%
  Signal value: LOW for top seeds (high certainty = low information)
  Signal value: MODERATE for mid-ranked players (upset possibility)
  Modifier: × 0.70 for matches with seed differential > 50 positions

ROUND 2 (64 to 32):
  Still largely predictable for top-16 seeds
  First genuine tests for seeded players
  Modifier: × 0.80 (moderate)

ROUND 3 (32 to 16):
  First real challenge for top-8 seeds begins
  Fatigue signal starts to register (2 matches already played)
  Modifier: × 0.90

ROUND 4 (last 32 → last 16):
  Seedings begin to matter less — upsets more frequent
  Fatigue from 3 previous matches is measurable
  Modifier: × 0.95
  Fatigue modifier: × 0.93 if player played 5-set match in R3

QUARTER-FINALS (8 to 4):
  Only 8 players remain — all elite
  Surface specialists at peak — form compression less relevant
  Modifier: × 1.05
  Signal quality: HIGH (fewer variables, elite field)

SEMI-FINALS (4 to 2):
  Maximum context from the entire tournament
  Players known quantities: 4 matches of data from this event
  Form on THIS surface in THIS tournament is the primary variable
  Modifier: × 1.10

FINAL:
  Highest signal tennis event
  Both players have full tournament form profile
  H2H on this specific surface maximally predictive
  Modifier: × 1.15
  Two-week physical accumulation: apply × 0.95 stamina factor for 5th set
```

## Surface specialisation model

```
THE FOUR SURFACES — signal implications:

HARD COURT (Australian Open, US Open):
  Most balanced surface — specialists exist but advantage smaller
  Serve tends to be more dominant than on clay
  Baseline rallies shorter than clay — physical attrition less
  Wind: US Open Flushing Meadows known for wind — outdoor variable
  Indoor hard (WTA Finals, some ATP 500): serve even more dominant
  Modifier range: ×0.90 (wrong surface) to ×1.10 (hard court specialist)

CLAY (Roland Garros):
  Greatest surface differential in tennis
  Clay specialists (Nadal era: ×1.25+; current era: ×1.15 for clay specialists)
  Serve disadvantage: slower surface reduces serve dominance
  Physical attrition: highest of all surfaces; 5-set clay is a stamina test
  Dew/humidity: evening clay matches with humidity → heavier ball, slower rallies
  Modifier range: ×0.82 (grass/hard specialist) to ×1.18 (clay specialist)
  
  CLAY SPECIALIST IDENTIFICATION:
    Win% on clay >70% with 50+ matches: confirmed clay specialist
    Win% on clay >60%: moderate specialist
    Win% on clay <50%: surface weakness — apply ×0.88 minimum

GRASS (Wimbledon):
  Fastest surface — serve dominance highest
  Grass specialists are rare; most players neutralise on grass
  Low bounce: short backswing players advantaged
  Wet grass: slower, more like clay — check morning weather at Wimbledon
  Short grass season (2-3 weeks) means small sample size
  Modifier range: ×0.88 (clay specialist) to ×1.15 (grass specialist)
  
  WIMBLEDON SPECIFIC:
    Seedings based on grass performance (not ATP ranking) — check seedings
    Qualifying week: grass surface evolves over the tournament (wears down)
    Service breaks less common on grass — hold % matters more

INDOOR HARD (Year-End Finals, some Masters):
  Pure serve/return contest
  Form on outdoor clay/grass less transferable than hard-to-indoor
  Pressure context: ATP Finals or WTA Finals = Year-End Champion stakes
  
SURFACE TRANSITION MODIFIER:
  Playing first event on new surface (within 10 days of last event):
    Apply × 0.92 adaptation modifier
  First event on new surface after injury break:
    Apply × 0.88 adaptation + rehabilitation modifier
```

## Physical stamina model

```
STAMINA FLAGS (tennis-specific):

BACK-TO-BACK TOURNAMENT PLAYER:
  Player who played final of last tournament last week:
  Apply × 0.88 fatigue modifier for first 2 rounds of new event
  5-set match within 24h of next match: × 0.85 (rare but possible in doubles/singles overlap)

5-SET ACCUMULATION (men's Grand Slam):
  Matches played in 5 sets in current tournament:
  1 five-set match: × 0.96 (moderate fatigue)
  2 five-set matches: × 0.91 (significant fatigue)
  3+ five-set matches: × 0.85 (stamina concern — flag for all remaining matches)

RETIREMENT RISK:
  Player with known injury playing through:
  Apply × 0.65 — mid-match retirement risk is real signal risk
  Injury aggravation = void for prediction purposes
  Any player mid-tournament with "will decide day-of": treat as lineup_unconfirmed

HOT WEATHER:
  Extreme heat (>35°C at US Open / Australian Open):
  Apply × 0.95 baseline for all players
  Heat rule activations possible → extended breaks
  Older players and those with injury history: apply additional × 0.95
```

## ATM framework for tennis

```
TENNIS ATM TIERS:

Tier 1 — Global Icons (ATM 0.90-0.95):
  Post-Big 3 era: Jannik Sinner, Carlos Alcaraz, Novak Djokovic (active)
  Women's: Iga Swiatek, Coco Gauff
  Characteristics: Major titles, 5M+ social following, global brand presence
  APS: 0.85+ — commercial identity fully portable

Tier 2 — Elite ATP/WTA (ATM 0.72-0.85):
  Top-20 players with developing commercial profiles
  Multiple titles, growing social following

Tier 3 — Established professionals (ATM 0.50-0.68):
  Top-50 players; known to tennis fans; limited casual recognition

RIVALRY SIGNAL:
  Sinner vs Alcaraz: current rivalry narrative × 1.15 ATM for both during their matches
  Historical: Federer/Nadal/Djokovic rivalry drove tennis commercial growth
  Established rivalries have higher H2H predictive power than surface alone
```

## Integration: Full Grand Slam workflow

```
Step 1: Load domain context
  Load sports/tennis/sport-domain-tennis.md

Step 2: Surface check FIRST
  get_surface_record for both players
  Clay specialist vs hard specialist: apply full surface modifier
  This overrides form differential for surface mismatches

Step 3: Tournament round context
  What round is this? Apply round modifier (R1 × 0.70 to Final × 1.15)
  How many 5-set matches has this player played? Fatigue check

Step 4: H2H on current surface
  get_head_to_head — surface-specific H2H is most predictive
  
Step 5: Stamina flags
  get_physical_stamina — back-to-back, 5-set accumulation, injury status
  
Step 6: Composite modifier
  get_athlete_signal_modifier (surface × H2H × round × stamina)
  
Step 7: Decision
  Surface match + strong H2H + late round: ENTER standard
  Surface mismatch or adaptation period: REDUCE to 65%
  Injury/retirement risk: WAIT until confirmed fitness
```


*MIT License · SportMind · sportmind.dev*
