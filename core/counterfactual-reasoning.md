---
name: counterfactual-reasoning
description: >
  Enduring reasoning framework for producing honest uncertainty ranges through
  counterfactual scenario analysis. Four-step framework, standard counterfactuals
  by signal type, and FTP PATH_2 three-scenario output.
---

# Counterfactual Reasoning

**How to reason about what the signal would be if a key variable were different.**
Honest intelligence produces ranges, not false-precision point estimates.

---

## The four-step framework

```
STEP 1 - IDENTIFY THE KEY UNCERTAIN VARIABLE:
  Most common: starting lineup confirmation.
  Sometimes: weather conditions (within 24h).
  Rarely: referee appointment.

STEP 2 - CALCULATE BOTH SCENARIOS:
  Favourable scenario: variable confirmed positive -> adjusted score
  Unfavourable scenario: variable confirmed negative -> adjusted score

STEP 3 - WEIGHT BY PROBABILITY:
  Apply current best-estimate probability to each scenario.
  Probability-weighted midpoint = base adjusted score.
  Range = favourable to unfavourable.

STEP 4 - COMMUNICATE THE RANGE:
  "adjusted_score": 72.4,
  "scenario_range": {
    "favourable": 80.2,
    "unfavourable": 64.6,
    "key_variable": "[variable name]",
    "resolution_window": "[when confirmed]"
  }
```

---

## Standard counterfactuals by signal type

```
PRE-MATCH - always calculate:

  Lineup uncertainty:
    Confirmed vs unconfirmed: +/-4-8 points typical
    Elite player fit vs absent: +/-8-16 points

  Weather (weather-sensitive sport): +/-4-8 points

  Resolution windows:
    Lineup: T-6h to T-2h (varies by league)
    Weather: reliable at T-12h; confirmed at T-2h
```

---

## FTP PATH_2 counterfactual output

```
ALWAYS CALCULATE AND COMMUNICATE ALL THREE SCENARIOS:

  WIN scenario:   supply event = BURN  | probability = [WIN prob]
  LOSS scenario:  supply event = MINT  | probability = [LOSS prob]
  DRAW scenario:  supply event = NONE  | probability = [DRAW prob]

  Do not output only the most likely scenario - communicate all three.
```

---

## Compatibility

**Uncertainty communication:** `core/uncertainty-communication.md`
**Signal interaction:** `core/signal-interaction-reasoning.md`
**PATH_2 mechanics:** `fan-token/ftp-path2.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | NOT APPLICABLE | Counterfactual reasoning is a methodology, not a domain intelligence file |
| Reasoning | ACTIVE | Core reasoning method: what-if analysis and alternative scenario evaluation |
| Context | ACTIVE | Counterfactuals are context-dependent — same event has different counterfactuals by situation |
| Memory | ACTIVE | Historical counterfactual baselines for common scenario types |
| Judgment | ACTIVE | Judgment on which counterfactuals are plausible vs speculative |
| Attention | ACTIVE | Counterfactual attention: identifies what to watch for that would change signal |
| Communication | ACTIVE | Counterfactual output: explicit statement of alternative scenarios considered |
| Verification | NOT APPLICABLE | Counterfactuals are hypothetical — verification applies to inputs, not the counterfactual itself |
| Learning | ACTIVE | Counterfactual model improves as actual outcomes validate or refute scenarios |
| Integration | ACTIVE | Counterfactual reasoning applied across all intelligence layers |
| Calibration | EMERGING | Counterfactual accuracy is difficult to calibrate — no direct outcome measurement |
| Adaptation | ACTIVE | Counterfactual scenarios adapt as real-world conditions evolve |
| Ethics | ACTIVE | Counterfactuals must be presented as hypothetical — not predictive certainties |
| Transparency | ACTIVE | Counterfactual scenarios explicitly labelled as alternative scenarios in output |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
