---
name: fraud-risk-intelligence
description: >
  Enduring red flag framework for reasoning about fraud risk signals in sports
  crypto assets. Three-tier red flag system, tournament fraud amplification
  patterns, agent output specification for unverified assets, and clear scope
  boundaries for what SportMind does and does not do. Reasoning frameworks only
  — not legal determinations and not specific asset classifications.
---

# Fraud Risk Intelligence

**Enduring red flag reasoning framework for sports crypto assets.**
Risk signals and verification recommendations — not fraud classifications.

> SportMind agents surface risk signals and recommend verification.
> They do not classify specific assets as fraudulent.
> Fraud is a legal determination requiring regulatory authority.
> Load alongside: `fan-token/official-verification-framework.md`

---

## Red flag framework

```
THREE-TIER RED FLAG SYSTEM:

  How to apply:
  · Any single Tier 1 flag → UNVERIFIED classification + strong verification recommendation
  · Two or more Tier 2 flags → UNVERIFIED + elevated risk signal
  · Single Tier 3 flag only → monitoring note; verification recommended but not urgent
  · Flags stack across tiers: a Tier 2 + a Tier 3 warrants elevated treatment

────────────────────────────────────────────────────────────────────

TIER 1 — CRITICAL RISK SIGNALS:
Any single Tier 1 flag alone warrants UNVERIFIED classification.

  ANONYMOUS OR UNVERIFIABLE TEAM:
    No named individuals, no company registration, no verifiable legal entity
    behind the token project.
    Official Fan Tokens™ always have named corporate backing (Mediarex/Chiliz).
    If the issuing entity cannot be verified as a named legal person or entity:
    Tier 1 flag — apply immediately.
    
  NO OFFICIAL SPORTS ORGANISATION ENDORSEMENT ON PRIMARY SOURCES:
    Token claims affiliation with a club, national association, or governing body
    but the organisation has not confirmed the partnership on their own official
    channels (official website, official verified social accounts, official press release).
    Media articles and community posts are NOT primary source confirmation.
    Absence of organisation-side confirmation = Tier 1 flag.
    
  CONTRACT ADDRESS NOT ON CHILISCAN.COM:
    A token claiming to be an official Fan Token™ that has no verified contract
    address on chiliscan.com is definitively not an official Fan Token™.
    This is a critical structural check — not a judgment call.
    If the contract is absent from chiliscan.com/tokens: Tier 1 flag.
    
  PASSIVE YIELD OR GUARANTEED RETURN PROMISES:
    Official Fan Tokens™ are utility tokens — they provide access to experiences,
    governance rights, and engagement rewards.
    They do not promise passive yield based on holding.
    Any token promising:
      "Earn [%] per month/year on your holdings"
      "Guaranteed returns from tournament revenue"
      "Staking yield from match results"
    → Tier 1 flag on two grounds:
      (1) Inconsistent with official Fan Token™ utility design
      (2) Potential CLARITY Act Section 404 violation for US-accessible tokens
          (passive yield on sports tokens is prohibited under the draft framework)
    
  SUDDEN LAUNCH TIMED TO MAJOR SPORTING EVENT:
    Token launches immediately before or during a major event (World Cup, UCL Final,
    Olympics, Super Bowl) with no prior official partnership announcement.
    The timing window: within 2 weeks of a major event start without any prior
    announcement from either the sports organisation or Chiliz/Socios.
    Official partnerships are announced in advance through both parties' channels.
    Event-timed launch with no prior announcement: Tier 1 flag.

────────────────────────────────────────────────────────────────────

TIER 2 — ELEVATED RISK SIGNALS:
Two or more Tier 2 flags warrant UNVERIFIED classification.

  COPYCAT TOKEN NAME OR TICKER:
    Tokens using names or tickers designed to be confused with official Fan Tokens™.
    Indicators: club name + "Token", national team name + "Fan", competition name + "Coin"
    without confirmed partnership. Compare against official registry.
    
  ARTIFICIAL URGENCY MESSAGING:
    "Limited time offer", "before the World Cup ends", "only X tokens remaining",
    "get yours before listing price rises."
    Urgency messaging designed to bypass due diligence.
    Official Fan Token™ launches do not use urgency tactics.
    
  UNVERIFIABLE WHITEPAPER OR ROADMAP CLAIMS:
    Claims about future utility, partnership pipelines, or revenue-sharing that
    cannot be confirmed through official primary sources.
    If claims are present but unverifiable: Tier 2 flag.
    Absence of any documentation at all: escalate to Tier 1 consideration.
    
  WALLET CONCENTRATION + UNVERIFIABLE TEAM:
    Very small number of wallets holding a large percentage of supply
    (top 3 wallets holding >50%) combined with an unverifiable team.
    This combination is a documented rug pull risk pattern.
    Either signal alone is Tier 3; the combination escalates to Tier 2.
    
  SOCIAL MEDIA ONLY PRESENCE:
    No official website. No company registration. No verifiable corporate structure.
    Exclusively social media accounts that may themselves be recently created.
    Check: when was the primary social media account created? Is it verified?
    
  UNVERIFIED CELEBRITY OR ATHLETE ENDORSEMENT:
    Claims of endorsement by named athletes, celebrities, or clubs that cannot
    be verified through the endorser's own official channels.
    Fabricated endorsements are common in fraudulent sports tokens.
    Method: check the named endorser's official accounts directly.
    If the endorser has not posted about it on their own verified channels: Tier 2 flag.

────────────────────────────────────────────────────────────────────

TIER 3 — MONITORING SIGNALS:
Single Tier 3 flag warrants additional verification but not immediate UNVERIFIED.

  · Very recently launched token (under 30 days) with no established track record
  · Very low holder count relative to the claimed fanbase size
  · Price activity inconsistent with sporting event calendar
    (significant spikes with no corresponding sporting trigger — possible
    wash trading or coordinated pump)
  · Limited exchange coverage — available only on obscure or unregulated exchanges
    with no listing on Tier 1 or Tier 2 exchanges or official platforms
```

---

## Tournament period fraud amplification

```
MAJOR TOURNAMENTS ARE THE HIGHEST-RISK WINDOWS:

  The tournament fraud amplification pattern is enduring — it repeats
  consistently across every major sporting tournament regardless of sport.
  
  WHY TOURNAMENT PERIODS AMPLIFY FRAUD RISK:
  
  1. LARGE NEW AUDIENCE:
     Major tournaments bring a surge of fans new to the sports crypto space.
     New entrants are less experienced with verification; more susceptible
     to urgency messaging and official-looking branding.
     
  2. HIGH EMOTIONAL ENGAGEMENT:
     National team tournaments create strong affiliation with specific teams.
     Emotional urgency ("support your country") is exploited to bypass due diligence.
     
  3. AMBIENT LEGITIMACY:
     Legitimate Fan Token price movements and FTP PATH_2 events receive real
     media coverage during major tournaments. Fraudulent projects deliberately
     appear in this ambient coverage to gain credibility.
     
  4. RAPID TOKEN PROLIFERATION:
     The volume of new tokens claiming sports affiliation increases sharply
     in the weeks before and during major tournaments, making it difficult
     to distinguish legitimate from fraudulent without systematic verification.

TOURNAMENT FRAUD RISK MODIFIER:
During the active risk window — defined as four weeks before to four weeks after
the start of a major international tournament — apply elevated scrutiny:

  ANY NEW TOKEN LAUNCH DURING WINDOW:
    Immediate four-source verification required before any other analysis.
    Do not proceed with SportMind intelligence frameworks until verified.
    
  ANY TOKEN CLAIMING NATIONAL TEAM AFFILIATION NOT IN REGISTRY:
    Apply UNVERIFIED status automatically.
    Cross-reference: fan-token/official-verification-framework.md national team list.
    
  ANY TOKEN PROMISING TOURNAMENT-SPECIFIC FINANCIAL RETURNS:
    Automatic Tier 1 red flag.
    Official Fan Tokens™ do not promise tournament-specific financial returns.

WORLD CUP 2026 — SPECIFIC RISK ELEVATION:
  Three factors make the 2026 FIFA World Cup a particularly high-risk window:
  
  SCALE (48-team format):
    More nations participating means more potential fraudulent tokens claiming
    national team affiliation from nations without official fan tokens.
    Only four national team Fan Tokens™ are confirmed in SportMind's dataset
    ($ARG, $POR, $SNFT, $BFT) — all other national team claims are UNVERIFIED.
    
  GEOGRAPHY (USA, Canada, Mexico host nations):
    Three large English-speaking North American markets with significant crypto
    user bases are newly exposed to sports crypto marketing in their home context.
    
  REGULATORY TIMING (CLARITY Act in legislative process):
    US regulatory framework is still developing during the tournament window.
    Fraudulent projects may make claims about US legality that cannot yet
    be definitively confirmed or denied.
    Apply the existing CLARITY Act Section 404 framework:
      Activity-based rewards: compliant model
      Passive yield promises: non-compliant signal + Tier 1 red flag
```

---

## Agent output for unverified assets

```
REQUIRED OUTPUT STRUCTURE FOR UNVERIFIED SPORTS CRYPTO ASSETS:

{
  "verification_status":   "UNVERIFIED",
  "official_fan_token":    false,
  "registry_match":        false,
  "sources_confirmed": {
    "club_official_website":  [true/false],
    "socios_listing":         [true/false],
    "chiliscan_contract":     [true/false],
    "fantokens_listing":      [true/false]
  },
  "risk_flags":   ["[list active red flag descriptions]"],
  "risk_tier":    "TIER_1" | "TIER_2" | "TIER_3",
  "risk_summary": "[one sentence description of the primary risk signal]",
  "recommendation": "Verify through official primary sources before any decision.",
  "primary_sources": [
    "socios.com",
    "chiliscan.com/tokens",
    "fantokens.com",
    "[club official website]"
  ],
  "framework_reference": "fan-token/official-verification-framework.md"
}

FOR VERIFIED OFFICIAL FAN TOKENS™:
{
  "verification_status":   "OFFICIAL",
  "official_fan_token":    true,
  "registry_match":        true,
  "sources_confirmed": {
    "club_official_website":  true,
    "socios_listing":         true,
    "chiliscan_contract":     true,
    "fantokens_listing":      true
  },
  "risk_flags":   [],
  "risk_tier":    null,
  "recommendation": "Proceed with SportMind intelligence frameworks."
}
```

---

## Agent verification workflow

```
STEP-BY-STEP AGENT WORKFLOW FOR ANY SPORTS CRYPTO ASSET CLAIM:

  STEP 1 — REGISTRY CHECK:
    Does this asset appear in fan-token/registry/complete-registry.md or
    fan-token/registry/bridge-supported.md?
    YES: apply OFFICIAL status; proceed with standard SportMind frameworks
    NO: proceed to Step 2
    
  STEP 2 — FOUR-SOURCE VERIFICATION:
    Run the four-source verification methodology from
    fan-token/official-verification-framework.md
    VERIFIED (all 4): apply OFFICIAL status; proceed
    LIKELY (3 sources): surface missing source; proceed with LIKELY_OFFICIAL caveat
    UNVERIFIED (≤2): flag; proceed to Step 3
    
  STEP 3 — RED FLAG ASSESSMENT:
    Apply the tier framework from this file.
    Any Tier 1 flag: surface immediately; output UNVERIFIED structure above
    Two or more Tier 2: surface elevated risk; output UNVERIFIED structure
    Tier 3 only: surface monitoring note; recommend verification
    
  STEP 4 — TOURNAMENT WINDOW CHECK:
    Is this occurring in a tournament risk window (4 weeks before/after major event)?
    YES: apply elevated scrutiny; require four-source verification for any new claim
    NO: standard verification applies
    
  STEP 5 — OUTPUT:
    Include verification status in any agent output involving this asset.
    Never proceed with price signals, demand modifiers, or PATH_2 calculations
    for an UNVERIFIED asset.
    Route all unverified queries to verification recommendation.
```

---

## What SportMind does and does not do

```
SPORTMIND DOES NOT:
  · Make legal determinations about specific assets
  · Classify any specific token as fraudulent
    (fraud is a legal determination requiring regulatory authority)
  · Provide financial or legal advice
  · Guarantee that verified assets are safe investments
  · Monitor real-time fraud activity or new launches continuously

SPORTMIND DOES:
  · Provide enduring reasoning frameworks for identifying verification signals
  · Surface red flags that warrant additional due diligence
  · Maintain a registry of confirmed official Fan Tokens™
  · Teach agents to reason about legitimacy signals systematically
  · Flag elevated risk during major tournament periods
  · Apply CLARITY Act Section 404 framework as a dual-purpose signal
    (passive yield promises = both fraud signal AND potential regulatory violation)
```

---

## Compatibility

**Verification methodology:** `fan-token/official-verification-framework.md`
**Registry files:**           `fan-token/registry/bridge-supported.md`
**CLARITY Act Section 404:**  `macro/macro-regulatory-sportfi.md`
**Ecosystem health:**         `fan-token/ecosystem-health-intelligence.md`
**Confidence framework:**     `core/signal-confidence-framework.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan token fraud risk intelligence: unofficial tokens, passive yield schemes, impersonation |
| Reasoning | ACTIVE | Fraud reasoning chain from red flag signals to fraud risk classification |
| Context | ACTIVE | Fraud context: World Cup window amplification, new token launches, passive yield promises |
| Memory | ACTIVE | Historical fraud pattern library and red flag signal catalogue |
| Judgment | ACTIVE | Highest judgment sensitivity: fraud signals require conservative threshold — false positives acceptable |
| Attention | ACTIVE | Maximum attention during World Cup fraud amplification window — ALL FOUR sources required |
| Communication | ACTIVE | Fraud risk output with risk level, red flags identified, and verification gaps |
| Verification | ACTIVE | Fraud assessment requires all four verification sources — single source is insufficient |
| Learning | ACTIVE | Fraud pattern library grows as new fraud types are identified and confirmed |
| Integration | ACTIVE | Integrates with official verification framework and US token taxonomy (Digital Collectible boundary) |
| Calibration | ACTIVE | Four-source verification framework is the calibrated standard for fraud detection |
| Adaptation | ACTIVE | Fraud intelligence adapts as new fraud mechanics emerge with new token launches |
| Ethics | ACTIVE | Fraud detection is a core ethics function — protects users from harmful schemes |
| Transparency | ACTIVE | Fraud risk level and specific red flags identified always explicit in output |


---

*SportMind v3.97.44 · MIT License · sportmind.dev*
*Red flags surface risk signals for verification — not fraud classifications.*
