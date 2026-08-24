---
name: wc2026-qf-spain-vs-belgium-2026-07-10
status: COMPLETE — post-match verified · HOME WIN · $SPAIN BTG burn #6 triggered
contributor: Internal submission
contributor-type: INTERNAL
issue: n/a — internal calibration record
description: >
  Pre-match calibration record for the 2026 FIFA World Cup Quarter-Final.
  Spain vs Belgium. SoFi Stadium, Los Angeles, USA. 2026-07-10.
  SportMind MCP server signal. Library v4.1.5. CHZ CAPITULATION ×0.70 active.
  DUAL-TOKEN record — $SPAIN (HOME) and $BELG (AWAY) both active Burn to Glory participants.
  Direction: HOME (Spain). Result: Spain 2-1 Belgium (90 min). Direction CORRECT ✓. Record 5.
---

# Calibration Record — FIFA World Cup 2026 · Quarter-Final
## Spain v Belgium · 2026-07-10

---

## Match details

```
Match:        Spain v Belgium
Competition:  FIFA World Cup 2026 — Quarter-Final
Season:       2026
Venue:        SoFi Stadium · Los Angeles · USA
Venue type:   NEUTRAL (third-party host nation — USA)
Date:         2026-07-10
Kickoff UTC:  2026-07-10T19:00:00Z
Fan tokens:   Home — $SPAIN (Spain · Chiliz Chain · verified ✓)
              Away — $BELG (Belgium · Chiliz Chain · verified ✓)
Token type:   DUAL-TOKEN
Submitted by: Internal submission
Series:       WC2026 Calibration Series · Record 5/9
PTG status:   ACTIVE — $SPAIN Burn to Glory participant · ACTIVE — $BELG Burn to Glory participant
BTG burn rate:Quarter-Final round burn rate: 5% (winner)
```

---

## Pre-match signal

*Generated: 2026-07-10 (pre-kickoff) · MCP server v3.97.89 · Library v4.1.5*

```
DIRECTION:          HOME (Spain)
RAW SCORE:          55.0
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE:     38.5
CONFIDENCE:         MEDIUM
ACTION:             HOLD (CAPITULATION gate — adjusted score 38.5 < 50.0 threshold)
SMS:                100 · HIGH_QUALITY · 5/5 layers loaded · 7 files
MACRO MODIFIER:     NEUTRAL ×1.00
COMPOSITE MODIFIER: ×0.70

OCCASION WEIGHT:    ×1.60 (Quarter-Final) — suppressed by CAPITULATION gate

FLAGS:
  CHZ_CAPITULATION_ACTIVE:          true — ×0.70 suppressor applied
  NEUTRAL_VENUE:                    true — SoFi Stadium, Los Angeles, USA
  BURN_TO_GLORY_ACTIVE_BOTH_TOKENS: true — $SPAIN and $BELG both active BTG participants
  LINEUP_CHECK_REQUIRED:            true — manual check at T-2h
  DSM_CHECK_REQUIRED:               true — manual check pre-kickoff

PRE-MATCH NOTE:
  Spain signalled HOME (administrative) at MEDIUM confidence in the first
  dual-BTG Quarter-Final of the WC2026 series. CAPITULATION ×0.70 suppresses
  the occasion weight — adjusted score 38.5 triggers the HOLD gate. Both
  $SPAIN and $BELG hold active BTG positions; loser eliminates their BTG
  run. Spain entering as tournament form leader (5 wins from 5).
  Belgium a confirmed Tier 1 fan token ($BELG). HOLD gate enforced under
  CAPITULATION regardless of occasion weight.
```

---

## Score derivation

```
Base score (SportMind pre-match):     55.0
Macro modifier (NEUTRAL ×1.00):       ×1.00 → 55.0
CHZ CAPITULATION modifier (×0.70):    ×0.70 → 38.5
Occasion weight (QF ×1.60):           noted — suppressed by CAPITULATION gate
Composite modifier applied:           ×0.70

Final adjusted score:                 38.5
ENTER threshold:                      50.0
Threshold comparison:                 38.5 < 50.0

Action gate outcome:
  Raw direction signal:               ENTER (HOME)
  CAPITULATION gate:                  ACTIVE — suppresses to HOLD
  Final action output:                HOLD
  Reason:                             Adjusted score 38.5 falls below
                                      50.0 ENTER threshold under
                                      CAPITULATION ×0.70 regime
```

---

## Primary signal drivers

```
DIRECTION CHOSEN: HOME (Spain)

POSITIVE DRIVERS:
  · Spain tournament form — 5 wins from 5 entering QF; consistent
    positional structure and goal output across WC2026 group and knockout
  · $SPAIN BTG momentum — 5 prior burns entering QF; supply reduction
    narrative active for $SPAIN holders
  · Iberian major tournament pedigree — Spain consistent knockout operators
  · First dual-BTG QF in WC2026 series — elevated fan token engagement
    context for both $SPAIN and $BELG holders

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — demand signal suppressed
  · NEUTRAL VENUE — no structural home advantage modifier applied
  · CAPITULATION gate — HOLD enforced regardless of QF occasion weight
  · $BELG BTG active — Belgium win would trigger $BELG burn; opposing
    token demand pressure present
```

---

## Signal layers applied

```
LAYER 1 — MACRO:
  CHZ regime:       CAPITULATION
  Modifier:         ×0.70
  Verdict:          HOLD gate triggered

LAYER 2 — SPORT DOMAIN:
  File:             sports/football/sport-domain-football.md
  Occasion weight:  ×1.60 (Quarter-Final)
  Venue:            NEUTRAL — SoFi Stadium, Los Angeles, USA
  Venue modifier:   NEUTRAL — no home advantage

LAYER 3 — FORM:
  Spain form:       5 wins from 5 in WC2026 — consistent output
  Belgium form:     Reached QF via knockout stages — competitive profile

LAYER 4 — H2H:
  H2H record:       Established fixture; Spain recent edge in major tournaments
  Gate:             PASS — sufficient sample

LAYER 5 — FAN TOKEN:
  $SPAIN:           Active · Chiliz Chain · verified ✓
                    BTG status: ACTIVE · 5% QF burn rate · 5 burns entering QF
  $BELG:            Active · Chiliz Chain · verified ✓
                    BTG status: ACTIVE · 5% QF burn rate · confirmed participant
  Dual-token note:  Both tokens active — dual-token modifier applicable
                    First dual-BTG QF in WC2026 series
```

---

## PTG / Burn to Glory status

```
PTG ROUND:     Quarter-Final · burn rate 5%
WINNER BURN:   5% of winner's treasury holdings burned permanently
LOSER OUTCOME: BTG run ends · no burn · eliminated

$SPAIN BTG HISTORY (pre-match):
  Group ×3 (1%) + R16 ×1 (2.5%) + extra burn ×1 = 5 burns entering QF
  Note: source record lists "extra burn ×1" — preserved as stated

$BELG BTG HISTORY (pre-match):
  Confirmed Burn to Glory participant · 5% QF rate
  Eliminated on loss — BTG run terminated

CHZ REGIME INTERACTION:
  Burns execute regardless of CHZ macro regime.
  Supply reduction is structural — price impact dampened by macro.
```

---

## Result — verified

```
ACTUAL RESULT:       Spain 2 — Belgium 1
WINNING TEAM:        Spain
SCORE:               2-1 (full time)
EXTRA TIME:          NO
PENALTIES:           NO

DIRECTION CORRECT:   YES — HOME (Spain) ✓
  SportMind predicted: HOME (Spain)
  Actual result:       Spain won 2-1
  Direction verdict:   CORRECT

ACTION OUTCOME:      HOLD — gate behaviour CORRECT ✓
  CAPITULATION gate correctly blocked ENTER on HOME signal.
  Adjusted score 38.5 < 50.0 threshold. HOLD preserved.

CALIBRATION VERDICT: CORRECT · HOLD gate CORRECT ✓
```

---

## Supply event outcome

```
$SPAIN BTG:
  Supply event:  BURN TRIGGERED
  Burn rate:     5% (Quarter-Final rate)
  Burn number:   6 (cumulative WC2026)
  Burn history:  Group ×3 (1%) + R16 ×1 (2.5%) + extra ×1 + QF ×1 (5%)
  Next:          Spain advance to Semi-Final · next burn rate 7.5% if Spain WIN SF
  Verify:        chiliscan.com

$BELG BTG:
  Supply event:  NOT TRIGGERED — Belgium eliminated
  BTG run:       TERMINATED at Quarter-Final stage
  Status:        No further Burn to Glory events for $BELG in WC2026
```

---

## Post-match notes

```
MATCH CHARACTER:
  Spain won 2-1 in 90 minutes. Dual-BTG fixture resolved in Spain's favour.
  First dual-BTG QF in the WC2026 series. $BELG BTG run terminated.
  $SPAIN advances to Semi-Final with burn #6 triggered.

WHAT THE SIGNAL GOT RIGHT:
  · CAPITULATION gate correctly applied — HOLD preserved ✓
  · MEDIUM confidence appropriate — competitive QF, decided by one goal
  · Dual-token demand mechanics correctly identified
  · BTG supply event correctly flagged for both tokens

WHAT THE SIGNAL GOT WRONG:
  · N/A — direction correct
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MEDIUM confidence at raw 55.0 was appropriate for a QF between two
dual-BTG nations. Spain's structural edge was present but Belgium were
competitive — match decided by a single goal. CAPITULATION ×0.70
compressing to 38.5 correctly framed this as a HOLD position.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓

FUTURE CALIBRATION NOTE:
  First dual-BTG QF record in the WC2026 series. Establishes the pattern
  for dual-token knockout records under CAPITULATION. $BELG contract
  reference should be checked in library for any subsequent $BELG records.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status:    ACTIVE
  Post-match resolution: ×0.70 applied correctly throughout.
                         BTG supply events executed regardless of regime.

FLAG: NEUTRAL_VENUE
  Pre-match status:    ACTIVE
  Post-match resolution: No home advantage conferred. HOME designation
                         administrative only. SoFi Stadium, Los Angeles, USA.

FLAG: BURN_TO_GLORY_ACTIVE_BOTH_TOKENS
  Pre-match status:    ACTIVE — $SPAIN and $BELG both holding active BTG positions
  Post-match resolution: $SPAIN burn #6 triggered at 5% QF rate.
                         $BELG BTG run terminated — eliminated at QF.
```

---

## Agent rules engaged

```
TFM6 Gate 1:         Pre-kickoff submission ✓
CHZ regime applied:  CAPITULATION ×0.70 applied before output ✓
Token verified:      $SPAIN verified on Chiliz Chain before signal ✓
Token verified:      $BELG verified on Chiliz Chain before signal ✓
HOLD gate:           Triggered correctly under CAPITULATION regime ✓
PTG verified:        $SPAIN BTG burn #6 confirmed at 5% QF rate ✓
                     $BELG BTG run terminated on elimination ✓
PATH_2 N/A:          $SPAIN is not a PATH_2 token ($AFC only) ✓
                     $BELG is not a PATH_2 token ($AFC only) ✓
Neutral venue noted: No home advantage modifier applied ✓
Series noted:        WC2026 Calibration Series 5/9 ✓
Dual-token noted:    Dual-token modifier applicable — both tokens active ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1c Token Registry | ACTIVE |
| 2. Reasoning | 2b Probabilistic · 2c Multi-Signal · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context (Quarter-Final) | ACTIVE |
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
  · fan-token/holder-tax-framework.md (Belgium Type A entry)
  · macro/regulatory/belgium.md
  · fan-token/national-profiles/spain.md
  · fan-token/national-profiles/arg.md
  · sports/football/sport-domain-football.md
  · core/h2h-framework.md
```

---

## Source and verification

```
Signal source:   SportMind MCP · sportmind_pre_match
MCP server:      v3.97.89
Signal generated:2026-07-10 (pre-kickoff)
Library version: v4.1.5
Match date:      2026-07-10
Submitted by:    Internal submission
Result source:   FIFA.com · ESPN · BBC Sport
Result verified: 2026-07-10

PTG verification: chiliscan.com — $SPAIN burn #6 confirmed
                  $BELG BTG run terminated on elimination
```

---

*SportMind v4.6.28 · MIT License · sportmind.dev*
*WC2026 Calibration Series 5/9 · part of the 137-record SportMind calibration base*
*STATUS: COMPLETE — direction CORRECT ✓ · HOLD gate CORRECT ✓*
*$SPAIN BTG burn #6 triggered at 5% QF rate*

© 2026 SportMind
