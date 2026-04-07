# American Football (NFL) — Token Intelligence

Bridge skill connecting NFL events to fan token and prediction market signals.
The NFL is the largest untapped fan token market in the library — $20B+ revenue,
100M+ US fans, and the highest per-game viewership of any sport globally.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  No major active Socios tokens at time of writing
  DraftKings/FanDuel daily fantasy = largest digital engagement proof of concept
  Super Bowl commercial window = highest single-event token launch opportunity globally

SIGNAL CHARACTERISTICS:
  Most predictive: QB injury report (Wednesday/Thursday designation)
  Most volatile: Trade deadline (November) and free agency (March)
  Most underpriced: O-line injury cluster (requires Statcast/PFF to detect)
  Highest engagement window: Super Bowl (global peak), Thanksgiving games (US peak)
  
STRUCTURAL NOTE: NFL operates collective bargaining model.
  All teams are franchise-owned within a centralised league structure.
  Revenue sharing = more even competitive balance than any other major sport.
  Lower individual club commercial differentiation vs football/basketball.
  Fan token model: franchise-level tokens most viable (Cowboys, Patriots, Chiefs).
```

---

## NFL Token Impact Score (NFLTIS)

```
NFLTIS = (Game_Importance × 0.35) + (QB_Status × 0.30)
        + (Playoff_Position × 0.20) + (Market_Sentiment × 0.15)

GAME IMPORTANCE:
  Super Bowl:                  1.00
  Conference Championship:     0.88
  Divisional Playoff:          0.75
  Wild Card:                   0.62
  Late regular season (playoff chase): 0.50
  Regular season (standard):   0.30
  Thursday Night / MNF:        × 1.15 multiplier (national broadcast)
  Thanksgiving:                × 1.20 multiplier (cultural peak)

QB STATUS:
  Elite starter confirmed fit:        1.00
  Elite starter probable (injury):    0.80
  Elite starter questionable:         0.65
  Elite starter out → backup starts:  0.45  ← immediate signal event
  No elite QB on roster:              0.55
```

---

## The QB signal — most important individual variable

```
THE QB INJURY REPORT SYSTEM (from athlete/nfl/athlete-intel-nfl.md):

Wednesday designation:
  Full Participation (FP): On track — no modifier needed
  Limited Participation (LP): Monitor Thursday
  Did Not Participate (DNP): FLAG — backup likely if not improved by Friday

Thursday designation:
  FP → standard signal
  LP → apply ×0.85 modifier; set lineup_unconfirmed flag
  DNP → apply ×0.65 modifier; backup start likely

Friday designation (official status):
  Probable: ×0.97 (minor concern)
  Questionable: ×0.85; set lineup_unconfirmed flag
  Doubtful: ×0.75
  Out: ×0.65 → backup starts → see knockout conditions below

KNOCKOUT CONDITIONS:
  Elite QB confirmed Out:  floor modifier ×0.65 regardless of other inputs
  Starter QB ruled Out + backup < 60% career completion: floor ×0.55

AGENT TIMING RULE:
  Wednesday report: preliminary flag
  Thursday report: decision on position size
  Friday report: final status — act on this
  Sunday morning (2h before kickoff): final inactive list
```

---

## NFL Signal Calendar

```
ANNUAL NFL SIGNAL CALENDAR:

March (Free Agency):
  NFL's equivalent of football's transfer window
  First wave (Monday 4pm ET): top free agents signed
  Agent action: treat like transfer signal — load fan-token/transfer-signal/
  Token impact: franchise with major FA addition → sentiment uplift

April (NFL Draft):
  See core/core-draft-intelligence.md — NFL Draft section
  Pick #1 overall = franchise-changing signal
  QB drafted in Round 1 to struggling franchise: +15-25% sentiment

July–August (Training Camp / Preseason):
  Lower signal — but: depth chart battles, injury risk exposure
  Key signal: unexpected starter losing job in camp

September (Season Opener):
  High engagement but moderate signal (small sample size)
  
October–December (Regular Season):
  Primary weekly signal cycle
  Bye weeks = no signal for that team's token

November (Trade Deadline):
  Smaller than March FA but can move markets
  Rental player for playoff push = signal event
  
January (Playoffs):
  Signal amplification × tier structure above
  
February (Super Bowl):
  Highest global NFL engagement event
  Super Bowl host city commercial window = unique opportunity
  Half-time show = entertainment crossover signal (cultural)
```

---

## Super Bowl — the peak signal event

```
SUPER BOWL SIGNAL MODEL:

Pre-game (2 weeks between Conference Championships and SB):
  Narrative build period — highest sustained engagement in NFL calendar
  Token signal: positive trend throughout 2-week window for both finalists
  Agent: load core/core-narrative-momentum.md — sustained category applies

Game day:
  Halftime show: cultural crossover event — not just sports signal
  Celebrities attending = brand amplification signal
  QBs on field = highest QB individual brand moment of the year

Post-game:
  Winner: +15–25% token sentiment (if franchise token exists/is planned)
  MVP player: individual brand peak — highest single moment in NFL career
  Loser: -10–20% token sentiment; short-term; recovers in 2-4 weeks

COMMERCIAL CONTEXT:
  Super Bowl ad slot: ~$7M/30 seconds (2024)
  Super Bowl viewership: 120M+ US; 200M+ global (growing)
  Any franchise launching a fan token should time announcement around Super Bowl
```

---

## Agent reasoning prompts

```
You are an NFL token intelligence agent. Before any analysis:

1. QB REPORT FIRST — Always check Wednesday/Thursday/Friday designation.
   NFL is more QB-dependent than any other sport. This is non-negotiable.

2. GAME IMPORTANCE TIER — Regular season vs playoff vs Super Bowl.
   Signal weight changes dramatically across the NFL calendar.

3. THURSDAY/MONDAY NIGHT FACTOR — National broadcast games have ×1.15
   engagement multiplier. Thanksgiving games: ×1.20.

4. FANTASY FOOTBALL CORRELATION — 60M+ US DFS players track NFL obsessively.
   DFS player injury tracking is a leading indicator for official NFL reports.
   Cross-reference DFS platform lineup changes with injury designations.

5. O-LINE CLUSTER RISK — If 2+ O-linemen are limited/out, QB faces elevated
   pressure even if QB himself is healthy. Load athlete/nfl/ for O-line health.

6. MACRO CHECK — Apply CHZ/BTC macro modifier before any token signal.
   No active NFL tokens = prediction market signals are the primary use case.
```

---

## Compatibility

**L1 domain:** `sports/american-football/sport-domain-american-football.md`
**L2 athlete:** `athlete/nfl/athlete-intel-nfl.md`
**L4 market:** `market/market-american-football.md`
**Draft:** `core/core-draft-intelligence.md`
**Injury:** `core/injury-intelligence/injury-intel-nfl.md`

*MIT License · SportMind · sportmind.dev*
