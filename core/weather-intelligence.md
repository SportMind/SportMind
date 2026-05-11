---
name: weather-intelligence
description: >
  Enduring weather and environmental signal modifier framework. Systematic
  modifiers for temperature, rain, wind, humidity, and sport-specific
  conditions. Extends core-weather-match-day.md with compound modifier
  logic and motorsport/combat sports environmental reasoning.
  Load alongside core-weather-match-day.md for full weather coverage.
---

# Weather and Environmental Intelligence

**Systematic weather modifier framework extending `core/core-weather-match-day.md`.**
Do not duplicate — that file covers sport-by-sport weather signals.
This file covers systematic modifier logic, compound conditions, and sports
not covered in the base file.

> Load both files for full weather signal coverage.

---

## Temperature modifiers

```
TEMPERATURE — SYSTEMATIC MODIFIER TABLE:

  EXTREME HEAT (above 30°C):
    Effect: aerobic capacity degrades; both teams affected equally in theory
    However: fitness-first teams with higher physical conditioning are relatively
      less affected than technically-oriented teams who rely on movement patterns
      
    Base modifier (both teams): second half performance ×0.94 (from 60 minutes)
    Fitness-first team advantage: apply ×1.03 to their adjusted score relative
      to technically-oriented opponent (relative advantage, not absolute)
    Technical team penalty: ×0.97 when facing fitness team in extreme heat
    
    Note: evening kickoffs in heat reduce this modifier — temperatures typically
      drop significantly at night; apply heat modifier only if kickoff temp confirmed

  COLD CONDITIONS (below 5°C):
    Effect: reduces technical precision; benefits physical, direct play
    
    Cold modifier:
      Physical/direct style teams: ×1.02 (marginal benefit)
      Technical/passing style teams: ×0.97
      Apply when: confirmed temperature below 5°C at kickoff
      
    Below 0°C (freezing):
      Pitch freezing risk: confirm pitch pass before applying signal
      If pitch passes inspection: apply cold modifier + artificial pitch reasoning
      If pitch condition uncertain: apply signal_confidence_reduction = ×0.85

  OPTIMAL CONDITIONS (12–20°C):
    No temperature modifier — baseline conditions for most sports
    Both teams expected to perform at full technical and physical capacity
    
  AGENT RULE:
    Always check kickoff temperature, not daytime forecast.
    Evening fixtures often significantly cooler than afternoon conditions.
    Source: weather service at T-6h for best accuracy.
```

---

## Rain and wet conditions

```
RAIN — SYSTEMATIC MODIFIER FRAMEWORK:

  HEAVY RAIN (confirmed forecast or in-play condition):
    Effect: reduces ball control precision, slows passing speed, increases
      physical contact, reduces kicking accuracy in some sports
      
    Technical team modifier:  ×0.94 (significant reduction in technical expression)
    Physical team modifier:   ×1.04 (relative advantage in rain)
    
  LIGHT RAIN / INTERMITTENT SHOWERS:
    Technical team modifier: ×0.97 (marginal impact)
    Physical team modifier:  ×1.01 (marginal advantage)
    
  WET BALL EFFECTS (sport-specific):
    Football: passing accuracy reduced; long shots less accurate; GK handling affected
      Apply: wet_ball_modifier = ×0.96 to both teams' technical precision signals
    Rugby: handling errors elevated; kicking game affected; set piece advantage shifts
      Apply: wet_condition_kicking_modifier = ×0.85 for teams reliant on kicking game
    Cricket: swing bowling amplified in overcast+wet; see dew factor separately
    
  WATERLOGGED PITCH:
    When pitch is waterlogged (pre-match inspection confirms):
      Apply: both soft pitch modifier (from venue-intelligence.md) AND wet ball modifier
      Combined: technical team penalty ×0.94 × ×0.96 = ×0.9024 (significant)
      Note: if match is called off — no signal; do not pre-apply modifier speculatively
      
  DEW FACTOR (cricket-specific):
    Dew accumulates in evening T20 matches when humidity exceeds 70%.
    Apply dew factor separately — see core-weather-match-day.md.
    This is a structural advantage signal, not a weather penalty signal.
```

---

## Wind modifiers

```
WIND — SPORT-SPECIFIC MODIFIERS:

  STRONG WIND (confirmed above 30mph / 48kph):

  RUGBY (union and league):
    Kicking-dominant team with wind against: ×0.88 attacking modifier
    Kicking-dominant team with wind behind: ×1.10 attacking modifier
    Wind direction matters: facing wind in first half → WITH wind in second half
    Apply: wind_direction_timing_modifier (which half does each team face the wind?)
    
  CRICKET:
    Swing bowling with crosswind or against wind: ×1.15 swing_modifier
    Crosswind: both swing AND seam movement affected
    Tail wind (bowling with wind): reduced swing but pace amplified
    Apply: assess wind direction relative to each bowler's style
    
  AMERICAN FOOTBALL:
    Kicking game: kicking_modifier = ×0.82 in strong wind for long kicks
    Deep passing: quarterback_deep_throw_modifier = ×0.88 in strong wind
    Short passing, running game: minimal wind effect
    Apply: wind_dominance_modifier for teams relying heavily on passing game
    
  FOOTBALL (soccer):
    Long balls and direct play: more effective WITH the wind ×1.05
    Short passing game: minimal impact below 35mph; at 40mph+ apply ×0.97
    
  CROSS WIND VERSUS HEAD WIND:
    Cross wind: affects ball flight trajectory — shots and crosses curve unpredictably
      Apply: cross_wind_uncertainty_modifier = widen signal confidence range ×1.10
    Head wind: reduces range of effective play; benefits short passing more than long
    Tail wind: amplifies direct play and long ball effectiveness
    
  AGENT RULE:
    For kicking sports (rugby, American football, golf): always check wind speed and direction.
    For football: apply only above 30mph confirmed sustained wind.
    Wind is NOT reliable from forecasts alone — confirm at T-2h from live weather station.
```

---

## Humidity modifiers

```
HUMIDITY — PERFORMANCE MODIFIER:

  HIGH HUMIDITY (above 80%):
    Effect: sweat evaporation reduces; core temperature regulation impaired
    Both teams affected; most acute in second half (accumulated heat stress)
    
    Apply: humidity_second_half_modifier = ×0.95 for both teams from 60 minutes
    This stacks with any temperature modifier if heat AND humidity apply.
    
  CRICKET DEW (60-80% humidity, evening):
    Apply the dew factor modifier (see core-weather-match-day.md)
    Dew factor is a separate structural signal, not a performance penalty.
    
  TROPICAL CONDITIONS (heat + humidity combined):
    Compound modifier: apply BOTH temperature modifier AND humidity modifier
    Do not add them — multiply:
      Example: heat ×0.94 AND humidity ×0.95 = ×0.94 × ×0.95 = ×0.893
    This compound is significant — flag in signal output as compound_condition = true
    
    Most relevant for:
      Football in Southeast Asia, Middle East summer, South American tropics
      Cricket in South Asia (India, Sri Lanka, Bangladesh in monsoon season)
      Rugby tours to tropical regions
      
  AGENT RULE:
    Check humidity alongside temperature for all matches in tropical regions.
    Apply compound modifier when BOTH temp >28°C AND humidity >75%.
    Source: same weather service as temperature — report both together.
```

---

## Motorsport environmental modifiers

```
FORMULA 1 — ENVIRONMENTAL SIGNAL MODIFIERS:

  TRACK TEMPERATURE:
    F1 tyre compounds are optimised for specific track temperature windows.
    Track temperature affects which tyre compounds work as intended.
    
    When track temperature falls outside a compound's optimal range:
      Underperforming compound: tyre_performance_modifier = ×0.95 for affected teams
      Strategic flexibility elevated: teams willing to deviate from optimal strategy
      
    Signal: teams with best tyre management in non-optimal conditions gain relative advantage
    Apply: tyre_management_specialist_modifier = ×1.03 for confirmed tyre management teams
    
  RAIN IN FORMULA 1:
    Rain changes the race signal fundamentally:
      Safety car probability: elevated (typical wet race SC probability ×2.5 vs dry)
      Lead lap changes: elevated (volatility signal increases)
      Overtaking: paradoxically may increase or decrease depending on circuit type
      Wet specialists: apply ×1.05 for teams/drivers with documented wet performance
      
    Safety car deployment signal:
      Every safety car increases unpredictability — widen adjusted score confidence range
      Apply: safety_car_uncertainty_modifier = expand prediction interval by ×1.30
      
  TOKEN NOTE ($SAUBER, $AM, $ALPINE — team tokens not driver tokens):
    Environmental modifiers affect TEAM performance signals, not individual drivers.
    Car performance in rain is engineering-determined, not driver-determined at team level.
    Apply: wet_performance_team_modifier based on team's wet weather car history.

MOTOGP — ENVIRONMENTAL SIGNAL MODIFIERS:

  RAIN IN MOTOGP (highest weather sensitivity in motorsport):
    Rain is the single most important variable in MotoGP — more transformative
    than in any other major motorsport.
    
    In dry conditions: established form and qualifying position are strong predictors.
    In wet conditions: the race outcome probability distribution widens dramatically.
    
    WET WEATHER SPECIALIST MODIFIER:
      Riders known for exceptional wet performance: ×1.20 in confirmed wet conditions
      (This is the highest single-variable modifier in the library for motorsport)
      This overrides their dry-conditions modifier — wet skill dominates in MotoGP.
      
    RACE DAY RAIN CONFIRMATION:
      Apply wet modifier only when rain is confirmed at track temperature (not forecast).
      If conditions are changing (drying track): apply intermediate_condition_modifier = ×1.10
      for wet specialists and ×0.95 for dry-track specialists.
      
    TOKEN SIGNAL ($MOTOGP not active; reference for future tokens):
      MotoGP wet race outcome is less predictable than dry — demand signals from
      wet race results should be weighted at ×0.70 of normal result weight
      (lower confidence in the outcome as a form signal).
      
  CIRCUIT TYPE (MotoGP):
    Power circuits (long straights, high top speed):
      Benefits: engines with highest peak power output
      Apply: power_circuit_modifier for teams with confirmed top-speed advantage
    Technical circuits (slow corners, fast direction changes):
      Benefits: bikes with high mechanical grip and agility
      Apply: technical_circuit_modifier for confirmed handling-dominant packages
```

---

## Compound condition framework

```
APPLYING COMPOUND ENVIRONMENTAL CONDITIONS:

  When multiple weather/environmental conditions apply simultaneously,
  multiply modifiers rather than adding them.
  
  EXAMPLES:
    Heat (×0.94) + Humidity (×0.95) = compound ×0.8930
    Rain (×0.94 technical) + Wind (×0.97 football) = ×0.9118 for technical team
    Altitude (×0.95) + Heat (×0.94) = ×0.8930 for low-altitude visiting team
    
  COMPOUND MODIFIER CAP:
    No single compound set of environmental modifiers should exceed ×0.75 reduction.
    If compound modifier drops below ×0.75: flag as extreme_conditions = true
    Apply: ×0.75 floor and flag for human review.
    
  SIGNAL CONFIDENCE REDUCTION:
    When compound conditions apply:
      Apply: compound_signal_confidence_reduction = ×0.90 on directional weight
      Compound conditions increase outcome variance — widen prediction interval.
      
  AGENT RULE:
    List each modifier applied separately in signal output.
    Show the compound product.
    Flag when compound modifier drops below ×0.85 as a caution signal.
```

---

## Compatibility

**Base weather file:**  `core/core-weather-match-day.md` (load alongside)
**Venue conditions:**   `core/venue-intelligence.md`
**Pitch conditions:**   `core/venue-intelligence.md` (soft/firm pitch)
**Copa altitude:**      `sports/football/sport-domain-copa-america.md`
**Cricket dew:**        `sports/cricket/sport-domain-cricket.md`

---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*Load alongside core-weather-match-day.md — this file extends, not replaces it*
