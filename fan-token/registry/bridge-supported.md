# Fan Token Bridge Support — V2.0 Multi-Chain Registry

**Definitive reference for Fan Token™ multi-chain support status.
All confirmed BRIDGE_LIVE tokens operate across three chains as of
the Fan Tokens V2.0 expansion (Chiliz official, April 2026).**

> Source: chiliz.com/chiliz-brings-fan-tokens-to-solana-and-base/ — VERIFIED
> Companion: fan-token/fan-token-pulse/references/chiliz-token-registry.md
> For supply data: fan-token/supply-intelligence.md
> For lifecycle context: fan-token/fan-token-lifecycle/fan-token-lifecycle.md

---

## Three-chain standard — Fan Tokens V2.0

```
FAN TOKENS V2.0 MULTI-CHAIN ARCHITECTURE:

  CHAIN 1 — Chiliz Chain (native):
    Role:     Settlement anchor and source of truth
    Standard: ERC-20 compatible (Chiliz Chain implementation)
    Decimal:  18 (upgraded from 0-decimal legacy standard)
    Explorer: chiliscan.com

  CHAIN 2 — Solana:
    Role:     High-throughput trading and DeFi access
    Bridge:   LayerZero protocol
    DEXs:     Jupiter, Raydium
    Standard: SPL token (Solana Program Library)

  CHAIN 3 — Base (Coinbase L2):
    Role:     Ethereum-ecosystem DeFi access
    Bridge:   LayerZero protocol
    DEXs:     Aerodrome, Uniswap Base
    Standard: ERC-20 (Base chain)

  BRIDGE MECHANISM:
    Protocol:  LayerZero omnichain messaging
    Direction: Chiliz Chain ↔ Solana ↔ Base (bidirectional)
    Settlement: Chiliz Chain remains the canonical settlement layer
    Ratio:     1:1 across all chains (no supply change on bridging)

  AGENT RULE:
    Post-V2.0, price discovery is multi-chain.
    On-chain monitoring must cover all three chains for confirmed BRIDGE_LIVE tokens.
    Bridge volume (Chiliz Chain → Solana/Base) is distinguishable from native volume
    and serves as a cross-chain accumulation/distribution signal.
```

---

## Confirmed BRIDGE_LIVE tokens (18 Fan Tokens™ + $CHZ + $PEPPER)

```
BRIDGE_LIVE STATUS — ALL THREE CHAINS CONFIRMED (April 2026):

FOOTBALL:
  $ACM   AC Milan Fan Token
  $AFC   Arsenal FC Fan Token          ← PATH_2 Model 2 confirmed
  $ARG   Argentina Fan Token
  $ASR   AS Roma Fan Token
  $ATM   Atlético de Madrid Fan Token
  $BAR   FC Barcelona Fan Token
  $CITY  Manchester City Fan Token
  $FLU   Fluminense Fan Token
  $GAL   Galatasaray Fan Token
  $INTER Inter Milan Fan Token
  $JUV   Juventus Fan Token
  $MENGO CR Flamengo Fan Token
  $NAP   SSC Napoli Fan Token
  $OG    OG Fan Token (Esports)
  $POR   FC Porto Fan Token
  $PSG   Paris Saint-Germain Fan Token
  $SPURS Tottenham Hotspur Fan Token
  $VCF   Valencia CF Fan Token

NATIVE CHAIN TOKENS:
  $CHZ   Chiliz native token (also BRIDGE_LIVE)
  $PEPPER Chiliz ecosystem token (also BRIDGE_LIVE)

TOTAL: 20 tokens confirmed BRIDGE_LIVE across Chiliz Chain, Solana, and Base.
```

---

## 18-decimal migration — technical context

```
DECIMAL MIGRATION (completed April 27, 2026):

  BEFORE V2.0 (legacy):
    Decimal places: 0
    Consequence: tokens only tradeable in whole units
    DeFi compatibility: limited (most DeFi protocols require 18 decimals)

  AFTER V2.0 (current):
    Decimal places: 18
    Consequence: fractional ownership enabled; full DeFi compatibility
    Price impact: sub-cent price movements now representable

  CONTRACT ADDRESS NOTE:
    All BRIDGE_LIVE tokens have new post-migration contract addresses.
    Legacy addresses are no longer the primary trading addresses.
    Verify current addresses at: chiliscan.com (Chiliz Chain)
    Verify Solana addresses via: Jupiter.ag token list
    Verify Base addresses via: Aerodrome or Uniswap Base token list

  AGENT RULE:
    Never use pre-April 2026 contract addresses for on-chain monitoring.
    Always verify contract addresses from chiliscan.com before any
    on-chain signal generation or transaction verification.
```

---

## Chain-specific monitoring

```
ON-CHAIN MONITORING BY CHAIN:

  CHILIZ CHAIN (chiliscan.com):
    Primary monitoring target for:
    - FTP supply events (burn/mint transactions → zero-address or treasury)
    - Holder count changes
    - Pre-liquidation events (Model 2, T-48h window)
    - Net bridge flow (tokens leaving to Solana/Base)

  SOLANA (Jupiter, Raydium, Birdeye):
    Monitoring for:
    - Trading volume (high-throughput, lower fees)
    - Accumulation patterns (rising Solana holder count pre-match)
    - Bridge inflow spikes (CHZ Chain → Solana = demand signal)
    - DEX price vs CHZ Chain price (arbitrage signals)

  BASE (Aerodrome, Uniswap Base, Basescan):
    Monitoring for:
    - DeFi yield activity (tokens deposited to yield protocols)
    - Institutional accumulation (lower gas, Coinbase-adjacent users)
    - Bridge inflow from Chiliz Chain
    - Cross-chain price correlation

  SIGNAL PATTERN — CROSS-CHAIN ACCUMULATION:
    Net inflow to Solana/Base before match day = accumulation signal
    Net outflow from Solana/Base after match = profit-taking signal
    Apply as: cross_chain_accumulation_modifier to pre-match CDI

  AGENT RULE:
    Do not monitor only Chiliz Chain — post-V2.0, 60-70%+ of volume
    may occur on Solana or Base depending on market conditions.
    Price is set by the aggregate of all three chains.
```

---

## V2.0 migration status flags

```
MIGRATION STATUS FLAGS (as of v3.97.22):

  BRIDGE_LIVE:           true for all 20 tokens
  MULTICHAIN_ACTIVE:     true for all 20 tokens
  DECIMAL_MIGRATION:     COMPLETE (April 27, 2026)
  V2.0_STANDARD:         ACTIVE

  BINANCE CAP20 MIGRATION (separate event — May 11, 2026):
    8 tokens have Binance deposit/withdrawal suspension as of 2026-05-11 01:00 UTC:
    $ACM $ASR $ATM $BAR $CITY $JUV $OG $PSG
    Status: V2_MIGRATION_ACTIVE + MIGRATION_SUSPENSION (Binance only)
    Trading: UNAFFECTED on Binance | DEX trading unaffected on all chains
    $AFC: NOT in Binance migration list — unaffected
    Monitor: Binance announcement for completion date

  NOTE: The Binance CAP20 migration and the Fan Tokens V2.0 bridge expansion
  are separate events. V2.0 bridge = chain expansion (complete).
  Binance CAP20 = exchange-level contract migration (in progress May 2026).
```

---

## Compatibility

**Lifecycle:**  `fan-token/fan-token-lifecycle/fan-token-lifecycle.md`
**Registry:**   `fan-token/fan-token-pulse/references/chiliz-token-registry.md`
**Supply:**     `fan-token/supply-intelligence.md`
**On-chain:**   `fan-token/on-chain-event-intelligence/`
**FTP:**        `fan-token/ftp-path2.md`

---

*SportMind v3.97.22 · MIT License · sportmind.dev*
*Fan Tokens V2.0 confirmed: chiliz.com/chiliz-brings-fan-tokens-to-solana-and-base/*
*All 20 tokens: BRIDGE_LIVE across Chiliz Chain, Solana, and Base*
