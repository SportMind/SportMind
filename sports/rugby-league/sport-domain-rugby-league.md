# Rugby League — SportMind Domain Skill

Sport-specific intelligence for rugby league fan tokens and prediction markets.
Covers Super League (UK/Europe), NRL (Australia), State of Origin, and international competitions.

---

## Overview

Rugby league is a distinct sport from rugby union — faster, 13-a-side, with a structured 6-tackle-then-hand-over possession system. The sport has two dominant leagues: Super League (UK) and NRL (Australia/New Zealand), which operate in opposite hemispheres and rarely overlap. State of Origin (Queensland vs New South Wales) is the highest-profile domestic series in the NRL suite and generates token/market movements comparable to major football derbies in the UK. The Challenge Cup final at Wembley is the UK's equivalent peak event.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| NRL season | Mar–Sep (AUS) | 24 rounds; NRL Finals Series in September |
| Super League season | Feb–Oct (UK/EU) | Round-robin + play-offs |
| State of Origin (AUS) | Jun–Jul | 3-game series; highest domestic rugby league audience |
| Challenge Cup | Jan–Jul | Knockout cup, final at Wembley |
| World Club Challenge | Feb | NRL champion vs Super League champion |
| Rugby League World Cup | Oct–Nov (every 4 years) | International peak |
| Super League Grand Final | Oct | Old Trafford — season champion |

### Event Tier System

```
Tier 1: State of Origin (AUS), NRL Grand Final, Rugby League World Cup
Tier 2: Super League Grand Final, Challenge Cup Final
Tier 3: Super League play-offs, NRL Finals Series
Tier 4: Regular season matches (Super League, NRL)
Tier 5: Domestic cups, reserve grade
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| NRL Grand Final win | +15–30% |
| State of Origin series win | +10–22% (state tokens) |
| Super League Grand Final win | +12–25% |
| Challenge Cup Final win | +10–20% |
| World Cup win | +20–40% |
| Regular season win vs rival | +2–5% |
| Key player injury (long-term) | -8–18% |
| Relegation to Championship (Super League) | -15–30% |

---

## Sport-Specific Risk Variables

### State of Origin — Unique Team Selection Risk

State of Origin players are selected by birthplace, not club. Star players' club tokens react to their state performance:

| Event | Impact |
|---|---|
| Player named in Origin squad | +3–8% (club token) |
| Player injured in Origin match | -10–20% (club token — lost for weeks) |
| Player man of the match in Origin | +5–12% (individual token) |

### Super League Relegation System

Super League has a promotion/relegation system unlike NRL:

| Event | Impact |
|---|---|
| Club enters relegation zone | -8–15% |
| Club relegated to Championship | -15–30% |
| Club promoted back to Super League | +10–20% |

---

## Event Playbooks

### Playbook 1: State of Origin Series Opener
```
trigger:  Game 1 of State of Origin series announced
entry:    Week of Game 1
exit:     Post-series result (all 3 games)
filter:   Player is named captain or marquee player for their state
sizing:   1.0× per game; 1.25× for series decider (Game 3)
note:     State of Origin is the most-watched annual rugby league event.
          Individual star player tokens react strongly to Origin performance.
```

### Playbook 2: Challenge Cup Final
```
trigger:  Challenge Cup Final confirmed (both finalists known)
entry:    Week of final
exit:     Final result + 2h
filter:   Club token is on-chain and liquid
sizing:   1.25× — Wembley final is the UK rugby league showcase
note:     Challenge Cup is open — upsets are possible and generate
          large token movements for smaller club winners.
```

### Playbook 3: Super League Play-Off Run
```
trigger:  Club qualifies for Super League play-offs (top 6)
entry:    Play-off entry confirmation
exit:     Elimination OR Grand Final
filter:   Club is top-3 seed; consistent home record in play-offs
sizing:   0.8× per round; scale up to 1.25× in Grand Final
note:     Super League play-offs are sudden death elimination.
          Each round win = sustained token momentum. Hold through.
```

---

## Agent Reasoning Prompts

```
1. Distinguish NRL (Australia) from Super League (UK) — different calendars, different audiences.
2. State of Origin is the highest-profile domestic rugby league event globally.
   Star player tokens react to Origin selection and performance.
3. Super League relegation is a structural negative — exit on relegation signals.
4. Challenge Cup has genuine upset potential — size smaller on paper favourites.
5. World Club Challenge (Feb) pits NRL vs Super League champion — unique cross-code interest.
```

---


---

## Signal Weight Adjustments

For Rugby League, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 25% | Institutional positioning in rugby token markets |
| Social sentiment | 15% | Moderate social signal |
| Sports catalyst | 35% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 10% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/rugby-league/sport-domain-rugby-league.md` | Every analysis |
| Athlete modifier | `athlete/rugby-league/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-rugby-league.md` | Commercial decisions |

## Data Sources

- **Official:** NRL (nrl.com), Super League (superleague.co.uk)
- **Stats:** NRL Stats (stats.nrl.com)
- **Rugby League Project:** rugbyleagueproject.org
- **Odds and prediction:** Betfair Exchange, Oddschecker

## Compatibility

**Pairs with athlete skill:** `athlete/rugby` (shared structure with rugby union)
**Recommended:** `signal-scores`, `oracle-signals`

*MIT License · SportMind · sportmind.dev*

### Playbook 4: State of Origin — Game 3 (decider)
```
trigger:  State of Origin Game 3 when series tied 1-1
entry:    48h before kickoff on squad announcement
exit:     Full time — series decider often tight; no early exit
filter:   Key players confirmed (check Origin availability carefully — some NRL clubs
          withhold players citing injury; verify through official State of Origin squads);
          load core-officiating-intelligence.md for referee assignment
sizing:   1.4× standard — State of Origin Game 3 is the highest-intensity single match
          in rugby league; outsized engagement and prediction market activity
note:     State of Origin Game 3 deciders are documented as the highest social volume
          events in Australian sport. NSW vs QLD rivalry is multi-generational.
          Home ground advantage shifts — Sydney for NSW, Brisbane for QLD — matters.
```
