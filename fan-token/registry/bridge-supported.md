---
name: bridge-supported
description: >
  Fan Token omnichain bridge registry. Documents confirmed omnichain tokens available
  on Solana and Base via the official Chiliz omnichain bridge (LayerZero technology),
  bridge mechanics, revenue model, DeFi availability, and ecosystem token status.
  As of April 28 2026 Fan Tokens are available on Solana and Base.
---

# SportMind Fan Token Bridge Registry
## Omnichain — Solana and Base

> As of April 28 2026 Fan Tokens are available on Solana and Base via the official
> Chiliz omnichain bridge using LayerZero technology.
>
> Chiliz Chain remains the primary chain. Solana and Base are distribution layers
> extending reach into the broader crypto economy.

---

## Confirmed Omnichain Tokens

CLUB TOKENS — Chiliz Chain + Solana + Base (three chains):

```
$AFC  — Arsenal FC
$BAR  — FC Barcelona
$CITY — Manchester City
$JUV  — Juventus
$PSG  — Paris Saint-Germain
```

NATIONAL TEAM TOKENS — Chiliz Chain + Solana only (two chains):

```
$ARG   — Argentina National Team
$POR   — Portugal National Team
$SAFA  — South Africa National Team
$SFA   — Scotland National Team
$BELG  — Belgium National Team
$SPAIN — Spain National Team (Solana confirmed June 2026)
```

CRITICAL DISTINCTION:
  Club tokens: Chiliz Chain + Solana + Base
  National tokens: Chiliz Chain + Solana only (not Base)
  Do not conflate. Base access is club-token-only as of June 2026.
  Bridge model (club tokens): lock-and-mint via LayerZero
  DeFi (national tokens): Jupiter DEX aggregator + Meteora
  liquidity protocol

All other active Chiliz Chain tokens may be bridged using the official Chiliz bridge
at app.fantokens.com but are not yet confirmed as actively traded on Solana or Base.

---

## Bridge Mechanics

```
Bridge:      Official Chiliz omnichain bridge
Technology:  LayerZero multi-DVN setup
Security:    Multi-DVN verification — multiple independent networks verify
             each cross-chain message
Bridge URL:  app.fantokens.com
Docs:        docs.chiliz.com/learn/about-bridging
```

---

## Revenue Model

```
10% of Fan Token revenue generated across all supported chains is allocated to
$CHZ buybacks — permanently removing $CHZ from circulating supply.

This creates a direct link between Fan Token trading activity on Solana and Base
and $CHZ deflationary pressure.
```

---

## Ecosystem Tokens — Omnichain

```
$CHZ    — Chiliz Chain, Solana, Base  (gas token — not a Fan Token)
$PEPPER — Chiliz Chain, Solana        (Kayen DEX governance token — not a Fan Token)
```

---

## DeFi Availability

```
On Solana:       Meteora and Jupiter DEX
On Base:         Standard EVM-compatible DEXs
On Chiliz Chain: FanX (Kayen) DEX
```

Fan Tokens now behave identically to ERC-20 tokens from any DeFi protocol's
perspective — 18-decimal precision enables full DeFi composability.

---

## Agent Intelligence Notes

```
OMNICHAIN DEMAND SIGNAL:
  Confirmed omnichain tokens have higher accessible holder base than
  Chiliz-Chain-only tokens. Apply ×1.05 addressable market premium
  when modelling demand for the five confirmed omnichain tokens.
## DeFi Platforms by Chain

```
SOLANA — Club tokens:
  Jupiter DEX aggregator — primary Solana trading venue
  Orca — liquidity pools

BASE — Club tokens:
  Aerodrome — primary Base liquidity protocol
  LP rewards via Aerodrome native infrastructure

SOLANA — National tokens:
  Jupiter DEX aggregator
  Meteora — liquidity protocol (confirmed June 2026)

DEX CAMPAIGN PATTERN:
  Chiliz runs competitive DEX trading campaigns during major events.
  Volume-ranked leaderboard with prize pools across platforms.
  This is a structural demand lever — DEX campaign volume amplifies
  organic demand during high-stakes fixtures and tournaments.
  Model DEX campaign volume separately from baseline organic volume.
```

CHZ BUYBACK MECHANIC:
  10% of Fan Token revenue across all chains → open market CHZ
  purchase → permanent burn.
  Cadence: monthly. Chiliz publishes burn reports at chiliz.com.

  THREE-WAY BURN DISTINCTION (never conflate):
    CHZ buy-back burn: protocol-level, CHZ asset, ongoing revenue
    Burn to Glory: treasury burn, Fan Token asset, WIN-triggered
    FTP PATH_2: market settlement, Fan Token asset, $AFC only
    See fan-token/burn-to-glory-framework.md for full framework.

BRIDGE SECURITY:
  LayerZero multi-DVN setup. Each cross-chain message requires multiple
  independent network verifications. This is institutional-grade bridge
  security — not a single-point-of-failure architecture.
```

---


---

## UCL Final Fan Token Club Pattern

```
SIGNAL: UCL Finals between fan token clubs — three consecutive finals (2023–2026)

CONFIRMED PATTERN:
  2023 UCL Final: Manchester City ($CITY) vs Inter Milan ($INTER)
    Result: Man City WIN
  2025 UCL Final: Paris Saint-Germain ($PSG) vs Inter Milan ($INTER)
    Result: $PSG WIN
  2026 UCL Final: Paris Saint-Germain ($PSG) vs Arsenal ($AFC)
    Scheduled: 30 May 2026, Puskás Aréna, Budapest
    Status: Fan token clubs in BOTH positions
    FTP PATH_2: ACTIVE ($AFC) — first UCL Final with live supply event mechanism

PATTERN SIGNIFICANCE:
  Fan token clubs are DISPROPORTIONATELY represented in UCL finals.
  All three consecutive UCL finals featured BOTH clubs with active fan tokens.
  The 2026 distinction: $AFC has FTP PATH_2 ACTIVE — making it the first UCL Final
  where a live burn/mint supply event fires based on the match result.
  2023 and 2025 finals had fan tokens but no active FTP burn/mint mechanics.
  This is not random — fan token clubs tend to be the highest-funded, most
  commercially active clubs in European football. Commercial investment and
  sporting success are correlated.

ENDURING SIGNAL FOR AGENT REASONING:
  When reasoning about competitive trajectory for top-tier fan token clubs:
    · UCL finalist status = CDI amplifier (×1.25 minimum, see competition-calendar-intelligence.md)
    · UCL final WIN = highest compound supply event in SportMind (×2.00 demand × burn event)
    · For $AFC specifically: UCL final WIN = PATH_2 supply reduction at maximum demand moment
    · For $PSG specifically: UCL final WIN = PATH_2 supply reduction (if PATH_2 confirmed)

AGENT RULE:
  When two fan token clubs meet in a UCL final:
    BOTH tokens receive the UCL Final demand premium simultaneously.
    The winning token's PATH_2 burn fires at peak demand.
    The losing token's PATH_2 mint fires at peak demand — supply expansion at worst moment.
    This asymmetry is the highest-stakes supply signal in the fan token ecosystem.

CALIBRATION NOTE:
  All three finals featured clubs with active fan tokens.
  The genuine 2026 distinction: $AFC has FTP PATH_2 ACTIVE — this is the FIRST UCL
  Final where a live supply event mechanism (burn on WIN, mint on LOSS) fires based
  on the match result. 2023 and 2025 had fan tokens but no active FTP mechanics.
  Token launch dates: $PSG January 2020 | $CITY March 2021 | $INTER September 2021 | $AFC 2021
  Monitor: relative price performance of $AFC and $PSG in the 72h window around
  the 2026 UCL Final for calibration baseline.
```

## Cross-Reference

**Complete registry:**         `fan-token/registry/complete-registry.md`
**DeFi integration:**          `fan-token/defi-integration-intelligence.md`
**FTP PATH_2 mechanics:**      `fan-token/ftp-path2.md`
**Ecosystem health:**          `fan-token/ecosystem-health-intelligence.md`
**Staking intelligence:**      `fan-token/staking-intelligence.md`

---

*SportMind v4.0.3 · MIT License · sportmind.dev*
*Five confirmed omnichain tokens: $AFC, $BAR, $CITY, $JUV, $PSG.*
*10% of cross-chain Fan Token revenue → $CHZ buybacks (permanent deflationary mechanic).*
