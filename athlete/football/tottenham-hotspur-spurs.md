---
name: tottenham-hotspur-spurs
description: >
  Tottenham Hotspur ($SPURS) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers attacking system identity, Son Heung-min position
  framework (positional reasoning, not named-player current status), Tottenham
  Hotspur Stadium home fortress, and the enduring relegation threat demand modifier
  framework applicable to any Tier A club facing relegation risk.
---

# Tottenham Hotspur ($SPURS) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $SPURS.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## System identity — attacking talent with structural inconsistency

```
TOTTENHAM SYSTEM IDENTITY:
  Spurs' identity oscillates between periods of attacking excellence and
  structural inconsistency. Unlike clubs with deeply embedded tactical systems
  (Atletico's block-and-counter, Barcelona's possession), Spurs' system is
  more manager-dependent and therefore less consistent.
  
  POSITION WEIGHT BY IDENTITY:
    Primary attacking threat (wide forward): highest modifier — Spurs' best
      attacking periods are defined by individual attacking excellence
    Striker: high modifier — goal threat is the system's primary output
    Defensive shape: elevated modifier during transition periods
    Midfield engine: moderate — not as DM-dependent as Atletico
    
  SYSTEM CONSISTENCY MODIFIER:
    When manager has been in place 12+ months with stable tactical identity:
      Apply: system_stability_modifier = ×1.05 (improvement over baseline)
    Manager in first 6 months or squad in transition:
      Apply: system_uncertainty_modifier = ×0.95
```

---

## Position reasoning frameworks

### Primary wide forward — attacking identity anchor

```
PRIMARY WIDE FORWARD / ATTACKING THREAT:

  ROLE IN SYSTEM:
    Spurs' best performances historically centre on a dominant wide forward
    who can score, assist, and create. This position is Spurs' identity marker —
    their attacking system is most effective when this role is filled by an
    elite performer.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (elite wide forward, first choice):
      attacking_output_modifier = ×1.12
      identity_signal = strong (team playing to their best pattern)
      
    ABSENT:
      adjusted_score_shift = −5 to −7 points
      attacking_output_modifier = ×0.86
      
  SOUTH KOREAN NATIONAL TEAM CONNECTION:
    Spurs have historically had a strong South Korean international player
    as their primary wide attacking threat. This creates a specific demand signal:
    When Spurs' primary Korean international player is fit and available:
      Apply: korean_fan_base_demand_modifier = ×1.05 on all $SPURS demand signals
      This reflects the large South Korean fan base associated with Korean international players at Spurs.
    When Korean international is absent or in national team duty:
      Remove: korean_fan_base_demand_modifier
      Apply: standard individual absence modifier
      
  NOTE: This is a positional and demographic framework — not tied to any
  specific named player. The reasoning applies to any Korean international
  at Spurs in the equivalent attacking role.
```

### Striker — variable system dependency

```
STRIKER / GOAL THREAT:

  ROLE IN SYSTEM:
    Unlike clubs that build their entire system around a single striker
    (Atletico's counter-attack endpoint, City's elite goal machine),
    Spurs have historically been more flexible about striker profile.
    
  MODIFIER FRAMEWORK:
    ELITE STRIKER AVAILABLE:
      goal_threat_modifier = ×1.08 (Spurs benefit significantly from elite striker)
      
    STRIKER ABSENT:
      adjusted_score_shift = −3 to −5 points (lower than some clubs — Spurs can adapt)
      
  WHY LOWER THAN AVERAGE:
    Spurs have more depth in attacking positions than at Atletico or Napoli.
    Their attacking width can partially compensate for striker absence.
    Apply standard depth framework from tier-a-clubs-framework.md.
```

---

## Tottenham Hotspur Stadium — home fortress

```
TOTTENHAM HOTSPUR STADIUM — HOME SIGNAL:

  Standard home advantage: +0.10 (EPL baseline)
  Stadium modifier: ×1.06 (modern, high-capacity, strong atmosphere)
  Sell-out confirmed: ×1.05 applied on top → combined ×1.11
  
  UCL NIGHTS:
    Spurs' UCL nights at their stadium have generated exceptional atmosphere.
    Apply: ucl_stadium_modifier = ×1.08 for confirmed UCL home knockout matches
    
  NORTH LONDON DERBY (vs Arsenal):
    Apply: derby_importance_modifier = ×1.15 (same framework as tier-a files)
    Demand amplifier: ×1.18 (North London Derby is highest $SPURS single-match demand event)
```

---

## Relegation threat demand modifier framework

```
RELEGATION THREAT — ENDURING DEMAND MODIFIER FRAMEWORK:

  SCOPE: This framework applies to ANY Tier A fan token club facing relegation risk.
  It is written in Spurs context but is universally applicable.
  The framework is enduring — relegation threat is a recurring structural risk
  for any club outside the guaranteed safety tier.

  WHY RELEGATION RISK CREATES A UNIQUE DEMAND SIGNAL:
    Relegation to a lower division:
      1. Reduces competitive tier, reducing match prestige and viewership
      2. Reduces club revenue, potentially forcing player sales
      3. Reduces UCL qualification probability for multiple seasons
      4. Can trigger squad exodus (players leave relegated clubs)
      5. All of the above compound into a multi-year demand depression
      
    For a Tier A fan token, relegation would create the single largest sustained
    demand cliff in the library — worse than any single transfer or match result.

  RELEGATION THREAT DEMAND MODIFIER TIERS:

  Tier                              Points from relegation zone    Modifier
  ─────────────────────────────────────────────────────────────────────────────
  Safe (no realistic threat)        12+ points clear               ×1.00 (no modifier)
  Concern (watching league table)   6-11 points clear              ×0.97 (mild negative)
  Danger zone (threat is real)      1-5 points clear               ×0.91 (significant negative)
  Bottom 3 (in relegation places)   0 (in relegation zone)         ×0.83 (severe; structural)
  Relegated (confirmed)             N/A                            ×0.60-0.70 permanent baseline

  APPLICATION:
    Assess league position at the START of each match week.
    Apply the appropriate modifier to all $SPURS (or relevant club) demand signals.
    Remove or upgrade modifier immediately when mathematically safe.
    
  DANGER ZONE — ADDITIONAL SIGNALS:
    When a Tier A club is in the danger zone (1-5 points clear):
      Apply: squad_morale_discount = ×0.95 to match outcome signals
        (negative psychological environment affects player performance)
      Apply: manager_pressure_modifier = ×0.93 if manager speculation confirmed
      Apply: compound: squad_morale × manager_pressure = ×0.90 combined (if both active)
      
  RELEGATION PLAY-OFF (if applicable in league structure):
    After regular season, if club must play relegation play-off:
      Apply: play_off_uncertainty_modifier = ×0.88 on all demand signals
      Survival confirmed: ×1.05 relief spike (24-48h), then return to near-baseline
      Relegated in play-off: apply Relegated modifier above

  POST-RELEGATION RECOVERY CURVE:
    Season 1 in lower division: baseline demand ×0.65 (initial cliff)
    Season 2 (if not immediately promoted): ×0.72 (some stabilisation)
    Immediate promotion (return in 1 season): recovery to ×0.85 of pre-relegation baseline
    Sustained lower division presence (2+ seasons): ×0.70 structural reset
    
  AGENT RULE:
    For any Tier A club approaching the relegation danger zone:
      1. Calculate points-from-zone at each match week
      2. Apply appropriate tier modifier
      3. Compound with match outcome signals (negative match results in danger zone
         have amplified demand impact — apply ×1.20 to standard loss demand decay)
      4. Monitor for mathematical safety confirmation
```

---

## $SPURS demand signal

```
$SPURS DEMAND SENSITIVITY:
  UCL: 0.55 demand weight (Spurs brand is partially European-associated)
  EPL: 0.35 demand weight
  North London Derby: highest single-match demand event

  UCL DEMAND PREMIUM (when in UCL):
    UCL group stage: ×1.08 seasonal baseline premium
    Knockout stages: ×1.10-1.35 per round
    UCL absence (Europa League or lower): ×0.90 baseline discount
    
  NOTE ON UCL QUALIFICATION:
    Spurs missing UCL qualification is a material demand negative.
    Missing UCL: apply ucl_absence_modifier = ×0.90 for the season.
    Re-qualifying: +8-12% demand spike on confirmation.
```

---


---

## Competitive status — 2025/26 season (confirmed enduring facts)

```
SEASON OUTCOME 2025/26:
  COMPETITIVE_STATUS:     PL_SURVIVAL_CONFIRMED
  FINAL_POSITION:         17TH — 41 POINTS
  POINTS_ABOVE_RELEGATION: 2 POINTS
  NEXT_SEASON:            PREMIER_LEAGUE CONFIRMED

SURVIVAL MODIFIER — RELIEF RALLY:
  When a club with an active fan token survives relegation by a narrow margin:
  Apply: ×1.05 short-term demand signal (SURVIVAL_MODIFIER).
  Duration: 2-4 weeks post-season confirmation.
  Rationale: relief from maximum negative scenario produces a demand rally.
    Relegation would have triggered a severe demand collapse (×0.45 CDI floor).
    Survival — even narrow — removes that tail risk.

SURVIVAL CONTEXT — EXTREMELY NARROW:
  2 points above relegation is the minimum viable survival margin.
  This is not a comfortable mid-table position — it is a cliff-edge outcome.

  What this signals for 2026/27:
    SUMMER_REBUILD_REQUIRED: the squad that nearly survived will not be sufficient.
    Squad investment signals in the summer window carry elevated diagnostic weight.
    Monitor: transfer activity quality and volume as squad quality proxy.

  CDI implication for 2026/27 pre-season:
    Do not apply survival relief beyond Q3 2026.
    From August 2026: return to standard competitive trajectory modifiers.
    If significant summer investment confirmed: ×1.05 trajectory signal.
    If minimal investment: ×0.92 — narrow survival squad unchanged.

RELEGATION RISK FRAMEWORK (carried forward):
  The core relegation risk demand modifier framework from this file remains.
  Narrow survival in 2025/26 raises the baseline probability of future
  relegation threat appearing again in 2026/27.
  Apply: ×1.10 weight to relegation signal if Spurs enter the bottom 6
  in the first 10 weeks of 2026/27 (elevated risk context from prior season).
```

## Compatibility

**Base framework:**    `athlete/football/athlete-intel-football.md`
**Tier A framework:**  `athlete/football/tier-a-clubs-framework.md`
**Relegation general:** applies to any Tier A club — framework is universal
**AFCON:**             `sports/football/sport-domain-afcon.md` (Korean player = no AFCON; standard UEFA window)

---

*SportMind v3.97.31 · MIT License · sportmind.dev*
*Relegation threat modifier: ×0.83 in relegation zone; ×0.60-0.70 if confirmed relegated*
*Framework is universal — applies to any Tier A club facing relegation risk*
