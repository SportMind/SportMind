---
name: fan-token-pulse
description: >
  Query live fan token ecosystem data for any football club or athlete on the Chiliz Chain
  and Socios Connect API. Use this skill whenever the user asks about fan token activity,
  token holder counts, voting participation, token velocity, token spikes, engagement index,
  geographic holder distribution, or any on-chain fan sentiment for a club or player.
  Also trigger when the user asks "what's happening with [club]'s token", "how engaged are
  [club] fans right now", "show me token data for [athlete/club]", or anything referencing
  CHZ, Socios, fan tokens, or blockchain fan engagement. This skill is the foundational data
  layer — always run it first before athlete-social-lift, transfer-signal, or brand-score.
---

# Fan Token™ Pulse

Retrieves, normalises, and interprets live fan token ecosystem data for a given club or
athlete. This is the ground-truth signal layer for SportMind — on-chain data cannot be
gamed the way social metrics can.

## What this skill produces

- **Holder Activity Score (HAS)** — 0–100 composite of holder count trend + vote participation rate
- **Token Velocity Index (TVI)** — Buy/hold/sell ratio over a configurable window (default 24h)
- **Geographic Holder Map** — Country-level breakdown of wallet activity
- **Event Classification** — Labels velocity spikes as: match-driven / social-driven / rumour-driven / airdrop-driven / market-driven
- **Engagement Trend** — 7-day and 30-day rolling direction (rising / stable / declining)

---

## Data sources

### 1. Chiliz Chain (public, no API key required)
All fan token data is on-chain and freely queryable.

**RPC endpoint (via Ankr):**
```
https://rpc.ankr.com/chiliz
Chain ID: 88888
```

**Chiliz Graph (subgraph queries):**
```
https://graph.chiliz.com/subgraphs/name/chiliz/exchange
```
Query pattern — holder count for a token:
```graphql
{
  token(id: "<CAP20_token_address>") {
    holderCount
    totalSupply
    tradeVolume
    tradeVolumeUSD
    txCount
  }
}
```

**Token address registry** (maintained by FanX/Kayen):
```
https://api.kayen.finance/v1/tokens?chain=chiliz
```
Returns all live fan token contract addresses with club metadata.

### 2. Socios Connect API (partner key required)
```
Base URL: https://connect.socios.com/partner-api
```
Key endpoints for this skill:
- `GET /polls` — active and recently closed polls, participation counts
- `GET /fan-engagement-events` — reward drops, fan challenges, voting events
- `GET /data/leagues` — league and club metadata for filtering
- `GET /data/sports` — sport type context

Auth: `Authorization: Bearer <SOCIOS_PARTNER_KEY>` (set in environment as `SOCIOS_PARTNER_KEY`)

### 3. FanX / Kayen DEX (public)
```
https://api.kayen.finance/v1/market/{token_address}
```
Returns: price, 24h volume, buy/sell pressure, liquidity depth.

---

## Workflow

### Step 1 — Resolve club/athlete to token address
1. Accept natural language input: "Barcelona", "PSG", "Man City", "Messi" etc.
2. Call Kayen token registry to resolve to CAP-20 contract address.
3. If ambiguous (e.g. "City" could be Man City or another), ask user to clarify.
4. Cache resolved address for this session.

**Common token addresses (as of Q1 2026):**
See `references/chiliz-token-registry.md` for the full list. Key ones:
- FC Barcelona (BAR): `0x...` — see registry
- Paris Saint-Germain (PSG): `0x...` — see registry
- Manchester City (CITY): `0x...` — see registry
- Juventus (JUV): `0x...` — see registry
- AC Milan (ACM): `0x...` — see registry

### Step 2 — Fetch on-chain signals
Run in parallel:
- Chiliz Graph: holder count, trade volume, tx count
- Kayen DEX: 24h price action, buy/sell ratio, liquidity
- Derive velocity: `TVI = (buy_volume - sell_volume) / total_volume * 100`

### Step 3 — Fetch Socios engagement signals
- Active polls: participation rate vs. average for this club
- Recent fan engagement events (last 7 days)
- Reward redemption counts if available

### Step 4 — Classify velocity spikes
If TVI > 20 or < -20 (significant movement), cross-reference:
- Match schedule (did club play in last 48h?)
- Socios engagement events (was a poll/reward dropped?)
- Transfer rumour feed (check transfer-signal skill if available)
- CHZ market movement (is the whole fan token market moving?)

Classification logic:
```
if match_result_in_48h AND spike_correlates → "match-driven"
elif socios_event_in_24h → "airdrop-driven" or "poll-driven"
elif CHZ_market_move > 5% → "market-driven"
elif no_clear_cause → flag for transfer-signal cross-check → "rumour-driven (unconfirmed)"
```

### Step 5 — Compute Holder Activity Score (HAS)
```
HAS = (
  holder_count_7d_trend * 0.30 +    # growing base = healthy
  vote_participation_rate * 0.35 +   # active holders vs passive
  tvi_normalised * 0.20 +            # net buying pressure
  reward_redemption_rate * 0.15      # are holders actually using tokens?
) * 100
```
Score bands:
- 80–100: Highly active ecosystem
- 60–79: Healthy engagement
- 40–59: Moderate — watch for decay
- 20–39: Low engagement — warning signal
- 0–19: Dormant ecosystem

### Step 6 — Format output
Return structured response covering:
1. Club/token identity confirmation
2. Current HAS with band label
3. TVI with classification
4. 7-day and 30-day trend direction
5. Top 5 holder geographies
6. Any active polls/events from Socios
7. Spike explanation if applicable
8. Feeds-into note (which other skills should run next)

---

## Output format

```
FAN TOKEN PULSE — [CLUB NAME] ([TOKEN_SYMBOL])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Holder Activity Score (HAS):  74 / 100  [Healthy engagement]
Token Velocity Index (TVI):   +18       [Moderate buy pressure]
Velocity classification:      Match-driven (El Clásico 48h ago)
7-day trend:                  ↑ Rising
30-day trend:                 → Stable

Top holder geographies:
  1. Spain          34%
  2. Brazil         18%
  3. Japan          12%
  4. United Kingdom  9%
  5. Argentina       8%

Active Socios events:
  - Poll: "Choose our Champions League walkout song" — 42% participation (above avg)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run athlete-social-lift to identify which players are driving holder responses
→ Run transfer-signal if velocity classification is unconfirmed
```

---

## Error handling

| Condition | Response |
|-----------|----------|
| Club not found in registry | Ask user to confirm club name; suggest closest match |
| Socios API key missing | Return on-chain data only; note engagement data incomplete |
| Chain RPC timeout | Retry once; if fails, return cached data with timestamp warning |
| Token migrated/deprecated | Flag and check for successor token in registry |
| No holder data | Token may be pre-launch or very low liquidity — state clearly |

---

## Environment variables required

```
SOCIOS_PARTNER_KEY=<your_partner_api_key>   # From Socios Connect partner portal
CHILIZ_RPC_URL=https://rpc.ankr.com/chiliz  # Default; can override
```

For read-only on-chain queries (HAS, TVI, geography), no API key is required.
For Socios engagement data (polls, events), `SOCIOS_PARTNER_KEY` is needed.

---

## Reference files

- `references/chiliz-token-registry.md` — Full CAP-20 address list for all active fan tokens
- `references/has-calibration.md` — HAS score calibration data by league tier
- `references/chiliz-api-response-shapes.md` — Example API response shapes for parsing

---

## Notes for SportMind integration

This skill is **always the first skill to run** in any SportMind agent chain. Its output
feeds directly into:
- `athlete-social-lift` — needs baseline HAS to measure lift above it
- `transfer-signal` — uses TVI spike classification to filter rumour signals
- `brand-score` — uses HAS + TVI as two of its five composite inputs

When running in an agent chain, pass the full structured output object (not just the
formatted text) to downstream skills so they can read component scores directly.
