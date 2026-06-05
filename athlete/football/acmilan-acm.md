---
name: acmilan-acm
description: >
  AC Milan ($ACM) athlete intelligence reasoning framework. Demand-only context —
  no confirmed FTP PATH_2. Covers trequartista / number ten dependency, striker
  partnership reasoning, San Siro home advantage compounding, and Milan Derby
  modifier interaction with athlete availability.
---

# AC Milan ($ACM) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $ACM.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## Position reasoning frameworks

### Attacking midfielder / trequartista

```
ATTACKING MIDFIELDER / TREQUARTISTA (NUMBER TEN):

  ROLE IN SYSTEM:
    AC Milan's attacking system centres on the number ten role more than
    most modern clubs. The trequartista is the creative hub between midfield
    and attack — providing through balls, set piece threat, and the link
    that connects the striker to the wider attack.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (first-choice number ten):
      attacking_output_modifier = ×1.12
      creative_hub_modifier = ×1.10
      chance_creation_modifier = ×1.15 (number ten is Milan's primary creator)
      
    ABSENT:
      adjusted_score_shift = −5 to −7 points
      attacking_output_modifier = ×0.85
      Milan's attacking system loses its primary creative axis — not just a
        talent absence but a system disruption
      Apply: system_disruption_flag = true (not just individual_modifier)
      
  COMPARISON TO OTHER POSITIONS AT MILAN:
    Number ten absence: −5 to −7 points (system disruption)
    Striker absence: −3 to −5 points (individual loss)
    CB absence: −3 to −4 points (defensive weakening)
    The trequartista carries the highest individual modifier weight at AC Milan.
```

### Striker partnership

```
STRIKER PARTNERSHIP / GOAL THREAT:

  ROLE IN SYSTEM:
    Milan typically operate with a primary striker, with the number ten
    providing support and creation. The striker is the direct goal threat
    endpoint of the creative chain from the trequartista.
    
  MODIFIER FRAMEWORK:
    PRIMARY STRIKER AVAILABLE:
      goal_threat_modifier = ×1.08
      
    PRIMARY STRIKER ABSENT:
      adjusted_score_shift = −3 to −5 points
      goal_threat_modifier = ×0.88
      Note: impact is moderated if the number ten is available — the creative
        chain can adapt to a different central target
        
    BOTH TREQUARTISTA AND STRIKER ABSENT:
      adjusted_score_shift = −8 to −12 points
      Apply: HOLD_RECOMMENDED (Milan's entire attacking system disrupted)
      
  PARTNERSHIP DYNAMICS:
    When striker and trequartista are both available and have established
    chemistry (10+ shared appearances): apply partnership_bonus = ×1.05
    This compound effect is unique to clubs with a clear two-player creative axis.
```

---

## San Siro home advantage compound modifier

```
SAN SIRO ATMOSPHERE — COMPOUND HOME ADVANTAGE:

  WHY SAN SIRO IS DIFFERENT:
    San Siro (Giuseppe Meazza) is one of the highest-capacity and highest-
    atmosphere stadiums in Serie A. The home advantage at San Siro is
    structurally above the Serie A average.
    
  STANDARD HOME ADVANTAGE (Serie A average):
    home_advantage_modifier = ×1.05 (standard across most grounds)
    
  SAN SIRO COMPOUND MODIFIER:
    san_siro_base_modifier = ×1.08 (above Serie A average)
    
  COMPOUND CONDITION — FULL SQUAD AT SAN SIRO:
    When AC Milan's key players (especially trequartista and striker) are
    BOTH available at San Siro, the home atmosphere amplifies their output.
    Apply: compound_san_siro_modifier = ×1.12 (×1.08 base × ×1.04 full-squad amplifier)
    
  PARTIAL SQUAD (key absence) AT SAN SIRO:
    Remove full-squad amplifier; retain base modifier only: ×1.08
    
  AWAY MATCHES:
    San Siro modifier does not apply. Use standard Serie A away modifier.
    
  EUROPEAN CONTEXT:
    UCL home matches at San Siro: apply ×1.10 (European night atmosphere amplifier
    replaces Serie A amplifier — different but comparable crowd intensity)
```

---

## Milan Derby reasoning

```
MILAN DERBY — ATHLETE AVAILABILITY INTERACTION:

  THE DERBY DELLA MADONNINA (Milan vs Inter):
    The Milan Derby is the highest-stakes regular fixture in Milan's calendar.
    Athlete availability interacts with derby match importance modifier.
    
  DERBY MATCH IMPORTANCE MODIFIER:
    match_importance_modifier = ×1.15 (applied to all athlete signals in derby)
    Meaning: each athlete's availability matters 15% MORE in the derby than
      in a standard Serie A match.
      
  HOW TO APPLY:
    Step 1: Calculate standard athlete modifier (e.g. trequartista absent: ×0.85)
    Step 2: Apply match importance amplifier to the DEVIATION from baseline
      Deviation = modifier − 1.00 = −0.15
      Amplified deviation = −0.15 × 1.15 = −0.1725
      Amplified modifier = 1.00 − 0.1725 = ×0.8275 (rounds to ×0.83)
      
  PRACTICAL RESULT:
    Standard match: trequartista absent → ×0.85 modifier
    Milan Derby: trequartista absent → ×0.83 modifier (amplified)
    
  POSITIVE AMPLIFICATION:
    If key players are all available in the derby:
      Existing bonuses are also amplified by ×1.15
      Example: compound San Siro modifier ×1.12 in derby → ×1.138 (rounds to ×1.14)
    
  DEMAND SIGNAL — DERBY:
    Milan Derby results carry elevated demand signal weight: ×1.20 on demand impact
    Derby win (with key players available): compound positive demand signal
    Derby loss: compound negative demand signal
    Apply: derby_demand_amplifier = ×1.20 to all demand signal calculations.
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**$ACM token:**       `fan-token/league-football-token-intelligence.md`
**Serie A context:**  `athlete/football/juventus-juv.md` (shared tactical context)


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | AC Milan ($ACM) athlete intelligence: squad signals, key player form, and CDI modifier |
| Reasoning | ACTIVE | ACM reasoning chain from squad/player signals to APS and CDI modifier |
| Context | ACTIVE | ACM context: Serie A position, European competition status, injury list |
| Memory | ACTIVE | Historical AC Milan player form patterns and season-specific baseline data |
| Judgment | ACTIVE | Judgment on ACM signal hierarchy — key position absences vs depth player changes |
| Attention | ACTIVE | Elevated attention for injury news and European qualification signals |
| Communication | ACTIVE | ACM athlete output with APS modifier, squad state, and CDI contribution |
| Verification | ACTIVE | ACM data from Serie A official and AC Milan official announcement sources |
| Learning | ACTIVE | ACM APS calibration from historical Serie A performance-outcome correlation data |
| Integration | ACTIVE | Integrates with market-football, athlete-intel-football, and fan-token football intelligence |
| Calibration | ACTIVE | ACM APS modifier calibrated against historical Serie A and European outcome data |
| Adaptation | ACTIVE | ACM intelligence adapts as squad composition and European status change |
| Ethics | NOT APPLICABLE | ACM athlete intelligence is sports analysis — no ethical dimension |
| Transparency | ACTIVE | APS modifier, squad state source, and CDI modifier explicit in output |


---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*Number ten dependency — trequartista carries highest individual modifier at AC Milan*
