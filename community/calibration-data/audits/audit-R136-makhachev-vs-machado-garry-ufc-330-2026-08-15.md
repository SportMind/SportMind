---
record: R136
audit-version: 1.0.0
framework: core/reasoning-audit-framework.md
audited-by: Human (Strategy Chat 22)
audit-date: 2026-08-28
calibration-record: community/calibration-data/mma/ufc-330-makhachev-vs-machado-garry-2026-08-15.md
library-version-at-audit: v4.6.37
overall: GREEN
---

# Reasoning Audit — R136
## UFC 330 · Islam Makhachev vs Ian Machado Garry · 2026-08-15
## Audit 3 of 10 prospective

---

## Verdict Summary

| Layer | Dimension | Verdict |
|---|---|---|
| L1 — Intelligence | Dim 1 | PASS |
| L2 — Reasoning | Dim 2 | PASS |
| L3 — Context | Dim 3 | PARTIAL |
| L4 — Judgment | Dim 5 | PASS |
| L5 — Verification | Dim 8 | PASS |
| L6 — Execution | Dim 15 | PASS |

**OVERALL: GREEN**
5 PASS · 1 PARTIAL · 0 FAIL. No Layer 4 FAIL. GREEN threshold met.

---

## Layer 1 — Intelligence (Mind Dimension 1)

**Verdict: PASS**

- $UFC verified active on Chiliz Chain — contract address documented ✓
- Token source: fantokens.com (Tier 2) used as cross-check alongside
  chiliscan.com contract reference ✓
- Sport framework: sports/mma/mma-intelligence-framework.md explicitly
  referenced and loaded ✓
- Event confirmed: ufc.com (Tier 1) ✓
- Weigh-in confirmed: UFC ceremonial weigh-in 2026-08-14 ✓
- Signal classification: archetype, card tier, occasion weight, regime —
  all correctly categorised for MMA context ✓
- No aggregator used as sole primary source ✓

Token verified on-chain via chiliscan.com contract reference. Tier 1
event source used. MMA framework confirmed loaded. Signal classification
appropriate for MMA org-level token context.

---

## Layer 2 — Reasoning (Mind Dimension 2)

**Verdict: PASS**

- Loading order: Macro (CAPITULATION ×0.70) → Form (MMA archetype
  analysis) → H2H (N/A — correctly skipped · first meeting at weight
  class) → Occasion (NUMBERED_PPV +++) → CDI (N/A — org-level token ·
  correctly skipped) ✓
- Modifier sequence: base score 55.0 → ×0.70 → 38.5 — single clean
  step, correctly documented ✓
- Compound synthesis: simple single-token single-modifier chain —
  fully traceable ✓
- MMA layer skips: H2H and CDI correctly skipped per MMA framework
  rules · explicitly documented with justification ✓
- SA intelligence layer: N/A ✓

Loading order correct for MMA context. Modifier sequence clean and
traceable. Layer skips documented with justification — not penalised
for correct framework application. Compound synthesis appropriate for
single-token org-level record.

---

## Layer 3 — Context (Mind Dimension 3)

**Verdict: PARTIAL**

- CHZ regime: CAPITULATION ×0.70 correctly identified and applied ✓
- Occasion weight: NUMBERED_PPV (+++) maximum MMA card weight —
  correct for UFC 330 title fight ✓
- Venue: Xfinity Mobile Arena · Philadelphia · NEUTRAL — no fortress
  modifier · correctly applied ✓
- Regulatory context: record notes "Regulatory: N/A — no
  jurisdiction-specific flag for this record." USA is the host
  jurisdiction. USA regulatory file exists (intelligence/country-scan/
  usa.md · holder-tax-framework.md Rule 11 — CONDITIONAL LONG HOLD
  BIAS + SEC UNCERTAINTY SUPPRESSOR). However, $UFC is an org-level
  token with global holder base and ~$120 daily volume — no
  jurisdiction-driven demand pressure dominates the signal. The N/A
  call is defensible given micro-cap context but was not documented
  with explicit reasoning.

Regime and occasion weight correct. Venue correct. USA regulatory
context not explicitly considered or documented. Defensible given
org-level token and micro-cap status, but the reasoning for N/A
should appear in the record.

NOTE: Layer 3 PARTIAL in all three audits to date (R137 · R132 ·
R136). Pattern consistent — regulatory loading documentation is the
recurring gap. Flag for 10-audit pattern review.

---

## Layer 4 — Judgment (Mind Dimension 5)

**Verdict: PASS**

- HOLD gate: adjusted score 38.5 < 80 threshold — HOLD correctly
  triggered ✓
- HOLD gate: DUAL grounds documented — CAPITULATION ×0.70 AND
  MICRO_CAP_ILLIQUIDITY independently sufficient ✓ — strongest HOLD
  gate documentation of any audit to date
- Uncertainty flags: 7 standard flags + 7 MMA-specific flags — all
  appropriate and resolved ✓
- Confidence tier: MEDIUM — correct given archetype uncertainty
  (elite grappler vs elite striker) and challenger momentum ✓
- PATH_2: not applicable · correctly absent ✓

HOLD gate applied on dual independent grounds — most thoroughly
documented HOLD gate of any audit to date. All uncertainty flags
present and appropriate. MEDIUM confidence well-calibrated — Garry
was genuinely competitive across 25 minutes. PATH_2 correctly absent.

---

## Layer 5 — Verification (Mind Dimension 8)

**Verdict: PASS**

- Gate 1 TFM6: "GitHub Issue submitted pre-kickoff ✓ COMPLIANT" —
  explicitly documented ✓
- Token active status: $UFC confirmed Chiliz Chain via contract
  address ✓
- Event source: ufc.com (Tier 1) ✓
- Weigh-in source: UFC ceremonial weigh-in confirmed — Tier 1 ✓
- chiliscan.com: explicitly referenced — "chiliscan.com/token/
  0x0ffa63502f957b66e61F87761cc240e51C74cee5 ✓" ✓
- PTG: N/A — $UFC has no PTG mechanics ✓

Gate 1 documented. All sources Tier 1. Token verified on-chain with
direct contract reference. chiliscan.com explicitly cited in Source
and Verification block.

PATTERN NOTE: R136 PASSES Layer 5 where R137 and R132 were PARTIAL.
The difference is the explicit chiliscan.com citation in the Source
and Verification section of this record. The MMA record template
includes a dedicated verification block — the football calibration
record template does not. This is a template-level gap, not a process
gap. Recommended fix: add explicit chiliscan.com verification field
to football CALIBRATION-RECORD-TEMPLATE.md. Flag for 10-audit pattern
review.

---

## Layer 6 — Execution (Mind Dimension 15)

**Verdict: PASS**

- Mandatory fields: DIRECTION ✓ · BASE SCORE ✓ · CHZ MODIFIER ✓ ·
  ADJUSTED SCORE ✓ · CONFIDENCE ✓ · ACTION (HOLD) ✓ · FLAGS ✓ —
  all present ✓
- PATH_2: correctly absent — $UFC is not $AFC ✓
- Dual-token modifier: N/A — single-token record · correctly
  documented ✓
- $VASCO MICRO_CAP_ILLIQUIDITY: N/A — MMA record ✓
- Agent Rules Engaged: 8 rules documented ✓
- Directory: community/calibration-data/mma/ — correct · new
  directory correctly established ✓
- MMA-specific flags section: present and complete ✓

All mandatory fields present. MMA-specific execution elements
handled correctly. New directory correctly established. Agent Rules
complete.

---

## Key Findings

**Strengths:**
- HOLD gate documented on dual independent grounds (CAPITULATION +
  MICRO_CAP_ILLIQUIDITY) — strongest HOLD gate justification of any
  audit to date
- Layer 5 PASS — chiliscan.com explicitly cited in Source and
  Verification block. This is precisely what R137 and R132 were missing
- MMA framework layer skips correctly documented with justification —
  framework flexibility applied correctly, not penalised
- MEDIUM confidence well-calibrated — Garry was genuinely competitive
  across full championship distance

**Gap:**
- Layer 3 PARTIAL: USA regulatory context (holder-tax-framework.md
  Rule 11 — CONDITIONAL LONG HOLD BIAS + SEC UNCERTAINTY SUPPRESSOR)
  not explicitly loaded or documented. N/A call defensible given
  micro-cap org-level token context, but reasoning not documented
  in the record.

**Pattern Update — Layer 3:**
Layer 3 PARTIAL in all three prospective audits (R137 · R132 · R136).
Consistent gap: regulatory loading not explicitly documented. Pattern
now established at 3 audits. Flag for 10-audit pattern review.

**Pattern Update — Layer 5 (critical):**
R136 PASSES Layer 5 — breaking the R137/R132 PARTIAL streak. Root
cause identified: the MMA record template includes a dedicated Source
and Verification block with explicit chiliscan.com reference. The
football CALIBRATION-RECORD-TEMPLATE.md does not. This is a
template-level fix, not a process change. Recommendation: add explicit
chiliscan.com verification field to football template at next Build
Chat session covering template maintenance.

---

## Audit Metadata

```
Record:              R136
Match:               Islam Makhachev vs Ian Machado Garry
Competition:         UFC 330 — Welterweight Championship
Date:                2026-08-15
Calibration file:    community/calibration-data/mma/ufc-330-makhachev-vs-machado-garry-2026-08-15.md
Audit file:          community/calibration-data/audits/audit-R136-makhachev-vs-machado-garry-ufc-330-2026-08-15.md
Audited by:          Human (Strategy Chat 22 · 2026-08-28)
Framework version:   reasoning-audit-framework.md v1.0.0
Library at audit:    v4.6.37
Prospective audit:   3 of 10
Overall verdict:     GREEN
Layer breakdown:     L1 PASS · L2 PASS · L3 PARTIAL · L4 PASS · L5 PASS · L6 PASS
Direction result:    CORRECT ✅
Gate result:         HOLD — CORRECT ✓ (dual grounds)
```

---

*SportMind v4.6.37 · MIT License · sportmind.dev*
*Reasoning Audit Framework v1.0.0*
*Audit: R136 · GREEN · 3 of 10 prospective*
