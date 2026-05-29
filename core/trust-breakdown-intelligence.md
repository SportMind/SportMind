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

CONSORTIUM_COLLAPSE — SUB-TYPE OF TRUST_BREAKDOWN LEVEL 3:
  Definition: trust breakdown where the acquiring party is a multi-entity
  consortium rather than a single buyer. Consortium insolvency differs
  from single-buyer failure in three structurally distinct ways:

  1. BLAME DIFFUSION:
     Multiple parties can deflect responsibility between themselves.
     This extends the uncertainty window — no single party is forced
     to formally acknowledge failure while others can still claim viability.
     The public narrative fractures across multiple parties simultaneously.

  2. REPUTATION SEPARATION:
     Individual consortium members may attempt to distance their own
     reputation from the failed deal. Each member has independent
     incentive to protect their standing. This creates competing
     public narratives and makes resolution signals harder to read —
     a positive signal from one member may be contradicted by silence
     from another.

  3. DISTRIBUTED LEGAL LIABILITY:
     Recovery paths are more complex and less predictable than single-buyer
     failure. Creditors, competition authorities, and the selling club must
     negotiate with multiple parties simultaneously. Legal proceedings may
     run in parallel across different jurisdictions if members are
     incorporated in different countries.

  CONSORTIUM_COLLAPSE CDI MODIFIER:
    Apply ×0.65 CDI (vs ×0.72 for standard TRUST_BREAKDOWN_L2).
    The uncertainty compounds with each additional party involved.
    Rationale: the standard Level 2 modifier (×0.72) assumes a
    two-party negotiation with a clear resolution path. Multi-party
    collapse has no such clarity — the uncertainty premium is higher.

  RESOLUTION TIMELINE:
    Single buyer failure: typically 30 days to clear resolution signal.
    Consortium collapse:  typically 60-90 days.
    Rationale: each additional party adds negotiation complexity.
    Do not apply Level 1 restoration signals until ALL consortium members
    have either formally confirmed withdrawal or confirmed continued
    participation. Partial resolution is not resolution.

  ESCALATION RULE FOR CONSORTIUM_COLLAPSE:
    If one consortium member publicly disputes another's claims of viability:
    escalate to CONSORTIUM_COLLAPSE immediately.
    Do not wait for formal insolvency filing — the public blame diffusion
    IS the confirmation signal.

  AGENT REASONING:
    When a trust breakdown involves multiple named parties on one side:
    1. Apply CONSORTIUM_COLLAPSE modifier (×0.65 CDI) immediately.
    2. Set resolution timeline expectation to 60-90 days not 30.
    3. Do not process any positive signal from a single consortium member
       as resolution — all members must confirm a consistent position.
    4. Track each member's public statements independently.
       Divergence between members is itself a signal of deeper collapse.
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

**Communication:** Trust breakdown conclusions must be stated explicitly — not implied through modifier changes alone. When Level 2 or Level 3 is confirmed, communicate the classification, the specific signals that triggered it, and the modifier applied. Do not allow the suppression of positive signals to be the only indication that trust breakdown reasoning is active.

**Calibration:** The three modifier values (×0.95 Level 1 / ×0.72 Level 2 / ×0.60 Level 3) and the CONSORTIUM_COLLAPSE modifier (×0.65) should be validated against confirmed case outcomes. If cases consistently resolve faster or slower than the 30-day / 60-90 day windows, recalibrate the timeline thresholds.

**Adaptation:** Trust breakdown classification must update immediately when new signals arrive — do not wait for a scheduled review cycle. A Level 2 situation can deteriorate to Level 3 within hours if terminal signals fire. The framework adapts to signal velocity, not calendar cadence.

**Verification:** Before applying Level 2 or Level 3 modifiers, verify that at least two independent sources confirm the triggering signals. A single media report without corroboration does not meet the verification threshold. Official filings, club communications, or regulatory notifications are Tier 1 sources. Media speculation is Tier 2.

**Ethics:** Trust breakdown intelligence must not be used to amplify negative sentiment beyond what the verified evidence supports. The framework exists to protect agents from misapplying positive modifiers in bad-faith situations — not to generate bearish signals beyond the evidence base. Apply the framework precisely — no more, no less.

**Transparency:** Every trust breakdown conclusion must show its reasoning chain: which signals triggered classification, which level was assigned, which modifier was applied, and what restoration conditions are set. Do not apply TRUST_BREAKDOWN modifiers silently. The suppression of standard positive signals requires explicit acknowledgment — agents and holders using the output must be able to see why standard signals are not being processed.

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
