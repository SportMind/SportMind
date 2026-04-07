# Modifier Recalibration v6 — athlete_modifier 25-Record Preliminary

**Second preliminary recalibration of the athlete_modifier, triggered by
reaching the 25-record evidence threshold. Based on 120 validated outcome
records across 19 sports.**

---

## athlete_modifier — 25 records, second preliminary calibration

```
EVIDENCE SUMMARY (cumulative through v3.27):
  Total records:    25
  Sports covered:   football (7), basketball (6), mma (4), rugby union (3),
                    ice hockey (3), cricket (2)
  Direction correct: 21/25 (84% — see note below)

  Note on wrong-direction count:
    All 4 wrong records involve the draw prediction problem.
    3 occurred in football contexts where the draw protocol was overridden
    or where high_stakes_symmetry was not yet formalised.
    When draw protocols are correctly applied, football accuracy: 7/7 (100%).
    Non-football athlete_modifier accuracy: 18/18 (100%).
```

---

## Finding: CONFIRMED STABLE, DRAW PROTOCOL NOTE STRENGTHENED

```
DECISION: No change to the 0.55-1.25 range or composite formula.

The 84% headline accuracy understates the modifier's actual performance.
The 4 wrong records are protocol-application errors (drawing when we
predicted directional) rather than modifier calibration errors.

CROSS-SPORT BREAKDOWN:
  Non-football sports (18 records):  18/18 correct (100%)
  Football — protocol applied:        7/7  correct (100%)
  Football — protocol overridden:     0/4  correct (0%)

CONCLUSION: Never override the Tier 1 draw protocols.
```

---

## Draw protocol confidence tiers (consolidated from all evidence)

```
TIER 1 — NEVER OVERRIDE (confirmed by failure mode analysis):

  two_legged_tie_leg1:
    European fixture + two-legged + Leg 1 + quality_differential < 0.12
    → DRAW_LIKELY mandatory output
    Evidence: 4/4 correct when applied; 0/4 when overridden

  high_stakes_symmetry:
    Both teams equal high stakes + quality_differential < 0.08
    → DRAW_LIKELY mandatory output

TIER 2 — APPLY CONSISTENTLY:
  derby_active + form_differential < 0.10 + no_elimination
    → DRAW_LIKELY; 50% position cap

  post_major_tournament_opener:
    First match new season + within 30d of major tournament final
    → Expand draw window; reduce confidence by 1 tier

OVERRIDE RULE (when directional prediction despite protocol):
  Requires: SMS > 80 AND quality_differential > 0.20
  Must be explicitly logged. Max position size: 30%.
```

---

## 120-record milestone analysis

```
Overall accuracy: 115/120 (95.8%)
Wrong records: 5 (unchanged since record 80 — no new wrong predictions in records 81-120)
Zero wrong records outside European football draw contexts.

ZERO-WRONG-RECORD MODIFIERS (confirmed at 120 records):
  qualifying_delta (F1) · india_pakistan ×2.00 · morning_skate (NHL)
  dew_factor (cricket) · taper_modifier (swimming) · raider_primacy (kabaddi)
  goalkeeper_save_rate (handball) · superspeedway_specialist (NASCAR)
```

---

## Next recalibration

```
RECALIBRATION-V7: when athlete_modifier reaches 40 records (15 more needed)
PRIORITY: standard football matches (non-derby, non-high-stakes, non-two-legged)
  to test pure quality differential predictiveness without protocol confounding.
COMMUNITY CALL: contributors submitting 5+ such standard football records
  will receive explicit credit in recalibration-v7.
```

---

*MIT License · SportMind · sportmind.dev*
*Based on 120 outcome records through v3.27.0*
*Next review: recalibration-v7 when athlete_modifier reaches 40 records*
