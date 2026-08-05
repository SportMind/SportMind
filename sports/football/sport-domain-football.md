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
- **La Liga** — El Clásico is the single highest-impact fixture in the suite
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

All commands route through the Fan Token™ Intel MCP / API backend.

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

Football reasoning chain — apply in this order for every football signal:

```
FOOTBALL REASONING CHAIN

STEP 1: ESTABLISH MATCH IMPORTANCE
  Identify the occasion weight before any other modifier.
    UCL Final:            ×2.00 (highest in library — demand amplifier)
    UCL semi/quarter:     ×1.60
    UCL group:            ×1.40
    Domestic cup final:   ×1.60
    Derby match:          ×1.35
    Standard domestic:    ×1.00
  Low-importance matches (dead rubber, end-of-season with nothing at stake):
    Apply ×0.90 motivation discount.
  Rule: set the occasion weight before assessing form, squad, or tactics.

STEP 2: ASSESS COMPETITIVE CONTEXT
  Is either side playing for a title, relegation survival, European qualification,
  or cup progression?
    MUST WIN context:        ×1.10–1.15 motivation modifier.
    Nothing to play for:     ×0.88–0.92 motivation modifier.
    Balanced stakes (both competing): standard modifiers.
  Rule: motivation only amplifies the stronger signal — it does not reverse direction.

STEP 3: LOAD SQUAD INTELLIGENCE
  Source: athlete/athlete-intelligence-framework.md → athlete/football/athlete-intel-football.md.
  Apply APS modifier for both sides.
  Flag if lineup_unconfirmed = true (T-2h confirmation not yet received).
  Key positions for football APS:
    Goalkeeper absent:              ×0.82–0.88
    Primary CDM absent:             ×0.85–0.90
    Primary striker absent:         ×0.83–0.88
    Tactical wide forward absent:   ×0.90–0.95

STEP 4: CHECK TACTICAL MATCHUP
  Identify the key corridor battle from confirmed lineups.
  Apply TMAS only when a structural mismatch is confirmed, not inferred.
    Elite winger vs inexperienced fullback: TMAS ×1.05
    Dominant aerial striker vs short defensive line: TMAS ×1.04
    No confirmed structural mismatch: TMAS = ×1.00 (do not apply)
  Reference: core/tactical-matchup-intelligence.md

STEP 5: APPLY ENVIRONMENTAL MODIFIERS
  Venue (home/away/neutral): apply home advantage or set to 0 if neutral.
  Travel fatigue: apply if intercontinental travel <72h before kickoff.
  Weather: apply if significant and sport-relevant (rain on heavy pitch, etc.)
  Reference: core/venue-intelligence.md, core/weather-intelligence.md

STEP 6: CHECK FAN TOKEN SIGNALS
  If either club has an active fan token in the SportMind registry:
    Check FTP status in fan-token/registry/complete-registry.md.
    If PATH_2 active ($AFC confirmed): flag path2_active = true.
      Supply event fires on result: LOSS = MINT EVENT (not neutral).
    For derby matches: always check BOTH tokens, not just the home side.
    If either token is in Phase 4+ lifecycle: apply demand modifier.
  Reference: fan-token/ftp-path2.md, fan-token/fan-token-lifecycle/

STEP 7: PRODUCE STRUCTURED OUTPUT
  Stack all modifiers from Steps 1–6. Multiply (never add).
  Check for modifier conflicts (same factor applied twice → apply once).
  Output: direction + adjusted_score + composite_modifier + flags.
  Reference: core/pre-match-signal-framework.md for full output schema.
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


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Core football signal intelligence: event playbook, signal weights, and reasoning prompts |
| Reasoning | ACTIVE | Football reasoning chain from squad and conditions to direction signal |
| Context | ACTIVE | Football context: competition tier, home advantage, European vs domestic competition |
| Memory | ACTIVE | Historical football outcome patterns — largest calibration dataset in SportMind |
| Judgment | ACTIVE | Judgment on football signal hierarchy — lineup quality index is the primary signal |
| Attention | ACTIVE | Maximum attention for confirmed lineups and injury news before kickoff |
| Communication | ACTIVE | Football signal output with LQI, modifier stack, and confidence level |
| Verification | ACTIVE | Football data from official club/league/UEFA sources |
| Learning | ACTIVE | Football is the most calibrated sport in the library — 96% direction accuracy |
| Integration | ACTIVE | Integrates with all football-specific files, LQI, APS, and fan-token/football/ framework |
| Calibration | ACTIVE | Football modifiers are the most calibrated in SportMind — 100+ records |
| Adaptation | ACTIVE | Football intelligence adapts as competition formats and tactical evolution continues |
| Ethics | NOT APPLICABLE | Football sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Modifier stack, signal weights, and source hierarchy explicit in football outputs |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |


---
MIT License · SportMind · sportmind.dev

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-football.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

