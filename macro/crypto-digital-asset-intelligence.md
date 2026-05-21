---
name: crypto-digital-asset-intelligence
description: >
  Enduring reasoning framework for crypto and digital asset market conditions as
  they affect fan token demand, liquidity, and holder behaviour. Extends
  macro/macro-crypto-market-cycles.md with Bitcoin dominance reasoning, altcoin
  season signals, L2/stablecoin intelligence, CHZ virtuous cycle, and market
  structure signals. Load alongside macro-crypto-market-cycles.md.
---

# Crypto and Digital Asset Intelligence

**How to reason about crypto market structure as it affects fan token signals.**
Extends `macro/macro-crypto-market-cycles.md` — do not re-read the four-phase cycle
model there. This file adds the structural reasoning layers beyond cycle phases.

> Load alongside: `macro/macro-crypto-market-cycles.md` (cycle phases 1-4)

---

## Bitcoin dominance framework

```
BITCOIN DOMINANCE AS MARKET STRUCTURE SIGNAL:

  WHAT BITCOIN DOMINANCE MEASURES:
    Bitcoin dominance = BTC market cap ÷ total crypto market cap.
    It measures whether capital is concentrating in Bitcoin (risk-off for alts)
    or rotating into altcoins (risk-on for alts including fan tokens).
    
  DOMINANCE MODIFIER TABLE:

  BTC Dominance       Signal               Fan token modifier
  ──────────────────────────────────────────────────────────
  Above 60%           Risk-off for alts    ×0.88 demand baseline
  50–60%              Neutral              ×1.00 (no modifier)
  Below 50%           Alt season likely    ×1.15 demand baseline

  APPLICATION:
    Check BTC dominance alongside the macro cycle phase.
    Dominance above 60% AND bear market phase: compound negative signal
      Apply both: ×0.88 dominance × ×0.85 bear phase = ×0.748 combined
      Apply: compound_floor = ×0.75 (do not go below this)
    Dominance below 50% AND bull market phase: compound positive signal
      Apply both: ×1.15 dominance × ×1.15 bull phase = ×1.3225 combined
      Apply: compound_ceiling = ×1.30 (cap at this level)
      
  AGENT RULE:
    Check BTC dominance independently from cycle phase.
    They are related but not identical — dominance can expand in early bull markets
    before altcoins catch up. Both signals required for complete assessment.
    Source: CoinGecko global market data (dominance percentage, real-time).
```

---

## Bitcoin price cycle framework (extended)

```
FOUR-PHASE OVERVIEW (see macro-crypto-market-cycles.md for full depth):
  Phase 1 (Accumulation) | Phase 2 (Expansion/Bull) |
  Phase 3 (Distribution) | Phase 4 (Contraction/Bear)

ADDITIONAL PHASE MODIFIERS NOT IN BASE FILE:

  ACCUMULATION PHASE (post-bear, pre-bull confirmation):
    Experienced holders: accumulating quietly; entry signal for long-term
    New entrants: absent — community growth is slow
    Fan token demand baseline: ×0.95
    Characterised by: low volume, muted sentiment, long consolidation periods
    
  DISTRIBUTION PHASE (late bull, before bear confirmation):
    Short-term: fan token demand ×1.10 (elevated by late-cycle FOMO)
    Risk: this is the phase of maximum danger for new entrants
    Exit signal: elevated volatility, muted new partnership announcements
    Signal flag: DISTRIBUTION_PHASE_CAUTION — elevated exit risk despite high prices
    
  KEY SIGNAL: BTC 200-DAY MOVING AVERAGE:
    BTC above 200-day MA with positive momentum = bull phase confirmed
    BTC below 200-day MA with negative momentum = bear phase confirmed
    BTC crossing 200-day MA with low volume = confirmation pending (wait)
    Apply: phase_confirmation_pending flag when 200-day MA cross is fresh (< 30 days)
```

---


---

## BTC sentiment regime framework

```
BTC CYCLE SENTIMENT REGIMES:
  The NUPL (Net Unrealized Profit/Loss) metric defines which sentiment
  regime is active. Each regime has a distinct demand modifier for fan tokens.
  Regimes are enduring framework categories — not daily metrics.

  CAPITULATION / DEPRESSION (NUPL < 0):
    Market is in extreme fear — most holders at a loss.
    Fan token demand modifier: ×0.70
    Rationale: risk-off behaviour is near-total. Only committed holders active.
    Signal duration: regime typically lasts weeks to months.

  HOPE / FEAR (NUPL 0.0 to 0.25):
    Market recovering from lows but uncertainty is high.
    Fan token demand modifier: ×0.88
    Rationale: downside correlation is elevated — fan tokens fall with BTC.
      Sentiment is fragile. Positive sporting events can still move demand,
      but the macro floor is lower than in neutral conditions.
    Key characteristic: governance signal weighting should be reduced by ×0.90
      in HOPE_FEAR regime — holder participation in votes is reduced.
    FTP PATH_2 interaction: WIN burn still fires, but demand response
      to the supply event is muted — apply ×0.90 to expected demand premium.

  OPTIMISM / ANXIETY (NUPL 0.25 to 0.50):
    Market in positive territory but anxiety about sustainability is present.
    Fan token demand modifier: ×0.95
    Rationale: improving sentiment but not yet confident.
    Standard modifiers apply with mild upward bias.

  BELIEF / THRILL (NUPL 0.50 to 0.75):
    Bull market in progress — holders in significant profit.
    Fan token demand modifier: ×1.10
    Rationale: risk appetite elevated, discretionary allocation to fan tokens grows.
    FTP PATH_2 WIN burns generate stronger demand responses in this regime.

  EUPHORIA / GREED (NUPL > 0.75):
    Late-cycle conditions — maximum retail participation.
    Fan token demand modifier: ×1.20 (short-term) then rapid reversal risk.
    Warning: apply this modifier cautiously — euphoria regimes are unstable.
    Agent rule: do not project euphoria modifier more than 2 weeks forward.

REGIME TRANSITION SIGNALS:
  Regime shifts are significant macro events — not incremental changes.
  When regime shifts from OPTIMISM to HOPE_FEAR:
    Apply ×0.88 modifier immediately on confirmed shift.
    Governance votes active during transition: apply ×0.85 participation weight.
    Commercial partnership signals launched in OPTIMISM may not land as expected.

  When regime shifts from HOPE_FEAR to OPTIMISM:
    Recovery signal — apply ×1.08 recovery premium for 7-14 days.
    Governance participation expected to recover.

REGIME IDENTIFICATION:
  Do not attempt to determine current regime from inference.
  Source: Glassnode, CryptoQuant — Tier 1 on-chain data providers.
  The regime label (HOPE_FEAR, OPTIMISM_ANXIETY, etc.) is a category framework.
  Apply the modifier for the labelled regime when a Tier 1 source confirms it.
  Do not log specific NUPL readings — those are expiring operational data.

FAN TOKEN DEMAND DURING HOPE_FEAR SPECIFICALLY:
  Standard demand modifier: ×0.88
  Governance votes: apply ×0.90 participation weight
  PATH_2 WIN burn demand response: multiply expected premium by ×0.90
  Duration signal: HOPE_FEAR is typically a multi-week to multi-month regime.
    Do not assume regime will resolve within a single fixture cycle.
```

## Altcoin season framework

```
ALTCOIN SEASON DEFINITION AND MODIFIERS:

  FORMAL DEFINITION:
    Altcoin season is confirmed when 75%+ of the top 50 altcoins
    (by market cap) outperform Bitcoin over a 90-day trailing period.
    
  MONITORING SOURCE:
    CoinGecko Altcoin Season Index — publicly available, updated continuously.
    Threshold: index reading above 75 = alt season confirmed.
    
  FAN TOKEN BEHAVIOUR IN ALT SEASON:
    Fan tokens historically outperform broader altcoins during alt season.
    Mechanism: fan tokens are further out on the risk curve than most altcoins;
      when capital rotates into alts, it eventually reaches niche/utility tokens.
    Apply: alt_season_fan_token_amplifier = ×1.20 during confirmed alt season
    
  FAN TOKEN BEHAVIOUR IN BITCOIN DOMINANCE EXPANSION:
    During confirmed Bitcoin dominance expansion (BTC dominance rising week-over-week):
    Capital is leaving alts and concentrating in BTC.
    Apply: dominance_expansion_suppressor = ×0.82 during confirmed BTC dominance expansion
    
  ALT SEASON TIMING RELATIVE TO BULL MARKET:
    Alt season typically lags the BTC bull market by 3-6 months.
    BTC peaks first; then capital rotates to large caps (ETH), then mid caps, then alts.
    Fan tokens typically reach their cycle peak in the late alt season phase.
    Agent rule: if BTC bull market is confirmed, alt season is likely 3-6 months away —
      not yet confirmed; apply bull market modifier (×1.15) not alt season modifier (×1.20).
```

---

## Ethereum and L2 signals

```
ETHEREUM GAS FEE ENVIRONMENT:

  HIGH GAS FEES:
    Reduces casual cross-chain trading activity.
    Bridges that use Ethereum as a settlement layer become expensive.
    Apply: high_gas_accessibility_discount = ×0.96 for fan tokens primarily
      accessed via Ethereum-connected bridge routes.
    Monitor: gas price above 50 gwei sustained = high gas condition
    
  LOW GAS FEES:
    Increases cross-chain activity; bridges become cost-effective for small trades.
    Increases fan token accessibility for retail holders.
    Apply: low_gas_accessibility_premium = ×1.02 (marginal; normalisation not uplift)
    Monitor: gas price below 10 gwei sustained = low gas condition

BASE AND SOLANA ACTIVITY SIGNALS:

  Fan Tokens V2.0 are live on Base and Solana (via LayerZero bridge).
  Activity levels on these chains directly affect fan token reach and demand.
  
  HIGH ACTIVITY ON BASE OR SOLANA:
    Apply: l2_activity_amplifier = ×1.05 to fan token demand signals
    Monitor: Base and Solana transaction volume trends (Dune Analytics, on-chain)
    Mechanism: higher chain activity = more potential buyers accessing fan tokens
    
  DEFI TVL GROWTH ON BASE AND SOLANA:
    Growing DeFi TVL signals increasing liquidity available for crypto assets.
    Apply: defi_tvl_growth_modifier = ×1.05 sustained when both chains show
      positive 30-day TVL growth trends.
    Source: DeFiLlama (publicly available TVL data)
```

---

## Stablecoin market intelligence

```
STABLECOIN MARKET CAP SIGNAL:

  STABLECOIN MARKET CAP GROWTH:
    Rising stablecoin market cap indicates capital has entered crypto and is
    waiting to be deployed. This is dry powder — a positive demand precursor.
    Apply: stablecoin_growth_demand_precursor = ×1.05 to demand signal confidence
    (Not a demand modifier itself — but increases reliability of positive demand signals)
    
  STABLECOIN MARKET CAP DECLINE:
    Declining stablecoin market cap indicates capital exiting crypto entirely.
    Negative signal for all crypto assets including fan tokens.
    Apply: stablecoin_decline_warning = flag; apply ×0.95 caution modifier

USDT AND USDC AVAILABILITY BY CHAIN:

  USDT/USDC available on Chiliz Chain natively:
    Reduces friction for fan token purchases. Positive accessibility signal.
    Apply: fiat_stablecoin_on_chain_modifier = ×1.03 for Chiliz Chain fan tokens
    
  USDT/USDC available on Base/Solana (for bridged V2.0 tokens):
    Full stablecoin support on both chains amplifies V2.0 token accessibility.
    Apply: ×1.03 for V2.0 BRIDGE_LIVE tokens (already have wider reach)

CLARITY ACT YIELD DESIGN CONSTRAINT (US SPECIFIC):

  ENDURING DESIGN BOUNDARY (applies if enacted; apply conservative interpretation now):
    PROHIBITED: passive/balance-based yield on stablecoins and fan tokens
    PERMITTED: activity-based rewards (governance, predictions, engagement)
    
  THIS PERMANENTLY SHAPES US FAN TOKEN UTILITY DESIGN:
    Any fan token platform targeting US holders must use activity-based reward models.
    "Buy and use" model: compliant.
    "Buy and hold for yield" model: non-compliant.
    
  Application: when assessing any US-linked fan token reward program,
    check against this boundary before applying a US market demand modifier.
    Source: macro/macro-regulatory-sportfi.md CLARITY Act section.
```

---

## CHZ native token framework

```
CHZ PRICE CYCLE EFFECTS ON FAN TOKENS:

  CHZ is the settlement and purchase currency for most fan token transactions.
  CHZ price movement therefore directly affects fan token purchasing dynamics.
  
  CHZ BULL (CHZ appreciating vs USD):
    Holders of CHZ can purchase more fan tokens per CHZ unit (relatively cheaper).
    New CHZ buyers are incentivised to enter → more potential fan token buyers.
    Apply: chz_bull_demand_amplifier = ×1.05 during sustained CHZ appreciation
    
  CHZ BEAR (CHZ depreciating vs USD):
    USD-priced fan token purchases become more CHZ-expensive.
    Reduced incentive to buy CHZ to then buy fan tokens.
    Apply: chz_bear_demand_suppressor = ×0.96 during sustained CHZ depreciation
    
CHZ VIRTUOUS CYCLE CONDITIONS:

  THREE COMPONENTS:
    1. Ecosystem growth: new club partnerships, new token launches
    2. Platform activity: governance votes, match predictions, user engagement
    3. Commercial partnerships: club deals, sponsor integrations
    
  ALL THREE RISING SIMULTANEOUSLY:
    virtuous_cycle_active = true
    Apply: virtuous_cycle_amplifier = ×1.12 to all fan token demand signals
    This is the strongest structural demand environment for the ecosystem
    
  TWO OF THREE ABSENT:
    virtuous_cycle_breakdown = true
    Apply: demand_headwind_modifier = ×0.93 across all tokens
    Not a crash — a structural headwind that persists until components recover
    
  ONE OF THREE ABSENT:
    No virtuous cycle modifier — monitoring mode
    Flag: virtuous_cycle_incomplete — watch for improvement or further deterioration
```

---

## Market structure signals

```
EXCHANGE LISTING / DELISTING SIGNALS:

  NEW EXCHANGE LISTING FOR CHZ:
    Positive ecosystem signal — broader CHZ access = broader fan token access
    Apply: new_listing_signal = ×1.08 sustained 2-4 weeks
    Tier matters: major exchange (Binance, Coinbase) > regional exchange
    Major exchange listing: ×1.12 | Regional exchange: ×1.05
    
  MAJOR EXCHANGE DELISTING OF CHZ:
    Negative ecosystem signal — reduced accessibility
    Apply: delisting_signal = ×0.88 sustained until relisting confirmed
    Monitor for: official exchange announcement as source (Tier 1 only)

SPOT BITCOIN ETF AND INSTITUTIONAL ADOPTION:

  SPOT BTC ETF CONFIRMED (enacted — applies where launched):
    Institutional capital can now access BTC in regulated wrappers.
    Indirect positive for all crypto including fan tokens.
    Apply: btc_etf_legitimacy_modifier = ×1.03 sustained
    Mechanism: institutional BTC adoption normalises crypto as an asset class;
      fan tokens benefit from this legitimacy premium at the margin.
    This is a slow-burn structural modifier — not a short-term spike.
    
  SPOT ETH ETF OR ALTCOIN ETF:
    If an ETF for a major altcoin is approved, the risk premium on all
    crypto assets decreases further.
    Apply: additional ×1.02 sustained for each approved altcoin ETF
    Cap: ETF legitimacy premium total ceiling ×1.08
```

---

## Compatibility

**Cycle phases (deep):**   `macro/macro-crypto-market-cycles.md`
**Regulatory layer:**      `macro/macro-regulatory-sportfi.md`
**Portfolio correlation:** `fan-token/portfolio-intelligence.md`
**Seasonal patterns:**     `core/seasonal-intelligence.md`
**Context bridge:**        `core/fan-token-context-bridge.md`

---

*SportMind v3.97.39 · MIT License · sportmind.dev*
*Extends macro-crypto-market-cycles.md — load both files for complete crypto intelligence*
