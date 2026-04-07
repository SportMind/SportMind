---
name: athlete-social-activity
description: >
  Comprehensive athlete social media intelligence skill covering content strategy,
  audience growth, sentiment trends, brand voice consistency, platform performance,
  crisis detection, and influence network mapping. Use this skill when the user asks
  about an athlete's social media presence, wants to analyse content performance,
  asks what an athlete is posting about, wants to understand their audience demographics,
  asks whether an athlete's social activity is growing or declining, wants to detect
  PR risks or reputation signals early, asks about an athlete's personal brand narrative,
  wants to map who influences or is influenced by this athlete, or needs a social
  health audit. Broader than athlete-social-lift (which focuses only on token correlation)
  — this skill covers the full social intelligence picture. Feeds athlete-social-lift,
  brand-score, and sports-brand-sponsorship.
---

# Athlete Social Activity

Full social media intelligence for an athlete — content, audience, sentiment, influence
networks, and brand narrative. The complete picture of an athlete's digital presence
beyond just token correlation.

## What this skill produces

- **Social Health Score (SHS)** — Overall social presence quality (0–100)
- **Audience Growth Index (AGI)** — Trajectory of following across platforms
- **Content Mix Analysis** — What is the athlete posting, and what works?
- **Brand Voice Profile** — Consistent themes, tone, values in their content
- **Sentiment Trend** — Fan sentiment over 30/90/365 days
- **Influence Network Map** — Key accounts amplifying or being amplified
- **Crisis Early Warning** — Negative sentiment spikes, reputation risk flags
- **Platform Recommendations** — Where to focus for maximum impact

---

## Data sources

### Social platforms
- **X (Twitter) API v2**: posts, engagement, follower counts, mentions
- **Instagram Graph API**: posts, stories highlights, reels, reach, impressions
- **TikTok Research API**: videos, views, engagement, audience demographics
- **YouTube Data API v3**: videos, views, subscribers, watch time
- **Facebook Graph API** (where relevant, older demographics)

### Audience intelligence
- **SparkToro** (if available): audience demographic profiling from social signals
- **Social Blade** (public): growth tracking over time for major accounts
- Platform native analytics (where athlete/club shares access)

### Sentiment
- Twitter/X mentions and reply sentiment (NLP)
- YouTube comment sentiment
- Reddit mentions across r/soccer, sport subreddits, athlete fan communities
- Google Trends: search interest volume and related queries

---

## Workflow

### Step 1 — Platform inventory
For the named athlete, resolve and confirm active accounts on:
```
X/Twitter · Instagram · TikTok · YouTube · Facebook · Snapchat (if active)
```
Note: verified status, account age, follower count per platform.

### Step 2 — Social Health Score (SHS)
```
SHS = (
  total_reach_vs_peer_median   * 0.20 +   # raw audience size, position-normalised
  engagement_rate              * 0.25 +   # likes+comments+shares / followers
  posting_consistency          * 0.15 +   # posts per week, gaps flagged
  sentiment_ratio              * 0.25 +   # positive mentions / total mentions
  growth_trajectory_90d        * 0.15     # follower growth rate
) * 100
```

Engagement rate benchmarks by platform:
- Instagram: <1% weak, 1–3% good, 3–6% strong, >6% exceptional
- TikTok: <3% weak, 3–8% good, 8–15% strong, >15% exceptional
- X/Twitter: <0.5% weak, 0.5–1.5% good, 1.5–3% strong, >3% exceptional
- YouTube: <2% weak, 2–5% good, 5–10% strong, >10% exceptional

### Step 3 — Content Mix Analysis
Classify last 60 posts per platform into content types:

```
CONTENT TYPES:
  match_day        → pre/post match, goals, celebrations, dressing room
  training         → sessions, gym, tactical prep, pre-season
  lifestyle        → travel, food, family, leisure, fashion, home
  community        → charity, fan engagement, local/national causes
  commercial       → #ad, tagged brand, obvious sponsorship
  token_fan        → explicit Socios/fan token reference, holder shoutout
  milestone        → career achievements, records, awards
  personal         → opinion, humour, behind-the-scenes personality
  controversy      → any post generating significant negative response
```

Per content type: post count, avg engagement rate, avg reach.
Identify top 3 content types by engagement. Flag lowest performing.

### Step 4 — Brand Voice Profile
Extract consistent patterns across posts to define the athlete's brand voice:

```
DIMENSIONS:
  tone:       [professional / casual / humorous / inspirational / raw]
  themes:     [top 3–5 recurring topics/values]
  languages:  [primary + secondary — multilingual athletes have wider reach]
  visual:     [consistent aesthetic? colour palette? photographer signature?]
  narrative:  [what story does this athlete tell about themselves?]
```

Flag inconsistencies: commercial posts that feel out-of-character, content that
contradicts stated brand values, jarring topic shifts.

### Step 5 — Sentiment Trend Analysis
```
Pull all @mentions and comments for athlete across platforms, last 90 days.
Classify: positive / neutral / negative using NLP.
Track weekly sentiment ratio.
Flag:
  - Any week where negative ratio > 30% (elevated risk)
  - Any single day where negative mentions > 3× weekly average (crisis signal)
  - Topics driving negative sentiment (keyword clustering)
  - Topics driving positive sentiment (amplify these)
```

### Step 6 — Influence Network Map
Identify:
1. **Amplifiers**: accounts that consistently repost/quote this athlete
   - Tier: media outlets, fan accounts, fellow athletes, brands
2. **Key connections**: who does the athlete tag, collaborate with, mention?
3. **Emerging audience**: are younger/new demographics discovering this athlete?
4. **Crossover accounts**: athletes or creators shared by this athlete's audience

### Step 7 — Crisis Early Warning System

Flag any of the following for immediate human review:
```
⚠ IMMEDIATE: negative sentiment spike >400% above baseline in <6 hours
⚠ IMMEDIATE: trending hashtag containing athlete name + negative term
⚠ MONITOR:  multiple Tier 1 media accounts sharing negative story
⚠ MONITOR:  athlete post ratio drops to zero for >5 days (unusual silence)
⚠ MONITOR:  significant spike in unfollow rate
```

### Step 8 — Format output

```
ATHLETE SOCIAL ACTIVITY — [ATHLETE NAME]
Platforms: Instagram (12.4M) · TikTok (8.1M) · X (4.2M) · YouTube (890K)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Social Health Score (SHS):         79 / 100  [Strong presence]
Audience Growth Index (90d):        +8.4%    [Accelerating]
Dominant platform:                  Instagram (highest engagement rate: 4.2%)

CONTENT MIX (last 60 posts, Instagram):
  Match day          34%   Avg engagement: 6.1%  ← top performer
  Lifestyle          28%   Avg engagement: 3.8%
  Training           18%   Avg engagement: 2.9%
  Commercial         12%   Avg engagement: 1.4%  ← authenticity gap
  Token/fan           5%   Avg engagement: 5.2%  ← high for volume posted
  Community           3%   Avg engagement: 4.8%

BRAND VOICE PROFILE
  Tone:       Motivational with moments of personal warmth
  Core themes: Dedication, family loyalty, national pride, faith
  Languages:  Portuguese (primary), English (secondary — growing)
  Narrative:  "From humble origins to the world stage" — consistent and authentic
  Visual:     High-production, warm tones, professional photographer consistent

SENTIMENT TREND (90 days)
  Overall:    78% positive / 15% neutral / 7% negative
  Trend:      Stable-positive. No crisis events in window.
  Top positive drivers: Goal vs. [Rival], charity school announcement
  Watch area: Commercial posts receiving 2.3× more negative comments than organic

INFLUENCE NETWORK
  Top amplifiers: [Club official account], [National team account], [Sports media X]
  Notable connections: [Peer athlete A] (mutual amplification), [Brand Y]
  Emerging audience: +22% 18–24 TikTok followers in last 30 days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run athlete-social-lift to measure token holder correlation from this social data
→ Run sports-brand-sponsorship to match brand voice profile to sponsorship strategy
⚡ Opportunity: Token/fan content (5% of posts) driving 5.2% engagement — under-utilised
⚠ Monitor: Commercial content sentiment gap — audiences detecting inauthenticity
```

---

## Comparative squad analysis

When user asks "how does [athlete] compare to teammates on social?":
1. Run SHS for all named athletes
2. Return ranked table: SHS, dominant platform, top content type, growth rate
3. Flag who is over-indexing (more engagement than following would predict)
4. Flag who has the most untapped potential (high following, low engagement)

---

## Social calendar planning mode

When user asks for a content strategy or posting plan:
1. Use content mix analysis to identify highest-performing types
2. Map against fixture calendar (match-day posts reliably outperform)
3. Map against fan token calendar (polls, events — tie athlete content to holder moments)
4. Suggest optimal posting times based on platform audience geography
5. Flag upcoming milestone dates (caps record, contract anniversary, etc.)

---

## Reference files

- `../athlete-social-lift/references/social-platform-api-setup.md` — Auth and rate limits (shared with athlete-social-lift)
- `references/content-classifier-patterns.md` — NLP patterns for content classification *(planned)*
- `references/sentiment-lexicon-sports.md` — Sport-specific sentiment vocabulary *(planned)*
- `references/engagement-benchmarks.md` — Position and league-adjusted benchmarks *(planned)*

---

## Environment variables

```
X_BEARER_TOKEN=<key>
INSTAGRAM_ACCESS_TOKEN=<key>
TIKTOK_API_KEY=<key>
YOUTUBE_API_KEY=<key>
REDDIT_CLIENT_ID=<id>
REDDIT_CLIENT_SECRET=<secret>
SPARKTORO_API_KEY=<key>          # optional, audience intelligence
```
