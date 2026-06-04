---
name: transfer-window-intelligence
description: >
  Core reasoning framework for transfer window activity as a signal modifier
  for fan tokens and match outcomes. Covers window calendar, arrival/departure
  modifiers, FTP PATH_2 implications for $AFC, deadline day signals, and
  post-window stability premium. Agent-facing interface that integrates with
  fan-token/transfer-window-intelligence/ and fan-token/transfer-intelligence/.
---

# Transfer Window Intelligence — Core Reasoning Framework

**How to reason about confirmed transfer activity as a signal modifier.**
Not transfer rumours — confirmed transfers and window dynamics only.

> Library Rule: framework for applying transfer signals, not a database of
> specific transfers. All elements are true and useful beyond six months.

Related files:
- `fan-token/transfer-window-intelligence/` — window calendar signal patterns
- `fan-token/transfer-intelligence/` — transfer fee benchmarks and profiles

---

## Window calendar reasoning

```
TRANSFER WINDOW CALENDAR — SIGNAL TIMING:

  SUMMER WINDOW (June – August, primary window):
    Structural characteristics:
      Major squad overhauls possible — all positions can change
      Fan token demand is most volatile during this period
      Multiple clubs active simultaneously — cross-token correlation elevated
      Squad uncertainty is at its highest — signal confidence reduced
      
    Signal implications:
      Apply: summer_window_uncertainty_modifier = ×0.92 on match outcome signals
        for matches during active summer window (lineups less settled)
      Fan token demand: amplified volatility — both arrivals and departures
        compound across multiple tokens at the same time
      Post-window (September onwards): demand stabilises as squads lock in
      
  WINTER WINDOW (January, secondary window):
    Structural characteristics:
      Limited structural changes typical — mostly gap fills
      AFCON disruption compounds with winter window activity simultaneously
      Financially distressed clubs may sell key assets in January
      
    Signal implications:
      Apply: winter_window_modifier = ×0.97 on match outcome signals (smaller effect)
      Financial distress sales: apply compound_negative_signal (see departure framework)
      AFCON compound: if key African player departs during winter window, apply
        both departure decay AND AFCON absence modifier — they are independent signals
        
  DEADLINE DAY (final 48 hours of any window):
    Signal characteristics:
      Confirmed signings in final 24 hours apply ×1.15 demand spike modifier
      Duration: 24-48 hours then normalises toward new baseline
      Multiple deadline day signings: each adds independently, but cap at ×1.40 combined
      Failed deal reports (player didn't complete medical, fee not agreed): apply
        ×0.97 brief negative sentiment if reported as confirmed then collapsed
        
  POST-WINDOW STABILITY PREMIUM:
    When window closes with squad confirmed for remainder of season:
      Apply: post_window_stability_modifier = ×1.02 for 2 weeks
      Mechanism: uncertainty resolves; holders gain confidence in squad
      Remove after 2 weeks: premium absorbed into new baseline
```

---

## Arrival impact framework

```
CONFIRMED ARRIVAL MODIFIERS:

  MARQUEE SIGNING (defined as: transfer fee above €50M OR player of clear
  established international quality, widely recognised globally):
    Demand premium: +15-25% over 2-4 weeks
    New structural baseline: +5-10% permanently above pre-signing baseline
    Duration of premium: 2-4 weeks from confirmation, then decay to new baseline
    
    Modifier table:
      Week 1-2 after confirmation: arrival_premium = ×1.20 (centre of range)
      Week 3-4: arrival_premium = ×1.10 (decaying)
      Week 5+: new baseline established; remove arrival premium
      
    Match outcome signal: apply squad_quality_improvement_modifier per position
      (see tier-a-clubs-framework.md for position modifier weights)
      
  NOTABLE SIGNING (recognised within sport; not globally marquee):
    Demand premium: +8-15% over 2-3 weeks
    New baseline: +2-4% above pre-signing
    
  SQUAD DEPTH SIGNING (squad depth, backup role):
    Demand modifier: ×1.00 — neutral
    No match outcome modifier — squad player does not change expected lineup
    
  ACADEMY PROMOTION (youth player promoted to first team):
    Demand modifier: ×1.02 (positive sentiment, minor)
    Match outcome: apply only if player enters expected starting XI
    Duration: 1 week sentiment spike then neutral
    
  AGENT RULE:
    Before applying arrival modifier, confirm:
      1. Is signing confirmed (club announcement)? Not rumour.
      2. What tier is the signing? Apply appropriate modifier tier.
      3. Does signing affect expected starting XI? If not, no match signal.
```

---

## Departure impact framework

```
CONFIRMED DEPARTURE MODIFIERS:

  MARQUEE DEPARTURE (defined as: transfer fee above €50M OR loss of key
  player to rival; player of clear international quality):
    Demand decay: -10-20% over 4-8 weeks
    New structural baseline: -5-10% permanently below pre-departure baseline
    Decay timeline:
      Week 1-2: initial_departure_drop = ×0.88 (acute negative sentiment)
      Week 3-4: secondary_decay = ×0.93 (processing phase)
      Week 5-8: stabilisation toward new baseline
      Week 8+: new structural baseline established
      
    Match outcome signal: apply squad_quality_reduction_modifier per position
      (mirror of arrival modifier — see position weights)
      
  FORCED SALE (financial distress signal):
    Compound negative — not just player value lost but club health signal
    Demand decay: -15-25% (wider range; uncertainty about club finances)
    Also apply: club_financial_health_flag = CAUTION
    Club health risk modifier: ×0.90 on all signals until financial clarity confirmed
    
  SALE TO DIRECT RIVAL:
    Additional rivalry_negative_modifier = ×0.97 applied on top of standard departure
    Mechanism: fan emotional response to seeing player succeed at rival club
    Duration: persists for 2-3 matches when rival plays a high-profile fixture
    
  LOAN DEPARTURE:
    Player still owned by club; return possible
    Demand modifier: ×0.99 (minimal — temporary absence, not permanent loss)
    Match outcome: apply only if departed player was expected starter
      For backup players: no modifier
      
  NET TRANSFER ACTIVITY (simultaneous arrival + departure):
    If same-tier signing arrives as same-tier departure occurs:
      Calculate net: arrival premium + departure decay
      Net positive arrival: net modifier > 0 → apply net demand signal
      Net negative: more significant departure → apply net negative signal
      Rough equivalence: ×1.00 net — no modifier (wash trade)
```

---

## FTP PATH_2 transfer implications

```
$AFC TRANSFER IMPLICATIONS — PATH_2 CHAIN:

  WHY TRANSFERS MATTER MORE FOR $AFC:
    Every squad quality change affects both match outcome probability AND
    expected FTP supply event magnitude.
    
    This double-signal does NOT apply to other clubs (demand only for $PSG,
    $BAR, $JUV, $ACM, $CITY etc. — see tier-a-clubs-framework.md).

  MARQUEE ARRIVAL AT ARSENAL ($AFC):
    Step 1: Apply standard demand arrival premium (+15-25%)
    Step 2: Determine which position the arrival fills
    Step 3: Apply squad quality improvement to win probability
    Step 4: Propagate win probability improvement to PATH_2 expected burn:
      Higher win probability → larger expected pre-liquidation burn event
      Apply: path2_arrival_uplift = squad_quality_improvement × 0.60
      (Not all squad quality improvement translates to PATH_2 signal — 0.60 factor)
      
  MARQUEE DEPARTURE FROM ARSENAL ($AFC):
    Step 1: Apply standard demand departure decay (-10-20%)
    Step 2: Determine which position is weakened
    Step 3: Apply squad quality reduction to win probability
    Step 4: Propagate win probability reduction to PATH_2 expected burn:
      Lower win probability → smaller expected burn; larger expected mint
      Apply: path2_departure_reduction = squad_quality_reduction × 0.60
      
  POSITION CRITICALITY:
    Departure of right winger (Arsenal's highest modifier position):
      Maximum PATH_2 impact — this position shifts win probability most
    Departure of squad depth player:
      Minimal PATH_2 impact — win probability barely changes
    See: athlete/football/arsenal-afc.md for position modifier weights
```

---

## Compatibility

**Window calendar depth:**  `fan-token/transfer-window-intelligence/`
**Transfer fee benchmarks:** `fan-token/transfer-intelligence/`
**Arsenal PATH_2 chain:**    `athlete/football/arsenal-afc.md`
**Tier A demand curves:**    `athlete/football/tier-a-clubs-framework.md`
**Social sentiment:**        `core/social-sentiment-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Transfer window intelligence: window timing, activity patterns, and market dynamics |
| Reasoning | ACTIVE | Transfer window reasoning chain from window status to squad change probability |
| Context | ACTIVE | Window context: days remaining, club financial state, known targets, loan market |
| Memory | ACTIVE | Historical transfer window patterns by club profile and window phase |
| Judgment | ACTIVE | Window judgment: late-window risk — deals accelerate near deadline |
| Attention | ACTIVE | Maximum attention during deadline day — highest velocity information environment |
| Communication | ACTIVE | Window signal output with status, days remaining, and active deal signals |
| Verification | ACTIVE | Transfer confirmation requires official club announcement — journalist reports are Tier 2 |
| Learning | ACTIVE | Window pattern calibration from historical deal completion timing data |
| Integration | ACTIVE | Integrates with squad intelligence, CDI, and player agent intelligence |
| Calibration | ACTIVE | Transfer window modifiers calibrated against historical window-activity-outcome data |
| Adaptation | ACTIVE | Window intelligence adapts as regulations and market structures evolve |
| Ethics | ACTIVE | Transfer speculation about young players requires additional care |
| Transparency | ACTIVE | Transfer source tier and confirmation status always explicit in output |


---

*SportMind v3.97.28 · MIT License · sportmind.dev*
*Confirmed transfers only — do not apply transfer rumour signals*
