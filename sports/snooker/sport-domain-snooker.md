# Snooker — SportMind Domain Skill

Sport-specific intelligence for snooker fan tokens and prediction markets.
Covers the Triple Crown (World Championship, Masters, UK Championship), ranking events,
and the full professional tour.

---

## Overview

Snooker is a precision cue sport dominated by a small elite of world-class players. The Triple Crown events — particularly the World Championship at the Crucible — generate the largest market movements. UK and Asian audiences are the primary fan bases; the sport has enormous following in China, which has produced multiple world-class players. Individual player tokens are the relevant unit. The sport's relatively short match format (best-of-frames) creates frequent daily signal opportunities during major tournaments.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| UK Championship | Nov–Dec | First Triple Crown — season opener prestige |
| Masters | Feb | Invitation event — top 16 only; prestige without ranking |
| World Championship | Apr–May | Crucible — highest impact event of the snooker year |
| Summer ranking events | Jun–Aug | Lower profile; points racing, less token impact |
| Home Nations series | Sep–Oct | Scottish, Welsh, English, Northern Irish Opens |
| International events (China, Saudi) | Year-round | Growing Asian market relevance |

### Event Tier System

```
Tier 1: World Championship (Crucible) — 17-day event, most prestigious
Tier 2: Masters (Alexandra Palace) — invitation-only, no ranking points but huge prestige
         UK Championship — Triple Crown #3
Tier 3: Tour Championship, Players Championship (invitational finals)
Tier 4: Regular ranking events (Welsh Open, German Masters, etc.)
Tier 5: Home Nations, pro-am events
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| World Championship win | +25–50% |
| Masters win | +15–30% |
| UK Championship win | +12–25% |
| Crucible semi-final | +8–15% |
| Maximum break (147) | +10–20% (rare achievement — media spike) |
| First ranking event win | +8–18% |
| World Championship first round exit | -10–20% |
| World number 1 ranking achieved | +10–22% |
| Retirement announced | -30–60% |

---

## Sport-Specific Risk Variables

### Crucible Pressure — Unique Venue Effect

The Crucible Theatre seats only 980 people in an intimate atmosphere. Some players thrive; others consistently underperform:

| Variable | Impact |
|---|---|
| Player has strong Crucible record | +modifier — "Crucible specialist" is real |
| First-time Crucible appearance | Higher variance — adjust sizing down |
| Player with history of Crucible collapses | Negative modifier even as favourite |

**Agent rule:** Always check Crucible-specific win/loss record separately from general form.

### Session Structure — Multi-Day Matches

World Championship matches are split across multiple sessions over multiple days:

```
World Championship format:
  First round: Best of 19 frames (2 sessions)
  Second round: Best of 25 (3 sessions)
  Quarter-final: Best of 25
  Semi-final: Best of 33 (3 days)
  Final: Best of 35 (over 2 days — 17 sessions total)
```

**Agent rule:** Session-end scores create overnight position opportunities.
A player 8–2 down going into a session is recoverable (best of 19) but still significant.

### Ranking Race Context

Player tokens react to world ranking changes:

| Event | Impact |
|---|---|
| Player breaks into world top 10 | +8–18% |
| Player drops out of top 16 (loses Crucible seed) | -8–15% |
| Player qualifies for Masters (top 16 by January) | +5–10% |
| Player loses ranking position significantly | -5–12% |

---

## Event Playbooks

### Playbook 1: World Championship Long
```
trigger:  World Championship draw confirmed; identify favourite
entry:    Draw day (typically early April)
exit:     Tournament winner announced
filter:   Player is top-4 seed AND has won/reached final in past 3 years
          Strong Crucible-specific record
sizing:   1.5× — highest-impact snooker event
note:     Scale in across the tournament: 40% at draw, add on quarter-final
          confirmation, top-up entering semi-final. Hard stop: first-round exit.
```

### Playbook 2: Masters Invitation Final
```
trigger:  Player reaches Masters semi-final (top 4 confirmed)
entry:    Semi-final morning
exit:     Tournament result
filter:   Top-4 world ranking player; Masters history positive
sizing:   1.0× — no ranking points but huge prestige impact
note:     Masters is invitation-only — only top 16 play.
          Winning the Masters without ranking pressure is a pure
          prestige catalyst. Strong social response in UK market.
```

### Playbook 3: Maximum Break Alert
```
trigger:  Player makes 147 maximum break in televised match
entry:    Immediately (within 30min of break completion)
exit:     +48h (media cycle fades)
filter:   Player has on-chain token; event is live televised
sizing:   0.5× — narrative event, not ranking result
note:     147s are rare — approximately 10–15 per season across all events.
          Televised maximums generate outsized media coverage.
          This is a social/narrative play, not performance signal.
```

### Playbook 4: First Ranking Title Breakthrough
```
trigger:  Player wins first ranking event title
entry:    Final confirmation (match win)
exit:     +72h (narrative peak)
filter:   Player is under-25 or newly breaking into top 20
sizing:   1.0× — career breakthrough is strong catalyst
note:     First ranking title often signals sustained performance upgrade.
          Check if player has been close before (multiple finalist records).
```

### Playbook 5: World Ranking Drop Fade
```
trigger:  Player falls outside top 16 at ranking cut-off (January / post-Crucible)
signal:   Loses Masters invitation; potentially unseeded at Crucible
action:   Reduce or exit position
note:     Dropping out of top 16 means playing qualifying rounds at the Crucible.
          This is a structural downgrade to the player's competitive position
          and token valuation floor.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Tournament results dominate |
| Social sentiment | 25% | UK audience is deeply engaged during Crucible |
| Market / whale flows | 20% | Pre-Crucible accumulation is real |
| Price trend | 15% | Recent form predictive but Crucible-specific form more important |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
You are a snooker sports intelligence agent. Before evaluating any snooker event:

1. Crucible record is not the same as general form. Always check venue-specific
   history separately. "Crucible specialist" is a real and measurable phenomenon.

2. World Championship > everything else. The Crucible is the only event that matters
   at a career level. Size positions accordingly.

3. Session structure creates position opportunities within matches.
   An 8-frame deficit in a best-of-19 is recoverable but significant — use it.

4. Maximum breaks are social catalysts not performance signals.
   Size them as narrative events at 0.5× maximum.

5. Top-16 ranking status determines event access (Masters, Crucible seeding).
   Monitor ranking positions — a drop from top-16 is a structural negative.

6. The Masters is invitation-only. Winning it does not affect world ranking
   but carries enormous prestige in the UK market.
```

---

## Data Sources

- Rankings and results: World Snooker Tour (wst.tv)
- Crucible statistics: CueTracker (cuetracker.net)
- Player profiles: World Snooker official site

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/snooker/sport-domain-snooker.md` | Every analysis |
| Athlete modifier | `athlete/snooker/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-snooker.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/snooker`
**Recommended:** `signal-scores` (social component strong in UK market), `oracle-signals`

*MIT License · SportMind · sportmind.dev*
