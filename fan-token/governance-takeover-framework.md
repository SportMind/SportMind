---
name: governance-takeover-framework
description: >
  Enduring reasoning framework for how club ownership transitions, failed takeovers,
  and ownership uncertainty affect fan token governance stability, holder confidence,
  CDI signals, and FTP PATH_2 mechanics. Covers the complete ownership transition
  signal framework from initial announcement through resolution. Complements
  fan-token/governance-intelligence.md with the specific ownership-transition
  governance layer.
---

# Fan Token Governance — Ownership Transition Framework

**How club ownership transitions affect fan token governance and demand signals.**
Ownership uncertainty creates governance instability that compounds independently of sporting results.

---

## Ownership transition stages and signal weights

```
STAGE 1 — RUMOUR / UNCONFIRMED INTEREST:
  Source tier applies — Tier 5 rumour: ignore.
  Named bidder, Tier 1 source: apply ×0.95 CDI uncertainty modifier.
  Rationale: confirmed interest creates commercial uncertainty
    (sponsor negotiations pause, commercial pipeline freezes).

STAGE 2 — LOI / EXCLUSIVITY SIGNED:
  Enduring signal: a signed Letter of Intent is a confirmed commercial event.
  Apply: ×0.92 CDI governance stability modifier.
  Rationale: exclusivity period means no competing buyer can emerge —
    if the deal fails, the club has no immediate alternative.
  Governance: votes on commercial decisions should be treated with
    reduced confidence during exclusivity period.

STAGE 3 — DUE DILIGENCE / PROOF OF FUNDS PENDING:
  Proof of funds not yet confirmed: FUNDING_UNCERTAINTY_ACTIVE.
  Apply: ×0.88 governance stability modifier.
  This is distinct from LOI — the deal is not progressing
    until funds are verified.
  Fan token governance decisions during this stage:
    Do not treat positively — governance credibility is reduced.

STAGE 4A — TAKEOVER CONFIRMED:
  New ownership confirmed by official club and regulatory channels.
  Initial signal: HONEYMOON_PHASE_ACTIVE (see below).
  Governance stability: RESTORING — takes 3-6 months to establish.

STAGE 4B — TAKEOVER_COLLAPSED:
  Deal falls through — no new owner, existing ownership remains.
  Apply: ×0.82 CDI sustained (COMMERCIAL_DISTRESS_SIGNAL tier).
  Rationale: collapsed takeover means: club was for sale (signals
    financial or strategic weakness), exclusivity period wasted
    (no competing bids invited), commercial partners who paused
    decisions now face uncertainty again.
  Governance: votes called during or after a collapsed takeover
    carry reduced credibility until club demonstrates financial stability.
  Duration: ×0.82 sustained for minimum 90 days post-collapse.
  Resolution trigger: new ownership confirmed, or club demonstrates
    financial health through Tier 1 commercial signals.
```

---

## TAKEOVER_COLLAPSED — detailed signal framework

```
IMMEDIATE SIGNALS (T+0 to T+14 days post-collapse):
  CDI:                  ×0.82 sustained
  Governance stability: COMPROMISED — votes called in this window
                        have reduced holder participation expected
  Commercial partners:  apply COMMERCIAL_DISTRESS_SIGNAL framework
                        (see market/commercial-partnership-intelligence.md)
  Fan token demand:     ×0.88 immediate suppressor
  FTP PATH_2:           supply mechanics unaffected — WIN/LOSS/DRAW
                        still fire normally. Demand response to PATH_2
                        events is reduced by ×0.92 during distress period.

MEDIUM-TERM SIGNALS (T+14 to T+90 days):
  Resolution paths and their modifiers:

  PATH A — NEW BUYER EMERGES:
    New LOI signed: ×1.05 recovery signal (relief rally pattern)
    New deal confirmed: ×1.10 — club sold, uncertainty resolved
    Governance stability: RESTORING at ×0.95 (new owner not yet established)

  PATH B — EXISTING OWNERSHIP STABILISES:
    Club demonstrates financial health (new commercial deal, debt cleared):
    ×1.04 recovery signal — existing ownership with confirmed resources
    Governance stability: PARTIAL_RECOVERY at ×0.96

  PATH C — NO RESOLUTION:
    90+ days post-collapse with no resolution:
    Apply: ONGOING_DISTRESS — maintain ×0.82 CDI, reassess quarterly.
    Governance votes: treat all major decisions with ×0.75 confidence weight.

TAKEOVER COLLAPSE CAUSE — MODIFIER PROFILES BY CAUSE TYPE:

  LIQUIDITY_FAILURE (buyer unable to provide proof of funds):
    Most severe collapse cause — buyer was never genuinely funded.
    CDI:          ×0.78 sustained (worse than standard ×0.82)
    Governance:   ×0.75 credibility weight (worse than standard ×0.80)
    Rationale:    LIQUIDITY_FAILURE signals the deal was speculative from the outset.
      Commercial partners lose confidence in the club's ownership vetting process —
      the collapse was avoidable. Governance stakeholders lose confidence in
      the board's due diligence capability.
    Recovery:     requires next buyer to proactively provide proof of funds
      BEFORE exclusivity — otherwise market applies a repeat-risk discount.
    Repeat signal: second consecutive LIQUIDITY_FAILURE:
      CDI: ×0.70 | Governance: ×0.65 — systematic due diligence failure signal.

  DUE_DILIGENCE_FAILURE (buyer fails regulatory or legal checks):
    Standard TAKEOVER_COLLAPSED modifiers apply.
    CDI: ×0.82 | Governance: ×0.80
    Recovery: faster than LIQUIDITY_FAILURE — failure may reflect regulatory
      complexity rather than buyer weakness. Path to remedy often exists.

  REGULATORY_BLOCK (deal blocked by competition or financial authority):
    Lightest collapse cause — neither buyer nor club at fault.
    CDI: ×0.88 (lighter than standard) | Governance: ×0.85
    Rationale: regulatory block may be resolved by remedies or structures.
    Recovery signal is faster — regulatory resolution is a defined path forward.

  PRICE_DISAGREEMENT (valuation gap — seller and buyer cannot agree):
    Standard modifiers: CDI ×0.82 | Governance ×0.80
    Positive sub-signal: club was valued — not distressed.
    Apply: ×1.04 to next recovery signal when next buyer emerges
      (demonstrates club has real commercial value).

HOLDER BEHAVIOUR PATTERN:
  Takeover collapse typically triggers two waves:
  Wave 1 (T+0 to T+7): panic selling by sentiment-driven holders
  Wave 2 (T+7 to T+30): stabilisation as governance clarity emerges
  Do not apply wave pattern modifiers — document the framework only.
  Actual holder behaviour depends on specific circumstances.
```

---

## New ownership honeymoon period

```
HONEYMOON_PHASE_ACTIVE: first 90 days of confirmed new ownership.
  New ownership honeymoon modifier: ×1.12 CDI premium.
  Rationale: new owners typically announce investment plans,
    commercial ambitions, and governance reforms in the first 90 days.
    These are aspirational signals — not yet confirmed delivery.

HONEYMOON SIGNAL QUALITY:
  Investment commitment + timeline confirmed: ×1.15 — upgrade from honeymoon
  Investment commitment unconfirmed: ×1.08 — reduced premium
  Named players or commercial deals immediately announced: ×1.20

POST-HONEYMOON ASSESSMENT (90+ days):
  Review whether honeymoon signals have been delivered.
  Delivered investment: ×1.08 sustained (confirmed trajectory)
  Undelivered promises: ×0.92 — credibility discount applied
  The gap between honeymoon promises and delivery is a strong CDI signal.
```

---

## Distressed sale vs strategic acquisition

```
DISTRESSED SALE PROFILE:
  Indicators: urgency, below-market valuation, debt resolution required,
    existing ownership seeking exit under financial pressure.
  Signal weight: new owner inherits existing financial structure.
  Honeymoon premium: ×1.08 (reduced from standard ×1.12).
  Risk: new owner may face same financial pressures.
  Governance stability post-completion: ×0.92 for first 90 days.

STRATEGIC ACQUISITION PROFILE:
  Indicators: premium valuation, competitive bidding process,
    acquirer has track record in sports investment.
  Signal weight: acquirer bringing resources, not just ownership transfer.
  Honeymoon premium: ×1.20 (enhanced — strategic investor signal).
  Governance stability post-completion: ×0.96 for first 90 days.

HOW TO CLASSIFY:
  Cannot classify without Tier 1 source confirmation of deal terms.
  Default: apply standard honeymoon (×1.12) until classification possible.
```

---

## Fan token governance vote validity during transitions

```
GOVERNANCE VOTES DURING OWNERSHIP UNCERTAINTY:
  Any major governance vote called during STAGE 2, 3, or TAKEOVER_COLLAPSED:
  Apply: ×0.80 governance credibility weight.
  Rationale: holder participation drops during uncertainty,
    and outcomes may be reversed or modified by incoming ownership.

  Minor utility votes (kit designs, matchday experiences):
  These are less affected by ownership transitions.
  Apply: ×0.92 credibility weight.

  Supply modification votes (burns, mints, treasury actions):
  During ownership uncertainty: apply ×0.70 confidence weight.
  These are material on-chain decisions — uncertainty about
  who controls the club governance framework is most critical here.

VOTE RESULT INTERPRETATION:
  If a supply modification vote passes during TAKEOVER_COLLAPSED:
  Treat the outcome with caution — the governance context is compromised.
  Do not apply full supply modifier until governance stability confirmed.
```

---

## Compatibility

**Governance intelligence:**    `fan-token/governance-intelligence.md`
**Commercial intelligence:**    `market/commercial-partnership-intelligence.md`
**Ownership framework:**        `market/club-ownership-intelligence.md`
**Financial sustainability:**   `core/financial-sustainability-intelligence.md`
**CDI framework:**              `market/market-intelligence.md`

---

*SportMind v3.97.69 · MIT License · sportmind.dev*
*TAKEOVER_COLLAPSED → ×0.82 CDI sustained for minimum 90 days.*
*Governance votes during ownership uncertainty: ×0.80 credibility weight.*
