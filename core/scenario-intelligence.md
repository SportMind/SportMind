---
name: scenario-intelligence
description: >
  Enduring reasoning framework for scenario mapping — constructing multiple possible
  outcome scenarios for any SportMind signal and weighting them by probability. Covers
  the scenario construction framework, $AFC as reference template, probability weighting,
  and resolution triggers. Scenario maps are more useful than probability-weighted averages
  — always output the full map alongside the summary.
---

# Scenario Intelligence

**How to construct and weight scenario maps for any SportMind signal.**
The full scenario map is always more useful than the weighted average alone.

---

## Scenario construction framework

```
MAXIMUM SCENARIOS: 4
  Building more than 4 scenarios reduces reasoning quality.
  Complexity beyond 4 creates false precision — not genuine insight.
  If more than 4 scenarios seem necessary: group the least probable
  into a single "other" scenario.

MINIMUM SCENARIOS: 2
  A single-scenario analysis is a point estimate — not a scenario map.
  Even when one scenario is overwhelming favourite: document the alternative.

SCENARIO QUALITY CRITERIA:
  Each scenario must be:
  · Mutually exclusive (cannot both occur simultaneously)
  · Collectively exhaustive (all scenarios together cover the space)
  · Distinguishable by a specific observable trigger
  · Modifiable by a specific SportMind modifier set
```

---

## $AFC FTP PATH_2 reference template

```
FOR ANY $AFC MATCH — THREE MANDATORY SCENARIOS:

  SCENARIO A — WIN:
    Supply event:       BURN
    Probability:        [from adjusted score WIN probability]
    Pool estimate:      circulating supply ÷ 400
    Demand signal:      ×1.08 WIN premium
    Duration:           24-48h demand | permanent supply reduction
    Resolution trigger: official match result + chiliscan.com burn confirmation

  SCENARIO B — LOSS:
    Supply event:       MINT
    Probability:        [from adjusted score LOSS probability]
    Demand signal:      ×0.92 suppressor
    Duration:           24-48h demand | permanent supply increase
    Resolution trigger: official match result + chiliscan.com mint confirmation

  SCENARIO C — DRAW:
    Supply event:       NONE
    Probability:        [from adjusted score DRAW probability]
    Demand signal:      ±5% context-dependent
    Duration:           24-48h
    Resolution trigger: official match result

  PROBABILITY CONSTRAINT: A + B + C must sum to 1.00.
  Resolution trigger for all three: match result (T+0 to T+4h).
```

---

## General scenario template

```
FOR NON-PATH_2 SCENARIOS:

  SCENARIO [N]:
    Label:              [descriptive name]
    Probability:        [0.00 to 1.00]
    Key modifier:       [from relevant SportMind file]
    Adjusted score:     [calculated]
    Fan token demand:   [signal and duration]
    Resolution trigger: [specific observable event]
    If confirmed:       [next reasoning action]
```

---

## Probability weighting

```
PROBABILITY SOURCE:
  Derive WIN/LOSS/DRAW probabilities from the adjusted score.
  Do not use market odds directly as probability — they include margin.
  Adjusted score → base probability → apply sport-specific conversion.

SCENARIO WEIGHTING RULE:
  Document all probability weights explicitly in output.
  Never apply implied probabilities — state them.
  Probability-weighted expected value = Σ(scenario outcome × probability).

IMPORTANT: Never output only the weighted average.
  The full scenario map alongside the summary is mandatory.
  Users need to see what happens in each scenario, not just the average.
```

---

## Resolution triggers

```
EVERY SCENARIO REQUIRES A RESOLUTION TRIGGER:
  The trigger is the specific observable event that confirms this scenario.
  Without a trigger, the scenario cannot be resolved.

  Examples:
    Lineup scenario: "confirmed lineup announcement T-2h"
    Regulatory scenario: "official regulatory announcement from [authority]"
    Match result: "official result confirmed via [source]"
    Transfer: "official club announcement or registered contract"

WHEN TRIGGER FIRES:
  Discard all other scenarios for this signal.
  Apply the confirmed scenario's modifier at full confidence (×1.00).
  Update the scenario map status to RESOLVED.
```

---

## REASONING CHAIN — SCENARIO MAPPING

```
STEP 1 — Load base signal:
  Run standard pre-match or pre-event reasoning chain from
  core/agent-reasoning-chains.md.
  Produce base adjusted score and direction.

STEP 2 — Identify key uncertain variable:
  What single variable would most change the outcome if resolved differently?
  Lineup confirmation? Key player fitness? Regulatory decision? Macro shift?

STEP 3 — Build scenario set (maximum 4):
  Define 2-4 distinct possible outcomes for the key variable.
  More than 4 reduces reasoning quality — group minor scenarios.

STEP 4 — Apply SportMind modifiers per scenario:
  For each scenario load the relevant intelligence files and calculate:
  · Adjusted score | FTP PATH_2 supply event if applicable
  · Fan token demand signal | Duration of the effect

STEP 5 — Weight by probability:
  Use SportMind adjusted score as WIN probability base.
  Document all weights explicitly.
  Probability-weighted expected value = Σ(scenario outcome × probability).

STEP 6 — Output the full map:
  Never output only the weighted average.
  Always output the complete scenario map alongside the weighted summary.

STEP 7 — Set resolution trigger:
  Document exactly what event confirms which scenario.
  When does uncertainty resolve? What observable event confirms it?

Cross-reference:
  core/agent-reasoning-chains.md
  core/uncertainty-communication.md
  core/counterfactual-reasoning.md
  fan-token/ftp-path2.md
```

---

## Compatibility

**Agent reasoning:**       `core/agent-reasoning-chains.md`
**Uncertainty:**           `core/uncertainty-communication.md`
**Counterfactual:**        `core/counterfactual-reasoning.md`
**Breaking news:**         `core/breaking-news-intelligence.md`
**PATH_2 mechanics:**      `fan-token/ftp-path2.md`
**State-space:**           `core/state-space-reasoning.md`

---

*SportMind v3.97.65 · MIT License · sportmind.dev*
*Never output only the weighted average. The full scenario map is always more useful.*
