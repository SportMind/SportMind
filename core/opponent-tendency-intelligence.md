---
name: opponent-tendency-intelligence
description: >
  Framework for building and applying historical tendency profiles of
  specific opponents — teams, coaches, and individual athletes. Distinct
  from tactical-matchup-intelligence (which scores structural system
  mismatches) — this skill models what a specific opponent TYPICALLY DOES
  in specific situations, derived from historical behavioural patterns.
  Covers four tendency domains: (1) In-game decision tendencies (coach
  substitution timing, formation shifts, timeout usage); (2) Situational
  tendencies (how a team/athlete behaves when leading, trailing, in
  high-pressure moments); (3) Set-piece routine tendencies (corner kick
  delivery patterns, free kick positioning, penalty tendencies); (4)
  Athlete-level micro-tendencies (dribble direction bias, serve pattern
  under pressure, grappling entry preference). Produces an Opponent
  Tendency Profile (OTP) that feeds into the pre-match signal chain as
  a contextual intelligence layer. Cross-sport: football, basketball,
  MMA, tennis, cricket, ice hockey, rugby. Fan token application: OTP
  signals feed into pre-match FTIS computation — a team with well-profiled
  opponents and documented tendency exploitation has measurably higher
  match win probability adjustments that affect supply mechanics.
---

# Opponent Tendency Intelligence — SportMind

**Teams and athletes are not random. They have patterns. Patterns are
exploitable. Exploitation is quantifiable.**

`core/tactical-matchup-intelligence.md` answers: given these two systems,
which structural advantages exist? This skill answers a different question:
given this specific opponent, what will they actually do — and which of
their habitual tendencies can be exploited or anticipated?

The distinction matters. A team might have a structural pressing advantage
over the opponent's build-up system (TMAS +6) but if the opponent's coach
historically switches to a low-block when losing at half-time (a documented
tendency), that structural advantage may never materialise. Tendency intelligence
makes the signal chain situationally aware, not just structurally aware.

---

## The Opponent Tendency Profile (OTP)

```
OTP = {
  team_tendencies:     coach_behaviour + formation_tendencies,
  situational_profile: leading + trailing + high_pressure,
  set_piece_patterns:  corner_delivery + dead_ball + penalties,
  athlete_tendencies:  individual micro-patterns (sport-specific)
}

HOW OTP MODIFIES THE SIGNAL CHAIN:
  OTP is not a modifier value — it is a CONTEXT LAYER that adjusts
  which modifiers are most relevant and whether structural signals
  will actually manifest.

  Usage: Load OTP after TMAS. If documented tendency contradicts
  structural signal, flag the conflict for human review rather than
  silently applying TMAS. Tendency intelligence increases confidence
  when it aligns with structural signals; creates FLAGS when it contradicts.

SAMPLE SIZE REQUIREMENTS:
  For reliable tendency identification:
    Team tendencies:       minimum 20 matches in relevant context
    Coach in-game decisions: minimum 15 matches as head coach of this team
    Individual athlete tendencies: minimum 30 relevant situations observed
  Below minimum: classify as PRELIMINARY (lower confidence)
```

---

## Domain 1 — Coach and team in-game tendencies

```
SUBSTITUTION TIMING TENDENCIES:
  Early (< 55 min): coach responds to scoreline quickly
    → If losing at 55 min: 78% of observations showed attacking sub
    → If drawing at 55 min: typically defensive consolidation
  Standard (56–70 min): most coaches; baseline
  Late (> 71 min): conservative; prefers to ride out the game
    → Late substitutors: match is usually decided before they react

FORMATION SHIFT TENDENCIES:
  "Going for it" triggers (when trailing):
    Shifts to higher line of engagement: which scoreline triggers this?
    Brings on an extra attacker: what deficit triggers the change?
    From back-4 to back-3: documented or rare for this coach?
  "Protecting" triggers (when leading):
    Drops into deeper block: what lead triggers this?
    Makes defensive substitution first: compare vs attacking sub ratio
    Slows tempo deliberately: measurable via possession-under-pressure %

TIMEOUT AND STOPPAGE TENDENCIES (basketball, volleyball, American football):
  Timeout usage patterns:
    First timeout timing (average, by game situation)
    Timeout clusters (sequential use to disrupt opponent momentum)
    End-of-half / end-of-quarter preference
  Agent rule: Cluster timeout usage = tendency to disrupt momentum spikes;
    apply when opponent is on a run of 8+ unanswered points

SPORT-SPECIFIC COACHING TENDENCIES:
  Football: high-press triggers vs low-block instructions at set scores
  Basketball: small-ball lineups (when deployed, vs which opponents)
  Cricket: aggressive field placements in death overs vs defensive
  MMA: corner advice patterns (push vs consolidate between rounds)
  Rugby: kicking vs carrying game selection by territory and scoreline
  Ice hockey: pull-goalie timing (when leading vs exact time remaining)
  Tennis: server tendency under pressure (body serve % when break point down)
```

---

## Domain 2 — Situational tendencies

```
WHEN LEADING:
  Does the team/athlete protect or continue pressing?
    Protection tendency: close-game wins in last 15 min when ahead 1-0:
    what % involved defensive shape deepening vs maintained press?
  Risk profile when leading:
    LOW RISK (protects leads reliably): reduces opponent OTP threat
    HIGH RISK (continues pressing, vulnerable to counter): amplifies risk

WHEN TRAILING:
  Desperation patterns vs tactical adjustment:
    Early trailing (< 30 min): does coach change shape or wait?
    Late trailing (> 70 min): predictable all-out attack vs managed approach
    Do they tend to concede more when behind? (loss of organisation under pressure)
  Tendency to score late equalisers:
    Track: trailing at 75 min → outcome frequency
    PATTERN SIGNAL: teams that equalise frequently when trailing late
    are structurally underestimated by standard form signals

HIGH-PRESSURE SITUATIONAL TENDENCIES:
  Elimination/must-win matches (from core/core-narrative-momentum.md):
    Does historical performance improve or decline under must-win pressure?
    Track: elimination match record vs standard performance
    ELIMINATION_RISER: performs above season average in must-win
    ELIMINATION_FALLER: performs below season average in must-win
  
  Derby / rivalry match tendencies (from core/derby-intelligence.md):
    Does rivalry context improve or flatten their typical tendencies?
    Some teams become more predictable (revert to direct play, more set pieces)
    Some teams become less predictable (unusual tactical choices)

  Back-to-back / congestion tendencies:
    Does this team's style change under fixture congestion?
    Track: pressing intensity, transition speed in match 3-of-7-days
    vs same team in standard preparation
```

---

## Domain 3 — Set piece tendencies

```
CORNER KICK DELIVERY PATTERNS:
  Inswinger vs outswinger: which delivery type by side of pitch?
  Near-post routine frequency: what % of corners target near post?
  Back-post flick-on: frequency and which players involved?
  Short corner frequency: when deployed (typical game state trigger)?
  Key delivery athletes: which player takes corners in high-pressure moments?

  OTP APPLICATION:
    Known set piece threat team + opponent with poor aerial marking:
    → Amplify structural TMAS set piece differential by ×1.15
    Known set piece threat team + opponent with strong aerial markers:
    → Apply at face value (structural signal holds)

FREE KICK TENDENCIES:
  Direct attempt frequency by zone:
    Zone 1 (< 20m from goal): direct attempt % vs crossing %
    Zone 2 (20–30m): which players attempt direct shots?
    Zone 3 (30m+): typically recycled vs speculative attempt
  Wall run timing: players who time runs into space from free kicks

PENALTY TENDENCIES (where applicable):
  Direction bias: left/right/centre tendency over last 30+ penalties
  Run-up change tendency: does the player stutter vs smooth run-up?
  Penalty under pressure (shootout vs open play): does tendency change?
  KEY RULE: Never publish penalty direction data publicly — use privately
  only. Opponents can also adapt. Flag this as intelligence with half-life.

SPORT-SPECIFIC SET PIECE EQUIVALENTS:
  Basketball:      end-of-game play calling patterns; pick-and-roll default
  Rugby:           lineout calling patterns by position and game state
  Cricket:         field setting patterns by bowling type and match situation
  Ice hockey:      power play formation and primary option sequence
  American football: red zone play tendencies by down and distance
```

---

## Domain 4 — Athlete micro-tendencies

```
INDIVIDUAL ATHLETE TENDENCY PROFILES:

FOOTBALL:
  Winger: preferred dribble direction (inside cut vs outside run)
    Frequency of inside cuts when ball received on preferred foot
    → Defender pre-positioning exploits this tendency
  Striker: finishing preference (near post, far post, penalty area zone)
  Midfielder: scanning frequency before receiving (predictive of decision speed)
  Goalkeeper: distribution tendency (long kick vs short play)

BASKETBALL:
  Ball handler: drive direction preference (left vs right)
  Shooter: pull-up vs drive tendency in pick-and-roll coverage
  Post player: drop step direction tendency
  Application: defensive scheme switches based on tendency profile

MMA / COMBAT SPORTS:
  Striking entries: preferred combination starters (jab-cross, body-head)
  Grappling entry: shot level (high vs low single/double leg)
  Clinch behaviour: offensive vs defensive; wall-work tendency
  Round 3 pattern: does fighter accelerate, conserve, or maintain?
  WEIGHT MISS ADDITION: fighters who have previously missed weight show
  altered tendency profiles in rounds 4–5 (energy management shifts)

TENNIS:
  Serve pattern under pressure: direction tendency on break point
  Return positioning: wide forehand return vs backhand preference
  Net approach triggers: which shot type typically precedes net approach?
  Tie-break tendency: does pattern simplify or diversify under tie-break pressure?

CRICKET:
  Bowler: go-to delivery when wicket needed (bouncer, yorker, off-cutter)
  Batter: technical weakness zone (outside off stump channel tendency)
  Captain: aggressive vs defensive field setting under pressure

ICE HOCKEY:
  Shooter: backhand tendency, shot selection from specific zones
  Centre: faceoff stance by zone (weak hand forward % and position)
  Defenceman: pinch tendency in offensive zone possession

RUGBY:
  Fly-half: kick vs carry decision by territory and proximity to opposition 22
  Back-row: breakdown clearing technique (from feet vs driving)
  Scrum-half: dummy half run tendency
```

---

## OTP output schema

```json
{
  "otp_brief": {
    "subject":       "Arsenal FC",
    "subject_type":  "team",
    "context":       "UCL Quarter-Final, away fixture",
    "assessed_at":   "2026-04-14T00:00:00Z",
    "sample_size":   "28 UCL matches under Arteta"
  },

  "coach_tendencies": {
    "trailing_at_60min":       "attacking substitution in 82% of observations",
    "formation_shift_trigger":  "goes to 3-4-3 when trailing by 1+ after 65 min",
    "leading_behaviour":        "drops into mid-block, reduces press intensity",
    "confidence":               "HIGH (28 match sample)"
  },

  "situational_profile": {
    "must_win":          "ELIMINATION_RISER — 73% win rate in elimination matches vs 67% overall",
    "when_trailing":     "significantly more direct play; set piece frequency increases 40%",
    "when_leading_late": "backs off press; vulnerable to transition from deep positions"
  },

  "set_piece_patterns": {
    "corner_delivery":   "inswinger from right flank (82%), near-post target (White, Gabriel)",
    "free_kick_zone_2":  "direct attempt from Saka or Odegaard; taker depends on angle",
    "penalty_record":    "[PRIVATE — not output in shared schema]"
  },

  "signal_chain_impact": {
    "tmas_alignment":    "CONFIRMS — structural pressing advantage likely to be deployed",
    "conflict_flags":    [],
    "confidence_adjustment": "+0.04 (tendency confirms structural signal)"
  },

  "plain_english": "Arsenal's tendency profile for away UCL knockout matches is well-documented: they press aggressively until conceding, then Arteta triggers an attacking sub quickly (usually before 65 min). If they're leading, they drop deep and become vulnerable in transition. The near-post inswing corner is their most reliable set-piece — if the opponent has poor near-post marking, weight this signal. No conflicts with the structural TMAS assessment.",

  "sportmind_version": "3.66.0"
}
```

---

## Agent loading rules

```
LOAD THIS SKILL WHEN:
  1. Match involves a well-documented opponent with significant historical record
  2. A coaching change has occurred < 10 matches ago (new tendency baseline forming)
  3. Structural TMAS produces a strong signal — use OTP to confirm or flag conflicts
  4. Set piece differential is a primary signal variable for this match
  5. Athlete tendency profiles are relevant (penalty shootout approaching in knockout)

DO NOT LOAD WHEN:
  Sample size is below minimum thresholds — preliminary OTP is noise
  Opponent is playing their first season under current coach (< 15 matches)
  Using OTP to override a strong structural signal without evidence

DATA SOURCES:
  Primary: Core coaching and tactical data from Tier 1 sports media
  Club press conference tendency data (manager language decoder applies)
  Statistical providers: Opta, StatsBomb, second-spectrum tracking data
  Community-contributed tendency records (flag as community-sourced)

TENDENCY HALF-LIFE:
  Coach substitution timing:      12–18 months (refreshes with new players)
  Formation shift triggers:       6–12 months (may adapt after analysis)
  Set piece routines:             4–8 weeks (most frequently changed)
  Athlete micro-tendencies:       Seasonal (may change with new coaching)
  Must-win situational profile:   Persistent (character-based, stable)
```

---

*SportMind v3.66 · MIT License · sportmind.dev*
*See also: core/tactical-matchup-intelligence.md · core/core-officiating-intelligence.md*
*core/derby-intelligence.md · core/core-narrative-momentum.md*
*core/spatial-game-intelligence.md · core/manager-intelligence.md*
*examples/agentic-workflows/scouting-agent.md (Pattern 10)*
