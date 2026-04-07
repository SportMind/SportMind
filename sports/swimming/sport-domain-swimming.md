# Swimming — SportMind Domain Skill

Sport-specific intelligence for swimming fan tokens and prediction markets.
Covers Olympic swimming, World Championships (Aquatics), and the International Swimming League (ISL).

---

## Overview

Swimming is an Olympic-cycle sport — the Games produce the overwhelming majority of token/market interest. World records at the Olympics are the highest-impact events. Outside of the Olympics and World Championships, swimming follows the short-course World Cup circuit and the ISL team-based league. Individual swimmer tokens follow the same doping risk profile as athletics — WADA enforcement is strict.

---

## Domain Model

### Season Calendar

| Phase | Dates | Signal Behaviour |
|---|---|---|
| Short Course World Cup circuit | Oct–Nov | Lower impact — non-Olympic format |
| World Aquatics Championships | Biennial (odd years) | Tier-2 peak |
| Olympic Games | Every 4 years | Tier-1 — maximum signal |
| ISL (International Swimming League) | Oct–Dec | Team format, growing interest |
| National Championships | Spring | Selection events — qualification signal |

### Event Tier System

```
Tier 1: Olympic Games
Tier 2: World Aquatics Championships (long course)
Tier 3: European Championships, Commonwealth Games swimming
Tier 4: ISL events, World Cup circuit
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| Olympic gold + world record | +35–60% |
| Olympic gold (no record) | +20–40% |
| Olympic silver/bronze | +8–18% |
| World record broken (any event) | +20–45% |
| World Championship gold | +15–30% |
| Heat exit at Olympics | -8–18% |
| Doping ban | -30–70% |

---

## Sport-Specific Risk Variables

### Doping Risk (Same profile as athletics)

Swimming has a strong WADA enforcement record. Chinese swimming controversies have created periodic market uncertainty. Same doping exit protocol as athletics — provisional suspension = immediate exit.

### Suit Technology Cycles

Technological changes (swimsuit regulations) periodically reset world records:

| Event | Impact |
|---|---|
| New suit technology approved | Cluster of world records likely — positive for token market |
| Suit ban after polyurethane era | Record books reset — historical comparisons invalidated |

### Multi-Event Fatigue (Olympic Schedule)

Olympic swimming runs 8 days with multiple events per session. Elite swimmers competing in multiple events accumulate fatigue:

| Variable | Impact |
|---|---|
| Swimmer enters 4+ events | Fatigue risk — form degrades across programme |
| Back-to-back events same day | Reduced expected performance in second swim |

---

## Event Playbooks

### Playbook 1: Olympic Final Entry
```
trigger:  Swimmer qualifies for Olympic final (heats/semis confirmed)
entry:    Morning of final
exit:     1h post-result
filter:   World or Olympic record holder in that event
sizing:   1.5× — Olympics is tier-1
note:     Enter after semi-final confirmation — not pre-Games.
```

### Playbook 2: World Record Attempt (ISL / World Champs)
```
trigger:  Meet specifically structured for world record environment
entry:    Day of target event
exit:     Post-swim
filter:   Swimmer within 0.5% of world record currently
sizing:   1.0× on success; 0.4× pre-swim
```

---

## Agent Reasoning Prompts

```
1. Olympic cycle drives everything in swimming. Non-Olympic years are secondary signals.
2. World records are the single most important individual achievement — size immediately on confirmation.
3. Doping risk is high. WADA positive = immediate exit signal, same protocol as athletics.
4. Multi-event fatigue is real. A swimmer going 4 events across 8 days will decline in later events.
5. Heat exit at Olympics is a significant negative — world records in heats do not compensate for final absence.
```

---


---

## Signal Weight Adjustments

For Swimming, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 10% | Institutional positioning in swimming token markets |
| Social sentiment | 25% | Moderate social signal |
| Sports catalyst | 40% | Dominant signal driver — the sporting event itself |
| Price trend | 20% | Between-event momentum |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/swimming/sport-domain-swimming.md` | Every analysis |
| Athlete modifier | `athlete/swimming/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-swimming.md` | Commercial decisions |

## Data Sources

- **Official:** World Aquatics (worldaquatics.sport)
- **Records:** swimrankings.net
- **Olympic:** olympics.com/sport/swimming
- **Odds and prediction:** Betfair Exchange, Oddschecker

## Compatibility

**Pairs with:** `athlete/meta`, `signal-scores`
*MIT License · SportMind · sportmind.dev*

### Playbook 3: World Record proximity signal
```
trigger:  Swimmer within 0.5% of world record entering a major final
entry:    On heat result confirming form; reassess on semifinal time
exit:     Race completion
filter:   Check: pool conditions (50m vs 25m), lane draw, start time (evening finals faster),
          recent training camp reports; check rivalry field quality
sizing:   1.3× standard — world record events are the highest-signal moment in swimming
note:     World records in swimming generate the highest social volume and prediction
          market activity in the sport. The proximity signal is documented and consistent.
          Phelps/Ledecky patterns showed 0.3% proximity = elevated probability of record.
```

### Playbook 4: Olympic Games multi-event schedule management
```
trigger:  Swimmer competing in 3+ individual events at Olympics; events within 48h
entry:    After heats on Day 1; reassess fatigue progression after each round
exit:     Each individual race; do not hold positions across disciplines simultaneously
filter:   Check schedule density; number of rounds still to swim; relay commitments;
          athlete history of multi-event Olympics performance
sizing:   0.7× standard — multi-event fatigue is the primary risk; hard to quantify
note:     The greatest swimmers (Phelps, Ledecky) manage multi-event schedules but
          fatigue accumulates in later events. Later individual events in a packed
          schedule deserve reduced confidence vs earlier events at same meet.
```
