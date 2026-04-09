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

*SportMind v3.36 · MIT License · sportmind.dev*
*X API v2 docs: developer.twitter.com/en/docs/twitter-api*
*See also: fan-token/kol-influence-intelligence/ · fan-token/athlete-social-lift/*
*fan-token/fan-sentiment-intelligence/ · platform/memory-integration.md*
