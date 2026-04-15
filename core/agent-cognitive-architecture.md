---
name: agent-cognitive-architecture
description: >
  Maps SportMind's components to the standard cognitive architecture
  taxonomy used in AI research and enterprise AI evaluation: reactive
  agents, model-based reflex agents, goal-based agents, utility-based
  agents, and learning agents (Russell & Norvig). Also covers Multi-Agent
  Systems (MAS) and Belief-Desire-Intention (BDI) frameworks. For each
  architecture class: what it is, how SportMind implements it, which
  specific files provide that capability, and what it can and cannot do.
  This document is for enterprise evaluators, researchers, and developers
  who need to understand SportMind's cognitive architecture in standard
  AI terminology. It does not add new capability — it makes existing
  capability legible to an audience that thinks in these terms. Explicit
  about limitations: SportMind agents are not AGI, cannot learn without
  human-mediated calibration, and operate within a tightly scoped domain.
---

# Agent Cognitive Architecture — SportMind

**SportMind agents are not one architecture. They implement multiple
cognitive patterns simultaneously, at different levels of the signal chain.**

The standard taxonomy from Russell and Norvig's *Artificial Intelligence:
A Modern Approach* provides a useful vocabulary for describing how SportMind
agents reason. This document maps that vocabulary to SportMind's actual
components — not to make grand claims, but to make the library legible to
researchers and enterprise evaluators who need to classify what they are
deploying.

**The honest framing first:** SportMind agents are domain-specific AI
systems operating within a carefully scoped intelligence domain (sports
analysis, fan token commercial intelligence). They are not general-purpose
reasoners. The cognitive architecture patterns below are *implemented within
that scope*, not across arbitrary domains.

---

## Architecture 1 — Reactive (Simple Reflex) Agent

```
WHAT IT IS:
  Acts based on current percept alone. No memory. No model of the world.
  IF [condition] THEN [action]. Fast, reliable, brittle.

HOW SPORTMIND IMPLEMENTS IT:
  The breaking-news agent pattern (core/breaking-news-intelligence.md) is
  the clearest reactive implementation. When a trigger fires (lineup change,
  injury news, macro override), the agent reacts with a pre-defined response
  rule regardless of prior context.

  Example reactive rules in SportMind:
    IF macro_override_active THEN suspend all pre-match signals
    IF lineup_unconfirmed at T-2h THEN add UNCERTAINTY flag
    IF weight_miss detected THEN load MMA weight-cut modifier immediately
    IF behind_closed_doors confirmed THEN cancel home_advantage modifier

SPORTMIND FILES IMPLEMENTING THIS:
  core/breaking-news-intelligence.md — event triggers and reaction rules
  core/temporal-awareness.md — freshness flags as reactive conditions
  core/contextual-signal-environment.md — behind-closed-doors override

LIMITATIONS IN SPORTMIND:
  Reactive rules are too simple for the majority of sports intelligence.
  A team trailing 2-0 in the 80th minute requires more than a trigger —
  it requires contextual reasoning about what the trailing team will do
  next. Reactive architecture handles the trigger; goal-based architecture
  handles the interpretation.

HONEST CAPABILITY RATING: Present and functional for event-driven triggers.
Not the primary architecture. Reactive components enable reliability
(consistent response to known events) not intelligence.
```

---

## Architecture 2 — Model-Based Reflex Agent

```
WHAT IT IS:
  Maintains an internal model of the world. Uses that model to reason
  about states not directly observable. Still rule-based but can handle
  partial observability.

HOW SPORTMIND IMPLEMENTS IT:
  The six-step reasoning chain (core/reasoning-patterns.md) maintains a
  "game state model" — a structured representation of the current match
  context that includes hidden variables (likely lineup before announcement,
  probable opponent formation, momentum state).

  The opponent tendency intelligence (core/opponent-tendency-intelligence.md)
  is specifically a model-based architecture component — it builds and applies
  an internal model of an opponent's hidden intentions based on historical
  observable behaviour.

  The fan token lifecycle model (fan-token/fan-token-lifecycle/) maintains an
  internal model of where a token is in its commercial arc — not directly
  observable from price alone.

SPORTMIND FILES IMPLEMENTING THIS:
  core/reasoning-patterns.md — six-step chain as world model
  core/opponent-tendency-intelligence.md — hidden opponent state modelling
  core/match-condition-snapshot.md — CSS as compressed world state
  fan-token/fan-token-lifecycle/ — token lifecycle state model
  core/historical-intelligence-framework.md — H2H history as world model
  core/temporal-awareness.md — freshness model of information reliability

WHAT "HIDDEN STATES" SPORTMIND REASONS ABOUT:
  Lineup before official announcement (pre-match-squad-intelligence.md)
  Opponent's likely formation (opponent-tendency-intelligence.md)
  Macro phase not yet confirmed by sources (macro regulatory files)
  Player motivation state not publicly disclosed (athlete-motivation-intelligence.md)
  Fan token holder composition not directly visible on-chain
    (fan-holder-profile-intelligence.md — inferred from on-chain behaviour)

HONEST CAPABILITY RATING: Strong. This is SportMind's primary cognitive mode.
The library's most commercially valuable content (tendency profiles, lifecycle
models, squad assembly) is model-based reasoning. The "model" is the structured
intelligence library itself.
```

---

## Architecture 3 — Goal-Based Agent

```
WHAT IT IS:
  Has explicit goals. Evaluates actions based on whether they move toward
  the goal state. Plans sequences of actions to reach objectives.
  More flexible than reflex agents; can handle novel situations.

HOW SPORTMIND IMPLEMENTS IT:
  core/agent-goal-framework.md is a direct implementation of goal-based
  architecture — three-level goal hierarchy (terminal, instrumental,
  immediate), goal state machine, planning cycle.

  Goal examples in SportMind agents:
    Terminal: "Maximise the commercial value of $AFC fan token"
    Instrumental: "Enter positions before WIN burn events"
    Immediate: "Confirm lineup at T-2h before computing ENTER signal"

  The autonomy spectrum (core/autonomous-agent-framework.md) defines
  how much goal-directed autonomy the agent exercises at each level:
    Level 0 (supervised): human sets all goals; agent executes only
    Level 1 (advisory): agent sets immediate goals; human approves
    Level 2 (semi-auto): agent sets instrumental goals autonomously
    Level 3+ (experimental): full goal-directed autonomy with oversight

SPORTMIND FILES IMPLEMENTING THIS:
  core/agent-goal-framework.md — goal hierarchy and planning cycle
  core/autonomous-agent-framework.md — autonomy levels and lifecycle
  core/agent-goal-framework.md — the planning cycle and goal state machine
  examples/agentic-workflows/ — 12 workflow patterns as goal implementations

LIMITATIONS:
  SportMind goal-based agents pursue goals within a constrained action space.
  The AGENT BOUNDARY is architectural: agents set intelligence goals;
  execution (trading, governance voting, contract negotiation) is always
  at the human layer. A goal like "maximise token value" cannot be pursued
  by directly executing trades — only by producing intelligence that informs
  human trading decisions.

HONEST CAPABILITY RATING: Good for intelligence objectives. Not applicable
to execution objectives. The boundary is intentional and non-negotiable.
```

---

## Architecture 4 — Utility-Based Agent

```
WHAT IT IS:
  Has a utility function — evaluates the desirability of states, not just
  whether they achieve a goal. Handles trade-offs and uncertainty.
  Optimal when multiple conflicting objectives must be balanced.

HOW SPORTMIND IMPLEMENTS IT:
  The confidence output schema (core/confidence-output-schema.md) is a
  utility-based output — ENTER/WAIT/ABSTAIN is a utility function applied
  to the combined signal stack, not a simple rule.

  Specific utility trade-offs SportMind agents evaluate:
    Signal strength vs macro risk:
      High SMS (strong match signal) but MACRO_OVERRIDE_ACTIVE
      → Utility function: macro risk outweighs match signal → WAIT
    Competition tier vs athlete availability:
      UCL Final (maximum commercial signal) but key player injured
      → Utility function: reduced event quality lowers expected utility
    FTP burn probability vs fraud risk:
      Strong WIN signal but MRS > 75 (COMPROMISED signal integrity)
      → Utility function: signal cannot be trusted → ABSTAIN

  The TMAS (tactical-matchup-intelligence.md) is explicitly utility-based:
    TMAS balances four competing dimensions (systemic, personnel, set piece,
    transition) to produce a net advantage score — not simply "who is better"
    but "given all trade-offs, what is the net utility of this system matchup."

  The ARI (athlete-readiness-index.md) is a utility function:
    Trades off fatigue, motivation, travel, injury risk, and availability
    into a single readiness score that represents expected utility
    of this athlete's contribution.

SPORTMIND FILES IMPLEMENTING THIS:
  core/confidence-output-schema.md — ENTER/WAIT/ABSTAIN utility function
  core/tactical-matchup-intelligence.md — TMAS as multi-dimensional utility
  core/athlete-readiness-index.md — ARI as readiness utility function
  core/contextual-signal-environment.md — CQS as context utility amplifier
  fan-token/fraud-signal-intelligence.md — MRS as signal integrity utility

HONEST CAPABILITY RATING: Strong for multi-variable trade-off problems.
SportMind's structured modifier chain is essentially a series of utility
computations. The ENTER/WAIT/ABSTAIN output is the terminal utility
function applied to all upstream computations.
```

---

## Architecture 5 — Learning Agent

```
WHAT IT IS:
  Improves performance over time by learning from experience.
  Has four components: performance element (current agent), critic
  (evaluates performance), learning element (updates based on feedback),
  problem generator (explores new approaches).

HOW SPORTMIND IMPLEMENTS IT:
  SportMind implements learning at the LIBRARY level, not the agent level.
  This is a deliberate design choice with significant implications.

  LIBRARY-LEVEL LEARNING (what SportMind does):
    Calibration records → modifier recalibration → library update
    126 records produced 6 recalibration cycles that updated modifier values
    Community contributions accelerate this cycle
    Version-controlled: learning is transparent, auditable, reversible

    The four components mapped:
    Performance element:  the agent running the six-step chain
    Critic:              the calibration record (was the direction correct?)
    Learning element:    the recalibration process (modifier value update)
    Problem generator:   community contributors submitting novel scenarios

  AGENT-LEVEL LEARNING (what SportMind does NOT do):
    SportMind agents do not update their own parameters between sessions.
    There is no in-context learning that persists across separate agent runs.
    Learning requires human-mediated calibration submission — it is not
    automatic, continuous, or unsupervised.

  WHY THIS IS INTENTIONAL:
    Unsupervised agent-level learning in a high-stakes commercial domain
    creates unverifiable drift. A modifier value that changes because an
    agent autonomously "learned" from three recent matches cannot be audited
    for correctness. Verifiable library-level learning with human review
    is slower but trustworthy.

SPORTMIND FILES IMPLEMENTING THIS:
  core/calibration-framework.md — the learning pipeline
  core/modifier-recalibration-v3/v4/v5/v6.md — documented learning outputs
  community/calibration-data/ — the training records
  CHANGELOG.md — transparent record of every learning-induced change

HONEST CAPABILITY RATING: Present but deliberately constrained. The learning
architecture is correct; the rate of learning is intentionally conservative.
Agents that need faster feedback loops can implement agent-level session
learning on top of the SportMind foundation — SportMind provides the domain
knowledge base that makes such learning meaningful.
```

---

## Architecture 6 — Multi-Agent Systems (MAS)

```
WHAT IT IS:
  Multiple agents coordinating to solve problems no single agent can solve
  alone. Includes cooperative, competitive, and mixed-motive systems.

HOW SPORTMIND IMPLEMENTS IT:
  core/multi-agent-coordination.md: the primary MAS framework
    Signal bus: shared state across agents
    Conflict resolution hierarchy: when agents disagree
    System orchestrator: meta-agent managing the fleet

  core/multi-agent-context-sharing.md: coordination protocol
    Signal authority model: which agent's output takes precedence
    Shared context bus: what agents share vs keep private
    Three failure modes and prevention rules

  Pattern architectures using MAS:
    Pattern 3 (Portfolio Monitor): multiple token agents reporting to orchestrator
    Pattern 4 (Pre-Match Signal Chain): macro + athlete + fan token agents in sequence
    Pattern 7 (Cross-Sport Monitor): sport-specific agents feeding cross-sport router

SPORTMIND MAS DESIGN PRINCIPLES:
  1. Signal authority is explicit — conflicting signals have a resolution hierarchy
  2. Each agent has a declared scope — no scope overlap without coordination rules
  3. The boundary holds across all agents — no agent in the system executes trades
  4. Escalation is always available — any agent can escalate to human

EXAMPLE MAS DEPLOYMENT:
  Arsenal Fan Token Intelligence System:
    Agent A: Macro monitor (Chiliz chain state, regulatory environment)
    Agent B: Match intelligence (Arsenal pre-match SMS, TMAS, ARI)
    Agent C: Fan token commercial (FTIS, PATH_2 state, FTP mechanics)
    Agent D: Community health (CHI, holder archetype distribution, fraud scan)
    Orchestrator: Combines A+B+C+D into unified signal; resolves conflicts

HONEST CAPABILITY RATING: Well-designed framework. MAS coordination requires
careful implementation by developers — SportMind provides the coordination
protocol but not the infrastructure.
```

---

## Architecture 7 — BDI (Belief-Desire-Intention)

```
WHAT IT IS:
  Agents have Beliefs (what they know), Desires (what they want),
  and Intentions (what they've committed to doing). Widely used in
  practical agent systems for complex, dynamic environments.

HOW SPORTMIND MAPS TO BDI:
  BELIEFS (the library and live data):
    The SportMind skill library is the agent's belief base.
    Freshness-checked data is the agent's current beliefs about the world.
    core/temporal-awareness.md manages belief validity.
    "I believe Arsenal will field their first XI because manager confirmed it."

  DESIRES (the goal framework):
    core/agent-goal-framework.md defines the desire structure.
    Terminal goals are stable desires; instrumental goals are derived.
    "I desire to produce an ENTER signal before the UCL match starts."

  INTENTIONS (the committed plans):
    The six-step reasoning chain is the committed plan — the agent has
    decided to follow this sequence and does not abandon it arbitrarily.
    core/autonomous-agent-framework.md defines when intentions are revised
    (when a breaking news event fires and the plan must be reconsidered).

BDI CONFLICT HANDLING IN SPORTMIND:
  Belief revision: BREAKING_NEWS_EVENT fires → beliefs updated → plan reconsidered
  Desire conflict: multiple goals active → goal hierarchy resolves conflict
  Intention reconsideration: macro_override → current intention suspended
```

---

## Summary table

```
ARCHITECTURE            SPORTMIND IMPLEMENTATION         STRENGTH
────────────────────────────────────────────────────────────────
Reactive                Breaking news triggers,           ★★★
                        freshness flags, macro override
────────────────────────────────────────────────────────────────
Model-Based Reflex      Six-step chain, tendency          ★★★★★
                        profiles, lifecycle models
────────────────────────────────────────────────────────────────
Goal-Based              agent-goal-framework.md,          ★★★★
                        autonomy spectrum
────────────────────────────────────────────────────────────────
Utility-Based           ENTER/WAIT/ABSTAIN output,        ★★★★★
                        TMAS, ARI, CQS, MRS
────────────────────────────────────────────────────────────────
Learning                Calibration → recalibration       ★★★
                        (library-level, not agent-level)
────────────────────────────────────────────────────────────────
Multi-Agent Systems     Coordination framework,           ★★★★
                        signal authority, orchestrator
────────────────────────────────────────────────────────────────
BDI                     Belief (library) + Desire         ★★★★
                        (goals) + Intention (chain)
────────────────────────────────────────────────────────────────
```

---

*SportMind v3.66 · MIT License · sportmind.dev*
*See also: core/autonomous-agent-framework.md · core/agent-goal-framework.md*
*core/agent-intelligence-model.md · core/multi-agent-coordination.md*
*core/reasoning-patterns.md · core/calibration-framework.md*
