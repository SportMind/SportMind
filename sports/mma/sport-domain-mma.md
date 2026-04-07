# Mixed Martial Arts (MMA) — SportMind Domain Skill

Sport-specific intelligence layer for MMA fan tokens on Chiliz Chain.
Pairs with `signal-scores`, `whale-intel`, `prematch-alpha`, and `oracle-signals` from the core fan-token-skills toolkit.

---

## Overview

MMA is the most event-concentrated sport in this ecosystem. Unlike football or basketball where tokens are
tied to clubs, MMA fan tokens are typically **fighter-centric** — the token IS the athlete. This makes
MMA uniquely high-risk/high-reward: a single fight card is the equivalent of an entire football season
compressed into one night.

Promotions to cover: UFC (dominant), Bellator/PFL (secondary), ONE Championship (Asia), KSW (Europe).

---

## Domain Model

### MMA Token Architecture

MMA tokens differ fundamentally from club tokens:

| Dimension | Club Token (Football) | Fighter Token (MMA) |
|---|---|---|
| Underlying asset | Team performance | Individual athlete |
| Event frequency | Weekly | Monthly or less |
| Career risk | Relegation | Retirement, injury, losing streak |
| Peak catalyst | Derby / final | Title fight / PPV main event |
| Sentiment driver | Squad + manager | Fighter + camp + opponent |

**Critical rule:** Fighter tokens can go to near-zero on retirement or career-ending injury.
This is an existential risk that has no equivalent in club token trading.

### Fight Card Hierarchy

UFC structures its events in a clear hierarchy — this directly determines token impact:

| Event Type | Frequency | Token Impact |
|---|---|---|
| UFC PPV (numbered events) | ~14/year | Highest — title fights, PPV buys, global audience |
| UFC Fight Night (main card) | ~30/year | Moderate — performance bonuses, ranked fighters |
| UFC Fight Night (prelims) | Same events | Low — unranked fighters, limited token exposure |
| Bellator / PFL main event | Monthly | Moderate for specific tokens |
| ONE Championship | Bi-weekly | Asia-focused, growing relevance |

### Fight Week Calendar

MMA has a distinct "fight week" structure that creates a multi-day alpha window:

```
Day -7:  Fight announced / opponent confirmed → initial social spike
Day -3:  Open workouts / media day → sentiment check
Day -2:  Weigh-ins → CRITICAL (see Weigh-In Risk below)
Day -1:  Ceremonial weigh-ins / face-off → social momentum peak
Day 0:   Fight night → price event
Day +1:  Post-fight → result digestion, title change confirmation
```

Use `prematch-alpha` windows mapped to this structure:
- `-24h` window → Day -1 (ceremonial weigh-in sentiment)
- `-2h` window → walk-out / preliminary card
- `-15m` window → main event imminent

### Weigh-In Risk — Unique MMA Variable

Weigh-ins are a binary risk event with no football equivalent:

| Weigh-In Outcome | Token Impact |
|---|---|
| Makes weight cleanly | Neutral to +2% (confirmation) |
| Misses weight (fighter's token) | -10–25% immediate |
| Opponent misses weight | +3–8% (opponent fined, fight may still proceed) |
| Fight cancelled (both miss / injury) | -15–35% |

**Rule:** Never hold a large position through weigh-ins without a risk-off plan.
Monitor social sentiment in the 2h window before weigh-ins — early leaks are common.

### Result Impact Matrix (MMA)

| Result | Winner Token | Loser Token |
|---|---|---|
| Win by KO/TKO (finish) | +15–40% | -15–30% |
| Win by submission | +12–30% | -10–25% |
| Win by decision | +5–15% | -5–12% |
| Draw | -3–8% both (unsatisfying) | |
| No contest / DQ | -10–20% both | |
| Title won | +25–60% | -20–40% |
| Title lost | -20–45% | +25–55% |

**Note:** Finishes (KO/TKO/sub) produce larger moves than decisions — method of victory matters.

### Fighter Career Risk Events

These are existential signals requiring immediate position review:

```
HIGH RISK (consider exit):
- Retirement announcement
- Career-ending injury (orbital fracture, ACL, neck)
- Suspension (USADA/WADA drug violation)
- Legal issues (criminal charges)
- Multiple consecutive losses (3+ in a row)
- Significant weight class move (performance uncertainty)

MODERATE RISK (reduce sizing):
- Cut from promotion (released by UFC)
- Failed weight cut (pattern, not one-off)
- Prolonged layoff (12+ months, age-related decline risk)

POSITIVE CATALYSTS:
- Title contender ranking achieved
- Superfight / crossover event announced (e.g. boxing match)
- Viral moment (Embedded series, interview)
- Fight of the Night / Performance of the Night bonus
```

---

## Competition Reference

### UFC (Primary)
- Dominant MMA promotion globally
- PPV events: title fights, rematches, superfights
- Key title belts: Heavyweight, Light Heavyweight, Middleweight, Welterweight,
  Lightweight, Featherweight, Bantamweight, Flyweight + Women's divisions
- Monitor: ESPN+ fight announcements, UFC rankings updates (weekly, Tuesdays)

### Bellator / PFL (Secondary)
- Bellator: established roster, Paramount/Showtime distribution
- PFL: season-format (wins = points → playoffs → $1M prize), unique structure
- PFL playoff format creates multi-event narrative arcs — tokens can run across a season

### ONE Championship (Asia)
- Mixed ruleset (MMA + Muay Thai + Kickboxing on same card)
- Growing Asian fan token market
- Events bi-weekly, primarily Singapore/Bangkok

### KSW (Europe)
- Poland-based, largest European MMA promotion
- Niche but relevant for European market fan tokens

---

## Event Playbooks

### Playbook 1: Title Fight Long (Pre-Event)
```
trigger: UFC PPV title fight announced with fighter token on-chain
entry:   Fight announcement day (Day -7) — small initial position
scale:   Add at Day -2 (post-weigh-in, IF fighter makes weight)
exit:    Day 0 post-fight (within 1h of result)
filter:  fighter ranked favourite (odds < -150), no weigh-in miss history
sizing:  0.8× standard pre-announcement, 1.5× post-weigh-in clean
risk:    Hard stop if fighter misses weight — exit immediately
```

### Playbook 2: Weigh-In Confirmation Entry
```
trigger: fighter makes weight cleanly at official weigh-ins
entry:   within 30min of weigh-in confirmation
exit:    post-fight (same day)
filter:  fighter is favourite or slight underdog (-200 to +150)
sizing:  1.0× standard — post-weigh-in is highest-conviction entry point
note:    this removes the weigh-in binary risk entirely
```

### Playbook 3: Upset Aftermath
```
trigger: significant underdog wins (odds > +250)
action:  Winner token — entry within 30min of result
exit:    +48–72h (narrative builds: "who's next?" / title shot talk)
filter:  winner token exists on-chain, finish (KO/sub preferred over decision)
sizing:  1.25× — upset victories generate outsized social momentum
```

### Playbook 4: Retirement Risk Fade
```
trigger: fighter announces retirement OR takes career-ending loss at 35+
signal:  oracle bearish signal + social negative spike
action:  exit position immediately, do not average down
note:    fighter tokens can lose 50–80% of value post-retirement
         this is a structural exit, not a tactical one
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

### Playbook 5: Superfight Announcement Pump
```
trigger: crossover event announced (UFC vs boxing, MMA legend vs celebrity)
entry:   announcement hour
exit:    +72h (hype front-loaded; actual event months away)
sizing:  0.5× (narrative play, not performance signal)
note:    Conor McGregor-type crossovers are highest-magnitude version of this
filter:  standard availability and macro checks apply
```

---

## Key Commands

| Command | Skill | Use Case |
|---|---|---|
| `get_signal_scores` | signal-scores | Social component critical — MMA is highly narrative-driven |
| `get_upcoming_alpha` | prematch-alpha | Map fight week windows to -24h/-2h/-15m structure |
| `get_whale_flows` | whale-intel | Accumulation ahead of PPV events |
| `get_oracle_signals` | oracle-signals | Bearish distribution ahead of fight or career risk |
| `get_distribution_alerts` | whale-intel | Smart money exiting ahead of high-risk events |
| `execute_trade` | order-router | Speed matters post-result — best-price routing |
| `run_backtest` | backtest-engine | Simulate fight-night strategies on historical data |

---

## Agent Reasoning Prompts

```
You are an MMA fan token trading agent. Before acting on any signal:
1. Identify whether the token is for an active fighter in a scheduled fight.
   If no fight scheduled, volume and alpha are minimal.
2. ALWAYS check weigh-in status before fight-day entry.
   A missed weight cut invalidates a long thesis immediately.
3. Method of victory matters — track whether a fighter tends to finish
   (KO/sub) or go to decisions. Finishers generate larger post-win moves.
4. Fighter career stage matters: a 35+ year old on a 2-fight losing streak
   carries retirement risk — apply a structural discount.
5. Superfight and crossover announcements are narrative events, not
   performance signals. Size them accordingly.
6. MMA titles are zero-sum: one token pumps, the other dumps simultaneously.
   Never hold both sides of a title fight.
```

---

## Data Sources
- Fight cards: UFC / Bellator / ONE Championship event feeds
- Fighter rankings: UFC rankings (updated weekly)
- Social sentiment: LunarCrush galaxy score + fighter social handles
- Weigh-in results: ESPN MMA, MMA Fighting, Tapology
- Price correlation: match_price_correlation adapted for fight events

---


---

## Signal Weight Adjustments

For Mixed Martial Arts (MMA), agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 15% | Institutional positioning in mixed token markets |
| Social sentiment | 35% | High narrative-driven fanbase |
| Sports catalyst | 30% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*

## Compatibility

`prematch-alpha` maps cleanly — treat fight night as "kickoff", weigh-ins as a new signal layer.
`oracle-signals` is especially important: MMA has more existential downside risks than any other sport.
`signal-scores` social component is highest-weighted signal for MMA (most narrative-driven sport).

```
npx skills add sportmind/fan-token
```

---
MIT License · SportMind · sportmind.dev

## Fan Token Layer

For MMA-specific fan token intelligence — fighter token multipliers (FTM), career risk
index (CRI), fight week signal maps, weigh-in risk assessment, and post-fight token
trajectory modelling — load the dedicated bridge skill:

**`fan-token/mma-token-intelligence`**

Recommended agent chain for MMA fan token decisions:
```
sports/mma                            ← domain context (this skill)
  + fan-token/fan-token-pulse         ← on-chain baseline
  + fan-token/mma-token-intelligence  ← MMA-specific token intelligence
  + fan-token/athlete-social-lift     ← live FTM confirmation
```

---
MIT License · SportMind · sportmind.dev

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-mma.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

