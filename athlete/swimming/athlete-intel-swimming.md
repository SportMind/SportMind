# Swimming — Athlete Intelligence

Player-level intelligence for swimming predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** Olympic and World Championship prediction markets

---

## Overview

Swimming athlete intelligence centres on how close an athlete is to their personal best and whether they are optimally tapered for this event. Olympic swimmers peak-taper once or twice per cycle; multiple swims per day require fatigue management.

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

Master composite modifier for Swimming. Combines availability, form, and sport-specific variables.

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
  "modifier_reason": "Event PB proximity and taper timing is the primary driver"
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

### Swimming pre-event workflow

```
# Step 1: Load domain context
Load sports/swimming/sport-domain-swimming.md

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

**L1 domain:** `sports/swimming/sport-domain-swimming.md`
**L4 market:** `market/market-swimming.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_taper_status` | Is athlete in taper phase? Peak-taper timing model | Yes |
| `get_pb_proximity` | Current form vs personal best — primary signal | Yes |
| `get_event_specialisation` | Stroke and distance specialist profile | Yes |
| `get_multi_swim_fatigue` | Heats → semi → final fatigue accumulation | Yes |
| `get_championship_record` | Olympics/Worlds performance vs regular meets | Yes |
| `get_athlete_signal_modifier` | Composite swimming modifier | Yes |

---

## Taper and peak performance model

```
TAPER IS THE PRIMARY SIGNAL IN COMPETITIVE SWIMMING:

Elite swimmers train at extreme volume for months, then taper (reduce volume)
for 2-4 weeks before major championships. A correctly tapered swimmer can be
significantly faster than their season form suggests.

TAPER STATUS:
  Peak taper (1-3 days before championship final): × 1.15
    Best times come at championships, not training meets
  
  In taper (1-2 weeks before): × 1.05
    Reducing load; energy recovering
    
  Post-meet fatigue (within 5 days of major meet): × 0.90
    Multiple races deplete physical reserves
    
  Mid-season training load: × 0.92
    Not rested for competition; performances are training signals only

IDENTIFYING TAPER STATUS:
  Championships and Olympics: assume all competitors are fully tapered
  World Series/Diamond League meets: check if this is peak or preparation
  
  KEY RULE: At the Olympics and World Championships, taper baseline applies
  to ALL athletes. The signal differentiation comes from PB proximity and
  event-specific form, not taper (everyone is tapered).

SEASON BEST vs PB:
  Olympics/Worlds: compare season best to all-time PB
  If season best is within 0.5% of PB: peak form signal × 1.12
  If season best is 1-2% below PB: normal championship form × 1.00
  If season best is 3%+ below PB: possible form concern × 0.93
```

## Event specialisation framework

```
SWIMMING STROKES AND DISTANCES — SIGNAL PROFILES:

SPRINT EVENTS (50m, 100m):
  Reaction time component: off-the-blocks reaction measurable
  Weather/temperature: 26-28°C pool optimal; cold slows performance × 0.98
  Technique: underwater dolphin kicks in 50m backstroke/butterfly = critical
  Primary signal: season best relative to PB (no tactical element)
  
MIDDLE DISTANCE (200m, 400m):
  Pacing strategy matters: even vs negative split
  Endurance component grows; lactate threshold relevant
  Primary signal: split times in heats (reveals pacing and form)
  
LONG DISTANCE (800m, 1500m):
  Primarily freestyle
  Tactical element: drafting, positioning
  Open water (10km): weather, current, sighting strategy all relevant
  Primary signal: race management history at championships

INDIVIDUAL MEDLEY (200m, 400m):
  All four strokes: weakness in one stroke = overall vulnerability
  Backstroke-to-breaststroke transition: technically critical
  Primary signal: weakest stroke's recent form

RELAY EVENTS:
  Team composition matters more than any individual
  Exchange times: well-rehearsed relays faster than individual best × 4
  National pride: relay events often produce above-PB individual legs
  Signal: team composition + relay exchange training history
```

## Olympic cycle intelligence

```
OLYMPIC GAMES — THE PEAK COMMERCIAL WINDOW FOR SWIMMING:

Swimming has more Olympic medals than any other sport.
The commercial window is therefore the longest sustained multi-athlete signal.

Olympic swimming schedule (typically 9 days):
  Day 1-3: Sprint and medley events (highest commercial ATM per day)
  Day 4-6: Middle distance, backstroke
  Day 7-9: Long distance, relays

NATIONAL ATM MULTIPLIERS:
  Australia: × 1.20 (dominant swimming nation; public engagement very high)
  USA: × 1.18 (team depth + commercial market)
  Hungary: × 1.15 (Budapest swimming culture; Katinka Hosszú era)
  China: × 1.15 (post-2008 surge; state programme)
  
RECORD-BREAKING AS SIGNAL:
  World record at Olympics: maximum ATM event for swimmer and nation
  Olympic record (not world): elevated but smaller than WR
  
  Token signal (if swimming tokens exist):
  World record = CDI × 1.80 (record lasts forever; narrative permanent)
  Olympic gold without record: CDI × 1.20

MULTI-EVENT STAR (Phelps/Ledecky model):
  Swimmer competing in 4+ events over 9 days
  Day 1 performance signal for later events
  Fatigue accumulates: apply × 0.96 per additional event day beyond Day 3
```

## Integration: Full swimming pre-event workflow

```
Step 1: Load domain context
  Load sports/swimming/sport-domain-swimming.md

Step 2: Taper status FIRST
  get_taper_status — is this athlete peak-tapered for this meet?
  Championships: assume all tapered; differentiate on PB proximity

Step 3: PB proximity
  get_pb_proximity — season best vs all-time PB
  Within 0.5%: × 1.12; 3%+ below: × 0.93

Step 4: Event specialisation check
  get_event_specialisation — is this their primary event?
  Secondary event (e.g. 100m backstroke for 200m specialist): × 0.92

Step 5: Multi-swim fatigue
  get_multi_swim_fatigue — heats + semi in last 24h?
  Two previous swims: × 0.95; three+: × 0.90

Step 6: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`
```json
{
  "athlete": "string",
  "event": "100m_freestyle|200m_butterfly|400m_IM|etc",
  "taper_modifier": 1.15,
  "pb_proximity_modifier": 1.08,
  "fatigue_modifier": 0.95,
  "event_specialist_modifier": 1.00,
  "composite_modifier": 1.12,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Heats and semi-final already swum today"],
  "modifier_reason": "Peak taper, strong PB proximity, primary event specialist"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `taper_modifier` | `get_taper_status` | 0.90–1.15 |
| `pb_proximity_modifier` | `get_pb_proximity` | 0.93–1.12 |
| `fatigue_modifier` | `get_multi_swim_fatigue` | 0.88–1.00 |
| `event_modifier` | `get_event_specialisation` | 0.92–1.08 |
| `composite_modifier` | Product of all applicable | 0.78–1.25 |


*MIT License · SportMind · sportmind.dev*
