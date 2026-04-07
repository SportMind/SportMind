# Calibration Methodology Report — SportMind v3.6

**First aggregate calibration run across all 7 seed outcome records.**

Generated: 2026-04-03
Records: 7 (all seed records submitted by `sportmind-core`)
Sports covered: basketball, cricket, football, formula1, mma, rugby-league

---

## Summary

| Metric | Value | Status |
|---|---|---|
| Total outcome records | 7 | Seed phase |
| Community records | 0 | Pending community submissions |
| Overall direction accuracy | 100% (7/7) | INFORMATIONAL — small sample |
| CRITICAL/HIGH modifier violations | 0 | Healthy |
| Modifiers ready for recalibration | 0 | Insufficient data (by design) |

---

## Direction accuracy by sport

| Sport | Correct | Total | Accuracy | Notes |
|---|---|---|---|---|
| Basketball | 2 | 2 | 100% | KD trade + NBA Finals G5 |
| Cricket | 1 | 1 | 100% | IPL DLS dew factor validated |
| Football | 1 | 1 | 100% | UCL Final Man City win |
| Formula 1 | 1 | 1 | 100% | British GP Verstappen |
| MMA | 1 | 1 | 100% | UFC 281 (macro override correctly applied) |
| Rugby League | 1 | 1 | 100% | State of Origin G3 decider |

**Interpretation:** 100% direction accuracy across 7 records is expected and
informational — seed records were selected from known-outcome historical events.
The sample is far too small to draw statistical conclusions. The calibrated
column shows `null` (not yet calibrated) for all tiers because minimum event
thresholds have not been reached. This is the correct behaviour.

---

## Confidence tier calibration

| Tier | N | Accuracy | Target | Calibrated? |
|---|---|---|---|---|
| HIGH | 4 | 100% | ≥72% | Not yet (N < 10 minimum) |
| MEDIUM | 1 | 100% | ≥58% | Not yet (N < 10 minimum) |
| LOW | 2 | 100% | ≥48% | Not yet (N < 10 minimum) |

**Interpretation of LOW tier 100% accuracy:** The two LOW-confidence records
are the State of Origin G3 (53.2 adjusted score) and the UFC 281 under macro
override (30.25 adjusted score). Both were correct — but LOW confidence means
"barely above coin flip reliability", not "we expect to be wrong". The seed
records validate that the confidence tier assignment logic is consistent with
the outcomes, but calibration requires 50+ events per tier before conclusions
are drawn.

---

## Modifier accuracy status

| Modifier | Events | Required | Status | Direction accuracy |
|---|---|---|---|---|
| athlete_modifier | 1 | 100 | INSUFFICIENT_DATA | 100% (1/1) |
| dew_modifier | 1 | 50 | INSUFFICIENT_DATA | 100% (1/1) |
| macro_modifier | 1 | 200 | INSUFFICIENT_DATA | 100% (1/1) |
| narrative_modifier | 1 | 100 | INSUFFICIENT_DATA | 100% (1/1) |
| qualifying_delta_modifier | 1 | 100 | INSUFFICIENT_DATA | 100% (1/1) |
| rivalry_form_discount | 1 | 50 | INSUFFICIENT_DATA | 100% (1/1) |
| player_tier_1_trade_signal | 1 | 100 | INSUFFICIENT_DATA | 100% (1/1) |

**All modifiers show INSUFFICIENT_DATA — this is correct and expected.** The
minimum event thresholds exist to prevent spurious calibration from small samples.
The first real calibration update will require community submissions bringing any
modifier to its minimum threshold.

**Closest to threshold:** dew_modifier and rivalry_form_discount both require
only 50 events. Cricket and rugby league are the target sports for early community
calibration submissions.

---

## Key insights from seed records

**1. The macro override validation is the most important single result.**
The UFC 281 record shows that a LOW confidence output (30.25 adjusted score, flagged
`macro_override_active`) correctly identified the event as not a token entry point —
the $UFC token fell 8.4% despite the correct fight prediction. The macro modifier
(×0.55 during FTX extreme bear) separated the prediction market signal (correct) from
the token signal (negative). This is the library's most complex signal interaction and
it behaved exactly as designed.

**2. Downstream signals were more valuable than primary signals in two records.**
The State of Origin G3 record notes that the downstream NRL congestion signal was
more commercially valuable than the Origin result itself. The F1 British GP record
notes that the Ferrari token moved negatively despite Verstappen winning — confirming
that constructor tokens must be aligned to the correct entity. Both learnings are now
documented in the calibration records and inform future agent design.

**3. Narrative modifiers behaved correctly.**
The UCL Final record (narrative_modifier ×1.08 for treble pursuit) and the NBA
Finals G5 record (narrative_modifier ×1.10 for championship closeout) both confirmed
the correct direction. The NBA Finals record also documents that `narrative_active`
in a championship closeout is a POSITIVE amplifier for the favored team — not a
caution flag. This nuance is now in the calibration data.

---

## Next calibration milestone

**Target:** 50 community outcome records for dew_modifier and rivalry_form_discount
(lowest thresholds). These require cricket T20 and rugby league match submissions
respectively.

**How to submit:** See `community/calibration-data/README.md`

**When first recalibration proposal will be made:** When any modifier reaches its
minimum event threshold AND shows direction accuracy outside the target range.
Expected timeline: dependent entirely on community submission volume.

---

*Methodology: `core/calibration-framework.md`*
*Generated by: `scripts/calibration_aggregate.py --all --report`*
*MIT License · SportMind · sportmind.dev*
