---
name: wc2026-group-mexico-vs-south-africa-2026-06-11-altcoindaddy
status: COMPLETE — post-match verified · HOME WIN · Direction CORRECT ✓
contributor: AltcoinDaddy
contributor-type: EXTERNAL
issue: n/a — external calibration record
description: >
  External calibration record submitted by @AltcoinDaddy (Founding Calibrator #1).
  FIFA World Cup 2026 Group A Match 1 — Mexico vs South Africa.
  Estadio Azteca, Mexico City, Mexico. 2026-06-11.
  First external calibration record in SportMind history.
  SINGLE-TOKEN record — $SAFA (AWAY) only. Mexico has no fan token ($MEX does not exist).
  Direction: HOME (Mexico). Result: Mexico 2-0 South Africa (90 min). Direction CORRECT ✓. Record 1.
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
Submitted by: @AltcoinDaddy (Founding Calibrator #1)
Recorded at:  2026-06-10T20:16:14Z
Series:       WC2026 Calibration Series · Record 1/9
PTG status:   $SAFA: BTG status at WC2026: NOT CONFIRMED — verify fantokens.com
              before asserting PTG eligibility
              Mexico: PTG N/A — no fan token
```

---

## Pre-match signal

*Submitted by @AltcoinDaddy · Founding Calibrator #1 · Recorded 2026-06-10T20:16:14Z*

```
DIRECTION:          HOME (Mexico)
RAW SCORE:          55.0
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE:     38.5
CONFIDENCE:         MEDIUM
ACTION:             HOLD (CAPITULATION gate — adjusted score 38.5 < 50.0 threshold)
SMS:                58
MACRO MODIFIER:     NEUTRAL ×1.00 (CAPITULATION regime applied — see note)
COMPOSITE MODIFIER: ×0.70

NOTE ON ORIGINAL SIGNAL:
  Original record showed adjusted score 61.0 and action WAIT.
  This was generated before CAPITULATION was the confirmed active regime.
  CAPITULATION ×0.70 is applied retroactively per library state active
  throughout WC2026. Adjusted score: 55.0 × 0.70 = 38.5. Action: HOLD.
  Original action WAIT is preserved as submitted. Under the current
  CAPITULATION framework, the equivalent gate output is HOLD.
  SMS 58 preserved as submitted.

FLAGS:
  CHZ_CAPITULATION_ACTIVE:    true — ×0.70 applied (retroactive per WC2026 library state)
  HOME_VENUE:                 true — Estadio Azteca, Mexico City — structural home advantage
  HOST_NATION_ADVANTAGE:      true — Mexico WC2026 host nation · altitude factor applies
  ONE_SIDED_RECORD:           true — Mexico has no fan token ($MEX does not exist)
  NO_HOME_TOKEN:              true — Mexico confirmed — $MEX does not exist on Chiliz Chain
  LINEUP_CHECK_REQUIRED:      true (signal produced before lineups confirmed)

PRE-MATCH NOTE (as submitted by @AltcoinDaddy):
  Mexico gets the directional edge on host-context and match-importance
  weighting. Estadio Azteca altitude (2,240m) creates a structural
  disadvantage for South Africa's preparation camp — reduced but not
  eliminated. Signal generated before confirmed lineups; confidence
  stays MEDIUM and the action remains WAIT rather than full-strength entry.
  Host home advantage in a high-importance tournament opener is the
  primary signal driver.
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

Action gate outcome:
  Original submitted action:          WAIT (pre-CAPITULATION framework)
  CAPITULATION gate (applied retro):  ACTIVE — equivalent output: HOLD
  Framework note:                     Signal generated before CAPITULATION was
                                      confirmed active regime. Original action
                                      WAIT preserved as submitted. Current
                                      framework equivalent: HOLD.
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

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — demand signal suppressed (applied retroactively)
  · Lineups unconfirmed at submission — reduces confidence from potential HIGH
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
  Verdict:          HOLD gate triggered

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

DIRECTION CORRECT:   YES — HOME (Mexico) ✓
  SportMind predicted: HOME (Mexico)
  Actual result:       Mexico won 2-0
  Direction verdict:   CORRECT

ACTION OUTCOME:      WAIT (as submitted) — HOLD equivalent under current framework
  Original submitted action: WAIT
  Current framework equivalent: HOLD (CAPITULATION gate, adjusted 38.5 < 50.0)
  Gate behaviour: CORRECT ✓

CALIBRATION VERDICT: CORRECT · gate behaviour CORRECT ✓
```

---

## Post-match notes

```
MATCH CHARACTER:
  Mexico won 2-0. HOME direction was correct. WAIT stance was appropriate —
  signal produced before confirmed lineups and without a full live multi-layer
  check. Direction and reasoning both verified correct. Altitude reasoning held
  cleanly — South Africa's prep camp reduced but did not eliminate the
  disadvantage, exactly as pre-match note described.

WHAT THE SIGNAL GOT RIGHT:
  · HOME direction correct — Mexico won 2-0 ✓
  · MEDIUM confidence appropriate given unconfirmed lineups at submission
  · Host nation advantage and altitude factor correctly identified
  · WAIT action appropriate given information available at submission time

WHAT THE SIGNAL GOT WRONG:
  · N/A — direction correct
  · Original adjusted score 61.0 was a pre-CAPITULATION calculation;
    correct adjusted score under current framework is 38.5
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MEDIUM confidence was appropriate — @AltcoinDaddy correctly identified the
host advantage and altitude factor as primary drivers but appropriately
held back from HIGH confidence given unconfirmed lineups. The WAIT action
was correct for the information state at submission time. Mexico's 2-0 win
validated the directional logic cleanly.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓ (current framework equivalent)

FUTURE CALIBRATION NOTE:
  This is the first external calibration record in SportMind history —
  submitted by @AltcoinDaddy (Founding Calibrator #1) before lineups were
  confirmed. The submission demonstrates that pre-lineup directional signals
  can be correct even at reduced confidence. $SAFA fan token gap (not
  referenced in original) corrected in this backfill. Record 1 of 9.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status:    Applied retroactively per WC2026 library state
  Post-match resolution: ×0.70 applied. Original adjusted score 61.0
                         corrected to 38.5 for framework consistency.
                         Original WAIT action preserved as submitted.

FLAG: HOST_NATION_ADVANTAGE
  Pre-match status:    ACTIVE — Estadio Azteca, altitude 2,240m
  Post-match resolution: Confirmed. South Africa's preparation reduced but
                         did not eliminate the altitude disadvantage, as stated
                         in pre-match note. Direction held cleanly.

FLAG: LINEUP_CHECK_REQUIRED
  Pre-match status:    ACTIVE — signal produced before lineups confirmed
  Post-match resolution: No material absences affected direction outcome.
```

---

## Agent rules engaged

```
TFM6 Gate 1:         Pre-kickoff submission ✓ (recorded 2026-06-10T20:16:14Z)
CHZ regime applied:  CAPITULATION ×0.70 applied (retroactively per WC2026 state) ✓
Token verified:      $SAFA verified on Chiliz Chain ✓
                     (contract: 0xf81Aa505Df80278Fc4cF2B050086f678D48bDdCE)
No home token:       Mexico confirmed — $MEX does not exist on Chiliz Chain ✓
HOLD gate:           Triggered correctly under CAPITULATION regime ✓
PTG verified:        $SAFA BTG status NOT CONFIRMED — verify fantokens.com ✓
PATH_2 N/A:          $SAFA is not a PATH_2 token ($AFC only) ✓
Series noted:        WC2026 Calibration Series 1/9 ✓
Attribution:         @AltcoinDaddy · Founding Calibrator #1 · First external record ✓
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
Signal source:   External submission — @AltcoinDaddy
MCP server:      N/A — external community submission
Signal generated:2026-06-10T20:16:14Z
Library version: N/A at submission time
Match date:      2026-06-11
Submitted by:    @AltcoinDaddy (Founding Calibrator #1)
Result source:   livescore.com — https://www.livescore.com/en/football/international/world-cup-2026/mexico-vs-south-africa/1417909/
Result verified: 2026-06-11

PTG: $SAFA BTG status NOT CONFIRMED for WC2026 — verify fantokens.com

NOTE — SINGLE TOKEN RECORD:
  Home side (Mexico) has no fan token. $MEX does not exist on Chiliz Chain.
  Direction signal driven by Mexico sporting context.
  $SAFA fan token present but BTG status unconfirmed.
  No dual-token modifier applicable.
```

---

*SportMind v4.6.28 · MIT License · sportmind.dev*
*WC2026 Calibration Series 1/9 · part of the 137-record SportMind calibration base*
*STATUS: COMPLETE — direction CORRECT ✓ · gate behaviour CORRECT ✓*
*Founding Calibrator #1: @AltcoinDaddy · First external calibration record in SportMind history*

© 2026 SportMind
