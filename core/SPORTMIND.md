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
  Gate:    If FTP PATH_2 active → supply event fires on result.
           LOSS = MINT EVENT (supply increases). Never describe as supply-neutral.

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

*SportMind v3.97.111 · MIT License · sportmind.dev*
*Load this file first. Follow the seven steps. Do not skip layers.*
