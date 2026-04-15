---
name: fan-engagement-connector
description: >
  Integration framework showing how SportMind's fan holder archetype
  intelligence (from fan-holder-profile-intelligence.md) translates
  into concrete engagement actions across notification systems, content
  platforms, CRM tools, and governance notification pipelines. Covers
  four engagement channels: (1) Push notification triggers by archetype
  and match event type; (2) Content targeting — what content each
  archetype responds to and when to surface it; (3) CRM integration —
  how archetype detection feeds into segment-based marketing and retention
  campaigns; (4) Governance alert timing — when to surface governance
  votes to maximise participation by archetype. Includes cross-sport
  application for clubs without active fan tokens (engagement patterns
  apply to any sports community digital product). Signal boundary:
  SportMind provides the intelligence and trigger logic — the execution
  layer (sending the notification, publishing the content) is the
  application's responsibility. The agent boundary holds.
---

# Fan Engagement Connector — SportMind

**The fan holder intelligence exists. This skill connects it to the
actions that make it commercially valuable.**

`fan-token/fan-holder-profile-intelligence.md` produces archetype
classifications (Loyalist, Speculator, Governor, Amplifier) and the
Community Health Index (CHI). This skill answers the next question:
once you know which archetype a holder is, what do you actually do?

The gap between intelligence and impact is an integration problem.
This connector closes it.

---

## The engagement signal chain

```
FLOW:
  SportMind intelligence output
    → Archetype classification (fan-holder-profile-intelligence.md)
    → Event trigger (match result, governance vote, PATH_2 burn, macro shift)
    → Engagement action selection (this skill)
    → Channel delivery (application layer — NOT SportMind)

WHAT SPORTMIND PROVIDES:
  → Which archetype each holder segment belongs to
  → Which events are commercially significant for each archetype
  → Optimal timing windows for each engagement type
  → Content brief — what the message should communicate

WHAT THE APPLICATION PROVIDES:
  → The notification infrastructure (push, email, in-app)
  → The CRM system (Salesforce, HubSpot, custom)
  → The content delivery platform
  → The governance voting interface

AGENT BOUNDARY:
  SportMind agents trigger engagement RECOMMENDATIONS, not sends.
  "Send WIN notification to Speculator segment within T+15 of result"
  is a recommendation. The application decides whether to send it.
  SportMind never directly communicates with end users.
```

---

## Channel 1 — Push notification triggers

```
TRIGGER ARCHITECTURE:
  Triggers are keyed to (event_type × archetype × timing_window).
  Each combination has an action, message brief, and priority level.

WIN RESULT — FTP PATH_2 burn confirmed:

  LOYALIST:
    Trigger window: T+0 to T+60 min (immediate emotional window)
    Message brief:  "[Club] win! The season continues."
    Tone:          Celebratory, community, belonging
    Do NOT include: token price, supply data, APR
    Priority:      HIGH

  SPECULATOR:
    Trigger window: T+15 to T+30 (after AMM rebalancing — core rule)
    Message brief:  "PATH_2 burn confirmed — supply reduced ~0.24%"
    Tone:          Data, concise, commercial
    Include:       Supply mechanics, burn amount, cumulative season burns
    Do NOT include: Emotional language, club sentiment
    Priority:      HIGH

  GOVERNOR:
    Trigger window: T+60 to T+120
    Message brief:  "WIN confirmed — next governance cycle opens [date]"
    Tone:          Participatory, process-focused
    Include:       Next vote date, quorum status
    Priority:      MEDIUM

  AMPLIFIER:
    Trigger window: T+0 to T+30 (social window is widest immediately)
    Message brief:  "[Club] win! Share the celebration [#hashtag]"
    Tone:          Social, shareable, energetic
    Include:       Social sharing assets, match highlights link
    Priority:      HIGH

LOSS RESULT — No PATH_2 supply change:

  LOYALIST:
    Trigger window: T+60 to T+240 (let emotional reaction settle)
    Message brief:  Community message from club — resilience narrative
    Tone:          Supportive, we're in this together
    Do NOT send immediately: emotional raw loss message amplifies churn

  SPECULATOR:
    Trigger window: T+60 to T+90
    Message brief:  "Result: [score]. Supply neutral — no burn event."
    Tone:          Factual. Reassurance that supply did not inflate.
    Include:       Confirmation that LOSS = supply neutral (not dilutive)
    Key education: Many Speculators incorrectly expect supply INCREASE on loss

  GOVERNOR / AMPLIFIER:
    Lower priority. Avoid amplifying loss narrative.
    Governance: next vote brief if scheduled within 48h
    Amplifier: DO NOT trigger social sharing after loss

KEY TIMING RULES:
  Never send PATH_2 commercial signals BEFORE T+15 post-WIN
    (AMM rebalancing incomplete — price signal not yet accurate)
  Never send two notifications within 30 min to same user
  Loyalist loss notification: minimum 60 min delay after final whistle
  Speculator notifications are time-critical — 15–90 min post-event window
```

---

## Channel 2 — Content targeting

```
CONTENT TYPE MATRIX by archetype:

LOYALIST content (what they consume and share):
  High response:
    ✓ Club history and heritage content
    ✓ Player profile features (non-statistical, personality-focused)
    ✓ Behind-the-scenes training ground access
    ✓ "Founding holder" loyalty recognition content
    ✓ Exclusive Q&A or AMA with club personnel
    ✓ Match-day experience content (atmosphere, tradition)
  Low/negative response:
    ✗ Price charts and token performance metrics
    ✗ APR and yield comparisons
    ✗ "Number of tokens burned this season" stats
    ✗ Technical blockchain content

  TIMING: Pre-match excitement window (T-24h to T-6h) and post-WIN celebration

SPECULATOR content (what drives action):
  High response:
    ✓ Pre-match SMS signal brief (direction, modifier summary)
    ✓ PATH_2 upcoming match calendar (burn event schedule)
    ✓ Supply reduction tracking (cumulative season burns)
    ✓ On-chain analytics (TVI trend, wallet activity)
    ✓ Competition exit impact analysis (CALENDAR_COLLAPSE signal)
    ✓ Historical burn event data (win rate this season)
  Low/negative response:
    ✗ Community emotion content
    ✗ Club nostalgia
    ✗ Governance participation requests (unless also a Governor)

  TIMING: T-48h to T-2h pre-match, T+15 to T+90 post-result

GOVERNOR content (what drives participation):
  High response:
    ✓ Governance vote announcements (advance notice 72h+ preferred)
    ✓ Vote outcome reporting (results with clear explanation)
    ✓ Community governance health data (participation rates, quorum)
    ✓ Explanation of what governance topics actually mean
    ✓ Criticism-acknowledgement content (club acknowledges voter concerns)
  Low/negative response:
    ✗ Trivial vote topics (destroys Governor engagement over time)
    ✗ Governance vote with < 48h notice
    ✗ Unexplained vote outcomes

  TIMING: Governance cycle (varies by club); NOT match-dependent primarily

AMPLIFIER content (what they share):
  High response:
    ✓ Shareable match graphics (score, key stats, visual format)
    ✓ "We are [Club]" identity content
    ✓ Record-breaking / milestone content ("100th UCL goal" etc.)
    ✓ Real-time match probability graphics
    ✓ Fan community showcase (fan photos, chants, celebrations)
    ✓ Player social media crossover content
  Low/negative response:
    ✗ Technical token data (does not amplify well)
    ✗ Long-form text content (not shareable)

  TIMING: Match window (T-2h to T+2h) is peak amplification window

AGENT RULE — CONTENT PERSONALISATION:
  When archetype is MIXED (holder segments multiple archetypes):
    Apply primary archetype content type
    Secondary archetype as supplementary only
    Never show Speculator commercial content to identified Loyalist —
    risk of relationship damage outweighs commercial gain
```

---

## Channel 3 — CRM integration

```
ARCHETYPE → CRM SEGMENT MAPPING:

SEGMENT: LOYALIST
  CRM actions:
    ✓ Long-term holder recognition programme (tier badges, anniversary messages)
    ✓ Suppress commercial upsell messaging — they respond to belonging, not yield
    ✓ Early access to limited utility events (before general release)
    ✓ Flag in CRM: HIGH_RETENTION_VALUE — churn here is structural damage
  Retention signal:
    CHURN_RISK_LOYALIST: triggered when CHI below 0.60 AND no engagement >30 days
    → Personalised re-engagement: club heritage message, not commercial offer

SEGMENT: SPECULATOR
  CRM actions:
    ✓ Pre-match signal delivery automation (T-48h, T-12h, T-2h)
    ✓ Supply mechanics education series (if new holder)
    ✓ Portfolio performance summary (weekly or post-match)
    ✓ Competition calendar with burn event schedule
  Retention signal:
    CHURN_RISK_SPECULATOR: triggered when no trades/activity >21 days
    → Re-engagement: upcoming burn event or competition signal brief

SEGMENT: GOVERNOR
  CRM actions:
    ✓ Governance calendar subscription (72h advance vote notice)
    ✓ Vote reminder at 24h before close
    ✓ Vote result notification (with explanation, not just outcome)
    ✓ Governance health report (quarterly)
  Retention signal:
    GOVERNOR_DISENGAGEMENT: participation in last 3 votes < 1 of 3
    → Check: were recent votes substantive? (trivial votes destroy Governors)
    → If votes were substantive: personal outreach by club community team
    → If votes were trivial: FLAG to governance team — topic quality issue

SEGMENT: AMPLIFIER
  CRM actions:
    ✓ Match-day content toolkit delivery (automated)
    ✓ Social sharing incentives (recognition for reach/engagement)
    ✓ Community spotlight nominations
    ✓ Influencer programme invitation (top Amplifiers by reach)
  Retention signal:
    AMPLIFIER_COOLING: social activity decline >50% over 4 weeks
    → Check: was there a loss streak? (normal; patience required)
    → Check: has content quality declined? (Amplifiers are discerning)

CHI INTEGRATION WITH CRM:
  CHI < 0.50: COMMUNITY_AT_RISK flag
    → CRM priority: stabilise Loyalists; suspend Speculator commercial
  CHI 0.50–0.70: COMMUNITY_NEEDS_ATTENTION flag
    → CRM priority: Governor engagement; check vote quality
  CHI > 0.80: COMMUNITY_HEALTHY
    → CRM: standard personalisation; growth programmes active
```

---

## Channel 4 — Governance alert timing

```
GOVERNANCE PARTICIPATION IS TIME-SENSITIVE:
  Governor archetype participation drops sharply with short notice.
  Average: 48h notice → 2.3× higher participation than 24h notice.
  72h notice → 1.6× higher than 48h.
  Recommended minimum: 72h for substantive votes.

OPTIMAL GOVERNANCE NOTIFICATION SEQUENCE:

  T-72h: FIRST NOTICE
    Content: Vote topic (described accessibly, not technically)
    Audience: Governor segment + interested Loyalists
    Channel: In-app + email (not push — not urgent yet)
    Action prompt: "See what's being decided for [Club]"

  T-24h: REMINDER
    Content: Vote closes tomorrow; current participation %
    Audience: Governors who have not voted yet
    Channel: Push + email
    Action prompt: "Your vote is needed — [x]% have voted"

  T-4h: FINAL REMINDER
    Content: Vote closes in 4 hours; quorum status
    Audience: Governors who have not voted — high urgency only
    Channel: Push only (time-critical)
    Action prompt: "Last chance — vote closes at [time]"

  T+2h post-close: RESULT NOTIFICATION
    Content: Vote outcome + what it means for the club
    Audience: All who voted + Governors who did not vote
    Channel: In-app + email
    Action: Explain the outcome clearly; acknowledge minority view

GOVERNANCE TOPIC QUALITY FILTER:
  Before triggering any governance notification:
    Is this vote substantive? (affects real club decisions, not trivial)
    Would a Governor archetype holder feel their participation matters?
    IF NO: do not publish the vote — trivial votes destroy long-term engagement
    THRESHOLD: at least one of:
      - Vote affects token utility
      - Vote affects club commercial decision
      - Vote affects governance structure itself
      - Vote was requested by the community (not top-down)

CROSS-SPORT (NO FAN TOKEN):
  Any sports organisation with a digital community product (app, membership)
  can apply the timing model without fan tokens.
  Replace "governance vote" with: community poll, fan feedback survey,
  membership benefit vote, supporter trust decision.
  The archetype model applies: not all fans want to participate in governance —
  identify your Governors and communicate with them differently.
```

---

## Non-fan-token application

```
SPORTS ORGANISATIONS WITHOUT FAN TOKENS:
  The four archetypes are not token-specific — they describe fan behaviour
  patterns that exist in any engaged sports community.

  LOYALIST → Long-term season ticket holder / member
    Engagement strategy: belonging, heritage, exclusive access
    Digital product: membership portal, early ticket access

  SPECULATOR → Performance-focused sports bettor or fantasy sports player
    Engagement strategy: data, predictions, performance signals
    Digital product: stats app, pre-match signal product

  GOVERNOR → Active supporter trust member, fan shareholder
    Engagement strategy: participation, transparency, real voice
    Digital product: supporter trust platform, shareholder communication

  AMPLIFIER → Social fan, content creator, community builder
    Engagement strategy: shareable content, recognition, social tools
    Digital product: fan zone, content toolkit, club social channels

MEDIA AND BROADCAST APPLICATION:
  Broadcaster segmentation — which archetype are your viewers?
  Loyalists: want pre-match build-up, history, context
  Speculators: want stats overlays, probability graphics, data
  Governors: want governance stories, club ownership, board decisions
  Amplifiers: want social-ready highlights, reaction content

THE UNDERLYING INSIGHT (applies everywhere):
  Not all fans want the same thing. Sending a supply reduction notification
  to a Loyalist is the equivalent of sending a "heritage and tradition" email
  to a Speculator. Both are fans. Neither gets what they need from the wrong message.
  Archetype-aware engagement is better engagement, regardless of the product.
```

---

## Output schema

```json
{
  "engagement_brief": {
    "club":        "Arsenal",
    "token":       "AFC",
    "event":       "WIN vs PSG — UCL QF",
    "event_time":  "2026-04-15T20:00:00Z",
    "assessed_at": "2026-04-15T22:05:00Z"
  },

  "triggered_actions": [
    {
      "archetype":     "LOYALIST",
      "channel":       "push_notification",
      "trigger_window":"T+0 to T+60",
      "message_brief": "Arsenal through to the UCL semi-final. Celebrate with the community.",
      "priority":      "HIGH",
      "do_not_include":["price", "supply_data", "burn_amount"]
    },
    {
      "archetype":     "SPECULATOR",
      "channel":       "push_notification",
      "trigger_window":"T+15 to T+30",
      "message_brief": "PATH_2 burn confirmed. Supply reduced. Season cumulative: −0.72%",
      "priority":      "HIGH",
      "include":       ["burn_amount", "cumulative_burns", "next_match_date"]
    },
    {
      "archetype":     "AMPLIFIER",
      "channel":       "push_notification",
      "trigger_window":"T+0 to T+30",
      "message_brief": "Semi-final bound! Share the celebration.",
      "priority":      "HIGH",
      "include":       ["shareable_graphic_url", "match_hashtag"]
    }
  ],

  "chi_state":     0.82,
  "chi_label":     "COMMUNITY_HEALTHY",
  "crm_flags":     [],

  "sportmind_version": "3.66.0"
}
```

---

*SportMind v3.66 · MIT License · sportmind.dev*
*See also: fan-token/fan-holder-profile-intelligence.md*
*fan-token/fan-sentiment-intelligence/ · fan-token/fan-token-lifecycle/*
*fan-token/gamified-tokenomics-intelligence/ · core/autonomous-agent-framework.md*
*market/broadcaster-media-intelligence.md*
