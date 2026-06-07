---
name: pre-match-signal-framework
description: >
  Pre-match signal assembly framework. The end-to-end orchestrating file for
  building a SportMind pre-match signal. Covers what a pre-match signal is,
  the seven-step assembly chain from match parameter confirmation through
  structured output, the output schema with full field definitions, and
  reference files for each step. Load this file when assembling a pre-match signal.
  All 14 Mind dimensions mapped.
---

# Pre-Match Signal Framework

**The orchestrating file for pre-match signal assembly.**
**Output:** structured direction signal with adjusted score, modifiers, and flags.

---

## What a pre-match signal is

```
A SPORTMIND PRE-MATCH SIGNAL IS:
  A probability-weighted directional assessment (HOME/AWAY/DRAW) produced
  before a sporting event by loading all five intelligence layers and applying
  the SportMind modifier stack.

  It outputs:
    · A direction (HOME | AWAY | DRAW)
    · An adjusted score (0–100, where 50 = equal probability)
    · An SMS (SportMind Score — how many layers were loaded, 0–100)
    · A confidence level (LOW | MEDIUM | MEDIUM-HIGH | HIGH)
    · A recommended action (ENTER | HOLD | PASS)
    · A composite modifier (the product of all applied modifiers)
    · A flags object (unconfirmed elements that reduce confidence)

A SPORTMIND PRE-MATCH SIGNAL IS NOT:
  A bet recommendation. A financial instrument. A guarantee.
  An output that requires fewer than five loaded layers to produce.
  A signal that can be produced from current data alone without the framework.
```

---

## Seven-step pre-match signal assembly chain

```
STEP 1: CONFIRM MATCH PARAMETERS
  Required: sport, competition name, tier (UCL/domestic/cup), date, kickoff time.
  Required: venue type — HOME | AWAY | NEUTRAL.

  NEUTRAL VENUE RULE:
    If venue is neutral (neither club's home ground):
      home_advantage_modifier = 0 (not ×1.00 — it is zero, not standard)
      Flag: neutral_venue = true in output.
    Reference: UCL Final examples in calibration/2026/.

  OCCASION WEIGHT (apply immediately):
    UCL Final:           ×2.00 demand amplifier
    UCL semi/quarter:    ×1.60
    UCL group:           ×1.40
    Domestic cup final:  ×1.60
    Derby match:         ×1.35
    Standard domestic:   ×1.00
    Apply occasion weight to fan token demand context (not to adjusted score directly).

STEP 2: LOAD ALL FIVE LAYERS — CONFIRM SMS = 100
  Load in order:
    1. core/smi-digest.md + core/agent-onboarding.md (core context)
    2. macro/macro-overview.md (macro layer)
    3. fan-token/ftp-path2.md (fan token layer, if applicable)
       Note: PATH_2 settlement is based on the 90-MINUTE RESULT ONLY.
       Extra time and penalties are NOT included — even in cup finals.
       A knockout match level at 90 minutes = DRAW = no supply event.
    4. sports/{sport}/sport-domain-{sport}.md (sport domain)
    5. athlete/athlete-intelligence-framework.md +
       athlete/{sport}/athlete-intel-{sport}.md (athlete layer)

  CALCULATE SMS:
    SMS = (layers_loaded / 5) × 100
    SMS 100 = all five layers. Required for a full SportMind signal.

  IF SMS < 100:
    Identify the missing layer(s) by name.
    Flag in output: layers_missing = [list of missing files].
    Reduce confidence tier: every missing layer = one tier reduction.
    If SMS < 60: do not produce a directional signal — output INCOMPLETE.

  MACRO GATE (check immediately after loading macro):
    If MACRO_OVERRIDE_ACTIVE = true →
      Apply bifurcated model (see macro/macro-overview.md).
      Category A acute event: HOLD on all positive signals. Do not proceed.
      Category B event: reduce confidence tier, note in output, continue.

STEP 3: CALCULATE BASE SCORE
  Source: sports/{sport}/sport-domain-{sport}.md signal weights.
  
  BASE SCORE INPUTS:
    · Competition tier weight (from occasion context, Step 1)
    · Historical head-to-head record (if available and relevant)
    · Home advantage modifier (×1.06–1.12 for strong home record)
      → Set to 0 if neutral venue (Step 1)
    · Relative form (league position, recent results, trajectory)
    · Tactical system stability (see coaching-intelligence.md)

  OUTPUT: base adjusted score on 0–100 scale.
  50 = equal probability. >50 = HOME advantage. <50 = AWAY advantage.

STEP 4: APPLY ATHLETE MODIFIER
  Source: athlete/athlete-intelligence-framework.md → Step 5 (APS composite).

  APPLY FOR BOTH SIDES:
    HOME team APS modifier → multiplied into base score.
    AWAY team APS modifier → multiplied into base score (inverse direction).

  LINEUP GATE:
    If lineup_unconfirmed = true at time of signal →
      Set flag: lineup_unconfirmed = true.
      Reduce confidence tier by one level.
      Use probability-weighted APS (50% of expected lineup, 50% of rotation).

  APS MODIFIER RANGE: 0.55–1.25×
  Reference: athlete/athlete-intelligence-framework.md for full chain.

STEP 5: APPLY MACRO MODIFIER
  Source: macro/macro-overview.md (regime) + macro/macro-crypto-market-cycles.md.

  MACRO REGIMES:
    EXPANSION:   Standard modifiers apply. ×1.00.
    ANXIETY:     Standard modifiers apply. ×1.00.
                 (ANXIETY means caution, not reduction — no modifier adjustment)
    CONTRACTION: Apply demand reduction modifier. ×0.93 to demand signals.
                 (Does not affect adjusted score directly)
    EUPHORIA:    Apply demand amplification. ×1.07 to demand signals.

  MACRO OVERRIDE CONDITIONS:
    Category A: HOLD — do not proceed with signal. Return HOLD output.
    Category B: Note in output. Reduce confidence. Continue with caution.

  REGULATORY MODIFIER (if jurisdiction-specific):
    EU: Check MiCA compliance status (EU_LIQUIDITY_RISK ×0.94 in transition window).
    US: Digital Collectible classification confirmed — no US_SECURITIES_RISK for
        verified non-fractionalized fan tokens.
    Reference: macro/macro-regulatory-sportfi.md

STEP 6: APPLY SITUATIONAL MODIFIERS
  Apply in this order. Check for conflicts after each.

  VENUE:
    Home advantage: see Step 3. Neutral: already set to 0 in Step 1.

  WEATHER:
    Cricket dew factor (evening T20, high humidity): ×0.95 batting first team.
    Extreme wind or precipitation for outdoor sports: see core/weather-intelligence.md.
    Apply only when weather is confirmed material for this sport and conditions.

  TRAVEL AND FATIGUE:
    Intercontinental travel <72h before match: ×0.94–0.97.
    Back-to-back fixtures: ×0.92–0.96 depending on sport.
    Reference: core/travel-timezone-intelligence.md

  TACTICAL MATCHUP (TMAS):
    Apply only when a structural mismatch is confirmed (not inferred).
    Example: elite winger vs inexperienced fullback confirmed in lineup.
    Range: ×0.95–1.05. Reference: core/tactical-matchup-intelligence.md

  REFEREE (if material):
    Apply only when referee assignment is confirmed and a strong pattern exists.
    Reference: core/referee-intelligence.md

  MODIFIER CONFLICT RULE:
    If two modifiers point in the same direction for the same factor → apply once.
    If two modifiers point in opposite directions → flag conflict, apply lower magnitude.
    Never stack the same signal source twice.

STEP 7: PRODUCE STRUCTURED OUTPUT
  Compile all modifier components. Apply composite. Generate flags.

  REQUIRED OUTPUT STRUCTURE:
    {
      "direction":           "HOME" | "AWAY" | "DRAW",
      "adjusted_score":      [0-100 number],
      "sms":                 [0-100 number],
      "confidence_level":    "LOW" | "MEDIUM" | "MEDIUM-HIGH" | "HIGH",
      "recommended_action":  "ENTER" | "HOLD" | "PASS",
      "composite_modifier":  [decimal — product of all applied modifiers],

      "modifiers_applied": {
        "athlete_modifier":   [decimal],
        "macro_modifier":     [decimal],
        "venue_modifier":     [decimal],
        "weather_modifier":   [decimal or null],
        "travel_modifier":    [decimal or null],
        "tactical_modifier":  [decimal or null]
      },

      "flags": {
        "lineup_unconfirmed":    [bool],
        "macro_override_active": [bool],
        "neutral_venue":         [bool],
        "path2_active":          [bool]
      },

      "layers_loaded": [list of files loaded for this signal]
    }

  CONFIDENCE LEVEL RULES:
    HIGH:         SMS 100, lineup confirmed, no unresolved flags.
    MEDIUM-HIGH:  SMS 100, minor flags (e.g. one doubtful player).
    MEDIUM:       SMS 80-100, lineup unconfirmed, or neutral venue.
    LOW:          SMS < 80, or multiple unresolved flags.

  RECOMMENDED ACTION RULES:
    ENTER: direction clear (adjusted score ≥ 58 or ≤ 42), confidence ≥ MEDIUM.
    HOLD:  macro override active, OR confidence LOW, OR SMS < 80.
    PASS:  adjusted score 47–53 (genuinely contested), HOLD conditions not met
           but signal not strong enough for entry.

  INCOMPLETE OUTPUT:
    If any required field cannot be populated → label output INCOMPLETE.
    State which layer is missing and what data cannot be confirmed.
    An INCOMPLETE output is not a SportMind signal — do not act on it.
```

---

## Reference files by step

| Step | Primary file | Reference files |
|---|---|---|
| 1 | Match parameters (agent input) | `core/venue-intelligence.md` |
| 2 | `core/agent-onboarding.md` | `core/smi-digest.md`, `core/signal-confidence-framework.md` |
| 3 | `sports/{sport}/sport-domain-{sport}.md` | `core/core-signal-weights-by-sport.md` |
| 4 | `athlete/athlete-intelligence-framework.md` | `athlete/{sport}/athlete-intel-{sport}.md` |
| 5 | `macro/macro-overview.md` | `macro/macro-crypto-market-cycles.md`, `macro/macro-regulatory-sportfi.md` |
| 6 | `core/master-reasoning-architecture.md` | `core/weather-intelligence.md`, `core/travel-timezone-intelligence.md`, `core/tactical-matchup-intelligence.md` |
| 7 | `core/signal-confidence-framework.md` | `core/match-condition-snapshot.md` |

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | End-to-end pre-match signal assembly — the library's primary use case |
| Reasoning | ACTIVE | Seven-step chain from match parameter confirmation through structured output |
| Context | ACTIVE | Neutral venue, occasion weight, competition tier — all context-dependent at Step 1 |
| Memory | ACTIVE | Historical form, head-to-head, and calibration record patterns inform base score |
| Judgment | ACTIVE | HOLD gate at Step 2 (macro), lineup gate at Step 4, conflict rule at Step 6 |
| Attention | ACTIVE | SMS check at Step 2 and lineup gate at Step 4 are highest-priority attention points |
| Communication | ACTIVE | Output schema defines the complete communication standard for all pre-match signals |
| Verification | ACTIVE | Source tier verification required at Step 4 (athlete) and Step 6 (situational) |
| Learning | ACTIVE | Base score weights and modifier values calibrated from 130-record calibration base |
| Integration | ACTIVE | All five intelligence layers integrated in one assembly chain |
| Calibration | ACTIVE | Confidence level rules and recommended action thresholds calibrated from 96% accuracy base |
| Adaptation | ACTIVE | Framework adapts as new modifier types and sport domains are added |
| Ethics | ACTIVE | INCOMPLETE label enforced when data is missing — prevents false confidence outputs |
| Transparency | ACTIVE | Full modifier stack and layers_loaded required in every output — no hidden inputs |

---

## Compatibility

**Agent entry point:**         `core/agent-onboarding.md`
**Master architecture:**       `core/master-reasoning-architecture.md`
**Athlete layer:**             `athlete/athlete-intelligence-framework.md`
**Signal confidence:**         `core/signal-confidence-framework.md`
**Calibration records:**       `calibration/`

---

*SportMind v4.0.0 · MIT License · sportmind.dev*
*Seven steps. All five layers. One structured output.*
*All 14 Mind dimensions mapped.*
