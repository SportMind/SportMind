#!/usr/bin/env python3
"""
SportMind Template — Fan Token Monitor
=======================================
Copy this file, fill in your configuration below, and run.
Monitors a single fan token using the SportMind MCP server.

Requirements:
  pip install aiohttp

Setup:
  1. Start the MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Fill in YOUR configuration below
  3. Run: python fan-token-monitor.py

What this does:
  - Checks macro state (gates all fan token analysis)
  - Looks up your token in the Chiliz Chain registry
  - Gets sentiment snapshot across all signal dimensions
  - Runs disciplinary check for key players
  - Outputs ENTER / WAIT / ABSTAIN with full reasoning

Docs: https://sportmind.dev/docs
"""

import asyncio
import json
import aiohttp
from datetime import datetime, timezone

# ── YOUR CONFIGURATION ────────────────────────────────────────────────────────
# Change these values. Everything else runs automatically.

SPORTMIND_MCP = "http://localhost:3001/mcp"   # MCP server endpoint

TOKEN          = "PSG"          # Token ticker: PSG, BAR, CITY, JUV, ACM,
                                # INTER, ATM, AFC, GAL, ASR, ARG, MENGO,
                                # AVL, BENFICA, TRA, CHVS, SAN, UFC,
                                # SHARKS, SARRIES, OG, SAUBER, AM, HASHTAG

SPORT          = "football"     # football, mma, rugby, esports, formula1

USE_CASE       = "fan_token_tier1"  # fan_token_tier1 or fan_token_tier2

KEY_PLAYERS    = [              # Players to check for disciplinary flags
    "",                         # Add names, e.g. "K. Mbappé", "R. Timber"
]

# ── END CONFIGURATION ─────────────────────────────────────────────────────────


async def call_tool(session: aiohttp.ClientSession, tool: str, args: dict) -> dict:
    """Call a SportMind MCP tool."""
    payload = {
        "jsonrpc": "2.0",
        "method":  "tools/call",
        "params":  {"name": tool, "arguments": args},
        "id":      1,
    }
    async with session.post(SPORTMIND_MCP, json=payload) as resp:
        data = await resp.json()
        content = data.get("result", {}).get("content", [{}])
        text = content[0].get("text", "{}") if content else "{}"
        return json.loads(text)


async def run():
    print(f"\n{'═' * 52}")
    print(f"  SportMind Fan Token Monitor")
    print(f"  Token: {TOKEN} · Sport: {SPORT}")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'═' * 52}\n")

    async with aiohttp.ClientSession() as session:

        # ── Phase 1: Macro gate ───────────────────────────────────────────────
        print("Phase 1 — Macro gate")
        macro = await call_tool(session, "sportmind_macro", {})
        cycle = macro.get("macro_state", {}).get("crypto_cycle", {})
        modifier = cycle.get("macro_modifier", 1.00)
        phase    = cycle.get("phase", "UNKNOWN")
        print(f"  Phase:    {phase}")
        print(f"  Modifier: {modifier}")

        if modifier < 0.75:
            print(f"\n  ⚠  MACRO OVERRIDE — modifier {modifier} < 0.75")
            print(f"  Recommendation: WAIT — crypto bear market active")
            print(f"  Resume analysis when macro_modifier returns to ≥ 0.75\n")
            return
        print(f"  ✓ Macro clear — proceeding\n")

        # ── Phase 2: Token lookup ─────────────────────────────────────────────
        print("Phase 2 — Token registry")
        lookup = await call_tool(session, "sportmind_fan_token_lookup",
                                  {"query": TOKEN})
        if not lookup.get("found"):
            print(f"  ✗ Token '{TOKEN}' not found in registry")
            print(f"  Check ticker against: {lookup.get('registry_size', 24)} registered tokens")
            return

        token_data = lookup["tokens"][0]
        print(f"  Token:    {token_data['name']} ({token_data['ticker']})")
        print(f"  Tier:     {token_data['market_cap_tier']}")
        print(f"  Chain:    {token_data['chain']}")
        print(f"  Contract: {token_data['contract_address']}")
        print(f"  Verify:   {token_data['chiliscan_url']}")
        print()

        # ── Phase 3: Sentiment snapshot ───────────────────────────────────────
        print("Phase 3 — Sentiment snapshot")
        sentiment = await call_tool(session, "sportmind_sentiment_snapshot",
                                     {"token": TOKEN, "use_case": USE_CASE})
        composite = sentiment.get("composite_signal", {})
        sms       = composite.get("sms", 0)
        action    = composite.get("recommended_action", "UNKNOWN")
        snap      = sentiment.get("sentiment_snapshot", {})
        macro_s   = snap.get("macro_sentiment", {})

        print(f"  SMS:    {sms} ({composite.get('sms_tier', '—')})")
        print(f"  Macro sentiment: {macro_s.get('signal', '—')} "
              f"(modifier {macro_s.get('macro_modifier', '—')})")
        print(f"  Action: {action}")
        print()

        # ── Phase 4: Disciplinary check ───────────────────────────────────────
        dsm_flags = []
        active_key_players = [p for p in KEY_PLAYERS if p.strip()]

        if active_key_players:
            print("Phase 4 — Disciplinary checks")
            for player in active_key_players:
                disc = await call_tool(session, "sportmind_disciplinary",
                                        {"player": player, "sport": SPORT,
                                         "include_framework": False})
                status = disc.get("disciplinary_check", {}).get("status", "")
                source = disc.get("regulatory_source", "")
                print(f"  {player}: {status}")
                print(f"    Verify: {source}")
            print()
        else:
            print("Phase 4 — Disciplinary check (add KEY_PLAYERS to enable)\n")

        # ── Phase 5: Final recommendation ─────────────────────────────────────
        print("Phase 5 — Final recommendation")

        commercial_blocked = any(
            f in dsm_flags for f in
            ["COMMERCIAL_RISK_ACTIVE", "LEGAL_PROCEEDINGS_ACTIVE"]
        )

        if commercial_blocked:
            recommendation = "ABSTAIN"
            reason         = "Active commercial or legal flag — see disciplinary check"
        elif modifier < 0.75:
            recommendation = "WAIT"
            reason         = f"Macro override active (modifier {modifier})"
        elif sms < 40:
            recommendation = "WAIT"
            reason         = f"SMS {sms} below minimum threshold (40)"
        elif sms < 60:
            recommendation = "WAIT"
            reason         = f"SMS {sms} — partial coverage, reduce sizing"
        else:
            recommendation = "ENTER"
            reason         = f"SMS {sms}, macro clear, no blocking flags"

        print(f"\n  ┌─────────────────────────────────────┐")
        print(f"  │  {recommendation:<35}│")
        print(f"  │  {reason[:35]:<35}│")
        print(f"  └─────────────────────────────────────┘")
        print(f"\n  Token:    {TOKEN} — {token_data['name']}")
        print(f"  Contract: {token_data['contract_address']}")
        print(f"  Market:   {token_data['fantokens_url']}")
        print(f"\n  ⚠  SportMind produces intelligence signals, not financial advice.")
        print(f"     Always verify against live sources before acting.\n")


if __name__ == "__main__":
    asyncio.run(run())
