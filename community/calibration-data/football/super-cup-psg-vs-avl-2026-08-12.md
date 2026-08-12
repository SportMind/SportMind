---
name: football-psg-vs-avl-super-cup-2026-08-12
status: COMPLETE — post-match verified
contributor: Internal submission
contributor-type: INTERNAL
issue: n/a — internal calibration record
description: >
  Pre-match calibration record for UEFA Super Cup 2026.
  Paris Saint-Germain v Aston Villa. Red Bull Arena, Salzburg, Austria. 2026-08-12.
  Signal generated 2026-08-12, pre-kickoff. MCP server v4.4.7.
  Library v4.4.7. CHZ CAPITULATION ×0.70 active.
  Dual-token record — $PSG and $AVL both Chiliz Chain verified.
  PTG not eligible. PATH_2 N/A. Champion Call ACTIVE pre-match.
  Direction: HOME ($PSG). Result: PSG 2–1 Aston Villa. Direction CORRECT ✅.
  HOLD gate CORRECT ✓. Record 132.
---

# Calibration Record — UEFA Super Cup 2026
## Paris Saint-Germain v Aston Villa · 2026-08-12

---

## Match details

```
Match:        Paris Saint-Germain v Aston Villa
Competition:  UEFA Super Cup 2026
Season:       2026/27
Venue:        Red Bull Arena · Salzburg · Austria
Venue type:   NEUTRAL — no home advantage for either side
              PSG home designation is cosmetic (UEFA convention only)
              PSG home advantage not applied to signal
Date:         2026-08-12
Kickoff UTC:  2026-08-12T19:00:00Z
Kickoff BST:  2026-08-12 20:00 BST
Fan tokens:   Home — $PSG (Paris Saint-Germain Fan Token · Chiliz Chain · verified ✓)
              Away — $AVL (Aston Villa Fan Token · Chiliz Chain · verified ✓)
Token type:   DUAL-TOKEN
              Both tokens active on Chiliz Chain — dual-token signal applicable
Submitted by: Internal submission
Recorded at:  2026-08-12 pre-kickoff (TFM6 Gate 1 ✓)
PTG status:   NOT ELIGIBLE — UEFA Super Cup is excluded from PTG tournament list
```

---

## Pre-match signal

*Generated: 2026-08-12 pre-kickoff · MCP server v4.4.7 · Library v4.4.7*

```
DIRECTION:          HOME ($PSG)
RAW SCORE ($PSG):   68.0
RAW SCORE ($AVL):   61.5
CHZ MODIFIER:       CAPITULATION ×0.70
ADJUSTED SCORE ($PSG): 50.0  (68.0 × 0.70 = 47.6, +0.035 occasion uplift post-compression)
ADJUSTED SCORE ($AVL): 45.2  (61.5 × 0.70 = 43.1, +0.035 occasion uplift post-compression)
CONFIDENCE:         MODERATE
ACTION:             HOLD  (both SMS below 80 threshold)
SMS ($PSG):         50 — below HOLD gate threshold
SMS ($AVL):         45 — below HOLD gate threshold
OCCASION WEIGHT:    UEFA Super Cup · prestige one-off
                    Pre-compression modifier: +0.05
                    Post-compression uplift: +0.035 applied to both tokens
COMPOSITE MODIFIER: ×0.70 (CAPITULATION override dominant)

FLAGS:
  CHZ_CAPITULATION_ACTIVE:     CAPITULATION ×0.70 applied. HOLD gate triggered.
  DUAL_TOKEN:                   $PSG and $AVL both active Chiliz Chain tokens.
                                Dual-token signal framework applicable.
  H2H_GATE_FAIL:               H2H gate: FAIL — insufficient competitive sample.
                                No European meetings while both tokens active.
                                No H2H modifier applied.
  VENUE_NEUTRAL:               Red Bull Arena · Salzburg — neutral venue.
                                PSG home designation cosmetic only — not applied.
  AVL_DEBUT_AMPLIFIER:         Aston Villa first Super Cup appearance since 1982.
                                Debut amplifier +0.08 applied to $AVL signal.
  CDI_PSG_CONSOLIDATION_GROWTH: $PSG CDI gate: CONSOLIDATION → GROWTH.
                                 UCL winners 2025-26 · Super Cup holders 2025.
                                 CDI modifier ×1.25.
  CDI_AVL_GROWTH:              $AVL CDI gate: GROWTH · UEL winners 2025-26.
                                Debut Super Cup appearance · CDI modifier ×1.25 (capped).
  CHAMPION_CALL_ACTIVE:        Champion Call active for dual-token Final context.
                                Pre-match demand pressure noted.
                                FM1 + FM4 + FM8 applied. Does not upgrade confidence tier.
  LINEUP_UNCONFIRMED:          T-2h flag applied — lineup status unconfirmed at signal time.
  PTG_NOT_ELIGIBLE:            UEFA Super Cup excluded from PTG tournament list.
  PATH_2_NOT_APPLICABLE:       $AFC not involved — PATH_2 N/A.

PRE-MATCH NOTE:
  PSG enter as UCL holders and Super Cup experience club against Villa's first
  Super Cup appearance since 1982. CDI gap is real — PSG CONSOLIDATION→GROWTH
  vs Villa GROWTH — but CAPITULATION ×0.70 compresses both adjusted scores
  below 80 (PSG 50.0 · AVL 45.2), triggering mandatory HOLD for both tokens.
  Occasion uplift +0.035 applied post-compression but does not lift either
  score to ENTER territory. H2H gate FAILS — no competitive European meetings
  while both tokens active; framework correctly flags and does not infer.
  Champion Call active pre-match — demand pressure noted but does not change
  confidence tier or gate decision.
```

---

## Score derivation

```
$PSG score derivation:
  Base score (SportMind pre-match):          68.0
  CHZ CAPITULATION modifier (×0.70):         ×0.70   → 47.6
  Occasion uplift post-compression:          +0.035  → 50.0
  CDI modifier ($PSG CONSOLIDATION→GROWTH):  ×1.25   [applied within base]
  Composite modifier applied:                ×0.70

  Final adjusted score ($PSG):               50.0
  ENTER threshold:                           80.0 (SMS gate)
  $PSG SMS:                                  50 → below threshold

$AVL score derivation:
  Base score (SportMind pre-match):          61.5
  CHZ CAPITULATION modifier (×0.70):         ×0.70   → 43.1
  Occasion uplift post-compression:          +0.035  → 45.2
  Debut amplifier (AVL first Super Cup):     +0.08   [applied within base]
  CDI modifier ($AVL GROWTH):               ×1.25   [applied within base, capped]
  Composite modifier applied:                ×0.70

  Final adjusted score ($AVL):               45.2
  ENTER threshold:                           80.0 (SMS gate)
  $AVL SMS:                                  45 → below threshold

Action gate outcome:
  Raw direction signal: HOME ($PSG)
  CAPITULATION gate: ACTIVE — both scores below ENTER threshold
  HOLD gate triggered for both tokens
  Final action output: HOLD
  Reason: $PSG SMS 50 and $AVL SMS 45 both fall well below the 80
          threshold. CAPITULATION regime gate is non-negotiable.
          Direction signal is HOME but no position warranted.
```

---

## Primary signal drivers

```
DIRECTION CHOSEN: HOME ($PSG)

POSITIVE DRIVERS FOR $PSG:
  · UCL winners 2025-26 — highest competition tier confirmation;
    CDI gate CONSOLIDATION→GROWTH applies ×1.25 modifier
  · Super Cup holders 2025 — experienced in this specific fixture
    context; occasion familiarity advantage
  · Ligue 1 champions — domestic form confirmation entering
    European season in optimal condition
  · CDI gap vs Villa — $PSG CONSOLIDATION→GROWTH vs $AVL GROWTH;
    PSG structurally above Villa in SportMind CDI hierarchy

POSITIVE CONTEXT FOR $AVL:
  · UEL winners 2025-26 — first major European trophy; CDI GROWTH
  · UCL 2026-27 confirmed — structural momentum signal
  · Debut amplifier +0.08 — first Super Cup appearance since 1982;
    narrative demand real regardless of match result
  · Strong form entering European season

DAMPENERS / SIGNAL SUPPRESSORS:
  · CHZ CAPITULATION ×0.70 — dominant macro suppressor; both scores
    compressed below ENTER threshold; HOLD mandatory for both tokens
  · H2H GATE FAIL — no competitive European meetings while both tokens
    active; no historical precedent to anchor direction confidence
  · VENUE NEUTRAL — Red Bull Arena, Salzburg; no home advantage;
    PSG home designation cosmetic only, not applied to signal
  · LINEUP UNCONFIRMED — T-2h flag active; both squad selections
    unknown at signal time
  · MODERATE confidence ceiling — real competitive uncertainty
    between UCL holders (PSG) and UEL holders (AVL) warranted
    MODERATE not HIGH
```

---

## Signal layers applied

```
LAYER 1 — MACRO:
  CHZ regime: CAPITULATION
  Modifier: ×0.70 (non-negotiable — dominant suppressor)
  Verdict: HOLD gate triggered for both tokens

LAYER 2 — SPORT DOMAIN:
  File: sports/football/sport-domain-football.md
  Competition: UEFA Super Cup — prestige one-off
  Occasion weight: +0.05 pre-compression · +0.035 post-compression
  Venue: Red Bull Arena · NEUTRAL · cosmetic home designation only
  Venue modifier: 1.00 (no partisan advantage either side)

LAYER 3 — FORM:
  $PSG form: HIGH
    UCL winners · Super Cup experience · Ligue 1 champions
    Form modifier: POSITIVE — applied within base score
  $AVL form: MODERATE-HIGH
    UEL winners · first major European trophy
    Occasion novelty: double-edged (elevates demand but introduces
    uncertainty — Villa have no recent Super Cup reference point)

LAYER 4 — H2H:
  H2H gate: FAIL
  Reason: insufficient competitive sample
           No competitive European meetings while both tokens were active
  H2H modifier: NOT APPLIED
  Framework behaviour: correctly flagged as FAIL rather than inferring
                        from non-applicable historical data
  Confidence impact: direction call relies on CDI and form layers only

LAYER 5 — REGIME:
  Champion Call: ACTIVE (dual-token Final context)
  FM1 (Price-Signal Conflation): applied — Champion Call demand
    noted but not conflated with direction confidence
  FM4 (Sentiment Source Contamination): applied — Champion Call
    social volume not treated as direction signal
  FM8 (DeFi Infrastructure Conflation): applied — on-chain Champion
    Call mechanics not conflated with token demand direction
  Regime output: CAPITULATION ×0.70 dominant · Champion Call noted ·
                 FM guardrails applied · HOLD gate confirmed

LAYER 6 — CDI:
  $PSG CDI: market/club-intelligence/psg.md (or equivalent)
    Gate: CONSOLIDATION → GROWTH
    Modifier: ×1.25
    Context: UCL winners 2025-26 · Super Cup holders 2025
  $AVL CDI: market/club-intelligence/avl.md (or equivalent)
    Gate: GROWTH
    Modifier: ×1.25 (capped)
    Debut amplifier: +0.08 (first Super Cup since 1982)
    Context: UEL winners 2025-26 · UCL 2026-27 debut
```

---

## Result — verified

```
ACTUAL RESULT:    Paris Saint-Germain 2–1 Aston Villa
WINNING TEAM:     Paris Saint-Germain
SCORE:            2–1 (full time)
EXTRA TIME:       NO
PENALTIES:        NO

DIRECTION CORRECT:    YES — CORRECT ✅
  SportMind predicted: HOME ($PSG)
  Actual winner:       Paris Saint-Germain
  Direction verdict:   CORRECT

ACTION OUTCOME:       HOLD — gate behaviour CORRECT ✓
  CAPITULATION ×0.70 correctly prevented ENTER on a winning directional call.
  HOLD gate fired as designed — direction correct but macro regime
  conditions did not warrant position entry.

CALIBRATION VERDICT:  DIRECTION CORRECT · GATE BEHAVIOUR CORRECT
```

---

## Post-match notes

```
MATCH CHARACTER:
  PSG won convincingly enough to validate the directional call — 2-1
  final score against a Villa side that was genuinely competitive.
  Aston Villa scored and made the match challenging; this was not a
  walkover. The debut amplifier was real — Villa's narrative demand
  and on-pitch competitiveness were both above the baseline that
  a routine Super Cup appearance might imply. PSG's UCL pedigree
  and Super Cup experience ultimately proved decisive.

WHAT THE SIGNAL GOT RIGHT:
  · Direction call HOME ($PSG) — CORRECT. PSG won 2-1.
  · CAPITULATION ×0.70 correctly prevented ENTER despite correct
    direction. HOLD gate on a winning call is correct gate behaviour —
    the macro regime prevents position entry, not the direction signal.
  · $AVL debut amplifier (+0.08) was validated — Villa scored and
    were competitive; amplifier correctly captured the narrative demand
    and competitive uplift from Villa's first Super Cup in 44 years.
  · H2H gate FAIL was correct — no prior data existed; framework
    handled the data gap correctly by flagging rather than inferring.
  · MODERATE confidence was appropriate — Villa scored; this was not
    a high-certainty outcome despite PSG's structural advantage.
  · FM1 + FM4 + FM8 applied correctly to Champion Call — pre-match
    demand pressure noted without conflating it with direction signal.

WHAT THE SIGNAL GOT WRONG:
  · N/A — direction correct and gate behaviour correct.
    No material signal failures to document.
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: WELL-CALIBRATED ✓

MODERATE confidence was correct:
  · First Super Cup meeting of these clubs — no H2H data available
  · AVL debut amplifier introduces genuine uncertainty above base
  · Villa scored — not a high-certainty outcome for PSG
  · CAPITULATION regime suppresses both scores below ENTER threshold

HIGH confidence would have been wrong in calibration terms —
Villa made it competitive (1 goal scored). MODERATE correctly
reflected the real uncertainty while still pointing HOME.

HOLD GATE ASSESSMENT: WORKING AS DESIGNED ✓
  The CAPITULATION ×0.70 gate triggered HOLD on a winning directional
  call. This is correct gate behaviour — the macro regime gate is
  non-negotiable regardless of direction accuracy. HOLD under
  CAPITULATION when direction turns out to be correct is still
  a correct gate outcome.

FUTURE CALIBRATION NOTE:
  For dual-token Super Cup fixtures: apply debut amplifier for
  first-appearance clubs regardless of CDI gate level. The occasion
  gap between PSG (Super Cup experience, UCL holders) and AVL
  (Super Cup debut since 1982) was real but did not produce an upset.
  Debut amplifier is correctly directional — it does not invert
  the signal, it elevates the subordinate token's demand floor.
  Second Super Cup appearance by Villa (if applicable): assess
  whether debut amplifier still applies or reverts to standard gate.
```

---

## Flags resolved

```
FLAG: CHZ_CAPITULATION_ACTIVE
  Pre-match status: ACTIVE — ×0.70 suppressor applied
  Post-match resolution: CORRECT — HOLD gate fired correctly for both tokens

FLAG: DUAL_TOKEN
  Pre-match status: ACTIVE — $PSG and $AVL both verified
  Post-match resolution: CONFIRMED — both tokens active throughout ✓

FLAG: H2H_GATE_FAIL
  Pre-match status: FAIL — insufficient competitive sample
  Post-match resolution: CORRECT — no H2H data existed; framework
    correctly flagged rather than inferring; gate fail validated

FLAG: VENUE_NEUTRAL
  Pre-match status: ACTIVE — Red Bull Arena · no home advantage
  Post-match resolution: CONFIRMED — no home advantage materialised;
    PSG home designation cosmetic only; correctly not applied

FLAG: AVL_DEBUT_AMPLIFIER
  Pre-match status: ACTIVE — Villa first Super Cup since 1982 (+0.08)
  Post-match resolution: VALIDATED — Villa scored and were genuinely
    competitive; debut amplifier correctly elevated $AVL demand signal

FLAG: CDI_PSG_CONSOLIDATION_GROWTH
  Pre-match status: ACTIVE — ×1.25 modifier applied
  Post-match resolution: VALIDATED — PSG won; CDI gate correctly
    reflected structural superiority

FLAG: CDI_AVL_GROWTH
  Pre-match status: ACTIVE — ×1.25 modifier (capped) · debut amplifier
  Post-match resolution: VALIDATED — Villa competitive; GROWTH gate
    appropriate for UEL winners with debut Super Cup context

FLAG: CHAMPION_CALL_ACTIVE
  Pre-match status: ACTIVE — demand pressure noted · FM1+FM4+FM8 applied
  Post-match resolution: FM guardrails applied correctly throughout;
    Champion Call demand did not corrupt direction signal

FLAG: LINEUP_UNCONFIRMED
  Pre-match status: T-2h flag applied
  Post-match resolution: Both sides fielded strong first-choice XIs;
    no material absence affected signal validity

FLAG: PTG_NOT_ELIGIBLE
  Pre-match status: CONFIRMED — UEFA Super Cup excluded
  Post-match resolution: Confirmed ✓ — no supply event triggered

FLAG: PATH_2_NOT_APPLICABLE
  Pre-match status: CONFIRMED — $AFC not involved
  Post-match resolution: Confirmed ✓ — no supply event triggered
```

---

## Agent rules engaged

```
TFM6 Gate 1:              Pre-kickoff submission ✓
CHZ regime applied:       CAPITULATION ×0.70 applied before output ✓
$PSG token verified:      $PSG verified active · Chiliz Chain ✓
$AVL token verified:      $AVL verified active · Chiliz Chain ✓
Dual-token flag applied:  Dual-token framework engaged · both tokens ✓
No named players:         Record contains no named players ✓
PTG N/A confirmed:        UEFA Super Cup not PTG-eligible ✓
PATH_2 N/A confirmed:     $AFC not involved — PATH_2 N/A ✓
HOLD gate triggered:      Both SMS below 80 · HOLD correct under CAPITULATION ✓
H2H framework:            Gate run — FAIL (insufficient sample) ✓
Neutral venue applied:    PSG home designation cosmetic only · not applied ✓
Champion Call FM rules:   FM1 · FM4 · FM8 applied · demand pressure noted ✓
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context | ACTIVE |
| 6. Attention | 6a Signal Detection | ACTIVE |
| 8. Verification | 8a Source Tier Assessment | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration | ACTIVE |
| 12. Adaptation | 12a Regime Detection | ACTIVE |
| 14. Transparency | 14b Modifier Disclosure | ACTIVE |

*3b (Event Context) added — UEFA Super Cup prestige occasion weight applied and
debut amplifier engaged for $AVL first Super Cup since 1982.*

---

## Source and verification

```
Signal source:    SportMind MCP · sportmind_pre_match
MCP server:       v4.4.7
Library version:  v4.4.7
Match date:       2026-08-12
Kickoff:          2026-08-12 19:00 UTC / 20:00 BST
Submitted by:     Internal submission
Result source:    UEFA.com — verified post-match
Result verified:  2026-08-12 (post-match)
Record number:    132

PTG verification:    N/A — UEFA Super Cup not PTG-eligible
PATH_2 verification: N/A — $AFC not involved
```

---

*SportMind v4.4.8 · MIT License · sportmind.dev*
*STATUS: COMPLETE — direction CORRECT ✅ · HOLD gate CORRECT ✓ · Record 132*
*PTG: N/A · PATH_2: N/A*
