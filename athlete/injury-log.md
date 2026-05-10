# Athlete Injury Log — Active High-Risk Flags

**Time-sensitive injury intelligence for named athletes ahead of confirmed
competition fixtures. Populated when a HIGH_RISK flag is raised for a major
event. Cleared after the event or when athlete is confirmed fit.**

> Companion to: `athlete/football/athlete-intel-football.md`
> Feeds directly into: pre-match signal T-48h updates and CDI calculations
> Update frequency: as confirmed injury reports arrive from Tier 1 sources

---

## Active flags — UCL Final 2026 (PSG vs Arsenal, 30 May 2026)

```
MATCH: UEFA Champions League Final 2025-26
DATE:  Saturday 30 May 2026 | Kickoff: 18:00 CEST | Puskás Aréna, Budapest
T-48H REASSESSMENT DATE: Thursday 28 May 2026

Both flags below require mandatory reassessment on 28 May 2026.
```

### Achraf Hakimi — PSG (RB) — HIGH_RISK_FOR_FINAL

```
PLAYER:         Achraf Hakimi
CLUB:           Paris Saint-Germain
POSITION:       Right Back / Wing Back
TOKEN:          $PSG (demand signal — no PATH_2 confirmed for PSG)

STATUS:         HIGH_RISK_FOR_FINAL
INJURY_TYPE:    Thigh (muscular)
INJURY_DETAIL:  Thigh injury — sidelined; active recovery protocol
AVAILABILITY:   UNCERTAIN — not cleared for final as of v3.97.15

SOURCE:         culturepsg.com — VERIFIED
VERIFIED_DATE:  2026-05-11

SIGNAL IMPLICATIONS:
  Hakimi absent → PSG right flank weakened
  Arsenal exploit: Martinelli or Saka vs replacement RB = elevated
  attacking opportunity for Arsenal on PSG's right side
  ATM modifier (PSG): apply availability_haircut = 0.05 if confirmed absent
    (Hakimi is a key contributor but PSG have squad depth at RB)
  CDI impact ($PSG): limited — PSG demand signal is not PATH_2 driven;
    Hakimi absence affects match signal, not direct supply mechanics
  CDI impact ($AFC): marginal positive — Arsenal attacking vs weakened flank

MANDATORY T-48H REASSESSMENT:
  Date: 28 May 2026
  Source: PSG official (psg.fr) + culturepsg.com + L'Equipe
  Action if CLEARED: remove HIGH_RISK flag; apply standard ATM modifier
  Action if CONFIRMED ABSENT: update ATM modifier, note in UCL Final signal
```

### Jurrien Timber — Arsenal (CB/RB) — HIGH_RISK_FOR_FINAL

```
PLAYER:         Jurrien Timber
CLUB:           Arsenal FC
POSITION:       Centre Back / Right Back (versatile defensive role)
TOKEN:          $AFC (PATH_2 Model 2 confirmed — signal directly affects supply)

STATUS:         HIGH_RISK_FOR_FINAL
INJURY_TYPE:    Groin (muscular)
INJURY_DETAIL:  Groin injury — sidelined; active recovery protocol
AVAILABILITY:   UNCERTAIN — not cleared for final as of v3.97.15

SOURCE:         arsenal.com — VERIFIED
VERIFIED_DATE:  2026-05-11

SIGNAL IMPLICATIONS:
  Timber absent → Arsenal defensive structure adjusted
  Timber provides versatility (CB or RB) that allows Calafiori/White to shift
  His absence reduces Arsenal's defensive tactical options vs PSG
  
  ATM modifier (Arsenal): apply absence_modifier = 0.90 if confirmed absent
    (Timber is significant but Arsenal have CB depth — Ben White, Calafiori,
    Kiwior available; Saliba anchors; impact is moderate not critical)
  
  $AFC CDI IMPLICATIONS (PATH_2 active):
    Timber absence is a negative ATM modifier for Arsenal match probability
    Reduced win probability → lower expected PATH_2 burn magnitude
    However: this is a marginal adjustment, not a direction reversal
    Saliba + partner defensive stability remains Arsenal's primary defensive asset
    
  CONTRAST WITH SAKA FLAG (from v3.97.7 UCL Final signal):
    Saka (RW) remains the CRITICAL $AFC flag (ATM ×1.10 fit / ×0.85 absent)
    Timber is SECONDARY $AFC flag (ATM 0.90 absent — smaller impact than Saka)
    Both flags active simultaneously would compound: apply combined modifier

MANDATORY T-48H REASSESSMENT:
  Date: 28 May 2026
  Source: Arsenal official (arsenal.com) + Sky Sports + The Athletic
  Action if CLEARED: remove HIGH_RISK flag; apply standard ATM modifier
  Action if CONFIRMED ABSENT: update ATM modifier, update UCL Final signal
```

---

## Combined injury flag — UCL Final signal update

```
COMBINED ATM MODIFIER — UCL FINAL (current library state v3.97.15):

  PSG ATM:     ×1.05 base → apply Hakimi_haircut = −0.05 if absent → ×1.00
  Arsenal ATM: ×1.05 base → apply Timber_absent = −0.05 if absent → ×1.00
               → additional Saka_absent = −0.20 if Saka also absent → ×0.85

  PRIORITY ORDER OF FLAGS:
    1. Saka (Arsenal RW):    CRITICAL — ×1.10 fit / ×0.85 absent
    2. Timber (Arsenal CB):  SECONDARY — ×0.90 if absent (from ×1.05 base)
    3. Hakimi (PSG RB):      TERTIARY — ×1.00 if absent (from ×1.05 base)

  T-48H REASSESSMENT:
    All three flags to be reassessed on 28 May 2026.
    Update UCL Final signal (examples/calibration/ucl-final-2026-psg-arsenal-signal.md)
    with confirmed modifier values before T-2h signal generation.

WHAT TO CHECK ON 28 MAY 2026:
  Saka:   Arsenal official + Sky Sports + Ornstein/The Athletic
  Timber: Arsenal official + arsenal.com injury updates
  Hakimi: PSG official + culturepsg.com + L'Equipe
```

---

## Injury log — closed flags

```
No closed flags for this competition window.
```

---

## Log format — for future entries

```
New HIGH_RISK entry template:

  PLAYER:         [Full name]
  CLUB:           [Club name]
  POSITION:       [Position]
  TOKEN:          [Token symbol and FTP status]

  STATUS:         HIGH_RISK_FOR_FINAL / CONFIRMED_ABSENT / CLEARED
  INJURY_TYPE:    [Type — muscular, ligament, suspension etc.]
  INJURY_DETAIL:  [Brief description]
  AVAILABILITY:   UNCERTAIN / CONFIRMED_ABSENT / CLEARED

  SOURCE:         [Tier 1 source — official club or verified press] — VERIFIED
  VERIFIED_DATE:  [YYYY-MM-DD]

  SIGNAL IMPLICATIONS:
    [Match signal impact]
    [Token CDI impact — especially if PATH_2 active]

  MANDATORY REASSESSMENT:
    Date: [T-48h of match]
    Source: [where to check]
    Action if CLEARED: [what to update]
    Action if CONFIRMED ABSENT: [what to update]
```

---

## Compatibility

**Pre-match signal:** `examples/calibration/ucl-final-2026-psg-arsenal-signal.md`
**Athlete base:** `athlete/football/athlete-intel-football.md`
**$AFC reference:** `fan-token/arsenal.md`
**CDI framework:** `fan-token/gamified-tokenomics-intelligence/`

---

*SportMind v3.97.15 · MIT License · sportmind.dev*
*Injury flags verified: 2026-05-11*
*All flags require T-48h reassessment before UCL Final (28 May 2026)*
