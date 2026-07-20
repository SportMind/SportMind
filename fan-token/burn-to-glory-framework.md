---
name: burn-to-glory-framework
description: >
  Enduring framework for performance-linked treasury burn mechanics in fan tokens.
  Applies to any tournament where a token issuer implements a progressive burn
  schedule tied to match progression. First confirmed instance: FIFA World Cup 2026
  (Chiliz/Socios — six national team tokens).
  Load alongside fan-token/national-team-tokens.md and fan-token/ftp-path2.md.
---

# Burn to Glory — Performance-Linked Treasury Burn Framework

**Enduring framework for tournament-linked treasury burn mechanics. Applies to any future tournament where this mechanic is active.**

> Library Rule: No match results, named players, tournament brackets, or current prices. This file teaches agents how to reason about the Burn to Glory mechanic — not what happened in any specific tournament.

---

## What is Burn to Glory

Burn to Glory is a performance-linked treasury burn mechanic introduced by Chiliz/Socios for national team fan tokens in major tournaments. When a token's associated nation wins a match, a percentage of the issuing entity's treasury holdings of that token is permanently burned. The burn source is always the treasury — user wallets are never affected. This is a structural supply reduction mechanic tied to sporting performance, distinct from FTP PATH_2 in both trigger, source, and scale.

---

## Three-way burn mechanic distinction

There are three distinct burn mechanics active in the Chiliz/Socios
ecosystem. Agents must never conflate them. All three can be active
simultaneously.

```
CHZ BUY-BACK BURN:
  What:     10% of Fan Token revenue across all chains → open market
            CHZ purchase → permanent burn
  Source:   Protocol-level — Chiliz treasury executes automatically
  Asset:    CHZ native token (not Fan Tokens)
  Trigger:  Ongoing — fires on all Fan Token trading revenue
  Cadence:  Monthly burn reports published at chiliz.com
  User:     UNAFFECTED — no user action required or possible

BURN TO GLORY:
  What:     Performance-linked treasury burn of Fan Token supply
  Source:   Issuing entity treasury holdings only
  Asset:    Fan Token (national team tokens confirmed WC2026)
  Trigger:  Team WIN in tournament match
  Scale:    Progressive — Group 1% → Final 10% (~25.18% compound max)
  User:     UNAFFECTED — treasury burn only
  Confirmed: $ARG · $POR · $BELG · $SAFA · $SFA · $SPAIN

FTP PATH_2:
  What:     Pre-liquidation market settlement — prediction market model
  Source:   Market (1/400th of circulating supply pre-liquidated T-48h)
  Asset:    Fan Token (club tokens only)
  Trigger:  WIN in qualifying PATH_2 match
  Scale:    Fixed — circulating_supply / 400 per match
  User:     UNAFFECTED — market mechanics only
  Confirmed: $AFC only as of current library state

AGENT RULE:
  Always identify WHICH mechanic is active before applying signals.
  CHZ buy-back burn → affects CHZ price / deflationary pressure
  Burn to Glory → affects Fan Token supply (national tokens, WIN-only)
  FTP PATH_2 → affects Fan Token supply ($AFC only, pre-liquidation)
  All three can be active in the same period — treat independently.
  Never conflate. Never apply one mechanic's logic to another's asset.
```

---

## Burn schedule — progressive by round

```
BURN TO GLORY — STANDARD SCHEDULE (Chiliz/Socios implementation):

  Stage                   Treasury burn on WIN
  Group stage             1.0%
  Round of 32             2.0%
  Round of 16             2.5%
  Quarter-final           5.0%
  Semi-final              7.5%
  Final                   10.0%

  COMPOUND EFFECT (maximum run — all stages won):
    Full tournament: ~25.18% compound burn of initial treasury holding
    Actual compound effect depends on tournament format and bracket depth.

  LOSS OR DRAW:
    No burn triggered. Treasury holding unchanged.
    Supply is not increased — this is NOT a mint mechanic.
    Burn to Glory is asymmetric: wins reduce supply, non-wins do not increase it.

  AGENT RULE:
    Burn to Glory is a WIN-ONLY supply reduction mechanic.
    No supply event on LOSS or DRAW.
    Apply the correct stage percentage — do not use a flat rate across rounds.
    Track cumulative burn percentage as tournament progresses.
```

---

## Signal interaction with macro regime

```
BURN TO GLORY x MACRO REGIME:

  CAPITULATION regime (×0.70 suppressor active):
    Burn to Glory fires normally — supply reduction is structural.
    Demand signal for the burn is suppressed by ×0.70.
    The burn itself is real; the price impact is dampened by macro conditions.

  RECOVERY regime (×1.00 or higher):
    Full demand signal applies to each burn event.
    Progressive burns in knockout rounds compound with recovering macro.

  AGENT RULE:
    Always check macro regime before applying Burn to Glory demand signal.
    The burn executes regardless of macro — but price impact is regime-dependent.
    Load macro/macro-crypto-market-cycles.md for current regime state.
```

---

## Compound signal — Burn to Glory × tournament occasion weight

```
COMPOUND SIGNAL FRAMEWORK:

  Burn to Glory interacts with tournament occasion weights in the SportMind
  signal architecture. Supply reduction (burn) and demand amplification
  (occasion weight) are separate signals that compound when both are active.

  Semi-final WIN example (enduring logic — no specific results):
    7.5% treasury burn + high occasion weight demand signal
    These are additive, not multiplicative — apply separately in signal chain.

  AGENT RULE:
    Calculate burn signal and occasion weight signal independently.
    Sum them in the output — do not multiply.
    Flag both in the recommended action output.
```

---

## Token eligibility and verification

```
VERIFICATION REQUIREMENT:

  Burn to Glory is an opt-in mechanic — not all national team tokens
  participate automatically. Confirm participation before applying signals.

  VERIFICATION SOURCES (priority order):
    1. fantokens.com/fan-token-play — official mechanic announcements
    2. chiliz.com/newsroom — Chiliz official press releases
    3. socios.com — token page with mechanic confirmation
    4. chiliscan.com — on-chain burn event verification

  AGENT RULE:
    Never assume a national team token participates in Burn to Glory.
    Confirm via Tier 1 source before applying burn signal.
    If unconfirmed: treat as demand-only national token (standard framework).
    Load fan-token/national-team-tokens.md for demand-only signal framework.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Burn to Glory mechanic intelligence: schedule, source, compound effect |
| Reasoning | ACTIVE | Reasoning chain from match result to treasury burn to supply signal |
| Context | ACTIVE | Tournament context: stage, round, macro regime, occasion weight |
| Memory | ACTIVE | Burn to Glory first confirmed instance: WC2026 — six national tokens |
| Judgment | ACTIVE | Judgment on burn signal materiality — progressive scale requires stage awareness |
| Attention | ACTIVE | Maximum attention at knockout rounds — burn percentage increases sharply |
| Communication | ACTIVE | Output always states: stage, burn %, treasury source, macro regime modifier |
| Verification | ACTIVE | Four-source verification required before applying Burn to Glory signal |
| Learning | ACTIVE | Mechanic calibration developing — WC2026 is first confirmed live instance |
| Integration | ACTIVE | Integrates with national-team-tokens.md, ftp-path2.md, tournament-macro.md |
| Calibration | EMERGING | First tournament cycle — calibration records accumulating via WC2026 |
| Adaptation | ACTIVE | Framework adapts as Chiliz/Socios extend mechanic to future tournaments |
| Ethics | ACTIVE | Treasury source must always be stated — user wallets never affected |
| Transparency | ACTIVE | Burn source, percentage, stage, and macro modifier always explicit in output |

---

## Compatibility

**National team demand:** `fan-token/national-team-tokens.md`
**FTP PATH_2 (club tokens):** `fan-token/ftp-path2.md`
**Tournament macro:** `macro/tournament-macro.md`
**On-chain verification:** `fan-token/on-chain-event-intelligence/`
**WC2026 specific:** `fan-token/world-cup-2026-intelligence/`

---

## Treasury Size Variation — Agent Rule

Confirmed structural fact (Tier 1, July 2026). Additive to the
percentage scale framework above.

```
STRUCTURAL FACT:
  Burn to Glory applies identical percentage rates across all
  participating tokens at each stage. However, the absolute number
  of tokens burned varies significantly across participants because
  each token begins the campaign with a different treasury size.

KEY AGENT RULE — PERCENTAGE IS THE COMPARABLE METRIC:
  When comparing Burn to Glory outcomes across multiple tokens:
  · Use burn PERCENTAGE as the comparable metric — uniform by stage
  · Do NOT compare absolute burn amounts across different tokens
  · Absolute amount = percentage × token's remaining treasury at
    time of burn — and treasuries differ materially between tokens

TREASURY SIZE PATTERN:
  · A newer token (recent FTO) typically has a larger remaining
    treasury than a long-established token with existing holder
    distribution and prior burn history
  · The same Final win (10%) therefore produces a larger absolute
    burn for a newer token than for a mature token
  · This does NOT mean the newer token has a stronger supply signal —
    the percentage impact on remaining supply is what matters

SUPPLY SIGNAL REASONING — CORRECT METHOD:
  To assess the structural supply impact of a Burn to Glory event:
  1. Load the token's current treasury balance (chiliscan.com)
  2. Apply the stage percentage to the current treasury balance
  3. Express the result as % of remaining supply (not absolute count)
  4. Compare across tokens only on this percentage basis

  Absolute token counts are useful for on-chain verification only —
  not for cross-token supply impact comparison.
```

---

*SportMind v4.1.12 · MIT License · sportmind.dev*
*Enduring framework — applies to any tournament with confirmed Burn to Glory activation.*
*See fan-token/fan-token-play.md for the full four-way burn mechanic distinction.*
*All 14 Mind dimensions mapped.*
