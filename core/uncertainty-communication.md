---
name: uncertainty-communication
description: >
  Enduring framework for how SportMind agents calculate and communicate signal
  uncertainty honestly. Three uncertainty types, three quantification steps,
  output format with uncertainty level and range, and NO_SIGNAL conditions.
  Prevents false precision in SportMind outputs.
---

# Uncertainty Communication

**How to calculate and communicate signal uncertainty honestly.**
NO_SIGNAL is not a failure — it is sometimes the most honest possible output.

---

## Uncertainty sources by type

```
TYPE 1 — DATA UNCERTAINTY (HIGH contribution):
  Unconfirmed information: lineup, weather, injury status, referee.
  Resolved: T-2h for most variables.

TYPE 2 — MODEL UNCERTAINTY (MEDIUM contribution):
  Modifier values calibrated on 129 records — not infinite data.
  Reduced as calibration base grows.

TYPE 3 — EVENT UNCERTAINTY (ALWAYS PRESENT):
  Genuine randomness in sports outcomes.
  Even perfect information does not produce perfect prediction.
  Minimum irreducible uncertainty: ±4 points on adjusted score.
```

---

## Uncertainty quantification

```
STEP 1 — COUNT UNCONFIRMED TIER 1 VARIABLES:
  0 unconfirmed:    LOW uncertainty
  1-2 unconfirmed:  MEDIUM uncertainty
  3+ unconfirmed:   HIGH uncertainty

STEP 2 — CALCULATE UNCERTAINTY RANGE:
  LOW:    ±4 points on adjusted score
  MEDIUM: ±8 points
  HIGH:   ±12 points

STEP 3 — FLAG IN OUTPUT:
  "uncertainty_level":          "MEDIUM",
  "adjusted_score_range":       [64.4, 80.4],
  "primary_uncertainty_source": "lineup_unconfirmed"
```

---

## When not to produce a signal

```
NO_SIGNAL conditions — apply HOLD when:
  · Three or more Tier 1 variables are unconfirmed simultaneously
  · Active macro override is in place
  · Official integrity investigation confirmed on the fixture
  · Adjusted score within 48-52 AND two or more key variables unconfirmed
  · CFTC enforcement action on the token

NO_SIGNAL output:
  {
    "signal":                 "NO_SIGNAL",
    "reason":                 "[primary reason]",
    "resolution_conditions":  "[what must be confirmed]",
    "estimated_resolution":   "[time window]"
  }

NO_SIGNAL is the most honest output when uncertainty exceeds the
reliable signal threshold. An agent that produces NO_SIGNAL appropriately
is better calibrated than one that produces false-confidence signals.
```


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | NOT APPLICABLE | Uncertainty communication is a methodology file — not a domain intelligence file |
| Reasoning | ACTIVE | Uncertainty quantification and communication standards for all reasoning outputs |
| Context | ACTIVE | Context affects uncertainty — lineup unconfirmed and neutral venue both raise uncertainty |
| Memory | NOT APPLICABLE | Uncertainty communication is a structural standard — not memory-dependent |
| Judgment | ACTIVE | Judgment on appropriate uncertainty level for different signal types |
| Attention | ACTIVE | Attention to signals that require elevated uncertainty flagging |
| Communication | ACTIVE | This file defines the communication standard for uncertainty expression |
| Verification | ACTIVE | Verification gaps directly increase uncertainty level in output |
| Learning | ACTIVE | Uncertainty thresholds calibrated from historical accuracy at different confidence levels |
| Integration | ACTIVE | Uncertainty communication standard applied across all five layers |
| Calibration | ACTIVE | Confidence calibration is the empirical basis for uncertainty thresholds |
| Adaptation | ACTIVE | Uncertainty standards adapt as new signal types and edge cases are encountered |
| Ethics | ACTIVE | Understating uncertainty is an ethics failure — overconfidence harms decision quality |
| Transparency | ACTIVE | This file IS a transparency tool — defining how uncertainty is made visible |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
*NO_SIGNAL is the most honest output when uncertainty exceeds reliable signal threshold.*
