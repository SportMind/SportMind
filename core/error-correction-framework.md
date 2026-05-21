---
name: error-correction-framework
description: >
  How SportMind agents should reason about their own errors — when a signal was
  wrong, what failed, and how to update reasoning going forward. Covers four error
  types (direction, magnitude, timing, context), the error pattern detection
  framework, calibration record as error log, and the six-step error correction
  reasoning chain. Error correction is how Intelligence becomes Learning.
---

# Error Correction Framework

**A signal that is wrong is not a failure — it is information.**
Wrong signals reveal which modifiers are overweighted, which intelligence is missing,
and which context was misread. An agent that cannot reason about its own errors
cannot improve.

---

## Error classification framework

```
TYPE 1 — DIRECTION ERROR (most serious):
  Signal said HOME. Result was AWAY.
  Requires full reasoning chain review.

  ANALYSIS STEPS:
    Step 1: Which modifier pushed the signal toward the wrong direction?
    Step 2: Was that modifier applied at full weight when it should have been discounted?
    Step 3: Was there a signal from another layer that contradicted the direction
      and was overridden? Why was it overridden?
    Step 4: Was the context correct? Right sport domain, right competition tier,
      right macro phase?

  DIRECTION ERROR MODIFIER REVIEW:
    If athlete modifier was dominant and direction was wrong:
      Apply ×0.85 confidence weight to that specific athlete modifier
      for next 3 comparable fixtures.
    If macro modifier was dominant and direction was wrong:
      Flag macro phase assessment for review.
    If venue modifier was dominant and direction was wrong:
      Flag venue intelligence for that specific venue.

TYPE 2 — MAGNITUDE ERROR:
  Direction was correct but adjusted score was significantly off (>15 points).
  Less serious than direction error. Modifier values need recalibration, not
  direction logic.

  ANALYSIS STEPS:
    Step 1: Which modifier stack created the magnitude overestimate or underestimate?
    Step 2: Was confidence level HIGH when it should have been MEDIUM?
    Step 3: Were unconfirmed variables treated as confirmed?

TYPE 3 — TIMING ERROR:
  Signal was correct at T-72h but wrong at T-2h due to late information.
  Not a reasoning failure — a signal freshness failure.
  Update temporal reasoning from core/temporal-reasoning.md.
  Ensure T-2h inputs override all earlier planning signals.
  This error type does not require modifier confidence discount.

TYPE 4 — CONTEXT ERROR:
  Right intelligence, right reasoning, wrong context.
  Examples:
    Applied FTP PATH_2 framework to a demand-only token.
    Applied bull market modifier during confirmed bear phase.
    Applied home advantage modifier to a neutral venue fixture.
    Applied UCL modifier to a domestic league match.

  Context errors indicate the agent onboarding sequence was not followed correctly.
  Return to core/agent-onboarding.md and verify loading sequence.
  Context errors do not require modifier recalibration — they require context check.
```

---

## Error pattern detection

```
PATTERN THRESHOLD:
  Three direction errors from the same modifier within 10 comparable situations:
    Flag as MODIFIER_REVIEW_REQUIRED.
    Apply ×0.75 confidence weight to that modifier until reviewed.
    Document in calibration records as a recalibration candidate.

  Five direction errors from the same modifier:
    Apply MODIFIER_SUSPENSION.
    Do not apply that modifier until explicit recalibration is completed.
    Human review required before reinstatement.

COMPARABLE SITUATION DEFINITION:
  Same sport domain, same competition tier, same macro phase.
  A Premier League modifier error in a La Liga context does not count
  as a comparable situation — pool characteristics differ.

PATTERN RESET:
  After human review and explicit recalibration approval:
  Reset confidence weight to Tier 1 (×0.80) — early evidence.
  The modifier must rebuild its confidence tier through new calibration records.
```

---

## Calibration record as error log

```
Every direction error is a calibration record candidate.
Wrong predictions are as valuable as correct ones.

Error analysis belongs in the notes field of the calibration record:
  · What failed: which modifier produced the wrong direction?
  · Which layer: sport domain, athlete, macro, venue, psychological?
  · What context was missed: competition tier, macro phase, lineup status?
  · What would have changed the output: which signal was underweighted?

This is how SportMind learns. The calibration record is not just a score tracking
system — it is the primary mechanism by which modifier confidence weights improve.

Reference: core/calibration-feedback-loop.md for how records update confidence tiers.
```

---

## REASONING CHAIN — ERROR CORRECTION

```
STEP 1 — Classify the error type:
  Direction / Magnitude / Timing / Context.
  This determines which response applies.

STEP 2 — Identify the dominant modifier:
  Which modifier produced the most weight toward the wrong output?
  Review the modifier stack from the original analysis.

STEP 3 — Review the reasoning chain:
  Load core/agent-reasoning-chains.md.
  Walk through the chain step by step.
  At which step did the output diverge from the correct direction?

STEP 4 — Apply confidence discount:
  Direction error, athlete modifier dominant: ×0.85 for next 3 comparable.
  Direction error, pattern detected (3/10): ×0.75 until reviewed.
  Direction error, severe pattern (5+): MODIFIER_SUSPENSION.
  Magnitude error: no discount — review modifier value, not confidence.
  Timing error: no discount — improve signal freshness process.
  Context error: no discount — improve context verification process.

STEP 5 — Submit calibration record:
  Include error analysis in notes field.
  Document which modifier failed and why.

STEP 6 — Pattern check:
  Has this modifier produced errors before?
  If pattern threshold met: flag for human review.
  Update core/smi-digest.md with MODIFIER_REVIEW_REQUIRED item.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches agents what types of errors exist and what each error type reveals about the modifier or context that failed — four distinct error types with distinct responses.

**Reasoning:** Provides the six-step error correction reasoning chain connecting error classification through modifier confidence discount to calibration record submission.

**Context:** Applies whenever a SportMind signal produces a confirmed wrong direction, significant magnitude deviation, timing failure, or context mismatch.

**Memory:** Draws on calibration records as the primary error log — past wrong signals are stored memory that informs current confidence weights and pattern detection.

**Judgment:** This file IS a Judgment framework — knowing what went wrong and why, and knowing when to suspend a modifier entirely, is the core Judgment function in SportMind.

**Attention:** Confirmed direction errors demand immediate attention — a confirmed error should redirect agent attention to the failing modifier before the next comparable fixture, not after.

**Learning:** The primary Learning file in SportMind — error classification directly triggers modifier confidence discount and pattern detection that updates future reasoning.

**Integration:** Error correction integrates across all layers simultaneously — a context error requires checking all active modifiers, not just the dominant one.

---

## Compatibility

**Calibration feedback:**    `core/calibration-feedback-loop.md`
**Reasoning chains:**        `core/agent-reasoning-chains.md`
**Temporal reasoning:**      `core/temporal-reasoning.md`
**Signal confidence:**       `core/signal-confidence-framework.md`
**Agent onboarding:**        `core/agent-onboarding.md`
**SMI digest:**              `core/smi-digest.md`

---

*SportMind v3.97.73 · MIT License · sportmind.dev*
*Error correction is how Intelligence becomes Learning. Wrong signals are not failures — they are information.*
