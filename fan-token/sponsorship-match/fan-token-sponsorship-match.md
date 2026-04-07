---
name: sponsorship-match
description: >
  Matches an athlete's fan token holder demographics and social audience profile to
  brand categories and sponsorship opportunities. Use this skill when the user asks
  which brands would be a good fit for an athlete, wants a sponsorship brief, asks
  about sponsorship ROI from fan token data, wants to know which brand categories align
  with a player's audience, asks "what sponsors would work for [athlete]?", wants to
  identify commercial partnership angles, or needs to present an athlete to potential
  sponsors. Requires fan-token-pulse and ideally brand-score outputs. Produces a
  Sponsor Match Report with ranked brand categories and outreach angles.
---

# Sponsorship Match

Translates fan token holder data and social audience profiles into actionable brand
partnership intelligence. Answers the question brands and agents both need: *which
athlete-brand combinations will drive real commercial results, backed by fan data?*

## What this skill produces

- **Sponsor Category Rankings** — which brand verticals best match this athlete's audience
- **Audience Fit Score (AFS)** per brand category (0–100)
- **Geographic opportunity map** — strongest commercial regions for this athlete
- **Outreach angle** — the specific narrative a brand should use when approaching
- **Activation ideas** — token-native campaign concepts that leverage the fan token ecosystem
- **Risk flags** — brand category mismatches or audience conflicts to avoid

---

## Prerequisites

- `fan-token-pulse` — geographic holder data, engagement profile
- `brand-score` — ABS and AELS as confidence inputs
- Athlete position, sport, age, nationality (from prior context or user input)

---

## Brand category taxonomy

```
PERFORMANCE SPORTS
  └── Sportswear & footwear        (Nike, Adidas, Puma, New Balance)
  └── Sports nutrition & supplements (Optimum Nutrition, Myprotein, Huel)
  └── Sports equipment             (sport-specific gear brands)
  └── Recovery & physio            (NormaTec, Hyperice, Therabody)

LIFESTYLE
  └── Fashion & apparel            (luxury, streetwear, casual)
  └── Watches & accessories        (luxury to mid-market)
  └── Fragrances & grooming        (male-skewed audience priority)
  └── Home & living                (if strong family/lifestyle content)

TECHNOLOGY
  └── Mobile & consumer electronics
  └── Gaming & esports             (strong if athlete has gaming content)
  └── Crypto & Web3                (natural fit for token-active athletes)
  └── Streaming & entertainment platforms

FOOD & BEVERAGE
  └── Energy drinks                (high engagement with young male audiences)
  └── Fast food & QSR
  └── Alcohol / beer               (age-gated; geography-dependent)
  └── Healthy food & snacks

FINANCIAL SERVICES
  └── Challenger banks & fintech
  └── Sports betting & gaming      (region-dependent, regulated)
  └── Crypto exchanges & wallets   (natural for token-active athletes)
  └── Insurance & financial planning

TRAVEL & HOSPITALITY
  └── Airlines & travel platforms
  └── Hotels & hospitality
  └── Tourism boards               (nationality-driven)

AUTOMOTIVE
  └── Performance cars
  └── Mass market / family
  └── Electric vehicles            (growing, strong for sustainability-positioned athletes)
```

---

## Workflow

### Step 1 — Build audience profile
Combine fan-token-pulse and brand-score outputs:

```
audience_profile = {
  geography: {top_countries_with_pct},
  age_estimate: derived from platform mix (TikTok → younger, Facebook → older),
  gender_split: estimated from sport + platform norms,
  engagement_style: "match-driven" / "lifestyle" / "mixed" (from AELS content breakdown),
  crypto_affinity: HAS score proxy — high HAS = crypto-comfortable audience,
  income_estimate: geography + platform mix proxy
}
```

### Step 2 — Score each brand category

For each category, compute Audience Fit Score (AFS):

```
AFS = (
  geographic_brand_market_overlap * 0.30 +  # does brand sell where fans live?
  demographic_alignment        * 0.25 +  # age, gender, lifestyle match
  engagement_style_match       * 0.25 +  # does brand category match content type?
  crypto_web3_affinity         * 0.10 +  # for crypto/fintech categories
  athlete_authenticity_signal  * 0.10    # does athlete already use/mention this category?
) * 100
```

Geographic brand market overlap:
- Pull brand's known primary markets (use general knowledge + web search if needed)
- Overlap with athlete's top 5 holder geographies

### Step 3 — Rank categories
Sort by AFS descending. Flag top 3 as "primary opportunities".
Flag any category where AFS < 30 as "avoid — poor fit".

### Step 4 — Token-native activation ideas
For top 3 categories, generate one token-native campaign concept each:

Template:
```
[Brand] × [Athlete] — Token Activation Concept:
  Mechanic: [What fan token holders get exclusively]
  Hook: [Why this works for the brand]
  Measurable: [How ROI is tracked via token holder behaviour]
```

Example:
```
Nike × [Athlete] — Token Activation Concept:
  Mechanic: Fan token holders vote on exclusive colourway of [Athlete]'s signature boot.
            Limited run delivered to top voters.
  Hook: Nike gets authentic co-creation data and global launch attention from
        142,000 engaged holders in their key markets.
  Measurable: Token holder participation rate pre/post campaign. TVI lift during
              campaign window. Socios poll engagement vs. baseline.
```

### Step 5 — Format Sponsor Match Report

```
SPONSOR MATCH REPORT — [ATHLETE NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Audience overview:
  Primary regions:     Brazil (28%), Spain (18%), UK (14%), Nigeria (9%)
  Engagement profile:  Match-driven, high crypto affinity (HAS: 74)
  Estimated reach:     4.8M combined social following

TOP BRAND CATEGORY MATCHES:
┌────────────────────────────┬──────┬──────────────────────────────────┐
│ Category                   │  AFS │ Key insight                       │
├────────────────────────────┼──────┼──────────────────────────────────┤
│ Crypto / Web3 platforms    │  88  │ High HAS = crypto-comfortable fan │
│ Sportswear & footwear      │  84  │ Match content drives highest AELS │
│ Energy drinks              │  77  │ Young male audience, LatAm weight │
│ Mobile & electronics       │  71  │ Global reach + tech-forward fans  │
│ Sports nutrition           │  68  │ Training content resonates        │
│ Fast fashion / streetwear  │  61  │ Social-first audience skews young │
└────────────────────────────┴──────┴──────────────────────────────────┘

AVOID: Alcohol (low AFS: 28 — LatAm audience under 21 heavy), 
       Automotive luxury (low geographic overlap with top markets)

TOKEN-NATIVE ACTIVATION IDEAS:
  1. [Crypto exchange] — Fan token holders get platform fee credits tied to
     [Athlete] milestones. Trackable, authentic, first-of-kind in market.

  2. [Sportswear brand] — Token holders vote on [Athlete]'s boots colourway.
     Limited run. Co-creation that brand can't fake.

  3. [Energy drink] — [Athlete] match-day content triggers exclusive discount
     in top 3 holder markets. Token-gated, performance-linked.

GEOGRAPHIC COMMERCIAL PRIORITY:
  Brazil — highest volume, strong sportswear + energy drink affinity
  Spain — premium lifestyle, watch/fashion potential
  UK — financial services + betting (where regulated)
  Nigeria — emerging market, mobile-first brands

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Use brand-score brief alongside this report for full commercial package
```

---

## Outreach angle generation

When user asks for a specific brand outreach message or deck angle:
1. Take top-ranked category + specific brand name
2. Generate: the insight a brand CMO hasn't thought of (token holder data as proof)
3. Frame: "Here's what [Brand] gets that no other [category] brand can claim right now"
4. Evidence: specific numbers from fan-token-pulse and AELS

---

## Reference files

- `references/brand-category-profiles.md` — Audience profiles per brand category
- `references/geographic-market-data.md` — Brand market presence by country
- `references/token-activation-templates.md` — Token-native campaign templates by category

---

## Environment variables

Inherits from prerequisite skills. No additional API keys required for core matching.
Optional: `CLEARBIT_API_KEY` for company firmographic enrichment on specific brands.
