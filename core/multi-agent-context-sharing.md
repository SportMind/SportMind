---
name: multi-agent-context-sharing
description: >
  Protocol for multiple SportMind agents sharing a single authoritative signal
  state without duplicating work or producing contradictory outputs. Use when
  deploying more than one SportMind agent simultaneously — e.g. a pre-match agent
  and a portfolio monitoring agent both analysing the same token at the same time.
  Covers signal authority rules, shared macro state, conflict resolution, and the
  context bus pattern. Extends core/multi-agent-coordination.md (which covers
  context window management and skill routing within a single agent) with the
  cross-agent coordination layer.
---

# Multi-Agent Context Sharing — SportMind

**How two or more SportMind agents share signal state without contradicting
each other or duplicating expensive analysis.**

`core/multi-agent-coordination.md` solves the single-agent problem: how one
agent manages its context window, routes queries to the right skills, and
maintains state across sessions.

This document solves the multi-agent problem: when two agents are both
analysing $AFC simultaneously — one running the pre-match chain, one running
portfolio monitoring — which macro check is authoritative? If both run
`sportmind_macro()` independently and get slightly different cached results,
their signals will diverge. If both run the full five-phase chain on the
same token at the same time, work is duplicated. If neither knows what the
other has already concluded, they may produce contradictory ENTER/WAIT signals.

---

## The three failure modes this protocol prevents

```
FAILURE 1 — SIGNAL CONTRADICTION:
  Agent A (pre-match): direction = HOME, recommended_action = ENTER
  Agent B (portfolio): recommended_action = WAIT (saw stale macro data)
  
  Root cause: Both agents ran macro check at different times.
  Agent A got modifier 1.00. Agent B got cached modifier 0.74 from 4h ago.
  
  Fix: One authoritative macro state, shared. Not two independent checks.

FAILURE 2 — REDUNDANT COMPUTATION:
  Agent A (pre-match): runs full five-phase chain for $AFC, takes 30 seconds
  Agent B (portfolio): runs full five-phase chain for $AFC, takes 30 seconds
  Both run simultaneously, both produce same output.
  
  Root cause: No shared result cache.
  Fix: First agent to complete publishes result. Second agent reads it.

FAILURE 3 — CONTEXT BLINDNESS:
  Agent A (pre-match): detects disciplinary flag on key player, sets ABSTAIN
  Agent B (portfolio): doesn't know about the disciplinary flag, still shows ENTER
  
  Root cause: No shared signal state between agents.
  Fix: Shared flag state that all agents read before making recommendations.
```

---

## Signal authority model

```
AUTHORITY HIERARCHY (which agent owns which signal):

TIER 1 — GLOBAL SIGNALS (one authoritative source, shared by all agents):
  macro_state:        The macro monitor agent OR the most recent sportmind_macro() call
  chz_burn_state:     Updated from quarterly Chiliz burn reports (low frequency)
  
  RULE: Any agent needing macro_modifier reads from shared macro state.
        Only the designated macro monitor updates it.
        Update frequency: every 4 hours maximum (or on breaking macro event).

TIER 2 — TOKEN SIGNALS (one authoritative source per token):
  pre_match_signal:   The pre-match agent for that token's next fixture
  dsm_flags:          The most recent disciplinary check for that token's key players
  ftp_status:         The Fan Token Play monitor (if active) for that token
  lifecycle_phase:    Updated by portfolio monitor on 24h cycle
  
  RULE: One agent "owns" each token's signal at any given time.
        Other agents READ that signal; they do not re-run the analysis.
        Ownership transfers on a time-based or event-based trigger.

TIER 3 — LOCAL SIGNALS (agent-specific, not shared):
  reasoning_trace:    Internal chain of thought — not shared
  skill_loading_log:  Which files this agent loaded — not shared
  session_history:    This agent's conversation history — not shared

OWNERSHIP TRANSFER TRIGGERS:
  Pre-match agent finishes analysis → portfolio agent inherits the signal
  Match kicks off → pre-match agent releases ownership; post-match agent takes over
  Fan Token Play monitor detects pre-liquidation → takes ownership of supply_mechanics
```

---

## The shared context bus

```
DEFINITION:
  A shared read/write data structure that all agents in a deployment access.
  Implemented via Memory MCP (platform/memory-integration.md) as the persistent store.
  Structured so that reads are cheap and writes are infrequent.

SCHEMA:

shared_context = {
  "schema_version":    "1.0",
  "last_updated":      "ISO-8601",
  
  "macro_state": {
    "modifier":        float,
    "phase":           "BULL|NEUTRAL|BEAR|EXTREME_BEAR",
    "override_active": bool,
    "updated_at":      "ISO-8601",
    "updated_by":      "agent_id",
    "stale_after":     "ISO-8601"   # 4h from update
  },
  
  "token_signals": {
    "AFC": {
      "owner_agent":       "pre_match_agent_001",
      "ownership_expires": "ISO-8601",
      "last_signal": {
        "direction":           "HOME|AWAY|DRAW",
        "adjusted_score":      float,
        "sms":                 float,
        "recommended_action":  "ENTER|WAIT|ABSTAIN",
        "generated_at":        "ISO-8601",
        "valid_until":         "ISO-8601"
      },
      "dsm_flags": {
        "COMMERCIAL_RISK_ACTIVE":    bool,
        "LEGAL_PROCEEDINGS_ACTIVE":  bool,
        "CITING_ACTIVE":             bool,
        "last_checked":              "ISO-8601"
      },
      "fan_token_play": {
        "active":              bool,
        "path":                "PATH_1|PATH_2|null",
        "pre_liq_detected":    bool,
        "pre_liq_tx":          "0x...|null",
        "season_net_burned_pct": float
      },
      "lifecycle_phase":       int
    }
  },
  
  "active_agents": {
    "pre_match_agent_001": {
      "status":     "RUNNING|IDLE|WAITING",
      "current_task": "string",
      "last_seen":  "ISO-8601"
    }
  }
}

MEMORY MCP KEYS:
  shared_macro_state      → macro_state object above
  token_signal_{ticker}   → per-token signal object above
  agent_registry          → active_agents object above
```

---

## Coordination rules

```
RULE 1 — MACRO READ-BEFORE-ANALYSIS:
  Every agent reads shared_macro_state before starting any analysis.
  If stale_after has passed: the reading agent refreshes it via sportmind_macro()
  and writes the result back to shared context.
  
  Result: macro is refreshed at most once per 4h regardless of how many agents
  are running. No redundant macro checks.

RULE 2 — SIGNAL OWNERSHIP CHECK:
  Before running full analysis on a token, an agent checks:
    a) Is there a valid signal in token_signals[ticker]?
    b) Has valid_until not yet passed?
    c) Is the current agent the owner?
  
  If (a) and (b) are true and (c) is false:
    → READ the existing signal, do not re-run analysis
    → Mark that this agent consumed the existing signal
  
  If (a) is false or (b) has expired:
    → Claim ownership (write own agent_id to owner_agent)
    → Run analysis, publish result to token_signals[ticker]
    → Set valid_until based on CDI and match timing

RULE 3 — DSM FLAG PROPAGATION:
  If any agent detects a DSM flag (COMMERCIAL_RISK_ACTIVE, LEGAL_PROCEEDINGS_ACTIVE):
    → Immediately write flag to shared context token_signals[ticker].dsm_flags
    → All other agents must re-read DSM flags before their next recommendation
  
  This is the highest-priority write in the protocol.
  A DSM flag written by any agent overrides any pending ENTER signal from any agent.

RULE 4 — FAN TOKEN PLAY EVENT PROPAGATION:
  If the Fan Token Play monitor detects pre-liquidation:
    → Write fan_token_play.pre_liq_detected = True to shared context
    → All other agents reading this token see the FTP status immediately
    → Pre-match agent knows to load gamified-tokenomics skill in its next analysis
  
  This prevents the pre-match agent from treating the pre-liquidation as a whale signal.

RULE 5 — CONFLICT RESOLUTION:
  If two agents write conflicting recommended_actions simultaneously:
    → The signal with the higher SMS wins
    → If SMS is equal: the more recent signal wins
    → Always log the conflict: both signals preserved in history, winner flagged
  
  Human review is triggered if: ENTER vs ABSTAIN conflict (maximum disagreement),
  or if the same token has 3+ consecutive conflicts in 24h.
```

---

## Implementation pattern

```python
# Minimal shared context manager using Memory MCP
# Full implementation: platform/memory-integration.md + this file

import asyncio
import json
from datetime import datetime, timezone, timedelta
from typing import Optional


class SharedContextManager:
    """
    Manages shared signal state between multiple SportMind agents.
    Uses Memory MCP as the persistent backing store.

    All agents in a deployment share one SharedContextManager instance
    (or connect to the same Memory MCP server).
    """

    MACRO_TTL_HOURS   = 4
    SIGNAL_TTL_HOURS  = 24

    def __init__(self, memory_mcp_url: str, agent_id: str):
        self.memory_url = memory_mcp_url
        self.agent_id   = agent_id

    async def get_macro_state(self) -> dict:
        """
        Get authoritative macro state. Refreshes if stale.
        All agents call this instead of sportmind_macro() directly.
        """
        stored = await self._memory_get("shared_macro_state")

        if stored and not self._is_stale(stored.get("stale_after")):
            return stored

        # Stale or missing — this agent refreshes it
        # (In production: call sportmind_macro() MCP tool here)
        fresh = await self._call_sportmind_macro()
        fresh["updated_by"]   = self.agent_id
        fresh["stale_after"]  = (
            datetime.now(timezone.utc) + timedelta(hours=self.MACRO_TTL_HOURS)
        ).isoformat()
        await self._memory_set("shared_macro_state", fresh)
        return fresh

    async def claim_token_ownership(self, ticker: str) -> bool:
        """
        Attempt to claim analysis ownership for a token.
        Returns True if claim succeeded (this agent can run analysis).
        Returns False if another agent owns it and has a valid recent signal.
        """
        key      = f"token_signal_{ticker}"
        existing = await self._memory_get(key)

        if existing:
            owner   = existing.get("owner_agent")
            valid   = existing.get("last_signal", {}).get("valid_until")
            if owner != self.agent_id and not self._is_stale(valid):
                return False  # Another agent has a valid signal

        # Claim ownership
        current = existing or {}
        current["owner_agent"]       = self.agent_id
        current["ownership_expires"] = (
            datetime.now(timezone.utc) + timedelta(hours=self.SIGNAL_TTL_HOURS)
        ).isoformat()
        await self._memory_set(key, current)
        return True

    async def publish_signal(self, ticker: str, signal: dict,
                              valid_hours: int = 24):
        """Publish analysis result to shared context."""
        key     = f"token_signal_{ticker}"
        current = await self._memory_get(key) or {}

        current["last_signal"] = {
            **signal,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generated_by": self.agent_id,
            "valid_until":  (
                datetime.now(timezone.utc) + timedelta(hours=valid_hours)
            ).isoformat(),
        }
        await self._memory_set(key, current)

    async def propagate_dsm_flag(self, ticker: str, flag: str, value: bool):
        """
        Write a DSM flag. Highest-priority write — overrides any pending signal.
        All agents reading this token will see the flag immediately.
        """
        key     = f"token_signal_{ticker}"
        current = await self._memory_get(key) or {}
        if "dsm_flags" not in current:
            current["dsm_flags"] = {}
        current["dsm_flags"][flag]          = value
        current["dsm_flags"]["last_checked"] = datetime.now(timezone.utc).isoformat()
        current["dsm_flags"]["flagged_by"]   = self.agent_id

        # If critical flag: immediately invalidate any existing ENTER signal
        if flag in ("COMMERCIAL_RISK_ACTIVE", "LEGAL_PROCEEDINGS_ACTIVE") and value:
            if current.get("last_signal", {}).get("recommended_action") == "ENTER":
                current["last_signal"]["recommended_action"] = "ABSTAIN"
                current["last_signal"]["override_reason"] = f"{flag} set by {self.agent_id}"

        await self._memory_set(key, current)

    async def propagate_ftp_event(self, ticker: str, event_type: str,
                                   tx_hash: Optional[str] = None):
        """
        Propagate Fan Token Play on-chain event to all agents.
        Prevents pre-match agent from misreading pre-liquidation as whale sell.
        """
        key     = f"token_signal_{ticker}"
        current = await self._memory_get(key) or {}
        if "fan_token_play" not in current:
            current["fan_token_play"] = {}

        if event_type == "FAN_TOKEN_PLAY_PRE_LIQUIDATION":
            current["fan_token_play"]["pre_liq_detected"] = True
            current["fan_token_play"]["pre_liq_tx"]       = tx_hash
            current["fan_token_play"]["pre_liq_time"]     = (
                datetime.now(timezone.utc).isoformat()
            )
            current["fan_token_play"]["agent_rule"] = (
                "DO NOT treat as Category 1 distribution signal. Protocol mechanics."
            )
        elif event_type == "FAN_TOKEN_PLAY_WIN_CONFIRMED":
            current["fan_token_play"]["win_confirmed"] = True
            current["fan_token_play"]["win_burn_tx"]   = tx_hash
        elif event_type == "FAN_TOKEN_PLAY_LOSS_CONFIRMED":
            current["fan_token_play"]["loss_confirmed"] = True
            current["fan_token_play"]["supply_effect"]  = "NEUTRAL"

        await self._memory_set(key, current)

    def _is_stale(self, expiry_iso: Optional[str]) -> bool:
        if not expiry_iso:
            return True
        try:
            expiry = datetime.fromisoformat(expiry_iso)
            return datetime.now(timezone.utc) > expiry
        except:
            return True

    async def _memory_get(self, key: str) -> Optional[dict]:
        """Read from Memory MCP — implement via memory-integration.md connector."""
        raise NotImplementedError("Connect to Memory MCP — see platform/memory-integration.md")

    async def _memory_set(self, key: str, value: dict):
        """Write to Memory MCP — implement via memory-integration.md connector."""
        raise NotImplementedError("Connect to Memory MCP — see platform/memory-integration.md")

    async def _call_sportmind_macro(self) -> dict:
        """Call sportmind_macro() MCP tool — implement via MCP connector."""
        raise NotImplementedError("Connect to SportMind MCP — see MCP-SERVER.md")
```

---

## Connection to other SportMind skills

```
BUILDS ON:
  core/multi-agent-coordination.md    → single-agent context and routing
  platform/memory-integration.md      → Memory MCP as shared state backing store
  platform/sequential-thinking-integration.md → five-phase chain (per-agent)
  platform/skill-discovery-protocol.md → dynamic skill selection (per-agent)

GOVERNS:
  fan-token/gamified-tokenomics-intelligence/ → FTP event propagation (Rule 4)
  core/athlete-disciplinary-intelligence.md  → DSM flag propagation (Rule 3)
  agent-prompts/agent-prompts.md             → Prompt 17 (four-server stack)
  examples/agentic-workflows/                → all multi-agent workflow patterns

REQUIRED FOR:
  Any deployment with 2+ concurrent SportMind agents
  Portfolio monitor + pre-match agent combination
  Fan Token Play monitor + portfolio monitor combination
```

---

*SportMind v3.46 · MIT License · sportmind.dev*
*See also: core/multi-agent-coordination.md · platform/memory-integration.md*
*platform/skill-discovery-protocol.md · platform/sequential-thinking-integration.md*
