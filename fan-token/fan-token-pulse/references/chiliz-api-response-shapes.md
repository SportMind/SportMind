# API Response Shapes — fan-token-pulse

Reference for parsing API responses from each data source.

---

## Kayen Token Registry
`GET https://api.kayen.finance/v1/tokens?chain=chiliz`

```json
[
  {
    "address": "0x5C7B3A9f2E6d4C8b1A5f3E9d7C2b6A4f8E1d5C3b",
    "symbol": "BAR",
    "name": "FC Barcelona Fan Token",
    "decimals": 2,
    "club": {
      "name": "FC Barcelona",
      "league": "La Liga",
      "country": "Spain",
      "logo_url": "https://cdn.kayen.finance/logos/bar.png"
    },
    "circulating_supply": "40000000",
    "max_supply": "40000000"
  }
]
```

---

## Kayen Market Data
`GET https://api.kayen.finance/v1/market/{token_address}`

```json
{
  "address": "0x5C7B...",
  "symbol": "BAR",
  "price_usd": "1.13",
  "price_chz": "3.42",
  "change_24h_pct": -1.8,
  "volume_24h_usd": "284000",
  "buy_volume_24h": "156000",
  "sell_volume_24h": "128000",
  "liquidity_usd": "1240000",
  "holders": 142800,
  "holders_change_24h": 340,
  "holders_change_7d": -1200
}
```

**Derived TVI calculation:**
```javascript
const TVI = ((buy_volume_24h - sell_volume_24h) / volume_24h_usd) * 100;
// Positive = net buy pressure, negative = net sell pressure
// Range typically -100 to +100
```

---

## Chiliz Graph — Token Query
`POST https://graph.chiliz.com/subgraphs/name/chiliz/exchange`

```graphql
query TokenData($id: String!) {
  token(id: $id) {
    id
    symbol
    name
    decimals
    totalSupply
    tradeVolume
    tradeVolumeUSD
    totalLiquidity
    txCount
    derivedCHZ
  }
}
```

Response:
```json
{
  "data": {
    "token": {
      "id": "0x5c7b3a9f...",
      "symbol": "BAR",
      "name": "FC Barcelona Fan Token",
      "totalSupply": "40000000",
      "tradeVolume": "8420000",
      "tradeVolumeUSD": "9504600",
      "txCount": "284930",
      "derivedCHZ": "3.42"
    }
  }
}
```

---

## Socios Connect API — Polls
`GET https://connect.socios.com/partner-api/polls?club_id={id}&status=active`

Headers: `Authorization: Bearer <SOCIOS_PARTNER_KEY>`

```json
{
  "polls": [
    {
      "id": "poll_abc123",
      "club_id": "barcelona",
      "title": "Choose our Champions League walkout song",
      "status": "active",
      "starts_at": "2026-03-28T10:00:00Z",
      "ends_at": "2026-04-04T10:00:00Z",
      "total_votes": 18420,
      "eligible_voters": 43800,
      "participation_rate": 0.420,
      "options": [
        { "id": "opt_1", "text": "Thunderstruck - AC/DC", "votes": 9840 },
        { "id": "opt_2", "text": "Seven Nation Army - White Stripes", "votes": 8580 }
      ]
    }
  ],
  "club_avg_participation_rate": 0.31
}
```

**Participation rate interpretation:**
- Poll participation rate vs club average: `(rate / club_avg - 1) * 100` = % above/below average
- Above +20%: strong engagement signal
- Below -20%: low engagement warning

---

## Socios Connect API — Fan Engagement Events
`GET https://connect.socios.com/partner-api/fan-engagement-events?club_id={id}&days=7`

```json
{
  "events": [
    {
      "id": "event_xyz789",
      "type": "reward_drop",
      "title": "Matchday reward — El Clásico",
      "timestamp": "2026-03-29T21:00:00Z",
      "tokens_distributed": 12000,
      "unique_recipients": 8400,
      "redemption_rate": 0.70
    },
    {
      "type": "fan_challenge",
      "title": "Predict the score",
      "timestamp": "2026-03-27T09:00:00Z",
      "participants": 22000
    }
  ]
}
```

---

## HAS Composite Computation

```javascript
function computeHAS(data) {
  const {
    holders_change_7d,     // from Kayen market
    total_holders,         // from Kayen market
    participation_rate,    // from Socios polls
    club_avg_participation,// from Socios polls
    tvi,                   // computed from buy/sell volumes
    redemption_rate        // from Socios engagement events
  } = data;

  // Normalise each component to 0–1
  const holder_trend = Math.max(0, Math.min(1,
    (holders_change_7d / total_holders * 100 + 5) / 10  // +5% per week = 1.0
  ));
  const vote_score = Math.min(1, participation_rate / 0.6);  // 60% participation = max
  const tvi_norm = Math.max(0, Math.min(1, (tvi + 100) / 200));  // TVI -100 to +100 → 0 to 1
  const redemption_norm = Math.min(1, (redemption_rate || 0.3) / 0.8);

  const HAS = (
    holder_trend * 0.30 +
    vote_score   * 0.35 +
    tvi_norm     * 0.20 +
    redemption_norm * 0.15
  ) * 100;

  return Math.round(HAS);
}
```
