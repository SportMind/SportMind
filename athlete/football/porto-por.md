---
name: porto-por
description: >
  FC Porto ($POR) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers youth academy pipeline system, Estádio
  do Dragão home fortress, Primeira Liga tactical context, and $POR demand
  signals linked to player export pipeline and Champions League campaigns.
---

# FC Porto ($POR) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $POR.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## System identity — youth pipeline and European ambition

```
FC PORTO SYSTEM IDENTITY:
  Porto's identity is built on two pillars:
  1. Elite youth development and player export — consistently producing and
     selling world-class players makes individual player departure a feature,
     not a disruption
  2. UCL overperformance — Porto consistently outperform their budget in
     Europe, creating demand signals that are disproportionate to domestic
     league profile
     
  POSITION WEIGHT BY IDENTITY:
    This dual identity creates a unique modifier context:
      Individual player departures: LOWER modifier impact than at peer clubs
        (Academy produces replacements; departures are factored into the model)
      UCL overperformance: demand signal disproportionate to Portuguese league profile
```

---

## Position reasoning frameworks

### Academy pipeline — reduced absence impact

```
ACADEMY PIPELINE — DEPTH DISCOUNT:

  WHY PORTO'S ACADEMY CHANGES THE MODIFIER FRAMEWORK:
    Porto's academy (youth system) is globally recognised for producing
    elite talent at every position. Unlike clubs that buy squad depth,
    Porto grow it. This creates a structural depth that reduces individual
    absence modifier weight.
    
  DEPTH DISCOUNT APPLICATION:
    Apply: porto_academy_depth_discount = ×0.80 on all non-elite individual modifiers
    (20% reduction in modifier weight across all non-marquee positions)
    
    Elite positions (key striker, primary creative midfielder): full modifier still applies
    Non-elite positions: discount applies — academy replacements are genuinely competitive
    
  COMPARISON:
    Barcelona: La Masia ×0.85 discount (15% reduction)
    Manchester City: squad depth ×0.85 discount (15% reduction)
    Porto: academy depth ×0.80 discount (20% reduction) — deeper pipeline relative to squad size
    
  PLAYER EXPORT SEASON DISRUPTION:
    Porto typically sell 2-3 key players each summer window.
    This is EXPECTED and should be modelled differently from surprise departures:
      Expected export sale: apply reduced departure decay (×0.95 vs standard ×0.88-0.93)
      Unexpected sale (mid-season): apply standard departure decay framework
      
  AGENT RULE:
    Before summer window: assume 2-3 key departures are likely.
    Do not apply full departure decay to anticipated Porto summer sales.
    Apply full decay only for unexpected or mid-season departures.
```

### Striker and creative midfielder

```
ELITE POSITION — FULL MODIFIER APPLIES:

  Despite the academy depth discount, Porto's elite positions retain full individual weight.
  
  PRIMARY STRIKER:
    goal_threat_modifier = ×1.08 (standard elite striker level)
    academy_discount: does NOT apply — elite striker quality not reliably replaced internally
    Absent: adjusted_score_shift = −4 to −6 points (standard; no academy discount here)
    
  PRIMARY CREATIVE MIDFIELDER:
    chance_creation_modifier = ×1.05
    academy_discount: does NOT apply for elite creative role
    Absent: adjusted_score_shift = −3 to −5 points
```

---

## Estádio do Dragão — home fortress

```
ESTÁDIO DO DRAGÃO — HOME SIGNAL:

  Porto's home ground has a documented strong home record.
  Porto are among the most dominant home teams in Portuguese football.
  
  Home advantage: standard +0.10 (football baseline)
  Dragão fortress modifier: ×1.08 (consistent home dominance)
  European nights: ×1.10 (Porto's European atmosphere is exceptional —
    Dragão on UCL nights is documented as genuinely intimidating for visitors)
    
  PRIMERA LIGA DOMESTIC CONTEXT:
    Portuguese league has weaker opposition depth than top-5 European leagues.
    Home advantage against smaller Portuguese clubs: standard — no amplification
    Home advantage against Sporting CP, Benfica (O Clássico): ×1.12 (derby modifier)
```

---

## UCL overperformance and $POR demand

```
$POR DEMAND — UCL OVERPERFORMANCE SIGNAL:

  PORTO'S STRUCTURAL UCL PREMIUM:
    Porto consistently qualify for UCL and regularly outperform their seeding.
    Their brand in European football exceeds their domestic league profile.
    
  DEMAND FRAMEWORK:
    UCL group stage qualification: demand_premium = ×1.12 (above average club premium;
      Porto's brand is UCL-associated more than Primeira Liga-associated)
    UCL knockout progression: ×1.12 per round (higher than average due to brand premium)
    UCL last-16 or better: significant global attention → elevated demand signal
    UCL Final appearance: maximum demand event for $POR; historically unprecedented
      but would create the largest demand spike in $POR history
      
  DEMAND SENSITIVITY WEIGHTING:
    UCL weight: 0.70 | Domestic (Primeira Liga): 0.30
    (Inverse of typical club: Porto's demand signal is European-dominant)
    
  PLAYER EXPORT DEMAND INTERACTION:
    When Porto sell a key player to a top-5 European club:
      Short-term: departure decay (−8-15% over 4-8 weeks)
      Long-term: global narrative — "Porto Academy produces world-class talent"
        This narrative creates a POSITIVE structural demand modifier:
        apply: talent_factory_brand_modifier = ×1.05 sustained
        (Porto's brand as talent exporter is value-enhancing, not just value-losing)
      Net: departure decay + talent_factory_modifier → net closer to neutral than
        a standard departure would suggest
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**Venue:**            `core/venue-intelligence.md`
**Transfer signal:**  `core/transfer-window-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | FC Porto ($POR) athlete intelligence: squad signals, Portuguese context, and CDI modifier |
| Reasoning | ACTIVE | POR reasoning chain from squad/player signals to APS and CDI modifier |
| Context | ACTIVE | POR context: Liga Portugal position, Champions League status, pipeline talent |
| Memory | ACTIVE | Historical Porto player form patterns and Liga Portugal/UCL performance data |
| Judgment | ACTIVE | Judgment on POR signal hierarchy — talent pipeline departures most material signal |
| Attention | ACTIVE | Elevated attention for Champions League qualifier signals and key player departure rumours |
| Communication | ACTIVE | POR athlete output with APS modifier, squad state, and CDI contribution |
| Verification | ACTIVE | POR data from Liga Portugal official and FC Porto official announcement sources |
| Learning | ACTIVE | POR APS calibration from historical Liga Portugal and UCL performance data |
| Integration | ACTIVE | Integrates with market-football, athlete-intel-football, and fan-token football intelligence |
| Calibration | ACTIVE | POR APS modifier calibrated against historical Liga Portugal and UCL outcome data |
| Adaptation | ACTIVE | POR intelligence adapts as talent pipeline cycles and European status change |
| Ethics | NOT APPLICABLE | POR athlete intelligence is sports analysis — no ethical dimension |
| Transparency | ACTIVE | APS modifier, squad state source, and CDI modifier explicit in output |


---

*SportMind v3.97.29 · MIT License · sportmind.dev*
*Academy pipeline creates ×0.80 depth discount on individual modifiers (deepest in library)*
