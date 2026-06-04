---
name: psychological-intelligence
description: >
  Enduring reasoning framework for psychological factors as pre-match and
  in-season signal modifiers. Covers pressure performance patterns, momentum,
  rivalry psychology, comeback psychology, post-trophy effects, and fan token
  psychological demand signals. Not current mental state — how to reason about
  patterns when live context arrives.
---

# Psychological Intelligence

**How to reason about psychological factors as signal modifiers.**
Not current mental state — the enduring framework for applying psychological
patterns when live context is provided by the agent.

> Library Rule: no named players, no current scores, no live states.
> All elements describe reasoning patterns that are permanently true.

---

## Pressure and performance reasoning

```
THE PRESSURE PERFORMANCE FRAMEWORK:

  PRINCIPLE:
    High-stakes situations affect performance probability differently from
    standard fixtures — but not uniformly. Teams and athletes vary in how
    they respond to pressure. This is measurable and enduring.
    
  SAMPLE MINIMUM:
    Five comparable high-pressure situations is the minimum before applying
    a psychological pattern modifier. Below five: too small to distinguish
    genuine pattern from variance.
    Apply: minimum_sample_flag = true when fewer than 5 comparable situations

CHOKING PATTERN FRAMEWORK:

  DEFINITION:
    A choking pattern is documented underperformance in high-pressure situations
    (finals, must-win matches, decisive moments) relative to the team's or
    athlete's standard performance level.
    
  IDENTIFICATION CRITERIA (all required):
    1. 5+ comparable high-pressure situations in historical record
    2. Win rate in those situations significantly below overall win rate
    3. Pattern is recent (within last 3 seasons) — old patterns decay
    4. Not explained purely by opponent quality differential
    
  MODIFIER:
    Confirmed choking pattern: ×0.92 applied to adjusted score in
    equivalent high-pressure situations
    Example: finals, knockout matches, must-win last match of season
    
  QUALIFICATION:
    Apply ONLY to the specific situation type in which the pattern appeared.
    A team that chokes in finals does NOT get the modifier in group stage matches.
    Situational specificity is required.

CLUTCH PERFORMER FRAMEWORK:

  DEFINITION:
    A clutch pattern is documented overperformance in high-pressure situations
    relative to the team's or athlete's standard performance level.
    
  IDENTIFICATION CRITERIA (all required):
    1. 5+ comparable high-pressure situations in historical record
    2. Win rate in those situations significantly above overall win rate
    3. Pattern is recent (within last 3 seasons)
    4. Not explained purely by opponent quality differential
    
  MODIFIER:
    Confirmed clutch pattern: ×1.08 applied to adjusted score in
    equivalent high-pressure situations
    
  AGENT RULE:
    Before applying either modifier:
      1. Confirm the situation type matches the historical pattern
      2. Confirm the sample meets the minimum of 5 comparable situations
      3. Confirm the pattern is within the last 3 seasons
      4. Apply to both teams independently — one may have a choking pattern,
         the other a clutch pattern, creating a compound signal
```

---

## Momentum and confidence signals

```
WIN STREAK MOMENTUM MODIFIER:

  Win streaks modify expected performance through elevated squad confidence,
  positive psychological environment, and opponent psychological preparation.
  
  MOMENTUM MODIFIER TABLE:
    3 consecutive wins:    ×1.03
    5 consecutive wins:    ×1.06
    7+ consecutive wins:   ×1.08 (CEILING — momentum does not compound indefinitely)
    
  OPPONENT QUALITY DISCOUNT:
    Momentum built against weak opposition is worth less.
    If 70%+ of the streak was against bottom-half opposition:
      Apply: opponent_quality_discount = ×0.75 to the momentum modifier
      (i.e. ×1.03 becomes ×1.022; ×1.06 becomes ×1.045 effectively)
    Reason: weak opponent momentum does not transfer to tough fixtures
    
  STREAK BREAK EFFECT:
    When a win streak ends: remove momentum modifier immediately.
    Do not carry momentum from a broken streak.

LOSS STREAK CONFIDENCE EROSION:

  Loss streaks erode squad confidence, create psychological fragility,
  and increase individual error rates under pressure.
  
  EROSION MODIFIER TABLE:
    3 consecutive losses:  ×0.96
    5 consecutive losses:  ×0.93
    7+ consecutive losses: ×0.90 (FLOOR — erosion does not compound beyond this)
    
  OPPONENT QUALITY DISCOUNT (same logic):
    If 70%+ of the streak was against top-half opposition:
      Reduce the erosion modifier — losing against strong teams is less
      psychologically damaging than losing against weak teams.
      Apply: opponent_quality_amelioration = ×0.50 to the erosion modifier
      
  RECOVERY SIGNAL:
    One win does not automatically remove the loss streak erosion modifier.
    Apply: 2-match wait before removing loss streak modifier after a win.
    Genuine recovery requires sustained performance, not a single result.
    
  MANAGERIAL INTERVENTION:
    If a new manager is appointed during a loss streak, the new manager
    effect (see coaching-intelligence.md) partially overrides the loss
    streak erosion. Apply: new manager modifier replaces loss streak modifier
    from match 1 of new manager's tenure.
```

---

## Rivalry psychology framework

```
RIVALRY PSYCHOLOGY — BEYOND FORM:

  WHY RIVALRIES REQUIRE SEPARATE TREATMENT:
    Derby matches and historical rivalries produce psychological effects
    that standard form-based analysis cannot fully capture.
    A team on poor form can significantly overperform against a specific
    rival. A team in excellent form can underperform against a psychologically
    challenging opponent.

HISTORICAL H2H DOMINANCE MODIFIER:

  ASSESSMENT:
    Review last 10 competitive meetings between these teams.
    
  DOMINANCE MODIFIER TABLE:
    70%+ H2H win rate in last 10 meetings:  ×1.04 for dominant team
    30% or below H2H win rate:              ×0.96 for submissive team
    40–60% (balanced H2H):                  no modifier — standard signal
    
  RECENCY WEIGHTING:
    Last 3 meetings carry twice the weight of meetings 4-10.
    If recent meetings (last 3) contradict long-term trend: reduce modifier
    by half — trend may be reversing.

DERBY MATCH PSYCHOLOGICAL MODIFIER:

  LOCAL DERBIES (same city or region):
    Apply ×1.10 to the home advantage baseline regardless of current form.
    Mechanism: crowd intensity amplifies psychological pressure on both sides;
      players on the home team are elevated; away team faces maximum hostility.
    This modifier COMPOUNDS with the standard venue home advantage.
    
  FORM SUSPENSION IN DERBIES:
    Form signals carry ×0.80 weight in local derbies.
    Derby results are less predictable from form than standard matches.
    Reason: psychological stakes neutralise form advantages partially.
    Apply: derby_form_discount = ×0.80 on all form-derived modifiers.
    
  AGENT RULE:
    For any confirmed local derby:
      1. Apply home advantage × 1.10 amplifier
      2. Apply H2H dominance modifier if applicable
      3. Discount all form modifiers by ×0.80
      4. These apply simultaneously
```

---

## Comeback and trailing psychology

```
FIRST GOAL PSYCHOLOGICAL IMPACT:

  SCORING FIRST:
    Scoring the first goal in a match creates a psychological advantage
    that compounds with the structural advantage (opponent must change plan).
    Apply: first_goal_scorer_modifier = ×1.06 to match outcome probability
    for the scoring team.
    
  CONCEDING FIRST:
    Apply: first_goal_conceder_modifier = ×0.94 to match outcome probability
    for the conceding team.
    
  EXCEPTION — COMEBACK SPECIALIST TEAMS:
    Some clubs have documented comeback ability — they win after conceding first
    at an above-average rate. Identify via historical data.
    Comeback specialist: reduce conceder modifier to ×0.97 (less negative)
    Apply only with 10+ matches of documented comeback sample.

HALF-TIME DEFICIT REASONING:

  TEAM TRAILING BY ONE GOAL AT HALF-TIME:
    Standard comeback probability varies by: club identity, manager style,
    home or away status, opposition quality.
    
    BASE MODIFIER (one goal down at half-time):
      Win probability modifier: ×0.85 for trailing team
      This reflects the structural disadvantage, not psychological pessimism.
      
    ADJUSTMENT FOR COMEBACK SPECIALISTS:
      Clubs with documented come-from-behind win rates above 25%:
        Apply: comeback_specialist_modifier = ×0.93 (less negative than ×0.85)
      Clubs with documented come-from-behind win rates below 15%:
        Apply: weak_comeback_modifier = ×0.78 (more negative than ×0.85)

CONCEDING MULTIPLE GOALS — PSYCHOLOGICAL COLLAPSE:

  Teams trailing by 2+ goals at half-time:
    Win probability modifier: ×0.60 (very low — across all clubs)
    Some clubs genuinely collapse at 2+ down; apply additional:
      collapse_tendency_modifier = ×0.90 for documented collapse clubs
      (these are clubs that historically ship additional goals when already behind)
```

---

## Post-trophy psychology

```
POST-TROPHY EFFECT:

  TROPHY WIN — IMMEDIATE AFTERMATH (first match within 7 days):
    Psychological hangover: celebration fatigue, mental let-down after peak effort.
    Apply: post_trophy_hangover_modifier = ×0.96 for first match within 7 days.
    
  If first match is more than 7 days after trophy win:
    Remove hangover modifier — adequate recovery time assumed.
    
  EXCEPTION:
    If the trophy match itself was dominant (large winning margin, low intensity):
      Hangover less pronounced; reduce to ×0.98.

POST-NEAR-MISS EFFECT (following season motivation):

  PAINFUL NEAR-MISS (final defeat, last-day title loss, playoff elimination):
    Creates documented motivation spike for the following season opening.
    Apply: near_miss_motivation_modifier = ×1.05 for opening 5-8 matches
    of the following season.
    
  QUALIFICATION:
    Applies only at the start of the following season — not ongoing.
    Must be a genuinely painful near-miss (not standard elimination).
    Examples: UCL Final defeat, title lost on last day, relegated via playoff.
    Remove after match 8 of following season regardless of results.
```

---

## Fan token psychological demand signals

```
PSYCHOLOGICAL MOMENTUM AND FAN TOKEN DEMAND:

  WIN STREAK DEMAND AMPLIFICATION:
    Community sentiment during win streaks amplifies demand beyond the
    standard match result signal.
    Win streak demand amplifier (applies on top of standard win demand signal):
      3-win streak: demand +3-5% sustained between matches
      5-win streak: demand +6-9% sustained
      7+ win streak: demand +10-12% sustained (ceiling)
      
  LOSS STREAK DEMAND ACCELERATION:
    Community psychological fragility during loss streaks accelerates
    demand decay beyond the standard loss signal.
    Loss streak demand discount (applied on top of standard loss decay):
      3-loss streak: accelerated decay ×1.30 on standard loss impact
      5-loss streak: accelerated decay ×1.50
      7+ loss streak: accelerated decay ×1.70 (severe fragility signal)
      
  TROPHY WIN EXTENDED DEMAND PREMIUM:
    Major trophy wins create a demand premium that extends beyond the
    standard post-win signal.
    Major trophy (domestic title, European trophy):
      Extended premium: +2-4 weeks of elevated demand above pre-win baseline
      Peak: +15-25% in first 48h
      Sustained: +8-12% for weeks 2-4
      New baseline: +5-10% permanently above pre-trophy baseline
      
  CHOKING PATTERN DEMAND IMPACT:
    When a confirmed choking pattern results in a high-profile failure:
      Demand drops compound: standard loss decay + psychological_disappointment_premium
      Apply: psychological_disappointment_multiplier = ×1.40 on standard loss decay
      Reason: fans expected better; disappointment is deeper than standard loss
```

---

## Compatibility

**Athlete modifiers:** `core/core-athlete-modifier-system.md`
**Coaching factors:** `core/coaching-intelligence.md`
**Momentum + rivalries:** `sports/football/sport-domain-football.md`
**MMA pressure:**      `sports/mma/sport-domain-mma.md`
**Fan token demand:**  `fan-token/fan-token-lifecycle/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Psychological intelligence: mental state, confidence signals, trauma and recovery patterns |
| Reasoning | ACTIVE | Psychological reasoning chain from observable signals to psychological modifier |
| Context | ACTIVE | Psychological context: competition history, personal circumstances, team environment |
| Memory | ACTIVE | Historical psychological pattern data for comparable athlete and team situations |
| Judgment | ACTIVE | Judgment on psychological signal materiality — most uncertain modifier category |
| Attention | ACTIVE | Elevated attention for psychological momentum shifts and crisis signals |
| Communication | ACTIVE | Psychological signal output with high uncertainty flag and confidence level |
| Verification | ACTIVE | Psychological signals are inherently soft — very high verification threshold applies |
| Learning | ACTIVE | Psychological pattern calibration from historical signal-to-outcome accuracy |
| Integration | ACTIVE | Integrates with motivation intelligence, perceptual pressure, and squad cohesion |
| Calibration | EMERGING | Psychological modifier calibration is the library's most uncertain signal category |
| Adaptation | ACTIVE | Psychological baselines adapt as athlete career stage and team environment change |
| Ethics | ACTIVE | Private psychological information is never used — only publicly observable signals |
| Transparency | ACTIVE | Psychological signals always flagged as SOFT_SIGNAL with maximum uncertainty disclosure |


---

*SportMind v3.97.35 · MIT License · sportmind.dev*
*Enduring reasoning framework — apply when live context arrives*
