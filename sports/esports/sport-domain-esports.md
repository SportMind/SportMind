# Esports — SportMind Domain Skill

Sport-specific intelligence layer for eSports fan tokens on Chiliz Chain.
Pairs with `signal-scores`, `whale-intel`, `order-router`, and `prematch-alpha` from the core fan-token-skills toolkit.

---

## Overview

eSports is the most structurally complex sport for fan token intelligence. Unlike football or basketball,
eSports operates across **multiple entirely separate games**, each with its own calendar, meta, and
fan community. A token for a League of Legends team has almost no correlation with the same org's
CS2 roster performance — they must be treated as distinct assets.

eSports also has the youngest and most digitally-native fanbase of any sport, making social sentiment
signals faster-moving and more volatile than any other category.

---

## Domain Model

### Title-Level Token Architecture

eSports tokens are typically org-level (e.g., Team Vitality, Natus Vincere, Fnatic), not game-level.
However, an org's token price is driven primarily by whichever of their rosters is currently in a
major tournament — the "active title" at any given moment.

```
token_price_driver = max_active_tournament_importance(org.all_rosters)

Where rosters may include:
  - CS2 (Counter-Strike 2) — highest global viewership
  - League of Legends — highest Asian viewership, Worlds is peak event
  - Valorant — fastest growing, Riot Games circuit
  - Dota 2 — The International is highest prize pool in eSports
  - FIFA / EA FC — most accessible, football crossover audience
  - Rocket League — growing, unique audience
  - Rainbow Six Siege — niche but established circuit
```

### Tournament Circuits by Game

#### CS2 (Counter-Strike 2) — Tier 1
- **ESL Pro League** (3 seasons/year) — group stage + playoffs
- **BLAST Premier** (circuit system) — Spring/Fall finals
- **ESL/FACEIT Majors** (2/year) — THE highest-impact CS2 events
- **IEM Katowice, IEM Cologne** — premier non-major tournaments
- **Impact rule:** Major wins generate the largest token movements in eSports

#### League of Legends — Tier 1
- **Regional splits:** LEC (Europe), LCS (NA), LCK (Korea), LPL (China) — Spring + Summer
- **Mid-Season Invitational (MSI)** — May international event
- **Worlds (World Championship)** — October–November, peak annual event
- **Impact rule:** Worlds is the single largest eSports event for token price; MSI is secondary

#### Valorant — Tier 1 (Growing)
- **VCT Circuit:** Americas, EMEA, Pacific leagues + Masters + Champions
- **Champions** (August–September) — annual world championship
- Riot-controlled format, stable calendar, growing viewership

#### Dota 2 — Tier 1 (Niche)
- **Majors circuit** — 3–4 majors per year
- **The International** — October, highest eSports prize pool (~$20M+)
- Smaller token audience but extremely passionate community

#### EA FC / FIFA — Tier 2
- **ePremier League, eChampions League** — football org crossover
- Relevant for football club orgs with eSports divisions
- Lower liquidity, higher crossover with football fan token audience

---

### Meta Risk — eSports-Specific Variable

Every competitive game has a "meta" — the dominant strategies, characters, and mechanics at a given patch.
A patch update can make a team's strategy obsolete overnight. This has no equivalent in traditional sports.

```
meta_risk_events:
  - Patch update (especially mid-tournament): HIGH RISK
  - New champion/agent/weapon release: MODERATE (adaptation required)
  - Map pool change: MODERATE
  - Rule change (format, scoring): LOW-MODERATE

Agent rule: If a major patch drops within 2 weeks of a tournament,
apply a 0.7× confidence multiplier to performance-based signals.
Teams with "patch-flexible" playstyles (known adaptors) are lower risk.
```

### Roster Change Risk

Player transfers in eSports are frequent and public. A roster move can:

| Change | Impact |
|---|---|
| Star player transfer (to team) | +8–20% announcement |
| Star player transfer (away) | -10–25% |
| Coach change (head coach) | -3–8% (stability concern) |
| Full roster rebuild | -10–30% (performance uncertainty) |
| Boot camp / roster lock-in | +2–5% (stability signal) |

**Transfer windows:** Unlike traditional sports, eSports has no fixed window — moves happen year-round,
but cluster around end-of-season (post-Worlds / post-Majors) in November–December.

### Result Impact Matrix (eSports)

| Result | Token Impact |
|---|---|
| Group stage win (regular) | +1–3% |
| Playoff bracket win | +3–8% |
| Tournament semifinal reached | +5–10% |
| Tournament win (non-major) | +8–18% |
| Major / Worlds win | +20–50% |
| Early elimination (group stage exit) | -5–15% |
| Relegation (dropped to tier 2) | -15–30% |

---

### Social Signal Velocity

eSports has the fastest social signal decay of any sport:
- Twitch/YouTube live viewership peaks are 2–6h events
- Twitter/X momentum for eSports is measured in hours, not days
- Reddit / Discord communities react in real-time during matches

**Rule:** For eSports, the `-15m` prematch-alpha window and the intra-match social feed are
more predictive than the `-24h` window. Social momentum signals should be weighted 1.5× for eSports
vs the default 1.0× weighting in `signal-scores`.

---

## Season / Tournament Calendar Overview

| Month | Key Events |
|---|---|
| Jan–Feb | IEM Katowice (CS2), LEC/LCS Spring begins, LCK Spring |
| Mar | VCT EMEA/Americas kickoff, ESL Pro League |
| Apr | LoL Spring Finals, CS2 Majors season build |
| May | MSI (LoL), BLAST Premier Spring, Dota 2 Majors |
| Jun | ESL Pro League Finals |
| Jul | VCT Masters, LoL Summer begins |
| Aug | IEM Cologne (CS2), Valorant Champions |
| Sep | CS2 Major (Fall), LoL Summer Finals |
| Oct–Nov | LoL Worlds (PEAK), The International (Dota 2), BLAST Premier Fall |
| Dec | Off-season, roster shuffles, transfer window |

**Highest-impact window:** October–November. LoL Worlds and The International overlap with CS2 Fall Major,
creating the densest concentration of major eSports events in the calendar year.

---

## Event Playbooks

### Playbook 1: Major / Worlds Run Long
```
trigger: org qualifies for CS2 Major, LoL Worlds, or Valorant Champions
entry:   qualification announcement (bracket placement day)
scale:   add at each playoff round won
exit:    elimination OR trophy lift
filter:  org has won or reached finals of equivalent event in prior 12 months
sizing:  0.6× at qualification, +0.2× per playoff round advanced
note:    Worlds / Major runs can generate the largest sustained gains in eSports
```

### Playbook 2: Patch Drop Fade
```
trigger: major patch released within 10 days of tournament start
signal:  team's known play style heavily dependent on nerfed mechanics
action:  reduce position by 30–50% until first match results confirm adaptation
exit:    resume standard position after 2+ wins on new patch
note:    "one-trick" orgs are highest risk; versatile rosters are lowest
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

### Playbook 3: Transfer Window Catalyst
```
trigger: marquee player joins org (announced on Twitter/X, verified)
entry:   within 2h of announcement
exit:    +48h (narrative fades; next catalyst is first match together)
filter:  player ranked top 20 in their game globally by tournament earnings/rating
sizing:  0.7× (unverified until first match performance)
```

### Playbook 4: Relegation Zone Alert
```
trigger: org placed in relegation match / promotion tournament
signal:  oracle bearish signal + whale distribution
action:  reduce or exit — relegation to tier 2 is a major negative structural event
note:    some orgs dissolve rosters entirely after tier 2 relegation
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

### Playbook 5: October–November Stack
```
trigger: calendar enters Oct 1 with org active in 2+ Tier 1 tournaments
action:  increase baseline position in October — highest event density of the year
scale:   monitor each tournament independently; add on each advancement
exit:    post-Worlds / post-Major, before December roster shuffle begins
sizing:  1.25× standard (event density justifies higher exposure)
filter:  standard availability and macro checks apply
```

---

## Key Commands

| Command | Skill | Use Case |
|---|---|---|
| `get_signal_scores` | signal-scores | Social component is 1.5× weighted for eSports |
| `get_score_detail` | signal-scores | Isolate social momentum from sports catalyst component |
| `get_whale_flows` | whale-intel | Smart money ahead of Major / Worlds events |
| `get_upcoming_alpha` | prematch-alpha | Pre-match packets — focus on -2h and -15m windows |
| `get_oracle_signals` | oracle-signals | Bearish distribution: patch risk, roster instability |
| `run_backtest` | backtest-engine | Simulate tournament-run strategies on historical data |
| `execute_trade` | order-router | Rapid post-result execution across 13 exchanges |

---

## Agent Reasoning Prompts

```
You are an eSports fan token trading agent. Before acting on any signal:
1. Identify WHICH game is the primary driver of this token right now.
   An org's token is driven by its highest-profile active roster.
2. Check the patch date — if a major patch dropped within 10 days of a
   tournament, reduce conviction on performance signals by 30%.
3. eSports social signals move FAST. Prioritise the -2h and -15m windows
   over -24h for eSports-specific plays.
4. Roster changes are year-round risks. Always check for recent transfer
   news before entering a position ahead of a tournament.
5. October–November is peak season. Higher baseline exposure is justified
   if the org is active in multiple Tier 1 events simultaneously.
6. Relegation is a structural event — not a dip to buy. Exit on relegation signals.
```

---

## Data Sources
- Tournament data: HLTV (CS2), Liquipedia (all games), Riot Games circuit feeds
- Player/roster: HLTV player rankings, Liquipedia roster pages
- Viewership: Esports Charts live peak concurrent
- Social sentiment: LunarCrush galaxy score + org social handles
- Price correlation: match_price_correlation adapted for tournament match events

---


---

## Signal Weight Adjustments

For Esports, agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | 15% | Institutional positioning in esports token markets |
| Social sentiment | 40% | High narrative-driven fanbase |
| Sports catalyst | 25% | Primary signal driver — the sporting event itself |
| Price trend | 15% | Supporting signal |
| Macro | 5% | CHZ/BTC cycle backdrop |

*See `core/core-signal-weights-by-sport.md` for full signal weight rationale.*

## Compatibility

`signal-scores` social component is the highest-signal input for eSports — weight it accordingly.
`prematch-alpha` is useful but prioritise shorter windows (-2h/-15m) over -24h for eSports.
`oracle-signals` is valuable for detecting institutional exit ahead of patch/roster risk events.

```
npx skills add sportmind/fan-token
```

---
MIT License · SportMind · sportmind.dev

## Fan Token Layer

For esports-specific fan token intelligence — OrgTIS, Game Roster Multiplier (GRM),
Patch Risk Score (PRS), Roster Stability Index (RSI), and multi-game October-November
stack window detection — load the dedicated bridge skill:

**`fan-token/esports-token-intelligence`**

Recommended agent chain for esports fan token decisions:
```
sports/esports                              ← domain context (this skill)
  + fan-token/fan-token-pulse               ← on-chain baseline
  + fan-token/esports-token-intelligence    ← esports-specific token intelligence
  + fan-token/athlete-social-lift           ← social signal (fastest in esports)
```

---
MIT License · SportMind · sportmind.dev
