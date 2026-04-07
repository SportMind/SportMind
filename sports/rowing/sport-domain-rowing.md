# Rowing — SportMind Domain Skill

Sport-specific intelligence for rowing fan tokens and prediction markets.
Covers Olympic rowing, World Rowing Championships, the Boat Race (Oxford vs Cambridge),
and the Henley Royal Regatta.

---

## Overview

Rowing operates on two distinct circuits — Olympic/international rowing (individual and crew boats across multiple disciplines) and the UK's unique tradition of collegiate and club rowing (Boat Race, Henley). The Olympic Games is the primary signal event. The Oxford–Cambridge Boat Race is a uniquely British cultural event that generates significant domestic market interest, particularly relevant for any collegiate or institutional fan tokens. Weather and water conditions are critical variables with no equivalent in field sports.

---

## Domain Model

### Season Calendar

| Phase | Dates | Signal Behaviour |
|---|---|---|
| Indoor training / ergo season | Nov–Feb | Minimal market signal |
| Boat Race (Oxford vs Cambridge) | Late Mar | UK cultural event — crew loyalty tokens react |
| Henley Royal Regatta | Jul | Prestige invitation event |
| World Rowing Championships | Sep (non-Olympic) | Tier-2 international signal |
| Olympic Games | Jul–Aug (every 4 years) | Tier-1 — all rowing medals covered |
| World Rowing Cup series | May–Jun | Qualifying and form indicator |

### Event Tier System

```
Tier 1: Olympic Games
Tier 2: World Rowing Championships
Tier 3: Boat Race (UK cultural event), Henley Royal Regatta
Tier 4: World Rowing Cup, national championships
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| Olympic gold | +20–40% |
| Olympic silver/bronze | +8–18% |
| World Championship gold | +12–25% |
| Boat Race win (Oxford / Cambridge) | +10–20% (university/collegiate tokens) |
| World record broken | +15–30% |
| Crew withdrawal (medical/coxing incident) | -10–20% |

---

## Sport-Specific Risk Variables

### Water and Weather Conditions

Rowing is uniquely weather-dependent on race day:

| Condition | Impact |
|---|---|
| Strong headwind | Slows all times; increases crew boat coordination errors |
| Tailwind | Faster times — record conditions possible |
| Rough water (Boat Race) | Increases capsizing risk; significantly increases upset probability |
| High river flow (Boat Race) | Favours crews comfortable in strong currents |

**Agent rule for Boat Race:** Check river conditions and wind direction on race morning. A strong headwind on the Championship Course heavily affects which crew's style is advantaged.

### Boat Race Rivalry Dynamics

The Oxford–Cambridge Boat Race has over 170 years of history:

| Variable | Signal impact |
|---|---|
| One crew has significantly faster erg scores pre-race | +modifier for faster crew |
| Crew has experienced cox vs less experienced | Significant advantage on bends |
| Injury to key rower in week before race | -8–15% for affected crew token |

---

## Event Playbooks

### Playbook 1: Olympic Rowing Final
```
trigger:  National crew qualifies for Olympic final
entry:    Morning of final (after semi confirmation)
exit:     1h post-result
filter:   Crew is defending champion or world record holder
sizing:   1.5×
```

### Playbook 2: Boat Race Day
```
trigger:  Boat Race morning — conditions confirmed
entry:    Race morning (conditions assessed)
exit:     Race result + 1h
filter:   One crew has demonstrably faster pre-race erg times
sizing:   0.8× — conditions create variance
note:     Rough water significantly equalises conditions. Reduce
          conviction in any forecast of rough/windy race day conditions.
```

---

## Agent Reasoning Prompts

```
1. Olympic cycle dominates. All other events are secondary unless culturally significant (Boat Race in UK).
2. Weather conditions are a primary variable — check wind and water on race morning.
3. Boat Race is a UK cultural event with genuine audience regardless of sporting significance.
4. Crew sports have collective performance — one weak rower affects the whole boat.
5. World records in rowing are genuine athletic achievements — size immediately on confirmation.
```

---


---

## Signal Weight Adjustments

For Rowing, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 10% | Institutional positioning in rowing token markets |
| Social sentiment | 20% | Moderate social signal |
| Sports catalyst | 45% | Dominant signal driver — the sporting event itself |
| Price trend | 20% | Between-event momentum |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/rowing/sport-domain-rowing.md` | Every analysis |
| Athlete modifier | `athlete/rowing/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-rowing.md` | Commercial decisions |

## Data Sources

- **Official:** World Rowing (worldrowing.com)
- **Oxford/Cambridge Boat Race:** theboatrace.org
- **Results:** Rowing Results Archive
- **Odds and prediction:** Betfair Exchange, Oddschecker

## Compatibility

**Pairs with:** `athlete/meta` (weather overlay), `signal-scores`
*MIT License · SportMind · sportmind.dev*

### Playbook 3: Oxford-Cambridge Boat Race (UK cultural peak)
```
trigger:  Annual Boat Race on the Thames (March/April)
entry:    48h before race on crew confirmation and weather report
exit:     Race completion (~18 minutes)
filter:   Check crew health declarations; weather (wind/current affect outcome materially);
          load core-weather-match-day.md (rowing section)
sizing:   1.2× standard — highest single-event rowing engagement in UK market
note:     The Boat Race is rowing's highest-volume token and prediction market event.
          Crew weight advantage and blade efficiency have documented predictive value.
          Cambridge have won more recent editions — do not weight historical records equally.
```

### Playbook 4: Olympic Games final (4-year cycle peak)
```
trigger:  Olympic rowing final (any event)
entry:    Heat and semifinal results loaded; progressive form analysis across rounds
exit:     Race completion
filter:   World ranking going in; recent World Championships result; lane draw loaded;
          weather conditions at venue
sizing:   1.0× standard — Olympic variance is highest; world records possible
note:     Olympic rowing finals are the peak signal event. World record attempts
          create outsized narrative signals. Lane draw matters on some courses.
          Load core-narrative-momentum.md — Olympic record proximity modifier applies.
```
