# SportMind Agent Types

**Eleven types of agents you can build with SportMind intelligence.**

Five come from the standard AI taxonomy (Russell & Norvig). Six are native to the
sports intelligence domain — patterns that don't have names in academic literature
but are directly supported by SportMind's skill stack.

This document answers the question every developer asks first: *"What kind of agent
should I build?"* Pick the type that matches your use case, then follow the links to
the implementation.

---

## Quick routing guide

| If you want to... | Build this agent type | Complexity | Start here |
|---|---|---|---|
| React to a breaking news event or lineup change | Simple Reflex | ⭐ | [Type 1](#type-1) |
| Generate a pre-match signal with full context | Model-Based Reflex | ⭐⭐ | [Type 2](#type-2) |
| Monitor a portfolio and act toward a goal | Goal-Based | ⭐⭐⭐ | [Type 3](#type-3) |
| Rank options and choose the best across dimensions | Utility-Based | ⭐⭐⭐ | [Type 4](#type-4) |
| Build a calibration pipeline that improves over time | Learning | ⭐⭐⭐⭐ | [Type 5](#type-5) |
| Watch PATH_2 supply mechanics in real time | Supply Surveillance | ⭐⭐ | [Type 6](#type-6) |
| Monitor regulatory signals and classify them | Regulatory Watchdog | ⭐⭐⭐ | [Type 7](#type-7) |
| Detect narrative momentum building before it moves prices | Narrative Aggregator | ⭐⭐⭐ | [Type 8](#type-8) |
| Drive governance participation for the right holder archetypes | Governance Participation | ⭐⭐ | [Type 9](#type-9) |
| Generate commercial briefs for clubs, brands, or agents | Commercial Brief | ⭐⭐ | [Type 10](#type-10) |
| Track 8+ tokens simultaneously through a 39-day tournament | World Cup Multi-Entity | ⭐⭐⭐⭐⭐ | [Type 11](#type-11) |

---

## The architecture principle behind all eleven

Every SportMind agent follows the same separation:

```
SportMind        Intelligence layer — reasoning, signals, context
Data layer       Raw inputs — Chiliz Chain, live scores, social data
Agent framework  Execution layer — Claude, GPT-4o, LangChain, CrewAI
Application      What you do with the intelligence — notify, rank, verify
```

SportMind never executes. It reasons. Every agent type below produces
intelligence; your application decides what to do with it.

**The agent boundary is non-negotiable.** SportMind agents produce signals.
They do not execute trades, submit governance votes, or negotiate contracts.
The human decision point is architectural, not optional.

---

## Part 1 — The five standard architecture types

<a name="type-1"></a>
### Type 1 — Simple Reflex Agent

**What it is:** Acts on a single current percept. No memory. No model of the world.
`IF [condition] THEN [action]`. Fast, reliable, narrow.

**When to use it:** You need an agent that fires on one trigger and does one thing.
Lineup confirmed → run availability check. Weight cut detected → load MMA protocol.
Macro override → suspend all signals. Under five minutes to build.

**How SportMind implements it:**

```python
# Simple reflex agent — lineup change trigger
# No memory required. Fires on a single event.

import requests

SPORTMIND_API = "http://localhost:8080"

def on_lineup_confirmed(sport: str, team: str, kickoff: str):
    """
    Reactive rule: lineup confirmed → immediate pre-match signal update.
    SportMind reactive rules: IF lineup_confirmed THEN re-run signal.
    """
    response = requests.post(f"{SPORTMIND_API}/signal", json={
        "sport":   sport,
        "team":    team,
        "kickoff": kickoff,
        "trigger": "LINEUP_CONFIRMED"
    })
    signal = response.json()

    # Reactive action based on percept alone
    if signal["recommended_action"] == "ENTER":
        notify(f"ENTER signal confirmed after lineup: {team} {signal['adjusted_score']:.1f}")
    elif signal["flags"]["lineup_unconfirmed"]:
        notify(f"WARNING: lineup still unconfirmed at {team}")

def on_macro_override(override_type: str):
    """
    Reactive rule: macro override → suspend all active signals immediately.
    """
    if override_type == "CRYPTO_BEAR_CONFIRMED":
        suspend_all_signals(reason="macro_override_active")
        notify("All signals suspended — macro override active")

def on_weight_miss(fighter: str, bout: str):
    """
    Reactive rule: MMA weight miss → load weight-cut protocol immediately.
    """
    response = requests.get(f"{SPORTMIND_API}/stack", params={
        "sport": "mma",
        "context": "weight_miss",
        "fighter": fighter
    })
    protocol = response.json()
    notify(f"WEIGHT MISS: {fighter} — {protocol['weight_cut_signal']}")
```

**SportMind files:**
- `core/breaking-news-intelligence.md` — reactive trigger taxonomy
- `core/temporal-awareness.md` — freshness flags as reactive conditions
- `core/contextual-signal-environment.md` — environmental overrides

**Autonomy level:** 0–1. Reactive agents always escalate to human review.
They act on percepts, not plans.

---

<a name="type-2"></a>
### Type 2 — Model-Based Reflex Agent

**What it is:** Maintains an internal model of the world and acts based on
that model combined with current percepts. SportMind's skill library *is*
the world model.

**When to use it:** This is SportMind's primary architecture and where the
most useful agents live. Any pre-match signal agent, fan token monitor, or
transfer intelligence agent is a model-based reflex agent. The agent's
"world model" is the five-layer skill stack — macro → market → sport domain
→ athlete → fan token.

**Why SportMind is this architecture:** The skill library encodes what a
well-informed sports analyst knows about the world. When an agent loads
`sports/football/sport-domain-football.md` + `athlete/football/athlete-intel-football.md`,
it is updating its internal model before reasoning. The six-step signal chain
is a model-based reflex loop.

**How SportMind implements it:**

```python
# Model-based reflex agent — full pre-match signal with world model
# The agent's world model = SportMind skill stack

import requests

SPORTMIND_API = "http://localhost:8080"

class PreMatchAgent:
    """
    Model-based reflex agent for pre-match intelligence.
    World model: SportMind five-layer skill stack.
    """

    def __init__(self, sport: str):
        self.sport = sport
        self.world_model = self._load_world_model()

    def _load_world_model(self) -> dict:
        """Load the sport-specific world model from SportMind."""
        response = requests.get(f"{SPORTMIND_API}/stack", params={
            "sport": self.sport
        })
        return response.json()  # Returns all five layers as structured context

    def analyse(self, home_team: str, away_team: str,
                competition: str, kickoff: str) -> dict:
        """
        Core reflex: percept (match context) + world model → action (signal).
        """
        # Step 1: Update world model with macro state
        macro = requests.get(f"{SPORTMIND_API}/macro").json()

        # Step 2: If macro override active, suspend — reactive rule fires
        if macro["macro_override_active"]:
            return {"recommended_action": "ABSTAIN",
                    "reason": "macro_override_active"}

        # Step 3: Generate signal using world model + current percept
        signal = requests.post(f"{SPORTMIND_API}/signal", json={
            "sport":       self.sport,
            "home_team":   home_team,
            "away_team":   away_team,
            "competition": competition,
            "kickoff":     kickoff,
            "world_model": self.world_model
        }).json()

        # Step 4: Model-based reflex — use world model to interpret signal
        if signal["sms"] < 60:
            signal["recommended_action"] = "WAIT"
            signal["reason"] = "SMS below threshold — insufficient model confidence"

        return signal

    def update_model(self, new_information: dict):
        """
        Update the world model when new information arrives.
        e.g. injury news, lineup change, manager sacking.
        """
        self.world_model.update(new_information)
```

**SportMind files:**
- `core/reasoning-patterns.md` — six-step signal chain
- `core/opponent-tendency-intelligence.md` — historical model of opponent behaviour
- `fan-token/football-token-intelligence/` — fan token world model
- `core/context-window-management.md` — managing model size in context

**Autonomy level:** 1–3. Model-based agents can operate semi-autonomously
within clearly defined boundaries.

---

<a name="type-3"></a>
### Type 3 — Goal-Based Agent

**What it is:** Has an explicit goal and reasons about which sequences of
actions achieve it. Unlike reflex agents, it plans rather than just reacts.

**When to use it:** You want an agent that monitors a portfolio over time,
manages a tournament tracker across weeks, or runs a continuous watch cycle
toward a defined objective. The agent needs to ask: "Does this action move
me toward my goal?"

**SportMind goals are always ENTER / WAIT / ABSTAIN.** The goal framework
defines terminal goals (what you ultimately want), instrumental goals
(what you need to achieve that), and immediate goals (the next action
to take). SportMind's autonomy levels 0–4 define how independently the
agent pursues the goal chain.

**How SportMind implements it:**

```python
# Goal-based agent — fan token portfolio monitor
# Goal: maintain ENTER signals only when all conditions are met
# Uses SportMind agent-goal-framework.md

import schedule
import time
import requests

SPORTMIND_API = "http://localhost:8080"

class PortfolioGoalAgent:
    """
    Goal-based agent for fan token portfolio monitoring.
    Terminal goal: optimal ENTER/WAIT/ABSTAIN across all held tokens.
    Instrumental goal: track macro + sport + token state continuously.
    Immediate goal: at each cycle, check each token and update recommendation.
    """

    def __init__(self, tokens: list[str], autonomy_level: int = 2):
        self.tokens = tokens
        self.autonomy_level = autonomy_level  # 0=supervised → 4=fully autonomous
        self.goal_state = {t: "UNKNOWN" for t in tokens}
        self.memory = {}

    def run_goal_cycle(self):
        """Execute one goal cycle across all held tokens."""

        # Instrumental goal: check macro first (gates everything else)
        macro = requests.get(f"{SPORTMIND_API}/macro").json()
        if macro["macro_override_active"]:
            # Goal blocked — macro override suspends all ENTER signals
            for token in self.tokens:
                self.goal_state[token] = "WAIT"
            self._escalate_if_needed("macro_override_active")
            return

        # Instrumental goal: check each token
        for token in self.tokens:
            signal = requests.get(f"{SPORTMIND_API}/fan-token", params={
                "token": token,
                "include_lifecycle": True,
                "include_gamified":  True
            }).json()

            # Goal evaluation: does this token meet ENTER criteria?
            new_state = self._evaluate_goal(signal)

            # State transition: has the goal state changed?
            if new_state != self.goal_state[token]:
                self._handle_transition(token, self.goal_state[token], new_state)
                self.goal_state[token] = new_state

    def _evaluate_goal(self, signal: dict) -> str:
        """Evaluate whether the current signal state achieves the terminal goal."""
        if signal.get("macro_override"):      return "ABSTAIN"
        if signal.get("mrs_score", 0) >= 75:  return "ABSTAIN"  # fraud signal
        if signal.get("sms", 0) < 60:         return "WAIT"
        if signal.get("recommended_action") == "ENTER":
            return "ENTER"
        return "WAIT"

    def _handle_transition(self, token: str, old: str, new: str):
        """Handle goal state transitions. Escalate if autonomy level requires it."""
        print(f"{token}: {old} → {new}")
        if self.autonomy_level <= 1:
            # Levels 0-1: always escalate transitions to human
            self._escalate(token, old, new)
        elif self.autonomy_level == 2:
            # Level 2: act on WAIT/ABSTAIN; escalate on ENTER
            if new == "ENTER":
                self._escalate(token, old, new)
        # Levels 3-4: act autonomously within hard boundaries

    def _escalate(self, token, old, new):
        print(f"ESCALATION REQUIRED: {token} {old}→{new} — human review needed")

    def _escalate_if_needed(self, reason):
        print(f"ESCALATION: {reason}")

# Schedule: run goal cycle every 4 hours
agent = PortfolioGoalAgent(tokens=["AFC", "PSG", "BAR"], autonomy_level=2)
schedule.every(4).hours.do(agent.run_goal_cycle)
```

**SportMind files:**
- `core/agent-goal-framework.md` — terminal/instrumental/immediate goal hierarchy
- `core/autonomous-agent-framework.md` — autonomy levels 0–4
- `examples/agentic-workflows/README.md` (Pattern 1) — continuous portfolio monitor

**Autonomy level:** 1–4 depending on configuration.

---

<a name="type-4"></a>
### Type 4 — Utility-Based Agent

**What it is:** Doesn't just ask "does this achieve the goal?" but "which
option *maximises value* across multiple competing dimensions?" It assigns
a utility score to outcomes and chooses the highest-utility action.

**When to use it:** Scouting (rank 20 transfer targets by composite value),
portfolio optimisation (which tokens to hold given budget constraints and
LTUI trajectories), fan token comparison (8 tokens with different lifecycle
phases, PATH_2 status, and CDI levels — which deserves the ENTER signal?).

**SportMind's named metrics are utility functions.** DQI, CVS, ARI, CQS,
TMAS — each is a multi-variable composite that trades off competing
dimensions and produces a score. A utility-based agent chains these
composites together to make a ranked decision.

**How SportMind implements it:**

```python
# Utility-based agent — Moneyball scouting agent
# Ranks transfer targets by composite value across four dimensions
# Uses sc_cvs_brief, sc_dqi, sc_system_fit, sc_valuation (MCP)

import requests

SPORTMIND_API = "http://localhost:8080"

class ScoutingUtilityAgent:
    """
    Utility-based agent for transfer target ranking.
    Utility function: CVS = performance × commercial × system_fit × risk.
    Dimension weights are configurable per club's priorities.
    """

    # Default utility weights — adjust per club's priorities
    UTILITY_WEIGHTS = {
        "performance":   0.35,  # DQI, stats, form
        "commercial":    0.25,  # ATM, AELS, ABS
        "system_fit":    0.25,  # TMAS, positional need
        "risk":          0.15   # age, injury, contract (inverse — lower = better)
    }

    def rank_targets(self, candidates: list[dict],
                     target_system: str) -> list[dict]:
        """
        Rank transfer targets by composite utility score.
        Returns candidates sorted highest utility first.
        """
        scored = []
        for candidate in candidates:
            utility = self._compute_utility(candidate, target_system)
            scored.append({**candidate, "utility_score": utility})

        # Sort descending by utility
        return sorted(scored, key=lambda x: x["utility_score"], reverse=True)

    def _compute_utility(self, candidate: dict, target_system: str) -> float:
        """Compute composite utility for one candidate."""

        # Dimension 1: Performance (DQI)
        dqi = requests.get(f"{SPORTMIND_API}/sc/dqi", params={
            "player":    candidate["name"],
            "position":  candidate["position"]
        }).json()
        perf_score = dqi["dqi_score"] / 100  # normalise 0-1

        # Dimension 2: Commercial value (ABS + AELS)
        commercial = requests.get(f"{SPORTMIND_API}/sc/cvs", params={
            "player": candidate["name"]
        }).json()
        comm_score = commercial["commercial_dimension"]["score"] / 100

        # Dimension 3: System fit (TMAS)
        fit = requests.get(f"{SPORTMIND_API}/sc/system-fit", params={
            "player":         candidate["name"],
            "target_system":  target_system
        }).json()
        fit_score = fit["fit_score"] / 100

        # Dimension 4: Risk (inverse — lower risk = higher utility)
        risk_score = 1.0 - (commercial["risk_dimension"]["score"] / 100)

        # Weighted utility function
        utility = (
            self.UTILITY_WEIGHTS["performance"] * perf_score +
            self.UTILITY_WEIGHTS["commercial"]  * comm_score +
            self.UTILITY_WEIGHTS["system_fit"]  * fit_score +
            self.UTILITY_WEIGHTS["risk"]        * risk_score
        )

        # UNDERVALUED flag: if DQI-adjusted value > market value, boost utility
        if dqi.get("undervalued_flag"):
            utility *= 1.10  # 10% utility bonus for undervalued targets

        return round(utility, 4)

# Usage
agent = ScoutingUtilityAgent()
candidates = [
    {"name": "Viktor Gyökeres", "position": "ST"},
    {"name": "Benjamin Šeško",  "position": "ST"},
    {"name": "Rasmus Højlund",  "position": "ST"},
]
ranked = agent.rank_targets(candidates, target_system="high_press_4-3-3")
for i, t in enumerate(ranked, 1):
    print(f"{i}. {t['name']}: utility={t['utility_score']:.3f}")
```

**SportMind files:**
- `core/athlete-decision-intelligence.md` — DQI formula and UNDERVALUED flag
- `core/tactical-matchup-intelligence.md` — TMAS system fit scoring
- `core/athlete-readiness-index.md` — ARI as readiness utility function
- `scripts/sportmind_sc_mcp.py` — scouting MCP tools
- `examples/agentic-workflows/scouting-agent.md` — Pattern 10

**Autonomy level:** 2–3. Rankings are advisory; transfer decisions require human approval.

---

<a name="type-5"></a>
### Type 5 — Learning Agent

**What it is:** Improves its performance over time based on feedback.
Modifies its behaviour or knowledge in response to outcomes.

**The honest framing for SportMind:** Learning is intentionally human-mediated.
Agents don't learn autonomously — a human reviews calibration records and the
library recalibrates at milestone thresholds (100-record, 120-record, 150-record).
This is a deliberate design choice. Unauditable autonomous drift is a risk,
not a feature. The calibration pipeline *is* the learning system.

**When to use it:** You want to build the calibration feedback loop — submit
predictions before real events, record outcomes, and contribute to the
modifier recalibration that improves SportMind's accuracy over time. The
library's 96% direction accuracy came from exactly this process.

**How SportMind implements it:**

```python
# Learning agent — calibration pipeline
# Submits predictions, records outcomes, feeds modifier recalibration
# Uses community/calibration-data/ + core/calibration-framework.md

import json
import requests
from datetime import datetime
from pathlib import Path

SPORTMIND_API = "http://localhost:8080"
CALIBRATION_DIR = Path("community/calibration-data")

class CalibrationAgent:
    """
    Learning agent for SportMind calibration.

    The learning loop:
      1. Generate pre-match signal (before the event)
      2. Record the prediction with all metadata
      3. After the event, record the actual outcome
      4. Submit the complete record for library recalibration

    Wrong predictions are as valuable as correct ones.
    The library learns from both.
    """

    def predict(self, sport: str, home: str, away: str,
                competition: str, kickoff: str) -> dict:
        """Step 1: Generate and record a prediction before the event."""

        signal = requests.post(f"{SPORTMIND_API}/signal", json={
            "sport": sport, "home_team": home,
            "away_team": away, "competition": competition,
            "kickoff": kickoff
        }).json()

        record = {
            "id":          f"{sport}_{home}_{away}_{kickoff[:10]}",
            "sport":       sport,
            "home":        home,
            "away":        away,
            "competition": competition,
            "kickoff":     kickoff,
            "submitted_at": datetime.utcnow().isoformat(),
            "prediction": {
                "direction":      signal["direction"],
                "adjusted_score": signal["adjusted_score"],
                "sms":            signal["sms"],
                "modifiers":      signal.get("modifiers_applied", {})
            },
            "outcome": None  # filled in after the event
        }

        # Save prediction before event
        path = CALIBRATION_DIR / f"{record['id']}_prediction.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record, indent=2))

        print(f"Prediction recorded: {home} vs {away} → {signal['direction']}")
        return record

    def record_outcome(self, record_id: str, actual_result: str,
                       home_score: int, away_score: int):
        """Step 2: After the event, record what actually happened."""

        pred_path = CALIBRATION_DIR / f"{record_id}_prediction.json"
        record = json.loads(pred_path.read_text())

        record["outcome"] = {
            "actual_result":   actual_result,  # "HOME" / "AWAY" / "DRAW"
            "home_score":      home_score,
            "away_score":      away_score,
            "recorded_at":     datetime.utcnow().isoformat(),
            "direction_correct": actual_result == record["prediction"]["direction"]
        }

        # Save completed record
        complete_path = CALIBRATION_DIR / f"{record_id}_complete.json"
        complete_path.write_text(json.dumps(record, indent=2))

        status = "✅ CORRECT" if record["outcome"]["direction_correct"] else "❌ WRONG"
        print(f"{status}: {record['home']} vs {record['away']}")
        print(f"  Predicted: {record['prediction']['direction']} | Actual: {actual_result}")

        return record

    def submit_for_recalibration(self, record_id: str):
        """
        Step 3: Submit complete record to SportMind calibration.
        HUMAN REVIEW required before modifier updates apply.
        """
        complete_path = CALIBRATION_DIR / f"{record_id}_complete.json"
        record = json.loads(complete_path.read_text())

        if record.get("outcome") is None:
            raise ValueError("Cannot submit — outcome not yet recorded")

        response = requests.post(f"{SPORTMIND_API}/calibration/submit",
                                 json=record)
        print(f"Submitted to calibration. Human review required before modifiers update.")
        return response.json()
```

**SportMind files:**
- `core/calibration-framework.md` — how predictions become modifiers
- `community/calibration-data/` — 126 existing records to learn from
- `community/calibration-data/CONTRIBUTING.md` — submission guidelines
- `core/modifier-recalibration-v3.md` through `v6.md` — milestone recalibrations

**Autonomy level:** 0–1. All learning is human-mediated by design.

---

## Part 2 — Six SportMind-native agent types

These don't have names in standard AI taxonomy. They emerge directly from
SportMind's intelligence stack.

---

<a name="type-6"></a>
### Type 6 — Supply Surveillance Agent

**What it is:** Watches PATH_2 Fan Token™ Play mechanics in real time — detects
treasury pre-liquidations at T-48h, verifies burn events post-match, and
raises flags when supply behaviour deviates from protocol expectations.

**Why it exists:** PATH_2 creates a detectable on-chain signal *before* the
match (the treasury pre-liquidation at T-48h). Standard models see this as
anomalous distribution. A supply surveillance agent knows it is a protocol
event and interprets it correctly. It also closes the loop post-match:
was the expected burn confirmed? Was there a BURN_ANOMALY?

**How SportMind implements it:**

```python
# Supply surveillance agent — PATH_2 Fan Token Play monitor
# Detects pre-liquidations, verifies burns, raises anomalies
# Uses wa_supply_verify + ft_token_state (MCP)

import schedule, time, requests
from datetime import datetime, timezone

SPORTMIND_MCP  = "http://localhost:3001"  # sportmind_mcp
SPORTMIND_FT   = "http://localhost:3002"  # sportmind_ft_mcp
SPORTMIND_WA   = "http://localhost:3008"  # sportmind_wa_mcp

MONITORED_TOKENS = ["AFC"]  # Expand as new PATH_2 tokens confirm

class SupplySurveillanceAgent:
    """
    Watches PATH_2 mechanics for confirmed Fan Token Play tokens.
    Phases monitored:
      T-48h: treasury pre-liquidation (PROTOCOL_EVENT — never bearish)
      T+30min: initial burn verification (AMM settling)
      T+6h:    definitive verification
      T+24h:   BURN_MISSING flag if not yet confirmed
    """

    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.match_log = {}  # token → {match_id, pre_liquidation, burn_status}

    def check_pre_liquidation(self, token: str):
        """T-48h check: has the treasury pre-liquidated?"""
        response = requests.get(f"{SPORTMIND_WA}/supply-verify", params={
            "token": token,
            "phase": "pre_match"
        }).json()

        if response.get("pre_liquidation_detected"):
            # PROTOCOL_EVENT — never treat as bearish distribution
            print(f"[{token}] PRE-LIQUIDATION DETECTED — PATH_2 active for next match")
            print(f"  Amount: {response['pre_liquidation_pct']:.3f}% of supply")
            print(f"  AGENT RULE: This is a PROTOCOL_EVENT. Not a whale sell.")
            self.match_log[token] = {
                "pre_liquidation": True,
                "pre_liquidation_pct": response["pre_liquidation_pct"],
                "checked_at": datetime.utcnow().isoformat()
            }

    def verify_post_match(self, token: str, result: str, hours_since: float):
        """Post-match: verify burn or mint occurred as expected."""

        if hours_since < 0.25:
            print(f"[{token}] Too early — AMM rebalancing not complete. Retry at T+30min.")
            return

        verify = requests.get(f"{SPORTMIND_WA}/supply-verify", params={
            "token":        token,
            "match_result": result,
            "hours_since":  hours_since
        }).json()

        status = verify["verification_status"]
        print(f"[{token}] Post-match supply verification: {status}")

        if status == "BURN_CONFIRMED":
            print(f"  ✅ Burn confirmed: {verify['burn_pct']:.4f}% supply reduction")
        elif status == "BURN_PENDING":
            print(f"  ⏳ Burn pending — retry at T+6h")
        elif status == "BURN_ANOMALY":
            print(f"  ❌ BURN_ANOMALY — supply change outside expected range")
            self._escalate(token, "BURN_ANOMALY", verify)
        elif status == "UNEXPECTED_SUPPLY_CHANGE":
            print(f"  ❌ Supply changed on LOSS result — ESCALATE IMMEDIATELY")
            self._escalate(token, "UNEXPECTED_SUPPLY_CHANGE", verify)

    def _escalate(self, token: str, flag: str, data: dict):
        print(f"ESCALATION REQUIRED: {token} — {flag}")
        print(f"  Data: {data}")
        # Send to human review queue

# Schedule surveillance
agent = SupplySurveillanceAgent(tokens=MONITORED_TOKENS)
schedule.every(30).minutes.do(lambda: [
    agent.check_pre_liquidation(t) for t in MONITORED_TOKENS
])
```

**SportMind files:**
- `fan-token/gamified-tokenomics-intelligence/` — PATH_2 protocol mechanics
- `platform/web-agent-connectors.md` — wa_supply_verify connector
- `platform/chiliz-chain-address-intelligence.md` — wallet identification
- `scripts/sportmind_wa_mcp.py` (port 3008) — wa_supply_verify tool

**Autonomy level:** 3. Surveillance runs autonomously; anomalies escalate to human.

---

<a name="type-7"></a>
### Type 7 — Regulatory Watchdog Agent

**What it is:** Monitors Tier 1 regulatory sources (ESMA, SEC/CFTC, Chiliz
official blog) for signals that change the macro intelligence framework.
Classifies new content using SportMind's three-tier intake framework.
Escalates to human review before any library update.

**Why it exists:** The fan token landscape is changing rapidly — MiCA registered
April 2026, SEC/CFTC joint guidance March 2026, US market opening. A regulatory
change that isn't reflected in the macro files produces wrong signals across
the entire library. This agent keeps the regulatory layer current.

**Hard rule:** This agent never updates the library automatically. Human review
is always required. The agent classifies and escalates — it does not act.

**How SportMind implements it:**

```python
# Regulatory watchdog agent — monitors Tier 1 sources for macro changes
# Uses wa_macro_monitor (MCP) + core/external-intelligence-intake.md

import schedule, time, requests, hashlib, json
from pathlib import Path

SPORTMIND_WA = "http://localhost:3008"

class RegulatoryWatchdogAgent:
    """
    Monitors regulatory sources and classifies new content.

    Tiers (from core/external-intelligence-intake.md):
      Tier 1: Act within 24h — ESMA, SEC/CFTC, Chiliz official
      Tier 2: Review within 72h — industry press, legal analysis
      Tier 3: Monitor — secondary sources, speculation

    HARD RULE: Never auto-update the library. Human review always required.
    """

    def __init__(self):
        self.seen_hashes = set()
        self.findings_queue = []

    def run_monitoring_cycle(self, tier: str = "1"):
        """Fetch monitoring targets and check for new content."""

        targets = requests.get(f"{SPORTMIND_WA}/macro-monitor", params={
            "tier": tier
        }).json()

        for source in targets.get("tier_1_sources", []):
            self._check_source(source)

    def _check_source(self, source: dict):
        """Check a single source for new content."""
        try:
            response = requests.get(source["url"], timeout=10)
            content_hash = hashlib.md5(response.text.encode()).hexdigest()

            if content_hash not in self.seen_hashes:
                self.seen_hashes.add(content_hash)
                self._classify_and_escalate(source, response.text)
        except Exception as e:
            print(f"Source unavailable: {source['name']} — {e}")

    def _classify_and_escalate(self, source: dict, content: str):
        """Classify new content and add to escalation queue."""

        finding = {
            "source":        source["name"],
            "url":           source["url"],
            "content_preview": content[:500],
            "library_file":  source.get("library_file_to_update"),
            "tier":          source.get("tier", "1"),
            "human_required": True  # always
        }

        # Pattern matching for common regulatory signals
        content_lower = content.lower()
        if any(term in content_lower for term in
               ["fan token", "digital asset", "utility token", "sportfi"]):
            finding["relevance"] = "HIGH — fan token / SportFi mention"
        elif any(term in content_lower for term in
                 ["crypto", "blockchain", "defi", "mica"]):
            finding["relevance"] = "MODERATE — general crypto regulation"
        else:
            finding["relevance"] = "LOW — indirect relevance"

        self.findings_queue.append(finding)
        print(f"NEW CONTENT: {source['name']} [{finding['relevance']}]")
        print(f"  Possible update needed: {finding['library_file']}")
        print(f"  HUMAN REVIEW REQUIRED before any library change")

# Schedule
agent = RegulatoryWatchdogAgent()
schedule.every().day.at("09:00").do(agent.run_monitoring_cycle, tier="1")
schedule.every().monday.at("09:00").do(agent.run_monitoring_cycle, tier="2")
```

**SportMind files:**
- `core/external-intelligence-intake.md` — three-tier classification framework
- `platform/web-agent-connectors.md` — wa_macro_monitor connector
- `macro/macro-regulatory-sportfi.md` — the file this agent protects
- `scripts/sportmind_wa_mcp.py` (port 3008) — wa_macro_monitor tool

**Autonomy level:** 2. Monitors autonomously; ALL findings require human review.

---

<a name="type-8"></a>
### Type 8 — Narrative Signal Aggregator

**What it is:** Monitors social volume, KOL tier signals, and media velocity
to detect when narrative momentum is building before it moves token prices.
The key insight: narrative builds 48–72h before peak token trading activity.
This agent detects it early.

**Why it exists:** A standard token monitor looks at on-chain data and match
signals. It misses the narrative layer — the revenge fixture, the record
chase, the comeback story — that drives 3–8% additional signal on top of
pure statistics. This agent catches that signal before the market prices it in.

**How SportMind implements it:**

```python
# Narrative signal aggregator
# Detects narrative momentum building before it affects token prices
# Uses social-intelligence-connector + core/core-narrative-momentum.md

import requests, re
from datetime import datetime

SPORTMIND_API = "http://localhost:8080"

# Tier 1 KOL accounts (from platform/social-intelligence-connector.md)
TIER_1_KOLS = [
    "FabrizioRomano",     # Transfer news — KIS score 96
    "David_Ornstein",     # Arsenal specific
    "OptaJoe",            # Statistical signals
]

class NarrativeAggregatorAgent:
    """
    Detects narrative momentum before it moves prices.

    Signal sources:
      1. Social volume spike (3× baseline = high narrative intensity)
      2. KOL Tier 1 mentions of specific clubs/players
      3. Media language patterns (revenge/record/comeback/must-win)
      4. Ticket demand signals (sold-out = narrative_active flag)

    Output: narrative_score 0-100 + narrative_category (1-8)
    """

    NARRATIVE_KEYWORDS = {
        "revenge":     ["revenge", "payback", "righting the wrong", "rematch"],
        "record":      ["historic", "record", "milestone", "never before", "first ever"],
        "comeback":    ["return", "redemption", "proves critics", "back from"],
        "rivalry":     ["derby", "local rivals", "more than a game"],
        "must_win":    ["must win", "do or die", "final chance", "survival"],
        "elimination": ["elimination", "knocked out", "last chance", "knocked out"],
    }

    def assess_narrative(self, sport: str, home: str,
                         away: str, kickoff: str) -> dict:
        """Assess narrative intensity for a fixture."""

        # Step 1: Social volume check
        social = requests.get(f"{SPORTMIND_API}/social/volume", params={
            "entities": [home, away],
            "hours": 72
        }).json()

        volume_multiplier = social.get("volume_vs_baseline", 1.0)

        # Step 2: Media language scan
        previews = requests.get(f"{SPORTMIND_API}/media/previews", params={
            "home": home, "away": away
        }).json()

        detected_categories = []
        for category, keywords in self.NARRATIVE_KEYWORDS.items():
            text = " ".join(previews.get("headlines", [])).lower()
            if any(k in text for k in keywords):
                detected_categories.append(category)

        # Step 3: Score the narrative (from core-narrative-momentum.md)
        narrative_score = self._score_narrative(
            volume_multiplier, detected_categories
        )

        # Step 4: Fan token implication
        token_implication = "none"
        if narrative_score >= 70:
            token_implication = "HIGH — 48-72h pre-event window; elevated trading expected"
        elif narrative_score >= 40:
            token_implication = "MODERATE — monitor social volume; CDI extension likely"

        result = {
            "fixture":             f"{home} vs {away}",
            "narrative_score":     narrative_score,
            "narrative_active":    narrative_score >= 40,
            "categories_detected": detected_categories,
            "volume_vs_baseline":  volume_multiplier,
            "token_implication":   token_implication,
            "maximum_modifier":    "±8% (SportMind cap — narrative never overrides strong adverse signals)"
        }

        if narrative_score >= 70:
            print(f"HIGH NARRATIVE: {home} vs {away} — score {narrative_score}")
            print(f"  Categories: {detected_categories}")
            print(f"  Token window opens now (T-72h)")

        return result

    def _score_narrative(self, volume_mult: float,
                         categories: list) -> int:
        base = 0
        if volume_mult >= 3.0: base += 40
        elif volume_mult >= 2.0: base += 20
        elif volume_mult >= 1.5: base += 10

        # Primary narrative
        if categories:
            base += 30
        # Secondary narratives (diminishing returns)
        if len(categories) >= 2:
            base += 15
        if len(categories) >= 3:
            base += 10

        return min(base, 100)
```

**SportMind files:**
- `core/core-narrative-momentum.md` — eight taxonomy categories + modifiers
- `platform/social-intelligence-connector.md` — X API v2 + LunarCrush
- `fan-token/kol-influence-intelligence/` — KIS scoring, Tier 1 accounts
- `core/media-intelligence.md` — media language detection

**Autonomy level:** 2–3. Signal generation is autonomous; position decisions require human.

---

<a name="type-9"></a>
### Type 9 — Governance Participation Agent

**What it is:** Monitors active fan token governance votes, evaluates proposal
quality, scores GSI (Governance Signal Index), and sends targeted notifications
to the right holder archetypes at the right times. Its output is community
engagement, not a trading signal.

**Why it's a distinct type:** Governance agents are fundamentally different
from signal-chain agents. They don't produce ENTER/WAIT/ABSTAIN. They produce
engagement actions — who to notify, when, with what message, based on the
proposal quality and archetype distribution. Wrong notifications drive churn;
right ones drive governance health.

**How SportMind implements it:**

```python
# Governance participation agent
# Drives fan token governance engagement for the right archetypes
# Uses gc_governance_state + gc_vote_alert (MCP, port 3005)

import requests
from datetime import datetime, timedelta

SPORTMIND_GC = "http://localhost:3005"

# Holder archetype notification rules (from fan-holder-profile-intelligence.md)
ARCHETYPE_RULES = {
    "GOVERNOR":   {"notify": True,  "timing": "T-72h",  "channel": "email+push"},
    "LOYALIST":   {"notify": True,  "timing": "T-48h",  "channel": "push"},
    "SPECULATOR": {"notify": False, "timing": None,      "channel": None},
    "AMPLIFIER":  {"notify": True,  "timing": "result",  "channel": "push"},
}

class GovernanceParticipationAgent:
    """
    Drives governance engagement without driving churn.

    Core principle: vote quality determines notification intensity.
    Substantive votes (kit design, charity partner, matchday decisions)
    justify Governor + Loyalist engagement. Trivial votes justify nothing.
    Speculators are never notified — they don't vote.
    """

    def assess_and_notify(self, token: str):
        """Assess active vote and send appropriate notifications."""

        gov_state = requests.get(f"{SPORTMIND_GC}/governance-state", params={
            "token": token
        }).json()

        if not gov_state.get("active_vote"):
            return  # No active vote — nothing to do

        vote = gov_state["active_vote"]
        gsi  = gov_state["gsi_score"]

        # Assess vote quality (is this worth notifying about?)
        quality = self._assess_vote_quality(vote, gsi)

        if quality == "TRIVIAL":
            print(f"[{token}] Vote quality TRIVIAL — no notifications sent")
            print(f"  Reason: trivial votes damage governor trust")
            return

        # Build notification sequence
        sequence = self._build_notification_sequence(vote, quality)

        print(f"[{token}] Vote: {vote['topic']}")
        print(f"  Quality: {quality} | GSI: {gsi}")
        print(f"  Notification sequence: {len(sequence)} touchpoints")

        for notification in sequence:
            self._send_notification(token, notification)

    def _assess_vote_quality(self, vote: dict, gsi: int) -> str:
        """Determine if this vote is worth notifying holders about."""
        topic = vote.get("topic", "").lower()

        # High-quality vote signals
        substantive_terms = [
            "kit", "charity", "matchday", "stadium", "sponsor",
            "training", "community", "foundation", "experience"
        ]

        if any(term in topic for term in substantive_terms):
            return "SUBSTANTIVE"
        elif gsi >= 70:
            return "STANDARD"
        elif "test" in topic or "placeholder" in topic:
            return "TRIVIAL"
        else:
            return "STANDARD"

    def _build_notification_sequence(self, vote: dict, quality: str) -> list:
        """Build archetype-targeted notification sequence."""
        close_time = datetime.fromisoformat(vote["closes_at"])
        sequence = []

        for archetype, rules in ARCHETYPE_RULES.items():
            if not rules["notify"]:
                continue  # Speculators never notified

            if rules["timing"] == "T-72h":
                notify_at = close_time - timedelta(hours=72)
            elif rules["timing"] == "T-48h":
                notify_at = close_time - timedelta(hours=48)
            elif rules["timing"] == "result":
                notify_at = close_time + timedelta(hours=2)
            else:
                continue

            sequence.append({
                "archetype":  archetype,
                "notify_at":  notify_at.isoformat(),
                "channel":    rules["channel"],
                "message":    self._build_message(archetype, vote, quality)
            })

        return sorted(sequence, key=lambda x: x["notify_at"])

    def _build_message(self, archetype: str, vote: dict, quality: str) -> str:
        if archetype == "GOVERNOR":
            return f"Active vote: {vote['topic']} — your voice shapes this decision"
        elif archetype == "LOYALIST":
            return f"Vote open: {vote['topic']} — {vote.get('hours_remaining', '48')}h remaining"
        elif archetype == "AMPLIFIER":
            return f"Community voted on: {vote['topic']} — share the result"
        return ""

    def _send_notification(self, token: str, notification: dict):
        print(f"  → [{notification['archetype']}] at {notification['notify_at']}: {notification['message'][:60]}")
```

**SportMind files:**
- `fan-token/sports-governance-intelligence/` — GSI framework
- `fan-token/fan-holder-profile-intelligence.md` — archetype targeting rules
- `platform/fan-engagement-connector.md` — engagement action templates
- `scripts/sportmind_gc_mcp.py` (port 3005) — gc_governance_state, gc_vote_alert

**Autonomy level:** 2–3. Notification timing is autonomous; governance strategy is human.

---

<a name="type-10"></a>
### Type 10 — Commercial Brief Agent

**What it is:** Generates structured commercial intelligence documents for
clubs, brands, sports agents, and commercial directors. Its output is a
*brief*, not a trading signal. ABS (Athlete Brand Score), APS (Athlete
Portability Score), AELS, TVS, DLVS — combined into a single deliverable.

**Why it's distinct:** Commercial brief agents don't produce ENTER/WAIT/ABSTAIN.
They produce structured content for human decision-makers. A sports agent
needs a concise APS brief on a transfer target. A brand needs an AFS (Audience
Fit Score) for a sponsorship decision. A club commercial director needs a BVS
(Broadcast Value Signal) brief for rights negotiations. This agent generates
those documents from SportMind intelligence.

**How SportMind implements it:**

```python
# Commercial brief agent
# Generates structured commercial intelligence for clubs/brands/agents
# Uses bc_ + sc_ MCP servers (ports 3004, 3006)

import requests
from datetime import datetime

SPORTMIND_BC = "http://localhost:3004"
SPORTMIND_SC = "http://localhost:3006"

class CommercialBriefAgent:
    """
    Generates commercial intelligence briefs.
    Output: structured document, not a trading signal.
    """

    def athlete_brief(self, player: str, context: str = "transfer") -> dict:
        """Generate a full commercial brief for an athlete."""

        # ABS — athlete brand value
        brand = requests.get(f"{SPORTMIND_SC}/cvs-brief", params={
            "player": player
        }).json()

        # AELS — social lift score
        social = brand.get("commercial_dimension", {})

        # APS — portability (does brand value travel with the player?)
        portability = requests.get(f"{SPORTMIND_SC}/valuation", params={
            "player": player
        }).json()

        brief = {
            "player":           player,
            "generated_at":     datetime.utcnow().isoformat(),
            "brief_type":       context,

            "brand_score": {
                "abs":       social.get("abs_score"),
                "aels":      social.get("aels"),
                "social_m":  social.get("social_following_m"),
                "summary":   f"Brand value: {social.get('abs_score', 0)}/100"
            },

            "portability": {
                "aps":     portability.get("aps_score"),
                "summary": "Brand transfers with player" if portability.get("aps_score", 0) >= 70
                           else "Brand is club-specific — value may not port"
            },

            "commercial_value": {
                "market_value_m":  portability.get("market_value_m"),
                "dqi_adjusted_m":  portability.get("dqi_adjusted_value_m"),
                "gap":             portability.get("valuation_gap"),
                "undervalued":     portability.get("undervalued_flag", False)
            },

            "fan_token_impact": brand.get("fan_token_impact"),

            "agent_boundary":
                "This brief is intelligence. Contract negotiations and "
                "commercial decisions are application-layer."
        }

        return brief

    def broadcast_brief(self, sport: str, competition: str,
                        home: str, away: str) -> dict:
        """Generate a broadcast value brief for rights holders."""

        bvs = requests.get(f"{SPORTMIND_BC}/broadcast-value", params={
            "sport": sport, "competition": competition,
            "home_club": home, "away_club": away
        }).json()

        cqs = requests.get(f"{SPORTMIND_BC}/context-quality", params={
            "sport": sport, "competition": competition
        }).json()

        return {
            "fixture":          f"{home} vs {away}",
            "competition":      competition,
            "bvs_score":        bvs.get("bvs_score"),
            "bvs_label":        bvs.get("commercial_tier"),
            "cqs_score":        cqs.get("cqs_score"),
            "audience_reach":   bvs.get("audience_reach_tier"),
            "rights_tier":      bvs.get("rights_tier"),
            "plain_english":    bvs.get("plain_english"),
            "note":             "CQS = commercial magnitude. Not a match outcome signal."
        }
```

**SportMind files:**
- `market/broadcaster-media-intelligence.md` — BVS framework
- `core/contextual-signal-environment.md` — CQS
- `fan-token/brand-score/` — ABS formula
- `fan-token/sponsorship-match/` — AFS for brand matching
- `scripts/sportmind_bc_mcp.py` (port 3004) — bc_broadcast_value, bc_context_quality
- `scripts/sportmind_sc_mcp.py` (port 3006) — sc_cvs_brief, sc_valuation

**Autonomy level:** 1–2. Brief generation is autonomous; commercial decisions are human.

---

<a name="type-11"></a>
### Type 11 — World Cup Multi-Entity Tracker

**What it is:** Manages parallel signal chains for 8+ tokens simultaneously
across a 39-day window — the World Cup 2026 (June 11 – July 19). This is the
most complex agent type in SportMind: it handles NCSI amplification per round
(×3.5 group → ×4.0 final), CALENDAR_COLLAPSE events on elimination, PATH_2
supply verification for $AFC and any other confirmed tokens, and post-tournament
signal reset.

**Why it's a distinct type:** No single-match or single-token agent handles
this. The multi-entity tournament tracker must maintain state across dozens
of matches, update NCSI amplifiers per round, cascade elimination signals
across both national and club tokens, and know when to apply the post-tournament
narrative decay model. It is the closest SportMind comes to a fully autonomous
long-horizon agent.

**How SportMind implements it:**

```python
# World Cup multi-entity tracker
# Manages 8+ tokens simultaneously across 39 days
# The most complex SportMind agent type

import requests, json
from datetime import datetime
from pathlib import Path

SPORTMIND_API = "http://localhost:8080"
SPORTMIND_FT  = "http://localhost:3002"
SPORTMIND_GC  = "http://localhost:3005"

# NCSI amplifiers per round (from WC2026 intelligence file)
NCSI_AMPLIFIERS = {
    "group_stage":     3.5,
    "round_of_32":     3.5,
    "round_of_16":     3.7,
    "quarter_final":   3.85,
    "semi_final":      3.95,
    "final":           4.0,
}

class WorldCupTracker:
    """
    Multi-entity tracker for World Cup 2026.

    Tracks simultaneously:
      - National token signals ($ARG and equivalents)
      - Club token NCSI effects (ATM players at tournament)
      - PATH_2 burn events for confirmed tokens ($AFC)
      - CALENDAR_COLLAPSE events on elimination
      - Post-tournament signal reset

    Scope: only official competitive World Cup matches trigger FTP mechanics.
    """

    def __init__(self, tokens: list[str], path2_tokens: list[str]):
        self.tokens      = tokens       # All tokens to monitor
        self.path2_tokens = path2_tokens # Tokens with PATH_2 active
        self.tournament_state = {
            t: {
                "status":           "ACTIVE",  # ACTIVE / ELIMINATED / CHAMPION
                "current_round":    "group_stage",
                "ncsi_amplifier":   NCSI_AMPLIFIERS["group_stage"],
                "matches_played":   0,
                "signal_history":   [],
            }
            for t in tokens
        }

    def process_match_result(self, nation: str, result: str,
                              round_stage: str):
        """Process a result and cascade effects across all affected tokens."""

        print(f"\n{'='*50}")
        print(f"RESULT: {nation} — {result} ({round_stage})")

        # Update NCSI amplifier for current round
        amplifier = NCSI_AMPLIFIERS.get(round_stage, 3.5)

        if result == "ELIMINATED":
            self._handle_calendar_collapse(nation, round_stage)
            return

        # WIN or advance — update token states
        affected_tokens = self._get_affected_tokens(nation)
        for token in affected_tokens:
            self._update_token_signal(token, nation, result, amplifier)

        # PATH_2 verification if applicable
        if nation in self.path2_tokens:
            self._schedule_supply_verification(nation, result)

    def _handle_calendar_collapse(self, nation: str, stage: str):
        """
        CALENDAR_COLLAPSE: nation eliminated.
        Immediate effects on national and club tokens.
        """
        print(f"CALENDAR_COLLAPSE: {nation} eliminated at {stage}")

        # National token: immediate signal reset
        print(f"  National token: NCSI amplifier removed")
        print(f"  Signal: WAIT for 72h (Speculator exit window)")

        # Club tokens: remove NCSI amplifier
        club_tokens = self._get_club_tokens_for_nation(nation)
        for club_token in club_tokens:
            print(f"  Club token {club_token}: NCSI amplifier removed")
            print(f"  PATH_2 continues on domestic schedule (unchanged)")

        # Log the collapse
        print(f"  CDI window: {self._get_cdi_window(stage)}")
        print(f"  Phase 1 (days 1-7): Do NOT act on residual narrative signal")

    def _update_token_signal(self, token: str, nation: str,
                              result: str, amplifier: float):
        """Update signal for a token after a result."""

        signal = requests.get(f"{SPORTMIND_FT}/token-state", params={
            "token": token
        }).json()

        # Apply NCSI amplifier
        raw_ncsi = signal.get("ncsi_base", 1.0)
        amplified = raw_ncsi * amplifier

        print(f"  {token}: NCSI {raw_ncsi:.2f} × {amplifier} = {amplified:.2f}")

        self.tournament_state[token]["signal_history"].append({
            "nation":    nation,
            "result":    result,
            "amplifier": amplifier,
            "ncsi":      amplified,
            "timestamp": datetime.utcnow().isoformat()
        })

    def _schedule_supply_verification(self, nation: str, result: str):
        """Schedule PATH_2 supply verification after match."""
        print(f"  PATH_2 supply verification scheduled:")
        print(f"    T+30min: initial check (AMM settling)")
        print(f"    T+6h:    definitive verification")
        print(f"    T+24h:   BURN_MISSING flag if not confirmed")
        if result == "WIN":
            print(f"    Expected: BURN_CONFIRMED (~0.24% supply reduction)")
        else:
            print(f"    Expected: SUPPLY_NEUTRAL_CONFIRMED (LOSS = mint back to treasury)")

    def _get_cdi_window(self, stage: str) -> str:
        windows = {
            "group_stage":  "18 days",
            "round_of_32":  "28 days",
            "round_of_16":  "35 days",
            "quarter_final":"40 days",
            "semi_final":   "46 days",
            "runner_up":    "52 days",
            "champion":     "75 days",
        }
        return windows.get(stage, "unknown")

    def _get_affected_tokens(self, nation: str) -> list:
        return [t for t in self.tokens if nation in t or t in self.path2_tokens]

    def _get_club_tokens_for_nation(self, nation: str) -> list:
        # In production: query ATM data for which clubs have players from this nation
        NATION_CLUB_MAP = {
            "Argentina": ["BAR"],  # e.g. players at Barcelona
            "England":   ["AFC", "CITY"],
            "Spain":     ["BAR", "ATM"],
            "France":    ["PSG"],
        }
        return NATION_CLUB_MAP.get(nation, [])

# Run for World Cup 2026
tracker = WorldCupTracker(
    tokens=["AFC", "PSG", "BAR", "CITY", "ATM", "ACM", "INTER", "JUV"],
    path2_tokens=["AFC"]  # Expand as confirmed
)

# Example: process results as they come in
tracker.process_match_result("Argentina", "WIN",       "group_stage")
tracker.process_match_result("England",   "WIN",       "group_stage")
tracker.process_match_result("Argentina", "WIN",       "quarter_final")
tracker.process_match_result("France",    "ELIMINATED","semi_final")
```

**SportMind files:**
- `fan-token/world-cup-2026-intelligence/` — NCSI amplifiers, CALENDAR_COLLAPSE
- `fan-token/gamified-tokenomics-intelligence/` — PATH_2 WC2026 interaction
- `core/core-narrative-momentum.md` — post-tournament decay phases
- `fan-token/tournament-elimination-intelligence.md` — elimination mechanics
- `scripts/sportmind_ft_mcp.py` (port 3002) — ft_token_state, ft_tournament_exit

**Autonomy level:** 3–4. Tracking is fully autonomous. Humans review CALENDAR_COLLAPSE
events and supply anomalies.

---

## Combining agent types

Most production systems combine multiple types. Common combinations:

**Fan token production stack:**
- Type 2 (Model-Based) for pre-match signals
- Type 6 (Supply Surveillance) for PATH_2 monitoring
- Type 8 (Narrative Aggregator) for CDI extension signals
- Type 9 (Governance Participation) for holder engagement

**World Cup 2026 stack:**
- Type 11 (Multi-Entity Tracker) as the orchestrator
- Type 6 (Supply Surveillance) for $AFC PATH_2 during tournament
- Type 7 (Regulatory Watchdog) for US market signals during tournament

**Commercial intelligence stack:**
- Type 4 (Utility-Based) for scouting and ranking
- Type 10 (Commercial Brief) for deliverable generation
- Type 8 (Narrative Aggregator) for timing commercial windows

---

---

## The most important thing this document doesn't say

The eleven types above are **patterns, not constraints**.

SportMind is structured markdown and a set of optional MCP tools. There is
no required framework, no opinionated runtime, no SDK you have to use. The
library doesn't know what kind of agent you're building — it just provides
intelligence when you ask for it.

You can ignore all eleven types and build something entirely your own.

---

## Building a custom agent

**What SportMind provides:**

```
Skill files     Structured markdown you load into any context
MCP tools       Optional — 8 servers, 45 tools, all accessible over HTTP
Skills API      Optional — REST endpoints if you prefer direct calls
Output schema   A suggestion, not a requirement
Agent prompts   24 production-ready system prompts to copy and adapt
```

**What SportMind does not constrain:**

```
Agent framework     Use Claude, GPT-4o, Gemini, LangChain, CrewAI, or none
Trigger mechanism   Schedule, webhook, event, manual, continuous — your call
State management    Memory MCP, your own database, stateless — any approach
Output format       ENTER/WAIT/ABSTAIN is one option; use whatever your system needs
Deployment          Local, cloud, serverless, container — SportMind doesn't care
```

**The only non-negotiable:**

```
AGENT BOUNDARY — non-negotiable regardless of architecture:

SportMind agents produce intelligence.
They do not execute trades, submit governance votes, or negotiate contracts.

This is architectural — not a limitation of what you can build, but a
separation of concerns between intelligence and execution. Your application
layer decides what to do with the intelligence. SportMind reasons.
```

**How to build a custom agent from scratch:**

```python
# Custom agent — minimum viable SportMind integration
# No framework required. No SDK. Just the skill files and your LLM.

import requests

SPORTMIND_API = "http://localhost:8080"  # Skills API

def build_custom_agent(your_question: str, relevant_skills: list[str]) -> str:
    """
    The simplest possible SportMind agent.
    Load the skills you need. Ask your question. Done.
    """

    # Step 1: Load whichever skill files are relevant to your use case
    context_parts = []
    for skill in relevant_skills:
        skill_content = requests.get(f"{SPORTMIND_API}/skill/{skill}").json()
        context_parts.append(skill_content["content"])

    # Step 2: Combine into a single context string
    system_context = "

---

".join(context_parts)

    # Step 3: Call your LLM of choice with the context + your question
    # This works with any LLM — Claude, GPT-4o, Gemini, open-source models
    response = call_your_llm(
        system_prompt=system_context,
        user_message=your_question
    )

    return response

# Example: load exactly the skills you need for your use case
result = build_custom_agent(
    your_question="What are the key signals for an Arsenal match tonight?",
    relevant_skills=[
        "macro/macro-overview",
        "sports/football/sport-domain-football",
        "athlete/football/athlete-intel-football",
        "fan-token/football-token-intelligence/football-token-intelligence",
    ]
)
```

**Combining SportMind with other data sources:**

SportMind is an intelligence layer, not a data layer. It is designed to
be combined with whatever data your use case needs:

```
SportMind intelligence    +    Your data source    =    Your agent

Pre-match signal          +    Live odds feed       =    Odds divergence detector
Fan token intelligence    +    Chiliz API           =    Portfolio manager
Athlete brief             +    Contract database    =    Negotiation assistant
Broadcast value           +    Rights calendar      =    Scheduling tool
Narrative signal          +    Social API           =    Trend monitor
```

The library already has connector templates for the most common data
sources in `platform/api-connector-examples.md` and five working Python
connectors in `platform/api-providers.md`.

**Adapting the eleven types:**

You don't have to choose one type and stick to it. Every production agent
in practice is a hybrid. The types in this document are entry points and
vocabulary — not boxes to build inside.

A pre-match signal agent that *also* monitors KOL signals and *also*
detects narrative momentum is a Type 2 + Type 8 hybrid. A World Cup
tracker that *also* runs governance notifications is a Type 11 + Type 9
hybrid. The types are additive, not exclusive.

---

## Summary — what you're free to do

```
✅ Build any agent architecture you want
✅ Use any LLM — Claude, GPT-4o, Gemini, open-source models
✅ Use any framework — LangChain, CrewAI, AutoGen, none at all
✅ Load any skill files in any order you choose
✅ Use the MCP tools, the REST API, or direct file loading
✅ Define your own output format
✅ Ignore all eleven types and build something completely new
✅ Combine multiple types in one agent
✅ Use SportMind as one layer alongside your own data and logic

❌ Execute trades, votes, or contracts from the agent layer
   (that's your application — SportMind reasons, you act)
```

The eleven types exist to give you a starting point and a vocabulary.
The library exists to give you the intelligence.
What you build with it is entirely up to you.

## Where to go next

| Next step | Resource |
|---|---|
| Run a simple signal in 5 minutes | `examples/starter-pack/README.md` |
| Full workflow pattern implementations | `examples/agentic-workflows/README.md` |
| Production application blueprints | `examples/applications/README.md` |
| System prompt for your agent | `agent-prompts/agent-prompts.md` |
| MCP server configuration | `platform/sportmind-mcp-suite.md` |
| Cognitive architecture deep-dive | `core/agent-cognitive-architecture.md` |

---

*SportMind v3.76.0 · MIT License · sportmind.dev*
*See also: core/agent-cognitive-architecture.md · core/agent-goal-framework.md*
*core/autonomous-agent-framework.md · examples/starter-pack/README.md*
