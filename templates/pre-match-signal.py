#!/usr/bin/env python3
"""
SportMind Template — Pre-Match Signal
======================================
Copy this file, fill in your match details below, and run.
Generates a complete pre-match intelligence signal in one call.
No MCP server required — calls the MCP tools directly.

Requirements:
  pip install aiohttp

Setup:
  1. Start the MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Fill in YOUR MATCH DETAILS below
  3. Run: python pre-match-signal.py

What this does:
  - Macro gate check
  - Full pre-match intelligence package (all five layers)
  - Verifiable source for lineup confirmation
  - Final ENTER / WAIT / ABSTAIN with reasoning trace

Sports available:
  football, basketball, cricket, mma, formula1, tennis, rugby,
  rugby_league, afl, baseball, ice_hockey, motogp, nascar, kabaddi,
  netball, handball, esports, darts, snooker

Docs: https://sportmind.dev/docs
"""

import asyncio
import json
import aiohttp
from datetime import datetime, timezone

# ── YOUR CONFIGURATION (MATCH DETAILS) ───────────────────────────────────────

SPORTMIND_MCP = "http://localhost:3001/mcp"

SPORT         = "football"                    # See sports list above
HOME_TEAM     = "PSG"                         # Home team / player / entry 1
AWAY_TEAM     = "Arsenal"                     # Away team / player / entry 2
COMPETITION   = "UCL Quarter-Final"           # Competition name
KICKOFF       = "2026-05-07T20:00:00Z"        # ISO-8601 UTC datetime

# fan_token_tier1, fan_token_tier2, pre_match, prediction_market, commercial_brief
USE_CASE      = "fan_token_tier1"

# Optional: token ticker if this is a fan token analysis
TOKEN         = "PSG"    # Leave as "" to skip token lookup

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
    print(f"\n{'═' * 56}")
    print(f"  SportMind Pre-Match Signal")
    print(f"  {HOME_TEAM} vs {AWAY_TEAM}")
    print(f"  {COMPETITION} · {SPORT}")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'═' * 56}\n")

    async with aiohttp.ClientSession() as session:

        # ── Phase 1: Macro gate ───────────────────────────────────────────────
        print("Phase 1 — Macro gate")
        macro    = await call_tool(session, "sportmind_macro", {})
        cycle    = macro.get("macro_state", {}).get("crypto_cycle", {})
        modifier = cycle.get("macro_modifier", 1.00)
        phase    = cycle.get("phase", "UNKNOWN")
        print(f"  {phase} — modifier {modifier}", end="")

        if modifier < 0.75:
            print(f" ⚠  OVERRIDE ACTIVE")
            print(f"\n  Recommendation: WAIT")
            print(f"  Reason: Macro override — modifier {modifier} < 0.75\n")
            return
        print(f" ✓\n")

        # ── Phase 2: Pre-match signal ─────────────────────────────────────────
        print("Phase 2 — Pre-match intelligence")
        prematch = await call_tool(session, "sportmind_pre_match", {
            "sport":       SPORT,
            "home_team":   HOME_TEAM,
            "away_team":   AWAY_TEAM,
            "competition": COMPETITION,
            "kickoff":     KICKOFF,
            "use_case":    USE_CASE,
        })

        signal   = prematch.get("signal", {})
        score    = prematch.get("sportmind_score", {})
        avail    = prematch.get("availability_check", {})
        sequence = prematch.get("reasoning_sequence", [])

        direction = signal.get("direction", "—")
        adj_score = signal.get("adjusted_score", 0)
        sms       = score.get("sms", 0)
        sms_tier  = score.get("sms_tier", "—")
        layers    = score.get("layers_loaded", [])
        action    = signal.get("recommended_action", "—")

        print(f"  Direction:     {direction}")
        print(f"  Score:         {adj_score}")
        print(f"  SMS:           {sms} ({sms_tier})")
        print(f"  Layers loaded: {layers}")
        print(f"  Action:        {action}")
        print()

        # ── Phase 3: Lineup verification source ───────────────────────────────
        print("Phase 3 — Lineup verification")
        print(f"  Source: {avail.get('source', '—')}")
        print(f"  Tier:   {avail.get('tier', '—')} (ground truth)")
        print()

        # ── Phase 4: Token context (optional) ────────────────────────────────
        if TOKEN:
            print("Phase 4 — Token context")
            lookup = await call_tool(session, "sportmind_fan_token_lookup",
                                      {"query": TOKEN})
            if lookup.get("found"):
                td = lookup["tokens"][0]
                print(f"  Token:    {td['name']} ({td['ticker']}) Tier {td['market_cap_tier']}")
                print(f"  Contract: {td['contract_address']}")
                print(f"  Verify:   {td['chiliscan_url']}")
            else:
                print(f"  Token '{TOKEN}' not in registry")
            print()

        # ── Phase 5: Final signal ─────────────────────────────────────────────
        print("Phase 5 — Final signal")

        if modifier < 0.75:
            final_rec = "WAIT"
            final_reason = f"Macro override ({modifier})"
        elif sms < 40:
            final_rec = "WAIT"
            final_reason = f"SMS {sms} — insufficient coverage"
        elif sms < 60:
            final_rec = "WAIT"
            final_reason = f"SMS {sms} — partial coverage"
        else:
            final_rec = action
            final_reason = f"SMS {sms}, macro {modifier}, direction {direction}"

        print(f"\n  {'─' * 50}")
        print(f"  Recommendation:  {final_rec}")
        print(f"  Reason:          {final_reason}")
        print(f"  Direction:       {direction}")
        print(f"  Adjusted score:  {adj_score}")
        print(f"  SMS:             {sms} ({sms_tier})")
        print(f"  Macro modifier:  {modifier} ({phase})")
        print(f"  {'─' * 50}")

        if sequence:
            print(f"\n  Reasoning sequence:")
            for step in sequence:
                print(f"    {step}")

        print(f"\n  ⚠  SportMind produces intelligence signals, not financial advice.")
        print(f"     Verify lineup at: {avail.get('source', 'official source')}")
        print(f"     before acting on any signal.\n")


if __name__ == "__main__":
    asyncio.run(run())
