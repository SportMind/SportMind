# Agentic Workflow Pattern 11 — Post-Match Analysis Agent

**Purpose:** Runs the full post-match intelligence cycle after a result
is confirmed — connecting sporting outcome, fan token commercial impact,
Fan Token Play settlement, social signal, and plain-English summary for
fan token holders. Bridges the pre-match signal to the next cycle.

**Trigger:** Match full-time confirmed (manual or calendar-driven)
**Cycle:** T+0h (immediate), T+2h (primary), T+24h (consolidation)
**Autonomy:** Level 2 — generates briefs autonomously, holder decides action
**Primary output:** Two formats — technical JSON (for agents/developers)
                   + plain-English brief (for fan token holders, Prompt 21)

---

## Why post-match needs its own pattern

The pre-match chain (Pattern 2) ends at kickoff. What happens in the
hours after a result is equally important and currently has no dedicated
workflow in SportMind.

For a token like $AFC on Fan Token Play Path 2, the post-match window
has three distinct events with different timing:
- T+0: result confirmed → sentiment shift begins
- T+2h to T+24h: FTP settlement (burn or re-mint) on-chain
- T+24h to T+72h: commercial window either opens (win) or closes (loss)

None of these are handled by the pre-match or portfolio patterns alone.

---

## How the layers connect

```
RESULT CONFIRMED (T+0)
        │
        ▼
LAYER 5 — MACRO CHECK
  Is the macro environment still the same as pre-match?
  A crypto market move during the match changes the signal.
  Source: sportmind_macro()
        │
        ▼
LAYER 1 — SPORTING RESULT ANALYSIS
  Was this expected or unexpected?
  Expected result: signal confirmed, standard post-match window
  Unexpected result (upset): recalibration required, larger signal shift
  Source: sports/{sport}/sport-domain-{sport}.md + result_impact_matrices
        │
        ▼
LAYER 2 — ATHLETE PERFORMANCE CHECK
  Did the key ATM (Athlete Token Multiplier) players perform?
  Standout performance → NCSI boost, APS re-evaluation trigger
  Absence confirmed (injury) → update athlete_modifier for next cycle
  Source: athlete/{sport}/athlete-intel-{sport}.md
        │
        ▼
LAYER 3 — FAN TOKEN COMMERCIAL IMPACT
  Run sentiment snapshot: has composite signal changed?
  Apply result modifier to LTUI trajectory
  Check on-chain: FTP settlement confirmed? (Path 2 tokens only)
  Source: fan-token/ stack + FanTokenPlayMonitor (if FTP active)
        │
        ▼
SOCIAL SIGNAL CHECK
  LunarCrush Galaxy Score: elevated (win) or declining (loss)?
  X/Twitter: what is the volume and tone from fans, journalists, club?
  Manager post-match press conference: any signals for next fixture?
  Source: platform/social-intelligence-connector.md + media-intelligence.md
        │
        ▼
PLAIN-ENGLISH BRIEF GENERATION
  Translate all layers into a human-readable fan brief (Prompt 21)
  Include: result summary, what it means for the token, what changed
  Include: FTP settlement status if applicable
  Include: what to watch for the next fixture
        │
        ▼
MEMORY MCP UPDATE
  Store: result, pre-match direction match/mismatch, FTP status
  Update: season supply position (FTP tokens)
  Flag: if unexpected result → submit calibration record
```

---

## The three time windows in detail

```
WINDOW 1 — T+0 to T+2h: SIGNAL CONFIRMATION
  Agent actions:
  □ Confirm result via Tier 1 source (BBC Sport, official league)
  □ Check: did result match pre-match SportMind direction?
    → Match: signal confirmed, note for calibration record
    → Mismatch: flag as calibration opportunity (wrong = valuable)
  □ Check macro: did crypto market move during the match?
  □ Note ATM player performance: goals, assists, standout moments
  □ FTP PATH 2: check chiliscan.com for settlement transaction
    → Win: look for burn to 0x0000...0000
    → Loss: look for re-mint to treasury wallet
  
  DO NOT generate new signal in this window.
  This is data collection, not signal generation.

WINDOW 2 — T+2h to T+24h: PRIMARY COMMERCIAL SIGNAL
  Agent actions:
  □ Run sportmind_sentiment_snapshot — has signal changed?
  □ Check LunarCrush Galaxy Score vs pre-match baseline
  □ Read manager post-match press conference for next-match signals
    → Injury confirmations / dismissals
    → Tactical hints for next fixture
    → Sentiment on player performances
  □ Generate post-match brief (plain English via Prompt 21)
  □ Update Memory MCP with result and FTP settlement status
  
  WIN result:
    Signal: 24-72h positive commercial window open
    FTP (Path 2): confirm burn tx on chiliscan; update season_net_burned_pct
    Brief tone: positive, note the supply reduction if FTP active
  
  LOSS result (expected):
    Signal: WAIT — CDI negative window, T+24h minimum before next entry
    FTP (Path 2): confirm re-mint to treasury; supply neutral, no punishment
    Brief tone: honest, note supply neutrality, point to next fixture
  
  LOSS result (unexpected — pre-match said HOME win):
    Signal: ABSTAIN — unexpected loss, full review before next position
    Flag: submit calibration record — unexpected losses most valuable
    Brief tone: transparent about what SportMind missed, what to watch next

WINDOW 3 — T+24h to T+72h: CONSOLIDATION AND NEXT CYCLE PREP
  Agent actions:
  □ Check: has sentiment stabilised post-result?
  □ Identify: when is the next fixture? Begin Pattern 2 pre-match prep
  □ Update season narrative: title race, relegation, cup progress
  □ FTP: confirm season supply position update in Memory MCP
  □ If transfer window open: did performance trigger APS re-evaluation?
```

---

## Real example: Arsenal 1-2 Bournemouth (11 April 2026)

```
PRE-MATCH SIGNAL:
  Direction expected: HOME (Arsenal at Emirates)
  Key flags active: lineup_unconfirmed (Gyökeres unexpected starter)
  Signal note: unexpected striker selection = lineup warning flag

T+0 CONFIRMATION:
  Result: HOME LOSS (1-2)
  ATM player check: Gyökeres scored (penalty) — unexpected contributor
  Macro: stable, no crypto move during match
  Classification: UNEXPECTED LOSS (pre-match expected HOME win)

T+2h COMMERCIAL SIGNAL:
  sentiment_snapshot: composite signal → WAIT
  Result modifier: UNEXPECTED_LOSS → -8-18% typical 24h window
  LunarCrush: Galaxy Score declining from pre-match baseline
  Calibration: FLAG — submit calibration record (unexpected result)

FAN TOKEN PLAY (PATH 2 — $AFC):
  Result: LOSS
  Settlement: re-mint to treasury (~0.25% supply) — supply NEUTRAL
  NOT a dilution event. Season net burned position: unchanged.
  Next match prep: FTP monitoring resets at T-48h next fixture.

MANAGER PRESS CONFERENCE SIGNALS:
  Listen for: Arteta on Gyökeres selection (injury to regular striker?)
  Listen for: any tactical acknowledgement re Bournemouth defensive block
  Listen for: next match squad news (any injury confirmations)

PLAIN-ENGLISH BRIEF (via Prompt 21):
  "Arsenal lost 1-2 to Bournemouth today at the Emirates. Viktor Gyökeres
  scored Arsenal's goal from the penalty spot, but Bournemouth defended
  well and took their chances when they came. For $AFC holders: this was
  a loss, but because Arsenal are on Fan Token Play, it means nothing
  changes to the token supply — it stays exactly as it was before the
  game. Losses don't punish. The signal now is WAIT — give it 24 hours
  before thinking about your position. The key thing to watch is whether
  Arsenal's regular striker was injured (which would explain the Gyökeres
  selection) and when the next fixture is."

MEMORY MCP UPDATE:
  result: "LOSS"
  pre_match_direction: "HOME"
  direction_match: false
  ftp_settlement: "NEUTRAL (re-mint confirmed)"
  calibration_flag: true
  next_action: "WAIT — T+24h minimum. Begin Pattern 2 at T-48h next fixture."
```

---

## Implementation

```python
"""
SportMind Agentic Workflow Pattern 11 — Post-Match Analysis Agent
Full post-match cycle: result → layers → commercial impact → plain-English brief.

Requirements: pip install aiohttp
Setup:
  1. Start MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Configure MATCH_CONFIG below after full-time
  3. Run: python post-match-agent.py

Output: technical JSON + plain-English brief
"""

import asyncio
import json
import logging
from datetime import datetime, timezone
from typing import Optional

log = logging.getLogger("sportmind.post-match")

SPORTMIND_MCP = "http://localhost:3001/mcp"

# ── Configure after full-time ─────────────────────────────────────────────
MATCH_CONFIG = {
    "home_team":        "Arsenal",
    "away_team":        "Bournemouth",
    "sport":            "football",
    "competition":      "Premier League",
    "result":           "AWAY_WIN",           # HOME_WIN | AWAY_WIN | DRAW
    "score":            "1-2",
    "token":            "AFC",                # fan token ticker
    "pre_match_direction": "HOME",            # what SportMind said pre-match
    "key_notes":        "Gyökeres unexpected starter. Bournemouth low-block.",
    "full_time_utc":    "2026-04-11T17:00:00Z",
}
# ── End configuration ─────────────────────────────────────────────────────


async def call_mcp(session, tool: str, args: dict) -> dict:
    import aiohttp
    payload = {
        "jsonrpc": "2.0",
        "method":  "tools/call",
        "params":  {"name": tool, "arguments": args},
        "id":      1,
    }
    async with session.post(SPORTMIND_MCP, json=payload) as resp:
        data    = await resp.json()
        content = data.get("result", {}).get("content", [{}])
        text    = content[0].get("text", "{}") if content else "{}"
        return json.loads(text)


def classify_result(config: dict) -> str:
    """Classify result as expected, unexpected, or draw."""
    result = config["result"]
    pre    = config["pre_match_direction"]

    if result == "DRAW":
        return "DRAW"
    if result == "HOME_WIN" and pre == "HOME":
        return "EXPECTED_WIN"
    if result == "AWAY_WIN" and pre == "AWAY":
        return "EXPECTED_WIN"
    if result == "HOME_WIN" and pre == "AWAY":
        return "UNEXPECTED_WIN"
    if result == "AWAY_WIN" and pre == "HOME":
        return "UNEXPECTED_LOSS"
    if (result in ("HOME_WIN", "AWAY_WIN")) and pre == "DRAW":
        return "EXPECTED_RESULT"
    return "LOSS"


def get_signal_recommendation(classification: str) -> dict:
    """Map result classification to post-match signal."""
    signals = {
        "EXPECTED_WIN": {
            "action":  "POSITIVE_WINDOW",
            "plain":   "Good result — 24-48h positive window. Check Galaxy Score.",
            "window":  "24-72h",
        },
        "UNEXPECTED_WIN": {
            "action":  "STRONG_POSITIVE_WINDOW",
            "plain":   "Surprise win — stronger and longer positive window than expected.",
            "window":  "48-96h",
        },
        "EXPECTED_RESULT": {
            "action":  "WAIT",
            "plain":   "Result as expected. Wait 24h for signal to stabilise.",
            "window":  "24h minimum",
        },
        "UNEXPECTED_LOSS": {
            "action":  "ABSTAIN",
            "plain":   "Unexpected loss. Full review before next position. Do not act yet.",
            "window":  "ABSTAIN until next fixture prep",
        },
        "DRAW": {
            "action":  "WAIT",
            "plain":   "Draw — neutral result. Signal depends on context (title race, etc.)",
            "window":  "24h",
        },
    }
    return signals.get(classification, {
        "action": "WAIT", "plain": "Review required.", "window": "24h"
    })


async def run_post_match(config: dict = MATCH_CONFIG):
    """Run full post-match analysis cycle."""
    import aiohttp

    classification = classify_result(config)
    signal         = get_signal_recommendation(classification)

    print(f"\n{'═'*58}")
    print(f"  POST-MATCH ANALYSIS — SportMind Pattern 11")
    print(f"  {config['home_team']} {config['score']} {config['away_team']}")
    print(f"  {config['competition']} · {config['full_time_utc'][:10]}")
    print(f"  Classification: {classification}")
    print(f"{'═'*58}\n")

    async with aiohttp.ClientSession() as session:

        # ── WINDOW 1: Signal confirmation ─────────────────────────────
        print("Window 1 — Signal confirmation (T+0)")

        macro = await call_mcp(session, "sportmind_macro", {})
        macro_mod = (macro.get("macro_state", {})
                          .get("crypto_cycle", {})
                          .get("macro_modifier", 1.00))
        macro_phase = (macro.get("macro_state", {})
                            .get("crypto_cycle", {})
                            .get("phase", "UNKNOWN"))
        print(f"  Macro: {macro_phase} ({macro_mod}) — {'stable' if macro_mod >= 0.85 else 'concern'}")

        direction_match = (
            (config["result"] == "HOME_WIN" and config["pre_match_direction"] == "HOME") or
            (config["result"] == "AWAY_WIN" and config["pre_match_direction"] == "AWAY") or
            (config["result"] == "DRAW" and config["pre_match_direction"] == "DRAW")
        )
        print(f"  Direction match: {direction_match} (pre-match: {config['pre_match_direction']}, result: {config['result']})")
        if not direction_match:
            print(f"  ⚑ CALIBRATION FLAG — submit calibration record (unexpected results are valuable)")

        # ── WINDOW 2: Commercial signal ───────────────────────────────
        print("\nWindow 2 — Commercial signal (T+2h)")

        lookup    = await call_mcp(session, "sportmind_fan_token_lookup",
                                   {"query": config["token"]})
        sentiment = await call_mcp(session, "sportmind_sentiment_snapshot",
                                   {"token": config["token"],
                                    "use_case": "fan_token_tier1"})

        # Check Fan Token Play status
        token_data   = lookup.get("tokens", [{}])[0] if lookup.get("found") else {}
        ftp_status   = token_data.get("fan_token_play", {})
        ftp_active   = bool(ftp_status)
        supply_mech  = (sentiment.get("sentiment_snapshot", {})
                                 .get("supply_mechanics", {}))
        ftp_confirmed = supply_mech.get("status") == "GAMIFIED_CONFIRMED"

        print(f"  Token: {token_data.get('name', config['token'])}")
        print(f"  Signal: {signal['action']}")
        print(f"  Window: {signal['window']}")

        if ftp_active or ftp_confirmed:
            ftp_result = "NEUTRAL — pre-liquidated amount restored to treasury only" \
                if config["result"] in ("AWAY_WIN",) and config["home_team"] == "Arsenal" \
                else "SUPPLY_REDUCED — burn transaction expected on chiliscan.com" \
                if config["result"] == "HOME_WIN" and config["home_team"] == "Arsenal" \
                else "Check FTP status"
            print(f"  FTP ({ftp_status.get('path', 'PATH_2')}): {ftp_result}")
            print(f"  → Verify: chiliscan.com/token/0x1d43... (treasury wallet activity)")

        # ── Social signal layer ───────────────────────────────────────
        print("\n  Social signal layer:")
        print(f"  Load: platform/social-intelligence-connector.md")
        print(f"  Check LunarCrush Galaxy Score vs pre-match baseline")
        print(f"  Monitor: @{config['home_team'].replace(' ','')} official account")
        print(f"  Watch: manager post-match press conference (media-intelligence.md)")

        # ── Plain-English brief ───────────────────────────────────────
        print(f"\nPlain-English brief (Prompt 21 output):")
        print(f"{'─'*56}")

        # Build the brief using the signal and context
        home  = config["home_team"]
        away  = config["away_team"]
        score = config["score"]
        token = config["token"]
        comp  = config["competition"]

        if classification == "UNEXPECTED_LOSS":
            brief = f"""{home} lost {score} to {away} today in the {comp}.

The result was a surprise — SportMind\'s pre-match signal pointed toward
a {home} win. These are the results worth paying attention to because they
tell us something we didn\'t know before the match. In this case, the
unexpected striker selection (lineup warning flag pre-match) materialised
as a real problem.

For ${token} holders: the signal now is WAIT. Give it at least 24 hours
before thinking about your position. An unexpected loss creates a
negative sentiment window that typically lasts 24-48 hours.

{"⚡ Fan Token Play: Arsenal are on Path 2. A LOSS means the pre-match supply adjustment is reversed — supply goes back to where it was before the game. No dilution, no punishment. The season supply position is unchanged." if ftp_active or ftp_confirmed else ""}

What to watch: Mikel Arteta\'s post-match press conference — specifically
whether he confirms the striker situation and who is available for the
next match. That will set up the next pre-match brief.

Calibration note: This result will be added to SportMind\'s record as an
incorrect prediction. Wrong predictions are as valuable as correct ones —
they improve the model."""
        elif classification == "EXPECTED_WIN":
            brief = f"""{home} won {score} vs {away} today. A positive result that
matches what SportMind expected pre-match.

For ${token} holders: a 24-48 hour positive commercial window is now
open. Galaxy Score should be elevated. This is a reasonable time to
review your position — but check the macro first (it\'s neutral today,
which is stable).

{"⚡ Fan Token Play: A win means a small permanent reduction in $AFC supply — the burn transaction should appear on chiliscan.com within 48 hours. Wins compound over the season." if ftp_active or ftp_confirmed else ""}

One thing to watch: the next fixture and when it is. The positive window
is real but it does not last indefinitely."""
        else:
            brief = f"""{home} {score} {away} in the {comp}.
Result classification: {classification}. Signal: {signal["plain"]}
Load Prompt 21 for the full plain-English brief based on this result."""

        print(brief)
        print(f"{'─'*56}")

        # ── Memory MCP update ─────────────────────────────────────────
        print(f"\nMemory MCP update:")
        memory_update = {
            "result":                config["result"],
            "score":                 config["score"],
            "pre_match_direction":   config["pre_match_direction"],
            "direction_match":       direction_match,
            "classification":        classification,
            "post_match_signal":     signal["action"],
            "ftp_settlement":        "NEUTRAL" if not direction_match else "CHECK_CHILISCAN",
            "calibration_flag":      not direction_match,
            "macro_at_fulltime":     macro_mod,
            "next_action":           f"WAIT {signal['window']}. Begin Pattern 2 at T-48h next fixture.",
            "updated_at":            datetime.now(timezone.utc).isoformat(),
        }
        print(json.dumps(memory_update, indent=2))

        return memory_update


if __name__ == "__main__":
    asyncio.run(run_post_match())
```

---

## The layers that connect post-match intelligence

```
LAYER 5 — Macro (always first)
  macro/macro-overview.md
  macro/macro-crypto-market-cycles.md
  → Did macro shift during the match? Crypto is live 24/7.

LAYER 1 — Sporting result
  sports/{sport}/sport-domain-{sport}.md
  core/core-result-impact-matrices.md
  → Was the result expected or unexpected?
  → What is the competition context? (title race, relegation, cup)

LAYER 2 — Athlete performance
  athlete/{sport}/athlete-intel-{sport}.md
  → Did the ATM player perform? (affects next cycle NCSI)
  → Any injury confirmed post-match? (update modifier)

LAYER 3 — Commercial + FTP
  fan-token/{sport}-token-intelligence/
  fan-token/gamified-tokenomics-intelligence/ (if FTP active)
  platform/chiliz-chain-address-intelligence.md (FanTokenPlayMonitor)
  → Apply result modifier to LTUI trajectory
  → Confirm FTP settlement on-chain

SOCIAL + MEDIA LAYER
  platform/social-intelligence-connector.md (LunarCrush Galaxy Score)
  core/media-intelligence.md (press conference signals)
  core/breaking-news-intelligence.md (any post-match news)
  → Is social sentiment following the expected pattern?
  → What is the manager signalling for the next fixture?

OUTPUT LAYER
  core/post-match-signal-framework.md (technical)
  agent-prompts/agent-prompts.md Prompt 21 (plain English)
  platform/memory-integration.md (Memory MCP update)
```

---

## Connection to other patterns

```
RECEIVES FROM:
  Pattern 2 (Pre-Match Chain)   — what the pre-match signal was
  Pattern 8 (FTP Monitor)       — FTP pre-liquidation and settlement status
  Pattern 1 (Portfolio Monitor) — token in portfolio, needs post-match update

FEEDS INTO:
  Pattern 2 (Pre-Match Chain)   — next fixture begins at T-48h
  Pattern 9 (Governance Delegate) — post-match performance triggers governance vote?
  Pattern 10 (Scouting Agent)   — breakout performance → APS re-evaluation

CALIBRATION:
  Unexpected results → submit calibration record
  community/calibration-data/{sport}/{year}/{month}/
  Wrong predictions are the most valuable calibration records.
```

---

*SportMind v3.48 · MIT License · sportmind.dev*
*See: core/post-match-signal-framework.md · agent-prompts/agent-prompts.md Prompt 21*
*platform/social-intelligence-connector.md · fan-token/gamified-tokenomics-intelligence/*
