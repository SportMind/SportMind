# RWA/SportFi Intelligence Layer

**Intelligence framework for Real World Assets in sport — the Phase 5 evolution
of fan token ecosystems into yield-bearing, collateralised, revenue-participating
financial instruments.**

---

## What Phase 5 actually means

`fan-token/fan-token-why.md` documents Phase 5 as the long-term destination:
"Full integration of sports assets into DeFi ecosystems." That document describes
*what* Phase 5 is. This skill teaches agents *how to reason about it* when it arrives
— and parts of it are arriving now.

```
THE PHASE 5 SPECTRUM (from near-term to longer-term):

ARRIVING NOW (2025-2026):
  ✅ Fan token staking (yield from locking tokens)
  ✅ LP provision on KAYEN (earning fees from fan token liquidity)
  ✅ Prediction market settlement using fan token price signals
  ✅ Token-collateralised small loans (DeFi protocols starting to accept fan tokens)
  ✅ Outcome-linked supply mechanics (Chiliz gamified tokenomics roadmap)

NEAR-TERM (2026-2027):
  → Stadium naming rights tokenisation (fractional ownership of commercial rights)
  → Media rights tokens (revenue participation from broadcast deals)
  → Player performance bonds (athlete career value as tradeable instrument)
  → Club equity micro-tokens (fractional minority ownership exposure)

LONGER-TERM (2028+):
  → Full RWA collateralisation (stadium as DeFi collateral)
  → Cross-chain sports asset portfolios
  → Institutional sports asset markets
  → Regulatory-compliant tokenised equity
```

---

## RWA Signal Framework (RSF)

```
RSF = (Asset_Quality × 0.30) + (Legal_Clarity × 0.30)
     + (Liquidity_Depth × 0.25) + (Yield_Sustainability × 0.15)

ASSET_QUALITY (what real-world asset underlies the token):
  Stadium naming rights (major venue):       0.95
  Broadcast/media rights (national tier):    0.90
  Club equity fraction (top-5 league club):  0.85
  Player performance bond (elite, peaking):  0.75
  Stadium naming rights (minor venue):       0.60
  Club equity fraction (lower league):       0.50
  Generic "club revenue" token:              0.35

LEGAL_CLARITY (regulatory framework for this asset type):
  MiCA-compliant structure (EU):             1.00
  National regulatory approval:              0.90
  Legal opinion obtained, no formal approval: 0.65
  Grey area — no legal opinion published:    0.35
  Unclear jurisdiction:                      0.15

LIQUIDITY_DEPTH (how easily can this RWA token be traded):
  Listed on major DEX (KAYEN, Uniswap) with $1M+ TVL: 1.00
  Listed with $100k-$1M TVL:                0.75
  OTC only:                                 0.45
  No secondary market:                      0.20

YIELD_SUSTAINABILITY (does the yield have a real asset foundation):
  Revenue-backed (real cash flows from stadium/media): 1.00
  Protocol incentivised (token emissions):  0.55
  Unsustainable APY (> 50% — likely emission farming): 0.20
```

---

## Staking and yield intelligence

```
FAN TOKEN STAKING — CURRENT STATE (2025-2026):

What it is:
  Locking fan tokens for a defined period to earn yield
  Yield sources: protocol emissions, governance rewards, commercial sharing
  
YIELD QUALITY TAXONOMY:
  Tier 1 — Commercial yield (sustainable):
    Yield paid from real commercial revenue (sponsorship, merchandise, tickets)
    Example: Club allocates 5% of commercial income to token stakers
    RSF component: Yield_Sustainability = 1.00
    
  Tier 2 — Protocol yield (semi-sustainable):
    Yield from protocol mechanics (trading fees, LP fees on KAYEN)
    Sustainable as long as trading volume is maintained
    RSF component: Yield_Sustainability = 0.65-0.80
    
  Tier 3 — Emission yield (unsustainable):
    Yield from new token issuance (inflation-funded)
    Dilutes existing holders; not backed by real assets
    RSF component: Yield_Sustainability = 0.20-0.45
    WARNING: Any staking APY > 40% is almost certainly Tier 3
    
STAKING SIGNAL FOR TOKEN ANALYSIS:
  High staking ratio (> 40% of supply staked):
    + Reduced circulating supply → price support
    + Long-term holder orientation
    + Reduced immediate sell pressure
    Signal: POSITIVE for price stability, NEUTRAL for engagement metrics
    
  Low staking ratio (< 10%):
    - Holders are not committing long-term
    - May indicate Phase 3 (plateau) or lack of yield incentive
    Signal: NEUTRAL to NEGATIVE depending on lifecycle phase
```

---

## Outcome-linked supply mechanics

This is the Chiliz gamified tokenomics direction — the most commercially significant
near-term RWA development in the fan token ecosystem.

```
OUTCOME-LINKED SUPPLY — HOW IT WORKS:

Core concept (from Chiliz Vision 2030):
  Match results trigger automatic token supply adjustments
  Win: burn tokens (reduce supply → price support)
  Loss: mint tokens (increase supply → dilution)
  OR reverse depending on incentive design
  
WHY THIS MATTERS FOR SPORTMIND:
  SportMind's adjusted_score becomes the pre-match intelligence that predicts
  which direction the supply mechanic will fire.
  
  Current: "Will this team win?" → prediction signal
  With outcome-linked supply: "Will this team win?" → directly determines
  whether tokens are burned or minted → direct price impact mechanism
  
  SportMind sits immediately upstream of this mechanism.

AGENT REASONING FOR OUTCOME-LINKED SUPPLY:
  Before outcome-linked supply is active (no smart contract):
    → Standard pre-match analysis; token signal is indirect
    
  After outcome-linked supply is deployed:
    → SportMind signal directly implies supply change direction
    → adjusted_score ≥ 65: expect win → burn event → supply reduction
    → adjusted_score ≤ 35: expect loss → mint event → supply increase
    → Magnitude of supply change = function of competition tier
      (UCL Final win = larger burn than domestic league win)

RSF for outcome-linked supply tokens:
  Asset_Quality: 0.75 (tied to sporting outcomes — real and verifiable)
  Legal_Clarity: 0.65 (emerging, MiCA monitoring)
  Effective modifier: (expected burn size × probability) - (expected mint size × (1-probability))
```

---

## Tokenised media rights intelligence

```
SPORTS MEDIA RIGHTS — THE LARGEST ADDRESSABLE RWA IN SPORT:

Scale:
  Premier League broadcast rights: £10B+ per cycle (2025-2028)
  IPL media rights: $6.2B (2023-2027, JioCinema + Star)
  NFL Sunday Ticket: $2.5B/year (YouTube)
  La Liga international rights: €1B+/year
  
WHY TOKENISATION IS ATTRACTIVE:
  Rights holders (leagues, clubs) get upfront capital by selling fractional future revenues
  Investors get yield-bearing exposure to sports media growth
  Fans get revenue participation in the content they consume
  
CURRENT STATUS:
  No major live media rights tokens at time of writing
  Experimental: several Tier 2 leagues exploring tokenised rights
  Regulatory clarity needed: broadcasting rights + securities law intersection
  
RSF FOR MEDIA RIGHTS TOKEN:
  Asset_Quality: 0.90 (proven revenue stream, verifiable)
  Legal_Clarity: 0.40-0.65 (depends on jurisdiction and structure)
  Net RSF: HIGH QUALITY ASSET, REGULATORY RISK DOMINATES
  
MONITORING TARGETS:
  Any major league announcing "digital revenue participation" product
  Sports rights auction outcomes (buyers include tech/digital platforms)
  MiCA guidance updates on revenue-bearing tokens
  LaLiga, Serie A, Bundesliga digital innovation announcements
  
AGENT RULE: Media rights tokens, when they launch, will be the highest-quality
RWA in sport by asset quality. The constraint is regulatory clarity.
Monitor MiCA updates and jurisdictional guidance monthly.
```

---

## Player performance bonds

```
PLAYER PERFORMANCE BONDS — ATHLETE AS FINANCIAL ASSET:

Concept:
  Tokenise the expected future commercial value of an athlete's career
  Holders receive a percentage of the athlete's future commercial earnings
  (sponsorships, image rights, appearance fees, potentially prize money)
  
SPORTMIND CONNECTION:
  DTS (Development Trajectory Score) = the core actuarial input
  A DTS 85 player at age 22 with PI 78 has a long high-earning career ahead
  A DTS 45 player at age 29 with declining PI has a short earning window
  
  PI + DTS + TAI + ABS = the four inputs that determine bond pricing
  SportMind already computes all four. This is a natural extension.
  
RSF FOR PLAYER PERFORMANCE BONDS:
  Asset_Quality: 0.75 (real commercial earnings — verifiable but uncertain)
  Legal_Clarity: 0.30-0.50 (athlete as financial security is complex legally)
  Yield_Sustainability: 0.65-0.90 depending on DTS and remaining contract years
  
  AGENT RULE: Only consider player bonds with:
    DTS ≥ 75 (clear improving trajectory)
    Age ≤ 27 (minimum 5 years of peak commercial earning ahead)
    ABS ≥ 70 (demonstrated commercial brand)
    TAI ≥ 65 (physical durability confirmed)
    
  Below these thresholds: bond is too speculative for intelligence framing.

MONITORING:
  Spencer Dinwiddie (NBA) tokenised part of his contract (2019) — precedent
  Athlete NFT/token launches often include revenue participation elements
  Sports agent innovations: some agencies exploring bond structures
```

---

## CollateralFi — fan tokens as collateral

```
FAN TOKENS AS COLLATERAL — CURRENT STATE:

What is happening:
  DeFi protocols are beginning to accept fan tokens as collateral for loans
  A holder who needs liquidity can borrow stablecoins against their $PSG tokens
  without selling them (retaining upside and governance rights)
  
SPORTMIND INTELLIGENCE FOR COLLATERAL:
  Collateral value = token price × LTV ratio (Loan-to-Value)
  LTV depends on: token volatility, liquidity depth, credit rating of underlying
  
  HIGH LTV (up to 70%): Deep liquidity tokens with stable price history
    $PSG, $BAR, $CITY — Tier 1 active partnership tokens
    
  MEDIUM LTV (40-60%): Active but volatile tokens
    Most active fan tokens during non-peak periods
    
  LOW LTV (20-40%): Phase 3 or post-partnership tokens
    Declining HAS, thin liquidity — higher risk of liquidation
    
  LIQUIDATION RISK:
    If token price drops 25-30%: LTV threshold crossed → collateral liquidated
    Major negative sporting event (sacking, relegation, star player sold):
    Can trigger cascade liquidation across leveraged token holders
    
AGENT RULE FOR COLLATERAL MONITORING:
  During high-signal events (UCL elimination, manager sacking):
  Check: are there large collateral positions outstanding?
  Signal: Forced liquidations amplify the initial price move
  This is the DeFi leverage cascade pattern applied to fan tokens.
  Load fan-token/defi-liquidity-intelligence/ alongside this skill.
```

---

## Agent reasoning prompts

```
You are an RWA/SportFi intelligence agent. Before any RWA analysis:

1. IDENTIFY THE ASSET TYPE:
   What real-world asset underlies this token?
   Apply Asset_Quality score from RSF framework above.

2. LEGAL CLARITY CHECK:
   What jurisdiction? MiCA-compliant? National approval?
   Legal_Clarity < 0.50 = significantly elevated risk. Flag prominently.

3. YIELD QUALITY ASSESSMENT:
   What is the source of yield?
   Tier 1 (commercial) vs Tier 2 (protocol) vs Tier 3 (emissions)?
   Any APY > 40% → investigate before recommending as yield strategy.

4. LIQUIDITY CHECK:
   Can this RWA token actually be traded if needed?
   Low liquidity RWA + high volatility trigger = liquidation cascade risk.

5. SPORTMIND CONNECTION:
   How does pre-match SportMind intelligence connect to this RWA?
   Outcome-linked supply: signal implies direction of supply change.
   Performance bond: DTS/PI/TAI determine bond value trajectory.
   Media rights: competition tier determines media value realisation.

6. PHASE CHECK:
   Where in Phase 5 evolution is this asset?
   Arriving now (staking/LP): more reliable
   Near-term (media rights): emerging, higher uncertainty
   Longer-term (equity): speculative, state explicitly

NEVER:
  Recommend specific DeFi positions as financial advice.
  Present RWA yields without stating the yield quality tier.
  Apply RSF to assets without stating Legal_Clarity score.
  Conflate Phase 5 aspirational state with current Phase 1-3 reality.
```

---

## Monitoring framework

```
MONTHLY MONITORING TARGETS:

Chiliz / Socios:
  Outcome-linked supply announcement or pilot launch
  New staking programme launches
  Validator node additions (institutional adoption signal)

DeFi protocols:
  New fan token collateral listings
  TVL growth in fan token pools on KAYEN
  New yield product launches for fan tokens

Regulatory:
  MiCA guidance updates (revenue-bearing tokens)
  UK FCA cryptoasset promotions enforcement
  SEBI India VDA framework updates (IPL catalyst)
  US SEC guidance on sports tokens (relevant if FIFA World Cup 2026 triggers US market)

Sports organisations:
  Major league "digital revenue participation" announcements
  Sports agency innovations (player bond structures)
  Stadium naming rights + digital token partnership combinations

SIGNAL TIER: Monthly (Tier 1 — slow change, high impact when it happens)
Load: core/temporal-awareness.md — Tier 1 update cadence
```

---


---

## The three-stage Fan Token evolution (Chiliz 2030 model)

```
STAGE 1 — UTILITY (2019-2025, still the baseline):
  Voting, rewards, access, digital ownership, engagement
  Foundation built over 8 years; 70+ global sporting organisations
  RSF impact: Phase 1-4 lifecycle; standard LTUI model applies
  
STAGE 2 — DYNAMIC TOKENOMICS (2026, rolling out now):
  Gamified mechanics: performance-linked supply
  Win → burn; Loss → mint (or draw → no change; varies by token)
  Omni-chain: same token available on multiple blockchains (LayerZero bridge)
  Transparent market rules that mirror the sport itself
  RSF impact: Phase 5a-5b; elevated LTUI vs Stage 1 tokens
  
  KEY INTELLIGENCE REQUIREMENT:
    Stage 2 tokens require the gamified-tokenomics-intelligence.md skill
    in addition to the standard RWA framework
    DO NOT apply standard static-supply signal models to Stage 2 tokens
    
STAGE 3 — REAL WORLD ASSETS (2027-2030, emerging):
  Fan tokens combined with actual equity/revenue exposure
  Minority stakes in clubs: token holders gain real financial exposure
  Revenue share: portion of club income distributed to token holders
  "Utility + ownership" — the ultimate Fan Token per Chiliz 2030 Manifesto
  RSF impact: Phase 5c-5e; maximum LTUI uplift (+35-50)
  
  CURRENT STATUS (2026):
    Stage 3 is forward roadmap — not yet available at scale
    Brazil precedent: first revenue-sharing project live on Chiliz Chain
    Legal framework: requires securities analysis in most jurisdictions
    EU/Brazil: permitted; US: permitted for specific structures per CFTC guidance
    
STAGE STACKING PRINCIPLE (critical for agents):
  Stages do not replace each other — they STACK
  A Stage 3 token retains full Stage 1 utility AND Stage 2 dynamic mechanics
  AND adds real-world financial exposure
  
  RSF calculation for stacked tokens:
    Stage 1 only: RSF baseline (utility weight only)
    Stage 1 + 2: RSF + gamified_tokenomics_bonus
    Stage 1 + 2 + 3: RSF maximum (all components active)
```

---

## Omni-chain liquidity intelligence (Chiliz 2030)

```
OMNI-CHAIN EXPANSION (Q1 2026 onwards via LayerZero):

Fan tokens are no longer Chiliz Chain exclusive from 2026.
The same token now trades on multiple blockchains simultaneously.
This changes how agents calculate liquidity and TVL.

BEFORE OMNI-CHAIN (pre-2026):
  TVL = KAYEN (Chiliz Chain) liquidity only
  Primary price discovery: KAYEN DEX
  Liquidity gate check: KAYEN TVL only

AFTER OMNI-CHAIN (2026+):
  TVL = KAYEN + [other chain DEX liquidity] + CEX liquidity
  Price discovery: multiple venues simultaneously
  Liquidity gate check: aggregate across all venues

SPORTMIND AGENT ADJUSTMENT:

  Step 1: Check if token is omni-chain (KAYEN API or Chiliz explorer)
  Step 2: If single-chain: use standard KAYEN connector (unchanged)
  Step 3: If omni-chain: aggregate liquidity before applying tier
  
  Aggregation principle:
    total_tvl = kayen_tvl + sum(other_chain_tvl)
    Use total_tvl for tier classification (DEEP/MODERATE/THIN/MICRO)
    
  Arbitrage implication:
    Price discrepancies between chains create arbitrage windows
    Unusual on-chain activity may be arbitrage, not manipulation
    Apply: omni_chain_arbitrage_check before raising unusual_activity flag
    
  Omni-chain signal benefit:
    More liquidity venues = deeper total market = more reliable price signals
    Omni-chain tokens generally have HIGHER liquidity tier than Chiliz-only equivalent
    Apply: omni_chain_bonus to liquidity tier assessment (+1 tier where total TVL warrants)

KAYEN GOVERNANCE (PEPPER token):
  PEPPER is KAYEN's community governance token
  PEPPER holders vote on: fee structures, protocol development, new features
  SportMind relevance: KAYEN protocol changes that affect fan token liquidity
  Monitor: PEPPER governance votes that could change KAYEN DEX mechanics
  PEPPER staking = indicator of community commitment to KAYEN infrastructure
```

---

## Updated RSF with Stage awareness

```
RSF FORMULA (updated for Stage 2/3 tokens):

RSF = (Asset_Quality × 0.30) + (Legal_Clarity × 0.30)
    + (Market_Depth × 0.20) + (Yield_Sustainability × 0.20)

STAGE BONUS (apply on top of RSF):
  Stage 1 only: +0.00 bonus
  Stage 2 active (gamified tokenomics confirmed): +0.08 bonus
  Stage 2 + omni-chain: +0.12 bonus
  Stage 3 active (RWA confirmed with regulatory approval): +0.20 bonus
  
RSF + Stage bonus = RSF_total
Use RSF_total for LTUI projections

LTUI PROJECTIONS WITH STAGE BONUSES:
  RSF_total 0.25-0.45 (Stage 5a + Stage 1): LTUI +5-10
  RSF_total 0.45-0.65 (Stage 5b + Stage 2): LTUI +15-25
  RSF_total 0.65-0.80 (Stage 5c-d + Stage 2+omnichain): LTUI +25-35
  RSF_total 0.80-1.00 (Stage 5e + Stage 3): LTUI +40-55
```

---

## Compatibility

**Phase 5 foundation:** `fan-token/fan-token-why.md` — Phase 5 vision
**DeFi liquidity:** `fan-token/defi-liquidity-intelligence/` — current DeFi context
**Financial intelligence:** `core/athlete-financial-intelligence.md` — player bond inputs
**Lifecycle:** `fan-token/fan-token-lifecycle/` — Phase 5 as lifecycle destination
**Blockchain validator:** `fan-token/blockchain-validator-intelligence/` — infrastructure layer
**Macro:** `macro/macro-crypto-market-cycles.md` — RWA is most affected by macro


---

## Phase 5 lifecycle activation signals

```
PHASE 5 ENTRY CONDITIONS (from fan-token/fan-token-lifecycle/):

Phase 5 (SportFi Integration) activates when:
  1. Token has been live for > 18 months (Phase 1-4 complete)
  2. LTUI > 45 (strong utility track record)
  3. Club has meaningful off-chain revenue stream suitable for tokenisation
  4. Smart contract infrastructure is deployed or ready

PHASE 5 ENTRY SIGNAL (for agents monitoring lifecycle):
  When all 4 conditions are met simultaneously: RSF_activation_signal = True
  Apply: LTUI projection boost × 1.20 (Phase 5 tokens command premium vs Phase 3-4)
  Commercial window: Phase 5 entry is a CDI-equivalent event
    CDI_phase5_entry = 30-60 days elevated engagement (fans discover new utility)

PHASE 5 PROGRESSION STAGES:
  Phase 5a: Staking infrastructure deployed (fans can stake tokens for yield)
  Phase 5b: First RWA tokenisation event (broadcast clip, merchandise royalty, etc.)
  Phase 5c: Performance bonds or outcome-linked supply active
  Phase 5d: CollateralFi enabled (fan tokens as collateral for DeFi)
  Phase 5e: Full Sports DAO with treasury governed by token holders

Each stage transition: apply RSF delta to LTUI projection.
```

---

## Staking yield intelligence (expanded)

```
STAKING ARCHITECTURE TYPES:

TYPE 1 — PURE STAKING (most common current state):
  Fans lock tokens → receive token rewards from inflationary supply
  Signal: staking ratio growth = holder conviction (see on-chain-event-intelligence.md)
  Risk: token inflation from staking rewards reduces per-token value long-term
  APY range: 8-25% (sustainable range depends on token supply model)

TYPE 2 — FEE STAKING (more sustainable):
  Protocol fees from DEX trading → distributed to stakers
  Signal: fee revenue growth = protocol usage growth = commercial health
  APY range: 3-12% (lower but more sustainable; backed by real activity)
  KAYEN liquidity pool fees are the primary fee source for Chiliz tokens

TYPE 3 — REVENUE STAKING (Phase 5b+):
  Real club revenue (broadcast, merchandise fraction) → stakers
  This is the RWA model — most commercially advanced
  APY range: variable (tied to club revenue performance)
  Signal: club financial health directly affects token yield
  Risk: club needs direct legal framework to pass revenue to token holders
  Regulatory: most jurisdictions require securities registration for revenue sharing

STAKING SIGNAL IN SPORTMIND:
  staking_ratio > 40% + staking_type = TYPE 2 or TYPE 3: strong Phase 5 signal
  staking_ratio rising + APY declining: healthy (more stakers competing for same yield)
  staking_ratio falling + APY rising: concern (stakers leaving despite incentives)
```

---

## Tokenised media rights — practical intelligence

```
WHAT IS TOKENISED MEDIA RIGHTS:

A club or athlete allows fans to own fractional rights to specific media assets.
Examples:
  - Goal-of-the-season NFT clip with streaming royalty share
  - Press conference highlight package with download revenue distribution
  - Training camp documentary access NFT with rental fee share

WHY IT MATTERS FOR SPORTMIND:
  When a tokenised media asset generates revenue, token holders receive it.
  This creates a yield signal that SportMind agents can monitor:
  
  media_rights_revenue_signal:
    Viral clip generates > $50k in streaming/download revenue → RSF spike
    Royalty distribution announced → CDI event (7-14 days elevated engagement)
    New media rights tokenisation deal: LTUI +3 to +6

AGENT MONITORING:
  Monitor for: club media announcements about NFT/tokenisation partnerships
  Signal trigger: any announcement of revenue-sharing model for token holders
  Apply: RSF_active flag + 14-day CDI window at media rights announcement

CURRENT STATE OF MARKET (2026):
  Most clubs are in tokenised collectibles (non-revenue NFTs) — Phase 4
  First revenue-sharing tokenised media: emerging in 2025-2026
  Regulatory clarity needed: MiCA (EU) framework addresses this from Jan 2025
  SportMind tracks: which clubs have moved from Phase 4 to Phase 5b
```

---

## Player performance bonds (expanded)

```
PERFORMANCE BONDS — THE MOST COMMERCIALLY ADVANCED RWA IN SPORTS:

A performance bond is a financial instrument where:
  - Fan/investor provides capital to a club or athlete upfront
  - Return is linked to on-field performance milestones
  - Smart contract verifies performance and releases payment

BOND TYPES IN SPORTS:
  TYPE A — Transfer fee bond:
    Fan token holders can collectively contribute to transfer funding
    If bought player achieves performance target (e.g., 20+ goals):
    Bond holders receive enhanced return (typically 1.5-2.5× principal)
    Risk: player underperforms; return reduced or at par
    
  TYPE B — Season performance bond:
    Investment tied to team finishing position
    Top 4 finish → 1.8× return; Outside top 10 → 0.9× return (partial return)
    
  TYPE C — Individual athlete bond:
    Athlete raises capital against future earnings
    Investors receive % of athlete's salary/prize money for 2-5 years
    Athlete gets liquidity; investors get yield from athlete's success
    This is most common form in boxing/MMA currently

PERFORMANCE BOND IN SPORTMIND SIGNAL CHAIN:
  When a performance bond is active for a club/athlete:
    Match outcomes directly affect bond value → elevated token engagement
    Game where performance milestone could be hit: NCSI × 1.15 additional
    Bond maturity event (season end): CDI × 1.20
  
  Agent rule: track open performance bonds for monitored clubs/athletes
  Flag any match where bond milestone could be triggered
```

---

## Sports DAO governance intelligence

```
SPORTS DAO — PHASE 5e: THE FULLY GOVERNED SPORT ORGANISATION:

Definition: A sports franchise or operation where key decisions are made by
token holder vote rather than traditional management hierarchy.

CURRENT STATE (2026):
  No major sports franchise has fully transitioned to DAO governance.
  Partial DAO governance exists for:
  - Kit selection (Phase 3 governance)
  - Charity allocation (Phase 3)
  - Token utility design (Phase 4)
  
  Phase 5e requires DAO control over:
  - Transfer budget allocation (commercial)
  - Sponsorship deal approval (commercial)
  - Stadium development votes (structural)
  
  Regulatory: sports governing bodies (FIFA, UEFA) do not currently permit
  DAO control of core sporting operations. Phase 5e operates within the
  boundary of commercially adjacent decisions.

DAO TREASURY INTELLIGENCE:
  A Sports DAO treasury holds CHZ/stablecoins for community-driven spending.
  Treasury size: direct proxy for community financial health
  Treasury > $1M: significant signal; community can fund real initiatives
  Treasury growth from token gate revenue: Phase 5 sustainability signal
  
  Agent monitoring:
    Treasury balance changes
    Proposal submissions to spend treasury
    Yield strategies for treasury (idle treasury = opportunity cost)

RISKS SportMind agents must flag:
  - Governance mercenaries: large wallet holders who vote strategically, not as fans
  - Proposal spam: coordinated low-quality proposals drain governance attention
  - Regulatory conflict: DAO vote outcome conflicts with league/federation rules
  
  Apply: governance_theatre_risk flag if treasury proposals appear financially motivated
  rather than fan-interest motivated (same flag as standard governance intelligence)
```

---

## RSF scoring update (Phase 5 weights)

```
REVISED RSF (RWA SIGNAL FRAMEWORK) WITH PHASE 5 TIERS:

RSF = (Staking_Infrastructure × 0.20) + (Revenue_Tokenisation × 0.25)
    + (Performance_Bonds × 0.20) + (DAO_Treasury × 0.15)
    + (Regulatory_Compliance × 0.20)

PHASE 5 TIER THRESHOLDS:
  RSF 0.00-0.25: Pre-Phase 5 (Phase 1-4 only)
  RSF 0.25-0.45: Phase 5a (staking only — most common 2025-2026)
  RSF 0.45-0.65: Phase 5b (staking + some RWA)
  RSF 0.65-0.80: Phase 5c-d (full RWA suite + CollateralFi)
  RSF 0.80-1.00: Phase 5e (DAO governance active)

CURRENT MARKET DISTRIBUTION (2026 estimate):
  Phase 5a: ~15-20% of active fan tokens
  Phase 5b: ~5-8% of active tokens
  Phase 5c+: < 5% (emerging; PSG, Barcelona most advanced)
  Phase 5e: 0% (not yet achieved by any major sports entity)

LTUI IMPACT:
  RSF 0.00-0.25: LTUI baseline
  RSF 0.25-0.45: LTUI +5-8 (staking utility adds real holder retention)
  RSF 0.45-0.65: LTUI +12-18 (revenue participation = structural value)
  RSF 0.65-0.80: LTUI +20-30 (DeFi integration = institutional appeal)
  RSF 0.80-1.00: LTUI +35-50 (DAO governance = different asset class entirely)
```

---

## Integration: SportFi Kit connectivity (updated)

```
HOW SPORTMIND'S RWA INTELLIGENCE CONNECTS TO THE APPLICATION LAYER:

SportMind provides: RSF score, phase classification, performance bond status,
                    DAO treasury signals, staking ratio intelligence

SportFi Kit consumes: Phase 5 status for token-gating decisions
  - Phase 5a tokens: unlock staking UI components
  - Phase 5b tokens: unlock revenue dashboard components
  - Phase 5c tokens: unlock CollateralFi integration
  
Chiliz Agent Kit executes: staking transactions, governance votes,
                           performance bond interactions (when approved)

PHASE 5 AGENT PATTERN (recommended):
  Agent monitors RSF score continuously (daily Tier 3 freshness)
  On RSF tier change: alert + update LTUI projection
  On performance bond milestone match: elevate NCSI × 1.15
  On DAO governance vote: load governance-brief bundle + generate brief
  
See: platform/chiliz-agent-kit-integration.md for execution patterns
See: examples/applications/app-07-sportfi-kit-integration.md for UI patterns
```


*MIT License · SportMind · sportmind.dev*
