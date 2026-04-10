# Social Intelligence Connector — SportMind

**X (Twitter) API v2 connector for feeding live social data into SportMind's
existing KOL influence, athlete social lift, and fan sentiment intelligence skills.**

SportMind already has the reasoning framework for social intelligence:
`fan-token/kol-influence-intelligence/`, `fan-token/athlete-social-lift/`,
and `fan-token/athlete-social-activity/` all define what social signals mean
and how they affect fan token commercial intelligence.

This connector is the data layer that feeds those frameworks — giving agents
live X API data formatted for direct input into SportMind's social skills.

---

## What this connector provides

```
KOL monitoring:
  → Real-time post tracking for identified Tier 1/2/3 KOLs
  → Engagement scoring per post (impressions, likes, retweets, replies)
  → Mindshare ranking: which accounts are driving CHZ/fan token conversation
  → Smart follower detection: high-signal follower identification

Crypto Twitter (CT) intelligence:
  → CHZ, fan token, and Chiliz Chain mention volume
  → Sentiment scoring on token-related posts
  → Trending hashtag detection (#ChilizChain, #FanTokens, #SportFi)

Fan token specific:
  → Token ticker mention tracking ($PSG, $BAR, $CITY etc.)
  → Athlete post monitoring → correlate with AELS (Athlete Engagement Lift Score)
  → Transfer rumour detection from verified journalists
  → Disciplinary news tracking → early signal before formal charge

1d / 7d / 30d trend analysis:
  → Mindshare trajectory for each token/club
  → Engagement rate trends (is reach growing or declining?)
  → Sentiment direction (net positive/negative momentum)
```

---

## X API v2 setup

```
1. Apply for API access:
   → https://developer.twitter.com/en/portal/dashboard
   → Free tier: 500,000 tweets/month read access
   → Basic tier ($100/month): 10M tweets/month — recommended for production

2. Create a project and app, then generate:
   → Bearer Token (for read-only access — sufficient for SportMind)
   → Store as environment variable: X_BEARER_TOKEN

3. Rate limits (free tier):
   → Search: 1 request per 15 seconds
   → Timeline: 5 requests per 15 minutes per user
   → Recent search: 1 request per second

Note: X API access and pricing have changed frequently.
Verify current terms at developer.twitter.com before building.
```

---

## Data connector

```python
# platform/connectors/social_intelligence.py
"""
X (Twitter) API v2 connector for SportMind social intelligence.
Feeds: kol-influence-intelligence, athlete-social-lift, fan-sentiment-intelligence

Requirements: pip install aiohttp python-dotenv
X Bearer Token: https://developer.twitter.com/en/portal/dashboard
"""
import aiohttp
import asyncio
from datetime import datetime, timezone, timedelta
from typing import Optional

X_API_BASE = "https://api.twitter.com/2"

# Fan token tickers for monitoring
FAN_TOKEN_TICKERS = [
    "$PSG", "$BAR", "$CITY", "$JUV", "$ACM", "$INTER", "$ATM",
    "$AFC", "$GAL", "$ASR", "$ARG", "$OG", "$TRA", "$BENFICA",
    "$UFC", "$MENGO", "$AVL", "$CHVS", "$SAN", "$AM", "$SAUBER",
    "$SHARKS", "$SARRIES", "$HASHTAG",
]

# Core CT KOL accounts to monitor (add verified accounts)
CORE_CT_ACCOUNTS = [
    "Chiliz",           # @Chiliz official
    "socios",           # @socios official
    "FanTokens",        # @FanTokens official
    # Add Tier 1 CT KOLs from kol-influence-intelligence/ skill
]

# Chiliz ecosystem hashtags
CHILIZ_HASHTAGS = [
    "#ChilizChain", "#FanTokens", "#SportFi", "#CHZ",
    "#Socios", "#SportMind",
]


class SocialIntelligenceConnector:
    """
    X API v2 connector for SportMind social intelligence layer.
    Produces data formatted for SportMind's KOL and social lift skills.
    """

    def __init__(self, bearer_token: str = ""):
        # Pass your X Bearer Token directly or load from your own config
        # Get token at: https://developer.twitter.com/en/portal/dashboard
        self.bearer_token = bearer_token
        self._session: Optional[aiohttp.ClientSession] = None

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.bearer_token}"}

    async def _get(self, endpoint: str, params: dict = {}) -> dict:
        if not self._session:
            self._session = aiohttp.ClientSession(headers=self._headers())
        try:
            async with self._session.get(
                f"{X_API_BASE}/{endpoint}",
                params=params,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                if resp.status == 200:
                    return await resp.json()
                elif resp.status == 429:
                    # Rate limited — wait 15 seconds
                    await asyncio.sleep(15)
                    return await self._get(endpoint, params)
                return {}
        except Exception:
            return {}

    async def search_recent(self, query: str, max_results: int = 100,
                             hours_back: int = 24) -> list:
        """
        Search recent tweets matching a query.
        Returns list of tweet objects with engagement metrics.
        """
        start_time = (
            datetime.now(timezone.utc) - timedelta(hours=hours_back)
        ).strftime("%Y-%m-%dT%H:%M:%SZ")

        data = await self._get("tweets/search/recent", {
            "query":        query + " lang:en -is:retweet",
            "max_results":  min(max_results, 100),
            "start_time":   start_time,
            "tweet.fields": "created_at,author_id,public_metrics,entities",
            "expansions":   "author_id",
            "user.fields":  "name,username,public_metrics,verified",
        })
        return data.get("data", [])

    async def get_token_mindshare(self, ticker: str,
                                   hours_back: int = 24) -> dict:
        """
        Mindshare analysis for a specific fan token ticker.
        Maps to SportMind's HAS and AELS framework inputs.
        """
        ticker_clean = ticker.lstrip("$")
        query = f"${ticker_clean} OR #{ticker_clean}FanToken"

        tweets = await self.search_recent(query, hours_back=hours_back)
        if not tweets:
            return {
                "ticker":        ticker,
                "mention_count": 0,
                "mindshare_tier": "SILENT",
                "sentiment":     "NEUTRAL",
            }

        # Engagement scoring
        total_likes     = sum(t.get("public_metrics", {}).get("like_count", 0)
                              for t in tweets)
        total_retweets  = sum(t.get("public_metrics", {}).get("retweet_count", 0)
                              for t in tweets)
        total_replies   = sum(t.get("public_metrics", {}).get("reply_count", 0)
                              for t in tweets)
        total_impressions = sum(t.get("public_metrics", {}).get("impression_count", 0)
                                for t in tweets)

        mention_count = len(tweets)

        # Mindshare tier (calibrated to typical fan token CT volume)
        if mention_count > 500:
            mindshare_tier = "VIRAL"
        elif mention_count > 200:
            mindshare_tier = "HIGH"
        elif mention_count > 50:
            mindshare_tier = "MODERATE"
        elif mention_count > 10:
            mindshare_tier = "LOW"
        else:
            mindshare_tier = "MINIMAL"

        # Simple sentiment proxy (engagement rate as positive proxy)
        engagement_rate = (
            (total_likes + total_retweets) / max(total_impressions, 1) * 100
        )
        sentiment = (
            "POSITIVE" if engagement_rate > 3.0 else
            "NEUTRAL"  if engagement_rate > 1.0 else
            "LOW_ENGAGEMENT"
        )

        return {
            "ticker":             ticker,
            "period_hours":       hours_back,
            "mention_count":      mention_count,
            "engagement": {
                "likes":          total_likes,
                "retweets":       total_retweets,
                "replies":        total_replies,
                "impressions":    total_impressions,
                "engagement_rate": round(engagement_rate, 3),
            },
            "mindshare_tier":     mindshare_tier,
            "sentiment_proxy":    sentiment,
            "sportmind_note": (
                "mindshare_tier feeds KOL influence intelligence. "
                "VIRAL/HIGH tiers extend CDI by up to 30%. "
                "See fan-token/kol-influence-intelligence/ for full framework."
            ),
        }

    async def get_ct_kol_activity(self, username: str,
                                   hours_back: int = 24) -> dict:
        """
        Activity summary for a specific CT KOL account.
        Feeds SportMind's KOL tier classification and HAS_spike detection.
        """
        tweets = await self.search_recent(
            f"from:{username}", hours_back=hours_back, max_results=50
        )

        fan_token_posts = [
            t for t in tweets
            if any(
                tag.lower() in t.get("text", "").lower()
                for tag in ["chiliz", "fantoken", "chz", "socios"] +
                           [t.lstrip("$").lower() for t in FAN_TOKEN_TICKERS]
            )
        ]

        return {
            "username":            username,
            "period_hours":        hours_back,
            "total_posts":         len(tweets),
            "fan_token_posts":     len(fan_token_posts),
            "is_active_in_ct":     len(fan_token_posts) > 0,
            "posts":               fan_token_posts[:5],  # Top 5 relevant posts
        }

    async def get_ecosystem_sentiment(self, hours_back: int = 24) -> dict:
        """
        Broad Crypto Twitter sentiment for the Chiliz/fan token ecosystem.
        Feeds SportMind macro social layer.
        """
        # Search for Chiliz ecosystem terms
        ecosystem_query = " OR ".join([
            "Chiliz", "#ChilizChain", "#FanTokens",
            "#SportFi", "fan token"
        ])

        tweets = await self.search_recent(
            ecosystem_query, max_results=100, hours_back=hours_back
        )

        # Token-specific mention counts
        token_mentions = {}
        for ticker in FAN_TOKEN_TICKERS:
            ticker_clean = ticker.lstrip("$")
            count = sum(
                1 for t in tweets
                if ticker_clean.lower() in t.get("text", "").lower() or
                   ticker.lower() in t.get("text", "").lower()
            )
            if count > 0:
                token_mentions[ticker] = count

        # Sort by mention count
        sorted_tokens = sorted(
            token_mentions.items(), key=lambda x: x[1], reverse=True
        )

        return {
            "period_hours":          hours_back,
            "ecosystem_tweet_count": len(tweets),
            "top_tokens_by_mention": dict(sorted_tokens[:10]),
            "total_tokens_mentioned":len(token_mentions),
            "generated_at":         datetime.now(timezone.utc).isoformat(),
            "sportmind_note": (
                "ecosystem_tweet_count feeds macro social modifier. "
                "token mention ranking indicates relative CT mindshare. "
                "See fan-token/fan-sentiment-intelligence/ for CDI framework."
            ),
        }

    async def get_mindshare_trend(self, ticker: str,
                                   windows: list = [1, 7, 30]) -> dict:
        """
        1d / 7d / 30d mindshare trend analysis for a token.
        """
        results = {}
        for days in windows:
            snapshot = await self.get_token_mindshare(ticker, hours_back=days * 24)
            results[f"{days}d"] = {
                "mentions":   snapshot.get("mention_count", 0),
                "tier":       snapshot.get("mindshare_tier", "MINIMAL"),
                "sentiment":  snapshot.get("sentiment_proxy", "NEUTRAL"),
            }

        # Calculate trend direction
        mentions_1d  = results.get("1d",  {}).get("mentions", 0)
        mentions_7d  = results.get("7d",  {}).get("mentions", 0)
        mentions_30d = results.get("30d", {}).get("mentions", 0)

        daily_avg_7d  = mentions_7d  / 7  if mentions_7d  else 0
        daily_avg_30d = mentions_30d / 30 if mentions_30d else 0

        trend = (
            "ACCELERATING" if mentions_1d > daily_avg_7d * 1.5 else
            "GROWING"      if mentions_1d > daily_avg_7d * 1.1 else
            "STABLE"       if mentions_1d > daily_avg_7d * 0.7 else
            "DECLINING"
        )

        return {
            "ticker":          ticker,
            "trend_direction": trend,
            "windows":         results,
            "sportmind_note": (
                f"Trend {trend}. "
                "Feeds KOL CDI extension model and HAS trajectory. "
                "ACCELERATING = potential KOL or event driver — investigate."
            ),
        }

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ──────────────────────────────────────────────────────────────

async def main():
    connector = SocialIntelligenceConnector()
    # bearer_token loaded from X_BEARER_TOKEN environment variable

    print("=== PSG Mindshare (24h) ===")
    psg = await connector.get_token_mindshare("$PSG", hours_back=24)
    import json
    print(json.dumps(psg, indent=2))

    print("\n=== Ecosystem sentiment ===")
    eco = await connector.get_ecosystem_sentiment(hours_back=24)
    print(json.dumps(eco, indent=2))

    print("\n=== PSG 1d/7d/30d trend ===")
    trend = await connector.get_mindshare_trend("$PSG", windows=[1, 7, 30])
    print(json.dumps(trend, indent=2))

    await connector.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Integration with SportMind skills

```
DATA FLOW:

get_token_mindshare()
  → mindshare_tier → feeds fan-token/kol-influence-intelligence/
  → engagement_rate → feeds fan-token/fan-sentiment-intelligence/ CDI model
  → VIRAL/HIGH tier → extend commercial duration signal

get_ct_kol_activity()
  → fan_token_posts → feeds KOL tier classification
  → is_active_in_ct → AELS (Athlete Engagement Lift Score) input

get_ecosystem_sentiment()
  → token_mentions ranking → macro social layer signal
  → ecosystem_tweet_count → broad CT activity baseline

get_mindshare_trend()
  → trend_direction → ACCELERATING = investigate for KOL driver
  → 1d/7d/30d comparison → CDI extension calculation

MEMORY MCP INTEGRATION:
  Store daily mindshare snapshots per token in memory
  Detect: "PSG mindshare ACCELERATING for 3 days — investigate driver"
  Cross-reference: mindshare acceleration + upcoming high-FTIS event = strong signal
```

---

## Smart follower detection framework

```
DEFINITION: Smart followers are accounts whose engagement with a fan token
post consistently precedes positive price moves within 24-72 hours.

IDENTIFICATION METHOD:
  1. Collect top 200 recent engagers on token-related posts
  2. For each account, check: did they engage BEFORE or AFTER the price moved?
  3. Score accounts: entries before price move = positive smart signal
  4. After 20+ data points: accounts with >60% pre-move engagement = smart follower

WHAT TO DO WITH SMART FOLLOWERS:
  → Monitor their own posts for token mentions
  → If smart follower posts about a token before an event:
    → Apply ×1.05 to commercial signal (informational advantage proxy)
  → If smart follower cluster (3+) posts about a token in 24h:
    → Apply ×1.10 to commercial signal; flag SMART_FOLLOWER_CONSENSUS

IMPORTANT LIMITATION:
  Smart follower detection requires historical data accumulation.
  First 30 days: insufficient data — use only with extreme caution.
  This is a pattern that develops over time via Memory MCP storage.
  See platform/memory-integration.md for storage schema.
```

---

## Source tier for social data

```
Apply SportMind's verifiable source tiers to social data:

TIER 1 (ground truth):
  Official club/team X accounts (@PSGofficial, @Arsenal etc.)
  Official Chiliz account (@Chiliz)
  Official Socios account (@socios)

TIER 2 (reliable):
  Verified sports journalists
  Established CT accounts with 3+ year track records
  
TIER 3 (usable with caution):
  Unverified CT accounts — corroborate before using as signal
  
TIER 4 (do not use as signal input):
  Anonymous accounts
  Accounts created within 30 days
  Accounts with engagement-to-follower ratio < 0.5%

Rule: Social data at Tier 3-4 is noise until corroborated by Tier 1-2.
Rule: Never override a DSM flag based solely on social sentiment.
```

---

## LunarCrush connector

LunarCrush is the recommended source for fan token Galaxy Score, cross-platform
social aggregation, and influencer identification. It complements the X API
connector — where X is better for real-time narrative tracking and journalist
monitoring, LunarCrush is better for pre-built composite scores, multi-platform
aggregation, and the structured influencer data that `kol-influence-intelligence/`
needs but the X API alone cannot provide.

LunarCrush is already referenced in eight SportMind sport domain files as the
recommended social sentiment source. This connector closes the loop.

---

### When to use LunarCrush vs X API

```
USE LUNARCRUSH WHEN:
  → You need a composite social score (Galaxy Score) for a fan token
  → You need cross-platform aggregation (X + Reddit + YouTube combined)
  → You need influencer identification with scoring for a specific asset
  → You need athlete social profile data across platforms
  → You need AltRank (relative social mindshare vs market)
  → The sport domain file references "LunarCrush galaxy score"

USE X API WHEN:
  → You need real-time narrative tracking (< 15 min latency)
  → You need journalist monitoring and transfer news velocity
  → You need specific hashtag or keyword volume
  → You need to track breaking news as it develops
  → You need the raw post content, not just aggregated scores
```

---

### LunarCrush API setup

```
Register:    https://lunarcrush.com/developers/api/authentication
Free tier:   Limited requests/day — sufficient for development and testing
Paid tiers:  Analyst ($29/mo), Pro ($99/mo) — for production monitoring

API base:    https://lunarcrush.com/api4/public
Auth:        Bearer token in header: Authorization: Bearer {your_key}

Key endpoints for SportMind:
  /coins/{coin}/v1          → Fan token Galaxy Score + social metrics
  /coins/list/v1            → All tracked crypto assets (find fan tokens)
  /coins/{coin}/influencers/v1  → Top influencers for a specific token
  /topic/{topic}/v1         → Social data for a topic/keyword
  /creators/{network}/{id}/v1   → Athlete/creator social profile
  /categories/list/v1       → Browse sports category
```

---

### Data connector

```python
# platform/connectors/lunarcrush_connector.py
"""
LunarCrush social intelligence connector for SportMind.
Feeds: kol-influence-intelligence, athlete-social-lift, fan-sentiment-intelligence

Covers:
  - Fan token Galaxy Score (composite social health metric)
  - AltRank (relative social mindshare ranking)
  - Cross-platform social aggregation (X, Reddit, YouTube)
  - Influencer identification and scoring
  - Athlete/creator social profiles

Requirements: pip install aiohttp
LunarCrush API: https://lunarcrush.com/developers/api/authentication
"""
import aiohttp
import asyncio
from datetime import datetime, timezone
from typing import Optional

LUNARCRUSH_BASE = "https://lunarcrush.com/api4/public"

# Fan token symbol mapping to LunarCrush coin IDs
# LunarCrush uses lowercase ticker or coin slug
# Verify at: https://lunarcrush.com/coins
FAN_TOKEN_LUNARCRUSH_MAP = {
    "PSG":     "paris-saint-germain-fan-token",
    "BAR":     "fc-barcelona-fan-token",
    "CITY":    "manchester-city-fan-token",
    "JUV":     "juventus-fan-token",
    "ACM":     "ac-milan-fan-token",
    "INTER":   "inter-milan-fan-token",
    "ATM":     "atletico-de-madrid-fan-token",
    "AFC":     "arsenal-fan-token",
    "GAL":     "galatasaray-fan-token",
    "ASR":     "as-roma-fan-token",
    "ARG":     "argentina-fan-token",
    "OG":      "og-fan-token",
    "UFC":     "ufc-fan-token",
    # Add others as LunarCrush coverage expands
    # Verify each slug at lunarcrush.com/coins before use
}


class LunarCrushConnector:
    """
    LunarCrush social intelligence connector for SportMind.
    Pass your API key directly — load from your own config/env.
    """

    def __init__(self, api_key: str = ""):
        # Get your key at: https://lunarcrush.com/developers
        self.api_key = api_key
        self._session: Optional[aiohttp.ClientSession] = None

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

    async def _get(self, endpoint: str, params: dict = {}) -> dict:
        if not self._session:
            self._session = aiohttp.ClientSession(headers=self._headers())
        try:
            async with self._session.get(
                f"{LUNARCRUSH_BASE}/{endpoint}",
                params=params,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                if resp.status == 200:
                    return await resp.json()
                elif resp.status == 429:
                    # Rate limited — back off
                    await asyncio.sleep(5)
                    return {}
                return {}
        except Exception:
            return {}

    async def get_token_galaxy_score(self, ticker: str) -> dict:
        """
        Galaxy Score and social metrics for a fan token.
        Maps to SportMind HAS and AELS framework inputs.

        Galaxy Score (0-100):
          > 70: strong social health — positive HAS signal
          50-70: moderate — neutral to positive
          30-50: low — monitor for decline
          < 30: weak — potential Phase 4 signal

        AltRank: relative ranking vs all crypto assets
          Lower = better (rank 1 = highest social activity)
          Rising AltRank (number increasing) = losing relative mindshare
          Falling AltRank (number decreasing) = gaining relative mindshare
        """
        slug = FAN_TOKEN_LUNARCRUSH_MAP.get(ticker.upper())
        if not slug:
            return {
                "ticker": ticker,
                "found":  False,
                "note":   f"Token {ticker} not in LunarCrush mapping. "
                          f"Verify slug at lunarcrush.com/coins and add to FAN_TOKEN_LUNARCRUSH_MAP."
            }

        data = await self._get(f"coins/{slug}/v1")
        coin = data.get("data", {})
        if not coin:
            return {"ticker": ticker, "found": False, "slug": slug}

        galaxy_score = coin.get("galaxy_score", 0)
        alt_rank     = coin.get("alt_rank", 0)
        social_vol   = coin.get("social_volume_24h", 0)
        sentiment    = coin.get("average_sentiment", 0)    # 1-5 scale
        contributors = coin.get("social_contributors_24h", 0)

        # Map to SportMind HAS tier
        if galaxy_score >= 70:
            has_signal = "HIGH"
        elif galaxy_score >= 50:
            has_signal = "MODERATE"
        elif galaxy_score >= 30:
            has_signal = "LOW"
        else:
            has_signal = "WEAK"

        # Sentiment normalise to 0-1 (LunarCrush uses 1-5)
        sentiment_norm = (sentiment - 1) / 4 if sentiment else 0.5

        return {
            "ticker":         ticker,
            "found":          True,
            "slug":           slug,
            "galaxy_score":   galaxy_score,
            "has_signal":     has_signal,
            "alt_rank":       alt_rank,
            "social_volume_24h":     social_vol,
            "social_contributors_24h": contributors,
            "sentiment_normalised":  round(sentiment_norm, 3),
            "sentiment_raw":  sentiment,
            "sportmind_note": (
                f"Galaxy Score {galaxy_score} → HAS signal {has_signal}. "
                f"AltRank {alt_rank} (lower = higher relative mindshare). "
                f"Feeds fan-token/kol-influence-intelligence/ and fan-token/fan-sentiment-intelligence/."
            ),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    async def get_token_influencers(self, ticker: str,
                                     limit: int = 20) -> dict:
        """
        Top influencers for a fan token.
        Feeds SportMind KOL tier classification with real scored data.

        LunarCrush influencer scores reflect:
          - Follower count and growth
          - Engagement rate on crypto/sports content
          - Historical correlation with asset price movement

        Maps to SportMind KOL tiers:
          influencer_rank 1-50:  likely Tier 1 (>500K engaged)
          influencer_rank 51-200: likely Tier 2 (50K-500K)
          influencer_rank 200+:  Tier 3 — monitor but do not modify signal
        """
        slug = FAN_TOKEN_LUNARCRUSH_MAP.get(ticker.upper())
        if not slug:
            return {"ticker": ticker, "found": False}

        data = await self._get(f"coins/{slug}/influencers/v1",
                                {"limit": limit})
        influencers = data.get("data", [])

        processed = []
        for inf in influencers:
            processed.append({
                "id":              inf.get("id", ""),
                "display_name":    inf.get("display_name", ""),
                "network":         inf.get("network", ""),
                "follower_count":  inf.get("followers", 0),
                "engagement_rate": inf.get("engagement_rate", 0),
                "influencer_rank": inf.get("influencer_rank", 999),
                "kol_tier_est":    (
                    "TIER_1" if inf.get("influencer_rank", 999) <= 50
                    else "TIER_2" if inf.get("influencer_rank", 999) <= 200
                    else "TIER_3"
                ),
            })

        return {
            "ticker":      ticker,
            "found":       True,
            "influencers": processed,
            "total":       len(processed),
            "sportmind_note": (
                "Tier 1 influencers (rank ≤50) apply full KOL modifier. "
                "Tier 2 (rank 51-200) apply 0.7x confidence weight. "
                "See fan-token/kol-influence-intelligence/ for full framework."
            ),
        }

    async def get_topic_social_score(self, topic: str) -> dict:
        """
        Social data for a topic/sport keyword.
        Useful for sports without dedicated fan tokens.
        e.g. topic = "MMA", "Formula 1", "cricket", "PSG"
        """
        data = await self._get(f"topic/{topic}/v1")
        topic_data = data.get("data", {})
        if not topic_data:
            return {"topic": topic, "found": False}

        return {
            "topic":           topic,
            "found":           True,
            "galaxy_score":    topic_data.get("galaxy_score", 0),
            "social_volume_24h": topic_data.get("social_volume_24h", 0),
            "sentiment":       topic_data.get("average_sentiment", 0),
            "posts_created":   topic_data.get("posts_created_24h", 0),
            "interactions":    topic_data.get("interactions_24h", 0),
            "sportmind_note":  (
                f"Topic '{topic}' social health. Useful for sports domain files "
                f"that reference 'LunarCrush galaxy score' as a signal input."
            ),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    async def get_athlete_social_profile(self, creator_id: str,
                                          network: str = "twitter") -> dict:
        """
        Social profile for an athlete/creator across platforms.
        Feeds AELS (Athlete Engagement Lift Score) calculation.

        network options: twitter, youtube, tiktok, reddit, instagram

        Returns engagement metrics that feed:
          fan-token/athlete-social-lift/ → AELS
          fan-token/athlete-social-activity/ → SHS, AGI
        """
        data = await self._get(f"creators/{network}/{creator_id}/v1")
        creator = data.get("data", {})
        if not creator:
            return {"creator_id": creator_id, "network": network, "found": False}

        followers      = creator.get("followers", 0)
        posts_24h      = creator.get("posts_created_24h", 0)
        engagement_24h = creator.get("engagement_24h", 0)
        avg_engagement = engagement_24h / max(posts_24h, 1)
        engagement_rate = avg_engagement / max(followers, 1) * 100

        # Map to AELS tier
        if engagement_rate > 3.0 and followers > 500000:
            aels_tier = "TIER_1_HIGH"
        elif engagement_rate > 1.5 and followers > 50000:
            aels_tier = "TIER_2_MODERATE"
        else:
            aels_tier = "TIER_3_LOW"

        return {
            "creator_id":       creator_id,
            "network":          network,
            "found":            True,
            "display_name":     creator.get("display_name", ""),
            "followers":        followers,
            "posts_24h":        posts_24h,
            "engagement_24h":   engagement_24h,
            "engagement_rate":  round(engagement_rate, 3),
            "aels_tier":        aels_tier,
            "sportmind_note": (
                f"Engagement rate {engagement_rate:.2f}% → AELS tier {aels_tier}. "
                f"Feeds fan-token/athlete-social-lift/ AELS calculation. "
                f"See fan-token/athlete-social-activity/ for full SHS framework."
            ),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    async def get_portfolio_social_snapshot(self,
                                             tickers: list) -> dict:
        """
        Galaxy Score snapshot across a portfolio of fan tokens.
        One call to rank all held tokens by current social health.
        Feeds portfolio-monitor.py social layer.
        """
        results = []
        for ticker in tickers:
            score = await self.get_token_galaxy_score(ticker)
            results.append(score)
            await asyncio.sleep(0.5)   # Respect rate limits

        # Sort by galaxy score descending
        found = [r for r in results if r.get("found")]
        not_found = [r for r in results if not r.get("found")]
        found.sort(key=lambda x: x.get("galaxy_score", 0), reverse=True)

        return {
            "portfolio":     found + not_found,
            "total_tokens":  len(tickers),
            "found":         len(found),
            "top_token":     found[0]["ticker"] if found else None,
            "top_score":     found[0]["galaxy_score"] if found else 0,
            "generated_at":  datetime.now(timezone.utc).isoformat(),
        }

    async def close(self):
        if self._session:
            await self._session.close()


# ── Usage example ──────────────────────────────────────────────────────────────

async def main():
    # Pass your LunarCrush API key directly
    # Get key at: https://lunarcrush.com/developers
    lc = LunarCrushConnector(api_key="your_key_here")

    print("=== PSG Galaxy Score ===")
    score = await lc.get_token_galaxy_score("PSG")
    import json
    print(json.dumps(score, indent=2))

    print("\n=== Portfolio snapshot ===")
    snapshot = await lc.get_portfolio_social_snapshot(["PSG", "BAR", "CITY"])
    print(json.dumps(snapshot, indent=2))

    print("\n=== MMA topic score ===")
    topic = await lc.get_topic_social_score("MMA")
    print(json.dumps(topic, indent=2))

    await lc.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

### Galaxy Score → SportMind modifier mapping

```
GALAXY SCORE → HAS SIGNAL → COMMERCIAL MODIFIER:

Score 70–100 (STRONG):
  HAS signal: HIGH
  Commercial modifier: ×1.08
  Agent action: Full ENTER eligible (subject to other checks)

Score 50–69 (MODERATE):
  HAS signal: MODERATE
  Commercial modifier: ×1.03
  Agent action: ENTER eligible with normal confidence

Score 30–49 (LOW):
  HAS signal: LOW
  Commercial modifier: ×0.97
  Agent action: Note but do not reduce signal unless sustained < 30

Score 0–29 (WEAK):
  HAS signal: WEAK
  Commercial modifier: ×0.90
  Agent action: Flag for lifecycle Phase 4 drift investigation
  Check: holder count trend for 14 days; if declining → Phase 4 signal confirmed

ALTRANK DIRECTION SIGNAL:
  AltRank falling (number decreasing over 7d): +0.02 modifier (gaining mindshare)
  AltRank rising (number increasing over 7d):  -0.02 modifier (losing mindshare)
  AltRank stable:                               ×1.00 (neutral)

COMBINATION RULE:
  Always apply Galaxy Score modifier AFTER macro and DSM modifiers.
  Social intelligence is an amplifier on a clean signal, not a gate.
  Never use Galaxy Score to override ABSTAIN decisions.
```

---

### Non-fan-token sport use cases

```
For sports where no fan token exists, LunarCrush topic scores
provide the social sentiment signal that domain files reference.

USAGE BY SPORT (matches existing domain file references):

Football (general):
  lc.get_topic_social_score("football")
  lc.get_topic_social_score("premier league")
  lc.get_topic_social_score("champions league")

MMA / UFC:
  lc.get_topic_social_score("UFC")
  lc.get_topic_social_score("MMA")
  lc.get_athlete_social_profile("athlete_twitter_handle", "twitter")

Formula 1:
  lc.get_topic_social_score("Formula 1")
  lc.get_athlete_social_profile("driver_handle", "twitter")

Golf:
  lc.get_topic_social_score("PGA Tour")
  lc.get_athlete_social_profile("golfer_handle", "twitter")

Esports:
  lc.get_topic_social_score("CS2")
  lc.get_topic_social_score("League of Legends")
  Per-org token if available: get_token_galaxy_score("OG")

Boxing:
  lc.get_topic_social_score("boxing")
  lc.get_athlete_social_profile("fighter_handle", "twitter")

RULE: Use topic scores for sports without fan tokens.
      Use get_token_galaxy_score() for all 24 registry tokens.
      Use get_athlete_social_profile() for individual athlete AELS.
```

---

### Connector selection guide

```
SCENARIO → CONNECTOR → METHOD

"What is the social health of $PSG right now?"
  → LunarCrush → get_token_galaxy_score("PSG")

"Who are the top influencers talking about $BAR?"
  → LunarCrush → get_token_influencers("BAR")

"What is the social score for MMA this week?"
  → LunarCrush → get_topic_social_score("MMA")

"What is [athlete] posting about right now?"
  → X API → get_ct_kol_activity(username)

"Is there a breaking transfer rumour about [player]?"
  → X API → search_recent(query="[player] transfer")

"What is the mindshare trend for $PSG over 1d/7d/30d?"
  → X API → get_mindshare_trend("$PSG") for narrative detail
  → LunarCrush → get_token_galaxy_score("PSG") for composite score

"Rank my portfolio by social health"
  → LunarCrush → get_portfolio_social_snapshot(tickers)

"Is there a viral KOL post about $CITY in the last 2 hours?"
  → X API → search_recent() — LunarCrush latency too slow for this
```

---

*LunarCrush API docs: lunarcrush.com/developers/api*
*Rate limits vary by plan — verify current limits at lunarcrush.com/pricing*
*Fan token slugs: verify each at lunarcrush.com/coins before use in production*

---

*SportMind v3.42 · MIT License · sportmind.dev*
*X API v2: developer.twitter.com/en/docs/twitter-api*
*LunarCrush API: lunarcrush.com/developers/api*
*See also: fan-token/kol-influence-intelligence/ · fan-token/athlete-social-lift/*
*fan-token/fan-sentiment-intelligence/ · platform/memory-integration.md*
