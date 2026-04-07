# Australian Rules Football (AFL) — Athlete Intelligence

Player-level intelligence for afl predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** AFL club tokens (emerging Tier 2); AFL prediction markets

---

## Overview

AFL player intelligence centres on kicking accuracy (the most predictive individual stat), clearance work, and contested possession. The MCG Grand Final context and climate are key external modifiers.

---

## Commands

| Command | Description |
|---|---|
| `get_availability` | Player/athlete availability status |
| `get_form_score` | Recent performance score (last 5 events) |
| `get_sport_modifier` | Sport-specific key variable modifier |
| `get_athlete_signal_modifier` | Composite modifier — runs all sub-skills |

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for Australian Rules Football (AFL). Combines availability, form, and sport-specific variables.

**Parameters:**
- `player_id` (required) — athlete identifier  
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{
  "athlete": "string",
  "availability": 1.0,
  "form_score": 0.85,
  "sport_specific_modifier": 1.05,
  "composite_modifier": 1.05,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["string"],
  "modifier_reason": "Kicking accuracy and clearances is the primary driver"
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Peak fitness, top recent form, ideal conditions | ×1.20 |
| Fit, good form | ×1.10 |
| Neutral | ×1.00 |
| Minor fitness concern | ×0.90 |
| Significant fitness doubt | ×0.80 |
| Key athlete confirmed unavailable | ×0.70 |

---

## Integration example

### Australian Rules Football (AFL) pre-event workflow

```
# Step 1: Load domain context
Load sports/afl/sport-domain-afl.md

# Step 2: Athlete checks
get_availability athlete=[ATHLETE_ID]
get_form_score athlete=[ATHLETE_ID]
get_sport_modifier athlete=[ATHLETE_ID]

# Step 3: Get composite modifier
get_athlete_signal_modifier athlete=[ATHLETE_ID] event=[EVENT_ID]

# Step 4: Decision logic
# composite_modifier >= 1.10 AND signal >= 65 → ENTER
# composite_modifier < 1.00 OR injury_warning → WAIT or ABSTAIN
```

---

## Compatibility

**L1 domain:** `sports/afl/sport-domain-afl.md`
**L4 market:** `market/market-afl.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_kicking_accuracy` | Disposal efficiency, kicking accuracy %, conversion rate | Yes |
| `get_contested_possession` | Contested marks, hard ball gets, clearance count | Yes |
| `get_ground_ball_work` | Pressure acts, tackles, uncontested disposals | Yes |
| `get_fitness_status` | Match fitness rating, games played, injury history | Yes |
| `get_fantasy_score_trend` | AFL fantasy score last 5 — strong form proxy | Yes |
| `get_athlete_signal_modifier` | Composite AFL athlete modifier | Yes |

---

## AFL positional framework

```
AFL IS POSITIONAL — different positions drive different signals:

MIDFIELDERS (primary signal drivers):
  Clearance count: most predictive individual AFL stat
  Contested possession rate: separates elite from good midfielders
  Centre bounce attendances (CBA %): usage proxy — higher = more important
  Tackling pressure: effort/pressure signal
  
  Elite midfielder modifier: × 1.12-1.18 when clearance avg > 8/game
  Form threshold: 110+ AFL fantasy points per game = elite form signal
  
KEY FORWARDS:
  Goals per game: most visible individual stat
  Shot conversion rate: efficiency signal
  Contested marks: separates genuine forwards from role players
  
  Star forward in form (6+ goals last 3 games): × 1.12
  Forward out of form (< 2 goals last 5 games): × 0.90
  
BACKS / DEFENDERS:
  One-on-one defensive success rate
  Rebound 50s: initiating forward entries
  Intercept marks: defensive dominance signal
  
  Elite tagger (assigned to shut down opponent's best): × 0.88 for tagged player
  
RUCKS:
  Hit-out to advantage: quality of ruck work
  Clearance contribution: rucks who also work in the midfield
  
  Ruck dominance (> 35 hit-outs per game): × 1.06
```

## Kicking accuracy model

```
KICKING ACCURACY — PRIMARY AFL INDIVIDUAL SIGNAL:

Kicking accuracy % = (effective kicks / total kicks) × 100

  > 70% accuracy: elite disposal user — × 1.08 signal modifier
  60-70%:         above average — × 1.03
  50-60%:         average — × 1.00
  < 50%:          turnover risk — × 0.92

SUPERCOACH/AFL FANTASY SCORE AS FORM PROXY:
  AFL fantasy scoring incorporates multiple positive and negative actions.
  It is the most comprehensive single-number form proxy in Australian rules.
  
  Last 5 game average:
    > 120 points: elite form — × 1.12
    100-120:      good form — × 1.06
    80-100:       average — × 1.00
    < 80:         poor form — × 0.92
    
  Trend matters more than level:
    Rising 3 consecutive games: × 1.04 additional modifier
    Declining 3 consecutive: × 0.94 additional modifier
```

## MCG and ground-specific intelligence

```
MCG (Melbourne Cricket Ground) — AFL's primary venue:
  75,000+ capacity — largest stadium in Australia
  Grand Final venue: always MCG (unless extraordinary circumstances)
  Oval shape: suits open, running, kicking game (not close-quarter grunt)
  Playing surface: occasionally difficult after cricket season use
  
  MCG advantage for:
    High-disposal midfielders (space to use the ball)
    Accurate kick-to-goal forwards (distance shots more common)
    Teams that run and carry (large ground suits team fitness)
  
  MCG disadvantage for:
    Physical, contested teams (less advantage in big spaces)
    
WESTERN AUSTRALIA (Optus Stadium, Perth):
  Perth teams (West Coast, Fremantle) have significant travel advantage
  Interstate teams: 3-4h flight, time zone change (-3h in Perth)
  Perth travel modifier: × 0.88 for eastern state visiting teams
  
NORTH QUEENSLAND (Cazaly's, Cairns):
  Heat and humidity: apply heat modifier × 0.93 for non-Queensland teams
  
DARWIN (Marrara):
  Extreme heat + humidity: × 0.90 for non-Northern Territory teams
  
AGENT RULE: Check venue before any AFL athlete modifier.
  Perth away travel and extreme heat venues override form data.
```

## AFL season structure

```
REGULAR SEASON (March - August):
  24 rounds; each club plays 22 games
  Finals begin September (top-8)
  
FINALS SERIES (September):
  Double chance (top-4) vs must-win (5-8)
  
  Finals signal multipliers:
    Elimination final (5v4 and 6v3): × 1.25 signal weight
    Semi-final: × 1.35
    Preliminary final: × 1.50
    Grand Final (MCG): × 2.00
    
TRAVEL FIXTURE INTELLIGENCE:
  Teams playing third consecutive away game: apply × 0.90 fatigue
  Teams playing in Perth away: × 0.88 (travel + time zone)
  Teams playing their first game in 16+ days: × 0.92 (match rustiness)
  
INDIGENOUS ROUND (Round 11 approximately):
  Significant cultural and community significance
  For clubs with strong Indigenous player cohort: × 1.05 motivation signal
  No signal impact for non-relevant clubs
```

## Integration: Full AFL pre-game workflow

```
Step 1: Load domain context
  Load sports/afl/sport-domain-afl.md
  
Step 2: Venue and travel check FIRST
  Perth away? → × 0.88 travelling team
  Extreme heat? → × 0.90-0.93
  
Step 3: Key midfielder assessment
  get_contested_possession — clearances, CBA %
  Elite midfielder in form? → × 1.12-1.18
  
Step 4: Kicking accuracy and fantasy score
  get_kicking_accuracy + get_fantasy_score_trend
  Rising trend × 3 games → × 1.04 additional
  
Step 5: Finals context
  Finals match? → Apply appropriate multiplier
  
Step 6: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "player": "string",
  "position": "midfielder|forward|back|ruck",
  "availability": 1.0,
  "kicking_accuracy_modifier": 1.05,
  "form_modifier": 1.08,
  "venue_modifier": 0.95,
  "composite_modifier": 1.08,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Perth travel — check if acclimatised"],
  "modifier_reason": "Elite midfielder in form; kicking accuracy above 65%"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `kicking_accuracy_modifier` | `get_kicking_accuracy` | 0.92–1.08 |
| `form_modifier` | `get_fantasy_score_trend` | 0.90–1.15 |
| `venue_modifier` | Venue/travel check | 0.88–1.00 |
| `position_modifier` | Positional role | 0.90–1.18 |
| `composite_modifier` | Product of all applicable | 0.75–1.25 |


*MIT License · SportMind · sportmind.dev*
