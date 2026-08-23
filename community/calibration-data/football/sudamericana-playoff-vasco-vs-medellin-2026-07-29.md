```yaml
record_id: R130
competition: Copa Sudamericana 2026
stage: Playoff Round of 32 — 2nd leg
home_team: Vasco da Gama
away_team: Independiente Medellín
home_token: $VASCO
away_token: null
venue: Estádio São Januário · Rio de Janeiro · Brazil
kickoff_utc: 2026-07-29T22:00:00Z
kickoff_bst: 2026-07-29T23:00:00+01:00
submitted_pre_kickoff: true
signal_source: SportMind MCP · sportmind_pre_match
library_version: v4.1.75
record_version: v4.6.27
type: seed
direction: HOME
confidence_pre_capitulation: MEDIUM
confidence_post_capitulation: LOW
base_score: 55.0
capitulation_multiplier: 0.70
adjusted_score: 38.5
hold_gate: HOLD
result: Vasco da Gama 1–0 Independiente Medellín
aggregate_result: Vasco 3–2 (advance)
direction_correct: true
hold_gate_correct: true
```

# Calibration Record R130 — Copa Sudamericana 2026 Playoff R32 (2nd leg)

**Record:** R130
**Type:** Seed · Pre-match submission · Result verified
**Competition:** Copa Sudamericana 2026 · Playoff Round of 32 · 2nd leg
**Library version at submission:** v4.1.75
**Record version:** v4.6.27 (backfill to current template standard)

---

## Match Details

```
Home:       Vasco da Gama ($VASCO)
Away:       Independiente Medellín (no fan token)
Venue:      Estádio São Januário · Rio de Janeiro · Brazil
Kickoff:    2026-07-29 · 23:00 BST (22:00 UTC)
Type:       Single-token record ($VASCO home token only)
Aggregate:  2–2 going into 2nd leg (first leg in Colombia)
Context:    Knockout playoff — winner advances to Copa Sudamericana
            Round of 16. Loser eliminated.
```

---

## Pre-Match Signal

```
DIRECTION:   HOME ($VASCO)
CONFIDENCE:  LOW (downgraded from MEDIUM via CAPITULATION ×0.70)
HOLD GATE:   HOLD — adjusted score 38.5 < 80 threshold
             DO NOT ENTER regardless of directional call

TOKEN STATUS: $VASCO — ACTIVE · Chiliz Chain · verified
```

---

## Score Derivation

```
BASE SCORE:               55.0
  Rationale: Standard competitive floor for a genuine knockout
  fixture with material uncertainty. Aggregate level at 2–2
  creates balanced two-leg context — neither team holds advantage.
  Home advantage at São Januário supports HOME direction but
  aggregate parity constrains confidence above MEDIUM.

CAPITULATION MULTIPLIER:  ×0.70 (CHZ macro regime · ACTIVE)
ADJUSTED SCORE:           55.0 × 0.70 = 38.5

HOLD GATE:                HOLD (38.5 < 80 threshold — non-negotiable)
CONFIDENCE OUTPUT:        LOW
  MEDIUM confidence downgraded to LOW by CAPITULATION regime.
  LOW correctly reflects: (1) CAPITULATION macro suppression,
  (2) aggregate level — genuine uncertainty, (3) two-leg knockout
  context where away goal rule does not apply (CONMEBOL format:
  replay or extra time/penalties if level after 90 min in 2nd leg).
```

---

## Primary Signal Drivers

```
POSITIVE (HOME):
  · Home advantage — Estádio São Januário · known home fortress
    for Vasco supporters
  · Aggregate parity means Vasco need only a win at home to
    advance — no away goal disadvantage to overcome
  · Brazilian club playing at home in South American competition
    — structural home advantage amplified by crowd intensity
  · $VASCO token holder demand aligns with home advancement

NEGATIVE / UNCERTAINTY:
  · First leg ended 2–2 in Colombia — Medellín showed away
    scoring capability (2 goals away)
  · Aggregate level = genuine uncertainty · any margin of
    victory for either team decides the tie
  · No $VASCO CDI file in library — domain framework applied
    (confidence ceiling applies without CDI validation)
  · CAPITULATION ×0.70 active — macro suppression overrides
    all positive demand signals

NET ASSESSMENT: HOME direction supported · MEDIUM confidence
  pre-CAPITULATION · LOW post-CAPITULATION · HOLD gate active
```

---

## Signal Layers Applied

```
LAYER 1 — MACRO (CHZ REGIME):
  CHZ CAPITULATION ×0.70 — ACTIVE at time of submission
  Applied to base score: 55.0 × 0.70 = 38.5
  Status: CORRECTLY APPLIED ✓

LAYER 2 — CDI (CLUB DEMAND INTELLIGENCE):
  $VASCO CDI file: NOT IN LIBRARY at time of submission
  Domain framework applied — no CDI multiplier available
  Confidence ceiling: MEDIUM (cannot exceed without CDI)
  Status: DOMAIN FRAMEWORK APPLIED · no CDI file ✓

LAYER 3 — FORM:
  Vasco had reached the playoff via group stage (runners-up)
  Away leg 2–2 in Medellín showed attacking capability
  Form layer: APPLIED — general form signal, no CDI precision
  Status: APPLIED AT DOMAIN LEVEL ✓

LAYER 4 — H2H:
  H2H gate: Copa Sudamericana knockout context
  Cross-confederation H2H sample insufficient for gate PASS
  H2H framework: GATE FAILS — insufficient competitive sample
  Status: H2H NOT APPLIED · gate correctly failed ✓

LAYER 5 — VENUE:
  Estádio São Januário · HOME fixture · STANDARD home advantage
  No FORTRESS classification confirmed at submission date
  Venue modifier: HOME STANDARD applied
  Status: CORRECTLY APPLIED ✓

LAYER 6 — REGULATORY:
  Brazil regulatory framework: 17.5% CGT (MP 1.303/2025)
  Applied as structural backdrop — no acute regulatory signal
  at submission date
  Status: BACKGROUND LAYER — no acute signal ✓

SMS (Signal Map Score): 83.3 — HIGH_QUALITY
  5/6 core layers loaded (CDI layer absent — no file available)
  H2H gate failed correctly — not a loading failure
  Regulatory layer loaded as background
```

---

## PTG / Burn to Glory Status

```
NOT APPLICABLE — Copa Sudamericana is NOT a PTG-eligible
competition. PTG mechanics apply to national team tokens only
(WC · EURO · Copa América — per Chiliz PTG programme rules).
$VASCO is a club token. No supply event applies to this fixture.
```

---

## FTP PATH_2 Status

```
NOT APPLICABLE — $VASCO is not $AFC.
PATH_2 (Fan Token Play market settlement) applies exclusively
to $AFC. Never generalise PATH_2 to other tokens.
```

---

## Result Verified

```
Full-time:    Vasco da Gama 1–0 Independiente Medellín
Aggregate:    Vasco da Gama 3–2 Independiente Medellín
Outcome:      VASCO DA GAMA ADVANCE to Copa Sudamericana Round of 16

DIRECTION:    HOME ✅ CORRECT
HOLD GATE:    CORRECT ✓
  HOLD prevented ENTER on a CORRECT directional call.
  CAPITULATION gate working as designed — macro suppression
  correctly prevented commitment despite correct direction.

CONFIDENCE NOTE:
  LOW confidence was appropriate — the 1–0 margin was narrow
  and the match context (2–2 aggregate, elimination stakes)
  validated the genuine uncertainty reflected in LOW confidence.
  MEDIUM pre-CAPITULATION was correctly calibrated to the
  signal strength available without a CDI file.
```

---

## Supply Event Outcome

```
NOT APPLICABLE — no supply event active for this fixture.
Copa Sudamericana is not PTG-eligible. No PATH_2 on $VASCO.
$VASCO treasury: unchanged by this result.
```

---

## Post-Match Notes

```
· Vasco advanced 3–2 on aggregate to the Copa Sudamericana R16
· The 1–0 second leg win validated HOME direction
· Medellín's 2 away goals in the first leg made this a genuine
  contest — LOW confidence was well-calibrated to that context
· No CDI file for $VASCO at submission — demand signal layer
  was thin. CDI file creation would strengthen future $VASCO
  calibration records.
· CAPITULATION ×0.70 correctly downgraded MEDIUM → LOW.
  Macro suppression working as designed.
· This is the first Copa Sudamericana calibration record in
  the library. Gate 6 classification: CONTINENTAL KNOCKOUT
  (equivalent to Copa Libertadores R16 context — Tier 2 Major
  Continental classification).
```

---

## Signal Quality Note

```
SMS: 83.3 — HIGH_QUALITY
  Core layers: 5/6 loaded (CDI absent — no file)
  H2H gate: correctly failed (insufficient sample)
  Venue: HOME STANDARD applied
  Regulatory: background layer
  CAPITULATION: applied

QUALITY ASSESSMENT:
  Record quality is HIGH_QUALITY despite absent CDI — the
  domain framework was correctly applied and the directional
  output was correct. CDI absence is a known library gap for
  $VASCO, not a calibration failure. Future $VASCO records
  benefit from CDI file creation.
```

---

## Flags Resolved

```
FLAG 1: CAPITULATION ACTIVE — ×0.70 applied · adjusted score
  38.5 · HOLD gate enforced · RESOLVED ✓

FLAG 2: NO CDI FILE — $VASCO CDI not in library · domain
  framework applied · confidence ceiling MEDIUM · RESOLVED ✓

FLAG 3: AGGREGATE CONTEXT — 2–2 going in · genuine two-leg
  knockout uncertainty · reflected in MEDIUM base confidence
  before CAPITULATION · RESOLVED ✓

FLAG 4: H2H GATE FAILS — cross-confederation sample
  insufficient · H2H layer correctly excluded · RESOLVED ✓

FLAG 5: SINGLE-TOKEN RECORD — Medellín has no fan token ·
  $VASCO holder demand only · no dual-token compound ·
  RESOLVED ✓

FLAG 6: NO PTG APPLICABLE — Copa Sudamericana not PTG-eligible
  · club token not national token · no supply event ·
  RESOLVED ✓
```

---

## Agent Rules Engaged

```
RULE 1 — TFM6 (Gate 1): Record submitted pre-kickoff ✅
  Non-negotiable gate — correctly met at submission.

RULE 2 — CAPITULATION GATE: ×0.70 applied before confidence
  output ✅ MEDIUM → LOW correctly executed.

RULE 3 — HOLD GATE: Adjusted score 38.5 < 80 = HOLD
  non-negotiable ✅ Gate correctly enforced.

RULE 4 — TOKEN VERIFICATION: $VASCO active on Chiliz Chain
  verified before signal generation ✅

RULE 5 — NO NAMED PLAYERS: No player names in record ✅
  Club Intelligence Gate compliant.

RULE 6 — PTG NOT APPLICABLE: Copa Sudamericana correctly
  excluded from PTG framework ✅

RULE 7 — PATH_2 NOT APPLICABLE: $VASCO is not $AFC ✅
  PATH_2 never generalised.

RULE 8 — H2H GATE CORRECTLY FAILED: Insufficient competitive
  sample · H2H layer excluded · no fabricated H2H modifier ✅

RULE 9 — DOMAIN FRAMEWORK: No CDI file · domain framework
  applied · confidence ceiling respected ✅

RULE 10 — REGULATORY BACKGROUND: Brazil 17.5% CGT applied
  as background structural layer · no acute signal at
  submission date ✅
```

---

## Mind Dimensions

| Dimension | Sub-dimension | Status | Notes |
|---|---|---|---|
| 1. Intelligence | 1a Domain Knowledge | ACTIVE | Copa Sudamericana format · two-leg playoff structure |
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE | Aggregate context · two-leg uncertainty reasoning |
| 3. Context | 3a Macro · 3b Event | ACTIVE | CAPITULATION regime · playoff elimination stakes |
| 4. Memory | 4b Semantic | ACTIVE | CDI absence flag · domain framework precedent |
| 5. Judgment | 5a Uncertainty · 5b HOLD | ACTIVE | LOW confidence correctly applied · HOLD enforced |
| 6. Attention | 6a Signal Detection | ACTIVE | Aggregate parity as key uncertainty signal |
| 7. Communication | 7a Output Clarity | ACTIVE | HOLD gate communicated clearly in output |
| 8. Verification | 8a Source Tier · 8b Token Status | ACTIVE | $VASCO active confirmed · result verified |
| 9. Learning | 9a Modifier Update | ACTIVE | CDI gap flagged for future improvement |
| 10. Integration | 10a Cross-layer | ACTIVE | 5/6 layers integrated · CDI absent noted |
| 11. Calibration | 11a Direction · 11b Confidence | ACTIVE | CORRECT ✅ · LOW confidence well-calibrated |
| 12. Adaptation | 12a Regime Detection | ACTIVE | CAPITULATION correctly detected and applied |
| 13. Ethics | 13a Transparency | ACTIVE | CDI absence disclosed · no fabricated modifier |
| 14. Transparency | 14b Modifier Disclosure | ACTIVE | All modifiers stated · HOLD reasoning visible |
| 15. Execution | 15a Entry Discipline | ACTIVE | HOLD enforced on correct call — gate architecture validated |
| 16. Collaboration | 16a Context Handoff | ACTIVE | Record structured for future CDI file cross-reference |

---

## Source and Verification

```
Signal submission: SportMind MCP · sportmind_pre_match
  Submitted: pre-kickoff · 2026-07-29 · 23:00 BST · TFM6 ✅

Result verification:
  Source: CONMEBOL.com (Tier 1)
  Full-time: Vasco da Gama 1–0 Independiente Medellín ✅
  Aggregate: 3–2 · Vasco advance ✅

Token verification:
  $VASCO: ACTIVE · Chiliz Chain · verified fantokens.com ✅

Record backfill note:
  Original record created v4.1.75 · 2026-07-30 · pre-template format.
  Full rewrite to current template standard at v4.6.27.
  All signal values preserved from original submission.
  No retroactive signal modification — base score 55.0,
  direction HOME, confidence LOW (post-CAPITULATION),
  HOLD gate enforced — all match original submission.
```

---

© 2026 SportMind
