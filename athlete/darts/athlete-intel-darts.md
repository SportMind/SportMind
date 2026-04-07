# Darts Athlete Intelligence — SportMind Skill

Player-level intelligence for darts fan tokens and prediction markets.

**Applicable tokens / markets:** Individual player tokens, PDC World Championship markets, Premier League markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_player_form_score` | Recent tournament results, average scores, checkout % | Yes |
| `get_three_dart_average` | Rolling 3-dart average trend — primary performance metric | Yes |
| `get_checkout_record` | Finishing % on doubles, crucial double statistics | Yes |
| `get_ally_pally_record` | Venue-specific World Championship history | Yes |
| `get_nine_dart_history` | Career 9-dart finishes — rarity and social impact signal | Yes |
| `get_tour_card_status` | PDC Tour Card status — determines event access | Yes |
| `get_athlete_signal_modifier` | Composite darts modifier | Yes |

---

## Command reference

### `get_three_dart_average`

The most important performance metric in darts — equivalent to strokes gained in golf.

**Parameters:**
- `player_name` (required)
- `matches` (optional, default: last 20)
- `tournament_level` (optional) — `"major"`, `"ranking"`, `"all"`

**Returns:**
```json
{
  "player": "Luke Littler",
  "three_dart_average_overall": 98.42,
  "three_dart_average_majors": 101.18,
  "three_dart_average_trend": "RISING",
  "personal_best_average": 112.37,
  "tour_average_rank": 2,
  "average_modifier": 1.15,
  "note": "Averages above 100 in majors — elite performance under pressure"
}
```

### `get_checkout_record`

**Parameters:**
- `player_name` (required)
- `matches` (optional, default: last 20)

**Returns:**
```json
{
  "player": "Luke Littler",
  "checkout_pct": 42.8,
  "checkout_pct_in_legs_over_100": 58.4,
  "double_top_hit_rate": 71.2,
  "bull_checkout_rate": 44.1,
  "highest_checkout": 170,
  "clutch_finish_label": "RELIABLE — above tour average in pressure finishes",
  "checkout_modifier": 1.08
}
```

### `get_ally_pally_record`

**Parameters:**
- `player_name` (required)

**Returns:**
```json
{
  "player": "Michael van Gerwen",
  "world_championship_appearances": 14,
  "wins": 3,
  "finals": 7,
  "semi_finals": 11,
  "win_pct_of_sets_played": 0.71,
  "ally_pally_label": "SPECIALIST",
  "ally_pally_modifier": 1.18
}
```

### `get_nine_dart_history`

**Parameters:**
- `player_name` (required)

**Returns:**
```json
{
  "player": "Phil Taylor",
  "nine_darters_career": 13,
  "televised_nine_darters": 7,
  "nine_darters_this_season": 1,
  "nine_dart_probability_per_match": 0.018,
  "note": "History increases probability — certain players are statistically more likely"
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `player_name` (required)
- `tournament` (required)

**Returns:**
```json
{
  "player": "Luke Littler",
  "tournament": "PDC World Championship 2026-27",
  "base_signal_score": 74,
  "composite_modifier": 1.18,
  "adjusted_signal_score": 87,
  "modifier_breakdown": {
    "form": 1.15,
    "three_dart_average": 1.15,
    "checkout_record": 1.08,
    "ally_pally_record": 1.05,
    "tour_card_status": 1.00
  },
  "confidence": 0.83,
  "recommendation": "BULLISH — elite averages, rising trend, growing Ally Pally record",
  "key_risks": ["MvG, Price, Clayton all capable of matching averages", "Young player — pressure variance at Ally Pally"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| 3-dart average > 100 in majors | ×1.15 |
| Checkout % > 42% | ×1.08 |
| Proven Ally Pally finalist (2+ finals) | ×1.18 |
| World number 1 ranking | ×1.12 |
| Rising average trend (last 10 matches) | ×1.08 |
| Tour card holder (top 64) | ×1.00 |
| Lost Tour Card | ×0.60 — structural negative |
| Below-average checkout rate (<35%) | ×0.88 |


---

## Three-dart average model

```
THREE-DART AVERAGE — PRIMARY DARTS SIGNAL:

Three-dart average = (total score / total darts thrown) × 3
This is the single most predictive individual darts statistic.

AVERAGE THRESHOLDS:
  > 100.00: elite tournament average — × 1.15 modifier
  95-100:   very good — × 1.08
  90-95:    above average — × 1.03
  85-90:    average — × 1.00
  < 85:     below average — × 0.92

CHECKOUT PERCENTAGE:
  Finishing ability on doubles — the second most important stat
  > 45%: elite finisher — × 1.08
  40-45%: good — × 1.03
  35-40%: average — × 1.00
  < 35%: finishing weakness — × 0.92

COMBINED MODEL:
  Elite average (>100) + elite checkout (>45%) = × 1.20 composite
  Elite average + weak checkout = × 1.06 (leaving doubles unexploited)
  Average + elite checkout = × 1.08 (clinical under pressure)
```

## Ally Pally and venue intelligence

```
ALEXANDRA PALACE (PDC World Championship, London):

The "Ally Pally" is to darts what the Crucible is to snooker:
a specific venue where atmosphere is a genuine competitive factor.

  Capacity: 3,000 (much larger than Crucible — more raucous)
  Atmosphere: New Year's Eve final = most electric atmosphere in darts
  Crowd favourites: British players have enormous crowd support
  
  Home crowd modifier:
    British player at Ally Pally: crowd_advantage × 1.06
    Overseas player at Ally Pally in semi/final: pressure_modifier × 0.97
    
  NIGHT SESSION vs AFTERNOON:
    Night sessions at Ally Pally have significantly higher crowd energy
    Crowd noise can affect concentration — apply × 1.04 for experienced players
    (they are accustomed to it); × 0.95 for first-time Ally Pally competitors

MARSHSIDE (Winter Gardens, Blackpool):
  UK Open venue; different crowd demographics (older, traditional darts fans)
  More sober atmosphere; precision over performance
  No crowd modifier (neutral venue effect)
```

## PDC Tour card and ranking intelligence

```
PDC TOUR CARD:
  Tour card = access to ranking events
  Players without tour card: amateur + Q-School only
  Loss of tour card: career-defining negative signal
  
  Monitor: Players who narrowly hold tour cards are maximum motivated
  Apply: × 1.10 motivation when player needs result to protect card

PDC ORDER OF MERIT:
  Rolling 2-year prize money system
  Top 32 on Order of Merit = PDC World Championship seeding
  
  RANKING SIGNALS:
    Player in top 10: stable; commercial opportunities maximised
    Player 17-32: border zone — motivation elevated (seeding implications)
    Player 33-64: Q-School risk visible on horizon

PREMIER LEAGUE DARTS:
  16-week league (January-May)
  Top 5 advance to Play-offs (O2 Arena, London)
  Highest TV audience darts competition outside World Championship
  
  Premier League invitation = ATM signal (chosen as face of the sport)
  ATM tier: Premier League players × 1.10 vs non-Premier League players
```

## ATM framework for darts

```
DARTS ATM TIERS:

Tier 1 — Icons (Phil Taylor era; current: Michael van Gerwen):
  ATM 0.78-0.85; global recognition within the sport; TV-friendly
  
Tier 2 — World Champions and Premier League regulars:
  ATM 0.60-0.74; recognised by all darts fans; strong UK commercial
  
Tier 3 — Tour card holders, ranking event winners:
  ATM 0.40-0.55; known to dedicated fans
  
  NINE-DART FINISH ATM BOOST:
  Career nine-dart finishes are ATM events (very rare)
  First nine-darter: permanent ATM +0.05
  Live nine-darter (on TV): permanent ATM +0.10 (most-replayed darts footage)
```

## Integration: Full darts pre-match workflow

```
Step 1: Load domain context
  Load sports/darts/sport-domain-darts.md
  
Step 2: Three-dart average and checkout
  get_three_dart_average — recent rolling average
  get_checkout_record — doubles percentage
  
Step 3: Venue check
  Ally Pally World Championship? Night session?
  Apply crowd and venue modifiers
  
Step 4: Ranking context
  get_tour_card_status — is card under pressure?
  High pressure → motivation signal
  
Step 5: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "player": "string",
  "average_modifier": 1.08,
  "checkout_modifier": 1.05,
  "venue_modifier": 1.04,
  "ranking_pressure_modifier": 1.10,
  "composite_modifier": 1.12,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Night session pressure — first time at Ally Pally"],
  "modifier_reason": "98.6 average, 42% checkout, strong ranking pressure motivation"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `average_modifier` | `get_three_dart_average` | 0.92–1.15 |
| `checkout_modifier` | `get_checkout_record` | 0.92–1.08 |
| `venue_modifier` | Ally Pally / venue check | 0.95–1.06 |
| `ranking_pressure_modifier` | `get_tour_card_status` | 1.00–1.10 |
| `composite_modifier` | Product of all applicable | 0.80–1.25 |


*MIT License · SportMind · sportmind.dev*
