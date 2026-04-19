---
name: fan-holder-profile-intelligence
description: >
  Intelligence framework for fan token holder behavioural segmentation —
  classifying individual and cohort holders by type, detecting community
  health signals, identifying churn risk, and producing personalised
  engagement triggers. Covers four holder archetypes (Loyalist, Speculator,
  Governor, Amplifier) with detection signals, churn risk scoring, and
  what each archetype responds to commercially. Community Health Index
  (CHI: 0–100) measures collective holder ecosystem quality beyond volume
  metrics. Directly relevant to the Ante et al. (2025) finding that fans
  are not homogeneous and token programmes that treat them as one group
  will underperform on both engagement and governance dimensions.
  Bridges the library's analytical layer to product teams building fan-
  facing applications. Load when: designing a holder engagement programme,
  assessing LTUI trajectory, building governance participation strategy,
  or evaluating community health before or after a major token event.
---

# Fan Holder Profile Intelligence — SportMind

**Fans are not homogeneous. A token programme that treats all holders
identically will underperform on every commercial metric.**

The library's existing fan intelligence (`fan-sentiment-intelligence`,
`fan-token-pulse`, `kol-influence-intelligence`) treats the fanbase as
a collective — aggregate HAS, TVI, social volume. This skill adds the
individual dimension: who are the holders, what do they want, what makes
them stay, and what makes them leave?

---

**Academic grounding: Manoli, Dixon & Antonopoulos (2024), *Leisure Studies* — 60-participant, 10-focus-group qualitative study. The identity-investment duality maps directly onto the Loyalist/Speculator distinction here. Vollero, Sardanelli & Manoli (2025), *Journal of International Marketing* — co-creation (governance participation) is more engagement-sustaining than passive holding; team brand identification moderates engagement depth. Ante et al. (2024), *Electronic Markets* — 3,576 polls, 4,003 average participants: governance participation data underpins CHI scoring.**

## The four holder archetypes

```
ARCHETYPE 1 — THE LOYALIST
  Definition: Long-term holder motivated by club identity and belonging.
  Crypto-sophistication: LOW to MEDIUM. Holds token as membership expression.
  Primary driver: Emotional connection, exclusive access, recognition.
  Governance behaviour: Votes on topics that feel meaningful to club identity
    (kit design, player tribute, stadium experience). Ignores DeFi governance.
  Churn trigger: Feeling devalued — especially if token-holders receive fewer
    perceived benefits than traditional members. Membership devaluation risk
    (Ante et al., 2025): key threat to this archetype.
  Token holding period: Months to years. Rarely sells on wins/losses.
  Cohort size signal: Wallet age distribution. Loyalists = wallets >6 months old.

ARCHETYPE 2 — THE SPECULATOR
  Definition: Holder primarily motivated by price appreciation and trading.
  Crypto-sophistication: MEDIUM to HIGH. Tracks token price vs CHZ, BTC.
  Primary driver: Return on investment, supply/demand signals, event arbitrage.
  Governance behaviour: Votes if it affects token economics. Ignores cultural votes.
  Churn trigger: Price underperformance vs broader crypto market for 30+ days.
  Token holding period: Days to weeks. High TVI (sells after price spikes).
  Cohort size signal: High TVI ratio + wallet age <30 days + exit after events.
  Note: Speculator cohort creates legitimate liquidity but inflates volume signals.
    An HAS spike driven by Speculators entering pre-match is not the same signal
    as Loyalists engaging. Agents must distinguish.

ARCHETYPE 3 — THE GOVERNOR
  Definition: Holder motivated by genuine influence over club decisions.
  Crypto-sophistication: MEDIUM. Interested in DAO governance, not just trading.
  Primary driver: Meaningful voting power, transparent decision-making, voice.
  Governance behaviour: High participation rate. Researches vote proposals before
    participating. Champions fair distribution of voting rights.
  Churn trigger: Governance theatre — votes on trivial topics only (kit colour,
    goal song) rather than commercially meaningful decisions. Feels patronised.
  Token holding period: Long-term IF governance feels meaningful. Will exit if
    governance quality declines.
  Cohort size signal: Governance participation rate. Governors = wallets that have
    voted in >60% of governance events in last 6 months.

ARCHETYPE 4 — THE AMPLIFIER
  Definition: Holder motivated by community status and social recognition.
  Crypto-sophistication: LOW to MEDIUM. Engages primarily via social platforms.
  Primary driver: Social status, recognition from club and community, content.
  Governance behaviour: Votes to be seen voting. Follows KOL recommendations.
  Churn trigger: Loss of community relevance — if holding the token is no longer
    a social identity signal (team relegated, club loses cultural relevance).
  Token holding period: Tied to club narrative arc. Spikes around major events.
  Cohort size signal: Social engagement correlation. Amplifiers = wallets whose
    activity correlates with KOL posts and social volume, not on-pitch events.
```

---

## Holder archetype detection

```
DETECTION METHOD — on-chain + social pattern analysis:

LOYALIST DETECTION:
  Wallet age > 6 months: strong loyalist signal
  No significant selling after match losses: confirmed loyalist behaviour
  Low TVI ratio (hold through volatility): loyalist confirmed
  Source: platform/chiliz-chain-address-intelligence.md — wallet age, transfer history

SPECULATOR DETECTION:
  New wallet entering < 48h before a high-stakes match: speculator entry signal
  High TVI post-event: buy-before → sell-after = speculator confirmed
  Wallet holds multiple fan tokens across different clubs: diversified speculator
  Source: platform/chiliz-chain-address-intelligence.md — Signal 4 (transfer velocity)

GOVERNOR DETECTION:
  Governance participation rate > 60%: Governor confirmed
  Multi-proposal voter (not just high-visibility votes): genuine Governor
  Source: Socios.com governance API / Chiliz Chain vote records

AMPLIFIER DETECTION:
  Wallet activity correlates with KOL posts (not on-pitch events): amplifier pattern
  New wallet created within 24h of viral KOL post: amplifier entry
  Source: fan-token/kol-influence-intelligence/ + wallet creation timestamps

MIXED ARCHETYPE:
  Most holders exhibit mixed behaviour. Primary archetype = dominant behaviour.
  Secondary archetype = secondary behaviour.
  A wallet that votes on every governance proposal AND held through a relegation
  battle = Governor-primary, Loyalist-secondary.
```

---

**Academic grounding: Alaminos et al. (2025), *SAGE Journals* — deep neural network analysis of fan token pricing. On-chain activity and club social engagement are the two most predictive features across all model architectures tested. Price data alone is less predictive than the combination of on-chain holder behaviour and club social signals. This empirically validates CHI's weighting of on-chain activity (35% loyalist share, 25% governance participation) over price-derived signals.**

## Community Health Index (CHI)

```
PURPOSE:
  A single composite score measuring the quality of a token's holder ecosystem —
  not just volume but the distribution and stability of holder types.

CHI = (loyalist_share × 0.35)
    + (governance_participation × 0.25)
    + (holder_retention_rate × 0.25)
    + (organic_volume_share × 0.15)

COMPONENT DEFINITIONS:

  loyalist_share (0–100):
    % of active wallets with age > 6 months that remain active.
    > 60%: 80–100. 40–60%: 50–79. < 40%: 0–49.

  governance_participation (0–100):
    % of eligible holders who voted in last 3 governance events.
    > 40%: 80–100. 20–40%: 50–79. < 20%: 0–49.
    Calibrated vs Socios platform average (typically 15–25%).

  holder_retention_rate (0–100):
    % of holders from 3 months ago still holding today.
    > 80% retention: 80–100. 60–80%: 50–79. < 60%: 0–49.

  organic_volume_share (0–100):
    % of TVI not attributable to KOL campaigns, airdrops, or pre-event speculation.
    > 70% organic: 80–100. 40–70%: 50–79. < 40%: 0–49.

CHI INTERPRETATION:
  CHI 75–100: HEALTHY — strong, diverse, engaged community
    Signal: LTUI stable-to-improving. Governance quality high.
  CHI 50–74: ADEQUATE — functional but watch for speculator dominance
    Signal: LTUI stable. Monitor organic_volume_share for trend.
  CHI 25–49: FRAGILE — short-term holders dominating, weak governance
    Signal: LTUI at risk. Apply uncertainty flag to long-term commercial signals.
  CHI 0–24: CRITICAL — community breakdown
    Signal: LTUI declining. ABSTAIN on new commercial positions.
    Investigate: was there a governance failure, a membership devaluation event,
    or a sustained price decline that drove Loyalists to exit?

CHI AND FTP PATH_2:
  High CHI (>75) + PATH_2 active = compounding positive signal:
    Loyalist holders who stay through PATH_2 burn cycles build long-term
    scarcity value in a healthy, engaged community.
  Low CHI (<40) + PATH_2 active = complicated signal:
    Speculator-dominated community will sell on burn confirmation,
    partially negating the supply reduction effect short-term.
```

---

## Churn risk framework

```
CHURN RISK SCORE (CRS: 0–100, higher = higher churn risk)

CRS = (price_underperformance × 0.30)
    + (governance_quality_decline × 0.25)
    + (membership_devaluation_signals × 0.25)
    + (community_fracture_signals × 0.20)

COMPONENT SIGNALS:

  price_underperformance:
    Token price vs CHZ index, 30-day rolling.
    > -20% vs CHZ: CRS component 70–100
    -10% to -20%: component 40–69
    < -10%: component 0–39

  governance_quality_decline:
    Vote topics becoming more trivial over time.
    Governance participation rate falling for 3+ consecutive events.
    Club not implementing results of governance votes: high component score.

  membership_devaluation_signals:
    Club grants non-token holders the same benefits previously exclusive to holders.
    Traditional members publicly object to token-holder privileges.
    Sources: club official communications, Tier 1/2 journalism.
    (Key finding from Ante et al., 2025: membership devaluation is the primary
    churn trigger for Loyalist archetype in German football context.)

  community_fracture_signals:
    Active public dispute between holder factions.
    KOLs turning negative (from organic promoters to critics).
    Governance vote fails by narrow margin with visible community division.

CHURN RISK LEVELS:
  CRS 70–100: HIGH CHURN RISK — structural community problem
    Action: flag COMMUNITY_HEALTH_RISK; apply -0.10 on LTUI confidence
  CRS 40–69: MODERATE CHURN RISK — monitor closely
    Action: note in signal brief; no modifier change yet
  CRS 0–39: LOW CHURN RISK — community stable
    Action: no modification needed
```

---

## Personalisation triggers by archetype

```
WHAT EACH ARCHETYPE RESPONDS TO — for product teams building engagement systems:

LOYALIST engagement triggers:
  ✓ Early access to club news before public announcement
  ✓ Exclusive digital experiences (player Q&A, training ground access)
  ✓ Recognition of long-term holding (loyalty tier badges)
  ✓ Governance votes on topics with real emotional weight
  ✗ Does NOT respond to: price performance messaging, APR, yield
  Agent signal: If club announces Loyalist-tier benefits → LTUI positive flag

SPECULATOR engagement triggers:
  ✓ Clear information on PATH_2 upcoming burn events (supply scarcity signal)
  ✓ Market data and on-chain analytics access
  ✓ Transparent tokenomics updates
  ✓ Pre-match probability signals
  ✗ Does NOT respond to: community/emotional content, governance
  Agent signal: Large Speculator cohort pre-match = elevated TVI volatility

GOVERNOR engagement triggers:
  ✓ Meaningful governance proposals (stadium name, charity partner, youth academy)
  ✓ Transparent implementation of voted decisions
  ✓ Governance delegation tools (for holders who can't vote every time)
  ✓ Governance result announcements with clear outcome explanation
  ✗ Does NOT respond to: trivial votes, governance theatre
  Agent signal: Governance participation rate drop = Governor churn warning

AMPLIFIER engagement triggers:
  ✓ Social-first content designed to be shared (highlight clips, memes, polls)
  ✓ Leaderboard and social recognition features
  ✓ Community events tied to match outcomes
  ✓ KOL collaboration content
  ✗ Does NOT respond to: governance, complex tokenomics messaging
  Agent signal: Amplifier-driven spike is short-duration; decay faster than organic

ANTI-PATTERN — treating all holders identically:
  A governance announcement sent to Speculators is noise.
  A yield farming opportunity promoted to Loyalists damages trust.
  A trivial governance vote presented to Governors causes disengagement.
  The library's LTUI model assumes this distinction matters — this skill quantifies it.
```

---

## Integration with SportMind patterns

```
PATTERN 6 (Athlete Commercial Tracker):
  Load holder profile alongside LTUI tracking.
  A LTUI decline driven by Loyalist churn is different from Speculator exit.
  Loyalist churn = structural community problem (more serious).
  Speculator exit = normal TVI cycle (less serious).

PATTERN 9 (Smart Governance Delegate):
  Governor archetype size = leading indicator of governance quality.
  Governor share < 20% of active holders = governance participation risk.
  Apply governance quality signal to pre-vote commercial brief.

FTP PATH_2 CONNECTION:
  Loyalist holders who stay through PATH_2 cycles = compounding long-term value.
  Speculator cohort cycling in/out around match events = short-term liquidity only.
  The CHI score modifies the PATH_2 commercial tier assessment:
    CHI > 75: PATH_2 burn creates genuine long-term scarcity in committed community
    CHI < 40: PATH_2 burn is partially arbitraged by speculator churn

ANTE ET AL. (2025) RESEARCH CONNECTIONS:
  This skill formalises several key findings from Ante, Henninger, Bauers,
  Schellinger (Digital Business, 2025):
  - "Fans should not be regarded as homogeneous" → four archetype framework
  - "Membership devaluation" concern → CRS membership_devaluation_signals component
  - "Governance theatre" risk → Governor churn trigger, governance quality signal
  - "Resistance to digitalization" → Loyalist archetype low crypto-sophistication flag
  - "Exclusivity concerns / exclusion of fan groups" → personalization by archetype
```

---

## Fan holder profile output schema

```json
{
  "holder_profile_brief": {
    "token":        "AFC",
    "assessed_at":  "2026-04-12T00:00:00Z"
  },

  "archetype_distribution": {
    "loyalist":    0.42,
    "speculator":  0.31,
    "governor":    0.15,
    "amplifier":   0.12,
    "note": "Loyalist-majority community — healthy composition for PATH_2 long-term value"
  },

  "chi_score":    72,
  "chi_label":    "ADEQUATE",
  "chi_components": {
    "loyalist_share":          78,
    "governance_participation": 28,
    "holder_retention_rate":   74,
    "organic_volume_share":    61
  },

  "churn_risk": {
    "crs_score":  31,
    "crs_label":  "LOW",
    "primary_risk": "governance_quality_decline — last 2 votes were trivial topics"
  },

  "personalisation_signals": {
    "loyalist_trigger_active":    true,
    "governor_alert":             "Governance quality declining — 2 trivial votes in last 30 days",
    "speculator_note":            "31% speculator share — expect elevated TVI pre-match"
  },

  "ftp_connection": {
    "loyalist_share_supports_path2": true,
    "speculator_arbitrage_risk":     "MODERATE — will cycle around burn events",
    "chi_path2_modifier":            1.02
  },

  "plain_english": "Arsenal's token community is in reasonable shape. Most holders are long-term fans who stay through wins and losses. About a third are traders who move in and out around matches — expect higher volume before big games. The governance participation rate is decent but the last two votes were trivial — if that continues, engaged fans who care about real governance will start to disengage.",

  "sportmind_version": "3.62.0"
}
```

---

*SportMind v3.62 · MIT License · sportmind.dev*
*See also: fan-token/fan-sentiment-intelligence/ · fan-token/fan-token-pulse/*
*fan-token/kol-influence-intelligence/ · platform/chiliz-chain-address-intelligence.md*
*fan-token/fan-token-lifecycle/ · fan-token/gamified-tokenomics-intelligence/*
*core/squad-cohesion-intelligence.md (parallel framework for player community)*
