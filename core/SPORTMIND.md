---
name: SPORTMIND
description: >
  SportMind master entry point. The canonical routing file for any agent or
  developer loading the library. Contains the seven-step reasoning chain,
  the Library Rule, the proper noun test, and routes to the correct file
  for every step. Load this file first. This file is a router, not a framework.
---

# SportMind — Master Entry Point

**The open sports intelligence library for AI agents.**
**Version:** see `core/smi-digest.md`
**Calibration base:** 130 records · 96% direction accuracy

---

## Library Rule

> **Will this intelligence still be true and useful in six months?**

Apply before using any file. Apply before adding any file.
Expiring data (current standings, today's prices, current squad status) is fetched
by the agent from primary sources. It is an input to the framework — not the framework.

**Proper noun test:** If a claim requires naming a specific current person, score, or
price to be meaningful, it fails the Library Rule and should not be in this library.

---

## Seven-step reasoning chain

```
STEP 1: LOAD CORE CONTEXT
  File:    core/agent-onboarding.md
  Purpose: Calibration base, current library version, active gaps,
           mandatory load order, common mistakes to avoid.
  Always:  Load this file every session before any other file.

STEP 2: LOAD MACRO LAYER
  File:    macro/macro-overview.md
  Purpose: Establish the macro regime (EXPANSION/ANXIETY/CONTRACTION/EUPHORIA),
           regulatory jurisdiction status, and crypto cycle phase.
  Gate:    If MACRO_OVERRIDE_ACTIVE → apply bifurcated model before Step 3.
           Category A acute event = HOLD on all positive signals.

STEP 3: LOAD FAN TOKEN CONTEXT
  File:    fan-token/ftp-path2.md (always — confirms PATH_2 status)
           fan-token/fan-token-lifecycle/fan-token-lifecycle.md (lifecycle context)
           fan-token/[token-specific].md (if token-specific analysis needed)
  Conditional: only if a fan token signal is relevant to the query.
  Gate:    If FTP PATH_2 active → supply event fires on the 90-MINUTE RESULT ONLY.
           90-min LOSS = MINT EVENT (supply increases). 90-min DRAW = no event.
           Extra time and penalties are NOT included — even in cup finals.

STEP 4: LOAD SPORT DOMAIN
  File:    sports/{sport}/sport-domain-{sport}.md
  Purpose: Event playbook, signal weights, risk variables, occasion multipliers.
  Note:    Load the most specific file available — e.g. sport-domain-football-ucl.md
           for UCL matches if it exists, rather than sport-domain-football.md.

STEP 5: LOAD ATHLETE INTELLIGENCE
  File:    athlete/athlete-intelligence-framework.md (master entry point)
           athlete/{sport}/athlete-intel-{sport}.md (sport-specific modifiers)
  Purpose: Form, availability, APS composite modifier (0.55–1.25×).
  Gate:    If athlete is confirmed OUT → apply ABSENCE modifier immediately.
           If lineup_unconfirmed → flag in output, reduce confidence tier.

STEP 6: APPLY SITUATIONAL MODIFIERS
  File:    core/master-reasoning-architecture.md
  Purpose: Stack all active modifiers, check for conflicts, apply priority order.
           Venue (home/away/neutral) · Weather · Referee · Travel · Psychological.
  Rule:    Never add modifiers. Always multiply. ×0.93 × ×0.97 = ×0.9021 (not ×0.90).

STEP 7: PRODUCE STRUCTURED OUTPUT
  Format:
    direction:           HOME | AWAY | DRAW
    adjusted_score:      0-100
    sms:                 0-100 (layers loaded count)
    confidence_level:    LOW | MEDIUM | MEDIUM-HIGH | HIGH
    recommended_action:  ENTER | HOLD | PASS
    composite_modifier:  [decimal]
    modifiers_applied:   {key: decimal for each modifier}
    flags:               {lineup_unconfirmed, macro_override_active,
                          neutral_venue, path2_active}
  Rule:    All fields required. If a field cannot be populated → flag INCOMPLETE.
           layers_loaded is mandatory — allows verification minimum layers were used.
```

---

## Minimum layers required

An output from fewer than five layers (Steps 1–5) is **not a SportMind signal**.
Label any partial-layer output as `INCOMPLETE`.

| SMS range | Interpretation |
|---|---|
| 100 | All five layers loaded — full signal |
| 80 | Four layers — flag missing layer |
| 60 | Three layers — INCOMPLETE, low confidence |
| < 60 | Do not produce a directional signal |

---

## File directory

| Layer | Master file | Directory |
|---|---|---|
| Core | `core/agent-onboarding.md` | `core/` |
| Macro | `macro/macro-overview.md` | `macro/` |
| Fan token | `fan-token/ftp-path2.md` | `fan-token/` |
| Sport domain | `sports/{sport}/sport-domain-{sport}.md` | `sports/` |
| Athlete | `athlete/athlete-intelligence-framework.md` | `athlete/` |
| Market | `market/market-overview.md` | `market/` |
| Platform | `platform/platform-overview.md` | `platform/` |

---

## AGENT TYPE COMPATIBILITY

SportMind is compatible with all seven recognised agent architectures.
Match your agent type to the recommended loading pattern below.

---

### 1. Simple reflex agents
IF-THEN rules only. No internal state.

SportMind fit: LOW for full signal production. SUITABLE for compressed
skills where token budgets are tight.

Recommended loading:
- Single compressed skill file from `compressed/` directory
- Apply rules as written without modifier stacking
- Do not attempt full five-layer load — context will be lost

---

### 2. Model-based reflex agents
Maintain internal state. Act on state + current percepts.

SportMind fit: HIGH. This is the primary SMI deployment pattern.

Recommended loading:
- Load `core/SPORTMIND.md` as the internal world model
- Update state from new signals (chiliz.com/blog, regulatory sources)
- React to percepts using existing framework files as reference
- The library IS the model — keep it current

---

### 3. Goal-based agents
Act to achieve specific goals. Reason about sequences of actions.

SportMind fit: HIGH. The pre-match signal framework and fan token
wallet starter kit are both goal-based.

Recommended loading:
- Full five-layer load in order
- Follow `core/pre-match-signal-framework.md` seven-step chain
- Goal = structured signal output with all required fields populated
- Use HOLD gates to pause when goal cannot be safely achieved

---

### 4. Utility-based agents
Maximise a utility function. Handle trade-offs between competing
desirable outcomes.

SportMind fit: MEDIUM. The adjusted score and confidence tier system
is a primitive utility function. Multi-objective trade-offs are not
yet fully formalised.

Recommended loading:
- Full five-layer load
- Use `adjusted_score` as the primary utility signal (0–100)
- Weight competing signals explicitly: supply event risk vs demand
  premium, macro regime vs sport domain signal
- Design your utility function before loading — SportMind provides
  the inputs, you define the weights

---

### 5. Learning agents
Improve performance over time from experience.

SportMind fit: MEDIUM currently. HIGH with sportmind-automation Phase 3.

Recommended loading:
- Full five-layer load
- The calibration records in `calibration/` are the learning signal —
  each verified outcome strengthens or weakens modifier confidence
- Submit calibration records after every verified prediction to
  contribute to the learning loop
- Check `CALIBRATION.md` for current modifier confidence levels before
  applying weights

---

### 6. Multi-agent systems
Networks of specialist agents coordinating toward complex goals.

SportMind fit: VERY HIGH. The SportMind suite is a multi-agent system —
SMI (perception), MCP server (tool exposure), calibration agent
(verification), library builder (knowledge maintenance).

Recommended loading:
- Assign each agent a specialist role
- Each agent loads ONLY the layers relevant to its role:
  - Perception agent: `macro/` + monitoring
  - Signal agent: all five layers
  - Verification agent: `calibration/` only
  - Registry agent: `fan-token/registry/` only
- Agents communicate via structured output — use SportMind JSON schema
- No agent should load all layers unless it is the primary signal agent

---

### 7. Hierarchical agents
Agents organised in layers — high-level agents decompose goals and
delegate to specialist agents.

SportMind fit: HIGH. The six-layer SportMind architecture is inherently
hierarchical. `MACRO_OVERRIDE_ACTIVE` is a hierarchical control mechanism.

Recommended loading:
- Enforce strict top-down load order: macro → market → sport domain →
  athlete → fan token → core
- Higher layers can suppress lower layers — if `MACRO_OVERRIDE_ACTIVE`
  fires, lower layer signals are held pending macro resolution
- Design delegation boundaries before building — which layer does each
  sub-agent own?
- The seven-step chain in `core/pre-match-signal-framework.md` is a
  hierarchical decomposition of the signal production goal

---

## AGENT ARCHITECTURE SUMMARY

| Agent type | SportMind fit | Primary use case |
|---|---|---|
| Simple reflex | LOW | Compressed skills only |
| Model-based reflex | HIGH | SMI, monitoring agents |
| Goal-based | HIGH | Pre-match signal, wallet agent |
| Utility-based | MEDIUM | Entry/exit trade-off decisions |
| Learning | MEDIUM → HIGH | Calibration feedback loop |
| Multi-agent | VERY HIGH | Full SportMind suite |
| Hierarchical | HIGH | Macro override, layer delegation |

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Master routing file — entry point for all SportMind intelligence |
| Reasoning | ACTIVE | Seven-step reasoning chain defines the canonical agent reasoning path |
| Context | ACTIVE | Library Rule and proper noun test frame all context loading decisions |
| Memory | NOT APPLICABLE | Routing file — not memory-dependent |
| Judgment | ACTIVE | Library Rule is the primary judgment gate for all intelligence use |
| Attention | ACTIVE | Routing file directs agent attention to the correct file at each step |
| Communication | ACTIVE | Seven-step chain defines how SportMind communicates structured outputs |
| Verification | ACTIVE | Minimum layers requirement enforces verification before output |
| Learning | NOT APPLICABLE | Master routing file — static structure, not a learning framework |
| Integration | ACTIVE | This file is the integration entry point for all seven library layers |
| Calibration | ACTIVE | 130 records, 96% accuracy — calibration basis referenced at entry point |
| Adaptation | ACTIVE | Routing adapts as new files are added and library structure evolves |
| Ethics | ACTIVE | Library Rule enforces ethical boundary — no expiring data in framework |
| Transparency | ACTIVE | Seven-step chain and output schema are fully public and version-controlled |

---

## Compatibility

**Start here:**      `core/agent-onboarding.md`
**Reasoning map:**   `core/master-reasoning-architecture.md`
**Output schema:**   `core/pre-match-signal-framework.md`
**Library state:**   `core/smi-digest.md`

---

*SportMind v4.0.0 · MIT License · sportmind.dev*
*Load this file first. Follow the seven steps. Do not skip layers.*
