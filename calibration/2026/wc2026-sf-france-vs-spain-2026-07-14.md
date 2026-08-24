---
name: wc2026-sf-france-vs-spain-2026-07-14
status: COMPLETE — post-match verified · AWAY WIN · $SPAIN BTG burn #7 triggered
contributor: Internal submission
contributor-type: INTERNAL
issue: n/a — internal calibration record
description: >
  Pre-match calibration record for the 2026 FIFA World Cup Semi-Final.
  France vs Spain. AT&T Stadium, Arlington, Texas, USA. 2026-07-14.
  SportMind MCP server signal. Library v4.1.8. CHZ CAPITULATION ×0.70 active.
  SINGLE-TOKEN record — $SPAIN (AWAY) only. France has no fan token.
  Direction: AWAY (Spain). Result: France 0-2 Spain (90 min). Direction CORRECT ✓. Record 7.
---

# Calibration Record — FIFA World Cup 2026 · Semi-Final
## France v Spain · 2026-07-14

---

## Match details

```
Match:        France v Spain
Competition:  FIFA World Cup 2026 — Semi-Final
Season:       2026
Venue:        AT&T Stadium · Arlington, Texas · USA
Venue type:   NEUTRAL (third-party host nation — USA)
Date:         2026-07-14
Kickoff UTC:  2026-07-14T19:00:00Z
Fan tokens:   Home — France · NO FAN TOKEN (confirmed — no Chiliz fan token ✓)
              Away — $SPAIN (Spain · Chiliz Chain · verified ✓)
Token type:   SINGLE-TOKEN (away side)
Submitted by: Internal submission
Series:       WC2026 Calibration Series · Record 7/9
PTG status:   ACTIVE — $SPAIN Burn to Glory participant
              France: PTG N/A — no fan token
BTG burn rate:Semi-Final round burn rate: 7.5% (winner)
```

---

## Pre-match signal

*Generated: 2026-07-14 (pre-kickoff) · MCP server v3.97.89 · Library v4.1.8*

```
DIRECTION:          AWAY (Spain)
RAW SCORE:          55.0
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE:     38.5
CONFIDENCE:         MEDIUM
ACTION:             HOLD (CAPITULATION gate — adjusted score 38.5 < 50.0 threshold)
SMS:                100 · HIGH_QUALITY · 5/5 layers loaded
MACRO MODIFIER:     NEUTRAL ×1.00
COMPOSITE MODIFIER: ×0.70

OCCASION WEIGHT:    ×1.80 (Semi-Final) — suppressed by CAPITULATION gate

FLAGS:
  CHZ_CAPITULATION_ACTIVE:          true — ×0.70 suppressor applied
  NEUTRAL_VENUE:                    true — AT&T Stadium, Arlington, Texas, USA
  BURN_TO_GLORY_ACTIVE_AWAY_ONLY:   true — $SPAIN (AWAY) only
  ONE_SIDED_RECORD:                 true — France has no fan token
  NO_HOME_TOKEN:                    true — France confirmed — no Chiliz fan token
  LINEUP_CHECK_REQUIRED:            true — manual check at T-2h
  DSM_CHECK_REQUIRED:               true — manual check pre-kickoff

PRE-MATCH NOTE:
  Spain signalled AWAY (administrative) at MEDIUM confidence. No structural
  away disadvantage modifier at neutral venue. CAPITULATION ×0.70 suppresses
  occasion weight — adjusted score 38.5 triggers the HOLD gate. France has no
  fan token: this is a one-sided record validating $SPAIN intelligence only.
  $SPAIN BTG burn #7 contingent on Spain win at 7.5% SF rate. HOLD gate
  enforced under CAPITULATION regardless of occasion weight or $SPAIN BTG
  momentum. ONE-SIDED RECORD: only $SPAIN fan token intelligence validated.
```

---

## Score derivation

```
Base score (SportMind pre-match):     55.0
Macro modifier (NEUTRAL ×1.00):       ×1.00 → 55.0
CHZ CAPITULATION modifier (×0.70):    ×0.70 → 38.5
Occasion weight (SF ×1.80):           noted — suppressed by CAPITULATION gate
Composite modifier applied:           ×0.70

Final adjusted score:                 38.5
ENTER threshold:                      50.0
Threshold comparison:                 38.5 < 50.0

Action gate outcome:
  Raw direction signal:               ENTER (AWAY)
  CAPITULATION gate:                  ACTIVE — suppresses to HOLD
  Final action output:                HOLD
  Reason:                             Adjusted score 38.5 falls below
                                      50.0 ENTER threshold under
                                      CAPITULATION ×0.70 regime
```

---

## Primary signal drivers

```
DIRECTION CHOSEN: AWAY (Spain)

POSITIVE DRIVERS:
  · Spain tournament dominance — 6 wins from 6 entering SF; consistent
    positional output and goal superiority across WC2026
  · $SPAIN BTG momentum — 6 prior burns entering SF; 7.5% supply event
    on win creates elevated on-chain demand catalyst
  · Spain structural superiority at neutral venue — no AWAY disadvantage
    modifier applicable; neutral site removes home bias
  · Major tournament track record — Spain consistent knockout operators

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — demand signal suppressed
  · NEUTRAL VENUE — no structural home advantage for France; no AWAY
    disadvantage for Spain
  · CAPITULATION gate — HOLD enforced regardless of SF occasion weight
  · ONE-SIDED RECORD — France has no fan token; no opposing signal
    or hedge available
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
  Occasion weight:  ×1.80 (Semi-Final)
  Venue:            NEUTRAL — AT&T Stadium, Arlington, Texas, USA
  Venue modifier:   NEUTRAL — no home advantage; no away disadvantage

LAYER 3 — FORM:
  Spain form:       6 wins from 6 in WC2026 — dominant output
  France form:      Strong SF progression; no fan token intelligence available

LAYER 4 — H2H:
  H2H record:       Established major tournament fixture
  Gate:             PASS — sufficient sample; Spain recent edge

LAYER 5 — FAN TOKEN:
  $SPAIN:           Active · Chiliz Chain · verified ✓
                    BTG status: ACTIVE · 7.5% SF burn rate · 6 burns entering SF
  France:           NO FAN TOKEN — no signal · no opposing exposure available
  One-sided note:   Only $SPAIN fan token intelligence validated in this fixture
```

---

## PTG / Burn to Glory status

```
PTG ROUND:     Semi-Final · burn rate 7.5%
WINNER BURN:   7.5% of $SPAIN treasury holdings burned permanently (on Spain win)
LOSER OUTCOME: $SPAIN BTG run ends · no burn (on France win)

$SPAIN BTG HISTORY (pre-match):
  Group ×3 (1%) + R16 ×1 (2.5%) + QF ×1 (5%) + extra burn ×1
  = 6 burns entering SF
  Note: source record lists "extra burn ×1" — preserved as stated

France BTG: NOT APPLICABLE — France has no fan token

CHZ REGIME INTERACTION:
  Burns execute regardless of CHZ macro regime.
  Supply reduction is structural — price impact dampened by macro.
```

---

## Result — verified

```
ACTUAL RESULT:       France 0 — Spain 2
WINNING TEAM:        Spain
SCORE:               0-2 (full time)
EXTRA TIME:          NO
PENALTIES:           NO

DIRECTION CORRECT:   YES — AWAY (Spain) ✓
  SportMind predicted: AWAY (Spain)
  Actual result:       Spain won 2-0
  Direction verdict:   CORRECT

ACTION OUTCOME:      HOLD — gate behaviour CORRECT ✓
  CAPITULATION gate correctly blocked ENTER on AWAY signal.
  Adjusted score 38.5 < 50.0 threshold. HOLD preserved.

CALIBRATION VERDICT: CORRECT · HOLD gate CORRECT ✓
```

---

## Supply event outcome

```
$SPAIN BTG:
  Supply event:  BURN TRIGGERED
  Burn rate:     7.5% (Semi-Final rate)
  Burn number:   7 (cumulative WC2026)
  Burn history:  Group ×3 (1%) + R16 ×1 (2.5%) + QF ×1 (5%) + extra ×1 + SF ×1 (7.5%)
  Next:          Spain advance to Final vs Argentina · next burn rate 10% if Spain WIN Final
  Verify:        chiliscan.com

France:
  Supply event:  NOT APPLICABLE — no fan token
```

---

## Post-match notes

```
MATCH CHARACTER:
  Spain won 2-0 at neutral venue. AWAY win delivered convincingly — not
  a tight match. Spain dominant. France eliminated at SF stage. $SPAIN
  burn #7 triggered — Spain confirmed in Final vs Argentina. Dual-token
  Final confirmed: $SPAIN vs $ARG.

WHAT THE SIGNAL GOT RIGHT:
  · CAPITULATION gate correctly applied — HOLD preserved ✓
  · MEDIUM confidence appropriate — SF between top nations
  · ONE-SIDED RECORD correctly identified — France has no fan token
  · BTG supply event correctly flagged pre-match
  · Neutral venue — no AWAY disadvantage applied correctly

WHAT THE SIGNAL GOT WRONG:
  · N/A — direction correct (Spain won 2-0, not a close call)
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MEDIUM confidence at raw 55.0 was appropriate for a WC SF. Spain won
convincingly 2-0 — the margin exceeded what MEDIUM confidence implied,
but the directional call was sound. CAPITULATION ×0.70 compressing to
38.5 was correct given the macro environment. HOLD gate enforced correctly.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓

FUTURE CALIBRATION NOTE:
  This record confirms the one-sided AWAY pattern — Spain as administrative
  AWAY at neutral venues with no opposing token. $SPAIN burn #7 triggered,
  setting up the dual-token Final. Record 7 of 9 in the WC2026 series.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status:    ACTIVE
  Post-match resolution: ×0.70 applied correctly throughout.
                         BTG supply event executed regardless of regime.

FLAG: NEUTRAL_VENUE
  Pre-match status:    ACTIVE
  Post-match resolution: No home advantage for France. No AWAY disadvantage
                         for Spain. AT&T Stadium, Arlington, Texas, USA.
                         AWAY designation administrative only.

FLAG: BURN_TO_GLORY_ACTIVE_AWAY_ONLY
  Pre-match status:    ACTIVE — $SPAIN only
  Post-match resolution: $SPAIN burn #7 triggered at 7.5% SF rate.
                         Spain advance to Final.

FLAG: ONE_SIDED_RECORD
  Pre-match status:    ACTIVE — France has no fan token
  Post-match resolution: Confirmed. Only $SPAIN fan token intelligence
                         validated in this fixture.
```

---

## Agent rules engaged

```
TFM6 Gate 1:         Pre-kickoff submission ✓
CHZ regime applied:  CAPITULATION ×0.70 applied before output ✓
Token verified:      $SPAIN verified on Chiliz Chain before signal ✓
No home token:       France confirmed — no Chiliz fan token ✓
HOLD gate:           Triggered correctly under CAPITULATION regime ✓
PTG verified:        $SPAIN BTG burn #7 confirmed at 7.5% SF rate ✓
PTG N/A:             France — no fan token · PTG N/A ✓
PATH_2 N/A:          $SPAIN is not a PATH_2 token ($AFC only) ✓
Neutral venue noted: No home advantage modifier applied ✓
Series noted:        WC2026 Calibration Series 7/9 ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1c Token Registry | ACTIVE |
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context (Semi-Final) | ACTIVE |
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
  · fan-token/national-profiles/spain.md
  · macro/regulatory/france.md
  · sports/football/sport-domain-football.md
  · core/h2h-framework.md
```

---

## Source and verification

```
Signal source:   SportMind MCP · sportmind_pre_match
MCP server:      v3.97.89
Signal generated:2026-07-14 (pre-kickoff)
Library version: v4.1.8
Match date:      2026-07-14
Submitted by:    Internal submission
Result source:   FIFA.com · ESPN · BBC Sport
Result verified: 2026-07-14

PTG verification: chiliscan.com — $SPAIN burn #7 confirmed
PTG: N/A (France — no fan token)

NOTE — SINGLE TOKEN RECORD:
  Home side (France) has no fan token.
  Direction signal applies to $SPAIN only.
  No opposing signal · no dual-token modifier applicable.
```

---

*SportMind v4.6.28 · MIT License · sportmind.dev*
*WC2026 Calibration Series 7/9 · part of the 137-record SportMind calibration base*
*STATUS: COMPLETE — direction CORRECT ✓ · HOLD gate CORRECT ✓*
*$SPAIN BTG burn #7 triggered at 7.5% SF rate*

© 2026 SportMind
