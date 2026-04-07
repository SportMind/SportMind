# Golf — SportMind Domain Skill

Sport-specific intelligence layer for golf fan tokens, prediction markets, and tournament outcome signals.
Covers PGA Tour, DP World Tour (European Tour), LIV Golf, and Major championships.

---

## Overview

Golf is an individual sport with a uniquely extended event window — a tournament spans four days, with
cut lines, weather delays, and leaderboard swings creating multiple distinct signal moments. Unlike team
sports, golf tokens are **player-centric**: the token IS the athlete, so form, injury, course fit, and
mental state carry enormous weight. The PGA Tour vs LIV Golf schism has also created a fractured calendar
that agents must navigate carefully when assessing event importance.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token / Prediction Behaviour |
|---|---|---|
| January warm-up | Jan | Low significance — Hawaii, Middle East events; speculative only |
| Pre-Masters swing | Feb–Mar | Rising interest, Florida swing; course-fit signals emerge |
| The Masters | Apr (first full week) | Highest single-event impact of the golf calendar |
| Spring Major season | May–Jun | PGA Championship (May), US Open (Jun) — top-3 impact events |
| Wimbledon / Open overlap | Jul | The Open Championship — prestige event, British audience peak |
| Summer swing | Aug | FedEx Cup Playoffs begin; season-defining points events |
| FedEx Cup Finals | Aug–Sep | Tour Championship — season climax, elevated stakes |
| Ryder Cup / Presidents Cup | Sep (odd years) | Team event — massive social catalyst, individual token relevance |
| LIV Golf season | Mar–Nov | Parallel calendar — separate ranking system, growing fan base |
| Off-season | Nov–Dec | Minimal signal; transfer news (LIV vs PGA) drives narrative |

**Rule:** The four Majors (Masters, PGA Championship, US Open, The Open) are tier-1 events and produce
the largest token movements. Non-Major events are tier-2 at best unless they are FedEx Cup playoffs or
the Ryder Cup.

### Tournament Structure — How Golf Events Work

Golf tournaments run Thursday–Sunday (4 rounds of 18 holes). The cut after round 2 is a critical signal:

```
Round 1 (Thursday):  Early leaderboard — course-fit signal emerges
Round 2 (Friday):    Cut line determined — typically top 65+ties make cut
                     AGENTS: player missing cut = major negative signal
Round 3 (Saturday):  "Moving day" — leaderboard compresses or separates
Round 4 (Sunday):    Final round — back-9 Sunday drama is highest-volatility window
```

### Event Tier System

```
Tier 1 — Majors (highest impact):
  The Masters        Augusta National, April — most prestigious
  PGA Championship   Rotation, May
  US Open            Rotation, June
  The Open           Rotation, July — oldest Major

Tier 2 — Elevated events:
  Players Championship   "5th Major" — strongest non-Major field
  FedEx Cup Playoffs    3-event series deciding season champion
  Ryder Cup (odd years) Europe vs USA — team format, huge social signal
  Genesis Invitational, Arnold Palmer, etc. — elevated PGA events

Tier 3 — Standard events:
  Regular PGA Tour / DP World Tour events
  LIV Golf League events (growing, but separate ecosystem)

Tier 4 — Low signal:
  Pre-season events, pro-ams, secondary tour events
```

### Result Impact Matrix

| Result | Token / Market Impact |
|---|---|
| Major win | +25–55% |
| Major top-5 (no win) | +8–18% |
| Major missed cut | -8–18% |
| Players Championship win | +12–25% |
| FedEx Cup won | +15–30% |
| Ryder Cup point scored (team win) | +5–12% |
| Standard PGA Tour win | +5–15% |
| Missed cut (standard event) | -3–8% |
| Injury withdrawal mid-tournament | -10–25% |
| World No. 1 ranking achieved | +8–20% |
| LIV Golf defection announced | -5–20% (PGA token) / +5–15% (LIV token) |

---

## Competition Reference

### The Majors (Tier 1)

**The Masters** — Augusta National, first full week of April. Most prestigious event. Course suits
specific shot shapes — agents should check historical Augusta performance, not just current form.
Green jacket winner sees largest single-event token pump in golf.

**PGA Championship** — May, rotation of major US venues. Second Major. Often produces first-time
winners; form signals are reliable here.

**US Open** — June, rotation. Known for brutal course setups — elite ball-strikers and patience
are rewarded. Identify players with US Open historical records.

**The Open Championship** — July, UK rotation (St Andrews, Royal St George's, Hoylake, etc.).
Links golf; wind and weather are critical variables. Check links golf record specifically.

### PGA Tour (Primary US circuit)

- 45+ events per season, FedEx Cup points structure
- Elevated events carry higher points and better fields
- FedEx Cup Playoffs: FedEx St. Jude → BMW → Tour Championship (staggered starts)
- Players without Tour card cannot compete — check status each season

### DP World Tour (European Tour)

- Co-sanctioned events with PGA Tour increasing
- Rolex Series events = highest tier (Scottish Open, Irish Open, BMW PGA)
- Pathway for European tokens — Ryder Cup qualification driving stakes

### LIV Golf

- Saudi-backed league; 54-hole stroke play (no cut), team format overlay
- Separate ranking system — not counted for Major eligibility historically (changing)
- Biggest names: Dustin Johnson, Brooks Koepka, Jon Rahm
- Token implications: LIV defection creates narrative uncertainty for PGA-affiliated tokens

---

## Sport-Specific Risk Variables

### Cut Line Risk

The most unique golf risk variable — players who miss the cut earn nothing and play no further.

| Cut outcome | Token / Market impact |
|---|---|
| Makes cut comfortably (top 30) | Neutral to +2% (confirmation) |
| Makes cut on the number | Neutral — relief rally small |
| Misses cut by 1–2 shots | -5–10% |
| Misses cut by 5+ shots | -10–18% |
| Missed cut in Major | -12–22% |

**Agent rule:** Check cut line projections after round 2 (Friday afternoon). A missed cut is
confirmed information — do not wait for the full tournament to close a position.

### Weather Window Risk

Golf is uniquely weather-dependent. Tee time draws create have/have-not conditions within the same round:

| Weather condition | Signal impact |
|---|---|
| Strong wind at course (>25 mph) | Increases variance — low scorers get lucky tee times |
| Rain delay / suspension | Extends tournament to Monday — sentiment uncertainty |
| Soft conditions | Scoring low — favours aggressive players |
| Firm, fast conditions | Scoring high — favours precision players |

**Agent rule:** Check tee time draw and forecast. A favourite in poor morning wave is significant.

### Putting Form vs Course History

Golf performance is split between ball-striking (stable, form-based) and putting (volatile, course-specific):

| Signal | Reliability |
|---|---|
| Ball-striking metrics (driving, approach) | HIGH — stable across venues |
| Course-specific putting history | HIGH — greens memory is real |
| Recent putting form alone | MODERATE — volatile week to week |
| General current form (recent finishes) | MODERATE — good but not definitive |

**Agent rule:** Prioritise course history at venues played repeatedly (Augusta, St Andrews) over
general recent form. Augusta especially — previous performance there is highly predictive.

### LIV vs PGA Split Risk

The fractured tour landscape creates structural risk for player tokens:

| Event | Token impact |
|---|---|
| Player defects to LIV (PGA token) | -5–20% immediately; long-term brand risk |
| LIV player announces return to PGA | +5–15% (increased Major access) |
| Major exemption granted to LIV player | +3–8% (competitive relevance restored) |
| PGA / LIV merger rumours | High volatility both sides |

---

## Event Playbooks

### Playbook 1: Major Championship Long
```
trigger:  Major week begins (Monday of Major week)
entry:    Monday–Tuesday — pre-tournament entry on favourite
exit:     After round 4 (Sunday evening)
filter:   Player in top-10 world ranking, strong course history
          (Augusta: previous top-10; Open: links golf record)
sizing:   1.5× standard — Majors produce largest moves
note:     Enter smaller on Monday, add if player leads or co-leads after R2.
          Exit immediately on missed cut. Do not hold through the weekend
          if player falls outside top-20 after R3.
```

### Playbook 2: Cut Line Confirmation Entry
```
trigger:  Player makes cut in top-15 after round 2
entry:    Friday evening post-cut confirmation
exit:     Sunday close
filter:   Player is pre-tournament favourite or top-3 world ranking
          No active injury concerns
sizing:   1.0× standard — cut confirmation removes binary risk
note:     This is the highest-conviction entry point in golf.
          Cut is made, field is reduced, leaderboard is real.
          Add if player leads or within 3 shots after R3 (Saturday).
```

### Playbook 3: Ryder Cup Team Win Pump
```
trigger:  Ryder Cup concludes — winning team's players' tokens
entry:    Immediately post trophy ceremony
exit:     +72h (celebration cycle; fades after day 3)
filter:   Player contributed positive points record in the event
          Token is on-chain and liquid
sizing:   1.0× standard
note:     Ryder Cup is team not individual — broad sentiment lift
          for all winning team members. Check points contribution:
          a player going 0-4 in a winning team sees muted individual lift.
```

### Playbook 4: World Ranking Breakthrough
```
trigger:  Player achieves new career-high world ranking (top-10 first time)
entry:    Ranking announcement (Monday)
exit:     +48h
filter:   Player won the event that triggered the ranking rise
          (ranking without win = lower conviction)
sizing:   0.8× — narrative event, not in-play result
note:     World No. 1 is a specific milestone — +8–20% historically.
          Top-10 for first time = +5–12%. New rankings release Mondays.
```

### Playbook 5: Injury Withdrawal Fade
```
trigger:  Player withdraws mid-tournament or announces injury ahead of event
signal:   Oracle bearish signal + social negative spike
action:   Exit or reduce position immediately
timing:   Within 1h of confirmed withdrawal announcement
note:     Back injuries are the most common golf withdrawal — they
          often signal multi-month absence. Check injury type:
          back/wrist = long timeline; flu/cold = short timeline.
          Do not average down on withdrawal news.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Tournament result is the primary driver |
| Social sentiment | 20% | Golf social moves fast on Sunday back-nine drama |
| Market / whale flows | 20% | Institutional positioning pre-Major is meaningful |
| Price trend | 15% | Form correlation is real but lagging |
| Macro | 10% | Minimal — golf tokens are sport-isolated |

---

## Key Commands

| Action | Skill | Command | Use case |
|---|---|---|---|
| Get upcoming tournament schedule | sports-data | `get_fixtures` | Identify Major and elevated event windows |
| Player form and ranking | athlete/golf | `get_player_form_score` | Assess recent tournament performance |
| Course history | athlete/golf | `get_course_history` | Augusta, Open venue historical records |
| Cut line status | athlete/golf | `get_cut_line_status` | Round 2 cut confirmation signal |
| Weather at venue | athlete/meta | `get_weather_impact` | Wind and conditions modifier |
| Whale flows | whale-intel | `get_whale_flows` | Pre-Major institutional positioning |
| Social momentum | signal-scores | `get_signal_scores` | Sunday leaderboard social spike detection |

---

## Agent Reasoning Prompts

```
You are a golf sports intelligence agent. Before evaluating any golf tournament or player token:

1. Identify the event tier first. Only Majors and elevated events justify full position sizing.
   Standard Tour events warrant 0.5× or less.

2. Check round number. Entry conviction increases with each round:
   Pre-tournament = speculative, post-R2 cut = confirmation, post-R3 leader = highest conviction.

3. Cut line is binary. A player who misses the cut plays no more golf that week.
   Always set a hard stop on missed cut — do not hold through the weekend.

4. Course history matters more than recent form at iconic venues.
   Augusta (Masters), St Andrews (Open) — past performance there is the primary signal.

5. Weather creates advantage/disadvantage within rounds. Check tee time draw and
   forecast. A favourite in a brutal morning wave is a significant risk factor.

6. LIV vs PGA context matters for player token valuation.
   LIV defectors have restricted Major access — adjust tier-1 event probability accordingly.

7. Sunday back-nine is the highest-volatility window in golf.
   Social sentiment spikes fast. Position management matters — take partial profits if
   player holds 54-hole lead entering final round.
```

---

## Data Sources

- Tournament schedule and results: PGA Tour official API, DP World Tour
- World rankings: Official World Golf Rankings (OWGR), updated Mondays
- Player stats: PGA Tour ShotLink (strokes gained, driving, approach, putting)
- Course history: PGA Tour historical stats, European Tour stats
- Weather: Open-Meteo venue-specific forecasts
- Social sentiment: LunarCrush galaxy score + player social handles

---

## Compatibility

**Pairs with athlete skill:** `athlete/golf`

**Recommended core skills:**
- `athlete/meta` — weather overlay is particularly important in golf
- `signal-scores` — social component elevated on Major Sundays
- `whale-intel` — pre-Major accumulation patterns exist

**Optional:**
- `backtest-engine` — simulate Major week strategies on historical data
- `oracle-signals` — bearish distribution ahead of withdrawal risk

---

*MIT License · SportMind · sportmind.dev*
