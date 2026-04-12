---
name: athlete-decision-intelligence
description: >
  Intelligence framework for athlete decision-making quality as a
  player-level signal modifier. Distinct from form (output statistics),
  motivation (effort level), and perceptual pressure (how well they
  read under pressure): decision intelligence models the quality and
  efficiency of choices an athlete makes with the ball/puck/position
  in real game conditions. Produces a Decision Quality Index (DQI: 0–100)
  and modifier (0.90–1.15). Quantified primarily through: xA (expected
  assists — measures decision quality in creating chances), progressive
  carry rate and press resistance (decision under pressure in possession),
  shot selection efficiency (taking high-value vs low-value shots), and
  defensive positioning quality (anticipation vs reaction). Feeds into
  LQI as a decision-quality positional weight and into the Scouting
  Agent (Pattern 10) as an undervalued-player detection mechanism —
  high DQI players who are statistically underappreciated are the
  primary targets of value-based scouting. Cross-sport: football,
  basketball, ice hockey, cricket (batting decision quality). Load when:
  comparing players of similar technical quality, when building LQI
  for a formation-specific system, or when running Pattern 10.
---

# Athlete Decision Intelligence — SportMind

**The quality of choices an athlete makes under game conditions —
what they do with the information they perceive.**

Perceptual pressure intelligence (PPI) measures how well an athlete
*reads* the game under pressure. Decision intelligence measures what
they *do* with what they read. The two are distinct and both matter.
A player can read the game brilliantly but make poor choices (high
PPI, low DQI). A player can make consistently good choices without
appearing to read the game as a conscious skill (lower PPI, high DQI —
high automation of correct decisions).

---

## Why decision intelligence is a measurable signal

```
THE CORE INSIGHT:
  Statistics measure outputs (goals, assists, blocks).
  Decision intelligence measures the quality of the choices that
  produced those outputs — was that shot the right choice? Was that
  pass the highest-value option available at that moment?

  Two players can score the same number of goals with very different
  decision quality:
  - Player A: 12 goals from 15 high-quality chances (high shot selection,
    high xG per shot) = efficient decision-making
  - Player B: 12 goals from 30 shots of mixed quality (poor shot selection,
    takes on difficult shots) = lower decision quality despite same output

  Why this matters for SportMind:
  High DQI players are MORE valuable than their statistics show.
  Low DQI players are LESS valuable than their statistics show.
  The library's LQI currently captures available evidence and form.
  DQI adds the decision-quality layer that LQI misses.

MEASURABLE DIMENSIONS:
  1. Chance creation quality (xA — expected assists)
  2. Possession decision (press resistance, progressive action rate)
  3. Shot selection efficiency (shot quality relative to opportunities)
  4. Defensive anticipation (interceptions vs reactive tackles)
```

---

## The Decision Quality Index (DQI)

```
DQI = (Chance_Creation_Quality × 0.30)
    + (Possession_Decision × 0.25)
    + (Shot_Selection × 0.25)
    + (Defensive_Anticipation × 0.20)

Scale: 0–100
Apply only dimensions relevant to position and sport.
Non-applicable dimensions: redistribute weight equally to applicable ones.

DQI → MODIFIER:
  DQI 85–100: ×1.15  ELITE DECISION-MAKER
  DQI 70–84:  ×1.08  STRONG
  DQI 55–69:  ×1.03  ABOVE BASELINE
  DQI 40–54:  ×1.00  NEUTRAL
  DQI 25–39:  ×0.96  BELOW BASELINE — poor choice patterns
  DQI 0–24:   ×0.90  SIGNIFICANT CONCERN — systematic poor decisions

LQI INTEGRATION:
  DQI feeds into LQI as a multiplier on the base player rating:
  LQI_player_contribution = base_rating × positional_weight
                          × availability_factor × DQI_modifier
  This means a highly available, fit player with poor decisions
  contributes less than their form metric alone would suggest.
```

---

## Dimension 1 — Chance Creation Quality (xA)

```
WHAT IS xA:
  Expected Assists — the sum of xG (expected goals) of the shots
  that a player's passes/crosses/set pieces created.
  
  xA measures decision quality in the final third: did the player
  choose the pass that created a high-value chance, or a low-value one?

xA vs Assists:
  A player who creates 20 low-xG chances that all happen to be scored
  has high assists but low xA — they were lucky, not decisive.
  A player who creates 15 high-xG chances that happen to not be scored
  has low assists but high xA — they are making good decisions that
  happen to have been wasted.
  
  For future prediction, xA is far more reliable than assists.

xA SCORING (per 90 minutes, position-adjusted):
  Attacking midfielder / winger:
    xA/90 > 0.25:   90–100 (elite chance creation decisions)
    0.15–0.25:      65–89
    0.08–0.15:      40–64
    < 0.08:         10–39
  
  Central midfielder:
    xA/90 > 0.15:   90–100
    0.08–0.15:      65–89
    0.04–0.08:      40–64
    < 0.04:         10–39
  
  Striker: xA is less relevant (receiving end, not creating)
    Redistribute this dimension weight to Shot_Selection for strikers.

SOURCES: FBref (fbref.com) — xA column in player stats
  Statsbomb Open Data for high-detail analysis
  Opta/WhoScored for historical xA data
```

---

## Dimension 2 — Possession Decision

```
PRESS RESISTANCE:
  How well does a player make good decisions when pressed?
  Under pressure, the correct decision is typically: play simply,
  maintain possession, find space. Poor press resistance means:
  losing the ball, making a lateral pass under pressure (no territory
  gained), or forcing a risky forward pass.

  PRESS RESISTANCE METRIC:
  % of possessions maintained under direct opposition pressure
  Source: Statsbomb "under pressure" tags; FBref — pressured pass completion%
  
  Press resistance score:
    Pressured pass completion% > 80%: 85–100
    70–80%: 60–84
    60–70%: 35–59
    < 60%:  0–34

PROGRESSIVE ACTION RATE:
  What % of touches contribute to moving the team forward?
  Progressive carries + progressive passes as % of total actions.
  
  This measures the decision quality at the team-context level:
  not just whether a player can do the skill, but whether they
  consistently choose the high-value option in their position.

  Progressive action rate scoring (position-adjusted):
    Attacking player:   > 40% of actions progressive: 80–100
    Central midfielder: > 30% progressive: 80–100
    Defensive mid:      > 20% progressive: 80–100
    
  Source: FBref progressive carries, progressive passes columns

BASKETBALL POSSESSION DECISION:
  Assist-to-turnover ratio (A/TO) is the primary basketball DQI input.
  Elite playmakers: A/TO > 4.0
  Good decision-makers: A/TO 2.5–4.0
  Below average: A/TO < 2.0
  Source: Basketball Reference player advanced stats
```

---

## Dimension 3 — Shot Selection

```
SHOT QUALITY PER ATTEMPT:
  Average xG per shot taken.
  A player who consistently takes high-xG shots is making better
  decisions than a player who takes many low-xG long shots.

SHOT SELECTION SCORE:
  xG per shot > 0.18:  85–100 (elite shot selection)
  0.12–0.18:           60–84
  0.08–0.12:           35–59
  < 0.08:              0–34

  Source: FBref npxG/shot (non-penalty xG per shot)

SHOT SELECTION CONTEXT:
  A striker in a low-quality-chances team will have lower xG/shot
  even with excellent decision-making — they are forced into worse
  positions by the team's limited creativity. Adjust for:
  - Team's average xG creation quality per match
  - Player's xA vs assists differential (are teammates finishing?)
  
  Contextual adjustment: if team xG/shot is >15% below league average,
  apply: player xG/shot × 1.10 normalisation before scoring.

BASKETBALL SHOT SELECTION:
  True Shooting% (TS%) relative to position average.
  TS% measures the quality of shots taken + conversion.
  TS% > 5 points above position average: 85–100
  Within ±5 points: 45–65
  > 5 points below: 0–35
  Source: Basketball Reference advanced stats

CRICKET BATTING DECISION:
  The cricket equivalent of shot selection is scoring-shot %
  vs dot-ball % in pressure situations.
  A batter who converts scoring opportunities consistently (does not
  play and miss at balls they could hit) has high decision quality.
  Strike rotation — converting 1s and 2s vs leaving scoring opportunities:
  measures the same underlying decision quality in cricket terms.
```

---

## Dimension 4 — Defensive Anticipation

```
INTERCEPTIONS vs REACTIVE TACKLES:
  Interceptions require the athlete to READ the game and position
  themselves for a pass before it arrives. They are pure decision-
  intelligence events — the player anticipated and chose correctly.
  
  Tackles can be reactive — the opponent made a move and the defender
  responded. Tackles are partly skill; interceptions are primarily decision.

ANTICIPATION SCORE:
  Interception rate per 90 relative to position average:
  > 150% of position average:  85–100
  100–150%:                    55–84
  50–100%:                     25–54
  < 50% of position average:   0–24

  IMPORTANT: High tackle rate with low interception rate signals
  a reactive defensive style — high effort but lower decision quality.
  The ratio (interceptions / total defensive actions) is more informative
  than the absolute count.

  Source: FBref interceptions column

DEFENSIVE POSITIONING (positional intelligence):
  For centre-backs: progressive pass prevention (blocking passing lanes
  through positioning rather than tackles)
  For defensive midfielders: PPDA contribution (positioning in defensive
  shape that forces long balls)
  
  These are harder to quantify directly but are observable via:
  xG conceded when player is on vs off the pitch (defensive on/off splits)
  Source: FBref on/off data

BASKETBALL DEFENSIVE ANTICIPATION:
  Deflections per game and Defensive Win Shares relative to minutes played.
  Steal rate in particular is the basketball interception equivalent.
  Steal% > 2.0: high anticipation. Source: Basketball Reference.

CRICKET FIELDING DECISION:
  Diving catch attempts vs catches taken. A fielder who attempts catches
  they cannot reach has lower decision quality than one who positions
  correctly and takes straightforward chances.
  Dropped catch rate is the clearest negative signal.
```

---

## DQI and the Scouting Agent (Pattern 10)

```
THE UNDERVALUATION DETECTION USE CASE:

The Pattern 10 CVS formula combines:
  APS × 0.30 + AELS × 0.25 + DTS × 0.20 + PI × 0.15 + LTUI × 0.10

APS and AELS are commercial metrics. DTS and PI are more performance-linked.
DQI adds a decision-quality layer that identifies players whose statistical
output understates their actual decision quality — the "Moneyball" signal.

HIGH DQI + LOW TRANSFER MARKET VALUE = UNDERVALUATION SIGNAL:
  A player with DQI > 75 but a market value that does not reflect this
  (Transfermarkt value below expected for their DQI tier) is being
  undervalued by the market.

DQI_UNDERVALUATION_FLAG:
  If DQI_modifier > 1.08 AND Transfermarkt_value < league_position_average:
  flag DECISION_QUALITY_UNDERVALUED — add 8–12 points to CVS score
  Note in scouting report: "Decision metrics exceed market valuation.
  Potential value target."

DQI also feeds directly into SPATIAL_SYSTEM_FIT:
  A high-DQI player in a system that demands good decision-making
  (positional play, tiki-taka, pick-and-roll) is worth more than
  their raw statistics suggest.
  A high-DQI player in a direct system (long balls, individual battles)
  may not get full value from their decision quality.
  The fit matters.
```

---

## Cross-sport application summary

```
FOOTBALL:
  Primary metrics: xA/90, pressured pass completion%, xG/shot, interceptions/90
  All available via FBref (free). Most reliable sport for DQI quantification.
  
  Position adjustments:
    Striker:      weight Shot_Selection ×0.40, Chance_Creation ×0.25
    AM/Winger:    weight Chance_Creation ×0.40, Possession ×0.30
    CM:           weight Possession ×0.35, Chance_Creation ×0.30
    CB/DM:        weight Defensive ×0.45, Possession ×0.35

BASKETBALL (NBA):
  Primary metrics: A/TO ratio, TS%, Steal%, Defensive Win Shares
  Source: Basketball Reference. All free.
  
  Note: NBA positions are increasingly fluid. Apply all four dimensions
  for multi-role players; primary role determines main weight.

ICE HOCKEY:
  Primary metrics: Primary assists rate (not secondary — primary requires
  direct decision), zone entry type (carry-in = decision quality;
  dump-in = lower), shot quality (xG/shot where available via Moneypuck)
  
  Note: Ice hockey DQI data is less granular than football or basketball.
  Apply with reduced confidence weighting.

CRICKET:
  Primary metrics: Dot ball % in pressured situations, strike rotation rate,
  false shot % (balls played at without control)
  Source: Cricbuzz, ESPNcricinfo ball-by-ball data
  
  Most relevant for: batting decision quality in T20 death overs,
  bowling decision quality in field placement for specific batters.

TENNIS:
  Primary metrics: Unforced error / winner ratio (lower is better decision-making),
  net approach success% (only come to net when decision is correct),
  second serve decision (playing safe vs attacking on second serve)
  Source: Tennis Abstract, ATP/WTA official stats

SPORTS WHERE DQI IS LESS APPLICABLE:
  Athletics (individual track/field): no game decision-making — performance
  is physical, not decisional. Do not apply.
  Swimming: same — no opponent interaction requiring decisions.
  NASCAR/F1 individual lap time: minimal in-race decision variance vs
  physical performance. Do not apply DQI to lap time analysis.
  F1 strategy decisions (team level): applicable but at team level, not driver.
```

---

## DQI output schema

```json
{
  "dqi_brief": {
    "athlete":    "Player name",
    "sport":      "football",
    "position":   "attacking_midfielder",
    "assessed_at":"2026-04-12T00:00:00Z"
  },

  "components": {
    "chance_creation": {
      "metric": "xA/90: 0.21", "score": 78, "source": "FBref 2025-26"
    },
    "possession_decision": {
      "metric": "Pressured pass completion: 76%", "score": 65, "source": "FBref"
    },
    "shot_selection": {
      "metric": "xG/shot: 0.14", "score": 62, "source": "FBref"
    },
    "defensive_anticipation": {
      "metric": "N/A for position", "score": null, "note": "redistributed"
    }
  },

  "dqi_score":    73,
  "dqi_modifier": 1.08,
  "dqi_label":    "STRONG",

  "scouting_signal": {
    "undervaluation_flag": false,
    "system_fit":          "HIGH — positional play system rewards xA quality",
    "cva_adjustment":      "+5 points"
  },

  "plain_english": "This player makes consistently good decisions in possession — their chance creation quality (xA) is well above position average, and they hold the ball well under pressure. Their shot selection is average for the position. Overall the decision metrics suggest they contribute more than their goal involvement numbers alone would indicate.",

  "sportmind_version": "3.61.0"
}
```

---

*SportMind v3.61 · MIT License · sportmind.dev*
*See also: core/lineup-quality-index.md · core/spatial-game-intelligence.md*
*core/perceptual-pressure-intelligence.md · core/athlete-motivation-intelligence.md*
*examples/agentic-workflows/scouting-agent.md (Pattern 10 CVS formula)*
*core/pre-match-squad-intelligence.md*
