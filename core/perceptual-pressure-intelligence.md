---
name: perceptual-pressure-intelligence
description: >
  Intelligence framework for athlete perceptual-cognitive capacity under
  pressure — the ability to rapidly read, process, and respond to complex
  game information in high-stakes environments. Distinct from form (what
  they have been doing) and motivation (why they are trying): perceptual
  pressure intelligence models HOW WELL an athlete reads the game when
  the stakes are highest. Produces a Pressure Performance Index (PPI:
  0–100) and modifier (0.88–1.18). Highest impact in: UCL knockout
  stages, playoff series, title deciders, major finals, individual sport
  high-pressure events (darts at Ally Pally, snooker at the Crucible,
  tennis at Wimbledon/US Open). Directly relevant to fan token commercial
  signals because high-PPI athletes in high-stakes matches increase win
  probability in exactly the matches that generate maximum fan token
  engagement and FTP PATH_2 supply mechanics. Cross-sport: football,
  basketball (NBA playoffs), tennis, MMA, darts, snooker, cricket, F1.
  Load when: analysing a high-stakes match where the pressure environment
  differs significantly from regular season conditions.
---

# Perceptual Pressure Intelligence — SportMind

**How well an athlete reads the game when the stakes are at their
highest — and what that means for the signal.**

Form tells you what an athlete has been doing. PPI tells you whether
that form will hold when the environment changes from regular to
extraordinary. The two are genuinely independent. An athlete can be
in excellent form (SMS 78) but have a documented history of
perceptual breakdown under finals-level pressure — the signal without
PPI is incomplete.

---

## Why perceptual pressure intelligence is a real, measurable signal

```
WHAT IT MEASURES:
  The cognitive-perceptual component of performance under elevated pressure.
  Not "bottle" as a vague narrative — a structured, verifiable framework.

THREE DOCUMENTED PRESSURE EFFECTS:

Effect 1 — Attentional narrowing:
  Under extreme pressure, attention narrows to primary cues and loses
  peripheral information. A goalkeeper under penalty shootout pressure
  focuses on the ball so intensely that they lose read on the striker's
  body language — the very information that predicts direction.
  
  Some athletes resist attentional narrowing better than others.
  This is not personality — it is a documented, trainable cognitive trait.
  Evidence: penalty conversion rates in shootouts vs regular play;
  close-game decision quality vs early-game decision quality.

Effect 2 — Decision latency increase:
  Under high cortisol (stress hormone), decision-making slows.
  A tennis player who normally decides shot selection in ~200ms takes
  ~280ms under final-set pressure. That 80ms is the difference between
  an attacking and a defensive shot selection. At elite level this is
  outcome-determining.
  
  Observable via: shot speed on key points vs routine points;
  unforced error rate in tiebreaks vs regular games;
  assist rate in playoff games vs regular season.

Effect 3 — Pattern recognition disruption:
  Elite athletes operate largely through pattern recognition — they
  "read" the game by matching present configurations to stored patterns.
  Under pressure, working memory is partially occupied by threat
  assessment, leaving less capacity for pattern matching.
  
  Some athletes compensate by operating in "auto mode" — highly trained
  motor programmes that bypass conscious decision-making.
  Observable: technical execution quality on routine actions under
  pressure (passing accuracy, first touch, shooting technique).
```

---

## The Pressure Performance Index (PPI)

```
PPI = (Clutch_Record × 0.35)
    + (High_Stakes_History × 0.30)
    + (Experience_Depth × 0.20)
    + (Recovery_Rate × 0.15)

Scale: 0–100. Maps to PPI modifier per table below.

PPI → MODIFIER:
  PPI 85–100: ×1.18  ELITE PRESSURE PERFORMER
  PPI 70–84:  ×1.10  STRONG
  PPI 55–69:  ×1.04  ABOVE BASELINE
  PPI 40–54:  ×1.00  NEUTRAL — no pressure adjustment
  PPI 25–39:  ×0.94  PRESSURE CONCERN — documented history
  PPI 10–24:  ×0.88  SIGNIFICANT CONCERN — consistent decline
```

---

## Component 1 — Clutch Record (35% weight)

```
WHAT IT MEASURES:
  Performance in defined "clutch" situations vs career baseline.
  Clutch = final 5 minutes of close games, tiebreaks, shootouts,
  deciding frames, final rounds of boxing, round 5 of 5-round MMA fights.

SPORT-SPECIFIC CLUTCH METRICS:

FOOTBALL:
  Goals/assists in matches decided by 1 goal in final 10 minutes
  Penalty conversion rate (career) — minimum 5 penalties
  xG overperformance in high-pressure matches
  Sources: FBref advanced stats, Transfermarkt career records
  
  CLUTCH_SCORE bands:
    Goals per 90 in clutch situations > 120% of career avg: 85–100
    110–120%: 65–84
    90–110%: 40–64
    < 90% of career avg: 0–39

TENNIS:
  Tiebreak win rate vs set win rate
  Break point conversion in deciding sets
  Performance in fifth sets / match tiebreaks
  Sources: Tennis Abstract, Jeff Sackmann's match charting data
  
  Primary metric: (Tiebreak_win% − Set_win%) normalised 0–100
  If positive differential (better in tiebreaks): high clutch score
  If negative differential (worse in tiebreaks): low clutch score

SNOOKER:
  Final frame win rate (existing metric: athlete/snooker/)
  Deciding frame record at major venues (Crucible specifically)
  Sources: World Snooker official statistics

DARTS:
  Checkout percentage at 170, 167, 160 (pressure checkouts)
  Performance in match-deciding legs vs earlier legs
  Ally Pally-specific record (venue pressure amplifier)
  Sources: Darts Reference, PDC official statistics

NBA:
  Clutch +/- (last 5 min, score within 5 points)
  Free throw percentage in 4th quarter close games vs season average
  Shot quality and shot selection in clutch vs regular play
  Sources: NBA Advanced Stats, Basketball Reference

MMA:
  Round 5 performance vs round 1–2 performance (5-round fights)
  Championship round success rate
  Performance when hurt (absorbing big shot and responding) —
  qualitative, sourced from fight analysis journalism
  Sources: UFC Stats, FightMetric

F1:
  Lap time variance in qualifying sector 3 (highest pressure section)
  Overtake decision quality under championship pressure
  Safety car restart performance
  Sources: Formula1.com sector data, Motorsport Stats
```

---

## Component 2 — High-Stakes History (30% weight)

```
WHAT IT MEASURES:
  Track record specifically in the highest-pressure competition formats
  vs regular season performance. The question: does performance RISE,
  hold STEADY, or FALL in the biggest moments?

COMPETITION TIERS FOR HIGH-STAKES ASSESSMENT:
  Tier A: Finals (World Cup final, UCL final, Grand Slam final, championship)
  Tier B: Semi-finals / knockout rounds / playoffs
  Tier C: Regular season / early rounds

HIGH-STAKES RATING:
  Tier A outperforms career average:     90–100
  Tier A matches career average:         65–89
  Tier A underperforms (1–2 matches):    40–64
  Tier A underperforms (3+ matches):     10–39
  No Tier A history:                     50 (neutral — insufficient data)

IMPORTANT — SMALL SAMPLE CAVEAT:
  Finals records are small samples. A player who has been in 2 UCL
  finals has insufficient data for high confidence scoring.
  When sample < 3 Tier A appearances: weight this component at 15%
  and redistribute 15% to Clutch Record.
  
  AGENT RULE: Flag LOW_SAMPLE when high_stakes_appearances < 3.
  Output: "High-stakes history based on N appearances — treat with
  caution. Clutch record given additional weight."
```

---

## Component 3 — Experience Depth (20% weight)

```
WHAT IT MEASURES:
  The cognitive benefit of having been in high-pressure environments
  before. First-time finals participants face a novel environment;
  veterans have established cognitive programmes for managing it.

  This is not a talent judgment — it is a pure exposure effect.
  The more times an athlete has operated at this pressure level,
  the better their perceptual system is at filtering signal from noise.

EXPERIENCE DEPTH SCORE:
  10+ appearances at Tier A/B level:     90–100
  6–9 appearances:                       70–89
  3–5 appearances:                       45–69
  1–2 appearances (first exposure):      20–44
  No high-pressure experience:           0–19

DEBUT EFFECT:
  First major final / first playoff series / first title decider:
  Experience depth score capped at 30 regardless of general career.
  Apply: DEBUT_PRESSURE flag in output.
  Note: Some athletes perform above expectation on debut (see
  core/athlete-motivation-intelligence.md — Debut career first).
  The debut effect is a genuine variance inflator — do not apply
  directional modifier, increase uncertainty window instead.

NEGATIVE EXPERIENCE:
  Multiple Tier A failures create a different cognitive pattern —
  specifically, hyperawareness of the failure scenario.
  If player has 3+ Tier A failures: reduce experience score by 15
  and note PRESSURE_SCAR flag.
  This is not permanent — one major Tier A success resets the flag.
```

---

## Component 4 — Recovery Rate (15% weight)

```
WHAT IT MEASURES:
  How quickly an athlete recovers from a negative event within a
  high-pressure match. Getting scored against, making an error,
  losing a set or frame — and the response in the next action.

  This is the most difficult component to quantify but the most
  observable in real-time. It feeds directly into in-match signal
  updating for agents running live analysis.

HIGH RECOVERY INDICATORS:
  Historical: Goals/assists/wins in the action/period/game AFTER
  a significant negative event (conceded, lost set, lost round)
  Sources: Sport-specific play-by-play data; journalist observation
  
  Observable signals:
    Player immediately seeks the ball after an error (football)
    First serve percentage in the game after losing serve (tennis)
    First break attempt after conceding a frame (snooker)
    Body language and movement pace after a knockdown (boxing/MMA)

RECOVERY SCORE:
  Documented bounce-back pattern (stat evidence or Tier 1 source): 80–100
  No documented pattern (neutral): 50
  Documented extended negative response: 20–40

AGENT NOTE:
  Recovery rate is the PPI component most useful for live analysis.
  If an agent has live match data, update PPI recovery component
  in real-time and re-run signal at key moments.
```

---

## Sport-specific PPI baselines

```
FOOTBALL:
  Most top-flight footballers: PPI 45–65 (baseline neutral zone)
  Elite big-game players (documented): PPI 70–90
  Known pressure concerns (journalism, historical evidence): PPI 25–45
  
  Highest PPI patterns: penalty specialists, set piece takers with
  clean records in decisive moments, captains who "lead from front"
  in knockouts.
  
  Lowest PPI patterns: players with documented "big game" underperformance
  (specific media narrative + statistical backing), first-time UCL KO
  participants, players recovering from public confidence crisis.

TENNIS:
  Grand Slam winners have earned their PPI by definition. The interesting
  signal is in the players approaching their first Grand Slam final or
  returning after a long absence. Fifth-set tiebreak specialists are
  among the highest PPI players in sport. Tiebreak records are fully
  public and highly reliable.

SNOOKER:
  The Crucible (World Championship) is the clearest venue-specific PPI
  amplifier in all of sport. A player's Crucible record is a direct
  proxy for pressure performance under maximum expectation.
  Already modelled in: athlete/snooker/athlete-intel-snooker.md
  PPI adds: the generalised framework; Crucible data is the primary input.

DARTS:
  Ally Pally atmosphere is the most documented crowd-pressure environment
  in darts. Players who improve at Ally Pally (vs Tour average) have
  demonstrated positive PPI. The atmosphere is consistently hostile and
  loud — players who "feed off" it are identifiable.
  Already modelled in: athlete/darts/athlete-intel-darts.md
  PPI adds: formalised framework; Ally Pally data is primary input.

MMA:
  Championship rounds (rounds 4–5) are the most reliable PPI test in
  MMA. A fighter who fades in championship rounds (documented in fight
  analysis) has low PPI. A fighter who gets stronger late has high PPI.
  Connects directly to: athlete/mma/athlete-intel-mma.md — cardio rating
  which is the physical component; PPI adds the cognitive-perceptual layer.

NBA:
  Clutch time stats are among the most granular in sport — the NBA tracks
  performance in final 5 minutes of close games as a dedicated stat block.
  High clutch +/- is the strongest PPI signal available in any sport.
```

---

## PPI and fan token commercial signals

```
WHY PPI MATTERS FOR FAN TOKENS:

1. FTP PATH_2 supply mechanics:
   High-PPI athletes in the starting XI increase win probability in
   exactly the high-stakes matches that carry the most supply mechanics
   weight. A UCL final with a high-PPI captain is a stronger PATH_2
   catalyst than a UCL final with equivalent form but low PPI.
   
   Formula: FTP_PPI_adjustment = (avg_PPI_top5_players − 55) × 0.002
   Range: approximately ±0.02 on win probability baseline.

2. CDI events:
   A high-PPI athlete performing in a major final generates larger
   CDI events than equivalent performance in regular matches.
   PPI amplifies the social signal — fans recognise big-game players
   and respond more strongly to their performances in finals.

3. Scouting (Pattern 10):
   PPI is a component of athlete value that Transfermarkt market value
   does not capture. A high-PPI player commands a premium above their
   statistical value. Add to CVS calculation:
   PPI_premium = (PPI − 50) × 0.15 (as additional CVS component)
   Cap: ±7.5 points on CVS score.
```

---

## PPI output schema

```json
{
  "ppi_brief": {
    "athlete":     "Player name",
    "sport":       "football",
    "match":       "UCL Final",
    "pressure_tier": "TIER_A",
    "assessed_at": "2026-04-12T00:00:00Z"
  },

  "components": {
    "clutch_record":      { "score": 82, "source": "FBref clutch stats", "sample_size": 14 },
    "high_stakes_history":{ "score": 75, "appearances": 4, "low_sample": false },
    "experience_depth":   { "score": 88, "tier_ab_appearances": 11 },
    "recovery_rate":      { "score": 70, "source": "Tier 2 journalist observation" }
  },

  "ppi_score":    80,
  "ppi_modifier": 1.10,
  "ppi_label":    "STRONG",
  "flags":        [],

  "plain_english": "Bukayo Saka has a strong record in big games — he consistently performs at or above his season average when the stakes are highest. His experience depth at UCL knockout level is genuine. The PPI adds a +10% uplift to his contribution to the pre-match signal tonight.",

  "sportmind_version": "3.61.0"
}
```

---

*SportMind v3.61 · MIT License · sportmind.dev*
*See also: core/athlete-motivation-intelligence.md · core/squad-cohesion-intelligence.md*
*core/lineup-quality-index.md · core/spatial-game-intelligence.md*
*athlete/snooker/athlete-intel-snooker.md (pressure_record)*
*athlete/darts/athlete-intel-darts.md (Ally Pally modifier)*
*athlete/mma/athlete-intel-mma.md (cardio rating)*
