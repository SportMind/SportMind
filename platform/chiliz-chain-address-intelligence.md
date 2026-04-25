# Chiliz Chain Address Intelligence — SportMind

**On-chain wallet analysis for fan token signals. Every entity identified,
every holding tracked, every movement interpreted through SportMind's
commercial intelligence framework.**

Address intelligence transforms the Chiliz Chain from a transparent ledger
into a structured intelligence signal. Who holds a token, how concentrated
the supply is, whether smart wallets are accumulating or distributing, and
how holder composition responds to disciplinary or sporting events — these
are signals unique to the tokenised sports economy that no off-chain data
source can replicate.

---

## Why address intelligence changes fan token analysis

```
WITHOUT ADDRESS INTELLIGENCE:
  PSG token at $0.82 → "market cap $16.2M → Tier 1 signal"
  
WITH ADDRESS INTELLIGENCE:
  PSG token at $0.82
  → Top 10 wallets hold 61% of supply (concentration risk HIGH)
  → 3 wallets have accumulated 2.1% of supply in past 48h (smart money signal)
  → Unique holder count up 4.2% this week (organic growth signal)
  → 847 new wallets created in past 7 days (acquisition event — check KOL activity)
  → Large wallet (0.8% supply) exited yesterday (distribution warning)
  
  SAME PRICE. COMPLETELY DIFFERENT SIGNAL QUALITY.
```

---

## Data sources — Chiliz Chain

All data is publicly available on-chain. No API key required for basic queries.

### 1. Chiliscan API (Etherscan-compatible)

```
Base URL: https://chiliscan.com
API docs: https://chiliscan.com/documentation/api/etherscan-like/accounts
Chain ID: 88888

Key endpoints:

Token holder list:
  GET https://chiliscan.com/api?module=token&action=tokenholderlist
      &contractaddress={token_address}
      &page=1&offset=100
      &apikey={optional}

Token info:
  GET https://chiliscan.com/api?module=token&action=tokeninfo
      &contractaddress={token_address}

Address token balance:
  GET https://chiliscan.com/api?module=account&action=tokenbalance
      &contractaddress={token_address}
      &address={wallet_address}

Token transfer events (ERC-20):
  GET https://chiliscan.com/api?module=account&action=tokentx
      &contractaddress={token_address}
      &address={wallet_address}
      &startblock=0&endblock=99999999
      &sort=desc

Transaction list for address:
  GET https://chiliscan.com/api?module=account&action=txlist
      &address={wallet_address}
      &startblock=0&endblock=99999999
      &sort=desc
```

### 2. Chiliz Chain RPC (direct node queries)

```
RPC endpoint (via Ankr, no key required):
  https://rpc.ankr.com/chiliz
  Chain ID: 88888

Use for:
  → Real-time block data
  → Direct contract calls (ERC-20 totalSupply, balanceOf)
  → Transaction receipt verification

Example — get token total supply:
  method: eth_call
  to: {token_contract_address}
  data: 0x18160ddd  (totalSupply() function selector)
```

### 3. Chiliz Graph (subgraph queries)

```
Endpoint: https://graph.chiliz.com/subgraphs/name/chiliz/exchange

Holder count query:
{
  token(id: "{token_address_lowercase}") {
    holderCount
    totalSupply
    tradeVolume
    tradeVolumeUSD
    txCount
  }
}

Recent swaps:
{
  swaps(
    first: 50,
    where: { token0: "{token_address}" }
    orderBy: timestamp, orderDirection: desc
  ) {
    timestamp
    amount0In
    amount0Out
    sender
    to
  }
}
```

---

## Address intelligence framework

### Signal 1 — Holder concentration

```
METRIC: Supply concentration ratio
CALCULATION: % of circulating supply held by top N wallets

Concentration tiers:
  TOP 10 wallets hold:
    < 30%:  LOW concentration — distributed, healthy
    30-50%: MODERATE — normal for fan tokens
    50-70%: HIGH — whale-dominated, volatility risk
    > 70%:  EXTREME — critical concentration, single wallet can move market

  AGENT RULE:
    EXTREME concentration → apply liquidity_warning flag regardless of TVL
    HIGH concentration → note in signal output; reduce position sizing recommendation
    LOW concentration → positive structural signal; supports ENTER confidence

WHAT IT DETECTS:
  → Whether a single entity could crash price by exiting
  → Whether "market cap" is a meaningful metric (it is not if 3 wallets hold 70%)
  → Long-term token health trajectory
```

---

### Signal 2 — Smart wallet tracking

```
DEFINITION:
  A "smart wallet" is one that has historically entered positions before
  positive price events and exited before negative events.
  Identification: retrospective analysis of wallet transaction timing
  vs subsequent price movements over 6+ months of data.

HOW TO IDENTIFY:
  Step 1: Get top-100 holder list for a token
  Step 2: For each holder, fetch transaction history
  Step 3: Map entry/exit dates against price history
  Step 4: Score wallet: entries within T-72h of +5%+ move = smart signal

SMART WALLET SIGNALS:
  Accumulation (smart wallet buying):
    T-72h to T-48h before event: early smart money positioning
    T-48h to T-24h:              institutional-equivalent entry window
    T-24h to T-2h:               final confirmation window
    
  Distribution (smart wallet selling):
    Any window pre-event: strong warning signal
    Multiple smart wallets selling simultaneously: WAIT or reduce position

MODIFIER:
  Smart wallet accumulation (1+ wallets, >0.3% supply each):
    Modifier: ×1.08 on commercial signal
    
  Smart wallet distribution (1+ wallets, >0.3% supply each):
    Modifier: ×0.88 on commercial signal
    
  Smart wallet consensus (3+ wallets same direction):
    Modifier: ×1.15 (accumulation) or ×0.80 (distribution)
    
  RULE: Never apply smart wallet modifier without confirming signal
        direction from sportmind_pre_match first. Smart wallet signal
        is a modifier on sporting signal — not a replacement for it.
```

---

### Signal 3 — Unique holder count trend

```
METRIC: 7-day and 30-day unique holder count change

Thresholds:
  +5%+ in 7 days:   strong organic growth — positive signal
  +2-5% in 7 days:  moderate growth — positive
  -1% to +2%:       stable — neutral
  -2% to -5%:       mild decline — flag
  -5%+ in 7 days:   significant decline — WAIT signal

WHAT DRIVES HOLDER COUNT CHANGES:
  Upward:
    → KOL content reaching new audiences (check social layer)
    → Governance event attracting new participants
    → CEX listing or exchange promotion
    → Airdrop or fan challenge reward distribution
    → Positive match outcome driving media coverage

  Downward:
    → Disciplinary event (DSM_SEVERE triggers measurable exit)
    → Post-governance event decay (participants sold after voting)
    → Token utility lapse (Phase 4-5 lifecycle)
    → Macro bear market (CHZ price decline)

CROSS-REFERENCE RULE:
  Holder count declining + DSM_SEVERE active = disciplinary cascade confirmed
  Holder count rising + no obvious catalyst = investigate KOL or media driver
  Holder count rising + sportmind_pre_match shows high FTIS = signal alignment

HOW TO MEASURE:
  Snapshot holder count daily using chiliscan tokenholderlist API
  Store in Memory MCP (see platform/memory-integration.md)
  Calculate 7-day and 30-day delta
```

---

### Signal 4 — Transfer volume velocity

```
METRIC: 24h transfer count and volume relative to 30-day baseline

Velocity calculation:
  baseline = average daily transfer count (30-day rolling)
  velocity_ratio = today_transfers / baseline

Velocity signal tiers:
  > 3.0×:  SPIKE — investigate immediately (match day? KOL event? news?)
  2.0-3.0×: ELEVATED — moderate event signal
  1.3-2.0×: ACTIVE — above normal activity
  0.7-1.3×: NORMAL — baseline activity
  < 0.7×:  QUIET — below normal (off-season? utility lapse?)

SPIKE CLASSIFICATION:
  SPIKE + upcoming high-FTIS match = pre-match positioning
  SPIKE + no match context = investigate social/news layer
  SPIKE + DSM_SEVERE active = disciplinary reaction — measure holder exit rate
  SPIKE post-win + LP additions = sustained positive signal
  SPIKE post-loss + LP removals = sustained negative signal

MONITORING WINDOW:
  Check transfer velocity:
    T-72h: establish baseline reading
    T-48h: first directional signal
    T-24h: confirmation window
    T-2h:  final velocity reading before signal generation
```

---

### Signal 5 — New wallet acquisition rate

```
METRIC: New wallets holding a token for the first time (7-day window)

Measurement:
  New holder = wallet with zero prior transactions for this token
  Source: tokentx API — filter for first-ever transaction per address

Acquisition rate benchmarks:
  > 500 new wallets/week: HIGH acquisition (major event or campaign)
  100-500/week:           MODERATE acquisition (normal for active token)
  < 100/week:             LOW acquisition (mature or declining token)
  Near zero:              Token entering Phase 5/6 lifecycle

ACQUISITION DRIVER IDENTIFICATION:
  High acquisition + UCL match = organic sporting driver
  High acquisition + KOL content = social driver (check decay rate)
  High acquisition + CEX promotion = exchange driver (may decay faster)
  High acquisition + governance vote = participation drive
  
COMMERCIAL SIGNIFICANCE:
  New wallets = potential long-term holders = commercial durability signal
  KOL-driven new wallets decay faster than match-driven new wallets
  Acquisition rate is a leading indicator for future HAS trajectory
```

---

### Signal 6 — Disciplinary event impact measurement

```
PURPOSE: Empirically measure how disciplinary events affect on-chain holder behaviour.
         This calibrates SportMind's DSM framework with real data over time.

MEASUREMENT PROTOCOL:

  T=0 (event disclosed):
    Record: holder count, transfer velocity, smart wallet positions, concentration

  T+24h:
    Record: same metrics
    Calculate: holder_exit_rate = (T0_holders - T24_holders) / T0_holders

  T+72h:
    Record: same metrics
    Assess: is exit accelerating or stabilising?

  T+verdict:
    Record: same metrics
    Compare: verdict severity vs actual holder response

EXPECTED RESPONSES BY DSM TIER (calibration benchmarks):
  DSM_MINIMAL:     holder_exit_rate < 0.5% (noise level)
  DSM_MODERATE:    holder_exit_rate 1-4% in 72h
  DSM_SEVERE:      holder_exit_rate 4-12% in 72h
  DSM_CATASTROPHIC:holder_exit_rate 12%+ in 72h; smart wallet consensus distribution

CALIBRATION USE:
  Record actual exit rates → compare to DSM modifier values
  If actual exits consistently higher than DSM predicts: update DSM_SEVERE modifier
  Submit as calibration record to community/calibration-data/
  Tag: dsm_calibration
```

---

## Data connector — chiliscan API

```python
# platform/connectors/chiliz_address_intelligence.py
"""
Chiliz Chain address intelligence connector.
Uses chiliscan Etherscan-compatible API.
No API key required for basic queries (rate limit: ~5 req/sec).
Optional API key for higher limits: https://chiliscan.com/register

pip install aiohttp
"""
import aiohttp
import asyncio
from datetime import datetime, timezone
from typing import Optional

CHILISCAN_BASE = "https://chiliscan.com/api"

class ChilizAddressIntelligence:
    """
    Fetches and interprets on-chain data for fan token address intelligence.
    All token contract addresses are in the SportMind fan token registry
    (scripts/sportmind_mcp.py → FAN_TOKEN_REGISTRY).
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or ""
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get(self, params: dict) -> dict:
        if not self._session:
            self._session = aiohttp.ClientSession()
        if self.api_key:
            params["apikey"] = self.api_key
        try:
            async with self._session.get(
                CHILISCAN_BASE, params=params, timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data if data.get("status") == "1" else {}
                return {}
        except Exception:
            return {}

    async def get_holder_list(self, contract_address: str,
                               page: int = 1, limit: int = 100) -> list:
        """Top N holders by balance. Returns list of {address, value} dicts."""
        data = await self._get({
            "module":          "token",
            "action":          "tokenholderlist",
            "contractaddress": contract_address,
            "page":            page,
            "offset":          limit,
        })
        return data.get("result", [])

    async def get_token_info(self, contract_address: str) -> dict:
        """Token metadata: name, symbol, total supply, holder count."""
        data = await self._get({
            "module":          "token",
            "action":          "tokeninfo",
            "contractaddress": contract_address,
        })
        results = data.get("result", [])
        return results[0] if results else {}

    async def get_token_transfers(self, contract_address: str,
                                   address: Optional[str] = None,
                                   limit: int = 100) -> list:
        """Recent ERC-20 transfers for a token, optionally filtered by address."""
        params = {
            "module":          "account",
            "action":          "tokentx",
            "contractaddress": contract_address,
            "startblock":      "0",
            "endblock":        "99999999",
            "sort":            "desc",
            "offset":          limit,
            "page":            "1",
        }
        if address:
            params["address"] = address
        data = await self._get(params)
        return data.get("result", [])

    async def get_concentration_signal(self, contract_address: str,
                                        total_supply: int) -> dict:
        """
        Calculate supply concentration from top-100 holders.
        Returns concentration tier and SportMind modifier.
        """
        holders = await self.get_holder_list(contract_address, limit=100)
        if not holders:
            return {"error": "No holder data available"}

        top_10_balance = sum(int(h["value"]) for h in holders[:10])
        top_50_balance = sum(int(h["value"]) for h in holders[:50])

        top_10_pct = (top_10_balance / total_supply * 100) if total_supply else 0
        top_50_pct = (top_50_balance / total_supply * 100) if total_supply else 0

        if top_10_pct > 70:
            tier, modifier = "EXTREME", 0.80
        elif top_10_pct > 50:
            tier, modifier = "HIGH", 0.90
        elif top_10_pct > 30:
            tier, modifier = "MODERATE", 1.00
        else:
            tier, modifier = "LOW", 1.05

        return {
            "top_10_holders_pct":  round(top_10_pct, 2),
            "top_50_holders_pct":  round(top_50_pct, 2),
            "concentration_tier":  tier,
            "signal_modifier":     modifier,
            "holder_count_sample": len(holders),
            "note": f"Top 10 wallets hold {top_10_pct:.1f}% of supply",
        }

    async def get_transfer_velocity(self, contract_address: str) -> dict:
        """
        Recent transfer count as signal of activity level.
        Returns velocity tier relative to a baseline estimate.
        """
        transfers = await self.get_token_transfers(contract_address, limit=200)
        if not transfers:
            return {"error": "No transfer data available"}

        now = datetime.now(timezone.utc).timestamp()
        day_ago = now - 86400
        week_ago = now - 604800

        last_24h = [t for t in transfers if int(t.get("timeStamp", 0)) > day_ago]
        last_7d  = [t for t in transfers if int(t.get("timeStamp", 0)) > week_ago]

        daily_avg = len(last_7d) / 7 if last_7d else 0
        velocity_ratio = (len(last_24h) / daily_avg) if daily_avg > 0 else 1.0

        if velocity_ratio > 3.0:
            tier = "SPIKE"
        elif velocity_ratio > 2.0:
            tier = "ELEVATED"
        elif velocity_ratio > 1.3:
            tier = "ACTIVE"
        elif velocity_ratio > 0.7:
            tier = "NORMAL"
        else:
            tier = "QUIET"

        return {
            "transfers_24h":      len(last_24h),
            "transfers_7d":       len(last_7d),
            "daily_average_7d":   round(daily_avg, 1),
            "velocity_ratio":     round(velocity_ratio, 2),
            "velocity_tier":      tier,
            "unique_senders_24h": len(set(t.get("from", "") for t in last_24h)),
        }

    async def get_address_intelligence_snapshot(self,
                                                  contract_address: str,
                                                  ticker: str) -> dict:
        """
        Full address intelligence snapshot for a fan token.
        Combines token info, concentration, and velocity signals.
        """
        token_info   = await self.get_token_info(contract_address)
        total_supply = int(token_info.get("totalSupply", 0))

        concentration, velocity = await asyncio.gather(
            self.get_concentration_signal(contract_address, total_supply),
            self.get_transfer_velocity(contract_address),
        )

        # Composite on-chain signal
        conc_mod = concentration.get("signal_modifier", 1.00)
        vel_tier = velocity.get("velocity_tier", "NORMAL")
        vel_modifier = {
            "SPIKE": 1.05, "ELEVATED": 1.03, "ACTIVE": 1.01,
            "NORMAL": 1.00, "QUIET": 0.97
        }.get(vel_tier, 1.00)

        composite_modifier = round(conc_mod * vel_modifier, 3)

        return {
            "ticker":              ticker,
            "contract_address":    contract_address,
            "chain":               "Chiliz Chain (88888)",
            "token_info": {
                "name":            token_info.get("tokenName", ""),
                "symbol":          token_info.get("symbol", ""),
                "total_supply":    total_supply,
                "holder_count":    token_info.get("holdersCount", "unknown"),
            },
            "concentration":       concentration,
            "velocity":            velocity,
            "composite_modifier":  composite_modifier,
            "chiliscan_url":       f"https://chiliscan.com/token/{contract_address}",
            "generated_at":        datetime.now(timezone.utc).isoformat(),
            "sportmind_version":   "3.36.0",
        }

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ──────────────────────────────────────────────────────────────

async def main():
    # Contract addresses from SportMind fan token registry
    PSG_CONTRACT = "0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105"
    BAR_CONTRACT = "0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b"

    intel = ChilizAddressIntelligence()

    print("=== PSG Address Intelligence ===")
    snapshot = await intel.get_address_intelligence_snapshot(PSG_CONTRACT, "PSG")
    import json
    print(json.dumps(snapshot, indent=2))

    await intel.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Integration with SportMind signals

```
BEFORE generating fan token commercial signal:

1. sportmind_macro          → macro modifier
2. sportmind_pre_match      → sporting signal + SMS
3. sportmind_disciplinary   → DSM check
4. ChilizAddressIntelligence → on-chain modifier
   .get_address_intelligence_snapshot(contract, ticker)
   
5. Combine modifiers:
   final_modifier = macro × DSM × concentration × velocity
   
   Example:
     macro_modifier:          1.00 (NEUTRAL)
     DSM_modifier:            0.88 (CITING_ACTIVE)
     concentration_modifier:  0.90 (HIGH — top 10 hold 58%)
     velocity_modifier:       1.03 (ELEVATED — pre-match activity)
     
     final = 1.00 × 0.88 × 0.90 × 1.03 = 0.815
     → Composite 0.815 → WAIT (below 0.88 threshold for ENTER)
     → Without address intelligence: 1.00 × 0.88 × 1.00 = 0.88 → borderline ENTER
     → Address intelligence changes the decision

6. Store snapshot in Memory MCP for pattern detection over time
```

---

## Connection to existing SportMind skills

```
FEEDS INTO:
  fan-token/fan-token-pulse/ — address data enriches HAS calculation
  fan-token/on-chain-event-intelligence/ — smart wallet = Category 1 signal
  fan-token/defi-liquidity-intelligence/ — concentration affects slippage model
  core/athlete-disciplinary-intelligence.md — holder exit rate calibrates DSM values

USES:
  scripts/sportmind_mcp.py → FAN_TOKEN_REGISTRY for contract addresses
  platform/memory-integration.md → store snapshots for pattern detection
  platform/fetch-mcp-disciplinary.md → combine with disciplinary fetch

CALIBRATION CONTRIBUTION:
  Disciplinary event exit rates → calibration records tagged dsm_calibration
  Submit to community/calibration-data/ to improve DSM modifier accuracy
```

---

## Fan Token™ Play Monitor

The `FanTokenPlayMonitor` class detects and classifies Fan Token Play on-chain events
for Path 2 tokens. It distinguishes protocol mechanics (pre-liquidation, post-match
burn/mint) from organic wallet activity, preventing the agent error documented in
`fan-token/on-chain-event-intelligence/` Category 7.

```python
# Extends ChilizAddressIntelligence for Fan Token Play detection
# Requires: contract address, treasury wallet address (from KAYEN or chiliscan metadata)
# Source: fan-token/gamified-tokenomics-intelligence/ Path 2 mechanics

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

class FanTokenPlayMonitor:
    """
    Detects Fan Token Play Path 2 on-chain events for SportMind agents.

    Prevents critical agent error: pre-liquidation must NOT trigger
    Category 1 distribution_signal — it is protocol mechanics, not whale selling.

    Three detectable events per match (Path 2 tokens only):
      1. Pre-liquidation (T-48h): treasury sells ~0.25% supply → USDT
      2. Post-win burn: 95% proceeds buy back + burn to zero address
      3. Post-loss re-mint: treasury receives ~0.25% supply (supply neutral)

    Requirements:
      - Contract address for the fan token
      - Treasury wallet address (from chiliscan token metadata or KAYEN API)
      - ChilizAddressIntelligence instance for transfer queries

    Usage:
      monitor = FanTokenPlayMonitor(
          contract   = "0x1d4343d35f0E0e14C14115876D01dEAa4792550b",  # $AFC
          treasury   = "0x...",   # AFC treasury wallet from chiliscan metadata
          chiliz_api = "https://api.chiliscan.com/api"
      )
      event = await monitor.check_pre_liquidation()
      result = await monitor.check_post_match_settlement(won=True)
    """

    def __init__(self, contract: str, treasury: str,
                 chiliz_api: str = "https://api.chiliscan.com/api"):
        self.contract    = contract
        self.treasury    = treasury.lower()
        self.chiliz_api  = chiliz_api
        self._session    = None

    async def _get_session(self):
        import aiohttp
        if not self._session:
            self._session = aiohttp.ClientSession()
        return self._session

    async def _get_transfers(self, limit: int = 50) -> list:
        """Fetch recent token transfers from Chiliz Chain explorer."""
        session = await self._get_session()
        params = {
            "module":          "account",
            "action":          "tokentx",
            "contractaddress": self.contract,
            "sort":            "desc",
            "offset":          limit,
        }
        try:
            async with session.get(self.chiliz_api, params=params) as resp:
                data = await resp.json()
                return data.get("result", [])
        except Exception:
            return []

    async def identify_treasury_wallet(self) -> dict:
        """
        Identify the treasury wallet for this token from on-chain patterns.
        Treasury wallet characteristics:
          - Holds large % of supply (often 20-40%)
          - Receives minted tokens after losses
          - Initiates pre-liquidation sells before matches
        Manual verification: chiliscan.com/token/{contract} → top holders

        Returns guidance; treasury address must be confirmed manually or via
        KAYEN API token metadata before FanTokenPlayMonitor can operate.
        """
        return {
            "status":       "MANUAL_CONFIRMATION_REQUIRED",
            "method":       "Check chiliscan.com/token/{contract} → Holders tab",
            "look_for":     "Large holder (20-40% supply), labelled 'Treasury' or unlabelled",
            "verify_via":   "KAYEN API: GET /tokens/{address} → treasury_wallet field (if present)",
            "once_confirmed": "Pass treasury address to FanTokenPlayMonitor(treasury=...)",
        }

    async def check_pre_liquidation(self,
                                     window_hours: int = 72) -> dict:
        """
        Detect Fan Token Play pre-liquidation event (T-48h before match).

        Path 2 mechanics: treasury sells exactly 1/400th of supply → USDT
        This is a PROTOCOL event, not organic selling. Never apply
        Category 1 distribution_signal to a confirmed pre-liquidation.

        Returns:
          detected: bool — pre-liquidation found in window
          event_type: FAN_TOKEN_PLAY_PRE_LIQUIDATION | ORGANIC_SELL | NONE
          amount_pct: approximate % of supply moved
          classification_confidence: HIGH | MEDIUM | LOW
          agent_instruction: what to do with this signal
        """
        from datetime import datetime, timezone, timedelta
        import time

        transfers = await self._get_transfers(limit=100)
        cutoff = int(time.time()) - (window_hours * 3600)

        pre_liq_candidates = []
        for tx in transfers:
            ts = int(tx.get("timeStamp", 0))
            if ts < cutoff:
                continue
            sender = tx.get("from", "").lower()
            # Pre-liquidation: treasury is the sender
            if sender == self.treasury:
                value = int(tx.get("value", 0))
                decimals = int(tx.get("tokenDecimal", 18))
                amount = value / (10 ** decimals)
                pre_liq_candidates.append({
                    "hash":      tx.get("hash"),
                    "timestamp": ts,
                    "amount":    amount,
                    "to":        tx.get("to", "").lower(),
                    "datetime":  datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
                })

        if not pre_liq_candidates:
            return {
                "detected":    False,
                "event_type":  "NONE",
                "window_hours": window_hours,
                "agent_instruction": "No pre-liquidation detected. Fan Token Play not active for current window.",
            }

        # Most recent treasury sell in window = likely pre-liquidation
        latest = sorted(pre_liq_candidates, key=lambda x: x["timestamp"], reverse=True)[0]

        # Confidence: HIGH if single treasury sell in window (clean signal)
        confidence = "HIGH" if len(pre_liq_candidates) == 1 else "MEDIUM"

        return {
            "detected":                  True,
            "event_type":                "FAN_TOKEN_PLAY_PRE_LIQUIDATION",
            "hash":                      latest["hash"],
            "datetime":                  latest["datetime"],
            "amount_tokens":             latest["amount"],
            "classification_confidence": confidence,
            "path":                      "PATH_2",
            "agent_instruction": (
                "Fan Token Play CONFIRMED for next match. "
                "DO NOT apply Category 1 distribution_signal. "
                "Set fan_token_play_active=True. "
                "Load fan-token/gamified-tokenomics-intelligence/ for Path 2 modifier."
            ),
            "verify_url": f"https://chiliscan.com/tx/{latest['hash']}",
        }

    async def check_post_match_settlement(self, won: bool,
                                           window_hours: int = 52) -> dict:
        """
        Detect post-match Fan Token Play settlement (within T+48h of result).

        WIN: 95% of proceeds buy back + burn to zero address → supply decreases
        LOSS: pre-liquidated amount minted back to treasury → supply neutral

        Args:
          won: True if team won; False if lost or drew
          window_hours: how far back to look (default 52h covers T+48h + buffer)
        """
        import time
        from datetime import datetime, timezone

        transfers = await self._get_transfers(limit=100)
        cutoff = int(time.time()) - (window_hours * 3600)

        if won:
            # Look for burn: tokens sent TO zero address
            burns = []
            for tx in transfers:
                ts = int(tx.get("timeStamp", 0))
                if ts < cutoff:
                    continue
                to_addr = tx.get("to", "").lower()
                if to_addr == ZERO_ADDRESS:
                    value = int(tx.get("value", 0))
                    decimals = int(tx.get("tokenDecimal", 18))
                    burns.append({
                        "hash":      tx.get("hash"),
                        "datetime":  datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
                        "amount":    value / (10 ** decimals),
                    })

            if burns:
                latest = sorted(burns, key=lambda x: x["datetime"], reverse=True)[0]
                return {
                    "event_type":   "FAN_TOKEN_PLAY_WIN_CONFIRMED",
                    "detected":     True,
                    "burn_hash":    latest["hash"],
                    "datetime":     latest["datetime"],
                    "amount_burned": latest["amount"],
                    "supply_effect": "PERMANENT_REDUCTION",
                    "chz_echo":     "WIN proceeds also contribute to CHZ buyback via 10% ecosystem rule.",
                    "agent_instruction": (
                        "Apply gamified_path2_win_modifier. "
                        "Update season_net_burned_pct in Memory MCP. "
                        "Note CHZ echo signal for macro layer."
                    ),
                    "verify_url":   f"https://chiliscan.com/tx/{latest['burn_hash']}",
                }
            return {
                "event_type":  "FAN_TOKEN_PLAY_WIN_PENDING",
                "detected":    False,
                "note":        "Settlement within T+48h. Check again if not yet confirmed.",
            }

        else:
            # Look for re-mint: treasury receives tokens post-loss
            mints = []
            for tx in transfers:
                ts = int(tx.get("timeStamp", 0))
                if ts < cutoff:
                    continue
                to_addr = tx.get("to", "").lower()
                if to_addr == self.treasury:
                    value = int(tx.get("value", 0))
                    decimals = int(tx.get("tokenDecimal", 18))
                    mints.append({
                        "hash":     tx.get("hash"),
                        "datetime": datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
                        "amount":   value / (10 ** decimals),
                    })

            if mints:
                latest = sorted(mints, key=lambda x: x["datetime"], reverse=True)[0]
                return {
                    "event_type":    "FAN_TOKEN_PLAY_LOSS_CONFIRMED",
                    "detected":      True,
                    "mint_hash":     latest["hash"],
                    "datetime":      latest["datetime"],
                    "amount_minted": latest["amount"],
                    "supply_effect": "NEUTRAL — pre-liquidated amount restored to treasury only",
                    "agent_instruction": (
                        "Path 2 LOSS is supply-neutral. Do NOT apply inflation modifier. "
                        "Apply standard loss sentiment signal only. "
                        "Season_net_burned_pct unchanged."
                    ),
                    "verify_url":    f"https://chiliscan.com/tx/{latest['mint_hash']}",
                }
            return {
                "event_type": "FAN_TOKEN_PLAY_LOSS_PENDING",
                "detected":   False,
                "note":       "Settlement within T+48h. Check again if not yet confirmed.",
            }

    async def get_season_supply_position(self,
                                          original_supply: float) -> dict:
        """
        Calculate season-to-date net supply change from Fan Token Play events.
        Reads all burns (to zero address) and treasury mints since season start.

        Args:
          original_supply: total supply at season start (from KAYEN or chiliscan)
        """
        transfers = await self._get_transfers(limit=500)

        total_burned = 0.0
        total_minted = 0.0

        for tx in transfers:
            value     = int(tx.get("value", 0))
            decimals  = int(tx.get("tokenDecimal", 18))
            amount    = value / (10 ** decimals)
            to_addr   = tx.get("to", "").lower()
            from_addr = tx.get("from", "").lower()

            if to_addr == ZERO_ADDRESS:
                total_burned += amount
            elif to_addr == self.treasury and from_addr != ZERO_ADDRESS:
                total_minted += amount

        net_burned     = total_burned - total_minted
        net_burned_pct = (net_burned / original_supply * 100) if original_supply else 0

        if net_burned_pct > 10:
            supply_signal = "STRONG_SCARCITY"
        elif net_burned_pct > 5:
            supply_signal = "MODERATE_SCARCITY"
        elif net_burned_pct > 0:
            supply_signal = "MILD_SCARCITY"
        elif net_burned_pct > -5:
            supply_signal = "MILD_DILUTION"
        else:
            supply_signal = "SIGNIFICANT_DILUTION"

        return {
            "total_burned_tokens": round(total_burned, 2),
            "total_minted_tokens": round(total_minted, 2),
            "net_burned_tokens":   round(net_burned, 2),
            "net_burned_pct":      round(net_burned_pct, 4),
            "supply_signal":       supply_signal,
            "season_modifier_note": (
                f"Apply season_supply_modifier if net_burned_pct > 5%. "
                f"Current: {net_burned_pct:.2f}% net burned."
            ),
        }

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ─────────────────────────────────────────────────────────────

async def fan_token_play_example():
    """
    Example: Monitor $AFC Fan Token Play for Arsenal UCL fixture.
    $AFC confirmed PATH_2 as of 07 April 2026.
    """
    import json

    monitor = FanTokenPlayMonitor(
        contract = "0x1d4343d35f0E0e14C14115876D01dEAa4792550b",  # $AFC
        treasury = "0x_CONFIRM_VIA_CHILISCAN",  # verify at chiliscan.com/token/0x1d43...
    )

    # 48h before match: check if pre-liquidation has occurred
    print("=== Checking for pre-liquidation (T-48h) ===")
    pre_liq = await monitor.check_pre_liquidation(window_hours=72)
    print(json.dumps(pre_liq, indent=2))

    # After match (if Arsenal won):
    print("\n=== Checking post-match settlement (WIN) ===")
    settlement = await monitor.check_post_match_settlement(won=True)
    print(json.dumps(settlement, indent=2))

    # Season supply position:
    print("\n=== Season supply position ===")
    # Get original supply from KAYEN: GET /tokens/{address} → total_supply
    position = await monitor.get_season_supply_position(original_supply=40_000_000)
    print(json.dumps(position, indent=2))

    await monitor.close()
```

---


---

*SportMind v3.45 · MIT License · sportmind.dev*
*Chiliz Chain — Chain ID 88888 · chiliscan.com/documentation/api/etherscan-like/accounts*
*See also: platform/data-connector-templates.md · fan-token/on-chain-event-intelligence/*
*platform/memory-integration.md · scripts/sportmind_mcp.py (FAN_TOKEN_REGISTRY)*
