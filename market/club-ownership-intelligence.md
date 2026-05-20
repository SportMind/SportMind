---
name: club-ownership-intelligence
description: >
  Enduring reasoning framework for club ownership transition intelligence.
  Covers ownership transition stages and modifier weights, failed takeover
  signal framework, new ownership honeymoon period, distressed sale versus
  strategic acquisition profiles, and how ownership uncertainty affects FTP
  PATH_2 mechanics, CDI signals, and fan token governance stability.
---

# Club Ownership Intelligence

**How ownership transitions, failed takeovers, and ownership uncertainty affect fan token signals.**
Ownership signals are market-level — they affect CDI, governance, and commercial signals simultaneously.

---

## Why ownership matters for fan token intelligence

```
Club ownership affects fan tokens through three distinct channels:

  COMMERCIAL CHANNEL:
    New owner brings new commercial strategy, sponsors, and partnerships.
    Distressed sale or collapsed takeover suppresses commercial pipeline.
    Modifier applied to CDI signals.

  GOVERNANCE CHANNEL:
    Ownership uncertainty compromises governance vote credibility.
    New ownership may modify or override governance decisions.
    Modifier applied to governance signal confidence weights.

  SPORTING CHANNEL:
    Ownership investment drives squad development and manager appointments.
    Financial distress reduces sporting ambition — affects adjusted score.
    Modifier applied to medium-term form trajectory.

These three channels are independent — apply all three simultaneously.
Do not use one modifier for all three effects.
```

---

## Ownership transition stage framework

```
STAGE 1 — RUMOUR / UNCONFIRMED INTEREST:
  Tier 5 source only: no modifier — noise level signal.
  Tier 1/2 source naming specific bidder:
    CDI: ×0.95 uncertainty | Governance: ×0.97 | Sporting: ×1.00

STAGE 2 — LOI / EXCLUSIVITY SIGNED:
  Confirmed by Tier 1 source.
  CDI: ×0.92 | Governance: ×0.92 | Sporting: ×1.00
  Rationale: exclusivity means no competing bid possible during period.
    If deal fails, no immediate alternative.

STAGE 3 — DUE DILIGENCE / PROOF OF FUNDS PENDING:
  Proof of funds not yet confirmed — deal not progressing.
  CDI: ×0.88 | Governance: ×0.85 | Sporting: ×0.97
  Apply FUNDING_UNCERTAINTY_ACTIVE flag.

STAGE 4A — TAKEOVER CONFIRMED:
  New ownership confirmed by official regulatory channels.
  CDI: ×1.12 honeymoon premium (90 days)
  Governance: ×0.96 (restoring — new owner not yet established)
  Sporting: ×1.05 (investment signal, new era)
  See honeymoon framework below.

STAGE 4B — TAKEOVER_COLLAPSED:
  Deal fails, existing ownership continues.
  CDI: ×0.82 sustained (COMMERCIAL_DISTRESS_SIGNAL tier)
  Governance: ×0.80 credibility weight on all votes
  Sporting: ×0.94 (ambition signal lost)
  Duration: minimum 90 days, reassess quarterly.
  See collapsed takeover framework below.
```

---

## Collapsed takeover signal framework

```
TAKEOVER_COLLAPSED is a compound negative signal across all three channels.
It is not equivalent to a simple commercial setback.

WHY IT IS SEVERE:
  1. Club was for sale — signals existing ownership weakness or intent to exit.
  2. Exclusivity period closed off competing bids.
  3. Commercial partners who paused decisions face renewed uncertainty.
  4. Governance credibility is compromised — who is authoritative?
  5. Sporting investment plans that depended on new ownership evaporate.

IMMEDIATE RESPONSE (T+0 to T+14):
  Apply all three channel modifiers simultaneously.
  Do not wait for secondary confirmation — the collapse itself is the signal.

RESOLUTION PATHS:
  New buyer (new LOI): CDI ×1.05 recovery | Governance ×0.90 (still uncertain)
  New buyer (confirmed): CDI ×1.10 | Governance ×0.95 | Sporting ×1.08
  Existing owner stabilises (Tier 1 financial confirmation):
    CDI ×1.04 | Governance ×0.96 | Sporting ×1.00
  No resolution at 90 days: ONGOING_DISTRESS — maintain modifiers.

FTP PATH_2 INTERACTION:
  Supply mechanics (WIN burn, LOSS mint) are on-chain — unaffected by ownership.
  However, the demand response to a supply event is reduced during distress:
  WIN + burn during TAKEOVER_COLLAPSED:
    Apply ×0.92 to the demand premium that would normally follow.
  The mechanic fires. The market response is muted.
```

---

## New ownership honeymoon period

```
STANDARD HONEYMOON (90 days post-confirmation):
  CDI premium: ×1.12
  Governance premium: ×0.96 (restoring, not yet stable)
  Sporting premium: ×1.05

ENHANCED HONEYMOON (strategic acquisition profile):
  CDI premium: ×1.20
  Governance premium: ×0.97
  Sporting premium: ×1.10

REDUCED HONEYMOON (distressed sale profile):
  CDI premium: ×1.08
  Governance premium: ×0.92
  Sporting premium: ×1.02

HONEYMOON DELIVERY ASSESSMENT (90 days+):
  Promises delivered → ×1.08 sustained CDI (confirmed trajectory)
  Promises not delivered → ×0.92 CDI (credibility discount)
  The gap between honeymoon announcement and delivery is a strong CDI signal.
  Do not assume delivery — require Tier 1 confirmation.
```

---

## Distressed sale vs strategic acquisition

```
DISTRESSED SALE INDICATORS (any 2+ = classify as distressed):
  · Below-market valuation
  · Urgency signals in reporting (short timeline, forced sale language)
  · Existing debt or financial liability transfer required
  · Existing ownership facing legal, financial, or regulatory pressure
  · Single buyer — no competitive process

STRATEGIC ACQUISITION INDICATORS (any 2+ = classify as strategic):
  · At or above market valuation
  · Competitive bidding with multiple named parties
  · Acquirer has demonstrable sports investment track record
  · Public investment thesis stated (specific sporting ambitions)
  · Long-term commitment signals in announcement

DEFAULT: if classification uncertain, apply standard modifiers.
Do not guess — wait for Tier 1 source confirmation of deal terms.
```

---

## Ownership uncertainty and commercial pipeline

```
COMMERCIAL PIPELINE FREEZE SIGNAL:
  During STAGE 2, STAGE 3, and TAKEOVER_COLLAPSED:
  Major sponsorship negotiations typically pause.
  New commercial partnerships are unlikely to be announced.
  Existing partner renewal decisions are deferred.

  Apply: CDI pipeline freeze modifier ×0.94 on top of base modifier.
  This stacks with the stage modifier — do not use instead of it.

  Example: STAGE 3 (×0.88) + pipeline freeze (×0.94) = ×0.83 effective CDI.

COMMERCIAL PIPELINE UNFREEZE (T+14 after new ownership confirmation):
  Commercial activity resumes — pipeline modifier lifts.
  Apply base honeymoon CDI modifier without pipeline penalty.
```

---

## Fan token registry cross-reference

```
For clubs with active fan token partnerships, ownership changes affect
the partnership structure itself:

  If new ownership changes club's commercial priorities:
    Monitor for fan token partnership renewal or termination.
    Partnership termination: NOT_ACTIVE (legacy on-chain) status.
    See: fan-token/registry/complete-registry.md

  If collapsed takeover involves the fan token platform (Socios/Chiliz)
  as a stakeholder in the deal:
    Escalate to ecosystem-level signal.
    See: fan-token/ecosystem-health-intelligence.md

$SEVILLA as reference case:
  $SEVILLA is an active Chiliz Chain partner.
  Any ownership transition at Sevilla FC affects $SEVILLA demand signals
  through all three channels (commercial, governance, sporting).
  Apply this framework to $SEVILLA in any ownership transition scenario.
  Reference: fan-token/governance-takeover-framework.md for governance detail.
```

---

## Compatibility

**Governance takeover:**        `fan-token/governance-takeover-framework.md`
**Governance intelligence:**    `fan-token/governance-intelligence.md`
**Commercial intelligence:**    `market/commercial-partnership-intelligence.md`
**Financial sustainability:**   `core/financial-sustainability-intelligence.md`
**Registry:**                   `fan-token/registry/complete-registry.md`
**Ecosystem health:**           `fan-token/ecosystem-health-intelligence.md`

---

*SportMind v3.97.69 · MIT License · sportmind.dev*
*TAKEOVER_COLLAPSED: apply CDI ×0.82 | Governance ×0.80 | Sporting ×0.94 simultaneously.*
*Honeymoon promises not delivered at 90 days → ×0.92 CDI credibility discount.*
