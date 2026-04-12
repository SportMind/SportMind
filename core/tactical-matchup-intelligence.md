---
name: tactical-matchup-intelligence
description: >
  Intelligence framework for opponent-specific tactical exploitation —
  which structural weaknesses in a known opponent a team's system is
  best placed to attack, and how quantified tactical mismatches translate
  into pre-match signal modifiers. Produces a Tactical Matchup Advantage
  Score (TMAS: -15 to +15 signal adjustment) from four matchup dimensions:
  systemic mismatch, personnel exploitation, set piece differential, and
  transition asymmetry. Distinct from spatial-game-intelligence (which
  models how teams use space generally) — this skill models how TEAM A's
  specific system exploits TEAM B's specific weaknesses in a specific match.
  Cross-sport: football primary, basketball (offensive scheme vs defensive
  coverage), ice hockey (power play vs penalty kill specialist mismatches),
  rugby union (kicking vs running game asymmetry). Connects directly to
  scouting agent (Pattern 10): the system fit dimension of CVS requires
  knowing what system the buying club actually runs and which player
  profiles are disproportionately valuable within it.
---

# Tactical Matchup Intelligence — SportMind

**Two teams of equal quality can produce very different expected outcomes
depending on how their systems interact. This skill quantifies that interaction.**

`core/spatial-game-intelligence.md` tells you how a team uses space.
`core/manager-intelligence.md` tells you how stable the system is.
This skill answers the specific pre-match question: given these two teams,
which structural matchup advantages exist, and how large are they?

---

## The Tactical Matchup Advantage Score (TMAS)

```
TMAS = systemic_mismatch + personnel_exploitation
     + set_piece_differential + transition_asymmetry

Range: -15 to +15 (from perspective of the team being analysed)
Positive = tactical advantage for that team
Negative = tactical disadvantage

TMAS APPLICATION:
  Apply as direct SMS adjustment: SMS + TMAS = adjusted pre-match SMS
  Cap: TMAS cannot push SMS below 20 or above 95
  Only apply when: both teams' systems are confirmed (T-2h lineup or
  manager press conference confirmation)
  Do not apply: if TMAS magnitude < 3 (within noise threshold)
```

---

## Dimension 1 — Systemic mismatch (range: -6 to +6)

```
DEFINITION:
  How well does Team A's tactical system structurally exploit Team B's
  system, and vice versa? Some system pairings create structural edges
  that exist regardless of individual quality.

FOOTBALL SYSTEM MATCHUPS:

  HIGH PRESS vs LOW BLOCK:
    Pressing team: +3 in first 60 minutes (pressure forces errors)
    Pressing team: -2 after 60 minutes (legs go; low block waits for this)
    Net advantage per 90: +1 to pressing team IF fitness is not compromised
    Compromise condition: congestion tier ≥ TIER 2 → net advantage = 0

  HIGH PRESS vs HIGH PRESS (mirror):
    Open, high-intensity game. No systemic advantage.
    Higher total goal probability. Signal: expect more goals, not advantage.
    Apply: over/under signal adjustment, not TMAS.

  POSSESSION vs COUNTER-ATTACK:
    Possession team: structural advantage in controlled games, home fixture
    Counter-attack team: structural advantage when losing OR in big games
    (Counter-attack teams historically over-perform vs top possession teams
    in knockout football — see H2H decay modifier in historical-intelligence)
    Net: neutral in league; counter-attack team +2 in knockout stage

  HIGH LINE vs PACE STRIKER:
    Already modelled in spatial-game-intelligence.md: ×1.08 to team with
    pace striker. TMAS interpretation: +4 to team with confirmed pace striker.
    Requires: confirmed lineup with pace striker starting (T-2h check).

  NARROW MIDFIELD OVERLOAD vs WIDE SYSTEM:
    Narrow (4-3-3 inverted / 4-2-3-1 with narrow 10):
    Creates overload in central zones → restricts wide team's key supply lines
    If opponent team relies on wide deliveries: +3 to narrow team

BASKETBALL SYSTEM MATCHUPS:

  PICK-AND-ROLL DOMINANT vs SWITCH-EVERYTHING DEFENCE:
    Switch defence neutralises P&R. Net: 0 (defences match offensive scheme)
    P&R team vs zone defence: +4 (zone disrupts P&R timing)
    
  PACE-AND-SPACE vs SLOW HALF-COURT:
    Fast team forces slow team out of comfort. Net: +3 to fast team
    Exception: playoff basketball (see game-tempo-intelligence.md)

  3-POINT HEAVY vs NO-CLOSE-OUT SCHEME:
    Teams that cannot contest perimeter shots vs elite 3P teams: +4
    Check: opponent's 3P% allowed vs league average

ICE HOCKEY SYSTEM MATCHUPS:

  FORECHECK HEAVY vs PUCK-POSSESSION DEFENCE:
    Aggressive forecheck forces turnovers in D-zone.
    If opponent is a puck-possession team: +3 to forechecking team
    If opponent is a quick outlet team: net neutral (they clear the zone)

  TRAP/NEUTRAL ZONE CLOG vs HIGH-OCTANE OFFENCE:
    Trap effectively reduces star forward production by 15–20%.
    If opponent has 60%+ of offence through top line: +3 to trap team.
```

---

## Dimension 2 — Personnel exploitation (range: -5 to +5)

```
DEFINITION:
  Does Team A have specific players whose profiles are structurally
  dangerous to Team B's defensive approach — or vice versa?

This is the bridge between tactical system and individual player quality.
A great player in the wrong system matchup is less effective.

FOOTBALL PERSONNEL MATCHUP SIGNALS:

  PHYSICAL MISMATCH (aerial):
    Aerial specialist striker vs opponent's short centre-back pairing.
    If opponent CB average height < 181cm AND attacker is aerial specialist:
    +3 personnel exploitation signal.
    Source: FBref aerial duel stats, squad height data.

  PACE DIFFERENTIAL AT FULL-BACK:
    Fast winger vs slow full-back = documented goal probability increase.
    Premier League analysis: pace advantage of 1.0+ m/s = +2 xG/90 impact.
    Check: sprinting speed data (where available) or tactical reports.

  SET PIECE SPECIALIST vs POOR AERIAL DEFENCE:
    If Team A has elite dead-ball specialist AND Team B concedes >35% of
    goals from set pieces: +3 personnel exploitation.
    Load alongside football set piece section in spatial-game-intelligence.md.

  PRESSING TRIGGER PLAYER vs BALL-PLAYING GOALKEEPER:
    Some pressing systems target the goalkeeper as the trigger point.
    If opponent GK is poor under pressure AND pressing team has high-PPDA:
    +2 to pressing team. Verify: GK passing accuracy under pressure (FBref).

BASKETBALL PERSONNEL MATCHUP:

  ISO SCORER vs SWITCH COMMITMENT:
    If defensive team commits to switching all screens AND opposing team has
    elite isolation scorer (usage rate >30%, TS% >58%): +3 to offensive team.

  SMALL-BALL vs PHYSICAL MISMATCH:
    Small-ball lineup (no traditional center) vs team with dominant post player.
    Paint dominance already in spatial-game-intelligence — TMAS adds: if
    small-ball team has no answer for post, apply -3 to small-ball team.

RUGBY UNION PERSONNEL:

  KICKING GAME vs POOR BACK-THREE AERIAL:
    If Team A has elite tactical kicker AND Team B has unreliable back-three
    in aerial contests: +3 to kicking team (territorial control advantage).
    Source: Opta aerial contest win rate for back-three players.
```

---

## Dimension 3 — Set piece differential (range: -3 to +3)

```
DEFINITION:
  Net set piece advantage — combining attacking set piece quality
  with opponent's defensive set piece vulnerability.

CALCULATION:
  SET_PIECE_DIFFERENTIAL = attack_rating - opponent_defence_rating

  ATTACK RATING (0–10):
    10: Elite dead-ball specialist + aerial attackers (>40% of goals from SP)
    7:  Above-average SP programme (25–40% from SP)
    4:  League average
    1:  Below average / no SP focus

  DEFENCE RATING (0–10) — inverted:
    10: Elite SP defence (concedes <15% of goals from SP)
    7:  Above average
    4:  League average
    1:  Poor SP defence (concedes >35% from SP)

  DIFFERENTIAL:
    +4 or above: +3 TMAS contribution (major set piece advantage)
    +2 to +3:    +2 TMAS contribution
    0 to +1:     +0 (neutral)
    -2 to -1:    -1 TMAS (slight disadvantage)
    -4 or below: -3 TMAS (major set piece disadvantage)

APPLICATION NOTE:
  Set piece advantage is most decisive in:
    Low-scoring expected games (one goal matters more)
    Knockout stages (game state management)
    Matches between closely-matched teams (where SP can be the difference)
  Least decisive in:
    High-tempo, high-scoring expected games (open play dominates)
```

---

## Dimension 4 — Transition asymmetry (range: -3 to +3)

```
DEFINITION:
  Which team creates more danger in transitions — the moment immediately
  after possession changes. High-transition teams can exploit opponents
  who commit bodies forward.

FOOTBALL TRANSITION SIGNALS:
  PPDA score (already in spatial): low PPDA team presses high → exposed on
  counter if they lose the ball. Opponent with counter-attack system: +3.
  
  Counter-attack team indicators:
    High transition speed (directional passing after winning ball)
    Attackers who make forward runs immediately after turnovers
    Low possession % but high xG per shot (efficient on the counter)
  
  Transition mismatch signal:
    Possession team (>55% possession average) vs counter-attack specialist:
    Counter team: +2 transition asymmetry
    This is amplified in knockout football (space opens up as possession
    team pushes for goals in tight games).

BASKETBALL TRANSITION:
  Fast break points allowed vs fast break points scored.
  Team A generates >15 fast break pts/game AND Team B allows >12: +2.
  Load from: game-tempo-intelligence.md pace section for amplification.

ICE HOCKEY TRANSITION:
  Zone exit % (team A) vs forecheck effectiveness (team B).
  If team A clears zone efficiently AND team B relies on forecheck: neutral.
  If team A struggles to exit AND team B has elite forecheck: +2 to team B.
```

---

## TMAS calculation example

```
MATCH: Arsenal (home, 4-3-3 high press) vs PSG (away, 4-3-3 possession)

DIMENSION 1 — Systemic mismatch:
  High press vs possession: Arsenal has home press advantage.
  PSG presses selectively (PPDA ~10): Arsenal's press more committed (PPDA ~7).
  First 60 min: +2 Arsenal. Post 60 if level: −1 (PSG pace).
  Net D1 contribution: +1 Arsenal

DIMENSION 2 — Personnel exploitation:
  Saka (if available) — pace vs PSG right-back: +2
  Arsenal aerial threat at set pieces vs PSG height: +1
  Net D2 contribution: +3 Arsenal (if Saka available)
  Note: Saka doubtful → D2 contribution drops to +1

DIMENSION 3 — Set piece differential:
  Arsenal SP rating: 8 (strong dead-ball record)
  PSG SP defence rating: 6 (above average)
  Differential: +2 → TMAS contribution: +2

DIMENSION 4 — Transition asymmetry:
  PSG commit men forward in possession. Arsenal counter quickly.
  Counter-attack advantage: +1 Arsenal

TOTAL TMAS (Saka available): +1 + 3 + 2 + 1 = +7
TOTAL TMAS (Saka absent):    +1 + 1 + 2 + 1 = +5

APPLICATION TO PRE-MATCH SIGNAL:
  Base SMS: 68
  TMAS applied: 68 + 7 = SMS 75 (Saka available)
  TMAS applied: 68 + 5 = SMS 73 (Saka doubtful)
```

---

## Integration with SportMind patterns

```
PATTERN 2 (Pre-Match Chain):
  Apply TMAS after LQI and modifier chain.
  Sequence: Macro → Competition tier → LQI → Modifier chain → TMAS → Final SMS

PATTERN 10 (Scouting Agent):
  TMAS is the missing link in system fit assessment.
  CVS SPATIAL_SYSTEM_FIT modifier already in spatial-game-intelligence.
  TMAS adds: which specific players are most valuable IN THIS SPECIFIC MATCHUP?
  Example: if scout targets a counter-attack team and TMAS shows the buying
  club faces many possession teams, counter-attack profile is less valuable.
  Apply: TMAS profile as system context for CVS role weighting.

PROMPT 22 (Pre-match build-up):
  Include TMAS plain_english note when TMAS magnitude ≥ 5:
  "Arsenal's high press has a structural edge against PSG's possession style —
  especially in the first hour. That's worth roughly 7 SMS points in this analysis."

LIVE MATCH CONTEXT (Pattern 12 — future):
  TMAS dimensions shift as game state changes:
  → Losing team must abandon low block / counter structure → opponent's
    systemic advantage reduces but transition asymmetry increases.
  → Half-time tactical adjustment: if confirmed by journalist, reload D1.
```

---

## TMAS output schema

```json
{
  "tactical_matchup_brief": {
    "match":        "Arsenal vs PSG",
    "competition":  "UCL Quarter-Final",
    "assessed_at":  "2026-04-12T00:00:00Z"
  },

  "home_system":  "4-3-3 high press (PPDA 7.2)",
  "away_system":  "4-3-3 possession (PPDA 10.4)",

  "tmas_components": {
    "systemic_mismatch":      1,
    "personnel_exploitation": 3,
    "set_piece_differential": 2,
    "transition_asymmetry":   1
  },

  "tmas_total":        7,
  "tmas_perspective":  "HOME",
  "tmas_label":        "MODERATE ADVANTAGE",

  "key_matchup_signal": "Arsenal's set piece programme vs PSG's above-average but not elite aerial defence is the largest single tactical edge tonight.",

  "conditions": {
    "saka_available":    true,
    "tmas_if_absent":    5,
    "lineup_confirmed":  true
  },

  "sms_adjustment":    7,

  "plain_english": "Arsenal have a genuine tactical edge tonight. Their pressing system targets PSG at the source, their set pieces are a threat against PSG's height, and if Saka plays, he has pace on PSG's right side. The tactical picture adds about 7 points to the signal — not decisive on its own, but meaningful.",

  "sportmind_version": "3.62.0"
}
```

---

*SportMind v3.62 · MIT License · sportmind.dev*
*See also: core/spatial-game-intelligence.md · core/manager-intelligence.md*
*core/lineup-quality-index.md · core/pre-match-squad-intelligence.md*
*core/athlete-decision-intelligence.md · core/perceptual-pressure-intelligence.md*
*examples/agentic-workflows/scouting-agent.md (Pattern 10)*
