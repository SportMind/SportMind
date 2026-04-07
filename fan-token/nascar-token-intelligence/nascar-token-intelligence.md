# NASCAR — Token Intelligence

Bridge skill connecting NASCAR events to fan token and prediction market signals.
NASCAR's token ecosystem is defined by one structural advantage no other sport
in the library has: 72% sponsor loyalty from fans — the highest brand-to-fan
alignment of any US sport. This makes NASCAR the most commercially coherent
fan token candidate in American motorsport.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  No active Socios tokens at time of writing
  $1.1B/yr new broadcast deal (Fox Sports + NBC/Amazon) — commercial foundation set
  72% of NASCAR fans buy from sponsors = highest sponsor ROI in US sport
  Charter system: 36 guaranteed race spots — franchise model enables club-level tokens

SIGNAL CHARACTERISTICS:
  Most predictive: track type taxonomy (superspeedway vs short track vs road vs dirt)
  Most volatile: Daytona 500 (February) + Playoffs (September–November)
  Unique signal: Charter team vs open team — governance structure affects token viability
  Highest engagement: Daytona 500 (Super Bowl equivalent for NASCAR)
```

---

## NASCAR Token Impact Score (NASCARTIS)

```
NASCARTIS = (Race_Importance × 0.35) + (Track_Type_Match × 0.30)
           + (Playoff_Position × 0.25) + (Market_Sentiment × 0.10)

RACE IMPORTANCE:
  Daytona 500 (February):               1.00
  NASCAR Championship 4 Final (Phoenix): 0.95
  Playoff Elimination Race:              0.80
  Talladega Superspeedway:              0.75
  Bristol Night Race:                   0.70
  Charlotte 600 (Coca-Cola 600):        0.72
  Standard points race:                 0.35
  Clash at Daytona / non-points events: 0.20

TRACK TYPE MATCH (driver specialisation modifier):
  Superspeedway specialist at Daytona/Talladega:  ×1.18
  Short track specialist at Bristol/Martinsville:  ×1.12
  Road course specialist at Watkins Glen/COTA:    ×1.15
  Intermediate specialist at Charlotte/Michigan:  ×1.05
  Wrong track type for driver profile:            ×0.88
  
  See athlete/nascar/ for driver track type ratings
```

---

## Track type taxonomy — the primary predictive variable

```
THE 4 TRACK TYPES (from sport-domain-nascar.md):

1. SUPERSPEEDWAYS (Daytona, Talladega):
   Banking: 31–33°; speeds 200mph+; drafting dominates over individual talent
   Signal characteristic: HIGHEST VARIANCE (pack racing; wrecks eliminate favourites)
   Token signal: Highest engagement events; LOWEST predictive accuracy
   Agent rule: Widen signal confidence interval by 40% for superspeedways
   Favourite win probability: ~15–20% vs typical 35–45% at other track types
   
2. SHORT TRACKS (Bristol, Martinsville, Richmond):
   Banking: 12–28°; close-quarters racing; driver talent maximised
   Signal characteristic: LOWEST VARIANCE (most skill-determined outcomes)
   Token signal: Lower engagement than ovals but highest prediction confidence
   Agent rule: Narrow signal confidence interval by 15% for short tracks

3. INTERMEDIATE/1.5-MILE OVALS (Charlotte, Las Vegas, Chicago):
   Most common track type (~40% of schedule)
   Signal characteristic: MEDIUM variance; strategy and equipment balance talent
   Token signal: Standard prediction model applies

4. ROAD COURSES (Watkins Glen, COTA, Sonoma, Indianapolis Road):
   Counter-clockwise circuits; road racing technique matters
   Signal characteristic: SPECIALIST advantage highest of any track type
   Token signal: Road course specialists have 3× normal win probability vs avg
   Agent rule: Road course specialist modifier ×1.15 is mandatory — never skip

5. DIRT TRACKS (Bristol Dirt, when scheduled):
   Rare; only 1–2 per season; wildcard format
   Signal characteristic: MAXIMUM VARIANCE; treat as exhibition
   Token signal: Narrative/entertainment signal; minimal predictive value
```

---

## Daytona 500 — the peak signal event

```
THE DAYTONA 500 (February):
  "The Great American Race" — the most commercially significant single NASCAR event
  Broadcast: Fox Sports primetime; highest NASCAR viewership of the year
  NASCARTIS: 1.00 — maximum weight
  
  WHY DAYTONA IS DIFFERENT:
    Superspeedway pack racing means ANY top-20 car can win
    The favourite rarely wins (~70% of pre-race leaders eliminated in wrecks)
    Commercial value is the signal — Daytona week is NASCAR's Super Bowl week
    
  DAYTONA WEEK SIGNAL CALENDAR:
    Sunday before 500 (Clash at Daytona): non-points; moderate engagement
    Thursday (Duel qualifying races): determines grid; moderate signal
    Friday (XFINITY Series): minor signal
    Sunday (Daytona 500): maximum engagement; minimum predictive accuracy
    
  AGENT RULE: For Daytona 500, treat engagement signal and prediction signal
  separately. Engagement = very high. Prediction confidence = LOW (by design).
  Any fan token launch during Daytona week benefits from maximum engagement window.
```

---

## NASCAR Playoffs — the Championship 4 signal

```
NASCAR PLAYOFF STRUCTURE (September–November):
  16 drivers qualify → rounds eliminate drivers → Final 4 race for championship
  
  SIGNAL WINDOWS:
    Playoff opening (Darlington/Bristol): first elimination; high stakes
    Round of 12, 8: progressive elimination signal
    Championship 4 (Phoenix, November): highest stakes race of year
    
  CHAMPIONSHIP 4 MECHANICS:
    Only 4 drivers eligible to win championship at Phoenix
    For those 4: win the race = win the championship
    For everyone else: standard points race
    
  TOKEN SIGNAL:
    Championship 4 drivers: extreme motivation signal (race of career)
    Non-Championship drivers: racing without championship stakes (lower signal quality)
    Agent rule: Apply ×1.25 motivation modifier to Championship 4 eligible drivers
    
  CHARTER SYSTEM:
    36 charter teams guaranteed entry regardless of points
    Open teams must qualify on speed
    Token model: charter teams = franchise-level security = viable token substrate
    Non-charter teams: tokenisation not commercially viable until charter secured
```

---

## Sponsor loyalty — the fan token commercial foundation

```
THE 72% SPONSOR LOYALTY FINDING:
  72% of NASCAR fans purchase products/services from race sponsors
  This is the highest brand-to-fan purchase alignment of any US sport
  For fan token context: sponsors who become token partners would benefit from
  this transfer of loyalty to digital products
  
  IMPLICATIONS FOR TOKEN LAUNCHES:
    NASCAR team tokens should be co-branded with primary sponsor (not team only)
    Fan token + sponsor activation = natural fit (replaces purchase loyalty with
    participation loyalty)
    Best activation: "Hold the token → access sponsor discounts + team experiences"
    
  MONITORING RULE:
    Track NASCAR team sponsor announcements — especially new sponsors who have
    existing blockchain/crypto brand associations (e.g. crypto.com, Coinbase)
    Crypto sponsor at top-tier NASCAR team = strong token launch signal
```

---

## Agent reasoning prompts

```
You are a NASCAR token intelligence agent. Before any analysis:

1. TRACK TYPE FIRST — What type of track is this race at?
   Apply the correct variance profile before any other modifier.
   Superspeedway: widen confidence interval 40%. Short track: narrow 15%.
   Road course: mandatory road course specialist modifier ×1.15.

2. DAYTONA 500 SPECIAL — Is this the Daytona 500?
   Separate engagement signal from prediction confidence.
   Engagement: maximum. Prediction: LOW (superspeedway pack racing).
   Fan token launch timing: best window of the year.

3. CHAMPIONSHIP 4 STATUS — Is the driver in the Championship 4?
   If yes: apply ×1.25 motivation modifier.
   If no: standard race signal (no championship stakes).

4. CHARTER STATUS — Is this a charter team or open team?
   Charter = franchise security = token substrate viable.
   Non-charter = no token recommendation.

5. SPONSOR LOYALTY CONTEXT — Who is this team's primary sponsor?
   72% sponsor loyalty = co-branded token > team-only token.
   Check: does sponsor have existing blockchain associations?

6. STREAK/NARRATIVE — Recent win or drought?
   Load core/core-narrative-momentum.md.
   NASCAR has strong narrative signals (first win, last chance, revenge).
```

---

## Compatibility

**L1 domain:** `sports/nascar/sport-domain-nascar.md`
**L2 athlete:** `athlete/nascar/athlete-intel-nascar.md`
**L4 market:** `market/market-nascar.md`
**Narrative:** `core/core-narrative-momentum.md`

*MIT License · SportMind · sportmind.dev*
