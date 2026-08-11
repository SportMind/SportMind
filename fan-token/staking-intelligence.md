---
name: staking-intelligence
description: >
  Enduring reasoning framework for staking mechanics as they affect fan token
  supply, demand, and FTP PATH_2 calculations. Covers platform staking vs DeFi
  staking, unlock events, and PATH_2 staking interaction for $AFC.
---

# Staking Intelligence

**How staking mechanics affect fan token supply, demand, and FTP PATH_2 calculations.**

---

## Staking category framework

```
CATEGORY 1 - PLATFORM STAKING (Socios/Chiliz native):
  Compliance: FULLY COMPLIANT - activity-based

  Above 20% staked: x1.05 demand signal (community commitment)
  Adjust PATH_2: Effective pool = (circulating - staked) / 400

CATEGORY 2 - DeFi STAKING (external protocols on Base/Solana):
  Compliance: higher risk if yield is passive (US market concern)

  Above 10% in DeFi staking:
  Apply: x0.90 confidence weight to demand signals

COMPLIANCE DISTINCTION:
  Platform staking for governance = COMPLIANT
  Staking for passive APY = NON-COMPLIANT in US
```

---

## Staking unlock events

```
LARGE UNLOCK (above 5% of circulating):
  Apply: x0.92 to demand signal for 48-72 hour post-unlock window
  Note: unlocking does not mean selling.

SMALL UNLOCK (below 2%): no modifier.
```

---

## FTP PATH_2 staking interaction

```
HIGH PLATFORM STAKING RATE ABOVE 30% ($AFC):
  Standard:  circulating / 400
  Adjusted:  (circulating x (1 - staking_rate)) / 400

  Example: 100M circulating, 35% staked
    Standard pool: 250,000
    Adjusted pool: 162,500

  Use adjusted figure when staking rate confirmed above 30%.

STAKING DOES NOT AFFECT:
  The burn/mint mechanic | 75% stop-loss | credit burn system
```

---

## Compatibility

**DeFi integration:** `fan-token/defi-integration-intelligence.md`
**Yield compliance:** `fan-token/yield-compliance-framework.md`
**PATH_2 mechanics:** `fan-token/ftp-path2.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan token staking intelligence: staking mechanics, lock-up signals, and supply impact |
| Reasoning | ACTIVE | Staking reasoning chain from lock-up data to effective circulating supply modifier |
| Context | ACTIVE | Staking context: lock-up period, yield structure, platform (Socios vs DeFi), compliance |
| Memory | ACTIVE | Historical staking pattern data and effective supply reduction baselines |
| Judgment | ACTIVE | Judgment on staking signal — compliant utility staking differs from yield-bearing staking |
| Attention | ACTIVE | Elevated attention for significant staking rate changes and unlock event signals |
| Communication | ACTIVE | Staking output with lock-up rate, effective supply, and compliance status |
| Verification | ACTIVE | Staking data from on-chain sources — verify lock-up contracts via chiliscan.com |
| Learning | EMERGING | Staking-to-supply-signal calibration is developing |
| Integration | ACTIVE | Integrates with supply intelligence, yield compliance framework, and DeFi intelligence |
| Calibration | EMERGING | Staking signal calibration requires more lock-up event data |
| Adaptation | ACTIVE | Staking intelligence adapts as Socios mechanics and DeFi staking evolve |
| Ethics | ACTIVE | Yield-bearing staking is flagged as regulatory risk per yield-compliance-framework.md |
| Transparency | ACTIVE | Staking structure type (utility vs yield) and compliance status explicit in output |
| Execution | ACTIVE | Signal generation workflow, event playbooks, and structured output templates defined |
| Collaboration | ACTIVE | Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer |


---

*SportMind v4.4.6 · MIT License · sportmind.dev*
