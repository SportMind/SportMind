# Basketball Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-basketball.md`.
Active Chiliz fan tokens include NBA and EuroLeague clubs.
NBA statistics infrastructure is the most mature in team sports.

Zero-dependency. NBA Stats API and Basketball-Reference are free.

---

## Overview

Basketball has the richest publicly available team statistics infrastructure
of any sport. Advanced metrics like Offensive Rating, Defensive Rating, True
Shooting %, and Net Rating have been validated across decades of NBA data.

The key insight for fan token signal purposes: basketball statistics are
better predictors at the **series level** (playoff series) than the game
level, because individual game variance in basketball is relatively high.
A good team loses individual games frequently; they win series consistently.

Load `core/match-statistics-intelligence.md` for universal modifier framework.

---

## Domain Model

### Statistics hierarchy for basketball signal impact

```
TIER 1 — OUTCOME-CORRELATED:

  NET RATING (points scored minus allowed per 100 possessions):
    The single most predictive team metric across both regular season and playoffs.
    > +8.0: elite team — apply × 1.12 to signal
    +4.0 to +8.0: strong team — apply × 1.06
    0 to +4.0: above average — apply × 1.03
    -4.0 to 0: below average — apply × 0.97
    < -4.0: struggling — apply × 0.92

  TRUE SHOOTING % (TS%):
    Measures shooting efficiency accounting for 3-pointers and free throws.
    > 59%: elite efficiency — apply × 1.08
    56–59%: above average — apply × 1.04
    < 53%: below average — apply × 0.94

  OFFENSIVE RATING (points scored per 100 possessions):
    > 118: elite offence — apply × 1.08 to offensive signal
    110–118: above average — neutral modifier
    < 105: struggling offence — apply × 0.92

  DEFENSIVE RATING (points allowed per 100 possessions — lower is better):
    < 108: elite defence — apply × 1.08 to defensive signal
    108–114: average — neutral modifier
    > 118: poor defence — apply × 0.92

  PACE (possessions per 48 minutes):
    Critical for matchup analysis — fast-paced team vs slow-paced team.
    Pace differential between opponents: high-variance signal.
    Fast team (> 100 pace) vs slow team (< 97 pace): apply × 0.90 to fast team
    (their advantage is neutralised; slow team controls pace).

TIER 2 — CONTEXTUAL:

  REBOUND DIFFERENTIAL:
    Teams controlling rebounds control possessions — second chance points signal.
    Offensive rebound rate > 30%: × 1.05 second-chance scoring signal.
    
  FREE THROW RATE AND CONVERSION:
    Getting to the line is a Tier 2 signal — converts team pressure to points.
    FTr (free throw rate) > 0.30: apply × 1.04 (pressure converted to fouls).
    FT% > 80%: maximises conversion; < 70%: gifting possessions back.

  ASSIST-TO-TURNOVER RATIO:
    > 2.0: controlled offence — ball movement signal.
    < 1.5: turnover-prone — apply × 0.96 to ball-movement signal.

TIER 3 — DESCRIPTIVE:
  Raw points per game (without pace adjustment)
  Raw rebounds (without per-possession adjustment)
  Win/loss record without strength-of-schedule context
```

### Individual player statistics for fan token signals

```
PLAYER-TOKEN CORRELATION IN BASKETBALL:
  Basketball has the highest player-token correlation of any team sport.
  A single player can change an NBA team's win probability by 15–20%.
  This makes individual player statistics critical for token signal.

  SUPERSTAR MODIFIER:
    Top-5 global basketball player (consensus, based on PER and Win Shares):
      Available: × 1.15 to team signal
      Out (injury confirmed): × 0.80 to team signal (highest ATM reduction
      of any team sport — basketball is the most top-heavy in player value)
    
  PER (Player Efficiency Rating):
    > 25.0: MVP-calibre season — top-line contributor
    21–25: All-Star level — significant modifier
    18–21: Solid starter — moderate modifier
    < 15: Role player — minimal individual signal

  BOX PLUS/MINUS (BPM):
    Player's impact per 100 possessions relative to a replacement player.
    > +6.0: elite — apply × 1.10 individual modifier
    +3.0 to +6.0: above average — apply × 1.05
    < 0.0: replacement-level contribution — apply × 0.92

  USAGE RATE AND PERFORMANCE:
    High usage (> 28%) + high TS% (> 58%): elite shot creator — × 1.12
    High usage + low TS% (< 53%): inefficient — × 0.90
    (High volume, low efficiency is the most common poor-signal indicator)

KEY PLAYER ABSENCE FRAMEWORK:
  Starting point guard / primary ball handler missing:
    Apply × 0.88 team signal modifier (organising role is high-leverage)
  Primary scoring wing missing:
    Apply × 0.85 team signal modifier
  Star centre (inside-out threat) missing:
    Apply × 0.82 team signal modifier
  Any two starters missing simultaneously:
    Apply × 0.75 team signal modifier — minimum two-person threshold
```

### Playoff-specific statistics

```
PLAYOFF SIGNAL ADJUSTMENT:

  Regular season statistics require adjustment for playoff context because:
  1. Opponents are better — defence intensity increases 15–20%
  2. Game plan specificity — scouting removes some offensive advantages
  3. Fatigue across a series — statistics decline in games 6–7 of a series

  PLAYOFF ADJUSTMENTS (apply to regular season statistics for playoff signals):
    Offensive Rating: reduce by 4–6 points for playoff estimate
    TS%: reduce by 2–3 percentage points
    Net Rating: the most stable metric — retains ~80% of regular season value
    
  SERIES CONTEXT MODIFIERS:
    Won previous series 4–0 or 4–1 (rested): × 1.05 playoff signal
    Won previous series 4–3 (fatigued/tested): × 0.95
    Home court advantage: × 1.06 in first round (fan atmosphere + schedule)
                          × 1.04 in conference finals (higher quality neutralises)
                          × 1.03 in Finals (highest quality reduces advantage)

  ELIMINATION GAME SIGNAL:
    A team facing elimination performs differently statistically.
    Historically: teams facing elimination (must-win) win ~46% of the time.
    Do not automatically favour the non-eliminated team — desperation is real.
    Apply × 1.04 to the elimination-facing team if they have elite Net Rating.
```

---

## Event Playbooks

### Playbook 1: Game signal with Net Rating
```
trigger:  Regular season or playoff game for monitored team token
timing:   T-2h
protocol:
  1. Pull Net Rating for both teams (last 20 games for regular season)
  2. Check for key player absence (starting lineup confirmed T-1h)
  3. Apply pace differential modifier if significant (> 5 possession difference)
  4. Apply home court advantage (regular season × 1.06; playoff see above)
  5. Generate signal with net_rating_differential noted
output:   Game signal with statistical_modifiers_applied
```

### Playbook 2: Playoff series entry
```
trigger:  NBA or EuroLeague playoff series matchup confirmed
timing:   T-24h to first game
protocol:
  1. Calculate season Net Rating for both teams
  2. Apply playoff adjustments (reduce ORtg by 4–6, TS% by 2–3)
  3. Check H2H regular season record (same season only)
  4. Assess home court advantage for the series
  5. Check star player health status (highest ATM impact)
  6. Generate series signal (not game signal — series level is more predictive)
output:   Series signal with game-by-game monitoring flags
note:     Series signal is the highest-confidence basketball signal
```

### Playbook 3: Trade deadline acquisition
```
trigger:  Trade confirmed for monitored team token
timing:   Trade deadline day (February) or confirmed trade date
protocol:
  1. Assess acquired player's PER and BPM (if available)
  2. If Tier 1 player acquired: apply × 1.12 CDI extension
  3. If rotation player acquired: apply × 1.05 (moderate improvement)
  4. If key player traded away: apply negative ATM modifier (× 0.85–0.88)
  5. Load athlete-modifier-system.md for full ATM calculation
output:   CDI update with trade_modifier noted
note:     Trade deadline is a major CDI event — often higher CDI impact than
          any regular season game result
```

### Playbook 4: Star player injury response
```
trigger:  Confirmed injury to key player (starting player confirmed out)
timing:   Immediately on confirmation from Tier 1 source
protocol:
  1. Classify player tier (superstar / starter / rotation)
  2. Apply appropriate absence modifier (×0.80 to ×0.88 based on tier)
  3. Load breaking-news-intelligence.md — Category 2 minimum
  4. For superstar (top-5 globally): Category 1 — RELOAD protocol
  5. Update all forward game/series signals with absence applied
output:   Updated signal with player_absent flag and ATM reduction noted
```

---

## Signal Weight Adjustments

For basketball statistics sub-module:

| Statistical modifier | Weight | Cap |
|---|---|---|
| Net Rating differential (Tier 1) | 14% additional weight | ±9 pts |
| Star player availability (ATM) | 10% additional weight | ±10 pts |
| TS% efficiency differential | 7% additional weight | ±5 pts |
| Playoff context adjustment | Applied as multiplier | ×0.80 to ×1.05 |
| Home court advantage | 5% additional weight | ±4 pts |

**Combined basketball statistical modifier cap: ±12 points on adjusted_score.**

---

## Autonomous Execution

**Trigger conditions:**
- Starting lineup confirmed for monitored game (T-1h)
- Key player confirmed absent from lineup
- Trade confirmed for monitored team token
- Playoff series result confirmed (CDI update)

**Execution at autonomy Level 2:**
- Lineup confirmed: apply star player status modifier. Notify operator.
- Key absence: apply ATM modifier. Flag "PLAYER_ABSENT_CONFIRMED". Notify.
- Trade: apply CDI modifier. Notify operator with full trade assessment.
- Playoff result: update series signal and CDI. Notify.

**Execution at autonomy Level 3–4:**
- Auto-process confirmed lineup within 10 min of publication
- Auto-dispatch CDI updates after playoff results within 20 min
- Auto-monitor team official channels for injury reports during playoffs
- Trade deadline: auto-process confirmed trades and dispatch CDI updates

**Hard boundaries:**
- Superstar absence (top-5 global): Category 1 RELOAD — human review required
  before any position signal is acted upon. No exceptions.
- Regular season statistics applied to playoff signals: must apply playoff
  adjustments. Never use raw regular season stats for playoff prediction.
- Player health information from social media / fan accounts: Tier 4 source.
  Never apply absence modifier from Tier 4 source autonomously.

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| Game signal | Load this + sport-domain-basketball.md | T-2h |
| Series signal | Playbook 2 | Playoff entry |
| Trade response | Playbook 3 + athlete-modifier | Trade deadline |
| Star injury | Playbook 4 + breaking-news | Category 1 or 2 |

---

## Agent Reasoning Prompts

- "Net Rating is the most predictive basketball metric — check it before any other statistic."
- "High usage + low TS%: inefficient volume scorer. Apply ×0.90 — not a signal-positive."
- "Playoff context: reduce regular season ORtg by 4–6 points. Defence intensifies."
- "Star player absent: basketball has the highest individual-to-team leverage ratio."
- "Series signal is more reliable than single game signal in basketball — use series level."

---

## Data Sources

- NBA Stats API (free): stats.nba.com — official advanced metrics (Tier 1)
- Basketball-Reference (free): basketball-reference.com — comprehensive historical (Tier 2)
- ESPN (free): espn.com — injury reports, lineup confirmations (Tier 2)
- EuroLeague official: euroleaguebasketball.net — EuroLeague statistics (Tier 1)
- Official team injury reports: team official accounts only (Tier 1)

---

## Compatibility

**Load alongside:** `sports/basketball/sport-domain-basketball.md`
**Universal framework:** `core/match-statistics-intelligence.md`
**Athlete layer:** `core/athlete-modifier-system.md` (star player ATM)
**Breaking news:** `core/breaking-news-intelligence.md` (star absence = Category 1)

---

*SportMind v3.91.0 · MIT License · sportmind.dev*
