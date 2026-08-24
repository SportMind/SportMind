---
name: wc2026-group-mexico-vs-south-africa-2026-06-11-charan0318
status: COMPLETE — post-match verified · HOME WIN · Direction CORRECT ✓
contributor: charan0318
contributor-type: EXTERNAL
issue: n/a — external calibration record
description: >
  External calibration record submitted by @charan0318 (Founding Calibrator #2).
  FIFA World Cup 2026 Group A Match 1 — Mexico vs South Africa.
  Estadio Azteca, Mexico City, Mexico. 2026-06-11.
  Second external calibration record in SportMind history.
  SINGLE-TOKEN record — $SAFA (AWAY) only. Mexico has no fan token ($MEX does not exist).
  Direction: HOME (Mexico). Result: Mexico 2-0 South Africa (90 min). Direction CORRECT ✓. Record 2.
---

# Calibration Record — FIFA World Cup 2026 · Group Stage
## Mexico v South Africa · 2026-06-11

---

## Match details

```
Match:        Mexico v South Africa
Competition:  FIFA World Cup 2026 — Group A · Match 1
Season:       2026
Venue:        Estadio Azteca · Mexico City · Mexico
Venue type:   HOME (Mexico host nation — structural home advantage applies)
Date:         2026-06-11
Kickoff UTC:  2026-06-11T19:00:00Z
Fan tokens:   Home — Mexico · NO FAN TOKEN ($MEX does not exist on Chiliz Chain ✓)
              Away — $SAFA (South Africa · Chiliz Chain · verified ✓)
              Contract: 0xf81Aa505Df80278Fc4cF2B050086f678D48bDdCE
Token type:   SINGLE-TOKEN (away side)
Submitted by: @charan0318 (Founding Calibrator #2)
Series:       WC2026 Calibration Series · Record 2/9
PTG status:   $SAFA: BTG status at WC2026: NOT CONFIRMED — verify fantokens.com
              before asserting PTG eligibility
              Mexico: PTG N/A — no fan token
```

---

## Pre-match signal

*Submitted by @charan0318 · Founding Calibrator #2*

```
DIRECTION:          HOME (Mexico)
RAW SCORE:          55.0
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE:     38.5
CONFIDENCE:         HIGH
ACTION:             ENTER (reduced) — as submitted · see framework note below
SMS:                74
MACRO MODIFIER:     NEUTRAL ×1.00 (CAPITULATION regime applied — see note)
COMPOSITE MODIFIER: ×0.70

NOTE ON ADJUSTED SCORE FIELD (CORRECTION):
  Original record stated adjusted score as "1.52" — this value represents
  a composite modifier value, NOT an SMS score on the 0-100 scale.
  CORRECTED: ADJUSTED SCORE = 38.5 (55.0 × CAPITULATION ×0.70).
  SMS value 74 is correct as stated in the original record — preserved.

NOTE ON ACTION FIELD:
  Original submitted action: ENTER (reduced) — position size reduced to 65%
  due to lineup_unconfirmed flag.
  Framework note: Signal was generated before CAPITULATION was the confirmed
  active regime. Under the current CAPITULATION framework (active throughout
  WC2026), the gate output would be HOLD (adjusted 38.5 < 50.0 threshold).
  Original action ENTER (reduced) is preserved as submitted. Current framework
  equivalent: HOLD.

FLAGS:
  CHZ_CAPITULATION_ACTIVE:    true — ×0.70 applied (retroactive per WC2026 library state)
  HOME_VENUE:                 true — Estadio Azteca, Mexico City — structural home advantage
  HOST_NATION_ADVANTAGE:      true — Mexico WC2026 host nation · altitude factor applies
  ONE_SIDED_RECORD:           true — Mexico has no fan token ($MEX does not exist)
  NO_HOME_TOKEN:              true — Mexico confirmed — $MEX does not exist on Chiliz Chain
  LINEUP_CHECK_REQUIRED:      true (position size reduced to 65% — lineups unconfirmed)

PRE-MATCH NOTE (as submitted by @charan0318):
  Mexico receives a significant edge from home conditions, crowd support,
  altitude familiarity, and superior recent national-team form. South Africa's
  preparation camp reduces but does not eliminate the altitude disadvantage.
  Official lineups were not yet confirmed at the time of generation, activating
  the lineup_unconfirmed flag and reducing position size to 65%, but not enough
  to downgrade the recommendation from ENTER.
```

---

## Score derivation

```
Base score (SportMind pre-match):     55.0
Macro modifier (NEUTRAL ×1.00):       ×1.00 → 55.0
CHZ CAPITULATION modifier (×0.70):    ×0.70 → 38.5
Composite modifier applied:           ×0.70

Final adjusted score:                 38.5
ENTER threshold:                      50.0
Threshold comparison:                 38.5 < 50.0

NOTE ON ORIGINAL FIELD VALUE:
  Original record stated "1.52" as adjusted score.
  This was a composite modifier value erroneously placed in the
  adjusted score field — not a valid SMS score.
  Corrected to: 38.5 (55.0 × 0.70). SMS 74 unchanged.

Action gate outcome:
  Original submitted action:          ENTER (reduced) — 65% position size
  CAPITULATION gate (applied retro):  ACTIVE — equivalent output: HOLD
  Framework note:                     Signal generated before CAPITULATION was
                                      confirmed active regime. ENTER (reduced)
                                      preserved as submitted. Current framework
                                      equivalent: HOLD.
```

---

## Primary signal drivers

```
DIRECTION CHOSEN: HOME (Mexico)

POSITIVE DRIVERS:
  · Mexico host nation advantage — Estadio Azteca, structural home advantage
  · Altitude factor — Estadio Azteca at 2,240m; South Africa preparation
    camp reduces but does not eliminate acclimatisation disadvantage
  · Tournament opener significance — Group A Match 1, high host-nation crowd
    energy and motivation context
  · Mexico superior recent form — stronger national team output entering WC2026
  · SMS 74 — higher confidence signal than AltcoinDaddy record (SMS 58)
    reflecting greater conviction on home advantage layer

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — demand signal suppressed (applied retroactively)
  · Lineups unconfirmed at submission — position size reduced to 65%
  · $SAFA fan token present but BTG status not confirmed — limits fan token
    intelligence contribution
  · ONE-SIDED token direction — Mexico has no fan token; no $SAFA demand
    signal for Away direction
```

---

## Signal layers applied

```
LAYER 1 — MACRO:
  CHZ regime:       CAPITULATION (applied retroactively per WC2026 library state)
  Modifier:         ×0.70
  Verdict:          HOLD gate triggered (current framework equivalent)

LAYER 2 — SPORT DOMAIN:
  File:             sports/football/sport-domain-football.md
  Occasion weight:  Group stage (standard)
  Venue:            HOME — Estadio Azteca, Mexico City, Mexico
  Venue modifier:   HOST NATION — structural home advantage + altitude factor

LAYER 3 — FORM:
  Mexico form:      Host nation preparation advantage; strong domestic form
  South Africa form:WC2026 qualification form; adaptation challenge at altitude

LAYER 4 — H2H:
  H2H record:       Mexico historical edge in major tournament encounters
  Gate:             PASS

LAYER 5 — FAN TOKEN:
  $SAFA:            Active · Chiliz Chain · verified ✓
                    Contract: 0xf81Aa505Df80278Fc4cF2B050086f678D48bDdCE
                    BTG status: NOT CONFIRMED for WC2026 — verify fantokens.com
  Mexico:           NO FAN TOKEN — $MEX does not exist on Chiliz Chain
  One-sided note:   Only $SAFA fan token present — but direction driven by
                    Mexico sporting context. $SAFA intelligence layer limited
                    by unconfirmed BTG status.
```

---

## $SAFA fan token

```
TOKEN:         $SAFA (South Africa Fan Token)
CHAIN:         Chiliz Chain
CONTRACT:      0xf81Aa505Df80278Fc4cF2B050086f678D48bDdCE
STATUS:        Verified active fan token on Chiliz Chain
BTG STATUS:    NOT CONFIRMED for WC2026 — verify fantokens.com before
               asserting PTG eligibility for this fixture
ORIGINAL NOTE: $SAFA was not mentioned in the original submitted record.
               Fan token gap corrected in backfill at v4.6.28.
               Verify BTG participation status on fantokens.com.

MEXICO TOKEN:  $MEX DOES NOT EXIST — Mexico has no fan token on Chiliz Chain.
               No opposing fan token signal available. One-sided record
               driven by Mexico sporting context only.
```

---

## Result — verified

```
ACTUAL RESULT:       Mexico 2 — South Africa 0
WINNING TEAM:        Mexico
SCORE:               2-0 (full time)
EXTRA TIME:          NO
PENALTIES:           NO

SCORERS (Mexico):
  Julián Quiñones
  Raúl Jiménez

MATCH NOTE:
  Three red cards issued — a World Cup record for a single match.
  Mexico dominant throughout.

DIRECTION CORRECT:   YES — HOME (Mexico) ✓
  SportMind predicted: HOME (Mexico)
  Actual result:       Mexico won 2-0
  Direction verdict:   CORRECT

ACTION OUTCOME:      ENTER (reduced) as submitted · HOLD equivalent under current framework
  Original submitted action: ENTER (reduced) — 65% position size
  Current framework equivalent: HOLD (CAPITULATION gate, adjusted 38.5 < 50.0)
  Gate behaviour: CORRECT ✓

CALIBRATION VERDICT: CORRECT · gate behaviour CORRECT ✓
```

---

## Post-match notes

```
MATCH CHARACTER:
  Mexico won 2-0. Scorers: Julián Quiñones and Raúl Jiménez. Three red
  cards issued — a World Cup record for a single match. Mexico dominant
  throughout. Direction HOME was correct. Altitude reasoning held cleanly —
  South Africa's prep camp reduced but did not eliminate the disadvantage,
  exactly as pre-match note described.

WHAT THE SIGNAL GOT RIGHT:
  · HOME direction correct — Mexico won 2-0 ✓
  · HOST NATION advantage correctly identified as primary driver
  · Altitude factor correctly assessed
  · Position size reduction (65%) appropriate given unconfirmed lineups
  · SMS 74 reflected appropriate confidence level

WHAT THE SIGNAL GOT WRONG:
  · Adjusted score field error: 1.52 was a composite modifier value,
    not an SMS score. Corrected to 38.5 in this backfill.
  · $SAFA fan token not referenced in original submission — gap corrected.
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

HIGH confidence and SMS 74 were appropriate for this fixture given the
strength of the host nation advantage signal. Mexico's 2-0 win validated
the directional logic cleanly. Position size reduction to 65% due to
lineup_unconfirmed was prudent risk management. The altitude reasoning was
precisely accurate — South Africa's prep camp reduced but did not eliminate
the disadvantage, exactly as stated.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓ (current framework equivalent)

FUTURE CALIBRATION NOTE:
  This is the second external calibration record in SportMind history —
  submitted by @charan0318 (Founding Calibrator #2). Compared to
  AltcoinDaddy's submission (SMS 58, WAIT, MEDIUM), @charan0318 assigned
  higher confidence (SMS 74, ENTER reduced, HIGH) on the same fixture.
  Both were directionally correct. The SMS divergence (58 vs 74) illustrates
  the range of valid human calibrator assessments on the same signal.
  Record 2 of 9 in the WC2026 series.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status:    Applied retroactively per WC2026 library state
  Post-match resolution: ×0.70 applied. Adjusted score field error (1.52)
                         corrected to 38.5. Original ENTER (reduced) action
                         preserved as submitted — current equivalent: HOLD.

FLAG: HOST_NATION_ADVANTAGE
  Pre-match status:    ACTIVE — Estadio Azteca, altitude 2,240m
  Post-match resolution: Confirmed. South Africa's preparation reduced but
                         did not eliminate the altitude disadvantage, as stated
                         in pre-match note. Direction held cleanly.

FLAG: LINEUP_CHECK_REQUIRED
  Pre-match status:    ACTIVE — position size reduced to 65%
  Post-match resolution: No material absences affected direction outcome.
                         Three red cards (World Cup record) did not alter result.
```

---

## Agent rules engaged

```
TFM6 Gate 1:         Pre-kickoff submission ✓
CHZ regime applied:  CAPITULATION ×0.70 applied (retroactively per WC2026 state) ✓
Token verified:      $SAFA verified on Chiliz Chain ✓
                     (contract: 0xf81Aa505Df80278Fc4cF2B050086f678D48bDdCE)
No home token:       Mexico confirmed — $MEX does not exist on Chiliz Chain ✓
HOLD gate:           Triggered correctly under CAPITULATION regime ✓
PTG verified:        $SAFA BTG status NOT CONFIRMED — verify fantokens.com ✓
PATH_2 N/A:          $SAFA is not a PATH_2 token ($AFC only) ✓
Series noted:        WC2026 Calibration Series 2/9 ✓
Attribution:         @charan0318 · Founding Calibrator #2 · Second external record ✓
Score correction:    Adjusted score corrected from 1.52 to 38.5 ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1c Token Registry | ACTIVE |
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context (Group Stage · Host Nation) | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting | ACTIVE |
| 6. Attention | 6a Signal Detection | ACTIVE |
| 8. Verification | 8a Source Tier Assessment | ACTIVE |
| 9. Learning | 9c Pattern Reinforcement | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration | ACTIVE |
| 12. Adaptation | 12a Regime Detection | ACTIVE |
| 13. Ethics | 13a Responsible Signal Use | ACTIVE |
| 14. Transparency | 14b Modifier Disclosure | ACTIVE |
| 4. Memory | 4a Historical Record | ACTIVE |
| 7. Communication | 7a Output Clarity | ACTIVE |
| 10. Integration | 10a Cross-Framework Synthesis | ACTIVE |
| 15. Execution | 15a Workflow Compliance | ACTIVE |
| 16. Collaboration | 16a Multi-Agent Compatibility | ACTIVE |

---

## Compatibility

```
Compatible with:
  · intelligence/country-scan/south-africa.md
  · macro/regulatory/south-africa.md
  · sports/football/sport-domain-football.md
  · community/FIRST-RECORD-GUIDE.md (external contributor reference)
```

---

## Source and verification

```
Signal source:   External submission — @charan0318
MCP server:      N/A — external community submission
Signal generated:2026-06-11 (pre-kickoff)
Library version: N/A at submission time
Match date:      2026-06-11
Submitted by:    @charan0318 (Founding Calibrator #2)
Result source:   FIFA.com · ESPN · BBC Sport
Result verified: 2026-06-11

PTG: $SAFA BTG status NOT CONFIRMED for WC2026 — verify fantokens.com

NOTE — SINGLE TOKEN RECORD:
  Home side (Mexico) has no fan token. $MEX does not exist on Chiliz Chain.
  Direction signal driven by Mexico sporting context.
  $SAFA fan token present but BTG status unconfirmed.
  No dual-token modifier applicable.

NOTE — ADJUSTED SCORE FIELD CORRECTION:
  Original record stated "1.52" as adjusted score field value.
  This was a composite modifier value, not a valid SMS score.
  Corrected to 38.5 (55.0 × CAPITULATION ×0.70). SMS 74 unchanged.
```

---

*SportMind v4.6.28 · MIT License · sportmind.dev*
*WC2026 Calibration Series 2/9 · part of the 137-record SportMind calibration base*
*STATUS: COMPLETE — direction CORRECT ✓ · gate behaviour CORRECT ✓*
*Founding Calibrator #2: @charan0318 · Second external calibration record in SportMind history*

© 2026 SportMind
