---
name: broadcast-media-intelligence
description: >
  Enduring reasoning framework for broadcast reach, media narrative, and official
  Chiliz/Socios ecosystem marketing as demand signal modifiers. Not current media
  coverage — how to reason about broadcast and media factors when context arrives.
---

# Broadcast and Media Intelligence

**How to reason about broadcast reach, media narrative, and ecosystem marketing as demand signals.**
Not current coverage — the enduring framework for applying these signals.

> Extends: `core/social-sentiment-intelligence.md` (social platform signals).
> This file covers broadcast, media narrative, and Chiliz/Socios official marketing.

---

## Broadcast reach modifier

```
BROADCAST REACH FRAMEWORK:

  WHY BROADCAST REACH MATTERS FOR FAN TOKEN DEMAND:
    Broader broadcast reach means more potential new holders are exposed to the
    club narrative simultaneously. Global broadcast events create coordinated
    demand spikes that regional broadcasts do not.

  GLOBAL BROADCAST (available to viewers across all major regions):
    Apply: global_broadcast_modifier = ×1.10 to demand signal
    Examples: UCL matches on major international networks; World Cup broadcasts;
      major international tournaments with global rights packages
    Duration: match day + 24h post-match
    
  REGIONAL BROADCAST (available primarily within one country or region):
    No modifier — regional broadcast is the baseline assumption for domestic matches.
    
  COMPARISON:
    Same result (team wins) in global broadcast context generates ×1.10 more
    demand signal than in regional broadcast.
    The result is identical; the audience size and narrative reach differ.

FREE-TO-AIR VERSUS SUBSCRIPTION:

  FREE-TO-AIR BROADCAST:
    Reaches significantly larger audience than subscription platforms.
    Apply: fta_broadcast_modifier = ×1.08 to demand signal for FTA-broadcast matches
    Mechanism: non-subscribers can watch; new-to-club audience exposed; narrative
      reaches casual fans who might become token holders
      
  SUBSCRIPTION PLATFORM:
    Baseline (no modifier) — most elite sport is now behind subscription.
    
  STREAMING PLATFORM DEAL (major platform acquires rights for a competition):
    A major streaming platform acquiring broadcast rights is a positive long-term
    demand signal for ALL fan tokens in that competition.
    Apply: streaming_rights_deal_modifier = ×1.05 sustained for the contract duration
    Mechanism: platform promotes content to its subscriber base; new audience segment
      attracted to the sport; fan token awareness grows with audience growth
    This is a slow-burn demand signal — not an immediate spike.
    
  AGENT RULE:
    For any match signal calculation:
      1. Identify the broadcast context (global / regional / FTA / subscription)
      2. Apply appropriate modifier
      3. Broadcast modifier is additive to match result signal (not a multiplier
         of the match result modifier — it adjusts the demand signal separately)
```

---

## Media narrative framework

```
NARRATIVE AS A DEMAND SIGNAL LAYER:

  PRINCIPLE:
    Sustained media narrative creates and reinforces holder sentiment
    independent of match results. A club in a "title contender" narrative
    attracts demand even in weeks without matches.

TITLE CONTENDER NARRATIVE:

  DEFINITION:
    Sustained media framing of a club as a genuine title challenger —
    appearing across multiple major outlets over 2+ weeks.
    
  MODIFIER:
    title_contender_narrative_modifier = ×1.05 applied to all demand signals
    Duration: 4-6 weeks from when narrative is established
    
  REMOVAL CONDITIONS:
    Form collapses (3 losses in 4 matches): narrative dissolves; remove modifier
    Mathematical elimination from title race: remove immediately
    
  COMPOUND WITH SEASONAL MODIFIER:
    Title contender narrative modifier stacks with the seasonal title race
    modifier from seasonal-intelligence.md (×1.15 for clubs in title race).
    Combined: ×1.05 narrative × ×1.15 seasonal = ×1.2075 combined
    Do not exceed combined narrative + seasonal cap of ×1.25.

CRISIS NARRATIVE:

  DEFINITION:
    Sustained negative media framing across multiple major outlets —
    "in crisis", "manager under pressure", "dressing room unrest."
    Must be multi-outlet, not a single article.
    
  MODIFIER:
    crisis_narrative_modifier = ×0.93 applied to all demand signals
    Duration: until three consecutive positive results shift the narrative
    
  REMOVAL CONDITIONS:
    Three consecutive wins: narrative shifts to "recovery" — remove crisis modifier
    Manager sacking resolves the narrative trigger: remove modifier on appointment
    
  DISTINGUISH FROM SOCIAL SENTIMENT:
    Crisis narrative (this file): professional media framing in sports press
    Negative social sentiment (social-sentiment-intelligence.md): community platforms
    Apply both modifiers independently when both are present — they affect different
    audience segments and compound without double-counting.

STAR PLAYER CONCENTRATION RISK:

  DEFINITION:
    When media coverage concentrates disproportionately on a single player,
    token demand becomes correlated with that player's availability more than
    squad-level signals would suggest.
    
  SIGNAL IMPLICATIONS:
    When media concentration is confirmed (player appears in >70% of club coverage):
      Apply: concentration_risk_flag = true
      Increase individual player availability modifier weight by ×1.20
      (player absence hurts demand more than position weight alone would suggest)
      
  AGENT RULE:
    Do not assume media concentration — confirm from recent coverage pattern.
    This is a contextual modifier, not a default.
```

---

## Official Chiliz and Socios ecosystem marketing

```
SOCIOS / CHILIZ OFFICIAL MARKETING CAMPAIGNS:

  WHY OFFICIAL ECOSYSTEM MARKETING IS A DISTINCT SIGNAL:
    Socios.com and Chiliz Group official marketing campaigns produce coordinated
    demand spikes across multiple tokens simultaneously. This is structurally
    different from a single club's media coverage.

  MAJOR CAMPAIGN (cross-platform, multi-club, sustained 7-14 days):
    Apply: major_campaign_modifier = ×1.15 to all affected token demand signals
    Duration: 7-14 days from campaign launch
    Affected tokens: all tokens featured in the campaign
    
  STANDARD CAMPAIGN (single-club focus, 3-7 days):
    Apply: standard_campaign_modifier = ×1.05 to featured token(s)
    Duration: 3-7 days
    
  HOW TO IDENTIFY:
    Official Socios.com and Chiliz channels announce campaigns.
    Coordinated social posts across Socios's official accounts.
    Source: official Socios/Chiliz social channels (verified accounts only)

NEW CLUB PARTNERSHIP ANNOUNCEMENT:

  DEFINITION:
    A new club (not previously on the Socios platform) announces a fan token
    partnership with Chiliz/Socios.
    
  SIGNAL:
    Positive ecosystem growth signal — platform is expanding.
    Apply: ecosystem_growth_modifier = ×1.03 sustained to all existing active tokens
    Duration: 4-6 weeks from announcement; decays as novelty normalises
    Mechanism: new partnership attracts new users to the platform; ecosystem activity
      benefits existing token liquidity marginally.
      
  TIERED BY CLUB PROFILE:
    Major global club (Tier A equivalent) joining:
      ecosystem_growth_modifier = ×1.05 (larger audience attracted to ecosystem)
    Mid-tier club joining:
      ecosystem_growth_modifier = ×1.03 (standard)
    Niche club joining:
      ecosystem_growth_modifier = ×1.01 (minimal broader ecosystem impact)

PLATFORM FEATURE LAUNCHES:

  NEW SOCIOS FEATURE (new governance mechanism, new reward type, new app feature):
    Apply: platform_feature_modifier = ×1.08 to all active token demand signals
    Duration: 5-10 days from launch (engagement spike, then normalises)
    
  WHAT QUALIFIES:
    New voting mechanism type: yes
    New reward category for holders: yes
    New app functionality: yes
    Minor UI update: no modifier

CRYPTO MEDIA COVERAGE OF FAN TOKEN ECOSYSTEM:

  WHY CRYPTO MEDIA IS A SEPARATE LAYER:
    CoinDesk, CoinTelegraph, and major crypto media outlets cover fan tokens
    as a crypto asset class, not as a sports product. Their coverage reaches
    a different audience segment than sports media.
    
  CRYPTO MEDIA COVERAGE OF FAN TOKENS (positive piece):
    Apply: crypto_media_modifier = ×1.04 to all covered tokens
    Duration: 48-72h spike; normalises
    Sources: CoinDesk, CoinTelegraph, The Block, Decrypt (verified)
    
  NEGATIVE CRYPTO MEDIA PIECE (critical analysis, regulatory risk coverage):
    Apply: crypto_negative_media_modifier = ×0.96 to all mentioned tokens
    Duration: 48-72h decay
    
  AGENT RULE:
    Crypto media and sports media operate independently.
    Apply both modifiers simultaneously when both types of coverage are present.
    They affect different potential holder audiences and do not overlap.
```

---

## Compatibility

**Social sentiment:**       `core/social-sentiment-intelligence.md`
**Seasonal demand:**        `core/seasonal-intelligence.md`
**Portfolio correlation:**  `fan-token/portfolio-intelligence.md`
**Lifecycle demand:**       `fan-token/fan-token-lifecycle/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Broadcast rights, media deal signals, and their impact on club commercial intelligence |
| Reasoning | ACTIVE | Broadcast deal reasoning chain: rights value → club revenue → CDI modifier |
| Context | ACTIVE | Broadcast context: rights cycle, streaming disruption, regional market dynamics |
| Memory | ACTIVE | Historical broadcast deal patterns and club revenue correlation |
| Judgment | ACTIVE | Judgment on broadcast signal materiality — deal expiry vs new deal impact differs |
| Attention | ACTIVE | Elevated attention during broadcast rights renewal windows |
| Communication | ACTIVE | Broadcast signal output with CDI modifier and revenue implication |
| Verification | ACTIVE | Broadcast deal figures require official announcement — estimates carry uncertainty flag |
| Learning | EMERGING | Broadcast deal impact learning from historical CDI correlation |
| Integration | ACTIVE | Integrates with market intelligence, CDI framework, and commercial partnership signals |
| Calibration | EMERGING | Broadcast revenue-to-CDI calibration requires more cross-league data |
| Adaptation | ACTIVE | Broadcast intelligence adapts as streaming disrupts traditional rights models |
| Ethics | NOT APPLICABLE | Broadcast intelligence is commercial data — no personal information involved |
| Transparency | ACTIVE | Revenue estimate vs confirmed deal distinction explicit in output |


---

*SportMind v3.97.36 · MIT License · sportmind.dev*
*Broadcast and media signals are additive to match result signals — not multiplicative*
