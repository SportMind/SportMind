# Rugby League — Token Intelligence

Bridge skill connecting rugby league events to fan token and prediction market signals.
Rugby league's token ecosystem sits at the intersection of Australia's high crypto
adoption rate and the State of Origin — the highest-single-match engagement event
in Australian sport outside the AFL Grand Final.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  No major active Socios tokens at time of writing
  State of Origin concept: strongest case for national-level token in rugby league
  NRL: 16 clubs, all with strong regional fanbases — club token potential
  Super League (UK): 12 clubs — lower commercial tier but cross-market opportunity

SIGNAL CHARACTERISTICS:
  Most volatile: State of Origin (May–July, NRL season)
  Most sustained: Finals series (September)
  Unique signal: State of Origin disrupts NRL club form for 6–8 weeks
  Downstream opportunity: Post-Origin congestion affects NRL club signals
```

---

## Rugby League Token Impact Score (RLTIS)

```
RLTIS = (Match_Importance × 0.35) + (SOO_Disruption × 0.25)
       + (Competition_Tier × 0.25) + (Market_Sentiment × 0.15)

MATCH IMPORTANCE:
  State of Origin Game 3 (series decider):     1.00
  State of Origin Game 1 or 2:                 0.85
  NRL Grand Final:                             0.90
  NRL Preliminary Final:                       0.75
  NRL Semi-Final / Elimination Final:          0.62
  State of Origin week (NRL matches):          × 0.80 (Origin disruption applied)
  Super League Grand Final:                    0.65
  Super League play-off semi:                  0.50
  Standard NRL / Super League:                 0.30

SOO_DISRUPTION (State of Origin modifier for NRL clubs):
  Club loses 4+ players to Origin: SOO_Disruption = HIGH (×0.88)
  Club loses 2–3 players:          SOO_Disruption = MEDIUM (×0.93)
  Club loses 0–1 players:          SOO_Disruption = LOW (×1.00) or POSITIVE (×1.05)
  Club benefits from opponents' Origin absences: POSITIVE (×1.04–1.07)
```

---

## State of Origin — the defining signal event

```
WHAT STATE OF ORIGIN IS:
  Annual series between New South Wales (Blues) and Queensland (Maroons)
  Three matches: typically May, June, July
  Most watched Australian sporting event outside AFL Grand Final and cricket
  Players represent their state of origin, not their NRL club

WHY IT DOMINATES THE TOKEN SIGNAL LANDSCAPE:

  1. The highest single-match engagement event in rugby league
     State of Origin G3 (series decider) > any NRL finals match for viewership
     
  2. Creates the most complex downstream signal in any sport in the library
     After each Origin match: NRL clubs that gave the most players are fatigued
     Clubs that benefit from depleted opponents gain × positive signal

  3. Form compression at Origin level
     State pride removes 40% of form differential predictability
     A Queensland team playing poorly in NRL can lift to beat NSW (and vice versa)
     Load core/core-narrative-momentum.md — rivalry amplifier applies

STATE OF ORIGIN SIGNAL CALENDAR:
  Pre-announcement (March–April): Squad announcement signals
  Game 1 (late May): Season-opener; highest uncertainty
  Game 2 (late June): Series context established
  Game 3 (mid-July if needed): Highest signal — series decider

DOWNSTREAM NRL SIGNAL (most undervalued signal in rugby league):
  After each Origin match:
    High-origin clubs (4+ players away): recovery week → apply congestion ×0.88-0.93
    Low-origin clubs (opponent depleted): opportunity → apply ×1.04-1.07
  
  This downstream signal is often MORE VALUABLE than the Origin result itself
  because it's systematic and less well understood by prediction markets.
  See core/core-fixture-congestion.md — State of Origin section
```

---

## NRL Signal Calendar

```
ANNUAL NRL SIGNAL CALENDAR:

February–March (Pre-season / NRL Nines):
  Low signal; squad depth signals; injury risk exposure
  NRL Nines competition: fast-format preview — moderate engagement

March (Round 1, Season Opener):
  High engagement but small sample — treat like AFL Round 1

April–May (Regular season, pre-Origin):
  Progressive signal building; form establishes
  ANZAC Day Round (NRL special round): elevated engagement
  
Late May–July (State of Origin):
  Season-within-a-season; see above
  NRL fixtures during Origin weeks: lower signal quality (depleted squads)

August–September (Regular season, finals chase):
  Top 8 qualification signal; ladder position critical
  Week 1 finals: elimination matches = highest single NRL signal per game

September (NRL Finals Series):
  Grand Final: MCG-equivalent for rugby league; Sydney or Brisbane

October (Off-season):
  Retention announcements; transfer rumours; NRL Draft
  Super League Grand Final (Old Trafford, Manchester): European peak
```

---

## Super League — UK rugby league commercial context

```
SUPER LEAGUE COMMERCIAL PROFILE:
  12 clubs: St Helens, Leeds Rhinos, Wigan Warriors, Hull FC, etc.
  Broadcast: Sky Sports (UK primary); Channel 4 (free-to-air since 2021)
  Geographic concentration: North of England (Leeds, Manchester, Hull)
  
  TOKEN POTENTIAL (lower than NRL but genuine):
    Strong regional fan identity (Lancashire/Yorkshire rivalries)
    Channel 4 deal = broadened reach; younger demographic access
    Magic Weekend (Newcastle): all clubs; highest Super League engagement event
    
  AGENT NOTE: Super League tokens, if launched, would follow:
    Challenge Cup Final (Wembley): highest prestige single match
    Grand Final (Old Trafford, October): season climax
    Magic Weekend: neutral venue, all clubs present
```

---

## Women's rugby league

```
WOMEN'S RUGBY LEAGUE — EMERGING SIGNAL:
  Women's State of Origin: launched 2018; growing fast
  NRLW (Women's NRL): 8 teams; season overlaps men's NRL
  Market/market-womens-sports.md: cross-reference for commercial context
  
  Signal note: Women's State of Origin creates its own NCSI spillover
  for clubs that contribute star players to NSW or Queensland women's squads.
```

---

## Agent reasoning prompts

```
You are a rugby league token intelligence agent. Before any analysis:

1. STATE OF ORIGIN STATUS — Is it Origin period (May–July)?
   If yes: apply SOO disruption modifier to ALL NRL club signals.
   Load athlete/rugby-league/ for SOO player count per club.

2. DOWNSTREAM CONGESTION — Who benefits from opponents' Origin absences?
   This is the highest-value underpriced signal in rugby league.
   Load core/core-fixture-congestion.md before any NRL club analysis.

3. SERIES CONTEXT — Origin game 1, 2, or 3?
   Game 3 (decider): RLTIS = 1.00; form compression maximum.
   Games 1 and 2: RLTIS = 0.85; earlier games have more predictability.

4. FORM COMPRESSION FOR ORIGIN — Reduce form differential by 40%.
   State pride overrides 40% of standard form signal.
   Never apply full form differential to an Origin match.

5. NRL vs SUPER LEAGUE — Which competition?
   NRL: higher signal weight; larger token opportunity.
   Super League: use same framework, lower weight (×0.75 vs NRL equivalent).

6. GRAND FINAL TIMING — NRL Grand Final or Super League Grand Final?
   Both are peak events for their competition tier.
   Apply maximum competition weight for respective code.
```

---

## Compatibility

**L1 domain:** `sports/rugby-league/sport-domain-rugby-league.md`
**L2 athlete:** `athlete/rugby-league/athlete-intel-rugby-league.md`
**L4 market:** `market/market-rugby-league.md`
**Congestion:** `core/core-fixture-congestion.md`
**Women's:** `market/market-womens-sports.md`

*MIT License · SportMind · sportmind.dev*
