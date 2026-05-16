---
name: marketing-advertising-intelligence
description: >
  Enduring reasoning framework for marketing activity as a signal layer affecting
  fan token demand, community engagement, and ecosystem health. Covers marketing
  cycle intelligence, official ecosystem marketing signals, viral vs sustained
  signal distinction, co-marketing signals, and marketing spend as financial
  health proxy. Enduring frameworks only — not current campaigns or ad spend data.
---

# Marketing and Advertising Intelligence

**How marketing activity patterns affect fan token demand, community, and ecosystem health.**

> LIBRARY RULE FOR MARKETING:
> Current advertising campaigns, specific creative, social media ad spend, and
> platform-specific performance data are all expiring — not stored in SportMind.
> The enduring intelligence is how marketing activity *patterns* affect signals.

---

## Marketing cycle intelligence

```
PRE-SEASON MARKETING PEAK (June–August for European clubs):
  New kit launches, pre-season tour announcements, new signing reveals concentrate here.
  Fan token demand amplifier: ×1.15 during pre-season marketing peak.
  This overlaps with the summer transfer window demand peak — the two compound.
  See: core/seasonal-intelligence.md for full seasonal cycle framework.

IN-SEASON MARKETING CADENCE:
  Regular season marketing maintains community engagement but rarely creates demand spikes.
  Treat as baseline — no modifier.

POST-TROPHY MARKETING AMPLIFIER:
  Clubs that win major trophies immediately invest in commemorative marketing.
  Extends the demand premium beyond the match result.
  Apply: ×1.05 sustained for 4-6 weeks beyond the standard WIN premium.

END OF SEASON:
  Final match day campaigns, season review content, summer planning announcements.
  Minor demand amplifier: ×1.03 during final 4 weeks of season.
```

---

## Official ecosystem marketing signals

```
MAJOR PLATFORM CAMPAIGN (Socios/Chiliz coordinated campaign):
  App feature launches, major partnership announcements, new market entries:
  Ecosystem-wide demand amplifier: ×1.10
  Duration: campaign period (typically 2-4 weeks)
  All active fan tokens benefit from increased platform visibility.

STANDARD PLATFORM CAMPAIGN (regular social/content marketing):
  Ecosystem signal: ×1.03 — maintains awareness, does not spike demand.

NEW MARKET ENTRY CAMPAIGN:
  When Socios officially launches marketing in a new geography (new country app,
  new language support):
  Addressable market expansion signal.
  Apply: ×1.05 to tokens with confirmed fanbase in the new market geography.

PLATFORM MARKETING WITHDRAWAL:
  Socios/Chiliz significantly reduces marketing activity — dramatic reduction in
  official content output:
  Negative ecosystem signal: ×0.92.
  Monitor for structural cause before applying modifier.
```

---

## Viral versus sustained signal distinction

```
VIRAL MARKETING MOMENT:
  Single piece of content generating massive short-term attention — not sustained investment.
  Duration: 48-72 hours typical.
  Signal: Tier 2 event trend only.
  Apply: trending signal modifier from macro/trending-signal-intelligence.md.
  Do NOT apply sustained CDI modifier.

SUSTAINED MARKETING CAMPAIGN:
  Coordinated multi-channel investment over 2+ weeks with consistent messaging.
  Signal: Tier 1 structural — apply CDI modifier based on campaign scale.

HOW TO DISTINGUISH:
  VIRAL indicators:     single source | rapid spike | no pre-announcement | no paid placement
  SUSTAINED indicators: multiple channels | consistent messaging | evidence of paid
                        distribution | pre-announced campaign
```

---

## Co-marketing signals

```
CLUB AND FAN TOKEN PLATFORM CO-MARKETING (joint press release, social, events):
  Both parties investing = maximum credibility and reach.
  CDI modifier: ×1.12 for the joint campaign period.

CLUB AND CRYPTO PARTNER CO-MARKETING (beyond fan token):
  Signals broader digital asset openness from club leadership.
  Positive ecosystem signal: ×1.05.
  RISK CHECK: if co-marketing partner is unverified or high-risk crypto project:
  Apply: ×0.90 credibility risk modifier instead.

COMPETITOR CLUB CO-MARKETING (derby/rivalry fixture content):
  Creates mutual demand amplification for both clubs' fan tokens.
  Apply: ×1.05 to both tokens for 48-72h surrounding the co-marketed fixture.
```

---

## Marketing spend as financial health proxy

```
MARKETING INVESTMENT INCREASE:
  Club significantly expands activity — more content, paid campaigns, new market presence:
  Financial health signal: CDI modifier ×1.04 sustained.

MARKETING INVESTMENT CONTRACTION:
  Club significantly reduces activity — less content, no paid campaigns, reduced events:
  Financial concern signal: CDI modifier ×0.94.
  Cross-reference: core/financial-sustainability-intelligence.md.

MARKETING DARK PERIOD (7+ days complete silence on all channels, no announced reason):
  Crisis signal.
  Apply: ×0.88 | Flag as: MARKETING_DARK_PERIOD
  Could indicate ownership dispute, legal issue, or financial emergency.
  Do not apply without verifying through Tier 1 or Tier 2 source.
```

---

## Compatibility

**Sponsorship signals:**   `market/sponsorship-endorsement-intelligence.md`
**Partnership signals:**   `market/commercial-partnership-intelligence.md`
**Trending signals:**      `macro/trending-signal-intelligence.md`
**Seasonal cycles:**       `core/seasonal-intelligence.md`
**Financial health:**      `core/financial-sustainability-intelligence.md`

---

*SportMind v3.97.59 · MIT License · sportmind.dev*
*Current campaigns are expiring. Marketing PATTERNS and their effect on demand are enduring.*
