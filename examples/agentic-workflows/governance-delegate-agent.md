# Agentic Workflow Pattern 9 — Smart Governance Delegate

**Purpose:** Monitors active and upcoming fan token governance proposals,
analyses each one using the full SportMind commercial intelligence stack,
and delivers a structured recommendation brief before the vote closes —
so token holders and delegates can vote with full commercial context.

**Trigger:** New governance proposal detected OR scheduled 12h check
**Cycle:** 12h monitoring; immediate alert on new proposal within 72h of close
**Autonomy:** Level 2 (recommendations autonomously; holder decides how to vote)
**Scope:** Any fan token with active Socios or on-chain governance

**Critical principle:** This agent produces intelligence, not votes.
Execution — submitting an on-chain vote — belongs to the application layer.
The agent's output is always a structured recommendation brief, never a
transaction. Developers decide how to wire the execution.

---

## Why governance needs its own agent

The pre-match chain (Pattern 2) and portfolio monitor (Pattern 1) focus on
sporting events and price signals. Neither monitors governance.

A governance vote is a different kind of event entirely:
- It has a hard deadline (vote closes at a specific time)
- It requires commercial intelligence, not sporting intelligence
- Its impact on the token is structural, not temporary
- A wrong vote cannot be undone after the window closes

A token holder who votes to approve a low-PHS commercial partnership without
knowing the LTUI implications has made a permanent structural error. The
governance delegate exists to prevent that.

---

## The three vote categories SportMind analyses

```
CATEGORY 1 — PLAYER SIGNING / TRANSFER VOTES
  "Should we sign [Player] for €[Fee]?"
  
  Intelligence required:
    APS  — how much of their commercial value transfers to us?
    AELS — does this player move our token holders?
    ABS  — what is their composite commercial brand value?
    PI   — on-pitch justification (performance index)
    DTS  — are they improving or declining?
    LTUI — what does this signing do to our token's lifetime utility?
  
  Recommendation frame:
    VOTE YES if: APS > 0.65, AELS > 0.60, LTUI positive, fee-to-value justified
    ABSTAIN if: APS uncertain, incomplete data, vote too close to call
    VOTE NO if: APS < 0.40, negative LTUI projection, fee-to-value poor
    
  Skill stack: fan-token/transfer-signal/ · fan-token/athlete-social-lift/
               fan-token/brand-score/ · fan-token/fan-token-lifecycle/
               core/athlete-financial-intelligence.md


CATEGORY 2 — COMMERCIAL PARTNERSHIP VOTES
  "Should we partner with [Brand] as [Sponsor category]?"
  
  Intelligence required:
    PHS  — Partnership Health Score: will this partnership be maintained?
    AFS  — Audience Fit Score: does the brand's audience match our holders?
    LTUI — does this extend or reduce token lifetime utility?
    GSI  — what does this vote's weight say about our governance quality?
  
  Recommendation frame:
    VOTE YES if: PHS > 0.70, AFS > 0.65, LTUI positive
    ABSTAIN if: brand is in a volatile sector, PHS uncertain
    VOTE NO if: brand alignment poor, LTUI negative, PHS < 0.50
  
  Skill stack: fan-token/fan-token-partnership-intelligence/
               fan-token/sports-brand-sponsorship/
               fan-token/sponsorship-match/
               fan-token/fan-token-lifecycle/


CATEGORY 3 — OPERATIONAL / COSMETIC VOTES
  "Which kit design?" / "Which charity?" / "Which stadium section name?"
  
  Intelligence required:
    GSI  — Decision_Weight assessment (is this governance or theatre?)
    Phase — what does the token's current lifecycle phase need?
    SHS  — will holders share and engage with this outcome?
  
  Recommendation frame:
    If GSI Decision_Weight < 0.30 (cosmetic): note governance theatre risk
    Vote on personal preference — SportMind has no commercial edge here
    Flag if: engagement opportunity worth maximising regardless of outcome
  
  Skill stack: fan-token/fan-token-lifecycle/
               fan-token/sports-governance-intelligence/
               fan-token/athlete-social-activity/ (if athlete-related)
```

---

## Governance brief output format

```json
{
  "governance_brief": {
    "token":          "AFC",
    "proposal_id":    "afc-gov-2026-047",
    "proposal_title": "Approve signing of [Player] for €45M",
    "category":       "PLAYER_SIGNING",
    "vote_closes":    "2026-08-15T23:59:00Z",
    "hours_remaining": 36,
    "generated_at":   "2026-08-14T11:00:00Z"
  },

  "commercial_assessment": {
    "APS":  {"score": 0.74, "tier": "HIGH",   "note": "74% of commercial signal transfers"},
    "AELS": {"score": 0.68, "tier": "GOOD",   "note": "This player lifts $AFC engagement"},
    "ABS":  {"score": 79,   "tier": "STRONG", "note": "Top quartile commercial brand"},
    "PI":   {"score": 77.3, "tier": "GOOD",   "note": "Top 22% for position this season"},
    "DTS":  {"score": 0.82, "tier": "IMPROVING", "note": "Career trajectory still upward"},
    "LTUI_projection": {
      "direction": "POSITIVE",
      "magnitude": "+6 to +9 LTUI points over 24-month window",
      "note": "High-APS, high-AELS signing in Phase 3 — utility extension confirmed"
    }
  },

  "recommendation": {
    "action":      "VOTE_YES",
    "confidence":  "HIGH",
    "sms":         81,
    "primary_reason": "APS 0.74 + AELS 0.68 confirms commercial value transfers. LTUI positive.",
    "risk_flags":  [],
    "abstain_if":  "Fee confirmed above €52M — recalculate fee-to-APS ratio"
  },

  "governance_context": {
    "GSI_decision_weight": 0.65,
    "vote_type": "COMPETITIVE",
    "governance_quality": "MEANINGFUL — above cosmetic threshold",
    "ltui_impact_category": "STRUCTURAL"
  },

  "skill_stack_used": [
    "fan-token/transfer-signal/",
    "fan-token/athlete-social-lift/",
    "fan-token/brand-score/",
    "fan-token/fan-token-lifecycle/",
    "core/athlete-financial-intelligence.md"
  ],

  "sportmind_version": "3.47.0"
}
```

---

## Implementation

```python
"""
SportMind Agentic Workflow Pattern 9 — Smart Governance Delegate
Monitors governance proposals and delivers commercial intelligence briefs.

Requirements: pip install aiohttp schedule
Setup:
  1. Start MCP server: python scripts/sportmind_mcp.py --http --port 3001
  2. Configure WATCHED_TOKENS below
  3. Implement fetch_active_proposals() for your governance source
     (Socios API, on-chain query, or manual feed)
  4. Run: python governance-delegate.py

Output: governance briefs to stdout, webhook, or Memory MCP
"""

import asyncio
import json
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional

log = logging.getLogger("sportmind.governance-delegate")

SPORTMIND_MCP = "http://localhost:3001/mcp"

# Tokens to monitor for governance activity
WATCHED_TOKENS = [
    "AFC",   # Arsenal FC — PATH_2 confirmed
    "PSG",
    "BAR",
    "CITY",
    "JUV",
]

# Alert when vote closes within this many hours
ALERT_WINDOW_HOURS = 72
MONITOR_CYCLE_HOURS = 12


# ── Vote category classifier ───────────────────────────────────────────────

def classify_proposal(title: str, description: str) -> str:
    """Classify a governance proposal into one of three categories."""
    text = (title + " " + description).lower()

    signing_keywords = [
        "sign", "signing", "transfer", "acquire", "purchase", "player",
        "loan", "permanent", "fee", "contract"
    ]
    partnership_keywords = [
        "partner", "partnership", "sponsor", "sponsorship", "brand",
        "commercial", "deal", "agreement", "kit", "naming rights"
    ]

    signing_score    = sum(1 for kw in signing_keywords if kw in text)
    partnership_score = sum(1 for kw in partnership_keywords if kw in text)

    if signing_score >= 2:
        return "PLAYER_SIGNING"
    elif partnership_score >= 2:
        return "COMMERCIAL_PARTNERSHIP"
    else:
        return "OPERATIONAL_COSMETIC"


# ── SportMind MCP caller ───────────────────────────────────────────────────

async def call_mcp(session, tool: str, args: dict) -> dict:
    """Call a SportMind MCP tool."""
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


# ── Governance analysis per category ──────────────────────────────────────

async def analyse_player_signing(session, token: str, proposal: dict) -> dict:
    """
    Run the full player signing commercial stack.
    Returns structured commercial assessment.
    """
    # 1. Get token context
    lookup    = await call_mcp(session, "sportmind_fan_token_lookup",
                                {"query": token})
    sentiment = await call_mcp(session, "sportmind_sentiment_snapshot",
                                {"token": token, "use_case": "fan_token_tier1"})

    # 2. Get lifecycle phase
    snap       = sentiment.get("sentiment_snapshot", {})
    fan_sent   = snap.get("fan_sentiment", {})
    lifecycle  = snap.get("commercial_sentiment", {})

    # 3. Build assessment (agents load APS/AELS/ABS/DTS skills for full calc)
    # These are the skill references — actual calculation requires loading the skills
    skill_stack = [
        "fan-token/transfer-signal/",
        "fan-token/athlete-social-lift/",
        "fan-token/brand-score/",
        "fan-token/fan-token-lifecycle/",
        "core/athlete-financial-intelligence.md",
    ]

    return {
        "category":          "PLAYER_SIGNING",
        "token_context":     lookup.get("tokens", [{}])[0] if lookup.get("found") else {},
        "lifecycle_signal":  fan_sent,
        "commercial_signal": lifecycle,
        "skill_stack":       skill_stack,
        "instruction": (
            "Load skill stack above to calculate APS, AELS, ABS, DTS, LTUI. "
            "Apply VOTE_YES if APS > 0.65 and LTUI_projection positive. "
            "See fan-token/sports-governance-intelligence/ for full framework."
        ),
    }


async def analyse_commercial_partnership(session, token: str, proposal: dict) -> dict:
    """Run the partnership intelligence stack."""
    sentiment = await call_mcp(session, "sportmind_sentiment_snapshot",
                                {"token": token, "use_case": "fan_token_tier1"})
    snap = sentiment.get("sentiment_snapshot", {})

    skill_stack = [
        "fan-token/fan-token-partnership-intelligence/",
        "fan-token/sports-brand-sponsorship/",
        "fan-token/sponsorship-match/",
        "fan-token/fan-token-lifecycle/",
    ]

    return {
        "category":          "COMMERCIAL_PARTNERSHIP",
        "commercial_signal": snap.get("commercial_sentiment", {}),
        "skill_stack":       skill_stack,
        "instruction": (
            "Load skill stack above to calculate PHS, AFS, LTUI. "
            "Apply VOTE_YES if PHS > 0.70 and AFS > 0.65. "
            "See fan-token/sports-governance-intelligence/ for full framework."
        ),
    }


async def analyse_operational(session, token: str, proposal: dict) -> dict:
    """Assess operational/cosmetic vote — governance quality signal."""
    return {
        "category":    "OPERATIONAL_COSMETIC",
        "note": (
            "Cosmetic vote — GSI Decision_Weight < 0.30. "
            "SportMind has no commercial edge on this vote type. "
            "If participation is high: governance engagement signal — LTUI neutral positive. "
            "If participation is low: governance theatre risk — monitor GSI."
        ),
        "skill_stack": [
            "fan-token/fan-token-lifecycle/",
            "fan-token/sports-governance-intelligence/",
        ],
    }


# ── Main governance delegate cycle ────────────────────────────────────────

async def analyse_proposal(session, token: str, proposal: dict) -> dict:
    """
    Full governance proposal analysis — classify, analyse, generate brief.
    
    proposal dict must contain:
      id:          unique proposal identifier
      title:       proposal title
      description: full proposal text
      closes_at:   ISO datetime when vote closes
    """
    closes_at   = datetime.fromisoformat(proposal["closes_at"].replace("Z", "+00:00"))
    now         = datetime.now(timezone.utc)
    hours_left  = (closes_at - now).total_seconds() / 3600

    if hours_left < 0:
        return {"status": "EXPIRED", "proposal_id": proposal["id"]}

    category = classify_proposal(proposal["title"], proposal.get("description", ""))

    if category == "PLAYER_SIGNING":
        assessment = await analyse_player_signing(session, token, proposal)
    elif category == "COMMERCIAL_PARTNERSHIP":
        assessment = await analyse_commercial_partnership(session, token, proposal)
    else:
        assessment = await analyse_operational(session, token, proposal)

    # Macro check — always run first
    macro = await call_mcp(session, "sportmind_macro", {})
    macro_mod = (macro.get("macro_state", {})
                      .get("crypto_cycle", {})
                      .get("macro_modifier", 1.00))

    brief = {
        "governance_brief": {
            "token":           token,
            "proposal_id":     proposal["id"],
            "proposal_title":  proposal["title"],
            "category":        category,
            "vote_closes":     proposal["closes_at"],
            "hours_remaining": round(hours_left, 1),
            "generated_at":    now.isoformat(),
        },
        "macro_context": {
            "modifier": macro_mod,
            "note": "Macro gate check — high bear market reduces urgency of all commercial signals",
        },
        "assessment":       assessment,
        "alert_priority":   "HIGH" if hours_left <= 24 else (
                            "MEDIUM" if hours_left <= 72 else "LOW"),
        "sportmind_version": "3.47.0",
    }

    return brief


async def governance_delegate_cycle(tokens: list = WATCHED_TOKENS):
    """
    Main monitoring cycle. Checks all watched tokens for active proposals.
    Replace fetch_active_proposals() with your governance data source.
    """
    import aiohttp

    async with aiohttp.ClientSession() as session:
        for token in tokens:
            proposals = await fetch_active_proposals(token)
            for proposal in proposals:
                closes_at = datetime.fromisoformat(
                    proposal["closes_at"].replace("Z", "+00:00")
                )
                hours_left = (closes_at - datetime.now(timezone.utc)).total_seconds() / 3600

                if hours_left <= ALERT_WINDOW_HOURS:
                    brief = await analyse_proposal(session, token, proposal)
                    print(f"\n{'═'*60}")
                    print(f"GOVERNANCE BRIEF — {token}")
                    print(json.dumps(brief, indent=2, default=str))


async def fetch_active_proposals(token: str) -> list:
    """
    Fetch active governance proposals for a token.
    
    IMPLEMENT THIS for your governance source:
      - Socios API: GET /api/governance/proposals?token={symbol}
      - On-chain: query governance contract for active proposal IDs
      - Manual feed: read from a local JSON file or database
    
    Must return list of dicts with: id, title, description, closes_at
    """
    # Example structure — replace with real data source
    return []  # pragma: no cover


if __name__ == "__main__":
    import schedule, time

    # Run immediately, then every 12 hours
    asyncio.run(governance_delegate_cycle())

    schedule.every(MONITOR_CYCLE_HOURS).hours.do(
        lambda: asyncio.run(governance_delegate_cycle())
    )

    log.info("Governance delegate running — monitoring %d tokens", len(WATCHED_TOKENS))
    while True:
        schedule.run_pending()
        time.sleep(60)
```

---

## Memory MCP schema for governance state

```json
{
  "governance_state": {
    "AFC": {
      "active_proposals": [
        {
          "id":          "afc-gov-2026-047",
          "title":       "Approve [Player] signing",
          "category":    "PLAYER_SIGNING",
          "closes_at":   "2026-08-15T23:59:00Z",
          "brief_generated_at": "2026-08-14T11:00:00Z",
          "recommendation": "VOTE_YES",
          "confidence":  "HIGH"
        }
      ],
      "vote_history": [
        {
          "proposal_id": "afc-gov-2026-031",
          "category":    "COMMERCIAL_PARTNERSHIP",
          "recommendation": "VOTE_YES",
          "outcome":     "PASSED",
          "ltui_actual_impact": "+5"
        }
      ],
      "last_checked":  "2026-08-14T11:00:00Z"
    }
  }
}
```

---

## Connection to other SportMind patterns

```
FEEDS FROM:
  Pattern 1 (Portfolio Monitor)  — detects tokens in active governance periods
  Pattern 6 (Athlete Tracker)    — APS/AELS data for player signing votes
  fan-token/sports-governance-intelligence/ — GSI framework
  fan-token/fan-token-lifecycle/            — LTUI calculations

FEEDS INTO:
  platform/memory-integration.md  — governance state storage
  core/multi-agent-context-sharing.md — governance signals shared across agents

REQUIRES FOR EXECUTION:
  Developer implements: fetch_active_proposals() data source
  Developer wires: vote submission to on-chain or Socios API
  SportMind provides: commercial intelligence brief only
```

---

*SportMind v3.47 · MIT License · sportmind.dev*
*See also: app-08-governance-intelligence.md · fan-token/sports-governance-intelligence/*
*fan-token/fan-token-lifecycle/ · core/athlete-financial-intelligence.md*
