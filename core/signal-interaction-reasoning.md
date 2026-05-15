---
name: signal-interaction-reasoning
description: >
  Enduring reasoning framework for when multiple signals fire simultaneously
  in different or contradictory directions. Four-level hierarchy, negative
  asymmetry rule, stacking caps, and signal independence checks.
---

# Signal Interaction Reasoning

**How to reason when multiple signals fire simultaneously in different directions.**

---

## Signal hierarchy

```
LEVEL 1 - OVERRIDE SIGNALS (always win - all others suspended):
  Macro override active | Official integrity investigation confirmed |
  CFTC enforcement action | Emergency smart contract pause
  -> HOLD. No exceptions.

LEVEL 2 - HIGH CONFIDENCE SIGNALS (win over Level 3 and below):
  Confirmed lineup (T-6h+) | Confirmed key player absence |
  Confirmed referee appointment | Confirmed match-day weather
  Apply Level 2 in full before considering Level 3.

LEVEL 3 - STANDARD MODIFIERS (stack within caps):
  Venue | Historical pattern | Psychological momentum | Coaching intelligence
  Stack additively up to x1.20 combined positive or x0.80 combined negative.

LEVEL 4 - WEAK SIGNALS (apply at x0.50 confidence weight only):
  Unverified team news | Single-source regulatory update |
  Social sentiment without cross-platform confirmation |
  Historical pattern with fewer than 5 comparable situations
```

---

## Contradictory signal resolution

```
TWO SIGNALS OF EQUAL LEVEL CONTRADICTING:
  Calculate weighted average.
  If within +/-0.03 of baseline: NEUTRAL. Flag as SIGNAL_CONFLICT_NEUTRAL.

NEGATIVE ASYMMETRY RULE:
  Negative signal takes precedence by x1.15 asymmetry factor over equal positive.
  Losses are more impactful than equivalent gains.
```

---

## Stacking rules and caps

```
MAXIMUM POSITIVE STACK: x1.25
MAXIMUM NEGATIVE STACK: x0.75
Cap and flag as: MODIFIER_CAP_APPLIED.
```

---

## Signal independence check

```
BEFORE STACKING: are both modifiers driven by the same underlying cause?
YES -> apply only the stronger one to avoid double-counting.

COMMON SHARED-CAUSE PAIRS:
  Athlete absence + psychological momentum: share a common cause.
  Apply only the athlete modifier.

INDEPENDENCE CONFIRMED -> stack both within caps.
```

---

## Compatibility

**Confidence framework:** `core/signal-confidence-framework.md`
**Uncertainty output:** `core/uncertainty-communication.md`

---

*SportMind v3.97.52 · MIT License · sportmind.dev*
