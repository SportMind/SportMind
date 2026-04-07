# Winter Sports — Athlete Intelligence

Player-level intelligence for winter-sports predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** Olympic prediction markets; Crystal Globe tracking

---

## Overview

Winter sports athlete intelligence requires course-specific assessment. Alpine skiing: gate technique matches course profile. Cross-country: endurance pacing. Ski jumping: wind conditions are binary. Olympic cycle is the primary commercial window.

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

Master composite modifier for Winter Sports. Combines availability, form, and sport-specific variables.

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
  "modifier_reason": "Course fit and snow conditions is the primary driver"
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

### Winter Sports pre-event workflow

```
# Step 1: Load domain context
Load sports/winter-sports/sport-domain-winter-sports.md

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

**L1 domain:** `sports/winter-sports/sport-domain-winter-sports.md`
**L4 market:** `market/market-winter-sports.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_course_specialisation` | Downhill/slalom/GS/super-G/cross-country specialist profile | Yes |
| `get_snow_conditions_modifier` | Course conditions: packed/icy/soft/variable | Yes |
| `get_wind_conditions` | Ski jumping wind hold rule; alpine wind impact | Yes |
| `get_crystal_globe_context` | Season standings — championship pressure signal | Yes |
| `get_olympic_context` | Olympic cycle position; four-year narrative | Yes |
| `get_athlete_signal_modifier` | Composite winter sports modifier | Yes |

---

## Alpine skiing discipline framework

```
ALPINE SKIING HAS FOUR DISTINCT DISCIPLINES — different signals for each:

DOWNHILL (DH):
  Highest speed; longest course; most dangerous
  Course inspection is critical — racers who inspect more thoroughly know
  where to carry speed vs where to be cautious
  
  Primary signal: gate technique matches course profile
  Start position in women's/men's DH: higher bib number = slower grooves
  (course deteriorates; first 15 starters generally faster)
  
  Bib order modifier:
    Bibs 1-15: × 1.05 (fresh snow surface)
    Bibs 16-30: × 1.00 (moderate wear)
    Bibs 31+: × 0.93 (significantly rutted course)
    Snow forecast refresh: if snow between runs, modifier resets
    
  Specialist indicator: top-5 DH ranking on World Cup circuit

SLALOM (SL):
  Two runs; highest gate count; most technical
  First run DNF is common (crash or miss gate)
  Top-15 after Run 1 reverses starting order for Run 2
  
  Primary signal: technical precision score (gate success rate in recent races)
  
GIANT SLALOM (GS):
  Two runs; middle ground between DH and SL
  Course is set fresh for each run: Run 2 form is independent of Run 1 conditions
  
SUPER-G (SG):
  One run; combines DH speed with SL technical gates
  No second chance: highest variance per race of all disciplines
  Primary signal: DH speed + SL precision combined

COMBINED / SUPER COMBINED:
  DH run + SL run; separate specialist advantage
  Versatile skiers (strong in both): large advantage
  Specialist weakness exposed: opponent can target
```

## Ski jumping and Nordic intelligence

```
SKI JUMPING:

Wind hold rule: competitions are suspended if wind is unfavourable
This is the most important variable in ski jumping — more than athlete form.

Wind monitoring:
  Head wind: beneficial (lift); most competitions require minimum head wind
  Tail wind: disadvantageous; competition suspended or gated compensated
  Changing conditions between jumpers: unfair advantage or disadvantage
  
  If wind conditions variable during competition:
    First jumpers in variable wind: high variance signal → widen confidence interval
    Competition with stable head wind: standard form-based signal applies
  
  Gate adjustments: jumps from lower gates (fewer metres available) = compensated
  in the points system; not a direct signal but affects comparison between jumpers

PRIMARY SIGNAL: take-off technique + in-flight position
  Clean take-off: launch angle precise → distance and points maximised
  Poor take-off: common in high-pressure competitions; crash risk elevated

CROSS-COUNTRY SKIING:
  Mass start, pursuit, interval start, skiathlon — different tactics per format
  
  Interval start: pure time trial; form vs PB model (same as athletics/swimming)
  Mass start: tactical; positioning in pack for final sprint
  Pursuit: starting from prior time gap; psychology of leading vs chasing
  
  Snow condition is critical: wax selection for temperature and snow type
  Bad wax choice: × 0.85 regardless of athlete form
  
BIATHLON:
  Cross-country skiing + rifle shooting (5 targets per stage)
  Miss rate: each missed shot = 1-minute penalty or extra loop
  Shooting range pressure: heart rate must drop quickly from skiing to shooting
  
  Primary signal: shooting accuracy under fatigue (last range = under most fatigue)
  Recent miss rate: > 1.0 misses per range (average) = significant disadvantage
  Clean shoot rate (all 5 targets hit): × 1.12 per clean range
```

## Olympic cycle and Crystal Globe intelligence

```
CRYSTAL GLOBE (Overall World Cup standings):
  Awarded to leader in each discipline's season-long standings
  Athletes leading Crystal Globe with < 10 races remaining: maximum motivation
  Apply: Crystal_Globe_pressure_modifier × 1.08 (proven winners protect leads)

FOUR-YEAR OLYMPIC CYCLE:
  Winter Olympics = peak commercial window for alpine and Nordic skiing
  
  Olympic year signals:
    Athletes "saving" peak form for Olympics: season form may understate potential
    Apply: championship_year_modifier × 1.05 for athletes with Olympic history
    
  Olympic gold narrative:
    First Olympic gold in iconic event (Downhill, 10km cross-country): maximum CDI
    CDI = 45 (trophy) × 2.00 (Olympic tier) = 90 days commercial window
    Defending Olympic champion: × 1.10 pressure and narrative modifier

ATM TIERS FOR WINTER SPORTS:
  Tier 1 (Global icons): Marcel Hirscher era; Mikaela Shiffrin, Lindsey Vonn
    ATM 0.75-0.82; recognised beyond skiing community
  Tier 2 (Multiple globe winners):
    ATM 0.60-0.72; well-known in skiing markets (Austria, Switzerland, Norway)
  National ATM premium:
    Austrian skier in Austria: × 1.30 (skiing is national religion)
    Norwegian cross-country skier in Norway: × 1.35 (cross-country identity)
    Swiss skier in Wengen/St Moritz: × 1.25 (home circuit)
```

## Integration: Full winter sports pre-event workflow

```
Step 1: Load domain context
  Load sports/winter-sports/sport-domain-winter-sports.md

Step 2: Discipline classification FIRST
  Downhill, Slalom, GS, Super-G, Ski Jump, Cross-country, Biathlon?
  Each has a different primary signal variable

Step 3: Conditions check
  get_snow_conditions_modifier — course type and conditions
  get_wind_conditions — especially critical for ski jumping
  If ski jumping: wind variable = widen confidence interval significantly

Step 4: Starting bib/position
  Downhill: bib 1-15 significantly advantaged
  Slalom Run 2: top-15 start reversed (leaders start last)
  
Step 5: Course specialist check
  get_course_specialisation — is this athlete a specialist at this venue?
  Home circuit (Wengen, Kitzbühel, etc.) = × 1.15-1.30 for home-nation athletes

Step 6: Olympic/Crystal Globe context
  get_crystal_globe_context — title pressure or defending
  get_olympic_context — Olympic year championship modifier

Step 7: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`
```json
{
  "athlete": "string",
  "discipline": "downhill|slalom|giant_slalom|ski_jump|cross_country|biathlon",
  "conditions_modifier": 1.03,
  "bib_modifier": 1.05,
  "specialist_modifier": 1.08,
  "crystal_globe_modifier": 1.00,
  "composite_modifier": 1.10,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Wind conditions variable for ski jumping segment"],
  "modifier_reason": "Specialist at this course type; fresh bib; clean conditions"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `conditions_modifier` | `get_snow_conditions_modifier` | 0.88–1.08 |
| `wind_modifier` | `get_wind_conditions` | 0.70–1.10 |
| `bib_modifier` | Starting order | 0.93–1.05 |
| `specialist_modifier` | `get_course_specialisation` | 0.90–1.30 |
| `olympic_modifier` | `get_olympic_context` | 1.00–1.10 |
| `composite_modifier` | Product of all applicable | 0.70–1.30 |


*MIT License · SportMind · sportmind.dev*
