---
name: napoli-nap
description: >
  Napoli ($NAP) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers high-pressing system identity, Maradona
  Stadium atmospheric modifier, post-championship demand baseline reasoning,
  and Serie A context application to $NAP demand signals.
---

# Napoli ($NAP) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $NAP.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`
Serie A context: `athlete/football/juventus-juv.md`

---

## System identity — high-pressing attack-minded

```
NAPOLI SYSTEM IDENTITY:
  Napoli's modern identity is built on high-pressing, attack-minded football
  with technically gifted forwards and energetic midfield. Unlike Juventus
  (defensive identity) or Inter (block-and-counter), Napoli's system
  prioritises attacking output and pressing intensity.
  
  POSITION WEIGHT BY IDENTITY:
    Primary striker / centre forward: highest individual modifier
    Wide attacking players: high modifier (pressing triggers and goal threat)
    Central midfield: important for pressing triggers and possession retention
    Defence: standard weight — system is attack-oriented
```

---

## Position reasoning frameworks

### Striker — system centrepiece

```
PRIMARY STRIKER:

  ROLE IN SYSTEM:
    Napoli's pressing system is triggered from the front — the striker leads
    the press and is also the primary goal threat. Napoli's attack begins with
    the striker. This dual role (press trigger + finisher) makes the position
    extremely high-value in their specific system.
    
  MODIFIER FRAMEWORK:
    AVAILABLE:
      goal_threat_modifier = ×1.12
      pressing_trigger_modifier = ×1.08 (front-foot press operational)
      combined system output: significantly elevated when striker available
      
    ABSENT:
      adjusted_score_shift = −6 to −8 points (striker + press trigger lost)
      pressing_intensity_modifier = ×0.88 (pressing system disrupted at source)
      This is a compound loss: not just a goal threat but a tactical disruption
      Apply: system_disruption_flag = true (not just individual_modifier)
```

### Wide attacking players

```
WIDE ATTACKING PLAYERS:

  ROLE IN SYSTEM:
    Napoli's wide players operate as both press triggers and directional
    goal threats. They provide width in attack and cover press responsibilities.
    
  MODIFIER FRAMEWORK:
    BOTH WIDE PLAYERS AVAILABLE:
      attacking_width_modifier = ×1.08
      press_coverage_modifier = ×1.05
      
    ONE WIDE PLAYER ABSENT:
      adjusted_score_shift = −3 to −4 points
      pressing_intensity_modifier = ×0.95 (one press trigger missing)
      
  WIDE PLAYER vs STRIKER PRIORITY:
    Striker absence: higher impact (−6-8pts) than wide player absence (−3-4pts)
    Napoli's system can adapt wide absences more easily than striker absence.
```

---

## Stadio Maradona atmospheric modifier

```
STADIO MARADONA — HOME ATMOSPHERE:

  LOCATION AND CONTEXT:
    Naples is one of Europe's most passionate football cities. The Maradona
    Stadium atmosphere for home matches — particularly high-stakes fixtures
    and European nights — is documented as exceptional.
    
  MODIFIER FRAMEWORK:
    Standard home advantage: +0.10 (football baseline)
    Maradona atmosphere modifier: ×1.08 (above average, below Türk Telekom level)
    European nights (UCL/UEL): ×1.10 (elevated occasion atmosphere)
    Derby vs Roma or against top-6 rivals: ×1.08 (rivalry amplification)
    
  SELL-OUT CONFIRMED:
    Apply: ×1.05 on top of base modifier
    Combined Maradona sell-out: ×1.13 (significant home advantage)
```

---

## Post-championship demand reasoning

```
POST-CHAMPIONSHIP BASELINE FRAMEWORK:

  CONTEXT:
    When a club wins a major championship (Scudetto, UCL), the demand
    baseline for the following season requires recalibration.
    
  POST-CHAMPIONSHIP YEAR 1 (season after winning):
    New baseline: 10-20% above the pre-championship baseline permanently
    Initial euphoria peak: decays over first 3-4 months of new season
    Championship defence signal: demand elevated if competing for title again
    
  POST-CHAMPIONSHIP YEAR 2+:
    If club does not repeat the championship: gradual baseline compression
    back toward peer-club level
    Sustained success: baseline remains elevated
    Relative decline: baseline compresses toward pre-championship level over 2-3 seasons
    
  FOR $NAP SPECIFICALLY:
    Apply post-championship premium framework when Napoli have recently won
    the Scudetto or made a deep UCL run.
    This is a structural demand modifier, not a transient spike.
    Confirm with: what has Napoli achieved in the trailing 2 seasons?
    Then apply appropriate baseline premium (10-20%) or compression (toward peer level).
```

---

## Serie A context

```
SERIE A TACTICAL CONTEXT FOR NAPOLI:
  Apply the same Serie A modifiers as documented in juventus-juv.md:
    Defensive modifiers: ×1.10 amplifier (lower-scoring context)
    Attacking modifiers: ×0.90 discount (relative to EPL)
    Set piece modifier: ×1.10 for confirmed specialists
    
  NAPOLI EXCEPTION — ATTACKING IDENTITY:
    For Napoli (attack-oriented), the attacking discount (×0.90) is partially
    offset by the pressing system premium.
    Net attacking modifier: ×0.95 (half the standard ×0.90 discount applies
    because Napoli generate more attacking output than average Serie A club)
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**Serie A context:**  `athlete/football/juventus-juv.md`
**Venue:**            `core/venue-intelligence.md`

---

*SportMind v3.97.29 · MIT License · sportmind.dev*
*Pressing system — striker absence is a compound loss (goal threat + press trigger)*
