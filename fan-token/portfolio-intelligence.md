---
name: portfolio-intelligence
description: >
  Reasoning framework for holding multiple fan tokens simultaneously as a
  portfolio. Covers cross-token correlation, concentration risk, calendar
  arbitrage, and portfolio rebalancing signals. All demand-only context —
  portfolio reasoning does not change individual token PATH_2 mechanics.
---

# Fan Token Portfolio Intelligence

**How to reason about multi-token holdings — correlation, concentration, and calendar risk.**

> Library Rule: framework applies to any portfolio of fan tokens at any time.
> No specific current prices or holdings data.

---

## Cross-token correlation

```
CORRELATION IN NORMAL CONDITIONS:

  SAME LEAGUE TOKENS:
    Tokens from the same league move together on league-wide news.
    Correlation coefficient: ~0.85 in normal market conditions
    Events that trigger correlated moves:
      Broadcasting rights announcement (affects all league clubs)
      League regulatory changes (affects all clubs simultaneously)
      Relegation/promotion season narrative (heightens all club uncertainties)
      
    Portfolio implication: five tokens from one league ≠ five independent signals.
    Effective diversification = roughly 1.5-2 independent signals from 5 same-league tokens.
    
  SAME COMPETITION TOKENS (e.g. UCL clubs):
    Tokens from clubs in the same European competition correlate strongly during
    the competition window.
    UCL correlation: ~0.80 during knockout stages
    Move together on: draws, format changes, broadcast announcements
    
  CHZ CORRELATION — MACRO RISK-OFF:
    All fan tokens show high correlation with $CHZ price during macro stress.
    In crypto market risk-off events: CHZ correlation rises to ×0.90+ for all tokens
    This is the highest correlation condition in the library.
    
    Implication: No fan token portfolio is diversified against CHZ/crypto macro moves.
    Diversification only helps against token-specific or sport-specific events.
    Apply: portfolio_correlation_warning when CHZ shows sustained downward movement.
```

---

## Concentration risk reasoning

```
CONCENTRATION RISK FRAMEWORK:

  HIGH CONCENTRATION (5+ tokens from one league):
    Single league events affect the entire portfolio simultaneously.
    Risk events: relegation drama, title race conclusion, broadcasting disputes
    Apply: concentration_risk_flag = HIGH
    Recommended: reduce to maximum 3 tokens per league for diversification benefit
    
  GEOGRAPHIC DIVERSIFICATION:
    Mixing tokens from different geographic markets reduces regional event risk.
    European tokens + Brazilian tokens ($FLU, $MENGO) + APAC tokens:
      Reduces correlation during regional political/economic events
      Brazilian real or APAC currency moves affect local demand independently
      
    Diversification premium:
      3+ geographic regions represented: apply portfolio_diversification_modifier = ×1.05
        (5% bonus to effective CDI stability — portfolio less vulnerable to single-region shocks)
      Single region only: no bonus, apply concentration_risk_flag = MODERATE
      
  COMPETITION DIVERSIFICATION:
    Mixing football, MMA ($UFC), rugby ($SARRIES), motorsport ($AM, $SAUBER):
      Reduces FTP PATH_2 event clustering risk
      Non-football tokens have different event calendars — they do not all fire
      supply/demand events on the same days
      
    FTP PATH_2 CLUSTERING (for $AFC only):
      $AFC PATH_2 events fire on Arsenal competitive match days.
      Other club tokens in portfolio: if they are NOT PATH_2, no supply clustering risk.
      Portfolio with $AFC + non-PATH_2 tokens: only $AFC fires supply events.
      This is not a risk — it is the correct structure.
      
  POSITION SIZE REASONING:
    PATH_2 tokens ($AFC) have a different risk profile than demand-only tokens:
      PATH_2 tokens: supply mechanic can actively burn or mint — higher volatility
      Demand-only tokens: price moves with sentiment only — lower structural volatility
      Apply: path2_position_sizing_guidance = size PATH_2 positions
        with awareness of supply event timing (match calendar driven)
```

---

## Calendar arbitrage framework

```
FTP PATH_2 EVENT DENSITY — CALENDAR SIGNAL:

  HIGHEST EVENT DENSITY PERIODS (most $AFC supply events concentrated):
    UCL knockout stages (February-May): up to 2 PATH_2 events per week
      Pre-liquidation + buyback sequence compressed into short windows
      Demand and supply signals peak simultaneously
      
    End of domestic season (April-May): fixture congestion; multiple events weekly
    
  LOWER EVENT DENSITY PERIODS:
    International breaks: no club competitive matches → no PATH_2 events
    Summer pre-season: no competitive matches → no supply events
    Early group stage (September-October): matches every 1-2 weeks; moderate density
    
  CALENDAR SIGNAL FOR PORTFOLIO:
    Before high-density periods: pre-position in $AFC for elevated PATH_2 signal period
    During international breaks: expect reduced $AFC CDI signal; no new supply events
    World Cup year (June-July): if Arsenal players at World Cup, no $AFC club matches
      → No PATH_2 events during World Cup club hiatus

NATIONAL TOKEN ROTATION:
  During major international tournaments (Euros, Copa, AFCON, World Cup):
    National tokens (or club proxy tokens — see sport-domain-euros.md) build demand
    Club tokens may underperform relatively during tournament windows
    
    Calendar rotation signal:
      Pre-tournament: rotate toward national sentiment proxies
      Post-tournament: rotate back toward club tokens as club season resumes
      Apply: tournament_rotation_signal = monitor 4-6 weeks before tournament start

TRANSFER WINDOW VOLATILITY:
  Summer window (June-August):
    Transfer activity creates demand volatility across MULTIPLE tokens simultaneously
    High cross-token correlation during window (all clubs buying/selling)
    Apply: window_volatility_flag during active summer window
    Post-window: stability premium ×1.02 across portfolio (not just individual tokens)
    
  Winter window (January):
    Smaller effect; compounds with AFCON disruption
    Lower window_volatility compared to summer; apply reduced flag
```

---

## Portfolio rebalancing signals

```
POST-SEASON REBALANCING:

  TRIGGER: End of football season (May-June)
    Squad changes affect multiple tokens simultaneously
    This is the widest rebalancing opportunity window of the year
    
  SIGNALS TO MONITOR:
    Which clubs are confirmed in UCL next season? → demand trajectory elevated
    Which clubs are relegated? → demand trajectory severely reduced for 12+ months
    Which clubs have made marquee signings? → apply arrival premium framework
    Which clubs lost key players? → apply departure decay framework
    
  REBALANCING GUIDANCE:
    Confirm squad compositions at summer window close (August)
    Only after window close do you have certainty about the season's squad
    Pre-window speculation: apply uncertainty discount ×0.95 to squad quality signals
    Post-window confirmed: remove uncertainty discount; apply confirmed squad modifiers

PRE-TOURNAMENT ROTATION:
  Before major international tournaments (4-6 weeks prior):
    National token proxies build demand — club token holders rotate toward national narrative
    Consider: which club tokens carry the national sentiment proxy signal?
      (see sport-domain-euros.md for European examples)
    
  POST-TOURNAMENT:
    Club season resumes; club token demand recovers
    Recovery speed varies by how far relevant national teams progressed:
      Early elimination: club demand recovers quickly (1-2 weeks)
      Tournament winners: elevated national sentiment persists 2-3 weeks; club recovery slower

MID-SEASON COMPETITION ELIMINATION:
  When a club token's club is eliminated from a competition:
    Competition-specific demand trajectory resets downward
    Apply: elimination_demand_decay (see national-team-tokens.md for decay curves —
      same framework applies to club tokens eliminated from European competition)
    UCL elimination: −15-25% demand drop depending on round
    Rotate: if UCL elimination is confirmed, reallocate demand weight to advancing clubs
```

---

## Compatibility

**Transfer volatility:**  `core/transfer-window-intelligence.md`
**National tokens:**      `fan-token/national-team-tokens.md`
**PATH_2 mechanics:**     `fan-token/ftp-path2.md`
**Euros club proxies:**   `sports/football/sport-domain-euros.md`
**Tournament macro:**     `macro/tournament-macro.md`
**AFCON disruption:**     `sports/football/sport-domain-afcon.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan token portfolio intelligence: multi-token diversification signals and portfolio-level modifiers |
| Reasoning | ACTIVE | Portfolio reasoning chain from individual token signals to aggregate portfolio signal |
| Context | ACTIVE | Portfolio context: correlation structure, token diversity, macro regime, CHZ exposure |
| Memory | ACTIVE | Historical portfolio performance patterns and correlation data |
| Judgment | ACTIVE | Judgment on portfolio signal aggregation — correlated tokens require concentration discount |
| Attention | ACTIVE | Elevated attention for portfolio-wide events: CHZ price movement, macro regime shifts |
| Communication | ACTIVE | Portfolio output with aggregate signal, concentration risk, and diversification assessment |
| Verification | ACTIVE | Portfolio signals aggregate verified individual token signals — single unverified token contaminates |
| Learning | EMERGING | Portfolio-level calibration is limited — requires multi-token tracking data |
| Integration | ACTIVE | Integrates with supply intelligence, ecosystem health, and macro intelligence |
| Calibration | EMERGING | Portfolio correlation structure calibration is an emerging framework |
| Adaptation | ACTIVE | Portfolio intelligence adapts as token set and correlation structure evolve |
| Ethics | NOT APPLICABLE | Portfolio analysis is financial — no ethical dimension beyond individual token ethics |
| Transparency | ACTIVE | Portfolio composition, correlation assumptions, and concentration risk explicit in output |
| Execution | ACTIVE | Signal generation workflow, event playbooks, and structured output templates defined |
| Collaboration | ACTIVE | Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer |


---

*SportMind v3.97.28 · MIT License · sportmind.dev*
*CHZ macro moves affect all tokens equally — no fan token portfolio diversifies against CHZ*
