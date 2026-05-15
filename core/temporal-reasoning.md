---
name: temporal-reasoning
description: >
  Enduring reasoning framework for how signals change over time — within a match,
  across a season, and across multiple seasons. Covers signal decay by type, momentum
  accumulation with logarithmic ceiling, fatigue accumulation, in-match temporal
  adjustment, and multi-season club trajectory signals.
---

# Temporal Reasoning

**How signals change over time and how to weight recent versus historical data.**

---

## Signal decay framework

```
NEW MANAGER EFFECT DECAY:
  Matches 1-5:    full effect ×1.06
  Matches 6-15:   partial effect ×1.02
  Match 16+:      no effect — baseline applies

FORM SIGNAL DECAY (recency weighting):
  Last 5 matches:      ×1.00 (full weight)
  Matches 6-10 ago:    ×0.75
  Matches 11-20 ago:   ×0.50
  Older than 20:       ×0.25 — discard; too distant to be reliable signal

INJURY RETURN DECAY (performance recovery curve):
  Match 1 back:    ×0.88 effective performance
  Match 2 back:    ×0.93
  Match 3 back:    ×0.97
  Match 4+ back:   full performance modifier applies

TRANSFER ARRIVAL INTEGRATION:
  Matches 1-3:    ×0.94 — integration uncertainty
  Matches 4-10:   ×0.97 — settling in
  Match 11+:      full modifier — fully integrated
```

---

## Signal accumulation framework

```
MOMENTUM ACCUMULATION (win streaks — logarithmic, ceiling at 7+):
  Win 3:   ×1.03
  Win 5:   ×1.06
  Win 7+:  ×1.08 ceiling — further wins do not increase above this

MOMENTUM DECAY (loss streaks):
  Loss 3:  ×0.96
  Loss 5:  ×0.93
  Loss 7+: ×0.90 floor — further losses do not decrease below this

FATIGUE ACCUMULATION (fixture congestion):
  Match 1 of congested period:            no modifier
  Match 2 within 4 days of previous:      ×0.97
  Match 3 within 7 days of match 1:       ×0.94
  Match 4+ within 10 days of match 1:     ×0.91
```

---

## In-match temporal reasoning

```
FIRST GOAL CONCEDED:
  WIN probability: reduces to approximately 65% of pre-match estimate
  DRAW probability: increases to approximately 150% of pre-match estimate
  For PATH_2: recalculate WIN probability and update burn magnitude estimate

HALF-TIME TRAILING BY ONE:
  WIN probability: approximately 25% of original pre-match estimate
  Communicate revised supply event expectation explicitly
```

---

## Multi-season trajectory signals

```
DOMINANT PERIOD (3+ consecutive trophies in same competition):
  Apply: ×1.08 psychological pedigree modifier

REBUILDING PERIOD (major squad overhaul or new manager + 2+ barren seasons):
  Apply: ×0.95 identity uncertainty modifier
  Suspend historical modifiers for first 10 matches of new era

DECLINE PERIOD (declining league position trend over 3+ seasons):
  Apply: ×0.92 trajectory discount
  Historical data increasingly overestimates current quality
```

---

*SportMind v3.97.52 · MIT License · sportmind.dev*
*Form older than 20 matches is noise, not signal. Discard at ×0.25 weight.*
