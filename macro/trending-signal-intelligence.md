---
name: trending-signal-intelligence
description: >
  Enduring reasoning framework for trending signals as fan token demand amplifiers
  or noise filters. Covers trend classification tiers, velocity assessment, platform
  weighting, manufactured trend detection, and tournament-specific trending signals.
  Not trend tracking — how to reason about trends when they are identified.
---

# Trending Signal Intelligence

**How to reason about trending signals as demand amplifiers or noise filters.**
Not trend tracking — the enduring framework for interpreting signals when context arrives.

> Key principle: trending is not the same as significant.
> Trend velocity, durability, and origin must all be assessed before applying any modifier.

---

## Trend classification framework

```
THREE-TIER CLASSIFICATION:

  TIER 1 — STRUCTURAL TREND:
    Definition: sustained across three or more major platforms over 72+ hours
    Origin: organic — not coordinated or manufactured (confirmed via velocity check)
    Modifier: demand_amplifier = ×1.08
    Duration: apply for full trend duration plus 24 hours after peak
    
  TIER 2 — EVENT TREND:
    Definition: spike triggered by specific event; single or dual platform
    Duration: typically 24-48 hours; tied to the triggering event
    Modifier: event_amplifier = ×1.04
    Apply: only within the event window; remove after 48 hours regardless
    
  TIER 3 — NOISE:
    Definition: single platform, short duration, low organic volume, or
      coordinated activity pattern detected
    Modifier: none — filter out; do not apply any demand modifier
    
  ESCALATION RULE:
    Same trend appearing on three or more platforms simultaneously →
    Treat as Tier 1 structural regardless of individual platform duration.
    Apply ×1.08 modifier immediately.
    
  FLAGS STACK: Tier 1 trend + manufactured signal detected → net cancel
    Apply ×1.00 (base) when manufactured signals are detected within a
    Tier 1-qualifying trend. Manufactured origin overrides tier classification.
```

---

## Trend velocity framework

```
VELOCITY ASSESSMENT — ORGANIC vs MANUFACTURED:

  EXPLOSIVE GROWTH (0 to trending in under 2 hours):
    Higher probability of manufactured or coordinated origin.
    Apply: bot_activity_filter before treating as organic signal.
    Confidence weight: ×0.70 — reduced reliability until organic verification
    Signs suggesting manufactured: uniform posting times, similar account ages,
      identical phrasing, no corresponding on-chain or price movement
      
  ORGANIC GROWTH (gradual build over 6-24 hours before trending):
    Higher probability of genuine community signal.
    Full confidence weight applies (×1.00 on the tier modifier).
    Signs suggesting organic: varied posting times, diverse account ages,
      natural language variation, corresponding community engagement metrics
      
  ASSESSMENT METHOD:
    When a trend is identified:
    1. Check time-to-trend velocity
    2. Check account creation date distribution of posting accounts
    3. Check phrasing diversity
    4. Check for corresponding on-chain or price movement
    5. Apply appropriate confidence weight to tier modifier
```

---

## Platform weighting

```
PLATFORM SIGNAL WEIGHT BY SOURCE TYPE:

  Platform                          Weight    Rationale
  ─────────────────────────────────────────────────────────────────────
  Official club channels            ×1.50     Highest authority source
  Twitter/X crypto community        ×1.20     High-signal community, fast-moving
  Telegram fan communities          ×1.10     High-engagement, direct holder base
  Reddit (r/socios or equivalent)   ×1.00     Standard weight; thoughtful community
  TikTok sports content             ×0.85     Lower conversion to holder action

  CROSS-PLATFORM CORRELATION BONUS:
    Three or more platforms simultaneously: treat as Tier 1
    Four or more platforms simultaneously: apply ×1.12 (above-tier amplifier)
    Cap: combined platform amplifier ceiling ×1.20

  AGENT RULE:
    When platform signals conflict (positive on one, negative on another):
      Apply the weighted average based on platform weights above.
      If official club channel contradicts social trend: club official takes priority.
      Official club announcement = always overrides social trend signal direction.
```

---

## Manufactured trend signals and filters

```
MANUFACTURED TREND DETECTION:

  RED FLAGS INDICATING MANUFACTURED ORIGIN:

  · Volume spike with no corresponding price movement or on-chain activity
    (genuine demand trends typically produce both social and market activity)
    
  · Accounts with similar creation dates posting simultaneously
    (coordinated bot network pattern)
    
  · Repeated identical phrasing across accounts with no organic variation
    (copy-paste coordination pattern)
    
  · Trend appears only in one timezone window (single-geography coordination)
    Organic trends build globally; manufactured trends concentrate geographically
    
  MANUFACTURED TREND MODIFIER:
    When any manufactured signal is detected:
    Apply: manufactured_confidence_modifier = ×0.90 to demand signal confidence
    If multiple red flags: apply ×0.80 — treat as high noise signal
    If Tier 1 classification and manufactured signal confirmed: revert to Tier 3 (no modifier)
    
  FALSE NEGATIVE PROTECTION:
    A trend that fails the manufactured filter is NOT automatically significant.
    Organic does not equal important — apply the tier classification framework
    separately from the organic/manufactured filter.
```

---

## Tournament period trending

```
WORLD CUP AND MAJOR TOURNAMENT TRENDING:

  During confirmed tournament window (four weeks before through end of tournament):
    Tier 1 trends related to PARTICIPATING NATIONAL TEAMS:
      Apply: tournament_trend_amplifier = ×1.15 on top of ×1.08 Tier 1 modifier
      Combined: ×1.24 effective amplifier for national team Tier 1 trends
      
    SIMULTANEOUSLY apply elevated manufactured trend filter:
      Tournament periods are the highest-risk window for coordinated trend manipulation.
      Apply bot_activity_filter at ×0.70 confidence threshold (more conservative).
      Organic verification required before applying full amplifier.

FAN TOKEN SPECIFIC TRENDING:

  WIN trending (confirmed organic):
    Modifier: ×1.08 demand amplifier
    Duration: 24-48 hours post-result
    Stack with: result demand signal from fan-token-context-bridge.md
    
  LOSS trending (confirmed organic):
    Modifier: ×0.92 demand signal (accelerated decay)
    Duration: 48-72 hours (loss sentiment persists longer than win sentiment)
    
  GOVERNANCE VOTE ANNOUNCEMENT trending:
    Modifier: ×1.05 engagement signal
    Duration: voting window duration
    
  TRANSFER ANNOUNCEMENT trending:
    See: core/transfer-window-intelligence.md for full framework
    Trending does not change the transfer modifier — it amplifies the existing signal.
    Transfer trending + Tier 1 structural: apply both modifiers multiplicatively
```

---

## Compatibility

**Social sentiment:**       `core/social-sentiment-intelligence.md`
**Result demand signals:**  `core/fan-token-context-bridge.md`
**Transfer trending:**      `core/transfer-window-intelligence.md`
**Tournament context:**     `macro/tournament-macro.md`
**Fraud detection:**        `fan-token/fraud-risk-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Trending signal intelligence: viral signal detection, meme cycle patterns, and short-term demand spikes |
| Reasoning | ACTIVE | Trending reasoning chain from viral signal to short-horizon demand modifier |
| Context | ACTIVE | Trending context: platform (X/Reddit/TikTok), signal source type, organic vs coordinated |
| Memory | ACTIVE | Historical trending signal patterns and their short-term demand correlation data |
| Judgment | ACTIVE | Judgment on trending signal duration — viral spikes decay rapidly, structural signals persist |
| Attention | ACTIVE | Elevated attention for unusual trending volume spikes near competition events |
| Communication | ACTIVE | Trending output with signal type, platform, organic assessment, and short-horizon modifier |
| Verification | ACTIVE | Trending signals require bot detection and coordination check before use |
| Learning | EMERGING | Trending signal calibration is limited — high noise and rapid decay make calibration difficult |
| Integration | ACTIVE | Integrates with social sentiment, KOL intelligence, and fan token demand intelligence |
| Calibration | EMERGING | Trending modifier calibration is developing — directionally useful but magnitude imprecise |
| Adaptation | ACTIVE | Trending intelligence adapts as platform dynamics and virality patterns evolve |
| Ethics | ACTIVE | Coordinated/artificial trending signals are flagged as manipulation — not used as organic signals |
| Transparency | ACTIVE | Trending platform, organic/coordinated assessment, and signal decay rate explicit in output |


---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Trending + manufactured signal detected = net cancel. Official channels override all trend signals.*
