# Result Impact Matrices

Historical average price / market impact by result type across all sports covered by SportMind. Use these as baseline estimates — always prefer token-specific or market-specific historical data when available.

All ranges are approximate. Actual impact depends on: importance of event, whether result was expected or upset, current market liquidity, and macro conditions.

---

## Football / Soccer

| Result | Home token | Away token |
|---|---|---|
| Home win (expected) | +2–4% | -1–3% |
| Home win (upset) | +6–12% | -4–8% |
| Away win (expected) | -2–4% | +2–5% |
| Away win (upset) | -5–10% | +8–15% |
| Draw (high-stakes) | -1–3% both | |
| Draw (low-stakes) | ~0% both | |
| Title clinched | +8–20% | — |
| Relegation confirmed | -15–35% | — |
| UCL group stage exit | -8–15% | — |
| Derby win (local rival) | +5–12% | -3–8% |

---

## Basketball

| Result | Token impact |
|---|---|
| Regular season win | +1–3% |
| Regular season loss | -1–2% |
| Playoff win (series advance) | +5–15% |
| Playoff elimination | -10–20% |
| Upset win vs top seed | +6–12% |
| Championship series win | +15–35% |
| Star player injury (out for season) | -10–25% |
| Star player trade acquisition | +8–20% |
| Star player traded away | -12–30% |

---

## MMA

| Result | Winner token | Loser token |
|---|---|---|
| Win by KO / TKO | +15–40% | -15–30% |
| Win by submission | +12–30% | -10–25% |
| Win by decision | +5–15% | -5–12% |
| Draw | -3–8% both | |
| No contest / DQ | -10–20% both | |
| Title won | +25–60% | -20–40% |
| Title lost | -20–45% | +25–55% |
| Weigh-in miss (own token) | -10–25% | |
| Weigh-in miss (opponent) | +3–8% | |
| Fight cancelled | -15–35% both | |
| Retirement announced | -30–70% | |

---

## Esports

| Result | Token impact |
|---|---|
| Regular season match win | +1–4% |
| Regular season match loss | -1–3% |
| Tournament quarter-final win | +3–8% |
| Major / tournament win | +10–25% |
| Major / tournament loss (final) | -5–15% |
| Upset win vs top-3 seed | +6–15% |
| Relegation to tier 2 | -10–30% |
| Star player transfer (to org) | +8–20% |
| Star player transfer (away) | -10–25% |
| Full roster rebuild | -10–30% |
| Worlds / TI / Major run (deep) | +15–40% over tournament |

---

## American football (NFL)

| Result | Token impact |
|---|---|
| Regular season win (expected) | +2–5% |
| Regular season upset win | +6–15% |
| Regular season loss (expected) | -2–4% |
| Regular season upset loss | -5–12% |
| Playoff win | +8–18% |
| Conference Championship win | +15–30% |
| Super Bowl win | +25–55% |
| Super Bowl loss | -15–30% |
| Elite QB injury (out for season) | -10–25% |
| Top QB signed in free agency | +10–25% |

---

## Cricket

| Result / event | Token / market impact |
|---|---|
| T20 match win | +2–5% |
| T20 match loss | -2–4% |
| IPL playoff qualification | +8–18% |
| IPL title win | +20–40% |
| Test match win | +3–7% |
| Star batter century (T20) | +3–8% same day |
| Star bowler 5-wicket haul | +3–6% |
| Key player injury | -8–20% |
| Toss win (batting-friendly pitch) | +2–5% |

---

## Rugby

| Result | Token / market impact |
|---|---|
| Regular match win (expected) | +2–5% |
| Regular match win (upset) | +6–14% |
| Six Nations / Rugby Championship win | +8–18% |
| World Cup win | +20–40% |
| Key kicker misses (costly loss) | -5–10% |
| Star player injury | -8–18% |

---

## Tennis

| Result | Token / market impact |
|---|---|
| Early round win (expected) | +1–3% |
| Grand Slam final win | +12–25% |
| Grand Slam upset win | +8–20% |
| Withdrawal before Grand Slam | -8–20% |
| Injury retirement mid-match | -10–25% |
| World No. 1 ranking achieved | +5–12% |

---

## Formula 1

| Result | Token / market impact |
|---|---|
| Race win (expected constructor) | +3–7% |
| Race win (upset) | +8–15% |
| Championship constructors title | +15–30% |
| DNF / mechanical failure | -3–8% |
| Driver/constructor announcement | +5–15% |
| Mid-season team principal change | -5–12% |

---

## Using these matrices

These matrices are **starting points**, not fixed values. When token-specific or market-specific historical data is available, always prefer it over these generic estimates. Use these when:

- No historical data exists for a token (new issuance)
- The sport is not yet in the base platform's historical database
- You need a quick sanity check on whether a signal magnitude is plausible

The `get_price_correlation` and `get_match_impact` commands from the sports-data skill return token-specific historical values that should override these estimates.

---

## Baseball (MLB)

Note: No active MLB fan token as of Q1 2026. Included for prediction market and
analytics agent use. Token impact ranges are estimates for when MLB tokens launch.

| Result / Event | Signal impact |
|---|---|
| Regular season win (standard) | Low — 1 of 162; never overweight single game |
| Ace starts (ERA < 3.00) vs weak rotation | High — pitching quality mismatch is strongest signal |
| Winning streak (7+ games) | Elevated form signal; rotation and bullpen healthy |
| Wild Card Series win (sweep) | Significant — ace preserved for Division Series |
| Division Series win | Strong (especially if ace-preserved) |
| World Series win | Maximum narrative — highest token event when tokens exist |
| No-hitter / perfect game | Extraordinary individual event; viral signal |
| Ace on 60-day IL | Most significant negative single event for team outlook |
| Elite trade deadline acquisition | August-September form improvement signal |

---

## Ice Hockey (NHL)

| Result / Event | Token impact |
|---|---|
| Regular season win (standard) | +2–4% |
| Playoff series win (Round 1) | +8–15% |
| Conference Finals win | +15–25% |
| Stanley Cup win | +25–50% |
| Top goaltender injured (IR) | -15–30% |
| Back-to-back backup starting | Opponent +8–15% |

---

## MotoGP

| Result / Event | Token impact |
|---|---|
| Race win | +8–18% |
| World Championship clinch | +25–50% |
| Home GP win | +12–22% |
| DNF / crash (leading rider) | -10–25% |
| Serious injury (season-altering) | -20–40% |
| Factory contract signed | +10–20% |

---

## AFL

| Result / Event | Token impact |
|---|---|
| Regular season win | +3–7% |
| Finals win (any round) | +8–18% |
| Grand Final win | +30–55% |
| Key forward injury (season-ending) | -15–30% |

---

## Handball

| Result / Event | Token impact |
|---|---|
| EHF FINAL4 / Champions League win | +20–40% |
| World Championship win | +25–45% |
| Domestic league title | +8–15% |
| Key player injury | -10–22% |

---

## Kabaddi (PKL)

| Result / Event | Token impact |
|---|---|
| PKL match win | +3–6% |
| PKL Final win | +25–45% |
| Star raider Super 10 milestone | +5–10% social signal |
| Star raider injury (season-ending) | -20–35% |

---

## NASCAR

| Result / Event | Token impact |
|---|---|
| Daytona 500 win | +25–50% |
| Regular season race win | +8–18% |
| Championship win | +30–55% |
| Playoff elimination | -15–30% |
