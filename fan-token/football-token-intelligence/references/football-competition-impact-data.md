# Competition Impact Data — Football Fan Token™ Intelligence
# Calibrated FTIS and token impact data by competition type and club tier
# Updated: Q1 2026 | Source: Kayen DEX historical data, Socios Connect, match_price_correlation

---

## How to use this file

This file provides the calibrated data behind the Football Token Impact Score (FTIS).
Use it to set baseline expectations before running fan-token-pulse for live data.
Live data from fan-token-pulse always overrides these baselines.

---

## UCL Token Impact by Round — Historical Averages

Average HAS change and TVI spike by UCL round (across all active fan token clubs, 2022–2025):

| UCL round | Avg HAS change (advance) | Avg TVI spike | Peak window |
|---|---|---|---|
| Group stage match (win) | +4–7% HAS | +12–18 TVI | Match day + 24h |
| Group stage qualification | +8–12% HAS | +18–25 TVI | Night of qualification |
| Round of 16 win | +12–18% HAS | +22–30 TVI | Match day + 48h |
| Quarter-final win | +15–22% HAS | +28–38 TVI | Match day + 72h |
| Semi-final win | +20–30% HAS | +35–48 TVI | 5-day window |
| Final win | +30–50% HAS | +50–80 TVI | 7-day window |
| Group stage elimination | -8–15% HAS | -20–35 TVI | Immediate |
| Knockout elimination | -12–22% HAS | -25–45 TVI | Immediate to 48h |

### UCL variation by club token tier

Token impact is NOT equal across all clubs. Clubs with larger, more active token
ecosystems (higher baseline HAS) generate larger absolute moves.

| Club token HAS baseline | UCL QF win: expected HAS impact |
|---|---|
| HAS 75–100 (highly active) | +18–25% |
| HAS 55–74 (active) | +14–20% |
| HAS 40–54 (moderate) | +10–15% |
| HAS < 40 (low activity) | +6–12% |

---

## Domestic League Impact by Context

League matches require context to interpret correctly. The same result carries
very different token weight depending on table position and stakes.

| Context | HAS impact (win) | HAS impact (loss) |
|---|---|---|
| Top-of-table clash (both in top 4) | +6–10% | -5–9% |
| Title-clinching match | +12–20% | N/A (cannot clinch with loss) |
| Top 4 / UCL qualification clinch | +8–14% | N/A |
| Relegation-zone opponent (expected win) | +2–4% | -8–15% |
| Mid-table, low stakes | +1–3% | -2–5% |
| Last matchday (any scenario) | +3–6% (win) | -4–10% (if matters) |

---

## International Tournament Impact on National Tokens

### World Cup group stage — average national token movements

| Result | National token impact |
|---|---|
| Win (expected) | +5–10% |
| Win (upset) | +12–22% |
| Draw (needed win) | -4–8% |
| Loss (eliminated) | -18–35% |
| Qualification from group (confirmed) | +8–15% |
| Group stage exit | -20–40% |

### World Cup knockout — national token scale

| Round | Advance impact | Exit impact |
|---|---|---|
| Round of 16 win | +10–18% | -15–28% |
| Quarter-final win | +15–25% | -20–35% |
| Semi-final win | +22–35% | -18–30% |
| Final win | +30–60% | -15–25% (runner-up retains some sentiment) |

### Club token NCSI calibration — World Cup 2026

Expected HAS change for top-3 associated club token (per national team performance):

| National event | Club token expected HAS change |
|---|---|
| Nation wins group | +3–6% |
| Nation wins Round of 16 | +5–9% |
| Nation wins Quarter-Final | +7–13% |
| Nation wins Semi-Final | +10–18% |
| Nation wins World Cup | +15–30% |
| Nation exits at group stage | -3–7% |
| Nation exits at knockout round | -5–10% |

---

## Multi-Token Fixture Historical Impact

### Derby della Madonnina (ACM vs INTER) — historical averages 2022–2025

| Outcome | ACM impact | INTER impact |
|---|---|---|
| ACM win (home) | +8–13% | -5–9% |
| ACM win (away) | +10–16% | -7–12% |
| INTER win (home) | -4–8% | +9–14% |
| INTER win (away) | -6–10% | +11–17% |
| Draw | -2–4% both | |
| Pre-match correlation (30-day): | 0.58–0.68 | |

### PSG vs Marseille (PSG vs OM) — historical averages 2022–2025

| Outcome | PSG impact | OM impact |
|---|---|---|
| PSG win (expected) | +2–5% | -5–10% |
| OM upset win | -5–10% | +14–24% |
| Draw | -1–3% PSG | +3–7% OM (surprise positive for OM) |
| Pre-match correlation: | 0.35–0.48 | (lower — different holder bases) |

---

## Friendly and Pre-Season Impact Reference

### Summer signing debut premium — historical calibration

| Player tier (by ATM estimate) | Debut HAS impact | Peak window |
|---|---|---|
| ATM ≥ 1.20 (global elite) | +10–20% | Day of debut + 24h |
| ATM 0.80–1.19 (premium) | +5–12% | Day of debut + 12h |
| ATM 0.60–0.79 (strong) | +2–6% | Day of debut only |
| ATM < 0.60 | +0–2% | Negligible |

### Pre-season venue premium

| Venue/context | Additional HAS modifier |
|---|---|
| Iconic rival pre-season (e.g., PSG vs Barça) | +3–6% on match day |
| US / Asia pre-season tour (for European clubs) | +2–4% (new geographic holder acquisition) |
| Standard tour match (low-profile opponent) | +0–1% (noise level) |

---

## Seasonal Calendar — FTIS Timeline for a UCL Club (indicative)

This timeline shows when FTIS peaks across a season for a club active in UCL,
La Liga / Premier League / Serie A, and with an active fan token:

```
Jul–Aug   Pre-season:       FTIS 15–45 (debut premium events only)
Aug       Season opener:    FTIS 55–65 (first league match momentum)
Sep       UCL group opens:  FTIS 68–75 (UCL matchday 1)
Oct–Nov   Mid-season:       FTIS 52–68 (alternating UCL and league)
Dec       Derby period:     FTIS 70–80 (high-stakes league + UCL last group match)
Jan       Transfer window:  FTIS 45–65 (transfer signal elevated, on-pitch FTIS moderate)
Feb       UCL R16:          FTIS 80–88 (knockout entry — major elevation)
Mar       UCL QF:           FTIS 85–92
Apr       UCL SF:           FTIS 90–96
May       UCL Final:        FTIS 98–100
May       Domestic close:   FTIS 72–84 (title or top-4 race)
Jun       Off-season:       FTIS 20–40 (transfer narrative only)
Jun–Jul   World Cup window: FTIS 75–95 for national tokens (2026: exceptional)
```

---

## Token Decay Curve — How Long Does Impact Last?

After a major positive event, token HAS elevation decays on a predictable curve:

| Event type | Day 1 | Day 3 | Day 7 | Day 14 |
|---|---|---|---|---|
| UCL Final win | 100% | 85% | 60% | 35% |
| UCL knockout win | 100% | 70% | 40% | 20% |
| League title clinch | 100% | 80% | 55% | 30% |
| World Cup win (national) | 100% | 90% | 75% | 55% |
| Summer signing debut | 100% | 40% | 15% | 5% |
| Standard league win | 100% | 30% | 10% | 3% |

**Implication for agents:**
- UCL knockout and title events justify holding positions for 3–5 days
- World Cup wins sustain for 2+ weeks (longest decay curve in the ecosystem)
- Standard league wins require quick exit — signal fades rapidly
- Summer signing debuts are front-loaded — exit within 24h for maximum capture

---

*Data reflects observed token behaviour across active Chiliz Chain fan tokens 2022–2025.
Past patterns are calibration tools, not guaranteed predictors. Always validate
with live fan-token-pulse data before entering positions.*
