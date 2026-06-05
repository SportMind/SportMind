---
name: agent-onboarding
description: >
  How to load and use SportMind correctly. File loading order, layer combination,
  signal production, and output formatting. The SportMind user manual for AI agents
  and developers. Load this file first in any SportMind session.
---

# Agent Onboarding — SportMind User Manual

**How to load and use SportMind correctly.**
This is the entry point for any agent or developer using the library.

> Load this file first. Then follow the loading order below.

---

## What SportMind is

```
SPORTMIND IS A REASONING LIBRARY — NOT A DATA FEED.

  SportMind teaches agents HOW TO THINK about sports.
  Not what is true right now.
  
  The agent's role:
    Load SportMind files as context → fetch live data from primary sources →
    apply SportMind reasoning frameworks to that live data → produce signal output
    
  SportMind does NOT replace live data sources.
  SportMind makes live data meaningful.
  
  What SportMind provides:
    Reasoning frameworks for interpreting sports events
    Modifier weights calibrated against 129 real match records
    Signal architecture (layers, chains, confidence framework)
    Fan token mechanics (FTP PATH_2, lifecycle, demand signals)
    
  What SportMind does NOT provide:
    Live scores or match results
    Current player injury status
    Today's token prices or market data
    Live league standings or current form snapshots
    
  The agent fetches live data independently.
  SportMind provides the reasoning to interpret it.
```

---

## Loading order — always follow this

```
MANDATORY LOAD ORDER FOR ANY SPORTMIND SESSION:

  STEP 1 — CORE CONTEXT (always first):
    core/smi-digest.md
    Purpose: current library state, known gaps, active modifier flags, version.
    Why first: smi-digest provides the reference point for everything that follows.
    
  STEP 2 — MACRO LAYER (always second):
    macro/macro-regulatory-sportfi.md
    macro/macro-crypto-market-cycles.md
    macro/tournament-macro.md (only if a major tournament is currently live)
    Purpose: macro context frames everything. If macro_override_active = true,
      stop here and return HOLD for all signals.
    
  STEP 3 — FAN TOKEN LAYER (load if any fan token signal is required):
    fan-token/ftp-path2.md (always — confirms PATH_2 status for all tokens)
    fan-token/fan-token-lifecycle/fan-token-lifecycle.md (for lifecycle context)
    fan-token/[specific-token-intelligence].md (if token-specific analysis needed)
    
  STEP 4 — SPORT DOMAIN:
    sports/[relevant-sport]/sport-domain-[sport].md
    Purpose: event playbook, signal weights, risk variables.
    Load the most specific file available (e.g., sport-domain-football-ucl.md
      rather than sport-domain-football.md for UCL matches if it exists).
    
  STEP 5 — ATHLETE INTELLIGENCE:
    athlete/football/[club].md (club-specific file if it exists)
    athlete/football/tier-a-clubs-framework.md (universal modifiers for Tier A clubs)
    Load only for the clubs or athletes involved in this specific scenario.
    
  STEP 6 — SITUATIONAL MODIFIERS (load only what is relevant):
    core/venue-intelligence.md (for any home/away/neutral venue reasoning)
    core/weather-intelligence.md + core/core-weather-match-day.md
      (if weather is material for this sport and match)
    core/referee-intelligence.md (if referee appointment is confirmed)
    core/psychological-intelligence.md (if rivalry or pressure pattern relevant)
    core/coaching-intelligence.md (if manager change or new manager pattern relevant)
    
  STEP 7 — REASONING CHAIN:
    core/agent-reasoning-chains.md
    Select the appropriate chain for this scenario type.
    Follow the chain steps exactly.
    
  STEP 8 — PRODUCE STRUCTURED OUTPUT (always last):
    core/signal-confidence-framework.md
    core/pre-match-signal-framework.md
    Assess confidence level based on confirmed vs unconfirmed variables.
    Apply override conditions if any are triggered.

    Required output fields (all fields mandatory — never omit):
      direction:           HOME | AWAY | DRAW
      adjusted_score:      0–100 (number)
      sms:                 0–100 (layers loaded count)
      confidence_level:    LOW | MEDIUM | MEDIUM-HIGH | HIGH
      recommended_action:  ENTER | HOLD | PASS
      composite_modifier:  [decimal — product of all modifiers applied]
      modifiers_applied:   {key: decimal for each modifier}
      flags: {
        lineup_unconfirmed:    [bool],
        macro_override_active: [bool],
        neutral_venue:         [bool],
        path2_active:          [bool]
      }
      layers_loaded:       [list of files loaded — mandatory for verification]

    If any required field cannot be populated → flag as INCOMPLETE and state
    which data is missing. An INCOMPLETE output is not a SportMind signal.
    
  MINIMUM LAYERS REQUIRED FOR ANY ACTIONABLE SIGNAL:
    Layers 1-5 (Steps 1-5) are required minimum.
    An output produced from fewer than five layers is not a SportMind signal.
    Label any partial-layer output as INCOMPLETE.
```

---

## Layer weighting principles

```
LAYER PRIORITY WHEN LAYERS CONFLICT:

  See: core/signal-confidence-framework.md for full conflict resolution hierarchy.
  Summary:
  
  1. Macro override (highest) — HOLD if active
  2. FTP PATH_2 mechanics ($AFC) — adds supply dimension
  3. Confirmed athlete absences — apply before direction assessment
  4. Sport domain base signal — primary source of adjusted score
  5. Venue and weather — final modifier stack
  6. Psychological and historical — minimum 5 comparable situations required
  
  Never reverse this order. A persuasive sport domain signal does not override
  an active macro flag. A psychological pattern does not override a confirmed
  athlete absence.
```

---

## Common mistakes to avoid

```
ERRORS THAT INVALIDATE A SPORTMIND SIGNAL:

  ✗ Applying historical pattern modifiers without minimum five
    comparable situations. Fewer than five = variance, not pattern.
    
  ✗ Treating FTP PATH_2 magnitude estimates as guaranteed figures.
    They are probability-weighted estimates. Label as estimates.
    Range: 1.40× to 2.0× multiplier. Central estimate: 1.50×.
    
  ✗ Overriding a HOLD signal based on single-layer confidence.
    HOLD means insufficient overall confidence — not a direction signal.
    One strong layer cannot override a system-level HOLD.
    
  ✗ Loading only Steps 1-2 and producing a signal.
    Minimum Steps 1-5 required. Fewer = INCOMPLETE — label it clearly.
    
  ✗ Treating expiring data as SportMind intelligence.
    Current injury status, today's prices, current standings are fetched
    by the agent from primary sources. They are inputs to the framework.
    They are not outputs of the framework.
    
  ✗ Adding modifiers instead of multiplying.
    All SportMind modifiers compound by multiplication: never addition.
    ×0.93 × ×0.97 = ×0.9021. Not ×0.93 + ×0.97 = ×0.90.
    
  ✗ Applying a modifier without confirming source.
    Each modifier requires a confirmed source (official announcement, Tier 1 source).
    Rumoured information: flag as unconfirmed; do not apply modifier.
```

---

## Output format

```
REQUIRED OUTPUT STRUCTURE — EVERY SPORTMIND SIGNAL:

  {
    "direction":           "HOME" | "AWAY" | "DRAW",
    "adjusted_score":      [0-100 number],
    "sms":                 [0-100 number],
    "recommended_action":  "ENTER" | "EXIT" | "HOLD" | "MONITOR",
    "composite_modifier":  [decimal],
    "modifiers_applied": {
      [key]: [decimal value for each modifier applied]
    },
    "flags": {
      "lineup_unconfirmed":    [bool],
      "macro_override_active": [bool],
      "ftp_path2_active":      [bool],
      "supply_event_type":     "REDUCTION" | "MINT" | "NONE" | null,
      "weather_override_active":[bool],
      "hold_recommended":      [bool]
    },
    "confidence_level":    "HIGH" | "MEDIUM" | "LOW",
    "signal_class":        "EXECUTION" | "PLANNING" | "MONITOR",
    "layers_loaded":       [list of file names loaded for this signal]
  }
  
  layers_loaded is mandatory — it allows verification that minimum layers were used.
  
  NAMING CONVENTION:
    Flags are snake_case booleans.
    Numeric fields are unquoted numbers.
    Direction is UPPERCASE string.
    All fields present even if null — never omit a field.
```

---

## Compatibility

**The other three anchor files (always load with this file):**
  `core/agent-reasoning-chains.md`
  `core/signal-confidence-framework.md`
  `core/fan-token-context-bridge.md`

**Library entry point:** `core/smi-digest.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Onboarding sequence for loading SportMind intelligence into a new agent |
| Reasoning | ACTIVE | Reasoning initialisation — establishing the five-layer context stack |
| Context | ACTIVE | Context loading order: macro → market → sport → athlete → fan token |
| Memory | EMERGING | Initial memory state establishment for a new agent session |
| Judgment | ACTIVE | First-run judgment calibration and confidence baseline setting |
| Attention | ACTIVE | Attention priming — which signals to prioritise on first use |
| Communication | ACTIVE | Output format initialisation and structured signal template |
| Verification | ACTIVE | Onboarding verification checklist — confirming layers loaded correctly |
| Learning | NOT APPLICABLE | Onboarding is initialisation, not a learning process |
| Integration | ACTIVE | Layer integration confirmation during onboarding |
| Calibration | ACTIVE | Calibration record orientation — what the accuracy baseline means |
| Adaptation | NOT APPLICABLE | Onboarding is a fixed process, not adaptive |
| Ethics | ACTIVE | Agent scope and boundary orientation during onboarding |
| Transparency | ACTIVE | Transparency about what SportMind can and cannot do — set at onboarding |


---

*SportMind v3.97.38 · MIT License · sportmind.dev*
*Load this file first. Follow the loading order. Do not skip layers.*
