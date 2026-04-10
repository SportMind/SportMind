#!/usr/bin/env python3
"""
SportMind Template — Portfolio Monitor
=======================================
Copy this file, fill in your token list below, and run.
Reviews multiple fan tokens in one session — macro check once,
then sentiment snapshot and disciplinary check for each token.

Requirements:
  pip install aiohttp

Setup:
  1. Start the MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Add your tokens to PORTFOLIO below
  3. Run: python portfolio-monitor.py

What this does:
  - One macro check (applies to all tokens)
  - Sentiment snapshot per token
  - Ranks portfolio by current opportunity
  - Flags any tokens needing immediate attention
  - Outputs a ranked summary with reasoning

Docs: https://sportmind.dev/docs
"""

import asyncio
import json
import aiohttp
from datetime import datetime, timezone

# ── YOUR CONFIGURATION ────────────────────────────────────────────────────────

SPORTMIND_MCP = "http://localhost:3001/mcp"

# Add or remove tokens. Format: {"ticker": "...", "sport": "...", "tier": 1 or 2}
# Available tickers: PSG, BAR, CITY, JUV, ACM, INTER, ATM, AFC, GAL, ASR,
#                    ARG, MENGO, AVL, BENFICA, TRA, CHVS, SAN, UFC,
#                    SHARKS, SARRIES, OG, SAUBER, AM, HASHTAG
PORTFOLIO = [
    {"ticker": "PSG",  "sport": "football", "tier": 1},
    {"ticker": "BAR",  "sport": "football", "tier": 1},
    {"ticker": "CITY", "sport": "football", "tier": 1},
    {"ticker": "ACM",  "sport": "football", "tier": 1},
    {"ticker": "UFC",  "sport": "mma",      "tier": 1},
]

MIN_SMS_ENTER = 60   # Minimum SMS to recommend ENTER
MIN_SMS_WAIT  = 40   # Below this = ABSTAIN from analysis

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


async def analyse_token(session: aiohttp.ClientSession,
                         token: dict, macro_modifier: float) -> dict:
    """Run full analysis for a single token."""
    ticker   = token["ticker"]
    sport    = token["sport"]
    use_case = f"fan_token_tier{token['tier']}"

    # Sentiment snapshot
    sentiment = await call_tool(session, "sportmind_sentiment_snapshot",
                                 {"token": ticker, "use_case": use_case})
    composite = sentiment.get("composite_signal", {})
    sms       = composite.get("sms", 0)
    name      = sentiment.get("name", ticker)

    # Determine recommendation
    if macro_modifier < 0.75:
        rec    = "WAIT"
        reason = "Macro override"
    elif sms < MIN_SMS_WAIT:
        rec    = "ABSTAIN"
        reason = f"SMS {sms:.0f} — insufficient coverage"
    elif sms < MIN_SMS_ENTER:
        rec    = "WAIT"
        reason = f"SMS {sms:.0f} — partial coverage"
    else:
        rec    = "ENTER"
        reason = f"SMS {sms:.0f} — clear signal"

    return {
        "ticker":   ticker,
        "name":     name,
        "sport":    sport,
        "sms":      sms,
        "rec":      rec,
        "reason":   reason,
        "fantokens":sentiment.get("fantokens_url", ""),
        "chiliscan":sentiment.get("chiliscan_url", ""),
    }


async def run():
    print(f"\n{'═' * 56}")
    print(f"  SportMind Portfolio Monitor")
    print(f"  {len(PORTFOLIO)} tokens · "
          f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'═' * 56}\n")

    async with aiohttp.ClientSession() as session:

        # ── Macro check (once for all tokens) ────────────────────────────────
        print("Macro check...")
        macro    = await call_tool(session, "sportmind_macro", {})
        cycle    = macro.get("macro_state", {}).get("crypto_cycle", {})
        modifier = cycle.get("macro_modifier", 1.00)
        phase    = cycle.get("phase", "UNKNOWN")
        print(f"  Phase: {phase}  Modifier: {modifier}")

        if modifier < 0.75:
            print(f"\n  ⚠  MACRO OVERRIDE — all tokens set to WAIT")
            print(f"  Resume when macro_modifier returns to ≥ 0.75\n")

        print()

        # ── Analyse each token ────────────────────────────────────────────────
        print("Analysing tokens...\n")
        results = []
        for token in PORTFOLIO:
            print(f"  {token['ticker']}...", end=" ", flush=True)
            result = await analyse_token(session, token, modifier)
            results.append(result)
            print(f"{result['rec']} (SMS {result['sms']:.0f})")

        # ── Sort and display ──────────────────────────────────────────────────
        order   = {"ENTER": 0, "WAIT": 1, "ABSTAIN": 2}
        results = sorted(results, key=lambda x: (order.get(x["rec"], 3), -x["sms"]))

        print(f"\n{'═' * 56}")
        print(f"  PORTFOLIO SUMMARY")
        print(f"{'═' * 56}\n")

        for group, label in [("ENTER", "✓ ENTER"), ("WAIT", "~ WAIT"), ("ABSTAIN", "✗ ABSTAIN")]:
            group_results = [r for r in results if r["rec"] == group]
            if not group_results:
                continue
            print(f"  {label}")
            for r in group_results:
                print(f"    {r['ticker']:<8} {r['name']:<30} {r['reason']}")
                if r["fantokens"]:
                    print(f"             {r['fantokens']}")
            print()

        # ── Flags ─────────────────────────────────────────────────────────────
        enter_count  = sum(1 for r in results if r["rec"] == "ENTER")
        wait_count   = sum(1 for r in results if r["rec"] == "WAIT")
        abstain_count= sum(1 for r in results if r["rec"] == "ABSTAIN")

        print(f"  Summary: {enter_count} ENTER · "
              f"{wait_count} WAIT · {abstain_count} ABSTAIN")
        print(f"  Macro:   {phase} ({modifier})")
        print(f"\n  ⚠  SportMind produces intelligence signals, not financial advice.")
        print(f"     Always verify against live sources before acting.\n")


if __name__ == "__main__":
    asyncio.run(run())
