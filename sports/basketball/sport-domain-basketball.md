# Basketball — SportMind Domain Skill

Sport-specific intelligence layer for basketball fan tokens on Chiliz Chain.
Pairs with `signal-scores`, `whale-intel`, `prematch-alpha`, and `order-router` from the core fan-token-skills toolkit.

---

## Overview

Basketball operates on a fundamentally different rhythm from football. The NBA regular season runs 82 games
over ~6 months, with games 3–4× per week per team. This high-frequency schedule means event-driven alpha
windows are shorter and more numerous, but individual game impact is lower than in football — until the playoffs,
when stakes compress and signals amplify significantly.

This skill teaches your agent how to navigate that rhythm for basketball fan tokens.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token Behaviour |
|---|---|---|
| Pre-season / Media Day | Sep–Oct | Speculation, roster reveal sentiment |
| Regular season | Oct–Apr | High game frequency, steady volume |
| All-Star break | Mid-Feb | Volume dip, narrative-driven (player awards) |
| Trade deadline | ~Feb 6 | Roster moves = sharp sentiment shifts |
| Play-In Tournament | Mid-Apr | Elevated stakes for bubble teams |
| Playoffs (R1–R2) | Apr–May | Major volume and price impact events |
| Conference Finals | May | Peak engagement, highest per-game impact |
| NBA Finals | Jun | Highest-impact series in the calendar |
| Draft / Free Agency | Jun–Jul | Off-season narrative catalyst |
| Summer League | Jul | Low impact, prospect hype only |

**Rule:** Weight playoff signals 2–3× regular season. The Finals produce football-derby-level token movements.

### Game Frequency Adjustment

Basketball teams play ~4× more often than football clubs. This requires:
- Lower per-game position sizing vs. football matchday plays
- Streak-based logic: a team on a 5+ win streak is more meaningful than a single result
- Series logic in playoffs: momentum builds across multiple games in a series

```
per_game_sizing = standard_football_size × 0.3     # regular season
per_game_sizing = standard_football_size × 0.7     # playoffs R1–R2
per_game_sizing = standard_football_size × 1.0     # conference finals / finals
```

### Player-Token Correlation

Basketball is more star-driven than any other team sport. A single player's status can dominate token sentiment:

| Player Event | Token Impact |
|---|---|
| Superstar injury (out for season) | -10–25% |
| Superstar returns from injury | +5–15% |
| Trade acquisition of star | +8–20% |
| Star traded away | -12–30% |
| MVP award / All-Star selection | +3–8% |
| Playoff performance (series-winning shot) | +5–12% same night |

**Agent rule:** Monitor player news as a first-class signal alongside match results. Use social sentiment
(`get_signal_scores` social component) as an early indicator of player-driven moves.

### Result Impact Matrix (Basketball)

| Situation | Token Impact |
|---|---|
| Regular season win | +1–3% |
| Regular season loss | -1–2% |
| Playoff series win (advance) | +5–15% |
| Playoff elimination | -10–20% |
| Upset win vs top seed | +6–12% |
| Finals win (championship) | +15–35% |

---

## Competition Reference

### NBA (Primary)
- 30 teams, 82-game regular season
- Playoffs: 16 teams, best-of-7 series format
- Fan tokens: select NBA franchises have issued or are expected on Chiliz
- Key series to monitor: any involving tokens issued on-chain

### EuroLeague (Secondary)
- Top European club basketball
- Turkish Airlines EuroLeague Final Four is highest-impact European event
- Lower liquidity tokens vs NBA — spreads wider, moves sharper

### FIBA (International)
- World Cup and EuroBasket create national team sentiment overlaps
- Typically lower direct token impact unless national players overlap with club tokens

---

## Event Playbooks

### Playbook 1: Playoff Series Entry Long
```
trigger: team qualifies for playoffs (end of regular season / play-in)
entry:   day of first playoff game announcement
exit:    series elimination OR after each series win, re-evaluate
filter:  team win % > 55% in regular season, no major injury to star player
sizing:  0.7× standard (series can run 4–7 games, manage exposure)
note:    hold through series unless star player injured or oracle signal fires
```

### Playbook 2: Trade Deadline Catalyst
```
trigger: major trade acquisition announced (star player joins team)
entry:   within 2h of official trade announcement
exit:    +48h (initial reaction fades)
filter:  player ranked top-30 NBA by usage/impact
sizing:  0.5× (news can reverse — verify trade is completed, not just rumoured)
note:    use social momentum signal to confirm direction before entry
```

### Playbook 3: Championship Rally
```
trigger: team wins NBA Championship / EuroLeague title
entry:   immediate post-game (within 30min of final buzzer)
exit:    +72h (celebration cycle: Day 1 pump, Day 2–3 fade)
filter:  price not already up >15% pre-game (check -24h movement)
sizing:  1.5× standard
note:    strongest single-event catalyst in basketball calendar
```

### Playbook 4: Injury Exit Signal
```
trigger: star player ruled out for rest of season
signal:  oracle bearish signal + social negative spike
action:  reduce or exit position
timing:  within 4h of confirmed medical report (not just rumour)
note:    rumour → denial cycles are common — wait for official confirmation
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

### Playbook 5: All-Star Weekend Narrative
```
trigger: player from token team wins All-Star MVP / Slam Dunk contest
entry:   event night
exit:    +24h
sizing:  0.3× (narrative event, not sporting result — lower conviction)
filter:  standard availability and macro checks apply
```

---

## Key Commands

| Command | Skill | Use Case |
|---|---|---|
| `get_signal_scores` | signal-scores | Composite score — social component especially relevant for basketball |
| `get_whale_flows` | whale-intel | Accumulation watch ahead of playoff games |
| `get_score_detail` | signal-scores | Player-driven social momentum breakdown |
| `get_upcoming_alpha` | prematch-alpha | Pre-game alpha packets (adapt football logic to basketball cadence) |
| `get_price_correlation` | sports-data | Historical price move at game events |
| `run_backtest` | backtest-engine | Simulate playoff series strategy across historical data |
| `get_oracle_signals` | oracle-signals | Bearish distribution ahead of injury/trade risk |
| `execute_trade` | order-router | Best-price execution across 13 exchanges post-event |

---

## Agent Reasoning Prompts

```
You are a basketball fan token trading agent. Before acting on any signal:
1. Distinguish regular season from playoffs — sizing and conviction differ significantly.
2. Basketball is star-driven. Always check player injury/availability before a position.
3. A team on a win streak is more reliable than a single result signal.
4. Trade deadline and draft periods create narrative moves disconnected from game results.
5. In a playoff series, think in terms of the full series outcome, not game-by-game.
6. Championship wins are the highest-conviction catalyst — act fast, exit within 72h.
```

---

## Data Sources
- Game data: NBA / EuroLeague schedule feeds
- Player news: social sentiment via LunarCrush galaxy score
- Price correlation: match_price_correlation dataset (adapt for game events)
- Whale flows: 10 CEX APIs, 4h rolling windows

---


---

## Signal Weight Adjustments

For Basketball, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 20% | Institutional positioning in basketball token markets |
| Social sentiment | 30% | High narrative-driven fanbase |
| Sports catalyst | 25% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 10% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*


## Autonomous Execution

**Trigger conditions:**
- Starting lineup confirmed for monitored game (NBA or EuroLeague)
- Star player confirmed absent (injury report or lineup exclusion)
- Trade confirmed for monitored team token (deadline day or any confirmed trade)
- Playoff series result confirmed

**Execution at autonomy Level 2:**
- Lineup: apply Net Rating and key player status. Notify operator.
- Star absent: apply ATM modifier. Flag "STAR_PLAYER_ABSENT". Notify immediately.
- Trade: apply CDI modifier. Notify with full assessment.
- Playoff result: update series signal and CDI. Notify.

**Execution at autonomy Level 3–4:**
- Auto-process lineup within 10 min of official publication
- Auto-dispatch playoff CDI updates within 20 min of confirmed result
- Auto-monitor team official channels for injury reports during playoffs
- Trade deadline: auto-process confirmed trades and dispatch CDI updates

**Hard boundaries:**
- Top-5 global player absence: Category 1 RELOAD. Human review required.
  No autonomous action on positions until operator confirms updated signal.
- Regular season stats for playoff prediction: mandatory playoff adjustment.
  Never use unadjusted regular season ORtg/TS% for playoff signal.
- Player injury information from fan/social media (Tier 4): never apply autonomously.
  Official team injury report or confirmed lineup only (Tier 1/2).

---

## Compatibility

Core `signal-scores` and `whale-intel` skills apply directly.
`prematch-alpha` logic translates to pre-game windows — treat game tip-off as "kickoff".
`backtest-engine` can simulate basketball strategies using price snapshot data.

```
npx skills add sportmind/fan-token
```

---
MIT License · SportMind · sportmind.dev
