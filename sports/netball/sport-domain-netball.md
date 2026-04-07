# Netball — SportMind Domain Skill

Sport-specific intelligence for netball fan tokens and prediction markets.
Covers Netball Superleague (UK), Suncorp Super Netball (Australia), and international competitions including the Netball World Cup and Commonwealth Games.

---

## Overview

Netball is one of the fastest-growing women's sports globally, with England Roses' Commonwealth Games gold (2018) and consistent World Championship contention accelerating UK interest significantly. The sport operates on two primary domestic leagues — Superleague (UK) and Super Netball (Australia) — with international competition centred on the Netball World Cup (every 4 years) and Commonwealth Games. Fan tokens in netball are an emerging asset class, driven by increasing broadcaster investment and the sport's young, digitally-engaged fan base.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| Superleague season (UK) | Feb–Jun | Domestic peaks; semi-finals and final are catalysts |
| Super Netball (AUS) | Mar–Sep | Australian domestic season |
| Quad Series | Jan (every 2 years) | England, Australia, NZ, South Africa — key form indicator |
| Commonwealth Games | Every 4 years | Netball is flagship event — medal contenders' tokens react |
| Netball World Cup | Every 4 years | Highest international catalyst |
| Nations Cup | Nov–Dec (varies) | International pre-season tournament |

### Event Tier System

```
Tier 1: Netball World Cup, Commonwealth Games (netball)
Tier 2: Superleague Grand Final (UK), Super Netball Grand Final (AUS)
Tier 3: Quad Series, Nations Cup
Tier 4: Regular Superleague / Super Netball season rounds
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| World Cup / Commonwealth Games gold | +20–40% |
| World Cup / Commonwealth Games silver/bronze | +8–15% |
| Superleague Grand Final win | +12–22% |
| Super Netball Grand Final win | +10–20% |
| England Roses major upset win | +10–22% |
| Star player injury | -8–18% |
| Top goal shooter: season top scorer | +5–12% |

---

## Sport-Specific Risk Variables

### Goal Circle Player Dominance

Netball scoring is position-specific — Goal Shooter (GS) and Goal Attack (GA) score all goals:

| Variable | Impact |
|---|---|
| Top GS/GA fit and in form | +modifier — scoring reliability key |
| GS injury or form slump | -8–15% for team token |
| Opponent GK (Goal Keeper) ranked world top-3 | Reduces scoring expectation |

### Commonwealth Games Netball — Elevated UK Interest

Netball is one of the few sports where England/Australia/NZ are genuinely competitive at the top. The Commonwealth Games final is a cultural event in the UK:

| Event | Impact |
|---|---|
| England reaches Commonwealth Games final | +10–20% |
| England wins gold (not guaranteed — Australia/NZ dominant) | +20–35% |

---

## Event Playbooks

### Playbook 1: World Cup / Commonwealth Games Final
```
trigger:  England, Australia, or New Zealand reaches final
entry:    Semi-final win confirmation
exit:     Final result
filter:   Nation has realistic gold medal chance (top-3 world ranked)
sizing:   1.5× — highest-tier netball event
```

### Playbook 2: Superleague Grand Final
```
trigger:  Grand Final confirmed (top-2 finalists known)
entry:    Semi-final week
exit:     Final result
sizing:   1.0×
note:     UK Superleague Grand Final is growing in broadcast reach —
          check if event is on BBC Red Button or Sky (signals audience size).
filter:  standard availability and macro checks apply
```

### Playbook 3: Star Shooter Form Run
```
trigger:  Goal shooter records 4+ consecutive 95%+ shooting accuracy rounds
entry:    After 4th consecutive high-accuracy round
exit:     Next major event result
sizing:   0.7× — individual performance signal
filter:  standard availability and macro checks apply
```

---

## Agent Reasoning Prompts

```
1. Netball is position-specific for scoring — GS/GA fitness is the primary individual variable.
2. World Cup and Commonwealth Games are tier-1 events; domestic leagues are tier-2.
3. England, Australia, and NZ compete at the top. England winning gold is not guaranteed
   — adjust expectations vs cricket or rugby where home nations dominate.
4. The sport is growing rapidly — social signals move faster than traditional valuations suggest.
5. BBC coverage of major events amplifies UK market sentiment significantly.
```

---


---

## Signal Weight Adjustments

For Netball, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 15% | Institutional positioning in netball token markets |
| Social sentiment | 30% | High narrative-driven fanbase |
| Sports catalyst | 35% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*


---



### Playbook 4: World Cup / Commonwealth Games final (peak event)
```
trigger:  Gold medal match or World Cup final
entry:    48h before match; lineup confirmed
exit:     Full time
filter:   Both teams' key shooters confirmed fit; check form across tournament;
          head-to-head in this tournament loaded
sizing:   1.3× standard — highest-engagement netball event; peak token/prediction signal
note:     Netball's commercial peak events are concentrated around the World Cup cycle
          and Commonwealth Games. Australia and New Zealand dominate but England and
          Jamaica have closed the gap. Use tournament form, not season form.
```

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/netball/sport-domain-netball.md` | Every analysis |
| Athlete modifier | `athlete/netball/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-netball.md` | Commercial decisions |

## Data Sources

- **Official:** World Netball (worldnetball.sport), Super Netball (supernetball.com.au)
- **Results:** BBC Sport Netball
- **Live scores:** FlashScore Netball
- **Odds and prediction:** Betfair Exchange, Oddschecker

## Compatibility

**Pairs with athlete skill:** Use `athlete/meta` for cross-sport context
**Recommended:** `signal-scores` (social component growing), `athlete/meta`

*MIT License · SportMind · sportmind.dev*
