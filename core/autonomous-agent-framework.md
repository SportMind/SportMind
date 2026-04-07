# Autonomous Agent Framework

**The SportMind model for agents that operate continuously, make decisions
independently, and coordinate with other agents and systems.**

This document defines what a SportMind autonomous agent is, how it reasons,
what it can decide alone, when it escalates, how it communicates with other
agents, and how it fits within the broader ecosystem of applications, platforms,
and LLMs that SportMind supports.

---

## The SportMind agent model

A SportMind agent is a reasoning system that:

1. **Loads SportMind intelligence** as its domain knowledge context
2. **Applies the reasoning chain** (`core/reasoning-patterns.md`) to sports signals
3. **Operates within defined autonomy boundaries** — acting independently within scope, escalating outside it
4. **Maintains state** across multiple cycles rather than treating each query as isolated
5. **Coordinates with other agents and systems** without duplicating their responsibilities
6. **Complements application-layer tools** — it does not replace FanTokenIntel, SportFi Kit, or any third-party application; it provides the intelligence layer they act on

The last point is architectural and non-negotiable. A SportMind agent's job is to know and reason — not to execute trades, submit governance votes, or make financial commitments. Those actions belong to the application layer. The agent's output is always intelligence, never execution.

```
SPORTMIND AGENT RESPONSIBILITY MODEL:

SportMind Agent DOES:
  → Analyse sporting events using the five-layer intelligence stack
  → Monitor signals continuously and detect conditions worth acting on
  → Generate confidence-scored outputs in the standard schema
  → Escalate when confidence is insufficient or conditions are unusual
  → Coordinate with other agents by sharing signal state
  → Maintain freshness awareness and flag stale data

SportMind Agent DOES NOT:
  → Execute financial transactions (fan token buys, sells, LP positions)
  → Submit governance votes on behalf of token holders
  → Make transfer offers or negotiate contracts
  → Override human decisions once escalation has been triggered
  → Operate without a defined autonomy boundary

These boundaries are not limitations — they are what makes autonomous
SportMind agents trustworthy enough to run unsupervised.
```

---

## The autonomy spectrum

SportMind agents operate at one of five autonomy levels. The level is set by
the developer at deployment time and should match the application's risk tolerance.

```
LEVEL 0 — SUPERVISED (fully human-gated)
  Agent generates analysis; human approves every recommendation before any action.
  Use case: high-stakes portfolio decisions; governance votes with large positions.
  Output: intelligence briefings with clear recommended_action for human review.
  Human touch: every cycle.

LEVEL 1 — ADVISORY (human decides, agent informs)
  Agent monitors continuously and surfaces intelligence proactively.
  Human makes all decisions; agent ensures they have the right context.
  Use case: club commercial directors; sports agents tracking transfer intelligence.
  Human touch: whenever the agent surfaces a recommendation.

LEVEL 2 — SEMI-AUTONOMOUS (agent acts within boundaries, escalates outside)
  Agent can act independently when SMS ≥ 80, no blocking flags, macro not overriding.
  Agent escalates when SMS < 60, any blocking flag active, or macro override.
  Use case: fan token portfolio monitoring with defined position parameters.
  Human touch: escalation events only (typically 10-20% of cycles).

LEVEL 3 — AUTONOMOUS WITH REVIEW (agent acts, human reviews asynchronously)
  Agent acts immediately; human reviews the log, not each individual decision.
  Anomaly detection triggers synchronous human alert.
  Use case: tournament tracking, calibration record generation, signal logging.
  Human touch: daily log review; anomaly alerts.

LEVEL 4 — FULLY AUTONOMOUS (within hard boundaries)
  Agent operates indefinitely without human input.
  Hard boundaries are technically enforced, not just policy.
  Use case: macro state monitoring, HAS tracking, calibration data collection.
  Human touch: configuration changes only; never individual decisions.

AUTONOMY RULE:
  Never deploy at Level 3+ for financial execution or governance decisions.
  These categories are hard-bounded at Level 0-1 regardless of SMS quality.
  The intelligence can be Level 3+; the action layer never is.
```

---

## Agent lifecycle

Every SportMind autonomous agent follows this lifecycle:

```
STATES:

INITIALISING
  → Load SportMind stack for configured sports/use_cases
  → Verify content integrity (sportmind_verify MCP tool)
  → Fetch initial macro state (sportmind_macro MCP tool)
  → Establish baseline for monitored tokens/events
  → Transition: → MONITORING

MONITORING (steady state)
  → Execute scheduled cycle (frequency depends on autonomy level and use case)
  → Check macro state freshness (Tier 3 — 4-8 hour cycle)
  → Scan for signal events meeting alert thresholds
  → Update state log
  → Transition: → ANALYSING (if event detected) | → MONITORING (if nothing triggered)

ANALYSING
  → Execute full six-step SportMind reasoning chain
  → Generate confidence output with SMS
  → Evaluate against autonomy boundary
  → Transition: → ACTING (Level 2+, SMS ≥ threshold) | → ESCALATING (below threshold)

ACTING (Level 2+ only)
  → Generate structured recommendation
  → Pass to application layer (FanTokenIntel, SportFi Kit, etc.) for execution
  → Log action with full reasoning trail
  → Transition: → MONITORING

ESCALATING
  → Generate escalation brief with full reasoning trail
  → Send to human review channel (email, Slack, push notification)
  → Pause autonomous action for this event until human responds
  → Transition: → WAITING_FOR_HUMAN

WAITING_FOR_HUMAN
  → Continue monitoring other events
  → Do not act on escalated event until human responds
  → Timeout: if no response in configured window, re-escalate
  → Transition: → MONITORING (after human response or timeout)

PAUSED
  → Triggered manually or by hard safety condition
  → No autonomous action; logging continues
  → Transition: → MONITORING (on manual resume) | → TERMINATED (on shutdown)

TERMINATED
  → Ordered shutdown; flush state log; close connections
  → Final report generated
```

---

## The decision framework

The autonomy boundary for any SportMind agent is determined by a matrix
of SMS quality, flag status, and decision category.

```
AUTONOMOUS ACTION MATRIX:

                    SMS ≥ 80        SMS 60-79       SMS < 60
                    No blocking     No blocking     OR any
                    flags           flags           blocking flag
────────────────────────────────────────────────────────────────
Signal generation   AUTONOMOUS      AUTONOMOUS      AUTONOMOUS
  (always auto)

Alert generation    AUTONOMOUS      AUTONOMOUS      AUTONOMOUS
  (always auto)

Recommendation      AUTONOMOUS      AUTONOMOUS      ESCALATE
  (Level 2+)        (Level 2+)      with note

Fan token signal    AUTONOMOUS      ADVISORY        ESCALATE
  analysis          (Level 2+)      only

DeFi/liquidity      AUTONOMOUS      ADVISORY        ESCALATE
  assessment        (Level 2+)      only

Governance brief    ADVISORY        ADVISORY        ESCALATE
  (never fully      only            only
  autonomous)

Financial           LEVEL 0-1       LEVEL 0-1       LEVEL 0-1
  execution         ONLY            ONLY            ONLY

Governance vote     LEVEL 0-1       LEVEL 0-1       LEVEL 0-1
  submission        ONLY            ONLY            ONLY
────────────────────────────────────────────────────────────────

BLOCKING FLAGS (always escalate regardless of SMS):
  macro_override_active = True
  liquidity_critical = True
  lineup_unconfirmed at T-0 (match has started without lineup data)
  governance_theatre flag active (do not act on unreliable governance)
  injury_warning for multiple key players simultaneously
```

---

## Agent-to-agent protocol

When multiple SportMind agents operate in the same environment, they need
a defined protocol for communication, state sharing, and conflict resolution.

```
AGENT REGISTRATION:

Each SportMind agent declares its capabilities at startup:

{
  "agent_id": "portfolio-monitor-001",
  "agent_type": "portfolio_monitor",
  "autonomy_level": 2,
  "sports_covered": ["football", "basketball", "cricket"],
  "use_cases": ["fan_token_tier1", "fan_token_tier2"],
  "tokens_monitored": ["PSG", "BAR", "CITY"],
  "cycle_frequency_minutes": 240,
  "escalation_channel": "slack://channel-id",
  "sportmind_version": "3.17.0",
  "registered_at": "2026-04-04T10:00:00Z"
}

SIGNAL SHARING:

When one agent generates a signal relevant to another agent's monitored scope,
it broadcasts to the shared signal bus:

{
  "source_agent": "prematch-001",
  "event_id": "ucl-qf-psg-arsenal-2026-05-07",
  "signal_type": "pre_match_t2h",
  "adjusted_score": 68.4,
  "flags": {"lineup_unconfirmed": false, "macro_override_active": false},
  "sms": 79,
  "timestamp": "2026-05-07T17:00:00Z",
  "intended_consumers": ["portfolio-monitor-001", "governance-agent-001"]
}

The portfolio monitor does not re-run pre-match analysis if the pre-match agent
has already run it. It consumes the shared signal and applies it to its own context.

CONFLICT RESOLUTION:

If two agents produce conflicting signals for the same event:
  1. Higher SMS wins (more complete intelligence takes precedence)
  2. More recent signal wins if SMS within 5 points of each other
  3. If both conditions are tied: escalate to human (genuine uncertainty)

Never silently discard a conflicting signal — log it and note the conflict.

CAPABILITY BOUNDARIES:

Agents must not request another agent to perform actions outside its
declared capabilities. A portfolio monitor must not ask a pre-match agent
to submit a governance vote. Each agent's capability declaration is its contract.
```

---

## Ecosystem integration protocol

SportMind agents operate within a broader ecosystem. This protocol defines
how they interact with each layer without creating conflicts.

```
APPLICATION LAYER INTEGRATION:

FanTokenIntel:
  SportMind agent provides: pre-match signals, macro state, NCSI calculations
  FanTokenIntel provides: portfolio management, holder analytics, display layer
  Interface: SportMind agent writes structured JSON to a shared signal store;
             FanTokenIntel reads from that store for display and portfolio logic
  Rule: SportMind agent never writes directly to FanTokenIntel's data store;
        it provides signals that FanTokenIntel chooses whether to consume

SportFi Kit:
  SportMind agent provides: intelligence context (should conditions allow entry?)
  SportFi Kit provides: contract execution (token-gating, P2P wagering, wallet detection)
  Interface: SportMind agent generates recommended_action; SportFi Kit reads it
             and executes only when human or application-layer logic approves
  Rule: SportMind agent output NEVER directly triggers a smart contract call;
        the application layer always mediates

Third-party applications:
  SportMind agent exposes its signal state via:
    - MCP tool calls (sportmind_signal, sportmind_macro, sportmind_stack)
    - Skills API endpoint (GET /stack)
    - Shared signal store (JSON file or database)
  Third-party applications choose which interface fits their architecture

LLM LAYER INTEGRATION:

Claude / GPT-4 / Gemini as reasoning engine:
  SportMind provides context; the LLM provides reasoning; the agent orchestrates.
  The LLM is not the agent — it is the reasoning component the agent calls.

  Agent → loads SportMind stack as context
  Agent → passes context + live data + user query to LLM
  LLM   → reasons using SportMind framework
  Agent → validates LLM output against confidence schema
  Agent → acts or escalates based on validated output

  RULE: Never treat LLM output as ground truth without schema validation.
  Even a well-prompted LLM will occasionally produce outputs that violate
  SportMind's confidence schema. The agent's validation layer catches this.

DATA LAYER INTEGRATION:

Chiliz Chain / KAYEN:
  Agent uses realtime-integration-patterns.py Pattern 3 (token monitor)
  Agent never writes to the chain directly — reads only

Live sports data APIs:
  Agent uses realtime-integration-patterns.py Pattern 2 (lineup webhook)
  and Pattern 4 (weather integration)

Crypto market data:
  Agent uses realtime-integration-patterns.py Pattern 1 (macro webhook)
  Updates macro-state.json every 4-8 hours
```

---

## Safety model

Six safety principles that all SportMind autonomous agents must implement.

```
PRINCIPLE 1 — INTELLIGENCE SEPARATION
  The agent generates intelligence. The application layer takes action.
  No SportMind agent ever directly executes a financial or governance action.
  This is the foundational safety principle. It is not overridable.

PRINCIPLE 2 — CONFIDENCE GATING
  Every autonomous action requires a minimum SMS threshold (developer-defined).
  Recommended minimum: SMS 60 for any advisory output; SMS 80 for Level 2 action.
  Below threshold: advisory output only, never autonomous action.

PRINCIPLE 3 — FLAG RESPECT
  Blocking flags are absolute. When any blocking flag is active:
  macro_override_active, liquidity_critical, lineup_unconfirmed at T-0
  → The agent downgrades to advisory regardless of SMS.
  → No exceptions, no overrides, no "but the signal looks good" reasoning.

PRINCIPLE 4 — ESCALATION COMPLETENESS
  When an agent escalates, it provides the full reasoning trail — not just
  "confidence too low" but why confidence is low, what data is missing,
  what the agent's best current assessment is, and what information would
  allow it to resolve the uncertainty.
  Partial escalations are more dangerous than full ones. A human receiving
  "low confidence" with no context cannot make a good decision.

PRINCIPLE 5 — AUDIT TRAIL
  Every agent cycle is logged with:
  → Input data and freshness timestamps
  → Reasoning chain steps and modifier values applied
  → Output with full confidence schema
  → Action taken OR escalation triggered and why
  → Outcome (if known) for calibration purposes
  The audit trail is the mechanism by which autonomous agent behaviour
  improves over time through calibration.

PRINCIPLE 6 — GRACEFUL DEGRADATION
  When an agent cannot access a required data source (macro state stale,
  live signals unavailable, skill files unverifiable):
  → It does not fail silently or produce outputs as if data was available
  → It generates a degraded output with explicit freshness warnings
  → It reduces its autonomy level for that cycle
  → It alerts the operator of the degraded state
  "I have incomplete data but here is what I know" is always better than
  either silence or false confidence.
```

---

## Agent status reporting

Every autonomous SportMind agent exposes its current state via the
`sportmind_agent_status` MCP tool (see `platform/sportmind-mcp-server.md`).

This makes agents observable — a prerequisite for trusting them to run unsupervised.

```json
{
  "agent_status": {
    "agent_id": "portfolio-monitor-001",
    "agent_type": "portfolio_monitor",
    "state": "MONITORING",
    "autonomy_level": 2,
    "health": "HEALTHY",
    "uptime_hours": 72.4,
    "last_cycle_at": "2026-04-04T09:45:00Z",
    "next_cycle_at": "2026-04-04T13:45:00Z",
    "cycles_completed": 18,
    "actions_taken": 3,
    "escalations_triggered": 1,
    "current_context": {
      "macro_state": "NEUTRAL",
      "macro_modifier": 1.00,
      "macro_age_hours": 3.2,
      "tokens_monitored": ["PSG", "BAR", "CITY"],
      "pending_escalations": 0,
      "upcoming_events": [
        {
          "event_id": "ucl-qf-psg-arsenal-2026-05-07",
          "hours_away": 68,
          "signal_tier": "TIER_1",
          "pre_match_chain_scheduled": true
        }
      ]
    },
    "data_freshness": {
      "macro_state": "FRESH",
      "sport_stacks": "FRESH",
      "skill_hashes_verified": true
    },
    "recent_actions": [
      {
        "action_type": "portfolio_alert",
        "timestamp": "2026-04-04T07:30:00Z",
        "trigger": "HAS spike PSG +18 points",
        "sms": 76,
        "outcome": "alerted"
      }
    ]
  }
}
```

---

## Implementation template

```python
# core/autonomous_agent_base.py
"""
Base class for all SportMind autonomous agents.
Implements the lifecycle, decision framework, and safety model.
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
import json, asyncio, logging

class AgentState(Enum):
    INITIALISING        = "INITIALISING"
    MONITORING          = "MONITORING"
    ANALYSING           = "ANALYSING"
    ACTING              = "ACTING"
    ESCALATING          = "ESCALATING"
    WAITING_FOR_HUMAN   = "WAITING_FOR_HUMAN"
    PAUSED              = "PAUSED"
    TERMINATED          = "TERMINATED"

class AutonomyLevel(Enum):
    SUPERVISED          = 0
    ADVISORY            = 1
    SEMI_AUTONOMOUS     = 2
    AUTONOMOUS_REVIEW   = 3
    FULLY_AUTONOMOUS    = 4

@dataclass
class AgentConfig:
    agent_id:             str
    agent_type:           str
    autonomy_level:       AutonomyLevel
    sports_covered:       list[str]
    use_cases:            list[str]
    min_sms_for_action:   float = 60.0
    cycle_interval_sec:   int   = 14400  # 4 hours default
    escalation_channel:   str   = ""
    sportmind_version:    str   = "3.17.0"

@dataclass
class AgentCycle:
    cycle_id:             str
    started_at:           str
    state:                AgentState
    signals_evaluated:    int = 0
    actions_taken:        int = 0
    escalations:          int = 0
    errors:               list = field(default_factory=list)
    completed_at:         Optional[str] = None

class SportMindAgent:
    """
    Base class for all SportMind autonomous agents.
    Subclass and implement: analyse(), should_act(), act(), escalate().
    """

    def __init__(self, config: AgentConfig, sportmind_api_url: str):
        self.config         = config
        self.api_url        = sportmind_api_url
        self.state          = AgentState.INITIALISING
        self.cycle_count    = 0
        self.action_count   = 0
        self.escalation_count = 0
        self.audit_log      = []
        self.logger         = logging.getLogger(f"sportmind.{config.agent_id}")

    # ── Lifecycle ──────────────────────────────────────────────────────────

    async def start(self):
        """Full agent lifecycle."""
        await self._initialise()
        while self.state not in (AgentState.PAUSED, AgentState.TERMINATED):
            await self._run_cycle()
            await asyncio.sleep(self.config.cycle_interval_sec)

    async def _initialise(self):
        self.logger.info(f"Initialising {self.config.agent_id}")
        # 1. Verify skill integrity
        await self._verify_skills()
        # 2. Load macro state
        self.macro = await self._fetch_macro()
        # 3. Establish baselines
        await self._establish_baselines()
        self._transition(AgentState.MONITORING)

    async def _run_cycle(self):
        self.cycle_count += 1
        cycle = AgentCycle(
            cycle_id  = f"{self.config.agent_id}-{self.cycle_count}",
            started_at = datetime.now(timezone.utc).isoformat(),
            state      = AgentState.MONITORING
        )
        try:
            # Refresh macro if stale
            if self._macro_is_stale():
                self.macro = await self._fetch_macro()

            # Detect signal events
            events = await self._scan_for_events()
            cycle.signals_evaluated = len(events)

            for event in events:
                self._transition(AgentState.ANALYSING)
                signal = await self.analyse(event)

                if self._should_act_autonomously(signal):
                    self._transition(AgentState.ACTING)
                    await self.act(signal)
                    cycle.actions_taken += 1
                    self.action_count += 1
                else:
                    self._transition(AgentState.ESCALATING)
                    await self.escalate(signal, event)
                    cycle.escalations += 1
                    self.escalation_count += 1

            self._transition(AgentState.MONITORING)

        except Exception as e:
            cycle.errors.append(str(e))
            self.logger.error(f"Cycle error: {e}")
            # Safety: errors never prevent audit logging
        finally:
            cycle.completed_at = datetime.now(timezone.utc).isoformat()
            self._log_cycle(cycle)

    # ── Decision framework ─────────────────────────────────────────────────

    def _should_act_autonomously(self, signal: dict) -> bool:
        """
        Core decision: can this agent act autonomously on this signal?
        Implements the Autonomous Action Matrix from this framework.
        """
        if self.config.autonomy_level.value < 2:
            return False  # Supervised and Advisory never act autonomously

        sms  = signal.get("sportmind_score", {}).get("sms", 0)
        flags = signal.get("modifiers", {}).get("flags", {})

        # PRINCIPLE 3: Blocking flags are absolute
        blocking = [
            flags.get("macro_override_active"),
            flags.get("liquidity_critical"),
            flags.get("governance_theatre"),
        ]
        if any(blocking):
            return False

        # PRINCIPLE 2: Confidence gating
        return sms >= self.config.min_sms_for_action

    # ── Safety checks ──────────────────────────────────────────────────────

    def _is_financial_execution(self, action: dict) -> bool:
        """PRINCIPLE 1: Financial execution never autonomous."""
        financial_types = {"buy", "sell", "lp_add", "lp_remove", "stake", "unstake"}
        return action.get("action_type", "") in financial_types

    def _is_governance_submission(self, action: dict) -> bool:
        """PRINCIPLE 1: Governance submission never autonomous."""
        return action.get("action_type", "") in {"vote", "governance_submit"}

    def validate_action(self, action: dict) -> bool:
        """Pre-action safety validation. Returns False to block unsafe actions."""
        if self._is_financial_execution(action):
            self.logger.error(f"BLOCKED: financial execution attempted autonomously")
            return False
        if self._is_governance_submission(action):
            self.logger.error(f"BLOCKED: governance submission attempted autonomously")
            return False
        return True

    # ── Observable state ───────────────────────────────────────────────────

    def get_status(self) -> dict:
        """Returns agent status for sportmind_agent_status MCP tool."""
        return {
            "agent_id":           self.config.agent_id,
            "agent_type":         self.config.agent_type,
            "state":              self.state.value,
            "autonomy_level":     self.config.autonomy_level.value,
            "uptime_cycles":      self.cycle_count,
            "actions_taken":      self.action_count,
            "escalations":        self.escalation_count,
            "macro_modifier":     self.macro.get("macro_state",{}).get("crypto_cycle",{}).get("macro_modifier",1.0),
            "sportmind_version":  self.config.sportmind_version,
            "timestamp":          datetime.now(timezone.utc).isoformat()
        }

    # ── Override in subclasses ─────────────────────────────────────────────

    async def analyse(self, event: dict) -> dict:
        raise NotImplementedError

    async def act(self, signal: dict):
        raise NotImplementedError

    async def escalate(self, signal: dict, event: dict):
        raise NotImplementedError

    async def _scan_for_events(self) -> list:
        raise NotImplementedError

    # ── Helpers ────────────────────────────────────────────────────────────

    def _transition(self, new_state: AgentState):
        self.logger.debug(f"{self.state.value} → {new_state.value}")
        self.state = new_state

    def _macro_is_stale(self) -> bool:
        last_updated = self.macro.get("macro_state",{}).get("last_updated","")
        if not last_updated: return True
        from datetime import timedelta
        try:
            age = datetime.now(timezone.utc) - datetime.fromisoformat(last_updated)
            return age > timedelta(hours=8)
        except: return True

    async def _fetch_macro(self) -> dict:
        import aiohttp
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.api_url}/macro-state") as r:
                return await r.json()

    async def _verify_skills(self):
        # Integrity check before loading any skills
        import aiohttp
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.api_url}/verify") as r:
                result = await r.json()
                if not result.get("verified"):
                    raise RuntimeError("SportMind skill integrity check failed")

    async def _establish_baselines(self): pass

    def _log_cycle(self, cycle: AgentCycle):
        self.audit_log.append(cycle.__dict__)
        # PRINCIPLE 5: Audit trail always written
        self.logger.info(
            f"Cycle {cycle.cycle_id}: "
            f"{cycle.signals_evaluated} signals, "
            f"{cycle.actions_taken} actions, "
            f"{cycle.escalations} escalations"
        )
```

---

## Compatibility

**Reasoning chain:** `core/reasoning-patterns.md` — the agent's core execution loop
**Temporal awareness:** `core/temporal-awareness.md` — data validity model
**Real-time patterns:** `platform/realtime-integration-patterns.md` — sensory layer
**Agentic workflows:** `examples/agentic-workflows/README.md` — concrete implementations
**Multi-agent coordination:** `examples/agentic-workflows/multi-agent-coordination.md` — coordinated system
**MCP server:** `platform/sportmind-mcp-server.md` — tool interface including agent_status
**Security:** `SECURITY.md` — Threats 6 and 7 apply to autonomous agent deployments
**Ecosystem:** `platform/integration-partners.md` — FanTokenIntel, SportFi Kit, LLM integrations

*MIT License · SportMind · sportmind.dev*
