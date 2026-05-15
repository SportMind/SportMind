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

---

*SportMind v3.97.52 · MIT License · sportmind.dev*
