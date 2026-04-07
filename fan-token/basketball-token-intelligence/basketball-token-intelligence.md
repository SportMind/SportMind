# Basketball (NBA) Token Intelligence — SportMind Layer 3

Bridge skill connecting NBA basketball events to fan token and prediction market signals.
The NBA's token ecosystem is player-centric rather than club-centric — individual star
athletes drive engagement more than team results in most markets.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 1 — active institutional interest; no major active Socios
  tokens at time of writing but NBA Top Shot precedent + growing DFS/prediction activity
  
SIGNAL CHARACTERISTICS:
  Most volatile: Star player trade/signing announcements
  Most sustained: Playoff run narratives (April–June)
  Most underpriced by market: Back-to-back fatigue signals (see core-fixture-congestion.md)
  Highest engagement window: Draft night (June) + Trade deadline (February)

PLAYER-TEAM DYNAMIC: Unlike football where club tokens dominate, NBA commercial value
  is heavily individual. LeBron James, Giannis, Curry, Jokić carry more token/brand
  signal than their respective franchises in most non-US markets.
```

---

## NBA Token Impact Score (NBATIS)

Composite metric for NBA-level token and prediction market signal impact.

```
NBATIS = (Game_Importance × 0.35) + (Star_Player_Status × 0.30)
        + (Playoff_Position × 0.20) + (Market_Sentiment × 0.15)

GAME IMPORTANCE TIERS:
  NBA Finals:           1.00 (maximum)
  Conference Finals:    0.85
  Second Round:         0.70
  First Round:          0.55
  Regular season (top seed tracking): 0.40
  Regular season (standard):          0.25
  Back-to-back (second night):        × 0.85 multiplier applied to result
  In-season tournament:               0.35

STAR PLAYER STATUS:
  MVP candidate / top-3 global recognition: 1.00
  All-Star starter: 0.80
  All-Star reserve: 0.65
  Starter (non-All-Star): 0.45
  Bench player: 0.20
  Player ruled out: 0.00 (immediate signal event)
```

---

## Player-first signal model

```
THE NBA PLAYER SIGNAL HIERARCHY:

TIER 1 — Franchise-defining players:
  LeBron James, Stephen Curry, Kevin Durant, Giannis Antetokounmpo, 
  Nikola Jokić, Luka Dončić, Joel Embiid, Jayson Tatum (and successors)
  Signal weight: Individual player moves carry 60-70% of total team signal
  Token/commercial impact: Global; Middle East, Europe, Asia markets respond independently
  
TIER 2 — Elite starters:
  All-Star calibre players with strong social presence
  Signal weight: 35-50% of team signal
  
TIER 3 — Role players:
  Signal weight: <15% of team signal
  Exception: When Tier 3 player unexpectedly stars (breakout performance)
  → Generates narrative momentum signal; load core-narrative-momentum.md

TRADE SIGNAL (highest single-event signal in NBA):
  Tier 1 player traded: +15–35% token signal for receiving team
                        -20–40% for trading team (losing franchise player)
  Tier 2 player traded: +8–15% / -10–20%
  Deadline rental (expiring contract): +5–10% / minimal negative

LOAD MANAGEMENT SIGNAL:
  Tier 1 player sits B2B: Apply × 0.75 modifier to that team's signal
  Surprise DNP (load management without announcement): immediate uncertainty flag
  → Apply: lineup_unconfirmed flag in confidence output schema
```

---

## Competition calendar and signal windows

```
ANNUAL NBA SIGNAL CALENDAR:

July (Free Agency):
  Highest volume period — major player moves reshape franchises
  Signal window: July 1 midnight opening through mid-July (most signings)
  Agent action: Monitor Twitter/X in real-time; verified reports = 80% reliable
  Sources: Woj (Adrian Wojnarowski), Shams Charania — two highest-reliability reporters

October (Opening Night):
  Season opening; narrative reset; new rosters debut
  Signal: +5–10% for teams with significantly upgraded rosters
  
November–January (Regular Season):
  Primary signal drivers: standings position, injury developments
  Sleeper catalyst: Load management decisions revealing team strategy

February (Trade Deadline):
  Second major signal window after July free agency
  Deadline day: high volatility; multiple moves in hours
  
March–April (Play-In Tournament):
  Seeds 7–10 competing for playoff spots
  High-stakes regular season equivalent; elevated engagement

April–June (Playoffs):
  Peak signal period; every round escalates engagement
  First-round upset: +15–25% for lower seed
  Injury to playoff star: immediate significant negative

June (NBA Draft):
  See core-draft-intelligence.md — NBA Draft section
  Lottery winner: +10–20% franchise sentiment signal

EUROLEAGUE CALENDAR:
  October–May: Regular season (18 clubs, home and away)
  Final Four (May, Belgrade/Istanbul): European peak event
  Tokens: ASVEL, Real Madrid, FC Barcelona Lassa — European club tokens
  Signal model: Club-centric (closer to football model than NBA player-centric model)
```

---

## NBA vs EuroLeague signal model comparison

```
NBA (PLAYER-CENTRIC):
  Primary driver: Individual star player performance and status
  Secondary: Team playoff position
  Token structure: Individual player tokens more viable than team tokens in NBA
  Global reach: Best-in-sport; every NBA star has global following
  
EUROLEAGUE (CLUB-CENTRIC):
  Primary driver: Final Four qualification (equivalent to Champions League)
  Secondary: Rivalry match results (Real Madrid vs Barça etc.)
  Token structure: Club tokens are the primary commercial vehicle
  Geographic concentration: Southern and Eastern Europe; Turkey
  
AGENT RULE: Apply NBA player-centric model for US-listed tokens/markets.
            Apply football-adjacent club-centric model for EuroLeague tokens.
            Do not conflate the two — different signal architectures.
```

---

## Key signal events

```
HIGHEST-IMPACT NBA SIGNAL EVENTS:

Event                           | Token/Market Impact
--------------------------------|-------------------
MVP announcement                | +10–20% franchise token
Finals MVP                      | +15–25% individual brand
Injury (Tier 1 player)          | -15–30% immediate; duration matters
Trade (Tier 1 player acquired)  | +15–35% receiving team
Draft lottery win               | +10–20% franchise sentiment
All-Star snub (Tier 2 player)   | -5–10% individual brand
Record broken (in-season)       | +3–8% narrative catalyst

NBA TOP SHOT PRECEDENT:
  NBA Top Shot ($1B+ in sales, 2020–2021) established that NBA IP drives
  the highest-value digital collectible market in sport. This precedent
  matters for any future NBA fan token — the fanbase has demonstrated
  willingness to purchase digital NBA assets.
  
  Agent implication: NBA token readiness tier should be assessed as Tier 1
  commercially, even without active Socios tokens. The infrastructure
  and willingness are documented.
```

---

## Agent reasoning prompts

```
You are an NBA basketball token intelligence agent. Before any analysis:

1. IDENTIFY PLAYER TIER — Is the primary player Tier 1, 2, or 3?
   The signal weight changes dramatically by player tier in the NBA.

2. CHECK BACK-TO-BACK STATUS — Is this the second game in two nights?
   Load core-fixture-congestion.md; apply × 0.85 to star player availability.

3. CHECK LOAD MANAGEMENT — Has any Tier 1 player been flagged for rest?
   LM decision can invalidate signal within minutes of tip-off.

4. CALENDAR CONTEXT — What phase is the season in?
   Playoff signal weight is 2–3× regular season for equivalent matchup quality.

5. TRADE WINDOW — Is it July (free agency) or late January/February (deadline)?
   These windows override sporting analysis; player movement is the signal.

6. APPLY NBA TIS — Calculate NBATIS for the specific game/event.
   High NBATIS + top player available + correct phase = high confidence entry.
```

---

## Compatibility

**L1 domain:** `sports/basketball/sport-domain-basketball.md`
**L2 athlete:** `athlete/nba/athlete-intel-nba.md`
**L4 market:** `market/market-basketball.md`
**Draft:** `core/core-draft-intelligence.md`
**Congestion:** `core/core-fixture-congestion.md`

*MIT License · SportMind · sportmind.dev*
