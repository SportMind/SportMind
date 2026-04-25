# Formula 1 — SportMind Domain Skill

Sport-specific intelligence for Formula 1 fan tokens, prediction markets, and race outcome signals.
Covers the FIA Formula 1 World Championship — constructors, drivers, race calendar, regulation cycles.

---

## Overview

Formula 1 is structurally unique among motorsports. It runs two parallel championships simultaneously —
**Drivers'** (individual) and **Constructors'** (team) — and tokens can be tied to either. A fixed
annual calendar of 20–24 Grands Prix creates a structured race weekend format (practice → qualifying
→ race) with multiple distinct signal windows per event. Regulation changes every few years reset the
competitive order completely, making historical form less predictive than in most other sports.
The 2026 season introduces major new technical regulations — a full reset of the competitive hierarchy.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token / Prediction Behaviour |
|---|---|---|
| Pre-season testing | Feb–Mar | Car launches + test pace — speculative signal only |
| Season opener | Mar | Highest-information event of the year |
| Spring swing | Mar–May | Competitive order establishing |
| European summer | Jun–Aug | Prestige venues — Monaco, Silverstone, Monza, Spa |
| Summer break | Aug (2 weeks) | Minimal; silly season transfer rumours |
| Sprint weekends | ~6 per season | Additional race format — elevated weekend signal |
| Championship run-in | Sep–Nov | Maximum stakes if title open |
| Season finale | Nov–Dec (Abu Dhabi) | Championship decider potential |

**Rule:** Never trade on pre-season testing pace alone. Wait for qualifying confirmation at race 1.

### Race Weekend Signal Windows

```
STANDARD WEEKEND:
  Thursday:    Press conferences — team news, driver quotes
  Friday FP1:  First competitive running — setup data, directional only
  Friday FP2:  Race simulation runs — more meaningful but still early
  Saturday FP3: Final setup tweaks — minor signal
  Saturday QF: QUALIFYING — grid position set — primary pre-race signal
  Sunday:      RACE — points, championship impact, primary result

SPRINT WEEKEND (~6 per season):
  Friday FP1 → Sprint Qualifying (SQ)
  Saturday:   Sprint Race (real points) → Full Qualifying
  Sunday:     Grand Prix
```

**Qualifying is the single most important pre-race signal.** Grid position predicts
race outcome more reliably than any other F1 variable. An unexpected front-row for
a midfield constructor is a genuine signal; expected pole for the champion is noise.

### Points and Championship Structure

```
Race points: 1st=25, 2nd=18, 3rd=15, 4th=12, 5th=10, 6th=8, 7th=6, 8th=4, 9th=2, 10th=1
Fastest lap bonus: +1 (if in top 10 finishers)
Sprint points: 1st=8, 2nd=7, 3rd=6 ... 8th=1

Constructor token key insight: both drivers' results combine.
A 1-2 finish is the maximum positive signal. A double DNF from mechanical
failure is a severe negative — constructor token, not just driver.
```

### Result Impact Matrix

| Result | Driver token | Constructor token |
|---|---|---|
| Race win (expected) | +5–10% | +4–8% |
| Race win (upset) | +15–30% | +12–25% |
| Pole position (unexpected) | +8–18% | +6–14% |
| Podium (not expected) | +6–12% | +5–10% |
| DNF — mechanical | -8–18% | -12–22% |
| DNF — driver error | -5–12% | -3–8% |
| Drivers' Championship win | +25–50% | +15–30% |
| Constructors' Championship win | +15–25% | +20–45% |
| Top driver transfer announced | ±10–25% | ±5–15% |

---

## Competition Reference

### Tier 1 Races (highest token impact)

**Monaco** — Cannot overtake; qualifying = race. Pole here is near a race win anywhere else.
**Silverstone (British GP)** — Home race for most constructor tokens; massive UK audience.
**Monza (Italian GP)** — Ferrari's home; Tifosi atmosphere; highest passion audience.
**Suzuka (Japanese GP)** — Honda/Red Bull connection; massive Asian audience.
**Las Vegas GP** — Night race, show-business format, North American market.
**Season finale (Abu Dhabi)** — Championship decider if mathematically open.

### Tier 2 Races
Bahrain, Australia, Spain, Canada, Austria, Hungary, Belgium, Singapore, USA (COTA), Brazil, Mexico.

### Constructor Token Profiles

| Constructor | Fan base | Key market | Token relevance |
|---|---|---|---|
| Ferrari | Largest global F1 fan base; Tifosi | Italy, global | Highest |
| Red Bull Racing | Dominant 2022–24; young global audience | Netherlands, global | Highest |
| Mercedes | Hamilton era legacy; strong worldwide | UK, Germany, global | High |
| McLaren | British heritage; resurgent 2023+ | UK, global | Growing |
| Aston Martin | UK premium; Alonso factor | UK, Spain | Moderate |
| Alpine | French national identity | France | Moderate |

---

## Sport-Specific Risk Variables

### Regulation Change Cycles

Major technical regulation resets occur every 3–5 years and invalidate prior form entirely:

| Event | Signal impact |
|---|---|
| Major reg reset announced | Speculative — years in advance |
| First pre-season test (new regs) | First evidence — who has adapted? |
| Season opener under new regs | Highest-information event of the cycle |
| Mid-season aero update | +5–15% if dominant; -8–15% if ineffective |
| 2026 regulations (current season) | Full reset — prior form largely irrelevant |

**Agent rule:** In a regulation-change year, reduce confidence in prior-season performance
data by 40%. The first 3 races establish the new competitive hierarchy.

### Safety Car and Weather

| Event | Impact |
|---|---|
| Safety car during leader's pit window | Major shuffle — championship implications |
| Wet race | Upsets 3× more likely — lower conviction on any favourite |
| Red flag suspension | Results can be declared at any point — uncertainty |
| Strategic pit stop error | -10–20% constructor token on widely reported error |

### DNF Reliability Risk

| DNF cause | Constructor impact | Driver impact |
|---|---|---|
| Engine failure | -12–20% | -5–10% |
| Gearbox failure | -8–15% | -4–8% |
| Collision (racing incident) | -3–8% | -3–8% |
| Driver error | -3–8% | -8–15% |
| Recurring same failure (2+ races) | -15–25% (systemic) | -5–10% |

---

## Event Playbooks

### Playbook 1: Season Opener Long
```
trigger:  First race of season — post-qualifying Saturday evening
entry:    Enter on unexpected front-runner confirmed by qualifying
exit:     Race result + 48h
filter:   Pre-season testing pace was consistent (not one fast lap)
          Qualifying confirms the testing signal
sizing:   1.25× — opener sets token narrative for next 4–6 races
note:     Wait for qualifying. Testing pace alone is insufficient.
          The constructor that wins race 1 typically leads narratively
          for the first quarter of the season.
```

### Playbook 2: Monaco Qualifying Upset
```
trigger:  Unexpected pole or front row at Monaco qualifying
entry:    Immediately post-qualifying (Saturday evening)
exit:     Race result + 1h
filter:   Constructor showed Friday pace (not pure fluke)
          Dry race forecast (wet Monaco = different dynamic)
sizing:   1.25× — Monaco pole is the highest-conversion qualifying result
note:     Monaco cannot overtake. Pole here = ~75% race win probability.
          Highest value qualifying play in the calendar.
```

### Playbook 3: Championship Run-in Accumulation
```
trigger:  Final 5 races, Drivers' or Constructors' gap < 50 points
entry:    Start of final 5-race run
exit:     Championship mathematically decided (either direction)
filter:   Leader's token HAS > 50 (actively traded ecosystem)
sizing:   1.25× — sustained multi-event narrative window
note:     Scale: 30% at trigger, add on each race leader maintained.
          Hard exit: title mathematically decided — narrative collapses instantly.
```

### Playbook 4: Top Driver Transfer Announcement
```
trigger:  Confirmed Tier 1 driver move (world champion or 5+ race wins)
entry:    Within 2h of official announcement
exit:     +72h (narrative peak)
filter:   Destination constructor has active token
sizing:   0.8× — off-season announcement, no on-track confirmation
note:     Destination token = positive. Departure token = negative.
          Both can move simultaneously — assess both before entering.
          Hamilton to Ferrari (2024) was the definitive precedent.
```

### Playbook 5: New Regulation Era Opener
```
trigger:  Season opener under major new technical regulations
entry:    Post-qualifying Saturday (after on-track confirmation)
exit:     After race 3 (competitive order clearer)
filter:   Pre-season AND Friday practice AND qualifying all point same direction
sizing:   1.5× — highest conviction playbook in all of F1 token intelligence
note:     A constructor dominating the opener of a new regulation era
          typically leads for 2–3 seasons. The narrative window is long.
          This playbook only applies ~every 3–5 years — it is rare and
          high-value when it does occur.
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Race and qualifying results dominate |
| Market / whale flows | 25% | Manufacturer backing is stable, informed money |
| Social sentiment | 20% | Large, vocal global F1 community |
| Price trend | 15% | Regulation cycles reduce trend predictiveness |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
You are a Formula 1 sports intelligence agent. Before evaluating any F1 event:

1. Check regulation context. If this is a regulation-change season (2026),
   discount prior-season data by 40% and treat the first 3 races as the new baseline.

2. Qualifying is the primary pre-race signal. Friday practice is directional only.
   Never enter a position based on Friday data alone.

3. Monaco qualifying is worth more than qualifying anywhere else.
   Pole at Monaco is approximately equal to a race win at most other circuits.

4. Constructor tokens react to BOTH drivers combined. A 1-2 finish is double
   the positive signal of a single win. A double mechanical DNF is a severe
   constructor token event.

5. Distinguish DNF causes. Mechanical failure hurts the constructor token.
   Driver error hurts the driver narrative but less so the constructor.
   Recurring mechanical failures (same issue twice) are a systemic signal.

6. Silly season runs July–October. Top driver transfer announcements are annual
   narrative events — monitor contract expiry dates and tier-1 source signals.

7. Wet races triple upset probability. Reduce conviction on any favourite
   when rain is forecast. Safety car deployments can reverse any race outcome.
```

---

## Data Sources

- Race results and standings: Formula 1 official, Ergast API (ergast.com/mrd)
- Timing and telemetry: FastF1 Python library (open source)
- Transfer news: motorsport.com, autosport.com, The Race, Sky Sports F1
- Technical regulations: FIA official documents
- Social: LunarCrush + constructor/driver social handles

---


## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Qualifying signal | `sport-statistics-formula1.md` | Apply qualifying delta + circuit type |
| Race day signal | `sport-statistics-formula1.md` Playbook 2 | Tyre compound strategy |
| Regulation update | `core/breaking-news-intelligence.md` | REGULATION_UNCERTAINTY flag |
| Constructor championship | Playbook 4 | Season finale context |
| DNF response | Breaking news Category 2 | Reliability modifier |

## Autonomous Execution

**Trigger conditions:**
- Qualifying session ends for any monitored F1 constructor token event
- Race result confirmed for any monitored constructor token
- FIA technical directive or regulation clarification announced
- DNF confirmed for a monitored team's car during race

**Execution at autonomy Level 2:**
- Post-qualifying: apply qualifying delta modifier. Flag circuit type used.
  Notify operator of updated signal. Await confirmation before position action.
- Race result: calculate CDI extension/contraction. Notify.
- Technical directive: flag REGULATION_UNCERTAINTY for 2 races. Notify.
- DNF: apply reliability modifier. If pattern (2+ DNFs in 3 races): escalate.

**Execution at autonomy Level 3–4:**
- Auto-recalculate qualifying signal within 15 min of session end
- Auto-dispatch race result CDI update within 30 min of result confirmation
- Auto-monitor FIA official communications for technical directives
- Auto-log all reliability events with circuit and failure type

**Hard boundaries:**
- Qualifying delta circuit-type modifier must match actual circuit category.
  Never apply street circuit modifier to a power circuit — cross-category error.
- Wet qualifying: reduce qualifying delta modifier by 0.50× regardless of gap size.
  Wet conditions equalise qualifying gaps — this is empirically documented.
- Cross-regulation-era statistics: 0× weight. F1 cars change fundamentally
  with each regulation cycle (typically every 3–5 years).

---

## Compatibility

**Fan token layer:** `fan-token/formula1-token-intelligence`
**Recommended:** `signal-scores`, `athlete/meta` (weather overlay essential in F1)

---

*MIT License · SportMind · sportmind.dev*

## Fan Token™ Layer

For Formula 1 fan token intelligence — FTIS, Constructor Token Index (CTI), Driver Token
Multiplier (DTM), regulation cycle position, silly season transfer scoring, and dual-token
championship battle logic — load the dedicated bridge skill:

**`fan-token/formula1-token-intelligence`**

Recommended agent chain for F1 fan token decisions:
```
sports/formula1                                  ← domain context (this skill)
  + fan-token/fan-token-pulse                    ← on-chain baseline
  + fan-token/formula1-token-intelligence        ← F1-specific token intelligence
  + fan-token/athlete-social-lift                ← DTM live confirmation
```

