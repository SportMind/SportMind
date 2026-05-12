---
name: financial-sustainability-intelligence
description: >
  Enduring reasoning framework for financial constraints and sustainability as fan
  token risk and demand modifiers. Covers UEFA FFP, Premier League PSR, ownership
  signals, relegation financial risk, and promotion opportunity. Not current financial
  figures — how to reason when financial context is confirmed.
---

# Financial Sustainability Intelligence

**How to reason about financial constraints and sustainability as signal modifiers.**
Not current financial figures — the enduring framework for applying financial context.

> Library Rule: no current balance sheets, specific debt figures, or named
> individual transactions. Framework teaches how to reason when confirmed
> financial facts arrive.

---

## Financial Fair Play (FFP) framework

```
UEFA FFP AND EQUIVALENT REGULATIONS — SIGNAL FRAMEWORK:

  WHY FINANCIAL REGULATIONS AFFECT SIGNAL QUALITY:
    Clubs under financial constraint cannot strengthen squads as freely.
    This reduces squad quality over time, increasing individual absence impact
    and reducing depth modifiers. Financial health is therefore a structural
    signal modifier on squad quality.

  CLUB UNDER FFP INVESTIGATION (not yet found in breach):
    Apply: ffp_investigation_modifier = ×0.94 on squad building capacity
    Mechanism: constrained transfer budget; uncertain future spend;
      potential sale of assets to comply
    Duration: applies while investigation is open; remove on resolution
    Match signal interaction: reduced ability to strengthen = individual
      player absence modifiers apply at FULL WEIGHT (no depth discount)
    
  CLUB WITH CONFIRMED FFP BREACH:
    Apply: ffp_breach_modifier = ×0.88 on squad building capacity
    Additional risks that must be flagged:
      Point deduction possibility (applies in current or future season)
      Transfer embargo possibility (cannot buy players)
      Fine (reduces available investment)
    When point deduction is CONFIRMED:
      Apply: points_deduction_competitive_modifier = adjust league position
        signal based on actual deducted points standing
      
  CLUB WITH CLEAN FFP RECORD AND STRONG OWNER BACKING:
    Apply: ffp_premium = ×1.05 squad building capacity premium
    Mechanism: financial flexibility to strengthen in any window;
      no regulatory overhang on recruitment decisions
    Confirm via: publicly available UEFA financial fair play assessments
```

---

## Premier League PSR framework

```
PREMIER LEAGUE PROFIT AND SUSTAINABILITY RULES (PSR):

  WHY PSR IS DISTINCT FROM UEFA FFP:
    PSR applies specifically to Premier League clubs and uses different
    calculations (stadium infrastructure and academy costs treated differently).
    A club can comply with UEFA FFP but breach PSR — the two are independent.
    
  PSR BREACH RISK ASSESSMENT:
    How to reason about clubs approaching PSR thresholds:
    
    APPROACHING THRESHOLD (estimated within £10M of limit):
      Apply: psr_risk_flag = true
      Signal: forced sales in upcoming windows likely to create compliance headroom
      Demand impact: uncertainty; potential departure of key assets
      
    CONFIRMED PSR BREACH (points deduction issued):
      Apply: psr_breach_competitive_modifier
        → Adjust league position based on actual standing with points deducted
        → This changes relegation/title race probability calculations directly
      Apply: forced_sale_demand_modifier = ×0.88 (see below)
      
  FORCED SALE SIGNAL (asset sales driven by financial distress):
    Forced sale of first-team players to meet financial compliance:
    Apply: forced_sale_modifier = ×0.88 demand and squad quality modifier
    Mechanism: forced sales reduce squad quality and signal financial fragility;
      holders and potential holders interpret this as negative stability signal
      
  ACADEMY PLAYER SALE (for PSR compliance):
    Selling academy graduates for compliance is less negative than first-team sales.
    Apply: academy_sale_modifier = ×0.95 (smaller penalty — squad quality less impacted;
      signal is that financial management is strained but core squad preserved)
    
  AGENT RULE:
    For any Premier League club: check PSR status at start of each season.
    PSR calculations run on a rolling 3-year basis — check trailing 3 seasons.
    Source: Premier League official statements; club financial filings.
```

---

## Ownership and investment signals

```
NEW HIGH-NET-WORTH OWNERSHIP:

  DEFINITION:
    New ownership by an individual or entity with documented significant wealth
    and stated intention to invest in the club.
    
  MODIFIER:
    Demand spike: +15% (×1.15) over 4-6 weeks from confirmed takeover
    Mechanism: expectation of squad investment; media narrative boost;
      new holder interest attracted by the story
    After 4-6 weeks: demand settles based on EVIDENCE of investment
      If investment confirmed (signings, infrastructure): ×1.05 sustained
      If investment is slower than expected: no sustained premium
      
  DISTINGUISH FROM UNCERTAINTY TAKEOVER:
    Confirmed completed takeover: apply ×1.15 above
    Bid in progress / uncertain takeover: apply volatility signal (see below)

OWNERSHIP UNCERTAINTY / TAKEOVER BID IN PROGRESS:

  DEFINITION:
    A takeover bid is publicly reported but not yet completed or confirmed.
    
  SIGNAL:
    Not a directional signal — outcome uncertain (positive or negative).
    Apply: ownership_uncertainty_volatility = ×1.20 to demand VARIANCE
      (prediction interval widens — demand could spike or drop on resolution)
    Direction: HOLD directional signal until outcome confirmed
    
  RESOLUTION:
    Bid succeeds: apply new ownership modifier as above
    Bid fails: remove volatility modifier; return to pre-bid baseline with
      small negative overhang (×0.97, 2-week duration) — disappointment signal

STATE-BACKED OWNERSHIP:

  DEFINITION:
    Club owned by or with significant financial backing from a sovereign
    wealth fund, state investment vehicle, or equivalent.
    
  MODIFIER:
    state_backed_stability_modifier = ×1.05 sustained demand modifier
    Mechanism: holder confidence in long-term club stability;
      lower perceived risk of financial distress;
      global brand investment expected
    Duration: sustained as long as ownership structure is confirmed
    
  REGULATORY NOTE:
    State-backed ownership creates additional regulatory scrutiny in some
    jurisdictions (UEFA financial investigations; "state aid" concerns).
    If regulatory challenge to state-backed ownership is confirmed:
      Apply: regulatory_challenge_modifier = ×0.96 (uncertainty period)
      Remove when resolved.
```

---

## Relegation financial risk

```
RELEGATION FINANCIAL RISK — COMPOUND SIGNAL:

  Clubs in relegation battles face compounding financial risk alongside
  competitive risk. For fan tokens, this creates a compound negative signal.
  
  PARACHUTE PAYMENTS:
    English Premier League provides parachute payments to relegated clubs
    for 2 seasons after relegation. This softens but does not eliminate
    the revenue shock.
    Signal: parachute payments reduce post-relegation financial catastrophe
      but do not prevent it. The fan token demand signal accounts for this.

  RELEGATION BATTLE DEMAND MODIFIER TABLE:
    
    Club in bottom three (in relegation zone) with 6+ matches remaining:
      relegation_zone_modifier = ×0.82 sustained (see tottenham-hotspur-spurs.md)
      
    Club in bottom three with ≤5 matches remaining:
      late_season_crisis_modifier = ×0.80 (higher urgency; outcome clearer)
      
    Club one place above relegation zone with 3+ matches remaining:
      Apply: relegation_concern_modifier = ×0.91

POST-RELEGATION DEMAND TRAJECTORY:

  MONTH 1 POST-RELEGATION:
    Demand drop: −25 to −40% from pre-relegation baseline
    This is structural — the competitive tier has changed
    
  MONTHS 2-6 (settling):
    Demand stabilises at 60-70% of pre-relegation baseline
    IF the club begins a credible promotion challenge: demand recovers
    IF the club struggles in the lower division: demand compresses further
    
  PROMOTION CHALLENGE FROM LOWER DIVISION:
    Club in top 3 of division below (credible automatic promotion candidate):
      Apply: promotion_challenge_modifier = ×1.05 to the depressed post-relegation baseline
      Each round of play-off confirmation: ×1.03 additional
      
  PROMOTION CONFIRMED:
    Apply: promotion_confirmation_modifier = ×1.20 immediate spike (48-72h)
    New settled baseline: ×1.10 above pre-promotion (but below original top-flight baseline)
```

---

## Promotion financial opportunity

```
NEWLY PROMOTED CLUBS:

  FIRST PROMOTION TO TOP FLIGHT (or return after long absence 5+ seasons):
    Promotion event: ×1.25 demand spike at confirmation
    First season in top flight: ×1.10 sustained demand modifier
    Mechanism: new broadcast revenue, new sponsorship opportunities,
      new global exposure, first-time fan token holder acquisition opportunity
      
  RETURN AFTER SHORT ABSENCE (2-4 seasons):
    Promotion event: ×1.15 demand spike (smaller — less novel)
    First season back: ×1.05 sustained
    
  IF FAN TOKEN LAUNCHES AT PROMOTION:
    Apply the emerging-sports-pipeline.md new launch framework.
    The promotion narrative amplifies the launch premium:
      Tier A equivalent promotion launch: +80-100% above pre-launch baseline
      (higher than standard +60-80% for same club not in promotion context)
```

---

## Compatibility

**Relegation modifier:**    `athlete/football/tottenham-hotspur-spurs.md`
**Transfer window:**        `core/transfer-window-intelligence.md`
**$AFC PATH_2 financial:**  `athlete/football/arsenal-afc.md`
**Seasonal demand:**        `core/seasonal-intelligence.md`
**Emerging pipeline:**      `fan-token/emerging-sports-pipeline.md`

---

*SportMind v3.97.37 · MIT License · sportmind.dev*
*Financial constraints reduce squad depth discounts — absence modifiers apply at full weight*
