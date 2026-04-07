# Signal Weight System

When a base signal score is produced by a sports intelligence platform, it is typically
a weighted composite of several components. SportMind recommends adjusting the
**interpretive weight** of each component based on the sport being analysed.

These are not overrides to any API output. They are reasoning guidelines — they tell
an agent which components to trust most when evaluating a signal for a given sport.

---

## Recommended weights by sport

| Sport | Market / whale | Social sentiment | Sports catalyst | Price trend | Macro |
|---|---|---|---|---|---|
| Football / soccer | 25% | 20% | **30%** | 15% | 10% |
| Basketball | 20% | **30%** | 25% | 15% | 10% |
| MMA | 15% | **35%** | **30%** | 15% | 5% |
| Esports | 15% | **40%** | 25% | 15% | 5% |
| American Football (NFL) | 25% | 25% | **30%** | 15% | 5% |
| Cricket | 20% | 15% | **35%** | 20% | 10% |
| Formula 1 | 20% | 20% | **30%** | 20% | 10% |
| Ice Hockey (NHL) | 25% | 15% | **35%** | 20% | 5% |
| Baseball (MLB) | 20% | 10% | **40%** | 20% | 10% |
| MotoGP | 20% | **25%** | **35%** | 15% | 5% |
| AFL | 20% | 20% | **35%** | 15% | 10% |
| Handball | 20% | 20% | **35%** | 15% | 10% |
| Kabaddi | 15% | **30%** | **35%** | 15% | 5% |
| NASCAR | 20% | 15% | **40%** | 20% | 5% |
| Rugby (Union / League) | 25% | 15% | **35%** | 15% | 10% |
| Tennis | 20% | 25% | **30%** | 20% | 5% |
| Golf | 15% | 20% | **35%** | 20% | 10% |
| Boxing | 10% | **35%** | **35%** | 15% | 5% |
| Cycling | 15% | 15% | **40%** | 20% | 10% |
| Athletics | 10% | **30%** | **35%** | 20% | 5% |
| Horse Racing | 20% | 10% | **45%** | 20% | 5% |
| Darts | 20% | **30%** | **35%** | 10% | 5% |
| Snooker | 20% | 20% | **40%** | 15% | 5% |
| Netball | 15% | **30%** | **35%** | 15% | 5% |
| Winter Sports | 15% | 20% | **40%** | 20% | 5% |
| Volleyball | 15% | **25%** | **40%** | 15% | 5% |
| Badminton | 15% | **25%** | **40%** | 15% | 5% |
| Swimming | 10% | **25%** | **40%** | 20% | 5% |
| Rowing | 10% | 20% | **45%** | 20% | 5% |
| Table Tennis | 10% | 20% | **45%** | 20% | 5% |

*All rows sum to 100%. Bold = highest weighted component(s) for that sport.*

---

## Rationale by component

### Market / whale flows
Institutional positioning data. Higher in sports with regular weekly events (football,
NFL) where whale accumulation patterns are well-established. Lower in narrative-heavy
sports (MMA, esports) and individual/Olympic sports (rowing, swimming, table tennis)
where retail sentiment and singular events dominate over institutional positioning.

### Social sentiment
Social media momentum, mentions, and sentiment scores. Highest for MMA, esports, and
kabaddi — all are highly narrative-driven with young, digitally-native fanbases whose
sentiment moves fast and correlates with price. Elevated for boxing, darts, netball
(where individual personality and narrative drive engagement). Lower for football and
rugby where structural outcomes dominate.

### Sports catalyst
The actual sporting event — match result, importance score, competition tier. Always
the highest or joint-highest component across all sports. Highest for horse racing
(the race IS the entire product; no surrounding narrative competes), cycling (Grand
Tour stage results are the dominant signal), and individual Olympic sports where a
single result defines an athlete's season. Slightly lower for basketball where star
player status often matters as much as the result.

### Price trend
Recent price momentum independent of sports events. Higher for sports with infrequent
events (cycling, winter sports, athletics) where price trends between major competitions.
Lower for MMA and esports where price action is dominated by fight-week / tournament
week catalysts rather than trends.

### Macro
Broader market conditions — CHZ/BTC trend, crypto cycle, risk-on/off environment.
Generally low across all sports. Fan token prices are primarily driven by sport-specific
catalysts. Slightly higher for football (most mature token market; more CHZ correlation
during quiet sporting periods) and outdoor/seasonal sports (cricket, AFL, cycling)
where economic and climate macro factors have documented commercial impact.

---

## How to use these weights in agent reasoning

```
# Example: evaluating a football signal of score 72

base_score = 72
sports_catalyst_component = 68   # below average — low-importance fixture
social_component = 81            # above average — fan excitement
whale_component = 74             # neutral accumulation

# Apply football weights:
# sports_catalyst (30%) + whale (25%) + social (20%) + price (15%) + macro (10%)

# Agent interpretation:
# The sports catalyst is below average for football (30% weight).
# Even with strong social, the composite should be treated as NEUTRAL,
# not BULLISH — match importance is the dominant input for football.
```

---

## Phase adjustments

Signal weights shift during different phases of a season or event cycle:

| Phase | Adjustment |
|---|---|
| Regular season | Use standard weights above |
| Playoffs / finals | Increase sports catalyst +5–10%; reduce macro to near-zero |
| Off-season | Increase social and price trend; reduce sports catalyst |
| International break (football) | Reduce sports catalyst to near-zero for club tokens |
| Fight week (MMA) | Increase social to 45%; reduce macro to 0% |
| Tournament week (esports) | Increase social to 45%; increase sports catalyst to 30% |
| Grand Tour week 3 (cycling) | Increase sports catalyst to 50%; fatigue is everything |
| Olympics (athletics/swimming/rowing) | Increase sports catalyst to 55%; 4-year cycle peak |
| Fight camp period (boxing/MMA) | Increase social to 40%; information scarcity premium |

---

## Macro cycle overlay

Apply an additional multiplier to all signals when a macro event is active.
See `macro/macro-crypto-market-cycles.md` for the full CHZ/BTC cycle framework:

| Macro condition | Signal multiplier |
|---|---|
| Crypto bull market (BTC above 200-day MA) | × 1.20 |
| Crypto neutral | × 1.00 |
| Crypto bear market (BTC below 200-day MA) | × 0.75 |
| Crypto extreme bear / capitulation | × 0.55 |

These multipliers apply after the sport-specific weights above have been calculated.

---

*See `macro/macro-overview.md` for full macro modifier framework.*
*See `core/core-athlete-modifier-system.md` for athlete modifier pipeline.*
*See `core/core-result-impact-matrices.md` for result-type price impact ranges.*
