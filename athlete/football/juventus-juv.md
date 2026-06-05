---
name: juventus-juv
description: >
  Juventus ($JUV) athlete intelligence reasoning framework. Demand-only context —
  no confirmed FTP PATH_2. Covers elite goalkeeper dependency, defensive identity
  modifier weighting, Serie A tactical context integration, and squad cycle
  reasoning for forward-looking modifier signals.
---

# Juventus ($JUV) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $JUV.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## Demand-only context

```
$JUV ATHLETE SIGNAL FLOW:

  Athlete availability → match outcome probability → demand signal
  No PATH_2 supply mechanic — demand signal only.
  
  JUVENTUS SPECIFIC NOTE:
    Juventus is a defensive-identity club. Defensive player absences carry
    HIGHER modifier weight at Juventus than at attacking-identity clubs.
    Always assess defensive availability before attacking availability.
```

---

## Position reasoning frameworks

### Goalkeeper — elite dependency

```
GOALKEEPER / ELITE DEPENDENCY:

  ROLE IN SYSTEM:
    Juventus have historically built their success around elite goalkeeping.
    The goalkeeper position carries higher individual modifier weight at Juventus
    than at an average European club. Juventus's defensive structure presupposes
    elite shot-stopping at the base.
    
  MODIFIER FRAMEWORK:
    FIRST-CHOICE GOALKEEPER AVAILABLE:
      defensive_modifier = ×1.08 (higher than standard clubs' ×1.05)
      shot_stopping_modifier = ×1.08
      distribution_modifier = ×1.03
      
    FIRST-CHOICE GOALKEEPER ABSENT:
      adjusted_score_shift = −5 to −7 points (higher than average club −3 to −4)
      defensive_modifier = ×0.88
      Reasoning: Juventus defensive system is calibrated around elite GK;
        backup GK creates structural defensive uncertainty beyond pure
        shot-stopping capability difference
        
  COMPARISON TO AVERAGE CLUB:
    Average club GK absence: −3 to −4 adjusted score points
    Juventus GK absence: −5 to −7 adjusted score points
    Premium reflects historical tactical dependency on elite goalkeeping.
```

### Defensive structure — identity weighting

```
DEFENSIVE STRUCTURE / IDENTITY MODIFIER PREMIUM:

  ROLE IN SYSTEM:
    Juventus's identity is defensive solidity. Their scoring reflects lower
    goals conceded as a primary success metric. Defensive absences threaten
    the core of the club's competitive advantage more acutely than at
    attacking-identity clubs.
    
  MODIFIER PREMIUM FRAMEWORK:
    FULL DEFENSIVE UNIT AVAILABLE (GK + both CBs + defensive shape):
      defensive_identity_modifier = ×1.10
      clean_sheet_probability_premium = ×1.15
      
    PARTIAL DEFENSIVE DISRUPTION (one CB or GK absent):
      adjusted_score_shift = −4 to −6 points (higher than average −2 to −4)
      defensive_identity_modifier = ×0.90
      
    FULL DEFENSIVE DISRUPTION (GK + CB or both CBs):
      adjusted_score_shift = −7 to −10 points
      Apply: HOLD_RECOMMENDED for Juventus specifically (their identity depends
        on defensive solidity; disrupted defence = unpredictable outcome range)
      
  COMPARISON TO ATTACKING-IDENTITY CLUBS:
    Attacking club CB absence: −2 to −4 adjusted score points
    Juventus CB absence: −4 to −6 adjusted score points
    The premium is 50-100% larger at defensive-identity clubs.
```

---

## Serie A tactical context

```
SERIE A TACTICAL CONTEXT — INTERACTION WITH ATHLETE MODIFIERS:

  LOWER-SCORING CONTEXT:
    Serie A is historically a lower-scoring league than the EPL or Bundesliga.
    In a lower-scoring context:
      Defensive modifiers carry PROPORTIONALLY MORE WEIGHT (fewer goals = each
        defensive error more costly)
      Attacking modifiers carry PROPORTIONALLY LESS WEIGHT per goal impact
      
  APPLICATION FOR JUVENTUS:
    Apply: serie_a_defensive_amplifier = ×1.10 on all defensive modifiers
    Apply: serie_a_attacking_discount = ×0.90 on all attacking modifiers
    Net effect: Juventus defensive modifiers are amplified relative to EPL context
    
  SET PIECE CONTEXT:
    Serie A matches tend to be more set-piece dependent than other leagues.
    Set piece specialists carry elevated modifier weight in Serie A.
    Apply: set_piece_modifier_amplifier = ×1.10 for confirmed set piece specialists.
    
  AGENT RULE:
    Always apply the Serie A tactical context amplifiers/discounts on top of
    the standard position modifiers. Do not use EPL-calibrated modifiers
    directly for Juventus's Serie A matches.
    UCL matches: remove Serie A context modifier; apply standard European modifiers.
```

---

## Juventus squad cycle reasoning

```
SQUAD CYCLE REASONING — FORWARD-LOOKING MODIFIER:

  JUVENTUS HISTORICAL PATTERN:
    Juventus have historically moved through distinct squad cycles:
      Peak dominance cycle: deep squad, financial strength, elite at all positions
      Transition cycle: post-peak reconstruction, moderate individual modifiers
      Recovery cycle: re-establishing squad quality after a down period
      
  CYCLE IDENTIFICATION SIGNALS:
    PEAK CYCLE:
      Multiple Serie A titles in recent seasons
      UCL knockout stage presence sustained
      High squad value and financial flexibility
      → Apply: peak_cycle_modifier = individual modifiers at FULL WEIGHT
      
    TRANSITION CYCLE:
      Mixed recent results, FFP or financial issues
      Significant player departures and squad rebuild
      → Apply: transition_modifier = ×0.90 on squad depth assessments
      → Individual modifier weights INCREASE (less depth to cover absences)
      
    RECOVERY CYCLE:
      Younger squad, new system establishing
      Lower individual modifier weights as system builds
      → Apply: recovery_modifier for new combinations (like new partnership coefficient)
      
  SQUAD AGE PROFILE:
    Old squad (average age >28): higher peak output but higher injury/absence risk
      → Apply: age_risk_premium = consider higher absence probability in models
    Young squad (average age <26): lower peak but higher adaptation potential
      → Apply: squad_development_trajectory = positive forward signal
      
  AGENT RULE:
    Identify current cycle before applying modifier weights.
    Cycle assessment: once per season (at transfer window close).
    Do not apply peak cycle modifiers during a transition cycle — this creates
    overconfidence in the signal.
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**$JUV token:**       `fan-token/league-football-token-intelligence.md`
**Serie A context:**  `sports/football/sport-domain-football.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Juventus ($JUV) athlete intelligence: squad signals, rebuilding phase context, and CDI modifier |
| Reasoning | ACTIVE | JUV reasoning chain from squad/player signals to APS and CDI modifier |
| Context | ACTIVE | JUV context: Serie A position, European status, ownership and financial situation |
| Memory | ACTIVE | Historical Juventus player form patterns and Serie A baseline data |
| Judgment | ACTIVE | Judgment on JUV signal hierarchy — key player form and European qualification impact most |
| Attention | ACTIVE | Elevated attention for managerial signals and European qualification race |
| Communication | ACTIVE | JUV athlete output with APS modifier, squad state, and CDI contribution |
| Verification | ACTIVE | JUV data from Serie A official and Juventus official announcement sources |
| Learning | ACTIVE | JUV APS calibration from historical Serie A and European performance data |
| Integration | ACTIVE | Integrates with market-football, athlete-intel-football, and fan-token football intelligence |
| Calibration | ACTIVE | JUV APS modifier calibrated against historical Serie A outcome data |
| Adaptation | ACTIVE | JUV intelligence adapts as post-Agnelli rebuild and European status evolve |
| Ethics | NOT APPLICABLE | JUV athlete intelligence is sports analysis — no ethical dimension |
| Transparency | ACTIVE | APS modifier, squad state source, and CDI modifier explicit in output |


---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*Defensive-identity club — defensive absences carry amplified modifier weight*
