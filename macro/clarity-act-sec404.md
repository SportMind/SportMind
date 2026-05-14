---
name: clarity-act-sec404
description: >
  Dedicated reasoning framework tracing the CLARITY Act Section 404 activity-based
  reward safe harbour for digital assets including fan tokens. Covers the permitted
  vs prohibited yield distinction, how the safe harbour applies to fan token utility
  design, the dual-purpose fraud signal, and implications for US market access.
  Enduring framework — Section 404 provisions are DRAFT_STABLE and the design
  principles are permanent regardless of final enactment date.
---

# CLARITY Act — Section 404: Activity-Based Reward Safe Harbour

**Complete Section 404 reasoning framework for fan token intelligence.**
Status: DRAFT_STABLE — provisions confirmed in released draft text.

> Primary reference: `macro/macro-regulatory-sportfi.md` (full CLARITY Act status)
> Full implementation: `macro/clarity-act-complete-framework.md`
> Stablecoin connection: `macro/stablecoin-cbdc-intelligence.md`

---

## Section 404 — Core provision

```
SECTION 404 — ACTIVITY vs PASSIVE YIELD DISTINCTION (Status: DRAFT_STABLE)

  WHAT SECTION 404 DOES:
    Creates a bright-line distinction between two types of returns on digital assets.
    The distinction determines which regulatory framework applies and which
    structures are legally permissible for US-accessible digital asset platforms.
    
  THE BRIGHT LINE:
    PROHIBITED (passive yield):
      Interest, yield, or return paid "solely in connection with the holding"
      of a digital asset — economically equivalent to a bank deposit.
      Also characterised as: staking yield, balance-based APY, automatic
      accumulation without user action.
      
    PERMITTED (activity-based rewards):
      Rewards contingent on a user's active participation or engagement.
      Includes: governance voting rewards, prediction participation rewards,
      match engagement rewards, platform activity incentives, transaction-linked
      rewards.
      Not contingent on holding alone — contingent on doing.
      
  THE SAFE HARBOUR:
    Any digital asset reward mechanism that is activity-based (not balance-based)
    is explicitly permitted under Section 404.
    This safe harbour applies regardless of whether the underlying asset is
    classified as a payment stablecoin, digital commodity, or other category.
    For fan tokens (classified as digital commodities): the safe harbour
    provides maximum flexibility — fan tokens are not payment stablecoins and
    therefore face no passive yield restriction from Section 404 directly.
```

---

## Application to fan tokens

```
FAN TOKEN CLASSIFICATION UNDER CLARITY ACT:
  Fan tokens: digital commodities (CFTC jurisdiction)
  NOT: payment stablecoins (banking regulator jurisdiction)
  NOT: investment contract assets (SEC jurisdiction)
  
  Section 404's passive yield prohibition applies primarily to payment stablecoins.
  Fan tokens as digital commodities are NOT subject to the passive yield prohibition.
  However: if a fan token were to offer equity-like returns or passive yield
  structured to mimic a bank deposit — it risks reclassification to investment
  contract asset territory (SEC jurisdiction).
  
  PRACTICAL IMPLICATION:
    Fan token reward structures safe for US market access:
      ✓ Governance voting reward (user must vote to earn)
      ✓ Prediction participation reward (user must submit prediction)
      ✓ Stadium or experience access via holding (utility, not yield)
      ✓ Match engagement reward (user must engage during match)
      ✓ Platform activity reward (user must transact or interact)
      
    Fan token structures that risk reclassification:
      ✗ Passive APY on token balance with no user action required
      ✗ Guaranteed financial return stated as percentage per period
      ✗ Dividend or revenue sharing rights (equity-like)
      ✗ Interest payment linked to holding duration
      
  CHILIZ/SOCIOS PLATFORM DESIGN ALIGNMENT:
    The existing fan token ecosystem is already aligned with Section 404:
    Governance votes: activity-based ✓
    Match predictions: activity-based ✓
    Experience access: utility not yield ✓
    FTP PATH_2 supply events: result of match outcome not holding duration ✓
    
    PATH_2 supply events (burns and mints) are not yield in any legal sense —
    they are supply mechanic events tied to sporting results.
    They do not accrue to holders based on holding; they fire on match results.
    Section 404 does not constrain PATH_2 mechanics.
```

---

## The dual-purpose fraud signal

```
PASSIVE YIELD PROMISE = DUAL RED FLAG:

  When any sports crypto asset promises passive yield on holdings:
    
  RED FLAG 1 — FRAUD SIGNAL:
    Official Fan Tokens™ do not promise passive yield.
    A token claiming to be an official Fan Token™ that promises passive yield
    is inconsistent with how the official ecosystem operates.
    This is a Tier 1 fraud red flag.
    See: fan-token/fraud-risk-intelligence.md
    
  RED FLAG 2 — REGULATORY VIOLATION SIGNAL:
    For any US-accessible token, a passive yield promise signals a potential
    Section 404 violation under the CLARITY Act framework.
    This applies even if the token is NOT a payment stablecoin:
    promising passive yield while operating in the US market risks
    regulatory action regardless of asset classification.
    
  COMBINED SIGNAL:
    When an agent detects a passive yield promise on a sports crypto asset:
    1. Apply Tier 1 fraud red flag immediately
    2. Flag Section 404 potential violation for US-accessible tokens
    3. Recommend verification through fan-token/official-verification-framework.md
    4. Do not apply SportMind fan token intelligence frameworks to unverified assets
    
  AGENT OUTPUT FOR PASSIVE YIELD DETECTED:
    {
      "passive_yield_detected": true,
      "fraud_risk_tier": "TIER_1",
      "section_404_signal": "POTENTIAL_VIOLATION",
      "recommendation": "Verify through official-verification-framework.md",
      "do_not_apply": "SportMind fan token frameworks until verified"
    }
```

---

## Duration-scaling of activity-based rewards

```
REWARD_TYPE: ACTIVITY_BASED | PERMITTED: DURATION_SCALING

  DEFINITION:
    Duration-scaling: rewards that increase in proportion to the DURATION or
    FREQUENCY of eligible user activity — not the duration of passive holding.

  THE CRITICAL DISTINCTION:
    Passive yield (prohibited):
      Reward accrues automatically for holding X tokens for Y days.
      User takes NO action — tokens sit, yield accumulates.
      
    Activity-based with duration scaling (permitted):
      Reward scales with how long or how consistently a user has ACTIVELY engaged.
      Examples: 10 governance votes earns a higher reward weight than 2 votes.
      The scaling factor is activity volume or frequency, not holding duration.

  PERMITTED DURATION-SCALING EXAMPLES:
    ✓ Governance reward scaling with number of votes cast (activity count)
    ✓ Prediction reward scaling with accuracy track record (activity quality)
    ✓ Platform loyalty reward based on cumulative interactions (activity volume)
    ✓ Match engagement reward scaling with matches engaged in (activity frequency)

  NOT PERMITTED (passive yield framing):
    ✗ Reward scaling purely with days tokens held, no action required
    ✗ "Loyalty bonus" for not selling — passive yield by another name
    ✗ Yield that increases automatically without user taking any action

  AGENT CLASSIFICATION:
    Duration of ACTIVITY → ACTIVITY_BASED → Section 404 safe harbour → COMPLIANT
    Duration of HOLDING  → PASSIVE YIELD  → Section 404 prohibited   → FLAG

  PLATFORM CONFIRMATION:
    Chiliz/Socios governance, prediction, and engagement mechanics are structured
    as activity-based — duration scaling within these systems is COMPLIANT.
    Apply: activity_duration_scaling_signal = COMPLIANT for confirmed Socios mechanics.
```

## Design guidance for US market compliance

```
HOW TO ASSESS US MARKET COMPLIANCE OF FAN TOKEN REWARD MECHANICS:

  STEP 1 — CLASSIFY THE REWARD TYPE:
    Does the reward require user action? → ACTIVITY-BASED (Section 404 safe harbour)
    Does the reward accrue automatically on holding? → PASSIVE YIELD (prohibited)
    Does the reward represent equity or profit sharing? → INVESTMENT CONTRACT RISK
    
  STEP 2 — APPLY THE BRIGHT LINE:
    Activity-based: Section 404 safe harbour applies → compliant for US market
    Passive yield: prohibited under Section 404 → non-compliant for US market
    
  STEP 3 — CHECK FOR DUAL-PURPOSE SIGNAL:
    Is this from an unverified source? → Apply fraud risk framework too
    
  DECISION TREE:
    
    Reward mechanism identified
          |
          ↓
    User action required?
    YES → Activity-based → Safe harbour → COMPLIANT ✓
    NO  → Passive yield?
              |
              YES → PROHIBITED ✗ + Fraud Tier 1 flag if unverified
              NO  → Equity/profit share?
                         |
                         YES → Investment contract risk → DO NOT MODEL
                         NO  → Utility (access, experience) → COMPLIANT ✓

PLATFORM COMPLIANCE SIGNAL:
  Platform confirmed compliant with Section 404 framework:
    Apply: section_404_compliant_signal = ×1.05 US market confidence modifier
    Mechanism: regulatory clarity reduces friction for US holder acquisition
    
  Platform confirmed non-compliant (passive yield active for US users):
    Apply: section_404_violation_signal = US holder access risk
    Monitor: FinCEN, SEC enforcement actions as primary sources
```

---

## Legislative status and monitoring

```
SECTION 404 MONITORING FRAMEWORK:

  Current status: DRAFT_STABLE
    Provision present in released draft text.
    Senate Banking Committee markup: IN_PROGRESS.
    Stable enough that platform design decisions can be made based on it.
    
  WHAT WOULD CHANGE THE FRAMEWORK:
    Section 404 removed in markup → downgrade to UNCERTAIN; apply ×0.80 confidence
    Section 404 narrowed (applies only to stablecoins, not all digital assets) →
      fan token implications reduced; update this file accordingly
    Section 404 expanded (broader passive yield prohibition) →
      check PATH_2 mechanics for compliance; PATH_2 fires on match result not holding
      
  ENACTMENT TIMELINE IMPLICATIONS:
    Pre-enactment: design decisions based on DRAFT_STABLE signal
    Post-enactment: full enforcement applies; 180-day CFTC provisional period begins
    Joint rulemaking (months 6-12): formal regulatory definitions published
    
  AGENT RULE:
    Before enactment: apply Section 404 as DRAFT_STABLE design constraint
    After enactment: apply as ENACTED regulatory requirement (full weight)
    During joint rulemaking: apply ×0.94 confidence (see clarity-act-complete-framework.md)
```

---

## Compatibility

**Full CLARITY Act framework:** `macro/clarity-act-complete-framework.md`
**Stablecoin connection:**      `macro/stablecoin-cbdc-intelligence.md`
**Fraud dual signal:**          `fan-token/fraud-risk-intelligence.md`
**Verification framework:**     `fan-token/official-verification-framework.md`
**Regulatory status:**          `macro/macro-regulatory-sportfi.md`
**Legislation process:**        `core/legislation-process-intelligence.md`

---

*SportMind v3.97.49 · MIT License · sportmind.dev*
*Section 404 passive yield = Tier 1 fraud signal + Section 404 violation signal (dual-purpose)*
