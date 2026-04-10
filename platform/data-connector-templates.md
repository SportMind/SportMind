# Data Connector Templates

**Copy-paste connection code for the three data sources SportMind agents
need most. Each template is production-ready, handles errors correctly,
and slots directly into the realtime integration patterns.**

SportMind is an intelligence framework — it does not bundle live data.
These templates give you the connection layer. Paste them into your agent
and replace the API keys/endpoints with your own credentials.

---

## Template 1 — Football lineup data (football-data.org)

The most important football signal: who is actually playing. Confirmed
30-120 minutes before kick-off via the official team sheet.

```python
# connectors/football_lineups.py
"""
Football lineup connector using football-data.org API.
Free tier: 10 requests/minute; covers top 12 European leagues.
Paid tier: all leagues, higher rate limits.
API key: https://www.football-data.org/client/register
"""
import asyncio
import aiohttp
from datetime import datetime, timezone
from typing import Optional

FOOTBALL_DATA_BASE = "https://api.football-data.org/v4"

class FootballLineupConnector:
    """
    Fetches confirmed lineups and match status from football-data.org.
    Integrates with SportMind's lineup_unconfirmed flag.
    """

    def __init__(self, api_key: str):
        self.api_key  = api_key
        self.headers  = {
            "X-Auth-Token": api_key,
            "Content-Type": "application/json"
        }
        self._session: Optional[aiohttp.ClientSession] = None

    async def get_session(self) -> aiohttp.ClientSession:
        if not self._session:
            self._session = aiohttp.ClientSession(headers=self.headers)
        return self._session

    async def get_upcoming_matches(self, competition_id: str,
                                    days_ahead: int = 7) -> list[dict]:
        """
        Get upcoming matches for a competition.
        
        Competition IDs:
          PL  = Premier League
          PD  = La Liga (Primera Division)
          BL1 = Bundesliga
          SA  = Serie A
          FL1 = Ligue 1
          CL  = UEFA Champions League
          EL  = UEFA Europa League
        """
        session = await self.get_session()
        url = f"{FOOTBALL_DATA_BASE}/competitions/{competition_id}/matches"
        params = {
            "status": "SCHEDULED",
            "dateFrom": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        }
        
        async with session.get(url, params=params) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data.get("matches", [])
            elif resp.status == 429:
                # Rate limited — wait and retry
                await asyncio.sleep(60)
                return await self.get_upcoming_matches(competition_id, days_ahead)
            else:
                return []

    async def get_lineup(self, match_id: int) -> dict:
        """
        Get confirmed lineup for a specific match.
        
        Returns SportMind-compatible lineup dict:
        {
          "lineup_confirmed": bool,
          "home_team": {
            "name": str,
            "formation": str,
            "starting_xi": [{"name": str, "position": str}, ...]
          },
          "away_team": {...},
          "status": "SCHEDULED" | "TIMED" | "IN_PLAY" | "FINISHED"
        }
        """
        session = await self.get_session()
        url = f"{FOOTBALL_DATA_BASE}/matches/{match_id}"
        
        async with session.get(url) as resp:
            if resp.status != 200:
                return {"lineup_confirmed": False, "error": resp.status}
            
            data = await resp.json()
            
            # lineup_confirmed when lineups have been posted
            lineups = data.get("lineups", [])
            confirmed = len(lineups) >= 2 and all(
                len(team.get("startingXI", [])) >= 11 for team in lineups
            )
            
            result = {
                "lineup_confirmed": confirmed,
                "status": data.get("status"),
                "utc_date": data.get("utcDate"),
                "match_id": match_id,
            }
            
            if confirmed:
                result["home_team"] = {
                    "name": data["homeTeam"]["name"],
                    "formation": lineups[0].get("formation", "unknown"),
                    "starting_xi": [
                        {"name": p["name"], "position": p.get("position", "")}
                        for p in lineups[0].get("startingXI", [])
                    ]
                }
                result["away_team"] = {
                    "name": data["awayTeam"]["name"],
                    "formation": lineups[1].get("formation", "unknown"),
                    "starting_xi": [
                        {"name": p["name"], "position": p.get("position", "")}
                        for p in lineups[1].get("startingXI", [])
                    ]
                }
            
            return result

    async def check_lineup_for_sportmind(self, match_id: int,
                                          key_players: list[str]) -> dict:
        """
        Returns SportMind-ready lineup signal:
        - lineup_unconfirmed flag
        - key_players_available dict
        - any injuries/absences detected
        """
        lineup = await self.get_lineup(match_id)
        
        if not lineup.get("lineup_confirmed"):
            return {
                "lineup_unconfirmed": True,
                "message": f"Lineup not yet confirmed for match {match_id}",
                "status": lineup.get("status", "UNKNOWN")
            }
        
        # Check key player availability
        all_players = []
        for team in ["home_team", "away_team"]:
            if team in lineup:
                all_players.extend(
                    [p["name"].lower() for p in lineup[team].get("starting_xi", [])]
                )
        
        key_player_status = {}
        for player in key_players:
            is_starting = any(player.lower() in p for p in all_players)
            key_player_status[player] = "STARTING" if is_starting else "ABSENT_OR_BENCH"
        
        return {
            "lineup_unconfirmed": False,
            "lineup": lineup,
            "key_player_status": key_player_status,
            "absences_detected": [p for p, s in key_player_status.items()
                                   if s == "ABSENT_OR_BENCH"]
        }

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ──────────────────────────────────────────────────────────────

async def example_usage():
    """
    How to use this connector with a SportMind agent:
    
    1. Get upcoming UCL matches
    2. For each match in next 48h, check lineup status
    3. Set lineup_unconfirmed flag appropriately
    4. If key player absent → trigger RELOAD protocol
    """
    connector = FootballLineupConnector(api_key="YOUR_FOOTBALL_DATA_API_KEY")
    
    # Get upcoming Champions League matches
    matches = await connector.get_upcoming_matches("CL")
    print(f"Found {len(matches)} upcoming UCL matches")
    
    for match in matches[:3]:  # Check first 3
        match_id = match["id"]
        # Define key players to track
        key_players = ["Mbappé", "Haaland", "Vinicius Jr"]
        
        lineup_signal = await connector.check_lineup_for_sportmind(
            match_id, key_players
        )
        
        if lineup_signal["lineup_unconfirmed"]:
            print(f"Match {match_id}: lineup not yet confirmed")
        else:
            absences = lineup_signal.get("absences_detected", [])
            if absences:
                print(f"Match {match_id}: ALERT — key players absent: {absences}")
                # → Trigger SportMind RELOAD protocol
            else:
                print(f"Match {match_id}: all key players starting — clear for signal")
    
    await connector.close()
```

---

## Template 2 — Fan token market data (KAYEN / Chiliz Chain)

TVL, price, liquidity depth — the data SportMind's DeFi layer reasons about.

**2026 update — omni-chain awareness required:**
From Q1 2026, fan tokens are available on multiple blockchains via LayerZero bridge
(Chiliz 2030 Manifesto). KAYEN remains the primary Chiliz Chain venue, but tokens
may also trade on Ethereum, Base, or other chains simultaneously. For omni-chain
tokens, aggregate TVL across all venues before applying SportMind's liquidity tier.

Check for omni-chain status: `GET /tokens/{address}` → look for `omni_chain: true`
and `cross_chain_tvl` field in the KAYEN API response.

**PEPPER governance token:**
PEPPER is KAYEN's community governance token. PEPPER holders govern KAYEN protocol
decisions including fee structures. Monitor PEPPER governance votes for changes that
could affect fan token liquidity mechanics on Chiliz Chain.

**Gamified tokenomics check:**
From Q2 2026, some tokens have performance-linked supply mechanics (Win → burn,
Loss → mint). Check for `gamified: true` in the KAYEN API response before applying
standard liquidity analysis. See `fan-token/gamified-tokenomics-intelligence/` for the
full signal model.

```python
# connectors/fan_token_market.py
"""
Fan token market data connector for KAYEN (Chiliz Chain DEX).
No API key required — KAYEN has a public API.
KAYEN docs: https://docs.kayen.finance/api

2026+ notes:
- Check omni_chain field: tokens may trade on multiple chains
- Check gamified field: some tokens have performance-linked supply
- Check cross_chain_tvl field: aggregate for accurate liquidity tier
"""
import aiohttp
from typing import Optional

KAYEN_API = "https://api.kayen.finance/v1"

# Token contract addresses on Chiliz Chain
# Find these at: https://explorer.chiliz.com/tokens
KNOWN_TOKENS = {
    "PSG":  "0x...",  # Replace with actual contract address
    "BAR":  "0x...",  # Replace with actual contract address
    "CITY": "0x...",  # Replace with actual contract address
    "JUV":  "0x...",  # Replace with actual contract address
    "ATM":  "0x...",  # Replace with actual contract address
}

class FanTokenMarketConnector:
    """
    Fetches fan token market data from KAYEN.
    Provides TVL tier, spread, and HAS proxy signals.
    """

    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def get_session(self) -> aiohttp.ClientSession:
        if not self._session:
            self._session = aiohttp.ClientSession()
        return self._session

    async def get_token_data(self, token_address: str) -> dict:
        """
        Fetch current market data for a fan token.
        Returns SportMind-compatible market signal dict.
        """
        session = await self.get_session()

        try:
            async with session.get(
                f"{KAYEN_API}/tokens/{token_address}"
            ) as resp:
                if resp.status != 200:
                    return {"error": f"KAYEN API returned {resp.status}"}
                data = await resp.json()
        except Exception as e:
            return {"error": str(e)}

        # Map to SportMind liquidity tier
        tvl_usd = data.get("tvl_usd", 0)
        if tvl_usd >= 5_000_000:
            liquidity_tier = "DEEP"
            liquidity_modifier = 1.00
        elif tvl_usd >= 500_000:
            liquidity_tier = "MODERATE"
            liquidity_modifier = 1.00
        elif tvl_usd >= 50_000:
            liquidity_tier = "THIN"
            liquidity_modifier = 0.92
        else:
            liquidity_tier = "MICRO"
            liquidity_modifier = 0.80

        # Spread calculation
        bid = data.get("bid_price", 0)
        ask = data.get("ask_price", 0)
        spread_pct = ((ask - bid) / bid * 100) if bid > 0 else 99.9
        spread_flag = "HIGH_SPREAD" if spread_pct > 2.0 else None

        return {
            "token":             data.get("symbol", "UNKNOWN"),
            "price_usd":         data.get("price_usd", 0),
            "price_chz":         data.get("price_chz", 0),
            "tvl_usd":           tvl_usd,
            "volume_24h_usd":    data.get("volume_24h_usd", 0),
            "price_change_24h":  data.get("price_change_24h_pct", 0),
            "liquidity_tier":    liquidity_tier,
            "liquidity_modifier": liquidity_modifier,
            "spread_pct":        round(spread_pct, 2),
            "flags":             [f for f in [spread_flag,
                                              "liquidity_warning" if tvl_usd < 50_000 else None]
                                  if f is not None],
            # Fan Token Play status — read directly from KAYEN API response
            # gamified: True means this token has active performance-linked supply mechanics
            # path: "PATH_1" | "PATH_2" — mechansim in use (check fantokens.com if not present)
            "gamified":          data.get("gamified", False),
            "fan_token_play_path": data.get("fan_token_play_path", None),
            "gamified_note": (
                "Token has confirmed Fan Token Play. Load fan-token/gamified-tokenomics-intelligence/. "
                "Check FanTokenPlayMonitor at T-48h before each match."
            ) if data.get("gamified") else (
                "Standard supply mechanics. Gamified modifier does not apply."
            ),
            "sportmind_ready":   True
        }

    async def get_portfolio_snapshot(self, tokens: list[str]) -> dict:
        """
        Fetch market data for a portfolio of tokens.
        Returns dict keyed by token symbol.
        """
        results = {}
        for symbol in tokens:
            address = KNOWN_TOKENS.get(symbol)
            if not address:
                results[symbol] = {"error": f"No address for {symbol}"}
                continue
            results[symbol] = await self.get_token_data(address)
        return results

    async def check_liquidity_gate(self, token_address: str,
                                    min_tvl_usd: float = 50_000) -> dict:
        """
        SportMind liquidity gate check.
        Returns: proceed=True/False with reason.
        """
        market = await self.get_token_data(token_address)
        if "error" in market:
            return {"proceed": False, "reason": "market_data_unavailable",
                    "liquidity_critical": True}

        tvl = market.get("tvl_usd", 0)
        if tvl < min_tvl_usd:
            return {"proceed": False, "reason": "insufficient_liquidity",
                    "tvl_usd": tvl, "required_usd": min_tvl_usd,
                    "liquidity_critical": True}

        return {"proceed": True, "tvl_usd": tvl,
                "tier": market["liquidity_tier"],
                "modifier": market["liquidity_modifier"]}

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ──────────────────────────────────────────────────────────────

async def example_usage():
    """
    Standard SportMind liquidity check before any signal:
    1. Always check macro first (SportMind API)
    2. THEN check liquidity — if MICRO tier, do not proceed
    3. Apply liquidity_modifier to adjusted_score
    """
    connector = FanTokenMarketConnector()

    # Check liquidity gate before generating signal
    gate = await connector.check_liquidity_gate(
        KNOWN_TOKENS["PSG"], min_tvl_usd=50_000
    )

    if not gate["proceed"]:
        print(f"LIQUIDITY GATE BLOCKED: {gate['reason']}")
        print("SportMind: set liquidity_critical=True, position_size=0%")
        return

    # Get full market data
    market = await connector.get_token_data(KNOWN_TOKENS["PSG"])
    print(f"$PSG liquidity: {market['liquidity_tier']} (${market['tvl_usd']:,.0f} TVL)")
    print(f"Liquidity modifier: {market['liquidity_modifier']}")
    if market["flags"]:
        print(f"Flags: {market['flags']}")

    await connector.close()
```

---

## Template 3 — Macro state (CoinGecko / CHZ price)

The macro check every SportMind agent must run first.

```python
# connectors/macro_state.py
"""
Macro state connector: CHZ price + BTC dominance + crypto market cap.
Used by SportMind to compute the macro_modifier.
CoinGecko free API — no key required (rate limited; paid tier available).
"""
import aiohttp
import json
from datetime import datetime, timezone
from pathlib import Path

COINGECKO_API = "https://api.coingecko.com/api/v3"

class MacroStateConnector:
    """
    Fetches crypto macro state and maps to SportMind macro_modifier.
    Updates macro-state.json for local caching (Tier 3 freshness = 4-8h).
    """

    MACRO_STATE_PATH = Path("platform/macro-state.json")

    async def get_macro_modifier(self) -> dict:
        """
        Compute current macro_modifier from live crypto market data.
        
        SportMind macro phases:
          BULL:         BTC > $60k OR total market cap > $2T → modifier 1.15
          NEUTRAL_HIGH: BTC $40-60k, market growing           → modifier 1.00
          NEUTRAL:      BTC $25-40k, market stable            → modifier 1.00
          BEAR:         BTC $15-25k OR market declining        → modifier 0.75
          EXTREME_BEAR: BTC < $15k OR crypto winter            → modifier 0.50
        """
        async with aiohttp.ClientSession() as session:
            # Fetch BTC + CHZ prices and market caps
            async with session.get(
                f"{COINGECKO_API}/simple/price",
                params={
                    "ids":             "bitcoin,chiliz",
                    "vs_currencies":   "usd",
                    "include_market_cap": "true",
                    "include_24hr_change": "true"
                }
            ) as resp:
                if resp.status != 200:
                    # Return cached state if API unavailable
                    return self._load_cached_state()
                prices = await resp.json()

            # Fetch global market cap
            async with session.get(f"{COINGECKO_API}/global") as resp:
                global_data = (await resp.json()).get("data", {}) if resp.status == 200 else {}

        btc_price    = prices.get("bitcoin", {}).get("usd", 0)
        chz_price    = prices.get("chiliz", {}).get("usd", 0)
        btc_change   = prices.get("bitcoin", {}).get("usd_24h_change", 0)
        total_mcap   = global_data.get("total_market_cap", {}).get("usd", 0)

        # Determine phase
        if btc_price >= 60_000 or total_mcap >= 2_000_000_000_000:
            phase, modifier = "BULL",          1.15
        elif btc_price >= 40_000:
            phase, modifier = "NEUTRAL_HIGH",  1.00
        elif btc_price >= 25_000:
            phase, modifier = "NEUTRAL",       1.00
        elif btc_price >= 15_000:
            phase, modifier = "BEAR",          0.75
        else:
            phase, modifier = "EXTREME_BEAR",  0.50

        # Momentum adjustment
        if btc_change > 5:
            modifier = min(1.20, modifier * 1.05)   # positive momentum
        elif btc_change < -5:
            modifier = max(0.40, modifier * 0.95)   # negative momentum

        state = {
            "macro_state": {
                "generated_at":  datetime.now(timezone.utc).isoformat(),
                "crypto_cycle":  {
                    "phase":           phase,
                    "macro_modifier":  round(modifier, 2),
                    "btc_price_usd":   btc_price,
                    "chz_price_usd":   chz_price,
                    "btc_24h_change":  round(btc_change, 2),
                    "total_mcap_usd":  total_mcap,
                }
            }
        }

        # Cache state
        self.MACRO_STATE_PATH.write_text(json.dumps(state, indent=2))
        return state

    def _load_cached_state(self) -> dict:
        """Return cached macro state if API is unavailable."""
        if self.MACRO_STATE_PATH.exists():
            return json.loads(self.MACRO_STATE_PATH.read_text())
        # Neutral fallback if no cache
        return {
            "macro_state": {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "crypto_cycle": {
                    "phase": "NEUTRAL",
                    "macro_modifier": 1.00,
                    "note": "Cached/fallback — live data unavailable"
                }
            }
        }

    def is_stale(self, max_age_hours: float = 4.0) -> bool:
        """Check if cached macro state needs refreshing (Tier 3 = 4-8h)."""
        if not self.MACRO_STATE_PATH.exists():
            return True
        try:
            state    = json.loads(self.MACRO_STATE_PATH.read_text())
            gen_time = datetime.fromisoformat(
                state["macro_state"]["generated_at"]
            )
            age_hours = (datetime.now(timezone.utc) - gen_time).total_seconds() / 3600
            return age_hours > max_age_hours
        except Exception:
            return True


# ── Complete startup sequence ───────────────────────────────────────────────────

async def sportmind_startup_check() -> dict:
    """
    The standard SportMind agent startup sequence:
    1. Check macro state (RULE 1: always first)
    2. Determine if conditions allow signal generation
    3. Return gate decision

    Call this at agent init and every 4-8h during operation.
    """
    connector = MacroStateConnector()

    # Refresh if stale
    if connector.is_stale(max_age_hours=4.0):
        state = await connector.get_macro_modifier()
    else:
        state = connector._load_cached_state()

    phase    = state["macro_state"]["crypto_cycle"]["phase"]
    modifier = state["macro_state"]["crypto_cycle"]["macro_modifier"]

    # Gate decision
    if modifier < 0.60:
        gate = "ABORT"
        note = f"Extreme bear market ({phase}) — suspend all token signal generation"
    elif modifier < 0.80:
        gate = "PROCEED_CAUTIOUSLY"
        note = f"Bear market ({phase}) — reduce position sizes; elevated uncertainty"
    else:
        gate = "PROCEED"
        note = f"{phase} — standard signal generation"

    return {
        "phase":           phase,
        "macro_modifier":  modifier,
        "gate":            gate,
        "note":            note,
        "btc_price_usd":   state["macro_state"]["crypto_cycle"].get("btc_price_usd", 0),
    }


# ── Usage example ──────────────────────────────────────────────────────────────

async def example_usage():
    """
    Every SportMind agent starts with this.
    If gate is ABORT, do not proceed with any token signals.
    """
    startup = await sportmind_startup_check()
    print(f"Macro: {startup['phase']} (modifier: {startup['macro_modifier']})")
    print(f"Gate: {startup['gate']} — {startup['note']}")

    if startup["gate"] == "ABORT":
        print("Macro override active — all token signals suspended")
        return

    print("Macro check passed — ready to generate signals")
```

---

## Connecting all three templates

```python
# agent_with_connectors.py
"""
A complete SportMind agent using all three data connectors.
This is the template for a production-ready fan token signal agent.
"""
import asyncio
from connectors.macro_state      import sportmind_startup_check
from connectors.fan_token_market import FanTokenMarketConnector, KNOWN_TOKENS
from connectors.football_lineups import FootballLineupConnector

async def generate_full_signal(token: str, match_id: int,
                                key_players: list[str],
                                football_api_key: str) -> dict:
    """
    Complete pre-match signal generation with all three connectors.
    Returns SportMind confidence output schema.
    """
    # STEP 1: Macro check (RULE 1 — always first)
    macro = await sportmind_startup_check()
    if macro["gate"] == "ABORT":
        return {"signal": "ABORT", "reason": "macro_override_active",
                "macro": macro}

    # STEP 2: Liquidity check
    market_connector = FanTokenMarketConnector()
    liquidity = await market_connector.check_liquidity_gate(
        KNOWN_TOKENS.get(token, ""), min_tvl_usd=50_000
    )
    if not liquidity["proceed"]:
        await market_connector.close()
        return {"signal": "WAIT", "reason": "liquidity_critical",
                "liquidity": liquidity}

    market = await market_connector.get_token_data(KNOWN_TOKENS.get(token, ""))
    await market_connector.close()

    # STEP 3: Lineup confirmation
    lineup_connector = FootballLineupConnector(api_key=football_api_key)
    lineup = await lineup_connector.check_lineup_for_sportmind(
        match_id, key_players
    )
    await lineup_connector.close()

    # STEP 4: Build SportMind signal
    # (In production: this is where you call SportMind Skills API
    # or load skill files and run reasoning chain)
    base_score = 62.0  # from SportMind skill analysis
    
    # Apply modifiers from connectors
    adjusted_score = (
        base_score
        * macro["macro_modifier"]
        * market["liquidity_modifier"]
    )

    # Flags from connectors
    flags = {
        "macro_override_active": macro["gate"] == "ABORT",
        "liquidity_critical":    not liquidity["proceed"],
        "lineup_unconfirmed":    lineup.get("lineup_unconfirmed", True),
        "key_player_absent":     bool(lineup.get("absences_detected")),
    }

    return {
        "token":           token,
        "macro":           {"phase": macro["phase"], "modifier": macro["macro_modifier"]},
        "market":          {"tier": market["liquidity_tier"], "tvl": market["tvl_usd"]},
        "lineup":          {"confirmed": not lineup.get("lineup_unconfirmed"),
                            "absences": lineup.get("absences_detected", [])},
        "signal": {
            "adjusted_score":     round(adjusted_score, 1),
            "recommended_action": "ENTER" if adjusted_score >= 65 and not any(flags.values()) else "WAIT",
            "flags":              {k: v for k, v in flags.items() if v},
        }
    }
```

---

## Other data sources

Beyond the three templates above, you may need:

```
CRICKET / T20 DATA:
  ESPN Cricinfo API: https://www.espncricinfo.com/ci/engine/app/index.html
  CricAPI (paid): https://www.cricapi.com/
  SportradarCricket: https://developer.sportradar.com/docs/read/Cricket

NBA / BASKETBALL:
  NBA Stats (free, unofficial): https://github.com/swar/nba_api
  BallDontLie (free): https://www.balldontlie.io/
  Sportradar NBA (paid): https://developer.sportradar.com/docs/read/basketball/NBA_v8

MMA / UFC:
  UFC Stats (free, unofficial): https://github.com/ufc/ufc-data
  MMA Decisions (free): https://mmadecisions.com/
  ESPN MMA API: unofficial; documented in community examples

FORMULA 1:
  Ergast API (free): https://ergast.com/mrd/ — lap times, results, qualifying
  FastF1 (Python): https://github.com/theOehrly/Fast-F1 — telemetry data
  
SOCIAL / SENTIMENT:
  Twitter/X API: https://developer.twitter.com/ — for KOL monitoring
  Reddit API: https://www.reddit.com/dev/api/ — community sentiment
  Google Trends (unofficial): https://github.com/GeneralMills/pytrends

ON-CHAIN (Chiliz):
  Chiliz Chain Explorer: https://explorer.chiliz.com/api
  KAYEN API: https://docs.kayen.finance/api (as in Template 2)
```

---

*MIT License · SportMind · sportmind.dev*
*See `platform/realtime-integration-patterns.md` for the full integration model.*
*See `platform/freshness-strategy.md` for data freshness requirements per tier.*
