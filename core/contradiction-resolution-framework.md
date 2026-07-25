# Contradiction Resolution Framework

**Domain:** core/contradiction-resolution-framework.md
**Version:** v4.1.37
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Unified contradiction resolution framework for all SportMind
agent types. An agent that cannot resolve contradictions will either
be paralysed by conflict or arbitrarily pick one signal and ignore
the other. This framework provides the structured hierarchy that
governs every contradiction SportMind agents encounter.

---

## Why Contradictions Occur

SportMind loads intelligence from multiple layers simultaneously.
Contradictions arise when:

- The macro regime signals HOLD but the sport layer signals ENTER
- An aggregator source says a fan token is active but on-chain shows it dormant
- Historical pattern says home team wins derbies but current form says away
- Two modifiers push in opposite directions with similar magnitude
- A PTG supply event fires automatically but the CHZ regime is CAPITULATION

Contradictions are not failures — they are information. The resolution
process itself produces intelligence about signal quality and confidence.

---

## Five Contradiction Types

### Type 1 — Layer Contradiction

*Cross-layer directional conflict: one layer says ENTER, another says HOLD or opposite direction.*

Most common contradiction. Occurs when signals from different library
layers point in different directions. The sport layer says HOME STRONG.
The macro layer says CAPITULATION ×0.70 and HOLD.

### Type 2 — Source Tier Contradiction

*Different facts from different source tiers.*

Aggregator source says fan token X is active. On-chain data shows
no treasury activity for 180 days and logo is black on fantokens.com.
Two sources, two different facts, same subject.

### Type 3 — Temporal Contradiction

*Current signal contradicts historical pattern.*

Historical calibration says this team wins 78% of home derbies.
Current signal shows the team has lost its last 4 home fixtures
with confirmed key player absences. Recency vs pattern.

### Type 4 — Modifier Contradiction

*Two modifiers apply but push in opposite directions.*

Derby active modifier: ×1.20 (favours home team, historical pattern).
Squad archetype shift modifier: SHORT CDI horizon (uncertainty discount).
Both apply. Both affect the same output. Direction of effect differs.

### Type 5 — Regime Contradiction

*Supply event fires automatically but macro regime signals HOLD.*

A PTG burn event executes on-chain regardless of CHZ macro state.
The agent's discretionary HOLD condition is in force. What executes,
what is deferred, and what is the agent's obligation?

---

## Six Resolution Rules (Strict Hierarchy)

Apply in order. Stop at the first rule that resolves the contradiction.
Do not skip rules. Do not apply lower rules before higher ones.

### Rule 1 — Safety Gate First

**HOLD conditions always win. No exception.**

```
IF any of the following are true:
  · CAPITULATION x0.70 regime active AND signal class below EXECUTION
  · User wallet safety guardrail is engaged
  · FM8 (Liquidity Illusion) — pool too thin to absorb position
  · Lineup unconfirmed at T-2h (football, rugby) — do not ENTER
  · Signal class = SPECULATIVE regardless of direction strength

THEN: OUTPUT = HOLD · do not resolve further.
State which HOLD condition applied.

EXCEPTION — AUTOMATIC SUPPLY EVENTS:
  PTG burns and FTP settlement execute automatically on-chain.
  They are NOT discretionary agent actions.
  CAPITULATION regime does NOT prevent PTG burns from executing.
  HOLD applies to the agent's discretionary actions, not to
  on-chain mechanics that execute without agent intervention.
  See Type 5 (Regime Contradiction) for full distinction.
```

### Rule 2 — Source Tier Hierarchy

**On-chain > Tier 1 > Tier 1.5 > Tier 2. Never average conflicting sources.**

```
HIERARCHY:
  Level 1: On-chain data (chiliscan.com, blockchain explorer)
    · Highest authority for supply events, treasury movements,
      token status, burn confirmations
  Level 2: Tier 1 official sources (chiliz.com, fca.org.uk, etc.)
    · Highest authority for announcements, partnerships, regulations
  Level 3: Tier 1.5 fast signals (@FanTokens, @Chiliz on X)
    · Fast signal only · requires Tier 1 corroboration to escalate
  Level 4: Tier 2 (aggregators, crypto news, sports media)
    · Context only · never overrides higher tier

RESOLUTION: Higher tier governs. Never split the difference between
  a Tier 1 and Tier 2 signal. The Tier 2 signal is incorrect or
  stale until Tier 1 confirms otherwise.

EXCEPTION: If two Tier 1 sources contradict each other, apply
  Rule 3 (Layer Hierarchy) or Rule 4 (Temporal Recency).
```

### Rule 3 — Layer Hierarchy

**Macro > Fan Token > Market > Sport > Athlete. Lower layers modulate magnitude, never reverse direction.**

```
HIERARCHY (highest → lowest authority for direction):
  1. macro/ — CHZ regime, regulatory, market cycle
  2. fan-token/ — supply mechanics, FTP, PTG, holder behaviour
  3. market/ — CDI, commercial tier, competition calendar
  4. sports/ — event playbooks, risk variables, sport mechanics
  5. athlete/ — form, availability, composite modifier

RESOLUTION:
  Direction is set by the highest layer that produces a signal.
  Lower layers apply as magnitude modifiers to that direction.
  A strong athlete modifier (×1.25) does NOT reverse a direction
  set by the macro layer. It modulates confidence and magnitude.

  Exception: if the highest signalling layer is NEUTRAL/HOLD,
  the next layer's direction takes precedence. Work down the
  hierarchy until a directional layer is found.

RULE: Never let a lower layer reverse a higher layer's direction.
  Lower layers MODULATE. They do not OVERRIDE.
```

### Rule 4 — Temporal Recency

**Three-question test. Recency alone does not determine priority.**

```
Before applying recency as a tiebreaker, answer three questions:

Q1: Is the historical pattern structurally enduring, or event-dependent?
  · Enduring: derby home advantage · qualifying delta (F1) · dew factor
  · Event-dependent: form streak · recent results · squad availability

Q2: Has the context changed sufficiently to invalidate the pattern?
  · Squad archetype shift = context change · CDI horizon resets
  · Coaching succession = context change · pattern may not apply

Q3: Is the current signal from a confirmed primary source?
  · Confirmed: official lineup, on-chain transaction, regulatory enactment
  · Unconfirmed: rumour, aggregator-only, journalist speculation

RESOLUTION:
  IF pattern is enduring AND context unchanged AND current signal
    is confirmed: use weighted composite (pattern + current signal).
  IF pattern is event-dependent AND current signal is confirmed:
    current signal takes priority.
  IF current signal is unconfirmed: default to historical pattern
    with uncertainty discount (MEDIUM or lower confidence).
```

### Rule 5 — Modifier Magnitude

**Larger magnitude takes directional priority. Never silently cancel opposing modifiers.**

```
WHEN two modifiers oppose each other:

Step 1: Calculate net modifier value
  (larger modifier value) − (smaller modifier value) = net

Step 2: Apply net modifier in direction of the larger modifier

Step 3: Reduce confidence tier by one level (HIGH → MEDIUM, etc.)
  Opposing modifiers reduce confidence regardless of net value.

Step 4: Document both modifiers in output — never silently drop one.
  An opposing modifier that is dropped without documentation
  violates Transparency (Dimension 14).

NEVER CANCEL: if two modifiers exactly offset (net = 0),
  output is NEUTRAL on that dimension with MEDIUM confidence.
  Do not treat as if neither modifier existed.
```

### Rule 6 — Unresolvable Contradictions

**HOLD + full contradiction report. Forced direction under unresolvable contradiction is a more serious failure than HOLD.**

```
A contradiction is UNRESOLVABLE when:
  · Rules 1-5 have been applied and no resolution is reached
  · Two Tier 1 primary sources directly contradict each other
    on a material fact (not a magnitude difference)
  · The contradiction involves a missing file from a known gap
    (e.g. temporal-reasoning-framework.md before v4.1.35)

WHEN UNRESOLVABLE:
  OUTPUT: HOLD
  Required contradiction report fields:
    · Contradiction type (Type 1-5)
    · Which sources or layers are in conflict
    · Why Rules 1-5 did not resolve it
    · What information would resolve it
    · Recommended action (monitor / escalate / wait)

RATIONALE: Forcing a direction when the contradiction is
  unresolvable introduces fabricated certainty. An honest HOLD
  with a contradiction report is more valuable to the operator
  than a direction that discards unresolved conflict silently.
```

---

## 12 Agent Rules

```
RULE 1: Apply resolution rules in hierarchy order. Never skip.
RULE 2: Document every contradiction encountered, even if resolved.
RULE 3: HOLD conditions (Rule 1) override all other rules. No exception.
RULE 4: PTG burns and FTP settlement are on-chain mechanics —
  CAPITULATION regime does not block them. Only discretionary
  agent actions are subject to HOLD conditions.
RULE 5: Never average conflicting source tiers. Hierarchy applies.
RULE 6: Lower layers modulate direction, never reverse it.
RULE 7: Recency alone is not sufficient to override historical pattern.
  Apply the three-question test before recency tiebreaking.
RULE 8: When opposing modifiers apply, always document both.
  Never silently cancel a modifier.
RULE 9: A net modifier of zero does not mean no modifiers applied.
  Output NEUTRAL with documented modifiers.
RULE 10: Unresolvable contradictions output HOLD + full report.
  Never force direction to avoid outputting HOLD.
RULE 11: If a contradiction is resolved by Rule 1 (HOLD), always
  state which specific HOLD condition applied.
RULE 12: After resolution, reduce confidence tier by one level
  if any contradiction was present, even if resolved cleanly.
  Contradicted signals carry inherent uncertainty.
```

---

## Four Worked Examples

### Example 1 — Type 1: CAPITULATION + Strong Event Signal

```
SITUATION:
  CHZ regime: CAPITULATION ×0.70 active
  Sport layer: HOME STRONG · adjusted score 72.4 · signal class EXECUTION
  Fan token layer: supply event potential confirmed (dual fan token derby)

RESOLUTION PROCESS:
  Rule 1 (Safety Gate): Is signal class below EXECUTION under CAPITULATION?
    Check: CAPITULATION with EXECUTION class signal — is HOLD mandatory?
    Per library: CAPITULATION suppresses confidence but does not
    auto-HOLD EXECUTION class signals. Signal proceeds with ×0.70.
  Rule 3 (Layer Hierarchy): Macro layer applies ×0.70 modifier.
    Sport layer direction stands. Macro modulates magnitude.

OUTPUT: HOME (reduced magnitude) · adjusted_score 72.4 × 0.70 = 50.7
  Confidence: MEDIUM (reduced one tier per Rule 12)
  Modifiers disclosed: CHZ CAPITULATION ×0.70 applied
```

### Example 2 — Type 2: Aggregator Active + On-Chain Dormant

```
SITUATION:
  fantokens.com shows fan token X as active, logo in brand colours.
  chiliscan.com: no treasury transactions in 180 days.
  fantokens.com: logo has turned black/greyscale on socios.com.

RESOLUTION PROCESS:
  Rule 2 (Source Tier): On-chain data > aggregator.
    On-chain = no activity. Black logo = potential inactivity signal.
    Aggregator display may be stale.

OUTPUT: VERIFY before using this token in any analysis.
  Do not assume active status. Treat as POTENTIALLY INACTIVE.
  Escalate to primary source (official club/Chiliz announcement).
  Flag with BLACK LOGO SIGNAL in briefing.
```

### Example 3 — Type 3: Derby Draw Premium vs Current Form

```
SITUATION:
  Historical calibration: this derby produces DRAW 42% of the time.
  Derby home advantage modifier: ×1.20 (home team historically stronger).
  Current signal: away team confirmed lineup · home team missing key midfield.
  Away team last 6 home: 5 wins 1 draw.

RESOLUTION PROCESS:
  Rule 4 (Temporal Recency): Three-question test.
    Q1: Is derby pattern enduring? YES — structural historical pattern.
    Q2: Has context changed? YES — home team missing key midfield (confirmed).
    Q3: Is current signal confirmed? YES — official lineup published.
    → Context changed sufficiently. Current signal adjusts historical weight.

  Rule 5 (Modifier Magnitude): Derby home advantage ×1.20 vs availability
    discount (estimate ×0.85 for confirmed absence). Net: reduced home edge.

OUTPUT: DRAW or AWAY lean · MEDIUM confidence
  Historical derby premium reduced by confirmed availability signal.
  Document: derby pattern partially overridden by confirmed context change.
```

### Example 4 — Type 5: PTG Burn + CAPITULATION Regime

```
SITUATION:
  CHZ regime: CAPITULATION ×0.70 active.
  Fan token national team wins SF match.
  PTG 7.5% burn expected per the programme mechanic.
  Agent is operating with HOLD conditions under CAPITULATION.

RESOLUTION PROCESS:
  Rule 1 (Safety Gate): Does CAPITULATION block PTG burn?
    NO. PTG burns execute automatically on-chain by smart contract.
    They are not agent actions. HOLD applies to discretionary
    agent actions only (ENTER, EXIT, SIZE).
    
  CRITICAL DISTINCTION:
    PTG burn: EXECUTES AUTOMATICALLY. Agent cannot block or trigger it.
    Agent's HOLD: applies to any discretionary fan token position
    the agent might take around the PTG event.
    
OUTPUT:
  PTG burn: CONFIRMED EXECUTING (on-chain, agent-independent)
  Discretionary position: HOLD (CAPITULATION regime active)
  The burn occurs. The agent does not enter a position around it.
  Verify burn on chiliscan.com when available.
```

---

## Known Contradiction Hotspots

| Combination | Type | Standard resolution |
|---|---|---|
| CAPITULATION + sport layer ENTER | Type 1 | Rule 1 + Rule 3: magnitude suppressed, direction survives if EXECUTION class |
| Aggregator active + on-chain dormant | Type 2 | Rule 2: on-chain governs · verify · black logo signal |
| PTG burn + CAPITULATION regime | Type 5 | Rule 1 exception: PTG executes automatically, HOLD is discretionary only |
| Derby premium + confirmed key absence | Type 3 | Rule 4: three-question test · context changed · reduce premium |
| Two Tier 1 sources disagree on fan token status | Type 2 | Escalate to on-chain (Level 1) · if no on-chain signal: VERIFY flag |
| High PTG burn expectation + low CHZ price | Type 1 | Rule 3: supply event (fan-token layer) independent of CHZ price (macro) |
| TRANSITION gate active + strong pre-season signal | Type 3 | Rule 4: CDI horizon SHORT · pre-season signal ≠ CDI confirmation yet |
| Bridge volume spike + directional signal | Type 1 | Rule 3: bridge volume = infrastructure signal (FM7) · not a demand signal |

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Contradiction types as signal intelligence patterns |
| Reasoning (2) | ACTIVE | Causal and multi-signal reasoning across five contradiction types |
| Context (3) | ACTIVE | Temporal and source context in Types 2, 3, 4 |
| Memory (4) | ACTIVE | Historical pattern vs current signal (Type 3), hotspot table |
| Judgment (5) | ACTIVE | Primary dimension — 5c Conflict Resolution across all six rules |
| Attention (6) | ACTIVE | Identifying when a contradiction has occurred before resolution |
| Communication (7) | ACTIVE | Contradiction report format, modifier documentation requirement |
| Verification (8) | ACTIVE | Source tier hierarchy (Rule 2), on-chain confirmation priority |
| Learning (9) | ACTIVE | Worked examples enable error classification and modifier revision |
| Integration (10) | ACTIVE | Cross-layer resolution (Rule 3), multi-signal combination |
| Calibration (11) | ACTIVE | Confidence tier reduction under contradiction (Rule 12) |
| Adaptation (12) | ACTIVE | Regime detection as contradiction context (Type 5) |
| Ethics (13) | ACTIVE | Rule 6: forced direction under contradiction = fabricated certainty |
| Transparency (14) | ACTIVE | Rule 8: never silently cancel modifiers · full disclosure required |
| Execution (15) | ACTIVE | Rules 3-5 govern execution timing and magnitude under contradiction |
| Collaboration (16) | ACTIVE | 16d Conflict Arbitration: resolving contradictions across agents |

---

## COMPATIBILITY

- core/mind-dimensions-framework.md — fills Dimension 5c (Conflict Resolution) gap
- core/temporal-reasoning-framework.md — Type 3 contradictions use temporal recency rules
- fan-token/agent-failure-modes-fan-token.md — FM1, FM7, FM8 are contradiction triggers
- fan-token/burn-to-glory-framework.md — Type 5 (PTG + CAPITULATION) worked example
- fan-token/fan-token-play.md — FTP PATH_2 settlement is Rule 1 exception candidate
- macro/chz-tokenomics.md — CAPITULATION regime as Type 1 and Type 5 trigger
- core/signal-confidence-framework.md — Rule 12 integrates with confidence tier system

© 2026 SportMind
