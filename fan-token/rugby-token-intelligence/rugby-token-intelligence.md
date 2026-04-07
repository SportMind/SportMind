# Rugby Union — Token Intelligence

Bridge skill connecting rugby union events to fan token and prediction market signals.
CVC Capital Partners' £200M+ investment in the Six Nations (2021) is the strongest
institutional private equity signal for token readiness in any sport outside football.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  CVC Capital Partners invested in Six Nations, URC, and Premiership Rugby
  Private equity entry = commercial professionalisation signal for token readiness
  Rugby World Cup 2027 (Australia): primary catalyst window
  Existing digital products: RugbyPass subscription, Haka analytics (NZ)

SIGNAL CHARACTERISTICS:
  Most predictive: kicker accuracy + set piece dominance
  Most volatile: Six Nations (concentrated European signal, February–March)
  Highest engagement window: Rugby World Cup (every 4 years)
  Unique signal: British & Irish Lions tours (every 4 years; British Isles composite)

KEY MARKET: UK, France, South Africa, New Zealand, Australia, Ireland
  CHZ/Socios primary markets overlap well with rugby union's European core
```

---

## Rugby Token Impact Score (RugbyTIS)

```
RugbyTIS = (Competition_Tier × 0.35) + (Kicker_Status × 0.25)
          + (Set_Piece_Dominance × 0.25) + (Market_Sentiment × 0.15)

COMPETITION TIERS:
  Rugby World Cup Final:              1.00
  Rugby World Cup Semi-Final:         0.88
  Six Nations Grand Slam decider:     0.85
  Six Nations match (top rivalry):    0.70
  URC Final / Premiership Final:      0.65
  Champions Cup Final:                0.75
  Champions Cup Quarter-Final:        0.58
  Standard Six Nations:               0.50
  Standard URC/Premiership:           0.30

KICKER STATUS:
  Penalty kicks win ~70% of close rugby matches.
  Starting kicker fit and in form: neutral (×1.00)
  Starting kicker doubtful: ×0.90
  Starting kicker out: ×0.82 (kicker replacement is most impactful positional loss)
  Replacement kicker (debutant): ×0.75
```

---

## The CVC investment signal

```
WHY CVC MATTERS FOR FAN TOKENS:

CVC Capital Partners investment pattern:
  F1 (2017): CVC sold stake → F1 went to Liberty Media → Drive to Survive →
              massive global fanbase growth → constructor tokens viable
  Six Nations (2021): £200M for 14.3% stake
  United Rugby Championship (2021): significant stake
  Premiership Rugby (2022): significant stake

The CVC pattern in sport:
  Step 1: Private equity invests for commercial professionalisation
  Step 2: Central commercial deals are negotiated (broadcast, digital)
  Step 3: Digital fan engagement products are prioritised
  Step 4: Fan token platforms become commercially viable
  
  F1 is the proof of concept: CVC investment → 5 years → constructor tokens active
  Rugby Union is approximately 3–4 years behind F1 on this trajectory

AGENT MONITORING RULE:
  Track: CVC/Six Nations digital strategy announcements
  Track: World Rugby digital product strategy (worldrugby.org)
  Track: Individual union digital rights discussions (RFU, FFR, IRFU, SARU)
  
  When any major union announces a digital fan product partnership:
    Apply Tier 2 → Tier 1 upgrade signal for that union's commercial tier
```

---

## Rugby World Cup 2027 — the primary catalyst window

```
RUGBY WORLD CUP 2027 (Australia):

Timeline:
  Host announced: Australia confirmed (2023)
  Tournament: September–November 2027
  Qualification period: 2025–2027

Why this RWC matters:
  Australia is the highest crypto-adoption country in the top rugby nations
  Australian government's clear crypto regulatory framework = commercial confidence
  Southern Hemisphere RWC = Southern Hemisphere fan engagement peak
  
Signal calendar (pre-2027):
  2025–2026: Pool draw, team qualification = progressive signal building
  2026: Final 20 teams confirmed = franchise signal events
  June 2027: RWC opens in Australia = global rugby peak

TOKEN LAUNCH TIMING:
  Optimal window: 12 months before RWC (September 2026)
  Second window: RWC pool draw announcement
  Emergency window: Any major upset in pool stages

BRITISH & IRISH LIONS (2025, Australia):
  Lions tours every 4 years are the highest-rated rugby broadcast events
  Composite team from England/Wales/Scotland/Ireland
  No Lions token exists (composite team) but Lions tour = signal catalyst
  for individual nation tokens (England $ENG, Ireland $IRE etc.)
```

---

## Six Nations — annual peak signal window

```
SIX NATIONS CALENDAR:
  February–March annually (5 rounds over 8 weekends)
  Teams: England, France, Ireland, Scotland, Wales, Italy
  
  Grand Slam: team wins all 5 matches — rarest achievement
  Triple Crown: Home Nations (ENG/WAL/SCO/IRE) win all 3 inter-HN matches
  Calcutta Cup: England vs Scotland (oldest international rugby fixture)
  
SIGNAL MAPPING:
  Grand Slam race (Round 4/5): highest Six Nations signal
  England vs Ireland: highest viewership clash in tournament
  France vs England: highest token-market-relevant match (both large CHZ markets)
  Italy: consistent underdog — upsets generate outsized narrative signal

HOME ADVANTAGE IN SIX NATIONS:
  Twickenham (England): capacity 82,000 — historically strongest home advantage
  Aviva Stadium (Ireland): capacity 51,700 — Ireland home record strong
  Stade de France (France): capacity 80,000
  
  Load core/core-weather-match-day.md for outdoor winter conditions
  February matches: wind/rain risk particularly relevant
```

---

## Agent reasoning prompts

```
You are a rugby union token intelligence agent. Before any analysis:

1. KICKER STATUS FIRST — Starting kicker confirmed fit?
   Kicker is the most impactful single position in rugby union.
   A kicker change can shift expected margin by 6-9 points.

2. SET PIECE CHECK — Lineout and scrum dominance assessment?
   Load athlete/rugby/ for set piece modifier.
   Teams with dominant set piece win close matches at ~65%.

3. COMPETITION TIER — RWC vs Six Nations vs URC vs Champions Cup?
   Apply correct tier weight. RWC Final and Six Nations Grand Slam
   deciders are the highest-weight events in the library.

4. HOME ADVANTAGE — Twickenham, Aviva, Stade de France, Loftus Versfeld?
   Rugby union home advantage is among the strongest in any team sport.
   Apply home factor before applying form differential.

5. CVC SIGNAL — Any CVC/union digital product announcements this week?
   Load as commercial tier upgrade signal if applicable.

6. WEATHER — February/March Six Nations = outdoor winter conditions.
   Load core/core-weather-match-day.md.
   Wind >20mph = kicking game favoured over handling.
```

---

## Compatibility

**L1 domain:** `sports/rugby/sport-domain-rugby-union.md`
**L2 athlete:** `athlete/rugby/athlete-intel-rugby-union.md`
**L4 market:** `market/market-rugby-union.md`
**Weather:** `core/core-weather-match-day.md`

*MIT License · SportMind · sportmind.dev*
