---
name: ecosystem-health-intelligence
description: >
  Enduring reasoning framework for the overall health of the Chiliz and Socios
  fan token ecosystem as a macro context modifier for all individual token signals.
  Covers partnership velocity, platform user growth, developer activity, V2.0
  migration completion, ecosystem risk signals, and a five-dimension maturity
  scoring framework.
---

# Ecosystem Health Intelligence

**How to reason about Chiliz/Socios ecosystem health as a modifier on all individual token signals.**
Load when assessing any fan token — ecosystem health is the outermost context layer.

> Load position: after macro layer (regulatory/crypto), before individual token files.
> Ecosystem health is the SECOND outermost modifier — inside crypto cycle, outside token-specific.

---

## Partnership velocity signals

```
NEW CLUB OR ORGANISATION JOINING SOCIOS:

  DEFINITION:
    A new club, sports organisation, or athlete officially announces a fan token
    partnership with Chiliz/Socios — a new token will be launched or is confirmed.
    
  RISING TIDE EFFECT:
    New partnerships benefit all existing tokens — more clubs means more users
    entering the platform, some of whom will also buy existing tokens.
    Apply: new_partnership_signal = ×1.03 to ALL active token demand baselines
    Duration: 2-4 weeks from announcement; normalises as novelty fades
    Scale by partner profile (as per broadcast-media-intelligence.md):
      Tier A equivalent new partner: ×1.05 (larger audience attracted)
      Mid-tier new partner: ×1.03 (standard)
      Niche new partner: ×1.01 (minimal broad ecosystem impact)
      
  HOW TO CONFIRM:
    Official Chiliz or Socios announcement (Tier 1 source required)
    Do not apply based on rumour or unconfirmed reports.

PARTNERSHIP TERMINATION OR NON-RENEWAL:

  DEFINITION:
    An existing partner club or organisation announces they will not renew
    their fan token partnership, or the partnership is explicitly terminated.
    
  SINGLE TERMINATION:
    negative_ecosystem_signal = ×0.96 to all token demand baselines
    Duration: 2-3 weeks; normalises if no further terminations follow
    Single exits are not uncommon in a maturing ecosystem — monitor for pattern.
    
  MULTIPLE TERMINATIONS (2+ within 3 months):
    negative_trend_signal = ×0.92 sustained
    Flag: partnership_erosion_trend = true
    This requires human review — potential structural concern.
    
  RECOVERY SIGNAL:
    New partnership announcement after a termination:
      Apply new_partnership_signal (×1.03) AND remove termination modifier
      Net: ecosystem recovery confirmed.
```

---

## Platform user growth

```
SOCIOS APP USER BASE GROWTH SIGNAL:

  SUSTAINED GROWTH ABOVE 10% ANNUALLY:
    ecosystem_growth_health_modifier = ×1.05 applied to all token demand baselines
    Mechanism: larger addressable market; more potential buyers for all tokens;
      positive network effects (more users → more community engagement → more activity)
    
  STATIC USER BASE (0-5% annual growth):
    No modifier — baseline applies
    Flag: growth_stagnation_monitor — watch for trend direction
    
  DECLINING ACTIVE USER BASE:
    ecosystem_contraction_modifier = ×0.93 applied to all token demand baselines
    Definition: declining monthly active users for 3+ consecutive months
    Mechanism: fewer potential buyers; reduced community engagement; holder retention risk
    
  DATA SOURCES:
    Socios official company reports or announced milestones
    App store download rank trends (secondary signal)
    Social media engagement trend (indirect signal)
    Note: Socios does not publish monthly user data publicly — use available
      proxy signals and official announcements.

GOVERNANCE PARTICIPATION RATES AS ENGAGEMENT PROXY:
  High governance participation across the ecosystem (multiple tokens):
    Signals healthy holder engagement — holders are active, not passive speculators
    Apply: ecosystem_engagement_health = positive flag
    Correlates with: lower holder fragility, more stable demand baseline
  Low governance participation across the ecosystem:
    Holder disengagement signal — holders are speculative, not engaged
    Apply: ecosystem_disengagement_flag — increase holder fragility estimates
```

---

## Developer activity on Chiliz Chain

```
DEVELOPER ECOSYSTEM SIGNALS:

  NEW DAPPS, PROTOCOLS, AND TOOLS ON CHILIZ CHAIN:
    Growing developer activity is a leading indicator of future user growth.
    Developers build the applications that attract users.
    Apply: developer_activity_growth_modifier = ×1.03 sustained when
      new deployments are occurring (monthly check via chiliscan.com)
    
  CHILIZ CHAIN DEVELOPER GRANTS OR HACKATHON:
    Official Chiliz grants programme or hackathon activity:
    Apply: innovation_signal = ×1.03 for 4-8 weeks post-event
    Mechanism: attracts new builders; signals platform investment in ecosystem growth

  TOTAL VALUE LOCKED (TVL) ON CHILIZ CHAIN DAPPS:
    Growing TVL = capital is being deployed in ecosystem applications
    Apply: tvl_growth_modifier = ×1.03 when TVL is in sustained growth
    Source: DeFiLlama (chiliz.com chain page) — publicly available
    
  DEVELOPER DEPARTURE / PROTOCOL ABANDONMENT:
    If established dApps or protocols on Chiliz Chain are abandoned:
    Apply: developer_departure_signal = ×0.97 (mild negative)
    Multiple departures in short period: apply ×0.94
```

---

## Fan Token V2.0 ecosystem signals

```
V2.0 MIGRATION COMPLETION RATE:

  V2.0 STATUS:
    Fan Tokens V2.0 migrates tokens to 18-decimal precision and enables
    cross-chain access via LayerZero to Base and Solana.
    
  HIGH COMPLETION (above 80% of tokens migrated):
    ecosystem_technical_maturity_signal = positive
    Apply: ×1.03 ecosystem confidence modifier
    Mechanism: ecosystem infrastructure is consistent; no fragmentation risk
    
  LOW COMPLETION (below 50% of tokens migrated):
    ecosystem_fragmentation_risk = ×0.94
    Mechanism: inconsistent user experience across the ecosystem;
      some tokens accessible cross-chain, others not — creates confusion
    
  STANDARD COMPLETION (50-80%):
    No modifier — transition is in progress; monitor for direction
    
CROSS-CHAIN VOLUME SIGNALS:
  Cross-chain volume growing (tokens moving between Chiliz Chain, Base, Solana):
    addressable_market_expansion_modifier = ×1.05
    Mechanism: each chain has a different holder segment — cross-chain growth
      means new segments are accessing fan tokens
    Monitor: LayerZero bridge explorer for Chiliz ↔ Base/Solana volumes
    
  Cross-chain volume declining:
    Monitor for 3+ consecutive weeks before applying any modifier
    Then: ×0.97 mild accessibility concern signal
```

---

## Ecosystem risk signals

```
SINGLE EXCHANGE CONCENTRATION RISK:

  IF ONE EXCHANGE PROVIDES >50% OF FAN TOKEN LIQUIDITY:
    exchange_concentration_risk = ×0.92 confidence weight on all demand signals
    Mechanism: ecosystem is vulnerable to a single exchange policy change;
      any delisting or restrictions by the dominant exchange would have
      outsized impact on all tokens
    Applies to: ecosystem-level signal confidence — not to individual token demands
    
  HOW TO ASSESS:
    Which exchange provides the majority of CHZ and fan token trading volume?
    Source: CoinGecko exchange volume breakdown for CHZ and individual tokens
    
REGULATORY CONCENTRATION RISK:

  IF MAJORITY OF FAN TOKEN VOLUME IS IN ONE JURISDICTION FACING UNCERTAINTY:
    regulatory_concentration_risk = ×0.90 applied to ecosystem health assessment
    Mechanism: single jurisdiction dependency creates systemic risk if regulatory
      conditions deteriorate in that jurisdiction
    Map: which jurisdiction accounts for >40% of fan token transaction volume?
    If that jurisdiction faces confirmed regulatory uncertainty: apply modifier
    
COMPETITOR PLATFORM EMERGENCE:

  DEFINITION:
    A new fan token or sports engagement token platform launches, targeting
    the same club fan base with a competing product.
    
  SIGNAL:
    Monitor for fragmentation — ecosystem users may split between platforms
    Apply: competitor_emergence_flag = true; monitor for 3 months
    If competitor is gaining meaningful traction (confirmed new partnerships):
      ecosystem_competition_modifier = ×0.96 for directly competing token categories
    If competitor fails to gain traction: remove flag; no modifier applied
```

---

## Ecosystem maturity scoring framework

```
FIVE-DIMENSION MATURITY ASSESSMENT:

  Assess the ecosystem on each of these five dimensions.
  Score each: HIGH (2 points) / MEDIUM (1 point) / LOW (0 points)
  Maximum: 10 points

  DIMENSION 1 — PARTNERSHIP DEPTH:
    HIGH: 30+ active club partnerships across major leagues; top clubs represented
    MEDIUM: 15-30 partnerships; some major clubs; gaps in key leagues
    LOW: fewer than 15 partnerships; limited to niche clubs

  DIMENSION 2 — TECHNICAL INFRASTRUCTURE:
    HIGH: V2.0 migration >80% complete; cross-chain active; developer tooling mature
    MEDIUM: V2.0 in progress 50-80%; some cross-chain; basic tooling
    LOW: V2.0 <50%; limited cross-chain; minimal developer tooling

  DIMENSION 3 — REGULATORY CLARITY:
    HIGH: clear frameworks in EU (MiCA), UK (SI 2026/102), UAE (VARA), GCC (HIGH+)
    MEDIUM: major markets covered; some jurisdictions still developing
    LOW: regulatory uncertainty in majority of major holder markets

  DIMENSION 4 — MARKET LIQUIDITY:
    HIGH: Tier 1 exchange coverage for CHZ; multiple tokens on Tier 1/2; tight spreads
    MEDIUM: CHZ on Tier 1; most tokens on Tier 2; reasonable spreads
    LOW: limited exchange coverage; wide spreads; thin order books

  DIMENSION 5 — COMMUNITY ENGAGEMENT:
    HIGH: governance participation consistently above 15%; low holder churn; active communities
    MEDIUM: governance 5-15%; some churn; moderate community activity
    LOW: governance below 5%; high churn; dormant communities

  SCORING AND MODIFIER TABLE:

  Total score    Rating           Modifier
  ─────────────────────────────────────────────────────────────────
  8-10           MATURE           ×1.10 ecosystem health amplifier
  5-7            DEVELOPING       ×1.00 (no modifier — baseline)
  0-4            EARLY STAGE      ×0.88 ecosystem health suppressor

  Apply: the ecosystem maturity modifier to all individual token demand
    baselines as the outermost context modifier (inside crypto cycle layer).
  This score should be assessed at the start of each quarter — not per match.
  
  TRIGGER FOR RE-ASSESSMENT:
    Major positive event (Tier A club joining, institutional custody launch): reassess
    Major negative event (large termination, exchange delisting of CHZ): reassess
    Otherwise: quarterly assessment is sufficient.
```

---

## Compatibility

**Crypto cycle (outermost):**   `macro/macro-crypto-market-cycles.md`
**Exchange risk:**              `macro/exchange-intelligence.md`
**New partnership detail:**     `core/broadcast-media-intelligence.md`
**Governance engagement:**      `fan-token/governance-intelligence.md`
**V2.0 mechanics:**             `fan-token/fan-token-lifecycle/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan token ecosystem health: CHI composite score, platform health, and ecosystem signals |
| Reasoning | ACTIVE | CHI reasoning chain from ecosystem signals to composite health modifier |
| Context | ACTIVE | Ecosystem context: Chiliz platform state, token count, trading volume trend |
| Memory | ACTIVE | Historical CHI baseline data and ecosystem health trend patterns |
| Judgment | ACTIVE | Judgment on CHI threshold — below 0.5 applies ECOSYSTEM_RISK modifier to all signals |
| Attention | ACTIVE | Elevated attention for ecosystem-wide signals: platform outages, CHZ price collapses |
| Communication | ACTIVE | Ecosystem health output with CHI value and active ecosystem modifiers |
| Verification | ACTIVE | Ecosystem data from Chiliz official sources and on-chain metrics |
| Learning | ACTIVE | CHI calibration from historical ecosystem state-to-token performance correlation |
| Integration | ACTIVE | CHI integrates across all fan token signals as baseline modifier |
| Calibration | ACTIVE | CHI values and thresholds calibrated against historical ecosystem-outcome data |
| Adaptation | ACTIVE | Ecosystem health framework adapts as Chiliz platform evolves |
| Ethics | ACTIVE | Ecosystem manipulation signals are flagged and escalated within this framework |
| Transparency | ACTIVE | CHI value and its component signals always explicit in output |
| Execution | ACTIVE | Signal generation workflow, event playbooks, and structured output templates defined |
| Collaboration | ACTIVE | Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer |


---

*SportMind v3.97.41 · MIT License · sportmind.dev*
*Ecosystem maturity modifier is quarterly — not per-match. Assess at season start.*
