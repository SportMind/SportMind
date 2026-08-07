---
name: yield-compliance-framework
description: >
  Enduring reasoning framework for fan token yield and reward mechanisms under the
  post-CLARITY Act statutory framework. Three compliance categories, three-step agent
  reasoning for new announcements, and FTP PATH_2 compliance clarity. Based on
  enacted statutory principles confirmed through Senate Banking Committee passage.
---

# Fan Token Yield Compliance Framework

**How to reason about yield and reward mechanisms under CLARITY Act Section 404.**
Section 404 survived committee markup intact — activity-based vs passive yield is the defining compliance boundary.

> Full framework: `macro/clarity-act-sec404.md` · Classification: `fan-token/token-classification-framework.md`

---

## Three compliance categories

```
CATEGORY 1 — FULLY COMPLIANT (activity-based):

  Governance participation rewards: tokens earned through voting — user must act.
  Match attendance verification rewards: tied to verified attendance.
  Transaction volume rewards: scaling with platform activity.
  Duration-based loyalty multipliers: Section 404 explicitly permits rewards that
    scale with holding duration when that duration reflects ongoing engagement.
  FTP PATH_2 supply events: NOT yield — permanent supply mechanics, not interest.
    Pre-liquidation is a protocol event. Burns are permanent supply reduction.
    Mints are treasury operations. The 1/400 ratio is a protocol mechanic.
    No compliance risk signal applies to PATH_2 mechanics.
  Engagement multipliers: rewards scaling with fan activity level.

────────────────────────────────────────────────────────────────────

CATEGORY 2 — NON-COMPLIANT IN US (passive yield):

  Interest-bearing token balances
  Staking yield paid as passive APY
  APR or APY style return promises
  Guaranteed return promises of any kind
  Revenue sharing from club commercial profit — reclassifies toward investment
    contract asset (SEC jurisdiction)

────────────────────────────────────────────────────────────────────

CATEGORY 3 — GREY AREA (case-by-case reasoning):

  Liquidity provision rewards:
    Active participation in platform liquidity → likely compliant
    Passive LP position yield → likely non-compliant
  Governance token distributions:
    Tied to voting participation → compliant
    Distributed as passive holding reward → non-compliant
  Cross-chain bridge rewards:
    Active bridging → likely compliant
    Passive holding on bridge → likely non-compliant
```

---

## Agent reasoning for new announcements

```
STEP 1 — Does the reward require active engagement to earn?
  YES → likely compliant; apply ×1.05 positive utility signal
  NO  → passive yield risk; apply ×0.88 compliance risk signal

STEP 2 — Does it promise a guaranteed return, APY, or APR figure?
  YES → COMPLIANCE_RISK_FLAG; non-compliant in US market
        apply ×0.75 US demand suppressor
  NO  → proceed to Step 3

STEP 3 — Does it create equity-like claims on club revenue or profits?
  YES → RECLASSIFICATION_RISK_FLAG; SEC jurisdiction risk
  NO  → likely compliant activity reward

DUAL-PURPOSE FLAG:
  If passive yield detected: apply BOTH Tier 1 fraud red flag AND
  Section 404 potential violation signal simultaneously.
```

---

## FTP PATH_2 compliance clarity

```
FTP PATH_2 SUPPLY EVENTS ARE CATEGORICALLY NOT YIELD:

  Pre-liquidation: protocol event — not a return payment
  Burns:           permanent supply reduction — not interest income
  Mints:           treasury operations — not yield distribution
  1/400 ratio:     protocol mechanic — not an interest rate

  SECTION 404 COMPLIANCE: FULLY COMPLIANT
  No compliance risk signal applies. Do not apply any Section 404
  modifier when processing PATH_2 signals.
```


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Yield compliance framework: regulatory boundaries for fan token yield structures |
| Reasoning | ACTIVE | Yield compliance reasoning chain from yield structure to regulatory risk classification |
| Context | ACTIVE | Compliance context: US Digital Collectible classification, MiCA, UAE VARA requirements |
| Memory | ACTIVE | Historical yield compliance case patterns and regulatory action data |
| Judgment | ACTIVE | Judgment on yield structure type — utility reward vs passive income is the critical boundary |
| Attention | ACTIVE | Elevated attention for any fan token yield announcement — potential securities risk |
| Communication | ACTIVE | Yield compliance output with structure type, risk level, and regulatory jurisdiction flags |
| Verification | ACTIVE | Yield compliance assessment requires legal structure verification — not marketing claims |
| Learning | ACTIVE | Yield compliance framework learning from SEC/CFTC guidance (March 17 2026) |
| Integration | ACTIVE | Integrates with us-token-taxonomy.md, eu.md, fraud-risk-intelligence.md, and staking-intelligence.md |
| Calibration | ACTIVE | Yield red flag framework calibrated against US Digital Collectible boundary (fractionalization test) |
| Adaptation | ACTIVE | Yield compliance framework adapts as regulatory guidance evolves across jurisdictions |
| Ethics | ACTIVE | Passive yield promises are simultaneously a fraud signal and regulatory violation risk — dual flag |
| Transparency | ACTIVE | Yield structure type and all applicable jurisdiction flags explicit in every yield compliance output |
| Execution | ACTIVE | Signal generation workflow, event playbooks, and structured output templates defined |
| Collaboration | ACTIVE | Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
*FTP PATH_2 is not yield. It is a protocol mechanic. No Section 404 restriction applies.*
