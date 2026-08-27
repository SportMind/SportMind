---
name: reasoning-audit-framework
version: 1.0.0
library: v4.6.37
status: ACTIVE
description: >
  Framework for auditing the process quality of SportMind calibration
  records, independent of directional outcome. Six layers mapped to Mind
  Dimensions. Traffic light summary (GREEN / AMBER / RED) with per-layer
  PASS / PARTIAL / FAIL verdicts. Output filed to
  community/calibration-data/audits/.
---

# Reasoning Audit Framework

## Purpose

Calibration records answer: *was the direction correct?*
This framework answers: *was the reasoning correctly applied?*

These are independent questions. A correct direction can result from
flawed reasoning (lucky). A wrong direction can result from sound
reasoning (unlucky — given a black swan or genuinely unforeseeable
event). Only process quality tells you whether the SportMind intelligence
stack is working as designed.

The Reasoning Audit Framework separates SportMind from prediction systems.
Prediction systems are judged solely on outcomes. SportMind is judged on
the quality of intelligence applied — outcomes provide additional signal,
but they are not the primary measure of library health.

---

## Scope

**Applies to:**
- All new pre-match verified records going forward (prospective)
- All 17 existing pre-match verified records — retroactive, after 10
  prospective audits establish the standard
- Seed records selectively — only where the reasoning chain is
  sufficiently documented to audit without inference

**Does not apply to:**
- Records where the pre-match signal chain is absent or too thin to audit
- Seed records filed without a full signal layers section

---

## Audit Layers

Six layers, each mapped to a Mind Dimension. Every layer receives a
verdict of PASS, PARTIAL, or FAIL with a one-line note.

---

### Layer 1 — Intelligence (Mind Dimension 1)

**What it checks:**
- Were sources Tier 1 (club channels, chiliscan.com, official competition
  sites) rather than aggregators?
- Were signals correctly classified (form, H2H, venue, regime, CDI)?
- Was the correct sport framework loaded?
- Was the fan token verified active on-chain before signal generation?

**PASS:** All sources Tier 1 or documented as best available. Token
verified. Sport framework confirmed loaded.

**PARTIAL:** Mix of Tier 1 and Tier 2 sources without justification.
Token verified but chain not confirmed. Sport framework loaded but not
confirmed in the record.

**FAIL:** Aggregator used as primary source. Token not verified. Wrong
sport framework loaded or no framework referenced.

---

### Layer 2 — Reasoning (Mind Dimension 2)

**What it checks:**
- Was the loading order correct? (Macro → Sport → Form → H2H → Regime
  → CDI → Regulatory — in that sequence)
- Were modifiers applied in the correct sequence?
- Was compound synthesis sound — signals correctly combined rather than
  netted or overridden without justification?
- For dual-token records: was CDI asymmetry applied correctly?
- For SA tokens: was the SA intelligence layer loaded (not individual CDI)?

**PASS:** Loading order correct and documented. Modifiers applied in
sequence. Compound synthesis explicit and traceable.

**PARTIAL:** Loading order partially documented. One modifier out of
sequence or applied without clear justification. Compound synthesis
present but opaque.

**FAIL:** Loading order absent or inverted. Modifiers applied arbitrarily.
No compound synthesis documented.

---

### Layer 3 — Context (Mind Dimension 3)

**What it checks:**
- Was the CHZ regime correctly identified and applied?
- Was occasion weight applied correctly for the competition tier?
- Was regulatory context loaded where a relevant jurisdiction was present
  (Brazilian clubs → brazil.md, Turkish clubs → turkey.md, etc.)?
- Was calendar context correct for SA tokens (August = PEAK DEMAND)?
- Was venue type and modifier correctly identified?

**PASS:** Regime correct and modifier applied. Occasion weight correct for
competition tier. All relevant regulatory files loaded. Venue tier correct.

**PARTIAL:** Regime applied but modifier value not confirmed against
current library state. Occasion weight applied but tier arguable. One
regulatory file missing where it should have been loaded.

**FAIL:** Regime not applied or wrong regime used. Occasion weight absent
for a knockout or final. Regulatory context entirely absent for a
jurisdiction with known fan token holder friction.

---

### Layer 4 — Judgment (Mind Dimension 5)

**What it checks:**
- Was the HOLD gate applied correctly under CAPITULATION regime?
  (TFM6: adjusted score must clear threshold — if not, HOLD is mandatory)
- Were uncertainty flags raised where warranted (thin H2H sample, lineup
  uncertainty, dual-signal jurisdiction)?
- Was confidence tier (HIGH / MEDIUM / LOW) appropriate given signal
  quality and sample available?
- Was PATH_2 handled correctly for $AFC fixtures?

**PASS:** HOLD gate applied correctly (or correctly not triggered).
Uncertainty flags present where signal quality demanded them. Confidence
tier defensible given available data. PATH_2 correctly separated.

**PARTIAL:** HOLD gate applied but reasoning not documented. Confidence
tier slightly mis-calibrated (HIGH where MEDIUM was warranted). One
missing flag that should have been raised.

**FAIL:** HOLD gate not applied under CAPITULATION when adjusted score
below threshold. No uncertainty flags on a thin or contested signal.
Confidence tier materially wrong. PATH_2 missing for an $AFC fixture.

---

### Layer 5 — Verification (Mind Dimension 8)

**What it checks:**
- Was on-chain data (chiliscan.com) checked for volume and token status?
- Were Tier 1 sources used for match details (UEFA.com, CONMEBOL.com,
  official club channels)?
- Was Gate 1 (TFM6) met — was the record submitted pre-kickoff?
- Was the token verified as active on Chiliz Chain (not dormant)?
- For PTG records: was the burn verified on chiliscan.com post-match?
- For PATH_2 records: was the supply event verified on fantokens.com?

**PASS:** On-chain check documented. Tier 1 sources used for match
details. Gate 1 met with submission time recorded. Token active status
confirmed.

**PARTIAL:** On-chain check referenced but not linked. Mixed source tiers
for match details. Gate 1 met but submission time not recorded.

**FAIL:** No on-chain check. Aggregator as sole match detail source.
Gate 1 not met (record filed post-kickoff). Token status not verified.

---

### Layer 6 — Execution (Mind Dimension 15)

**What it checks:**
- Are all mandatory output fields present (DIRECTION, RAW SCORE, CHZ
  MODIFIER, ADJUSTED SCORE, CONFIDENCE, ACTION, FLAGS)?
- Was PATH_2 correctly separated from the main direction signal for $AFC?
- Was dual-token modifier applied (or correctly noted as N/A)?
- Was the $VASCO MICRO_CAP_ILLIQUIDITY flag applied where relevant?
- Are Agent Rules Engaged documented?
- Is the record correctly filed in the right directory?
  (community/calibration-data/football/ for club records,
  calibration/2026/ for WC/UCL Final only)

**PASS:** All mandatory fields present. PATH_2 correctly handled.
Dual-token modifier applied or N/A documented. Agent Rules section
complete. Filed in correct directory.

**PARTIAL:** One or two minor fields missing. PATH_2 noted but not
fully separated. Agent Rules section present but incomplete.

**FAIL:** Multiple mandatory fields absent. PATH_2 absent for an $AFC
fixture. Record filed in wrong directory.

---

## Verdict Structure

Each audit produces a traffic light summary plus per-layer verdicts.

Overall verdict thresholds:

GREEN  — 5 or 6 layers PASS with no FAIL
AMBER  — mix of PASS and PARTIAL, maximum 1 FAIL
RED    — 2 or more FAILs, OR Layer 4 (Judgment) FAIL on HOLD gate

Layer 4 FAIL triggers RED regardless of other layers. The HOLD gate is
the most critical safety mechanism in the library. A missed HOLD gate
under CAPITULATION is the single most consequential reasoning failure —
it means the library recommended action when it should have stood down.

---

## Audit File Format

Each audit is a separate file in community/calibration-data/audits/

Naming convention:
audit-R[N]-[home-slug]-vs-[away-slug]-[competition-slug]-[YYYY-MM-DD].md

Example:
audit-R138-psg-vs-gal-ucl-md1-2026-09-09.md

See AUDIT-RECORD-TEMPLATE.md in community/calibration-data/audits/ for
the full file format.

---

## Process

**Mode — first 10 to 15 records:** Human-run.
Load the parent calibration record. Work through each layer against the
criteria above. Record PASS / PARTIAL / FAIL with a one-line note. File
the audit to community/calibration-data/audits/ via GitHub Desktop.

**Mode — after 15 audited records:** SMI-assisted.
SMI Chat loads the calibration record and produces a draft audit using
this framework as a checklist. Human reviews and confirms or adjusts
each layer verdict before filing. SMI never files autonomously.

**Trigger:** Every new pre-match verified record receives an audit.
Retroactive application to the 17 existing pre-match verified records
begins after 10 prospective audits establish the standard.

---

## Pattern Tracking

After every 5 audits, note which layers are producing the most PARTIAL
or FAIL verdicts. This is the map of which frameworks need strengthening.

Patterns to watch:

· Layer 2 PARTIAL repeatedly — loading order guidance needs clarifying
· Layer 3 PARTIAL repeatedly — regulatory loading triggers need tightening
· Layer 4 FAIL — most serious recurring failure — escalate immediately
· Layer 5 PARTIAL repeatedly — on-chain verification habit needs reinforcing

Aggregate pattern review: Strategy Chat, every 10 audited records.

---

## MIND DIMENSIONS

| Dimension | Sub-dimension | Status |
|---|---|---|
| 1. Intelligence | 1a Source Tier · 1b Signal Classification | ACTIVE |
| 2. Reasoning | 2a Loading Order · 2b Modifier Sequence · 2c Compound Synthesis | ACTIVE |
| 3. Context | 3a Regime Detection · 3b Occasion Weight · 3c Regulatory Context | ACTIVE |
| 4. Memory | 4a Framework Loading | ACTIVE |
| 5. Judgment | 5a HOLD Gate · 5b Uncertainty Flags · 5c Confidence Tier | ACTIVE |
| 6. Attention | 6a Signal Detection · 6b Flag Identification | ACTIVE |
| 7. Communication | 7a Verdict Clarity | ACTIVE |
| 8. Verification | 8a Source Tier · 8b Gate 1 TFM6 · 8c On-Chain | ACTIVE |
| 9. Learning | 9a Pattern Recognition across audits | ACTIVE |
| 10. Integration | 10a Cross-framework alignment | ACTIVE |
| 11. Calibration | 11c Process Quality independent of outcome | ACTIVE |
| 12. Adaptation | 12a Regime-aware audit criteria | ACTIVE |
| 13. Ethics | 13a Honest verdict — no outcome bias | ACTIVE |
| 14. Transparency | 14a Per-layer disclosure · 14b Verdict reasoning | ACTIVE |
| 15. Execution | 15a Output Fields · 15b Directory Compliance · 15c PATH_2 | ACTIVE |
| 16. Collaboration | 16a Human-SMI handoff · 16b Pattern escalation | EMERGING |

---

## Compatibility

- core/compound-signal-framework.md
- core/reasoning-framework.md
- fan-token/token-framework-master.md (TFM6 — Gate 1)
- sports/football/sport-domain-football.md
- market/south-america/south-america-fan-token-intelligence.md
- macro/regulatory/ (all 14 jurisdiction files)
- community/calibration-data/football/CALIBRATION-RECORD-TEMPLATE.md
- community/calibration-data/audits/AUDIT-RECORD-TEMPLATE.md
- community/calibration-data/audits/ (output directory — new)

---

*SportMind v4.6.37 · MIT License · sportmind.dev*
*Reasoning Audit Framework v1.0.0 · core/reasoning-audit-framework.md*
*© 2026 SportMind*
