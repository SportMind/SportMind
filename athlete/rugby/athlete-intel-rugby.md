# Rugby Union — Athlete Intelligence

**Player-level intelligence for rugby union fan tokens and pre-match signal analysis.**
Covers positional intelligence, set piece contributions, physicality metrics,
disciplinary profile, international cycle impact, and the Lions selection signal.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_positional_profile` | Position-specific performance metrics | Yes |
| `get_set_piece_contribution` | Lineout/scrum/restart contributions | Yes |
| `get_physicality_profile` | Carries, tackles, metres, offloads | Yes |
| `get_kicker_profile` | Kicking game: accuracy, territory, conversions | Yes |
| `get_disciplinary_record` | Cards, penalties conceded, cited incidents | Yes |
| `get_international_availability` | Lions, national team, Six Nations dates | Yes |
| `get_player_form_score` | Rolling form over last N matches | Yes |
| `get_athlete_signal_modifier` | Composite rugby union modifier | Yes |

---

## Positional framework

Rugby union's 15 positions have fundamentally different signal contributions.
The kicker and the loosehead prop contribute to team performance in completely
different ways — no single metric applies across all positions.

```
POSITIONAL SIGNAL WEIGHT:

FLY-HALF (10):
  Primary signal driver: kicking accuracy, decision-making, game management
  Modifier range: 0.78 (poor kicker) to 1.22 (elite game controller)
  ATM: highest of forwards/backs (face of the team; most media-visible)

PROP (1, 3):
  Primary signal driver: scrum dominance / set piece stability
  Modifier range: 0.88 (weak scrummager) to 1.12 (dominant)
  ATM: low individually; high collectively (scrum dominance is team signal)

HOOKER (2):
  Primary signal driver: lineout accuracy (throwing), scrum binding
  Modifier range: 0.85 (poor lineout throw) to 1.10 (precision thrower)
  Note: lineout winning rate is the most statistically predictive set-piece metric

LOCKS (4, 5):
  Primary signal driver: lineout possession won, carries, tackle completion
  Modifier range: 0.90 to 1.10
  ATM: moderate — known to hardcore fans; low to casual market

FLANKERS / NUMBER 8 (6, 7, 8):
  Primary signal driver: breakdown success, turnover count, metres carried
  Star back-row player (70+ tackles + 10+ turnovers/season): modifier 1.12-1.18
  ATM: highest among forwards — breakdown stars have genuine commercial profile

SCRUM-HALF (9):
  Primary signal driver: service speed, box kick accuracy, breakdown support
  Secondary: run threat from base of ruck
  ATM: high when team is running an attacking system; lower in kicking game

CENTRES (12, 13):
  Primary signal driver: metres gained, line breaks, defensive organisation
  Star centre: 1.10-1.15 when in form; international recognition boosts ATM

WINGERS (11, 14) / FULLBACK (15):
  Primary signal driver: tries scored, metres, kick receipt under pressure
  Try scorers have highest individual ATM — touchdowns drive social engagement
  Star winger: modifier 1.15-1.20 in high-scoring games
```

---

## Key metrics

### `get_kicker_profile`

The kicker is the most important individual in rugby union signal analysis.
40-50% of points in professional rugby come from kicks. Kicker form directly
determines match outcomes more than any other single position.

```json
{
  "player": "Finn Russell",
  "position": "fly-half",
  "kicking_metrics": {
    "conversion_accuracy_pct": 82.4,
    "penalty_accuracy_pct": 78.6,
    "drop_goals_this_season": 2,
    "territorial_kick_avg_metres": 47.2,
    "kicks_from_hand_per_match": 12.4,
    "box_kick_accuracy_pct": 71.0
  },
  "kicker_tier": "ELITE",
  "signal_modifier": 1.18,
  "modifier_note": "Elite kicker in form — 82% conversions significantly above league average (71%)"
}
```

### `get_set_piece_contribution`

```json
{
  "match_context": "Bath vs Saracens — Premiership",
  "lineout": {
    "own_lineout_win_rate": 0.88,
    "opposition_lineout_disruption_rate": 0.24,
    "hooker": "Jamie George",
    "throw_accuracy_pct": 91.0,
    "lineout_modifier": 1.08
  },
  "scrum": {
    "own_scrum_win_rate": 0.92,
    "penalties_won_from_scrum": 3.2,
    "scrum_modifier": 1.10
  },
  "set_piece_composite_modifier": 1.09,
  "signal_note": "Dominant set piece — expect territory and field position advantage"
}
```

### `get_disciplinary_record`

```json
{
  "player": "Tom Curry",
  "position": "flanker",
  "disciplinary": {
    "yellow_cards_this_season": 2,
    "red_cards_this_season": 0,
    "penalties_conceded_per_match": 3.8,
    "cited_incidents": 0,
    "discipline_tier": "MODERATE_RISK"
  },
  "discipline_modifier": 0.94,
  "note": "2 yellow cards this season indicates breakdown aggression — elevated dismissal risk"
}
```

### `get_international_availability`

```json
{
  "player": "Antoine Dupont",
  "national_team": "France",
  "availability": {
    "six_nations_window": "UNAVAILABLE",
    "six_nations_dates": "2026-02-06 to 2026-03-21",
    "club_during_six_nations": "STADE TOULOUSAIN",
    "club_signal_impact": "NEGATIVE — key player unavailable 7 weeks",
    "lions_eligible": true,
    "lions_year": 2029,
    "lions_selection_probability": "HIGH"
  },
  "availability_modifier": 0.82,
  "note": "France's most important player absent for Six Nations window — major squad disruption"
}
```

---

## Rugby union modifier table

| Condition | Modifier |
|---|---|
| Elite kicker in form (>80% accuracy) | 1.18 |
| Elite kicker out of form (<65% accuracy) | 0.85 |
| Set piece dominance (scrum + lineout >90%) | 1.10 |
| Star breakdown player in form (10+ turnovers) | 1.12 |
| Key player on international duty (absent) | 0.82 |
| Star back-row player with 2 yellows this season | 0.94 |
| Lions selection announcement week | 1.08 (ATM spike) |
| Player cited post-match (suspended risk) | 0.88 |
| Hooker with <75% lineout throw accuracy | 0.90 |

---

## International cycle integration

```
RUGBY UNION AVAILABILITY CALENDAR (annual):

November (Autumn Internationals):
  Club players released to national teams for 3-4 test windows
  Impact: club squads depleted; form data less reliable during this period
  High-Origin clubs (3+ test players): apply congestion modifier × 0.88
  
February–March (Six Nations):
  7-week sustained disruption for clubs with Six Nations players
  England, Ireland, France, Wales, Scotland clubs most affected
  Italy clubs: some disruption but lower-tier impact
  
June–July (Summer tours):
  Less disruptive — end of season; most clubs in off-season
  Southern hemisphere Autumn tours: NZ/SA/AUS clubs affected in June
  
British & Irish Lions (every 4 years — 2025, 2029):
  Most elite British/Irish club players absent for 8-10 weeks (June-July)
  Top 20% of Premiership/URC talent pool absent simultaneously
  Apply × 0.78 availability modifier for clubs losing 4+ Lions
  
ATM SIGNAL:
  Lions selection = career peak profile moment for most players
  Apply ATM spike × 1.15 at Lions squad announcement for selected players
  Club token signal: positive if player selected (recognition); negative if absent 6+ weeks

AGENT RULE:
  Check international window calendar before any rugby union athlete modifier.
  International availability overrides form data — an absent player has modifier 0.82
  regardless of their recent form.
```

---

## Integration example

```
RUGBY UNION PRE-MATCH WORKFLOW:

Step 1: Load domain context
  Load sports/rugby/sport-domain-rugby-union.md
  Check market/international-rugby-cycle.md — which window is active?

Step 2: Kicker assessment (ALWAYS first)
  get_kicker_profile for both teams' primary kickers
  Apply kicker_tier modifier before any other modifier

Step 3: Set piece assessment
  get_set_piece_contribution (lineout win rate, scrum dominance)
  Set piece winner has structural territory advantage

Step 4: Availability check
  get_international_availability for all key players
  International window? Apply × 0.82 for each absent star

Step 5: Disciplinary check
  get_disciplinary_record for key players with elevated risk
  2+ yellow cards this season: apply × 0.94

Step 6: Composite modifier
  get_athlete_signal_modifier (combines all above)
  Output: SportMind confidence schema
```

**See:** `core/core-officiating-intelligence.md` for referee modifier (referee
signal is especially important in rugby — penalty counts vary significantly by official).

---

## Compatibility

**Domain skill:** `sports/rugby/sport-domain-rugby-union.md`
**Market cycle:** `market/international-rugby-cycle.md`
**Officiating:** `core/core-officiating-intelligence.md`
**Manager intel:** `core/manager-intelligence.md`

*MIT License · SportMind · sportmind.dev*

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for rugby union. Combines kicker form, set piece contribution,
availability, and disciplinary record into one multiplier.

**Parameters:**
- `player_id` (required) — Player identifier or name
- `match_id` (optional) — Specific fixture; defaults to next scheduled

**Returns:**
```json
{
  "player": "string",
  "position": "string",
  "availability": 1.0,
  "kicker_modifier": 1.12,
  "set_piece_modifier": 1.05,
  "disciplinary_modifier": 0.97,
  "international_availability": true,
  "composite_modifier": 1.08,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["string"],
  "modifier_reason": "Elite kicker in form; set piece advantage; minor discipline concern"
}
```

---

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `kicker_modifier` | `get_kicker_profile` | 0.78–1.22 |
| `set_piece_modifier` | `get_set_piece_contribution` | 0.85–1.10 |
| `disciplinary_modifier` | `get_disciplinary_record` | 0.88–1.00 |
| `availability_modifier` | `get_international_availability` | 0.78–1.05 |
| `lions_selection_atm_spike` | Squad announcement week | ×1.15 |
| `composite_modifier` | Product of all applicable | 0.65–1.25 |
