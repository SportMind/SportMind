---
name: game-tempo-intelligence
description: >
  Intelligence framework for game tempo and rhythm as pre-match signal
  modifiers. Covers pace-of-play as a structural competitive variable,
  tempo mismatch between teams as a signal amplifier, session and period
  rhythm patterns, and momentum transfer from recent matches. Distinct
  from narrative momentum (core/core-narrative-momentum.md) which covers
  storyline effects: tempo intelligence covers the structural pace and
  rhythm characteristics of how a team or athlete operates. Produces a
  Tempo Context Modifier (TCM: 0.90–1.12). Primary sports: basketball
  (pace and spacing are primary competitive variables), cricket (session
  rhythm and over-rate are structural), football (pressing tempo and
  transition speed), ice hockey (line matching tempo), tennis (point
  construction tempo). Load when: a significant tempo mismatch exists
  between opponents, a team has shifted system (high press to low block
  or vice versa), or a sport where tempo is a primary competitive variable.
---

# Game Tempo Intelligence — SportMind

**Rhythm and pace as structural signal variables — not narrative,
not form, but the operating tempo of how the game is played.**

Narrative momentum (`core/core-narrative-momentum.md`) covers what
a match *means*. Tempo intelligence covers how *fast and rhythmically*
it is played — and whether one side can impose, disrupt, or adapt to
the tempo better than the other.

---

## The tempo signal framework

```
THREE TEMPO DIMENSIONS:

1. PACE — How quickly the game moves (possessions per minute, points
   per game, overs per hour). Fast pace suits teams with depth and
   conditioning; slow pace suits teams that are individually superior.

2. RHYTHM — The predictability and structure of play patterns.
   Teams with high rhythm execute their game model consistently.
   Rhythm disruption (injury, early red card, weather change) affects
   high-rhythm teams disproportionately.

3. MOMENTUM — The directional flow of the contest within a match.
   Which team is "on" at any given moment. Momentum is the most volatile
   tempo dimension and the most commercially significant for fan tokens
   (it drives live social volume).

AGENT RULE: Apply TCM when a clear tempo advantage or mismatch exists.
Do not apply for tempo-neutral matchups. TCM is a sharpening modifier
on top of existing signals — not a standalone basis for ENTER/WAIT/ABSTAIN.
```

---

## Basketball — tempo as primary competitive variable

```
NBA PACE INTELLIGENCE:

Pace (possessions per 48 minutes) is the single most important tempo
signal in basketball. It determines how many scoring opportunities each
team gets and directly interacts with roster construction.

PACE BANDS:
  Fast pace (>102 possessions/48): rewards depth, athleticism, shooting
  Moderate (98–102): neutral — both styles viable
  Slow pace (<98): rewards half-court execution, star isolation, size

TEMPO MISMATCH SIGNAL:
  A fast-pace team (>102) vs a slow-pace team (<98):
  The pace will settle between the two. Identify who benefits:
  
  Pace imposed upward (faster than slow team wants): +1.08 for fast team
    Indicator: fast team has better conditioning, more depth
  Pace controlled downward (slower than fast team wants): +1.06 for slow team
    Indicator: slow team has elite half-court execution, strong rebounding
  Pace contested (neither can impose): neutral — no TCM

PACE DATA SOURCE: NBA Advanced Stats (nba.com/stats/teams/advanced)
  Also: Basketball Reference team stats — Pace column

TRANSITION RATE:
  Fast break points as % of total points.
  Teams with >18% fast break points are heavily transition-dependent.
  Against a transition-heavy team: apply defensive pace modifier
  If opponent is strong in transition defence: ×0.94 for transition team
  If opponent is weak in transition defence: ×1.08 for transition team

HALF-COURT RHYTHM:
  Pick-and-roll execution rate, off-ball movement frequency.
  High-rhythm half-court teams (Warriors system, Spurs tradition):
  Disruption from injury to the point guard or primary ball-handler =
  disproportionate rhythm loss. Apply ×0.92 if primary orchestrator absent.

NBA PLAYOFF TEMPO:
  Playoffs consistently lower pace by 2–4 possessions per game vs
  regular season. Agents should apply a playoff_tempo_discount when
  extrapolating regular season pace data to playoff predictions.
  Playoff TCM recalibration: reduce pace-based modifiers by 30%.
```

---

## Cricket — session rhythm and over-rate

```
SESSION RHYTHM IS STRUCTURAL IN CRICKET:

Test cricket runs in three sessions per day. Each session has a
distinct rhythm that shifts the competitive balance.

MORNING SESSION:
  Ball: hard, new. Surface: has overnight dew/moisture.
  Bowling advantages: greatest of the day.
  Batting is hardest; dismissals cluster in early overs.
  Signal: Team batting in morning session has structural disadvantage.
  TCM: ×0.94 for batting team if key batters face morning conditions.

POST-LUNCH (afternoon session):
  Ball: worn but not reversing yet. Pitch: drying, more even.
  Partnership building phase. Batting becomes easier.
  TCM: ×1.02 for batting team (batting conditions improving).

EVENING SESSION:
  Ball: worn, potentially reversing. Pitch: variable.
  Reverse swing can become dominant from ~60 overs.
  TCM: ×1.04 for bowling side if reverse swing specialists available.

DEW-AFFECTED EVENING (day-night matches, tropical venues):
  Already modelled in: core/core-weather-match-day.md
  TCM connection: dew disrupts bowling rhythm specifically for
  spinners. Apply ×0.92 to spinner-dependent bowling attacks in
  high-dew conditions.

OVER-RATE INTELLIGENCE:
  Slow over rates affect match rhythm and can trigger penalties.
  If team is known for slow over rates (ICC penalty history):
    Session pressure signal: last session likely rushed → ×0.96
    Opponent batting benefit: extra time in session → ×1.02

T20 TEMPO:
  Powerplay (overs 1–6): batting tempo highest.
  Middle overs (7–15): pace chess — batting builds platform.
  Death overs (16–20): maximally contested tempo battle.
  
  DEATH BOWLING SPECIALIST signal:
  Teams with proven death bowling specialists impose rhythm disruption.
  Opponent's death over batting score vs their PowerPlay score is a
  tempo indicator — some teams cannot change rhythm when required.
  TCM: ×1.06 for specialist death bowling unit vs poor death-over batting team.

PARTNERSHIP MOMENTUM (Test cricket):
  A partnership of >50 runs establishes batting rhythm.
  Disruption signals: DRS review (temporary pause), rain delay,
  new ball, strategic bowling change.
  All of these reset the rhythm and introduce a brief vulnerability window.
  TCM: ×1.04 for bowling side for 2–3 overs following rhythm disruption.
```

---

## Football — pressing tempo and transition speed

```
PRESSING INTENSITY AS TEMPO:
  Already quantified in core/spatial-game-intelligence.md (PPDA).
  TCM adds the temporal dimension: pressing tempo degrades over
  90 minutes in a way that spatial intelligence does not fully capture.

FIRST HALF vs SECOND HALF PRESSING:
  High-press teams (PPDA < 8) show consistent second-half PPDA decay.
  Average decay: PPDA increases by 2–3 points in second half.
  This means: the press is less effective in the final 30 minutes.
  
  TCM signal: If pre-match analysis shows match will be decided late
  (high-stakes with likely close score), pressing team's advantage
  diminishes. Apply: ×0.96 on pressing_intensity modifier for minutes 70+.
  Agent note: This is a second-half signal, not a whole-match signal.

TRANSITION SPEED:
  Time from defensive action to attacking position.
  Fast-transition teams (< 6 seconds from turnover to shot attempt):
  vs slow-defensive-set teams = ×1.06 for transition team
  vs fast-defensive-recovery teams = neutral

RHYTHM DISRUPTION EVENTS (football):
  Events that reset match rhythm:
    Red card: entire tactical system requires recalibration
    Penalty scored/missed: psychological reset for both teams
    Substitution that changes system: rhythm test for new unit
    
  All of these create a tempo uncertainty window (5–15 minutes).
  Pre-match: lower TCM confidence if red card risk is elevated
  (player with CITING_ACTIVE or high yellow count — see DSM framework).
```

---

## Ice hockey — line matching and shift tempo

```
LINE MATCHING AS TEMPO CONTROL:

The home team in the NHL controls line matching — deploying their
top line against the opponent's weaker lines and protecting their
defensive pair against the opponent's top offensive unit.

This is pure tempo intelligence: the home team imposes a favourable
rhythm of competitive quality throughout the game.

HOME ICE ADVANTAGE MODIFIER (tempo component):
  Strong top line + home ice = ability to create favourable matchups
  on every shift: ×1.04 (already partially in spatial framework)
  
  Away team must manage line deployment reactively — more energy spent
  on system management, less on execution.

SHIFT TEMPO:
  Teams that play short, fast shifts (<40 seconds average) maintain
  higher energy levels throughout. Teams with longer shifts (>50 sec)
  may accumulate fatigue in late periods.
  
  Fatigue signal: Long-shift teams in back-to-back games:
  Load alongside: core/core-fixture-congestion.md — this is the
  tempo complement to the congestion framework.

PERIOD RHYTHM:
  First period: systems establish. Lower scoring.
  Second period: most ice time. Scoring rates peak.
  Third period: decisive. Protect-vs-push tension.
  
  Teams with strong third-period records (documented in advanced stats)
  have positive TCM for late-game scenarios.
```

---

## Tennis — point construction tempo

```
SERVE + 1 vs RALLY TEMPO:

Two fundamental tennis tempo archetypes:
  SERVE + 1: win points quickly (serve wide, put away second shot)
  RALLY CONSTRUCTION: extend points, wear down opponent

TEMPO MISMATCH SIGNAL:
  A serve-and-volley / serve + 1 specialist vs a heavy rally player:
  
  On fast surfaces (grass, fast hard): serve + 1 advantage ×1.06
  On slow surfaces (clay): rally player advantage ×1.08
  Surface is the primary TCM input in tennis.

TIEBREAK TEMPO:
  Tiebreaks tend to shift players toward safer tempo — slower ball
  speeds, higher first-serve percentage, fewer winners attempted.
  Players who resist this and maintain attacking tempo in tiebreaks
  have high PPI AND positive TCM contribution.
  
  Tiebreak tempo stat: winner count in tiebreaks vs regular games.
  Source: Tennis Abstract match charting.

MOMENTUM WITHIN MATCH:
  Break of serve creates a 12–15 minute elevated pressure window.
  The server attempting to break back operates under elevated tempo
  pressure. Players with strong break-back records have positive TCM
  after being broken.
```

---

## Tempo Context Modifier (TCM) calculation

```
TCM FORMULA:
  TCM = 1.00 + (pace_advantage × pace_weight)
            + (rhythm_advantage × rhythm_weight)
            - (disruption_risk × 0.05)

  Where advantages are on a scale of −0.10 to +0.10
  and weights are sport-specific.

SPORT WEIGHTS:
  Basketball: pace_weight=0.60, rhythm_weight=0.40
  Cricket:    pace_weight=0.30, rhythm_weight=0.70
  Football:   pace_weight=0.45, rhythm_weight=0.55
  Ice hockey: pace_weight=0.50, rhythm_weight=0.50
  Tennis:     pace_weight=0.40, rhythm_weight=0.60

TCM BOUNDS: 0.90 to 1.12 (tighter than most other modifiers —
  tempo is a sharper but smaller effect)

ANTI-STACKING:
  Never apply TCM > ×1.06 when spatial_modifier is already > ×1.04.
  The two frameworks share some underlying variance — cap combined
  effect at ×1.10 from tempo + spatial combined.
```

---

## TCM output schema

```json
{
  "tempo_brief": {
    "match":   "Arsenal vs PSG",
    "sport":   "football",
    "format":  "UCL knockout"
  },

  "tempo_profiles": {
    "home": {
      "system":          "high_press",
      "pace_preference": "HIGH",
      "rhythm_label":    "HIGH — disciplined pressing system, 3 years under same manager"
    },
    "away": {
      "system":          "possession",
      "pace_preference": "MEDIUM",
      "rhythm_label":    "MEDIUM — can shift tempo, technically strong"
    }
  },

  "tempo_matchup": {
    "pace_advantage":     "HOME +0.04 (home press forces fast game)",
    "rhythm_advantage":   "HOME +0.06 (established system vs transitioning away side)",
    "disruption_risk":    0.02,
    "second_half_decay":  "HOME −0.03 (high press fades after 70 min)"
  },

  "tcm":        1.07,
  "tcm_label":  "HOME TEMPO ADVANTAGE",

  "plain_english": "Arsenal's high press should give them a rhythm advantage — they've been running this system for three years and PSG are still adjusting. The main risk is the second half: Arsenal's press always loses intensity after 70 minutes. If the match is close in the final 20, the tempo advantage flips.",

  "sportmind_version": "3.61.0"
}
```

---

*SportMind v3.61 · MIT License · sportmind.dev*
*See also: core/core-narrative-momentum.md · core/spatial-game-intelligence.md*
*core/core-fixture-congestion.md · core/core-weather-match-day.md*
*core/perceptual-pressure-intelligence.md*
