# American Football (NFL) — Athlete Intelligence

Player-level intelligence for NFL fan tokens. Covers QB metrics, O-line health, receiver efficiency, defensive matchups, kicker form, and snap count trends.

**Applicable tokens:** Any NFL team tokens added to Chiliz Chain in future. Architecture ready.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_qb_metrics` | CPOE, air yards, pressure stats, red zone efficiency | Yes |
| `get_oline_health` | Individual blocker availability, pass/run block win rates | Yes |
| `get_receiver_profile` | Separation, target share, YAC, contested catch rate | Yes |
| `get_defensive_matchup` | Coverage grade, blitz success, run stop rate | Yes |
| `get_kicker_form` | FG % by distance and conditions, clutch record | Yes |
| `get_snap_count_trend` | Usage trending up or down, practice status | Yes |
| `get_injury_designations` | Q/D/O designations for all key players | Yes |
| `get_athlete_signal_modifier` | Composite NFL athlete modifier for signal score | Yes |

---

## Key metrics

### `get_qb_metrics`
```json
{
  "player": "Patrick Mahomes",
  "token": "KC_TOKEN",
  "metrics": {
    "CPOE": 4.8,
    "air_yards_per_attempt": 9.2,
    "yards_after_catch_generated": 3.1,
    "passer_rating_under_pressure": 94.2,
    "time_to_throw_avg_sec": 2.54,
    "red_zone_td_pct": 68.0,
    "4th_quarter_comeback_record": "5-2 this season",
    "interception_worthy_throw_pct": 2.1,
    "form_score": 91,
    "signal_modifier": 1.14
  }
}
```

### `get_oline_health`
```json
{
  "token": "KC_TOKEN",
  "offensive_line": [
    { "name": "Creed Humphrey", "position": "C", "status": "ACTIVE", "pass_block_win_rate": 94.0, "run_block_win_rate": 87.0 },
    { "name": "Joe Thuney", "position": "LG", "status": "QUESTIONABLE", "fit_pct": 65 }
  ],
  "starting_5_health_pct": 82,
  "pressure_rate_projected": 24.0,
  "signal_modifier": 0.91,
  "modifier_reason": "LG questionable — pressure rate increases against strong edge rushers"
}
```

### `get_injury_designations`
```json
{
  "token": "KC_TOKEN",
  "week": 18,
  "designations": [
    { "player": "Patrick Mahomes", "position": "QB", "designation": "FULL", "practice": "FP" },
    { "player": "Travis Kelce", "position": "TE", "designation": "QUESTIONABLE", "practice": "LP", "injury": "Knee" },
    { "player": "Joe Thuney", "position": "LG", "designation": "QUESTIONABLE", "practice": "LP", "injury": "Ankle" }
  ],
  "risk_level": "MEDIUM",
  "signal_modifier": 0.89
}
```

---

## NFL modifier table

| Condition | Modifier |
|---|---|
| Starting QB confirmed, CPOE >3.0 | 1.12 |
| QB questionable | 0.82 |
| QB ruled out (backup starts) | 0.65 |
| O-line fully healthy | 1.05 |
| 2+ O-line starters out | 0.85 |
| Star receiver out | 0.88 |
| Kicker in top-10 form, dome game | 1.04 |

---

## Injury intelligence

Full injury intelligence for nfl is available in the dedicated framework:

- **Core framework:** `core/injury-intelligence/core-injury-intelligence.md`
  Injury taxonomy (Tier A/B/C), modifier pipeline, replacement quality delta,
  squad depth stress index, return-to-play curves, recurrence risk.
  
- **Sport-specific:** `core/injury-intelligence/injury-intel-nfl.md`
  
  
  Wednesday/Thursday/Friday designation system, QB positional criticality tiers, O-line blind spot, practice squad promotion patterns, weather interaction.
  
  
  

Load these files alongside this skill for injury-aware agent reasoning.


---

## Integration example

### NFL Football pre-event workflow

```
# Step 1: Load domain context
Load sports/nfl/sport-domain-nfl.md

# Step 2: Check athlete availability and form
get_availability token=[NFL]
get_form_score token=[NFL]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[NFL]

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

## QB primacy model

```
THE QUARTERBACK IS THE NFL'S PRIMARY SIGNAL VARIABLE:

No other position in professional sport has more individual impact on team
outcome than an NFL quarterback. A Tier 1 QB with a competent supporting
cast wins more than any other sport's star player would.

QB TIERS:
  Tier 1 — Franchise MVP (Patrick Mahomes, Josh Allen, Lamar Jackson tier):
    Wins games teams have no right winning; covers for weak O-line
    When healthy: team signal modifier × 1.18-1.22
    When absent: immediate reload required; apply × 0.65 (backup starts)
    ATM: 0.88-0.92 (global recognition; highest commercial signal in NFL)
    
  Tier 2 — Elite starter (consistent playoff-level QB):
    Wins when supporting cast is competent
    Team signal modifier: × 1.10-1.15 when in form
    ATM: 0.75-0.85
    
  Tier 3 — Average starter (manages games, does not win them):
    Team wins come from defense and running game
    Team signal modifier: × 1.00-1.05
    ATM: 0.50-0.65
    
  Tier 4 — Backup / practice squad:
    Team modifier: × 0.65 (this is the primary backup signal in the NFL)
    ATM: < 0.40

QB METRICS THAT MATTER:
  CPOE (Completion % Over Expected): most predictive single QB stat
    > +5% CPOE: elite accuracy → × 1.10
    -5% to +5%: average → × 1.00
    < -5% CPOE: accuracy concern → × 0.92
    
  Clean pocket vs under pressure split:
    Big differential (>20% drop in accuracy under pressure): vulnerable to pass rush
    Apply × 0.88 if facing top-5 pass rush defence
    
  Fourth quarter / clutch performance:
    Passer rating in Q4/OT > 95: clutch modifier × 1.08
    Passer rating in Q4/OT < 75: late-game concern × 0.92
```

## Injury designation protocol

```
NFL INJURY DESIGNATIONS — most important weekly signal:

Wednesday:
  Initial injury designations published
  Q (Questionable): ~50% chance of playing
  D (Doubtful): ~25% chance
  O (Out): will not play
  IR (Injured Reserve): out minimum 4 weeks
  DNR (Did Not Return): left last game; status for next game unclear

Thursday/Friday:
  Updated designations with practice participation
  Full Practice (FP): strong signal to play
  Limited Practice (LP): still uncertain — wait for final report
  Did Not Practice (DNP): significant doubt; two consecutive DNP = almost certainly out

Saturday (Final Injury Report — mandated):
  Definitive for Sunday games
  RULE: Never finalise a signal until Saturday injury report
  Any key player as Q on Saturday: maintain lineup_unconfirmed flag at 30%

Sunday Morning:
  Inactives declared ~90 minutes before kickoff
  INACTIVES RULE: 7 players declared inactive per game — this is the definitive signal
  If star player declared inactive: RELOAD (same protocol as Category 1 breaking news)

KEY POSITIONS BY SIGNAL IMPACT:
  QB (absent → × 0.65): always Category 1 reload
  WR1/WR2 (absent → × 0.90 passing game): significant
  RB1 (absent → × 0.92): varies by team's running scheme
  O-line (2+ absent → × 0.88): cumulative effect matters
  Pass rusher (absent → × 0.92 defence): changes pressure rate
```

## Weather and outdoor stadium intelligence

```
NFL WEATHER SIGNAL MODEL:

WIND:
  > 20 mph: apply wind modifier to passing game
    Passing efficiency reduction: × 0.88 for both QBs
    Running game beneficiary: × 1.08 for run-heavy teams
  > 30 mph: severe wind — quarterback tier matters less
    Top-tier QB advantage partially neutralised
    Apply × 0.92 across all passing modifiers
  > 40 mph: extreme — game becomes pure run/defence contest
    Apply × 0.75 to all passing-dependent signals

COLD:
  < 10°F (-12°C) with wind chill: apply cold modifier
    Ball-handling affected: fumble risk up 15-20%
    Kicker accuracy reduced: × 0.85 for > 50-yard field goals
  Cold-weather teams (Buffalo, Green Bay, Chicago in winter) have
  systematic home advantage in extreme cold: × 1.06 for home team

PRECIPITATION:
  Heavy rain/snow: similar to wind — passing game suppressed
  Apply: × 0.90 to both QBs in heavy precipitation
  Dome teams playing in outdoor elements: additional × 0.92

DOME vs OUTDOOR:
  Dome team visiting outdoor stadium in bad weather: × 0.88
  Cold-weather team at indoor dome: slight advantage neutralised — × 0.98
```

## NFL fan token market context

```
NFL TOKENS — MARKET STATUS (2025-2026):

No NFL team tokens currently on Chiliz Chain.
Architecture ready: this skill file is prepared for when NFL tokens launch.

PROJECTED MARKET CHARACTERISTICS (based on league analysis):
  NFL addressable market: 200M+ US fans; highest-value domestic sports market
  Digital engagement: NFL Mobile app, YouTube, social media = massive digital audience
  
  When tokens launch:
    Top 5 by ATM: Kansas City Chiefs, Dallas Cowboys, San Francisco 49ers,
                  New England Patriots (legacy), Philadelphia Eagles
    Super Bowl hosting city: elevated token signal during Super Bowl week
    
  SUPER BOWL SIGNAL:
    Game itself: × 2.50 signal weight (largest single-day US sports event)
    Super Bowl week: narrative_active for competing team tokens
    Host city clubs: commercial activation signal regardless of on-field performance
    
  DRAFT (April):
    First overall pick's team: immediate LTUI +15-20 (franchise impact)
    Top-5 QBs drafted: × 1.12 for drafting team's future token value
    High-profile trade-up: excitement + LTUI signal for acquiring team
```

## Integration: Full NFL pre-game workflow

```
Step 1: Load domain context
  Load sports/nfl/sport-domain-nfl.md

Step 2: QB status CHECK FIRST (most critical step in NFL)
  Is the starter active? Check Saturday inactives (game day: 90 min before)
  Backup starting: RELOAD with × 0.65 modifier immediately

Step 3: Injury report review
  get_injury_designations — all key positions
  O-line health: 2+ starters out → pass protection compromised

Step 4: Weather check
  Outdoor game with wind > 20mph: apply passing modifier × 0.88
  Cold < 10°F: fumble risk elevated, kicker signal reduced

Step 5: Matchup analysis
  get_defensive_matchup — opponent coverage vs this team's WR1
  get_oline_health — pass rush vs O-line matchup

Step 6: Composite modifier
  get_athlete_signal_modifier (QB × O-line × weather × matchup)
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "player": "string",
  "position": "QB|WR|RB|TE|OL|DL|LB|DB|K",
  "availability": 1.0,
  "cpoe_modifier": 1.08,
  "clutch_modifier": 1.05,
  "weather_modifier": 0.92,
  "matchup_modifier": 0.95,
  "composite_modifier": 1.00,
  "adjusted_direction": "NEUTRAL",
  "key_risks": ["Wind 28mph — passing game suppressed"],
  "modifier_reason": "Elite QB but weather significantly neutralises passing advantage"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `qb_tier_modifier` | QB tier classification | 0.65–1.22 |
| `cpoe_modifier` | `get_qb_metrics` | 0.92–1.10 |
| `weather_modifier` | Weather check | 0.75–1.00 |
| `oline_health_modifier` | `get_oline_health` | 0.82–1.05 |
| `injury_modifier` | `get_injury_designations` | 0.65–1.00 |
| `composite_modifier` | Product of all applicable | 0.55–1.25 |


*MIT License · SportMind · sportmind.dev*
