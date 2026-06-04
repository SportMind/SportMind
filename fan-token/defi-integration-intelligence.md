---
name: defi-integration-intelligence
description: >
  Enduring reasoning framework for DeFi protocol interactions with fan tokens
  as they affect supply signals, demand signals, and FTP PATH_2 mechanics.
---

# DeFi Integration Intelligence

**How to reason about DeFi protocol interactions with fan token signals.**
DeFi modifiers affect demand signal confidence. They do not affect PATH_2 supply mechanics.

---

## Liquidity pool reasoning

```
THIN LIQUIDITY SIGNAL:
  Definition: DEX depth on Base or Solana below 5% of 24h CEX volume
  Apply: x0.90 confidence weight to PATH_2 magnitude estimates

DEEP LIQUIDITY SIGNAL:
  Definition: DEX liquidity above 20% of CEX volume
  Apply: x1.05 to demand baseline

LIQUIDITY CONCENTRATION RISK:
  Definition: top three wallets above 60% of DEX liquidity
  Apply: x0.85 confidence weight on all demand signals
```

---

## Yield farming supply distortion

```
ABOVE 15% OF CIRCULATING SUPPLY LOCKED IN YIELD FARMING:
  Apply: x0.85 confidence weight to all sports-driven demand signals

  HOW TO IDENTIFY: large wallets depositing into DeFi protocols on-chain;
    price rising without sports news trigger; volume in DeFi interactions.

  PATH_2 NOTE: DeFi supply distortion does not affect PATH_2 mechanics.
```

---

## Cross-chain yield arbitrage

```
DeFi YIELDS FOR LP POSITIONS EXCEED 15% APR:
  Apply: x0.85 confidence weight to sports-driven demand signals.
  PATH_2 mechanics unaffected.
```

---

## Wrapped token supply adjustment

```
WRAPPED SUPPLY ABOVE 5% OF TOTAL SUPPLY:
  Adjusted PATH_2 calculation: (native supply + wrapped supply) / 400
  Use when wrapped supply data is available.
```

---

## DeFi signal priority hierarchy

```
CFTC enforcement on DeFi protocol with fan token exposure:
  HOLD immediately

Large LP withdrawal above 10% of pool depth:
  Apply: x0.88 to all demand signals for 24-48 hours

Yield farm APR spike above 25%:
  Apply: x0.85 confidence weight to sports demand signals

Standard DeFi conditions: no adjustment
```

---

## Compatibility

**Staking:** `fan-token/staking-intelligence.md`
**Yield compliance:** `fan-token/yield-compliance-framework.md`
**PATH_2:** `fan-token/ftp-path2.md`
**Macro DeFi:** `macro/defi-macro-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | DeFi integration intelligence: fan token DeFi use cases, yield, and liquidity signals |
| Reasoning | ACTIVE | DeFi reasoning chain from integration event to supply and demand modifier |
| Context | ACTIVE | DeFi context: protocol type, TVL, audit status, integration announcement timing |
| Memory | ACTIVE | Historical DeFi integration patterns and their token impact data |
| Judgment | ACTIVE | Judgment on DeFi integration materiality — yield promises are fraud signals |
| Attention | ACTIVE | Elevated attention for DeFi integration announcements and TVL changes |
| Communication | ACTIVE | DeFi signal output with integration type, risk level, and modifier |
| Verification | ACTIVE | DeFi integration requires protocol audit verification and official announcement |
| Learning | EMERGING | DeFi integration impact calibration is limited — new domain |
| Integration | ACTIVE | Integrates with yield compliance framework and fraud risk intelligence |
| Calibration | EMERGING | DeFi integration signal calibration requires more outcome data |
| Adaptation | ACTIVE | DeFi intelligence adapts as protocols and integration patterns evolve |
| Ethics | ACTIVE | Yield promises are both fraud signals and potentially regulatory violations — flagged prominently |
| Transparency | ACTIVE | DeFi protocol audit status and risk classification explicit in output |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
