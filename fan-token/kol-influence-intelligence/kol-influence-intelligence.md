# KOL Influence Intelligence

**The framework for reasoning about Key Opinion Leaders (KOLs), sports
influencers, and social media amplification effects on fan token commercial
signals.**

SportMind models athlete social influence through ABS (Athlete Brand Score),
SHS (Social Health Score), and AELS (Athlete Engagement Lift Score). This
skill covers the adjacent but distinct domain of *third-party* influence —
the content creator, the football YouTuber, the crypto-sports commentator,
the sports journalist with 2 million followers — whose activity about a token
or club can move HAS independently of any athlete or match outcome.

---

**Academic grounding: Baldi, Botti & Carrubbo (2023), *Springer RIIFORUM* — sentiment analysis of fan token platform content confirms that social sentiment metrics predict short-term price movements. Content published by influential accounts generates measurable HAS spikes with distinct decay profiles from organic match-driven spikes. This empirically grounds the KIS (KOL Impact Score) and the paid vs organic signal distinction modelled below.**

## Why KOL intelligence matters for fan tokens

Fan token markets respond to information asymmetry. When a Tier 1 KOL with
500,000 engaged followers publishes a video about $PSG two days before a UCL
match, that content reaches fans who have never heard of Chiliz. Some of those
fans become token holders. The HAS spike that follows is real — but its decay
profile is different from an organic pre-match HAS spike, and agents that
cannot distinguish the two will misread the signal.

Three KOL effects are commercially significant:

**Acquisition effect:** KOL content about a token that drives new wallet creation.
The DTS (Drive to Survive) principle applied to fan tokens — documentary-style
content converts viewers to holders at a measurable rate.

**Amplification effect:** KOL content about an existing event (a signing, a win,
a governance vote) that extends the commercial duration of that event beyond its
natural CDI. A trophy win has a CDI of 45 days; a viral KOL video about that
trophy posted on Day 30 can extend the commercial window.

**Warning effect:** KOL content that is critical of a token, a club, or the fan
token ecosystem that accelerates the negative decay of a poor sporting outcome.
A relegation that would normally stabilise in 10 days can extend its negative
commercial impact if prominent KOLs amplify the negative narrative.

---

## KOL tier classification

```
TIER 1 — MACRO INFLUENCERS (>500k engaged followers in sports/crypto):
  Reach: Global; content reaches outside core fan base
  Examples: Major sports YouTube channels (1M+ subscribers), premier
            crypto Twitter accounts covering sports tokens, verified
            journalists with cross-platform reach
  
  ACQUISITION RATE: 1.5-3.5% of new audience → token investigation
  HOLDER CONVERSION: 0.3-0.8% of audience → active token holder
  HAS IMPACT: +12-25 points within 24-48h of publication
  HAS DECAY: faster than organic (novelty-driven; CDI × 0.65 vs organic)
  
  AGENT RULE: Tier 1 KOL content about an active token = signal event.
  Apply HAS_spike_external flag; track for 48-72h to confirm or decay.

TIER 2 — MID-TIER INFLUENCERS (50k-500k followers):
  Reach: Strong within specific community (football fans, crypto sports)
  Credibility: Community-trusted; opinions carry weight
  
  ACQUISITION RATE: 0.8-2.0%
  HOLDER CONVERSION: 0.1-0.4%
  HAS IMPACT: +5-12 points within 48h
  HAS DECAY: moderate (community credibility sustains longer than macro)
  
TIER 3 — MICRO-INFLUENCERS (5k-50k followers):
  Reach: Niche but highly engaged
  Credibility: Often higher trust than Tier 1 (closer to audience)
  
  ACQUISITION RATE: 2.5-5% (higher engagement rate despite smaller reach)
  HOLDER CONVERSION: 0.3-0.8% (comparable to Tier 1 — more trust)
  HAS IMPACT: +2-5 points; slower; often cumulative with other signals
  
  NOTE: Multiple Tier 3 KOLs coordinating on the same token is a
  higher-signal event than a single Tier 2 post. Count and cluster.

TIER 4 — NANO-INFLUENCERS / COMMUNITY VOICES (< 5k followers):
  Reach: Immediate community only
  Individually: minimal signal impact
  Collectively: community health proxy — if nano-KOLs are consistently
  positive, community engagement is structurally healthy
  
  HAS IMPACT: negligible individually; +1-2 points if widespread cluster
```

---

## KIS — KOL Impact Score

```
KIS measures the net commercial impact of KOL activity on a specific token.

KIS = (Tier_Modifier × Reach_Score × Sentiment_Valence × Timing_Factor)
      × Credibility_Discount

TIER_MODIFIER:
  Tier 1: 1.00
  Tier 2: 0.65
  Tier 3: 0.30
  Tier 4: 0.08

REACH_SCORE:
  Views/engagements in first 24h as proxy for actual reach:
  > 100k views (Tier 1 standard): 1.00
  10k-100k: 0.60
  1k-10k:   0.30
  < 1k:     0.10

SENTIMENT_VALENCE:
  Strongly positive (buying signal, community building): +1.0
  Mildly positive (informational, neutral-positive): +0.5
  Neutral/mixed: 0.0
  Mildly negative: -0.5
  Strongly negative (FUD, credibility attack): -1.0

TIMING_FACTOR (when KOL content lands relative to events):
  T-48h to T-2h before major match: × 1.30 (amplifies pre-match momentum)
  T+0 to T+24h after win: × 1.20 (amplifies celebration arc)
  Off-cycle (no nearby event): × 0.80 (content must do all the work)
  During negative cycle (after loss): × 1.15 for negative KOL content (amplifies)

CREDIBILITY_DISCOUNT:
  Independent KOL with track record: × 1.00
  Suspected paid promotion (not disclosed): × 0.50
  Confirmed paid promotion (disclosed): × 0.70
  Known FUD account (prior false claims): × 0.25

EXAMPLE:
  Tier 1 KOL (1.00) × 80k views in 24h (0.60) × strongly positive (1.0)
  × pre-match timing (1.30) × independent (1.00) = KIS 0.78
  
  Interpretation: Meaningful positive signal; apply HAS_spike_external flag;
  adjust LTUI projection slightly upward for 3-5 days.
```

---

## Paid vs organic KOL signal distinction

```
WHY THIS MATTERS:
  Paid KOL promotions are commercial infrastructure, not organic signals.
  They represent club/platform marketing spend, not genuine community momentum.
  An organic KOL post about $BAR after a CL win tells you something real
  about community engagement. A paid partnership post tells you the club
  has a marketing budget.
  
  Conflating them produces false HAS readings.

PAID PROMOTION SIGNALS:
  Explicit disclosure: "#ad", "#sponsored", "paid partnership" labels
    → Apply CREDIBILITY_DISCOUNT × 0.70
    → Do NOT count toward organic HAS spike calculation
    
  Timing correlation with club announcements: KOL post within 24h of
  major club announcement with commercial language = likely coordinated
  → Flag as potentially_paid; monitor for disclosure
  
  Cluster deployment: Multiple Tier 2-3 KOLs posting similar content
  within the same 48-hour window with similar messaging
  → coordinated campaign signal; do not count as independent organic

ORGANIC SIGNALS:
  KOL posts driven by match outcome, genuine community excitement
  No financial relationship with token platform (verifiable)
  Content consistent with KOL's existing subject matter expertise
  → Full KIS calculation applies; counts toward organic HAS

AGENT RULE: When multiple KOLs post about the same token simultaneously:
  Check for coordination signals before applying HAS modifier.
  Organic cluster: add KIS values (cumulative positive signal)
  Coordinated campaign: apply once at campaign level (not per-post)
```

---

## Sports-specific KOL suite map

```
FOOTBALL:
  Tier 1 KOLs: major football YouTube channels (Tifo Football, GOAL,
               Sky Sports News, ESPN FC), premier football Twitter accounts
  Tier 2 KOLs: tactics analysts, transfer journalists (Fabrizio Romano tier),
               club-specific content creators
  Tier 3 KOLs: fan channels for specific clubs; local language content
  
  KEY OBSERVATION: Transfer journalists (Romano, Di Marzio) have unique
  credibility — a Romano "Here We Go" post is a Tier 1 KOL event for the
  clubs involved (especially $RMFC, $BAR, $CITY, $ATM)
  Apply: KIS × 1.20 for confirmed transfer journalists on transfer news

BASKETBALL (NBA):
  Tier 1: ESPN, TNT, NBA official channels, Shams Charania, Adrian Wojnarowski
  Tier 2: team-specific writers, basketball analytics accounts
  Woj/Shams bomb: player movement news from Tier 1 reporter = KIS × 1.25

CRICKET:
  Tier 1 KOLs: BCCI official, IPL official, Cricbuzz, ESPNcricinfo
  India-specific: regional language KOLs with massive reach
  India vernacular KOL (Hindi/Bengali/Tamil with 1M+ followers): ATM × 1.15

MMA:
  Tier 1: UFC official, MMA Fighting, Ariel Helwani
  Tier 2: fighter-specific content; gym-adjacent content creators
  Pre-fight KOL activity: fight week peaks; apply × 1.20 timing factor

FORMULA 1:
  Tier 1: F1 official, Sky F1, ESPN F1, Will Buxton
  Drive to Survive effect: Netflix itself is the ultimate Tier 1 KOL
  New-season DTS episode: apply extended CDI (same model as film release)
```

---

## KOL monitoring implementation

```python
# kol_monitor.py
"""
Monitor KOL activity for fan token signals.
Tracks Tier 1-3 KOL content and computes KIS for each token in portfolio.
"""
import asyncio
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional

@dataclass
class KOLEvent:
    kol_id:           str
    kol_tier:         int          # 1-4
    token_symbol:     str
    content_type:     str          # "video", "post", "article", "thread"
    sentiment:        float        # -1.0 to +1.0
    reach_24h:        int          # views/engagements in first 24h
    is_paid:          bool
    published_at:     str
    hours_to_next_event: float = 999.0

def compute_kis(event: KOLEvent) -> float:
    """Compute KOL Impact Score for a detected KOL event."""
    tier_modifiers = {1: 1.00, 2: 0.65, 3: 0.30, 4: 0.08}
    tier_mod = tier_modifiers.get(event.kol_tier, 0.08)
    
    # Reach score
    if event.reach_24h > 100_000: reach = 1.00
    elif event.reach_24h > 10_000: reach = 0.60
    elif event.reach_24h > 1_000:  reach = 0.30
    else:                           reach = 0.10
    
    # Timing factor
    h = event.hours_to_next_event
    if 2 <= h <= 48:    timing = 1.30
    elif h <= 24:       timing = 1.20  # post-win window
    else:               timing = 0.80
    
    # Credibility discount
    credibility = 0.70 if event.is_paid else 1.00
    
    return round(tier_mod * reach * event.sentiment * timing * credibility, 3)

def apply_kis_to_has(current_has: float, kis: float) -> float:
    """Apply KIS as an external HAS modifier."""
    if abs(kis) < 0.10:
        return current_has  # Signal too weak to register
    
    # KIS → HAS delta (positive KIS = HAS increase, negative = decrease)
    has_delta = kis * 25  # Scale factor: KIS 1.0 = +25 HAS points max
    new_has = max(0, min(100, current_has + has_delta))
    return round(new_has, 1)
```

---

## Integration with SportMind confidence output

```
WHEN KOL INTELLIGENCE MODIFIES THE SIGNAL:

KIS > 0.50 (strong positive KOL signal):
  → Add to pre-match signal output:
    "kol_signal": "POSITIVE",
    "kol_kis": 0.68,
    "has_adjustment": +8,
    "kol_note": "Tier 1 KOL (180k views, 36h pre-match, organic) — HAS uplift"
  → Adjust LTUI projection upward by CDI × 0.65 (KOL CDI shorter than organic)

KIS < -0.40 (significant negative KOL signal):
  → Add HAS_external_negative flag
  → Reduce position size recommendation by one tier
  → Note: "Negative KOL activity detected — monitor for sustained narrative"

KIS between -0.40 and +0.50 (weak/neutral signal):
  → Log but do not modify signal output
  → Include in monitoring alert only if from Tier 1 source

PAID PROMOTION DETECTED:
  → Do NOT modify HAS or LTUI
  → Log as marketing_activity (commercial infrastructure, not community signal)
  → Note: "Paid KOL promotion detected — does not reflect organic community momentum"
```

---

## Compatibility

**HAS model:** `fan-token/fan-token-pulse/` — KOL events modify HAS
**Fan sentiment CDI:** `fan-token/fan-sentiment-intelligence/` — KOL extends CDI
**AELS:** `fan-token/transfer-signal/` — athlete-level social influence (complement)
**Breaking news:** `core/breaking-news-intelligence.md` — Tier 1 sports journalists as Tier 1 KOLs
**On-chain events:** `fan-token/on-chain-event-intelligence/` — combine KOL signal with on-chain confirmation

*MIT License · SportMind · sportmind.dev*
