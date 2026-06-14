---
name: burn-to-glory-framework
description: >
  Enduring framework for performance-linked treasury burn mechanics in fan tokens.
  Applies to any tournament where a token issuer implements a progressive burn
  schedule tied to match progression. First confirmed instance: FIFA World Cup 2026
  (Chiliz/Socios — five national team tokens).
  Load alongside fan-token/national-team-tokens.md and fan-token/ftp-path2.md.
---

# Burn to Glory — Performance-Linked Treasury Burn Framework

**Enduring framework for tournament-linked treasury burn mechanics. Applies to any future tournament where this mechanic is active.**

> Library Rule: No match results, named players, tournament brackets, or current prices. This file teaches agents how to reason about the Burn to Glory mechanic — not what happened in any specific tournament.

---

## What is Burn to Glory

Burn to Glory is a performance-linked treasury burn mechanic introduced by Chiliz/Socios for national team fan tokens in major tournaments. When a token's associated nation wins a match, a percentage of the issuing entity's treasury holdings of that token is permanently burned. The burn source is always the treasury — user wallets are never affected. This is a structural supply reduction mechanic tied to sporting performance, distinct from FTP PATH_2 in both trigger, source, and scale.

---

## Critical distinction — Burn to Glory vs FTP PATH_2

```
BURN TO GLORY:
  Trigger:      Team WIN in tournament match
  Burn source:  Issuing entity treasury holdings only
  User wallets: UNAFFECTED — never touched
  Scale:        Progressive — percentage increases with tournament round
  Tokens:       National team tokens (tournament-specific activation)
  Confirmed:    Chiliz/Socios — FIFA World Cup 2026 (five tokens)

FTP PATH_2:
  Trigger:      WIN in qualifying match (pre-liquidation model)
  Burn source:  Market (pre-liquidated from circulating supply)
  User wallets: UNAFFECTED — settlement via prediction market
  Scale:        Fixed per-match (circulating_supply / 400)
  Tokens:       Club tokens only (confirmed: $AFC)
  Confirmed:    Arsenal Fan Token only as of current library state

AGENT RULE:
  Never conflate Burn to Glory with FTP PATH_2.
  They are separate mechanics with different triggers, sources, and scales.
  Burn to Glory = treasury deflationary | FTP PATH_2 = market settlement
  A token can have both mechanics active simultaneously if both are confirmed.
  Always identify which mechanic is active before applying signal weights.
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
| Memory | ACTIVE | Burn to Glory first confirmed instance: WC2026 — five national tokens |
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

*SportMind v4.0.2 · MIT License · sportmind.dev*
*Enduring framework — applies to any tournament with confirmed Burn to Glory activation.*
*All 14 Mind dimensions mapped.*
