---
name: coaching-intelligence
description: >
  Enduring reasoning framework for coaching and management as a signal modifier.
  Covers new manager effect, managerial stability, tactical system interaction
  with player absences, coaching staff intelligence, combat sports corner team
  reasoning, and fan token coaching demand signals.
---

# Coaching and Management Intelligence

**How to reason about coaching and management as pre-match and in-season signal modifiers.**
Permanently enduring reasoning frameworks.

> Library Rule: no named managers, no current appointment status, no specific
> tactical details tied to a named individual. Framework teaches how to reason
> when live context arrives.

---

## New manager effect

```
NEW MANAGER APPOINTMENT — PERFORMANCE UPLIFT FRAMEWORK:

  DOCUMENTED PATTERN:
    New manager appointments reliably produce short-term performance improvements
    across professional football, rugby, basketball, and most team sports.
    The pattern is well-documented and repeatable — it belongs in the library.
    
  MECHANISM:
    1. Squad motivation reset — players compete for positions under new assessment
    2. Opponent unfamiliarity — new tactical approach not yet well-scouted
    3. Media narrative boost — "new era" storyline generates positive attention
    4. Temporary suspension of internal negativity from previous regime
    
  NEW MANAGER PERFORMANCE MODIFIER TABLE:
    Matches 1-5:    ×1.06 — strong uplift; full novelty and motivation effect
    Matches 6-15:   ×1.02 — moderate sustained uplift; familiarity sets in
    Match 16+:      ×1.00 — return to structural baseline (system normalises)
    
  HOW TO APPLY:
    Count from the new manager's first official competitive match.
    Apply the appropriate modifier to the match outcome signal.
    Remove at match 16 — do not carry new manager effect indefinitely.
    
  CARETAKER MANAGER EXCEPTION:
    Caretaker managers produce a shorter, less pronounced uplift.
    Apply: ×1.02 only (not ×1.06) for all caretaker matches.
    Mechanism: squad knows the situation is temporary; lower commitment to rebuild.
    Remove: when a permanent appointment is confirmed.
    
  INTERIM-TO-PERMANENT TRANSITION:
    If a caretaker is made permanent, apply the full new manager framework
    from the date of permanent appointment — restart the count at match 1.
    The initial caretaker matches count separately and do not consume the
    permanent appointment modifier window.
```

---

## Managerial stability modifier

```
LONG-TENURE STABILITY PREMIUM:

  The longer a manager has been embedded in a system, the more the system
  itself becomes a structural performance asset — independent of the
  manager's individual tactical decisions in any given match.
  
  STABILITY MODIFIER TABLE:
    Manager in post 2+ seasons:  ×1.03 — system familiarity premium
    Manager in post 4+ seasons:  ×1.05 — deep system embedding premium
    
  WHAT THIS COVERS:
    Squad comfort with defensive shape, pressing triggers, set piece routines,
    transition patterns. Players execute without conscious effort — this reduces
    variance and improves baseline performance.
    
  HOW TO CONFIRM TENURE:
    Count from the manager's first competitive match at this club.
    Interruptions (leaves and returns) reset the clock.
    
  INSTABILITY DISCOUNT:
    High managerial turnover club (3+ managers in 2 seasons):
    Apply: instability_discount = ×0.94 to match outcome signal.
    Mechanism: tactical identity confusion, squad trust erosion, recruitment
      misalignment (players signed for a system that no longer exists).
    Remove: when the same manager has been in post for a full season.
    
  AGENT RULE:
    Confirm manager tenure at start of each season. It changes once per window
    at most. A simple check at the season start is sufficient.
```

---

## Tactical system and player absence interaction

```
HOW MANAGER TACTICAL IDENTITY CHANGES ABSENCE MODIFIER WEIGHTS:

  The same position absence carries different modifier weight depending on
  what the manager's system demands. A defensive midfielder departure means
  more to a high-pressing manager than to a counter-attacking manager.
  
  POSSESSION-BASED SYSTEM (tiki-taka, positional play variants):
    Midfield absences carry elevated weight: ×1.15 multiplier on standard modifier
    Reason: the midfield triangle is the system's centre of gravity
    
  COUNTER-ATTACKING SYSTEM:
    Striker and wide player absences carry elevated weight: ×1.15
    Reason: speed transitions need reliable endpoints and wide runners
    Defensive absences are relatively less costly (deep block system tolerates backup CBs)
    
  HIGH-PRESS SYSTEM:
    Physical fitness and press-trigger availability carry elevated weight
    Fatigue signals are more significant than at other systems
    Apply: press_fitness_modifier — when key press triggers are fatigued or absent,
      the whole pressing system degrades (not just individual positions)
      Pressing system degradation: ×0.92 when primary press triggers absent
      
  REACTIVE / DEFENSIVE SYSTEM:
    Organisation and defensive cohesion signals elevated
    GK and CB absences carry highest weight (×1.15 on standard modifier)
    
  AGENT RULE:
    Before applying player absence modifiers:
      1. Identify the manager's tactical system identity
      2. Identify which position group carries highest modifier weight for that system
      3. Apply the ×1.15 multiplier to that group's individual modifiers
      4. Do not apply ×1.15 to all positions — only the system-critical group
```

---

## Coaching staff intelligence

```
ASSISTANT MANAGER CONTINUITY:

  WHEN A MANAGER LEAVES BUT THE ASSISTANT STAYS:
    System disruption is materially reduced when the assistant remains.
    The tactical identity is partially preserved through the assistant's
    presence and influence on the new appointment.
    
    MODIFIER:
      Apply: ×0.97 rather than full new manager ×1.06 for match 1-5
      (system disruption is lower; novelty effect is also lower)
      If assistant becomes caretaker: standard caretaker modifier ×1.02
      If assistant supports new incoming manager: new manager gets ×1.04
        (slightly reduced — tactical environment already partially defined)
        
GOALKEEPER COACH QUALITY:

  DOCUMENTED PATTERN:
    Clubs with specialist, experienced GK coaches show measurably more
    consistent GK performance than clubs relying on general coaching staff
    for GK development.
    
  MODIFIER:
    Confirmed specialist GK coach presence: ×1.02 on GK modifier
    Apply to: all GK-related modifier calculations for this club
    This is a season-level modifier — confirm at start of each season
    
  HOW TO ASSESS:
    Is there a dedicated GK coach on the coaching staff?
    Is the GK coach recognised within the sport as a specialist?
    
  NOTE:
    This is a marginal modifier — it applies to edge cases when GK
    quality is the decisive factor in a pre-match signal. It should
    not be applied as a routine adjustment on every match.
```

---

## Combat sports coaching

```
CORNER TEAM QUALITY — PRE-FIGHT MODIFIER:

  WHY CORNER TEAM MATTERS IN COMBAT SPORTS:
    In MMA and boxing, the corner team provides real-time strategic guidance,
    physical recovery between rounds, and psychological support under pressure.
    Corner team quality is measurable and enduring.
    
FIGHT CAMP STABILITY MODIFIER:

  SAME CORNER TEAM FOR 3+ CONSECUTIVE FIGHTS:
    Apply: fight_camp_stability_modifier = ×1.04
    Mechanism: developed communication patterns, established trust,
      tailored preparation built over multiple camps
    
  FIGHT CAMP CHANGE — UNCERTAINTY SIGNAL:
    Switching fight camps before a major fight:
    Apply: camp_change_uncertainty_modifier = ×0.94 for the first fight
      after the camp change
    Mechanism: new communication patterns, unfamiliar preparation methods,
      potential strategic identity confusion
    Remove: after the first fight in the new camp (one-match penalty only)
    
  HOW TO IDENTIFY A CAMP CHANGE:
    Fighter is not training at their historical location
    New coaches listed in pre-fight media
    Fighter explicitly discusses changing camp in pre-fight interviews
    
CORNER TEAM TACTICAL QUALITY:

  ELITE CORNER TEAM SIGNAL (recognised strategists at the elite level):
    Apply: elite_corner_modifier = ×1.03
    Applies to: fights where corner team has documented impact on tactical
      adjustments between rounds (opponent gameplan exploitation)
    Identify via: historical fights where corner adjustments were credited
      with changing fight outcomes (minimum 3 documented examples)
```

---

## Fan token coaching demand signals

```
MANAGER APPOINTMENT — DEMAND SIGNAL:

  HIGH-PROFILE NEW APPOINTMENT:
    Definition: manager with documented success at a comparable or higher level club
    Demand spike: +10-20% over 1-2 weeks from announcement
    Peak: appointment confirmation day (+1)
    Decay: normalises to new baseline by week 3
    New baseline: +3-5% above pre-appointment baseline (sustained positive signal)
    
  UNKNOWN / UNPROVEN APPOINTMENT:
    Definition: manager without major prior success at elite level
    Demand signal: neutral to mildly negative
    Apply: ×0.99 (marginal uncertainty signal, 1-2 week duration)
    
MANAGER DEPARTURE — DEMAND SIGNAL:

  FORCED DEPARTURE (sacking, mutual termination after poor results):
    Demand decay: -8-15% over 2-3 weeks from announcement
    Mechanism: uncertainty + negative form association
    
  RESIGNATION / MUTUAL AGREEMENT (not performance-driven):
    Demand decay: -4-8% over 1-2 weeks (smaller; less negative narrative)
    
  DEPARTURE + IMMEDIATE REPLACEMENT ANNOUNCED:
    Net demand signal may be positive if replacement is high-profile.
    Apply: new_appointment_premium – departure_decay (net calculation)
    
MANAGER CONTRACT EXTENSION:

  Confirmed contract extension signals stability and shared vision.
  Apply: contract_extension_stability_modifier = ×1.02 sustained
  Duration: remainder of the season (signals long-term commitment)
  Applies to: demand baseline calculations for the token
```

---

## Compatibility

**Psychological factors:**  `core/psychological-intelligence.md`
**Athlete modifiers:**      `core/core-athlete-modifier-system.md`
**Tier A club systems:**    `athlete/football/tier-a-clubs-framework.md`
**MMA corner:**             `sports/mma/sport-domain-mma.md`
**Tactical continuity:**    `athlete/football/mancity-city.md` (long-tenure system model)

---

*SportMind v3.97.35 · MIT License · sportmind.dev*
*Enduring framework — no named managers; applies when live context arrives*
