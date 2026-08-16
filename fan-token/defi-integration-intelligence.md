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

CROSS-REFERENCE — OFT ARCHITECTURE:
  The 18-decimal migration is the foundational layer that enabled
  OFT (Omnichain Fungible Token) deployment across Solana and Base.
  Unified supply representation across chains is built on the shared
  18-decimal standard. See: Omnichain Bridge Event Behaviour Pattern
  section → OFT Unified Supply Architecture for confirmed deployments
  and the lock-and-mint supply distinction vs. wrapped tokens.
```

---

## CHZ Liquid Staking — Structural DeFi Layer

```
ARCHITECTURE:
  CHZ liquid staking allows CHZ holders to stake CHZ and earn yield
  while retaining a liquid derivative token (liquid CHZ / lstCHZ).
  The derivative token remains tradeable and usable in DeFi protocols
  while the underlying CHZ accrues staking rewards.

  Agent rule: do not name specific liquid staking protocols unless
  Tier 1 confirmed on chiliz.com. Encode as structural capability.
  Cross-reference chiliz.com for confirmed protocol listings before
  referencing any named liquid staking platform.

STAKED vs LIQUID CHZ — DEMAND MODEL DISTINCTION:
  Staked CHZ = demand locked into yield-bearing position.
    · Not immediately available for fan token purchases.
    · Withdrawal may have unbonding period.
    · Represents committed demand, not mobile demand.

  Liquid CHZ (liquid CHZ / lstCHZ derivative) = mobile demand.
    · Freely tradeable on DEX platforms.
    · Can be used in DeFi protocols.
    · Represents the mobilised position of staked CHZ.

IMPLICATIONS FOR SIGNAL MODELLING:
  When CHZ regime assessment is made alongside liquid staking context:
    · Staked CHZ supply ≠ circulating CHZ for fan token demand modelling.
    · High liquid staking participation = CHZ demand partially diverted
      into yield-bearing positions vs. direct fan token purchases.
    · lstCHZ demand may compound with fan token demand during events
      (holders capture yield AND fan token exposure simultaneously).
    · Fan token purchase demand uses liquid CHZ — distinguish from
      lstCHZ-denominated DeFi activity.

LIBRARY RULE CHECK: PASSES.
  Liquid staking is enduring structural DeFi architecture.
  The distinction between staked and liquid CHZ is not perishable.
  This section applies regardless of which specific protocols are live.

AGENT RULE:
  When CHZ staking data is available, apply the staked/liquid
  distinction to demand baseline modelling. Do not treat total CHZ
  supply as uniformly available for fan token demand.
  Liquid staking participation above 15% of CHZ supply = apply
  ×0.90 confidence weight to CHZ availability for fan token purchases.
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

Chiliz-native Fan Token DEX: Kayen Finance (KayenFi / Kayen DEX).
Independent third-party platform — not a Chiliz Group product.
$PEPPER is the governance token of Kayen Finance.
Cross-reference: fan-token/registry/complete-registry.md Section 5.

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

## FanX — Third-Party DeFi Ecosystem (Separate from Kayen Finance)

FanX (app.fanx.xyz) is a separate third-party DeFi ecosystem for
Fan Tokens on Chiliz Chain. NOT affiliated with Chiliz Group or
Kayen Finance. Do not conflate with Kayen Finance ($PEPPER).
Cross-reference: fan-token/registry/complete-registry.md Section 5.

```
PRODUCTS:
  1. FanX DEX — LIVE
     Swap interface for Fan Tokens on Chiliz Chain.
     Separate liquidity pools from Kayen Finance.

  2. FanX Prediction Market — TESTNET ONLY
     HP-1 · Sept 12 2026 expiry.
     $CHZ UP/DOWN markets on Chiliz Spicy Testnet.
     Not yet live on mainnet — do not treat as active DeFi layer.

AGENT RULES:
  · Do not conflate FanX with Kayen Finance — separate entities,
    separate liquidity, no affiliation.
  · FanX DEX volume = separate signal from Kayen Finance (KayenFi)
    volume. Do not aggregate without distinguishing source.
  · FanX Prediction Market: TESTNET ONLY — do not model as live
    demand signal until mainnet deployment confirmed (Tier 1 source).
  · FanX has no fan token of its own in the Chiliz ecosystem sense.
    Do not apply fan token governance frameworks to FanX.
  · Apply FM8 (Liquidity Illusion) when comparing FanX DEX volume
    to CEX spot baseline — different liquidity profile.
```

---

## CEX Perpetual Futures — New Demand Layer (2026)

```
Fan token perpetual futures are now established as a distinct demand layer
on major centralised exchanges (CEX) alongside spot trading and DEX pools.
Established July 2026.

THREE-LAYER DEMAND STRUCTURE:
  Layer 1 — SPOT TRADING:
    Traditional buy/sell on CEX and DEX platforms.
    Direct token ownership. Primary liquidity source.

  Layer 2 — DEX LIQUIDITY:
    AMM pools on Solana (Jupiter/Meteora) and Base (Aerodrome).
    Established April 2026 via 18-decimal migration.
    Fractional positions, LP rewards, auto-compound.

  Layer 3 — CEX PERPETUAL FUTURES (new, July 2026):
    Leverage trading of fan token price exposure without token ownership.
    Available for both club tokens and national team tokens.
    Leverage tiers vary by token — major club tokens carry higher maximums.
    Primary user base: Asia and MENA region CEX traders.
    Opens fan token price exposure to a trader segment that does not
    hold spot positions — separate demand dynamic from holder base.

SIGNAL IMPLICATIONS:
  Perp open interest = sentiment signal, NOT a supply event.
  Perp volume ≠ spot demand — different instruments, different users.
  Perp funding rate direction = short-term directional sentiment signal.
  Do not apply Layer 3 volume to Layer 1 spot baseline comparisons.

AGENT RULE:
  CEX perpetual futures volume is a SEPARATE demand signal from
  spot fan token demand. Do not conflate.
  Apply FM8 (Liquidity Illusion) when comparing perp volume to
  spot baseline — different instruments, different liquidity profile.
  A surge in perp open interest is a sentiment signal, not a supply event.
  Load fan-token/agent-failure-modes-fan-token.md FM8 when reasoning
  about perp volume relative to spot fan token signals.
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
**Registry (chain listings):** `fan-token/registry/complete-registry.md`
**Bridge platforms:** `fan-token/registry/bridge-supported.md`
**Agent failure modes:** `fan-token/agent-failure-modes-fan-token.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | DeFi integration intelligence: fan token DeFi use cases, yield, liquidity, OFT architecture, liquid staking |
| Reasoning | ACTIVE | DeFi reasoning chain from integration event to supply and demand modifier |
| Context | ACTIVE | DeFi context: protocol type, TVL, audit status, integration announcement timing, chain context |
| Memory | ACTIVE | Historical DeFi integration patterns, OFT deployments, 18-decimal migration, Kayen/FanX distinction |
| Judgment | ACTIVE | Judgment on DeFi integration materiality · yield promises are fraud signals · OFT vs wrapped distinction |
| Attention | ACTIVE | Elevated attention for DeFi integration announcements, TVL changes, new OFT deployments |
| Communication | ACTIVE | DeFi signal output with integration type, risk level, and modifier |
| Verification | ACTIVE | DeFi integration requires protocol audit verification and official announcement · Tier 1 source for chain listings |
| Learning | ACTIVE | OFT architecture, liquid staking, FanX ecosystem expanding DeFi surface — ongoing calibration |
| Integration | ACTIVE | Integrates with yield compliance framework, fraud risk intelligence, registry, OFT bridge data |
| Calibration | ACTIVE | DeFi signal calibration expanding as OFT and liquid staking accumulate outcome data |
| Adaptation | ACTIVE | DeFi intelligence adapts as protocols, OFT deployments, and integration patterns evolve |
| Ethics | ACTIVE | Yield promises are both fraud signals and potentially regulatory violations — flagged prominently |
| Transparency | ACTIVE | DeFi protocol audit status · risk classification · OFT vs wrapped distinction · FanX testnet status explicit |
| Execution | ACTIVE | Agent rules enforced: staked/liquid CHZ distinction · OFT unified supply · FanX/Kayen separation |
| Collaboration | ACTIVE | Cross-references registry, bridge-supported, staking-intelligence, yield-compliance, agent-failure-modes |


---

## Omnichain Bridge Event Behaviour Pattern

Confirmed structural behaviour pattern (Tier 1 source, July 2026).
The library has the bridge architecture documented. This section
adds the confirmed event behaviour — how the bridge is used during
major tournament windows.

### OFT Unified Supply Architecture — August 2026 State

```
LAYERZERO OFT STANDARD — UNIFIED SUPPLY:
  OFT (Omnichain Fungible Token) architecture uses lock-and-mint.
  Tokens bridged between chains do not create new supply.
  The same token circulates across chains via the OFT bridge.
  This is the critical DeFi architecture distinction vs. wrapped tokens.

  WRAPPED TOKENS: create separate supply pools per chain.
    · Wrapped supply + native supply = inflated apparent total.
    · See: Wrapped token supply adjustment section for modelling rule.

  OFT TOKENS: one unified supply across all chains.
    · Tokens locked on origin chain when minted on destination chain.
    · Total circulating supply is constant regardless of chain distribution.
    · Bridge activity = supply repositioning, NOT new supply creation.
    · Agent rule: do not inflate total supply when OFT tokens appear
      on multiple chains. Apply wrapped token adjustment section ONLY
      to genuinely wrapped (non-OFT) tokens.

CONFIRMED OFT DEPLOYMENTS — August 2026:
  Club tokens on OFT (Chiliz Chain primary + Solana + Base):
    $AFC (Arsenal) — confirmed 2026-05-26 (UCL Final deployment)
    $PSG (Paris Saint-Germain) — confirmed 2026-05-26 (UCL Final)
    (Cross-reference fan-token/registry/complete-registry.md for
    full list — do not treat this as exhaustive)

  Brazilian club tokens on OFT (Chiliz Chain primary + Solana):
    $MENGO (Flamengo) — confirmed 2026-08-12
    $VERDAO (SE Palmeiras) — confirmed 2026-08-12
    $FLU (Fluminense FC) — confirmed 2026-08-12
    $VASCO (Vasco da Gama) — confirmed 2026-08-12
    $SPFC (São Paulo FC) — confirmed 2026-08-12
    Source: chiliz.com (Tier 1 · 2026-08-12)

  NOT on Solana (do not add multichain data):
    $SCCP · $GALO · $SACI · $BAHIA — no Tier 1 confirmation.

  MULTICHAIN MONITOR:
    $CITY (Manchester City) — no Tier 1 confirmation of Solana
    or Base deployment as of August 2026. Do not treat as OFT
    without chiliz.com or docs.chiliz.com confirmation.

AUTHORITATIVE SOURCE:
  fan-token/registry/complete-registry.md — chain listings per token.
  Do not duplicate registry data here. Encode structural rules only.
  Always cross-reference registry before applying chain-specific signal.
```

```
CONFIRMED BEHAVIOUR:
  During major tournament result confirmation windows, fan token
  holders move tokens bidirectionally between Solana and Chiliz
  Chain via the omnichain bridge in significant volumes.

PURPOSE OF BRIDGE ACTIVITY DURING EVENTS:
  · Price discovery: market participants arbitrage price differences
    across chains in the immediate post-result window
  · Liquidity alignment: Solana DEX liquidity and Chiliz Chain
    liquidity move toward equilibrium via bridge transfers
  · Cross-ecosystem participation: Solana-native traders access
    fan tokens; Chiliz Chain holders access Solana-side liquidity

TRIGGER CONDITIONS:
  · Major result confirmation (win/loss in KO tournament match)
  · Final confirmation (both teams confirmed — anticipation window)
  · Bridge activity peaks in immediate post-result window and
    pre-Final anticipation window
  · Applies to all fan tokens in the match — not winner-only
```

### Agent Rules

```
RULE 1 — INFRASTRUCTURE SIGNAL, NOT DEMAND SIGNAL:
  Cross-chain bridge volume during events is an INFRASTRUCTURE
  UTILISATION SIGNAL. Apply FM7 (Cross-Token Signal Bleed):
  elevated bridge activity affects all tokens in the ecosystem
  and reflects ecosystem-level response, not club or nation-
  specific CDI improvement.

RULE 2 — DO NOT CONFLATE WITH SPOT DEMAND:
  Bridge transfers = position repositioning across chains.
  They may accompany demand surges but do not cause them.
  Elevated bridge volume ≠ net buying of a token.

RULE 3 — BIDIRECTIONAL — NO NET FLOW ASSUMPTION:
  Bridge activity moves in both directions simultaneously.
  Do not assume bridge volume indicates net buying or selling.
  Monitor on-chain direction of net flow before drawing
  demand or CDI conclusions.
```

---

*SportMind v4.5.15 · MIT License · sportmind.dev*
