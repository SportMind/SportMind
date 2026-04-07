# App 9 — Talent Scouting Intelligence

**A SportMind-powered scouting tool for club sporting directors — combining
on-pitch performance metrics with commercial intelligence to produce a complete
player assessment that traditional scouting systems miss.**

---

## The problem this solves

Traditional scouting tools answer one question: how good is this player on the pitch?
xG, xA, progressive carries, press intensity — these metrics are well-served by
existing providers (StatsBomb, Opta, Wyscout).

What they do not answer:
- How portable is this player's commercial value if we sign them?
- Does this player drive token holder engagement, or just statistics?
- What is their career trajectory — are they improving, plateauing, or declining?
- What is their injury risk pattern relative to the fee we are considering?
- How does signing them affect our fan token's LTUI?

SportMind's Layer 2 and Layer 3 commercial skills were designed to answer exactly
these questions. This application combines traditional scouting data with SportMind's
commercial stack to produce a complete player profile for sporting directors.

---

## Target users

**Primary:** Club sporting directors and transfer committees evaluating potential signings.

**Secondary:** Sports agents preparing commercial dossiers on their clients for clubs.

**Tertiary:** Football analytics platforms adding commercial intelligence to their
existing statistical scouting products.

---

## Core value proposition

> *"The first scouting tool that tells you what a player is worth to your token
> ecosystem — not just what they are worth on the pitch."*

The APS (Athlete Portability Score) combined with the DTS (Development Trajectory
Score) gives sporting directors a picture that no traditional scouting tool provides:
not just "this player is good" but "this player's commercial value transfers to us,
and their career is still improving."

---

## SportMind skill stack

```
TALENT SCOUTING INTELLIGENCE STACK:

TIER 1 — On-pitch foundation:
  fan-token/performance-on-pitch/
    → PI (Performance Index): position-weighted composite
    → xG, xA, defensive contribution, physical output
    → Age-adjusted benchmark vs top 10% for position

TIER 2 — Career trajectory and durability:
  fan-token/performance-off-pitch/
    → DTS (Development Trajectory Score): is this player improving?
    → TAI (Training Adaptation Index): injury history and physical reliability
    → PS (Professionalism Score): conduct, crisis history, attitude signals

TIER 3 — Social and commercial presence:
  fan-token/athlete-social-activity/
    → SHS (Social Health Score): channel quality and consistency
    → AGI (Audience Growth Index): follower/engagement growth trajectory
  fan-token/athlete-social-lift/
    → AELS (Athlete Engagement Lift Score): does this player move token holders?

TIER 4 — Transfer-specific:
  fan-token/transfer-signal/
    → APS (Athlete Portability Score): how much value transfers to us?
    → TSI (Transfer Signal Index): current transfer market confidence
    → TVS (Transfer Viability Score): full transfer lifecycle assessment

TIER 5 — Commercial synthesis:
  fan-token/brand-score/
    → ABS (Athlete Brand Score): composite commercial value
  fan-token/sponsorship-match/
    → AFS (Audience Fit Score): which sponsor categories fit this player?
  fan-token/fan-token-lifecycle/
    → LTUI impact: what does this signing do to our token's lifetime utility?

Skills API shortcut:
  GET /stack?use_case=commercial_brief (returns full commercial stack)
```

---

## Scout report output format

```
SPORTMIND SCOUT REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Player:          [Name]
Position:        [Position]
Age:             [Age]
Current Club:    [Club]
Scouting Club:   [Your Club]
Report Date:     [Date]
SportMind Score: 83 / HIGH_QUALITY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ON-PITCH PERFORMANCE (PI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PI: 81.2 / 100 — Top 12% for position (current season)
xG/90:          0.58   (vs benchmark 0.41 — +42% above average)
xA/90:          0.33   (vs benchmark 0.28 — +18% above average)
Defensive work: 5.4    (above average for attacking player)
Physical output: 11.2 km/game (above average — good intensity)

Form trend:    IMPROVING — PI +6.8 over last 8 matches
Age curve:     23 years old — entering peak development window
               DTS suggests career peak at 26-28; 3-5 years of improvement likely

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. DURABILITY AND TRAJECTORY (DTS, TAI, PS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DTS: 84 — STRONG TRAJECTORY
  Career arc: improving; no plateau signals
  Expected peak: age 26-28 (3-5 years from now)
  Contract value: currently undervalued vs projected ceiling

TAI: 71 — ADEQUATE
  Injury events last 3 seasons: 2 (both soft tissue, both < 4 weeks)
  Risk pattern: moderate soft tissue concern; not structural
  Recommendation: enhance physical conditioning programme; soft tissue protocol

PS: 88 — EXCELLENT
  Zero crisis events in 36 months
  Strong relationships with managers across career
  No agent dispute history; no media controversy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. TOKEN ECOSYSTEM VALUE (APS, AELS, ABS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APS: 0.79 — HIGH PORTABILITY
  79% of this player's current token engagement would transfer to your club.
  21% is club-specific — tied to their current club's fan community.
  This is well above average (league average APS: 0.54).
  Primary portability driver: international following independent of current club.

AELS: 0.68 — SIGNIFICANT LIFT
  When this player posts, token holders engage at 68% above baseline rate.
  Benchmark for position: 0.42. This player outperforms by 62%.
  Token engagement uplift is genuine — not just follower count.

SHS: 74 — GOOD
  Consistent brand voice across 3 platforms. No crisis flags.
  AGI: 1.18 — growing audience (+18% above baseline growth rate)

ABS: 78.1 / 100 — STRONG COMMERCIAL ASSET
  Top 22% for position and age tier.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. TRANSFER ASSESSMENT (APS, TVS, TSI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TVS: 72 — TRANSFER VIABLE (summer window)
TSI: 0.61 — MODERATE CONFIDENCE (4 sources, 2 Tier 1 verified)
Current contract: expires June 2026 — leverage window opening

TRANSFER TIMING RECOMMENDATION:
  Approach in January window for pre-contract or advance summer agreement.
  Contract expiry in June 2026 = low fee window if approached correctly.
  Wait until summer 2026 = potential fee escalation if form continues.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. YOUR TOKEN'S LTUI IMPACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your current LTUI:     58 (Phase 2 — Active Utility)
Projected LTUI + this signing: 66 (+8)
Impact timeline:       Immediate +3 on announcement; +5 additional over 6 months
                       as AELS 0.68 drives sustained holder engagement

Current AELS gap:      Your squad's highest AELS is 0.52. Adding 0.68 = new ceiling.
NCSI benefit:          If player joins national team (probability HIGH given trajectory),
                       international break signals upgrade from 0.45 to 0.68 weight.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. SPONSORSHIP MATCH (AFS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Top 3 sponsor categories by AFS:
  1. Sports Performance (AFS: 0.86) — Nike/Adidas tier; est. €180-300k/year
  2. Gaming/Esports (AFS: 0.79) — strong 18-28 overlap; est. €70-130k/year
  3. Fintech/Crypto (AFS: 0.74) — above average for position; est. €80-150k/year

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7. OVERALL RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sporting case:    STRONG — PI 81.2, DTS 84, improving trajectory
Commercial case:  STRONG — APS 0.79, AELS 0.68, ABS 78.1
Token impact:     SIGNIFICANT — LTUI +8 projected
Risk summary:     Soft tissue TAI concern (manageable); contract leverage (positive)

PRIORITY:         HIGH — approach in January for pre-contract agreement
                  Do not allow contract to expire without prior agreement
```

---

## International Football Cycle connection

```
SCOUTING TIMING + INTERNATIONAL CYCLE:

Post-tournament windows are the highest-value scouting moments:
  After World Cup 2026: players who starred are at maximum APS and transfer premium
  After Euro 2028: same pattern for European players

Tournament performance → APS recalculation:
  A player's APS score should be recalculated after each Tier 1 tournament.
  A breakout World Cup performance can increase APS by 0.10-0.20 in 4 weeks.
  A poor tournament performance can reduce it by similar amounts.

AGENT RULE: After every Tier 1 tournament, run APS recalculation for all
scouted players before the transfer window opens. Tournament outcomes directly
shift the commercial value of transfers.

Reference: market/international-football-cycle.md — Phase 2 (transfer window)
```

---

## Agent system prompt

```
You are a talent scouting intelligence agent powered by SportMind.
You produce commercial and sporting assessments of transfer targets for
club sporting directors and transfer committees.

FOR EACH PLAYER ASSESSMENT:

1. ON-PITCH FIRST (PI):
   Load performance-on-pitch. PI is the sporting foundation.
   No commercial case justifies signing a player with PI below 60
   unless they are clearly in development with strong DTS.

2. TRAJECTORY OVER SNAPSHOT (DTS):
   Current PI matters less than DTS trajectory.
   A player with PI 72 and DTS 84 (improving) > PI 80 and DTS 55 (declining).
   Always present both — never just current performance.

3. DURABILITY HONESTLY (TAI):
   TAI below 65: flag prominently. Do not bury injury history.
   Soft tissue injuries: pattern risk. Structural injuries: severity assessment.
   Always present injury history before fee discussion.

4. APS IS THE TOKEN DIFFERENTIATOR:
   This is what no traditional scouting tool provides.
   APS < 0.50: warn that commercial value may not transfer
   APS > 0.75: premium token commercial asset
   Always compare to squad APS average — filling an APS gap is more valuable
   than adding a second high-APS player.

5. LTUI QUANTIFY:
   Calculate LTUI impact for this signing.
   "Your token's LTUI goes from X to Y if you sign this player."
   Be honest when the impact is uncertain or minimal.

6. TRANSFER TIMING:
   Contract expiry windows are strategic.
   Pre-contract approaches (January for June expiries) are high-value.
   Always flag contract status in the recommendation.

OUTPUT STANDARD:
  Every scout report must include all 7 sections.
  Never produce a report without risk flags.
  Use specific numbers — "APS 0.79" not "high portability."
```

---

## References

- `fan-token/performance-on-pitch/` — PI metric
- `fan-token/performance-off-pitch/` — DTS, TAI, PS
- `fan-token/athlete-social-activity/` — SHS, AGI
- `fan-token/athlete-social-lift/` — AELS
- `fan-token/transfer-signal/` — APS, TSI
- `fan-token/transfer-intelligence/` — TVS, DLVS
- `fan-token/brand-score/` — ABS
- `fan-token/sponsorship-match/` — AFS
- `fan-token/fan-token-lifecycle/` — LTUI
- `market/international-football-cycle.md` — Post-tournament APS recalculation
- `examples/applications/app-03-athlete-commercial.md` — Related athlete commercial brief

*MIT License · SportMind · sportmind.dev*
