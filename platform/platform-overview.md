# SportMind Platform — Overview

**SportMind's sole purpose, unchanged:** Open sports intelligence for AI agents
and developers. The platform layer makes that intelligence reliable, composable,
and buildable-upon — it does not change what SportMind is or restrict who can use it.

---

## What the platform layer adds

```
SPORTMIND WITHOUT PLATFORM LAYER:
  Pull system — developer loads skill files manually into agent context
  Static — intelligence reflects the version of the file at load time
  Informal — integrations are bespoke; no standard interface
  Developer-assembled — developer decides which files to load and when

SPORTMIND WITH PLATFORM LAYER:
  Push/pull hybrid — agents can query intelligence when they need it
  Dynamic — intelligence can reflect current state (injury, macro event)
  Formal — standard skill contracts; composable across any agent framework
  Agent-driven — agents query what they need; platform serves the right context

WHAT DOESN'T CHANGE:
  The intelligence itself — same five layers, same skills, same open access
  The MIT license — everything remains free and open
  The purpose — serving AI agents and developers building sports intelligence
  The community model — contributions, skill templates, validator script
```

---

## The platform structure

```
platform/
├── api-contracts.md          Formal skill call specifications
│                             Input → guaranteed output for every skill type
│
└── integration-partners.md   How external systems connect to SportMind
                              FanTokenIntel, Chiliz, Azuro, data providers, LLMs
```

These two files sit alongside the intelligence library — they don't replace it.
The skill files in `sports/`, `athlete/`, `fan-token/`, `core/`, `market/`, and
`macro/` remain the source of truth. The platform layer is how that truth is served.

---

## The division of responsibility

SportMind never competes with data providers. The division is explicit:

```
DATA PROVIDERS provide:          SPORTMIND provides:
────────────────────────         ───────────────────────────────
Raw signal scores                How to interpret those scores by sport
On-chain token data              What that data means for agent decisions
Player statistics                How player status changes signal weight
Market prices                    How macro conditions affect all signals
Pool TVL and LP activity         How liquidity constrains execution
Prediction market odds           How sport context validates those odds

The base_score is always external. The reasoning is always SportMind.
```

---

## Three ways to use SportMind (unchanged + new)

### Option 1 — Library mode (unchanged, always available)

Load skill files directly into your agent's system prompt.
No API, no dependencies, works with any LLM.

```
# Still works exactly as before:
Load sports/football/sport-domain-football.md
Load athlete/football/athlete-intel-football.md
Load core/confidence-output-schema.md
Agent reasons with this context
```

### Option 2 — Contract mode (new)

Call SportMind skills via the contract interface.
Standardised inputs and outputs; composable with any data platform.

```python
response = sportmind.call({
    "skill": "signal.full",
    "sport": "football",
    "inputs": {"base_score": 72}
})
adjusted_score = response["signal"]["adjusted_score"]
```

### Option 3 — Integrated mode (new — with partner data)

Combine a data partner's signals with SportMind's intelligence layer.

```python
base = fti.signals_active(token="BAR").score    # FanTokenIntel provides base
sm   = sportmind.call({                          # SportMind interprets it
    "skill": "signal.full",
    "sport": "football",
    "inputs": {"base_score": base}
})
decision = sm["sizing"]["recommended_action"]    # Agent acts on result
```

---

## What this means for agents

An agent built on SportMind's platform layer gets three things it didn't have before:

**Reliability:** The confidence output schema guarantees specific fields.
An agent built against `signal.full` knows it will always receive `adjusted_score`,
`confidence_tier`, `flags`, and `sizing`. No matter which sport, which event,
or which data platform supplied the base signal.

**Currency:** The platform can serve current intelligence — today's injury status,
this morning's going report, the macro condition as of right now. The library
serves intelligence; the platform serves intelligence at the moment it's needed.

**Composability:** Any agent that consumes the SportMind confidence output schema
can be extended, replaced, or connected to other SportMind-compatible systems
without changing the integration. The contract is stable.

---

## What this means for developers

Developers building on SportMind gain a defined, versioned API surface.

```
BEFORE PLATFORM LAYER:
  "Load these files into your agent" — developer figures out the integration

AFTER PLATFORM LAYER:
  "Call this contract with these inputs; receive this guaranteed output"
  — developer has a stable interface to build against

The developer can now:
  → Build a product that depends on SportMind without tracking individual skill files
  → Connect any data provider to SportMind using the integration-partners patterns
  → Know exactly what schema version their agent is consuming
  → Upgrade to new SportMind versions with a defined migration path
  → Build multi-sport products using the same contract interface for all sports
```

---

## The open intelligence guarantee

The platform layer does not create a paid tier, a restricted API, or a closed
suite. Everything documented in `platform/` is MIT licensed, open, and free.

```
WHAT REMAINS FULLY OPEN:
  All skill files (sports/, athlete/, fan-token/, core/, market/, macro/)
  All platform documentation (platform/api-contracts.md, platform/integration-partners.md)
  All agent prompts, worked examples, and testing scenarios
  The confidence output schema and all contracts
  The skill validator script
  All templates and contribution guides

WHAT THE PLATFORM LAYER ENABLES (without restricting):
  Third-party developers building products on SportMind
  Data platforms integrating SportMind as their intelligence layer
  Agent frameworks that treat SportMind contracts as a stable dependency
  Community contributors who know what interface their skills must satisfy
```

---

## Reading order for platform developers

```
1. README.md                        What SportMind is (5 minutes)
2. sportmind-overview.md            Full library context
3. platform/api-contracts.md        The formal skill interfaces
4. platform/integration-partners.md How existing systems connect
5. core/confidence-output-schema.md The output format every contract returns
6. agent-prompts/agent-prompts.md   Ready-to-deploy prompts using the contracts
7. examples/testing/testing-scenarios.md  Verify your integration is correct
```

---

*SportMind is an independent open-source project. The platform layer is community
infrastructure, not a commercial product. It serves the same developers and agents
that the library has always served — with better tools to build on it reliably.*

*MIT License · SportMind · sportmind.dev*
