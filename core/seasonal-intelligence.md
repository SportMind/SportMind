---
name: seasonal-intelligence
description: >
  Enduring seasonal and cyclical pattern intelligence for sports and fan token
  demand. Covers annual demand cycles, weekly patterns, competition calendar
  signals, and crypto market cycle overlay. All cycles repeat reliably —
  permanently true reasoning frameworks.
---

# Seasonal and Cyclical Pattern Intelligence

**Predictable cycles that repeat every year. Use to calibrate signal timing.**

> Load alongside: `macro/macro-crypto-market-cycles.md` for crypto cycle depth.
> This file adds the sports calendar layer and weekly demand patterns.

---

## Annual fan token demand cycle

```
ANNUAL CYCLE — EUROPEAN FOOTBALL FAN TOKENS (primary market):

  The annual demand cycle is predictable and repeatable. Signal weighting
  should account for the cyclical context — a signal in the dead period
  carries less demand weight than the same signal in the summer window.

  ┌─────────────────────────────────────────────────────────────────────────────
  │ PERIOD             │ MONTHS     │ DEMAND MODIFIER  │ PRIMARY DRIVER
  ├─────────────────────────────────────────────────────────────────────────────
  │ Summer window      │ Jun-Aug    │ ×1.20 — PEAK     │ Transfers, squad builds
  │ Season start       │ Sep        │ ×1.10            │ New season anticipation
  │ Regular season     │ Oct-Jan    │ ×1.00 (baseline) │ Match results
  │ Winter window      │ Jan        │ ×1.10            │ Transfer + AFCON compound
  │ End of season      │ Apr-May    │ ×1.10-1.15       │ Title/relegation narrative
  │ UCL Final period   │ May        │ See tournament-macro.md (highest event)
  │ Dead period        │ Jun-Jul    │ ×0.85 — MIN      │ Off-season; no fixtures
  └─────────────────────────────────────────────────────────────────────────────

  SUMMER WINDOW (June–August) — HIGHEST VOLATILITY:
    Transfer activity, squad announcements, pre-season form all compound.
    Multiple tokens affected simultaneously — cross-correlation elevated.
    Apply: summer_window_volatility_flag during this period.
    Signals in this period: amplified by ×1.20 but less reliable (uncertainty).
    
  WINTER WINDOW (January) — SECONDARY VOLATILITY SPIKE:
    AFCON disruption compounds with transfer activity (see sport-domain-afcon.md).
    Apply: winter_window_modifier = ×1.10 baseline.
    
  END OF SEASON (April–May) — NARRATIVE-DRIVEN DEMAND:
    Clubs in title race: demand amplifier ×1.15 (sustained until outcome)
    Clubs in relegation battle: ×0.88 sustained demand discount
      (uncertainty + fear of relegation cascade; see tottenham-hotspur-spurs.md)
    European qualification race: ×1.08 for clubs within 3 points of qualifying
    These apply to all clubs simultaneously — portfolio correlation elevated.
    
  DEAD PERIOD (June–July off-season, pre-summer-window opening):
    Minimum demand baseline for most European club tokens.
    Apply: ×0.85 to all standard demand signals in this window.
    No fixtures → no match signals → no PATH_2 events → demand floor.
    
    EXCEPTION — NATIONAL TOKENS IN WORLD CUP / EUROS YEARS:
      National team tokens INVERT this pattern during tournament years.
      When European or World Cup tournament is live (June–July), national
      token proxies (club tokens with national association) see elevated demand.
      See: sport-domain-euros.md and sport-domain-copa-america.md.
```

---

## Weekly demand patterns

```
INTRA-WEEK DEMAND PATTERN:

  MATCH DAY:
    Day of match: demand_premium = ×1.08 (pre-match liquidity movement,
      holder engagement, PATH_2 pre-liquidation window activity)
    
  POST-MATCH:
    Day after WIN:
      win_demand_premium = ×1.05 (sustained; decays over 48h)
      Note: win sentiment decays faster than loss sentiment (see social-sentiment-intelligence.md)
    Day after LOSS:
      loss_demand_decay begins immediately
      ×0.92 in first 24h; normalises over 48-96h depending on severity
      
  MID-WEEK (non-match days):
    No systematic demand pattern absent a specific event.
    Demand drifts toward the weekly baseline unless a news event intervenes.
    
  FTP PATH_2 SPECIFIC — PRE-MATCH LIQUIDATION WINDOW (T-12h to T-2h):
    For $AFC and any future PATH_2 tokens:
      Pre-liquidation window creates structured demand movement.
      See: fan-token/ftp-path2.md for the full pre-liquidation framework.
      This is the most reliable intra-week signal for PATH_2 tokens.
      
  AGENT RULE:
    For demand signals, always note the match day context.
    A governance vote on a match day has amplified demand signal (two signals compound).
    A transfer announcement in the dead period has muted signal (×0.85 base).
```

---

## Competition calendar signals

```
FIXTURE CONGESTION — SQUAD QUALITY MODIFIER:

  DEFINITION: Three or more competitive matches in seven days.
  
  CONGESTION MODIFIER:
    Third match in congested window: apply ×0.94 to squad quality modifier
    Mechanism: accumulated fatigue, rotation of key players, recovery incomplete
    
  WHICH MATCHES ARE AFFECTED:
    Apply the modifier to the third (and beyond) match in the congested window.
    First two matches: standard modifiers.
    Third match: ×0.94 applied on top of all other modifiers.
    
  ROTATION DISCOUNT:
    If the manager has historically rotated heavily in cups/less important matches:
      Apply ×0.50 discount to the congestion modifier (×0.97 effective rather than ×0.94)
      Reason: rotation prevents individual fatigue; key players are fresh

INTERNATIONAL BREAK — REASSEMBLY SIGNAL:

  FIRST MATCH AFTER AN INTERNATIONAL BREAK:
    Apply: international_break_reassembly_modifier = ×0.97
    Mechanism: squad reassembles with different chemistry than pre-break;
      training time is compressed; players return from different time zones
      and distances; some return with international fatigue.
    Duration: first match only. Remove for second match post-break.
    
  LONG-HAUL INTERNATIONAL TRAVEL COMPOUND:
    If key players returned from intercontinental international duty
    (more than 8 hours travel): see injury-reasoning-framework.md for
    individual long-haul return modifier (×0.97 per player affected).
    Apply to the international break modifier multiplicatively.

CUP EXIT TIMING — LEAGUE FOCUS SIGNAL:

  EARLY CUP EXIT (R1 or R2 in domestic cups):
    Frees squad and training focus for the league.
    Apply: early_cup_exit_modifier = ×1.03 to league performance signals
    Duration: remainder of the season (structural, not temporary)
    Remove: when the club re-enters cup competition next season
    
  DEEP CUP RUN (reaching semi-final or final):
    Compound effect: fixture congestion increases (see above) but
    squad morale and motivation also increase.
    Net signal: the two effects partially offset.
    Congestion modifier (×0.94) + morale premium (×1.03):
      Net: ×0.97 effective modifier during congested deep-run periods.
      
  UCL VS DOMESTIC CUP TRADE-OFF:
    Some clubs implicitly prioritise UCL over domestic cups.
    When a club has a UCL knockout match within 7 days of a domestic cup match:
      Apply domestic_cup_rotation_flag — squad rotation likely;
      don't weight domestic cup performance signal highly in this window.
```

---

## Crypto market cycle overlay

```
CRYPTO CYCLE OVERLAY ON FAN TOKEN DEMAND:

  See: macro/macro-crypto-market-cycles.md for the full four-phase cycle framework.
  This section summarises the overlay effect on fan token demand signals.

  BITCOIN BULL MARKET PHASE (BTC in sustained uptrend, above 200-day MA):
    All fan token demand signals amplified approximately ×1.15.
    Risk appetite is elevated — speculative assets attract capital.
    Signal: sports-specific and club-specific demand signals are stronger
      than in neutral market conditions.
    
  BITCOIN BEAR MARKET PHASE (BTC in sustained downtrend, below 200-day MA):
    All fan token demand signals suppressed approximately ×0.85.
    Risk appetite is compressed — speculative assets lose capital.
    Signal: sports-specific signals still apply but overall demand floor is lower.
    
  ALTCOIN SEASON CONDITIONS:
    Fan tokens typically outperform broader crypto during confirmed altcoin season.
    Definition: altcoins outperforming BTC significantly over a 30-day window.
    Apply: alt_season_demand_amplifier = ×1.20 during confirmed alt season.
    Source: check macro/macro-crypto-market-cycles.md for current phase assessment.
    
  AGENT RULE:
    Before applying any fan token demand signal:
      1. Check current crypto cycle phase (macro/macro-crypto-market-cycles.md)
      2. Apply the appropriate cycle overlay multiplier
      3. Then apply sport-specific and token-specific signals on top
      4. Cycle overlay is the OUTERMOST layer — it affects all tokens equally
      
  IMPORTANT — CYCLE INDEPENDENCE FROM SPORTS SIGNALS:
    The crypto cycle overlay does not change the direction of sport signals.
    It changes their MAGNITUDE.
    A strong positive match result in a bear market: still positive,
      but smaller absolute demand impact.
    A strong negative match result in a bull market: still negative,
      but surrounded by elevated baseline.
```

---

## Compatibility

**Crypto cycles (deep):**   `macro/macro-crypto-market-cycles.md`
**AFCON winter compound:**  `sports/football/sport-domain-afcon.md`
**Transfer volatility:**    `core/transfer-window-intelligence.md`
**Euros dead period inv.:**  `sports/football/sport-domain-euros.md`
**FTP pre-liquidation:**    `fan-token/ftp-path2.md`
**Social sentiment:**       `core/social-sentiment-intelligence.md`
**Portfolio calendar:**     `fan-token/portfolio-intelligence.md`

---

*SportMind v3.97.35 · MIT License · sportmind.dev*
*Cycles repeat reliably every year — use for signal timing calibration*
