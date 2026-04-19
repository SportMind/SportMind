# Ice Hockey (NHL) — Token Intelligence

Bridge skill connecting NHL events to fan token and prediction market signals.
Ice hockey's token potential is anchored by two structural realities: the goaltender
is the single highest-impact individual position in any team sport in the library,
and the Canadian market has the highest sports-per-capita engagement of any country
where cryptocurrency is mainstream.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — high credibility, near-term
  No active fan tokens at time of writing
  Canadian crypto adoption: ~30% (among highest per-capita globally)
  Rogers/Bell broadcast deal: major revenue anchor through 2026
  European entry point: Swedish, Finnish, Czech clubs have token readiness

SIGNAL CHARACTERISTICS:
  Most predictive: Goaltender start confirmation + GSAx (Goals Saved Above Expected)
  Most volatile: Trade deadline (March) + Stanley Cup Playoffs
  Most concentrated: Game 7s (highest single-game hockey signal)
  Unique signal: Back-to-back games create systematic fatigue signal

STRUCTURE NOTE: NHL 82-game season + expanded playoffs (16 teams).
  Regular season signals carry less weight than baseball's 162-game model.
  Playoff format: best-of-7 series = series momentum compounds game-by-game.
```

---

## NHL Token Impact Score (NHLTIS)

```
NHLTIS = (Game_Importance × 0.30) + (Goaltender_Quality × 0.35)
        + (Playoff_Position × 0.20) + (Market_Sentiment × 0.15)

GAME IMPORTANCE:
  Stanley Cup Final Game 7:              1.00
  Stanley Cup Final Game 6 (clinch):     0.92
  Stanley Cup Final Game 1:              0.75
  Conference Final Game 7:              0.85
  Conference Final (any):                0.70
  Conference Semifinal Game 7:           0.78
  Conference Semifinal (any):            0.62
  First Round Game 7:                    0.68
  First Round (any):                     0.50
  Regular season (final week, playoff chase): 0.35
  Regular season (standard):             0.20
  Winter Classic (outdoor game, Jan 1):  0.60 (cultural peak; not always high-stakes)
  Heritage Classic (outdoor):            0.55

GOALTENDER QUALITY (GSAx — Goals Saved Above Expected):
  GSAx season leader (top 5, > +10): ×1.18
  Above average (GSAx 0 to +10):     ×1.08
  Average (GSAx -5 to 0):            ×1.00
  Below average (GSAx -10 to -5):    ×0.88
  Backup starter:                    ×0.80
  Emergency call-up:                 ×0.72
```

---

## The goaltender model — primary variable

```
WHY GOALTENDERS DOMINATE NHL SIGNALS MORE THAN ANY OTHER SPORT:

In football: a GK with 35%+ save rate shifts outcomes
In ice hockey: the goaltender faces ~30 shots per game, many of high quality
  A difference of 2-3 saves per game = direct win probability swing of 15-20%

GSAx (Goals Saved Above Expected):
  The premier goaltender metric: actual saves minus expected saves
  Based on Evolving-Hockey, Natural Stat Trick shot quality models
  Season GSAx > +15: elite tier — this goaltender is winning games independently
  Season GSAx > +8:  above average — clear positive signal
  Season GSAx < -5:  liability — apply negative modifier even if team is strong

GOALTENDER START CONFIRMATION:
  NHL teams rarely confirm starting goaltender until day-of
  Morning skate (10-11am ET): goaltenders who participate = likely starter
  Pre-game warmup: goaltender taking starting warmup = confirmed
  
  TIMING RULE:
    Not yet confirmed (morning skate pending): set lineup_unconfirmed flag
    Morning skate confirmed: remove flag; apply full GSAx modifier
    Surprise scratch (confirmed at warmup): reload analysis — treat as backup start

BACK-TO-BACK MODIFIER:
  NHL schedules back-to-back games (two games in two days) throughout the season.
  Starting goaltender in second game of B2B: ×0.88 fatigue modifier
  
  AGENT RULE: Always check if this is the second game of a B2B.
  Teams frequently start backup goaltenders on B2B second games.
  Load core/core-fixture-congestion.md — NHL B2B section.
```

---

## Stanley Cup Playoffs — the peak signal architecture

```
STANLEY CUP PLAYOFF STRUCTURE:
  16 teams qualify (8 per conference)
  Four rounds, all best-of-7
  Average series: 5.4 games (approximately)
  
SERIES MOMENTUM — compound signal:
  Teams that win Game 1: historically win series at ~65%
  Teams that win Game 1 of Finals: historically win Cup at ~70%
  
  AGENT RULE: Track series score alongside game-level analysis.
  A team down 3-0 in a series behaves differently than a team leading 3-0.
  Elimination game pressure modifies GK performance (positive for veterans;
  negative for playoff-inexperienced starters).

GAME 7 SIGNAL MODEL:
  Game 7s have unique statistical properties:
  - Home ice advantage increases (home team wins ~54% of Game 7s)
  - Overtime frequency increases (~25% of Game 7s go to OT)
  - Experience modifier amplifies: veterans outperform regular-season rating
  
  Load core/core-narrative-momentum.md — elimination category for Game 7s.

STANLEY CUP FINAL — CANADIAN MARKET PEAK:
  Last Canadian team to win: Montreal Canadiens (1993)
  If a Canadian team reaches the Final: token engagement potential ×1.5-2.0
  Canadian markets: Toronto, Montreal, Vancouver, Ottawa, Calgary, Edmonton, Winnipeg
  Any Canadian team in Cup contention = disproportionate national engagement signal.
```

---

## Canadian market — the core opportunity

```
WHY CANADA IS THE PRIMARY NHL TOKEN MARKET:

7 Canadian franchises in NHL (Toronto, Montreal, Vancouver, Ottawa,
  Calgary, Edmonton, Winnipeg)

Canadian hockey culture:
  NHL viewership per-capita: Canada is ~3× USA; hockey is national identity
  Sportsnet/TSN: broadcast rights → concentrated national platform
  Rogers deal through 2026: national English-language TV anchor
  
Crypto adoption: Canada ~30% adoption rate; among highest in developed world.
  Combined with hockey cultural intensity = strongest per-capita token readiness
  of any NHL market.

TORONTO MAPLE LEAFS — highest commercial value target:
  Most valuable NHL franchise (~$3.5B)
  Largest hockey market by population
  Last Cup win: 1967 — narrative of sustained drought = chronic fan engagement
  
MONTREAL CANADIENS — cultural heritage token:
  Most historic franchise (24 Stanley Cups)
  French-Canadian market — unique token identity (French + English fanbase)
  
MONITORING RULE:
  Track: NHL digital rights and fan engagement platform announcements
  Track: Maple Leafs Sports & Entertainment (MLSE) digital product strategy
  Track: Rogers/Bell partnership developments post-2026 deal renewal
```

---

## European NHL market

```
EUROPEAN ENTRY POINTS FOR TOKEN PRODUCTS:

Sweden: ~30% of NHL rosters are Swedish; Tre Kronor is a cultural identity
  Swedish Hockey League (SHL): established professional infrastructure
  Stockholm / Gothenburg: high crypto adoption in Nordic region
  
Finland: Finnish market mirrors Sweden; Liiga (Finnish league) strong
  "Hockey is the national sport" — more accurate in Finland than any other sport
  
Czech Republic / Slovakia: significant NHL presence; domestic leagues strong

WHY EUROPEAN HOCKEY MATTERS FOR TOKENS:
  European players in NHL = dual-market signal
  A Swedish player on a Canadian team with tokens:
    Canadian engagement from NHL + Swedish engagement from national connection
  
  This cross-market dynamic is most comparable to NCSI in football
  but has not been formally documented as a token signal until this skill.
  
  AGENT RULE: For high-profile European NHL players:
  Apply ×1.05-1.10 cross-market signal during World Championship (May) and
  Olympics (when NHL participates).
```

---

## Agent reasoning prompts

```
You are an NHL token intelligence agent. Before any analysis:

1. GOALTENDER FIRST — Starting goaltender confirmed? What is their GSAx?
   More important than any other single variable in hockey.
   Not confirmed yet: set lineup_unconfirmed. Morning skate: check participation.

2. BACK-TO-BACK CHECK — Is this game 2 of a back-to-back?
   If yes: expect backup goaltender. Apply ×0.88 B2B fatigue modifier.
   Load core/core-fixture-congestion.md.

3. PLAYOFF SERIES CONTEXT — What is the series score?
   Series leads compound. A team facing elimination behaves differently.
   Game 7: home ice ×1.10, veteran GK experience modifier, load narrative skill.

4. CANADIAN TEAM CHECK — Is a Canadian franchise involved?
   Canadian hockey engagement is 3× US per-capita.
   Canadian team in Stanley Cup contention: apply ×1.5-2.0 market multiplier.

5. TRADE DEADLINE PROXIMITY — Is it mid-to-late March?
   Trade deadline is the primary non-playoff signal event.
   Buyer team (adds players): positive signal.
   Seller team (trades away): rebuilding signal — significant disruption.

6. EUROPEAN PLAYER SIGNAL — World Championship or Olympic context?
   High-profile European player on token-relevant team:
   Apply cross-market multiplier during international tournaments.
```

---

## Compatibility

**L1 domain:** `sports/ice-hockey/sport-domain-ice-hockey.md`
**L2 athlete:** `athlete/nhl/athlete-intel-nhl.md`
**L4 market:** `market/market-ice-hockey.md`
**Congestion:** `core/core-fixture-congestion.md`
**Draft:** `core/core-draft-intelligence.md`

*MIT License · SportMind · sportmind.dev*
