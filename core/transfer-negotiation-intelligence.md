---
name: transfer-negotiation-intelligence
description: >
  Intelligence framework for the transfer negotiation process — the
  phases between rumour and announcement that generate commercial signals
  the library previously missed. Covers four negotiation types: player
  contract renewal, incoming transfer, outgoing transfer, and commercial
  partner (sponsorship/naming rights). Each type has phase-specific
  signals, modifier implications, and fan token commercial consequences.
  Includes a Relocation Adjustment Factor (RAF) for moves with significant
  lifestyle disruption — cross-league, cross-continent, and culturally
  distinct destinations. Cross-sport: football is primary (most negotiation
  signal visibility); NBA free agency, cricket IPL/BBL auction, F1 driver
  market, and MMA contract cycles all modelled. Load when: a transfer
  negotiation is in progress, a contract renewal is reported, a commercial
  partnership announcement is expected, or a destination involves meaningful
  relocation disruption.
---

# Transfer Negotiation Intelligence — SportMind

**The process between rumour and announcement is not noise.
Every phase generates a signal.**

The library already models the outcome of transfers (star-departure-intelligence,
transfer-signal, athlete-financial-intelligence). This skill models the
*process* — the phases of negotiation that precede the outcome and produce
distinct commercial signals at each stage.

---

## Why negotiation intelligence belongs in SportMind

```
WHAT THE LIBRARY PREVIOUSLY CAPTURED:
  ✓ Transfer confirmed → APS, destination club HAS impact
  ✓ Contract year → motivation modifier ×1.12
  ✓ Release clause → financial portability signal
  ✓ Departure confirmed → AELS void, LTUI impact

WHAT THIS SKILL ADDS:
  + Phase detection: which stage is the negotiation at right now?
  + Phase-specific modifier: different phases = different signal weight
  + Pre-announcement intelligence: the signal before the confirmation
  + Commercial partner negotiation: sponsorship as a fan token signal
  + Relocation adjustment: performance degradation from lifestyle disruption
  + Negotiation failure: what happens when a deal collapses
```

---

## Negotiation Type 1 — Player contract renewal

```
WHAT IT IS:
  A club negotiating with their own player to extend their contract.
  The most commercially sensitive ongoing negotiation type — visible to
  fans, monitored by rivals, and directly affects LTUI and APS.

PHASES AND SIGNALS:

  PHASE 1: NEGOTIATION OPENS (contract 18–24 months from expiry)
  Status: Club confirms talks are ongoing
  Signal: Positive stability signal. LTUI trajectory: improving.
  Modifier: +0.05 on HAS (holder confidence period)
  Source check: Official club statement OR Tier 1 journalist confirmation
  Fan token implication: Mild positive. Not yet an ENTER signal alone.

  PHASE 2: TALKS PROGRESSING (12–18 months from expiry)
  Status: Progress reported, no agreement yet
  Signal: Background positive. Watch for stalling signals (agent noise,
  rival club interest reported alongside renewal talks)
  Modifier: Neutral — hold current signal
  Fan token implication: Monitor. No action yet.

  PHASE 3: STALLING (12 months from expiry, talks reported as difficult)
  Status: Disagreement on terms publicly acknowledged
  Signal: LTUI uncertainty begins. APS portability rising.
  Modifier: −0.08 on LTUI confidence score
  Fan token implication: WAIT signal if stalling for ATM player (see ATM tiers)
  Alert: If ATM player + stalling + rival interest reported → LTUI_RISK flag

  PHASE 4: PRE-CONTRACT ELIGIBLE (6 months from expiry)
  Status: Player can sign pre-contract with another club
  Signal: SIGNIFICANT negative if no extension signed by this point.
  Modifier: −0.15 LTUI; APS calculation now fully activated
  Fan token implication: Approaching ABSTAIN on LTUI dimension
  Source: Transfermarkt contract expiry date (verify)

  PHASE 5: EXTENSION CONFIRMED
  Status: New contract signed, announced officially
  Signal: STRONG positive. CDI-equivalent commercial event.
  Modifier: +0.20 LTUI; reset uncertainty period; APS stability signal
  Fan token implication: ENTER signal amplifier — pair with macro check
  Note: Announcement timing matters. Pre-season = maximum uplift.
  During a run of wins = double positive. After a loss = reduced effect.

  PHASE 6: DEPARTURE CONFIRMED (talks failed, player leaving)
  → Load core/star-departure-intelligence.md for full void model
  → This file has provided pre-departure intelligence; that file handles aftermath

AGENT RULE:
  Never apply Phase 5 modifier before official club confirmation.
  "Close to signing" (journalist language) = Phase 3–4, not Phase 5.
  The signal does not fully apply until the pen is on paper.
```

---

## Negotiation Type 2 — Incoming transfer

```
WHAT IT IS:
  A buying club negotiating to acquire a player from a selling club.
  Creates commercial signals for both clubs throughout the process.

PHASES AND SIGNALS:

  PHASE 1: INITIAL INTEREST (rumour, unconfirmed)
  Status: Journalist reports interest, no bid submitted
  Signal: Rumour signal only. Apply Rumour Confidence Score from
  transfer-signal skill before weighting any modifier.
  Modifier: No change until Tier 1 source confirms bid submitted
  Fan token implication: Token spike is likely rumour-driven. Do not chase.

  PHASE 2: BID SUBMITTED (confirmed)
  Status: Formal offer made to selling club
  Signal: FIRST CONCRETE SIGNAL. Now apply commercial modifiers.
  Buying club: +0.08 holder sentiment (ambition signal)
  Selling club: depends on ATM tier of departing player
  Source required: Tier 1 journalist ("bid submitted") OR official
  club statement ("received an offer which has been turned down")

  PHASE 3: BID REJECTED / NEGOTIATIONS ONGOING
  Status: Seller has rejected initial offer, talks continuing
  Signal: Price discovery phase. The gap between bid and valuation
  is now the signal — not the outcome.
  Modifier: Hold. Neither positive nor negative until new information.
  Watch for: "Bid significantly short of valuation" (large gap = lower
  completion probability); "Clubs are confident" (small gap = higher)

  PHASE 4: AGREEMENT IN PRINCIPLE (fee agreed)
  Status: Fee agreed between clubs, personal terms not yet agreed
  Signal: STRONG completion probability. 80–85% deals complete from here.
  Buying club: +0.12 on HAS anticipation modifier
  Source: "Fee agreed" from Tier 1 journalist or club statement
  Note: Personal terms failure can still kill the deal at this stage
  (see Phase 4b below)

  PHASE 4b: PERSONAL TERMS COLLAPSE (fee agreed but player refuses)
  Status: Club deal done but player terms cannot be agreed
  Signal: NEGATIVE surprise. Buying club -0.10 HAS (expectation gap)
  This is rare (~10% of fee-agreed deals) but commercially significant.

  PHASE 5: MEDICAL / OFFICIAL CONFIRMATION
  Status: Player undergoing medical + contract signed
  Signal: NEAR-CERTAIN completion. 97%+ complete from here.
  Modifier: Full APS destination uplift now applicable
  Fan token: ENTER signal — applies APS, LQI, commercial tier uplift

  PHASE 6: ANNOUNCEMENT
  Status: Official club announcement
  Signal: CDI event (Category 2 commercial signal). Apply full APS model.
  
FAILED DEAL SIGNAL (Phase 2–4 collapse):
  Deal collapses after bid or fee-agreed stage:
  Buying club: −0.10 HAS (disappointment window, 1–2 weeks)
  The more public the deal, the larger the disappointment signal.
  Recovery: 3–4 weeks unless alternative target immediately announced.
  Selling club: APS portability remains high if player wanted to leave.
```

---

## Negotiation Type 3 — Outgoing transfer (source club perspective)

```
For full departure impact, load core/star-departure-intelligence.md.
This section covers the negotiation-specific signals only.

KEY SIGNAL: Is the player pushing for the move, or is the club selling?

CLUB INITIATING SALE:
  Signal: Financial pressure or squad strategy signal.
  If driven by FFP/PSR compliance: negative perception signal
  If driven by tactical rotation/age: neutral to mild positive
  Fan token: monitor CDI — forced sale of fan favourite = negative CDI

PLAYER REQUESTING TRANSFER:
  Phase: Request submitted (confirmed by club or Tier 1 source)
  Signal: Dressing room cohesion risk (see core/squad-cohesion-intelligence.md)
  SCI component: leadership_quality and recent_disruption_inverse both decline
  Fan token: WAIT until clarity — could be resolved or could escalate

COMPETING BIDS (auction scenario):
  Multiple clubs bidding for one player = fee maximisation signal.
  Source club: financial upside signal (+0.06 HAS if selling ATM player well)
  The auction outcome (fee received relative to Transfermarkt valuation) is a
  club quality signal: receiving 120%+ of market value = strong negotiation.
  
SELL-TO-RIVAL RISK:
  If departing player is joining a direct rival:
  Load core/star-departure-intelligence.md — Type 1 or 4 departure
  Additional commercial signal: fan sentiment is amplified negative
  Apply: rivalry_discount on token holder sentiment (1–4 weeks)
```

---

## Negotiation Type 4 — Commercial partner negotiations

```
WHAT IT IS:
  Kit deal, stadium naming rights, main shirt sponsor, sleeve partner,
  official partner category. These are the largest commercial contracts
  in sport and directly affect the fan token commercial tier.

WHY IT MATTERS FOR FAN TOKENS:
  A new major sponsorship announcement is a CDI-equivalent event.
  The negotiation before it is an intelligence opportunity — the fan
  token's commercial tier is about to change, but the market does not
  yet know.

SIGNAL PHASES:

  PHASE 1: CONTRACT EXPIRY APPROACHING (12–18 months)
  Existing deal expiring. Three outcomes: renewal, upgrade, or replacement.
  Signal: Low-level uncertainty. Current commercial tier stable.
  Watch for: Sponsor reduces activation (events, social content) —
  early signal of non-renewal.

  PHASE 2: MARKET PROCESS BEGINS (club confirms exploring options)
  Signal: Positive if club is upmarket. Ambition signal.
  Fan token: Mild positive — club demonstrating commercial ambition.

  PHASE 3: EXCLUSIVITY / HEADS OF TERMS
  Status: One partner in exclusive negotiations
  Signal: STRONG positive. 90%+ of exclusivity talks result in signed deals.
  Fan token: ENTER signal amplifier — commercial tier upgrade imminent.
  Source: Financial press (SportsPro Media, Sportico, Bloomberg Sports)

  PHASE 4: ANNOUNCEMENT
  Status: Official new partnership signed
  Signal: CDI EVENT. Commercial tier upgrade.
  Fan token modifier: See fan-token/fan-token-lifecycle/ commercial tier bands.
  Upgrade from Tier 3 → Tier 2: significant LTUI uplift
  Upgrade from Tier 2 → Tier 1: maximum CDI event

COMMERCIAL PARTNER LOSS:
  Sponsor terminates deal mid-contract or fails to renew:
  Commercial tier downgrade signal.
  If reason is club-related (conduct, poor results): compound negative
  If reason is sponsor-internal (cost-cutting): lower negative weight
  Fan token: flag CDI_RISK; apply LTUI uncertainty period (4–8 weeks)
```

---

## Relocation Adjustment Factor (RAF)

```
WHAT IT IS:
  A performance modifier applied when a player transfers to a destination
  that involves significant lifestyle, cultural, or geographical disruption.
  Standard transfer models assume the player performs at their statistical
  baseline immediately. Evidence consistently shows a 1–2 season adjustment
  period for culturally disruptive moves.

EVIDENCE BASE:
  Cross-continent moves (Europe → Saudi Arabia, MLS, Japan, Australia):
  Documented 15–25% performance reduction in Year 1 vs European baseline.
  Most return to 85–95% of baseline in Year 2 once adjusted.
  Cross-league moves within Europe (Bundesliga → Premier League):
  ~8–12% adjustment period for 6–12 months (pace, physicality differential).
  Domestic moves: RAF = 0 (no adjustment needed).

RAF CALCULATION:
  RAF = lifestyle_disruption × league_gap × age_factor

  LIFESTYLE DISRUPTION (how different is the destination?):
    Same city / local derby: 0.00
    Same country, different city: 0.02
    European cross-border: 0.05
    Middle East (Saudi, UAE, Qatar): 0.18
    MLS (USA): 0.14
    Asia (Japan, Australia, India): 0.16
    Very high disruption (multiple factors): cap at 0.22

  LEAGUE GAP (quality differential):
    Same league: 0.00
    Adjacent tier (same country): 0.04
    Cross-league, similar quality: 0.06
    Cross-league, significant quality change: 0.10

  AGE FACTOR (amplifier on total RAF):
    Player aged < 24 (adaptable): × 0.80
    Player aged 24–29 (prime): × 1.00
    Player aged 30–33 (settled): × 1.20
    Player aged 34+ (late career): × 1.40

  COMBINED:
    RAF_adjusted = (lifestyle_disruption + league_gap) × age_factor
    Performance modifier Year 1: × (1.00 − RAF_adjusted)
    Performance modifier Year 2: × (1.00 − RAF_adjusted × 0.35)
    Performance modifier Year 3+: × 1.00 (fully adjusted)

EXAMPLE — Bukayo Saka (26) Arsenal to Saudi Arabia:
  lifestyle_disruption = 0.18 (Middle East)
  league_gap = 0.10 (significant quality change)
  age_factor = 1.00 (prime)
  RAF = (0.18 + 0.10) × 1.00 = 0.28 → cap at 0.22
  Year 1 modifier: × 0.78
  Year 2 modifier: × 0.92
  Year 3+: × 1.00

FTP SUPPLY CONNECTION:
  Year 1 relocation adjustment → lower effective LQI at destination →
  lower win probability contribution → slower PATH_2 supply reduction.
  Apply: RAF modifier to win_probability calculation in FTP PATH_2 model.

CROSS-SPORT APPLICATION:

  NBA FREE AGENCY:
  Cross-conference moves involve no meaningful relocation disruption
  (all NBA cities are broadly similar lifestyle environments).
  Exception: International player moving from Europe to NBA — Year 1 adjustment
  lifestyle_disruption = 0.10, age_factor applies.

  CRICKET (IPL / BBL / T20 GLOBAL):
  Short-format tournaments (6–10 weeks): RAF does not apply
  (too short for adjustment to matter; players are effectively visiting).
  Multi-year franchise deals in new leagues: apply full RAF model.

  FORMULA 1:
  Driver changes teams but not country of residence typically.
  RAF = 0 for team changes unless combined with complete lifestyle relocation.
  Exception: New driver from junior formula entering F1 — team culture
  adjustment applies a modified RAF concept (0.05–0.08 Year 1).

  MMA:
  No relocation disruption from fight camp perspective (fighters maintain
  home base). Training camp location matters more than residence.
  Application: Camp disruption from training relocation → see camp signals
  in athlete/mma/athlete-intel-mma.md.
```

---

## Negotiation failure — what happens when deals collapse

```
COLLAPSE CATEGORIES:

  FEE DISAGREEMENT (clubs cannot agree price):
  Buying club: −0.06 HAS (failed ambition signal), 2–3 week window
  Selling club: neutral if player retained; positive if fee demand justified
  Player: motivation signal — player who wanted to leave + deal collapsed
  = motivation risk (core/athlete-motivation-intelligence.md — reduced flag)

  PERSONAL TERMS FAILURE (player rejects the move):
  Rare. Signals: player's preferred destination was elsewhere, agent using
  club as leverage, or significant lifestyle concern about destination.
  Apply RAF assessment retroactively — the collapse may be RAF-driven.

  MEDICAL FAILURE:
  Significant negative signal. Reveals undisclosed injury or physical concern.
  Apply: injury_warning flag + reduced athlete modifier (0.85–0.92 range)
  Duration: 4–8 weeks minimum; may persist if chronic issue revealed.
  Fan token: significant negative CDI event if ATM player fails medical.

  REGULATORY FAILURE (work permit, salary cap, FFP breach):
  Institutional signal. Not player-specific. Club-specific concern.
  Financial regulatory failure: apply financial_risk flag to club token.
```

---

## Integration with SportMind patterns

```
PATTERN 4 (Transfer Window Monitor):
  This skill provides the phase detection layer Pattern 4 was missing.
  Load alongside fan-token/transfer-signal/ for full transfer intelligence.

PATTERN 10 (Scouting Agent):
  RAF modifier feeds directly into CVS calculation for cross-league targets.
  A player with EXCELLENT CVS score but high RAF destination = adjust FAS.

PROMPT 22 (Pre-match build-up):
  New arrival in first few matches: apply RAF Year 1 modifier to LQI.
  Reference in plain_english summary: "Still adapting to the league."

PATTERN 2 (Pre-Match Chain):
  Phase 4 commercial partner announcement (CDI event) → check within
  T-72h window — could amplify social signal before match.
```

---

*SportMind v3.59 · MIT License · sportmind.dev*
*See also: core/star-departure-intelligence.md · core/athlete-financial-intelligence.md*
*core/athlete-motivation-intelligence.md · core/squad-cohesion-intelligence.md*
*fan-token/transfer-signal/ · fan-token/fan-token-lifecycle/*
