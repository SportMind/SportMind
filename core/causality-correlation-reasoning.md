---
name: causality-correlation-reasoning
description: >
  Enduring reasoning framework for distinguishing causal signals from correlational
  signals. Three causality tests, SportMind causal signal register, and a
  calibration feedback loop for upgrading signal confidence over time.
---

# Causality and Correlation Reasoning

**Causal signals apply at full weight. Correlational signals apply at x0.75.**

---

## The fundamental distinction

```
CAUSAL SIGNAL:
  Variable directly causes outcome through a clear, understood mechanism.
  Weight: full modifier value.

CORRELATIONAL SIGNAL:
  Correlates historically but mechanism unclear or confounded.
  Weight: x0.75 confidence weight applied to modifier value.
```

---

## Three tests for causality

```
TEST 1 - MECHANISM CLARITY: can you describe the physical or psychological mechanism?
  YES -> causal candidate | NO -> correlational only

TEST 2 - TEMPORAL PRECEDENCE: does the variable always precede the outcome?
  CLEARLY PRECEDES -> causal candidate | UNCLEAR -> correlational only

TEST 3 - SAMPLE ROBUSTNESS: does it hold across different squads, managers, eras?
  HOLDS -> stronger causal case | VARIES -> correlational with confounders

ALL THREE PASSED -> confirmed causal -> full weight
ONE OR TWO -> provisional causal -> x0.90 weight
ZERO -> correlational -> x0.75 weight
```

---

## SportMind causal signal register

```
CONFIRMED CAUSAL (full weight):
  Dew factor in T20 cricket: mechanism = moisture affects ball grip. x0.75 spin.
  Weight miss in MMA: mechanism = physiological/psychological failure. x0.88.
  Altitude for sea-level teams: mechanism = oxygen availability. up to x0.90.
  Rain on technical football teams: mechanism = passing accuracy reduced. x0.94.

CORRELATIONAL - APPLY x0.75 WEIGHT:
  Home venue H2H record: confounded by squad/manager changes over time.
  Kit colour or superstition patterns: no clear causal mechanism.
  Referee nationality bias claims: insufficient sample, confounded.
```

---

## Calibration feedback loop

```
10 confirmed calibration records for a modifier:
  Upgrade: correlational -> provisional causal. Weight: x0.75 -> x0.90.

20 confirmed records:
  Upgrade: provisional -> confirmed causal. Full modifier weight.

5 incorrect records:
  Downgrade: confirmed -> provisional. x0.90 until rebuilt to 20 correct.

Current base: 129 records across 21 sports.
Modifiers with fewer than 5 records remain correlational.
```

---

## Compatibility

**Signal interaction:** `core/signal-interaction-reasoning.md`
**Calibration:** `core/calibration-framework.md`
**Historical patterns:** `core/historical-pattern-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | NOT APPLICABLE | This is a reasoning methodology file, not a domain intelligence file |
| Reasoning | ACTIVE | Core reasoning methodology: distinguishing causation from correlation in sports signals |
| Context | ACTIVE | Context dependency — causation vs correlation varies by sport and signal type |
| Memory | ACTIVE | Pattern library for known causal relationships vs spurious correlations |
| Judgment | ACTIVE | Primary judgment tool: causal mechanism test before applying modifier |
| Attention | ACTIVE | Attention flag for high-correlation signals lacking causal mechanism |
| Communication | ACTIVE | Output must distinguish: causal modifier vs correlated signal |
| Verification | ACTIVE | Causal claims require mechanism verification — not just statistical association |
| Learning | ACTIVE | Causality library grows from calibration records demonstrating causal relationships |
| Integration | ACTIVE | Applied across all intelligence layers when signal relationships are assessed |
| Calibration | ACTIVE | Calibration records validate or invalidate assumed causal relationships |
| Adaptation | ACTIVE | Causal models adapt as sport rules, player pools, and conditions change |
| Ethics | ACTIVE | Misleading correlation-as-causation outputs are an integrity failure |
| Transparency | ACTIVE | Reasoning must explicitly state whether a relationship is causal or correlational |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
