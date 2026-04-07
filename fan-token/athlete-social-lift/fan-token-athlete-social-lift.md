---
name: athlete-social-lift
description: >
  Measures whether an athlete's social media activity is driving measurable fan token
  holder responses. Use this skill when the user asks whether a player's posts affect
  token engagement, wants to know a player's social influence on their club's fan token
  ecosystem, asks for an engagement lift score, asks "does [player] move the needle on
  token holders", wants to compare which players drive the most token activity, or needs
  social ROI for an athlete. Always requires fan-token-pulse to have run first for the
  relevant club. Produces the Athlete Engagement Lift Score (AELS) — a key input to
  brand-score and sponsorship-match.
---

# Athlete Social Lift

Measures the causal relationship between an athlete's social media posts and fan token
holder behaviour. Produces the **Athlete Engagement Lift Score (AELS)** — the quantified
value of an athlete's social presence to their club's token ecosystem.

## What this skill produces

- **AELS** — Athlete Engagement Lift Score (0–100): does this athlete's social activity
  measurably move token holder behaviour?
- **Lag profile** — How quickly does token holder response follow a post? (minutes to hours)
- **Platform breakdown** — Which social channel (X, Instagram, TikTok, YouTube) drives
  the strongest token response?
- **Content type analysis** — Match posts vs. lifestyle vs. transfer hints vs. token
  references — which resonates most?
- **Authenticity signal** — Organic vs. sponsored content response differential

---

## Prerequisites

Run `fan-token-pulse` first for the relevant club. This skill needs:
- Club baseline HAS (to measure lift *above* baseline)
- Club TVI over the measurement window (to isolate athlete-driven moves)

---

## Data sources

### Social APIs (public/authenticated)
- **X (Twitter) API v2** — posts, engagement metrics, timestamp
  - `GET /2/users/{id}/tweets` with `tweet.fields=created_at,public_metrics`
- **Instagram Graph API** — posts, impressions, reach, engagement
  - `GET /{user-id}/media` — requires `instagram_basic` permission
- **TikTok Research API** — for public accounts
- **YouTube Data API v3** — `GET /youtube/v3/search` for channel posts

### Token response measurement window
Default: measure token holder activity 0–6 hours post-post.
Extended: 0–24 hours for major content (transfer announcements, goal celebrations).

---

## Workflow

### Step 1 — Build athlete social profile
1. Resolve athlete name to social handles across platforms
2. Fetch last 30 posts per platform (or configurable window)
3. For each post: timestamp, platform, content type, engagement metrics
   (likes, shares, comments, impressions if available)

**Content type classifier:**
```
"match"        → contains match score, celebration, opponent mention
"training"     → gym, training ground, pre-match
"lifestyle"    → personal, family, travel, fashion
"token/fan"    → explicitly mentions Socios, fan token, CHZ, holder vote
"transfer"     → club change hints, goodbye/hello posts, contract language
"sponsor"      → tagged brand, #ad, #sponsored
```

### Step 2 — Fetch token holder behaviour windows
For each athlete post:
1. Record post timestamp `T`
2. Pull token data at `T-1h` (baseline), `T+1h`, `T+3h`, `T+6h`, `T+24h`
3. Measure: holder count delta, TVI delta, poll participation if active

### Step 3 — Compute per-post lift
```
post_lift = (
  tvi_at_T+3h - tvi_baseline +
  holder_delta_rate * normalisation_factor
)
```
Filter out posts where CHZ market moved >3% in the same window (market noise).

### Step 4 — Compute AELS
```
AELS = weighted_average(post_lifts) * reach_multiplier * authenticity_factor

where:
  reach_multiplier = log10(avg_post_impressions) / log10(10_000_000)  # 10M = max 1.0
  authenticity_factor = 1.0 for organic, 0.65 for sponsored
```

AELS bands:
- 80–100: Elite influence — posts reliably move token holders
- 60–79: Strong influence — consistent positive correlation
- 40–59: Moderate — some correlation, inconsistent
- 20–39: Low — minimal measurable token impact
- 0–19: Negligible — no detectable signal

### Step 5 — Platform and content breakdown
Compute AELS separately per platform and per content type.
Identify the athlete's highest-leverage channel and content category.

### Step 6 — Format output

```
ATHLETE SOCIAL LIFT — [ATHLETE NAME] @ [CLUB] ([TOKEN_SYMBOL])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Athlete Engagement Lift Score (AELS):  73 / 100  [Strong influence]
Posts analysed:  38 posts over 30 days
Avg response lag:  2.4 hours to peak token response

Platform breakdown:
  Instagram    AELS: 81  [highest leverage channel]
  X/Twitter    AELS: 64
  TikTok       AELS: 58

Content type breakdown:
  Match posts         AELS: 88  ← strongest
  Token/fan content   AELS: 79
  Lifestyle           AELS: 51
  Sponsored           AELS: 34  ← authenticity discount applied

Key insight: [Athlete]'s Instagram match posts drive a +14 TVI spike
within 2–3 hours. Organic content outperforms sponsored 2.3× in
token holder response.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run brand-score to synthesise AELS with portability and reach data
→ Run sponsorship-match to align content strengths with brand categories
```

---

## Comparing multiple athletes at a club

If the user asks "which players drive the most token engagement at [club]":
1. Fetch social data for all squad members with active public profiles
2. Run AELS computation for each
3. Return ranked table with top 5 and their primary leverage channels
4. Flag if any player's AELS is pulling *down* sentiment (negative lift cases)

---

## Reference files

- `references/social-platform-api-setup.md` — API authentication and rate limit guidance
- `references/content-classifier.md` — Detailed content type classification patterns
- `references/lift-calibration.md` — AELS calibration data by position and league tier

---

## Environment variables

```
X_BEARER_TOKEN=<twitter_api_v2_bearer>
INSTAGRAM_ACCESS_TOKEN=<instagram_graph_token>
YOUTUBE_API_KEY=<youtube_data_api_v3_key>
TIKTOK_API_KEY=<tiktok_research_api_key>   # optional
```
