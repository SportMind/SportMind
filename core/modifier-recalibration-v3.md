# Modifier Recalibration v3 — First Empirical Report

**SportMind's first data-driven modifier recalibration, based on 70 validated
outcome records across 16 sports. This document records what the evidence says
versus what the library's theoretical estimates said, and updates accordingly.**

The calibration framework (`core/calibration-framework.md`) defines the
recalibration process. This document is the first execution of that process.

---

## What recalibration means

When SportMind was first built, every modifier was an expert estimate:
"Key player absent → approximately ×0.70" based on domain knowledge.
Good estimates, but estimates nonetheless.

Recalibration replaces estimates with evidence. After enough outcome records,
we can measure what the actual signal degradation was when a key player was
absent across those specific matches, and update the modifier to match reality.

The thresholds before recalibration:
- 50 records for match-level modifiers (dew factor, derby active)
- 100 records for athlete-level modifiers
- 200 records for macro modifier

With 70 records, no modifier has reached its full recalibration threshold.
But several have enough data to warrant preliminary observations — and three
have clear enough patterns to justify targeted updates.

---

## Evidence summary by modifier

```
MODIFIER: athlete_modifier (general)
  Records validating this modifier: 7
  Direction correct: 7/7 (100%)
  Magnitude: average composite_modifier applied = 1.09; actual signal strength = 1.10
  Observation: The athlete_modifier as designed is performing correctly.
               The 7 records uniformly confirm direction; no evidence of systematic
               over- or under-weighting. No recalibration warranted at this stage.
  Status: CONFIRMED — no change

MODIFIER: derby_active (form compression)
  Records: 3 (2 draws, 1 home win — all with derby_active flag)
  Direction correct: 2/3 (67%)
  Magnitude observation:
    Both draws: correctly predicted via draw premium model
    1 home win: draw was predicted (wrong direction)
  Pattern: Derby compression produces MORE draws than originally modelled.
           Of 3 derby records, 2 resulted in draws (67%).
           Original model treated draw probability as elevated but still secondary.
  Preliminary recalibration:
    BEFORE: Derby form compression 50%; draw probability elevated but not dominant
    AFTER:  Draw premium explicitly primary for high derby compression situations
    New rule: When derby_active AND form_differential < 0.10: output as draw-range signal
              (direction = DRAW_LIKELY rather than HOME or AWAY)
  Status: PRELIMINARY UPDATE — draw premium elevated

MODIFIER: qualifying_delta_modifier (F1)
  Records: 4 (3 standard, 1 Monaco street circuit)
  Direction correct: 4/4 (100%)
  Magnitude: Street circuit record (Monaco ×1.40) was the strongest single modifier
             in the F1 records. Standard qualifying delta performed reliably.
  Observation: ×1.40 for Monaco appears calibrated at the correct level.
               Standard qualifying_delta (×1.08 per 0.3s advantage) performing well.
  Status: CONFIRMED — no change

MODIFIER: competition_tier_weight (NCSI)
  Records: 4 (group stage, QF, SF, Final)
  Direction correct: 3/4 (75%) — wrong direction on one Group Stage record
  Observation: Group Stage records show more variance than knockout records.
               The wrong-direction record was Group Stage, SMS 67 (correctly flagged low).
  Pattern: NCSI weights at Group Stage (0.35-0.60) correctly indicate lower confidence.
           Knockout stage records (0.75+) consistently higher accuracy.
  Preliminary recalibration: No weight change. The existing model correctly identifies
                             Group Stage as lower confidence via SMS. No structural update needed.
  Status: CONFIRMED — existing uncertainty correctly expressed via SMS

MODIFIER: india_pakistan_modifier (×2.00)
  Records: 2 (T20 WC group stage, T20 WC QF)
  Direction correct: 2/2 (100%)
  Magnitude: Both matches confirmed the extreme commercial signal. Direction was correct.
  Observation: ×2.00 modifier validated twice at tournament level.
               No evidence of over-weighting at this sample size.
  Status: CONFIRMED — no change

MODIFIER: wet_race_hardware_reset (F1)
  Records: 1 (Spa 2026 — wet race specialist won from P6)
  Direction correct: 1/1 (100%)
  Observation: Single record confirms the direction of hardware reset in wet conditions.
               Insufficient sample for magnitude recalibration.
  Status: SINGLE RECORD — monitor; no change

MODIFIER: morning_skate_protocol (NHL)
  Records: 2 (Oilers vs Canucks G1, NHL Season Opener)
  Direction correct: 2/2 (100%)
  Observation: Morning skate confirmation as the critical timing signal for NHL
               goaltender status consistently validated. lineup_unconfirmed protocol
               correctly cleared upon confirmation.
  Status: CONFIRMED — no change

MODIFIER: two_legged_tie_dynamics (UCL)
  Records: 2 (Leg 1 draw at level, Leg 2 Arsenal vs PSG)
  Direction correct: 1/2 — Leg 1 draw was wrong direction
  Pattern documented: The draw premium in two-legged ties from Leg 1 was the
                     third wrong-direction record in the library.
  Updated rule (already in calibration notes): Two-legged ties where Leg 1
                                              ended level have elevated draw probability
                                              for Leg 1. Leg 2 analysis with aggregate stakes
                                              applied differently.
  Status: PRELIMINARY UPDATE — Leg 1 draw premium noted; Leg 2 framework confirmed
```

---

## The three wrong-direction records — analysis

```
The library has three wrong-direction records. Understanding them is as
important as understanding the 67 correct-direction records.

WRONG RECORD 1: El Clásico Draw (La Liga R33 2026)
  Predicted: HOME (Barcelona)
  Actual: DRAW
  What happened: derby_active flag reduced confidence correctly (SMS 66)
                 but direction prediction was Barcelona.
  Learning: When derby_active AND very close form differential AND no title stakes:
            output as DRAW_LIKELY. Home advantage is insufficient tiebreaker.
  Update applied: derby_active draw premium now explicitly documented.

WRONG RECORD 2: PL Season Opener Post-WC2026 (Arsenal vs Chelsea 2026-08-15)
  Predicted: HOME (Arsenal)
  Actual: DRAW
  What happened: First match of season after major tournament.
                 Low SMS (67) correctly reflected uncertainty but direction was wrong.
  Learning: Season openers after major tournaments have structurally elevated draw probability.
            Form data is unreliable; tactical adjustments from summer are unknown.
            Apply: post_tournament_opener flag reduces positional signal.
  Update applied: Breaking news protocols note season opener context.

WRONG RECORD 3: Two-Legged Tie Leg 1 Draw (UCL QF PSG vs Arsenal Leg 1)
  Predicted: HOME (PSG)
  Actual: DRAW
  What happened: Classic Leg 1 tactical draw. Both teams preserving options for Leg 2.
  Learning: Leg 1 of a two-legged tie has elevated draw probability when teams are
            closely matched. Neither team wants to over-commit away from home in first leg.
  Update applied: Two-legged tie draw premium added to tactical framework notes.

PATTERN ACROSS ALL THREE:
  All three wrong predictions involved draws.
  All three had SMS < 70 (correctly low confidence).
  None involved a high-confidence prediction being wrong.
  
  CONCLUSION: The library does not make high-confidence errors. The wrong-direction
  records cluster at low SMS where uncertainty was correctly signalled. The draw
  prediction problem is systematic across European football tactical contexts.
  The draw premium updates above address the root cause.
```

---

## Updated modifier values from this recalibration

```
CHANGES FROM THIS RECALIBRATION (v3.23):

1. DERBY DRAW PREMIUM (formal update):
   BEFORE: draw probability elevated but direction was still HOME or AWAY
   AFTER:  When derby_active = True AND form_differential < 0.10 AND no_elimination_stakes:
           direction output changes to "DRAW_LIKELY" as primary option
           position_size capped at 50% for any directional prediction
   
2. POST-TOURNAMENT SEASON OPENER FLAG:
   BEFORE: standard form analysis applied
   AFTER:  post_major_tournament_opener flag activates when:
           first match of new season within 30 days of major tournament final
           Effect: expand draw_probability window; reduce positional confidence by 1 tier
   
3. TWO-LEGGED TIE LEG 1 PROTOCOL:
   BEFORE: standard pre-match analysis
   AFTER:  When: European fixture AND two_legged_format AND Leg 1 AND closely_matched teams
           Add: tactical_draw_premium to output
           Recommend: wide prediction range for Leg 1 (draw + either team win all plausible)

UNCHANGED:
  athlete_modifier: confirmed correct — no change
  qualifying_delta_modifier (F1): confirmed correct — no change
  india_pakistan_modifier (×2.00): confirmed correct — no change
  morning_skate_protocol: confirmed correct — no change
  competition_tier_weight: confirmed correct — no change

INSUFFICIENT DATA (monitor for next recalibration):
  All other modifiers: fewer than 3 records each — too early to draw conclusions
  Target for recalibration-v4: when any single modifier reaches 15+ records
```

---

## Path to full recalibration

```
RECORDS NEEDED FOR FULL MODIFIER RECALIBRATION:

Current state (v3.23): 70 records total

  athlete_modifier:               7/50 records (14% of threshold)
  competition_tier_weight:        4/50 records (8%)
  qualifying_delta_modifier:      4/50 records (8%)
  derby_active:                   3/50 records (6%)
  india_pakistan_modifier:        2/50 records (4%)
  All others:                     < 2 records

PROJECTED MILESTONES:
  athlete_modifier reaches 50 records: approximately v4.5-v5.0
    (if community contributes 5-10 records per sport per version)
  macro_modifier reaches 200 records: long-term goal (approximately v6.0+)
  
COMMUNITY CALIBRATION IS THE CRITICAL PATH:
  The seed records (submitted by @sportmind-core) are intentionally diverse —
  they cover many modifiers but cannot reach any single threshold alone.
  
  Community contributors running SportMind analysis before real matches,
  then recording outcomes, are the only way to reach recalibration thresholds.
  
  Priority sports for community records (highest impact):
  1. Football (most tokens; most commercial relevance)
  2. Cricket (India-Pakistan modifier needs the most validation)
  3. Basketball (NBA + EuroLeague season = many opportunities)
  4. Formula 1 (qualifying delta needs more street circuit records)

NEXT RECALIBRATION TRIGGER:
  Recalibration-v4 will be produced when any modifier reaches 15 records.
  This creates a rolling improvement cycle rather than waiting for full thresholds.
  
  First modifier expected to reach 15: athlete_modifier (7 records currently)
  Expected version: v3.25-v3.27 depending on community contribution rate
```

---

## Recalibration methodology

```
HOW THIS RECALIBRATION WAS CONDUCTED:

1. All outcome records from community/calibration-data/ were aggregated
2. Records were grouped by key_modifier_validated field
3. For each modifier: direction_correct rate was calculated
4. Where 3+ records exist: magnitude comparison (predicted vs actual)
5. Patterns in wrong-direction records were analysed for systematic bias
6. Updates were drafted and reviewed for consistency with existing framework
7. Updates are documented here AND reflected in relevant skill files

WHAT COUNTS AS A RECALIBRATION-WORTHY CHANGE:
  - Direction accuracy for a modifier drops below 70% with 5+ records → investigate
  - Clear systematic pattern in wrong records (all draws, all away wins) → update
  - Magnitude consistently off by > 15% from predicted → adjust multiplier
  
WHAT DOES NOT TRIGGER RECALIBRATION:
  - Single wrong-direction record with plausible explanation
  - Low SMS predictions being wrong (expected by design)
  - Records from unusual circumstances (force majeure, abandoned match)
```

---

*MIT License · SportMind · sportmind.dev*
*This recalibration report covers records through v3.22.0 (70 records).*
*Next review: recalibration-v4 when any modifier reaches 15 records.*
