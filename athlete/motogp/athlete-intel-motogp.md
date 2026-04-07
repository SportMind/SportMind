# MotoGP — Athlete Intelligence

Player-level intelligence for motogp predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** MotoGP team and rider prediction markets; emerging tokens

---

## Overview

MotoGP is rider-first but hardware-constrained. A world-class rider on a satellite bike cannot match a factory team's pace in dry conditions. Wet races are the exception — rider skill dominates over hardware. Crash probability is the primary risk variable.

---

## Commands

| Command | Description |
|---|---|
| `get_availability` | Player/athlete availability status |
| `get_form_score` | Recent performance score (last 5 events) |
| `get_sport_modifier` | Sport-specific key variable modifier |
| `get_athlete_signal_modifier` | Composite modifier — runs all sub-skills |

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for MotoGP. Combines availability, form, and sport-specific variables.

**Parameters:**
- `player_id` (required) — athlete identifier  
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{
  "athlete": "string",
  "availability": 1.0,
  "form_score": 0.85,
  "sport_specific_modifier": 1.05,
  "composite_modifier": 1.05,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["string"],
  "modifier_reason": "Wet weather rating and hardware tier is the primary driver"
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Peak fitness, top recent form, ideal conditions | ×1.20 |
| Fit, good form | ×1.10 |
| Neutral | ×1.00 |
| Minor fitness concern | ×0.90 |
| Significant fitness doubt | ×0.80 |
| Key athlete confirmed unavailable | ×0.70 |

---

## Integration example

### MotoGP pre-event workflow

```
# Step 1: Load domain context
Load sports/motogp/sport-domain-motogp.md

# Step 2: Athlete checks
get_availability athlete=[ATHLETE_ID]
get_form_score athlete=[ATHLETE_ID]
get_sport_modifier athlete=[ATHLETE_ID]

# Step 3: Get composite modifier
get_athlete_signal_modifier athlete=[ATHLETE_ID] event=[EVENT_ID]

# Step 4: Decision logic
# composite_modifier >= 1.10 AND signal >= 65 → ENTER
# composite_modifier < 1.00 OR injury_warning → WAIT or ABSTAIN
```

---

## Compatibility

**L1 domain:** `sports/motogp/sport-domain-motogp.md`
**L4 market:** `market/market-motogp.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_qualifying_position` | Grid position, Q1/Q2 progression, gap to pole | Yes |
| `get_tyre_management_profile` | Tyre degradation rate, compound preference, late-race pace | Yes |
| `get_wet_weather_rating` | Wet race specialist score — most predictive in rain | Yes |
| `get_circuit_history` | Win%, podium%, DNF% at this specific circuit | Yes |
| `get_crash_risk` | Historical crash rate, aggressive style rating, recent incidents | Yes |
| `get_manufacturer_tier` | Factory vs satellite; current championship competitiveness | Yes |
| `get_athlete_signal_modifier` | Composite MotoGP modifier | Yes |

---

## Hardware vs rider intelligence

```
MOTOGP IS HARDWARE-CONSTRAINED — but less than F1:

Unlike Formula 1 where constructor tier explains ~60% of outcomes,
MotoGP rider talent explains ~45-50% — more individual than F1.
The gap between factory and satellite hardware is real but smaller.

MANUFACTURER TIERS (updated seasonally):
  Factory Tier 1 (championship-contending hardware):
    Riders: Factory team designation, full development bike, 2026 parts access
    Base modifier: × 1.10
    
  Factory Tier 2 (competitive but trailing):
    Base modifier: × 1.03
    
  Satellite Tier 1 (year-old factory bike — "A-spec" satellite):
    Base modifier: × 0.97
    
  Satellite Tier 2 (2+ year old bike):
    Base modifier: × 0.90

FACTORY vs SATELLITE IN WET RACES:
  Wet race hardware gap: REDUCED significantly (same as F1)
  In wet: rider_wet_skill dominates over hardware tier
  Apply: ignore hardware modifier in wet; use wet_weather_rating instead
```

## Rider ATM tiers

```
MOTOGP ATM FRAMEWORK:

Tier 1 — Global icons (ATM 0.85-0.90):
  Marc Márquez era defined MotoGP commercial reach
  Current Tier 1: Márquez (if active), Francesco Bagnaia, Jorge Martín
  Characteristics: 5M+ social following; sponsor billboard faces; global recognition
  APS: 0.80+ — commercial identity transcends any single manufacturer

Tier 2 — Championship-level riders (ATM 0.70-0.82):
  Consistent podium contenders; multiple race wins
  Regional ATM boost: Spanish riders in Spain, Italian riders in Italy (especially Mugello)
  
Tier 3 — Race winners (ATM 0.55-0.68):
  Occasional winners; team narrative drivers
  
REGIONAL ATM MULTIPLIERS:
  Spanish rider at Circuit de Catalunya or Jerez: ATM × 1.25 (home crowd)
  Italian rider at Mugello: ATM × 1.30 (tifosi — most passionate MotoGP crowd)
  Japanese rider at Motegi or Twin Ring: ATM × 1.20
  Malaysian rider at Sepang: ATM × 1.15
  
  These regional ATM spikes are the MotoGP equivalent of a footballer
  playing in their home nation's colours.
```

## Circuit intelligence

```
MOTOGP CIRCUITS — SIGNAL PROFILES:

MUGELLO (Italy):
  Most passionate crowd in MotoGP — Italian tifosi (110k+ fans)
  Italian rider bonus: Bagnaia/Bastianini at Mugello = ATM × 1.30
  Manufacturer: Ducati home race (Italian); extra motivation signal
  Surface: Worn tarmac; high grip for experienced riders
  Signal modifier: × 1.12 for Italian riders / Ducati at Mugello

CIRCUIT DE CATALUNYA (Spain):
  Barcelonan crowd for Spanish riders — highly partisan
  Márquez/Martin at Catalunya: ATM × 1.25
  Technical circuit: balance between straight-line speed and cornering
  
SEPANG (Malaysia):
  High heat + humidity: apply heat modifier × 0.93 for non-Asian riders
  Wet season risk: afternoon thunderstorms common; wet race probability elevated
  Surface: Grippy; suits aggressive riding styles

MOTEGI (Japan):
  Technical stop-start circuit — high on electronics, lower on raw power
  Japanese riders + Japanese manufacturers (Honda, Yamaha, Suzuki): home signal
  Fan context: polite Japanese crowds; lower partisan noise
  
LE MANS (France):
  Variable weather: rain likely in May; wet specialist advantage
  High-speed section: straight-line speed matters
  French riders (Zarco, Quartararo heritage): ATM × 1.15

PHILLIP ISLAND (Australia):
  Most spectacular circuit — high-speed sweeping corners
  Southern Hemisphere: October race; spring in Australia
  Global reputation: often produces the best racing of the season
  Signal: late-season championship implications often active here
```

## The Márquez factor

```
MARC MÁRQUEZ — THE EXCEPTIONAL CASE:

Marc Márquez is the most commercially significant individual in MotoGP history.
His impact on the sport's commercial metrics during 2013-2023 was equivalent
to what Cristiano Ronaldo was to football or Lewis Hamilton to F1.

When Márquez is active (injury status is chronic — always check):
  Championship contention: × 1.20 narrative multiplier on all MotoGP signals
  Injury/absence: × 0.88 narrative deflation
  Return from injury: CDI event — Márquez return = commercial peak moment
  
  ATM: 0.88 (even post-peak injury period; brand is structural)
  APS: 0.82 (commercial value transcends any single manufacturer)
  
MANUFACTURER SWITCH (historical precedent — applies to any top rider change):
  When a Tier 1 rider switches manufacturer (Honda → Ducati, Yamaha → Aprilia):
  Previous manufacturer: −8 to −15% commercial impact (losing the face)
  New manufacturer: +10 to +18% (gaining the face + narrative)
  Apply immediately on confirmation, not on rumour.
```

## Crash risk intelligence

```
CRASH RISK MODEL:

MotoGP has the highest crash rate of any major motorsport.
Understanding crash probability is as important as understanding pace.

CRASH RISK FACTORS:
  Aggressive riding style rating (subjective + statistical):
    Conservative → 0.88 crash risk modifier
    Average → 1.00
    Aggressive → 1.15 crash risk modifier
    Very aggressive (Mir-era, early Márquez) → 1.30
    
  Wet surface crash multiplier:
    All riders: crash probability × 1.40 in wet vs dry
    Wet specialists: × 1.15 (better wet riders crash less, but still more than dry)
    
  First lap crash rate:
    Some riders have elevated first-lap crash history
    Apply first_lap_risk_flag when historic first-lap DNF rate > 15%
    
  Championship pressure effect:
    Leader with large gap (> 50pts, 5+ races left): conservative modifier × 0.90
    Leader with narrow gap (< 25pts, last 5 races): pressure modifier × 1.10
    Trailing rider must win: desperation modifier × 1.25

CRASH RISK IN SIGNAL OUTPUT:
  Always include in key_risks for any MotoGP analysis
  crash_risk_elevated flag when composite crash modifier > 1.20
  Position size: × 0.80 when crash_risk_elevated is active
```

## Championship battle intelligence

```
MOTOGP CHAMPIONSHIP SIGNAL CALENDAR:

SEASON START (Qatar, March):
  First race gives hardware snapshot — who has winter testing advantage
  Apply: 30% confidence on first-race hardware tiers (small sample)
  
PRE-SUMMER BREAK (after ~8 races):
  Championship standings define narrative arc for rest of season
  Gap > 50 points: leader enters conservative phase
  Gap < 25 points: title fight narrative maximally active
  
FINAL 5 RACES:
  Championship decider applies maximum signal weight
  Title decided at race: × 1.25 NCSI for winner's manufacturer token
  
SEASON FINALE (Valencia, November typically):
  Multiple outcomes possible until final lap: apply × 1.20 signal weight
  If title decides at Valencia: maximum CDI event for championship winner
```

## Integration: Full MotoGP pre-race workflow

```
Step 1: Load domain context
  Load sports/motogp/sport-domain-motogp.md

Step 2: Hardware check FIRST
  get_manufacturer_tier — factory or satellite?
  
Step 3: Weather forecast
  Rain > 40%? → wet race hardware RESET; use wet_weather_rating
  
Step 4: Circuit-specific check
  get_circuit_history — win% and podium% at this track
  Italian rider at Mugello? → ATM × 1.30
  
Step 5: Crash risk assessment
  get_crash_risk — is crash risk elevated for this rider?
  If crash_risk_elevated: position_size × 0.80
  
Step 6: Qualifying position (Saturday signal)
  get_qualifying_position — grid position as primary signal
  Front row start: + signal; 5+ rows back: negative modifier
  
Step 7: Composite modifier
  get_athlete_signal_modifier (hardware × circuit × wet × crash × qualifying)
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "rider": "string",
  "manufacturer": "string",
  "manufacturer_tier": "Factory Tier 1",
  "grid_position": 3,
  "qualifying_modifier": 1.05,
  "circuit_history_modifier": 1.08,
  "wet_weather_modifier": 1.00,
  "crash_risk_modifier": 1.00,
  "composite_modifier": 1.10,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["First-lap crash rate elevated at this circuit"],
  "modifier_reason": "Factory Tier 1 hardware; front row start; good circuit history"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `manufacturer_tier_modifier` | `get_manufacturer_tier` | 0.90–1.10 |
| `qualifying_modifier` | `get_qualifying_position` | 0.85–1.15 |
| `wet_weather_modifier` | Weather + `get_wet_weather_rating` | 0.75–1.20 |
| `circuit_history_modifier` | `get_circuit_history` | 0.88–1.18 |
| `crash_risk_modifier` | `get_crash_risk` | 0.88–1.30 |
| `regional_atm_modifier` | Regional crowd + rider nationality | 1.00–1.30 |
| `composite_modifier` | Product of all applicable | 0.65–1.35 |


*MIT License · SportMind · sportmind.dev*
