---
name: fan-token-play
description: >
  Fan Token Play — dynamic mint/burn tokenomics framework for club Fan Tokens.
  Introduces protocol-level supply mechanics directly linking competitive match
  results to on-chain token supply. Announced April 2026, in public testing.
  Includes protocol-level treasury model and PATH_2 prediction market model
  ($AFC trial only). Load alongside fan-token/burn-to-glory-framework.md
  and fan-token/ftp-path2.md for full burn mechanic picture.
  Library Rule: PASSES — mechanic is enduring structural architecture,
  not tied to any specific season, result, or tournament.
---

# Fan Token Play — Dynamic Mint/Burn Tokenomics Framework

**Most significant Fan Token supply mechanic introduced since the 2019 launch.**
**Announced April 2026. In public testing phase.**

> Library Rule: No match results, specific prices, or perishable data.
> This file teaches agents how to reason about Fan Token Play mechanics —
> not what happened in any specific match.

---

## What is Fan Token Play

Fan Token Play introduces dynamic supply mechanics for club Fan Tokens,
directly linking on-pitch competitive results to on-chain token supply.
The mechanic operates at the protocol level via treasury-controlled smart
contracts. Two models exist: the treasury model (in public testing across
club tokens) and the PATH_2 prediction market model ($AFC trial only).

---

## Protocol-level treasury model

```
SUPPLY MECHANIC:
  WIN:  tokens permanently burned from treasury → circulating supply ↓
  LOSS: tokens minted to treasury → circulating supply ↑
  DRAW: no supply change

TRIGGER CONDITIONS:
  Qualifying matches: official men's first-team competitive matches only
  Scope: club Fan Tokens (NOT national team tokens)
  Execution: treasury-controlled smart contracts — no user action required
  User wallets: UNAFFECTED — treasury mechanics only

SUPPLY GUARDRAILS:
  Stop-loss floor:   Burns cease at 75% net supply reduction OR
                     treasury depletion to 0%
  Burn credits:      WIN at stop-loss generates credits offsetting
                     future minting on subsequent LOSS results
  Vesting cap:       Treasury releases capped per year
  Annual inflation:  Variable — linked to season win rate

AGENT RULE:
  Fan Token Play treasury model applies to club tokens only.
  Do not apply to national team tokens ($ARG, $POR, $SAFA, $SFA, $BELG).
  National team supply mechanics → fan-token/burn-to-glory-framework.md
  Always verify whether a specific club token has Fan Token Play active
  before applying supply signals.
```

---

## PATH_2 prediction market model — $AFC trial only

```
WHAT IT IS:
  Pre-liquidation prediction market model — a distinct implementation
  of Fan Token Play mechanics using market settlement rather than
  direct treasury action.

MECHANICS:
  Pre-liquidation:    1/400th of circulating supply pre-liquidated
                      at T-48h before kickoff
  WIN outcome:        Proceeds buy back and burn tokens from secondary
                      market (95% of proceeds after fee)
  LOSS outcome:       Equivalent tokens minted back to treasury
  Execution window:   48h pre-kickoff + 48h post-result
  Settlement basis:   90-MINUTE RESULT ONLY — extra time and penalties
                      not included (see fan-token/ftp-path2.md)

CONFIRMED SCOPE:
  $AFC (Arsenal Fan Token) ONLY as of current library state.
  Do not generalise PATH_2 mechanics to other club tokens.
  PATH_2 is a specific trial implementation — not the standard model.

AGENT RULE:
  PATH_2 is Fan Token Play prediction market model.
  It is NOT the same as the treasury model.
  For $AFC pre-match analysis: load fan-token/ftp-path2.md
  for the full PATH_2 signal framework.
```

---

## Four-way burn mechanic distinction

There are now FOUR distinct burn mechanics in the Chiliz/Socios ecosystem.
Agents must never conflate them. All four can be active simultaneously
on different tokens.

```
1. CHZ BUY-BACK BURN
   Asset:    CHZ native token (not Fan Tokens)
   Source:   10% of Fan Token revenue across all chains
   Trigger:  Automatic, revenue-linked, ongoing
   Cadence:  Monthly burn reports at chiliz.com
   User:     UNAFFECTED

2. FAN TOKEN PLAY — TREASURY MODEL
   Asset:    Fan Token (club tokens)
   Source:   Club treasury
   Trigger:  Competitive match result (WIN=burn / LOSS=mint / DRAW=none)
   Scope:    Club tokens in public testing — verify per token
   User:     UNAFFECTED

3. FAN TOKEN PLAY — PATH_2 PREDICTION MARKET MODEL
   Asset:    Fan Token (club tokens)
   Source:   Pre-liquidation + secondary market
   Trigger:  WIN/LOSS settlement at 90 minutes
   Scope:    $AFC ONLY (confirmed trial)
   User:     UNAFFECTED — market mechanics only

4. BURN TO GLORY
   Asset:    Fan Token (national team tokens)
   Source:   Issuing entity treasury
   Trigger:  Team WIN in tournament match
   Scale:    Progressive Group 1% → Final 10%
   Scope:    $ARG · $POR · $SAFA · $SFA · $BELG (WC2026 confirmed)
   User:     UNAFFECTED

AGENT RULE:
  Always identify WHICH mechanic applies to the specific token.
  CHZ buy-back → affects CHZ price
  Fan Token Play treasury → affects club Fan Token supply (testing)
  Fan Token Play PATH_2 → affects $AFC supply (90-min settlement)
  Burn to Glory → affects national Fan Token supply (WIN only)
  Never apply one mechanic's logic to another token type.
  All four can be active in the same period — treat independently.
```

---

## Signal interaction with macro regime

```
CAPITULATION REGIME (×0.70 suppressor active):
  Fan Token Play mechanics execute regardless of macro regime.
  Demand signal from supply events is suppressed by ×0.70.
  The burn/mint is real — the price impact is regime-dampened.

RECOVERY REGIME (×1.00 or higher):
  Full demand signal applies to each supply event.
  WIN streaks compound deflationary narrative in recovery.

AGENT RULE:
  Always check macro regime before applying Fan Token Play
  demand signal. Load macro/macro-crypto-market-cycles.md
  for current regime state.
```

---

## Verification requirement

```
Fan Token Play is an opt-in mechanic — not all club tokens
participate automatically. Confirm participation before applying signals.

VERIFICATION SOURCES (priority order):
  1. fantokens.com/fan-token-play — official mechanic announcements
  2. chiliz.com/newsroom — Chiliz official press releases
  3. socios.com — token page with mechanic confirmation
  4. chiliscan.com — on-chain event verification

AGENT RULE:
  Never assume a club token participates in Fan Token Play.
  Confirm via Tier 1 source before applying supply signals.
  If unconfirmed: treat as demand-only club token (standard framework).
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan Token Play mechanic intelligence: treasury model, PATH_2, supply guardrails |
| Reasoning | ACTIVE | Reasoning chain from match result to supply event to demand signal |
| Context | ACTIVE | Match type, token scope, macro regime, stop-loss guardrail conditions |
| Memory | ACTIVE | PATH_2 $AFC trial confirmed. Public testing phase as of April 2026 |
| Judgment | ACTIVE | Four-way burn distinction — agent must identify correct mechanic per token |
| Attention | ACTIVE | Elevated attention at stop-loss threshold and during PATH_2 execution window |
| Communication | NOT APPLICABLE | Output format layer — governed by pre-match signal framework |
| Verification | ACTIVE | Four-source verification required before applying any Fan Token Play signal |
| Learning | ACTIVE | Public testing phase — calibration records accumulating |
| Integration | ACTIVE | Integrates with ftp-path2.md, burn-to-glory-framework.md, macro-crypto-market-cycles.md |
| Calibration | ACTIVE | Supply guardrail values (75% floor, 1/400 PATH_2) confirmed from official source |
| Adaptation | ACTIVE | Framework adapts as public testing expands to more club tokens |
| Ethics | EMERGING | User wallet safety implications of dynamic supply to be developed |
| Transparency | ACTIVE | All four mechanics, their sources, scopes, and user impact always explicit |

---

## Compatibility

**PATH_2 full framework:** `fan-token/ftp-path2.md`
**Burn to Glory:** `fan-token/burn-to-glory-framework.md`
**CHZ buy-back:** `fan-token/registry/bridge-supported.md`
**Macro regime:** `macro/macro-crypto-market-cycles.md`
**On-chain verification:** `fan-token/on-chain-event-intelligence/`

---

*SportMind v4.0.7 · MIT License · sportmind.dev*
*Enduring framework — applies to any club token with confirmed Fan Token Play activation.*
*All 14 Mind dimensions mapped.*
