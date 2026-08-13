---
name: football-mengo-vs-cruzeiro-libertadores-r16-2026-08-13
status: COMPLETE — post-match verified
contributor: Internal submission
contributor-type: INTERNAL
issue: n/a — internal calibration record
description: >
  Pre-match calibration record for Copa Libertadores Last 16 · First Leg.
  Cruzeiro v Flamengo. Estádio Governador Magalhães Pinto (Mineirão), Belo Horizonte, Brazil.
  2026-08-13. Signal generated 2026-08-13, pre-kickoff. MCP server v4.1.5.
  Library v4.4.9. CHZ CAPITULATION ×0.70 active.
  Single-token record — $MENGO (Flamengo) is the AWAY token only.
  Cruzeiro has no fan token. Direction assessed from $MENGO holder perspective.
  Raw signal HOME (Cruzeiro). H2H gate correction: AWAY lean (Flamengo).
  Direction contested. HOLD confirmed under CAPITULATION.
  Result: Cruzeiro 1–1 Flamengo. Direction INCORRECT ❌. HOLD gate CORRECT ✓. Record 134.
---

# Calibration Record — Copa Libertadores Last 16 · First Leg
## Cruzeiro v Flamengo · 2026-08-13

---

## Match details

```
Match:        Cruzeiro v Flamengo
Competition:  Copa Libertadores 2026 — Last 16 · First Leg
Season:       2026
Venue:        Estádio Governador Magalhães Pinto (Mineirão) · Belo Horizonte · Brazil
Venue type:   HOME (Cruzeiro home ground — Cruzeiro stronghold)
Date:         2026-08-13
Kickoff UTC:  2026-08-13T00:30:00Z
Kickoff BST:  2026-08-13 01:30 BST
Fan tokens:   Home — Cruzeiro — NO FAN TOKEN
              Away — $MENGO (Flamengo Fan Token · Chiliz Chain · verified ✓)
Token type:   SINGLE-TOKEN · AWAY TOKEN
              $MENGO is the away token — direction note applied.
              Direction assessed from $MENGO holder perspective.
              No dual-token modifier applicable.
Submitted by: Internal submission
Recorded at:  2026-08-13 pre-kickoff (TFM6 Gate 1 ✓)
PTG status:   N/A — Copa Libertadores is not a PTG-eligible tournament
Token note:   $MENGO holder outcome is assessed from AWAY side
              (Flamengo winning = positive for $MENGO holders)
```

---

## Pre-match signal

*Generated: 2026-08-13 pre-kickoff · MCP server v4.1.5 · Library v4.4.9*

```
DIRECTION:          HOME (Cruzeiro) — raw signal
                    H2H gate correction: direction contested
                    H2H PASSED in favour of AWAY (Flamengo)
                    Actual signal: CONTESTED (HOME raw · AWAY H2H lean)
RAW SCORE:          55.0 (HOME · Cruzeiro)
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE:     38.5  (55.0 × 0.70)
CONFIDENCE:         MEDIUM
ACTION:             HOLD  (CHZ regime gate applied · direction contested by H2H)
SMS:                100.0 · HIGH_QUALITY · 5/5 layers loaded
MACRO MODIFIER:     NEUTRAL ×1.0
COMPOSITE MODIFIER: ×0.70 (CAPITULATION override)

AWAY TOKEN NOTE:
  $MENGO is the away token in this fixture. Direction is assessed
  from the $MENGO holder perspective — a Flamengo WIN or favourable
  result is the positive signal. Raw SportMind signal of HOME (Cruzeiro)
  is an adverse signal for $MENGO holders. H2H gate correction (AWAY lean)
  partially contests the raw HOME signal.

FLAGS:
  CHZ_CAPITULATION_ACTIVE:     CAPITULATION ×0.70 applied. HOLD gate triggered.
  AWAY_TOKEN_FLAG:             $MENGO is the away token. Direction note applied.
                                $MENGO holder perspective: HOME = adverse.
  H2H_AWAY_LEAN:               H2H gate PASSED in favour of AWAY (Flamengo).
                                Flamengo won 3 of last 5 H2H meetings.
                                Cruzeiro failed to score in 3 of last 5 H2H encounters.
                                H2H modifier: AWAY lean · partially offsets HOME raw signal.
  DIRECTION_CONTESTED:         Raw signal HOME vs H2H AWAY lean.
                                Direction genuinely contested — real uncertainty.
                                MEDIUM confidence appropriate.
  NO_HOME_TOKEN:               Cruzeiro has no fan token.
                                Single-token record — no home opposing signal.
  NO_CDI_FILE:                 No $MENGO CDI file exists.
                                Football sport domain framework applied.
  BRAZIL_REGULATORY_LOADED:    brazil.md loaded · MP 1.303/2025 · T-60 active.
                                Brazilian calendar: INVERTED (Série A mid-season).
  PTG_NOT_ELIGIBLE:            Copa Libertadores is not a PTG-eligible tournament.
  PATH_2_NOT_APPLICABLE:       $AFC not involved — PATH_2 N/A.
  LINEUP_UNCONFIRMED:          Standard T-2h flag applied.

PRE-MATCH NOTE:
  Raw SportMind signal is HOME (Cruzeiro) based on Mineirão home advantage
  and Cruzeiro's strong domestic form. H2H gate PASSES in favour of AWAY
  (Flamengo): Flamengo won 3 of last 5 meetings; Cruzeiro failed to score
  in 3 of last 5 H2H encounters. Direction is genuinely contested —
  venue advantage vs H2H away lean. CAPITULATION ×0.70 applies — adjusted
  score 38.5, HOLD gate triggered for both directions. $MENGO is the away
  token; a HOME win is an adverse signal for $MENGO holders.
```

---

## Score derivation

```
Base score (SportMind pre-match):          55.0  (HOME · Cruzeiro)
Macro modifier (NEUTRAL ×1.0):             ×1.00   → 55.0
CHZ CAPITULATION modifier (×0.70):         ×0.70   → 38.5
Composite modifier applied:                ×0.70

Final adjusted score:                      38.5
ENTER threshold:                           50.0 (standard)
Threshold comparison:                      38.5 < 50.0

Direction contest:
  Raw direction signal: HOME (Cruzeiro) — 55.0 base
  H2H gate: PASSED in favour of AWAY (Flamengo)
  H2H adjustment: AWAY lean applied — partially contests HOME signal
  Effective direction signal: CONTESTED (HOME weighted · AWAY lean)

Action gate outcome:
  CAPITULATION gate: ACTIVE — both directions suppressed to HOLD
  Direction contested: HOLD reinforced by genuine uncertainty
  Final action output: HOLD
  Reason: adjusted score 38.5 below threshold; CAPITULATION
          non-negotiable; direction genuinely contested by H2H gate.

$MENGO holder note:
  HOME result is adverse for $MENGO holders.
  Contested direction with HOLD gate is the correct output
  given genuine uncertainty about fixture outcome.
```

---

## Primary signal drivers

```
RAW DIRECTION: HOME (Cruzeiro)
CONTESTED BY: H2H AWAY lean (Flamengo)

HOME SIGNAL DRIVERS (Cruzeiro):
  · Mineirão stronghold — described as Cruzeiro home fortress;
    home advantage real in Copa Libertadores knockout context
  · Strong domestic run — 4 wins 1 draw last 5 Série A matches;
    Copa do Brasil quarter-finalist; Série A 5th
  · Copa Libertadores group stage — runners-up in group;
    European competition momentum

AWAY SIGNAL DRIVERS (Flamengo / $MENGO):
  · H2H dominance — Flamengo won 3 of last 5 H2H meetings;
    durable structural advantage over Cruzeiro in this fixture
  · Cruzeiro scoring record vs Flamengo — failed to score in
    3 of last 5 H2H encounters; defensive solidity signal for Flamengo
  · Unbeaten run — Flamengo unbeaten last 6 matches;
    67% win rate over last 30 days
  · Best Libertadores group stage record — topped Group A
  · Leonardo Jardim tenure — from March 2026; squad stabilised
    under new system

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — macro suppressor overrides;
    HOLD mandatory for both directions
  · DIRECTION CONTESTED — genuine uncertainty between venue
    advantage and H2H away lean; MEDIUM confidence ceiling correct
  · NO CDI FILE — no $MENGO CDI intelligence; direction relies on
    sport domain and H2H framework only
  · AWAY TOKEN — $MENGO is on the away side; HOME result adverse;
    additional contextual asymmetry in signal interpretation
```

---

## Signal layers applied

```
LAYER 1 — MACRO:
  CHZ regime: CAPITULATION
  Modifier: ×0.70 (non-negotiable — overrides all layers)
  Verdict: HOLD gate triggered

LAYER 2 — SPORT DOMAIN:
  File: sports/football/sport-domain-football.md
  Copa Libertadores occasion weight: ×1.30 (knockout · Last 16)
  Venue: Mineirão · HOME (Cruzeiro stronghold) · STANDARD tier
  Venue modifier: STANDARD +0.06

LAYER 3 — FORM:
  Flamengo form: POSITIVE
    Unbeaten last 6 · best Libertadores group stage record ·
    67% win rate last 30 days · topped Group A
    Leonardo Jardim tenure from March 2026 — squad stabilised
  Cruzeiro form: POSITIVE
    4 wins 1 draw last 5 · Copa do Brasil QF · Série A 5th ·
    Strong domestic run entering knockout fixture

LAYER 4 — H2H:
  Applied: core/h2h-framework.md · five-condition gate · decay model
  Gate: PASSED — in favour of AWAY (Flamengo)
  Record: Flamengo won 3 of last 5 H2H meetings
  Cruzeiro scoring: failed to score in 3 of last 5 H2H encounters
  H2H modifier: AWAY lean — partially offsets HOME raw signal
  Result: direction contested between LAYER 2 venue advantage
          and LAYER 4 H2H away lean

LAYER 5 — REGIME:
  Brazil regulatory: brazil.md loaded
  MP 1.303/2025: active (T-60 from August 11 2026)
  Brazilian calendar: INVERTED (Série A mid-season)
  Regime output: CAPITULATION ×0.70 dominant; Brazil regulatory noted
```

---

## Result — verified

```
ACTUAL RESULT:    Cruzeiro 1–1 Flamengo
WINNING TEAM:     None (draw)
SCORE:            1–1 (full time)
EXTRA TIME:       NO
PENALTIES:        NO
AGGREGATE:        1–1 after first leg (second leg at Maracanã to follow)

DIRECTION CORRECT:    NO — INCORRECT ❌
  SportMind raw signal: HOME (Cruzeiro win)
  Actual result:       DRAW (1–1)
  Direction verdict:   INCORRECT

$MENGO HOLDER OUTCOME:
  DRAW — Flamengo held away from home at the Mineirão.
  Aggregate level (1–1) going into second leg at Maracanã
  (Flamengo home ground). Strong position for $MENGO holders.

ACTION OUTCOME:       HOLD — gate behaviour CORRECT ✓
  CAPITULATION ×0.70 correctly prevented position on an incorrect
  directional call. HOLD on a contested direction signal is the
  correct output under CAPITULATION regime.

CALIBRATION VERDICT:  DIRECTION INCORRECT · GATE BEHAVIOUR CORRECT
```

---

## Post-match notes

```
MATCH CHARACTER:
  Draw at the Mineirão — Flamengo's away record and H2H strength
  were validated. Cruzeiro, despite stronghold status, were unable
  to win at home. Flamengo secured a 1-1 aggregate level going into
  the second leg at the Maracanã (Flamengo's home ground) — a strong
  position for $MENGO holders. The H2H gate correction proved
  directionally useful: raw signal said HOME but H2H flagged AWAY lean;
  the actual result was a draw, confirming real Flamengo competitive
  strength at this fixture.

WHAT THE SIGNAL GOT RIGHT:
  · CAPITULATION ×0.70 correctly prevented ENTER on incorrect call.
  · H2H gate functioning correctly — AWAY lean flagged in a match
    where raw signal said HOME; result was draw, not a Cruzeiro win;
    H2H gate partially vindicated.
  · DIRECTION_CONTESTED flag correctly captured genuine uncertainty —
    DRAW was a plausible outcome; MEDIUM confidence was appropriate.
  · Away token framing was correct — $MENGO holders are well-positioned
    going into the Maracanã second leg with the aggregate at 1-1.

WHAT THE SIGNAL GOT WRONG:
  · Raw direction call HOME (Cruzeiro win) — result was DRAW (1-1).
    Mineirão stronghold status was overstated relative to H2H evidence.
  · H2H gate should have more heavily weighted Cruzeiro's failure to
    score in 3 of last 5 H2H meetings as a structural signal.
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MEDIUM confidence was correct for this fixture:
  · Direction genuinely contested (HOME raw vs H2H AWAY lean)
  · Both sides in strong form — real competitive uncertainty
  · $MENGO is away token — additional asymmetry in signal
  · CAPITULATION regime suppressing signal ceiling

HIGH confidence would have been wrong — the match was a draw.
MEDIUM correctly reflected the contested direction and genuine
uncertainty between venue advantage and H2H structure.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓
  CAPITULATION ×0.70 prevented ENTER on an incorrect directional call.
  HOLD on a genuinely contested direction is the correct framework
  output regardless of outcome.

FUTURE CALIBRATION NOTE:
  For future $MENGO calibrations:
  Flamengo H2H dominance over Cruzeiro is a durable structural signal —
  encode as a standing CDI modifier when $MENGO CDI file is created.
  Away token calibrations: H2H gate is particularly valuable when
  the token is on the away side; prevents over-reliance on venue
  modifier when away side has structural H2H advantage.
  Second leg at Maracanã: $MENGO home context will apply in next leg.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status: ACTIVE — ×0.70 suppressor applied
  Post-match resolution: CORRECT — HOLD gate fired correctly

FLAG: AWAY_TOKEN_FLAG
  Pre-match status: ACTIVE — $MENGO is away token; direction note applied
  Post-match resolution: CONFIRMED — away context applied correctly ✓
    $MENGO holders well-positioned going into second leg at 1-1

FLAG: H2H_AWAY_LEAN
  Pre-match status: ACTIVE — Flamengo H2H dominance flagged
  Post-match resolution: PARTIALLY VALIDATED — result was draw (not
    a Cruzeiro win); H2H away lean correctly contested raw HOME signal

FLAG: DIRECTION_CONTESTED
  Pre-match status: ACTIVE — raw HOME vs H2H AWAY lean
  Post-match resolution: VALIDATED — result was DRAW; direction
    uncertainty was real; MEDIUM confidence correctly captured this ✓

FLAG: NO_HOME_TOKEN
  Pre-match status: ACTIVE — Cruzeiro has no fan token
  Post-match resolution: Confirmed throughout — single-token record ✓

FLAG: NO_CDI_FILE
  Pre-match status: ACTIVE — no $MENGO CDI file
  Post-match resolution: Football domain framework applied ✓

FLAG: BRAZIL_REGULATORY_LOADED
  Pre-match status: ACTIVE — brazil.md · MP 1.303/2025 · T-60
  Post-match resolution: Noted — no material signal impact ✓

FLAG: PTG_NOT_ELIGIBLE
  Pre-match status: CONFIRMED — Copa Libertadores not PTG-eligible
  Post-match resolution: Confirmed ✓ — no supply event triggered

FLAG: PATH_2_NOT_APPLICABLE
  Pre-match status: CONFIRMED — $AFC not involved
  Post-match resolution: Confirmed ✓ — no supply event triggered

FLAG: LINEUP_UNCONFIRMED
  Pre-match status: Standard T-2h flag
  Post-match resolution: Resolved pre-kickoff — no material absences ✓
```

---

## Agent rules engaged

```
TFM6 Gate 1:              Pre-kickoff submission ✓
CHZ regime applied:       CAPITULATION ×0.70 applied before output ✓
$MENGO token verified:    $MENGO verified active · Chiliz Chain ✓
Single-token flag:        Applied — away token · no dual-token modifier ✓
No named players:         Record contains no named players ✓
PTG N/A confirmed:        Copa Libertadores not PTG-eligible ✓
PATH_2 N/A confirmed:     $AFC not involved — PATH_2 N/A ✓
HOLD gate triggered:      Correctly under CAPITULATION + direction contested ✓
H2H framework:            Gate run — PASSED (AWAY lean) ✓
brazil.md loaded:         Brazil regulatory context loaded ✓
No CDI file:              Football domain framework applied ✓
Away token direction:     Direction note applied — $MENGO holder perspective ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE |
| 6. Attention | 6a Signal Detection | ACTIVE |
| 8. Verification | 8a Source Tier Assessment | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration | ACTIVE |
| 12. Adaptation | 12a Regime Detection | ACTIVE |
| 14. Transparency | 14b Modifier Disclosure | ACTIVE |

---

## Source and verification

```
Signal source:    SportMind MCP · sportmind_pre_match
MCP server:       v4.1.5
Library version:  v4.4.9
Match date:       2026-08-13
Kickoff:          2026-08-13 00:30 UTC / 01:30 BST
Submitted by:     Internal submission
Result source:    Verified post-match (CONMEBOL / sports data)
Result verified:  2026-08-13 (post-match)
Record number:    134

PTG verification:    N/A — Copa Libertadores not PTG-eligible
PATH_2 verification: N/A — $AFC not involved

NOTE — SINGLE TOKEN RECORD (AWAY TOKEN):
  $MENGO (Flamengo) is the away token in this fixture.
  Cruzeiro has no fan token.
  Direction signal applies to $MENGO only, from Flamengo holder perspective.
  No opposing home signal · no dual-token modifier applicable.
  HOME result = adverse signal for $MENGO holders.
```

---

*SportMind v4.4.9 · MIT License · sportmind.dev*
*STATUS: COMPLETE — direction INCORRECT ❌ · HOLD gate CORRECT ✓ · Record 134*
*PTG: N/A · PATH_2: N/A*
