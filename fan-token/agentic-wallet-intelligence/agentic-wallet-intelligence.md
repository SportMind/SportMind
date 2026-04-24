# Agentic Fan Token Wallet Intelligence — SportMind

**The bridge between SportMind signal outputs and autonomous wallet action.**

This file answers a question no other sports intelligence library addresses:
*given a SportMind signal, what should an autonomous agent actually do with it —
and what must it never do without human confirmation?*

Zero-dependency. Works with any wallet infrastructure. The reasoning frameworks
are universal; the execution layer is yours to implement.

---

## Overview

A SportMind signal produces a structured output: direction, adjusted_score,
recommended_action, flags. A human reading this knows what to consider.
An agentic wallet needs more: explicit action thresholds, position sizing rules,
escalation triggers, safety rails, and — critically — a clear boundary between
what the agent decides and what the human must confirm.

This file defines that boundary. It is not a trading system. It is a reasoning
framework for agents that manage fan token positions, governance participation,
and commercial monitoring on behalf of their operators.

---

## Domain Model

### The three agentic wallet contexts

```
CONTEXT 1 — POSITION MONITORING AGENT
  Monitors an existing fan token position.
  Actions: alert, log, flag for review, adjust CDI tracking.
  Never: open new positions, close positions without threshold breach.
  Autonomy ceiling: Level 2 (semi-autonomous).

CONTEXT 2 — GOVERNANCE PARTICIPATION AGENT
  Monitors governance proposals and casts votes on behalf of holder.
  Actions: vote within delegated mandate, abstain outside mandate, escalate.
  Never: vote on constitutional changes, large position votes, novel proposals.
  Autonomy ceiling: Level 1 (advisory) for novel proposals, Level 2 for routine.

CONTEXT 3 — COMMERCIAL SIGNAL AGENT
  Monitors fan token commercial signals for brand, sponsorship, or media teams.
  Actions: generate briefings, alert on CDI changes, flag transfer window signals.
  Never: financial execution. This context is intelligence-only.
  Autonomy ceiling: Level 3 (autonomous with review) — no financial execution.
```

### Signal thresholds for autonomous action

```
SIGNAL THRESHOLD FRAMEWORK:

  SMS ≥ 85 + recommended_action = ENTER + no blocking flags:
    → Agent may flag as HIGH CONFIDENCE opportunity
    → Context 1 agent: notify operator; do not act without confirmation
    → Context 2 agent: N/A
    → Context 3 agent: generate and dispatch briefing automatically

  SMS 75–84 + recommended_action = ENTER + no blocking flags:
    → MEDIUM CONFIDENCE signal
    → All contexts: log and notify; do not act autonomously

  SMS < 75 OR any blocking flag active:
    → INSUFFICIENT CONFIDENCE for autonomous action
    → All contexts: monitor and log only

  SMS ≥ 80 + recommended_action = EXIT + any blocking flag:
    → EXIT SIGNAL with urgency
    → Context 1 agent: escalate to human immediately; flag as priority
    → Never exit autonomously — position changes require human confirmation

  macro_override_active = true:
    → HALT all position signals regardless of SMS
    → Macro override is a hard stop; no SMS score overrides it
    → Log the override state; check again after macro state clears

BLOCKING FLAGS — any of these present = no autonomous action:
  lineup_unconfirmed: true
  macro_override_active: true
  mrs_elevated: true (Market Regime Signal — fraud/manipulation elevated)
  edli_above_threshold: true (Exchange Delisting Risk)
  liquidity_insufficient: true
```

### Position sizing framework

```
POSITION SIZING PRINCIPLES FOR AUTONOMOUS AGENTS:
  
  SportMind does not produce specific monetary position sizes — that is the
  operator's decision based on their risk tolerance and portfolio parameters.
  What SportMind provides is a signal confidence framework that maps to
  relative sizing guidance.

  SIGNAL CONFIDENCE → RELATIVE SIZE GUIDANCE:
    SMS 85+, no flags, confirmed lineup:   Maximum allowed position (operator-defined)
    SMS 75-84, no flags:                   60–80% of maximum
    SMS 65-74, no flags:                   30–50% of maximum
    SMS < 65:                              Monitor only; no position signal

  CONCENTRATION RULES (hard limits for autonomous agents):
    Never exceed operator-defined maximum per single token
    Never hold > 40% of portfolio in tokens from same league (correlation risk)
    Never increase position size without fresh signal recalculation
    Always reduce position size when CDI is declining, regardless of SMS

  DIVERSIFICATION SIGNAL:
    If monitoring > 3 tokens and all show ENTER simultaneously:
    Flag for human review — correlated signals may indicate macro event
    that the agent's individual token analysis has not captured.
    This is the most common autonomous agent error in fan token contexts.
```

---

## Governance Participation Intelligence

```
GOVERNANCE MANDATE FRAMEWORK:

  Before deploying a governance participation agent, the operator defines
  a mandate — the scope within which the agent can vote autonomously.

  MANDATE TIERS:

  Tier A — ROUTINE VOTES (agent votes autonomously within mandate):
    Community events and match day activations
    Token utility feature additions (new merchandise, experiences)
    Cosmetic changes (badge updates, seasonal designs)
    Standard poll votes with no financial or structural implication
    Operator approval required: NO (within defined mandate)

  Tier B — MATERIAL VOTES (agent flags and recommends; operator confirms):
    Changes to token utility scope
    Partnership announcements involving token integration
    Voting on club operational decisions
    Any vote described as "historic" or "first time"
    Operator approval required: YES — agent recommends only

  Tier C — CONSTITUTIONAL VOTES (agent never votes autonomously):
    Changes to tokenomics or supply mechanics
    Platform migration (Chiliz Chain to another chain)
    Governance structure changes (voting weight, quorum rules)
    Any vote that modifies what the token represents
    Operator approval required: MANDATORY — halt, escalate, await instruction

  VOTE TIMING INTELLIGENCE:
    Many governance votes have short windows (24-72h).
    Agent should alert at: 72h remaining, 24h remaining, 6h remaining.
    If operator unreachable and Tier B/C vote closes: ABSTAIN.
    Abstention is always safer than a wrong autonomous vote.

GOVERNANCE SIGNAL INTEGRATION:
  Load fan-token/fan-token-governance-intelligence.md for full governance
  signal framework before applying this protocol.
  Governance participation rate (active voting) is a CHI positive signal.
  Agents that vote regularly on behalf of holders improve CHI for the token.
```

---

## Decision Trees

### Decision Tree 1: Pre-match signal → wallet action

```
INCOMING SIGNAL:
  direction, adjusted_score, recommended_action, flags

  Step 1: Check macro_override_active
    YES → HALT. Log. Do not proceed. Check again in 4h.
    NO  → Continue.

  Step 2: Check blocking flags
    Any blocking flag active → Monitor only. Log reason. No action.
    No blocking flags → Continue.

  Step 3: Check SMS threshold
    SMS < 65 → Monitor only.
    SMS 65-74 → Log. Notify operator. No autonomous action.
    SMS 75-84 → Generate briefing. Notify. Await operator confirmation for positions.
    SMS 85+ → High confidence. Notify with full signal chain. Await confirmation.

  Step 4: Check recommended_action
    ENTER → Follow SMS threshold protocol above.
    HOLD → Confirm current position. Log signal. No action required.
    EXIT → Escalate immediately regardless of SMS. EXIT always requires human.
    WAIT → Monitor. Recalculate after defined wait period.

  Step 5: Dispatch output
    Log full signal chain with all modifiers applied.
    Include: timestamp, token, SMS, direction, flags, action_taken.
    Never discard reasoning — the log is auditable history.
```

### Decision Tree 2: Governance vote → agent action

```
INCOMING GOVERNANCE EVENT:
  proposal_id, proposal_type, vote_deadline, impact_assessment

  Step 1: Classify proposal tier (A / B / C per mandate framework)
    Tier A → Vote per mandate. Log. Confirm on-chain.
    Tier B → Generate recommendation. Alert operator. Await confirmation.
    Tier C → HALT autonomous action. Alert operator urgently. Do not vote.

  Step 2: Check deadline
    > 72h remaining → Standard processing
    24-72h remaining → Escalate urgency of operator notification
    < 24h remaining → HIGH URGENCY. All channels. If Tier B/C and operator
                      unreachable: ABSTAIN. Log abstention reason.
    Deadline passed → Log missed vote. Review mandate timing parameters.

  Step 3: Confirm vote execution
    On-chain confirmation required before marking as complete.
    Log: vote_cast, vote_direction, timestamp, tx_hash.
```

### Decision Tree 3: CDI declining → position review

```
CDI DECLINE DETECTED:
  CDI drop > 10 points in 48h window

  Step 1: Check decline cause
    Match result (expected) → Standard CDI decay. No position action.
    Transfer rumour (negative Tier 1 source) → Escalate. Load transfer intelligence.
    On-chain sell pressure → Check MRS. If MRS elevated: flag urgency.
    Unexplained (no news source) → Investigate. Do not act until cause identified.

  Step 2: CDI magnitude check
    CDI drop 10-20 points → Alert. Monitor closely. No position change.
    CDI drop 20-35 points → Escalate to operator. Recommend review.
    CDI drop > 35 points → CRITICAL. Escalate immediately.
                           Macro override check. MRS check.
                           Await operator instruction.

  Step 3: Recovery assessment
    CDI recovering within 24h + cause resolved → Resume normal monitoring.
    CDI not recovering after 48h → Maintain escalation status.
```

---

## Safety Rail Architecture

```
HARD RAILS — technically enforced by the agent operator:

  1. FINANCIAL EXECUTION CAP
     No single autonomous action may exceed operator-defined maximum.
     This cap is set at deployment; it cannot be changed by the agent.

  2. MACRO OVERRIDE HARD STOP
     macro_override_active = true is an absolute halt.
     No SMS, no urgency, no exception overrides macro override.

  3. EXIT ALWAYS REQUIRES HUMAN
     No position exit is fully autonomous. EXIT signals always escalate.
     The agent may recommend, alert, and prepare — never execute exit alone.

  4. GOVERNANCE TIER C HARD BLOCK
     Constitutional votes (Tier C) are hard-blocked from autonomous execution.
     Agent abstains if confirmation is unavailable before deadline.

  5. MINIMUM SIGNAL FRESHNESS
     Agent must recalculate signal before any action if last calculation
     was > 4h ago. Stale signals are not actionable signals.

  6. CORRELATION FLAG
     If ≥ 3 monitored tokens show simultaneous ENTER signals:
     Flag for human review. Do not act on all signals simultaneously.

SOFT RAILS — recommended, operator-configurable:

  7. OVERNIGHT PAUSE
     During 23:00-06:00 local time, reduce autonomy level by one.
     Level 2 → Level 1. Level 1 → Level 0.
     Rationale: major news events without human monitoring capacity.

  8. VOLATILITY CIRCUIT BREAKER
     If CHZ price moves > 15% in 4h: pause position signals, check macro.
     Do not act during extreme CHZ volatility without macro state check.

  9. NOVELTY FLAG
     If a governance proposal or token event has no precedent in the
     agent's training data: flag as NOVEL, escalate for human review.
     "This is the first time this type of vote has appeared for this token"
     is a reason to pause, not proceed.
```

---

## Example Agent Implementations

### Example 1: $AFC PATH_2 position monitor

```
AGENT PROFILE:
  Token: $AFC (Arsenal)
  Special mechanics: PATH_2 (WIN = supply reduction)
  Primary watch: match results, set piece goals, squad news
  Autonomy level: 2

WATCH CONDITIONS:
  Match day (T-6h to T+48h): load sport-statistics-football.md for set piece signals
  Squad news: Category 2 alert if Tier 1 ATM player or set piece specialist absent
  Match result: if WIN — flag PATH_2 event, note supply reduction, log CDI extension
  If LOSS — note supply addition (PATH_2 reversal), log CDI impact

AUTOMATED OUTPUTS:
  Pre-match: signal briefing with set piece specialist status
  Post-match: PATH_2 status update, CDI extension / contraction logged
  Transfer window: ATM recalculation on any confirmed signing/departure

NEVER AUTOMATES:
  Position sizing decisions
  Exit from position
  Governance votes without operator mandate confirmation
```

### Example 2: Multi-token PL governance delegate

```
AGENT PROFILE:
  Tokens: $AFC, $CITY, $SPURS, $AVL, $EFC, $CPFC, $LUFC (all 7 PL tokens)
  Primary function: governance participation
  Mandate: Tier A votes autonomous; Tier B/C escalate
  Autonomy level: 2 (Tier A), 1 (Tier B), 0 (Tier C)

WATCH CONDITIONS:
  Daily governance scan across all 7 token platforms
  72h, 24h, 6h deadline alerts
  Proposal classification per mandate framework

AUTOMATED OUTPUTS:
  Tier A: cast vote, log tx_hash, notify operator of vote cast
  Tier B: analysis brief, recommendation, operator notification
  Tier C: urgent escalation, abstention if deadline passes without instruction

NEVER AUTOMATES:
  Any structural tokenomics vote
  Any vote described as "historic" or without clear precedent
```

### Example 3: WC2026 national token signal agent ($ARG, $POR)

```
AGENT PROFILE:
  Tokens: $ARG (Argentina), $POR (Portugal)
  Active window: June 11 – July 19, 2026
  Primary watch: match results, squad news, tournament progression
  Autonomy level: 3 (briefing generation), 1 (position signals)

WATCH CONDITIONS:
  Match day: pre-match signal (T-4h), post-match CDI update (T+2h)
  Squad news: Category 1/2 injury alerts (Messi, Ronaldo = Category 1)
  Knockout: each round advances = CDI extension + NCSI spike calculation
  Elimination: immediate CDI calculation with tournament_exit_modifier

AUTOMATED OUTPUTS:
  Pre-match signal briefings dispatched automatically
  Post-match CDI update dispatched automatically
  Injury alerts dispatched immediately on confirmation (Tier 1 source only)

NEVER AUTOMATES:
  Position signals without SMS ≥ 80 AND confirmed lineup
  Any action when macro_override_active = true
```

---

## Autonomous Execution

**This file's own autonomous execution rules:**

**Trigger conditions:**
- New governance proposal detected for any monitored token
- CDI drop > 20 points in 24h for any monitored token
- PATH_2 goal scored (for $AFC agents)
- macro_override_active status changes (either direction)

**At autonomy Level 2:**
- Generate briefing and notify operator
- Log signal state at time of trigger
- Pre-classify governance proposals (Tier A/B/C) for operator review

**At autonomy Level 3:**
- Dispatch briefings without operator confirmation
- Execute Tier A governance votes autonomously within mandate
- Log all actions with full reasoning chain

**Hard boundaries (never autonomous at any level):**
- Position entry or exit
- Tier B/C governance votes
- Any action when macro_override_active = true
- Any action when MRS = ELEVATED

---

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Full pre-match protocol | Load this file + sport-domain-football.md | Standard combined load |
| Governance classification | Load Governance Participation Intelligence | Before any vote |
| CDI monitoring | Load fan-token-lifecycle.md + this file | CDI decay context |
| PATH_2 specific | Load gamified-tokenomics-intelligence + this file | $AFC only |
| Multi-token WC2026 | Load world-cup-2026-pre-tournament.md + this file | June–July 2026 |

---

## Agent Reasoning Prompts

- "SMS ≥ 85, no blocking flags: high confidence signal. Notify operator. Await confirmation before any position action."
- "EXIT signal received: escalate immediately. Never execute exit autonomously. Prepare reasoning chain for operator."
- "macro_override_active = true: halt all signals. Log state. No action until override clears."
- "Governance proposal Tier C detected: abstain or await operator. Never vote on constitutional changes autonomously."
- "Simultaneous ENTER on 3+ tokens: flag correlation. Human review required before acting on any."
- "CDI drop > 35 points unexplained: critical escalation. Do not act until cause is identified."

---

## Data Sources

- On-chain governance proposals: Socios platform API, Chiliz Chain governance feeds
- Fan token price and volume: CoinGecko, CoinMarketCap (Tier 2 — verify against on-chain)
- Match results: official competition websites (Tier 1)
- Squad news: official club channels (Tier 1 — do not use Tier 2 for autonomous action)
- CHZ price (for volatility circuit breaker): Binance, Kraken (Tier 2)

---

## Compatibility

**Load alongside:** `fan-token/fan-token-lifecycle.md` · `fan-token/fan-token-governance-intelligence.md`
**Path-2 tokens:** `fan-token/gamified-tokenomics-intelligence/`
**Sport-specific:** relevant sport domain skill
**Macro gate:** `macro/macro-crypto-market-cycles.md` — always load before any wallet action
**Agent framework:** `core/autonomous-agent-framework.md` — autonomy levels and safety model

---

*SportMind v3.87.0 · MIT License · sportmind.dev*
