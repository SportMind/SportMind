# Football / Soccer — SportMind Domain Skill

Sport-specific intelligence layer for football fan tokens on Chiliz Chain.
Pairs with `sports-data`, `prematch-alpha`, `signal-scores`, and `whale-intel` from the core fan-token-skills toolkit.

---

## Overview

Football is the native sport of the Chiliz ecosystem — 27 clubs, 10 leagues, 847+ matchdays of historical data.
This skill gives your agent a structured mental model of how football events translate into token price behaviour,
so it can reason about timing, context, and risk rather than just reacting to raw signals.

---

## Domain Model

### Season Rhythm

Football tokens follow a predictable annual calendar. Agents should weight signals differently by phase:

| Phase | Months (EU) | Token Behaviour |
|---|---|---|
| Pre-season | Jul–Aug | Low volume, speculative sentiment, transfer rumours drive social |
| Early season | Aug–Oct | High engagement, results volatile, momentum builds |
| Mid-season | Nov–Feb | Derby peaks, cup competitions add event density |
| Title run-in | Mar–May | Elevated stakes matches, whale accumulation common |
| International break | Various | Club token volume drops, fan attention shifts |
| Off-season | Jun–Jul | Lowest liquidity, transfer window opens late June |

**Rule:** Reduce position sizing during international breaks and off-season. Increase at season opener and derby windows.

### Match Importance Scoring

Not all matches are equal. Prioritise signals for high-importance events:

```
importance_score = base_weight × rivalry_multiplier × stakes_multiplier × form_differential

base_weight:
  - League match: 1.0
  - Cup quarter-final+: 1.4
  - Derby: 1.6
  - Title decider: 2.0
  - Relegation six-pointer: 1.8

rivalry_multiplier:
  - Local derby: 1.5
  - Historical rival: 1.3
  - No rivalry: 1.0

stakes_multiplier:
  - Top 4 race: 1.3
  - Relegation zone: 1.4
  - Mid-table: 1.0
```

Use `get_importance_scores` and `get_derby_schedule` from `sports-data` to fetch pre-computed values.

### Result Impact Matrix

Historical average token price movement by result type (source: match_price_correlation, 847+ matchdays):

| Result | Home Token | Away Token |
|---|---|---|
| Home win (expected) | +2–4% | -1–3% |
| Home win (upset) | +6–12% | -4–8% |
| Away win (expected) | -2–4% | +2–5% |
| Away win (upset) | -5–10% | +8–15% |
| Draw (high-stakes) | -1–3% both | |
| Draw (low-stakes) | ~0% both | |

Use `get_price_correlation` and `get_match_impact` to retrieve token-specific historical values — these override generic estimates.

---

## Competition Reference

### Tier 1 Competitions (highest token impact)
- **UEFA Champions League** — group stage draw and knockout rounds are major catalysts
- **Premier League** — highest liquidity tokens (BAR, PSG adjacents, Man City-linked)
- **La Liga** — El Clásico is the single highest-impact fixture in the ecosystem
- **Serie A** — Juventus, Inter, AC Milan tokens; Derby della Madonnina and Derby d'Italia

### Tier 2 Competitions (moderate impact)
- **Ligue 1** — PSG dominance creates asymmetric token behaviour
- **Bundesliga** — stable, lower volatility tokens historically
- **Europa League** — signals matter from quarter-finals onward

### Tier 3 (low direct impact, monitor for sentiment)
- Domestic cups (Coppa Italia, Copa del Rey, FA Cup)
- Pre-season tournaments (Club World Cup, friendlies)

---

## Event Playbooks

### Playbook 1: Standard Matchday Long
```
trigger: match importance_score > 1.3
entry:   -2h window (prematch-alpha packet)
exit:    +1h post fulltime
filter:  signal_score > 60, whale_sell_ratio < 0.4
sizing:  standard
```

### Playbook 2: Derby Accumulation
```
trigger: get_derby_schedule → match within 72h
entry:   -24h window, scale in over 3 tranches
exit:    fulltime or +30min if momentum continues
filter:  no active oracle bearish signal
sizing:  1.5× standard (elevated impact expected)
note:    both home and away tokens often move — check which side has
         stronger whale accumulation via get_whale_flows
```

### Playbook 3: Champions League Knockout Catalyst
```
trigger: CL round of 16, QF, SF, or Final
entry:   -24h (draw announced or match week begins)
exit:    post-match +24h
filter:  team in positive form (get_team_form last 5: W≥3)
sizing:  1.25× standard
note:    CL final week is highest-liquidity event of the football calendar
```

### Playbook 4: Relegation Panic Fade
```
trigger: team enters relegation zone after loss
signal:  oracle bearish signal fires + whale sell_ratio > 0.6
entry:   short signal or avoid
exit:    when team exits zone or oracle signal clears
note:    relegation risk tokens can lose 15–30% in severe cases;
         this is a fade / avoidance signal, not a short setup
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

### Playbook 5: Title Win Pump
```
trigger: team mathematically clinches title
entry:   immediate (within 1h of final whistle)
exit:    +48–72h (sentiment fades fast post-celebration)
filter:  not already priced in (check -24h price move < 5%)
sizing:  standard — momentum can be strong but fades quickly
```

---

## Key Commands

All commands route through the Fan Token Intel MCP / API backend.

| Command | Skill | Use Case |
|---|---|---|
| `get_fixtures` | sports-data | Upcoming match calendar with league and cup context |
| `get_derby_schedule` | sports-data | Identify elevated-impact matches in next 7–14 days |
| `get_importance_scores` | sports-data | Numeric importance rating per upcoming fixture |
| `get_team_form` | sports-data | Last 5/10 results, home/away split |
| `get_price_correlation` | sports-data | Historical price move at kickoff, FT, +1h, +24h |
| `get_match_impact` | sports-data | Average impact by match type for a specific token |
| `get_upcoming_alpha` | prematch-alpha | -24h, -2h, -15m alpha packets for upcoming matches |
| `get_signal_scores` | signal-scores | Composite 0–100 score including sports catalyst component |
| `get_whale_flows` | whale-intel | Accumulation/distribution ahead of fixture |
| `run_backtest` | backtest-engine | Test any football-specific strategy across full history |

---

## Agent Reasoning Prompts

Use these as system prompt fragments when deploying a football-focused agent:

```
You are a football fan token trading agent. Before acting on any signal:
1. Check match importance — low-importance matches generate noise, not alpha.
2. Check team form — a signal for a team in a 5-game losing run needs higher confirmation.
3. Cross-reference whale flows with prematch alpha — divergence is a warning sign.
4. Respect the season calendar — reduce exposure during international breaks.
5. For derby matches, always check BOTH tokens, not just the home side.
```

---

## Data Sources
- Match data: Football API (27 clubs, 10 leagues)
- Price correlation: match_price_correlation dataset (847+ matchdays)
- Whale flows: 10 CEX APIs, 4h rolling windows
- Social sentiment: LunarCrush galaxy score + mentions

---


---

## Signal Weight Adjustments

For Football / Soccer, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 25% | Institutional positioning in football token markets |
| Social sentiment | 20% | Moderate social signal |
| Sports catalyst | 30% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 10% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*

## Compatibility

Requires `sports-data` skill (core).
Recommended: `prematch-alpha`, `signal-scores`, `whale-intel`, `oracle-signals`.
Optional: `backtest-engine` (validate playbooks before deploying capital).

```
npx skills add sportmind/fan-token
```

---

## Fan Token Layer

For fan token intelligence specific to football — competition × token impact scoring,
national team × club token spillover (including World Cup 2026), athlete token
multiplier profiles, and multi-token fixture logic — load the dedicated bridge skill:

**`fan-token/football-token-intelligence`**

This skill sits between the sport domain layer (this file) and the commercial
intelligence layer (`fan-token-pulse`, `brand-score`, `athlete-social-lift`) and
provides football-specific precision that no other skill in SportMind covers.

Recommended agent chain for football fan token decisions:
```
sports/football                          ← domain context (this skill)
  + fan-token/fan-token-pulse            ← on-chain baseline
  + fan-token/football-token-intelligence ← football-specific token intelligence
  + fan-token/athlete-social-lift        ← live ATM confirmation
```

---
MIT License · SportMind · sportmind.dev

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-football.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

