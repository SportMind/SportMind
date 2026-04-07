# Gamified Tokenomics Intelligence

**Intelligence framework for fan tokens with outcome-linked supply mechanics —
the Chiliz 2030 gamified tokenomics model where match results directly trigger
on-chain mint or burn events via smart contract.**

This is a new and distinct signal type introduced in 2026. Standard fan token
intelligence applies to static-supply tokens. Gamified tokenomics tokens require
a different analytical model because a WIN prediction is simultaneously a SUPPLY
REDUCTION prediction, creating a compounding commercial signal that does not exist
in the standard fan token lifecycle.

---

## What gamified tokenomics are

```
STANDARD FAN TOKEN (pre-2026 model):
  Supply is fixed or changes only via governance
  Price is driven by sentiment, utility, and macro
  Match outcome → changes sentiment → changes demand → price moves
  
GAMIFIED TOKENOMICS TOKEN (Chiliz 2030 model):
  Supply is dynamic — linked to live match outcomes via smart contract
  If team WINS: tokens BURN (supply decreases → scarcity signal)
  If team LOSES: tokens MINT (supply increases → dilution signal)
  Match outcome → directly triggers supply change → price moves from both
                  demand side (sentiment) AND supply side (burn/mint)

WHY THIS MATTERS FOR SPORTMIND:
  A WIN signal now has two compounding positive effects:
    1. Sentiment uplift (standard — fans excited, engagement high)
    2. Supply burn (new — fewer tokens in circulation → price support)
    
  A LOSS signal now has two compounding negative effects:
    1. Sentiment depression (standard)
    2. Supply dilution (new — more tokens → price pressure)
    
  The combined effect is LARGER than standard token signals.
  SportMind must apply a GAMIFIED_MULTIPLIER to these tokens.
```

---

## Identifying gamified tokenomics tokens

```
DETECTION SIGNALS (check before any analysis):

ON-CHAIN INDICATORS:
  Burn events after match wins: visible on Chiliz Chain explorer
  Mint events after match losses: visible on explorer
  Smart contract address with outcome oracle: linked in token metadata
  
PLATFORM INDICATORS:
  Socios.com 2026+: Live mint/burn tracking displayed on match day
  Token description mentions "performance-linked supply"
  "Dynamic tokenomics" flag in KAYEN token metadata
  
API CHECK:
  GET /tokens/{address} on KAYEN → check for "gamified": true field
  Chiliz Chain explorer: check contract for outcome_oracle binding

RULE: If uncertain whether a token has gamified tokenomics, treat it
as STANDARD. Do not apply the gamified multiplier unless confirmed.
Applying the multiplier to a standard token overstates the signal.
```

---

## The gamified signal model

```
BURN RATE INTELLIGENCE:

Burn rate = tokens burned per win as % of circulating supply
Typical range (Chiliz 2026 initial rollout): 0.1% - 0.5% per win

Burn rate tiers:
  > 0.5% per win: HIGH burn — significant scarcity signal
                  Win prediction + HIGH burn = strong combined signal
  0.2-0.5%:       MODERATE burn — meaningful but not dominant
  < 0.2%:         LOW burn — cosmetic; signal weight similar to standard

MINT RATE INTELLIGENCE:

Mint rate = tokens minted per loss as % of circulating supply
Typical range: matched to burn rate (symmetric by default)
May be asymmetric: some tokens burn more than they mint (deflationary bias)

Asymmetric tokenomics signal:
  Burn rate > Mint rate: deflationary bias → long-term supply reduction
                         Apply: long_term_scarcity_signal = True
  Burn rate < Mint rate: inflationary bias → long-term supply expansion
                         Apply: long_term_dilution_flag = True
  Burn rate = Mint rate: symmetric → neutral long-term supply outlook

CUMULATIVE SUPPLY POSITION:
  Track season-to-date burn/mint net:
  Net burned > 5% of original supply: significant scarcity accumulated
  Net minted > 5%: significant dilution accumulated
  Apply as season_supply_modifier to ongoing signal calculations
```

---

## Pre-match signal adjustment for gamified tokens

```
GAMIFIED TOKENOMICS MODIFIER (apply AFTER standard SportMind signal):

Step 1: Confirm gamified tokenomics active for this token
Step 2: Get burn rate and mint rate
Step 3: Get current circulating supply position (net season burn/mint)
Step 4: Get pre-match WIN/LOSS direction from standard signal

IF direction = HOME WIN or AWAY WIN (and predicted team has gamified token):
  
  gamified_win_multiplier = 1.00 + (burn_rate_pct × 2.5)
  
  Examples:
    0.5% burn per win: gamified_win_multiplier = 1.00 + (0.005 × 2.5) = 1.0125
    0.3% burn per win: gamified_win_multiplier = 1.00 + (0.003 × 2.5) = 1.0075
    0.1% burn per win: gamified_win_multiplier = 1.00 + (0.001 × 2.5) = 1.0025
  
  Apply: adjusted_score × gamified_win_multiplier
  
  Note: The multiplier is deliberately conservative. Burn rates in the
  0.1-0.5% range create meaningful but not dominant supply effects.
  The sentiment signal remains primary; the burn signal amplifies it.

IF direction = LOSS (for a team with gamified tokenomics):

  gamified_loss_multiplier = 1.00 - (mint_rate_pct × 2.0)
  
  Apply: adjusted_score × gamified_loss_multiplier (further reduces score)
  
  Note: Mint dilution has smaller effect than burn scarcity because
  dilution is gradual and expected; scarcity events are more psychologically
  impactful on holder sentiment.

IF direction = DRAW:
  No supply change triggered (standard draw → no burn or mint)
  Apply standard draw signal; no gamified modifier
  
  Exception: Check individual token smart contract for draw handling —
  some tokens mint on draw at reduced rate (verify before assuming no effect)
```

---

## Season-level gamified intelligence

```
SEASON SUPPLY TRACKING:

Unlike standard tokens where supply is effectively constant within a season,
gamified tokens accumulate supply changes across all matches.

At the start of a season:
  Supply position = 0 (neutral)
  
During season:
  After each win: net_burned += burn_rate
  After each loss: net_minted += mint_rate
  
Season supply signal tiers:
  Net burned > 10% cumulative: STRONG SCARCITY — elevated base signal all season
  Net burned 5-10%: MODERATE SCARCITY — meaningful floor support
  Net burned 0-5%: MILD SCARCITY — early signal, not yet dominant
  Net minted 0-5%: MILD DILUTION — minor headwind
  Net minted > 10%: SIGNIFICANT DILUTION — reduces sentiment impact of individual wins

CHAMPIONSHIP RUN SIGNAL:
  A team on a 10-match winning streak with 0.3% burn per win has burned
  approximately 3% of supply. This is a significant cumulative scarcity event.
  Apply: championship_run_scarcity_modifier = 1.08 (season-level floor boost)
  
  Conversely, a team on a losing streak with 10+ losses:
  Apply: season_dilution_concern_flag = True
  Reduce pre-match signal by an additional 0.95× per loss beyond 5 consecutive
```

---

## Prediction market interaction

```
GAMIFIED TOKENS + PREDICTION MARKETS:

The Chiliz 2030 manifesto explicitly frames gamified tokenomics as "a perfect
complement to prediction markets where users can take long-horizon positions
across multiple teams at once."

This creates a new intelligence requirement: when a prediction market is active
on a team with gamified tokenomics, the prediction market position and the
token supply position interact.

AGENT RULE — PREDICTION MARKET WITH GAMIFIED TOKEN:
  If: prediction market open AND token has gamified tokenomics
  Then: the prediction market outcome AND the supply change are correlated
  Apply: prediction_market_gamified_correlation_flag = True
  
  Signal interpretation:
    A large prediction market position betting on a WIN creates buying pressure
    on the token (anticipating burn) in addition to the standard prediction market dynamic.
    
    Monitor: Is there unusual token buying before prediction market events?
    This may indicate informed participants anticipating both the win AND the burn.
    
  Caution: This creates a new surveillance requirement.
    Large pre-match token buys that correlate with prediction market positions
    may indicate market manipulation or informed trading.
    Apply: unusual_pre_match_activity_flag if token volume > 3× average
           in the 4h before a gamified token match.
```

---

## Chiliz 2030 rollout context

```
CURRENT STATE (2026):
  Gamified tokenomics announced in Chiliz 2030 Manifesto (February 2026)
  Performance-linked mint/burn mechanics: Q2 2026 rollout per roadmap
  Initial rollout: selected tokens only (not all fan tokens immediately)
  
WHICH TOKENS HAVE GAMIFIED TOKENOMICS:
  Check: Socios.com token page for "performance-linked" indicator
  Check: KAYEN API for gamified flag
  Default assumption: tokens issued before Q2 2026 are STANDARD unless confirmed
  
DETECTION RULE FOR AGENTS:
  At agent initialisation, for each monitored token:
    1. Query KAYEN API for gamified status
    2. If gamified = true: load this skill
    3. If gamified = false or unknown: use standard on-chain-event-intelligence.md
    4. Re-check at start of each new season (status may change between seasons)

ROADMAP AWARENESS:
  2026: Performance-linked tokenomics rolling out to initial tokens
  2026 Q4+: Expanded rollout expected across more tokens
  2030 target: Full three-stage token evolution (utility → dynamic → RWA)
  
  SportMind agents should monitor for gamified status changes on all tracked tokens.
  A token transitioning from standard to gamified is a significant lifecycle event.
  Apply: CDI equivalent signal on gamified tokenomics activation (14-day window)
```

---

## Complete pre-match workflow for gamified token

```
Step 1: MACRO CHECK (always first)
  macro_modifier from macro/macro-overview.md
  
Step 2: GAMIFIED STATUS CONFIRMATION
  Is this token gamified? (KAYEN API check)
  If NO: use standard fan token signal chain. Stop here.
  If YES: continue with gamified workflow.
  
Step 3: BURN/MINT RATES
  burn_rate_pct: tokens burned per win / circulating supply
  mint_rate_pct: tokens minted per loss / circulating supply
  
Step 4: SEASON SUPPLY POSITION
  net_season_change: cumulative burns minus cumulative mints this season
  
Step 5: STANDARD SPORTMIND SIGNAL
  Run standard pre-match signal for the sport
  Output: direction, adjusted_score, SMS
  
Step 6: APPLY GAMIFIED MODIFIER
  If direction = WIN:
    final_score = adjusted_score × gamified_win_multiplier
  If direction = LOSS:
    final_score = adjusted_score × gamified_loss_multiplier
  If direction = DRAW:
    final_score = adjusted_score (no supply change)
    
Step 7: SEASON SUPPLY CONTEXT
  Apply season_supply_modifier if net burned/minted > 5%
  
Step 8: PREDICTION MARKET FLAG
  If prediction market active: set correlation flag
  Check for unusual pre-match volume (>3× average in 4h window)
  
Step 9: OUTPUT
  Standard confidence schema + gamified_modifier field + season_supply_position
```

---

## Output schema extension for gamified tokens

```json
{
  "token": "PSG",
  "gamified_tokenomics": true,
  "burn_rate_pct": 0.003,
  "mint_rate_pct": 0.003,
  "season_net_change_pct": -0.021,
  "season_supply_signal": "MILD_SCARCITY",
  
  "standard_signal": {
    "direction": "HOME",
    "adjusted_score": 72.4,
    "sms": 78
  },
  
  "gamified_modifier": 1.0075,
  
  "final_signal": {
    "direction": "HOME",
    "adjusted_score": 72.9,
    "recommended_action": "ENTER",
    "gamified_amplification": "WIN prediction + 0.3% burn = mild supply scarcity if correct"
  },
  
  "flags": {
    "gamified_tokenomics_active": true,
    "season_scarcity_accumulated": true,
    "prediction_market_correlation": false,
    "unusual_pre_match_volume": false
  }
}
```

---

## Compatibility

**On-chain events:** `fan-token/on-chain-event-intelligence/` — burn/mint detection
**Fan token lifecycle:** `fan-token/fan-token-lifecycle/` — Phase 5 dynamic tokenomics
**RWA intelligence:** `fan-token/rwa-sportfi-intelligence/` — Stage 2 dynamic token model
**DeFi liquidity:** `fan-token/defi-liquidity-intelligence/` — supply changes affect TVL
**Data connectors:** `platform/data-connector-templates.md` — KAYEN gamified status API

*MIT License · SportMind · sportmind.dev*
*Based on Chiliz 2030 Manifesto (February 2026) — performance-linked tokenomics*
