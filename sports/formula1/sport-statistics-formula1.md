# Formula 1 Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-formula1.md`. Load alongside
the main domain skill when qualifying and race data are available.
Highest statistical signal value of any sport in the calibrated library:
qualifying delta already validated 4/4 in SportMind calibration records.

Zero-dependency: agents source data from Ergast API (free) or their
chosen provider. See Data Sources.

---

## Overview

Formula 1 is the most statistics-rich motorsport in the world.
Every lap, every sector, every tyre compound generates machine-precision data.
For fan token signal purposes, three statistics dominate all others:

1. **Qualifying delta** — the single most predictive F1 statistic
2. **Tyre compound degradation rates** — race strategy signal
3. **Sector time analysis** — circuit-type advantage prediction

Load `core/match-statistics-intelligence.md` for universal modifier framework.

---

## Domain Model

### Statistics hierarchy for F1 signal impact

```
TIER 1 — OUTCOME-CORRELATED (apply as primary modifiers):

  QUALIFYING POSITION DELTA:
    The 0.3 second qualifying advantage finding is SportMind-calibrated (4/4 ✓).
    A 0.3s+ gap over the next competitor on low-downforce circuits predicts
    race outcomes at a higher rate than season championship standing.
    
    Signal threshold calibration:
      > 0.5s advantage:   × 1.18 signal modifier (dominant qualifying)
      0.3–0.5s advantage: × 1.12 (strong qualifying — calibrated threshold)
      0.1–0.3s advantage: × 1.06 (marginal advantage)
      < 0.1s / grid mix:  × 1.00 (neutral — race variables dominate)
      Behind by > 0.3s:   × 0.90 (qualified behind expectation)
      Behind by > 0.5s:   × 0.85 (significant underperformance)
    
    CIRCUIT TYPE MODIFIER on qualifying delta:
      Low-downforce high-speed circuits (Monza, Spa, Silverstone):
        Qualifying delta is most predictive here. Apply ×1.15 to the above.
      High-downforce street circuits (Monaco, Singapore, Baku):
        Track position is critical; overtaking near-impossible.
        Apply ×1.20 to qualifying advantage (pole is most valuable here).
      Mixed circuits (Barcelona, Suzuka, COTA):
        Standard qualifying delta weights. No circuit modifier.
      Temporary circuits or new layouts:
        Reduce qualifying delta modifier by ×0.85 (setup uncertainty higher).

  CHAMPIONSHIP POSITION PRESSURE:
    Leader defending within 25 points of end of season: × 1.08 (urgency signal)
    Leader with > 50 point margin at season end: × 0.92 (reduced urgency)
    Constructor championship race active: multiplies team token signals

TIER 2 — CONTEXTUAL STATISTICS:

  RACE PACE DIFFERENTIAL (last 3 races):
    Race pace vs qualifying pace delta. A team fast in race but slow in qualifying
    is categorically different to the reverse.
    Strong race pace + weak qualifying: underestimated — apply × 1.06
    Strong qualifying + weak race pace: overpriced — apply × 0.94

  FREE PRACTICE PACE:
    FP1–FP3 gap to P1: < 0.3s = strong race weekend probability
    FP mileage on new package (new floor, new sidepod): unreliable modifier × 0.85
    Note: teams deliberately sandbag in practice — treat as directional only

TIER 3 — CONTEXTUAL INDICATORS:
  Pitstop time reliability (mechanical risk indicator — use to confirm, not signal)
  Lap times in wet vs dry conditions (circuit-specific confirmation only)
  Overtaking attempts (narrative indicator for social sentiment, not outcome)
```

### Tyre compound intelligence

```
TYRE COMPOUND SIGNAL FRAMEWORK:

  Tyre strategy is F1's primary race variable — more decisive than race pace
  in 40–55% of races (based on strategy analyst consensus).

  COMPOUND PERFORMANCE WINDOW:
    Soft compound: 20–30 lap optimal window (varies by circuit temperature)
    Medium compound: 30–45 laps
    Hard compound: 45+ laps but slower initial pace
    
  STRATEGIC ADVANTAGE SIGNAL:
    Team starting on soft compound when leader starts on medium at circuit
    where undercut works (< 3s pitstop loss threshold): × 1.08 race signal
    
    Team with demonstrably superior tyre management (based on last 3 races
    at similar compound thermal demand circuits): × 1.06
    
    Team with documented tyre cliff vulnerability (last 3 races showing
    > 0.8s/lap degradation beyond competitor): × 0.92
    
  TEMPERATURE CONDITIONS MODIFIER:
    Track temp > 45°C: reduces soft compound window by 20–30%. Benefit
    teams with harder compound preference. Increases strategic variability.
    Apply × 0.90 confidence modifier on pre-race tyre predictions if
    temperature uncertainty is high (weather forecast variance > 10°C).
    
  RAIN TYRE SIGNAL:
    Wet weather in qualifying: removes qualifying delta signal entirely.
    Apply × 0.50 to all qualifying-based modifiers.
    Teams with documented wet weather strength (Hamilton, Verstappen era):
    apply × 1.15 to their expected race outcome in mixed conditions.
```

### Sector time analysis

```
SECTOR TIME FRAMEWORK:

  F1 circuits divide into three sectors. A team's sector advantage indicates
  where their car is strongest — and therefore which circuit types suit them.

  SECTOR ADVANTAGE → CIRCUIT TYPE MATCH:
    Sector 1 advantage (typically high-speed entry or long straight):
      Predicts advantage at Monza, Spa, Bahrain (power circuits)
    Sector 2 advantage (typically technical, chicane, varied corners):
      Predicts advantage at Suzuka, Barcelona (all-around circuits)
    Sector 3 advantage (typically stadium section or hairpin-heavy):
      Predicts advantage at Monaco, Singapore, Baku (street circuits)
    
  PREDICTIVE APPLICATION:
    If a team has Sector 1 advantage at previous power circuit AND upcoming
    race is also a power circuit: × 1.06 compound circuit-match signal.
    
    If team has documented weakness in specific corner type (slow-speed
    corners, high-energy corners) AND upcoming circuit is dominated by that
    corner type: × 0.92 circuit-mismatch signal.

QUALIFYING SIMULATION GAPS (FP2):
  Many teams run race-representative tyre simulation in FP2.
  FP2 long-run pace on medium compound:
    < 0.3s/lap behind leader: race-competitive
    0.3–0.6s/lap: midfield risk
    > 0.6s/lap: significant race pace deficit — apply × 0.88 race signal
```

### Historical statistics — F1 specific

```
RELIABILITY HISTORY:
  DNF rate per season (engine, gearbox, hydraulics failures):
    < 1 DNF per season: low mechanical risk, neutral modifier
    2–3 DNFs per season: elevated risk, × 0.93 long-race signal
    > 3 DNFs per season: high risk, × 0.88 signal for race outcome

  CIRCUIT-SPECIFIC HISTORY (same regulations era):
    F1 regulations change significantly every 2–4 years.
    Circuit history is valid only within the same regulation era.
    Cross-era circuit history: 0× weight (car characteristics too different).

  TEAMMATE COMPARISON (same car):
    When two drivers share the same car, their relative qualifying and race
    performance eliminates car-level variables.
    Consistent qualifying gap (same team, 5+ races): reliable individual metric.
    Apply teammate gap as modifier to individual driver signal.
    Example: Driver A qualifies 0.25s ahead of Driver B consistently.
    Both reach same circuit — Driver A gets × 1.06 individual signal.
```

---

## Event Playbooks

### Playbook 1: Qualifying — immediate signal generation
```
trigger:  Qualifying session complete
timing:   Immediately post-qualifying (within 15 min)
protocol:
  1. Calculate qualifying delta: P1 time vs P2, P3, etc.
  2. Apply circuit type modifier to qualifying delta
  3. Check tyre compound strategy declared for race start
  4. Check weather forecast for race day — wet reduces qualifying signal
  5. Generate updated signal with qualifying_delta and circuit_type noted
output:   Updated signal replacing or modifying pre-weekend signal
note:     Qualifying is the highest signal-refresh point in any F1 weekend
```

### Playbook 2: Tyre strategy signal — race day
```
trigger:  Starting grid and tyre compounds confirmed (T-2h race start)
timing:   Race day morning after warm-up / final press conference
protocol:
  1. Map all cars' starting compounds
  2. Identify strategic undercut/overcut opportunities
  3. Check temperature forecast and its impact on compound windows
  4. Apply tyre strategic modifier to race signal
  5. Flag if weather may trigger early tyre change (safety car risk elevated)
output:   Race day signal with tyre_strategy_modifier applied
```

### Playbook 3: Mid-season regulation update signal
```
trigger:  FIA announces technical directive or regulation clarification
timing:   Announcement day
protocol:
  1. Assess which teams are most affected (loaded from domain file regulation section)
  2. Apply × 0.85 confidence reducer to all statistics for 2 races post-update
  3. Flag: "REGULATION_UNCERTAINTY" in signal output
  4. Resume standard statistical weights after 2 races of data in new spec
note:     Regulation changes are the biggest statistical disruption in F1
```

### Playbook 4: Constructor championship token signal — season finale
```
trigger:  Constructor championship decided (or within 25 points on final race)
timing:   Season finale weekend
protocol:
  1. Check constructor standings and points gap
  2. If championship clinched: apply post-win CDI protocol
  3. If within 25 points: apply × 1.12 urgency modifier to token signal
  4. If second place team is fighting for position: dual-token signal event
note:     Constructor championship is more token-relevant than driver title
          because the team token represents the constructor, not a driver
```

---

## Signal Weight Adjustments

For F1 statistics sub-module — adds to the `sport-domain-formula1.md` weights:

| Statistical modifier | Weight | Cap |
|---|---|---|
| Qualifying delta (Tier 1) | 15% additional weight | ±10 pts |
| Circuit type match (compound) | 8% additional weight | ±6 pts |
| Tyre strategy advantage | 6% additional weight | ±4 pts |
| Race pace vs qualifying delta | 4% additional weight | ±3 pts |
| Reliability history | 3% additional weight | ±3 pts |

**Combined F1 statistical modifier cap: ±12 points on adjusted_score.**

---

## Autonomous Execution

**Trigger conditions:**
- Qualifying session ends for any monitored F1 token event
- Weather forecast changes significantly (> 30% probability shift for rain)
- DNF confirmed for a monitored team's constructor token
- FIA technical directive or regulation update announced

**Execution at autonomy Level 2:**
- Post-qualifying: recalculate signal with qualifying delta applied. Notify.
- DNF: apply reliability modifier update. Notify if modifier changes recommendation.
- Regulation update: apply uncertainty flag. Reduce statistical confidence.

**Execution at autonomy Level 3–4:**
- Auto-recalculate and dispatch qualifying signal within 15 min of session end
- Auto-monitor FIA official communications for technical directives
- Auto-apply tyre compound modifier when grid positions confirmed

**Hard boundaries:**
- Qualifying delta is calibrated for specific circuit types — never apply
  high-downforce circuit qualifying modifier to a power circuit or vice versa
- Weather forecast changes are Tier 3 signals until rain is confirmed on circuit
- Never apply cross-regulation-era circuit statistics — 0× weight

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| Qualifying signal | Load this + sport-domain-formula1.md | Run post-qualifying |
| Race day signal | Tyre Playbook 2 | T-2h before race |
| Championship signal | Playbook 4 | Season finale context |
| Regulation update | Playbook 3 | FIA directive response |

---

## Agent Reasoning Prompts

- "Qualifying complete: calculate delta, apply circuit type modifier, update signal immediately."
- "0.3s+ qualifying gap on low-downforce circuit: highest predictive confidence in F1 library."
- "Rain in forecast: qualifying delta modifier reduced. Weather dominates statistical signal."
- "Regulation update detected: apply REGULATION_UNCERTAINTY flag for 2 races."
- "Constructor championship within 25 points: urgency modifier active for both team tokens."

---

## Data Sources

- Ergast F1 API (free): lap times, qualifying, results — developer.ergast.com/mrd
- FastF1 (Python library, free): sector times, tyre data, telemetry
- FIA official: timing.fiaformulae.com — official qualifying results (Tier 1)
- F1 official: formula1.com/en/results — race results and standings (Tier 1)
- Weather: weather.com / meteoblue (Tier 2 — cross-reference pre-race)

---

## Compatibility

**Load alongside:** `sports/formula1/sport-domain-formula1.md`
**Universal framework:** `core/match-statistics-intelligence.md`
**Fan token layer:** `fan-token/formula1-token-intelligence/token-intelligence-formula1.md`
**Breaking news:** `core/breaking-news-intelligence.md` (DNF, regulation directive)

---

*SportMind v3.89.0 · MIT License · sportmind.dev*
