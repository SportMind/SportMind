# Cricket Token Intelligence — SportMind Layer 3

Bridge skill connecting cricket events to fan token and prediction market signals.
Cricket's token ecosystem is format-dependent, geography-concentrated, and uniquely
influenced by India's regulatory environment — the single largest variable in the
global cricket token market.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS:
  Active tokens: PSL (Pakistan Super League) clubs — most commercially developed
  Largest opportunity: IPL (India Premier League) — blocked by Indian regulation
  Growing: The Hundred (England), WBBL (Australia), Caribbean Premier League
  
SIGNAL CHARACTERISTICS:
  Most format-sensitive sport in the library — T20, ODI, Test require separate models
  Highest single-match signal: India vs Pakistan (ICC events)
  Most data-rich: ESPNcricinfo Statsguru — deepest cricket database globally
  DLS risk: Weather creates unique in-match signal complexity
  Dew factor: Evening matches in South Asia change game dynamics mid-innings
```

---

## Cricket Token Impact Score (CricTIS)

```
CricTIS = (Format_Weight × 0.30) + (Match_Importance × 0.30)
         + (India_Factor × 0.25) + (Token_Suite_Status × 0.15)

FORMAT WEIGHTS:
  ICC T20 World Cup final:        1.00
  ICC ODI World Cup final:        0.95
  IPL final:                      0.90 (when tokens exist)
  Ashes Test series (decisive):   0.85
  PSL final:                      0.75
  The Hundred final:              0.65
  Standard T20 league match:      0.40
  Standard ODI:                   0.35
  Standard Test match:            0.30 (lower token volatility; longer duration)

INDIA FACTOR:
  Match involves Indian team or IPL franchise: × 1.40 multiplier
  Match involves Pakistan: × 1.25 multiplier
  India vs Pakistan: × 2.00 multiplier (highest single-match factor in cricket)
  No India or Pakistan involvement: × 1.00 (standard)
```

---

## Format intelligence

```
T20 FORMAT — PRIMARY TOKEN SIGNAL FORMAT:
  Duration: ~3 hours (both innings combined)
  DLS risk: Moderate (rain interruptions trigger DLS calculation)
  Dew factor: HIGH in evening matches at South Asian venues
  Token signal speed: Fast — match result known within 3h of start
  
  Key T20 catalysts:
    Super Over (tie): Highest single-T20 engagement event; social volume 5–8× normal
    Last-over victory: Extended narrative window; +3–6h engagement
    Star batter century: Record proximity signal (rare in T20); +8–12% token signal
    Upset (lower-ranked team wins): Load core-narrative-momentum.md

ODI FORMAT — SECONDARY TOKEN SIGNAL FORMAT:
  Duration: ~7 hours
  DLS risk: HIGH (50-over matches have more weather exposure)
  World Cup matches: Treated as Tier 1 equivalent
  
  Agent note: ODI World Cup (every 4 years) is cricket's highest commercial event.
  ICC Cricket World Cup 2027 (South Africa): Mark as primary catalyst window.

TEST FORMAT — LOWEST TOKEN VOLATILITY:
  Duration: Up to 5 days
  No DLS: Abandoned days are replayed; no artificial targets
  Ashes series (England vs Australia): Highest prestige; strongest narrative arc
  Agent note: Test cricket generates sustained narrative but not single-event spikes.
  Use rolling 5-day narrative momentum model rather than event-based signal.
```

---

## IPL — the blocked opportunity

```
THE IPL SIGNAL GAP:

IPL is the highest-value untapped fan token market globally:
  IPL franchise valuations: $1B+ for top clubs
  IPL media rights: $6.2B cycle
  IPL viewership: 650M+ total viewers per season
  Fantasy cricket (Dream11): 200M+ users — largest daily fantasy platform globally
  
WHY NO IPL TOKENS EXIST:
  India's regulatory framework: Virtual Digital Assets (VDA) regulations do not
  currently provide a clear pathway for sports fan tokens as a distinct category.
  BCCI (Board of Control for Cricket in India) has not engaged with token platforms.
  Dream11's success shows the market appetite exists — regulatory timing is the only barrier.

AGENT MONITORING RULE:
  Track: India Ministry of Finance / SEBI crypto framework announcements
  Track: BCCI digital strategy communications
  Track: IPL franchise announcements on digital products
  
  When Indian VDA framework provides token clarity:
    → IPL fan tokens become the most important single launch event in sports blockchain
    → Estimated CHZ/token ecosystem impact: +20–40% from IPL alone
    → Cross-reference with: market/market-cricket.md (India regulatory variable section)

WIPL (WOMEN'S IPL) PATHWAY:
  Women's IPL launched 2023 with $572M franchise valuations
  May face fewer regulatory sensitivities than men's IPL
  Could precede men's IPL token launches
  See: market/market-womens-sports.md
```

---

## PSL token intelligence

```
PSL (PAKISTAN SUPER LEAGUE) TOKENS:
  The most commercially developed cricket token ecosystem
  Active Socios partnership; multiple franchise tokens
  
PSL SIGNAL FRAMEWORK:
  Season: February–March annually (6 weeks)
  Venues: Karachi, Lahore, Rawalpindi, Multan, Peshawar
  
  Top-tier match signal: PSL final / Karachi Kings vs Lahore Qalandars derby
  CHZ signal impact: Peak PSL match → +3–8% related token signal
  
  GEOPOLITICAL MODIFIER:
    PSL is played in Pakistan; geopolitical stability is a signal input
    Load macro/macro-geopolitical.md for Pakistan political stability assessment
    Any security incident → immediate ABSTAIN flag for PSL token positions
    Pakistan-India diplomatic relationship affects tournament scheduling
    → Monitor: BCCI-PCB relations for bilateral series potential

PSL SIGNAL CALENDAR:
  January: Team draft and squad announcements
  February: Season opens — Lahore or Karachi opener
  Late February: Derby matches (highest engagement)
  March: Playoffs + Final
  Off-season: Monitor player retentions and international call-ups
```

---

## Key agent reasoning rules

```
CRICKET TOKEN AGENT RULES:

1. CHECK FORMAT FIRST — T20, ODI, and Test require completely different
   signal models. Never apply T20 logic to Test cricket.

2. DEW FACTOR CHECK — For evening matches at South Asian venues (IPL, PSL,
   BPL, CPL), check dew forecast. High dew = batting second advantage +8–12%.
   Load core-weather-match-day.md — cricket section.

3. INDIA-PAKISTAN MODIFIER — Whenever these teams meet, apply × 2.00 to
   the base signal weight. No other fixture in any sport generates equivalent
   commercial and social volume.

4. DLS AWARENESS — Any outdoor match with rain forecast carries DLS risk.
   Check weather 24h and 3h before. Rain probability >40% in T20 = DLS possible.
   Load core-weather-match-day.md — DLS section.

5. IPL REGULATORY TRACKING — If India announces regulatory clarity for
   sports tokens, treat as the highest-priority market intelligence event
   in the entire library. Escalate to full portfolio review.

6. TEST SERIES DEPTH — By Test 4–5 of a 5-match series, fast bowlers are
   significantly fatigued. Apply Tier 2 congestion modifier for leading
   quick bowlers. Load core-fixture-congestion.md — cricket section.
```

---

## Compatibility

**L1 domain:** `sports/cricket/sport-domain-cricket.md`
**L2 athlete:** `athlete/cricket/athlete-intel-cricket.md`
**L4 market:** `market/market-cricket.md`
**Women's cricket:** `market/market-womens-sports.md`
**Weather/DLS:** `core/core-weather-match-day.md`
**Geopolitical:** `macro/macro-geopolitical.md`

*MIT License · SportMind · sportmind.dev*
