# Mind Dimensions Framework

**Domain:** core/mind-dimensions-framework.md
**Version:** v4.1.33
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Canonical reference for SportMind's 16 Mind Dimensions and
64 sub-dimensions. Mapping conventions, status values, and known gaps.

---

## Why Dimensions Exist

SportMind files teach AI agents how to reason about sports intelligence.
The Mind Dimensions system makes explicit *which reasoning capabilities*
each file strengthens. This serves three purposes:

1. **Gap visibility** — two files can both claim "Calibration: ACTIVE"
   but one validates direction accuracy and the other validates modifier
   magnitude. Sub-dimensions make this visible.

2. **File completeness gate** — every new library file must map to all
   16 dimensions before merge. Omissions are visible, not hidden.

3. **Agent capability audit** — operators can assess which dimensions
   are well-served and which are thin by scanning MIND DIMENSIONS sections
   across the library.

---

## The 16 Dimensions

### 1. Intelligence

*Domain knowledge, signal awareness, pattern recognition.*

The agent knows what to look for. It recognises meaningful events,
understands domain-specific patterns, and has the background knowledge
to interpret signals correctly.

| Sub-dimension | Description |
|---|---|
| 1a. Domain knowledge | Knowing the sport, token type, competition structure, or regulatory framework |
| 1b. Signal awareness | Recognising when a meaningful event has occurred |
| 1c. Pattern recognition | Identifying recurring structures across events |
| 1d. Contextual relevance | Knowing which signals matter in which context |

---

### 2. Reasoning

*Causal, probabilistic, multi-signal, and temporal reasoning.*

The agent can think about why signals matter, how probable outcomes are,
how multiple signals interact, and how timing affects interpretation.

| Sub-dimension | Description |
|---|---|
| 2a. Causal reasoning | Understanding why a signal produces an effect |
| 2b. Probabilistic reasoning | Weighting outcomes by likelihood, not certainty |
| 2c. Multi-signal reasoning | Combining signals across layers without conflation |
| 2d. Temporal reasoning | Reasoning about timing, sequence, and signal decay |

---

### 3. Context

*Macro, event, historical, cultural, and temporal context.*

The agent understands the environment in which signals occur. The same
event can mean different things in different contexts.

| Sub-dimension | Description |
|---|---|
| 3a. Macro context | CHZ regime, regulatory environment, market cycle |
| 3b. Event context | Competition stage, fixture significance, tournament position |
| 3c. Historical context | Prior outcomes, precedent chain, calibration history |
| 3d. Cultural/regional context | Fandom models, regulatory jurisdiction, language/market |

---

### 4. Memory

*Episodic, semantic, procedural, and working memory.*

The agent retains and applies relevant knowledge across time and across
the span of a single reasoning session.

| Sub-dimension | Description |
|---|---|
| 4a. Episodic memory | Specific past events — matches, burns, outcomes |
| 4b. Semantic memory | Frameworks, definitions, structural facts |
| 4c. Procedural memory | How to execute — reasoning chains, playbooks |
| 4d. Working memory | Holding multiple signals in context during a single session |

---

### 5. Judgment

*Uncertainty, risk weighting, HOLD conditions, and conflict resolution.*

The agent knows when to act, when to wait, and how to weight competing
signals when they conflict.

| Sub-dimension | Description |
|---|---|
| 5a. Uncertainty handling | Acting correctly under partial information |
| 5b. Risk weighting | Adjusting confidence and sizing for risk level |
| 5c. HOLD condition detection | Knowing when not to act (FM8, liquidity, regime) |
| 5d. Conflict resolution | Deciding between contradictory signals |

---

### 6. Attention

*Signal prioritisation, urgency detection, and filtering.*

The agent knows what to focus on and what to ignore. Not all signals
require action — attention quality determines which receive response.

| Sub-dimension | Description |
|---|---|
| 6a. Signal prioritisation | Ranking signals by relevance and urgency |
| 6b. Urgency detection | Recognising time-sensitive signals requiring immediate response |
| 6c. Noise filtering | Distinguishing meaningful signals from market noise |
| 6d. Threshold awareness | Knowing when a signal has crossed an action threshold |

---

### 7. Communication

*Output clarity, format, and confidence expression.*

The agent produces outputs that are clear, correctly formatted, and
accurately represent its confidence level.

| Sub-dimension | Description |
|---|---|
| 7a. Output clarity | Signal expressed in plain, unambiguous language |
| 7b. Format compliance | Structured output matching expected schema |
| 7c. Confidence expression | Accurately stating HIGH/MEDIUM/LOW and why |
| 7d. Audience calibration | Adjusting output depth for the agent type receiving it |

---

### 8. Verification

*Source checking, on-chain confirmation, and corroboration.*

The agent checks its facts. It does not act on unverified signals and
knows which sources are authoritative for which claim types.

| Sub-dimension | Description |
|---|---|
| 8a. Source hierarchy application | Using primary sources over aggregators |
| 8b. On-chain confirmation | Verifying supply events via chiliscan.com |
| 8c. Cross-source corroboration | Confirming signals across ≥2 independent sources |
| 8d. Black logo / inactivity check | Verifying fan token active status before use |

---

### 9. Learning

*Modifier updating, error learning, and calibration feedback.*

The agent improves from experience. Wrong predictions inform modifier
revision. Calibration records accumulate into improved accuracy.

| Sub-dimension | Description |
|---|---|
| 9a. Error classification | Identifying which modifier or framework produced a wrong signal |
| 9b. Modifier revision | Updating modifier values based on accumulated evidence |
| 9c. Calibration feedback | Feeding verified outcomes back into the reasoning framework |
| 9d. Pattern generalisation | Extracting enduring rules from specific outcomes |

---

### 10. Integration

*Cross-layer signal combination and multi-tool coordination.*

The agent combines signals from multiple library layers without
conflation and coordinates across tools where multi-agent workflows apply.

| Sub-dimension | Description |
|---|---|
| 10a. Cross-layer combination | Combining sport, athlete, fan-token, macro signals |
| 10b. Signal chain management | Maintaining correct loading order across layers |
| 10c. Tool coordination | Coordinating MCP tools in correct sequence |
| 10d. Conflict detection | Identifying when cross-layer signals contradict |

---

### 11. Calibration

*Accuracy tracking, verified outcomes, and modifier validation.*

The agent maintains a verifiable record of its predictions and outcomes.
Calibration is the measure of real-world accuracy.

| Sub-dimension | Description |
|---|---|
| 11a. Direction accuracy | Tracking HOME/AWAY/DRAW direction correctness |
| 11b. Modifier magnitude validation | Confirming modifier size reflects actual outcome distribution |
| 11c. Confidence tier validation | Checking whether HIGH/MEDIUM/LOW confidence tiers are calibrated |
| 11d. Supply event verification | Confirming PTG/FTP supply events occurred as predicted |

---

### 12. Adaptation

*Regime detection, real-time updating, and context switching.*

The agent responds to changing conditions. When the macro regime shifts,
when a supply event fires, when new information arrives — the agent updates.

| Sub-dimension | Description |
|---|---|
| 12a. Regime detection | Identifying CHZ regime state (CAPITULATION / RECOVERY) |
| 12b. Real-time updating | Incorporating new information within a reasoning session |
| 12c. Context switching | Moving between fixture types, token types, or competition stages |
| 12d. Modifier decay awareness | Knowing when a modifier's effect diminishes over time |

---

### 13. Ethics

*Transparency about limits, no fabrication, and user wallet safety.*

The agent does not fabricate data, does not overstate confidence, and
never takes actions that put user funds at risk without explicit consent.

| Sub-dimension | Description |
|---|---|
| 13a. Fabrication prevention | Never inventing data, prices, or outcomes |
| 13b. Limit transparency | Clearly stating when the agent lacks sufficient information |
| 13c. Wallet safety | Not executing wallet actions beyond defined guardrails |
| 13d. Conflict of interest avoidance | Not biasing signals toward any token, club, or outcome |

---

### 14. Transparency

*Reasoning chain visibility, modifier disclosure, and confidence clarity.*

The agent shows its working. It discloses which modifiers were applied,
why, and what confidence level results.

| Sub-dimension | Description |
|---|---|
| 14a. Reasoning chain disclosure | Showing the signal → modifier → output chain |
| 14b. Modifier disclosure | Naming modifiers applied and their values |
| 14c. Confidence justification | Explaining why a signal is HIGH/MEDIUM/LOW |
| 14d. Uncertainty flagging | Explicitly noting where information is incomplete |

---

### 15. Execution *(added v4.1.33)*

*Translating signals into concrete, disciplined action.*

The agent acts on its signals in a structured, disciplined way. A correct
signal is only valuable if it produces a correctly executed action. This
dimension covers the gap between knowing and doing.

| Sub-dimension | Description |
|---|---|
| 15a. Entry discipline | Acting at the right moment — not early, not late |
| 15b. Exit discipline | Closing positions or ending actions per defined rules |
| 15c. Sizing logic | Calibrating action magnitude to signal confidence and risk |
| 15d. Playbook adherence | Following defined playbooks rather than improvising |

---

### 16. Collaboration *(added v4.1.33)*

*How agents work with other agents and systems.*

SportMind serves multi-agent architectures (agent type 6). This dimension
covers how agents delegate, hand off context, coordinate outputs, and
resolve conflicts when multiple agents produce competing conclusions.

| Sub-dimension | Description |
|---|---|
| 16a. Task delegation | Assigning sub-tasks to specialist agents correctly |
| 16b. Context handoff | Passing sufficient context for downstream agents to act |
| 16c. Output coordination | Aligning outputs across agents to a consistent signal |
| 16d. Conflict arbitration | Resolving contradictions when specialist agents disagree |

---

## Mapping Conventions

### Format

Every library file must include a `## MIND DIMENSIONS` section before
the compatibility list. Sections must map to all 16 dimensions.

```markdown
## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Domain knowledge for fan token supply mechanics |
| Reasoning (2) | ACTIVE | Causal and probabilistic signal weighting |
| Context (3) | ACTIVE | Tournament stage and macro regime context |
| Memory (4) | NOT APPLICABLE | — |
| Judgment (5) | ACTIVE | HOLD condition detection, conflict resolution |
| Attention (6) | NOT APPLICABLE | — |
| Communication (7) | NOT APPLICABLE | — |
| Verification (8) | ACTIVE | On-chain supply event confirmation |
| Learning (9) | NOT APPLICABLE | — |
| Integration (10) | ACTIVE | Cross-layer signal combination |
| Calibration (11) | ACTIVE | Direction accuracy and supply event verification |
| Adaptation (12) | EMERGING | Regime detection applied |
| Ethics (13) | NOT APPLICABLE | — |
| Transparency (14) | ACTIVE | Modifier disclosure |
| Execution (15) | NOT APPLICABLE | — |
| Collaboration (16) | NOT APPLICABLE | — |
```

### Status Values

| Value | Meaning |
|---|---|
| ACTIVE | This dimension is actively strengthened by the file |
| NOT APPLICABLE | This dimension is not relevant to this file's purpose |
| EMERGING | The file begins to address this dimension but does not fully implement it |

### Sub-dimension Citation

When flagging a gap at the sub-dimension level, cite the sub-dimension
explicitly in the gap note. Example: `Calibration (11) · 11b modifier
magnitude validation — not yet validated for this modifier.`

### Retroactive Mapping

Files added before v4.1.33 map to 14 dimensions only. Dimensions 15
(Execution) and 16 (Collaboration) were not yet defined. A retroactive
mapping pass is planned but not yet scheduled. Until complete, pre-v4.1.33
files may show `EXECUTION: [NOT MAPPED — pre-v4.1.33]` or omit the row.

---

## Known Dimension Gaps (as of v4.1.33)

| Gap | File | Status | Priority |
|---|---|---|---|
| Temporal reasoning framework | core/temporal-reasoning-framework.md | NOT YET CREATED | Tier 1 |
| Contradiction resolution framework | core/contradiction-resolution-framework.md | NOT YET CREATED | Tier 1 |
| Execution playbook reference | core/execution-playbook.md | NOT YET CREATED | Tier 2 |
| Collaboration protocol reference | core/collaboration-protocol.md | NOT YET CREATED | Tier 2 |

**Tier 1 gaps** affect agent reasoning quality in every briefing cycle.
**Tier 2 gaps** affect specific agent types (execution gaps → utility agents;
collaboration gaps → multi-agent systems).

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Defines what each dimension enables |
| Reasoning (2) | ACTIVE | Sub-dimension 2d temporal reasoning flagged as Tier 1 gap |
| Context (3) | ACTIVE | Mapping conventions and status values |
| Memory (4) | NOT APPLICABLE | — |
| Judgment (5) | ACTIVE | Status value guidance for uncertain mappings |
| Attention (6) | NOT APPLICABLE | — |
| Communication (7) | ACTIVE | Format specification for MIND DIMENSIONS sections |
| Verification (8) | NOT APPLICABLE | — |
| Learning (9) | ACTIVE | Gap table drives calibration feedback loop |
| Integration (10) | ACTIVE | Cross-dimension and cross-file mapping guidance |
| Calibration (11) | NOT APPLICABLE | — |
| Adaptation (12) | EMERGING | Framework evolves as dimensions are added |
| Ethics (13) | NOT APPLICABLE | — |
| Transparency (14) | ACTIVE | Retroactive mapping note; gap table fully disclosed |
| Execution (15) | NOT APPLICABLE | — |
| Collaboration (16) | NOT APPLICABLE | — |

---

## COMPATIBILITY

- All library files — every file maps to this dimension framework
- core/agent-failure-modes.md — FM5 (over-confidence) maps to Judgment (5)
- core/signal-confidence-framework.md — maps to Calibration (11), Transparency (14)
- core/pre-match-signal-framework.md — maps to Reasoning (2), Integration (10)

© 2026 SportMind
