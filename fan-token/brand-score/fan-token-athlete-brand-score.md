---
name: brand-score
description: >
  Synthesises fan token ecosystem data, social lift, and transfer intelligence into a
  single Athlete Brand Score (ABS) and exportable commercial brief. Use this skill when
  the user wants to know an athlete's commercial value, asks "what is [player] worth as
  a brand?", wants a contract negotiation brief, asks how to quantify an athlete's fanbase
  as an asset, wants a sponsorship readiness score, asks for a player's commercial profile,
  or needs a summary report for an agent or club decision-maker. This is the synthesis
  skill — it always needs fan-token-pulse and should ideally have athlete-social-lift and
  transfer-signal outputs too. Produces the definitive SportMind commercial intelligence
  brief for an athlete.
---

# Brand Score

Synthesises all SportMind signal layers into the **Athlete Brand Score (ABS)** — a
single, defensible commercial metric designed for use in contract negotiations, sponsorship
pitches, and player acquisition decisions.

## What this skill produces

- **ABS** — Athlete Brand Score (0–100): composite commercial brand value
- **Component breakdown** — Transparent sub-scores for each input dimension
- **Peer comparison** — Where does this athlete rank vs. positional peers in their league?
- **Commercial brief** — Exportable 1-page summary for agent or club use
- **Trend signal** — Is the brand growing, stable, or declining?
- **Key leverage insight** — The single most actionable finding for this athlete

---

## Prerequisites (in order of importance)

| Skill | Status | Impact if missing |
|-------|--------|-------------------|
| `fan-token-pulse` | Required | Cannot compute ABS without token baseline |
| `athlete-social-lift` | Strongly recommended | AELS estimated from proxies if absent |
| `transfer-signal` | Recommended | APS estimated if not run; TSI context unavailable |

If prerequisites are missing, compute ABS with available data and flag confidence level:
- All three run: High confidence
- fan-token-pulse + one other: Medium confidence
- fan-token-pulse only: Low confidence (estimated)

---

## ABS Formula

```
ABS = (
  HAS  * 0.25 +   # Fan token ecosystem health (from fan-token-pulse)
  AELS * 0.25 +   # Social→token conversion (from athlete-social-lift)
  APS  * 0.20 +   # Portability / transferable audience (from transfer-signal)
  REACH * 0.15 +  # Normalised social following vs. league median
  SENTI * 0.15    # Sentiment stability score (consistency over 90 days)
) → raw score mapped to 0–100 band
```

### Component computation when source skill not run

**AELS proxy** (if athlete-social-lift not run):
```
AELS_proxy = log10(total_followers_all_platforms) / log10(100_000_000) * 60
# Caps at 60 to reflect absence of actual correlation data — never full score from proxy
```

**APS proxy** (if transfer-signal not run):
```
APS_proxy = (
  global_following_vs_league_median * 0.5 +
  club_has_active_token * 0.3 +
  athlete_nationality_in_top_holder_countries * 0.2
) * 70  # Capped at 70 without actual cross-holder and portability data
```

**REACH score:**
```
REACH = (
  (ig_followers + x_followers + tiktok_followers) / league_median_combined
) clamped to 0–100
```
League median combined followers (approximate, update annually):
- Premier League: 4.2M
- La Liga: 6.1M
- Serie A: 3.8M
- Bundesliga: 3.2M
- Ligue 1: 3.5M

**SENTI (Sentiment Stability):**
Pull 90 days of social sentiment (positive ratio from X and Instagram comment analysis).
```
SENTI = avg_positive_ratio * 100 - volatility_penalty
volatility_penalty = std_dev(weekly_sentiment_scores) * 20
# Erratic sentiment hurts brand value even if average is high
```

---

## ABS bands and interpretation

| Band | Score | Interpretation |
|------|-------|----------------|
| Elite | 80–100 | Top 5% commercial asset. Transformational signing for any club's token |
| Premium | 65–79 | Strong commercial profile. Meaningful sponsor and token value |
| Mid-market | 50–64 | Solid base. Specific niches or regions of high value |
| Developing | 35–49 | Growing brand. Value in trajectory, not current score |
| Early-stage | 0–34 | Limited commercial profile. Token impact marginal |

---

## Peer comparison

1. Pull ABS scores for all players at same position (or nearest equivalent) in same league
2. Rank the athlete and return:
   - Percentile rank (e.g. "top 12% of midfielders in La Liga")
   - Top 3 comparators with their ABS
   - Gap analysis: which component is most below peer average?

---

## Trend signal

Compute ABS at three points: 90 days ago, 30 days ago, today.
```
if ABS_now > ABS_30d > ABS_90d → "Rising brand (+X points in 90 days)"
if ABS_now < ABS_30d < ABS_90d → "Declining brand (-X points in 90 days)"
else → "Stable brand (±X points in 90 days)"
```
Trend is often more valuable to an agent than the absolute score.

---

## Commercial brief output

The brief is a structured, exportable document designed for a sports agent or club
decision-maker. It contains no jargon — written for an executive audience.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPORTMIND COMMERCIAL BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Athlete:       [Name]
Current club:  [Club] ([Token])
Position:      [Position]
Report date:   [Date]
Confidence:    High / Medium / Low
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ATHLETE BRAND SCORE (ABS):  76 / 100  [Premium]
Trend: Rising (+8 points in 90 days)
Peer rank: Top 18% of forwards in Premier League

COMPONENT BREAKDOWN:
  Fan Token Ecosystem (HAS):   74  Token holders active, voting above avg
  Social→Token Lift (AELS):    81  Instagram posts reliably move token holders
  Portability Score (APS):     68  Strong transferable audience
  Social Reach (REACH):        72  2.1× above league median
  Sentiment Stability (SENTI): 65  Consistently positive, low volatility

KEY COMMERCIAL INSIGHT:
  [Athlete]'s Instagram match posts drive measurable fan token engagement
  within 2–3 hours. A club signing this athlete gains an estimated +8–12
  point HAS boost in the first 60 days, based on comparable transfers.

FANBASE GEOGRAPHY (top 5):
  Brazil 28% · Spain 18% · UK 14% · Nigeria 9% · Japan 7%

SUGGESTED COMMERCIAL ANGLES:
  1. South American market activation (28% Brazilian holder base)
  2. Athletic performance / sportswear (engagement strongest in match content)
  3. Global fan engagement campaign leveraging token holder community

COMPARABLE ATHLETES:
  [Peer A]  ABS: 79  [slight premium — 2 years older, established global brand]
  [Peer B]  ABS: 71  [similar profile, lower social reach]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated by SportMind · Data sources: Chiliz Chain, Socios Connect API,
X API v2, Instagram Graph API · [Timestamp]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Export formats

When the user asks for an exportable brief:
- Plain text (default): formatted as above
- If docx skill available: trigger docx skill with brief content → professional Word doc
- If pdf skill available: trigger pdf skill → signed PDF with SportMind branding

---

## Reference files

- `references/social-following-league-medians.md` — Social following and HAS medians by league and position
- `references/abs-validation.md` — Historical ABS calibration against actual transfer fees
  and sponsorship deals (where public data available)
- `references/brief-template.md` — Extended brief template with additional sections

---

## Environment variables

Inherits all env vars from prerequisite skills. No additional requirements.
