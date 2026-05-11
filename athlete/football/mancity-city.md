---
name: mancity-city
description: >
  Manchester City ($CITY) athlete intelligence reasoning framework.
  Demand-only context — no confirmed FTP PATH_2. Covers elite striker
  system dependency, false nine fallback reasoning, positional system
  modifier logic, Guardiola-model tactical continuity, and squad depth
  premium calculation for EPL's deepest squad.
---

# Manchester City ($CITY) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $CITY.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## Position reasoning frameworks

### Striker — elite goal threat in optimised system

```
STRIKER / ELITE GOAL THREAT:

  ROLE IN SYSTEM:
    Manchester City's system is designed to maximise a single elite striker's
    output. The striker is not just a target — they are the final product of an
    elaborate positional build-up system. Every City midfielder, fullback, and
    winger creates space and angles that funnel opportunities to the striker.
    
  MODIFIER FRAMEWORK:
    ELITE STRIKER AVAILABLE:
      goal_threat_modifier = ×1.15 (higher than most clubs)
      system_output_modifier = ×1.12 (entire system calibrated around striker)
      
    STRIKER ABSENT — FALSE NINE FALLBACK:
      adjusted_score_shift = −4 to −6 points (LOWER than most clubs with striker absent)
      Note: City's squad depth and tactical flexibility reduce the impact
      system_reconfiguration_modifier = ×0.93 (false nine fallback modifier)
      See false nine section below
      
  COMPARISON TO AVERAGE ELITE CLUB:
    Average Tier A club striker absence: −5 to −8 points
    Manchester City striker absence: −4 to −6 points
    The smaller impact reflects City's squad depth and tactical adaptability.
    
  ELITE STRIKER SYSTEM MULTIPLIER:
    When elite striker is available AND City are at home:
      compound_modifier = ×1.15 (striker) × ×1.05 (Etihad home) = ×1.2075
      This is one of the highest compound modifiers in the library.
```

### False nine fallback reasoning

```
FALSE NINE FALLBACK — STRIKER ABSENT:

  WHEN ELITE STRIKER IS ABSENT:
    City have the squad depth and tactical intelligence to deploy a false nine.
    Unlike most clubs, City's midfielders and wingers can perform false nine
    duties reasonably effectively within the established system.
    
  FALSE NINE FALLBACK MODIFIER:
    system_reconfiguration_modifier = ×0.93
    (compared to standard absence modifier of ×0.88 at most clubs)
    
  WHY ×0.93 NOT ×0.88:
    City's deeply embedded system means even without the striker, their
    positional framework continues to create chances.
    The false nine generates fewer direct goal threats but maintains:
      → Positional overloads in midfield
      → Wide threat through wingers and fullbacks
      → Set piece threat through specialist deliverers
    Net: 7% reduction in output, not 12%
    
  LIMITS OF FALSE NINE REASONING:
    Against very deep defensive blocks: false nine is less effective
    Apply: deep_block_vulnerability_modifier = ×0.95 when opponent parks defensively
    City needs the elite striker to unlock deep blocks more than the system average.
    
  PLAYER-SPECIFIC NOTE:
    False nine reasoning applies only when the chosen false nine has >10 City
    appearances in a central role. New to system: apply additional ×0.97.
```

### Positional system dependency

```
POSITIONAL SYSTEM DEPENDENCY:

  HOW CITY'S SYSTEM DIFFERS:
    Manchester City under a sustained tactical manager (see below) operate with
    high positional discipline. Every player has defined zones and responsibilities.
    Absences do not just remove a player — they remove a system role.
    
  SYSTEM ROLE DISRUPTION (distinct from standard player absence):
    When a player who is deeply embedded in a specific system role is absent:
      Step 1: Apply standard individual position modifier
      Step 2: Apply system_role_disruption_modifier = ×0.97 if no direct system-fit
        replacement exists
      Step 3: If replacement has been trained in the same role: remove step 2 modifier
      
  POSITIONAL GROUPS AND THEIR SYSTEM WEIGHT:
    Central midfield controller (ball retention, PPDA management):
      system_role_weight = HIGH; system_disruption = ×0.95 if absent
    Inverted winger (cutting inside for shots/assists):
      system_role_weight = MEDIUM-HIGH; standard individual modifier applies
    Overlapping full back (progressive width):
      system_role_weight = MEDIUM; ×0.97 disruption modifier if absent
      
  AGENT RULE:
    For City, always assess: "Does a direct system-role replacement exist?"
    If YES: apply standard individual modifier only
    If NO: apply standard individual modifier × system_role_disruption_modifier
```

---

## Guardiola-model tactical continuity

```
TACTICAL SYSTEM CONTINUITY — SUSTAINED MANAGER FRAMEWORK:

  PRINCIPLE:
    When a highly tactical manager has been in place for multiple seasons
    (typically 3+ seasons), the system itself becomes an additional modifier.
    Players become more interchangeable within the system than at clubs with
    tactical discontinuity.
    
  CITY-SPECIFIC APPLICATION:
    Under a long-tenure tactical manager:
      individual_interchangeability_premium = ×0.15 reduction in individual modifiers
      (15% reduction because the system absorbs individual absences more smoothly)
      
  HOW THIS WORKS IN PRACTICE:
    Typical Tier A club: striker absent = −6 points
    City under long-tenure manager: striker absent = −4.8 points (×0.80 of impact)
    The system provides structural compensation.
    
  SYSTEM CONTINUITY CONDITION:
    Apply the continuity modifier ONLY if:
      → Same manager for 3+ consecutive seasons
      → No major system change signalled (tactical identity stable)
      → Core system players (e.g. central midfield controller) are available
        (if the system's core is absent, continuity modifier reduces to ×0.05 reduction)
        
  MANAGER DEPARTURE NOTE:
    If long-tenure manager departs: remove continuity modifier immediately.
    Apply: system_reset_modifier = ×0.90 for first 15 matches under new manager.
    The embedded system takes time to establish under new tactical direction.
```

---

## Squad depth premium

```
SQUAD DEPTH PREMIUM — DEEPEST EPL SQUAD:

  CITY'S STRUCTURAL DEPTH ADVANTAGE:
    Manchester City consistently carry the deepest quality squad in English football.
    This structural advantage reduces the impact of individual absences across
    almost all positions.
    
  DEPTH PREMIUM APPLICATION:
    Apply squad_depth_modifier = ×0.85 to all individual absence modifiers.
    (15% reduction in modifier impact across all non-elite positions)
    
  EXCEPTION — ELITE STRIKER POSITION:
    The squad depth discount does NOT apply to the elite striker position.
    No squad-depth club reliably replaces a generational striker.
    Apply: full individual modifier for striker despite depth premium.
    
  SEASONAL RECALIBRATION:
    Squad depth must be confirmed at start of each season.
    Depth events that reduce the premium:
      Major injuries to multiple first-team players simultaneously
      Net loss in transfer window (key players departed, not replaced)
    When depth is temporarily reduced: apply ×0.93 (reduced discount) instead of ×0.85.
    
  COMPARISON TO OTHER TIER A CLUBS:
    Average EPL club: no depth discount — standard individual modifiers
    Barcelona: La Masia discount ×0.85 (academy-based)
    Manchester City: squad depth discount ×0.85 (financial/recruitment-based)
    Same numeric discount, different structural reason.
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**$CITY token:**      `fan-token/league-football-token-intelligence.md`
**EPL context:**      `sports/football/sport-domain-football.md`

---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*Deepest EPL squad — apply ×0.85 depth discount on all individual modifiers except elite striker*
