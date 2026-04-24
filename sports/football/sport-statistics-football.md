# Football Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-football.md`. Load alongside the
main domain skill when granular match statistics are available. Extends the
standard signal framework with possession, set piece, and performance modifiers.

Zero-dependency: this file provides the reasoning framework. Agents source
statistics independently from their chosen data provider (Opta, StatsBomb,
FBref, Understat — see Data Sources).

---

## Overview

Match statistics transform the directional signal from the domain skill into a
calibrated, evidence-grounded output. A team with strong possession metrics facing
a high-press opponent is categorically different from two teams with equal form.
This file formalises how to translate raw statistics into signal modifiers.

The framework operates at two levels:
- **Pre-match** — historical statistics as predictive inputs
- **In-match** — live statistics as signal refinement (for agents with live data)

---

## Domain Model

### Statistics hierarchy for signal impact

```
TIER 1 — HIGHEST PREDICTIVE VALUE (apply as primary modifiers):
  Expected Goals (xG) — strongest pre-match signal across all statistics
  xG against (xGA) — defensive quality, harder to sustain than clean sheets
  Set piece xG share — proportion of xG from set pieces (see Set Piece module)
  Pressing intensity (PPDA) — passes allowed per defensive action

TIER 2 — SECONDARY MODIFIERS (apply after Tier 1):
  Possession % — meaningful only in context of PPDA and pass accuracy
  Pass accuracy — distinguishing between recycling possession and progressing
  Progressive passes / carries — actual forward intent, not just ball retention
  Penalty conversion rate — stable individual metric, high signal for cup games

TIER 3 — CONTEXTUAL SIGNALS (use to confirm or flag):
  Crosses attempted / accuracy — only significant against specific defensive shapes
  Corners won — correlated with xG but not independently predictive
  Clearances (defensive) — proxy for defensive pressure absorbed
  Interceptions — proxy for defensive line height and pressing shape

RULE: Never apply Tier 3 signals without Tier 1-2 context.
A team with high clearances but poor xGA is defending dangerously, not well.
```

### Possession intelligence

```
POSSESSION AS SIGNAL:
  Possession alone is weakly predictive of match outcome.
  Possession combined with PPDA and progressive passes is strongly predictive.

  PPDA < 9.0  = high-press team (forces errors, generates xG from turnovers)
  PPDA > 13.0 = low-press team (cedes possession, defends deeper)

  Possession modifier table:
    65%+ possession + low PPDA (< 9.0): × 1.08 favoured team
    65%+ possession + high PPDA (> 13.0): × 0.95 (possession without pressure = risk)
    40% possession + low PPDA (< 9.0): × 1.05 (pressing specialist — control is a trap)
    40% possession + high PPDA (> 13.0): × 0.90 (neither pressing nor controlling)

  NOTE: A team "sitting deep" intentionally (holding a lead, away leg of UCL)
  will show low possession and high PPDA by design. Always check match context
  before applying possession modifier.
```

### Passing intelligence

```
PASSES AS SIGNAL:
  Total passes: not meaningful without accuracy and direction
  Pass accuracy: > 88% = high technical quality; < 78% = structural pressure
  Progressive passes: passes moving the ball 10m+ toward opponent goal
  Key passes (creating shots): most directly linked to xG generation

  PASS MODIFIER:
    Progressive pass rate in top 20% of league + high pass accuracy: × 1.06
    High total passes but low progressive pass rate: × 0.97 (recycling, not advancing)
    Key passes per 90 > 1.0 from starting XI: × 1.05 (creative density)

  KEY PLAYER ABSENCE IMPACT ON PASSING:
    Loss of primary playmaker (key passes > 1.5 per 90): apply × 0.88 ATM reduction
    Load athlete-modifier-system.md for full availability calculation
```

### Defensive statistics

```
INTERCEPTIONS AND CLEARANCES:
  Neither interceptions nor clearances are standalone positive signals.
  Context is required:

  HIGH CLEARANCES + LOW xGA:
    Team defending set pieces or direct play effectively. Neutral modifier.
    
  HIGH CLEARANCES + HIGH xGA:
    Team defending under sustained pressure. Danger signal.
    Apply × 0.92 to favoured team signal if they are the team making clearances.

  HIGH INTERCEPTIONS + LOW PPDA:
    Pressing team winning the ball high up the pitch. POSITIVE signal.
    Apply × 1.06 if the pressing team is the favoured team.

  HIGH INTERCEPTIONS + HIGH PPDA:
    Intercepting in own half — reactive defending, not proactive.
    Apply × 0.95 if sustained over 5+ matches.

  CROSS MODIFIER:
    Crosses completed > 30% accuracy against a team conceding aerial duels: × 1.05
    Crossing team missing a wide specialist (winger with > 3 key passes / 90): × 0.88
    Only apply crossing modifier when opponent has documented aerial weakness.
```

---

## Set Piece Intelligence

Set pieces account for approximately 28–32% of Premier League goals (2020–2025
average) and 25–30% of top division goals across major European leagues.
For fan tokens, set piece goals are identical in CDI terms to open-play goals —
but set piece *capability* is predictable, while open-play finishing is volatile.
This makes set pieces the most underpriced signal category in standard models.

### Penalty intelligence

```
PENALTY CONVERSION RATES — AGENT PROTOCOL:

  Individual rates are stable over 10+ attempts. Treat < 10 attempts as unreliable.
  League average conversion rate: 76–78% across top European leagues.

  ABOVE-AVERAGE SPECIALISTS (> 85% conversion over 10+ penalties):
    Apply × 1.08 to xG calculation when the specialist is confirmed available
    and their team has an above-average rate of winning penalties.
    
  BELOW-AVERAGE CONVERTERS (< 70% conversion over 10+ penalties):
    Apply × 0.94 to xG calculation when they are the designated penalty taker.
    This modifier applies even if they are otherwise a Tier 1 ATM player.

  PENALTY WINNING RATE:
    Some teams systematically win more penalties than expected by xG (through
    player movement, box entries, or drawing fouls). High penalty-winning teams
    facing high PPDA opponents: × 1.05 additional modifier.

  SHOOTOUT INTELLIGENCE (knockout competitions):
    Penalty shootout outcomes are closer to random than general public believes
    (approximately 57% to the stronger team in meta-analyses).
    Do not apply individual conversion rates to shootout predictions without
    5+ shootout records per player — insufficient data for most players.
    Shootout modifier: × 1.04 maximum regardless of conversion statistics.

  PATH_2 NOTE ($AFC Arsenal):
    Any penalty scored by $AFC counts as a goal toward PATH_2 supply reduction.
    Penalty specialist availability is therefore a supply mechanics signal,
    not just a match outcome signal. Load gamified-tokenomics-intelligence.md
    alongside this modifier for $AFC analysis.
```

### Free kick intelligence

```
FREE KICK SPECIALIST MATRIX:

  Free kicks from dangerous positions (15–30m, central and channel angles)
  are the highest-value dead ball situation after penalties.
  Quality varies enormously by player, foot, and distance band.

  DISTANCE BANDS:
    18–22m: highest conversion (goalkeeper positioning constraint)
    22–28m: optimal range for most specialists (6–12% conversion typical)
    28–35m: low probability for most players (2–5% conversion)
    > 35m: negligible direct threat; primarily aerial ball into box

  FOOT AND ANGLE MATRIX:
    Right-footed player, right channel (inswing to goalkeeper's right):
      Moderate difficulty. Standard specialist modifier applies.
    Right-footed player, left channel (outswing / curl away from keeper):
      Higher difficulty. Reduce conversion estimate by 15%.
    Left-footed player, left channel (natural inswing):
      Highest value position. Apply × 1.10 specialist modifier.
    Left-footed player, right channel (outswing):
      Reduce conversion estimate by 20%.

  SPECIALIST TIERS:
    Tier 1 (elite): > 12% conversion from optimal range, correct foot/angle.
      Apply × 1.12 to set piece xG contribution.
    Tier 2 (competent): 6–12% conversion from optimal range.
      Apply × 1.05 to set piece xG contribution.
    Tier 3 (non-specialist): < 6% conversion or taking from non-optimal angle.
      Apply × 0.90 — team is likely kicking direct or hoping for second ball.

  ABSENCE MODIFIER:
    When a Tier 1 or Tier 2 free kick specialist is unavailable:
    Apply × 0.88 to that team's set piece xG.
    This is a Category 2 breaking news item — load breaking-news-intelligence.md.

  WALL POSITIONING:
    Home advantage × 1.04 for free kicks (referee positioning, familiarity).
    Away from home: reduce Tier 1 specialist modifier by × 0.97.
```

### Corner intelligence

```
CORNER DELIVERY INTELLIGENCE:

  Corners generate approximately 2–3% direct conversion to goal per corner,
  but delivery quality varies significantly.

  DELIVERY TYPES:
    Inswing (curling toward goal): higher aerial threat, more dangerous
    Outswing (curling away): harder for keeper to claim, creates second balls
    Short corner routine: maintains possession but reduces direct threat

  AERIAL DUEL DOMINANCE:
    Team with aerial duel win rate > 60% facing opponent < 50%:
    Apply × 1.06 to corner-derived xG.

  HEIGHT MISMATCH:
    If starting XI average height differential > 5cm AND opponent concedes
    > 30% of goals from set pieces: × 1.08 to corner xG.

  DELIVERY SPECIALIST ABSENCE:
    As with free kicks, the corner delivery specialist creates disproportionate
    value. Their absence reduces corner threat × 0.85.

  CROSS INTELLIGENCE (open play):
    Open play crosses from wide areas follow similar foot/angle logic to free kicks.
    A right-footed winger delivering crosses from the right touchline produces
    outswing (away from goal) — lower quality than left-footed delivery from same side.
    Crossing modifier only applies when:
    (a) the crossing specialist is confirmed available
    (b) the opponent has documented aerial weakness (< 55% aerial duel win rate)
    (c) the team has a target striker with aerial win rate > 60%
    All three conditions required for × 1.05 crossing modifier.
```

---

## Historical Statistics Framework

```
RECENCY WEIGHTING FOR STATISTICS:
  Apply the same RAF (Recency Adjustment Formula) from historical-intelligence-framework.md
  to statistical modifiers:
    Last 5 matches: 100% weight
    Last 6-10 matches: 75% weight
    Last 11-20 matches: 50% weight
    Season average: 30% weight (useful only for set piece rates — more stable)

OPPONENT-SPECIFIC HISTORICAL DATA:
  Head-to-head statistics within the same era (manager/system stable) carry
  2× weight vs general form statistics.
  H2H statistical patterns to specifically check:
    xG in this specific fixture over last 3 meetings
    Set piece vulnerability in this matchup
    Pressing success rate against this opponent's passing style
    Penalty rate in this fixture (some matchups consistently produce more)

  ERA DEFINITION: same manager, same tactical system.
  If either team has changed manager since last H2H: discard H2H statistical data
  and use only current era general form. Systems change more than players.

SAMPLE SIZE RULES:
  Minimum 5 matches for any statistical modifier to be applied.
  Minimum 10 attempts for individual penalty conversion modifier.
  Minimum 3 meetings same era for H2H statistical modifiers.
  Below minimums: apply × 0.50 weight to statistical modifier (partial signal).
```

---

## Event Playbooks

### Playbook 1: Statistical confirmation — pre-match signal enhancement
```
trigger:  Access to current season statistics for both teams
timing:   T-6h; load after domain signal is generated
protocol:
  1. Check xG and xGA for both teams (Tier 1 stats)
  2. Apply possession + PPDA modifier if applicable
  3. Check set piece specialist availability (Tier 1 set piece signal)
  4. If free kick or penalty specialist absent: apply absence modifier
  5. Recalculate adjusted_score with statistical modifiers
output:   Enhanced signal with statistical_modifiers_applied field
note:     Statistical modifiers can move adjusted_score ± 8 points maximum
```

### Playbook 2: Set piece specialist unavailable — breaking signal
```
trigger:  Confirmed absence of Tier 1 or Tier 2 set piece specialist
timing:   Immediate — Category 2 breaking news protocol
protocol:
  1. Load breaking-news-intelligence.md — Category 2 squad news
  2. Apply × 0.88 to team's set piece xG contribution
  3. If specialist is also penalty taker: apply penalty absence modifier
  4. Recalculate signal with absence modifier
  5. Dispatch updated signal with "set_piece_specialist_absent": true flag
note:     PATH_2 implication: applies to $AFC penalty specialist absence
```

### Playbook 3: Historical H2H statistics — matchup-specific signal
```
trigger:  Same-era H2H data available (same managers, min 2 meetings)
timing:   T-12h; background enrichment
protocol:
  1. Extract H2H xG, set piece patterns, pressing success
  2. Apply 2× weighting vs general form statistics
  3. Flag any persistent H2H anomalies (one team consistently overperforming xG)
  4. Note any set piece vulnerability that is H2H-specific vs general
output:   matchup_h2h_modifier field added to signal output
note:     Discard H2H data if either manager changed since last meeting
```

### Playbook 4: In-match statistics refinement
```
trigger:  Live match data available (agent has access to live statistics feed)
timing:   Ongoing from kickoff
protocol:
  15 min: check xG accumulated vs expected pace. Significant divergence = signal flag.
  30 min: possession + PPDA confirmed vs pre-match estimate. Adjust if needed.
  45 min + corners: set piece count and delivery quality assessment.
  60 min: if xG significantly outperforming: review for sustainability.
  75 min: pressing intensity typically drops. Factor into late-match signal.
output:   in_match_statistical_refinement field with current xG, possession, PPDA
note:     In-match statistics are Level 3-4 autonomy territory — load
          autonomous-agent-framework.md for live action thresholds.
```

---

## Signal Weight Adjustments

For the statistics sub-module, apply these weights on top of the standard
sport-domain-football.md signal weights:

| Statistical modifier | Weight | Cap |
|---|---|---|
| xG differential (Tier 1) | 12% additional weight | ± 8 pts |
| Set piece specialist available | 8% additional weight | ± 5 pts |
| Possession + PPDA combined | 6% additional weight | ± 4 pts |
| Passing quality (progressive rate) | 4% additional weight | ± 3 pts |
| H2H statistical patterns | 4% additional weight | ± 3 pts |
| Crossing / aerial specialist | 2% additional weight | ± 2 pts |

**Total statistical modifier cap: ± 10 points on adjusted_score.**
Prevents statistical over-fitting — sport domain and athlete modifiers
remain the primary signal drivers.

---

## Autonomous Execution

**Trigger conditions — when this skill should self-invoke:**
- Set piece specialist injury detected in squad news feed (Category 2 event)
- Live xG diverges > 0.8 from pre-match estimate at 30 min mark
- Penalty awarded in match for monitored token club

**Execution at autonomy Level 2:**
- Recalculate signal with updated statistical modifiers
- Flag any change to recommended_action
- Notify if adjusted_score crosses 75 threshold in either direction

**Execution at autonomy Level 3–4:**
- Automatically update signal output and dispatch briefing
- Log statistical modifier changes with full chain of reasoning
- For PATH_2 tokens ($AFC): flag any set piece goal immediately

**Hard boundaries:**
- Statistical modifiers never override macro_override_active
- Never apply statistical modifiers from a single match as predictive data
- Minimum sample sizes are hard floors — never reduce below them autonomously

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| Full statistical pre-match | Load this file + sport-domain-football.md | Standard combined load |
| Set piece signal only | Load Set Piece Intelligence section | For rapid specialist check |
| H2H enrichment | Load Historical Statistics Framework | Requires same-era data |
| Live match refinement | Playbook 4 + autonomous-agent-framework.md | Level 2+ agents only |

---

## Agent Reasoning Prompts

- "xG available for both teams: load Tier 1 statistics and apply modifiers before finalising signal."
- "Specialist absent from confirmed lineup: load Playbook 2 immediately. Category 2 event."
- "Same manager H2H data available: check for persistent xG anomalies before applying general form."
- "In-match at 30 min: compare current xG pace to pre-match estimate. Flag if > 0.5 divergence."
- "PATH_2 token ($AFC): set piece specialist availability is a supply mechanics signal, not just form."

---

## Data Sources

- xG and match statistics: FBref (free), Understat (free, European leagues)
- Advanced metrics (PPDA, progressive passes): FBref, StatsBomb Open Data
- Set piece analysis: StatsBomb (subscription), Opta (subscription)
- Live match statistics: SofaScore (Tier 2 — verify against official where possible)
- Official lineup confirmation: club official channels (Tier 1 only for specialist absence)

---

## Compatibility

**Load alongside:** `sports/football/sport-domain-football.md`
**Fan token layer:** `fan-token/football-token-intelligence/token-intelligence-football.md`
**Athlete layer:** `athlete/athlete-modifier-football.md`
**Breaking news:** `core/breaking-news-intelligence.md` (Category 2 for specialist absence)
**PATH_2 tokens:** `fan-token/gamified-tokenomics-intelligence/` ($AFC set piece goals)

---

*SportMind v3.87.0 · MIT License · sportmind.dev*
