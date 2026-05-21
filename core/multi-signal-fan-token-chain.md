---
name: multi-signal-fan-token-chain
description: >
  How to reason when multiple fan token signals fire simultaneously. The Integration
  dimension of the eight-dimension Mind architecture. Covers five signal interaction
  rules, the compound modifier calculation framework, the standard UCL Final $AFC
  multi-signal template, and probability-weighted expected output calculation.
  Signals do not process sequentially in reality — they interact.
---

# Multi-Signal Fan Token Chain

**Signals do not process sequentially in reality — they interact.**
This file is the Integration framework: how to hold multiple simultaneous signals
and produce a coherent unified output rather than processing them one at a time.

---

## The integration problem

```
Analysing $AFC before the UCL Final requires simultaneously reasoning about:
  · Match outcome probability (sport domain layer)
  · FTP PATH_2 pre-liquidation pool estimate (fan token layer)
  · Macro sentiment regime suppressor (macro layer)
  · Governance vote timing (fan token governance layer)
  · Key athlete absence signal (athlete layer)
  · Seasonal peak demand amplifier (seasonal intelligence)
  · Tournament demand multiplier ×2.0 (tournament intelligence)
  · Community psychological momentum (psychological intelligence)
  · Press conference signals from T-24h (breaking news layer)
  · On-chain pre-liquidation monitoring (blockchain intelligence)

These do not process sequentially in reality — they interact.
Some compound positively. Some offset each other. Some are independent.
```

---

## Signal interaction rules

```
RULE 1 — SUPPLY MECHANICS ARE INDEPENDENT:
  FTP PATH_2 supply events fire based on match result only.
  Macro sentiment, governance votes, and community psychology do not affect
  whether the burn fires — only the match outcome does.
  They affect the demand response to the supply event.
  Agent rule: report supply event and demand response separately. Never merge them.

RULE 2 — MACRO APPLIES TO DEMAND, NOT SUPPLY:
  HOPE_FEAR ×0.88 suppresses the demand premium from a WIN.
  It does not suppress the burn itself.
  Correct output: "burn fires, but demand response is ×0.88 of expected premium."
  Incorrect output: "burn may be reduced due to market conditions."

RULE 3 — GOVERNANCE VOTE COMPOUNDS WITH RESULT:
  Governance vote active on match day:
    Pre-result community engagement: ×1.05
  WIN + active governance vote on same day:
    ×1.05 (governance) × ×1.08 (WIN) = ×1.134 combined demand.
  LOSS + active governance vote on same day:
    ×0.92 (LOSS) × ×1.03 (governance participation) = ×0.948 combined.

RULE 4 — TOURNAMENT MULTIPLIER COMPOUNDS WITH RESULT:
  UCL Final × WIN:  ×2.0 × ×1.20 = ×2.40 combined demand.
  UCL Final × LOSS: ×2.0 × ×0.80 = ×1.60 combined demand.
  Note: the tournament multiplier compounds the result signal —
  it does not replace it. Both are active simultaneously.

RULE 5 — ATHLETE ABSENCE AFFECTS SUPPLY EVENT PROBABILITY:
  Athlete absence reduces WIN probability → reduces expected burn magnitude.
  Example: key player absent reduces WIN probability from 65% to 55%.
  Expected burn = pool × 0.55 (not pool × 0.65).
  The absence changes what we expect from the supply event, not whether it fires.
```

---

## Standard UCL Final $AFC multi-signal template

```
INTEGRATE THESE SIMULTANEOUSLY:

  1. Match adjusted score:        [calculate from sport domain layer]
  2. FTP PATH_2 pool estimate:    circulating supply ÷ 400
  3. Macro regime modifier:       [current regime — e.g. HOPE_FEAR = ×0.88]
  4. Tournament multiplier:       ×2.0 (UCL Final)
  5. Active athlete modifiers:    [list each with confidence tier]
  6. Governance vote active:      [YES → apply ×1.05 pre-result | NO → skip]
  7. Seasonal demand:             [check seasonal-intelligence.md — May = ×1.15]
  8. Psychological momentum:      [from psychological-intelligence.md]

WIN SCENARIO OUTPUT:
  Supply event:   burn [estimated magnitude from pool ÷ 400]
  Demand (net):   ×2.0 (tournament) × ×1.20 (WIN) × ×0.88 (HOPE_FEAR)
                = ×2.112 sustained 2-4 weeks
  With seasonal: ×2.112 × ×1.15 = ×2.429

LOSS SCENARIO OUTPUT:
  Supply event:   none (no burn on LOSS)
  Demand (net):   ×2.0 (tournament) × ×0.80 (LOSS) × ×0.88 (HOPE_FEAR)
                = ×1.408 sustained 24-48h

DRAW SCENARIO OUTPUT:
  Supply event:   none
  Demand (net):   ×2.0 (tournament) × ×1.00 (DRAW) × ×0.88 = ×1.76

PROBABILITY-WEIGHTED EXPECTED OUTPUT:
  Demand expected = (WIN% × ×2.112) + (DRAW% × ×1.76) + (LOSS% × ×1.408)

  Supply expected (net):
  = (WIN% × burn_estimate) + (LOSS% × mint_estimate × -1)
  = net expected supply change — positive = deflationary, negative = inflationary
```

---

## Stacking caps and conflict rules

```
POSITIVE STACKING CAP: ×1.25 maximum compound positive modifier.
  No matter how many positive signals fire simultaneously, the compound
  positive demand modifier cannot exceed ×1.25 above the tournament base.
  This prevents unrealistic compounding from low-confidence signals.

  Exception: Tournament multipliers (×2.0, ×1.80) are applied before the cap.
  The cap applies to the signals stacked on top of the tournament base.

NEGATIVE STACKING FLOOR: ×0.75 minimum compound negative modifier.
  Prevents catastrophic compounding of uncertainty discounts.

CONFLICTING SIGNALS:
  When a macro negative (e.g. HOPE_FEAR ×0.88) fires simultaneously with
  a strong positive (UCL Final ×2.0):
  Apply both independently — do not cancel either.
  Both signals are real. The output reflects both.
  Correct: ×2.0 × ×0.88 = ×1.76 (tournament positive + macro headwind)
  Incorrect: "signals conflict — apply neutral modifier."

INDEPENDENT SIGNALS:
  Supply mechanics (burn/mint) are always independent.
  Report them separately regardless of what demand signals are doing.
  Never merge supply and demand into a single number.
```

---

## HOLD condition for multi-signal scenarios

```
Apply HOLD if five or more signals are simultaneously uncertain
(each at Tier 0 or Tier 1 confidence from calibration-feedback-loop.md).

Rationale: compound uncertainty compounds itself.
Five uncertain signals do not produce one partially confident output —
they produce near-maximum uncertainty.

When HOLD applies in multi-signal context:
  Report: "too many unresolved uncertain signals for reliable compound output."
  Identify: which signals need resolution before analysis can proceed.
  Set: resolution triggers for each uncertain signal.
  Revisit: when at least three signals reach Tier 2 or higher confidence.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches the five interaction rules governing how simultaneous fan token signals compound, offset, or remain independent — the rules that make multi-signal analysis correct rather than additive guessing.

**Reasoning:** Provides compound signal calculation rules and the UCL Final $AFC multi-signal template as a complete end-to-end reasoning framework for the most complex SportMind scenarios.

**Context:** Applies to any analysis where three or more fan token signals are active simultaneously — most critical for major events involving FTP PATH_2 tokens.

**Memory:** Draws on calibration records of past multi-signal events to validate compound modifier values — particularly tournament and supply event combinations.

**Judgment:** Apply HOLD when five or more signals are simultaneously uncertain — compound uncertainty compounds itself and the honest output is insufficient data for reliable analysis.

**Attention:** This is the highest Attention-demand file in SportMind — multi-signal scenarios require the agent to hold all signals simultaneously rather than processing sequentially.

**Learning:** Each confirmed multi-signal outcome validates or invalidates the compound modifier calculation rules. UCL Final $AFC outcomes are the most significant multi-signal calibration records SportMind will produce.

**Integration:** This file IS the Integration framework — it explicitly addresses how to hold multiple signals simultaneously and produce a coherent unified output across supply mechanics, demand signals, macro conditions, and match probability simultaneously.

---

## Compatibility

**FTP PATH_2 mechanics:**    `fan-token/ftp-path2.md`
**Signal interaction:**      `core/signal-interaction-reasoning.md`
**Scenario intelligence:**   `core/scenario-intelligence.md`
**Calibration feedback:**    `core/calibration-feedback-loop.md`
**Error correction:**        `core/error-correction-framework.md`
**Arsenal intelligence:**    `fan-token/arsenal.md`

---

*SportMind v3.97.73 · MIT License · sportmind.dev*
*Supply mechanics are always independent. Demand signals compound. Report both separately.*
*HOLD when five or more signals are simultaneously uncertain.*
