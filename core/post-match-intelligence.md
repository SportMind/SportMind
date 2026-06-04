---
name: post-match-intelligence
description: >
  Enduring reasoning framework for the complete post-match signal cycle. Covers
  immediate result processing, demand signal application, FTP PATH_2 settlement
  for $AFC, post-match narrative signals, form signal updates, and pre-match signal
  reset. The post-match cycle feeds directly into the pre-match intelligence for
  the next fixture — intelligence accumulates, it does not reset.
---

# Post-Match Intelligence

**How to reason through the complete post-match signal sequence.**
Post-match intelligence feeds directly into pre-match intelligence for the next fixture.

---

## Immediate result processing (T+0)

```
RESULT CONFIRMATION:
  Load the confirmed result from official source (Tier 1).
  Compare result to pre-match signal direction.

  DIRECTION CORRECT: calibration record candidate.
    Note for submission to calibration framework.
    Cross-reference: core/calibration-framework.md

  DIRECTION INCORRECT: review which modifier failed.
    Which layer produced the wrong signal?
    Flag the modifier for recalibration review.
    Do not discard — incorrect records are as valuable as correct ones.
```

---

## Demand signal application (T+0 to T+4h)

```
WIN:  ×1.08 demand premium
LOSS: ×0.92 demand suppressor
DRAW: ±5% — assess direction from match context
  (dominant draw → mild positive | defensive draw → mild negative)

Duration: 24-48 hours before decaying toward baseline.
Compound with FTP PATH_2 supply event if applicable.
```

---

## FTP PATH_2 settlement — $AFC only (T+0 to T+4h)

```
Monitor chiliscan.com for burn or mint confirmation.

WIN + BURN CONFIRMED:
  Apply permanent supply reduction to next pool calculation.
  New circulating supply = old supply − burned amount.
  New pre-liquidation pool = new supply ÷ 400.
  This is a permanent enduring change — not a temporary modifier.

LOSS + MINT CONFIRMED:
  Apply supply increase to next pool calculation.
  New circulating supply = old supply + minted amount.

DRAW: no supply event. Carry forward unchanged pool.

Source: chiliscan.com (on-chain confirmation required before updating).
Reference: fan-token/ftp-path2.md
```

---

## Post-match narrative signals (T+0 to T+24h)

```
PRESS CONFERENCE SIGNALS:
  Apply manager tone framework from core/press-conference-intelligence.md.
  Positive tone → ×1.02 psychological modifier carry-forward.
  Negative/crisis tone → ×0.94 psychological modifier carry-forward.

INJURY REVELATIONS:
  Any injury confirmed post-match that was not known pre-match:
  Update athlete intelligence file reasoning for next fixture.
  Apply appropriate return timeline from core/temporal-reasoning.md.

TACTICAL SIGNALS:
  Manager discusses tactical approach post-match → update coaching intelligence.
  Formation or system change confirmed → revise pre-match modifier assumptions.
```

---

## Form signal update (T+24h+)

```
Add result to rolling form record.
Apply form decay framework from core/temporal-reasoning.md:
  Last 5 results:      ×1.00 weight (full)
  Results 6-10 ago:    ×0.75 weight
  Results 11-20 ago:   ×0.50 weight
  Older than 20:       ×0.25 — discard

Momentum accumulation: apply win streak modifier from temporal-reasoning.md.
```

---

## Pre-match signal reset

```
CLEAR match-day modifiers — do not carry forward:
  · Specific lineup confirmation (stale after match)
  · Match-day weather conditions
  · Referee appointment signal

CARRY FORWARD to next fixture:
  · Updated form signal (with decay applied)
  · Updated circulating supply (if burn or mint occurred)
  · Psychological modifier from post-match narrative
  · Any injury revelations confirmed post-match
  · Manager tactical intelligence updates
  · Calibration record if applicable
```

---

## REASONING CHAIN — POST-MATCH CYCLE

```
STEP 1 — Confirm result (T+0):
  Load confirmed result from Tier 1 source.
  Compare to pre-match signal direction.
  Correct: flag as calibration candidate.
  Incorrect: identify which modifier failed — flag for recalibration.

STEP 2 — Apply immediate demand signal (T+0 to T+4h):
  WIN: ×1.08 | LOSS: ×0.92 | DRAW: ±5% (context-dependent)

STEP 3 — FTP PATH_2 settlement ($AFC only) (T+0 to T+4h):
  Monitor chiliscan.com for burn/mint confirmation.
  WIN + burn: recalculate circulating supply → new 1/400 pool.
  Update permanently — this feeds into every future PATH_2 calculation.

STEP 4 — Post-match narrative signals (T+0 to T+24h):
  Apply press conference framework (core/press-conference-intelligence.md).
  Manager tone → psychological modifier.
  Injury revelations → update athlete intelligence reasoning.

STEP 5 — Form signal update (T+24h+):
  Add to rolling form record.
  Apply decay: results 6-10 at ×0.75 | results 11-20 at ×0.50.
  Update momentum accumulation signal.

STEP 6 — Pre-match signal reset:
  Clear: lineup, weather, referee signals.
  Carry forward: form, supply, psychological modifier, injury updates,
    tactical intelligence, calibration record.

Cross-reference:
  core/agent-reasoning-chains.md
  core/temporal-reasoning.md
  core/press-conference-intelligence.md
  fan-token/ftp-path2.md
```

---

## Compatibility

**Calibration:**          `core/calibration-framework.md`
**Form and decay:**       `core/temporal-reasoning.md`
**Press conference:**     `core/press-conference-intelligence.md`
**PATH_2 mechanics:**     `fan-token/ftp-path2.md`
**Reasoning chains:**     `core/agent-reasoning-chains.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Post-match intelligence: result analysis, performance signals, and forward-looking implications |
| Reasoning | ACTIVE | Post-match reasoning chain from result to updated signals and modifier adjustments |
| Context | ACTIVE | Post-match context: competition stage, injury updates, manager reaction, form trend |
| Memory | ACTIVE | Post-match result records feed into historical pattern library and calibration base |
| Judgment | ACTIVE | Post-match judgment: distinguishing one-off performance from trend signals |
| Attention | ACTIVE | Post-match attention priority: injury news, performance outliers, signal confirmation |
| Communication | ACTIVE | Post-match output with result, form update, and signal implications |
| Verification | ACTIVE | Post-match injury and performance data requires official confirmation |
| Learning | ACTIVE | Post-match outcomes verify or refute pre-match signals — core calibration input |
| Integration | ACTIVE | Post-match intelligence integrates with calibration framework and form tracking |
| Calibration | ACTIVE | Post-match outcomes are the primary calibration data source |
| Adaptation | ACTIVE | Post-match modifiers adapt immediately — form is recalculated after each result |
| Ethics | NOT APPLICABLE | Post-match analysis is factual — no ethical dimension |
| Transparency | ACTIVE | Pre-match prediction vs post-match outcome comparison explicit in calibration output |


---

*SportMind v3.97.65 · MIT License · sportmind.dev*
*Post-match intelligence accumulates — it does not reset between fixtures.*
