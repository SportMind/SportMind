---
name: ucl-final-psg-vs-arsenal-2026-05-30
status: DRAFT — awaiting post-match verification
description: >
  Pre-match calibration record for the 2026 UEFA Champions League Final.
  PSG vs Arsenal. Puskás Aréna, Budapest. 2026-05-30.
  SportMind MCP server T-48h signal produced 2026-05-28.
  FTP PATH_2 $AFC active — first UCL Final with live supply event mechanism.
  Result fields to be completed after full time.
---

# Calibration Record — 2026 UCL Final
## PSG vs Arsenal · 2026-05-30

---

## Match details

```
Match:        Paris Saint-Germain vs Arsenal
Competition:  UEFA Champions League Final
Season:       2025/26
Venue:        Puskás Aréna, Budapest, Hungary
Venue type:   NEUTRAL (neither club's home ground)
Date:         2026-05-30
Kickoff:      18:00 CET
```

---

## Pre-match signal

*Produced by SportMind MCP server · T-48h · 2026-05-28*

```
DIRECTION:          PSG (HOME — administrative designation only)
ADJUSTED SCORE:     55
CONFIDENCE:         MEDIUM
ACTION:             ENTER
SMS:                100 (all five layers loaded)
COMPOSITE MODIFIER: 1.00

MODIFIERS APPLIED:
  Macro modifier:   ANXIETY ×1.00
  Venue modifier:   NEUTRAL — Puskás Aréna, Budapest
                    PSG designated HOME for administrative purposes only
                    No true home advantage applied
  Athlete modifier: applied within adjusted score
  Fan token layer:  FTP PATH_2 active — supply event pending on result

FLAGS:
  lineup_unconfirmed:    false (at time of signal)
  macro_override_active: false
  neutral_venue:         true
  path2_active:          true ($AFC)
```

---

## FTP PATH_2 status

```
TOKEN:            $AFC (Arsenal Fan Token)
STATUS:           ACTIVE — Model 2 (Prediction Market / PATH_2)
PRE-LIQUIDATION:  CONFIRMED at T-48h (2026-05-28)

PRE-LIQUIDATION ESTIMATE:
  $AFC:   100,000 (based on prior match records)
  USDC:   ~49,600 (estimated — prior match baseline)
  Note:   Actual amounts from chiliscan.com pre-liquidation confirmation

SUPPLY EVENT TRIGGER:
  WIN (Arsenal):  $AFC tokens repurchased from market → burn/treasury split
                  (implementation-specific — Arsenal trial ~95% burned)
  LOSS (Arsenal): $AFC tokens minted to treasury (supply increases)
  DRAW:           No supply event — 0 burned, 0 minted

HISTORICAL CONTEXT:
  This is the FIRST UCL Final where a live FTP supply event mechanism fires.
  2023 UCL Final ($CITY vs $INTER): fan tokens present, no active FTP mechanics
  2025 UCL Final ($PSG vs $INTER): fan tokens present, no active FTP mechanics
  2026 UCL Final ($PSG vs $AFC):   $AFC PATH_2 ACTIVE — live supply event

$PSG PATH_2 STATUS: Not confirmed as of pre-match signal
```

---

## Result — TO BE COMPLETED AFTER FULL TIME

```
ACTUAL RESULT:         [TBC]
WINNING TEAM:          [TBC]
SCORE:                 [TBC]
EXTRA TIME:            [TBC — YES/NO]
PENALTIES:             [TBC — YES/NO]

DIRECTION CORRECT:     [TBC — YES / NO / DRAW]
  SportMind predicted: PSG (HOME)
  Actual winner:       [TBC]

SUPPLY EVENT OUTCOME:
  $AFC event:          [TBC]
    WIN:  burn — [TBC amount] $AFC burned, [TBC] USDC payout
    LOSS: mint — [TBC amount] $AFC minted to treasury
    DRAW: no supply event
  Chiliscan confirmation: [TBC — link to transaction]

POST-MATCH NOTES:      [TBC]

CALIBRATION VERDICT:   [TBC — CORRECT / INCORRECT / DRAW]
```

---

## Signal notes

```
NEUTRAL VENUE REASONING:
  PSG designated HOME per UEFA administrative assignment.
  Puskás Aréna is a neutral ground with no partisan home advantage.
  SportMind applied no venue home advantage modifier.
  True home advantage modifier: 0.

MACRO CONTEXT AT TIME OF SIGNAL:
  ANXIETY regime active (×1.00 — no amplification or reduction).
  BTC cycle: assessed at standard weight.
  No macro override triggered.

CONFIDENCE LEVEL — MEDIUM:
  Medium confidence reflects:
    · Neutral venue (removes home advantage certainty)
    · UCL Final one-off match (small sample, high variance)
    · Both clubs in form (Arsenal PL Champions 2025/26)
    · No lineup confirmation at T-48h signal time

FAN TOKEN DEMAND CONTEXT:
  UCL Final = ×2.00 demand amplifier (highest in SportMind)
  $AFC PATH_2 active = supply event fires on result
  This is the highest compound signal possible in the SportMind framework.
  WIN: ×2.00 demand × burn event = peak signal
  LOSS: ×2.00 demand × mint event = worst supply outcome at worst moment
```

---

## Source and verification

```
Signal source:    SportMind MCP server — T-48h pre-match output
Signal date:      2026-05-28
Match date:       2026-05-30
Submitted by:     SportMind (library internal record)
FTP source:       fantokens.com/fan-token-play — verified pre-liquidation
On-chain source:  chiliscan.com — to be verified post-match
```

---

*SportMind v3.97.94 · MIT License · sportmind.dev*
*STATUS: DRAFT — result fields blank, awaiting post-match verification*
*Update this file within 2h of full time whistle*
