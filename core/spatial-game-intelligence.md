---
name: spatial-game-intelligence
description: >
  Intelligence framework for how teams use and deny space — the tactical
  and spatial dimension of team sports that standard form analysis misses.
  Covers formation systems and their signal implications, pressing intensity
  as a form modifier, defensive line height, set piece dependency, and
  transition zones. Produces a Spatial Context Modifier (SCM) applied to
  pre-match signals for football, basketball, ice hockey, and rugby.
  Connects to LQI (which players are disproportionately valuable in a
  specific spatial context) and to manager intelligence (tactical system
  changes are spatial disruptions). Load when: a match features a notable
  tactical mismatch, a manager has changed system, a key spatially-dependent
  player is absent, or the scouting intelligence (Pattern 10) requires
  understanding which athletic profiles fit a specific system.
  Not applicable to individual sports.
---

# Spatial Game Intelligence — SportMind

**How teams use and deny space — and why the same LQI can produce
very different outcomes depending on who is creating the space.**

The LQI (`core/lineup-quality-index.md`) tells you how good the players are.
This skill tells you how the space is organised — which changes which players
matter most, which opponents are structurally disadvantaged, and what type
of goals or scoring plays are most likely to determine the outcome.

This is not tactical commentary. It is a structured modifier framework
that agents can apply without tactical expertise, derived from verifiable
match data and manager press conference signals.

---

## Football — formation and space framework

```
THE CORE INSIGHT:
  Formation is a spatial commitment. It creates structural advantages
  and structural vulnerabilities that exist regardless of individual
  player quality. Two teams with identical LQI scores but different
  formations will produce different expected outcomes.

FORMATION SIGNAL CATEGORIES:

HIGH PRESS (examples: 4-3-3 intensive, 4-2-3-1 gegenpressing):
  What it creates:
    Turnovers in advanced zones → high-probability scoring opportunities
    Opponent goalkeeper forced to distribute quickly under pressure
    Intensity degrades in second half → opponent second-half performance uplift
  
  Key signals:
    PPDA (Passes Per Defensive Action) < 8: elite pressing team
    PPDA 8–12: high press applied selectively
    PPDA > 12: structured mid/low block
  
  Modifier implications:
    High press vs low-quality ball-players: × 1.06 for pressing team
    High press with high fixture congestion: × 0.96 (press requires legs)
    High press vs press-resistant player (dribbler, quick release): neutral
  
  LQI connection: A high-press system depends disproportionately on
  forwards who press intelligently. If the primary pressing forward is
  absent, the system loses its engine. Increase departure_impact for
  pressing forwards at pressing teams.

LOW BLOCK / DEEP DEFENCE (examples: 5-4-1, 4-5-1 defensive):
  What it creates:
    Compact defensive shape → limits opponent crossing and through-balls
    Transition attacks on the counter → premium on striker pace
    Set piece dependency → aerial ability of defenders and attackers elevated
    
  Key signals:
    Shots faced per game > 16: typically a low-block team
    PPDA > 15: passive defensive positioning
    High proportion of goals from set pieces: signal of defensive dependency
  
  Modifier implications:
    Low block vs creative midfield-heavy opponent: × 0.96 for low-block team
    Low block vs direct, physical attack: × 1.04 for low-block team
    Low block → set piece dependency: increase weight on set piece specialists

HIGH LINE (advanced defensive position):
  What it creates:
    Offside trap catches through-ball runners → reduces goal threat
    Vulnerable to quick vertical passes behind the line (speed test)
    Creates space for midfield to press forward
  
  Key signals:
    High defensive line: typically 4-3-3 or 3-4-3 systems
    Opponent pace at striker = primary counter-signal
  
  LQI connection: High line teams need fast centre-backs or a sweeper.
  Apply × 0.92 LQI if high-line team is missing its fastest central defender
  against a genuinely pace-based opponent.

SPATIAL MATCHUP MODIFIERS (football):
  HIGH PRESS vs LOW BLOCK: slight edge to pressing team in first 60 min,
  slight edge to low block team in final 30 if score is level
  HIGH LINE vs PACE STRIKER: apply × 1.08 to team with recognised pace striker
  NARROW FORMATION vs WIDE WINGERS: apply × 1.06 to team with wide attackers
  against narrow-defensive formation (wing space created)
  OVERLOADED MIDFIELD vs ISOLATED STRIKER: apply × 0.94 to team with lone
  striker against a three-man midfield with defensive capacity
```

---

## Football — set piece intelligence

```
Set pieces deserve separate treatment because they are fully spatial
events — goals scored regardless of open-play tactical matchup.

IMPORTANCE SIGNAL:
  ~25–30% of all football goals come from set pieces at professional level.
  For some teams this proportion is 40–50% — set pieces ARE their game model.

AERIAL DOMINANCE:
  Teams with multiple 6'2"+ players in defensive and attacking phases
  hold a structural set piece advantage.
  Check: Average squad height, aerial duel win rate, set piece goals
  scored and conceded per season.
  Modifier: × 1.04 for set piece specialist team; × 0.96 for opponent
  if opponent concedes high proportion of aerial set piece goals

CORNER AND FREE KICK SPECIALISTS:
  A team's corner-taker quality changes the expected value of each corner.
  Elite deliverer (Trent Alexander-Arnold, Kevin De Bruyne equivalent):
  × 1.06 on set piece threat signal
  If that player is absent: revert to neutral

SET PIECE CONCEDE PATTERN:
  If an opponent concedes > 35% of goals from set pieces, flag this:
  → Defensive set piece vulnerability modifier × 0.96 for that team
  → Attacking set piece team modifier × 1.04 for the opponent
```

---

## Basketball (NBA) — spacing and zone framework

```
FLOOR SPACING:
  The single most important spatial concept in modern basketball.
  A team with multiple 3-point threats forces defenders to guard the
  perimeter → creates driving lanes → elevates star player impact.
  
  Spacing signal:
    Team 3PA per game > 35: elite spacing team
    Team 3P% > 37%: spacing is a genuine weapon
    Key player eFG% > 58%: spacing premium is reflected in efficiency
  
  LQI connection:
    In a spacing-first system, star players at the top of the paint are
    disproportionately valuable. If the primary spacing shooter is absent:
    driving lanes close → star player LQI impact reduced by 15–20%
    Apply: lqi_contextual_adjustment × 0.88 for interior star without shooters

TRANSITION PACE:
  High-pace teams (PACE > 100.5 possessions per 48 min) exploit open court
  space before defences set.
  
  Modifier implications:
    High pace vs slow defensive team: × 1.06 for fast-paced team
    High pace in back-to-back game (fatigue): × 0.94 (pace is first to go)
    Playoff basketball (pace drops): reduce pace-dependent modifier by 40%
    in playoff series vs regular season

PAINT DOMINANCE:
  Teams that win the paint by > 10 points per game win approximately 70%
  of matches in the NBA. This is the most reliable spatial signal in basketball.
  
  Paint points indicator:
    Superior interior size team vs undersized opponent: × 1.04
    Superior interior size team vs zone defence: neutral (zone neutralises size)
    Superior interior size team with absent primary big: × 0.90

ZONE DEFENCE DISRUPTION:
  Some teams perform dramatically worse vs zone defence — reducing spacing
  benefit and forcing outside shooting.
  If opponent deploys zone AND attacking team has no zone-breaking playmaker:
  × 0.96 spatial modifier for the offensive team

CLUTCH SPATIAL PATTERNS:
  In the final 5 minutes of close games, most teams revert to isolation
  plays — removing team-spatial intelligence in favour of individual quality.
  In clutch situations: weight individual clutch metrics (athlete/nba/)
  more heavily than spatial system modifiers.
```

---

## Ice hockey — zone and line match framework

```
ZONE ENTRY STRATEGY:
  Two fundamental approaches — carry-in (more dangerous) vs dump-and-chase.
  Teams with high skilled forwards carry the puck in.
  Teams with physical but less skilled forwards dump and chase.
  
  Zone entry signal:
    Carried zone entries % > 60%: skilled possession team
    Dump-in % > 50%: physical dump-and-chase team
    
  Matchup modifier:
    Skilled entry team vs high-event defensive team: neutral
    Dump-and-chase team vs goaltender with exceptional puck handling: × 0.94

LINE MATCHING:
  Top defensive pair deployed against opponent's top line.
  This is the primary spatial decision in hockey — if a team can
  regularly match its top defensive pair against the opponent's elite line,
  that line's impact is reduced.
  
  Signal: Home teams control line matching. Away teams cannot guarantee it.
  Home ice advantage amplification: × 1.04 if significant line quality gap
  exists (home team can match favourable; away team cannot avoid the mismatch)

POWER PLAY SPATIAL DOMINANCE:
  Power play efficiency (PP%) is a major spatial signal.
  Top-5 NHL power play unit: × 1.08 when facing a penalty-prone opponent
  (opponent averages > 3 penalties/game)
  Poor penalty kill (PK% < 76%): × 1.04 for opponent's power play threat

GOALTENDER SPATIAL POSITIONING:
  A positionally elite goaltender reduces the value of high-volume shot
  strategies. Square-angle attacks require elite puck-moving shooters.
  GSAx (from Natural Stat Trick) is the primary signal for this —
  already modelled in athlete/nhl/athlete-intel-nhl.md.
  Spatial context adds: if goaltender's weak side is known (documented),
  the spatial value of players who attack that side is elevated × 1.04.
```

---

## Rugby union — spatial framework

```
TERRITORIAL CONTROL:
  Rugby is fundamentally a territorial game. Winning the kicking battle
  determines where the game is played. Territory % > 55 correlates
  with ~65% win rate in Test rugby.
  
  Key spatial signals:
    Elite kicker vs accurate opposition kicker: monitor individual kicker
    form and match-day wind conditions (core/core-weather-match-day.md)
    If premier kicker is absent: × 0.94 on territorial control modifier

GAIN LINE DOMINANCE:
  Winning the gain line (advancing past the defensive line at first contact)
  opens up space in the wider channels.
  
  Physical size + ball-in-hand advantage team: × 1.04
  Against defensive line speed teams: neutral

SET PIECE PLATFORM:
  Scrum and lineout dominance provide free-phase territory and possession.
  Dominant scrum team vs weaker scrum opponent: × 1.04
  Loss of primary lineout jumper (tall second row): × 0.94 on lineout platform
  
SPATIAL SIGNAL FOR FAN TOKENS:
  Rugby's spatial intelligence is most relevant for national team tokens
  (World Cup, Six Nations) where tactical matchups are well-documented.
  For club tokens: apply spatial framework to Premiership, URC, Top 14
  where Sportradar data provides detailed territory and possession stats.
```

---

## Scouting connection (Pattern 10)

```
The spatial game framework feeds directly into the Moneyball Scouting
Agent (Pattern 10 / examples/agentic-workflows/scouting-agent.md).

The CVS formula includes DTS (Development Trajectory Score) and PI
(Position Intelligence). Spatial context answers:
  WHICH POSITIONS ARE VALUED IN THIS SYSTEM?
  WHICH ATHLETIC PROFILES FIT SPECIFIC SPATIAL ROLES?

Examples:
  High press 4-3-3 team: needs intelligent pressing forwards, not traditional
  number 10s. A target forward with high DTS but low pressing work rate
  scores high on CVS but low on system fit — flag the mismatch.
  
  Spacing-first NBA team needs 3-and-D wings more than ball-dominant scorers.
  A ball-dominant scorer with high AELS and APS may score well on CVS but
  poorly on spatial system fit — the commercial value is real but the sporting
  fit is not.

SPATIAL_SYSTEM_FIT modifier for scouting:
  HIGH FIT (profile matches spatial system requirements): CVS × 1.08
  NEUTRAL FIT:                                            CVS × 1.00
  LOW FIT (profile mismatches system requirements):       CVS × 0.88
  
  Note: This is separate from the MgSI SYSTEM_FIT component in
  core/manager-intelligence.md, which measures the existing squad's
  fit. This modifier evaluates a potential arrival's fit.
```

---

## Spatial context output schema

```json
{
  "spatial_brief": {
    "match":        "Arsenal vs PSG",
    "competition":  "UCL",
    "assessed_at":  "2026-04-12T00:00:00Z"
  },

  "home_spatial_profile": {
    "system":            "4-3-3 high press",
    "pressing_intensity": "HIGH (PPDA avg 7.2)",
    "set_piece_rating":  "STRONG (28% of goals)",
    "line_height":       "HIGH",
    "spatial_strengths": ["press recovery", "set piece aerial", "wide attacks"],
    "spatial_vulnerabilities": ["pace behind high line", "second-half press decline"]
  },

  "away_spatial_profile": {
    "system":            "4-3-3 possession",
    "pressing_intensity": "MEDIUM (PPDA avg 10.4)",
    "set_piece_rating":  "MODERATE",
    "spatial_strengths": ["quick wide transitions", "press resistance"],
    "spatial_vulnerabilities": ["aerial duels", "defensive transitions"]
  },

  "matchup_modifiers": {
    "home_spatial_advantage": 1.04,
    "away_spatial_advantage": 0.98,
    "key_spatial_signal": "Arsenal's set piece threat vs PSG's aerial weakness — amplify set piece modifier"
  },

  "lqi_spatial_adjustments": {
    "note": "Saka absence removes key press trigger — Arsenal's press efficacy reduced",
    "adjustment": "Pressing system modifier reduced from ×1.06 to ×1.02 without primary press trigger"
  },

  "plain_english": "Arsenal's high press is their main weapon tonight. Without Saka as the press trigger, the system loses some of its bite — the modifier is slightly reduced. PSG struggles with aerial set pieces; Arsenal should exploit this.",

  "sportmind_version": "3.56.0"
}
```

---

*SportMind v3.56 · MIT License · sportmind.dev*
*See also: core/lineup-quality-index.md · core/manager-intelligence.md*
*core/pre-match-squad-intelligence.md · examples/agentic-workflows/scouting-agent.md*
*core/core-weather-match-day.md (wind affects spatial kicking games)*
*athlete/nhl/athlete-intel-nhl.md (GSAx for goaltender spatial positioning)*
