# Cricket — Athlete Intelligence

Player-level intelligence for cricket fan tokens (IPL, ICC, BBL, The Hundred). Covers batter vs bowler head-to-head, pitch conditions, batting/bowling metrics, DRS patterns, and fatigue.

**Applicable tokens:** Any cricket team tokens on Chiliz (architecture ready for IPL expansion).

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_batter_vs_bowler` | Historical head-to-head: average, SR, dismissal mode | Yes |
| `get_pitch_conditions` | Surface, weather, toss impact, dew factor | Yes |
| `get_batting_profile` | Phase-specific batting, boundary %, dot ball % | Yes |
| `get_bowling_profile` | Economy by phase, wickets, dismissal modes | Yes |
| `get_drs_patterns` | LBW susceptibility, caught-behind tendencies | Yes |
| `get_player_availability` | Injury, fatigue, selection status | Yes |
| `get_player_form_score` | Rolling form over last N innings/matches | Yes |
| `get_athlete_signal_modifier` | Composite cricket modifier | Yes |

---

## Key metrics

### `get_batter_vs_bowler`
```json
{
  "batter": "Virat Kohli",
  "bowler": "Jasprit Bumrah",
  "format": "T20",
  "balls_faced": 84,
  "runs": 62,
  "dismissals": 4,
  "batting_average": 15.5,
  "strike_rate": 73.8,
  "boundary_pct": 18.0,
  "dot_ball_pct": 42.0,
  "dismissal_modes": ["caught behind x2", "LBW x1", "bowled x1"],
  "matchup_verdict": "BOWLER_DOMINANT",
  "signal_modifier": 0.88,
  "modifier_note": "Bumrah historically dominant vs Kohli — significant containment expected"
}
```

### `get_pitch_conditions`
```json
{
  "venue": "Wankhede Stadium, Mumbai",
  "pitch_report": "BATTING_FRIENDLY",
  "spin_assistance": "LOW",
  "pace_assistance": "MODERATE",
  "dew_factor": "HIGH",
  "dew_advantage": "CHASING_TEAM",
  "toss_win_bat_first_win_rate": 0.38,
  "avg_first_innings_score": 182,
  "avg_second_innings_score_when_won": 189,
  "pitch_modifier": 1.04,
  "notes": "Heavy dew — chasing team has significant advantage. Toss critical."
}
```

### `get_batting_profile`
```json
{
  "player": "Rohit Sharma",
  "format": "T20",
  "last_10_innings": {
    "avg": 38.2,
    "SR": 148.4,
    "powerplay_SR": 162.0,
    "middle_overs_SR": 131.0,
    "death_SR": 188.0,
    "boundary_pct": 32.0,
    "dot_ball_pct": 28.0,
    "big_hits_per_innings": 3.4
  },
  "form_score": 82,
  "signal_modifier": 1.10
}
```

---

## Cricket modifier table

| Condition | Modifier |
|---|---|
| Star batter in form, batting-friendly pitch | 1.15 |
| Star bowler vs weak batting lineup | 1.12 |
| Key batter vs dominant bowler (historical) | 0.85 |
| Heavy dew, chasing team | 1.08 |
| Toss lost on turning pitch | 0.88 |
| Star player injured/rested | 0.80 |
| Bowler over-bowled (40+ overs last 3 days) | 0.88 |

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for cricket. Combines availability, batter/bowler H2H, pitch conditions, and format.

**Parameters:**
- `player_id` (required) — Player identifier
- `match_id` (optional) — specific match; defaults to next scheduled

**Returns:**
```json
{
  "player": "string",
  "format": "Test|ODI|T20",
  "availability": 1.0,
  "h2h_modifier": 1.05,
  "pitch_condition_modifier": 0.95,
  "format_specialist_modifier": 1.10,
  "composite_modifier": 1.05,
  "adjusted_direction": "NEUTRAL_POSITIVE",
  "key_risks": ["Dew factor expected — bowling first team disadvantaged"],
  "modifier_reason": "Specialist batter in favourable pitch conditions"
}
```

## Integration example

### Cricket pre-match workflow

```
# Step 1: Load domain context
Load sports/cricket/sport-domain-cricket.md

# Step 2: Check pitch report and weather (DLS/dew risk)
get_pitch_report match=[MATCH_ID]
get_weather_conditions venue=[VENUE_ID]

# Step 3: Get athlete modifiers for key players
get_athlete_signal_modifier player=[BATTER_ID] match=[MATCH_ID]
get_athlete_signal_modifier player=[BOWLER_ID] match=[MATCH_ID]

# Step 4: Decision logic
# T20/ODI: Check dew factor + toss result before entry
# Test: Check pitch type and specialist suitability
# Output: SportMind confidence schema
```

---

## IPL Franchise Intelligence

```
IPL PLAYER-TOKEN SIGNAL FRAMEWORK:

No IPL fan tokens currently exist (see market/international-cricket-cycle.md — regulatory gap).
However, IPL player performance is the highest-value cricket ATM signal globally.
When tokens launch, this framework activates immediately.

IPL AUCTION SIGNAL:
  Sold at: > ₹15 crore — star franchise signal; ATM premium justified
  Sold at: ₹5-15 crore — solid franchise asset
  Unsold / low bid: negative ATM signal regardless of historical performance
  
  Retention signal (stronger than auction):
  Club retaining a player at max retention fee = highest confidence commercial signal
  Retained players: MI (Rohit/Bumrah model), CSK (Dhoni model) = maximum franchise ATM

IPL FORMAT-SPECIFIC MODIFIERS:
  Powerplay specialist (overs 1-6):
    T20 powerplay SR > 160: modifier 1.15 (runs in powerplay drive game momentum)
  Death bowling specialist (overs 17-20):
    Economy < 9.0 in death: modifier 1.18 (death overs are the highest-leverage phase)
  Finisher (batting 5-7, death SR > 180):
    modifier 1.12 — most direct impact on match outcomes
    
  "Matchwinners" (players who individually win matches):
    These are the highest ATM players in cricket fan tokens
    Identify by: strike rate differential vs team SR, win % correlation, H2H dominance
```

## Format specialist model

```
T20 SPECIALIST:
  Optimised for 20-over game; may be liability in other formats
  High T20 SR (>145) but Test average <30: T20 only — do not apply to Tests
  Platform: IPL, T20 World Cup, BBL, PSL

ODI SPECIALIST:
  Anchoring vs acceleration balance; different to T20 pace
  Often overlap with Test specialists; more transferable than T20-only

TEST SPECIALIST:
  Pure Test batters: high average (>40) but low T20 SR — not valuable in T20 context
  Test bowlers: may be rested for T20 tournaments
  
  AGENT RULE: Format-match the player to the match being analysed.
  A Test specialist's metrics are irrelevant for an IPL analysis.
  Always confirm which format is being played before loading any modifier.

DUAL-FORMAT PLAYERS (most valuable commercially):
  Virat Kohli, Rohit Sharma, Babar Azam: elite across all three formats
  These players have the highest ATM in cricket — metrics apply regardless of format
  modifier: 1.15-1.20 for elite dual-format players in their home conditions
```

## Indian player ATM framework

```
INDIA PLAYER ATM TIERS:

Tier 1 — National icons (ATM 0.90-0.95):
  Virat Kohli, Rohit Sharma: global icons; metrics in any format carry maximum signal
  Social following: 200M+ combined; independent of club/team
  APS: 0.85+ (commercial identity transcends any single tournament)
  
Tier 2 — IPL franchise stars (ATM 0.75-0.85):
  Jasprit Bumrah, Hardik Pandya, Suryakumar Yadav
  Franchise-linked ATM: strong for their IPL club; moderate for national team
  
Tier 3 — Format specialists (ATM 0.55-0.70):
  Test specialists (not regular T20 squad), domestic T20 stars not in national squad
  
Tier 4 — Emerging players (ATM 0.35-0.50):
  Under-25 IPL debutants; domestic standouts awaiting national selection

INDIA-PAKISTAN MATCH ATM:
  Any India player's ATM doubles during India-Pakistan matches
  This is not an exaggeration — 400-500M viewer context amplifies every individual signal
  Apply × 2.00 to all Indian player ATM calculations during Ind-Pak matches
```

## Bowler intelligence

```
BOWLING PHASE INTELLIGENCE:

POWERPLAY BOWLERS (overs 1-6):
  Expected to set up match with early wickets
  Economy target: < 8.0 runs/over (T20 powerplay average ~8.5)
  Wicket probability: >20% per over in powerplay = elite

MIDDLE OVERS (overs 7-15):
  Spin and variations dominate
  Economy target: < 7.5 runs/over
  Dot ball % > 35% = significant pressure signal

DEATH BOWLERS (overs 16-20):
  Most financially valuable bowling skill in T20 cricket
  Economy target: < 9.0 runs/over at death (average is ~11.0)
  Top death bowler: modifier 1.18 (premium talent, hardest skill to find)
  
OVER-BOWLED SIGNAL:
  Bowler who has bowled 40+ overs in last 3 days:
  Apply × 0.88 fatigue modifier — pace decreases, accuracy suffers
  Critical: IPL schedule sometimes forces fatigue situations
```
