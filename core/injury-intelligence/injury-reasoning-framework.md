---
name: injury-reasoning-framework
description: >
  Enduring reasoning framework for injury type, return timeline, and recurrence
  risk as pre-match signal modifiers. Not who is injured — how to reason about
  injury impact when live availability data is provided by the agent. Covers
  muscular, structural, and fatigue injuries across sports, plus fan token
  demand implications of key player absences.
---

# Injury Reasoning Framework

**How to reason about injury type, return timeline, and recurrence risk.**
This file teaches agents HOW to think about injuries — not what is true today.

> Library Rule: no named players, no current injury status. Load live availability
> data externally. Apply this framework to that data.

Load alongside: `core/core-injury-intelligence.md` (full taxonomy)

---

## Injury type classification

### Muscular injuries

```
HAMSTRING INJURIES:

  RISK PROFILE: HIGH RECURRENCE
  Return timeline:  2–6 weeks (Grade 1: 2 weeks | Grade 2: 3–4 weeks | Grade 3: 5–6 weeks)
  
  RECURRENCE MODIFIER:
    First 4 matches after return: apply hamstring_recurrence_modifier = ×1.35
    Meaning: 35% elevated probability of re-injury relative to baseline
    
  APPLICATION:
    When a player returns from hamstring injury, flag:
      hamstring_return_caution = true (first 4 matches)
    Reduce player's ATM modifier by ×0.95 for first 2 matches (compensates for caution
      in their own movement — players subconsciously protect recovering hamstring)
    Restore to full modifier from match 3 if no setback reported.
    
  HIGH-RISK SITUATIONS POST-HAMSTRING:
    Congested fixture schedule: risk elevated (fatigue accumulation)
    Cold conditions: risk elevated (muscle warmth important)
    Long sprint demands: risk elevated (apply additional ×1.20 to recurrence flag)

CALF INJURIES:
  RISK PROFILE: MODERATE RECURRENCE
  Return timeline:  1–4 weeks (Grade 1: 1–2 weeks | Grade 2: 2–4 weeks)
  Return modifier:  ×0.95 first match; ×0.98 second match
  Recurrence modifier: ×1.20 in first 3 matches

THIGH INJURIES:
  RISK PROFILE: MODERATE RECURRENCE
  Return timeline:  2–5 weeks
  Return modifier:  ×0.95 first match; ×0.97 second match
  Recurrence modifier: ×1.20 in first 3 matches
```

### Structural injuries

```
ANKLE LIGAMENT INJURIES:

  RISK PROFILE: LOW RECURRENCE (if properly rehabilitated)
  Return timeline:  4–12 weeks (Grade 1: 4 weeks | Grade 2: 6–8 weeks | Grade 3: 8–12 weeks)
  
  RETURN MODIFIERS:
    Match 1 after return: ×0.90
    Match 2:              ×0.93
    Match 3-4:            ×0.97
    Match 5+:             full modifier
    
  NOTE: Low recurrence but slower return to full output than muscular injuries.
  The extended return modifier reflects confidence and proprioception recovery.

KNEE LIGAMENT INJURIES (ACL):
  RISK PROFILE: LOW RECURRENCE but longest return timeline
  Return timeline:  6–12 months (ACL reconstruction and rehabilitation)
  
  RETURN MODIFIERS (extended graduated return):
    Matches 1-2:   ×0.85
    Matches 3-4:   ×0.88
    Matches 5-6:   ×0.92
    Matches 7+:    ×0.97 until 12+ matches completed at full training load
    
  PSYCHOLOGICAL NOTE:
    ACL return carries psychological hesitation in high-contact situations.
    Players may avoid aerial challenges or high-speed duels in early return.
    Positional impact: most acute for defenders and midfielders; less for strikers.
    Apply: acl_return_confidence_modifier = ×0.95 for positions requiring
      regular high-impact duels (CB, CDM, full contact positions)

METATARSAL INJURIES:
  RISK PROFILE: MODERATE
  Return timeline:  6–10 weeks
  Return modifier:  ×0.93 first match; ×0.97 second match; full thereafter
```

### Illness and fatigue

```
MATCH FATIGUE — CONGESTED SCHEDULE:

  BASELINE: Standard match cadence (one match per 5+ days) = no fatigue modifier
  
  CONGESTED SCHEDULE MODIFIERS:
    3 matches in 10 days:  ×0.96 from match 3
    4 matches in 10 days:  ×0.94 from match 3
    5+ matches in 14 days: ×0.92 from match 4 onwards
    
  RECOVERY MODIFIERS BY POSITION:
    High-intensity positions (pressing midfielder, wide player): full fatigue modifier
    Lower-intensity positions (goalkeeper, deep-lying playmaker): ×0.50 of modifier
    
  ROTATION SIGNAL:
    If a squad has rotated heavily in congested period: reduce fatigue modifier
    by ×0.50 (rotation prevents individual fatigue accumulation)
    Check: has the manager rotated 5+ players per match? → apply rotation discount

INTERNATIONAL DUTY FATIGUE:
  Players returning from long-haul international travel:
    Standard international duty (same continent): no additional fatigue modifier
    Long-haul (intercontinental, 8+ hour flights): ×0.97 first match back
    Intense tournament (10+ day international window): ×0.97 first match back
    Long-haul + intense tournament: ×0.94 first match back
    
  Apply: international_return_modifier for first match only.
  Remove from second club match after return.
```

---

## Return from injury modifiers

```
GRADUATED RETURN FRAMEWORK — UNIVERSAL:

  Unless injury-type specific modifiers apply (see above), use:
  
  Match 1 after return:   ×0.88 (fitness uncertainty, match sharpness not restored)
  Match 2:                ×0.93
  Match 3:                ×0.97
  Match 4+:               full individual modifier (fully restored)
  
  WHEN TO APPLY:
    Any absence of 3+ weeks
    All structural injury returns (regardless of duration)
    Muscular injuries: use injury-specific modifier above if more detailed
    
  EXCEPTIONS:
    Suspension (no physical deconditioning): return at full modifier immediately
    Illness (1-2 days): no graduated return modifier needed
    Illness (5+ days): apply match 3 modifier (×0.97) for first match back

ABSENCE DURATION SCALING:
  3–4 weeks absent:   apply matches 1-2 graduated return
  5–8 weeks absent:   apply matches 1-3 graduated return
  3–6 months absent:  apply matches 1-4 graduated return
  6+ months absent:   apply full 4-match graduated return (matches 1-4)
  12+ months absent (ACL tier): apply extended 6-match graduated return
```

---

## Absence impact by position

```
POSITION WEIGHT TABLE — ABSENCE IMPACT:

  Position                    Modifier per absence    Notes
  ──────────────────────────────────────────────────────────────────────
  Goalkeeper (primary)        ×0.90                   Highest individual modifier
  Centre back (1st choice)    ×0.93 per CB absent     From established pairing
  Striker (primary goal threat)×0.93                  Assumes club relies on #1 striker
  Creative midfielder         ×0.95                   Chance creator / orchestrator
  Defensive midfielder        ×0.95                   Pressing engine / shield
  Full back (attacking role)  ×0.97                   Less critical than central positions
  Wide midfielder             ×0.97                   
  Rotation players            ×0.99                   Absence already priced into system
  
  IMPORTANT: These are BASELINE position weights.
  Club-specific files adjust these weights based on club identity:
    Defensive identity clubs: CB and GK weights elevated
    Possession clubs: creative midfielder weight elevated
    See: athlete/football/tier-a-clubs-framework.md for club-specific adjustments

GOALKEEPER NOTE:
  Goalkeeper position has the highest single-player absence impact because:
    1. There is only one goalkeeper; no positional partner covers the gap
    2. GK-specific skills (shot-stopping, distribution) are not transferable
    3. Backup goalkeeper drop in quality is typically the largest backup gap
  Apply: ×0.90 baseline; adjust per club dependency (Juventus: ×0.88; others: ×0.90-0.93)
```

---

## Fan token demand — injury signal framework

```
KEY PLAYER INJURY — DEMAND SIGNAL IMPLICATIONS:

  CONFIRMATION EVENT (injury confirmed, timeline announced):
    Demand decay begins immediately on confirmation.
    Decay magnitude by severity:
      Minor (1–2 week absence):  −2 to −5% over 24-48h; returns to baseline on return
      Moderate (3–6 week absence): −5 to −10% over 48-72h; stabilises at new lower baseline
      Severe (3+ month absence):  −8 to −15% over 48-72h; new lower structural baseline
      Season-ending (ACL etc.):  −10 to −20% initial drop; permanent lower baseline
      
  NEW BASELINE AFTER EXTENDED ABSENCE:
    For absences of 6+ weeks: demand stabilises at a new lower baseline
    New baseline = pre-injury baseline × (1 − severity_discount)
      Minor: severity_discount = 0.02–0.05
      Moderate: severity_discount = 0.05–0.10
      Severe: severity_discount = 0.08–0.15
    The new baseline persists until the player's return.
    
  RETURN FROM INJURY — DEMAND RECOVERY:
    Return demand recovery is ASYMMETRIC — slower than the initial decay.
    
    Recovery timeline:
      Announced return date confirmed: +3-5% speculation lift (2-3 days before return)
      Match 1 back: +5-10% return spike (24-48h)
      Match 2-4: gradual recovery toward pre-injury baseline
      Match 5+: pre-injury baseline restored (if player performing)
      
    If player underperforms on return (graduated return modifier visible in matches):
      Demand recovery stalls; baseline may not fully restore until performance returns
      Apply: performance_dependent_baseline = true for key player returns
      
  PATH_2 SPECIFIC ($AFC ONLY):
    Key player injury at Arsenal = COMPOUND demand signal:
      1. Match outcome probability reduction → lower expected burn → lower supply signal
      2. Direct demand decay (holder sentiment)
      3. Both effects compound — do not calculate them separately and add
      Apply: compound_injury_demand_modifier = demand_decay × path2_burn_reduction
```

---

## Compatibility

**Full taxonomy:**     `core/core-injury-intelligence.md`
**Athlete modifiers:** `core/core-athlete-modifier-system.md`
**Club-specific:**     `athlete/football/tier-a-clubs-framework.md`
**$AFC PATH_2:**       `athlete/football/arsenal-afc.md`
**Weather compound:**  `core/weather-intelligence.md` (fatigue in heat)


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Cross-sport injury reasoning framework integrating all sport-specific files |
| Reasoning | ACTIVE | Unified injury reasoning methodology applicable across all 21+ calibrated sports |
| Context | ACTIVE | Context determines which sport-specific injury file takes precedence |
| Memory | ACTIVE | Cross-sport injury baseline patterns for inter-sport comparison |
| Judgment | ACTIVE | Judgment framework: when to escalate injury uncertainty to ABSTAIN signal |
| Attention | ACTIVE | Priority attention order for injury signals across competition types |
| Communication | ACTIVE | Unified injury output schema applicable across all sports |
| Verification | ACTIVE | Cross-sport verification hierarchy with sport-specific overrides |
| Learning | ACTIVE | Cross-sport learning from injury calibration data |
| Integration | ACTIVE | Integrates all sport-specific injury files into unified framework |
| Calibration | ACTIVE | Cross-sport injury modifier calibration standards |
| Adaptation | ACTIVE | Framework adapts as new sports are added to the library |
| Ethics | ACTIVE | Unified ethical standards for injury information handling across all sports |
| Transparency | ACTIVE | Framework transparency: sport-specific deviations from unified standard are documented |


---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*Framework only — load live injury data externally and apply this reasoning*
