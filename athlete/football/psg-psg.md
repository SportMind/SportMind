---
name: psg-psg
description: >
  Paris Saint-Germain ($PSG) athlete intelligence reasoning framework.
  Demand-only context — no confirmed FTP PATH_2 mechanic. Covers position
  modifiers, post-marquee-departure system reasoning, UCL pedigree modifier,
  and how squad transitions affect demand signal calculation.
---

# Paris Saint-Germain ($PSG) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $PSG.**
Athlete intelligence affects match outcome probability and demand signal only.
No supply mechanic implications — do not apply PATH_2 chain to PSG athlete signals.

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## Demand-only athlete signal chain

```
$PSG ATHLETE SIGNAL FLOW:

  Athlete availability → match outcome probability → demand signal
  
  NO PATH_2 SUPPLY MECHANIC:
    PSG athlete signals do NOT propagate into supply event probability.
    This is categorically different from $AFC.
    Apply: demand_signal_only = true for all PSG athlete intelligence.
    
  WHAT THE DEMAND SIGNAL COVERS:
    Win probability → tournament progression probability → demand trajectory
    Key player availability → fan sentiment → trading volume signal
    Star player performance → media narrative → organic demand amplifier
```

---

## Position reasoning frameworks

### Right back — attacking width

```
RIGHT BACK / ATTACKING FULLBACK:

  ROLE IN SYSTEM:
    PSG's system depends on overlapping fullbacks to provide attacking width.
    The right back provides progressive carries, crosses, and wide combinations
    that unlock central spaces. Without the first-choice right back, PSG's
    attacking width is materially reduced.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (first-choice right back):
      attacking_width_modifier = ×1.05
      wide_threat_signal = FULL WEIGHT
      
    ABSENT (right back replacement):
      adjusted_score_shift = −3 to −4 points
      attacking_output_modifier = ×0.93
      wide_threat_signal = REDUCED
      
  DEMAND SIGNAL NOTE:
    Right back absence is a moderate negative demand signal for PSG — not acute.
    The position matters tactically but carries lower fan sentiment weight than
    attacking positions. Apply: sentiment_weight = 0.4 (vs 1.0 for striker).
```

### Striker — primary goal threat

```
STRIKER / PRIMARY GOAL THREAT:

  ROLE IN SYSTEM:
    PSG's goal threat centralises on a primary striker. The striker's
    availability directly affects match outcome probability and fan sentiment
    in the highest-intensity way of any position.
    
  MODIFIER FRAMEWORK:
    AVAILABLE:
      goal_threat_modifier = ×1.10
      adjusted_score: full signal weight
      
    ABSENT:
      adjusted_score_shift = −5 to −7 points
      goal_threat_modifier = ×0.85
      
  DEMAND SIGNAL NOTE:
    Striker absence is the highest-sentiment demand signal at PSG.
    Fan attention concentrates on the goal scorer.
    Apply: demand_sentiment_weight = 1.0 (maximum) for striker availability.
    Striker absence + UCL knockout stage = compound negative demand signal.
```

### Wingers — system width and creativity

```
WINGERS — OFFENSIVE SYSTEM:

  ROLE IN SYSTEM:
    PSG operates with active wingers who rotate positions and combine with
    the striker and attacking midfielder. Winger availability affects both
    direct threat and combination play in the final third.
    
  MODIFIER FRAMEWORK:
    BOTH FIRST-CHOICE WINGERS AVAILABLE:
      final_third_combination_modifier = ×1.08
      
    ONE WINGER ABSENT:
      adjusted_score_shift = −2 to −4 points
      attacking_output_modifier = ×0.94
      Note: which winger matters — dominant side winger carries higher modifier
      
    BOTH WINGERS ABSENT:
      adjusted_score_shift = −5 to −7 points
      attacking_output_modifier = ×0.85
      Apply: HOLD_RECOMMENDED consideration if both absent + striker uncertain
      
  WINGER COMBINATION NOTE:
    PSG's winger pairing develops chemistry over time.
    New winger combinations: apply combination_adjustment_modifier = ×0.97
    for first 3-4 matches before chemistry establishes.
```

---

## Post-marquee departure reasoning

```
POST-MARQUEE-DEPARTURE SYSTEM REASONING:

  WHEN A GENERATIONAL PLAYER DEPARTS:
    PSG has experienced high-profile departures of world-class players.
    When a player of generational quality leaves, the club undergoes a
    system identity transition that affects modifier calculations for
    multiple subsequent seasons.

  TRANSITION PHASES:
    Phase 1 — Immediate post-departure (first season):
      Squad identity undefined around new system.
      Apply: system_uncertainty_modifier = ×0.95 for first 10-15 matches.
      Individual player modifiers are less reliable (roles still establishing).
      Demand signal: short-term negative, but stabilises as new identity forms.
      
    Phase 2 — Recalibration (remainder of first season):
      New system identity begins to stabilise.
      Individual player modifiers can be re-established around new roles.
      Remove system_uncertainty_modifier after 15 matches.
      
    Phase 3 — New identity established (second season+):
      Apply normal individual modifier framework.
      Demand signal: reset to new baseline (no longer penalised for departure).
      Note: demand baseline may be lower than during marquee era — this is the
        new structural baseline, not a temporary depression.

  DEMAND SIGNAL — MARQUEE DEPARTURE:
    Departure event itself: apply departure_demand_decay = −15 to −25%
    Recovery timeline: 4-8 weeks then stabilises at new lower baseline
    Permanent baseline reduction: proportional to departed player's global profile
    (Ballon d'Or-level departure = larger and longer baseline reduction)

  AGENT RULE:
    Monitor: how many seasons post-departure?
    Phase 1: apply system_uncertainty_modifier
    Phase 2+: apply normal framework
    Never assume PSG's system identity is static across player generations.
```

---

## UCL pedigree modifier

```
UCL PEDIGREE MODIFIER:

  WHEN TO APPLY:
    Apply ×1.05 psychological modifier in UCL knockout matches when PSG
    have won the most recent UCL edition (i.e. defending champions).
    
  REASONING:
    Defending UCL champions carry structural psychological advantages
    in knockout stages:
      Experience: the squad has navigated the pressure stages successfully
      Confidence: belief in ability to handle high-pressure moments
      Opponent respect: opponents may be more cautious or reactive
      
  MODIFIER:
    ucl_defending_champion_modifier = ×1.05
    Apply to: UCL knockout matches only (R16, QF, SF, Final)
    Do NOT apply to: group stage, domestic matches, other competitions
    Remove when: PSG are no longer the defending UCL champion
    
  DEMAND SIGNAL INTERACTION:
    PSG defending UCL champion + UCL knockout progression = amplified demand signal
    Each knockout round advanced while defending champion = elevated demand premium
    Apply: ucl_champion_demand_amplifier = ×1.03 per knockout round advanced
    
  AGENT RULE:
    Confirm PSG's UCL status before any UCL knockout match.
    Apply modifier only if PSG won the previous season's UCL Final.
    Do not apply in years when PSG did not win the previous edition.
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**$PSG token:**       `fan-token/league-football-token-intelligence.md`
**UCL structure:**    `sports/football/sport-domain-football.md`

---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*Demand-only — no PATH_2 supply mechanic for $PSG*
