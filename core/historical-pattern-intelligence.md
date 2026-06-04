---
name: historical-pattern-intelligence
description: >
  Enduring reasoning framework for applying historical patterns as signal modifiers.
  Covers sample requirements, competition stage performance patterns, tactical matchup
  patterns, seasonal position patterns, and fan token historical demand patterns.
  Not archival data — how to reason when patterns are confirmed across sufficient samples.
---

# Historical Pattern Intelligence

**How to reason about recurring historical patterns as enduring signal modifiers.**
Not archival data — the framework for applying confirmed patterns.

> Load alongside: `core/psychological-intelligence.md` (minimum sample framework
> and psychological pattern reasoning — do not duplicate).

---

## Minimum sample requirement

```
SAMPLE REQUIREMENT FRAMEWORK:

  All historical pattern modifiers in this file share the same sample requirement.
  See: core/psychological-intelligence.md for the core sample requirement principle.
  
  TIERED APPLICATION:
  
  Fewer than 5 comparable situations:
    Do NOT apply a pattern modifier.
    Apply: insufficient_sample_flag = true
    Note this as uncertainty in signal output.
    
  5 to 9 comparable situations:
    Apply modifier at ×0.50 CONFIDENCE WEIGHT.
    i.e.: A pattern modifier of ×1.06 becomes ×1.03 (50% of the deviation applied)
    Note: pattern_confidence = MODERATE in signal output.
    
  10 or more comparable situations:
    Apply full modifier.
    Note: pattern_confidence = HIGH in signal output.
    
  ENDURING PATTERN QUALIFICATION:
    A pattern is only enduring (and therefore belongs in this framework) when:
    1. It spans different squad compositions — not just one golden generation
    2. It spans different manager regimes — not just one tactical era
    3. It has repeated across at least two distinct time periods
    If the pattern fails these tests: it is circumstantial, not structural.
    Do not apply as an enduring modifier — apply as a contextual note only.
```

---

## Competition stage performance patterns

```
CUP TEAM PATTERN — KNOCKOUT OVERPERFORMANCE:

  DEFINITION:
    Some clubs consistently outperform their league standing in cup and knockout
    competition — performing better than expected based on squad quality alone.
    
  IDENTIFICATION:
    Club wins knockout rounds at a rate significantly above their league win rate.
    Pattern spans 2+ managerial regimes and 2+ distinct squad eras.
    Minimum 5 cup runs across which the overperformance is observed.
    
  MODIFIER:
    Confirmed cup team pattern: ×1.06 applied to knockout round signal
    Apply to: each knockout round match (not group stage or league matches)
    Condition: pattern must be in knockout stage ONLY — not all cup matches
    
  MECHANISM:
    Short preparation windows favour organised defensive teams.
    Single-leg or two-leg knockout formats suit compact, counter-attacking styles.
    Cup team identity creates psychological clarity — different from league mode.
    
  LIMIT:
    Do not apply cup team modifier AND clutch performer modifier simultaneously.
    They overlap conceptually. Apply the more specific modifier (cup team in cup
    matches; clutch performer in finals and high-stakes single matches).

FINAL ANXIETY PATTERN — FINAL UNDERPERFORMANCE:

  DEFINITION:
    Some clubs consistently underperform in finals despite performing well in
    semi-finals and throughout the tournament — reaching finals but losing them
    at a rate above what squad quality would predict.
    
  IDENTIFICATION:
    Minimum 3 comparable finals in which underperformance is observed.
    Pattern: win rate in finals below win rate in semi-finals for this club.
    Note: 3 finals is a lower sample threshold because finals are rare events.
    Apply ×0.50 confidence weight for 3-4 finals; full weight for 5+ finals.
    
  MODIFIER:
    Confirmed final anxiety pattern: ×0.94 applied to adjusted score in finals
    Apply to: finals only — not semi-finals, not earlier rounds
    
  DISTINGUISH FROM CHOKING:
    Choking pattern (psychological-intelligence.md): general high-pressure underperformance
    Final anxiety pattern: specifically finals — some clubs perform well under knockout
      pressure generally but deteriorate specifically in finals
    Apply the more specific modifier when both could apply.
    
OVERPERFORMANCE IN SPECIFIC COMPETITION CONTEXTS:

  Some clubs have enduring strong records in specific competitions (domestic cups,
  continental competitions) that exceed their general performance level.
  
  ASSESSMENT:
    Win rate in this specific competition vs win rate in equivalent fixtures
    in other competitions. If significantly higher (15%+ above), pattern exists.
    
  MODIFIER:
    Competition-specific overperformance: ×1.04 (moderate; competition context varies)
    Apply only within the specific competition — not cross-competition.
```

---

## Tactical matchup patterns

```
HIGH-PRESS VERSUS LOW-BLOCK — RECURRING MATCHUP PATTERN:

  DOCUMENTED PATTERN:
    High-pressing teams historically struggle against organised low-block defences
    when the press fails to produce an early goal. The longer the match stays
    goalless, the more the low-block team's structural advantage compounds.
    
  MODIFIER FRAMEWORK:
    Pre-match: identify high-press team vs confirmed low-block opponent
    Standard pre-match signal applies (no modification)
    
    IN-MATCH (after 30 minutes goalless):
      Apply: press_frustration_modifier = ×0.93 to high-press team's adjusted score
      Mechanism: pressing energy wasted without reward; low-block opponent increasingly
        confident; high-press team's most productive window (first 30 min) has passed
        
    IN-MATCH (after 60 minutes goalless):
      Apply: press_frustration_modifier = ×0.90 (deepening frustration)
      Low-block team's win probability increases accordingly
      
  PRE-MATCH APPLICATION:
    This is primarily an in-match reasoning tool — not a pre-match modifier.
    Pre-match: flag the matchup type (press vs low-block) in the signal output.
    In-match: apply the time-based modifier when the pattern is confirming.

POSSESSION VERSUS TRANSITION — SURFACE INTERACTION:

  HIGH-POSSESSION TEAMS VS TRANSITION-FOCUSED OPPONENTS:
    High-possession teams are structurally exposed to counter-attacking transitions.
    This exposure is amplified on specific pitch surfaces:
    
    FIRM, FAST SURFACE:
      Transition opportunities are more dangerous (ball moves faster in counter)
      Apply: possession_vs_transition_surface_modifier = ×0.96 for possession team
      (see venue-intelligence.md for soft/firm surface framework)
      
    SOFT, HEAVY SURFACE:
      Transition attacks slowed by pitch — possession team's structural exposure reduced
      Apply: no modifier for possession vs transition on soft pitch
      
  ENDURING CLUB-LEVEL PATTERN:
    Some clubs have enduring tactical matchup strengths/weaknesses beyond surface:
    Apply only when the matchup pattern spans 5+ meetings between these specific
    tactical style types and is confirmed enduring across squad generations.
```

---

## Seasonal position patterns

```
CHRISTMAS FIXTURE CONGESTION — SQUAD DEPTH INTERACTION:

  English Premier League and Championship have a dense fixture schedule in
  December–January (typically 6-8 matches in 3-4 weeks). This creates a
  predictable pattern based on squad depth.
  
  SQUAD DEPTH × CONGESTION INTERACTION:
    Deep squads (20+ quality first-team players):
      Congestion modifier: ×0.97 (small impact — depth absorbs rotation)
    Standard squads (16-20 quality players):
      Congestion modifier: ×0.94 (standard; third match in sequence)
    Shallow squads (<16 quality players):
      Congestion modifier: ×0.91 (significant; fatigue compounds for regular starters)
      
  APPLICATION:
    Apply from the third match in any 10-day window of 3+ matches.
    Combine with seasonal-intelligence.md fixture congestion framework.
    
FINAL DAY MOTIVATION PATTERNS:

  End-of-season final day creates one of the most complex motivation signals
  in all of football. Multiple scenarios produce different modifier effects.
  
  TEAM WITH NOTHING TO PLAY FOR:
    Mid-table team, guaranteed of their position, playing against a rival in crisis.
    Apply: dead_rubber_motivation_modifier = ×0.93
    Reason: reduced intensity is well-documented when stakes are zero.
    
  TEAM UNDER RELEGATION PRESSURE:
    Apply: survival_motivation_modifier = ×1.05 to adjusted score
    Reason: survival instinct produces above-average intensity (paradoxically benefits)
    Combine with: relegation_crisis modifier from tier-a-clubs-framework.md
    
  TEAM IN TITLE RACE ON FINAL DAY:
    Apply: title_pressure_modifier — use clutch/choking pattern from
    psychological-intelligence.md (the psychological framework is more precise here)
    
  TEAM WITH HOME ADVANTAGE AND CROWD EXPECTATIONS:
    Final day crowd (full sell-out expected): apply sell-out modifier from venue-intelligence.md
    Combine with appropriate motivation modifier from above.
```

---

## Fan token historical demand patterns

```
TITLE CHALLENGE VS TROPHY-LESS SEASONS — DEMAND PATTERN:

  TITLE CHALLENGE SEASON:
    When a fan token club is in a genuine title challenge (top 2 with 10+ matches
    remaining), demand patterns show sustained amplification throughout the run.
    
    Title contention demand modifier: ×1.15 sustained (see seasonal-intelligence.md)
    Historical pattern amplifier: if club has NOT won the title for 5+ years:
      Apply: historical_drought_narrative_modifier = ×1.05 additional
      Reason: narrative weight ("ending the wait") amplifies holder engagement
      
  TROPHY-LESS SEASON:
    When the season ends without a trophy:
      Standard post-season demand adjustment applies (seasonal-intelligence.md)
      
  CONSECUTIVE TROPHY-LESS SEASONS:
    First trophy-less season: standard demand pattern (no extra modifier)
    Second consecutive: no immediate additional modifier
    Holder expectation recalibration happens gradually
    
HOLDER FATIGUE — CONSECUTIVE UNDERPERFORMANCE MODIFIER:

  DEFINITION:
    Holder fatigue occurs when a club consistently underperforms relative to
    holder expectations across two or more consecutive seasons.
    
  THRESHOLD:
    Two consecutive seasons of below-expectation performance.
    "Below expectation" = finishing materially below the level that
    attracted original holders (e.g. expected UCL, finished mid-table).
    
  MODIFIER:
    holder_fatigue_modifier = ×0.92 applied to demand baseline
    This reflects structural holder base erosion: holders who stay have
    lower expectations; new holders less attracted to underperforming club.
    
  REMOVAL CONDITIONS:
    One season of materially above-expectation performance removes the modifier.
    Trophy win: removes holder fatigue modifier immediately.
    
  LIMITS:
    Holder fatigue modifier cannot stack below ×0.88 regardless of how many
    consecutive underperformance seasons occur.
    Floor: ×0.88 — this is the structural demand floor for major clubs.

RECOVERY FROM EXTENDED LOW PERIOD:

  When a club returns to above-expectation performance after an extended
  underperformance period, demand recovery shows a specific pattern:
  
    First season of recovery: demand recovers to pre-fatigue baseline level
    Second season of sustained performance: ×1.03 above pre-fatigue baseline
      (recovery premium — returning holders re-engage and new holders attracted)
    Trophy win during recovery: skip recovery curve; apply trophy premium directly
```

---

## Compatibility

**Psychological patterns:** `core/psychological-intelligence.md` (choking, clutch, minimum sample)
**Venue interaction:**      `core/venue-intelligence.md` (surface modifiers)
**Seasonal patterns:**      `core/seasonal-intelligence.md` (congestion, final day)
**Demand baselines:**       `fan-token/fan-token-lifecycle/`
**Relegation patterns:**    `athlete/football/tottenham-hotspur-spurs.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Pattern recognition across historical sports data for predictive intelligence |
| Reasoning | ACTIVE | Pattern-to-prediction reasoning chain with confidence weighting by pattern strength |
| Context | ACTIVE | Pattern context: recency, frequency, sample size, era relevance |
| Memory | ACTIVE | Pattern library with frequency, success rate, and context conditions |
| Judgment | ACTIVE | Judgment on pattern applicability — small sample patterns require uncertainty flag |
| Attention | ACTIVE | Attention elevation when current signal matches a historically strong pattern |
| Communication | ACTIVE | Pattern match output with sample size, success rate, and confidence |
| Verification | ACTIVE | Pattern frequency data requires verifiable historical records |
| Learning | ACTIVE | Pattern library updated continuously from calibration outcome data |
| Integration | ACTIVE | Pattern intelligence integrates with domain-specific files across all sports |
| Calibration | ACTIVE | Pattern success rates are calibration outputs — empirically derived |
| Adaptation | ACTIVE | Patterns deprecated when sport conditions change enough to invalidate them |
| Ethics | NOT APPLICABLE | Pattern recognition is analytical — no ethical dimension |
| Transparency | ACTIVE | Pattern sample size and recency explicit in all pattern-based outputs |


---

*SportMind v3.97.36 · MIT License · sportmind.dev*
*Enduring patterns only — minimum 5 comparable situations; spans multiple squads and managers*
