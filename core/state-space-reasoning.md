---
name: state-space-reasoning
description: >
  Enduring reasoning framework for competitive and commercial state classification.
  Covers competitive state definitions, commercial state signals, fan token state
  from registry, state-dependent modifier profiles, transition detection, and
  connection to scenario intelligence. Current state determines the base modifier
  profile within which all match-specific signals are interpreted.
---

# State-Space Reasoning

**How to classify current competitive and commercial state and apply state-dependent modifiers.**
State determines the base modifier profile — match-specific signals operate within it.

---

## Competitive state definitions

```
TITLE_CONTENDER:
  Definition: mathematically capable of winning the league/competition
    with realistic probability (above 20%) given matches remaining
  Base modifier: ×1.10 motivation premium
  Risk signal: squad rotation risk as manager balances competitions

EUROPEAN_QUALIFICATION_PUSH:
  Definition: in contention for European competition spots
    (top 4/6 depending on league) with 10+ matches remaining
  Base modifier: ×1.05 motivation premium

MID_TABLE_STABLE:
  Definition: neither in title/European contention nor relegation risk
  Base modifier: ×1.00 (no adjustment)
  Signal: form and recent results are primary drivers

RELEGATION_BATTLE:
  Definition: within 6 points of relegation zone with 15+ matches remaining,
    or within 3 points with fewer than 15 remaining
  Base modifier: ×0.88 — see financial-sustainability-intelligence.md
  Compound with squad morale and key player transfer risk signals

RELEGATED:
  Definition: mathematically relegated — confirmed
  Base modifier: ×0.75 — Championship/equivalent context applies
  Fan token demand: −25 to −40% immediate | 4-8 week recovery baseline
```

---

## Commercial state definitions

```
COMMERCIAL_GROWTH:
  New major partnership confirmed in last 90 days.
  CDI ascending trajectory confirmed.
  Base CDI modifier: ×1.05 sustained.

COMMERCIAL_STABLE:
  No significant commercial changes in last 90 days.
  Base CDI modifier: ×1.00 (no adjustment).

COMMERCIAL_DECLINE:
  Partnership lost or COMMERCIAL_DISTRESS_SIGNAL triggered.
  CDI descending trajectory confirmed.
  Base CDI modifier: ×0.92 sustained.
  Reference: market/commercial-partnership-intelligence.md
```

---

## Fan token state (from registry)

```
ACTIVE_PARTNER: confirmed active Chiliz/Socios partnership
  Apply full fan token intelligence framework.

PIPELINE: MOU or early-stage partnership
  Apply pipeline modifier only — do not model as active token demand.

LEGACY_ONCHAIN: partnership ended, token exists on-chain
  Do not apply demand signal framework.
  Reference for on-chain activity monitoring only.

DELISTED: partnership ended, token delisted
  No demand modelling applicable.

Reference: fan-token/registry/complete-registry.md for current status.
```

---

## Transition trigger detection

```
COMPETITIVE STATE TRANSITIONS:
  MID_TABLE → TITLE_CONTENDER:   5+ consecutive wins + top-2 position
  TITLE_CONTENDER → MID_TABLE:   3+ consecutive losses + 10+ points behind
  MID_TABLE → RELEGATION_BATTLE: within 6 points of drop zone
  RELEGATION_BATTLE → RELEGATED: mathematically confirmed

COMMERCIAL STATE TRANSITIONS:
  STABLE → GROWTH:    new Tier 1/2 sponsor or partnership confirmed
  STABLE → DECLINE:   partnership terminated or COMMERCIAL_DISTRESS_SIGNAL
  GROWTH → STABLE:    no new commercial signals for 90 days post-announcement

TRANSITION CONFIDENCE WEIGHT:
  During confirmed state transition: apply ×0.90 confidence weight.
  States in transition have higher uncertainty than settled states.
  Reassess after 3 full months in new state.
```

---

## REASONING CHAIN — STATE ASSESSMENT

```
STEP 1 — Assess competitive state:
  What is current league position relative to objectives?
  Apply competitive state definitions to assign correct state.
  Check: is any transition trigger currently active?

STEP 2 — Assess commercial state:
  Any commercial signals fired in last 90 days?
  New partnership → COMMERCIAL_GROWTH
  Lost partnership → COMMERCIAL_DECLINE
  No change → COMMERCIAL_STABLE

STEP 3 — Assess fan token state:
  Is partnership active, pipeline, legacy, or delisted?
  Is FTP PATH_2 confirmed? Is token omnichain?
  Assign from fan-token/registry/complete-registry.md.

STEP 4 — Apply state-dependent base modifiers:
  Each state has a base modifier profile.
  Apply the profile for the current state before any match-specific modifiers.
  Match-specific modifiers operate within the state context — not independently.

STEP 5 — Check for state transition:
  Any transition triggers present?
  YES: apply ×0.90 confidence weight during transition period.
  States in transition are more uncertain than settled states.

STEP 6 — Connect to scenario intelligence:
  Each possible future state is a scenario.
  Load core/scenario-intelligence.md.
  Map transition probabilities as scenario weights.
  Current state = base case. Possible next states = scenarios.

Cross-reference:
  fan-token/registry/complete-registry.md
  core/trajectory-intelligence.md
  core/scenario-intelligence.md
  core/financial-sustainability-intelligence.md
```

---

## Compatibility

**Registry:**              `fan-token/registry/complete-registry.md`
**Trajectory:**            `core/trajectory-intelligence.md`
**Scenario:**              `core/scenario-intelligence.md`
**Financial:**             `core/financial-sustainability-intelligence.md`
**Commercial:**            `market/commercial-partnership-intelligence.md`

---

*SportMind v3.97.65 · MIT License · sportmind.dev*
*State determines the base modifier profile. Match-specific signals operate within state context.*
*Transitions: apply ×0.90 confidence weight during confirmed transition periods.*
