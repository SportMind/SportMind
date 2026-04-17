---
name: standings-intelligence
description: >
  League table position intelligence framework for SportMind agents.
  Transforms raw standings data into actionable signal inputs: table
  trajectory (rising, stable, falling), season-arc phase (title race,
  European qualification, relegation battle, mid-table stability),
  proximity thresholds for meaningful position changes, and the
  commercial implications of standings changes for fan token signal
  chains. Produces a Standings Intelligence Brief (SIB) that feeds
  directly into pre-match SMS computation and the gc_standings MCP
  tool. Cross-sport: football (Premier League, La Liga, Bundesliga,
  MLS, and equivalents), basketball (NBA standings and playoff seeding),
  ice hockey (NHL points race), American football (NFL divisional
  standings), and any league competition with table-based qualification.
  Fan token application: standings position is a primary driver of
  LTUI trajectory — a title charge sustains elevated holder engagement
  for weeks; a relegation battle creates commercial uncertainty that
  suppresses CDI regardless of match results.
---

# Standings Intelligence — SportMind

**Where a team sits in the table tells you something. Which direction
they are moving tells you much more.**

Raw standings data — position, points, goal difference — is widely
available and already priced into pre-match signals by the market.
SportMind's standing intelligence framework extracts the signal that
is not priced: trajectory, proximity to threshold events, and the
commercial arc implications of where a team is heading.

---

## The Standings Intelligence Brief (SIB)

```
SIB = {
  current_position:         integer
  points:                   integer
  trajectory:               RISING | STABLE | FALLING | VOLATILE
  season_arc_phase:         one of six phases (see below)
  proximity_flags:          active thresholds within reach
  commercial_signal:        effect on CDI and LTUI
  pre_match_modifier:       SMS adjustment from standings context
}

HOW SIB FEEDS THE SIGNAL CHAIN:
  1. Load SIB before pre-match SMS computation
  2. Apply proximity_flags as context for match importance
  3. Apply commercial_signal to CDI / LTUI for fan token chain
  4. Cross-reference with CQS (season_position dimension = 0.10 weight)
  Note: SIB enhances context; it does not override the six-step chain
```

---

## Trajectory model

```
TRAJECTORY is computed from the last 5 match points vs season average:

  last_5_ppg = points from last 5 matches / 5
  season_ppg  = total points / matches played

  last_5_ppg ≥ season_ppg + 0.40:  RISING   (meaningfully above average)
  last_5_ppg ≥ season_ppg − 0.25:  STABLE   (within normal variance)
  last_5_ppg ≤ season_ppg − 0.40:  FALLING  (meaningfully below average)
  Alternating wins/losses pattern:  VOLATILE (inconsistent form)

TRAJECTORY MODIFIES MATCH SIGNAL:
  RISING + home fixture:    +3 SMS points (confidence boost)
  FALLING + away fixture:   −3 SMS points (vulnerability signal)
  VOLATILE:                 no SMS modifier; flag for human context
  STABLE:                   no SMS modifier (baseline)

TRAJECTORY HALF-LIFE: 3 matches
  If trajectory reverses over next 3 matches, reclassify.
  Do not carry a RISING label from 6 weeks ago into today's analysis.
```

---

## Six season arc phases

```
PHASE 1 — TITLE RACE (top 2, within 7 points of leader, 15+ matches remaining)
  Definition: Team has a realistic mathematical chance of winning the title
  Commercial effect: CDI elevation +15–25 points, LTUI positive trajectory
  Pre-match: every match becomes high-stakes; CQS season_position = 1.30
  Fan token: HAS sustains elevated levels; LTUI expected to continue rising
  Exits: mathematically eliminated from title race → transition to Phase 2 or 3

PHASE 2 — EUROPEAN QUALIFICATION RACE (position 3–7, within 3 of threshold, 12+ remaining)
  Definition: Within reach of a European competition place
  Commercial effect: CDI moderate elevation +8–15 points
  Pre-match: matches near 6-match window carry elevated weight
  Fan token: LTUI stable to positive; holder sentiment elevated if trajectory RISING
  Exits: confirmed European place → PHASE 5; fall to 10+ from threshold → PHASE 6

PHASE 3 — RELEGATION BATTLE (bottom 3, or within 3 points of zone, 12+ remaining)
  Definition: Realistic threat of relegation
  Commercial effect: CDI suppression −10–20 points; holder uncertainty elevated
  Pre-match: every match is high-stakes; tactical approach typically more defensive
  Fan token: LTUI at risk; long-term supply trajectory uncertain
  Critical: PATH_2 WIN burns continue regardless of league position, but
            season win frequency may drop → slower cumulative supply reduction
  Manager sacking probability elevated → raise MgSI flag for opponent analysis

PHASE 4 — ACTIVE RELEGATION (bottom 3, mathematically in danger, final 10 matches)
  Definition: In relegation zone with insufficient matches to recover easily
  Commercial effect: CDI suppressed −25–35 points; LTUI reset risk active
  Pre-match: extreme importance; strong home advantage due to emotional intensity
  Fan token: LTUI negative trajectory; holder churn begins; Speculators exit first
  Note: Relegation confirmed → CALENDAR_COLLAPSE equivalent for domestic signals

PHASE 5 — CONFIRMED QUALIFICATION / SAFETY (secured position, cannot change materially)
  Definition: Title won, European place secured, or relegation mathematically impossible
  Commercial effect: CDI normalises to baseline unless title race continues
  Pre-match: remaining matches may become dead rubbers → CQS drops
  Fan token: LTUI stable; maintenance mode until next season narrative begins
  DEAD_RUBBER_FLAG: if confirmed safe + no European place → flag matches as lower weight

PHASE 6 — MID-TABLE STABILITY (no meaningful threshold within reach)
  Definition: Position between phases — too far from top for European, too far from bottom
  Commercial effect: CDI at baseline; no elevation or suppression from standings
  Pre-match: standard analysis; no standings modifier applied
  Fan token: LTUI requires non-standings drivers (cup runs, transfers, player stories)
```

---

## Proximity threshold flags

```
TITLE WITHIN REACH:
  Within 7 points of first with ≥ 15 matches remaining
  → Raise: TITLE_RACE_ACTIVE
  → Commercial: sustained LTUI elevation expected

TITLE CLINCHED THIS MATCH:
  Win would clinch title mathematically
  → Raise: TITLE_CLINCH_POSSIBLE
  → CQS amplifier: maximum (1.35–1.40)
  → Fan token: single highest-value WIN burn event of the season

CHAMPIONS LEAGUE SPOT THIS MATCH:
  Win would confirm top-4 / top-3 / UCL place (league-specific)
  → Raise: UCL_CONFIRMATION_POSSIBLE
  → Pre-match importance elevated; FTIS amplified

RELEGATION ESCAPE THIS MATCH:
  Win would move team above relegation zone
  → Raise: RELEGATION_ESCAPE_POSSIBLE
  → Massive home crowd pressure; defensive tactical approach likely
  → Fan token: CDI recovery signal if team escapes

RELEGATED THIS MATCH:
  Combination of results could confirm relegation
  → Raise: RELEGATION_CONFIRMATION_POSSIBLE
  → CQS suppressed regardless of match quality
  → Fan token: prepare LTUI_RESET_SIGNAL on confirmation

RECORD PURSUIT:
  Win would set points record (for this team or league all-time)
  → Raise: RECORD_IN_SIGHT
  → Commercial signal only; no SMS modifier

PROMOTED THIS MATCH (lower divisions):
  → Raise: PROMOTION_POSSIBLE
  → Commercial arc reset; new LTUI trajectory begins
```

---

## Cross-sport standings application

```
FOOTBALL (Premier League / La Liga / Bundesliga / Serie A / Ligue 1):
  Thresholds: top 4 = UCL; 5 = UEL; 6 = UECL (varies by league/season)
  Relegation zone: bottom 3 of 20 (PL), bottom 3 of 18 (Bundesliga)
  Points per win: 3 | Draw: 1 | Loss: 0
  SIB: fully applicable as described above

NBA (Basketball):
  Standings determine playoff seeding (1–8 each conference)
  Play-in: positions 7–10 compete for final two playoff spots
  Threshold flags:
    TOP_SEED_POSSIBLE: home court advantage in playoffs
    PLAY_IN_ZONE: positions 7–10 (extra risk — must win extra game)
    ELIMINATED: mathematically cannot make playoffs
  Commercial: playoff race = sustained LTUI elevation (NBA equivalent of UCL chase)
  Play-in tournament = CALENDAR_COLLAPSE equivalent if team loses

NHL (Ice Hockey):
  Wild card spots: top 3 in division + 2 wild cards per conference
  Points system: Win=2, OT Loss=1, Regulation Loss=0 (different from football)
  Threshold flags:
    PLAYOFF_SPOT_THIS_GAME: win clinches playoff berth
    WILD_CARD_CHASE: within 3 points of wild card spot
    LOTTERY_BOUND: eliminated from playoffs (draft lottery implications)
  Note: NHL standings tighter than football — apply trajectory model weekly not monthly

NFL (American Football):
  Division winner = guaranteed playoff spot; 3 wild cards per conference
  Season only 17 regular season games → every game more impactful
  Apply SIB from Week 10 onward (first 9 weeks too early for proximity)
  Threshold flags:
    DIVISION_CLINCH_POSSIBLE: win clinches division
    WILD_CARD_CHASE: within 1 game of wild card
    ELIMINATED: mathematically cannot reach playoffs

MLS (Major League Soccer):
  Top 9 each conference qualify for playoffs (from 15 teams)
  Supporter's Shield: best regular season record (separate trophy)
  Apply standard six-phase model with 9-team threshold instead of 4

RELEGATION LEAGUES NOT APPLICABLE:
  NBA, NHL, NFL, NBA — no relegation mechanics
  Set PHASE to STABLE or appropriate playoff-equivalent phase
  Do NOT apply RELEGATION flag sets
```

---

## Pre-match SMS integration

```
STANDINGS MODIFIER RULES:

Apply when standings context materially changes match importance:

  Phase 1 (Title Race), home team:          +4 SMS
  Phase 1 (Title Race), away team:          +2 SMS
  Phase 3 (Relegation Battle), home team:   +5 SMS (desperation factor)
  Phase 3 (Relegation Battle), away team:   +3 SMS
  Phase 4 (Active Relegation), home team:   +7 SMS (maximum desperation)
  TITLE_CLINCH_POSSIBLE, any team:          +6 SMS
  TITLE_CLINCH_POSSIBLE, opposition:        +4 SMS (try to deny title)
  RELEGATION_ESCAPE_POSSIBLE, home:         +8 SMS
  Phase 6 (Mid-table, dead rubber risk):    −4 SMS
  DEAD_RUBBER confirmed:                    −8 SMS

TRAJECTORY MODIFIER (applied after phase modifier):
  RISING trajectory adds +3 | FALLING trajectory adds −3

MAXIMUM COMBINED STANDING MODIFIER: ±12 SMS
  Floor rule: standings modifier cannot reduce SMS below 20
  Ceiling rule: standings modifier cannot increase SMS above 95

AGENT RULE:
  Load SIB before sportmind_pre_match for any match where either team
  is within 5 positions of a meaningful threshold.
  For mid-table matches far from all thresholds: standings context minimal.
```

---

## Fan token commercial integration

```
LTUI TRAJECTORY FROM STANDINGS:

  Title race (Phase 1):       LTUI trajectory = STRONGLY POSITIVE
  European chase (Phase 2):   LTUI trajectory = POSITIVE
  Mid-table (Phase 6):        LTUI trajectory = NEUTRAL (requires other drivers)
  Relegation battle (Phase 3):LTUI trajectory = UNCERTAIN (depends on exit)
  Relegated (confirmed):      LTUI trajectory = NEGATIVE; phase reset next season

CDI ADJUSTMENT FROM STANDINGS:
  Title race week:       CDI +20 (days of engagement sustained)
  Title clinch week:     CDI +35 (peak commercial event, short-lived burst)
  Relegation battle:     CDI −15 (uncertainty suppresses engagement)
  Relegated:             CDI −30 (structural decay begins)

HOLDER BEHAVIOUR BY STANDINGS PHASE:
  LOYALIST: responds most strongly to title race narrative; stays through relegation
  SPECULATOR: exits early in relegation battle; re-enters on title race entry
  GOVERNOR: most active in stability (Phase 5/6) — stable governance engagement
  AMPLIFIER: peaks on title clinch, record moments; fades in mid-table

PATH_2 NOTE:
  Standings phase does NOT change PATH_2 mechanics.
  WIN = burn regardless of league position.
  But in a relegation battle, win frequency may drop → slower cumulative reduction.
  Model this as: season_win_rate_adjusted = base_win_rate × relegation_difficulty_factor
  relegation_difficulty_factor: bottom-3 schedule vs remaining = typically 0.78–0.88
```

---

## SIB output schema

```json
{
  "sib_brief": {
    "club":          "Arsenal",
    "league":        "Premier League",
    "assessed_at":   "2026-04-17T00:00:00Z",
    "matches_played": 32,
    "matches_remaining": 6
  },

  "current_position": {
    "position":       3,
    "points":         68,
    "goal_difference":"+31",
    "points_behind_leader": 7,
    "points_above_relegation": 38
  },

  "trajectory": {
    "label":          "RISING",
    "last_5_ppg":     2.4,
    "season_ppg":     2.13,
    "last_5_results": ["W","W","D","W","W"]
  },

  "season_arc_phase": "PHASE_2_EUROPEAN_QUALIFICATION",

  "proximity_flags": [
    "UCL_CONFIRMATION_POSSIBLE: win + City draw = UCL spot confirmed",
    "TITLE_MATHEMATICALLY_POSSIBLE: 7 points from leader, 6 matches remaining"
  ],

  "pre_match_modifier": {
    "phase_modifier":      "+2",
    "trajectory_modifier": "+3",
    "total_sms_adjustment":"+5",
    "note":               "Applied when Arsenal are the team being analysed"
  },

  "commercial_signal": {
    "ltui_trajectory":   "POSITIVE",
    "cdi_adjustment":    "+10",
    "holder_note":       "Speculator interest elevated; title narrative sustaining engagement",
    "path2_note":        "Win rate elevated (RISING trajectory); projected 3–4 more burns this season"
  },

  "plain_english": "Arsenal are in a strong run — 4 wins from 5 — and sitting 7 points off the title with 6 games left. Mathematically alive but needing help. More importantly for the fan token, a UCL confirmation this weekend would lock in European football next season and sustain the commercial arc. The 3 remaining HOME games this season all carry elevated importance.",

  "sportmind_version": "3.69.0"
}
```

---

*SportMind v3.69 · MIT License · sportmind.dev*
*See also: core/contextual-signal-environment.md (season_position dimension)*
*fan-token/fan-token-lifecycle/ · fan-token/fan-sentiment-intelligence/*
*fan-token/gamified-tokenomics-intelligence/ · scripts/sportmind_gc_mcp.py*
*core/core-fixture-congestion.md · core/breaking-news-intelligence.md*
