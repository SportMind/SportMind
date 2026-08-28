---
record: R132
audit-version: 1.0.0
framework: core/reasoning-audit-framework.md
audited-by: Human (Strategy Chat 22)
audit-date: 2026-08-28
calibration-record: community/calibration-data/football/super-cup-psg-vs-avl-2026-08-12.md
library-version-at-audit: v4.6.37
overall: GREEN
---

# Reasoning Audit — R132
## UEFA Super Cup 2026 · Paris Saint-Germain vs Aston Villa · 2026-08-12
## Audit 2 of 10 prospective

---

## Verdict Summary

| Layer | Dimension | Verdict |
|---|---|---|
| L1 — Intelligence | Dim 1 | PASS |
| L2 — Reasoning | Dim 2 | PASS |
| L3 — Context | Dim 3 | PARTIAL |
| L4 — Judgment | Dim 5 | PASS |
| L5 — Verification | Dim 8 | PARTIAL |
| L6 — Execution | Dim 15 | PASS |

**OVERALL: GREEN**
4 PASS · 2 PARTIAL · 0 FAIL. No Layer 4 FAIL. GREEN threshold met.

---

## Layer 1 — Intelligence (Mind Dimension 1)

**Verdict: PASS**

- $PSG verified active on Chiliz Chain ✓
- $AVL verified active on Chiliz Chain ✓
- Sport framework: sports/football/sport-domain-football.md explicitly referenced ✓
- Match result source: UEFA.com (Tier 1) ✓
- Signal classification: form, H2H, venue, regime, CDI all correctly categorised ✓
- No aggregator used as primary source ✓

All tokens verified on-chain. Tier 1 sources throughout. Sport framework
confirmed loaded. Signal classification complete across all categories.

---

## Layer 2 — Reasoning (Mind Dimension 2)

**Verdict: PASS**

- Loading order: Macro (CAPITULATION ×0.70) → Sport (occasion weight) →
  Form → H2H (FAIL — flagged) → Regime (Champion Call) → CDI ($PSG
  CONSOLIDATION→GROWTH · $AVL GROWTH) ✓
- Modifier sequence: CHZ regime applied first, then occasion uplift
  post-compression, then CDI within base score ✓
- Compound synthesis: explicit and traceable — score derivation section
  documents each step for both tokens ✓
- Dual-token CDI asymmetry: $PSG CONSOLIDATION→GROWTH vs $AVL GROWTH
  correctly applied with CDI gap documented ✓
- SA intelligence layer: N/A — neither club is a South American token ✓

Loading order correct and documented. Modifier sequence traceable.
Compound synthesis explicit for both tokens. CDI asymmetry correctly applied.

---

## Layer 3 — Context (Mind Dimension 3)

**Verdict: PARTIAL**

- CHZ regime: CAPITULATION ×0.70 correctly identified and applied ✓
- Occasion weight: +0.05 pre-compression · +0.035 post-compression for
  UEFA Super Cup prestige one-off ✓ — tier appropriate
- Venue: Red Bull Arena · Salzburg · NEUTRAL correctly identified ·
  home designation cosmetic only · not applied ✓
- Regulatory context: PSG = France (macro/regulatory/france.md · 30% PFU
  Type C) · AVL = UK (holder-tax-framework.md · Type D CGT) — neither
  file explicitly referenced or loaded in the record

Regime, occasion weight, and venue all correct. France and UK regulatory
files not explicitly referenced. Given CAPITULATION regime was dominant
and HOLD gate fired, the omission had no impact on signal output — but
the framework requires regulatory loading for jurisdictions with active
files.

---

## Layer 4 — Judgment (Mind Dimension 5)

**Verdict: PASS**

- HOLD gate: both adjusted scores below 80 threshold
  ($PSG 50.0 · $AVL 45.2) — HOLD correctly triggered under
  CAPITULATION ×0.70 ✓
- HOLD gate reasoning: documented explicitly and at length ✓
- Uncertainty flags raised: H2H_GATE_FAIL · LINEUP_UNCONFIRMED ·
  VENUE_NEUTRAL · CHZ_CAPITULATION_ACTIVE — all appropriate ✓
- Confidence tier: MODERATE — correct given H2H FAIL, genuine
  competitive uncertainty, and Villa scored ✓
- PATH_2: $AFC not involved — correctly noted as N/A ✓

HOLD gate correctly applied and documented. All warranted uncertainty
flags present. MODERATE confidence appropriate and validated by match
character (Villa scored, match was competitive). PATH_2 correctly handled.

---

## Layer 5 — Verification (Mind Dimension 8)

**Verdict: PARTIAL**

- Gate 1 TFM6: "Recorded at: 2026-08-12 pre-kickoff (TFM6 Gate 1 ✓)"
  explicitly confirmed ✓
- Token active status: both $PSG and $AVL confirmed Chiliz Chain
  verified ✓
- Match result source: UEFA.com — Tier 1 ✓
- PTG: confirmed N/A — UEFA Super Cup excluded from PTG list ✓
- PATH_2: confirmed N/A — $AFC not involved ✓
- On-chain check (chiliscan.com): not explicitly referenced in the record
  — volume and token status not documented as checked against chiliscan.com

Gate 1 met and documented. Token active status confirmed. Tier 1 result
source. However, explicit on-chain check via chiliscan.com not referenced.

PATTERN NOTE: This is the same Layer 5 gap identified in R137. Two audits,
same PARTIAL. Emerging pattern — flag for 10-audit pattern review in
Strategy Chat.

---

## Layer 6 — Execution (Mind Dimension 15)

**Verdict: PASS**

- Mandatory fields: DIRECTION ✓ · RAW SCORE ✓ · CHZ MODIFIER ✓ ·
  ADJUSTED SCORE ✓ · CONFIDENCE ✓ · ACTION ✓ · FLAGS ✓ — all present ✓
- PATH_2: correctly noted N/A ✓
- Dual-token modifier: framework engaged and documented ✓
- $VASCO MICRO_CAP_ILLIQUIDITY: N/A ✓
- Agent Rules Engaged: complete section present with all rules
  documented ✓
- Directory: community/calibration-data/football/ — correct ✓

All mandatory fields present. PATH_2 correctly handled. Dual-token
modifier applied. Agent Rules complete. Filed in correct directory.

---

## Key Findings

**Strengths:**
- HOLD gate correctly applied and thoroughly documented — the most
  critical judgment call executed perfectly
- Loading order and compound synthesis exemplary — both token score
  derivations fully traceable step by step
- Dual-token CDI asymmetry correctly handled ($PSG CONSOLIDATION→GROWTH
  vs $AVL GROWTH — gap documented and applied)
- MODERATE confidence tier validated by match character — Villa scored,
  result was not high-certainty

**Gaps:**
- Layer 3 PARTIAL: France (macro/regulatory/france.md) and UK
  (holder-tax-framework.md) regulatory files not explicitly loaded or
  referenced. Low impact given HOLD gate outcome, but regulatory loading
  should be documented for all active jurisdictions represented.
- Layer 5 PARTIAL: chiliscan.com on-chain verification not explicitly
  referenced in the record. Same gap as R137.

**Emerging Pattern — Layer 5:**
Both R137 and R132 show Layer 5 PARTIAL on the same criterion:
chiliscan.com on-chain check not documented. Two audits is early but
consistent. Flag for 10-audit pattern review. Recommendation: calibration
record template should include an explicit on-chain verification field
to prompt this step at record creation time.

---

## Audit Metadata

```
Record:              R132
Match:               Paris Saint-Germain vs Aston Villa
Competition:         UEFA Super Cup 2026
Date:                2026-08-12
Calibration file:    community/calibration-data/football/super-cup-psg-vs-avl-2026-08-12.md
Audit file:          community/calibration-data/audits/audit-R132-psg-vs-avl-super-cup-2026-08-12.md
Audited by:          Human (Strategy Chat 22 · 2026-08-28)
Framework version:   reasoning-audit-framework.md v1.0.0
Library at audit:    v4.6.37
Prospective audit:   2 of 10
Overall verdict:     GREEN
Layer breakdown:     L1 PASS · L2 PASS · L3 PARTIAL · L4 PASS · L5 PARTIAL · L6 PASS
Direction result:    CORRECT ✅
Gate result:         HOLD — CORRECT ✓
```

---

*SportMind v4.6.37 · MIT License · sportmind.dev*
*Reasoning Audit Framework v1.0.0*
*Audit: R132 · GREEN · 2 of 10 prospective*
