# Athletics Athlete Intelligence — SportMind Skill

Player-level intelligence for athletics fan tokens and prediction markets.
Covers sprints, middle distance, long distance, jumps, throws, hurdles, and combined events.

**Applicable tokens / markets:** Individual athlete tokens, championship final markets, world record prediction markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_athlete_form_score` | Season form based on recent times/distances vs personal bests | Yes |
| `get_seasonal_peak` | Is athlete peaking for target event or in off-form phase | Yes |
| `get_world_record_proximity` | How close to world record — record attempt probability | Yes |
| `get_multi_round_fitness` | Multi-day fatigue assessment for heats→semi→final schedule | Yes |
| `get_doping_status` | WADA / AIU clearance check | Yes |
| `get_conditions_fit` | Wind, altitude, temperature adjustment | Yes |
| `get_athlete_signal_modifier` | Composite athletics modifier | Yes |

---

## Command reference

### `get_athlete_form_score`

**Parameters:**
- `athlete_name` (required)
- `discipline` (required) — e.g. `"100m"`, `"400m_hurdles"`, `"long_jump"`, `"shot_put"`
- `events` (optional, default: season-to-date)

**Returns:**
```json
{
  "athlete": "Mondo Duplantis",
  "discipline": "pole_vault",
  "form_score": 97,
  "form_label": "DOMINANT",
  "season_best": "6.27m",
  "personal_best": "6.27m (WR)",
  "world_record_holder": true,
  "season_results": [
    { "event": "Brussels DL", "result": "6.25m", "place": 1 },
    { "event": "Zurich DL", "result": "6.22m", "place": 1 },
    { "event": "Oslo DL", "result": "6.27m WR", "place": 1 }
  ],
  "wins_this_season": 12,
  "form_modifier": 1.22
}
```

### `get_world_record_proximity`

**Parameters:**
- `athlete_name` (required)
- `discipline` (required)

**Returns:**
```json
{
  "athlete": "Sydney McLaughlin-Levrone",
  "discipline": "400m_hurdles",
  "current_world_record": "50.65s",
  "athlete_personal_best": "50.68s",
  "gap_to_record_pct": 0.06,
  "record_proximity_label": "IMMINENT",
  "record_attempt_probability": 0.72,
  "conditions_required": "< +1.0 wind, sea level or below, championship final pressure",
  "wr_modifier": 1.20,
  "note": "Within 0.06% of world record — any championship final is a record attempt event"
}
```

### `get_doping_status`

**Parameters:**
- `athlete_name` (required)

**Returns:**
```json
{
  "athlete": "Marcell Jacobs",
  "wada_status": "CLEARED",
  "aiu_status": "CLEARED",
  "last_tested": "2026-03-01",
  "historical_flags": [],
  "doping_risk_label": "LOW",
  "doping_modifier": 1.00,
  "note": "Clean record — no historical flags"
}
```

**CRITICAL:** If `wada_status` or `aiu_status` is anything other than `CLEARED`, the composite modifier floors at 0.50 and the recommendation is EXIT.

### `get_multi_round_fitness`

**Parameters:**
- `athlete_name` (required)
- `schedule` (required) — array of round dates e.g. `["Day1_heat", "Day2_semi", "Day3_final"]`

**Returns:**
```json
{
  "athlete": "Noah Lyles",
  "events_entered": ["100m", "200m", "4x100m_relay"],
  "total_rounds": 9,
  "fatigue_risk": "HIGH",
  "fatigue_label": "THREE_EVENT_STACK",
  "expected_performance_drop": {
    "100m_final": "0.01–0.03s slower than season best",
    "200m_final": "0.05–0.10s slower",
    "relay": "minimal — short burst"
  },
  "fatigue_modifier": 0.92,
  "recommendation": "Multi-event stack reduces form ceiling — adjust expectations for later events"
}
```

### `get_athlete_signal_modifier`

**Parameters:**
- `athlete_name` (required)
- `event` (required) — `"Olympic_final"`, `"World_Champs_final"`, `"DL_meeting"` etc.
- `discipline` (required)

**Returns:**
```json
{
  "athlete": "Mondo Duplantis",
  "event": "Olympic_final",
  "discipline": "pole_vault",
  "base_signal_score": 75,
  "composite_modifier": 1.28,
  "adjusted_signal_score": 96,
  "modifier_breakdown": {
    "form": 1.22,
    "world_record_proximity": 1.20,
    "doping_status": 1.00,
    "multi_round_fitness": 1.00,
    "conditions_fit": 1.05
  },
  "confidence": 0.92,
  "recommendation": "MAXIMUM CONVICTION — dominant world record holder in a single-discipline event with no meaningful competition. Olympic final is near-certain gold.",
  "key_risks": ["Equipment failure (pole)", "Wind conditions on night", "Ankle/leg injury risk on warm-up"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| World record holder, DOMINANT form | ×1.22 |
| Within 0.1% of world record | ×1.18 |
| Qualified for Olympic / World Champs final | ×1.12 |
| CLEARED doping status, no flags | ×1.00 |
| Multi-event athlete (3+ events, Olympics) | ×0.92 |
| Heat exit (did not qualify for final) | ×0.00 — exit signal |
| Provisional doping suspension | ×0.50 — strong exit |
| Confirmed doping ban | ×0.00 — full exit |


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_personal_best_context` | PB vs current form gap — primary signal | Yes |
| `get_championship_record` | Major championships (Olympics/Worlds) performance | Yes |
| `get_season_peak_timing` | Is athlete in peak form for this competition? | Yes |
| `get_event_specialisation` | Track: distance, hurdles, jumps, throws | Yes |
| `get_doping_clearance` | WADA/AIU clearance status | Yes |
| `get_athlete_signal_modifier` | Composite athletics modifier | Yes |

---

## The personal best model

```
PERSONAL BEST (PB) is the primary athletics signal.

Unlike team sports where current form matters more than historical peak,
athletics performances are directly comparable to historical records.
The gap between an athlete's PB and their recent performances indicates
where they are in their seasonal curve.

PB PROXIMITY MODEL:
  Recent performance within 0.5% of PB: PEAK FORM — × 1.15
  Within 1.0% of PB: very good form — × 1.08
  Within 2.0% of PB: good form — × 1.03
  Within 3.5% of PB: average form — × 1.00
  More than 3.5% below PB: below par — × 0.92
  
  NOTE: This model applies differently by event type:
  Sprint events (100m, 200m): 0.2% PB gap = significant difference
  Distance events (5000m, marathon): 2% PB gap = acceptable variation
  Calibrate the threshold by event type.
  
SEASONAL BEST vs ALL-TIME PB:
  First year athlete running SB = PB: form trajectory positive
  Veteran athlete significantly below career PB: natural decline signal
  Apply: career trajectory modifier for athletes > 30 in sprint events
```

## Event specialisation framework

```
TRACK EVENTS:

SPRINTS (60m, 100m, 200m):
  Reaction time is a component (especially 100m)
  Wind assistance: if > +2.0 m/s: performance does not count for records
  Temperature: optimal ~20-25°C; cold reduces sprint performance × 0.98
  Lane draw: outer lanes (7-8) can be slight disadvantage in 200m (curve)
  
MIDDLE DISTANCE (400m, 800m, 1500m):
  Tactical racing: position at final bend is critical
  Kicking ability (final 200m): strong finishers modifier × 1.06
  Pacing judgement: 400m hurdles requires even pacing; poor pacing = × 0.92
  
DISTANCE (5000m, 10000m, marathon, steeplechase):
  Weather is significant: ideal marathon conditions 10-15°C, no wind
  Heat: marathon in > 25°C: all times 2-4% slower; form modifier × 0.95
  Elevation: high altitude races: sea-level athletes × 0.94
  Course profile: "fast course" (flat, closed-loop) vs "hard course" (hills)
  
HURDLES (110mH, 100mH, 400mH):
  Clearance technique is a separate component from sprint speed
  "Clipping" hurdles: each hurdle touched adds ~0.05-0.10s
  Dominant hurdlers with clean technique: × 1.08

FIELD EVENTS:

HIGH JUMP / POLE VAULT:
  Conditions: wind is critical for pole vault; no wind threshold
  Psychological: bar height as pressure signal
  Medal competition order: athletes reach personal limits late in competition
  
LONG JUMP / TRIPLE JUMP:
  Wind assistance: same rule as sprints (max +2.0 m/s for records)
  Approach run quality: significant variance possible
  
THROWS (shot put, discus, hammer, javelin):
  Weather: wind for javelin and discus is a significant modifier
  Technical consistency: throws athletes often show high variance
```

## Championship vs Diamond League intelligence

```
CHAMPIONSHIP VS CIRCUIT PERFORMANCE:

Olympics and World Championships are different from Diamond League meets.
Athletes peak specifically for championship years. Circuit form does not
always predict championship performance.

CHAMPIONSHIP YEAR SIGNALS:
  Olympic/World Championships year: athletes "save" peak performances
  Early season performances in championship year may be deliberately conservative
  Apply: championship_year_modifier × 1.05 for athletes with championship history
  
  Defending champion: × 1.08 (knows championship pressure; proven performer)
  First championship final: × 0.94 (unknown pressure response)

DIAMOND LEAGUE (Pre-championship circuit):
  High quality but not championship pressure
  Using DL performances to predict championships: × 0.92 reliability
  (Athletes often hold back in DL to peak at championships)

OLYMPICS SPECIFICITY:
  Once-in-4-years significance amplifies every signal
  Personal narrative (national pride, career culmination): × 1.10 narrative modifier
  First Olympics for young athlete: maximum uncertainty; wide confidence interval
  
WORLD CHAMPIONSHIPS (biennial):
  High quality; championship pressure; more predictable than Olympics
  Defending world champion: × 1.08 (proven championship performer)
```

## ATM framework for athletics

```
ATHLETICS ATM TIERS:

Tier 1 — Global icons (Bolt, Kipchoge tier currently active):
  ATM 0.85-0.92; transcend the sport; global recognition
  Usain Bolt-era: maximum ATM in history of athletics
  Eliud Kipchoge (marathon legend): ATM 0.82 sustained post-peak
  
Tier 2 — World record holders and Olympic champions:
  ATM 0.65-0.78; highly recognised in running community
  
Tier 3 — World Championship medallists:
  ATM 0.45-0.60; known to athletics fans

NATIONAL NARRATIVE:
  Jamaica sprint legacy: Jamaican sprinters have ATM × 1.20 at home events
  Ethiopia/Kenya distance runners: enormous pride signal at home events
  USA track and field: high commercial value at US events (Penn Relays, etc.)
```

## Command reference

### `get_athlete_signal_modifier`

```json
{
  "athlete": "string",
  "event": "100m|marathon|high_jump|etc",
  "pb_proximity_modifier": 1.08,
  "championship_context_modifier": 1.05,
  "conditions_modifier": 1.00,
  "composite_modifier": 1.09,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["Wind conditions marginal — check forecast at T-2h"],
  "modifier_reason": "Within 0.8% of PB; defending champion; optimal conditions"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `pb_proximity_modifier` | `get_personal_best_context` | 0.92–1.15 |
| `championship_modifier` | `get_championship_record` | 0.94–1.10 |
| `conditions_modifier` | `get_season_peak_timing` + weather | 0.92–1.08 |
| `event_specific_modifier` | `get_event_specialisation` | 0.90–1.12 |
| `composite_modifier` | Product of all applicable | 0.78–1.25 |


---

## Integration example

### Athletics pre-competition workflow

```
# Step 1: Load domain context
Load sports/athletics/sport-domain-athletics.md

# Step 2: PB proximity check FIRST
get_personal_best_context — recent performance vs career PB
Within 0.5% of PB → PEAK FORM ×1.15

# Step 3: Championship context
get_championship_record — defending champion or first final?
Defending champion: ×1.08

# Step 4: Conditions check
get_season_peak_timing — is this a championship year?
Weather: heat >25°C for marathon/distance → ×0.95

# Step 5: Event specialisation
get_event_specialisation — sprints need wind/temperature check;
throws need wind direction; hurdles need technical form check

# Step 6: Composite modifier
get_athlete_signal_modifier
```

**See:** `core/confidence-output-schema.md` for full output format.


*MIT License · SportMind · sportmind.dev*
