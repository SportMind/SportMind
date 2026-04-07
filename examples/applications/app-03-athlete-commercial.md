# App 3 — Athlete Commercial Intelligence Platform

**A structured briefing tool for sports agents, club commercial departments, and brands —
using SportMind's Layer 3 commercial stack to generate athlete valuation reports,
sponsorship recommendations, and transfer impact assessments.**

---

## The problem this solves

Sports agents and brand managers make commercial decisions about athletes using
primarily on-pitch statistics (goals, assists, ratings) and gut instinct. These
metrics miss the commercial picture entirely: does this athlete's social activity
actually move their club's token holders? How portable is their commercial value
if they transfer? Which brand categories genuinely fit their audience?

SportMind's Layer 3 was specifically designed to answer these questions. The ABS
(Athlete Brand Score), APS (Athlete Portability Score), AELS (Athlete Engagement
Lift Score), and AFS (Audience Fit Score) are metrics that no commercial sports
intelligence tool provides. This application puts them into a structured workflow
that sports professionals can use.

---

## Target users

**Primary:** Sports agents and player representatives evaluating commercial value
and transfer impact for their clients.

**Secondary:** Club commercial departments building sponsorship decks and evaluating
athlete partnership ROI.

**Tertiary:** Brands and sponsors assessing athlete fit before committing to deals.

**Quaternary:** Sports analytics platforms adding commercial intelligence to their
existing statistical products.

---

## Core value proposition

> *"The first athlete valuation platform built on on-chain holder data, not just
> on-pitch statistics. Know what an athlete is worth to the token ecosystem before
> you negotiate."*

The APS (Athlete Portability Score) is the unique insight. It quantifies how much of
an athlete's commercial value — measured in on-chain holder engagement — transfers
to a new club. An athlete with APS 0.82 brings 82% of their current club's token
signal with them. An athlete with APS 0.41 does not — their value is deeply tied
to their current club identity and a transfer would damage both parties' tokens.

No existing commercial sports tool provides this metric. SportMind does.

---

## SportMind skill stack

```
FULL COMMERCIAL INTELLIGENCE STACK:

1. fan-token/performance-on-pitch/
   → PI (Performance Index): position-weighted on-pitch performance
   → xG/xA metrics, scout report format
   → Athlete valuation multiplier for commercial decisions

2. fan-token/performance-off-pitch/
   → DTS (Development Trajectory Score): career arc
   → TAI (Training Adaptation Index): physical reliability
   → PS (Professionalism Score): off-pitch conduct

3. fan-token/athlete-social-activity/
   → SHS (Social Health Score): channel quality and consistency
   → AGI (Audience Growth Index): follower/engagement growth rate
   → Crisis early warning: narrative risk detection

4. fan-token/athlete-social-lift/
   → AELS (Athlete Engagement Lift Score): does this athlete move token holders?
   → Social-to-token correlation analysis

5. fan-token/transfer-signal/
   → APS (Athlete Portability Score): how much commercial value transfers?
   → TSI (Transfer Signal Index): current transfer rumour confidence

6. fan-token/transfer-intelligence/
   → TVS (Transfer Viability Score): full transfer lifecycle analysis
   → DLVS (Domestic Loan Value Score): loan spell assessment

7. fan-token/brand-score/
   → ABS (Athlete Brand Score): composite commercial synthesis
   → Exportable commercial brief format

8. fan-token/sponsorship-match/
   → AFS (Audience Fit Score): brand category ranking
   → Token-native activation ideas

9. fan-token/sports-brand-sponsorship/
   → Market rate benchmarking
   → Deal structure recommendations
   → Conflict audit (existing sponsorship clashes)

Skills API shortcut:
  GET /stack?use_case=commercial_brief
  Returns full commercial intelligence stack in correct order.
```

---

## Output: Athlete Commercial Brief

```
SPORTMIND COMMERCIAL BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Athlete: [Name]
Club: [Current Club]
Position: [Position]
Generated: [Date]
SportMind Score (SMS): 82 / HIGH_QUALITY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ON-PITCH PERFORMANCE (PI Score)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PI: 78.4 / 100 (Top 15% for position, current season)
xG: 0.62/90 | xA: 0.31/90 | Defensive contribution: 6.2
Injury days this season: 12 (within normal range for position)
Form trend: IMPROVING (+8.2 PI over last 6 matches)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OFF-PITCH COMMERCIAL PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DTS: 82 — Strong trajectory. Current contract year 3 of 4.
TAI: 76 — Good physical reliability. Minor knee concern (monitor).
PS: 91 — Excellent professionalism. Zero crisis events in 36 months.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOCIAL & TOKEN ENGAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHS: 74 (Good — consistent brand voice, no crisis flags)
AGI: 1.24 (Growing audience — 24% above baseline growth rate)
AELS: 0.68 (Significant lift — when this athlete posts, token
           holders engage at 68% above baseline rate)

TOKEN ENGAGEMENT VERDICT: HIGH VALUE
This athlete is a genuine driver of token holder engagement.
Recommend featuring in all token-native activations.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRANSFER INTELLIGENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APS: 0.74 (MODERATE PORTABILITY)
  74% of current token engagement would transfer to a new top-6 club.
  26% is club-specific — tied to current club's fan community.
  Recommendation: Transfer would retain most commercial value if
  destination club is a Tier 1 fan token club.

TVS: 68 (Moderate — transfer possible in summer window)
TSI: 0.42 (Low-confidence rumour pool — 3 reports, none Tier 1 verified)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ATHLETE BRAND SCORE (ABS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ABS: 76.8 / 100 — STRONG COMMERCIAL ASSET

Component breakdown:
  On-pitch value:        82 × 0.30 = 24.6
  Social reach:         74 × 0.25 = 18.5
  Token engagement:     68 × 0.25 = 17.0
  Off-pitch conduct:    91 × 0.20 = 18.2
                               ──────────
                               ABS = 78.3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPONSORSHIP RECOMMENDATIONS (AFS Rankings)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Top brand categories by AFS:

1. Sports Performance (AFS 0.88): Nike/Adidas tier
   Recommended: Performance apparel or boot deal
   Estimated market rate: €180k–€350k/year

2. Gaming/Esports (AFS 0.81): 18-28 audience overlap strong
   Recommended: Gaming peripheral or esports org partnership
   Estimated market rate: €80k–€150k/year

3. Fintech/Crypto (AFS 0.76): Above-average for position
   Recommended: Token-native activation or exchange partner
   Estimated market rate: €100k–€200k/year (variable)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOKEN-NATIVE ACTIVATIONS (recommended)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Exclusive pre-match Q&A available only to token holders
   (AELS 0.68 means this drives measurable holder engagement)
2. Training ground content drops linked to token milestones
3. Signed kit NFT drops to holders who attended 3+ home games
```

---

## Agent system prompt

```
You are an athlete commercial intelligence agent powered by SportMind.
You generate structured commercial briefs for sports agents, clubs, and brands.

FOR EACH ATHLETE ASSESSMENT:

1. ON-PITCH FOUNDATION (PI Score):
   Load performance-on-pitch skill. Calculate PI using position weights.
   Position context matters: a striker's xG is weighted differently
   from a goalkeeper's save percentage.

2. OFF-PITCH RELIABILITY (DTS, TAI, PS):
   Load performance-off-pitch skill. Three dimensions:
   - Development: is career trajectory improving or plateauing?
   - Physical: injury history and adaptation indicators
   - Professional: conduct and crisis risk assessment

3. SOCIAL AND TOKEN ENGAGEMENT (SHS, AGI, AELS):
   Load athlete-social-activity and athlete-social-lift skills.
   The AELS is the most commercially significant metric here:
   it measures whether this athlete actually moves token holders.
   An athlete with 10M followers but AELS 0.21 does not drive
   token engagement. An athlete with 2M followers and AELS 0.68 does.

4. PORTABILITY ASSESSMENT (APS):
   Load transfer-signal skill. APS tells the client how much
   commercial value travels with this athlete if they move.
   Always present this as a percentage and explain what's portable
   vs what's club-specific.

5. BRAND SYNTHESIS (ABS):
   Compute ABS from all sub-scores. Present as a single number
   with component breakdown. Rank against typical values for
   this athlete's position and tier.

6. SPONSORSHIP RECOMMENDATIONS (AFS):
   Load sponsorship-match skill. Rank top 3 brand categories
   with estimated market rates from sports-brand-sponsorship skill.
   Always include at least one token-native activation idea.

OUTPUT STYLE: Professional, concise, evidence-based. This brief will be
shown to sponsors, agents, and club executives. No speculation — every
number has a SportMind source.
```

---

## References

- `fan-token/performance-on-pitch/` — PI metric
- `fan-token/performance-off-pitch/` — DTS, TAI, PS metrics
- `fan-token/athlete-social-activity/` — SHS, AGI
- `fan-token/athlete-social-lift/` — AELS
- `fan-token/transfer-signal/` — APS, TSI
- `fan-token/transfer-intelligence/` — TVS, DLVS
- `fan-token/brand-score/` — ABS
- `fan-token/sponsorship-match/` — AFS
- `fan-token/sports-brand-sponsorship/` — market rates
- `agent-prompts/agent-prompts.md` — Prompt 4 (commercial intelligence agent)

*MIT License · SportMind · sportmind.dev*
