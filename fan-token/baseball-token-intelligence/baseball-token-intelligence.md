# Baseball (MLB) — Token Intelligence

Bridge skill connecting MLB events to fan token and prediction market signals.
Baseball is the most data-rich sport ecosystem on the planet — Statcast generates
over 30 million data points per season. The signal model is built on this richness:
pitcher-first analysis, Ohtani-effect franchise catalysts, and Japan-US market bridges.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — high credibility, near-term
  No active Chiliz tokens at time of writing
  MLB digital history: MLB Champions NFTs (2019), MLB Crypto Baseball
  Ohtani/Dodgers Japan catalyst: highest individual commercial value in baseball
  Latin American market: DR, Venezuela, Cuba, Panama = deep token-ready fanbase

SIGNAL CHARACTERISTICS:
  Most predictive: Starting pitcher quality (PQS) — more decisive than in any team sport
  Most volatile: Trade deadline (July 31) + post-season roster construction
  Most concentrated: World Series + All-Star Game (ASG)
  Unique signal: Ohtani two-way player creates dual signal (pitcher AND batter)

STRUCTURE NOTE: MLB operates a 162-game season — longest in any North American sport.
  Weighted signal: regular season signals carry less weight than post-season.
  Playoff expansion (12 teams since 2022) = more signal events, more token windows.
```

---

## MLB Token Impact Score (MLBTIS)

```
MLBTIS = (Game_Importance × 0.35) + (Pitcher_Quality × 0.35)
        + (Franchise_Factor × 0.20) + (Market_Sentiment × 0.10)

GAME IMPORTANCE:
  World Series clinch game:              1.00
  World Series Game 7:                   0.98
  World Series Game 1:                   0.80
  LCS (League Championship Series):      0.72
  LDS (Division Series):                 0.60
  Wild Card Game:                        0.50
  Regular season (final week, playoff chase): 0.40
  Regular season (standard):             0.20
  All-Star Game:                         0.55 (engagement event, low prediction value)

PITCHER QUALITY (PQS — from athlete/baseball/athlete-intel-baseball.md):
  PQS 5 (dominant): ×1.18
  PQS 4 (quality):  ×1.09
  PQS 3 (average):  ×1.00
  PQS 2 (poor):     ×0.88
  PQS 1–0 (failed): ×0.75
  
  AGENT RULE: Always compute PQS before evaluating any MLB matchup.
  In baseball, the starting pitcher is more decisive than any other single
  variable in any sport in the library — more than the MMA weigh-in.
```

---

## Pitcher-first model — the defining principle

```
WHY BASEBALL IS PITCHER-FIRST:

Every other team sport distributes performance across multiple players.
In baseball, the starting pitcher controls roughly 60-70% of game outcome variance.
No other single player position in sport has this dominance — not even the MMA fighter.

PRACTICAL IMPLICATIONS:
  Injury to starting pitcher = reload analysis entirely, not just apply modifier
  Starting pitcher change (< 24h before game): set lineup_unconfirmed flag
  Opener strategy (sub-5-inning starter): apply ×0.85 strategy adjustment
  
  The five-man rotation means each pitcher starts every 5th game.
  AGENT RULE: Track pitcher rotation cycle — identify who starts each game
  before applying any other signal analysis.

BULLPEN AS SECONDARY VARIABLE:
  After 5-6 innings: bullpen ERA and workload from last 3 days
  Load athlete/baseball/ — bullpen workload modifier
  High-workload bullpen (3+ appearances in last 4 days): ×0.90
  Fresh bullpen (0-1 appearances in last 4 days): ×1.05
```

---

## The Ohtani effect — dual signal model

```
SHOHEI OHTANI — UNIQUE SIGNAL IN ALL OF SPORT:

Ohtani is the only active two-way player in baseball at elite level.
He pitches AND bats — two independent signal streams from one player.

Commercial profile (Los Angeles Dodgers, 2024+):
  Contract: $700M / 10 years (largest in North American sports history)
  Japan market: Ohtani drives 40-50% of Dodgers social engagement in Japan
  NPB (Nippon Professional Baseball): Ohtani = gateway for MLB→Japan digital products
  
  ANY Dodgers fan token would inherit this Ohtani dual signal.

SIGNAL ON DAYS HE PITCHES:
  Ohtani as starter: apply PQS modifier as pitcher
  Plus: his presence = Dodgers attendance premium + social engagement spike
  Combined: PQS modifier × 1.08 Ohtani attendance multiplier

SIGNAL ON DAYS HE ONLY BATS:
  Ohtani BQS applies: multi-category hitter (HR, BA, OPS, SB)
  Monitor: is he in full health? Two-way load = injury management is key variable
  
NPB CATALYST:
  MLB + NPB partnership potential: if MLB tokens launch, Japan is the first market
  Ohtani = highest-value individual driver of Japan adoption
  Monitor: NPB digital product announcements; Softbank/Rakuten (NPB club owners)
```

---

## MLB Signal Calendar

```
ANNUAL MLB SIGNAL CALENDAR:

February–March (Spring Training):
  Squad news, roster battles, injury signals
  Opening Day roster announcement: first definitive signal of season

April–September (Regular Season — 162 games):
  Low individual game weight; cumulative form matters more than single games
  
July 31 (Trade Deadline):
  PEAK summer signal event — equivalent to football's transfer window
  Contending team buys: positive signal
  Selling team: roster disruption, negative signal
  Monitor: pitcher acquisitions (most impactful) then closer/bat

August–September (playoff chase):
  Wild Card standings: last 6 weeks of regular season = elevated signal
  Teams within 3 games of Wild Card: maximum regular-season weight

October (Post-Season):
  Wild Card Series → Division Series → LCS → World Series
  All-or-nothing format: signal amplifies at each elimination stage

November (Free Agency opens):
  Shohei Ohtani / Juan Soto type signings = franchise-level signal events
  Monitor: front-page signings only — regular free agency is lower signal

December (Hot Stove):
  Lower signal but: Ohtani and elite players can drive December peaks
```

---

## Latin American market context

```
BASEBALL'S NATURAL FAN TOKEN MARKET:

Dominican Republic: ~40% of MLB foreign-born players are Dominican
  - Deep cultural connection to baseball; high digital engagement
  - DR has one of the highest crypto adoption rates in Latin America

Venezuela: historic MLB pipeline; Cabrera, Altuve, Soto generation
Cuba: Puig, Gurriel, Céspedes diaspora = significant US + Latin American fan base
Panama: Mariano Rivera cultural icon; growing digital sports market
Puerto Rico: US jurisdiction; highest per-capita baseball viewership globally

COMBINED LATIN AMERICA + JAPAN:
  These two markets are naturally complementary for MLB token products
  Latin America: emotional, community-driven engagement
  Japan: data-driven, statistics-obsessed engagement
  Together they form the natural first-adopter base for any MLB token launch.
```

---

## Agent reasoning prompts

```
You are an MLB token intelligence agent. Before any analysis:

1. PITCHER FIRST — Who is starting and what is their PQS?
   Do not proceed with any other analysis until pitcher is identified.
   Starting pitcher change (< 24h): reload entire analysis.

2. GAME IMPORTANCE TIER — Regular season vs Wild Card vs World Series?
   Weight signals significantly lower for regular season games.
   Post-season: apply full MLBTIS weight.

3. OHTANI CHECK — Is this a Dodgers game?
   If Ohtani pitching: apply PQS × 1.08 combined modifier.
   If Ohtani batting only: apply BQS + load management check.

4. TRADE DEADLINE PROXIMITY — Is it late July?
   Trade deadline signals are the highest summer signal event in MLB.
   Buyer team: positive. Seller team: disruption modifier.

5. BULLPEN WORKLOAD — Last 3 games of bullpen usage?
   High workload after close game: ×0.90. Fresh: ×1.05.

6. LATIN AMERICA + JAPAN CONTEXT — For token launch signals:
   Monitor DR, Venezuela, Japan market activation events.
   These are the natural first-adopter markets for MLB tokens.
```

---

## Compatibility

**L1 domain:** `sports/baseball/sport-domain-baseball.md`
**L2 athlete:** `athlete/baseball/athlete-intel-baseball.md`
**L4 market:** `market/market-baseball.md`
**Draft:** `core/core-draft-intelligence.md`

*MIT License · SportMind · sportmind.dev*
