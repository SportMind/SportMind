---
name: inter-milan-inter
description: >
  Inter Milan ($INTER) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers defensive block identity, attacking wing
  depth, Milan Derby reasoning, Serie A tactical context, and $INTER demand
  signal interaction with European campaign progress.
---

# Inter Milan ($INTER) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $INTER.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`
Serie A context: `athlete/football/juventus-juv.md`

---

## System identity — defensive block with transitional threat

```
INTER MILAN SYSTEM IDENTITY:
  Inter operate a cohesive defensive block — disciplined shape, strong
  aerial presence, and counter-attacking efficiency. Their identity is
  closer to Juventus (defensive solidity) than to Barcelona (possession)
  or AC Milan (trequartista creativity).
  
  POSITION WEIGHT BY IDENTITY:
    Defensive positions (goalkeeper, CBs): elevated modifier weight
    Defensive midfielder: critical to pressing trap and block cohesion
    Striker: primary goal threat for counter-attack system
    Wingers (wing-backs in 3-5-2): high system dependency — they ARE
      the width in Inter's three-at-the-back system
```

---

## Position reasoning frameworks

### Wing-backs — system-critical width

```
WING-BACKS / ATTACKING WIDTH:

  ROLE IN SYSTEM:
    In Inter's typical 3-5-2 / 3-4-3 system, wing-backs provide ALL
    attacking width. They are not supplementary — they are the only wide
    outlet. Absence at wing-back has a larger system impact than at most clubs.
    
  MODIFIER FRAMEWORK:
    BOTH WING-BACKS AVAILABLE:
      system_width_modifier = ×1.10 (full system operational)
      
    ONE WING-BACK ABSENT:
      adjusted_score_shift = −4 to −6 points
      attacking_width_modifier = ×0.88
      Note: larger modifier than typical full back absence at other clubs
      because wing-backs carry the ONLY wide threat — no inside forward covers
      
    BOTH WING-BACKS ABSENT:
      System integrity severely compromised; apply HOLD consideration
```

### Central defensive block

```
CENTRAL DEFENSIVE BLOCK:

  ROLE IN SYSTEM:
    Three-centre-back system with deep defensive shape. CB quality directly
    determines clean sheet probability and set piece defensive solidity.
    
  MODIFIER FRAMEWORK:
    ALL THREE CBS AVAILABLE:
      defensive_block_modifier = ×1.10 (three-CB system at full strength)
      aerial_dominance_modifier = ×1.08 (set piece defensive aerial threat)
      
    ONE CB ABSENT:
      adjusted_score_shift = −3 to −5 points
      defensive_block_modifier = ×0.95
      
    TWO CBS ABSENT:
      adjusted_score_shift = −6 to −8 points; apply HOLD consideration
      
  SERIE A AMPLIFIER:
    Apply Serie A defensive amplifier ×1.10 to all defensive modifiers
    (same as Juventus context — lower-scoring league; defensive absences more costly)
```

### Striker — counter-attack focal point

```
STRIKER / GOAL THREAT:

  ROLE IN SYSTEM:
    Inter's striker is the endpoint of the counter-attack. The system
    is built to release the striker into space behind defensive lines.
    A physically imposing striker who holds up play and finishes is
    the system's primary output mechanism.
    
  MODIFIER FRAMEWORK:
    PRIMARY STRIKER AVAILABLE:
      goal_threat_modifier = ×1.10 (system designed around striker release)
      counter_attack_efficiency = ×1.08
      
    PRIMARY STRIKER ABSENT:
      adjusted_score_shift = −5 to −7 points
      counter_attack_efficiency = ×0.85 (system loses its primary outlet)
      Note: striker absence hits Inter harder than most clubs because the
        counter-attack structure requires a reliable finish point
```

---

## Milan Derby reasoning ($INTER specific)

```
DERBY DELLA MADONNINA — $INTER CONTEXT:
  See acmilan-acm.md for the full Derby framework.
  For $INTER, the same ×1.15 match importance amplifier applies.
  
  $INTER SPECIFIC DEMAND SIGNAL:
    Derby result carries elevated demand weight: ×1.20 demand amplifier
    Derby win vs AC Milan: highest single demand event in $INTER's calendar
    Derby loss: sustained negative demand period (similar to $ACM framework)
    
  INTER vs JUVENTUS (Derby d'Italia):
    Also elevated demand weight — historic rivalry signal.
    Apply: ×1.12 match importance modifier (slightly below Milano Derby)
    Demand amplifier: ×1.15
```

---

## European campaign and $INTER demand

```
$INTER UCL DEMAND SIGNAL:
  Inter Milan have a strong European pedigree — UCL progress drives demand.
  
  UCL DEMAND PREMIUM:
    Knockout stage progression: ×1.10 per round advanced
    UCL semi-final appearance: demand premium ×1.25
    UCL Final appearance: demand premium ×1.40
    
  DEMAND SENSITIVITY:
    $INTER demand is more European-sensitive than purely domestic-sensitive.
    Serie A is important but UCL progress drives the larger demand spikes.
    Apply: european_weight = 0.60 | domestic_weight = 0.40 for $INTER demand
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**Serie A context:**  `athlete/football/juventus-juv.md`
**Milan Derby:**      `athlete/football/acmilan-acm.md`

---

*SportMind v3.97.29 · MIT License · sportmind.dev*
*Three-CB system — wing-back absence carries higher modifier than standard fullback*
