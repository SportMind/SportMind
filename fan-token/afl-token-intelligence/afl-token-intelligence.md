# Australian Rules Football (AFL) — Token Intelligence

Bridge skill connecting AFL events to fan token and prediction market signals.
Australia has the highest per-capita cryptocurrency adoption of any major sports
market (25%+), making AFL the most crypto-ready untapped token opportunity in
the Southern Hemisphere.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  No major active Socios tokens at time of writing
  AFL club membership culture = strongest existing digital fan product
  AFL Fantasy: 1M+ users = largest Australian sports DFS platform
  MCG Grand Final: highest-attended single-sport event in Southern Hemisphere

SIGNAL CHARACTERISTICS:
  Most predictive: kicking accuracy differential + home ground advantage
  Most volatile: Finals series entry (August — September squeeze)
  Highest engagement window: MCG Grand Final (September)
  Unique signal: ANZAC Day Collingwood–Essendon (highest single-game AFL attendance)

STRUCTURAL NOTE: AFL operates under a centralised commission model.
  18 clubs across Australia and New Zealand.
  Hard salary cap + draft system = strongest competitive balance in global sport.
  Fan token model: club-level tokens viable; MCG + home crowd are amplifiers.
```

---

## AFL Token Impact Score (AFLTIS)

```
AFLTIS = (Game_Importance × 0.35) + (Home_Ground_Factor × 0.25)
        + (Finals_Position × 0.25) + (Market_Sentiment × 0.15)

GAME IMPORTANCE:
  AFL Grand Final (MCG):           1.00
  Preliminary Final:               0.85
  Semi-Final:                      0.72
  Elimination/Qualifying Final:    0.60
  ANZAC Day (Collingwood vs Essendon): 0.80 (cultural peak; non-final)
  Round 1 (season opener):         0.55
  Standard home-and-away:          0.30

HOME GROUND FACTOR:
  Home team at own ground (50,000+): +12% signal boost
  MCG specifically: highest home advantage in AFL — +15% boost
  Travelling team (2+ states away): -8% signal adjustment
  Interstate travel (WA/QLD/SA vs VIC/NSW): apply fatigue modifier
```

---

## The MCG Grand Final — peak signal architecture

```
THE GRAND FINAL SIGNAL MODEL:

MCG context:
  Capacity: ~100,000 (largest capacity for any regular sporting venue in world)
  Grand Final always at MCG (by tradition since 1902)
  Cultural significance in Melbourne = equivalent to FA Cup Final in England
  
Timing:
  Always last Saturday in September
  Week off between Preliminary Final and Grand Final = recovery advantage
  Grand Final week = highest AFL media coverage of year

Signal windows:
  Preliminary Final (2 weeks before): finalist identity locked — signal event
  Grand Final week: sustained positive signal for both clubs
  Grand Final day: peak single-event signal
  Post-Grand Final: winner +20–30% sustained (Premiership year)
                    loser: -10–15% immediate; recovery over 4-6 weeks

ANZAC DAY EXCEPTION:
  Collingwood vs Essendon, April 25 at MCG
  Always sells out (~85,000) — cultural event, not just sporting
  Signal weight: treat as Finals-level for token/prediction purposes
  Even in low-ladder years, this match generates disproportionate engagement
```

---

## Australian crypto market context

```
WHY AFL IS THE HIGHEST-PRIORITY SOUTHERN HEMISPHERE TOKEN OPPORTUNITY:

Crypto adoption rate:
  Australia: ~25% of adults have owned crypto (among highest globally)
  AFL fanbase demographic: 18–45 skew = high crypto overlap

Existing digital engagement:
  AFL Fantasy: 1M+ registered users
  SuperCoach (AFL): 600,000+ users
  Kayo Sports (streaming): 1M+ subscribers
  These platforms prove AFL fans will pay for digital sports products

Club membership culture:
  AFL clubs have the strongest fan membership culture in Australian sport
  Average Collingwood/Richmond/Carlton member: pays $200-400/yr for membership
  Fan tokens = natural extension of existing digital membership products

Token launch timing:
  Best window: Grand Final week announcement
  Second best: ANZAC Day week for Melbourne clubs
  Season start (March): Round 1 launch if club has strong offseason recruitment

MONITORING RULE:
  Track AFL club digital product announcements
  Track Chiliz/Socios APAC expansion communications
  AFL Players' Association digital rights = key commercial gateway
```

---

## Competition structure signal map

```
FINALS SERIES — 8 teams qualify:

Week 1:
  Qualifying Final (1v2, 3v4): winners through to Prelim; losers get second chance
  Elimination Final (5v8, 6v7): losers eliminated immediately — sharp negative signal
  
Week 2:
  Semi-Final: last-chance for Qualifying losers
  
Week 3:
  Preliminary Final: last match before Grand Final — highest tension
  
Week 4:
  Grand Final (always MCG, always September)

TOKEN SIGNAL BY STAGE:
  Making finals: +8–12% sentiment
  Winning Qualifying Final (direct path): +5–8%
  Losing Elimination Final (exit): -15–20%
  Grand Final qualification: +18–25%
  Premiership win: +25–35% sustained
```

---

## Agent reasoning prompts

```
You are an AFL token intelligence agent. Before any analysis:

1. GRAND FINAL PROXIMITY — How many rounds until Grand Final?
   Signal intensity scales as finals approach. Treat September as peak.

2. HOME GROUND FACTOR — Home team at MCG or own ground?
   AFL home advantage is among the strongest in the library. Always apply.

3. INTERSTATE TRAVEL — Is the away team from WA, QLD, or SA playing in VIC?
   Fatigue modifier applies. Load core/core-fixture-congestion.md.

4. ANZAC DAY CHECK — Is this Collingwood vs Essendon on April 25?
   Apply Finals-level signal weight regardless of ladder position.

5. KICKING ACCURACY — Load athlete/afl/ for kicking accuracy differential.
   This is the primary predictive individual variable in AFL.

6. CRYPTO CONTEXT — Australia's 25% adoption rate means AFL token launches
   will get disproportionate early adopter response vs other markets.
   Model token launch timing around Grand Final week.
```

---

## Compatibility

**L1 domain:** `sports/afl/sport-domain-afl.md`
**L2 athlete:** `athlete/afl/athlete-intel-afl.md`
**L4 market:** `market/market-afl.md`
**Draft:** `core/core-draft-intelligence.md`

*MIT License · SportMind · sportmind.dev*
