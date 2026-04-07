---
name: transfer-signal
description: >
  Monitors football transfer rumours, classifies fan token velocity spikes by cause,
  and computes the Athlete Portability Score (APS) — the quantified fan audience an
  athlete brings to a new club. Use this skill when the user asks about transfer rumours
  and their impact on fan tokens, wants to know how a potential signing would affect a
  club's token ecosystem, asks about player portability, wants to predict fan acceptance
  of a transfer, asks "how would signing [player] affect [club]'s token?", wants to know
  if a token spike is rumour-driven, or needs pre-announcement fan sentiment intelligence.
  Also trigger when fan-token-pulse returns an "unconfirmed" velocity spike. Works
  alongside fan-token-pulse and feeds directly into brand-score.
---

# Transfer Signal

Monitors transfer activity, classifies token velocity events by cause, and scores
athlete portability. The **Athlete Portability Score (APS)** quantifies how much of an
athlete's engaged fanbase would activate the destination club's token ecosystem.

## What this skill produces

- **APS** — Athlete Portability Score (0–100): how much fan value travels with a player
- **Transfer Sentiment Index (TSI)** — Fan acceptance of a specific transfer (incoming or outgoing), 0–100
- **Rumour Confidence Score** — How likely is a reported transfer to complete? (%)
- **Token Spike Attribution** — Was this velocity event rumour-driven?
- **Destination Club Impact Forecast** — Expected HAS change at destination club if transfer completes

---

## Prerequisites

- `fan-token-pulse` output for the relevant club(s) — needed for baseline HAS and TVI
- Athlete social handle (for cross-referencing athlete's own posts for hints)

---

## Data sources

### Transfer news feeds
- **Transfermarkt API** (unofficial): market values, transfer history, rumour dates
  - `https://transfermarkt-api.fly.dev/players/{id}/transfers`
- **BBC Sport / Sky Sports RSS**: major English-language transfer reporting
  - `https://feeds.bbci.co.uk/sport/football/rss.xml`
- **Twitter/X transfer accounts**: `@FabrizioRomano`, `@David_Ornstein`, `@tjuanmata`
  — monitor for "here we go" and high-confidence phrases
- **Football-API.com** or **API-Football**: match schedules, club data
  - `https://api-football-v1.p.rapidapi.com/v3/transfers`

### Sentiment sources
- Reddit: r/soccer, r/[clubsubreddit] — NLP on post title + comment sentiment
- Twitter/X: hashtag and club mention sentiment around transfer rumours
- Socios community (via Connect API if available): direct fan token holder sentiment

---

## Workflow

### Step 1 — Resolve athlete and clubs
1. Accept: athlete name + (optional) rumoured destination club
2. Resolve to Transfermarkt player ID and club IDs
3. Identify current club's fan token + destination club's fan token (via token registry)

### Step 2 — Rumour intelligence
Fetch recent transfer news mentioning the athlete:
1. RSS feed scan (BBC Sport, Sky Sports, L'Equipe, Marca, Gazzetta) — last 30 days
2. Twitter/X search: `[athlete name] transfer OR signing OR deal OR contract`
3. NLP extract: source credibility, confidence language, clubs mentioned, fee range

**Rumour Confidence Score:**
```
RCS = (
  source_tier_weight * 0.40 +     # Fabrizio Romano = 0.95, fan blog = 0.20
  corroboration_count * 0.25 +    # # of independent sources
  official_denial_penalty * 0.20 + # club/agent denial = -0.40
  athlete_hint_bonus * 0.15        # player's social post hints = +0.15
) * 100
```

Source tier weights:
- Tier 1 (0.90–0.95): Romano, Ornstein, official club announcements
- Tier 2 (0.65–0.80): Sport, Marca, Gazzetta, Sky Sports
- Tier 3 (0.40–0.60): Transfer aggregators, regional press
- Tier 4 (0.10–0.30): Fan accounts, forums

### Step 3 — Token spike attribution
If `fan-token-pulse` returned an unconfirmed TVI spike:
1. Check if any transfer rumour appeared within 48h of spike
2. Check if destination club's token also spiked (bidirectional signal = stronger rumour evidence)
3. Cross-reference athlete's own recent social activity for hints
4. Return classification: `"rumour-driven (confidence: X%)"` or `"unattributed"`

### Step 4 — Transfer Sentiment Index (TSI)
Measures *how fans feel* about a specific transfer (not just if it will happen):

**Incoming transfer TSI (destination club fans):**
```
Pull Reddit/Twitter sentiment from destination club's communities.
Filter: last 14 days, mentions of athlete name + club.
NLP: positive/negative/neutral classification.
TSI = positive_ratio * 100, adjusted for volume (low volume → wider confidence interval)
```

**Outgoing transfer TSI (source club fans):**
Same methodology on source club communities.
Low TSI on outgoing = high fan resistance = potential token sell pressure.

### Step 5 — Athlete Portability Score (APS)
The APS answers: "If [athlete] moves, how much fan value travels with them?"

```
APS = (
  athlete_global_following / league_median_following * 0.30 +  # raw reach
  AELS_if_available * 0.25 +                                    # social→token conversion
  cross_club_holder_overlap * 0.20 +                            # fans holding BOTH tokens already
  destination_club_has_token * 0.15 +                           # destination ecosystem exists
  athlete_nationality_in_destination_top_holders * 0.10         # cultural/geographic fit
) * 100
```

If AELS is not yet computed (athlete-social-lift not run), use estimated AELS based
on follower count and league tier.

APS bands:
- 80–100: High portability — athlete brings a major, activatable fanbase
- 60–79: Good portability — meaningful contribution to destination token
- 40–59: Moderate — some audience transfer, not transformational
- 20–39: Low — limited cross-over fan engagement expected
- 0–19: Minimal — audience largely stays with original club

### Step 6 — Format output

```
TRANSFER SIGNAL — [ATHLETE NAME]
Current club: [CLUB A] ([TOKEN_A])
Rumoured destination: [CLUB B] ([TOKEN_B])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rumour Confidence Score:        72%   [Tier 2 sources corroborated]
Primary sources:                Sky Sports, Marca (2 independent)
Official denial:                None recorded
Athlete hint signal:            Weak (no clear post evidence)

Transfer Sentiment Index:
  [CLUB B] incoming fans:       81 / 100  [Strong acceptance]
  [CLUB A] outgoing fans:       38 / 100  [High resistance — sell pressure risk]

Athlete Portability Score:      68 / 100  [Good portability]
  Global following vs. median:  2.4× above
  Cross-holder overlap:         12% of CLUB A holders also hold CLUB B token
  Destination ecosystem:        Active token (HAS: 71) — good landing environment

Token spike attribution:
  CLUB A TVI spike (+22, 2 days ago) → Rumour-driven (72% confidence)
  CLUB B TVI movement:          +8 (moderate interest signal)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run athlete-social-lift for full AELS to sharpen APS calculation
→ Run brand-score to value this athlete's commercial profile at destination
⚠ Watch [CLUB A] token — outgoing TSI of 38 suggests sell pressure if confirmed
```

---

## Transfer window mode

During Jan and summer transfer windows, run in continuous monitoring mode:
- Check rumour feeds every 6 hours
- Alert if Rumour Confidence Score for any monitored athlete crosses 60%
- Alert if both clubs' tokens spike simultaneously (strongest signal pattern)

---

## Reference files

- `references/journalist-source-tiers.md` — Full journalist and publication credibility tiers
- `references/sentiment-patterns.md` — Common fan community phrases and NLP mappings
- `references/aps-calibration.md` — APS validation data from historical transfers

---

## Environment variables

```
RAPIDAPI_KEY=<key>           # For API-Football transfer data
X_BEARER_TOKEN=<key>         # For Twitter rumour monitoring
REDDIT_CLIENT_ID=<id>        # For subreddit sentiment
REDDIT_CLIENT_SECRET=<secret>
```
