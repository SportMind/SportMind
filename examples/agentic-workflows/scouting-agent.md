# Agentic Workflow Pattern 10 — Moneyball Scouting Agent

**Purpose:** Systematically evaluates a list of transfer targets using
SportMind's five-tier commercial scouting stack, ranks candidates by
commercial value-to-transfer-fee ratio, and produces comparative scout
reports for sporting directors and transfer committees.

**Trigger:** Manual (new transfer window opens or target list changes)
**Cycle:** On-demand + weekly refresh during transfer windows
**Autonomy:** Level 1 (runs analysis autonomously; human decides on targets)
**Primary user:** Club sporting directors, transfer committees, sports agents

**What makes this "Moneyball":** Traditional scouting finds the best player
on the pitch. This pattern finds the best commercial value — the player whose
APS, AELS, DTS, and LTUI impact is highest relative to their transfer fee.
A €20M player with APS 0.80 may deliver more commercial value to a fan token
ecosystem than a €60M player with APS 0.45.

---

## What this pattern does that Pattern 6 does not

Pattern 6 (Athlete Commercial Tracker) monitors athletes already in your
portfolio — tracking their APS/AELS/SHS over time to detect commercial
trajectory changes.

Pattern 10 evaluates candidates you do not yet have — comparing multiple
targets against each other and ranking them by commercial value-to-fee ratio.
The output is a ranked comparison table, not a monitoring feed.

---

## The five commercial scouting tiers

```
TIER 1 — On-Pitch Foundation (is this player good enough?)
  PI (Performance Index)
    → Position-weighted composite from available statistics
    → Age-adjusted benchmark: is this player top 20% for position?
    → Without sufficient PI, commercial value cannot be sustained long-term

TIER 2 — Career Trajectory (will they still be good in 18 months?)
  DTS (Development Trajectory Score)
    → Is the player improving, plateauing, or declining?
    → 0.80+ = improving → commercial window is opening
    → 0.50-0.79 = stable → commercial window is open now
    → < 0.50 = declining → commercial window is closing
  
  TAI (Training Adaptation Index)
    → Physical reliability and injury pattern
    → A highly portable player who misses 40% of games provides 60% of value

TIER 3 — Social and Commercial Presence (do they move the market?)
  AELS (Athlete Engagement Lift Score)
    → Does this player's activity lift fan token engagement?
    → The key question: will our token holders care about this signing?
    → AELS > 0.65: strong engagement signal — signing will move the token
    → AELS < 0.40: weak signal — signing may be commercially neutral
  
  SHS (Social Health Score)
    → Quality and consistency of social presence
    → A high-SHS player amplifies every commercial moment
    → A low-SHS player has high volatility commercial exposure

TIER 4 — Transfer-Specific (does the value actually transfer?)
  APS (Athlete Portability Score)
    → How much of their current commercial value travels with them?
    → The most important single metric for this pattern
    → High APS = their audience follows them; value is in the player
    → Low APS = their audience belongs to their current club; value stays behind
  
  TVS (Transfer Viability Score)
    → Is this transfer actually achievable?
    → Financial fit, contract situation, club willingness

TIER 5 — Token Ecosystem Impact (what does this do to the token?)
  LTUI (Lifetime Token Utility Index)
    → What does this signing do to our token's long-term commercial trajectory?
    → The strategic metric: not "is this player good" but "is this signing good
       for our token ecosystem"
  
  ABS (Athlete Brand Score)
    → Composite commercial value: sponsorship attractiveness, media coverage,
       brand partnership potential
```

---

## The commercial value-to-fee ratio

```
COMMERCIAL_VALUE_SCORE = (APS × 0.30)
                       + (AELS × 0.25)
                       + (DTS × 0.20)
                       + (PI_percentile × 0.15)
                       + (LTUI_projection_normalised × 0.10)

FEE_ADJUSTED_SCORE = COMMERCIAL_VALUE_SCORE / log10(transfer_fee_millions + 1)

Interpretation:
  FEE_ADJUSTED_SCORE > 0.25: EXCELLENT commercial value for fee
  0.15–0.25:                 GOOD — worth pursuing
  0.08–0.14:                 MODERATE — consider lower fee or different target
  < 0.08:                    POOR — fee exceeds commercial value delivery

Examples:
  Player A: APS 0.78, AELS 0.72, DTS 0.85, PI 80th pct, fee €22M
    → CVS = 0.234 + 0.180 + 0.170 + 0.120 + 0.080 = 0.784
    → FAS = 0.784 / log10(23) ≈ 0.784 / 1.36 = 0.576 → EXCELLENT
  
  Player B: APS 0.44, AELS 0.38, DTS 0.62, PI 85th pct, fee €65M
    → CVS = 0.132 + 0.095 + 0.124 + 0.128 + 0.060 = 0.539
    → FAS = 0.539 / log10(66) ≈ 0.539 / 1.82 = 0.296 → GOOD
    (Player B is better on pitch but worse commercial value per euro)
```

---

## Scout report output format

```json
{
  "scouting_report": {
    "generated_at":  "2026-08-01T09:00:00Z",
    "club_token":    "AFC",
    "window":        "summer-2026",
    "targets_evaluated": 4
  },

  "ranking": [
    {
      "rank": 1,
      "player": "Target A",
      "transfer_fee_estimate_m": 22,
      "commercial_value_score": 0.784,
      "fee_adjusted_score": 0.576,
      "tier": "EXCELLENT",
      "headline": "High APS + AELS — commercial value transfers strongly. Fee justified.",
      "metrics": {
        "APS":  {"score": 0.78, "note": "78% of commercial signal travels with player"},
        "AELS": {"score": 0.72, "note": "Signing will lift $AFC token engagement"},
        "DTS":  {"score": 0.85, "note": "Career trajectory still improving"},
        "PI":   {"percentile": 80, "note": "Top 20% for position"},
        "LTUI_projection": "+7 to +10 points over 24 months"
      },
      "recommendation": "PURSUE — best commercial return in this target list"
    },
    {
      "rank": 2,
      "player": "Target B",
      "transfer_fee_estimate_m": 65,
      "commercial_value_score": 0.539,
      "fee_adjusted_score": 0.296,
      "tier": "GOOD",
      "headline": "Strong on pitch but low APS — commercial value belongs to current club.",
      "metrics": {
        "APS":  {"score": 0.44, "note": "56% of audience stays with current club"},
        "AELS": {"score": 0.38, "note": "Modest token engagement lift"},
        "DTS":  {"score": 0.62, "note": "Career stable, not improving"},
        "PI":   {"percentile": 85, "note": "Top 15% for position"},
        "LTUI_projection": "+3 to +5 points over 24 months"
      },
      "recommendation": "CONDITIONAL — strong on pitch but fee exceeds commercial value. Negotiate lower or prioritise Target A."
    }
  ],

  "sportmind_version": "3.47.0"
}
```

---

## Implementation

```python
"""
SportMind Agentic Workflow Pattern 10 — Moneyball Scouting Agent
Evaluates transfer targets by commercial value-to-fee ratio.

Requirements: pip install aiohttp
Setup:
  1. Start MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Define your TARGET_LIST below with fee estimates
  3. Run: python scouting-agent.py

Output: ranked scout report JSON to stdout or file
"""

import asyncio
import json
import math
import logging
from datetime import datetime, timezone

log = logging.getLogger("sportmind.scouting-agent")

SPORTMIND_MCP = "http://localhost:3001/mcp"

# ── Configure your target list ─────────────────────────────────────────────
CLUB_TOKEN = "AFC"  # The buying club's fan token
SPORT      = "football"

TARGET_LIST = [
    # Each target: name, estimated fee (€M), and any known context
    {"name": "Target A", "fee_m": 22, "context": "Left winger, La Liga"},
    {"name": "Target B", "fee_m": 65, "context": "Striker, Premier League"},
    {"name": "Target C", "fee_m": 38, "context": "Central midfielder, Bundesliga"},
    {"name": "Target D", "fee_m": 15, "context": "Right back, Serie A"},
]
# ── End configuration ──────────────────────────────────────────────────────


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


def compute_commercial_value_score(metrics: dict) -> float:
    """
    Compute composite commercial value score from scouting metrics.
    Returns 0.0–1.0. Requires: APS, AELS, DTS, PI_percentile (0-1), LTUI_norm.
    """
    aps   = metrics.get("APS", 0.5)
    aels  = metrics.get("AELS", 0.5)
    dts   = metrics.get("DTS", 0.5)
    pi    = metrics.get("PI_percentile", 0.5)   # normalised 0-1
    ltui  = metrics.get("LTUI_norm", 0.5)        # normalised 0-1

    return (aps * 0.30) + (aels * 0.25) + (dts * 0.20) + (pi * 0.15) + (ltui * 0.10)


def compute_fee_adjusted_score(cvs: float, fee_m: float) -> float:
    """Adjust commercial value score by transfer fee."""
    if fee_m <= 0:
        return cvs
    return cvs / math.log10(fee_m + 1)


def tier_from_fas(fas: float) -> str:
    if fas >= 0.25:
        return "EXCELLENT"
    elif fas >= 0.15:
        return "GOOD"
    elif fas >= 0.08:
        return "MODERATE"
    else:
        return "POOR"


async def scout_target(session, target: dict, club_token: str, sport: str) -> dict:
    """
    Run commercial scouting analysis for a single target.
    
    In a full implementation this would load:
      - fan-token/transfer-signal/ for APS/TVS
      - fan-token/athlete-social-lift/ for AELS
      - fan-token/brand-score/ for ABS
      - core/athlete-financial-intelligence.md for wage/contract context
    
    Here we demonstrate the framework with the MCP tools available.
    """
    # Get club token context
    club_context = await call_mcp(session, "sportmind_sentiment_snapshot",
                                   {"token": club_token,
                                    "use_case": "fan_token_tier1"})

    # Get macro context
    macro = await call_mcp(session, "sportmind_macro", {})
    macro_mod = (macro.get("macro_state", {})
                      .get("crypto_cycle", {})
                      .get("macro_modifier", 1.00))

    # Build skill loading instruction
    skill_stack = [
        f"sports/{sport}/sport-domain-{sport}.md",
        "fan-token/transfer-signal/",
        "fan-token/athlete-social-lift/",
        "fan-token/brand-score/",
        "fan-token/performance-on-pitch/",
        "core/athlete-financial-intelligence.md",
        "fan-token/fan-token-lifecycle/",
    ]

    return {
        "target":         target["name"],
        "transfer_fee_m": target["fee_m"],
        "context":        target.get("context", ""),
        "macro_modifier": macro_mod,
        "skill_stack":    skill_stack,
        "club_token":     club_token,
        "instruction": (
            f"Load skill stack above to calculate APS, AELS, DTS, PI, LTUI for {target['name']}. "
            f"Apply commercial_value_score formula. Adjust for fee €{target['fee_m']}M. "
            f"Compare against other targets in this list."
        ),
        "club_context": club_context.get("sentiment_snapshot", {}),
    }


async def run_scouting_session(
    targets: list = TARGET_LIST,
    club_token: str = CLUB_TOKEN,
    sport: str = SPORT,
) -> dict:
    """Run full scouting analysis across all targets and produce ranked report."""
    import aiohttp

    print(f"\nSportMind Scouting Agent")
    print(f"  Club token:  {club_token}")
    print(f"  Targets:     {len(targets)}")
    print(f"  Window:      {datetime.now(timezone.utc).strftime('%B %Y')}")
    print(f"{'─'*50}\n")

    results = []

    async with aiohttp.ClientSession() as session:
        for target in targets:
            print(f"  Scouting: {target['name']} (€{target['fee_m']}M)...")
            analysis = await scout_target(session, target, club_token, sport)
            results.append(analysis)
            await asyncio.sleep(0.3)

    # Produce ranked report structure
    report = {
        "scouting_report": {
            "generated_at":       datetime.now(timezone.utc).isoformat(),
            "club_token":         club_token,
            "sport":              sport,
            "targets_evaluated":  len(targets),
            "instruction": (
                "Run each target through the skill stack provided. "
                "Compute commercial_value_score and fee_adjusted_score per target. "
                "Rank targets by fee_adjusted_score descending. "
                "See: examples/agentic-workflows/governance-delegate-agent.md "
                "and app-09-talent-scouting.md for full metric framework."
            ),
        },
        "targets":           results,
        "ranking_formula": {
            "commercial_value_score": "APS×0.30 + AELS×0.25 + DTS×0.20 + PI_pct×0.15 + LTUI_norm×0.10",
            "fee_adjusted_score":     "CVS / log10(fee_m + 1)",
            "tier_thresholds": {
                "EXCELLENT": ">= 0.25",
                "GOOD":      "0.15-0.25",
                "MODERATE":  "0.08-0.15",
                "POOR":      "< 0.08",
            },
        },
        "sportmind_version": "3.47.0",
    }

    print(f"\n  Analysis complete — {len(targets)} targets evaluated")
    print(f"  Load each target's skill stack to calculate final rankings.")
    print(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    asyncio.run(run_scouting_session())
```

---

## When to use this pattern vs Pattern 6

```
PATTERN 6 — Athlete Commercial Tracker:
  USE WHEN: monitoring athletes already in your portfolio
  TRIGGER:  scheduled 12h cycle
  OUTPUT:   trajectory alerts (APS declining, AELS spike, DSM flag)
  QUESTION: "how is our existing roster performing commercially?"

PATTERN 10 — Moneyball Scouting Agent:
  USE WHEN: evaluating new transfer targets before committing
  TRIGGER:  on-demand at start of transfer window
  OUTPUT:   ranked comparison table by commercial value-to-fee
  QUESTION: "which candidate gives us the best commercial return?"

COMBINED:
  Run Pattern 10 at window open to identify targets.
  Add chosen player to Pattern 6 monitoring post-signing.
```

---

## Connection to other SportMind skills

```
FEEDS FROM:
  app-09-talent-scouting.md                     — full blueprint
  fan-token/transfer-signal/                    — APS, TVS, TSI
  fan-token/athlete-social-lift/                — AELS
  fan-token/brand-score/                        — ABS
  fan-token/performance-on-pitch/               — PI
  core/athlete-financial-intelligence.md        — wage/contract context
  fan-token/fan-token-lifecycle/                — LTUI projection

FEEDS INTO:
  Pattern 9 (Governance Delegate)               — winning target → governance vote
  Pattern 6 (Athlete Commercial Tracker)        — signed player → ongoing monitoring
  platform/memory-integration.md               — store scouting session results
```

---

*SportMind v3.47 · MIT License · sportmind.dev*
*See also: app-09-talent-scouting.md · fan-token/transfer-signal/*
*core/athlete-financial-intelligence.md · examples/agentic-workflows/README.md*
