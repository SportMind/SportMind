# API Providers — SportMind Data Layer Guide

**Which data APIs work well with SportMind, how to get started quickly,
and a complete end-to-end flow from API key to production signal.**

SportMind is the intelligence framework. These APIs are the data layer.
Together they produce production-quality signals — SportMind tells your
agent what the numbers mean; the APIs give you the numbers.

This document is for developers who want to go from zero to a working
SportMind signal as fast as possible.

---

## The principle

```
SPORTMIND + DATA API = PRODUCTION SIGNAL

SportMind provides (free, static, loaded once):
  → Reasoning framework — what signals matter and why
  → Modifier models — how to weight each input
  → Disciplinary intelligence — how conduct affects signals
  → Fan token commercial intelligence — how sport affects token price

Data API provides (live, fetched per-analysis):
  → Who is playing (lineup confirmation)
  → Current form and statistics
  → Match results and standings
  → Weather and conditions

The agent applies SportMind's framework to the API data.
SportMind is the brain. The API is the sensory input.
```

---

## Quickest path to a working signal

If you want a SportMind football signal running in under an hour:

```
1. Get an API-Football key (free):
   → https://dashboard.api-football.com/register
   → Free tier: 100 requests/day — enough for testing

2. Clone SportMind and install dependencies:
   → git clone https://github.com/SportMind/SportMind
   → pip install mcp aiohttp

3. Run the MCP server:
   → python scripts/sportmind_mcp.py

4. Call sportmind_pre_match for your chosen fixture

5. Fetch lineup confirmation from API-Football

6. Combine: SportMind signal + live lineup = production signal
```

Full working code is in the flow section below.

---

## API providers by sport

### Football — Tier 1 recommendations

**API-Football** (api-football.com / api-sports.io)
```
Free tier:     100 requests/day
Paid tier:     from $9.99/month (1,000 req/day)
Coverage:      900+ leagues and competitions globally
Endpoint base: https://v3.football.api-sports.io
RapidAPI:      https://rapidapi.com/api-sports/api/api-football

Best for:      Lineup confirmation, match results, standings, form,
               player statistics, head-to-head data

SportMind fit: Maps directly onto lineup_unconfirmed flag and
               form sub-modifier inputs. The most complete free
               football API available.

Key endpoints:
  /fixtures?id={id}                → match status + lineup (T-1h)
  /players?id={id}&season={year}   → player form and statistics
  /standings?league={id}&season=   → current standings
  /fixtures/statistics?fixture={id}→ post-match stats
```

**football-data.org**
```
Free tier:     10 requests/minute, top 12 European leagues
Paid tier:     from £11/month (all competitions)
Coverage:      Major European leagues + UCL/UEL
Endpoint base: https://api.football-data.org/v4

Best for:      UCL/UEL/Premier League focused agents
               Already has a working connector in platform/data-connector-templates.md

Note: More limited coverage than API-Football but well-documented
      free tier. Use for UCL fan token work specifically.
```

---

### Multi-sport — API-Sports suite

API-Sports (api-sports.io) provides the same API structure across
multiple sports under one account and one API key pattern.

```
Account:  https://dashboard.api-sports.io/register
Free tier: 100 requests/day per sport
Pricing:  Per-sport subscriptions or bundle

Sports covered with SportMind-relevant endpoints:

FOOTBALL    api.football  → lineups, fixtures, stats, standings
BASKETBALL  api.basketball → NBA, EuroLeague, fixtures, standings
BASEBALL    api.baseball  → MLB fixtures, standings, player stats
RUGBY       api.rugby     → fixtures, standings (limited player stats)
CRICKET     api.cricket   → fixtures, standings (limited granularity)
HANDBALL    api.handball  → EHF fixtures, standings

Endpoint pattern (same across all sports):
  https://v1.{sport}.api-sports.io/{endpoint}
  Header: x-apisports-key: {your-key}

SportMind fit: One account covers six SportMind-supported sports.
               Significant reduction in integration friction for
               multi-sport agents.
```

---

### RapidAPI hub

```
URL:  https://rapidapi.com/hub
Role: Marketplace and unified key management for 40,000+ APIs

Why useful for SportMind developers:
  → Discover sports APIs not listed here
  → Single billing account across multiple providers
  → API-Football is available via RapidAPI with same free tier
  → Consistent header pattern: X-RapidAPI-Key + X-RapidAPI-Host

When to use RapidAPI vs direct:
  Direct (api-sports.io): lower latency, simpler setup, recommended
  RapidAPI: if you already use it for other APIs or prefer unified billing

Notable sports APIs on RapidAPI:
  API-Football:   https://rapidapi.com/api-sports/api/api-football
  API-Basketball: https://rapidapi.com/api-sports/api/api-nba
  The Sports DB:  https://rapidapi.com/theapidb/api/thesportsdb
  Sportradar:     https://rapidapi.com/sportradar/api (paid, professional tier)
```

---

### Sport-specific providers

**Cricket — ESPNcricinfo / Cricbuzz**
```
ESPNcricinfo API: No official public API — use web scraping carefully
                  or Sportmonks Cricket (sportmonks.com/cricket-api)
Sportmonks Cricket:
  Free tier:     Limited — trial available
  Paid:          from €29/month
  Coverage:      International + IPL + all major T20 leagues
  Best for:      Format-specific stats, pitch conditions, DLS scenarios
  
Cricbuzz: No official public API — community wrappers exist on RapidAPI
  https://rapidapi.com/cricketapilive/api/cricbuzz-cricket

For SportMind cricket agents: Sportmonks is the recommended paid option.
Free option: ESPNcricinfo Statsguru (manual query, not API).
```

**Rugby Union — SportRadar**
```
Sportradar Rugby Union:
  URL:      https://developer.sportradar.com
  Coverage: Six Nations, Premiership, URC, World Cup
  Pricing:  Trial available; production pricing on request (professional tier)
  Best for: Team stats, player availability (limited)
  
Honest note: Rugby Union has the most limited free API landscape of any
SportMind-supported sport. For free data: use official World Rugby website
and Fetch MCP (see platform/fetch-mcp-disciplinary.md).
```

**Formula 1 — Jolpica / Ergast**
```
Jolpica F1 API (successor to Ergast):
  URL:      https://api.jolpi.ca/ergast/
  Cost:     Free
  Coverage: Full F1 historical + current season results and standings
  Best for: Race results, qualifying times, driver standings, constructor standings
  
  Key endpoints:
    /f1/current/results.json    → latest race result
    /f1/current/qualifying.json → latest qualifying
    /f1/{year}/{round}/qualifying.json → specific round

  SportMind fit: Qualifying delta (the primary F1 signal) is directly
                 available. No authentication required.

OpenF1 API:
  URL:      https://openf1.org
  Cost:     Free
  Coverage: Live telemetry, car data, lap times during race weekends
  Best for: Real-time race weekend data (practice, qualifying, race)
```

**MMA — UFC Stats API**
```
UFC Stats (unofficial):
  URL:      https://ufcstats.com (scrape carefully)
  RapidAPI: Search "UFC" on rapidapi.com — several wrappers available
  Coverage: All UFC fight history, fighter stats, fight results
  
  For SportMind: fighter strike rate, takedown accuracy, finishing tendency
  are all available via UFC Stats data.
  
Official UFC API: Not publicly available. UFC Stats is the de facto standard.
```

**Basketball — NBA**
```
NBA Official API:
  URL:      https://stats.nba.com (unofficial access — no key required)
  Coverage: Full NBA stats, player tracking, advanced metrics
  
  Better option: balldontlie API
  URL:       https://www.balldontlie.io
  Free tier: 60 requests/minute
  Coverage:  NBA stats, players, games, standings

  SportMind fit: Load management status, on/off splits, injury reports
                 all derivable from balldontlie + official NBA injury page.
```

**Weather (cross-sport)**
```
Open-Meteo:
  URL:      https://open-meteo.com
  Cost:     Free (non-commercial), no API key required
  Coverage: Global weather forecast + historical
  Best for: Cricket dew prediction, F1 wet weather, outdoor sports
  
  Key endpoint:
    https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}
    &hourly=precipitation_probability,windspeed_10m,relativehumidity_2m

  SportMind fit: Maps directly onto core/core-weather-match-day.md signals.
                 Cricket dew factor requires humidity at ground location.
```

---

## What to look for in any sports API

Use this framework to evaluate APIs not listed here:

```
ESSENTIAL:
  ✓ Lineup data available T-2h or earlier (for lineup_unconfirmed flag)
  ✓ Player-level statistics (for form sub-modifier)
  ✓ Historical data accessible (for H2H and form window)
  ✓ Reasonable free tier for development and testing

USEFUL:
  ✓ Injury/availability status (saves manual monitoring)
  ✓ Real-time match updates (for in-play signal adjustment)
  ✓ Competition-level coverage matching your use case
  ✓ Consistent player ID system (for cross-referencing)

CAUTION FLAGS:
  ✗ No historical data — cannot verify form signals
  ✗ Lineup data only available T-30min — too late for fan token positioning
  ✗ No player-level stats — only team-level aggregates
  ✗ Documentation sparse or out of date
  ✗ No rate limit documentation — unexpected 429 errors in production
```

---

## Complete end-to-end flow — football fan token signal

This is a working example of a full SportMind signal pipeline combining
API-Football live data with SportMind intelligence.

**Scenario:** PSG vs Arsenal, UCL Quarter-Final. Token: PSG (Tier 1).
**Goal:** Generate a pre-match fan token signal with live lineup confirmation.

### Step 1 — Environment setup

```bash
# Install dependencies
pip install mcp aiohttp python-dotenv

# .env file
API_FOOTBALL_KEY=your_key_here
SPORTMIND_PATH=/path/to/SportMind
```

### Step 2 — Run SportMind MCP server

```bash
python /path/to/SportMind/scripts/sportmind_mcp.py
# Server running on stdio — Claude Desktop connects automatically
```

### Step 3 — Phase 1: Macro gate

```
# SportMind MCP tool call — use via Claude Desktop, Claude Code,
# or the Anthropic API. See MCP-SERVER.md for connection setup.
#
# Tool: sportmind_macro | Arguments: {}
# Returns: macro_modifier, macro_phase, active_events
#
# If macro_modifier < 0.75: output WAIT_MACRO_OVERRIDE and stop.
```

### Step 4 — Phase 2: SportMind pre-match signal

```python
pre_match = tool_pre_match(
    sport       = 'football',
    home_team   = 'PSG',
    away_team   = 'Arsenal',
    competition = 'UCL',
    kickoff     = '2026-05-07T20:00:00Z',
    use_case    = 'fan_token_tier1'
)

print(f"Direction: {pre_match['signal']['direction']}")
print(f"SMS: {pre_match['sportmind_score']['sms']}")
print(f"Reasoning sequence: {pre_match['reasoning_sequence']}")
```

### Step 5 — Phase 3: Fetch live lineup from API-Football

```python
import aiohttp
import asyncio
from datetime import datetime, timezone

API_FOOTBALL_KEY = "your_key_here"
API_FOOTBALL_BASE = "https://v3.football.api-sports.io"

async def get_psg_arsenal_fixture():
    headers = {
        "x-apisports-key": API_FOOTBALL_KEY
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        # Search for the fixture
        async with session.get(
            f"{API_FOOTBALL_BASE}/fixtures",
            params={
                "league": "2",         # UCL league ID
                "season": "2025",
                "team": "85",          # PSG team ID
                "status": "NS"         # Not started
            }
        ) as resp:
            data = await resp.json()
            fixtures = data.get('response', [])
            
            # Find Arsenal fixture
            for f in fixtures:
                teams = f['teams']
                if (teams['home']['name'] == 'Paris Saint-Germain' and
                    teams['away']['name'] == 'Arsenal') or \
                   (teams['away']['name'] == 'Paris Saint-Germain' and
                    teams['home']['name'] == 'Arsenal'):
                    return f
            return None

async def get_lineup(fixture_id: int):
    headers = {"x-apisports-key": API_FOOTBALL_KEY}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(
            f"{API_FOOTBALL_BASE}/fixtures/lineups",
            params={"fixture": fixture_id}
        ) as resp:
            data = await resp.json()
            lineups = data.get('response', [])
            
            if len(lineups) >= 2:
                return {
                    "lineup_confirmed": True,
                    "home_xi": [p['player']['name']
                                for p in lineups[0]['startXI']],
                    "away_xi": [p['player']['name']
                                for p in lineups[1]['startXI']],
                    "home_formation": lineups[0]['formation'],
                    "away_formation": lineups[1]['formation'],
                }
            return {"lineup_confirmed": False}

# Run
fixture = asyncio.run(get_psg_arsenal_fixture())
if fixture:
    fixture_id = fixture['fixture']['id']
    lineup = asyncio.run(get_lineup(fixture_id))
    print(f"Lineup confirmed: {lineup['lineup_confirmed']}")
```

### Step 6 — Phase 3: Disciplinary check

```python
# Check key PSG players for any active DSM flags
disc = tool_disciplinary(
    player = '',  # Check general PSG squad status
    sport  = 'football',
    club   = 'PSG',
    include_framework = False
)

# Then verify against FA/UEFA source
source = tool_verifiable_source('disciplinary_ban', 'football')
print(f"Verify at: {source['source']}")
# Output: FA: thefa.com/football-rules-governance/disciplinary

# Assume clean for this example
dsm_modifier = 1.00
active_flags = []
```

### Step 7 — Phase 4: Fan token context

```python
# Get PSG token context
psg_lookup = tool_fan_token_lookup('PSG', False)
psg_token  = psg_lookup['tokens'][0]

print(f"Contract: {psg_token['contract_address']}")
print(f"Verify:   {psg_token['chiliscan_url']}")
print(f"Market:   {psg_token['fantokens_url']}")
print(f"Tier:     {psg_token['market_cap_tier']}")

# Get sentiment snapshot
sentiment = tool_sentiment_snapshot('PSG', 'fan_token_tier1')
print(f"Composite signal: {sentiment['composite_signal']['sms']}")
print(f"Recommended action: {sentiment['composite_signal']['recommended_action']}")
```

### Step 8 — Phase 5: Synthesise final signal

```python
def generate_final_signal(macro_modifier, pre_match, lineup, dsm_modifier, sentiment):
    
    sms = pre_match['sportmind_score']['sms']
    direction = pre_match['signal']['direction']
    adjusted_score = pre_match['signal']['adjusted_score'] * dsm_modifier
    
    # Apply lineup confirmation modifier
    lineup_modifier = 1.0 if lineup['lineup_confirmed'] else 0.92
    
    # Composite
    composite = round(macro_modifier * dsm_modifier * lineup_modifier, 3)
    
    # Decision
    if macro_modifier < 0.75:
        recommendation = "ABSTAIN"
        reason = "Macro override active"
    elif any(f in ['LEGAL_PROCEEDINGS_ACTIVE','COMMERCIAL_RISK_ACTIVE']
             for f in active_flags):
        recommendation = "ABSTAIN"
        reason = "Active disciplinary commercial flag"
    elif sms >= 60 and composite >= 0.88:
        recommendation = "ENTER"
        reason = f"SMS {sms}, composite modifier {composite}"
    elif sms >= 40:
        recommendation = "WAIT"
        reason = f"SMS {sms} — partial coverage"
    else:
        recommendation = "WAIT"
        reason = "Insufficient signal coverage"
    
    return {
        "token":               "PSG",
        "fixture":             "PSG vs Arsenal — UCL QF",
        "recommendation":      recommendation,
        "reason":              reason,
        "signal": {
            "direction":       direction,
            "adjusted_score":  adjusted_score,
            "sms":             sms,
            "composite":       composite,
        },
        "modifiers": {
            "macro":           macro_modifier,
            "dsm":             dsm_modifier,
            "lineup":          lineup_modifier,
        },
        "lineup_confirmed":    lineup['lineup_confirmed'],
        "verification": {
            "chiliscan":       psg_token['chiliscan_url'],
            "fantokens":       psg_token['fantokens_url'],
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sportmind_version": "3.35.0"
    }

final = generate_final_signal(
    macro_modifier = macro_modifier,
    pre_match      = pre_match,
    lineup         = lineup,
    dsm_modifier   = dsm_modifier,
    sentiment      = sentiment
)

print(f"\n{'='*50}")
print(f"FINAL SIGNAL: {final['recommendation']}")
print(f"Reason: {final['reason']}")
print(f"Direction: {final['signal']['direction']}")
print(f"SMS: {final['signal']['sms']}")
print(f"Composite modifier: {final['signal']['composite']}")
print(f"Lineup confirmed: {final['lineup_confirmed']}")
print(f"Verify token: {final['verification']['chiliscan']}")
print(f"{'='*50}\n")
```

### Expected output

```
Macro modifier: 1.00 (NEUTRAL)
Direction: HOME
SMS: 76
Lineup confirmed: True
Reasoning sequence: ['1. sportmind_macro — verify macro modifier', ...]

==================================================
FINAL SIGNAL: ENTER
Reason: SMS 76, composite modifier 1.0
Direction: HOME
SMS: 76
Composite modifier: 1.0
Lineup confirmed: True
Verify token: https://chiliscan.com/token/0xc2661815C69...
==================================================
```

---

## Flow diagram

```
                    ┌─────────────────────┐
                    │   API-Football       │
                    │   (live lineup)      │
                    └──────────┬──────────┘
                               │
┌──────────────┐     ┌─────────▼──────────┐     ┌──────────────────┐
│ SportMind    │     │                    │     │ Chiliz Chain     │
│ MCP Server   ├────►│  Signal synthesis  ├────►│ (token verify)   │
│ (framework)  │     │                    │     │ chiliscan.com    │
└──────────────┘     └─────────┬──────────┘     └──────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │ ENTER / WAIT /       │
                    │ ABSTAIN + reasoning  │
                    └─────────────────────┘

SportMind tools used in this flow:
  sportmind_macro              → Phase 1 gate
  sportmind_pre_match          → Phase 2 base signal
  sportmind_disciplinary       → Phase 3 DSM check
  sportmind_fan_token_lookup   → Phase 4 token registry
  sportmind_sentiment_snapshot → Phase 4 sentiment state
  sportmind_verifiable_source  → Source verification at any phase

External APIs used:
  API-Football (api-sports.io) → Live lineup confirmation
  Open-Meteo (optional)        → Weather if outdoor sport
  CoinGecko (already in templates) → Macro state
```

---

## API rate limit reference

| API | Free tier | Rate limit | Best for |
|---|---|---|---|
| API-Football | 100 req/day | 10/min | Football lineup + stats |
| football-data.org | 10 req/min | 10/min | UCL/PL focused |
| API-Basketball | 100 req/day | 10/min | NBA lineup + stats |
| API-Cricket | 100 req/day | 10/min | IPL/ICC fixtures |
| API-Rugby | 100 req/day | 10/min | Fixtures only |
| Jolpica F1 | Unlimited | Fair use | F1 results + qualifying |
| Open-Meteo | Unlimited | Fair use | Weather (all sports) |
| balldontlie | 60 req/min | 60/min | NBA advanced stats |
| CoinGecko | 30 req/min | 30/min | Already in templates |

---

## Already documented

These providers already have working connector code in
`platform/data-connector-templates.md` — use that file for
copy-paste integration:

- `football-data.org` — Template 1 (football lineups)
- `KAYEN` — Template 2 (fan token market data)
- `CoinGecko` — Template 3 (macro state / CHZ price)

---

*SportMind v3.35 · MIT License · sportmind.dev*
*See also: platform/data-connector-templates.md · platform/realtime-integration-patterns.md*
*platform/sequential-thinking-integration.md · platform/fetch-mcp-disciplinary.md*
