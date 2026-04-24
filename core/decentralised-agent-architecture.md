# Decentralised Agent Architecture — SportMind

**Patterns for multi-agent SportMind deployments, distributed intelligence loading,
autonomous skill execution, and agent-to-agent coordination.**

This document extends `core/autonomous-agent-framework.md` (single-agent model)
into distributed environments where multiple specialised agents collaborate.
It also defines the concept of **autonomous skills** — skills that carry their
own trigger conditions and execution logic.

---

## Overview

A single SportMind agent loading the full five-layer stack is powerful.
A network of specialised agents — each owning one layer, one sport, or one
function — is more resilient, more scalable, and more maintainable.

SportMind's layered architecture (macro → market → domain → athlete → fan token)
maps naturally to a distributed agent network. Each layer can be owned by a
separate agent. Signals flow between agents as structured handoffs. The network
produces the same output as a single agent, but each component is independently
testable, updateable, and replaceable.

This is not a requirement. Single-agent deployment remains fully supported.
This document is for teams building production systems that need to scale.

---

## Domain Model

### The distributed SportMind stack

```
LAYER AGENT MAPPING:

  ┌─────────────────────────────────────────────────────────┐
  │  ORCHESTRATOR AGENT                                     │
  │  Receives user query. Routes to layer agents.           │
  │  Assembles signal from layer outputs.                   │
  │  Applies conflict resolution. Dispatches final output.  │
  └────────────────────┬────────────────────────────────────┘
                       │ coordinates
    ┌──────────────────┼──────────────────────┐
    │                  │                      │
    ▼                  ▼                      ▼
  MACRO AGENT      MARKET AGENT          SPORT DOMAIN AGENT
  Owns Layer 5     Owns Layer 4          Owns Layer 1
  macro/           market/               sports/{sport}/
  Runs first       Runs second           Runs third
    │                  │                      │
    └──────────────────┼──────────────────────┘
                       │ feeds into
         ┌─────────────┼─────────────┐
         │                           │
         ▼                           ▼
  ATHLETE AGENT                FAN TOKEN AGENT
  Owns Layer 2                 Owns Layer 3
  athlete/                     fan-token/
  Runs fourth                  Runs fifth (final)

SIGNAL FLOW:
  macro_output → market_agent → market_output →
  domain_agent → domain_output → athlete_agent →
  athlete_output → fan_token_agent → FINAL SIGNAL OUTPUT
```

### Agent specialisation patterns

```
PATTERN 1 — LAYER SPECIALISATION (recommended for large deployments):
  One agent per layer. Each agent owns its layer's skills completely.
  Handoff: structured JSON between layers (see Signal Handoff Protocol).
  Best for: production systems with 10+ monitored tokens across multiple sports.

PATTERN 2 — SPORT SPECIALISATION (recommended for focused deployments):
  One agent per sport (or per sport cluster). Each agent owns all layers
  for their sport(s).
  Handoff: only needed when signals cross sport boundaries (e.g., athlete
  playing in two token ecosystems simultaneously).
  Best for: single-sport or dual-sport monitoring at depth.

PATTERN 3 — FUNCTION SPECIALISATION (recommended for complex use cases):
  One agent per function: signal generation, governance monitoring, CDI
  tracking, commercial briefing.
  All agents share a common intelligence layer (the SportMind library).
  Handoff: agents subscribe to each other's outputs.
  Best for: fan token platforms needing multiple concurrent outputs.

PATTERN 4 — HYBRID (most common in production):
  Macro + market as shared global agents (run once, broadcast to all).
  Sport-specific agents for domain + athlete.
  Function-specific agents for fan token (position, governance, commercial).
  Best for: teams that start with Pattern 2 and scale toward Pattern 1.
```

### Signal handoff protocol

```
STANDARDISED HANDOFF SCHEMA:
  Every agent passes a structured handoff to the next agent in the chain.
  This ensures the receiving agent has exactly what it needs and nothing extra.

{
  "handoff_from":         "macro_agent",
  "handoff_to":           "market_agent",
  "sportmind_version":    "3.87.0",
  "timestamp":            "ISO-8601",
  "token":                "$AFC",
  "sport":                "football",

  "layer_output": {
    "layer":              5,
    "modifier":           0.92,
    "confidence":         "HIGH",
    "override_active":    false,
    "active_events":      ["CHZ bear phase — Q2 2026"],
    "pass_to_next":       true
  },

  "cumulative_signal": {
    "direction":          "HOME",
    "adjusted_score":     null,
    "modifiers_applied":  [{"source": "macro", "value": 0.92}],
    "blocking_flags":     [],
    "notes":              []
  }
}

HANDOFF RULES:
  If any agent sets override_active: true → all subsequent agents HALT.
  If any agent sets pass_to_next: false → orchestrator receives partial signal
    and must decide whether to proceed or escalate.
  blocking_flags accumulate across all layers — later agents never clear flags
    set by earlier agents.
  All agents must log their handoff output for auditing.
```

---

## Autonomous Skills

An autonomous skill is a skill file that carries its own execution logic —
it knows when to invoke itself, what to do when triggered, and what it must
never do without human confirmation.

### What makes a skill autonomous

```
CONVENTIONAL SKILL:
  - Passive: loaded on request, applied to a query
  - Stateless: no memory of previous invocations
  - Query-driven: only runs when an agent asks it to

AUTONOMOUS SKILL:
  - Active: monitors for trigger conditions
  - Maintains state between invocations (via agent memory)
  - Event-driven: runs when conditions are met, not when asked
  - Carries its own safety rails alongside its execution logic

The distinction matters for deployment:
  Conventional skills are tools.
  Autonomous skills are behaviours.
```

### Autonomous skill anatomy

Every autonomous skill contains an `## Autonomous Execution` section with
four mandatory components:

```
1. TRIGGER CONDITIONS
   When does this skill invoke itself?
   Triggers should be specific, measurable, and based on SportMind signal outputs.
   Examples:
     - SMS crosses 75 threshold on recalculation
     - CDI drops > 20 points in 24h
     - Set piece specialist confirmed absent (squad news Category 2)
     - Governance proposal detected for monitored token
     - macro_override_active state changes

2. EXECUTION BY AUTONOMY LEVEL
   What does the skill do at Level 2 vs Level 3 vs Level 4?
   Each level has a specific, bounded set of permitted actions.
   Level 2: notify and log — never act on positions
   Level 3: dispatch briefings automatically — still no financial execution
   Level 4: continuous background monitoring — hardest boundaries apply

3. HARD BOUNDARIES
   What does this skill NEVER do, regardless of autonomy level or signal quality?
   Hard boundaries are listed explicitly and are not configurable by the operator.
   Examples:
     - Never execute financial positions autonomously
     - Never vote on Tier C governance proposals
     - Never act when macro_override_active = true
     - Never use statistics from < minimum sample size

4. ESCALATION CONDITION
   When does the autonomous skill stop acting and hand control to a human?
   Escalation conditions are specific and non-negotiable.
```

### Skills with autonomous execution sections (current library)

```
SKILL FILE                                          | TRIGGER CLASS
----------------------------------------------------|------------------
sports/football/sport-statistics-football.md        | Squad news, live xG
fan-token/agentic-wallet-intelligence/              | Signal threshold, CDI
fan-token/fan-token-lifecycle.md                    | Phase transition
fan-token/gamified-tokenomics-intelligence/         | Goal scored (PATH_2)
fan-token/fan-token-governance-intelligence.md      | Proposal detection
core/breaking-news-intelligence.md                  | News Category 1/2
macro/macro-crypto-market-cycles.md                 | Regime change

TO ADD autonomous execution sections (future):
  fan-token/fan-sentiment-intelligence.md           | Sentiment threshold
  fan-token/league-football-token-intelligence.md   | League-specific triggers
  athlete/athlete-modifier-system.md                | Injury confirmation
  sports/football/sport-domain-football.md          | Match result
```

### Building an autonomous skill section

```markdown
## Autonomous Execution

**Trigger conditions — when this skill should self-invoke:**
- [Specific, measurable condition based on SportMind signal output]
- [Second trigger — keep to 2–4 maximum]

**Execution at autonomy Level 2:**
- [Specific permitted actions — notify, log, flag]
- [What the agent may do without human confirmation]

**Execution at autonomy Level 3–4:**
- [Additional permitted actions at higher autonomy]
- [What the agent does automatically]

**Hard boundaries — never autonomous at any level:**
- [What this skill never does regardless of signal quality]
- [What requires human confirmation]
```

---

## Distributed Load Patterns

### Cold start (no state)

```
COLD START SEQUENCE FOR DISTRIBUTED NETWORK:

  T=0:  Orchestrator receives query or scheduled trigger fires
  T+1:  Macro agent loads macro/macro-crypto-market-cycles.md
        Macro agent generates handoff → broadcasts to all layer agents
  T+2:  Market agent loads market/{sport} files
        Market agent generates handoff → passes to domain agent
  T+3:  Domain agent loads sports/{sport}/sport-domain-{sport}.md
        Domain agent generates handoff → passes to athlete agent
  T+4:  Athlete agent loads athlete/athlete-modifier-{sport}.md
        Athlete agent generates handoff → passes to fan token agent
  T+5:  Fan token agent loads relevant fan-token/ files
        Fan token agent produces FINAL SIGNAL OUTPUT
  T+6:  Orchestrator assembles, applies conflict resolution, dispatches

TOTAL: 5–8 minutes for full cold start (including LLM processing time)
WARM START (cached macro/market state): 2–3 minutes
```

### Continuous monitoring (warm state)

```
CONTINUOUS MONITORING CYCLE (recommended for production):

  Macro agent: runs every 4h — updates macro state, broadcasts changes
  Market agent: runs every 24h — updates commercial tier, CDI baselines
  Domain agent: runs on match schedule — active T-6h to T+48h
  Athlete agent: runs on squad news events — triggered by breaking news
  Fan token agent: runs every 30 min during active windows (match day)
                   runs every 4h during quiet periods

  SHARED STATE:
    All agents write to a shared signal state object.
    Each agent reads the current state before processing.
    The signal state is the single source of truth for the network.

  CONFLICT RESOLUTION:
    If two agents produce conflicting signals (macro says BEAR,
    domain says strong HOME signal):
    → Macro modifier takes precedence (applies as multiplier to domain signal)
    → Domain signal is not discarded — it is modulated
    → blocking_flags from either agent propagate to final output
    This is not a conflict — it is how the modifier system is designed to work.
    A conflict requiring escalation is: two domain agents producing opposite
    directions for the same event. This should never occur; if it does,
    escalate to human review.
```

### Agent registration and capability declaration

```json
{
  "agent_id":              "football-domain-agent-001",
  "agent_type":            "domain_specialist",
  "layer":                 1,
  "sport":                 "football",
  "autonomy_level":        2,
  "skills_loaded": [
    "sports/football/sport-domain-football.md",
    "sports/football/sport-statistics-football.md"
  ],
  "tokens_monitored":      ["AFC", "CITY", "SPURS", "AVL", "EFC", "CPFC", "LUFC"],
  "trigger_classes": [
    "squad_news",
    "match_schedule",
    "live_xg_divergence"
  ],
  "autonomous_skills":     ["sport-statistics-football"],
  "escalation_channel":    "slack://sportmind-alerts",
  "handoff_destination":   "athlete-agent-001",
  "cycle_frequency":       "match-driven",
  "sportmind_version":     "3.87.0",
  "registered_at":         "ISO-8601"
}
```

---

## Conflict Resolution Framework

```
TYPE 1 — MODIFIER CONFLICT (normal, not a real conflict):
  Macro modifier 0.88 (bear phase) × Domain signal 82 SMS.
  Result: 82 × 0.88 = 72.2 adjusted score.
  This is expected behaviour. Apply and proceed.

TYPE 2 — FLAG CONFLICT (one agent blocks, another proceeds):
  Athlete agent sets macro_override_active: false.
  Macro agent sets macro_override_active: true.
  RULE: macro_override_active = true ALWAYS wins. No negotiation.
  Blocking flags are never overridden by a downstream layer.

TYPE 3 — DIRECTION CONFLICT (genuine conflict, requires human):
  Domain agent: direction = HOME.
  Fan token agent: direction = AWAY (based on CDI and holder behaviour).
  RULE: Escalate to human. Do not produce a signal under direction conflict.
  Log both outputs. Flag for manual review.
  This is rare — usually means a live event (e.g., injury in warm-up)
  has not propagated through all agents simultaneously.

TYPE 4 — STALE STATE CONFLICT (one agent has old data):
  If any agent's last_calculation is > 4h old on a match day:
  Force recalculation before assembling final signal.
  Stale signals are not combined with fresh signals.
```

---

## Compatible Frameworks

```
MULTI-AGENT ORCHESTRATION:
  CrewAI:     Layer agents → Crew roles. Orchestrator → Crew manager.
  AutoGen:    Layer agents → Assistants. Orchestrator → GroupChat manager.
  LangChain:  Layer agents → Chain steps. Handoffs → LCEL chain composition.
  Custom:     Any architecture that respects the signal handoff schema.

MCP INTEGRATION:
  Each layer agent can expose its output as an MCP tool.
  Orchestrator calls layer MCP tools in sequence.
  Full MCP server implementation: scripts/sportmind_mcp.py
  See: MCP-SERVER.md for tool schemas.

DEPLOYMENT ENVIRONMENTS:
  Local: all agents on one machine, shared filesystem for state
  Cloud: agents as serverless functions, shared state via object storage
  Hybrid: macro/market agents central, sport agents edge-deployed
```

---

## Event Playbooks

### Playbook 1: Distributed cold start for new token
```
trigger:  New fan token added to monitoring scope
timing:   Immediate — run full cold start sequence
protocol:
  1. Macro agent: check current macro state
  2. Market agent: load market intelligence for token's sport
  3. Domain agent: load sport domain skill
  4. Athlete agent: identify Tier 1 ATM players, load modifiers
  5. Fan token agent: load lifecycle phase, CDI baseline, holder profile
  6. Register token in all agent monitoring scopes
  7. Generate initial signal as baseline reference
output:   Initial signal state with "first_run": true flag
```

### Playbook 2: Propagating a Category 1 breaking news event
```
trigger:  Category 1 news (Tier 1 source — official club/federation)
timing:   Immediate
protocol:
  1. Breaking news agent (or domain agent with news monitoring) fires
  2. Athlete agent recalculates ATM modifier with new availability status
  3. Domain agent recalculates match signal with updated lineup
  4. Fan token agent recalculates CDI with updated signal
  5. Orchestrator assembles updated signal and dispatches
  6. All agents log the event with source tier and timestamp
timing target: full recalculation within 8 minutes of confirmed news
```

### Playbook 3: Macro regime change propagation
```
trigger:  Macro agent detects regime change (bull → bear or bear → bull)
timing:   Immediate broadcast
protocol:
  1. Macro agent generates new handoff with updated modifier
  2. Broadcasts to ALL layer agents simultaneously (not sequential)
  3. Each agent applies new macro modifier to its current signal state
  4. Fan token agent recalculates all active signals
  5. Orchestrator dispatches updated signals for all affected tokens
  6. If macro_override_active changes to true: all active signals HALT
note:     Macro regime change is the highest-priority event in the network.
          It propagates immediately and asynchronously — do not queue it.
```

### Playbook 4: Agent failure recovery
```
trigger:  One layer agent becomes unavailable or returns error
timing:   Immediate
protocol:
  1. Orchestrator detects failed handoff (timeout or error)
  2. Mark affected layer as DEGRADED in signal state
  3. Proceed with partial signal (remaining layers only)
  4. Flag output: "signal_degraded": true, "missing_layer": [layer_number]
  5. Alert operator: partial signal in production
  6. Do not discard signal — a partial signal is better than no signal
  7. Attempt agent restart; if successful, recalculate with full stack
note:     A signal missing one layer is still actionable if the missing
          layer is not the fan token layer. Missing fan token layer:
          produce no signal — that layer is the output layer.
```

---

## Signal Weight Adjustments

In distributed deployments, signal weights remain identical to single-agent
deployments. The architecture does not change the weights — it distributes
the calculation.

One exception: **latency-induced stale signals**.

```
STALENESS DISCOUNT:
  If a layer agent's last_calculation is:
    < 1h old:  full weight (1.00×)
    1–4h old:  slight discount (0.95×) on that layer's modifier
    4–8h old:  moderate discount (0.85×) — flag for recalculation
    > 8h old:  heavy discount (0.70×) — urgent recalculation required

This prevents a network from acting on a match-day signal calculated
8 hours ago by an athlete agent that hasn't been updated since.
```

---

## Agent Reasoning Prompts

- "Layer agent handoff received: check override_active and blocking_flags before proceeding."
- "Macro regime change detected: broadcast immediately to all layer agents — do not queue."
- "Direction conflict between domain and fan token agent: halt, escalate, do not produce signal."
- "Agent layer marked DEGRADED: proceed with partial signal, flag output, alert operator."
- "Autonomous skill trigger fired: check autonomy level, apply hard boundaries, log reasoning."
- "New token added to scope: run cold start sequence before monitoring begins."

---

## Key Commands

| Action | Load | Notes |
|---|---|---|
| Single agent (standard) | `core/autonomous-agent-framework.md` | Full single-agent framework |
| Distributed deployment | This file + `core/autonomous-agent-framework.md` | Complete architecture |
| Autonomous skills only | `## Autonomous Skills` section | Standalone reference |
| Signal handoff | `## Signal handoff protocol` section | Schema reference |
| MCP integration | `MCP-SERVER.md` | Tool exposure for layer agents |

---

## Data Sources

Architecture and multi-agent orchestration references:
- CrewAI documentation: docs.crewai.com
- AutoGen documentation: microsoft.github.io/autogen
- LangChain documentation: python.langchain.com
- MCP specification: modelcontextprotocol.io

---

## Compatibility

**Extends:** `core/autonomous-agent-framework.md`
**MCP layer:** `MCP-SERVER.md` (tool schemas for distributed agents)
**Agentic wallet:** `fan-token/agentic-wallet-intelligence/agentic-wallet-intelligence.md`
**Breaking news:** `core/breaking-news-intelligence.md` (Category 1/2 propagation)
**Examples:** `examples/agentic-workflows/multi-agent-coordination.md`

---

*SportMind v3.87.0 · MIT License · sportmind.dev*
