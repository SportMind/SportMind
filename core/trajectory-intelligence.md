---
name: trajectory-intelligence
description: >
  Enduring reasoning framework for club and fan token trajectory assessment across
  multiple seasons. Covers ascending/plateauing/descending trajectory classification,
  duration-scaled modifiers, inflection signal detection, horizon application rules,
  and connection to state-space reasoning. Minimum 6 months of signals required
  before trajectory modifier applies.
---

# Trajectory Intelligence

**How to assess and apply trajectory intelligence for a club or token over time.**
Trajectory is a medium-term signal — it applies to planning signals, not execution signals.

---

## Trajectory classification

```
ASCENDING trajectory:
  Adjusted score trend rising consistently across 6+ months.
  Multiple seasons of consistent improvement.
  Commercial health improving.

PLATEAUING trajectory:
  Adjusted score trend flat across 6+ months.
  Neither clearly improving nor declining.
  Apply no modifier — baseline only.

DESCENDING trajectory:
  Adjusted score trend falling consistently across 6+ months.
  Multiple seasons of consistent decline.
  Commercial health deteriorating.

MIXED trajectory:
  No consistent direction across the signal set.
  Apply no modifier — insufficient evidence for directional signal.
```

---

## Duration-scaled modifiers

```
ASCENDING:
  6-11 months:   ×1.025 (half modifier — trend establishing)
  12+ months:    ×1.05  (full modifier — trend confirmed)

DESCENDING:
  6-11 months:   ×0.975 (half modifier)
  12+ months:    ×0.95  (full modifier)

MINIMUM DATA REQUIREMENT: 6 months of signals.
  Fewer than 6 months: insufficient for trajectory assessment.
  Apply single-match signal reasoning only.
  Do not apply trajectory modifier.
```

---

## Inflection signal detection

```
SIGNALS THAT OVERRIDE CURRENT TRAJECTORY:

  POSITIVE INFLECTION (descending → potential ascending):
    New manager with immediate positive results (3+ wins in 5)
    Major commercial partnership announced (Tier 1 sponsor)
    Key player acquisition in primary position gap
    Ownership change with confirmed investment commitment

  NEGATIVE INFLECTION (ascending → potential descending):
    Manager departure mid-season (not end of season)
    Key player departure without replacement
    Regulatory or financial investigation confirmed
    Multiple partnership terminations within 90 days

  TRANSITION PERIOD RULE:
    When inflection signal detected: do not apply current trajectory modifier.
    Apply ×0.90 confidence weight instead — transition uncertainty.
    Reassess trajectory after 3 full months of new-era data.
```

---

## Fan token trajectory signals

```
FAN TOKEN DEMAND TRAJECTORY (distinct from club trajectory):
  Fan token demand can trajectory differently from club performance.
  A club in descending sporting trajectory may have ascending token demand
  if commercial signals are strong (new partnerships, ecosystem growth).

  Apply BOTH trajectories independently:
    Club trajectory → adjusted score modifier
    Fan token trajectory → demand signal modifier
  These are separate signals — do not merge them.

CDI TRAJECTORY:
  If CDI (Club Demand Index) has been rising for 6+ months:
  Apply ×1.04 sustained demand trajectory modifier.
  If CDI declining for 6+ months:
  Apply ×0.96 sustained demand trajectory discount.
```

---

## REASONING CHAIN — TRAJECTORY ASSESSMENT

```
STEP 1 — Gather multi-season data:
  Minimum 6 months of signals required.
  Fewer than 6 months: do not apply trajectory modifier.
  Apply single-match signal reasoning only.

STEP 2 — Identify trend direction:
  Rising consistently? → ASCENDING
  Flat? → PLATEAUING (no modifier)
  Falling consistently? → DESCENDING
  Mixed? → No trajectory modifier

STEP 3 — Check trajectory duration:
  6-11 months: apply half modifier (×1.025 ascending | ×0.975 descending)
  12+ months:  apply full modifier (×1.05 ascending | ×0.95 descending)

STEP 4 — Look for inflection signals:
  Any inflection signals present from the framework above?
  YES: do not apply current trajectory modifier
       apply ×0.90 transition confidence weight instead

STEP 5 — Apply to appropriate horizon:
  Trajectory modifiers are MEDIUM-TERM.
  Apply to planning signals (T-72h+).
  Do NOT apply to execution signals (T-2h).
  Execution signals use confirmed match-day intelligence only.

STEP 6 — Connect to state-space:
  Load core/state-space-reasoning.md.
  Does the trajectory modifier align with the current competitive state?
  Both ascending + TITLE_CONTENDER: compound positive signal.
  Descending + TITLE_CONTENDER: contradiction — investigate cause
    before applying either modifier.

Cross-reference:
  core/state-space-reasoning.md
  core/multi-horizon-reasoning.md
  core/historical-pattern-intelligence.md
```

---

## Compatibility

**State-space:**           `core/state-space-reasoning.md`
**Multi-horizon:**         `core/multi-horizon-reasoning.md`
**Historical patterns:**   `core/historical-pattern-intelligence.md`
**Temporal reasoning:**    `core/temporal-reasoning.md`
**Scenario intelligence:** `core/scenario-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Trajectory intelligence: performance trend analysis, form arc, and momentum signals |
| Reasoning | ACTIVE | Trajectory reasoning chain from trend data to form modifier and APS adjustment |
| Context | ACTIVE | Trajectory context: window length, opposition quality, competition context of results |
| Memory | ACTIVE | Historical trajectory pattern data and their predictive accuracy |
| Judgment | ACTIVE | Trajectory judgment: distinguishing genuine form shift from statistical noise |
| Attention | ACTIVE | Elevated attention for significant trajectory changes in either direction |
| Communication | ACTIVE | Trajectory output: trend direction, window, and form modifier value |
| Verification | ACTIVE | Result data for trajectory calculation requires official sources |
| Learning | ACTIVE | Trajectory pattern calibration from historical trend-to-outcome data |
| Integration | ACTIVE | Integrates with APS modifier, post-match intelligence, and form tracking |
| Calibration | ACTIVE | Trajectory modifiers calibrated against historical form-outcome correlation |
| Adaptation | ACTIVE | Trajectory windows adapt by sport domain and competition type |
| Ethics | NOT APPLICABLE | Trajectory analysis is factual — no ethical dimension |
| Transparency | ACTIVE | Trajectory window, result set, and trend basis explicit in output |


---

*SportMind v3.97.65 · MIT License · sportmind.dev*
*Minimum 6 months of signals required before trajectory modifier applies.*
*Trajectory applies to planning signals only — never execution signals.*
