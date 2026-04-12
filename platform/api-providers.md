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

**Cricket — recommended stack**
```
CricketData.org:
  URL:      https://cricketdata.org
  Cost:     Free tier: 100 req/day | Paid: from $10/month
  Coverage: International + IPL + BBL + The Hundred + all major leagues
  Key endpoints:
    /matches?apikey={key}&offset=0           → upcoming matches
    /currentMatches?apikey={key}             → live matches
    /series?apikey={key}                     → active series
    /players?apikey={key}&search={name}      → player search
  SportMind fit: Toss data, pitch conditions, playing XI, squad changes
                 Maps to: athlete/cricket/athlete-intel-cricket.md

Cricbuzz (via RapidAPI — community wrapper):
  URL:      https://rapidapi.com/cricketapilive/api/cricbuzz-cricket
  Free:     100 requests/day
  Best for: Live scores, squad news, match commentary (detect DLS triggers)
  Key endpoints (RapidAPI path):
    /mcenter/v1/{matchId}/comm              → live commentary
    /series/v1/{seriesId}/squads/{teamId}   → confirmed squad
  SportMind fit: T-0 squad confirmation, DLS weather interruption signal

Sportmonks Cricket:
  URL:      https://sportmonks.com/cricket-api
  Paid:     from €29/month
  Best for: Batter vs bowler H2H stats (the most valuable signal in cricket)
  Key endpoint:
    /cricket/fixtures/{fixtureId}/scorecard → full scorecard with batter/bowler splits
  SportMind fit: athlete/cricket/athlete-intel-cricket.md get_batter_vs_bowler

ESPNcricinfo Statsguru:
  URL:      https://stats.espncricinfo.com/ci/engine/stats/index.html
  Cost:     Free (manual query only — no API)
  Best for: Deep historical batter vs bowler records
  Use with: Fetch MCP for specific player matchup lookups
  
Key signals for SportMind cricket agents:
  1. Toss result:             CricketData.org /currentMatches → toss winner
  2. Playing XI:              Cricbuzz squad endpoint → confirmed T-0
  3. Dew factor:              Open-Meteo humidity at venue (see Weather below)
  4. Batter vs bowler H2H:    Sportmonks or manual Statsguru lookup
  5. Pitch report:            Commentary via Cricbuzz → detect "spin-friendly" cues
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

**MMA / UFC — recommended stack**
```
UFC Stats (ufcstats.com):
  URL:      http://ufcstats.com/statistics/events/completed
  Cost:     Free (scrape or use wrapper)
  Coverage: All UFC fight history, fighter stats, results
  Endpoints (via RapidAPI wrappers):
    Fighter profile: /fighter-details/{fighter_id}
    Event results:   /event-details/{event_id}
    Fight stats:     /fight-details/{fight_id}
  SportMind fit: Strike rate, takedown accuracy, finishing tendency
                 → maps to core/injury-intelligence/injury-intel-mma.md
                 → fight camp signals, weight cut history

Best RapidAPI wrapper (stable as of 2026):
  https://rapidapi.com/api-sports/api/api-mma
  Free tier: 100 requests/day
  Paid:      from $9.99/month

Tapology (tapology.com):
  URL:      https://www.tapology.com (scrape or unofficial API)
  Best for: Fighter records, opponent quality, betting lines history
  RapidAPI: https://rapidapi.com/tapology/api/mma-fighters
  SportMind fit: Opponent quality scoring for style matchup analysis
                 → historical-intelligence-framework.md (MMA H2H section)

Sherdog (sherdog.com):
  URL:      https://www.sherdog.com
  Best for: Deep fight history, amateur records, ranking history
  No official API — use Fetch MCP for specific fighter pages
  SportMind fit: Career stage and decline modelling (injury-intel-mma.md)

Key signals for SportMind MMA agents:
  1. Weight cut history:      Tapology fight page → pre-fight weight
  2. Finishing rate:           UFC Stats → method of victory breakdown
  3. Fight camp duration:      Sherdog → fight announcement date vs event
  4. Style classification:     Manual from UFC Stats grappling/striking ratio
```

**Basketball — NBA recommended stack**
```
Official NBA injury report (Tier 1 — act on immediately):
  URL:      https://www.nba.com/players/injuries
  Cost:     Free — no API key required
  Format:   Web page updated daily (Wednesday/Thursday for weekend games)
  Designations: OUT (O), DOUBTFUL (D), QUESTIONABLE (Q), PROBABLE (P), GTD
  Fetch:    Use Fetch MCP to parse injury report page at T-24h and T-2h
  SportMind fit: Maps directly to core/pre-match-squad-intelligence.md
                 NBA Q/D/O/GTD decoder section

balldontlie API:
  URL:      https://www.balldontlie.io
  Free:     60 req/min
  Coverage: Games, players, stats, standings, box scores
  Key endpoints:
    GET /v1/games?dates[]={YYYY-MM-DD}           → today's games
    GET /v1/players?search={name}                → player lookup
    GET /v1/stats?game_ids[]={id}&player_ids[]={id} → player stats
  SportMind fit: On/off splits for star player → net_rating → LQI input
                 (core/lineup-quality-index.md NBA section)

NBA Stats API (unofficial, high detail):
  URL:      https://stats.nba.com/stats/
  Cost:     Free — no API key (unofficial access, respect rate limits)
  Key endpoints:
    /leaguegamefinder?LeagueID=00    → recent games
    /boxscoreadvancedv3?GameID={id}  → advanced box score
    /playerdashboardbygeneralsplits  → player splits (home/away, clutch)
  Headers required:
    Referer: https://www.nba.com
    User-Agent: Mozilla/5.0 ...
  SportMind fit: Net rating for LQI, clutch performance, rest days

Key signals for SportMind NBA agents:
  1. Injury designations:     nba.com/players/injuries → Q/D/O/GTD
  2. Lineup:                  balldontlie /v1/games → starters (post tip-off)
  3. Net rating:              NBA Stats /playerdashboard → for LQI calculation
  4. Back-to-back flag:       balldontlie /v1/games → check previous day game
  5. Load management:         Official injury report "REST" designation
```

**Ice Hockey — NHL morning skate stack**
```
NHL official data:
  URL:      https://api-web.nhle.com/v1/ (unofficial — no key required)
  Cost:     Free
  Key endpoints:
    /schedule/now                             → today's games
    /club-schedule/{team}/week/now            → team schedule
    /roster/{team}/current                    → current roster
    /player/{playerId}/landing                → player profile + status
  SportMind fit: Starting goaltender confirmation from morning skate
                 (athlete/nhl/athlete-intel-nhl.md morning skate section)

NHL injury reserve (official):
  URL:      https://www.nhl.com/info/ir-list (IR/LTIR designations)
  Fetch:    Use Fetch MCP to parse at T-24h
  Designations:
    IR   = Injured Reserve (minimum 7 days, retroactive allowed)
    LTIR = Long-Term IR (minimum 24 days / 10 games)
    DTD  = Day-to-Day (not on IR — monitor morning skate)
  SportMind fit: core/pre-match-squad-intelligence.md NHL section

Daily Faceoff (projected lineups):
  URL:      https://www.dailyfaceoff.com/projected-lineups
  Cost:     Free
  Best for: Morning skate line combinations and defensive pairs
  No API — use Fetch MCP at T-3h to T-1h on game day
  SportMind fit: GK confirmation before morning skate is official

Natural Stat Trick (advanced stats):
  URL:      https://www.naturalstattrick.com
  Cost:     Free
  Best for: GSAx (Goals Saved Above Expected), 5-on-5 shot quality
  No API — use Fetch MCP for specific game/player pages
  SportMind fit: GSAx feeds directly into LQI goaltender rating

Key signals for SportMind NHL agents:
  1. Morning skate GK:        Daily Faceoff at T-3h → primary lineup signal
  2. IR/LTIR status:          nhl.com IR list at T-24h
  3. Goaltender GSAx:         Natural Stat Trick → LQI GK component
  4. Back-to-back:            NHL API /schedule → check previous night game
  5. Power play unit:         Daily Faceoff lineup page → PP1 specialist
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

## Odds and prediction markets

```
The Odds API (the-odds-api.com):
  URL:      https://the-odds-api.com
  Free:     500 requests/month
  Paid:     from $0/month (usage-based: $0.002 per request above free tier)
  Coverage: 40+ sports, 70+ bookmakers, live and upcoming markets
  RapidAPI: https://rapidapi.com/theoddsapi/api/odds-by-api-football
  
  Key endpoints:
    GET /v4/sports                              → list active sports
    GET /v4/sports/{sport}/odds?regions=uk,eu   → pre-match odds for sport
    GET /v4/sports/{sport}/scores               → live scores
    GET /v4/sports/{sport}/events/{eventId}/odds → specific event odds
  
  Headers:
    apiKey={key} (query param, not header)
  
  Sample sports keys:
    soccer_epl         → Premier League
    basketball_nba     → NBA
    mma_mixed_martial_arts → MMA
    cricket_ipl        → IPL
    icehockey_nhl      → NHL
  
  Response structure:
    {id, sport_key, commence_time, home_team, away_team,
     bookmakers: [{key, title, markets: [{key, outcomes: [{name, price}]}]}]}
  
  SportMind fit:
    → core/prediction-market-intelligence.md: divergence detection
    → Convert decimal odds to probability: 1 / decimal_odds
    → Compare SportMind direction vs market consensus
    → Flag when SportMind SMS > 70 but market odds contradict signal

Implied probability from odds:
  Decimal 1.85 HOME → 1/1.85 = 0.541 = 54.1% implied probability
  Decimal 3.40 AWAY → 1/3.40 = 0.294 = 29.4% implied probability
  Overround = sum of all implied probs (usually 1.05–1.10 for typical books)
  Remove overround: prob / sum_of_all_probs × 100

When to use in SportMind agent chain:
  CONFIRMING signal:  SportMind SMS ≥ 70, market odds agree → increase conviction
  DIVERGENCE signal:  SportMind SMS ≥ 70, market odds strongly disagree →
                      highest-value signal (SportMind may have structural edge)
  LOW LIQUIDITY:      Market depth < $10k → ignore as signal input
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
| CricketData.org | 100 req/day | 10/min | Cricket squad + fixtures |
| API-MMA (RapidAPI) | 100 req/day | 10/min | UFC fight history + stats |
| NHL API (unofficial) | Unlimited | Fair use | NHL rosters + schedule |
| nba.com (unofficial) | Unlimited | Low | NBA advanced box scores |
| The Odds API | 500 req/month | 10/min | Multi-sport odds, divergence |
| Daily Faceoff (Fetch) | Unlimited | Manual | NHL morning skate lineups |
| Natural Stat Trick (Fetch) | Unlimited | Manual | GSAx for LQI GK rating |

---

## Already documented

These providers already have working connector code in
`platform/data-connector-templates.md` — use that file for
copy-paste integration:

- `football-data.org` — Template 1 (football lineups)
- `KAYEN` — Template 2 (fan token market data)
- `CoinGecko` — Template 3 (macro state / CHZ price)

---

*SportMind v3.52 · MIT License · sportmind.dev*
*See also: platform/data-connector-templates.md · platform/realtime-integration-patterns.md*
*platform/sequential-thinking-integration.md · platform/fetch-mcp-disciplinary.md*
