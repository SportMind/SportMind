---
name: clarity-act-complete-framework
description: >
  Complete CLARITY Act reasoning framework for SportMind agents. Covers legislative
  path weighting at each stage, implementation timeline with joint rulemaking window
  modifier, three-tier classification impact on fan tokens, DeFi/developer provisions,
  bank/institutional provisions, mature blockchain pathway, and conflict of interest
  provision as legislative risk. Extends macro/macro-regulatory-sportfi.md.
---

# CLARITY Act — Complete Framework

**Full CLARITY Act reasoning framework for fan token intelligence.**
Extends `macro/macro-regulatory-sportfi.md` — do not duplicate jurisdiction detail there.

> Library Rule note: scheduled dates and current vote counts are expiring data.
> This file documents the enduring reasoning framework for how each legislative
> stage affects modifier weights — permanently true regardless of current status.

---

## Committee reconciliation bottleneck framework

```
BICAMERAL COMMITTEE RECONCILIATION:
  When Senate Banking and Senate Agriculture committees produce different
  versions of the same legislation, a reconciliation process is required
  before a floor vote can proceed.

  This pattern is a named legislative bottleneck — not a failure state.
  Reconciliation is a normal and expected part of bicameral legislation.

COMMITTEE_MERGER_PENDING:
  Status: Banking and Agriculture versions require reconciliation.
  This is the primary structural delay mechanism for CLARITY Act timing.

  Key areas of typical bicameral conflict:
    SEC jurisdiction scope (Banking draft focus)
    CFTC jurisdiction scope (Agriculture draft focus)
    Activity-based reward classification (Section 404)
    Fan token classification under "digital commodity" definition

  Signal weighting during COMMITTEE_MERGER_PENDING:
    Apply: ×0.95 confidence to all CLARITY Act framework modifiers.
    Rationale: direction is confirmed but final text is unresolved.
      Substantive changes to Section 404 or jurisdiction boundaries
      could materially affect fan token classification outcomes.

RECONCILIATION_BLOCKER_2 — ADMINISTRATIVE_ETHICS_FRICTION:
  A second class of legislative blocker distinct from the bicameral
  jurisdiction conflict documented above.

  WHAT IT IS:
    Ethics and conflict-of-interest provisions for federal officials
    governing their interactions with digital asset entities require
    cross-party support — specifically supermajority Democrat backing
    in a Senate floor vote context.
    When these provisions are not yet resolved, the 60-vote floor
    threshold cannot be met regardless of the underlying digital
    asset policy content.

  WHY IT IS DISTINCT FROM COMMITTEE_MERGER_PENDING:
    COMMITTEE_MERGER_PENDING = technical/jurisdictional text conflict.
    ADMINISTRATIVE_ETHICS_FRICTION = political supermajority requirement.
    Both can be active simultaneously. They have different resolution paths.
    Technical conflicts resolve through committee negotiation.
    Ethics provisions resolve through political deal-making.

  ENDURING LEGISLATIVE PATTERN:
    Ethics provisions in financial legislation frequently attract
    supermajority requirements because they implicate personal conduct
    of legislators and federal officials — making partisan compromise
    structurally harder than on purely technical regulatory questions.
    This pattern recurs across financial reform cycles — not unique
    to digital asset legislation.

  SIGNAL WEIGHTING:
    When ADMINISTRATIVE_ETHICS_FRICTION is active:
      Apply: ×0.92 confidence (lower than COMMITTEE_MERGER_PENDING ×0.95)
      Rationale: political supermajority blockers are harder to resolve
        than technical drafting conflicts. Resolution requires explicit
        deal-making rather than technical amendment.
    When BOTH blockers are active simultaneously:
      Apply: ×0.90 confidence — dual-blocker compound discount.

  RESOLUTION SIGNALS:
    Ethics provisions agreed (bipartisan) → ADMINISTRATIVE_ETHICS_FRICTION lifted.
      Return to COMMITTEE_MERGER_PENDING confidence weight (×0.95) if still active.
    Both resolved → SENATE_FLOOR_PENDING. Confidence returns to full pathway weight.

  DOCUMENTATION_DELAY interaction:
    ADMINISTRATIVE_ETHICS_FRICTION is a DOCUMENTATION_DELAY amplifier.
    When active: maintain ×0.95 timing suppressor on all US-linked
      fan token demand signals that depend on CLARITY Act enactment.

  RECONCILIATION RESOLUTION SIGNALS:
    Joint committee agreement announced:
      Apply: ×0.75 confidence (SENATE_FLOOR_PENDING stage — see below).
    Floor vote scheduled:
      Signal: reconciliation complete.
      Apply: SENATE_FLOOR_PENDING modifiers from path weighting framework.

  WHAT DOES NOT CHANGE DURING RECONCILIATION:
    The directional framework: US digital asset regulation is progressing.
    Fan tokens remain in REGISTRATION_REQUIRED / UTILITY_EXEMPTION tension.
    State-level frameworks (Wyoming, Texas) operate independently.
    These signals remain at their established confidence weights.

DOCUMENTATION_DELAY (timing suppressor):
  Active when: any stage transition is delayed beyond expected timeline.
  Apply: ×0.95 to timing-dependent US-linked fan token demand signals.
  Purpose: prevents premature "regulation enacted" modelling.
  Remove: when next stage is officially confirmed.
```

---



```
HOW TO WEIGHT THE CLARITY ACT SIGNAL AT EACH STAGE:

  Each stage produces a different signal weight — how confidently to apply
  the CLARITY Act's modifier implications before full enactment.

  Stage: DRAFT_RELEASED (current as of library state)
    Signal weight: LOW-MEDIUM (×0.40)
    Apply to: long-term planning only; flag direction confirmed
    
  Stage: COMMITTEE_MARKUP_PASSED
    Signal weight: MEDIUM (×0.60)
    Apply: provisional modifier values with ×0.60 confidence weight
    
  Stage: SENATE_FLOOR_PASSED (60-vote threshold)
    Signal weight: MEDIUM-HIGH (×0.85)
    Bipartisan requirement — historically achievable for crypto legislation
    Primary risk remaining: conflict-of-interest provision (see below)
    
  Stage: BOTH_CHAMBERS_PASSED
    Signal weight: HIGH (×0.95)
    Apply near-confirmed modifier values
    
  Stage: ENACTED_INTO_LAW
    Signal weight: CONFIRMED (×1.00)
    Update macro-regulatory-sportfi.md status to ENACTED
    Begin implementation timeline modifiers
    
  Stage: IMPLEMENTATION_COMPLETE (18 months post-enactment)
    Signal weight: FULL_EFFECT
    All modifier values apply at full weight
    
  LEGISLATIVE RISK FLAG — CONFLICT OF INTEREST PROVISION:
    The ethics provision (requiring Members of Congress to divest crypto assets)
    remains the primary Senate floor risk.
    Binary outcome: provision added = passes; provision absent = Democratic vote risk.
    Apply: legislative_risk_flag until provision is resolved.
    Do not apply enacted modifiers until risk is resolved.
```

---

## Implementation timeline and joint rulemaking window

```
IMPLEMENTATION TIMELINE — ENDURING FRAMEWORK:

  Day 1 post-enactment:
    Three-tier classification framework becomes law.
    Fan tokens: digital commodity status confirmed (CFTC jurisdiction).
    Apply: enactment_day1_modifier = ×1.15 for US market access signal
    
  Days 1-180 — CFTC expedited registration:
    Expedited registration process for digital commodity exchanges, brokers, dealers.
    Provisional status allows continued operations during registration window.
    Fan token platforms in provisional status: OPERATIONAL_CONTINUITY confirmed.
    Apply: no demand disruption modifier during this window.
    
  Months 6-12 — JOINT SEC/CFTC RULEMAKING WINDOW:
    Joint rulemaking on definitions begins.
    DURATION: 12 months from enactment.
    Critical window — fan token classification formally confirmed in regulation.
    
    JOINT RULEMAKING WINDOW MODIFIER:
      During the 12-month joint rulemaking window:
      Apply: joint_rulemaking_uncertainty_modifier = ×0.94 to all US market signals
      Mechanism: definitions are being confirmed in rulemaking — technical risk
        of classification adjustment exists (low probability but non-zero)
      Remove: when joint rulemaking publishes final effective rules
      
    If joint rulemaking CONFIRMS fan token as digital commodity:
      Apply: classification_confirmed_modifier = ×1.10 (removes uncertainty premium)
      
    If joint rulemaking RECLASSIFIES (very low probability — would require
      significant departure from current guidance):
      Apply: HOLD on all US market signals; reassess full framework
      
  Months 12-18 — MAIN RULES FULLY EFFECTIVE:
    Full CFTC registration required for exchanges, brokers, dealers.
    Fan tokens on CFTC-registered platforms:
    Apply: institutional_credibility_modifier = ×1.05 sustained
    Mechanism: regulated platform presence signals legitimate asset class status

MATURE BLOCKCHAIN PATHWAY:
  CLARITY Act provides a 24-month pathway for established blockchains
  (those with sufficient decentralisation) to qualify as digital commodities
  without ongoing regulatory classification risk.
  
  CHILIZ CHAIN MATURE PATHWAY:
    Duration: 24 months from enactment.
    If Chiliz Chain qualifies under mature blockchain criteria:
    Apply: mature_blockchain_modifier = ×1.08 sustained (structural positive)
    Mechanism: chain-level regulatory certainty — all tokens on a confirmed
      mature blockchain carry reduced classification risk indefinitely
    
  MONITORING SIGNAL:
    Watch for Chiliz Group official statements regarding mature blockchain
    qualification process. This is a 24-month horizon item — not immediate.
    Flag as: mature_blockchain_pathway_open once enactment confirmed.
```

---

## Three-tier classification impact on fan tokens

```
FAN TOKEN CLASSIFICATION: DIGITAL COMMODITY

  Under CLARITY Act framework: fan tokens are digital commodities.
  CFTC jurisdiction applies.
  
  WHAT THIS ENABLES:
    Exchange listing: requires CFTC-registered platform (positive — legitimises)
    Institutional custody: permitted through CFTC-registered custodians
    Activity-based rewards: explicitly permitted
    Governance rights: permitted
    Experience access: permitted
    
  WHAT THIS PREVENTS:
    Passive yield on balance: not applicable (payment stablecoin restriction
      does not apply to digital commodities — no passive yield restriction)
    Equity or profit sharing: would trigger investment contract reclassification
      → avoid in any fan token utility design intended for US market
      
  UTILITY DESIGN REQUIREMENTS FOR US MARKET:
    ✓ Governance rights
    ✓ Experience access (stadium, merchandise, VIP)
    ✓ Activity rewards (predictions, polls, engagement)
    ✗ Equity or dividend rights
    ✗ Guaranteed financial return promises
    
  See: core/odds-market-intelligence.md for how CLARITY Act affects betting
    market integration with fan token signals.
```

---

## DeFi and developer provisions

```
NON-CUSTODIAL DEVELOPER PROTECTION:

  Non-custodial blockchain developers not classified as money transmitters
  for writing code that moves value.
  
  IMPLICATIONS FOR CHILIZ CHAIN:
    Open-source fan token infrastructure development confirmed not subject
    to money transmission licensing.
    Apply: developer_ecosystem_signal = ×1.05 sustained when enacted
    Mechanism: removes legal risk from building on Chiliz Chain — attracts
      more developers to the ecosystem
      
  CENTRALISED DeFi INTERMEDIARIES:
    Centralised intermediaries interacting with DeFi face additional compliance.
    May delay DeFi feature rollout but does not block it.
    Monitor: Chiliz DeFi feature announcements for compliance pathway details.
```

---

## Bank and institutional provisions

```
BANK AND INSTITUTIONAL AUTHORISATION:

  Banks and credit unions explicitly authorised to use digital assets
  for custody and trading when enacted.
  
  IMPLICATIONS FOR FAN TOKEN DEMAND:
    Institutional adoption signal: ×1.10 sustained when enacted
    Mechanism: traditional financial institutions can hold fan tokens —
      opens institutional holder category previously absent
      
  IMPACT ON DEMAND MODEL:
    Pre-enactment demand model: retail holders primarily
    Post-enactment demand model: retail + institutional holders
    This is a structural expansion of the potential holder base —
    not a temporary spike but a permanent baseline expansion.
    
  MONITORING SIGNAL:
    Watch for: first traditional bank or credit union announcing
    fan token custody or trading services.
    First institutional custody launch = ×1.15 (see institutional-intelligence.md)
    This would be the strongest institutional signal in the library.
```

---

## Compatibility

**Stablecoin connection:**   `macro/stablecoin-cbdc-intelligence.md`
**Jurisdiction detail:**     `macro/macro-regulatory-sportfi.md` (current status)
**Institutional signals:**   `macro/institutional-intelligence.md`
**Government strategy:**     `macro/government-intelligence.md`
**Legislation framework:**   `core/legislation-process-intelligence.md`

---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Joint rulemaking window (months 6-12): ×0.94 US signals | Mature blockchain (24m): ×1.08*
