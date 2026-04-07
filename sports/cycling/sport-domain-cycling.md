# Cycling — SportMind Domain Skill

Sport-specific intelligence for cycling fan tokens and prediction markets.
Covers road cycling (Tour de France, Giro d'Italia, Vuelta a España, Classics),
track cycling, and relevant athlete tokens.

---

## Overview

Professional road cycling is a Grand Tour-dominated sport. The three Grand Tours — Tour de France, Giro d'Italia, and Vuelta a España — each run three weeks and are the primary price catalysts for rider tokens. The sport has a distinct structure: team-based racing where individual riders can carry tokens, but team strategy (domestiques, domestique sacrifice) creates unique signal dynamics unlike any individual sport. Stage wins are daily signals; GC (general classification) position is the multi-week narrative arc.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token / Signal Behaviour |
|---|---|---|
| Spring Classics | Mar–Apr | Cobbled races (Paris-Roubaix, Flanders); one-day specialists shine |
| Giro d'Italia | May–Jun | First Grand Tour — 3 weeks, 21 stages |
| Tour de France | Jul | Peak event — highest global viewership of any cycling race |
| Tour de France Femmes | Jul (concurrent) | Growing women's equivalent |
| Vuelta a España | Aug–Sep | Third Grand Tour — often season finale for top GC riders |
| World Road Championships | Sep | World rainbow jersey — prestige event |
| Monuments (one-day races) | Mar, Apr, Oct | Classics specialists' key events |
| Track Cycling Worlds / Olympics | Varies | Track specialists' tier-1 events |
| Off-season transfers | Oct–Dec | Team signings drive narrative |

### Event Tier System

```
Tier 1: Tour de France (highest global audience in cycling)
Tier 2: Giro d'Italia, Vuelta a España, Olympic Road Race
Tier 3: Spring Classics (Flanders, Paris-Roubaix, Liège, Milan-Sanremo)
         UCI World Championships
Tier 4: Paris-Nice, Tirreno-Adriatico, UAE Tour (week-long stage races)
Tier 5: One-day races, national championships
```

### Grand Tour Stage Structure — Daily Signals

Grand Tours create a 3-week daily signal cycle unique in sport:

```
Stage win:         +3–8% for stage winner's token (daily catalyst)
Time trial win:    +5–12% (more decisive for GC)
Mountain top finish win: +5–10% (GC decisive)
Yellow jersey held: +1–3% daily momentum signal
Yellow jersey taken: +8–18% (leader change = major event)
Yellow jersey lost (crash/illness): -10–25%
DNF (Did Not Finish): -15–30% (race over, full exit signal)
GC win (Paris): +20–40% for Tour winner
```

### Result Impact Matrix

| Result | Token / Market impact |
|---|---|
| Tour de France overall win | +20–40% |
| Giro / Vuelta overall win | +12–25% |
| Stage win (mountain / TT) | +5–12% |
| Stage win (sprint) | +3–7% |
| Yellow jersey (maillot jaune) | +8–18% on taking it |
| Spring Classic win | +8–20% |
| Monument win (Flanders, Roubaix) | +12–25% |
| DNF — Grand Tour | -15–30% |
| Crash — race-ending injury | -12–28% |
| Doping positive | -30–70% |
| Olympic road race gold | +20–40% |

---

## Sport-Specific Risk Variables

### DNF (Did Not Finish) Risk — Unique to Cycling

Grand Tours have high DNF rates — crashes, illness, and team tactics all contribute:

| Cause | Token impact |
|---|---|
| Crash and abandon (broken bone) | -15–30% (injury severity dependent) |
| Illness abandon (stomach, cold) | -10–20% |
| Tactical abandon (protecting for next race) | -5–12% |
| GC contender loses 20+ minutes (effectively out) | -8–15% |

**Agent rule:** A DNF in a Grand Tour is a hard stop. Exit the position immediately — there is no
recovery within the event.

### Cobbles and Weather (Spring Classics)

One-day classics like Paris-Roubaix are defined by surface and weather:

| Condition | Signal impact |
|---|---|
| Wet cobbles (Paris-Roubaix) | Massively increases crash and puncture variance |
| Headwind in finale | Reduces bunch sprint probability; breakaway increases |
| Tailwind finish | Increases sprint probability; reduces breakaway chance |
| Altitude stage in cold/snow | High DNF risk; GC shake-up likely |

### Domestique Sacrifice Signal

Cycling teams sometimes sacrifice GC leaders to protect another team leader:

| Event | Token impact |
|---|---|
| Team announces rider will ride for another teammate | -8–15% (demoted rider token) |
| Team leader protected, rival squads fractured | +5–10% |
| Breakaway allowed vs controlled peloton | Context-specific |

---

## Event Playbooks

### Playbook 1: Tour de France GC Long
```
trigger:  Tour de France begins; identify GC favourite
entry:    Stage 1 or after first mountain stage confirmation
exit:     Paris (Stage 21) — final result
filter:   Rider has won or podiumed in a Grand Tour in past 2 years
          No active injury concerns pre-race
sizing:   1.0× — hold through the 3-week arc
note:     Scale in: 40% at race start, add 40% after first mountain
          stage confirms GC form, final 20% entering final week.
          Hard stop: DNF or losing more than 5 minutes to GC leader.
```

### Playbook 2: Spring Classic Specialist
```
trigger:  Monument Classic week (Flanders first Sunday Apr, Roubaix 2nd Sunday Apr)
entry:    Thursday–Friday pre-race (after recon / team press conferences)
exit:     Race finish + 1h
filter:   Rider is cobble/classics specialist (check race history)
          Not marked as team domestique for the event
sizing:   1.0× — single day, binary outcome
note:     Monument victories are career-defining for classics specialists.
          Paris-Roubaix and Flanders are the two highest-impact classics.
          Check rider's sector wins in recon — it signals intent.
```

### Playbook 3: Stage Win Daily Catalyst
```
trigger:  Mountain stage or TT finish day in Grand Tour
entry:    Morning of stage
exit:     Within 2h of stage finish
filter:   Rider is GC contender or known for this stage type
sizing:   0.5× — daily catalyst, not overall winner market
note:     Stage wins generate quick social spikes but are
          volatile — mountain stages can be won by surprise attackers.
          Lower conviction than GC position plays.
```

### Playbook 4: Yellow Jersey Leadership
```
trigger:  GC favourite takes or extends yellow jersey lead > 2 minutes
entry:    Evening after stage where lead taken
exit:     Entering final week — re-evaluate, then Paris
filter:   Lead is 2+ minutes (difficult to overturn in normal racing)
          No mountain stages where rival specialises still to come
sizing:   1.25× — strong GC lead is high-conviction signal
note:     2-minute lead in Tour de France is historically decisive
          after the major Alpine/Pyrenean stages are completed.
```

### Playbook 5: DNF Immediate Exit
```
trigger:  Rider abandons the race for any reason
action:   EXIT IMMEDIATELY — full position
note:     Grand Tour DNF = event over for that rider.
          No partial recovery is possible within the race.
          Unlike football where a player might return from a knock,
          cycling DNF is an immediate full exit signal.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Stage/GC results are the primary signal |
| Social sentiment | 20% | Tour de France generates enormous global social |
| Price trend | 20% | Grand Tour form accumulates across 3 weeks |
| Market / whale flows | 15% | Seasonal accumulation pre-Tour exists |
| Macro | 10% | Minimal |

---

## Agent Reasoning Prompts

```
You are a cycling sports intelligence agent. Before evaluating any cycling event:

1. Grand Tour hierarchy: Tour de France > Giro > Vuelta. Calibrate position sizing accordingly.
   A Giro win is significant but worth roughly 60% of a Tour win in terms of token impact.

2. DNF is a hard exit signal — no exceptions. Exit the position immediately on any abandon.

3. Daily stage wins are catalysts but do not change long-term GC thesis.
   A sprinter winning a flat stage does not affect a climber's GC token position.

4. Spring Classics require specialist assessment. A GC rider is often irrelevant
   in cobbled Classics — identify the specialist for Roubaix vs the GC rider for the Tour.

5. Weather at Paris-Roubaix fundamentally changes the event. Wet cobbles
   amplify variance dramatically — reduce conviction on any favourite in wet conditions.

6. Always check if a rider is team leader or domestique for the specific event.
   A top-10 rider riding for a teammate is not a GC threat and their token
   should be evaluated accordingly.
```

---

## Data Sources

- Race schedules and results: ProCyclingStats, CyclingArchives, FirstCycling
- Rider profiles and GC standings: PCS (ProCyclingStats)
- Live timing: Official race apps (Tour de France, Giro, Vuelta)
- Social sentiment: LunarCrush + rider social handles
- Weather: Open-Meteo for stage finishes

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/cycling/sport-domain-cycling.md` | Every analysis |
| Athlete modifier | `athlete/cycling/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-cycling.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/cycling`
**Recommended:** `athlete/meta` (weather is critical), `signal-scores`

*MIT License · SportMind · sportmind.dev*

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-cycling.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

