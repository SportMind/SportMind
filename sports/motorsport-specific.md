---
name: motorsport-specific
description: >
  MotoGP and NASCAR extended reasoning frameworks, plus F1 team token reasoning.
  Covers weather primacy in MotoGP, NASCAR track type classification, F1 team
  token vs driver token distinction, and demand signals for $SAUBER, $AM,
  $ROUSH, $ALPINE. Extends existing sport domain files.
---

# Motorsport Extended Reasoning — MotoGP, NASCAR, F1 Team Tokens

**Extends existing sport domain files. Load base files first, then this file.**
Base files: `sports/formula1/sport-domain-formula1.md` ·
            `sports/motogp/sport-domain-motogp.md` ·
            `sports/nascar/sport-domain-nascar.md`

---

## Fan token context

```
ACTIVE MOTORSPORT FAN TOKENS:
  $SAUBER  — Sauber / Audi F1 team (TEAM token — demand-only)
  $AM      — Aston Martin F1 team (TEAM token — demand-only)
  $ROUSH   — Roush Fenway Racing NASCAR (TEAM token — demand-only)
  $ALPINE  — Alpine F1 team (TEAM token — demand-only)

ALL DEMAND-ONLY / ALL TEAM TOKENS:
  Motorsport fan tokens are TEAM tokens, not driver tokens.
  Constructor championship position is the primary demand driver.
  Individual race wins matter less than trajectory and championship position.
  No FTP PATH_2 confirmed for any motorsport token.
```

---

## MotoGP extended reasoning

```
WEATHER — HIGHEST VARIABLE IN MOTOGP:

  Rain transforms MotoGP race outcome probability more than any other variable
  in any other major motorsport. The core reasoning is in weather-intelligence.md.
  
  Additional MotoGP-specific rain reasoning:
  
  THE WET/DRY DECISION:
    In MotoGP, the tyre choice at race start is a binary that determines
    the entire race trajectory. Choosing wet tyres in conditions that dry
    is as disadvantageous as choosing dry in wet.
    Signal: pre-race track condition creates a decision point that amplifies
    the importance of the first lap — if conditions change, the leaders may
    switch tyres (pit stop = position change = increased race volatility).
    Apply: wet_tyre_decision_volatility_modifier = widen confidence interval ×1.40
    
  WET WEATHER SPECIALIST MODIFIER:
    ×1.20 for confirmed wet weather specialists (see weather-intelligence.md)
    How to identify: historical wet race win rate vs dry race win rate
    If wet win rate is 2×+ dry win rate: confirmed wet specialist
    
  INTERMEDIATE CONDITIONS (drying track):
    Most volatile race condition in MotoGP
    apply: intermediate_volatility_modifier = widen confidence interval ×1.50
    No directional signal reliable in intermediate conditions — HOLD or widen.

CIRCUIT TYPE REASONING — MOTOGP:

  POWER CIRCUITS (high-speed, long straights):
    Primary advantage: peak engine power; top speed
    Bike characteristic: low drag setup
    Signal: Teams with confirmed top-speed advantage → power_circuit_modifier = ×1.05
    
  TECHNICAL CIRCUITS (low speed, technical corners):
    Primary advantage: mechanical grip, agility, braking performance
    Bike characteristic: high downforce setup
    Signal: Teams with confirmed handling advantage → technical_circuit_modifier = ×1.05
    
  MIXED CIRCUITS (most circuits are mixed):
    No strong type modifier — standard form and qualifying apply
    
  TYRE COMPOUND REASONING:
    Michelin provides tyre selection per circuit; soft/medium/hard compounds.
    Teams that better manage tyre degradation outperform in the final laps.
    Signal: teams confirmed as better tyre managers → tyre_management_modifier = ×1.04
    in circuits known for high tyre degradation (identified through race history).
```

---

## NASCAR extended reasoning

```
TRACK TYPE — MOST CRITICAL NASCAR VARIABLE:

  NASCAR's most important pre-race signal is track type.
  Driver skill profiles differ dramatically across track types.
  (See base file sport-domain-nascar.md for track classification.)

OVAL vs ROAD COURSE:
  Traditional ovals (the NASCAR core):
    Standard form signals apply; car setup and drafting skill dominate
    
  Road courses (growing presence in NASCAR calendar):
    Internationally experienced drivers (F1, sports car, IndyCar backgrounds)
    have a documented advantage on road courses.
    road_course_experience_modifier = ×1.05 for confirmed road course specialists
    Apply: check driver's non-NASCAR road course competition history
    
SUPERSPEEDWAY REASONING (Daytona, Talladega):
  Pack racing fundamentally transforms outcome probability:
    Individual car quality is nearly irrelevant — pack dynamics dominate
    Drafting partnerships and positioning near lap 200 matter most
    Mechanical failures become the primary differentiator
    Apply: superspeedway_variance_modifier = widen confidence interval ×1.80
    Do NOT apply standard form signals at superspeedways — they are near-useless
    
  TOKEN NOTE ($ROUSH):
    Superspeedway results for $ROUSH have lower demand signal weight
    (unpredictable result reflects poorly on predictive framework)
    Apply: superspeedway_demand_weight = ×0.70 vs standard race demand weight

NASCAR PLAYOFF REASONING:
  Regular season final races with playoff position at stake:
    Teams near the playoff cut line race with elevated aggression
    Apply: playoff_bubble_aggression_modifier = ×1.05 for teams needing points
    Teams safely in or safely out: may manage risk more conservatively
    Apply: playoff_clinched_conservation_modifier = ×0.97 for teams already in
    
  Note: this changes racing behaviour, not car performance.
  The modifier affects signal for teams taking extra risks to qualify.
```

---

## F1 team token reasoning

```
TEAM TOKENS vs DRIVER TOKENS — THE CRITICAL DISTINCTION:

  WHY TEAM TOKENS DIFFER FROM CLUB FOOTBALL TOKENS:
    A football fan token reflects a CLUB identity (Arsenal, PSG, Barcelona).
    An F1 team token reflects a CONSTRUCTOR identity (Aston Martin, Alpine, Sauber).
    
    Individual race wins are less important for team tokens because:
      Championships are decided over 20+ races — one race changes little
      Constructor championship position is the primary season narrative
      Driver changes are common — team identity persists beyond driver

  PRIMARY DEMAND DRIVER — CONSTRUCTOR CHAMPIONSHIP POSITION:
    Team token demand follows constructor championship position, not race-by-race wins.
    
    Championship trajectory signals:
      Rising through the standings: demand_momentum_modifier = ×1.08
      Falling through the standings: demand_decline_modifier = ×0.93
      Stable mid-table: no modifier — baseline demand
      Challenging for constructors title: demand_premium = ×1.20

  SECONDARY DEMAND DRIVER — DEVELOPMENT TRAJECTORY:
    For midfield/lower teams ($SAUBER, $AM, $ALPINE):
      Faster improving teams generate stronger demand than stagnant frontrunners
      A team moving from P8 → P5 in constructors generates MORE demand signal
      than a top-3 team maintaining position.
      Apply: development_trajectory_modifier = ×1.10 for confirmed improving teams
      
  TERTIARY DEMAND DRIVER — TEAM NARRATIVE EVENTS:
    New title sponsorship: +5-10% demand spike (2-3 days)
    New driver announcement: +8-15% spike depending on driver profile
    Factory upgrades / new technical partnership: +3-7% spike
    These are transient spikes — see tier-a-clubs-framework.md for framework.

$SAUBER / AUDI F1 TRANSITION:
  Sauber is undergoing transition to become the Audi F1 works team.
  This creates a long-term narrative premium (Audi brand entry = major interest).
  Apply: manufacturer_entry_narrative_modifier = ×1.10 to $SAUBER demand
    during the transition announcement/entry period.
  Once Audi is fully established as manufacturer: remove modifier, reset to standard.

$AM — ASTON MARTIN F1:
  Aston Martin entered F1 as a team brand (previously Racing Point/Force India).
  Apply standard team token framework.
  Aston Martin's commercial luxury brand association adds a demographic premium:
    premium_brand_association_modifier = ×1.03 (marginal; affluent demographic)

$ALPINE — RENAULT F1 BRAND:
  Alpine is the Renault Group's F1 brand.
  French national identity in F1 creates a geographic demand concentration.
  Apply: french_market_demand_modifier = ×1.05 for French racing circuit events
    (Monaco especially — French-adjacent market concentration).
```

---

## Compatibility

**F1 base:**     `sports/formula1/sport-domain-formula1.md`
**MotoGP base:** `sports/motogp/sport-domain-motogp.md`
**NASCAR base:** `sports/nascar/sport-domain-nascar.md`
**Weather:**     `core/weather-intelligence.md` (MotoGP rain modifiers)


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Motorsport cross-domain framework: shared signal methodology for F1, MotoGP, and NASCAR |
| Reasoning | ACTIVE | Motorsport cross-domain reasoning chain with series-specific override hierarchy |
| Context | ACTIVE | Motorsport context: shared qualifying/form signals vs series-specific circuit/tyre differences |
| Memory | ACTIVE | Cross-motorsport outcome patterns and inter-series comparison data |
| Judgment | ACTIVE | Judgment on when cross-motorsport framework applies vs series-specific override |
| Attention | ACTIVE | Attention allocation framework across simultaneous motorsport events |
| Communication | ACTIVE | Cross-motorsport output with series identifier and framework version |
| Verification | ACTIVE | Motorsport verification — FIA (F1), FIM (MotoGP), NASCAR.com official sources |
| Learning | ACTIVE | Cross-motorsport calibration from accumulated series-specific outcome data |
| Integration | ACTIVE | Integrates with sport-domain-formula1.md, sport-domain-motogp.md, and sport-domain-nascar.md |
| Calibration | ACTIVE | Motorsport cross-series calibration: F1 qualifying_delta (4/4) as benchmark |
| Adaptation | ACTIVE | Motorsport framework adapts as new series enter the ecosystem |
| Ethics | NOT APPLICABLE | Motorsport framework is analytical — no ethical dimension |
| Transparency | ACTIVE | Series type, applied framework, and override rationale explicit in output |


---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*Motorsport tokens are TEAM tokens — constructor championship position drives demand*
