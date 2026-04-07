# MotoGP — SportMind Domain Skill

Sport-specific intelligence for MotoGP — the FIM MotoGP World Championship,
the premier class of motorcycle road racing.

---

## Overview

MotoGP is the highest class of motorcycle road racing and the second-largest
motorsport in the world by global audience. Unlike Formula 1, MotoGP has a
single championship (no constructors championship with equal weight), making
the rider the central prediction and token unit. The sport is characterised
by extreme physical demands, high crash probability, and a weather sensitivity
that exceeds any four-wheel motorsport.

Three manufacturers dominate: Ducati, Honda, and Yamaha — with Aprilia and KTM
as significant challengers. Factory team riders receive superior machinery;
satellite team riders run previous-generation or spec equipment, creating a
structural hardware advantage that is quantifiable and persistent.

---

## Domain Model

### Season Calendar

```
SEASON STRUCTURE:
  ~20 race weekends per year (March–November)
  Venues across Europe, Asia, Americas, and Middle East
  
RACE WEEKEND FORMAT:
  Friday:     Free Practice 1 + Free Practice 2
  Saturday:   Practice 3 + Qualifying (Q1 → Q2) + Sprint Race (new from 2023)
  Sunday:     Main Grand Prix race (~20 laps, ~45 minutes)

SPRINT RACE (introduced 2023):
  Half the main race distance; half the championship points
  Separate prediction unit from the main GP — different risk profile
  Tyre conservation not required; more aggressive riding
  
CHAMPIONSHIP POINTS (main race): 25-20-16-13-11-10-9-8-7-6-5-4-3-2-1
CHAMPIONSHIP POINTS (sprint):    12-9-7-6-5-4-3-2-1
```

### Tier Classification

**Tier 1:** MotoGP World Championship title clinch | Home GP of championship leader |
Final 3 rounds when title is close

**Tier 2:** Traditional 'cathedral' circuits — Mugello (Italy), Catalunya (Spain),
Assen (Netherlands), Phillip Island (Australia) — strongest fan base and token activation

**Tier 3:** Standard championship rounds

---

## The Motorcycle Hardware Advantage

Unlike Formula 1 where aerodynamic development is continuous, MotoGP technical
advantage is rooted in engine architecture and electronics packages that change
between generations. This creates predictable tiers:

```
HARDWARE TIER SYSTEM:

Factory (works) specification:
  Latest engine, electronics, aero, and data support
  Ducati Lenovo Team, Repsol Honda, Monster Yamaha (factory entries)
  Highest performance ceiling — but also highest setup complexity

Satellite with factory spec:
  Current-year bike supplied to satellite teams (Ducati especially does this)
  Pramac Ducati, Gresini Ducati: essentially factory spec bikes
  Performance close to factory; less data support and fewer custom setups

Satellite with previous-year spec:
  One-year-old machinery; measurable performance deficit
  Typically 0.3–0.8 seconds per lap slower than factory at same circuit
  More common at Honda and Yamaha satellite teams

AGENT RULE: Always identify whether a rider is on factory or satellite spec
before any performance prediction. A satellite Honda rider should never be
expected to match a factory Ducati on pace — regardless of rider talent.
```

---

## Crash Probability — MotoGP's defining risk

MotoGP has the highest crash rate of any motorsport in this library. Understanding
crash risk is not just about safety — it is a core prediction variable because
crashes directly determine race results.

```
CRASH RISK BY CIRCUIT TYPE:

Technical / twisty circuits (Assen, Mugello, Jerez):
  Higher corner count → more crash opportunities
  Low-speed technical sections: crashes more survivable; bike damage variable
  
High-speed circuits (Phillip Island, Losail/Qatar):
  Fewer corners but higher crash speeds
  Slide-off crashes more likely (less wall impact) but higher physical toll
  
Street circuits and unusual surfaces:
  Highest crash probability (barriers closer, grip less predictable)
  
WEATHER CRASH AMPLIFICATION:
  Wet conditions: crash probability rises sharply
  Mixed conditions (drying track): HIGHEST crash risk
    → Different sections of track dry at different rates
    → Tyre choice becomes critical and uncertain
  Cold temperatures: tyre warm-up incomplete early in race → crash risk elevated
  
RIDER CRASH HISTORY:
  Some riders have documented higher crash rates than peers
  Check: season crash rate vs field average
  Aggressive style riders (e.g. high lean angle specialists): elevated crash risk
  but also higher win ceiling

CRASH MODIFIER TABLE:
  Dry, normal circuit conditions:           × 1.00 (baseline)
  Wet conditions (full wet declared):       × 1.30 crash probability
  Mixed / drying conditions:               × 1.60 crash probability (highest risk)
  Cold track (< 15°C track temperature):   × 1.20 crash probability first 5 laps
```

---

## Tyre Management — the strategic core

MotoGP uses Michelin tyres supplied to all teams equally, but tyre selection
and management is a key differentiator. Unlike F1, there is no mandatory pit stop —
riders must complete the race on their chosen tyres.

```
TYRE COMPOUNDS (per race weekend, Michelin provides):
  Soft / Medium / Hard for front and rear independently
  Allocation varies by circuit — not all compounds available at every race
  
TYRE CHOICE SIGNAL:
  Qualifying: most riders go soft for maximum one-lap grip
  Race: choice depends on race length, circuit abrasion, temperature
  
  Soft rear tyre:   Higher early pace; degrades faster; risky in longer races
  Hard rear tyre:   Lower early pace; more consistent; better for hot conditions
  
TYRE DEGRADATION INDICATORS:
  Lap time evolution through a race reveals tyre management skill
  Riders who can preserve tyres in first half then attack late: consistent
  Riders who go hard early and fall off: high variance / crash risk late

TRACK EVOLUTION:
  First laps of Q2 on fresh track: rubber not laid yet → less grip
  By Sunday race: optimal rubber laid → lap times faster than practice
  Rain between sessions: washes rubber away → circuit reverts to low grip
```

---

## Weather — the highest-impact variable

MotoGP is more weather-sensitive than any four-wheel motorsport in this library.

```
WET RACE DYNAMICS:
  Race direction can declare: Dry | Wet | Mixed conditions
  Under wet conditions, riders may swap bikes mid-race (pit lane rule)
  
  WET RACE SPECIALISTS:
    Some riders dramatically outperform their dry-weather ranking in wet conditions
    Historical wet-race performance is a highly persistent individual trait
    Marc Márquez, Valentino Rossi: documented elite wet performance
    Check: rider's wet race win rate vs dry win rate — gap reveals specialist status
    
  WET RACE MODIFIER:
    Known wet specialist: × 1.25 vs their dry race expected position
    Known wet-averse rider: × 0.75 vs their dry expected position
    
FLAG-TO-FLAG RACES (conditions change during race):
  Complex — part dry, part wet
  First pit stop timing (when to switch bikes) is a critical decision
  Team strategy errors are common; results are highly unpredictable
  Agent rule: In flag-to-flag conditions, reduce position sizing (high variance)

WIND:
  Strong crosswinds increase instability on fast sections
  Long straight sections become physically demanding
  Suzuka, Portimão: known wind exposure circuits
```

---

## Championship Dynamics

```
TITLE CONTENTION SIGNAL:
  Rider within 50 points of leader with 5+ rounds remaining: contender status
  Rider 50–100 points back: must win + rely on errors ahead
  Rider 100+ points back: mathematical elimination approaching
  
  Agent rule: Championship leader approaching clinch is one of the highest
  sustained narrative signals in motorsport.

CONSTRUCTORS CHAMPIONSHIP:
  Exists but has lower fan token relevance than rider championship
  Factory team performance drives constructor standings
  
MOTIVATION SIGNAL:
  Rider who has clinched title: motivation to risk may reduce
  Rider who has mathematically lost: performance sometimes drops
  Rider in final year with team before leaving: complex motivation (prove value vs protect)
  
SILLY SEASON (rider transfer announcements):
  Typically August–October for following season
  Rider announced as leaving team: complex motivation for rest of season
  Major signing announced (new factory contract): positive motivation signal
```

---

## Event Playbooks

### Playbook 1: Factory vs Satellite Mismatch
```
trigger:  Factory-spec rider in dominant form vs satellite spec riders
entry:    After Q2 qualifying (grid position confirmed)
exit:     Race completion
filter:   Dry conditions expected (wet changes dynamics)
          Circuit suits the dominant manufacturer
sizing:   1.15× — hardware advantage is structural and persistent
note:     Ducati factory advantage at current-generation circuits is the
          most persistent structural signal in MotoGP prediction.
```

### Playbook 2: Wet Race — Known Specialist Starting
```
trigger:  Rain declared for race; known wet specialist in top-5 grid position
entry:    After wet conditions confirmed
exit:     Race completion
filter:   Full wet (not mixed — too unpredictable)
          Specialist has 3+ wet race wins in last 5 seasons
sizing:   1.20× — wet specialist advantage is the single strongest
          weather-performance correlation in any motorsport
```

### Playbook 3: Championship Clinch Weekend
```
trigger:  Leader can clinch title at this round
entry:    After Saturday qualifying
exit:     Race completion (or DNF)
filter:   Title gap requires only a points finish (not necessarily a win)
          Key rivals have mechanical or injury risk
sizing:   1.10× on narrative signal (clinch creates sustained token activation)
note:     Championship clinch is the highest single-event narrative moment
          in MotoGP. Even a 2nd-place clinch generates maximum coverage.
```

### Playbook 4: Home Grand Prix — National Rider
```
trigger:  Rider competing at their home nation Grand Prix
entry:    Pre-qualifying (elevated crowd narrative already building)
exit:     Race completion + 24h post-race
filter:   Rider in competitive form (top-10 pace this season)
          Home nation GP has strong token holder community
sizing:   1.10× on social/sentiment component
note:     Mugello (Italian riders), Catalunya/Jerez (Spanish riders),
          Phillip Island (Australian riders): highest home GP crowd effects.
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| Race win | +8–18% per token/prediction unit |
| World Championship clinch | +25–50% |
| Home GP win | +12–22% (sentiment amplified) |
| DNF / crash (leading rider) | -10–25% |
| Serious crash / injury | -20–40% (season-altering) |
| Wet race specialist wins wet race | Strong confirmation — expected |
| Factory contract signed | +10–20% long-term signal |
| Rider retirement announcement | -25–45% |

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Race results and championship progress dominant |
| Social sentiment | 25% | Rider-centric fandom; strong personality-driven narrative |
| Market / whale | 20% | Sophisticated motorsport bettor community |
| Price trend | 15% | Championship lead creates sustained trends |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
1. HARDWARE TIER FIRST. Identify factory vs satellite spec before any prediction.
   A satellite-spec rider cannot consistently outperform a factory-spec rider
   regardless of talent, unless conditions (wet, chaos) override machinery.

2. WEATHER IS PARAMOUNT. Check forecast before every race weekend.
   Mixed / drying conditions = highest variance race in this library.
   Reduce position sizing significantly in mixed conditions.

3. WET SPECIALIST DATABASE. Maintain a list of known wet-race specialists.
   When rain is confirmed, this is the single most actionable signal in MotoGP.

4. CRASH RISK CHANGES EXPECTATION. A rider leading on lap 15 of 25 in dry
   conditions on a degrading soft tyre is not a secure prediction — crash
   probability is elevated. Always factor completion probability.

5. SPRINT RACE IS A SEPARATE PREDICTION UNIT. Different tyre strategy, different
   risk profile, different form signal. Do not conflate sprint and main race.

6. CHAMPIONSHIP NARRATIVE BUILDS MOMENTUM. A rider closing on the title creates
   sustained week-on-week token engagement, not just single-race spikes.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
MotoGP-specific notes:
- Crash injuries are the primary injury mechanism — collarbone, wrist, shoulder most common
- Multiple fractures are common; riders often return faster than expected (motivation to race)
- Wild card rule: injured rider can be replaced by wild card entry for specific rounds
- "Race against the clock" injuries: riders frequently race with undisclosed fractures

## Data Sources

- **MotoGP official (motogp.com)**: Timing, results, championship standings
- **Motorsport.com**: Paddock news, rider statements, technical analysis
- **GPone.com**: Italian-language technical depth (factory team intelligence)
- **crash.net**: Crash incidents and injury tracking
- **WeatherAPI for circuit locations**: Pre-race weather forecasting


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/motogp/sport-domain-motogp.md` | Every analysis |
| Athlete modifier | `athlete/motogp/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-motogp.md` | Commercial decisions |

## Compatibility

**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
