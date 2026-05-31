---
name: ucl-final-psg-vs-arsenal-2026-05-30
status: VERIFIED — post-match confirmed 2026-05-30 — PSG win 4-3 penalties
description: >
  Calibration record — 2026 UEFA Champions League Final.
  PSG vs Arsenal. Puskás Aréna, Budapest. 2026-05-30.
  SportMind MCP server T-48h signal produced 2026-05-28.
  FTP PATH_2 $AFC active — first UCL Final with live supply event mechanism.
  RESULT: PSG win 1-1 AET (4-3 penalties). Direction CORRECT. Record 130.
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

PRE-LIQUIDATION ACTUAL:
  $AFC:   ~111,500 (confirmed — higher than 100,000 prior match estimate)
  USDC:   estimated from pool (chiliscan.com confirmation pending within 48h)
  Note:   Pool was larger than prior match baseline

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

## Result — VERIFIED

```
ACTUAL RESULT:         PSG win on penalties
SCORE:                 1-1 after extra time — PSG 4-3 on penalties
EXTRA TIME:            YES
PENALTIES:             YES — PSG win 4-3
WINNING TEAM:          Paris Saint-Germain

GOALSCORERS:
  Arsenal: Havertz 6'
  PSG:     Dembélé 65' (penalty)
  Decisive moment: Gabriel penalty miss — blazed over the bar

DIRECTION CORRECT:     YES ✓
  SportMind predicted: PSG (HOME)
  Actual winner:       PSG

SUPPLY EVENT OUTCOME:
  $AFC event:          LOSS — MINT EVENT
  Arsenal LOST therefore:
    $AFC tokens minted to treasury (supply INCREASES)
    Pre-liquidation pool: ~111,500 $AFC (confirmed — higher than estimate)
    Mint amount: equivalent to pre-liquidation pool
  Chiliscan confirmation: PENDING — verify on chiliscan.com within 48h

POST-MATCH NOTES:
  First UCL Final to go to extra time since Real Madrid vs Atletico Madrid 2016.
  PSG retain the UCL title — second consecutive Champions League winners.
  First club to defend the UCL title since Real Madrid in 2018.

  Havertz opened the scoring at 6'.
  Dembélé equalised via penalty at 65'.
  Gabriel missed the decisive penalty in the shootout — blazed over the bar.

  SportMind direction CORRECT despite:
    · Neutral venue
    · Match going to extra time
    · Near-equal squads
    · MEDIUM-HIGH confidence was appropriate — 120 minutes + penalties
      confirmed genuine closeness.

  $AFC PATH_2 LOSS outcome:
    Mint event expected within 48h.
    Monitor chiliscan.com for on-chain transaction confirmation.

  $PSG PATH_2 status: not confirmed — no supply event for PSG holders.

CALIBRATION VERDICT:   CORRECT ✓
  Direction: PSG ✓
  Adjusted score 58 reflected genuine PSG edge confirmed over 120 minutes
  and penalties. Confidence MEDIUM-HIGH correct — match was genuinely close
  but PSG ultimately prevailed.
  Record 130 — SportMind calibration base now 130 records.
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

T-24h UPDATE (2026-05-29):
  Adjusted score revised to 56-57
  Reason: Hakimi and Dembélé both confirmed fit and in squad.
  Both DSM gates cleared.
  Ben White OUT confirmed.
  Timber status unresolved but minor relative to PSG fitness boost.
  Signal locked at T-24h.

T-2h UPDATE (2026-05-30):
  Confirmed lineups received.
  Adjusted score revised to 58.
  Confidence: MEDIUM-HIGH.
  PSG: Hakimi confirmed starting — HIGH RISK fully resolved.
  Kvaratskhelia vs Mosquera (Arsenal right back) is a structural PSG advantage.
  Dembélé confirmed starting.
  Arsenal: Mosquera starts at right back — inexperienced at this level.
  Timber not in starting XI.
  Madueke not starting.
  Saka confirmed starting.
  Signal locked. No further gates.

POST-MATCH SIGNAL REVIEW:
  Final adjusted score 58 reflected genuine PSG edge.
  Extra time and penalties confirmed genuine closeness — MEDIUM-HIGH was correct.
  Kvaratskhelia vs Mosquera structural advantage held — Dembélé penalty at 65'
  was the equaliser and decisive momentum shift.
  Gabriel penalty miss (blazed over) was the decisive shootout moment.
  SportMind did not predict the exact mechanism (penalties) but the direction
  (PSG) was correct — which is what the calibration record measures.
```

---

## Source and verification

```
Signal source:    SportMind MCP server — T-48h pre-match output
Signal date:      2026-05-28
Match date:       2026-05-30
Submitted by:     SportMind (library internal record)
Result verified:  2026-05-30 — post-match confirmed
FTP source:       fantokens.com/fan-token-play — verified pre-liquidation
On-chain source:  chiliscan.com — mint transaction confirmation pending 48h
Calibration record: #130 — SportMind calibration base
```

---

*SportMind v3.97.96 · MIT License · sportmind.dev*
*STATUS: VERIFIED — PSG win 1-1 AET (4-3 pens) · Direction CORRECT ✓ · Record 130*
*$AFC PATH_2 LOSS — mint event pending on-chain confirmation (chiliscan.com)*
*First MCP server live UCL Final test — all five layers confirmed loaded*
