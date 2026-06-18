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

## 18-Decimal Migration — April 2026

```
PRIOR ARCHITECTURE (pre-April 2026):
  Fan Tokens existed as whole integer units only (e.g. 5 tokens, not 4.7).
  This created a structural DeFi exclusion barrier:
    · AMMs could not price Fan Tokens efficiently
    · Lending protocols rejected Fan Tokens as incompatible
    · Fractional liquidity provision was impossible
    · DeFi composability blocked at the token standard level

APRIL 2026 MIGRATION — 18 DECIMAL PLACES:
  Fan Tokens migrated to 18 decimal precision across all chains:
    · Base: now ERC-20 compatible (18 decimals) — full DeFi primitive access
    · Solana: now SPL Token standard (18 decimals) — AMM and lending compatible
    · Chiliz Chain: underlying architecture updated
  Omnichain architecture (LayerZero OFT standard) built on this foundation —
  unified supply representation across chains enabled by shared decimal standard.

IMPLICATIONS FOR AGENT REASONING:
  Any reasoning about Fan Token DeFi exclusion based on pre-April 2026
  architecture is now outdated. 18-decimal Fan Tokens are DeFi-native assets.
  AMMs, lending protocols, and liquidity provision are now available.
  Model Fan Token DeFi depth using current post-migration architecture.

AGENT RULE:
  Do not apply pre-April 2026 DeFi exclusion logic to Fan Token signals.
  18-decimal migration is permanent — architecture does not revert.
  Load fan-token/registry/bridge-supported.md for DeFi platform details
  per chain (Jupiter/Orca/Solana · Aerodrome/Base · Meteora/national tokens).
```

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

## DEX Campaign Volume — Structural Demand Lever

```
DEX campaign volume is a confirmed structural demand lever during
major events. Chiliz runs competitive DEX trading campaigns tied
to high-demand fixtures with volume-ranked leaderboards.

DEMAND LEVER CLASSIFICATION (priority order):
  1. Buying — direct purchase, primary demand signal
  2. Holding — reduced sell pressure, passive signal
  3. Staking locks — Socios staking, active hold signal
  4. DEX campaign volume — event-driven, compound signal
  5. Auto-compound — LP rewards, sustained volume signal
  6. FTP supply events — PATH_2, structural supply signal
  7. Burn to Glory — tournament WIN, treasury supply signal
  8. Balance-gated dApp — soft hold, passive participation signal

AGENT RULE:
  During major events (UCL Final, WC knockout rounds):
    Expect DEX campaign amplification of organic demand signal.
    Do not treat peak campaign volume as baseline for future signals.
    Identify whether a campaign is active before modelling volume.
    Campaign volume + organic demand + supply event = compound signal.
    Model each component independently before summing.
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
