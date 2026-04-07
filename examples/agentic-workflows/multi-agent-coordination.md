# Multi-Agent Coordination — SportMind Coordinated System

**The four SportMind agentic workflow patterns operating together as a
coordinated autonomous intelligence system.**

The four patterns in `README.md` are individually useful. This document
shows how they work as an integrated system — sharing state, triggering
each other, resolving signal conflicts, and producing a coherent intelligence
output that is greater than the sum of its parts.

---

## The coordinated system architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  SPORTMIND COORDINATED AGENT SYSTEM             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────┐         ┌──────────────────────────────┐  │
│  │  MACRO MONITOR   │────────▶│     SHARED SIGNAL BUS        │  │
│  │  (always first)  │         │  {event_id: signal_state}    │  │
│  └──────────────────┘         └──────────────────────────────┘  │
│                                        │ ▲                       │
│  ┌──────────────────┐                  │ │                       │
│  │  PORTFOLIO       │◀─────────────────┘ │                       │
│  │  MONITOR         │───signals──────────┘                       │
│  │  (4h cycle)      │                                            │
│  └────────┬─────────┘                                            │
│           │ triggers                                             │
│           ▼                                                       │
│  ┌──────────────────┐         ┌──────────────────┐              │
│  │  PRE-MATCH       │◀────────│  TRANSFER WINDOW │              │
│  │  CHAIN           │ player  │  MONITOR         │              │
│  │  (T-48h, T-2h)   │ absent  │  (window active) │              │
│  └────────┬─────────┘         └──────────────────┘              │
│           │ feeds NCSI                                           │
│           ▼                                                       │
│  ┌──────────────────┐                                            │
│  │  TOURNAMENT      │                                            │
│  │  TRACKER         │                                            │
│  │  (per match)     │                                            │
│  └──────────────────┘                                            │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              ESCALATION / ALERT CHANNEL                  │   │
│  │  (email, Slack, push — human receives consolidated view) │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## The shared signal bus

All four agents read from and write to a shared signal bus. This prevents
redundant analysis and ensures consistent signals across the system.

```python
# coordination/signal_bus.py
"""
Shared signal bus for SportMind coordinated agent system.
Agents write their signals here; other agents consume rather than re-analyse.
"""
import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

class SignalBus:
    """
    Thread-safe shared signal store.
    In production: replace with Redis, PostgreSQL, or your preferred store.
    """

    def __init__(self, store_path: str = "coordination/signal_state.json"):
        self.store_path = Path(store_path)
        self.store_path.parent.mkdir(exist_ok=True)
        self._lock = threading.Lock()
        self._state = self._load()

    def publish(self, source_agent: str, event_id: str,
                signal_type: str, signal: dict,
                intended_consumers: list[str] = None):
        """Publish a signal from one agent for consumption by others."""
        with self._lock:
            entry = {
                "source_agent":       source_agent,
                "event_id":           event_id,
                "signal_type":        signal_type,
                "signal":             signal,
                "published_at":       datetime.now(timezone.utc).isoformat(),
                "intended_consumers": intended_consumers or [],
                "consumed_by":        []
            }
            if event_id not in self._state:
                self._state[event_id] = {}
            self._state[event_id][signal_type] = entry
            self._save()

    def consume(self, consumer_agent: str, event_id: str,
                signal_type: str) -> Optional[dict]:
        """Consume a signal — marks it as consumed by this agent."""
        with self._lock:
            entry = self._state.get(event_id, {}).get(signal_type)
            if entry:
                if consumer_agent not in entry["consumed_by"]:
                    entry["consumed_by"].append(consumer_agent)
                self._save()
                return entry["signal"]
            return None

    def has_signal(self, event_id: str, signal_type: str,
                   max_age_hours: float = 4.0) -> bool:
        """Check if a current signal exists for this event/type."""
        entry = self._state.get(event_id, {}).get(signal_type)
        if not entry: return False
        published = datetime.fromisoformat(entry["published_at"])
        age_hours = (datetime.now(timezone.utc) - published).total_seconds() / 3600
        return age_hours <= max_age_hours

    def get_all_for_event(self, event_id: str) -> dict:
        """Get all signals for an event — for conflict resolution."""
        return self._state.get(event_id, {})

    def resolve_conflict(self, event_id: str, signal_type: str) -> Optional[dict]:
        """
        Conflict resolution: higher SMS wins; recency wins on tie.
        Returns the best available signal or None.
        """
        signals = []
        for agent_signal in self._state.get(event_id, {}).values():
            if agent_signal.get("signal_type") == signal_type:
                sms = agent_signal["signal"].get("sportmind_score", {}).get("sms", 0)
                signals.append((sms, agent_signal["published_at"], agent_signal["signal"]))

        if not signals: return None
        signals.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return signals[0][2]  # Best signal

    def _load(self) -> dict:
        if self.store_path.exists():
            return json.loads(self.store_path.read_text())
        return {}

    def _save(self):
        self.store_path.write_text(json.dumps(self._state, indent=2))
```

---

## How the four agents coordinate

### Trigger 1 — Portfolio monitor triggers pre-match chain

```python
# In Portfolio Monitor (Pattern 1)
class CoordinatedPortfolioMonitor(SportMindAgent):

    def __init__(self, config, api_url, signal_bus: SignalBus,
                 prematch_agent: 'CoordinatedPreMatchChain'):
        super().__init__(config, api_url)
        self.bus            = signal_bus
        self.prematch_agent = prematch_agent

    async def analyse(self, event: dict) -> dict:
        event_id = event["event_id"]

        # Check if pre-match chain has already analysed this event
        if self.bus.has_signal(event_id, "pre_match_t48h", max_age_hours=48):
            # Consume existing analysis — do not re-run
            signal = self.bus.consume(
                self.config.agent_id, event_id, "pre_match_t48h"
            )
            self.logger.info(f"[{event_id}] Consuming pre-match signal from bus")
            return signal

        # No existing analysis — trigger pre-match chain
        hours_away = event.get("hours_away", 999)
        if hours_away <= 48 and not self.bus.has_signal(event_id, "pre_match_t48h"):
            self.logger.info(f"[{event_id}] Triggering pre-match chain (T-48h)")
            asyncio.create_task(
                self.prematch_agent.run_for_event(event)
            )

        # Portfolio monitor generates its own portfolio-level signal
        return await self._generate_portfolio_signal(event)

    async def act(self, signal: dict):
        # Publish to bus so other agents can consume
        self.bus.publish(
            source_agent      = self.config.agent_id,
            event_id          = signal["event_context"]["event_id"],
            signal_type       = "portfolio_signal",
            signal            = signal,
            intended_consumers= ["governance-agent", "prematch-001"]
        )
        # Alert if warranted
        if signal["signal"]["recommended_action"] == "ENTER":
            await self._send_alert(signal)
```

### Trigger 2 — Pre-match chain feeds NCSI to tournament tracker

```python
# In Pre-Match Chain (Pattern 2)
class CoordinatedPreMatchChain(SportMindAgent):

    def __init__(self, config, api_url, signal_bus: SignalBus,
                 tournament_tracker: 'CoordinatedTournamentTracker'):
        super().__init__(config, api_url)
        self.bus                = signal_bus
        self.tournament_tracker = tournament_tracker

    async def run_t2h_update(self, event: dict):
        """T-2h update — called by scheduler or triggered by portfolio monitor."""
        signal = await self._generate_t2h_signal(event)

        # Publish to bus
        self.bus.publish(
            source_agent = self.config.agent_id,
            event_id     = event["event_id"],
            signal_type  = "pre_match_t2h",
            signal       = signal
        )

        # If this is a tournament match, feed NCSI to tournament tracker
        if event.get("is_tournament_match") and self.tournament_tracker:
            await self.tournament_tracker.receive_prematch_signal(event, signal)

        return signal

    async def handle_key_player_absent(self, event: dict, absent_players: list):
        """Key player absent — notify transfer monitor."""
        self.logger.warning(f"[{event['event_id']}] Key players absent: {absent_players}")

        # Publish absence signal to bus
        self.bus.publish(
            source_agent = self.config.agent_id,
            event_id     = event["event_id"],
            signal_type  = "player_absence",
            signal       = {
                "absent_players": absent_players,
                "injury_warning": True,
                "requires_reload": True
            },
            intended_consumers = ["transfer-monitor", "portfolio-monitor-001"]
        )
```

### Trigger 3 — Transfer monitor alerts pre-match chain on player news

```python
# In Transfer Window Monitor (Pattern 4)
class CoordinatedTransferMonitor(SportMindAgent):

    def __init__(self, config, api_url, signal_bus: SignalBus):
        super().__init__(config, api_url)
        self.bus = signal_bus

    async def confirm_transfer(self, player_id: str, new_club: str, fee: float):
        """Transfer confirmed — alert any agents monitoring affected events."""

        # Find upcoming events involving this player's old/new club
        affected_events = await self._find_affected_events(player_id)

        for event_id in affected_events:
            # Check if pre-match chain has a pending signal for this event
            existing = self.bus.has_signal(event_id, "pre_match_t48h")
            if existing:
                # Signal is now stale — mark for reload
                self.bus.publish(
                    source_agent = self.config.agent_id,
                    event_id     = event_id,
                    signal_type  = "signal_invalidation",
                    signal       = {
                        "reason":       "transfer_confirmed",
                        "player_id":    player_id,
                        "requires_reload": True,
                        "message":      f"Transfer of {player_id} to {new_club} confirmed. Pre-match signal requires reload."
                    },
                    intended_consumers = ["prematch-001", "portfolio-monitor-001"]
                )
                self.logger.info(f"[{event_id}] Pre-match signal invalidated by transfer: {player_id}")
```

### Trigger 4 — Tournament tracker updates portfolio monitor with NCSI

```python
# In Tournament Tracker (Pattern 3)
class CoordinatedTournamentTracker(SportMindAgent):

    def __init__(self, config, api_url, signal_bus: SignalBus):
        super().__init__(config, api_url)
        self.bus  = signal_bus
        self.ncsi = {}  # {token_symbol: cumulative_ncsi}

    async def process_match_result(self, match: dict):
        """Process result and update NCSI — share with portfolio monitor."""
        ncsi_updates = await self._calculate_ncsi_updates(match)

        # Update local state
        for token, delta in ncsi_updates.items():
            self.ncsi[token] = self.ncsi.get(token, 0) + delta

        # Publish NCSI updates to bus for portfolio monitor
        self.bus.publish(
            source_agent = self.config.agent_id,
            event_id     = f"tournament-{match.get('tournament_id', 'unknown')}",
            signal_type  = "ncsi_update",
            signal       = {
                "ncsi_deltas":    ncsi_updates,
                "cumulative_ncsi": dict(self.ncsi),
                "match":          match.get("event_id"),
                "stage":          match.get("stage")
            },
            intended_consumers = ["portfolio-monitor-001"]
        )

        # Alert on significant NCSI moves
        for token, delta in ncsi_updates.items():
            if abs(delta) > 0.15:  # Significant NCSI shift
                await self._send_alert({
                    "type": "ncsi_significant_move",
                    "token": token,
                    "delta": delta,
                    "cumulative": self.ncsi[token],
                    "match": match.get("event_id")
                })
```

---

## Conflict resolution in practice

```python
# coordination/conflict_resolver.py
"""
Handles signal conflicts when multiple agents produce different analyses
for the same event. Implements the conflict resolution protocol from
core/autonomous-agent-framework.md.
"""

class ConflictResolver:

    def __init__(self, signal_bus: SignalBus):
        self.bus = signal_bus

    def resolve(self, event_id: str, signal_type: str) -> dict:
        """
        Get the best available signal for an event.
        Protocol: higher SMS wins; recency wins on tie; escalate on genuine conflict.
        """
        best = self.bus.resolve_conflict(event_id, signal_type)
        if best:
            return best

        # No signals available — check if any are stale
        all_signals = self.bus.get_all_for_event(event_id)
        stale_signals = {
            k: v for k, v in all_signals.items()
            if not self.bus.has_signal(event_id, k, max_age_hours=4.0)
        }

        if stale_signals:
            return {
                "conflict_detected": True,
                "reason": "All available signals are stale",
                "stale_signal_types": list(stale_signals.keys()),
                "recommendation": "ESCALATE — refresh signals before acting"
            }

        return {
            "conflict_detected": True,
            "reason": "No signals available for this event",
            "recommendation": "ESCALATE — no SportMind analysis available"
        }

    def detect_genuine_conflict(self, event_id: str, signal_type: str) -> bool:
        """
        True if two agents have produced conflicting signals that cannot be
        resolved by SMS or recency alone (SMS within 5 points of each other).
        """
        signals = []
        for entry in self.bus.get_all_for_event(event_id).values():
            if entry.get("signal_type") == signal_type:
                sms = entry["signal"].get("sportmind_score", {}).get("sms", 0)
                signals.append(sms)

        if len(signals) < 2: return False

        signals.sort(reverse=True)
        return abs(signals[0] - signals[1]) <= 5  # Within 5 SMS points — genuine conflict
```

---

## System orchestrator

```python
# coordination/system_orchestrator.py
"""
Starts, monitors, and coordinates all four SportMind agents.
The orchestrator is not itself an agent — it is infrastructure.
"""
import asyncio
from coordination.signal_bus import SignalBus, ConflictResolver

class SportMindOrchestrator:

    def __init__(self, sportmind_api_url: str, config: dict):
        self.api_url    = sportmind_api_url
        self.config     = config
        self.bus        = SignalBus()
        self.resolver   = ConflictResolver(self.bus)
        self.agents     = {}

    async def start_system(self):
        """Start all agents and the coordination layer."""

        # Instantiate agents
        from examples.agentic_workflows.portfolio_monitor import CoordinatedPortfolioMonitor
        from examples.agentic_workflows.prematch_chain    import CoordinatedPreMatchChain
        from examples.agentic_workflows.tournament_tracker import CoordinatedTournamentTracker
        from examples.agentic_workflows.transfer_monitor  import CoordinatedTransferMonitor

        tournament = CoordinatedTournamentTracker(
            self.config["tournament"], self.api_url, self.bus
        )
        prematch = CoordinatedPreMatchChain(
            self.config["prematch"], self.api_url, self.bus, tournament
        )
        transfer = CoordinatedTransferMonitor(
            self.config["transfer"], self.api_url, self.bus
        )
        portfolio = CoordinatedPortfolioMonitor(
            self.config["portfolio"], self.api_url, self.bus, prematch
        )

        self.agents = {
            "tournament": tournament,
            "prematch":   prematch,
            "transfer":   transfer,
            "portfolio":  portfolio
        }

        # Start all agents concurrently
        await asyncio.gather(
            tournament.start(),
            prematch.start(),
            transfer.start(),
            portfolio.start(),
            self._health_monitor()
        )

    async def _health_monitor(self):
        """Monitor agent health every 30 minutes."""
        while True:
            await asyncio.sleep(1800)
            statuses = {aid: agent.get_status() for aid, agent in self.agents.items()}
            degraded = [aid for aid, s in statuses.items() if s.get("health") != "HEALTHY"]
            if degraded:
                await self._alert_operator(
                    f"DEGRADED: {degraded}. Full status: {statuses}"
                )

    async def get_system_status(self) -> dict:
        """Returns system-wide status for sportmind_agent_status MCP tool."""
        agent_statuses = [agent.get_status() for agent in self.agents.values()]
        degraded_count = sum(1 for s in agent_statuses if s.get("health") != "HEALTHY")
        return {
            "agents":        agent_statuses,
            "system_health": "HEALTHY" if degraded_count == 0 else "DEGRADED",
            "agent_count":   len(self.agents),
            "degraded_count": degraded_count,
            "signal_bus_events": len(self.bus._state)
        }
```

---

## Ecosystem integration in the coordinated system

```
HOW THE COORDINATED SYSTEM SITS IN THE BROADER ECOSYSTEM:

FanTokenIntel
  ← consumes portfolio_signal from signal bus
  ← reads pre_match_t2h signals for display
  ← receives ncsi_update for portfolio analytics

SportFi Kit
  ← reads recommended_action from signal bus BEFORE executing any contract call
  ← never reads directly from SportMind agents; always via application layer
  ← Example: useGovernanceVote hook reads pre-generated governance brief from bus

Third-party prediction markets
  ← subscribe to signal bus via webhook for pre_match_t2h signals
  ← use as intelligence context, not as executable instructions

LLMs (Claude/GPT-4/Gemini)
  ← called by agents for reasoning; consume SportMind context as system prompt
  ← LLM output validated against confidence schema before publishing to bus
  ← LLM is a reasoning component, not an orchestrator

Human operators
  ← receive escalation briefs from escalation channel
  ← monitor agent health via sportmind_agent_status MCP tool
  ← approve Level 0-1 actions
  ← never needed for Level 3-4 routine operation
```

---

## Compatibility

**Agent framework:** `core/autonomous-agent-framework.md` — lifecycle, safety, decision model
**Individual patterns:** `examples/agentic-workflows/README.md` — four base patterns
**MCP tools:** `platform/sportmind-mcp-server.md` — including sportmind_agent_status
**Real-time patterns:** `platform/realtime-integration-patterns.md` — live data integration
**Ecosystem:** `platform/integration-partners.md` — FanTokenIntel, SportFi Kit, LLMs

*MIT License · SportMind · sportmind.dev*
