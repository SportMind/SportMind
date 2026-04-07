# Live Signals — SportMind Platform

**The division between static intelligence and live inputs.**

SportMind skill files contain structured intelligence that changes slowly —
how a sport works, what signals matter, how modifiers combine. This file
defines the inputs that change continuously and must be fetched in real-time
rather than read from static files.

This is the foundation of SportMind's self-updating architecture.

---

## The static vs live distinction

```
STATIC INTELLIGENCE (read from skill files):
  How football works → sports/football/sport-domain-football.md
  What signals matter for fan tokens → fan-token/fan-token-pulse/
  How to apply the modifier pipeline → core/core-athlete-modifier-system.md
  What the DeFi liquidity thresholds are → fan-token/defi-liquidity-intelligence/
  
  These change rarely (sport rule changes, market structure shifts).
  When they do change, a human contributor updates the relevant skill file.
  Agents read these once and cache them for the session.

LIVE INPUTS (fetched at query time):
  Is BTC above or below its 200-day moving average right now?
  What is this fan token's current pool TVL?
  What is the current holder count trend for $BAR?
  Is this player confirmed in today's lineup?
  What is the current CHZ price vs 30-day average?
  
  These change continuously. Agents must fetch them before each analysis.
  SportMind documents WHAT to check and HOW to interpret it.
  The live data itself comes from external sources (see core/data-sources.md).
```

---

## Live signal categories

### Category 1 — Macro state signals

**Check frequency:** Daily minimum; before any fan token analysis.

```
SIGNAL: Crypto market cycle phase

What to fetch:
  BTC current price
  BTC 200-day moving average (any major exchange or data provider)
  CHZ current price
  CHZ 30-day rolling average

How to interpret (from macro/macro-crypto-market-cycles.md):
  BTC above 200-day MA: → Crypto bull market → apply ×1.20 macro modifier
  BTC below 200-day MA: → Crypto bear market → apply ×0.75 macro modifier
  BTC >20% below 200-day MA OR capitulation signals: → Extreme bear → ×0.55
  Neutral zone (within 5% of MA): → Neutral → ×1.00

Sources:
  CoinGecko API: api.coingecko.com/api/v3/simple/price?ids=bitcoin,chiliz&vs_currencies=usd
  TradingView: BTC/USD chart with 200-day EMA overlay
  Binance API: api.binance.com/api/v3/klines (200-period daily close)

Agent rule: Cache result for 24 hours. Re-fetch if a major price movement
is reported in financial news. Never use a cached result older than 24h
for fan token entry decisions.
```

```
SIGNAL: Active geopolitical or public health event

What to fetch:
  Reuters/Bloomberg headline monitoring (major international news)
  WHO emergency declarations (who.int/emergencies)
  
How to interpret (from macro/macro-geopolitical.md, macro/macro-pandemic-public-health.md):
  Direct conflict affecting a club's home country: apply ×0.60 modifier for that entity
  Global health emergency declared: physical sports ×0.30; digital/tokens ×1.15
  Economic recession confirmed (2+ quarters negative GDP): premium sport ×0.85
  
Agent rule: Flag if a headline matches any of: "war", "invasion", "pandemic",
"health emergency", "recession confirmed", "sanctions". Load the relevant
macro event file and compute the specific modifier.
```

---

### Category 2 — Fan token on-chain signals

**Check frequency:** Before each fan token analysis (per token, per session).

```
SIGNAL: Holder count trend (HCT — component of PHS)

What to fetch:
  Current holder count for the token
  Holder count 30 days ago
  
Source: Chiliz Chain explorer (explorer.chiliz.com) or CoinGecko token page

How to interpret:
  Growing >+2% in 30 days: HCT = 1.0 (healthy)
  Flat ±2%: HCT = 0.7
  Declining 2–10%: HCT = 0.4
  Declining >10%: HCT = 0.1 (critical — begin non-contractual assessment)

Python snippet:
  holders_now = get_chiliz_holders(token_address)
  holders_30d_ago = get_chiliz_holders(token_address, date=today - 30)
  hct_trend_pct = (holders_now - holders_30d_ago) / holders_30d_ago * 100
```

```
SIGNAL: Token Velocity Index (TVI)

What to fetch:
  24h trading volume (CEX primary)
  7-day average trading volume
  
Source: CoinGecko API or Binance API

How to interpret (from fan-token/fan-token-pulse/):
  Current volume / 7-day avg > 2.0: High velocity — elevated engagement signal
  Current volume / 7-day avg 0.8–2.0: Normal velocity
  Current volume / 7-day avg < 0.5: Low velocity — reduced engagement
  Sudden spike (>3× avg) without sporting catalyst: investigate before entering
```

```
SIGNAL: Utility event frequency (UEF — component of PHS)

What to fetch:
  Count of official Socios utility events in last 90 days for this token
  
Source: Socios.com token page (utility event history)

How to interpret:
  ≥4 events in 90 days: UEF = 1.0 (active partnership)
  2–3 events: UEF = 0.7
  0–1 events: UEF = 0.3 (plateau or declining signal)
  0 events for 180+ days: Begin non-contractual token assessment
```

---

### Category 3 — DeFi and liquidity signals

**Check frequency:** Before every fan token position entry — no exceptions.

```
SIGNAL: Pool TVL and slippage estimate

What to fetch:
  Primary DEX pool TVL for the token pair
  24h pool volume (for slippage estimation)
  
Source: GeckoTerminal API
  GET https://api.geckoterminal.com/api/v2/networks/chiliz/pools/{pool_address}
  Returns: reserve_in_usd, volume_usd_24h, price_change_percentage_*

How to interpret (from fan-token/defi-liquidity-intelligence/):
  TVL > $5M: No position size constraint
  TVL $500k–$5M: Normal execution
  TVL $100k–$500k: LIQUIDITY_WARNING — max 40% position
  TVL < $100k: LIQUIDITY_CRITICAL — max 20% position or ABSTAIN

Slippage estimation:
  estimated_slippage_pct = (intended_trade_usd / (tvl_usd / 2)) * 100
  If > 3%: LIQUIDITY_CRITICAL regardless of TVL
```

```
SIGNAL: LP activity (recent additions/removals)

What to fetch:
  Last 48h pool add/remove transactions
  
Source: GeckoTerminal pool transactions or Dune Analytics dashboard

How to interpret:
  Large LP addition (>5% TVL) from new wallet: ACCUMULATION signal
  Multiple small additions over 24h: Patient accumulation — possible pre-event
  Large LP removal (>10% TVL): Monitor — could be profit-taking or exit signal
  Complete pool drain: CRITICAL — begin lifecycle phase reassessment
```

---

### Category 4 — Athlete and team live signals

**Check frequency:** 24h before event, 3h before event, and at lineup confirmation.

```
SIGNAL: Official lineup / player availability

What to fetch:
  Official team lineup (released T-60min for most competitions)
  Injury report (varies by sport — see sport domain skill for timing)
  
Sources by sport:
  Football: Official club website, BBC Sport, Sky Sports lineups
  NFL: NFL.com official injury report (Wed/Thu/Fri designations)
  NBA: ESPN injury tracker, team official injury report
  Cricket: ESPNcricinfo match page (playing XI announced day of match)
  MMA: UFC.com official lineup (confirmed at weigh-in completion)
  Horse racing: Racing Post racecard (final declarations)

How to interpret:
  Official lineup confirmed: Apply lineup_confirmed modifier (×1.15)
  Key player DOUBT: Apply availability modifier (×0.85); set injury_warning flag
  Key player OUT: Apply availability floor (×0.70); reassess signal
  Lineup still unconfirmed at T-2h: Set lineup_unconfirmed flag; reduce position

Agent timing rule:
  T-24h: Preliminary availability check (injury designations, press conference)
  T-3h: Official lineup check (most sports release by this point)
  T-60min: Final confirmation check; last chance to set lineup_confirmed modifier
```

```
SIGNAL: Fixture congestion (days since last match)

What to fetch:
  Date of team's last competitive match
  Date of team's next match after this one
  Any travel required between matches
  
Source: Official competition fixture lists (league websites, BBC Sport)

How to interpret (from core/core-fixture-congestion.md):
  3+ matches in 7 days: Tier 1 congestion → ×0.88
  3 matches in 8–12 days: Tier 2 → ×0.93
  3 matches in 13–18 days: Tier 3 → ×0.97
  Standard spacing: Tier 4 → ×1.00 (no modifier)
  8+ days rest: Tier 5 → ×1.03

This is calculable from fixture data. No external API needed — just dates.
```

---

### Category 5 — Weather and match conditions

**Check frequency:** 24h before event (flag) and 3h before event (confirm).

```
SIGNAL: Match-day weather forecast

What to fetch:
  Wind speed and direction at venue
  Rain probability (%)
  Temperature
  
Source: Weather.com (weather.com/weather/hourbyhour), BBC Weather,
        or Weather API: api.weatherapi.com/v1/forecast.json

Applicable sports (from core/core-weather-match-day.md):
  Cricket, horse racing, cycling, athletics, golf, rugby, NFL, football, tennis (outdoor)
  
Agent rule: For indoor sports (MMA, esports, snooker, basketball, ice hockey):
  Skip weather check entirely — no modifier needed.

Abandonment check:
  If rain probability > 40% for T20 cricket: DLS scenario possible
  If wind > 40mph for outdoor athletics: Check event modification policy
  If abandonment probability > 15%: Reduce position size
  If abandonment probability > 30%: ABSTAIN
```

---

### Category 6 — Prediction market and DeFi protocol signals

**Check frequency:** When using prediction markets or DeFi platforms.

```
SIGNAL: Prediction market pool size (Azuro / Polymarket)

What to fetch:
  Pool TVL for the specific match outcome market
  Current implied odds from pool state
  LP add/remove activity in last 24h
  
Source:
  Azuro: api.azuro.org (market liquidity endpoint)
  Polymarket: clob.polymarket.com/markets

How to interpret (from fan-token/defi-liquidity-intelligence/):
  Large pool (>$500k): Market has conviction — odds are meaningful signal
  Small pool (<$50k): Odds are low-signal; thin liquidity distorts pricing
  Odds moving against market consensus: Possible information asymmetry — flag
  Pool TVL growing rapidly before event: Elevated engagement — cross-reference
    with social volume and athlete social lift (AELS)
```

---

## Automated monitoring architecture

The live signals above fall into three monitoring patterns:

```
PATTERN 1 — CONTINUOUS MONITORING (run every 4–6 hours):
  BTC vs 200-day MA → macro_modifier update
  CHZ price vs 30-day avg → CHZ trend state
  Active geopolitical/health events → macro event flags
  
  Implementation: Cron job or scheduled Lambda/Cloud Function
  Output: Update a shared state object that all agent sessions read on startup
  Alert trigger: When state changes (e.g. BTC crosses 200-day MA)

PATTERN 2 — SESSION MONITORING (run at session start + before each decision):
  Token holder count trend → HCT component
  Token trading volume → TVI component
  Pool TVL → liquidity flags
  LP activity → accumulation/distribution signal
  
  Implementation: API calls at decision time (not cached between sessions)
  Output: Populate defi_context and token-specific PHS components

PATTERN 3 — EVENT MONITORING (run at T-24h, T-3h, T-60min before events):
  Official lineup → lineup_confirmed modifier
  Injury designations → injury_warning flag
  Weather forecast → weather modifier
  Fixture congestion → congestion modifier
  
  Implementation: Scheduled webhooks per event; or polling on event calendar
  Output: Final modifier values for the confidence output schema
```

---

## Self-update signals — what triggers a skill file review

Some live signal patterns indicate that a SportMind skill file may need updating:

```
SKILL FILE REVIEW TRIGGERS:

Automatic detection (agent can flag these):
  "Sport X has changed its competition format" → Review sports/{sport}/
  "New Tier 1 fan token launched" → Review market/{sport}/; update tier
  "Chiliz announces new validator" → Review blockchain-validator-intelligence/
  "Major regulatory change in key market" → Review macro-economic-cycles.md

How to flag:
  Create a GitHub Issue with label: skill-review-needed
  Include: which skill file, what change was detected, source URL
  A maintainer reviews within 72h and updates the relevant file

What agents should NOT try to update automatically:
  Sport domain intelligence (requires domain expert review)
  Modifier weights (requires calibration against historical data)
  Partnership health assessments (requires human verification)
  Any content requiring sport-specific judgment

The self-update architecture keeps files accurate at the FACT level
while keeping intelligence accurate at the REASONING level.
Facts can be detected automatically. Reasoning requires humans.
```

---

## Developer integration

```python
# Example: full live signal check before fan token analysis

import requests
from datetime import datetime, timedelta

def get_live_signals(token_symbol: str, sport: str, trade_size_usd: float) -> dict:
    """Fetch all live signals needed before a fan token analysis."""
    
    signals = {}
    
    # Category 1: Macro state
    btc = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "bitcoin,chiliz", "vs_currencies": "usd",
                "include_24hr_change": "true"}
    ).json()
    signals["btc_price"] = btc["bitcoin"]["usd"]
    signals["chz_price"] = btc["chiliz"]["usd"]
    # Note: 200-day MA requires historical data; use TradingView or Binance klines
    
    # Category 3: DeFi/liquidity
    pool_data = requests.get(
        f"https://api.geckoterminal.com/api/v2/search/pools",
        params={"query": token_symbol, "network": "chiliz"}
    ).json()
    if pool_data.get("data"):
        pool = pool_data["data"][0]["attributes"]
        tvl = float(pool.get("reserve_in_usd", 0))
        signals["pool_tvl_usd"] = tvl
        signals["estimated_slippage_pct"] = (trade_size_usd / (tvl / 2)) * 100 if tvl > 0 else 100
        signals["liquidity_warning"] = tvl < 500_000
        signals["liquidity_critical"] = tvl < 100_000 or signals["estimated_slippage_pct"] > 3
    
    return signals

# Then pass to SportMind contract
response = sportmind.call({
    "skill": "signal.full",
    "sport": sport,
    "context": {"token_symbol": token_symbol},
    "inputs": {
        "base_score": your_platform_score,
        "trade_size_usd": trade_size_usd,
        "live_signals": signals  # Pass pre-fetched signals
    }
})
```

---

## Relationship to v3.0 roadmap items

```
This file enables:
  ✓ "Macro event monitoring alerts" — Category 1 signals define exactly what to monitor
  ✓ "Real-time skill updates" — Self-update signal triggers define what flags reviews
  ✓ "SportMind score (unified metric)" — All Category 1-5 signals feed the score
  ✓ "Skill registry API" — Live signals are the dynamic layer the API serves

This file does NOT replace:
  Static skill files — intelligence layer; updated by community
  Modifier pipeline — reasoning layer; updated through calibration
  Platform contracts — interface layer; versioned independently
```

---

*MIT License · SportMind · sportmind.dev*
