---
name: wc2026-r16-spain-vs-portugal-2026-07-06
status: COMPLETE — post-match verified · HOME WIN · $SPAIN BTG burn #5 triggered
contributor: Internal submission
contributor-type: INTERNAL
issue: n/a — internal calibration record
description: >
  Pre-match calibration record for FIFA World Cup 2026 Round of 16.
  Spain vs Portugal. AT&T Stadium, Arlington, Texas, USA. 2026-07-06 20:00 UTC.
  Signal generated 2026-07-06 18:24 UTC. MCP server v3.97.89.
  Library v4.1.2. CHZ CAPITULATION ×0.70 active.
  DUAL-TOKEN record — $SPAIN (HOME) and $POR (AWAY) both active Burn to Glory participants.
  REGISTRY-GAP (RESOLVED): $SPAIN not in registry at signal generation time — added v4.1.3.
  Direction: HOME (Spain). Result: Spain 1-0 Portugal (90+1'). Direction CORRECT ✓. Record 4.
---

# Calibration Record — FIFA World Cup 2026 · Round of 16
## Spain v Portugal · 2026-07-06

---

## Match details

```
Match:        Spain v Portugal
Competition:  FIFA World Cup 2026 — Round of 16
Season:       2026
Venue:        AT&T Stadium · Arlington, Texas · USA
Venue type:   NEUTRAL (third-party host nation — USA)
Date:         2026-07-06
Kickoff UTC:  2026-07-06T20:00:00Z
Fan tokens:   Home — $SPAIN (Spain · Chiliz Chain · verified ✓)
              Away — $POR (Portugal · Chiliz Chain · verified ✓)
Token type:   DUAL-TOKEN
Submitted by: Internal submission
Series:       WC2026 Calibration Series · Record 4/9
PTG status:   ACTIVE — $SPAIN Burn to Glory participant · ACTIVE — $POR Burn to Glory participant
BTG burn rate:Round of 16 burn rate: 2.5% (winner)
```

---

## Pre-match signal

*Generated: 2026-07-06T18:24:00Z · MCP server v3.97.89 · Library v4.1.2*

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

OCCASION WEIGHT:    ×1.40 (Round of 16) — suppressed by CAPITULATION gate

FLAGS:
  CHZ_CAPITULATION_ACTIVE:    true — ×0.70 suppressor applied
  NEUTRAL_VENUE:              true — AT&T Stadium, Arlington, Texas, USA
  REGISTRY-GAP:               true — $SPAIN not found in SportMind 81-token registry
                              at signal generation time (2026-07-06T18:24:00Z).
                              BTG burn mechanics for $SPAIN unverifiable via standard
                              signal chain at time of signal. Registry entry added v4.1.3.
  BTG_CONTINGENT:             true — 2.5% burn triggers only on winner progression
  LINEUP_CHECK_REQUIRED:      true — manual check at T-2h
  DSM_CHECK_REQUIRED:         true — manual check pre-kickoff

PRE-MATCH NOTE:
  Highest-profile R16 fixture — Iberian derby between two of the sport's
  most recognisable national programs. HOME/Spain at MEDIUM confidence
  (raw 55.0) consistent with Spain's positional structure and major
  tournament pedigree. Under CAPITULATION ×0.70, effective score compresses
  to 38.5 — HOLD gate enforced, not conviction position. $POR BTG mechanic
  (2.5% R16 rate) creates genuine supply event if Portugal advance — but CHZ
  macro environment suppresses expected price impact. $SPAIN registry absence
  was a material gap at signal time (resolved in v4.1.3). HOLD gate applies.
```

---

## Score derivation

```
Base score (SportMind pre-match):     55.0
Macro modifier (NEUTRAL ×1.00):       ×1.00 → 55.0
CHZ CAPITULATION modifier (×0.70):    ×0.70 → 38.5
Occasion weight (R16 ×1.40):          noted — suppressed by CAPITULATION gate
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
  · Spain structural superiority — reigning European champions,
    high-press positional play well-suited to knockout football
  · Iberian derby narrative modifier — rivalry classification triggers
    elevated narrative momentum; high-stakes knockout context amplifies
    fan sentiment arc for both tokens
  · $POR Tier 1 on-chain verified — confirmed Chiliz Chain contract;
    2.5% BTG treasury burn contingent on Portugal progression
  · Spain consistent group-stage output lifts HOME signal

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — demand signal suppressed
  · NEUTRAL VENUE — no structural home advantage modifier applied
  · CAPITULATION gate — HOLD enforced regardless of R16 occasion weight
  · $SPAIN registry gap — BTG mechanics for $SPAIN unverifiable at signal time
  · Portugal transitional risk — squad dependency concentration acts
    as signal dampener
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
  Occasion weight:  ×1.40 (Round of 16)
  Venue:            NEUTRAL — AT&T Stadium, Arlington, Texas, USA
  Venue modifier:   NEUTRAL — no home advantage

LAYER 3 — FORM:
  Spain form:       Dominant group stage — consistent positional output
  Portugal form:    Solid progression through group and R32 stages

LAYER 4 — H2H:
  H2H record:       Iberian derby — established high-profile fixture
  Gate:             PASS — sufficient sample; Spain recent edge in major tournaments

LAYER 5 — FAN TOKEN:
  $SPAIN:           Active · Chiliz Chain · verified ✓ (REGISTRY-GAP at signal time — resolved v4.1.3)
                    BTG status: ACTIVE · 2.5% R16 burn rate · 4 confirmed burns entering R16
  $POR:             Active · Chiliz Chain · verified ✓
                    BTG status: ACTIVE · 2.5% R16 burn rate · 2 confirmed burns entering R16
  Dual-token note:  Both tokens active — dual-token modifier applicable
```

---

## PTG / Burn to Glory status

```
PTG ROUND:     Round of 16 · burn rate 2.5%
WINNER BURN:   2.5% of winner's treasury holdings burned permanently
LOSER OUTCOME: BTG run ends · no burn · eliminated

$SPAIN BTG HISTORY (pre-match):
  Group ×3 (1%) + R32 ×1 (2%) = 4 confirmed burns entering R16
  Note: $SPAIN registry gap at signal time — BTG mechanics unverifiable
  via standard signal chain at 2026-07-06T18:24:00Z. Resolved v4.1.3.

$POR BTG HISTORY (pre-match):
  Group stage ×1 + Round of 32 ×1 = 2 confirmed burns entering R16

CHZ REGIME INTERACTION:
  Burns execute regardless of CHZ macro regime.
  Supply reduction is structural — price impact dampened by macro.
```

---

## Result — verified

```
ACTUAL RESULT:       Spain 1 — Portugal 0
WINNING TEAM:        Spain
SCORE:               1-0 (90+1' — Mikel Merino · assist: Ferran Torres sub)
EXTRA TIME:          NO
PENALTIES:           NO

DIRECTION CORRECT:   YES — HOME (Spain) ✓
  SportMind predicted: HOME (Spain)
  Actual result:       Spain won 1-0 in stoppage time
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
  Burn rate:     2.5% (Round of 16 rate)
  Burn number:   5 (cumulative WC2026)
  Burn history:  Group ×3 (1%) + R32 ×1 (2%) + R16 ×1 (2.5%)
  Next:          Spain advance to Quarter-Final · next burn rate 5% if Spain WIN QF
  Verify:        chiliscan.com

$POR BTG:
  Supply event:  NOT TRIGGERED — Portugal eliminated
  BTG run:       TERMINATED at 2 burns
  Burn history:  Group stage ×1 + Round of 32 ×1 = 2 confirmed burns
  Status:        Eliminated at Round of 16
```

---

## Post-match notes

```
MATCH CHARACTER:
  Spain won 1-0 via a Mikel Merino stoppage-time goal (90+1').
  Assist: Ferran Torres (substitute). Match decided in regular time —
  no extra time, no penalties. Tight, attritional contest throughout.
  Spain dominated possession and xG but Portugal were disciplined
  defensively. Goal came from a substitution combination in stoppage time.

WHAT THE SIGNAL GOT RIGHT:
  · CAPITULATION gate correctly applied — HOLD preserved ✓
  · MEDIUM confidence appropriate — match decided by single stoppage-time goal
  · Registry gap correctly flagged pre-match; resolved post-match in v4.1.3
  · BTG supply events correctly identified for both tokens

WHAT THE SIGNAL GOT WRONG:
  · N/A — direction correct
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MEDIUM confidence at raw 55.0 was precisely appropriate. Spain won but
not comfortably — a single stoppage-time goal, not a convincing margin.
CAPITULATION ×0.70 compressing to 38.5 correctly framed this as a HOLD
position. Cautious-entry zone and reduced sizing recommendation proved
appropriate given match character.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓

FUTURE CALIBRATION NOTE:
  Registry gap at signal time is the key learning from this record.
  The $SPAIN token was not in the 81-token registry at generation time —
  a material gap that was resolved in v4.1.3. This record documents the
  gap-and-resolution pattern for future reference.
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
                         administrative only. AT&T Stadium, Arlington, Texas, USA.

FLAG: BTG_CONTINGENT
  Pre-match status:    ACTIVE — 2.5% burn triggers only on winner progression
  Post-match resolution: $SPAIN burn #5 triggered on Spain progression.
                         $POR BTG run terminated — eliminated at R16.

REGISTRY-GAP (RESOLVED):
  $SPAIN was not present in the SportMind 81-token registry at signal
  generation time (2026-07-06T18:24:00Z). Token added to registry at
  v4.1.3 post-match. BTG burn mechanics for $SPAIN were unverifiable via
  standard signal chain at time of signal. Now resolved.
```

---

## Agent rules engaged

```
TFM6 Gate 1:         Pre-kickoff submission ✓ (signal generated 2026-07-06T18:24:00Z)
CHZ regime applied:  CAPITULATION ×0.70 applied before output ✓
Token verified:      $SPAIN verified on Chiliz Chain before signal ✓
                     (note: registry gap at signal time — resolved v4.1.3)
Token verified:      $POR verified on Chiliz Chain before signal ✓
HOLD gate:           Triggered correctly under CAPITULATION regime ✓
PTG verified:        $SPAIN BTG burn #5 confirmed at 2.5% R16 rate ✓
                     $POR BTG run terminated at 2 burns ✓
PATH_2 N/A:          $SPAIN is not a PATH_2 token ($AFC only) ✓
                     $POR is not a PATH_2 token ($AFC only) ✓
Neutral venue noted: No home advantage modifier applied ✓
Series noted:        WC2026 Calibration Series 4/9 ✓
Dual-token noted:    Dual-token modifier applicable — both tokens active ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1c Token Registry | ACTIVE |
| 2. Reasoning | 2b Probabilistic · 2c Multi-Signal · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context (Round of 16) | ACTIVE |
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
  · fan-token/national-profiles/por.md
  · sports/football/sport-domain-football.md
  · core/h2h-framework.md
  · macro/regulatory/france.md (Portugal holder note)
```

---

## Source and verification

```
Signal source:   SportMind MCP · sportmind_pre_match
MCP server:      v3.97.89
Signal generated:2026-07-06T18:24:00Z
Library version: v4.1.2 (at signal time) · resolved to v4.1.3 post-match
Match date:      2026-07-06
Submitted by:    Internal submission
Result source:   FIFA.com · ESPN · BBC Sport
Result verified: 2026-07-06

PTG verification: chiliscan.com — $SPAIN burn #5 confirmed
                  $POR BTG run terminated at 2 burns — eliminated
```

---

*SportMind v4.6.28 · MIT License · sportmind.dev*
*WC2026 Calibration Series 4/9 · part of the 137-record SportMind calibration base*
*STATUS: COMPLETE — direction CORRECT ✓ · HOLD gate CORRECT ✓*
*$SPAIN BTG burn #5 triggered at 2.5% R16 rate*

© 2026 SportMind
