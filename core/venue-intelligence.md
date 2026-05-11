---
name: venue-intelligence
description: >
  Enduring reasoning framework for venue as a pre-match signal modifier.
  Covers neutral venue logic, home advantage baselines by sport, artificial
  pitch effects, altitude, pitch conditions, and stadium familiarity. Applies
  to every sport and fixture type. Load alongside sport-domain files.
---

# Venue and Stadium Intelligence

**Enduring framework for reasoning about venue as a pre-match signal modifier.
Applies to every sport and every fixture type.**

> SportMind Library Rule: all elements are permanently true regardless of
> specific venues, forecasts, or current match schedules.

---

## Neutral venue reasoning

```
NEUTRAL VENUE — SIGNAL FRAMEWORK:

  WHAT NEUTRAL VENUE REMOVES:
    Standard home advantage modifier is eliminated at neutral venues.
    Neither team receives the baseline home advantage adjustment.
    Do NOT apply home_advantage_modifier when venue is confirmed neutral.

  WHAT REPLACES HOME ADVANTAGE:
    At neutral venues, home advantage is replaced by THREE proxy signals:
    
    1. CROWD COMPOSITION:
       Estimate the crowd split based on:
         Geographic proximity of each team's fan base to the venue
         Ticket allocation if officially published
         Historical attendance data for similar fixtures at this venue
       Application:
         ≥60% crowd for Team A: apply crowd_proxy_modifier = ×1.03 for Team A
         ≥75% crowd for Team A: apply crowd_proxy_modifier = ×1.05 for Team A
         50/50 split: no modifier — true neutral
         
    2. GEOGRAPHIC PROXIMITY:
       Team travelling shorter distance to the neutral venue:
         <500km from home: proximity_modifier = ×1.02
         500-1,500km: no modifier
         1,500km+: apply travel_fatigue_modifier (see world cup framework)
         
    3. PSYCHOLOGICAL FAMILIARITY:
       Has one team played at this specific neutral venue more recently?
       Same stadium within last 12 months: familiarity_modifier = ×1.01 (marginal)
       Never played at this stadium: first_visit_modifier = ×0.97 (see below)

  TOURNAMENT FINAL VENUE REASONING:
    Final matches at neutral venues have additional signal characteristics:
      1. Both teams arrive after extended tournament runs — apply tournament
         fatigue framework (see sport-domain-football-world-cup.md)
      2. Crowd composition is more even than domestic neutral fixtures
      3. First visit modifier applies to BOTH teams if neither has played the venue
      4. Apply: finals_neutral_signal_weight = STANDARD (not elevated — equal
         preparation time for both teams reduces signal variance)

  AGENT RULE:
    Before every match: confirm neutral or home/away status.
    Neutral venue: remove home_advantage_modifier, apply proxy signals.
    Do not assume neutral = 50/50 without checking crowd composition.
```

---

## Home venue modifiers — by sport

```
HOME ADVANTAGE BASELINE BY SPORT:

  Sport                 Baseline modifier    Notes
  ──────────────────────────────────────────────────────────────────────
  Football (soccer)     +0.10 to adj score   Crowd pressure on officials, pitch familiarity
  Rugby union           +0.12               Lineout calls, crowd noise on scrums
  Basketball            +0.08               Crowd proximity in enclosed arenas
  Cricket               +0.15               Pitch preparation (home team prepares pitch)
  MMA                   +0.05               Crowd noise marginal; fighter psychology only
  Ice hockey            +0.09               Last change advantage; ice familiarity
  Rugby league          +0.11               Similar to union but slightly lower
  NFL American football +0.07               Less home advantage than other team sports
  Tennis                +0.04               Surface familiarity; crowd marginal effect
  Formula 1             +0.02               Home circuit familiarity; crowd negligible
  MotoGP                +0.03               Home circuit knowledge; crowd negligible

  NOTE: Cricket's +0.15 reflects pitch preparation — home groundskeepers tailor
  pitch conditions to home bowlers. This is structural, not just atmospheric.

STADIUM CAPACITY AMPLIFICATION:
  Larger stadiums amplify atmosphere signals — but only at or near full capacity.
  
  Framework:
    <50% capacity (sparse attendance):  apply home_advantage_modifier × 0.80
    50-75% capacity:                    standard modifier
    75-95% capacity:                    standard modifier
    95-100% capacity (near sell-out):   standard modifier × 1.03
    CONFIRMED SELL-OUT:                 standard modifier × 1.05

  SELL-OUT MODIFIER APPLICATION:
    Confirm sell-out from official source before applying.
    Do not assume sell-out from historical average attendance.
    Apply: sellout_confirmed_flag = true when verified.

FORTRESS VENUES:
  Some venues have documented statistical home records significantly above
  the sport average. Identify these through historical win% at venue.
    Standard home win% + 15%+:  apply fortress_modifier = ×1.08 on top of baseline
    Standard home win% + 10%+:  apply fortress_modifier = ×1.05
    These are rare — verify through calibration data before applying.
```

---

## Artificial pitch reasoning

```
ARTIFICIAL PITCH (4G/3G TURF) SIGNAL FRAMEWORK:

  WHAT ARTIFICIAL SURFACES CHANGE:
    Passing tempo: ball moves faster and more predictably on artificial turf
    Ball bounce: higher and more consistent than natural grass
    Injury risk: different injury patterns (ankle/knee contact injuries)
    Playing style: benefits technical passing teams; disadvantages direct/physical

  STYLE INTERACTION MODIFIERS:
    Technical possession team on artificial: attacking_output_modifier = ×1.05
    Physical/direct team on artificial: style_mismatch_modifier = ×0.97
    These modifiers apply to the VISITING team's style only — the home team on
    artificial is already calibrated to the surface.

  VISITING TEAM FAMILIARITY:
    First visit to artificial pitch:     unfamiliarity_modifier = ×0.94
    Occasional visitor (1-3 times/season): ×0.97
    Regular artificial pitch team (own ground is artificial): no modifier
    
  FAMILIARITY CHECK:
    Count the visiting team's artificial pitch matches in the current season.
    0 matches: apply ×0.94
    1-3 matches: apply ×0.97
    4+ matches: no modifier (calibrated)
    
  LEAGUES WITH SIGNIFICANT ARTIFICIAL PITCH PRESENCE:
    Scottish Premiership, Belgian Pro League, Scandinavian leagues, some MLS venues.
    When analysing fixtures in these leagues: always check surface before signal.
    
  AGENT RULE:
    Confirm surface before applying any artificial pitch modifier.
    Source: club official website or league ground database.
    Natural grass: no modifier. Artificial: apply framework above.
```

---

## Altitude reasoning

```
ALTITUDE AS A PERFORMANCE MODIFIER:

  MECHANISM: Reduced atmospheric oxygen at altitude decreases aerobic capacity.
  Effect is most pronounced for teams arriving from sea level.

  ALTITUDE MODIFIER TABLE:
    Venue altitude        Teams from sea level    Teams from high altitude
    ────────────────────────────────────────────────────────────────────
    Below 1,500m          No modifier             No modifier
    1,500 – 2,500m        ×0.95 (first 2 matches) No modifier (acclimatised)
    Above 2,500m          ×0.90 (first 2 matches) No modifier

  ACCLIMATISATION MODIFIER:
    Team arriving 5+ days early at altitude venue:
      Reduce altitude modifier by half:
        Normal ×0.95 → ×0.975 (effectively ×0.975 with early arrival)
        Normal ×0.90 → ×0.95
    Source: confirm early arrival from training camp reports (Tier 2 signal)

  DURATION:
    Altitude modifier applies to first 2 matches at altitude.
    After 2 matches: assume partial acclimatisation, reduce modifier to ×0.97.
    After 5+ days resident: remove altitude modifier entirely.

  SOUTH AMERICAN FOOTBALL CONTEXT:
    Highest risk venues (regularly above 2,500m):
      La Paz, Bolivia: ~3,600m — apply ×0.82 for first match (extreme altitude)
      Quito, Ecuador: ~2,850m — apply ×0.88 for first match
      Bogotá, Colombia: ~2,600m — apply ×0.90 for first match
      Medellín, Colombia: ~1,500m — apply ×0.95 for first match
    Note: South American clubs based at these altitudes: no altitude modifier
    Compound with Copa América framework (see sport-domain-copa-america.md)

  AGENT RULE:
    Check venue altitude for every South American fixture.
    Check altitude for any World Cup or tournament fixture in elevated regions.
    Do not assume European venues have significant altitude — most do not.
```

---

## Pitch condition reasoning

```
PITCH CONDITION SIGNAL FRAMEWORK:

  SOFT / HEAVY PITCH:
    Characteristics: waterlogged, slow ball, high physical demand
    Benefits:        physical, direct teams; reduces technical advantage
    Disadvantages:   technical passing teams; reduces quick combination play
    
    Soft pitch modifiers:
      Physical/direct team: ×1.05
      Technical/possession team: ×0.95
      Apply when: confirmed soft from pitch inspection report or recent rain
      
  FIRM / FAST PITCH:
    Characteristics: fast ball movement, quick passing lanes, low physical toll
    Benefits:        technical, passing teams; amplifies speed of play
    Disadvantages:   physical teams lose their slow-down advantage
    
    Firm pitch modifiers:
      Technical/possession team: ×1.05
      Physical/direct team: ×0.97
      
  WET / RAINY CONDITIONS (see also weather-intelligence.md):
    Ball slippage, reduced passing accuracy, elevated physicality value
    Combine wet weather modifier with pitch condition modifier if both apply.
    
  CRICKET-SPECIFIC PITCH CONDITIONS:
    Dry/dusty: benefits spin bowling significantly from day 1; deteriorates rapidly
      Apply: spin_modifier = ×1.25 on dusty pitches from day 3 onwards in Tests
    Green seamer-friendly: benefits pace bowling on day 1; flattens over time
      Apply: pace_modifier = ×1.20 on day 1 of seamer-friendly pitches
    Flat/batting paradise: neutralises bowlers; batting team advantage
      Apply: batting_team_modifier = ×1.08 on confirmed flat pitches
    Crumbling (day 4-5 Test): heavy spin expected; batting progressively harder
      Apply: spin_modifier ×1.35 and batting_difficulty_modifier ×1.20 on day 5

  AGENT RULE:
    Pitch condition is a signal at T-48h for cricket.
    For football/rugby: confirm from pitch inspection report at T-24h.
    Do not carry pitch condition modifier from previous match without confirmation.
```

---

## Stadium familiarity reasoning

```
STADIUM FAMILIARITY AS A SIGNAL MODIFIER:

  FIRST VISIT TO A STADIUM:
    Away team playing at a stadium for the first time applies a marginal modifier.
    Mechanism: unfamiliarity with dimensions, dressing room layout, crowd noise
    direction, turf characteristics at this specific ground.
    
    first_visit_modifier = ×0.97 (away team only)
    Duration: first match at this venue only
    Remove: from second visit onwards
    
  EUROPEAN AWAY GROUND CONTEXT:
    Certain European venues have documented hostile atmosphere reputations
    that amplify the standard away team disadvantage:
      Venues known for exceptional supporter pressure: apply ×0.95 away modifier
        (replaces standard ×0.97 — higher impact than typical away ground)
      Identify via: historical away team results at this venue, fan culture
    
  HOW TO ASSESS FAMILIARITY:
    Check away team's fixture history at this specific ground.
    Count matches in last 3 seasons: 0 = first visit; 1-2 = occasional; 3+ = familiar
    Apply: first_visit_modifier only on confirmed first visit.
    Do not apply for returning visits regardless of gap between them.
    
  GROUND DIMENSIONS:
    Some grounds have notably different dimensions affecting style of play:
      Narrow pitches: reduce wide play effectiveness ×0.95 for wide-play teams
      Large pitches: reduce pressing effectiveness ×0.97 for pressing teams
    Apply only when confirmed significant deviation from sport's standard dimensions.

  AGENT RULE:
    Stadium familiarity is a minor modifier (×0.97) — never the primary signal.
    Only apply when confirmed first visit.
    European hostile atmosphere applies ×0.95 — confirm via historical data.
```

---

## Compatibility

**Weather:**        `core/weather-intelligence.md`
**Altitude (Copa):**`sports/football/sport-domain-copa-america.md`
**Cricket pitch:**  `sports/cricket/sport-domain-cricket.md`
**Referee:**        `core/referee-intelligence.md`
**Tournament:**     `sports/football/sport-domain-football-world-cup.md`

---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*Enduring framework — applies to every sport and fixture type*
