# Basketball (NBA) — Athlete Intelligence

Player-level intelligence for NBA fan tokens. Covers load management, scoring efficiency, on/off splits, playmaking, defensive assignments, and clutch performance.

**Applicable tokens:** CITY (Manchester City — not NBA, but template for any NBA token), APL, and any NBA tokens added to Chiliz.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_load_management_status` | DNP-rest vs injury, back-to-back flag, minutes trend | Yes |
| `get_scoring_efficiency` | TS%, shot location, 3PT rate, clutch stats | Yes |
| `get_on_off_splits` | Net rating with/without player on court | Yes |
| `get_playmaking_profile` | AST%, usage, pick-and-roll efficiency | Yes |
| `get_defensive_assignment` | Matchup vs opponent star, opponent FG% when guarded | Yes |
| `get_foul_trouble_risk` | Fouls per 36 min, disqualification history | Yes |
| `get_player_form_score` | Rolling form over last N games | Yes |
| `get_athlete_signal_modifier` | Composite NBA athlete modifier | Yes |

---

## Key metrics

### `get_load_management_status`
```json
{
  "token": "CITY_NBA",
  "star_player": "Nikola Jokić",
  "load_management": {
    "status": "ACTIVE",
    "dnp_reason": null,
    "back_to_back": false,
    "days_rest": 2,
    "minutes_last_5_games": [34, 32, 36, 30, 35],
    "season_minutes_per_game": 33.4,
    "managed_rest_games_this_season": 3,
    "injury_designation": "NONE"
  },
  "availability_modifier": 1.05,
  "signal_modifier": 1.05
}
```

### `get_on_off_splits`
```json
{
  "player": "Nikola Jokić",
  "on_court_net_rating": 14.2,
  "off_court_net_rating": -3.8,
  "net_rating_differential": 18.0,
  "on_court_offensive_rating": 124.6,
  "on_court_defensive_rating": 110.4,
  "signal_modifier": 1.20,
  "modifier_reason": "18pt net rating swing — team dramatically better with player on court"
}
```

### `get_defensive_assignment`
```json
{
  "player": "Jrue Holiday",
  "matchup_vs": "Luka Dončić",
  "opponent_fg_pct_when_guarded": 38.2,
  "opponent_3pt_pct_when_guarded": 29.8,
  "opponent_points_per_possession": 0.81,
  "assignment_win_rate": 0.67,
  "defensive_modifier": 1.10
}
```

---

## NBA modifier table

| Condition | Modifier |
|---|---|
| Star player active, 2+ days rest | 1.08 |
| Back-to-back game, star player | 0.88 |
| Star player DNP-rest | 0.70 |
| Star player injured (out) | 0.62 |
| Net rating differential >15pts | 1.18 |
| Foul trouble risk (>6 fouls/36) | 0.90 |
| Clutch performer (>40% clutch TS) | 1.12 |


---

## Integration example

### NBA Basketball pre-event workflow

```
# Step 1: Load domain context
Load sports/nba/sport-domain-nba.md

# Step 2: Check athlete availability and form
get_availability token=[NBA]
get_form_score token=[NBA]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[NBA]

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

## NBA Star Tier Framework

```
NBA ATM TIERS (for fan token commercial intelligence):

TIER 1 — Global Icons (ATM 0.92-0.95):
  LeBron James era: redefined global basketball commercial reach
  Current tier 1: Giannis Antetokounmpo, Nikola Jokić, Luka Dončić, Anthony Edwards
  Characteristics: 10M+ social following; shoe deals; global market recognition
  APS: 0.88+ — commercial identity fully portable to any franchise

TIER 2 — Franchise Stars (ATM 0.78-0.88):
  Defines their franchise; top-5 in conference MVP conversations
  On/off net rating differential: typically 12-20 points
  Social: 3-10M followers; regional to national recognition
  APS: 0.72-0.82

TIER 3 — Starter Quality (ATM 0.55-0.72):
  All-Star calibre or below; well-known to basketball fans
  On/off differential: 5-12 points
  APS: 0.50-0.65

TIER 4 — Role Players (ATM 0.25-0.50):
  Known within league; limited casual fan recognition
  APS: 0.25-0.45 (limited portability beyond core fans)
```

## Playoff intelligence

```
NBA PLAYOFF MODIFIER MODEL:

REGULAR SEASON vs PLAYOFFS:
  Regular season form has different predictive value in playoffs
  Physical intensity increases; defensive focus increases
  Apply × 0.92 to regular-season-only based predictions in playoffs
  
SERIES CONTEXT MODIFIERS:
  Team leading 3-0: apply rest management modifier × 0.92 (blowout risk)
  Team trailing 0-3: maximum desperation; apply × 1.15 motivation modifier
  Series tied 2-2: equal stakes; no series modifier (pure current form)
  
PLAYOFF SPECIFIC PLAYER SIGNALS:
  "Playoff performer" (career playoff stats > regular season):
    modifier × 1.10 in any playoff context
  "Regular season player" (career regular season stats > playoffs):
    modifier × 0.90 in playoff context
    
  Star player in Finals for first time:
    High variance — excitement vs pressure; apply × 1.05 with widened uncertainty
    
ELIMINATION GAME:
  Both teams: apply × 1.08 maximum effort modifier
  Trailing player with historically poor elimination records: × 0.90
```

## Trade deadline intelligence

```
NBA TRADE DEADLINE (February 6):

PRE-DEADLINE SIGNALS:
  "In trade talks" (Tier 1 journalist): apply TSI 0.60+; APS recalculation triggered
  Player publicly requesting trade: APS spike × 1.20 (motivated to move)
  Star player not in trade talks: positive signal for franchise stability
  
POST-TRADE SIGNALS:
  Buying team: apply × 1.08 for first 5 games (integration adjustment)
  Selling team: negative signal × 0.90 for first 5 games (disruption)
  Player traded: individual APS calculation for new franchise fit
    Check: does new team's system match player's strengths?
    On/off split compatibility with new roster = key integration signal
  
BUYOUT MARKET (post-deadline):
  Veteran player bought out and signed by contender:
  Apply × 1.12 motivation modifier — player chose the team; high buy-in signal

AGENT RULE: After any trade involving a token-connected franchise:
  Reload athlete modifier calculations immediately
  Old form data has reduced reliability in new context
  Apply × 0.85 form data reliability for first 5 games post-trade
```

## Contract year intelligence

```
CONTRACT YEAR EFFECT:

Player in final year of contract (career incentive):
  Historically: +8-12% performance above expected in contract years
  Apply × 1.08 motivation modifier for star players in contract year
  
Max contract pending:
  Player seeking max extension: maximum motivation signal
  Player in "prove it" deal (below market): elevated performance incentive
  
AGENT RULE: Check contract status for key players on each analysis.
  Contract year × max available = highest individual motivation modifier in the library.
  Combine with: form, health, system fit for complete modifier picture.
```
