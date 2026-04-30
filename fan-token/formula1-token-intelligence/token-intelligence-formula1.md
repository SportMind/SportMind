---
name: formula1-token-intelligence
description: >
  Formula 1 specific fan token intelligence. Use when the user asks about F1
  constructor or driver token impact from race events, qualifying results,
  championship standings, driver transfers, regulation changes, or any
  on-chain signal tied to F1. Produces FTIS (F1 Token Impact Score),
  Constructor Token Index (CTI), and Driver Token Multiplier (DTM).
  Load alongside sports/formula1 and fan-token-pulse.
---

# Formula 1 Token Intelligence

The bridge between the F1 sporting calendar and the fan token ecosystem.
F1 is the second-most developed sport in the Chiliz fan token ecosystem after
football. Its unique dual-championship structure, annual regulation cycles,
and driver transfer market create token dynamics that no other motorsport
— and no team sport — fully replicates.

---

## What this skill produces

- **F1 Token Impact Score (FTIS)** — Race weekend × championship stakes × token ecosystem composite
- **Constructor Token Index (CTI)** — Relative strength ranking of active constructor tokens
- **Driver Token Multiplier (DTM)** — Individual driver's amplification of their constructor's token
- **Regulation Cycle Position** — Where in the regulation era are we? (affects all valuations)
- **Silly Season Signal** — Driver transfer rumour scoring and token impact forecast
- **Dual-Token Alert** — When driver AND constructor tokens should be assessed together

---

## F1 Token Impact Score (FTIS)

```
FTIS = (
  race_tier_weight        * 0.30 +   # which circuit / event type?
  championship_stakes     * 0.30 +   # how much does this race matter?
  constructor_token_health * 0.20 +  # is the suite active?
  driver_token_multiplier * 0.20     # are high-DTM drivers involved?
) * 100
```

| FTIS | Label | Agent action |
|---|---|---|
| 85–100 | Maximum | Full analysis — qualifying + race + social chain |
| 70–84 | High | fan-token-pulse + pre-qualifying entry assessment |
| 55–69 | Elevated | Monitor; enter post-qualifying on unexpected result |
| 40–54 | Standard | Base signal — standard position sizing |
| 25–39 | Low | Skip or minimal exposure |
| 0–24 | Negligible | Ignore for token purposes |

---

## Constructor Token Index (CTI)

CTI ranks active constructor tokens by their current token ecosystem strength.
Unlike football where all clubs have similar token structures, F1 constructor
tokens vary dramatically in liquidity, holder base, and signal responsiveness.

```
CTI = (
  HAS_score              * 0.35 +   # from fan-token-pulse
  championship_position  * 0.25 +   # current standings (1st = 1.0, 10th = 0.1)
  driver_quality_score   * 0.20 +   # are the drivers generating DTM?
  fan_base_breadth       * 0.20     # geographic token holder distribution
) * 100
```

**CTI tier implications for agent sizing:**
- CTI 75+: Full position sizing applicable
- CTI 50–74: Standard sizing — suite active but not elite
- CTI 25–49: Reduce sizing 30% — thinner liquidity, wider spreads
- CTI <25: Avoid — insufficient token ecosystem for reliable signal

**Constructor CTI approximate ranking (Q1 2026, recalibrate each season):**

| Constructor | CTI range | Key driver of score |
|---|---|---|
| Ferrari | 78–88 | Largest fan base; Tifosi global reach |
| Red Bull Racing | 72–84 | Dominant era legacy; young global base |
| Mercedes | 68–80 | Hamilton era; strong but transition phase |
| McLaren | 60–74 | Rising — results and fan base both growing |
| Aston Martin | 45–60 | Alonso factor; UK premium base |
| Alpine | 38–52 | French-heavy; limited global spread |
| Others | 15–35 | Small suites — exercise caution |

---

## Driver Token Multiplier (DTM)

In F1, individual drivers amplify or dampen their constructor's token signal.
A world champion driving for a midfield team elevates that constructor's CTI
beyond what their results alone would justify. A reserve driver replacing an
injured star depresses it.

```
DTM = (
  career_achievement_score * 0.30 +  # championships, race wins, legendary status
  current_form_score       * 0.25 +  # recent qualifying and race performance
  social_presence_score    * 0.25 +  # following, engagement, narrative presence
  nationality_market_fit   * 0.20    # do driver's fans overlap with token holders?
) normalised to 0.50–1.50
```

### DTM archetypes

**Elite DTM (1.25–1.50) — The Legend**
Profile: Multiple world champion, global following, iconic status. Presence at a
constructor immediately elevates their token narrative beyond race results.
Pattern: Token moves on this driver's QUOTES, not just results. A "we will win
this championship" press conference comment moves the constructor token.
Example archetype: A driver of Schumacher/Hamilton/Verstappen career stature.

**High DTM (1.10–1.24) — The Contender**
Profile: Active title contender, top 5 career wins, strong social presence.
Pattern: Token peaks during championship run-ins and podium streaks. Qualifying
laps become social events that move token prices.

**Standard DTM (0.85–1.09) — The Journeyman**
Profile: Solid race driver, consistent points scorer. Results move the constructor
token normally without individual amplification.

**Low DTM (0.50–0.84) — The Reserve / Rookie**
Profile: Unproven talent or reserve called up. Presence creates uncertainty,
sometimes depressing the constructor token even when they score points.
A rookie replacing an Elite DTM driver is one of the most negative single-event
token impacts in F1 outside of catastrophic mechanical failure.

### DTM and nationality-token overlap

The single most important DTM amplifier: when a driver's nationality matches
a large segment of the constructor token holder base.

| Scenario | DTM adjustment |
|---|---|
| Driver nationality = constructor's #1 holder market | ×1.20 additional |
| Driver nationality = constructor's #2 holder market | ×1.10 additional |
| No nationality-market overlap | ×1.00 (no adjustment) |
| Driver nationality strongly associated with rival constructor | ×0.90 |

---

## Race-by-Race FTIS Reference

### Tier 1 Races (FTIS 80–100)

**Monaco Grand Prix**
```
FTIS baseline: 90
Peak window: Qualifying Saturday (primary) + Race Sunday
Special rule: QUALIFYING IS THE RACE at Monaco.
  Pole = ~75% race win probability.
  Enter constructor/driver token immediately post-qualifying.
  Race day adds confirmation but most of the signal is in qualifying.
Token note: Monaco rewards aerodynamically efficient cars.
  Constructors with top-10 qualifying lock-outs see HAS spikes
  before the race even starts.
```

**Silverstone (British Grand Prix)**
```
FTIS baseline: 84
Peak window: Race weekend (all sessions)
Special rule: Home race premium for UK-heavy constructor tokens
  (McLaren, Aston Martin, Williams if token-active).
Token note: Largest live attendance of any race. Social signal
  is amplified by crowd atmosphere. UK-heavy token holder bases
  respond disproportionately to home race results.
```

**Monza (Italian Grand Prix)**
```
FTIS baseline: 86
Peak window: Race Sunday (Tifosi atmosphere peaks at result)
Special rule: Ferrari token has maximum Monza premium.
  Ferrari win at Monza = highest single-race token impact event
  for a constructor in the calendar (+20–35% historical).
  Ferrari DNF at Monza = maximum negative (-15–28%).
Token note: Monza is a low-downforce circuit. Constructors with
  strong straight-line speed outperform their usual ranking.
```

**Season Finale (Abu Dhabi)**
```
FTIS baseline: 78 (standard year) → 96 (title-deciding year)
Peak window: Race Sunday
Special rule: FTIS scales directly with championship closeness.
  < 10-point gap entering finale: FTIS 96
  < 25-point gap: FTIS 90
  < 50-point gap: FTIS 84
  Already decided: FTIS 60 (still elevated for podium narrative)
```

### Tier 2 Races (FTIS 62–79)

| Race | FTIS | Key signal |
|---|---|---|
| Bahrain GP (often season opener) | 78 | Opener premium: +10 FTIS in regulation-change year |
| Japanese GP (Suzuka) | 76 | Honda/Red Bull market; Asian audience |
| Las Vegas GP (night) | 74 | North American market; spectacle premium |
| Brazilian GP (Interlagos) | 72 | Wet race probability high; South American market |
| Singapore GP (night) | 70 | Street circuit; upset probability elevated |
| Spanish GP (Barcelona) | 65 | High-data circuit; technical baseline |
| Canadian GP (Montreal) | 65 | Street/hybrid circuit; North American timing |
| Hungarian GP (Hungaroring) | 62 | Overtaking difficult; qualifying matters more |

### Sprint Race Weekends
```
Sprint races (~6 per season) add an additional live signal event.
Sprint race result adds +5–10 FTIS to the full weekend score.
Sprint qualifying (SQ) on Friday afternoon is a genuine signal.
Key: Sprint points are real but fewer (max 8 vs 25 for race win).
Constructor token response to Sprint results is approximately 40%
of the response to a main race result of the same finishing position.
```

---

## Championship Stakes Multiplier

The championship context amplies all race signals:

```
championship_stakes_multiplier:
  Race 1 of season:                1.25 (baseline establishment)
  Races 2–8 (early season):        1.00
  Races 9–16 (mid-season):         1.10 (standings clearer, stakes higher)
  Final 5 races (gap < 50 pts):    1.35
  Final 3 races (gap < 25 pts):    1.50
  Final race (gap < 10 pts):       1.75
  Championship already decided:    0.75

FTIS_adjusted = FTIS_baseline × championship_stakes_multiplier
```

---

## Regulation Cycle Intelligence

Where in the regulation cycle the season sits affects all token intelligence:

| Cycle position | Token intelligence adjustment |
|---|---|
| Year 1 of new regs (opener race) | Maximum uncertainty — reduce CTI confidence 40%; FTIS ×1.25 for opener |
| Year 1 (races 2–5) | New hierarchy establishing — update CTI after each race |
| Year 1 (races 6+) | New competitive order mostly confirmed — restore normal confidence |
| Year 2–3 of regs | Stable hierarchy — historical form most predictive |
| Year 4+ of regs | Diminishing returns; development convergence — midfield upsets more likely |
| Final year before reset | Known order; speculation about next era begins — silly season elevated |

**2026 specific:** Major regulation reset. All prior CTI baselines should be treated
as provisional until race 3 confirms the new competitive order.

---

## Silly Season — Driver Transfer Token Intelligence

F1's annual transfer silly season (July–October) creates recurring narrative signals:

### Transfer signal hierarchy for token impact

```
TIER 1 signal (act immediately):
  Official announcement from constructor or FIA registration confirmed
  → Destination constructor token: enter within 2h

TIER 2 signal (monitor closely):
  Fabrizio Romano / David Croft / Ted Kravitz of F1 media confirms
  (Sky Sports F1, The Race, autosport.com Tier 1 sources)
  → Enter if two independent Tier 1 sources agree

TIER 3 signal (wait):
  Single source, unverified rumour
  → Do not enter; monitor for Tier 1/2 confirmation
```

### Transfer impact matrix

| Scenario | Destination token | Departure token |
|---|---|---|
| Elite DTM driver (1.25+) arrives | +12–22% | -8–15% |
| High DTM driver (1.10–1.24) arrives | +8–15% | -5–10% |
| Driver leaves mid-season (injury/fired) | -5–12% (uncertainty) | Varies |
| Star driver signs multi-year extension | +6–12% (stability signal) | N/A |
| Reserve driver called up (replacing Elite) | -8–15% (talent downgrade) | N/A |

---

## Multi-Token Events in F1

Unlike football, most F1 token events involve a SINGLE constructor.
However, two scenarios create genuine multi-token dynamics:

### Championship battle between two token-active constructors

When two constructor tokens are battling for the title in the final races:
```
if both constructors have active tokens AND points gap < 30:
  → Both tokens are INVERSELY correlated before each race
  → Do NOT hold both simultaneously
  → Enter winner post-race; do not hold both pre-race
  → Pre-race correlation check: tokens in title battle often have
    correlation > 0.75 leading up to the race (both elevated by stakes),
    then sharply diverge at result
```

### Driver moves between token-active constructors

When a driver transfers between two active-token constructors:
```
Destination constructor: immediate positive signal
Departure constructor:   immediate negative signal
Net strategy: Enter destination immediately; exit departure simultaneously
Hold period: 48–72h (peak narrative window for transfer news)
```

---

## Agent Reasoning Prompts

```
You are a Formula 1 fan token intelligence agent. Before evaluating any F1 event:

1. REGULATION CONTEXT FIRST. Is this a regulation-change year?
   If yes: reduce confidence in all prior-season CTI data by 40%.
   First 3 races of 2026 are the new baseline — treat them as maximum-information events.

2. QUALIFYING IS THE PRIMARY SIGNAL for all races.
   Friday practice is directional only — do not enter positions on practice data.
   Monaco qualifying is worth more than any other qualifying session in the calendar.

3. CONSTRUCTOR vs DRIVER tokens have different sensitivities.
   Mechanical DNF hurts constructor token more than driver.
   Driver error hurts driver token more than constructor.
   A 1-2 finish for the constructor is the maximum positive signal.

4. CHAMPIONSHIP STAKES MULTIPLIER adjusts all signals.
   A win in race 3 means less than a win with 5 races left and a 20-point deficit.
   Always check the current standings context before sizing.

5. SILLY SEASON (July–October) is an annual narrative window.
   Monitor contract expiry dates. Elite DTM driver announcement = immediate signal.
   Only act on Tier 1 source confirmation — F1 rumours are abundant and unreliable.

6. WET RACES are variance events — not prediction events.
   Reduce position sizes when rain is forecast. Safety car deployments can
   reverse any competitive advantage regardless of token ecosystem strength.

7. DUAL-TOKEN CHAMPIONSHIP BATTLES: never hold both tokens pre-race
   when they are in direct title contention. Enter the winner post-race only.
```

---

## Data Sources

- Race results and standings: Formula 1 official API, Ergast API
- Qualifying and lap times: FastF1 Python library
- Transfer news: motorsport.com, autosport.com, The Race, Sky Sports F1
- Token data: Kayen/FanX API + Socios Connect (via fan-token-pulse)

---

## Compatibility

**Layer 1 companion:** `sports/formula1` — load alongside for full domain context.
**Required Layer 3:** `fan-token-pulse` — always run first for on-chain baseline.
**Recommended:** `athlete-social-lift` — DTM confirmation via live social signal.
**Recommended:** `transfer-intelligence` — silly season contract analysis.
**Recommended:** `athlete/meta` — weather overlay (critical in F1).

---

*MIT License · SportMind · sportmind.dev*
