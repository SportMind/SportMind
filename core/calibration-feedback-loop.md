---
name: calibration-feedback-loop
description: >
  How calibration records should systematically update modifier confidence weights
  over time. The Learning dimension of the eight-dimension Mind architecture.
  Covers confidence tier framework (Tier 0-5), accuracy adjustment rules,
  recalibration triggers, and the six-step calibration reasoning chain. Closes
  the gap between having calibration records and using them systematically.
---

# Calibration Feedback Loop

**SportMind currently has 129 calibration records. This file makes them count.**
A modifier tested 20 times and correct 19 times should carry higher confidence
than one tested twice. This is the framework that enforces that principle.

---

## The learning gap

```
Current state: 129 calibration records exist.
Missing: a systematic framework for how those records update modifier weights.

Without this framework: all modifiers carry equal confidence regardless of
  how many times they have been tested or how often they have been correct.
With this framework: confidence is earned through empirical validation —
  tested modifiers carry more weight than theoretical ones.
```

---

## Confidence tier framework

```
TIER 0 — THEORETICAL (0 tests):
  Modifier derived from domain expertise and first principles.
  No empirical validation yet.
  Confidence weight: ×0.70
  Flag: THEORETICAL — communicate explicitly to output consumers.
  Agent rule: always state "this modifier is untested" in output.

TIER 1 — EARLY EVIDENCE (1-4 tests):
  Small sample. Direction may be correct but magnitude uncertain.
  Confidence weight: ×0.80
  Flag: EARLY_EVIDENCE
  Agent rule: apply modifier but note limited validation.

TIER 2 — EMERGING (5-9 tests):
  Sufficient for directional confidence. Magnitude still uncertain.
  Confidence weight: ×0.90
  Flag: EMERGING
  Agent rule: full application, note emerging status.

TIER 3 — ESTABLISHED (10-19 tests):
  Full confidence weight applies. Directional and magnitude reliable.
  Confidence weight: ×1.00
  No flag required — this is the standard operating confidence weight.

TIER 4 — VERIFIED (20-49 tests):
  Enhanced confidence from extended empirical record.
  Confidence weight: ×1.05
  Flag: VERIFIED_MODIFIER

TIER 5 — BENCHMARK (50+ tests):
  Rarely questioned. SportMind's most reliable signals.
  Confidence weight: ×1.10
  Flag: BENCHMARK_MODIFIER

  CURRENT SPORTMIND BENCHMARKS (as of library compilation):
    qualifying_delta (F1):    4/4 ✓ — heading toward Tier 1
    dew_factor (cricket):     5/5 ✓ — Tier 2 confirmed
    india_pakistan ×2.00:     3/3 ✓ — Tier 1 early evidence
    morning_skate (NHL):      3/3 ✓ — Tier 1 early evidence
    raider_primacy (kabaddi): 1/1 ✓ — Tier 0/1 boundary
```

---

## Accuracy adjustment

```
ACCURACY THRESHOLD RULES:
  If accuracy within a tier drops below 80%:
    Reduce confidence weight by ×0.10.
    Example: Tier 3 (×1.00) with 75% accuracy → ×0.90 effective weight.

  If accuracy drops below 70%:
    Flag MODIFIER_REVIEW_REQUIRED regardless of sample size or tier.
    Escalate to error correction framework: core/error-correction-framework.md.
    A large sample of poor accuracy is worse than a small sample of poor accuracy —
    it means the modifier is systematically wrong, not just unlucky.

ACCURACY MEASUREMENT:
  Count: direction correct / total direction predictions for this modifier.
  Only count predictions where the modifier was the dominant influence.
  Mixed-signal outcomes should be noted but not counted against single modifiers.
```

---

## Modifier recalibration triggers

```
TRIGGER 1: 3 direction errors in 10 consecutive tests for same modifier.
TRIGGER 2: Accuracy drops below 80% within current tier.
TRIGGER 3: New structural information makes modifier theoretically suspect.
  Example: a rule change in the sport invalidates the underlying logic.
TRIGGER 4: Human flags for review based on domain expertise.

WHEN TRIGGERED:
  Apply ×0.75 confidence weight (see error-correction-framework.md).
  Document as MODIFIER_REVIEW_REQUIRED in core/smi-digest.md.
  After review and approval: reset to Tier 1 (×0.80) — rebuild from evidence.
```

---

## REASONING CHAIN — CALIBRATION FEEDBACK

```
STEP 1 — Retrieve calibration history:
  Pull all calibration records where this modifier was dominant.
  Count total tests and direction-correct calls.

STEP 2 — Assign confidence tier:
  0 tests → Tier 0 (×0.70)
  1-4 → Tier 1 (×0.80)
  5-9 → Tier 2 (×0.90)
  10-19 → Tier 3 (×1.00)
  20-49 → Tier 4 (×1.05)
  50+ → Tier 5 (×1.10)

STEP 3 — Check accuracy:
  Calculate accuracy rate within sample.
  Below 80%: apply ×0.10 penalty.
  Below 70%: trigger MODIFIER_REVIEW_REQUIRED.

STEP 4 — Apply resulting confidence weight:
  Tier weight × accuracy adjustment = effective confidence weight.
  This multiplies the modifier itself — not the final output.
  Example: athlete modifier ×1.10 at Tier 2 (×0.90) = effective ×0.99.

STEP 5 — Update record after outcome:
  After confirmed result: note whether this modifier contributed to
  correct or incorrect direction. Increment the test count.
  Update accuracy rate.

STEP 6 — Check for recalibration trigger:
  If any trigger met: flag for human review.
  Document in smi-digest.md.
  Apply ×0.75 confidence weight until reviewed.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches which confidence tier applies to each modifier based on its empirical validation history — converting raw calibration record counts into actionable confidence weights.

**Reasoning:** Provides the six-step calibration reasoning chain connecting test count and accuracy rate to the effective confidence weight applied in analysis.

**Context:** Applies whenever a modifier is being used — every analysis should check the confidence tier of each active modifier before applying it.

**Memory:** This file IS the Memory framework — calibration records are SportMind's memory of what has been tested, how many times, and whether the outcomes were correct.

**Judgment:** Agents should apply Judgment when a high-tier modifier (many tests, high accuracy) contradicts a low-tier modifier (few tests) — the high-tier modifier should usually dominate, but a Tier 0 modifier with strong theoretical basis warrants explicit acknowledgment.

**Attention:** Tier 0 and Tier 1 modifiers require more agent attention and should be communicated with explicit uncertainty flags. Tier 4 and 5 modifiers can be applied with less scrutiny.

**Learning:** This file IS the Learning framework — systematic update of modifier confidence weights from confirmed outcomes is SportMind's primary mechanism for self-improvement over time.

**Integration:** Confidence tiers integrate across all simultaneously active modifiers — when stacking modifiers each carries its own confidence weight, and the compound output should reflect the weakest link in the stack.

---

## Compatibility

**Error correction:**        `core/error-correction-framework.md`
**Calibration records:**     `core/calibration-framework.md`
**SMI digest:**              `core/smi-digest.md`
**Signal confidence:**       `core/signal-confidence-framework.md`
**Modifier recalibration:**  `core/modifier-recalibration-v6.md`

---

*SportMind v3.97.73 · MIT License · sportmind.dev*
*Tier 3 (10-19 tests) is the standard operating confidence weight. Below it, flag. Above it, trust.*
