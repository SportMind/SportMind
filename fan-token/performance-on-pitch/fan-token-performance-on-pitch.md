---
name: performance-on-pitch
description: >
  Deep statistical performance analysis for footballers covering match data, advanced
  metrics, positional benchmarking, form trajectories, injury history, and AI-driven
  performance forecasting. Use this skill whenever the user asks about a player's
  statistics, match performance, how a player is performing this season, positional
  comparisons, expected goals, pressing metrics, defensive actions, physical data,
  whether a player is in form or out of form, how a player has performed after a transfer
  or injury return, or any request for statistical evidence about a footballer's quality.
  Also trigger for squad analysis, scouting reports, player comparison requests, or
  "is [player] worth [fee]" questions where performance data provides the answer. Feeds
  transfer-intelligence (valuation), brand-score (performance credibility multiplier),
  and performance-off-pitch (context for training and loan analysis).
---

# Performance On-Pitch

Statistical performance intelligence for footballers — from basic match stats to
advanced expected metrics, physical benchmarks, and AI-driven form forecasting.

## What this skill produces

- **Performance Index (PI)** — Overall on-pitch quality score for position (0–100)
- **Form Trajectory** — Last 5 / 10 / 20 match trend with momentum indicator
- **Positional Benchmark** — How does this player rank vs. peers in their league?
- **Advanced Metrics Profile** — xG, xA, progressive carries, pressing intensity, etc.
- **Physical Profile** — Distance covered, sprint counts, high-intensity runs
- **Injury Risk Flag** — Load patterns, return-from-injury context, historical injury profile
- **Scout Report Summary** — Strengths, weaknesses, tactical best-fit scenarios
- **Valuation Multiplier** — Performance-based adjustment for transfer-intelligence

---

## Data sources

### Primary statistics
- **API-Football** (via RapidAPI): `https://api-football-v1.p.rapidapi.com/v3`
  - `/players?id={id}&season={year}` — goals, assists, passes, cards, minutes
  - `/fixtures/players?fixture={id}` — per-match breakdown
  - `/players/topscorers?league={id}&season={year}` — league context
- **FBref** (StatsBomb-powered, public): advanced metrics for top leagues
  - Progressive passes, carries, xG, xA, pressing stats, defensive actions
  - Access via web scrape or data export (research/commercial licensing available)
- **Sofascore API** (unofficial): ratings, heatmaps, match event data
  - `https://api.sofascore.com/api/v1/player/{id}/statistics/season/{id}`
- **Opta** / **StatsBomb** (commercial): premium detailed event data
  - Required for top-tier analysis; licence required

### Physical data
- **Tracab / ChyronHego**: tracking data (club/league partnership required)
- **STATSports / Catapult**: GPS load data (direct club partnership required)
- **API-Football**: basic physical stats (distance, duels) available via standard API

### Injury history
- **Transfermarkt** injury history: `https://transfermarkt-api.fly.dev/players/{id}/injuries`
- **PhysioRoom.com** (public): historical injury records

---

## Workflow

### Step 1 — Resolve player and season context
1. Accept: player name + optional (club / league / season)
2. Resolve to API-Football player ID and current season
3. Identify position (affects which metrics are primary)
4. Fetch: current season stats + last 3 seasons for trend context

### Step 2 — Compute Performance Index (PI)

PI is position-weighted. Each position has a different metric priority:

**Forwards / Attackers:**
```
PI = (
  goals_per_90 / position_median_g90     * 0.25 +
  xG_per_90 / position_median_xG90       * 0.20 +
  shot_on_target_pct                     * 0.15 +
  key_passes_per_90                      * 0.15 +
  dribble_success_pct                    * 0.15 +
  pressing_intensity_score               * 0.10
) * 100
```

**Midfielders (central):**
```
PI = (
  pass_completion_pct / median_pct       * 0.20 +
  progressive_passes_per_90             * 0.20 +
  chances_created_per_90                * 0.15 +
  duels_won_pct                         * 0.15 +
  pressing_score                        * 0.15 +
  xA_per_90 / median_xA90               * 0.15
) * 100
```

**Defenders (centre-back):**
```
PI = (
  aerial_duel_win_pct                   * 0.20 +
  tackles_interceptions_per_90          * 0.20 +
  progressive_carries_per_90            * 0.15 +
  pass_completion_pct (long balls)      * 0.15 +
  dribbled_past_per_90 (inverted)       * 0.20 +
  errors_leading_to_shots (inverted)    * 0.10
) * 100
```

**Fullbacks:**
```
PI = (
  progressive_carries_per_90            * 0.20 +
  crossing_accuracy                     * 0.15 +
  tackles_per_90                        * 0.15 +
  key_passes_per_90                     * 0.15 +
  dribble_success_pct                   * 0.15 +
  defensive_actions_per_90              * 0.20
) * 100
```

**Goalkeepers:**
```
PI = (
  save_pct                              * 0.25 +
  PSxG_minus_GA (post-shot xG)          * 0.25 +
  pass_launch_pct / median              * 0.15 +
  clean_sheet_pct                       * 0.15 +
  crosses_claimed_pct                   * 0.10 +
  distribution_accuracy                 * 0.10
) * 100
```

PI bands: Elite (85–100), Premium (70–84), Quality (55–69), Average (40–54), Below average (<40)

### Step 3 — Form Trajectory
Compute PI per match for the last 20 appearances.
```
form_5  = avg(last 5 match PIs)
form_10 = avg(last 10 match PIs)
form_20 = avg(last 20 match PIs)

momentum = form_5 - form_20
  > +5:  Strongly rising form
  +2–5:  Rising
  -2–+2: Stable
  -5–-2: Declining
  < -5:  Sharp decline — investigate cause
```

Cross-reference sharp declines with: injury return, manager change, position change,
transfer rumour distraction, personal events (where publicly known).

### Step 4 — Positional Benchmark
Rank the player among all players of the same position in the same league (current season):
- Overall PI percentile
- Top 5 comparator players (similar PI range) with their key differentiating metrics
- Identify: which metrics is this player elite at? Which are below peer average?
- Gap analysis: largest single improvement opportunity

### Step 5 — Advanced Metrics Profile
Pull from FBref (where available for the league):

```
OFFENSIVE
  Non-penalty xG per 90
  Shots on target %
  Progressive carries per 90
  Successful dribbles per 90
  Shot-creating actions per 90
  Key passes per 90

DEFENSIVE
  Pressures per 90
  Pressure success rate
  Tackles won per 90
  Interceptions per 90
  Ball recoveries per 90
  Aerial duels won %

PASSING & BUILD-UP
  Pass completion %
  Progressive passes per 90
  Passes into final third per 90
  Through balls per 90
  Long ball completion %

PHYSICAL (where available)
  Distance covered per match (km)
  High-intensity distance per match
  Sprint count per match
  Top speed recorded
```

### Step 6 — Injury Risk Flag
Pull injury history from Transfermarkt:
- Total injury days in last 3 seasons
- Injury type pattern (muscular = recurrence risk, structural = long-term concern)
- Current season: matches played vs. matches available (availability %)
- Recent return from injury: within last 8 weeks → flag as load management risk

```
injury_risk = (
  injury_days_per_season / 30 * 0.40 +       # days out per season (30d = high risk)
  recurrent_injury_type_flag * 0.30 +         # same injury type twice = elevated
  age_factor * 0.20 +                         # 30+ = higher injury risk
  recent_return_flag * 0.10                   # <8 weeks post-return = monitor
)
```

Bands: Low (<25) / Medium (25–50) / Elevated (50–75) / High (>75)

### Step 7 — Scout Report Summary
Synthesise into a human-readable format for a scout or analyst:

Structured as:
```
STRENGTHS (top 3 metrics above 75th percentile for position)
WEAKNESSES (bottom 3 metrics below 40th percentile for position)
TACTICAL BEST-FIT (formation and role where this player excels)
TACTICAL CONCERN (formations or styles that would expose weaknesses)
COMPARABLE PLAYERS (2–3 current players with similar profiles)
DEVELOPMENT TRAJECTORY (for U25: where could this player improve most?)
```

### Step 8 — Format output

```
PERFORMANCE ON-PITCH — [ATHLETE NAME]
Club: [CLUB]  |  Position: [POS]  |  Season: [YEAR]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Performance Index (PI):          82 / 100  [Premium]
League percentile (position):    Top 14% of forwards in La Liga
Form trajectory:                 Rising (+6 momentum — best 5 matches of season)
Injury risk:                     Low (18/100) — full availability this season

ADVANCED METRICS  (per 90, percentile vs La Liga forwards)
  Non-penalty xG:    0.52   [88th pct]  ←  elite finishing
  Progressive carries: 3.1  [71st pct]
  Pressing intensity:  18.4  [65th pct]  — solid but not elite
  Key passes:          1.2   [58th pct]  — room to grow as creator
  Dribble success:     62%   [79th pct]

POSITIONAL BENCHMARK
  Comparable players: [Peer A] PI:84, [Peer B] PI:79, [Peer C] PI:78
  Above peers: Finishing efficiency (+12%), aerial threat
  Below peers:  Chance creation (-8%), pressing in final third (-11%)

SCOUT REPORT SUMMARY
  Strengths:   Elite penalty box finishing, aerial dominance, hold-up play
  Weaknesses:  Pressing intensity drops in away games, limited left foot
  Best fit:    Target forward in 4-2-3-1 or second striker in 4-4-2
  Concern:     High-press systems would expose limited tracking back

PHYSICAL  (where available)
  Distance/match:  10.8km  |  Sprints: 24  |  High-intensity: 1.2km

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Valuation multiplier for transfer-intelligence: +8% (above-median PI, rising form)
→ Run performance-off-pitch for training load and loan context
→ Run brand-score — strong PI adds +12 credibility premium to commercial value
```

---

## Multi-player comparison mode

When asked to compare two or more players:
1. Run full PI + metrics for each
2. Create side-by-side profile
3. Identify: which player is better suited for which system?
4. For transfers: "buying club plays X system — which player fits better?"

---

## Reference files

- `references/advanced-metric-definitions.md` — Detailed definition of every metric used
- `references/position-weights.md` — Full PI formula variants per position *(planned)*
- `references/league-benchmarks.md` — Median and percentile data by league/position *(planned)*
- `references/injury-type-risk.md` — Injury classification and recurrence probability data *(planned)*

---

## Environment variables

```
RAPIDAPI_KEY=<key>              # API-Football
STATSBOMB_USER=<user>           # StatsBomb Open Data (free) or commercial
STATSBOMB_PASS=<pass>
OPTA_API_KEY=<key>              # Optional premium data
```
