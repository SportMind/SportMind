---
name: trust-breakdown-intelligence
description: >
  Judgment framework for situations where trust breakdown between parties makes
  standard financial and governance modifiers unreliable. Covers three-level
  trust breakdown classification, the five-step Judgment reasoning chain for
  when to suspend normal modifiers, and restoration triggers. Teaches agents
  when NOT to apply standard financial reasoning — the core Judgment function.
  First MIND DIMENSION GAP identified by SMI and actioned.
---

# Trust Breakdown Intelligence

**When to suspend standard financial reasoning — the Judgment dimension.**
Standard financial modifiers assume good faith even under difficulty.
Trust breakdown is categorically different and requires a separate framework.

---

## The Judgment problem

```
STANDARD FINANCIAL MODIFIERS ASSUME:
  Buyer wants to complete but faces funding difficulty.
  Both parties are negotiating in good faith.
  Stated positions broadly reflect actual positions.
  Documents presented reflect the actual financial situation.

TRUST BREAKDOWN CHANGES ALL OF THESE ASSUMPTIONS:
  One party may be deliberately misrepresenting their position.
  Documents presented may not reflect actual financial status.
  Stated positions may be tactical rather than honest.
  Normal financial valuation logic produces false signals.

CONSEQUENCE OF APPLYING WRONG FRAMEWORK:
  An agent reasoning from LIQUIDITY_FAILURE during a trust breakdown:
  → Underestimates collapse probability (assumes funding problem is solvable)
  → Overestimates recovery probability (assumes good faith resolution path)
  → Applies wrong CDI modifier (too lenient)

THE DIAGNOSTIC QUESTION:
  "Is this a party that wants to complete but cannot?
   Or a party that is misrepresenting their ability to complete?"
  If the answer is the second: LIQUIDITY_FAILURE does not apply.
  Apply the trust breakdown framework instead.
```

---

## Three-level trust breakdown classification

```
LEVEL 1 — EARLY TENSION:
  Signals:
    One party makes public statements that contradict private communications.
    Advisers begin making anonymous briefings to press.
    Minor document discrepancies emerge between versions.
    Communication becomes more formal than situation warrants.
  Assessment: trust is fraying but not broken. Standard modifiers still apply
    with a confidence discount.
  Modifier: apply ×0.95 confidence weight to all positive governance signals.
  Monitor for escalation to Level 2.

LEVEL 2 — ACTIVE MISTRUST:
  Signals:
    Formal complaints between parties transmitted via legal channels.
    Lawyers becoming the primary communication channel, not principals.
    Board members or advisers briefing media with language indicating paranoia
      or strategic distrust rather than reassurance.
    Verification documents not produced when formally requested — especially:
      Bank-verified escrow not produced when required.
      Intention document presented instead of proof of funds.
      Third-party confirmation absent despite repeated requests.
  Assessment: trust has broken down. Standard LIQUIDITY_FAILURE modifier
    no longer applies — it was calibrated for good-faith failure.
    Collapse probability is materially higher than a standard funding failure.
  Modifier: TRUST_BREAKDOWN ×0.72 CDI sustained.
    Suspend standard LIQUIDITY_FAILURE modifier entirely.
    Do not stack — TRUST_BREAKDOWN replaces, not adds.
  Communication: must explicitly state the modifier substitution.

LEVEL 3 — TERMINAL BREAKDOWN:
  Signals:
    One party publicly disputes terms that were previously formally agreed.
    Official termination notices issued by either party.
    Regulatory bodies or competition authorities notified of failure.
    Media reporting terminal collapse using crisis language (not speculation).
    Parties stop communicating through any channel, including legal.
  Assessment: collapse is highly probable. All positive signals suspended.
  Modifier: TRUST_COLLAPSE_IMMINENT flag.
    Collapse probability above 80%.
    Apply ×0.60 CDI floor.
    Suspend all positive governance signals for the affected entity.

LEVEL ESCALATION RULE:
  If Level 2 conditions are met and no resolution signals appear within
  the exclusivity or negotiating window: escalate to Level 3 automatically.
  Do not wait for explicit confirmation — absence of resolution is itself
  a signal when a deadline is structurally embedded in the situation.
```

---

## Reference case: Sevilla 2026

```
SEVILLA FC OWNERSHIP TRANSITION — TRUST BREAKDOWN REFERENCE CASE

This case is the first documented trust breakdown scenario in SportMind's
calibration history. It establishes the template for future similar situations.

STRUCTURAL PATTERN (enduring — not current status):
  A prospective buyer presented an intention document when bank-verified
  escrow was required by the club as proof of funds.
  Board communications indicated strategic distrust rather than reassurance.
  This pattern is distinct from standard LIQUIDITY_FAILURE:
    Standard: buyer cannot raise funds.
    This case: verification of funds was refused or substituted.

CLASSIFICATION AT TIME OF DOCUMENTATION: Level 2 — Active Mistrust.

MODIFIER APPLIED: TRUST_BREAKDOWN ×0.72 CDI.
  Standard LIQUIDITY_FAILURE modifier was suspended.

FAN TOKEN IMPLICATION ($SEVILLA):
  $SEVILLA governance signals were treated as unreliable during Level 2.
  Governance vote participation data from this period carries reduced weight.
  Apply ×0.80 confidence to any governance data produced during the
  trust breakdown window when retrospectively assessing $SEVILLA signals.

CALIBRATION OUTCOME (when confirmed — pending at library compilation):
  This case will produce a confirmed outcome.
  Record as: TRUST_BREAKDOWN_CASE_001
  Outcome options: deal collapsed / trust restored / extended limbo.
  The confirmed outcome directly validates or challenges the ×0.72 modifier.
```

---

## REASONING CHAIN — TRUST BREAKDOWN

```
STEP 1 — DIAGNOSE: FINANCIAL FAILURE OR TRUST BREAKDOWN?

  Financial failure indicators:
    Buyer acknowledges funding difficulty.
    Replacement investor being sought openly.
    Regulatory filings reflect genuine attempts to complete.
    Documents requested are being produced, even if delayed.

  Trust breakdown indicators:
    Documents produced do not match what was required.
    Buyer's actions contradict buyer's stated position.
    Third-party confirmations requested but not provided.
    Advisers briefing media with language suggesting deception.

  If trust breakdown indicators are present:
    Do not apply LIQUIDITY_FAILURE. Proceed to Step 2.

STEP 2 — SUSPEND STANDARD MODIFIERS.

  Standard financial modifiers suspended for this situation:
    LIQUIDITY_FAILURE ×0.78 — suspended.
    TAKEOVER_COLLAPSED (standard) — suspended.
    INVESTOR_WITHDRAWAL_COLLAPSE — suspended.
  These modifiers assume good faith. They do not apply.

STEP 3 — APPLY TRUST BREAKDOWN LEVEL.

  Assess signals against Level 1 / Level 2 / Level 3 criteria above.
  Apply the corresponding modifier.
  Level 1: ×0.95 confidence on positive signals.
  Level 2: TRUST_BREAKDOWN ×0.72 CDI (replaces standard modifiers).
  Level 3: TRUST_COLLAPSE_IMMINENT. ×0.60 CDI floor. All positive signals suspended.

STEP 4 — COMMUNICATE THE SUBSTITUTION EXPLICITLY.

  Required output language:
  "Standard LIQUIDITY_FAILURE modifier suspended.
   TRUST_BREAKDOWN [Level X] modifier applied instead.
   Normal financial reasoning does not apply in this context."

  Do not present trust breakdown analysis as if standard modifiers apply.
  The substitution must be visible in the output.

STEP 5 — SET RESOLUTION TRIGGERS.

  What would restore good faith and allow return to standard modifiers?

  Tier 1 restoration signals:
    Bank-verified escrow produced and confirmed by independent third party.
    Regulatory filing submitted confirming deal structure.
    New buyer with verified proof of funds confirmed.

  Tier 2 restoration signals:
    Third-party mediator formally appointed and accepted by both parties.
    Public statement from both principals acknowledging resolution framework.

  Tier 1 restoration: return directly to standard financial modifiers.
  Tier 2 restoration only: reduce to Level 1 (×0.95 confidence discount).
    Maintain monitoring for full resolution before returning to standard.
```

---

## Scenario intelligence connection

```
WHEN TRUST BREAKDOWN (LEVEL 2 OR 3) IS CONFIRMED:
  Build a three-scenario map using core/scenario-intelligence.md.

  Scenario 1 — TRUST_RESTORED:
    Assign probability based on: Tier 1 restoration signals present?
    Time remaining in exclusivity or negotiating window?
    History of prior similar situations resolving positively?

  Scenario 2 — DEAL_COLLAPSED:
    Assign probability based on: Level of breakdown confirmed.
    Number of Level 2/3 signals simultaneously present.
    History of escalating vs de-escalating communications.

  Scenario 3 — EXTENDED_LIMBO:
    Assign probability based on: Structural incentives for delay.
    Absence of hard deadlines that force resolution.
    Third-party mediator involvement that could slow but not resolve.

  The three scenario probabilities must sum to 100%.
  Report as: "Trust breakdown active. Three-scenario map required."
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches how to identify trust breakdown signals that indicate a situation has moved beyond standard financial reasoning — specifically the distinction between a party that cannot fund versus a party that is misrepresenting their ability to fund.

**Reasoning:** Provides the three-level trust breakdown classification and the five-step Judgment reasoning chain — from diagnosis through modifier suspension, level assignment, explicit communication, and restoration trigger setting.

**Context:** Applies to any M&A, ownership transition, or commercial negotiation where evidence of misrepresentation or bad faith has emerged. Not applicable to routine financial distress. The trigger is specific conduct evidence, not general financial difficulty.

**Memory:** Draws on the Sevilla 2026 reference case (TRUST_BREAKDOWN_CASE_001) as the first documented trust breakdown scenario in SportMind's calibration history. Future similar situations should be cross-referenced against this case pattern.

**Judgment:** This file IS the Judgment framework. Its primary purpose is teaching agents when NOT to apply standard financial reasoning — knowing what you do not know, and explicitly communicating that standard modifiers have been suspended. The Judgment function is the substitution decision, not the modifier value.

**Attention:** Trust breakdown signals require elevated Attention — they are rare but high-impact. When Level 2 or Level 3 signals are present, all governance and financial signals for the affected entity should be treated as unreliable until trust is restored. Do not process these signals through standard frameworks.

**Learning:** Each trust breakdown case that reaches a confirmed outcome (deal collapsed / trust restored / extended limbo) directly validates or challenges the modifier values in this framework. TRUST_BREAKDOWN_CASE_001 (Sevilla 2026) is the first such calibration data point.

**Integration:** Trust breakdown integrates simultaneously with governance intelligence (fan-token/governance-intelligence.md), financial intelligence (market/club-ownership-intelligence.md), scenario intelligence (core/scenario-intelligence.md), and the takeover framework (fan-token/governance-takeover-framework.md). All four must be recalibrated under trust breakdown conditions when Level 2 or above is confirmed.

---

## Compatibility

**Ownership transitions:**     `market/club-ownership-intelligence.md`
**Takeover framework:**        `fan-token/governance-takeover-framework.md`
**Scenario intelligence:**     `core/scenario-intelligence.md`
**Signal confidence:**         `core/signal-confidence-framework.md`
**Error correction:**          `core/error-correction-framework.md`

---

*SportMind v3.97.83 · MIT License · sportmind.dev*
*Trust breakdown: suspend standard financial modifiers. Apply TRUST_BREAKDOWN [level] instead.*
*Level 1 ×0.95 confidence | Level 2 ×0.72 CDI | Level 3 ×0.60 CDI floor.*
*First MIND DIMENSION GAP identified by SMI — Judgment dimension.*
