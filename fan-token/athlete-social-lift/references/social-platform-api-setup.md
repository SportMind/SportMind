# Social API Setup — athlete-social-lift

## X (Twitter) API v2
- Apply for Elevated access at: https://developer.twitter.com/en/portal
- Required permissions: Read (tweet.read, users.read)
- Rate limits: 500k tweets/month on Basic; 10M on Pro
- Key endpoint: GET /2/users/:id/tweets
  - Fields: id,text,created_at,public_metrics,entities
  - tweet.fields=created_at,public_metrics
  - max_results=100 per request

## Instagram Graph API
- Requires Facebook Developer App + Instagram Business/Creator account
- Permission: instagram_basic, pages_read_engagement
- Endpoint: GET /{user-id}/media?fields=timestamp,like_count,comments_count,impressions,reach
- Note: impressions/reach require instagram_manage_insights permission (business accounts only)

## TikTok Research API
- Apply at: https://developers.tiktok.com/products/research-api/
- Academic/research tier available; commercial requires business account
- Rate limit: 1000 requests/day on research tier

## YouTube Data API v3
- Enable at: https://console.cloud.google.com/
- Quota: 10,000 units/day (free tier)
- Endpoint: GET /youtube/v3/search?channelId={id}&type=video&order=date&maxResults=50
- Then: GET /youtube/v3/videos?id={ids}&part=statistics,snippet

## Rate limit handling
All social APIs have rate limits. Recommended pattern:
1. Cache athlete social handles on first lookup (avoid repeated user resolution)
2. Cache post data for 1 hour (posts don't change rapidly)
3. Implement exponential backoff on 429 responses
4. For large squad analyses (20+ athletes), batch requests across a 10-minute window
