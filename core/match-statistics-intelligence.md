# Match Statistics Intelligence — SportMind Cross-Sport Framework

**Universal reasoning framework for applying match statistics as signal modifiers.**

This file defines the principles that apply across all sports. It is the
foundation that sport-specific statistics modules build upon. Load this file
before any `sport-statistics-{sport}.md` file.

Zero-dependency: this framework provides the reasoning layer. Agents source
statistics independently. SportMind does not store or retrieve live statistics.

---

## Overview

Statistics are not signals. They are evidence that — when correctly interpreted —
sharpen the directional signal produced by the sport domain and athlete layers.

The most common error in statistics-driven sports analysis is treating raw numbers
as predictive without context. A team with 70% possession may be dominant or
desperately chasing a deficit. A boxer with 10 knockouts may face opponents
carefully selected to produce them. This framework defines how to avoid that error.

The universal rule: **statistics modify signals; they do not replace them.**

---

## Domain Model

### The four-tier statistics hierarchy

```
TIER 1 — OUTCOME-CORRELATED STATISTICS
  Definition: metrics with demonstrated correlation to match outcomes
  across large sample sizes in peer-reviewed or extensively validated analysis.
  Weight: Primary modifier — apply before any other statistical input.
  Examples by sport:
    Football:   xG (expected goals), xGA, PPDA
    Cricket:    Economy rate (bowling), run rate vs target
    Basketball: Offensive/defensive rating, pace, true shooting %
    F1:         Qualifying delta (0.3s = race outcome predictor)
    MMA:        Significant strikes landed per minute, takedown accuracy
    Esports:    Win rate on current patch, KDA ratio
    Tennis:     First serve percentage, break point conversion rate
    Baseball:   FIP (fielding independent pitching), wOBA, exit velocity
    Ice hockey: Corsi %, PDO, power play efficiency
    AFL:        Disposal efficiency, contested possession differential
    Rugby:      Set piece success %, gainline success %
    Kabaddi:    Raid success %, do-or-die raid conversion

  IMPORTANT: Tier 1 statistics are sport-specific. The ones listed above
  are starting points, not exhaustive lists. Each sport-statistics-{sport}.md
  file defines the authoritative Tier 1 metrics for that sport.

TIER 2 — CONTEXTUAL STATISTICS
  Definition: metrics that are meaningful only when combined with Tier 1 context.
  Weight: Secondary modifier — apply after Tier 1 is established.
  Universal examples:
    Possession / territory — meaningful only with pressing/defensive shape context
    Total shots / attempts — meaningful only with quality-adjusted xG context
    Pass accuracy — meaningful only with pass direction and risk context
    Win/loss record — meaningful only within same competitive era/tier
  Rule: Never apply Tier 2 modifiers without confirming Tier 1 first.

TIER 3 — DESCRIPTIVE STATISTICS
  Definition: metrics that describe what happened but have weak predictive power.
  Weight: Contextual confirmation only — use to confirm or flag, never as modifier.
  Universal examples:
    Total possession time (without quality metrics)
    Corners/set pieces won (without delivery quality or aerial advantage)
    Total passes (without progressive direction)
    Fouls committed (without tactical context)
  Rule: Tier 3 statistics alone justify no modifier. They may support a
  Tier 1 conclusion or flag an anomaly worth investigating.
```

### Sample size requirements — universal minimums

```
SAMPLE SIZE FLOORS (hard minimums — never apply statistical modifier below these):

  Individual performance statistics:
    5 matches minimum for any team-level modifier
    10 matches for individual player modifier (performance stats)
    10 attempts for individual conversion rate (penalties, free throws, etc.)
    3 head-to-head meetings same era for H2H statistical modifier

  Season-level statistics:
    10 matches minimum before any season-average modifier applies
    Season average carries 30% weight vs recent form after 20+ matches

  Sample size discount — when below minimum but above half-minimum:
    Apply 0.50× weight to the statistical modifier (partial signal only)
    Flag: "BELOW_MINIMUM_SAMPLE" in signal output
    Never apply modifier at all if below half-minimum (< 3 matches, < 5 attempts)

  Era rule:
    Statistics from a different competitive era (previous manager, previous league
    level, different tactical system) carry 0× weight by default.
    Exception: individual physical statistics (speed, strength) carry 50% weight
    across era boundaries — the body does not reset with a managerial change.
```

### Recency weighting framework

```
UNIVERSAL RECENCY WEIGHTS (apply to all sport statistical modifiers):

  Last 3 matches / events:    100% weight (current form — maximum signal)
  Last 4-5 matches:            85% weight
  Last 6-10 matches:           65% weight
  Last 11-20 matches:          40% weight (season context)
  Earlier / season average:    25% weight

  VOLATILITY ADJUSTMENT:
    High-variance sports (MMA, individual combat, golf): increase recency weight
    Higher: 100% / 75% / 50% / 30% / 15% (last event matters most)
    
    Low-variance sports (football, basketball): standard weights apply
    
    Team sports with high squad rotation: check whether the same starting XI
    played in recent matches before applying team statistical recency weights.
    A team stat from a match with 8 rotated players is not relevant to the
    full-strength lineup's upcoming performance.

  H2H RECENCY:
    H2H statistics from the same tactical era carry 2× weight vs general form.
    H2H statistics from a different era (different manager, different division):
    apply 0× weight — tactical era matters more than the opponents' history.
```

### The five-question protocol

```
BEFORE APPLYING ANY STATISTICAL MODIFIER, answer all five:

  1. TIER QUESTION: Is this a Tier 1 statistic for this sport?
     If Tier 2 or 3: confirm Tier 1 first. If Tier 1 not available: do not proceed.

  2. SAMPLE QUESTION: Is the sample size above the minimum floor?
     If below minimum: apply 0.50× discount or do not apply at all.

  3. ERA QUESTION: Were these statistics generated in the same competitive era?
     If different era: discard or apply 0.50× for physical stats only.

  4. CONTEXT QUESTION: Does this statistic mean what it appears to mean?
     (70% possession — dominant, or losing and chasing?)
     (10 KOs in a row — genuine power, or opponent selection bias?)
     If context is ambiguous: load the relevant domain skill for clarification.

  5. CAP QUESTION: Will applying this modifier exceed the statistical modifier cap?
     Universal cap: statistical modifiers combined may not exceed ±12% of
     the adjusted_score. Above this, statistics are over-fitted to the signal.
     Exception: Tier 1 outlier events (confirmed injury to the best player) may
     exceed the cap — but only Tier 1, and only when confirmed from Tier 1 source.
```

### Statistical modifier capping framework

```
UNIVERSAL MODIFIER CAPS:

  Single Tier 1 statistical modifier:    ±8 points on adjusted_score (max)
  Single Tier 2 statistical modifier:    ±4 points on adjusted_score (max)
  Combined statistical modifier total:   ±12 points on adjusted_score (max)

  These caps prevent statistical over-fitting. The domain skill (match context,
  competition tier, home advantage) and athlete layer (squad availability, form)
  remain the primary signal drivers. Statistics sharpen; they do not override.

  EXCEPTION — confirmed Tier 1 outlier (Tier 1 stat, Tier 1 source, breaking news):
    Category 1 breaking news event (e.g., injury to best player in warm-up):
    Up to ±15 points. Requires: Category 1 event confirmed from Tier 1 source only.

  STACKING RULE: When multiple statistical modifiers point the same direction,
  apply diminishing returns to each additional modifier:
    First modifier: 100% of its value
    Second modifier same direction: 70% of its value
    Third modifier same direction: 40% of its value
    Fourth and beyond: 20% of its value each
  Prevents 5 positive statistics each adding their full modifier to the signal.
```

---

## Opponent-Specific Intelligence Framework

```
HEAD-TO-HEAD STATISTICS PROTOCOL (universal):

  STEP 1: Confirm same-era H2H exists
    Same era = same manager for both clubs, same competitive tier
    Minimum 3 meetings. If < 3 or different era: do not apply H2H stats.

  STEP 2: Identify persistent H2H anomalies
    A team consistently overperforming xG in this matchup?
    A specific statistical pattern that appears in every meeting?
    These anomalies are meaningful — some matchups produce genuine edge
    that general form statistics do not capture.

  STEP 3: Apply H2H weight
    H2H statistics: 2× weight vs general form statistics
    H2H xG (if available): strongest H2H signal — apply at full 2× weight
    H2H set piece / dead ball: stable across eras — apply at 1.5× weight
    H2H pressing success: only valid if same tactical system — apply at 1× weight

  STEP 4: Note if H2H anomaly contradicts general form signal
    If H2H stats point opposite direction to form-based signal:
    Flag as "H2H_CONTRADICTION" — do not automatically apply H2H override
    Surface the contradiction in signal output for agent/human review

OPPONENT WEAKNESS TARGETING:
  Statistics are most powerful when a team's Tier 1 strength matches an
  opponent's Tier 1 weakness in the same metric.
  Example: Team A's xG from set pieces is in the top 20% of the league.
           Team B concedes 35% of goals from set pieces.
           This alignment is a compound signal — apply both as combined modifier.
  Universal principle: look for the Tier 1 vs Tier 1 alignment across matchups.
```

---

## Data Quality Framework

```
STATISTICS SOURCE TIERS:

  Tier 1 — Official competition data:
    Official league / federation statistics
    Official broadcast partner data (e.g., ChyronHego, Hawk-Eye)
    Apply at full weight.

  Tier 2 — Validated third-party analytics:
    Established analytics platforms with documented methodologies
    (Opta, StatsBomb, Second Spectrum, Synergy Sports, Sportradar)
    Apply at 95% weight. Treat as equivalent to Tier 1 for most purposes.

  Tier 3 — Public aggregators and fan platforms:
    FBref, Understat, Basketball-Reference, FanGraphs (public versions)
    Reliable for basic statistics; methodology is documented and validated.
    Apply at 85% weight. Verify Tier 1 statistics against Tier 1/2 when possible.

  Tier 4 — Unverified / unclear methodology:
    Social media statistics, fan-compiled data, prediction market implied stats
    Apply at 50% weight MAXIMUM. Flag as low-confidence source.
    Never use Tier 4 statistics for Tier 1 modifiers.

  FRESHNESS REQUIREMENT:
    Statistics must be current-season unless specifically using H2H historical data.
    Previous-season statistics: apply 25% weight maximum (player development,
    tactical changes, and competition level shifts reduce cross-season validity).
    More than 2 seasons old: 0% weight for performance stats. Physical stats
    (speed, aerial win rate) retain 30% weight for 3 seasons.
```

---

## Cross-Sport Statistics Application Guide

```
SPORT CATEGORY → PRIMARY STATISTICAL FRAMEWORK:

  INVASION GAMES (Football, Basketball, Hockey, Rugby, Handball, AFL):
    Primary: expected outcomes (xG, expected points, etc.)
    Secondary: possession quality, territorial dominance
    Contextual: set piece, transition frequency
    Load: sport-statistics-{sport}.md for sport-specific weights

  COMBAT SPORTS (MMA, Boxing, Wrestling):
    Primary: striking/grappling efficiency, finish rate
    Secondary: cardio indicators (pace statistics, output by round)
    Contextual: reach/physical advantage, weight management
    Note: Historical H2H is highest-value statistic in combat sports

  PRECISION / INDIVIDUAL (Tennis, Golf, Snooker, Darts):
    Primary: error rate, conversion under pressure
    Secondary: consistency metrics (standard deviation of performance)
    Contextual: surface/venue-specific statistics
    Note: Individual sports — player statistics carry 100% of the modifier

  RACING (Formula 1, MotoGP, NASCAR, Horse Racing):
    Primary: qualifying position / time delta
    Secondary: mechanical reliability history, pit stop performance
    Contextual: weather impact on performance (significant for F1, MotoGP)
    Note: F1 qualifying delta already calibrated 4/4 in SportMind records

  PERFORMANCE SPORTS (Athletics, Swimming, Cycling):
    Primary: personal best / season best vs current form
    Secondary: peak timing (tapering indicators)
    Contextual: head-to-head at this specific distance/event

  TEAM STRATEGIC (Cricket, Baseball, American Football):
    Primary: matchup-specific statistics (batter vs pitcher, etc.)
    Secondary: situational statistics (pressure performance)
    Contextual: conditions (pitch, weather, venue dimensions)
    Note: These sports have the richest available public statistics
```

---

## Autonomous Execution

**Trigger conditions — when this framework's logic should self-invoke:**
- Agent is about to generate a signal and Tier 1 statistics are available
- Statistical modifier is about to exceed the ±12 point cap
- H2H contradiction detected (H2H stats conflict with form-based signal)
- Statistics source is below Tier 3 — quality check required

**Execution at autonomy Level 2:**
- Apply five-question protocol automatically before any statistical modifier
- Flag if sample size is below minimum
- Apply stacking diminishing returns without requiring explicit instruction
- Notify if statistical modifier cap is being approached

**Execution at autonomy Level 3–4:**
- Run five-question protocol as background pre-processing step
- Auto-apply recency weights to all incoming statistics
- Auto-flag H2H_CONTRADICTION for operator review if detected
- Log all statistical modifiers applied with source tier and weight

**Hard boundaries:**
- Never apply statistical modifier from Tier 4 source to Tier 1 signal position
- Never exceed ±12 point cap without a confirmed Category 1 breaking news event
- Never apply H2H statistics across era boundary (different manager/system)
- Never reduce sample size minimum below hard floors

---

## Event Playbooks

### Playbook 1: Statistics pre-processing before signal generation
```
trigger:  Tier 1 or Tier 2 statistics available before signal generation
protocol:
  1. Run five-question protocol on all available statistics
  2. Classify each statistic into Tier 1 / 2 / 3
  3. Check sample sizes against minimums
  4. Apply recency weights
  5. Check opponent-alignment (Tier 1 strength vs Tier 1 weakness)
  6. Calculate combined modifier — check against cap
  7. Apply to adjusted_score
  8. Log: statistics_used, tiers, weights, final_modifier
```

### Playbook 2: H2H statistics integration
```
trigger:  Same-era H2H statistics available (min 3 meetings)
protocol:
  1. Confirm same-era (same managers, same competitive tier)
  2. Apply 2× weight to H2H Tier 1 stats vs general form
  3. Check for H2H anomaly (persistent over/under performance vs xG)
  4. If H2H contradicts form signal: flag H2H_CONTRADICTION, surface to operator
  5. Integrate H2H modifier within statistical cap framework
```

### Playbook 3: Statistics unavailable — degraded signal protocol
```
trigger:  No Tier 1 or Tier 2 statistics available for upcoming event
protocol:
  1. Flag: "STATISTICS_UNAVAILABLE" in signal output
  2. Proceed with domain skill + athlete layer signal only
  3. Note reduced confidence in signal output
  4. Do not substitute Tier 3/4 statistics to fill the gap
  5. If H2H is available even without current-season stats: apply H2H at 50% weight
```

### Playbook 4: Conflicting statistics — two Tier 1 metrics disagree
```
trigger:  Two Tier 1 statistics point in opposite signal directions
protocol:
  1. Identify which Tier 1 metric is more directly predictive for this sport
  2. Apply primary Tier 1 metric at full weight
  3. Apply secondary Tier 1 metric at 50% weight (not discarded, but secondary)
  4. Flag: "TIER1_CONFLICT" with both metrics noted in signal output
  5. Reduce combined statistical confidence from HIGH to MEDIUM
```

---

## Signal Weight Adjustments

Universal statistical modifier weights — before sport-specific calibration:

| Modifier type | Max weight | Cap |
|---|---|---|
| Tier 1 statistical modifier | ±8 pts | Per modifier |
| Tier 2 statistical modifier | ±4 pts | Per modifier |
| H2H Tier 1 (2× weight) | ±10 pts | Combined with general form |
| Combined statistical total | ±12 pts | Absolute cap |
| Category 1 breaking news | ±15 pts | Only with Tier 1 confirmation |

---

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Pre-signal statistics | Load this file first | Universal framework |
| Sport-specific metrics | Load sport-statistics-{sport}.md | After this file |
| H2H framework | This file § Opponent-Specific | Same-era requirement |
| Breaking news impact | core/breaking-news-intelligence.md | Category 1/2 protocol |
| Data source verification | This file § Data Quality | Source tier check |

---

## Agent Reasoning Prompts

- "Statistics available: run five-question protocol before applying any modifier."
- "Tier 2 statistic: confirm Tier 1 is established first. Never apply Tier 2 in isolation."
- "Sample size below minimum: apply 0.50× discount or do not apply at all."
- "H2H statistics available: check same-era. If different manager: discard."
- "Two Tier 1 stats conflict: flag TIER1_CONFLICT. Apply primary at full, secondary at 50%."
- "Statistical cap: combined modifiers must not exceed ±12 points total."

---

## Data Sources

- Sport-specific data sources: see individual sport-statistics-{sport}.md files
- Methodology documentation: StatsBomb open methodology (statsbomb.com/resources)
- Sample size guidance: Sports analytics literature — Baio & Blangiardo (2010) for football
- Cross-sport statistics overview: American Statistical Association Sports Statistics section

---

## Compatibility

**Load before:** `sports/football/sport-statistics-football.md` and all future
`sport-statistics-{sport}.md` files.
**Sport domain:** Load alongside the relevant `sport-domain-{sport}.md`.
**Athlete layer:** `core/athlete-modifier-system.md` — statistics inform ATM calculations.
**Breaking news:** `core/breaking-news-intelligence.md` — Category 1 events override caps.
**Historical:** `core/historical-intelligence-framework.md` — H2H and recency principles.

---

*SportMind v3.88.0 · MIT License · sportmind.dev*
