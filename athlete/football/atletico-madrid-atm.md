---
name: atletico-madrid-atm
description: >
  Atletico de Madrid ($ATM) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers defensive midfielder system dependency (the
  Atletico engine), central defensive block identity, counter-attack focal point,
  Wanda Metropolitano home fortress, and La Liga / UCL demand signal reasoning.
---

# Atletico de Madrid ($ATM) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $ATM.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## System identity — defensive-press hybrid

```
ATLETICO DE MADRID SYSTEM IDENTITY:
  Atletico's enduring tactical identity under sustained management is a
  disciplined defensive block combined with efficient counter-attacking output.
  The system is more structured than most Tier A clubs — individual position
  availability has above-average impact because roles are precisely defined.
  
  POSITION WEIGHT BY IDENTITY:
    Defensive midfielder: HIGHEST modifier — the engine of the entire system
    Centre backs: elevated — defensive block is the primary identity
    Striker: high — counter-attack endpoint; system built to release one forward
    Wide players: moderate — provide width but within narrow defensive structure
```

---

## Position reasoning frameworks

### Defensive midfielder — Atletico system engine

```
DEFENSIVE MIDFIELDER — HIGHEST POSITION MODIFIER AT ATLETICO:

  ROLE IN SYSTEM:
    Atletico's pressing trap and defensive block requires a defensive midfielder
    who covers ground, screens the back four, and enables rapid transitions.
    This position is more system-critical at Atletico than at most clubs —
    it is the pivot between defence and attack.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (first-choice DM):
      pressing_intensity_modifier = ×1.10
      defensive_block_cohesion = ×1.08
      transition_speed = FULL (rapid counter-press operational)
      
    ABSENT (DM replacement):
      adjusted_score_shift = −5 to −8 points
      pressing_intensity_modifier = ×0.86
      defensive_block_cohesion = ×0.90
      transition_vulnerability_flag = true
      
    WHY DM ABSENCE HURTS ATLETICO MORE THAN MOST CLUBS:
      At Arsenal: DM absence hurts pressing → apply ×0.90 modifier
      At Atletico: DM absence disrupts the ENTIRE defensive identity
        → apply ×0.86 modifier (deeper impact because system is DM-centred)
      The Atletico system is more DM-dependent than any other Tier A club in the library.
      
  DEFENSIVE MIDFIELDER vs ATTACKING POSITIONS:
    At attacking clubs: striker/winger absence = highest modifier
    At Atletico: DM absence = highest modifier
    This is the key distinction from Barcelona, PSG, AC Milan frameworks.
```

### Central defensive block

```
CENTRAL DEFENSIVE BLOCK:

  ROLE IN SYSTEM:
    Atletico's back four (or back five in some formations) is the defensive
    anchor. CB quality and availability is the foundation of Atletico's
    entire competitive approach.
    
  MODIFIER FRAMEWORK:
    BOTH FIRST-CHOICE CBs AVAILABLE:
      defensive_block_modifier = ×1.10
      Set piece defensive threat: ×1.08
      
    ONE CB ABSENT:
      adjusted_score_shift = −4 to −6 points
      defensive_block_modifier = ×0.93
      
    BOTH CBs ABSENT:
      adjusted_score_shift = −7 to −10 points; HOLD consideration
      
  LA LIGA CONTEXT:
    La Liga is a high-technical-quality league — attacking players create numerous
    opportunities. Atletico's defensive block is therefore tested at the highest
    level every week. CB reliability is particularly valuable in this context.
    Apply: la_liga_defensive_premium = ×1.05 amplifier on all CB modifiers
    (La Liga context makes CB availability relatively more valuable than average)
```

### Striker — counter-attack endpoint

```
STRIKER / COUNTER-ATTACK ENDPOINT:

  ROLE IN SYSTEM:
    Atletico's system creates space through defensive discipline, then releases
    one forward into open space. The striker is the endpoint of a carefully
    constructed counter-attack. A powerful, fast striker who can hold up play
    AND finish is the ideal system fit.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (system-fit striker):
      goal_threat_modifier = ×1.10
      counter_attack_efficiency = ×1.08 (system designed for this specific output)
      
    ABSENT:
      adjusted_score_shift = −4 to −6 points
      counter_attack_efficiency = ×0.88
      Note: lower impact than DM absence (DM is more system-critical)
      
  SYSTEM FIT VS GENERIC QUALITY:
    Atletico's system requires a specific striker profile. A generically talented
    striker who does not fit the high-work-rate, hold-up-play model disrupts the
    system even if they have high individual quality.
    Apply: system_fit_modifier = ×0.95 when a non-system-fit striker replaces the starter
      (system produces less efficiently with an ill-fitting profile)
```

---

## Wanda Metropolitano home fortress

```
WANDA METROPOLITANO — HOME SIGNAL:

  Standard home advantage: +0.10 (La Liga baseline)
  Wanda Metropolitano fortress modifier: ×1.08 (above La Liga average)
  UCL nights at Wanda: ×1.10 (elevated occasion atmosphere)
  
  DERBY — ATLETICO vs REAL MADRID or ATLETICO vs BARCELONA:
    Metropolitano derby (Madrid derby especially): ×1.12 atmosphere modifier
    Demand amplifier: ×1.15 for any Madrid derby result signal
    
  SELL-OUT CONFIRMED:
    Combined with fortress modifier: ×1.13

LA LIGA CONTEXT FOR ATLETICO:
  Apply standard La Liga tactical context:
    Set piece modifier: ×1.08 for confirmed Atletico set piece specialists
      (Atletico have historically been one of the best set piece teams in La Liga)
    Defensive modifier amplifier: ×1.05 (La Liga context premium — see CB section)
```

---

## $ATM demand signal

```
$ATM DEMAND — UCL AND LA LIGA:

  DEMAND SENSITIVITY:
    UCL: 0.60 demand weight (European campaign drives highest demand)
    La Liga: 0.30 demand weight
    Copa del Rey: 0.10 demand weight
    
  UCL DEMAND PREMIUM:
    Knockout stage progression: ×1.10 per round
    UCL semi-final: ×1.25
    UCL Final: ×1.40
    
  MADRID DERBY DEMAND:
    Atletico vs Real Madrid is the highest demand single-match event for $ATM.
    Apply: madrid_derby_demand_amplifier = ×1.20
    Duration: 48h spike then decays to baseline
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**$ATM token:**       `fan-token/league-football-token-intelligence.md`
**La Liga context:**  `sports/football/sport-domain-football.md`

---

*SportMind v3.97.31 · MIT License · sportmind.dev*
*DM-dependent system — defensive midfielder absence is the highest modifier at Atletico*
