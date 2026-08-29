---
record: UCL-FINAL-2026 (legacy: R130)
audit-version: 1.0.0
framework: core/reasoning-audit-framework.md
audited-by: Human (Strategy Chat 22)
audit-date: 2026-08-29
calibration-record: calibration/2026/ucl-final-psg-vs-arsenal-2026-05-30.md
library-version-at-audit: v4.6.44
library-version-at-signal: v3.97.96
library-version-at-backfill: v4.6.30
overall: GREEN
record-type: pre-match verified · dual-token · $AFC PATH_2 ACTIVE
regime-at-signal: ANXIETY ×1.00 (pre-CAPITULATION)
---

# Reasoning Audit — UCL Final 2025/26
## Paris Saint-Germain vs Arsenal · Puskás Aréna · Budapest · 2026-05-30
## Audit 8 of 10 prospective
## Note: Pre-match verified · ANXIETY ×1.00 regime · dual-token · $AFC PATH_2 ACTIVE
## Signal at library v3.97.96 · backfilled to template standard at v4.6.30

---

## Verdict Summary

| Layer | Dimension | Verdict |
|---|---|---|
| L1 — Intelligence | Dim 1 | PARTIAL |
| L2 — Reasoning | Dim 2 | PASS |
| L3 — Context | Dim 3 | PASS |
| L4 — Judgment | Dim 5 | PASS |
| L5 — Verification | Dim 8 | PARTIAL |
| L6 — Execution | Dim 15 | PASS |

**OVERALL: GREEN**
4 PASS · 2 PARTIAL · 0 FAIL. No Layer 4 FAIL. GREEN threshold met.

---

## Layer 1 — Intelligence (Mind Dimension 1)

**Verdict: PARTIAL**

- $PSG verified on Chiliz Chain ✓
- $AFC verified on Chiliz Chain ✓
- Sport framework: sports/football/sport-domain-football.md
  explicitly referenced ✓
- Signal generated MCP server v3.97.96 at T-48h ✓
- Result source: UEFA.com (Tier 1) ✓
- Signal classification: ANXIETY regime · occasion weight ×2.00 ·
  NEUTRAL venue · PATH_2 · dual-token · CDI both tokens —
  all correctly categorised ✓
- PTG: UCL correctly NOT PTG-eligible ✓
- $AFC PATH_2: correctly identified and loaded —
  Model 2 (Prediction Market) ✓
- dual-fan-token-match-dynamics.md: explicitly confirmed loaded ✓
  — FIRST record in audit series to explicitly confirm this
- chiliscan.com: NOT referenced for token verification — stated as
  verified but no on-chain source URL documented
- PATH_2 pre-liquidation: ~111,500 $AFC noted with
  "chiliscan.com confirmation pending within 48h post-match"
  — partial on-chain citation

Both tokens verified. Tier 1 result source. Sport framework and
PATH_2 both correctly loaded. dual-fan-token-match-dynamics.md
explicitly confirmed — first record in audit series to do so.
chiliscan.com not cited for token verification — consistent
football template gap (7 of 7 football records).

---

## Layer 2 — Reasoning (Mind Dimension 2)

**Verdict: PASS**

- Loading order: Macro (ANXIETY ×1.00) → Sport domain (UCL Final
  ×2.00) → Form (NEUTRAL — both strong) → H2H (INSUFFICIENT
  SAMPLE — Final stage) → Regime ($AFC UK · $PSG France) →
  CDI (both CONSOLIDATION · dual-fan-token-match-dynamics.md) ✓
- Modifier sequence: base 29.0 → ×1.00 (ANXIETY) → ×2.00
  (occasion) → 58.0 — clean and fully traceable ✓
- ANXIETY regime correctly applied: neutral modifier · does not
  suppress · CAPITULATION distinction explicitly documented with
  counterfactual (40.6 under CAPITULATION) ✓ — outstanding
  regime awareness
- Score progression documented: T-48h → T-24h → T-2h → 58.0
  locked — FIRST record in audit series to document score
  evolution across pre-match window ✓
- Dual-token compound: both CDI stacks assessed independently ·
  dual-fan-token-match-dynamics.md loaded · relationship type
  (ALIGNED/ASYMMETRIC/CONFLICTED) not explicitly named in output
  — minor gap per Section 6 mandatory output format
- PATH_2 correctly handled as supply event layer alongside demand
  stack — never inside it ✓
- H2H gate: correctly INSUFFICIENT SAMPLE for Final-stage context ✓

Loading order correct and most sophisticated in audit series.
ANXIETY regime handling exemplary — CAPITULATION counterfactual
documented (unique in series). Score progression unique and
valuable. Dual-token relationship classification not explicitly
named — minor gap.

---

## Layer 3 — Context (Mind Dimension 3)

**Verdict: PASS**

- CHZ regime: ANXIETY ×1.00 correctly identified as active regime
  at signal time (May 2026 — pre-CAPITULATION) · correctly
  preserved under backfill ✓
- Occasion weight: UCL Final ×2.00 — highest tier in SportMind ✓
- Venue: Puskás Aréna · Budapest · NEUTRAL · 67,215 capacity —
  correctly classified with capacity documented ✓
- Regulatory context: uk-cryptoasset-regime.md loaded ($AFC) ✓ ·
  france.md loaded ($PSG) ✓ — both explicitly named in Signal
  Layers Applied AND Agent Rules
- PATH_2 context: correctly framed as demand context —
  supply event contingent on 90-minute result ✓

FIRST DUAL-JURISDICTION LAYER 3 PASS in the football audit series.
Both uk-cryptoasset-regime.md and france.md explicitly named in
Signal Layers and Agent Rules — equivalent to two simultaneous
REGULATORY_LOADED flags. Confirms pattern: explicit file naming
forces documentation → PASS. Absence → PARTIAL.

---

## Layer 4 — Judgment (Mind Dimension 5)

**Verdict: PASS**

- HOLD gate: NOT triggered — ANXIETY ×1.00 · adjusted score
  58.0 > 50.0 ENTER threshold — correctly not triggered ✓
- ENTER gate: ENTER correctly applied · direction PSG ✓
- Regime judgment: ANXIETY correctly identified as neutral ·
  ENTER eligible ✓
- Counterfactual: "Under CAPITULATION, same base (29.0) × ×2.00
  × ×0.70 = 40.6 — below ENTER threshold" documented ✓ —
  ONLY record in audit series to document this
- Confidence progression: MEDIUM T-48h → MEDIUM-HIGH T-2h ·
  correctly calibrated to information arrival ✓
- PATH_2 judgment: DRAW correctly identified on 90-minute
  rule — no supply event ✓
- Correction transparency: initial LOSS/MINT filing error
  documented · corrected at v4.0.0 · rule documented in
  defi-integration-intelligence.md ✓ — exemplary transparency
- Flags: NEUTRAL_VENUE · PATH2_ACTIVE · LINEUP_CHECK_REQUIRED ·
  DSM_CHECK_REQUIRED · PTG_NOT_APPLICABLE — all appropriate and
  resolved ✓

Outstanding Layer 4. ENTER correctly applied under ANXIETY with
full regime justification and CAPITULATION counterfactual.
PATH_2 DRAW correctly identified on 90-minute rule. Correction
transparency exemplary — LOSS/MINT error, correction, and rule
documentation form the most important calibration lesson in series.

---

## Layer 5 — Verification (Mind Dimension 8)

**Verdict: PARTIAL**

- Gate 1 TFM6: signal 2026-05-28 · kickoff 2026-05-30 17:00 UTC
  — T-48h · clearly compliant ✓
- Token active status: both $PSG and $AFC stated as verified ✓
- Result source: UEFA.com — Tier 1 ✓
- PATH_2 verification: fantokens.com/fan-token-play — DRAW
  confirmed · 0 burned · 0 minted ✓ — explicit Tier 2 citation
- chiliscan.com: referenced only as pending for PATH_2
  pre-liquidation — not completed Tier 1 on-chain verification
  for token status
- PTG: N/A confirmed ✓
- Correction documented in defi-integration-intelligence.md ✓

Gate 1 clearly documented at T-48h. Result Tier 1. PATH_2
verified via fantokens.com. chiliscan.com referenced as pending
but not completed — consistent football template gap.

PATTERN ABSOLUTE: 7 of 7 football records PARTIAL on Layer 5.
The football CALIBRATION-RECORD-TEMPLATE.md lacks a dedicated
on-chain verification field. Single template addition resolves
this entire class for future records.

---

## Layer 6 — Execution (Mind Dimension 15)

**Verdict: PASS**

- Mandatory fields: DIRECTION ✓ · BASE SCORE ✓ · CHZ MODIFIER ✓ ·
  ADJUSTED SCORE ✓ · CONFIDENCE ✓ · ACTION (ENTER) ✓ ·
  FLAGS ✓ — all present ✓
- PATH_2 execution: full section — pre-liquidation amount ·
  outcome gates documented · DRAW settlement · correction note ·
  supply change 0 — most complete PATH_2 execution block in
  library ✓
- Dual-token: both tokens documented · dual-fan-token-match-
  dynamics.md confirmed ✓
- Agent Rules: 16 rules documented — largest rule set audited ✓
- MIND DIMENSIONS: full 16 of 16 — backfill at v4.6.30 ✓
- Directory: calibration/2026/ — correct for this record type ✓
- Score progression in execution block ✓
- Correction note preserved in four locations (frontmatter ·
  PATH_2 section · source block · footer) ✓

Outstanding Layer 6. Full 16 MIND DIMENSIONS via backfill.
16 agent rules — largest set in audit series. PATH_2 execution
most complete in library. Correction preserved in four locations
— exemplary transparency and execution discipline.

---

## Key Findings

**Strengths — richest record in the audit series:**
- ANXIETY regime handling exemplary — correctly identified,
  preserved under backfill, explicitly distinguished from
  CAPITULATION with counterfactual (40.6 under CAPITULATION).
  Only record in audit series to document the counterfactual.
- Score progression T-48h → T-24h → T-2h documented — unique in
  series; demonstrates live signal evolution discipline under
  information arrival.
- First dual-jurisdiction Layer 3 PASS — both uk-cryptoasset-
  regime.md and france.md explicitly loaded. Confirms pattern:
  explicit regulatory file naming → Layer 3 PASS.
- PATH_2 DRAW correctly identified on 90-minute rule — first live
  PATH_2 record in audit series.
- Correction transparency exemplary — initial LOSS/MINT error
  documented, corrected at v4.0.0, preserved in four locations,
  rule documented in defi-integration-intelligence.md. Most
  important calibration lesson in the series.
- dual-fan-token-match-dynamics.md explicitly confirmed loaded —
  first record in audit series to do so.
- 16 agent rules — largest set audited.

**Gaps:**
- Layer 1 PARTIAL: chiliscan.com not cited for token verification
  — football template gap, 7 of 7 football records.
- Layer 5 PARTIAL: chiliscan.com referenced only as pending —
  7 of 7 football records now PARTIAL. Pattern absolute.
- Dual-token relationship type (ALIGNED/ASYMMETRIC/CONFLICTED)
  not explicitly named in output — minor gap per dual-fan-token-
  match-dynamics.md Section 6 mandatory output format.

**Pattern updates:**
- Layer 5: 7 of 7 football records PARTIAL — absolute. Template
  fix is the only remedy.
- Layer 3: Second dual-jurisdiction PASS. Pattern confirmed —
  explicit regulatory file naming → PASS. Absence → PARTIAL.
- New minor gap identified: dual-token relationship classification
  not named. Flag for template review — should appear in all
  future dual-token records.

---

## Audit Metadata

```
Record:              UCL Final 2025/26 (legacy: R130)
Match:               Paris Saint-Germain vs Arsenal
Competition:         UEFA Champions League Final 2025/26
Date:                2026-05-30
Record type:         Pre-match verified · dual-token · $AFC PATH_2 ACTIVE
Regime at signal:    ANXIETY ×1.00 (pre-CAPITULATION)
Calibration file:    calibration/2026/ucl-final-psg-vs-arsenal-2026-05-30.md
Audit file:          community/calibration-data/audits/audit-ucl-final-psg-vs-arsenal-2026-05-30.md
Audited by:          Human (Strategy Chat 22 · 2026-08-29)
Framework version:   reasoning-audit-framework.md v1.0.0
Library at audit:    v4.6.44
Library at signal:   v3.97.96
Library at backfill: v4.6.30
Prospective audit:   8 of 10
Overall verdict:     GREEN
Layer breakdown:     L1 PARTIAL · L2 PASS · L3 PASS · L4 PASS · L5 PARTIAL · L6 PASS
Direction result:    CORRECT ✅ (PSG)
Gate result:         ENTER — CORRECT ✓ (ANXIETY ×1.00 · 58.0 > 50.0)
PATH_2 outcome:      DRAW — no supply event · 0 burned · 0 minted ✓
Notable:             Richest record in audit series — ANXIETY regime ·
                     T-48h score progression · dual-jurisdiction Layer 3 ·
                     PATH_2 DRAW · exemplary correction transparency ·
                     16 agent rules · dual-fan-token-match-dynamics.md confirmed
```

---

*SportMind v4.6.44 · MIT License · sportmind.dev*
*Reasoning Audit Framework v1.0.0*
*Audit: UCL Final 2025/26 · GREEN · 8 of 10 prospective*
