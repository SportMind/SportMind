# Agentic Workflow Pattern 8 — Fan Token Play Monitor

**Purpose:** Autonomous monitoring of Fan Token Play Path 2 tokens across the full
T-48h → kickoff → T+48h match cycle. Detects pre-liquidation events, applies correct
gamified modifiers, verifies post-match settlement, and updates season supply position
in Memory MCP after every confirmed event.

**Trigger:** T-48h before any match involving a confirmed Fan Token Play token
**Cycle:** Event-driven (match calendar) + T+48h post-result check
**Autonomy:** Level 2 (alerts autonomously; human decides on action)
**Confirmed token:** $AFC (Arsenal FC) — PATH_2 confirmed 07 April 2026
**Required:** FanTokenPlayMonitor (platform/chiliz-chain-address-intelligence.md)

---

## Why Fan Token Play needs its own workflow

Existing workflow patterns assume a single key timing event: T-2h lineup confirmation.
Fan Token Play Path 2 adds a second critical timing event: T-48h pre-liquidation.

An agent running Pattern 1 (Portfolio Monitor) on $AFC without this workflow will:
- See the T-48h treasury sell as a Category 1 distribution signal (incorrect)
- Apply a bearish modifier to a protocol event (incorrect)
- Miss the post-match burn or re-mint confirmation (incomplete)
- Fail to update season supply position in Memory MCP (incomplete)

This pattern corrects all four failures.

---

## The four-phase match cycle

```
PHASE 1 — T-72h to T-48h: Pre-liquidation window
  Agent checks: Has the treasury sold ~0.25% of supply to USDT?
  If YES: Fan Token Play ACTIVE for this match
          Set fan_token_play_active = True in Memory MCP
          Do NOT apply Category 1 distribution signal
  If NO:  Check again at T-36h (settlement may be early or late by a few hours)

PHASE 2 — At kickoff: Confirm play status
  Agent verifies: pre-liquidation tx visible on chiliscan.com
  Proceeds with Path 2 gamified modifier in pre-match signal

PHASE 3 — T+0 to T+48h: Post-match settlement window
  Agent polls every 4h for settlement transaction
  WIN: burn to 0x0000...0000 detected → apply gamified_path2_win_modifier
  LOSS: treasury mint detected → confirm supply-neutral (no negative modifier)
  DRAW: no supply change expected → standard sentiment signal

PHASE 4 — T+48h: Season supply position update
  Agent calculates net season supply change from all confirmed FTP events
  Updates Memory MCP: season_net_burned_pct, supply_signal tier
  Generates season supply report if >5% net burned
```

---

## Implementation

```python
"""
SportMind Agentic Workflow Pattern 8 — Fan Token Play Monitor
Monitors Fan Token Play Path 2 tokens across the full match cycle.

Requirements: pip install aiohttp schedule
Setup:
  1. Start MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Confirm treasury wallet for each monitored token via chiliscan.com
  3. Set TREASURY_WALLETS below (must be confirmed manually)
  4. Run: python fan-token-play-monitor.py

Confirmed tokens:
  AFC (Arsenal FC) — PATH_2 confirmed 07 April 2026
  All others: check sportmind_fan_token_lookup for fan_token_play field
"""

import asyncio
import json
import aiohttp
import logging
from datetime import datetime, timezone
from typing import Optional

log = logging.getLogger("sportmind.ftp-monitor")

# ── CONFIGURATION ─────────────────────────────────────────────────────────────
SPORTMIND_MCP = "http://localhost:3001/mcp"

# Tokens with confirmed Fan Token Play status
# Treasury addresses MUST be confirmed via chiliscan.com before use
FTP_TOKENS = {
    "AFC": {
        "contract":     "0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
        "treasury":     "0x_CONFIRM_VIA_CHILISCAN",  # verify: chiliscan.com/token/0x1d43...
        "path":         "PATH_2",
        "confirmed":    "2026-04-07",
    },
    # Add more tokens as Fan Token Play rolls out:
    # "PSG": {"contract": "0xc2661...", "treasury": "0x...", "path": "PATH_2"},
}

CHILIZ_API       = "https://api.chiliscan.com/api"
CHECK_INTERVAL_H = 4     # How often to poll in each phase
ORIGINAL_SUPPLY  = {     # Total supply at season start — confirm from KAYEN
    "AFC": 40_000_000,
}
# ── END CONFIGURATION ─────────────────────────────────────────────────────────


class FTPMatchCycle:
    """Tracks state for a single Fan Token Play match cycle."""

    def __init__(self, token: str, match_date: str):
        self.token        = token
        self.match_date   = match_date
        self.phase        = "AWAITING_PRE_LIQ"
        self.pre_liq_tx   = None
        self.result       = None  # "WIN" | "LOSS" | "DRAW"
        self.settlement_tx = None
        self.ftp_active   = False

    def to_dict(self):
        return {
            "token":         self.token,
            "match_date":    self.match_date,
            "phase":         self.phase,
            "ftp_active":    self.ftp_active,
            "pre_liq_tx":    self.pre_liq_tx,
            "result":        self.result,
            "settlement_tx": self.settlement_tx,
        }


async def call_mcp(session: aiohttp.ClientSession, tool: str, args: dict) -> dict:
    """Call a SportMind MCP tool."""
    payload = {
        "jsonrpc": "2.0", "method": "tools/call",
        "params":  {"name": tool, "arguments": args}, "id": 1,
    }
    async with session.post(SPORTMIND_MCP, json=payload) as resp:
        data     = await resp.json()
        content  = data.get("result", {}).get("content", [{}])
        text     = content[0].get("text", "{}") if content else "{}"
        return json.loads(text)


async def check_pre_liquidation(token: str, contract: str,
                                 treasury: str) -> dict:
    """
    Query chiliscan.com for treasury pre-liquidation in the T-72h window.
    Treasury sell of ~0.25% supply = Fan Token Play active.
    """
    import time
    async with aiohttp.ClientSession() as session:
        params = {
            "module": "account", "action": "tokentx",
            "contractaddress": contract, "sort": "desc", "offset": 50,
        }
        async with session.get(CHILIZ_API, params=params) as resp:
            data = await resp.json()

        transfers  = data.get("result", [])
        cutoff     = int(time.time()) - (72 * 3600)
        treasury_l = treasury.lower()

        for tx in transfers:
            ts = int(tx.get("timeStamp", 0))
            if ts < cutoff:
                continue
            if tx.get("from", "").lower() == treasury_l:
                return {
                    "detected":    True,
                    "hash":        tx["hash"],
                    "datetime":    datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(),
                    "agent_rule":  "PROTOCOL MECHANICS — do not apply Category 1 distribution_signal.",
                }
    return {"detected": False}


async def check_post_match_settlement(contract: str, treasury: str,
                                       won: bool) -> dict:
    """Check for post-match burn (WIN) or re-mint (LOSS)."""
    import time
    ZERO = "0x0000000000000000000000000000000000000000"
    async with aiohttp.ClientSession() as session:
        params = {
            "module": "account", "action": "tokentx",
            "contractaddress": contract, "sort": "desc", "offset": 100,
        }
        async with session.get(CHILIZ_API, params=params) as resp:
            data = await resp.json()

        transfers  = data.get("result", [])
        cutoff     = int(time.time()) - (52 * 3600)
        treasury_l = treasury.lower()

        for tx in transfers:
            ts = int(tx.get("timeStamp", 0))
            if ts < cutoff:
                continue
            if won and tx.get("to", "").lower() == ZERO:
                return {
                    "event":   "FAN_TOKEN_PLAY_WIN_CONFIRMED",
                    "hash":    tx["hash"],
                    "note":    "Supply permanently reduced. Update season_net_burned_pct.",
                    "chz_echo": "WIN also contributes to CHZ ecosystem burn.",
                }
            elif not won and tx.get("to", "").lower() == treasury_l:
                return {
                    "event":  "FAN_TOKEN_PLAY_LOSS_CONFIRMED",
                    "hash":   tx["hash"],
                    "note":   "Supply neutral — pre-liquidated amount restored to treasury only.",
                }
    return {"event": "PENDING", "note": "Settlement not yet confirmed. Check again in 4h."}


async def run_match_cycle(token: str, match_date: str, result: Optional[str] = None):
    """
    Run the full four-phase Fan Token Play match cycle.

    Args:
      token:      Token ticker (e.g. "AFC")
      match_date: ISO date string of the match
      result:     "WIN" | "LOSS" | "DRAW" — set after full-time
    """
    config  = FTP_TOKENS.get(token)
    if not config:
        log.warning(f"{token} not in FTP_TOKENS config")
        return

    cycle = FTPMatchCycle(token, match_date)
    print(f"\n{'═'*52}")
    print(f"  Fan Token Play Monitor — {token}")
    print(f"  Match: {match_date}  |  Path: {config['path']}")
    print(f"{'═'*52}\n")

    # PHASE 1: Check for pre-liquidation
    print("Phase 1 — Pre-liquidation check (T-72h to T-48h)")
    pre_liq = await check_pre_liquidation(
        token    = token,
        contract = config["contract"],
        treasury = config["treasury"],
    )

    if pre_liq["detected"]:
        cycle.phase    = "PRE_LIQ_DETECTED"
        cycle.ftp_active = True
        cycle.pre_liq_tx = pre_liq["hash"]
        print(f"  ✅ FAN TOKEN PLAY ACTIVE — pre-liquidation detected")
        print(f"  Tx: {pre_liq['hash']}")
        print(f"  Rule: {pre_liq['agent_rule']}")
    else:
        print(f"  ○ No pre-liquidation detected yet. Check again at T-36h.")
        return

    # PHASE 2: Pre-match signal (load gamified modifier)
    print("\nPhase 2 — Pre-match signal with gamified modifier")
    async with aiohttp.ClientSession() as session:
        macro = await call_mcp(session, "sportmind_macro", {})
        mod   = macro.get("macro_state", {}).get("crypto_cycle", {}).get("macro_modifier", 1.00)
        print(f"  Macro: {macro.get('macro_state', {}).get('crypto_cycle', {}).get('phase', '?')} ({mod})")

        # Path 2 win modifier ≈ 1.006 per match
        path2_win_modifier = 1.006
        print(f"  Path 2 gamified_win_modifier: {path2_win_modifier}")
        print(f"  Load: fan-token/gamified-tokenomics-intelligence/ for full calculation")
        cycle.phase = "MATCH_IN_PROGRESS"

    # PHASE 3: Post-match settlement (if result known)
    if result:
        cycle.result = result
        if result == "DRAW":
            print(f"\nPhase 3 — Draw: no supply change expected")
            cycle.phase = "SETTLEMENT_COMPLETE"
        else:
            print(f"\nPhase 3 — Post-match settlement check ({result})")
            settlement = await check_post_match_settlement(
                contract = config["contract"],
                treasury = config["treasury"],
                won      = (result == "WIN"),
            )
            cycle.settlement_tx = settlement.get("hash")
            print(f"  {settlement['event']}")
            print(f"  {settlement['note']}")
            if "chz_echo" in settlement:
                print(f"  CHZ: {settlement['chz_echo']}")
            cycle.phase = "SETTLEMENT_COMPLETE"

    # PHASE 4: Season supply update
    if cycle.phase == "SETTLEMENT_COMPLETE":
        print(f"\nPhase 4 — Season supply position update")
        print(f"  Run: FanTokenPlayMonitor.get_season_supply_position({token})")
        print(f"  Update Memory MCP: season_net_burned_pct for {token}")
        print(f"  See: platform/memory-integration.md for token_memory schema")

    print(f"\n  Cycle complete: {json.dumps(cycle.to_dict(), indent=2)}\n")
    return cycle


# ── Run example ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example: AFC European fixture
    # Set result after full-time: "WIN", "LOSS", or "DRAW"
    asyncio.run(run_match_cycle(
        token      = "AFC",
        match_date = "2026-04-10",
        result     = "WIN",   # set to None if pre-match only
    ))
```

---

## Memory MCP schema for Fan Token Play

```json
{
  "token_memory": {
    "AFC": {
      "fan_token_play": {
        "path":                  "PATH_2",
        "season_net_burned_pct": -1.44,
        "supply_signal":         "MILD_SCARCITY",
        "confirmed_ftp_events": [
          {
            "match_date":    "2026-04-07",
            "result":        "WIN",
            "pre_liq_tx":    "0x...",
            "settlement_tx": "0x...",
            "supply_effect": "PERMANENT_REDUCTION"
          }
        ],
        "last_updated":  "2026-04-10T12:00:00Z"
      }
    }
  }
}
```

---

## Connection to other SportMind patterns

```
FEEDS FROM:
  Pattern 2 (Pre-Match Chain) — standard pre-match signal; add gamified modifier
  Pattern 1 (Portfolio Monitor) — AFC in portfolio triggers this pattern

FEEDS INTO:
  pattern/memory-integration.md    — season supply position storage
  fan-token/gamified-tokenomics-intelligence/ — Path 2 modifier calculation
  platform/chiliz-chain-address-intelligence.md — FanTokenPlayMonitor class
  macro/macro-crypto-market-cycles.md — CHZ echo signal via virtuous cycle

TRIGGER INTEGRATION:
  Add to portfolio monitor: if token has fan_token_play field AND match in next 72h:
    → Spawn FTP monitor cycle alongside standard pre-match chain
    → Two concurrent checks: lineup (T-2h) + pre-liquidation (T-48h)
```

---

*SportMind v3.45 · MIT License · sportmind.dev*
*See: fan-token/gamified-tokenomics-intelligence/ · platform/chiliz-chain-address-intelligence.md*
*$AFC PATH_2 confirmed 07 April 2026*
