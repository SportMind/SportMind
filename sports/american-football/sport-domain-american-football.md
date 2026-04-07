# American Football (NFL) — SportMind Domain Skill

Sport-specific intelligence layer for American football fan tokens on Chiliz Chain.
Pairs with `signal-scores`, `prematch-alpha`, `whale-intel`, and `backtest-engine` from the core fan-token-skills toolkit.

---

## Overview

American football (NFL) is uniquely structured for fan token alpha: it's **one game per week per team**,
with enormous social anticipation building across the full week. This means each matchday carries far more
weight than a football or basketball game — closer to a UEFA Champions League knockout tie in terms of
cultural and sentiment impact. The trade-off is low event frequency (~18 regular season games per season).

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token Behaviour |
|---|---|---|
| NFL Draft | Apr–May | Franchise-building narrative, major for fan sentiment |
| OTAs / Training Camp | May–Aug | Roster news, injury watch, depth chart speculation |
| Pre-season games | Aug | Low impact — starters play minimally |
| Regular season | Sep–Jan | Core alpha window — 18 weeks, 1 game/week |
| Wild Card weekend | Jan | Playoff entry confirmed — high excitement |
| Divisional round | Jan | Higher stakes, significant token impact |
| Championship games | Jan | Conference title — major catalyst |
| Super Bowl | Feb | Highest-impact single event in American sport |
| Free agency | Mar | Roster speculation, star player moves |

**Rule:** Weekly cadence means agents can be highly deliberate — there is no "missed the game" pressure.
Signals accumulate across a full week; the `-24h` and `-2h` prematch-alpha windows are most actionable.

### The Weekly Alpha Window

NFL's weekly schedule creates a structured 7-day cycle per matchup:

```
Monday:   Previous game result digestion, injury report begins
Tuesday:  Coaching/game film review, injury designations (DNP, limited, full)
Wednesday: First official injury report — most impactful for signal
Thursday:  (Thursday Night Football — short-week game, different dynamics)
Friday:    Final injury report — "questionable" designations resolved
Saturday:  Travel day, locker room atmosphere leaks
Sunday:    Game day — peak alpha window
Monday:    Recap, next week's opponent announced
```

**Wednesday injury report** is the most important non-game event in the weekly cycle.
A star quarterback listed as "DNP" (Did Not Practice) on Wednesday is a significant bearish signal.

### Injury Report Risk Tiers

| Designation | Meaning | Token Impact |
|---|---|---|
| Out | Will not play | -5–15% (star player) |
| Doubtful | <25% chance to play | -3–8% |
| Questionable | ~50% chance to play | -2–5% / +2–5% on resolution |
| Limited | Practiced with restrictions | Neutral to -1% |
| Full | Full practice — cleared | +1–3% (recovery confirmation) |
| IR (Injured Reserve) | Out minimum 4 weeks | -8–20% (star player) |

### Result Impact Matrix (NFL)

| Situation | Token Impact |
|---|---|
| Regular season win (expected) | +2–5% |
| Regular season upset win | +6–15% |
| Loss (expected) | -2–4% |
| Upset loss | -5–12% |
| Playoff win | +8–18% |
| Conference Championship win (Super Bowl bound) | +15–30% |
| Super Bowl win | +25–55% |
| Super Bowl loss | -15–30% |

### Key Sentiment Catalysts (Non-Game)

| Event | Impact |
|---|---|
| Top QB signed in free agency | +10–25% |
| Star player traded to team | +8–18% |
| Head coach fired mid-season | -8–15% |
| #1 overall draft pick | +5–12% narrative pump |
| Super Bowl location/date announced | Minimal |
| Hard Knocks (HBO) team selection | +3–7% media exposure |

---

## Competition Reference

### NFL (Primary)
- 32 teams, 18-game regular season + 17th game added 2021
- 14 teams qualify for playoffs (7 per conference)
- Single-elimination playoffs: Wild Card → Divisional → Championship → Super Bowl
- Key rivalries (highest matchday impact): Chiefs–Raiders, Cowboys–Giants,
  Bears–Packers, Steelers–Ravens, Patriots-adjacent (legacy media attention)

### College Football (Secondary — NCAAFB)
- CFP (College Football Playoff) expanding to 12 teams
- Heisman Trophy announcement is a narrative catalyst for associated programs
- Lower direct token relevance currently, but growing GameFi angle (NIL-linked tokens)

---

## Event Playbooks

### Playbook 1: Standard Weekly Matchday Long
```
trigger: team with fan token playing this week (Sunday / MNF / TNF)
entry:   Wednesday post-injury-report (if star QB/skill position = Full/Limited, not DNP)
exit:    Sunday evening post-game (within 2h of final whistle)
filter:  signal_score > 55, no active oracle bearish signal, team W% > 50%
sizing:  0.8× standard (weekly cadence, conservative sizing per event)
note:    Thursday Night Football = shorter prep, more upsets — reduce conviction by 20%
```

### Playbook 2: Injury Report Escalation Fade
```
trigger: star QB or primary skill player listed DNP on Wednesday
signal:  oracle bearish + social negative shift
action:  reduce position by 50%, fully exit if DNP confirmed Friday
re-entry: if player confirmed active Friday afternoon → reverse, enter long
sizing:  This is a risk management playbook, not a directional trade
exit:    hold to event completion
filter:  standard availability and macro checks apply
```

### Playbook 3: Playoff Bracket Entry Long
```
trigger: team clinches playoff spot (late regular season)
entry:   clinching game night
exit:    each round: post-win hold, post-loss exit immediately
filter:  team on winning streak (W4+ of last 6), QB healthy
sizing:  1.0× at Wild Card, 1.25× at Divisional, 1.5× at Championship game
note:    playoff momentum is cumulative — increase exposure with each round
```

### Playbook 4: Super Bowl Pre-Event Accumulation
```
trigger: team reaches Super Bowl (Conference Championship win)
entry:   immediately post Conference Championship win
exit:    Super Bowl day (game night), regardless of result
note:    2-week hype period between Conference Championship and Super Bowl
         generates sustained social momentum — one of the longest alpha windows
sizing:  1.25× (sustained window; exit before game to avoid binary risk)
alternative: hold through game for championship pump if conviction high
filter:  standard availability and macro checks apply
```

### Playbook 5: Free Agency Star Signing Catalyst
```
trigger: elite QB or top-3 skill player signed in free agency (March window)
entry:   within 2h of official signing announcement
exit:    +72h (hype peaks quickly; next catalyst is training camp performance)
filter:  player is starter-calibre, not a depth signing
sizing:  0.6× (off-season, lower liquidity; narrative trade not performance trade)
```

---

## Key Commands

| Command | Skill | Use Case |
|---|---|---|
| `get_upcoming_alpha` | prematch-alpha | Weekly game alpha packets |
| `get_signal_scores` | signal-scores | Composite score incl. social (injury news drives social fast) |
| `get_whale_flows` | whale-intel | Institutional accumulation ahead of playoff weeks |
| `get_oracle_signals` | oracle-signals | Bearish distribution on injury/coach news |
| `get_team_form` | sports-data | Win/loss streak — critical for NFL playoff seeding context |
| `run_backtest` | backtest-engine | Simulate weekly game strategies on historical data |
| `execute_trade` | order-router | Best-price execution post-result |

---

## Agent Reasoning Prompts

```
You are an American football fan token trading agent. Before acting on any signal:
1. Check the weekly injury report — quarterback health is the single most
   important variable in NFL fan token pricing. A healthy elite QB = bullish baseline.
2. NFL games are weekly, not daily. You have time to be deliberate.
   Never rush into a position before Wednesday's injury report is out.
3. Thursday Night Football games deserve a 20% conviction reduction —
   short-week preparation creates more volatility and upset probability.
4. Playoff rounds are independent events — re-evaluate sizing each round.
   Don't simply hold through the playoffs without checking injury and opponent context.
5. The Super Bowl 2-week window is unique: 14 days of pure narrative alpha.
   Consider an exit-before-the-game strategy to capture hype without binary risk.
6. Free agency and the NFL Draft are the off-season's price movers.
   Monitor signing announcements in March and draft night in April–May.
```

---

## Data Sources
- Game schedule: NFL official schedule feed
- Injury reports: Official NFL injury designations (Wed/Thu/Fri each week)
- Social sentiment: LunarCrush galaxy score + team social handles
- Price correlation: match_price_correlation adapted for NFL game events
- Whale flows: 10 CEX APIs, 4h rolling windows

---


---

## Signal Weight Adjustments

For American Football (NFL), agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 25% | Institutional positioning in american token markets |
| Social sentiment | 25% | Moderate social signal |
| Sports catalyst | 30% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*

## Compatibility

`prematch-alpha` maps cleanly — weekly cadence fits the -24h/-2h/-15m structure well.
`signal-scores` sports catalyst component should incorporate injury report status.
`backtest-engine` can simulate NFL weekly strategies using available historical price data.

```
npx skills add sportmind/fan-token
```

---
MIT License · SportMind · sportmind.dev

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-nfl.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

