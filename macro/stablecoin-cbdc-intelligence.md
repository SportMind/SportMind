---
name: stablecoin-cbdc-intelligence
description: >
  Enduring reasoning framework for stablecoin and CBDC developments as they affect
  fan token market access, settlement mechanics, and holder behaviour. Covers the
  CLARITY Act three-tier classification, FTP PATH_2 settlement interaction, on-ramp
  accessibility by jurisdiction, CBDC signals, and GENIUS Act connection.
---

# Stablecoin and CBDC Intelligence

**How to reason about stablecoin and CBDC developments as fan token market signals.**
Enduring frameworks only — not current stablecoin prices or yields.

> Extends: `macro/macro-regulatory-sportfi.md` (jurisdiction-level frameworks)
> Extends: `macro/clarity-act-complete-framework.md` (CLARITY Act full framework)

---

## CLARITY Act three-tier classification (stablecoin-relevant)

```
THREE CATEGORIES UNDER CLARITY ACT FRAMEWORK:

PAYMENT STABLECOINS (banking regulator jurisdiction):
  Requirements: capital, custody, anti-manipulation standards
  Yield restriction: CANNOT pay passive yield on balances
  Activity-based rewards: PERMITTED
    Examples: transaction rewards, platform usage rewards, engagement rewards
  Fan token design relevance:
    Any US-compliant fan token reward mechanic must follow activity-based model.
    "Hold and earn" = prohibited. "Engage and earn" = permitted.
    Source: CLARITY Act Section 404 (DRAFT_STABLE)

DIGITAL COMMODITIES (CFTC jurisdiction):
  Profile: tokens tied to decentralised blockchains — Bitcoin model
  Yield restriction: passive yield restriction does NOT apply to this category
  Fan token classification: digital commodities under current framework
  Implication: fan tokens may offer engagement rewards without the payment
    stablecoin yield restrictions — but must not offer equity-like returns
    (which would trigger investment contract asset classification)

INVESTMENT CONTRACT ASSETS (SEC jurisdiction):
  Profile: tokens representing equity, debt, or similar economic rights
  Fan tokens: EXPLICITLY EXCLUDED from this category
  Source: SEC/CFTC joint guidance March 2026 + CLARITY Act framework
  
AGENT RULE:
  When assessing any US-linked fan token reward programme:
    1. Confirm token classification as digital commodity (not payment stablecoin)
    2. Confirm reward mechanics are activity-based (not passive yield)
    3. Confirm no equity or profit-sharing rights (would trigger reclassification)
    4. Apply ×1.05 US market access signal if all three confirmed
```

---

## Fan token stablecoin interaction

```
FTP PATH_2 PRE-LIQUIDATION SETTLEMENT:

  PATH_2 pre-liquidation pools settle via CHZ on Chiliz Chain.
  Cross-chain settlement (Base/Solana) uses bridge infrastructure.
  Stablecoin liquidity on Base and Solana affects cross-chain efficiency.
  
  HIGH STABLECOIN LIQUIDITY ON BASE/SOLANA:
    Smoother pre-liquidation execution — no modifier needed (expected baseline)
    
  LOW STABLECOIN LIQUIDITY ON BASE/SOLANA:
    Settlement delay risk — apply: ×0.95 confidence to supply event timing estimates
    Affects: timing of burn confirmation, not the burn magnitude itself
    Source: monitor Uniswap/Aerodrome liquidity depth on Base for USDC/CHZ pairs

ON-RAMP ACCESSIBILITY BY JURISDICTION:

  Stablecoin availability in a jurisdiction directly affects fan token purchasing power
  for holders in that market. On-ramp = local fiat → stablecoin → CHZ → fan token.
  
  USDT RESTRICTION IN A KEY MARKET:
    Apply: regional_demand_suppressor = ×0.88 for that jurisdiction's estimated holder base
    Duration: sustained while restriction is active
    Assessment: what percentage of estimated global holder base is in this jurisdiction?
    Scale modifier proportionally to jurisdiction size relative to global holder base
    
  USDC EXPANSION (banking regulatory approval in new jurisdiction):
    Apply: usdc_expansion_signal = ×1.05 for that market's estimated holder demand
    Mechanism: easier fiat on-ramp reduces friction for new holders entering the ecosystem
    
  COMBINED STABLECOIN RESTRICTION (USDT + USDC both unavailable in jurisdiction):
    Apply: ×0.80 regional demand floor for that jurisdiction
    Mechanism: double on-ramp restriction significantly reduces market access
```

---

## CBDC framework

```
CHINA — e-CNY (most advanced CBDC, operational):

  Digital yuan creates parallel payment infrastructure to USD-based stablecoins.
  China has significant fan token holder activity (largest Socios user base historically).
  
  e-CNY INTEGRATION WITH CHILIZ ECOSYSTEM (if confirmed):
    Signal: major positive demand signal for Chinese holder base
    Apply: ecny_integration_modifier = ×1.15 (rare, high-magnitude)
    Mechanism: removes stablecoin friction for Chinese holders entirely;
      CHZ purchase via digital yuan = direct access without USDT/USDC dependency
  
  CURRENT STATUS:
    e-CNY operational domestically. No confirmed Chiliz integration.
    Monitor official Chiliz announcements for integration news.

UAE — DIGITAL DIRHAM (in development):

  UAE is a primary MENA fan token market. VARA regulatory framework already clear.
  
  DIGITAL DIRHAM INTEGRATION SIGNAL (when confirmed):
    Apply: digital_dirham_modifier = ×1.08 for UAE holder base demand signals
    Mechanism: VARA clarity + digital dirham = frictionless regulated on-ramp
    UAE holder base is Tier 1 MENA market — this is a material demand signal

NIGERIA — eNaira (launched but limited adoption):

  Nigeria has one of the largest crypto user bases in Africa.
  Significant football fan token interest — $PSG, $BAR among most held in West Africa.
  eNaira adoption has been limited; monitor for expansion signals.
  No modifier applied until eNaira-to-crypto pathway confirmed accessible.

BRAZIL — DREX (in development):

  Brazil is a primary Chiliz market — $FLU and $MENGO tokens active.
  DREX adoption could improve fan token on-ramp efficiency for Brazilian holders.
  
  DREX INTEGRATION SIGNAL (when confirmed):
    Apply: drex_integration_modifier = ×1.05 for Brazilian holder base demand
    Monitor: Chiliz official announcements for DREX integration news

CBDC CRYPTO RESTRICTION RISK:

  If a major CBDC explicitly restricts conversion to crypto assets:
    Apply: cbdc_restriction_modifier = ×0.82 for that jurisdiction's demand signals
    This is a severe jurisdiction-level access block — same tier as exchange delisting
    Sustained until restriction is confirmed lifted.
    Source: central bank official statements only (Tier 1)
```

---

## GENIUS Act connection

```
GENIUS ACT — STABLECOIN LICENSING FRAMEWORK:

  The GENIUS Act sets stablecoin licensing, capital, custody, and AML requirements.
  Key provisions shape payment token infrastructure before the broader CLARITY Act
  framework is fully implemented.
  
  COMPLIANT PLATFORM (GENIUS Act standards met):
    Apply: genius_compliant_signal = ×1.05 for US holder base confidence
    Mechanism: regulated stablecoin infrastructure increases institutional and
      retail US holder confidence in the broader ecosystem
    
  NON-COMPLIANT PLATFORM:
    Apply: genius_compliance_risk = US holder base access risk signal
    Non-compliant platforms may face access restrictions for US users
    Monitor: FinCEN and OCC enforcement actions
    
  GENIUS ACT AND FAN TOKEN UTILITY:
    The GENIUS Act passthrough: compliant stablecoin infrastructure enables
    activity-based fan token reward mechanics to function reliably in the US market.
    Stablecoin compliance → fan token utility chain integrity → US holder demand signal
```

---

## Compatibility

**CLARITY Act framework:**  `macro/clarity-act-complete-framework.md`
**Jurisdiction detail:**     `macro/macro-regulatory-sportfi.md`
**Exchange signals:**        `macro/exchange-intelligence.md`
**On-chain settlement:**     `core/blockchain-onchain-intelligence.md`
**PATH_2 mechanics:**        `fan-token/ftp-path2.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Stablecoin and CBDC macro intelligence: stablecoin stability signals and CBDC policy impact |
| Reasoning | ACTIVE | Stablecoin reasoning chain from stability signal to payment infrastructure and macro modifier |
| Context | ACTIVE | Stablecoin context: GENIUS Act (US), algorithmic vs fiat-backed, CBDC development stage |
| Memory | ACTIVE | Historical stablecoin failure patterns (UST/LUNA) and CBDC policy development data |
| Judgment | ACTIVE | Judgment on stablecoin signal materiality — de-peg risk vs routine basis point variation |
| Attention | ACTIVE | Maximum attention for stablecoin de-peg signals and major CBDC policy announcements |
| Communication | ACTIVE | Stablecoin output with stability status, de-peg risk, GENIUS Act status, and modifier |
| Verification | ACTIVE | Stablecoin signals require on-chain reserves verification — marketing claims are not Tier 1 |
| Learning | ACTIVE | Stablecoin risk calibration from historical de-peg event-to-market impact data |
| Integration | ACTIVE | Integrates with crypto-digital-asset-intelligence and macro-regulatory-sportfi |
| Calibration | ACTIVE | Stablecoin de-peg risk modifiers calibrated from historical event data |
| Adaptation | ACTIVE | Stablecoin intelligence adapts as GENIUS Act and CBDC frameworks develop |
| Ethics | ACTIVE | Stablecoin stability signals affect user funds — accuracy is a safety-relevant ethics requirement |
| Transparency | ACTIVE | Stablecoin type, reserve verification status, and de-peg risk always explicit in output |


---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Stablecoin liquidity affects PATH_2 settlement timing — not burn magnitude*
