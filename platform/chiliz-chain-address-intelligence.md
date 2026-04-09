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

*SportMind v3.36 · MIT License · sportmind.dev*
*Chiliz Chain — Chain ID 88888 · chiliscan.com/documentation/api/etherscan-like/accounts*
*See also: platform/data-connector-templates.md · fan-token/on-chain-event-intelligence/*
*platform/memory-integration.md · scripts/sportmind_mcp.py (FAN_TOKEN_REGISTRY)*
