# Athletics — SportMind Domain Skill

Sport-specific intelligence layer for athletics fan tokens, prediction markets, and athlete outcome signals.
Covers track and field: sprints, middle/long distance, jumps, throws, hurdles, relays, and combined events.

---

## Overview

Athletics is an Olympic-cycle sport with four-year peaks around the Games, and a year-round Diamond League circuit providing sustained signal windows. Individual athlete tokens dominate — there are no meaningful team tokens except relay squads in niche markets. The sport is uniquely star-dependent: world record breakers generate token/market moves independent of the event tier. Doping risk is the highest of any mainstream sport — a positive test is a structural exit signal.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token / Signal Behaviour |
|---|---|---|
| Indoor season | Jan–Mar | Secondary — World Indoors in even years |
| Diamond League circuit opens | Apr–May | Form signals emerge; season baseline |
| European / national championships | Jun–Jul | Regional peaks; national tokens react |
| World Athletics Championships | Aug–Sep (odd years) | Tier-2 event — biggest non-Olympic |
| Diamond League Finals | Sep | Season climax — consistent performers rewarded |
| Olympic Games | Jul–Aug (every 4 years) | Tier-1 — highest possible athletics catalyst |
| Off-season | Oct–Dec | Minimal; contract and training news only |

### Event Tier System

```
Tier 1: Olympic Games
Tier 2: World Athletics Championships (odd years)
Tier 3: Diamond League Finals / Continental Championships
Tier 4: Individual Diamond League meetings (Zurich, Brussels, Oslo, Rome...)
Tier 5: National championships, indoor events
```

### Result Impact Matrix

| Result | Token / Market impact |
|---|---|
| Olympic gold | +30–60% |
| World Championship gold | +20–45% |
| World record broken | +25–55% (any meeting — record transcends tier) |
| Olympic silver/bronze | +10–20% |
| Championship final (no medal) | +3–8% |
| Heat / semi exit (did not make final) | -8–18% |
| Injury withdrawal | -12–25% |
| Doping ban (provisional) | -25–50% |
| Doping ban (confirmed 4yr) | -50–80% |
| Diamond League series win | +8–15% |

---

## Sport-Specific Risk Variables

### Doping / WADA Suspension Risk — Highest of Any Sport

| Outcome | Token impact |
|---|---|
| Provisional doping suspension | -25–50% (uncertainty phase) |
| Confirmed 4-year ban | -50–80% |
| Lifetime ban | -70–95% (token collapse) |
| Acquittal / suspension overturned | +30–50% recovery |

**Agent rule:** Always check WADA / AIU status before entering. Any athlete under investigation is uninvestable.

### Wind and Conditions

| Condition | Signal impact |
|---|---|
| World record with legal wind (≤+2.0 m/s) | Full historical significance |
| Wind-assisted performance | Diminished — not officially ratified |
| Rain or cold in sprint finals | Increases times, reduces record probability |
| High altitude venue | Distances and sprints run faster — adjust expectations |

### Multi-Round Format Risk (Sprints / Hurdles)

| Factor | Impact |
|---|---|
| Athlete exits in heats (before semi) | -8–18% — failed to qualify |
| Outside lane draw (200m / 400m) | Minor psychological disadvantage |
| False start history | Increases DQ risk — check recent record |
| Strong heat field draws | Upset qualification risk even for favourites |

---

## Event Playbooks

### Playbook 1: Olympic Track Final
```
trigger:  Athlete qualifies for Olympic sprint or middle-distance final
entry:    Morning of final (after semi confirmation)
exit:     Within 1h of result
filter:   Athlete is defending champion or world record holder
          No injury reports during Games
sizing:   1.5× — Olympics is highest tier
note:     Enter after semifinal result — not pre-competition.
          Athlete in final = form just proven, qualification confirmed.
```

### Playbook 2: World Record Attempt
```
trigger:  Meeting specifically structured for WR attempt (e.g. Duplantis special events)
entry:    Day of event on announcement
exit:     Immediately post-attempt
filter:   Athlete within 1–2% of world record; legal conditions expected
sizing:   1.25× on confirmed success; 0.5× pre-event (binary)
note:     World records cluster — athletes often attempt multiple times
          in one season. Build position if multiple attempts are likely.
```

### Playbook 3: Championship Heat Monitor
```
trigger:  World Championships / Olympics begins
entry:    Hold until athlete confirms semifinal qualification
exit:     Final result
filter:   Qualified comfortably (top-2 in heat, not on time)
sizing:   1.0× after semi; 0.4× before heats
note:     Do not enter full position pre-heats. Exit early round
          is a real risk even for favourites. Premature entry is
          the most common mistake in athletics trading.
```

### Playbook 4: Diamond League Series Leader
```
trigger:  Athlete leads Diamond League standings entering Finals
entry:    DL Finals announcement week
exit:     Finals result
filter:   Won 3+ DL meetings in the season
sizing:   0.8× — consistency signal, not championship spike
note:     Diamond League win = season-long performance validation.
          Use as confidence builder, not a high-conviction single trade.
```

### Playbook 5: Doping Alert Exit
```
trigger:  Provisional suspension or doping investigation confirmed
action:   EXIT IMMEDIATELY — full position
note:     Athletics doping cases take months to resolve.
          Even eventual acquittals come after months of token underperformance.
          Provisional suspension is a structural exit, not a dip to hold.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Championship results are primary |
| Social sentiment | 25% | World records and Olympic moments go instantly viral |
| Market / whale flows | 20% | Pre-Olympics accumulation is real |
| Price trend | 15% | Season form is predictive |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
You are an athletics sports intelligence agent. Before evaluating any athletics event:

1. Check Olympic cycle. Olympic year = maximum signal for all athletics tokens.
   Odd non-Olympic year (World Championships) = tier-2. Even non-Olympic = tier-3.

2. Never enter before heat qualification. Wait for semifinal confirmation
   before committing full position in sprint/hurdle events.

3. World records transcend event tier. A world record at any Diamond League
   meeting is a tier-1 signal regardless of competition context.

4. ALWAYS check WADA / AIU status before any entry. Provisional suspension
   is an exit signal — do not hold through a doping investigation.

5. Wind conditions matter. A wind-assisted "world record" has no
   historical significance — adjust expectations accordingly.

6. Some athletes face near-zero competition in their discipline (Duplantis in
   pole vault, Warholm in 400m hurdles). These carry different risk profiles —
   their only real risk is injury or doping, not being beaten.
```

---

## Data Sources

- Results and schedules: World Athletics (worldathletics.org)
- Diamond League: diamondleague.com
- WADA / doping: wada-ama.org, AIU Athletics Integrity Unit
- Social sentiment: LunarCrush + athlete social handles

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/athletics/sport-domain-athletics.md` | Every analysis |
| Athlete modifier | `athlete/athletics/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-athletics.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/athletics`
**Recommended:** `signal-scores`, `oracle-signals`, `athlete/meta`

*MIT License · SportMind · sportmind.dev*
