---
name: exchange-intelligence
description: >
  Enduring reasoning framework for crypto exchange activity as it affects fan
  token accessibility, liquidity, and demand signals. Covers listing/delisting
  tiers, migration and upgrade events, exchange regulatory status, traditional
  finance signals, and market maker intelligence. Scoped to structural
  reasoning only — not live trading data.
---

# Exchange Intelligence

**How to reason about exchange activity as fan token accessibility and demand signals.**
Not live trading data — structural reasoning about exchange events and their effects.

> Extends: `macro/crypto-digital-asset-intelligence.md` (CHZ listing entry at ×1.08)
> This file adds the full exchange tiering, delisting, migration, and TradFi frameworks.

---

## Exchange tier classification

```
EXCHANGE TIER FRAMEWORK:

  TIER 1 — GLOBAL DOMINANT EXCHANGES:
    Definition: top global exchanges by volume, regulatory standing, and global reach
    Examples: Binance, Coinbase, Kraken
    Signal weight: HIGHEST — Tier 1 listings reach the largest potential holder base
    
  TIER 2 — MAJOR REGIONAL/SPECIALIST EXCHANGES:
    Definition: significant volume; regional or specialist dominance
    Examples: KuCoin, Bybit, OKX, Bitfinex
    Signal weight: MODERATE — meaningful but smaller holder base expansion
    
  TIER 3 — SMALLER / REGIONAL EXCHANGES:
    Definition: limited volume; primarily regional or niche audience
    Signal weight: LOW — minimal holder base expansion; low liquidity signal
    
  CHZ NATIVE PLATFORM:
    Socios.com and FanToken.com are primary distribution platforms for fan tokens.
    These are not exchanges in the crypto sense — they are the fan token ecosystem.
    Activity on these platforms is a direct CDI signal (see fan-token files).
    Exchange listings are secondary market access points, not primary distribution.
```

---

## Exchange listing framework

```
FAN TOKEN LISTING ON NEW EXCHANGE:

  TIER 1 LISTING (Binance, Coinbase, Kraken):
    Signal: major accessibility unlock — token reaches the largest global retail base
    Demand spike: +20-40% typical at listing
    Duration: 1-2 weeks then decay to new baseline
    New structural baseline: +15-25% above pre-listing baseline
    Mechanism: new holder segment can now buy without visiting the Socios platform;
      price discovery improves; trading volume increases; media coverage amplified
      
  TIER 2 LISTING (KuCoin, Bybit, OKX):
    Signal: moderate accessibility expansion
    Demand spike: +10-20% at listing
    Duration: 5-10 days then new baseline
    New structural baseline: +5-10% above pre-listing baseline
    
  TIER 3 LISTING:
    Signal: minimal demand impact — primarily signals ecosystem activity, not access
    Apply: ×1.02 sentiment modifier (marginal positive)
    No material baseline change expected
    
  MULTIPLE SIMULTANEOUS LISTINGS (same token on 2+ exchanges in same week):
    Amplified signal: compound the tier modifiers (not additive)
    Example: Tier 2 + Tier 2 simultaneously = ×1.20 combined (+20%)
    Cap: combined listing spike capped at ×1.40 regardless of tier combination
    
CHZ LISTING ON NEW EXCHANGE:
  CHZ is the ecosystem's native token. New CHZ listings amplify ecosystem access.
  Tier 1 CHZ listing: ×1.08-1.12 sustained to all fan token demand signals
  (See crypto-digital-asset-intelligence.md market structure section for full detail)
  
AGENT RULE:
  Confirm listing via official exchange announcement (Tier 1 source).
  Do not apply listing modifier based on unconfirmed reports.
  Source: exchange official blog / announcement channel.
```

---

## Delisting framework

```
FAN TOKEN DELISTED FROM EXCHANGE:

  TIER 1 DELISTING (Binance, Coinbase, Kraken):
    Signal: significant negative liquidity event — largest holder segment loses access
    Demand decay: −20-35% sustained
    Recovery timeline: 8-16 weeks if relisting confirmed on another Tier 1 exchange
    Mechanism: forced selling from holders who cannot or will not migrate to other platforms;
      reduced price discovery; negative media narrative ("delisted from X")
    Apply: delisting_decay_modifier until relisting confirmed or new baseline established
    
  TIER 2 DELISTING:
    Demand decay: −10-20% sustained
    Recovery: 4-8 weeks to new lower baseline
    
  CHZ DELISTED FROM MAJOR EXCHANGE:
    Ecosystem-wide negative signal — affects all fan tokens simultaneously
    Apply: chz_delisting_signal = ×0.82 across all fan token demand signals
    This is one of the most severe ecosystem-wide negative signals in the framework
    Duration: sustained until relisting confirmed
    Monitor: official Chiliz/CHZ team communications as primary source
    
  VOLUNTARY DELISTING (exchange regulatory exit from jurisdiction):
    Distinguish from performance-driven delisting:
    Regulatory exit = exchange is leaving a jurisdiction (not rejecting the token)
    Apply: regional_access_modifier ×0.88 for the affected jurisdiction only
    Global access is preserved — only the specific jurisdiction is affected.
```

---

## Migration and upgrade events

```
CONTRACT MIGRATION EVENTS (e.g. V2 CAP20 standard):

  CONFIRMED AND OFFICIALLY ANNOUNCED MIGRATION:
    Context: Chiliz has migrated tokens to improved contract standards (CAP20/V2).
    Official confirmation from Chiliz: migration is a positive technical signal.
    
  SUSPENSION DURATION FRAMEWORK:
    Deposits and withdrawals suspended during migration is EXPECTED.
    
    Duration < 7 days:
      neutral_signal = true — part of standard upgrade process
      No demand modifier applied; flag as MIGRATION_IN_PROGRESS
      
    Duration 7-14 days:
      mild_uncertainty_signal = ×0.97 — slightly longer than expected
      
    Duration > 14 days:
      uncertainty_signal = ×0.94 — flag for human review
      Investigate: is delay technical or commercial?
      
  POST-MIGRATION SIGNAL:
    Successful migration completion: positive signal
    Apply: migration_completion_modifier = ×1.03 for 1-2 weeks post-completion
    Mechanism: technical upgrade removes uncertainty; improved functionality

18-DECIMAL PRECISION MIGRATION:
  Context: fan tokens upgraded to 18-decimal precision (ERC-20 standard).
  Signal: positive technical maturity indicator
  Apply: decimal_upgrade_modifier = ×1.03 sustained
  Mechanism: enables micro-transactions, DeFi integration, omnichain bridge compatibility
  This is a one-time structural upgrade — remove modifier once baseline resets.
  
BRIDGE UPGRADE (new chain support added):
  New chain support (Base, Solana, future chains):
    Apply: new_chain_accessibility_modifier = ×1.05 at launch
    Settled sustained: ×1.02 (permanent accessibility improvement)
```

---

## Exchange regulatory status

```
EXCHANGE LOSES OPERATING LICENCE IN KEY JURISDICTION:

  Signal: fan token accessibility reduced for all users in that jurisdiction
  Apply: regional_access_modifier = ×0.88 for affected jurisdiction
  Global demand modifier: ×0.96 if the jurisdiction has >20% of the token's holder base
  Monitor: which jurisdiction? Map to fan token's known holder base concentration.
  
  KEY JURISDICTIONS (where licence loss has material fan token impact):
    USA (if major US exchange loses licence): significant impact given US holder base
    UK (FCA licence): affects UK Premier League token holder base most
    EU (MiCA compliance loss): affects broader EU holder base
    Apply the regional modifier scaled to the jurisdiction's holder base proportion.

EXCHANGE GAINS REGULATORY APPROVAL IN NEW JURISDICTION:
  Signal: positive accessibility expansion
  Apply: new_jurisdiction_access_modifier = ×1.05 for tokens on that exchange
  Map: does the new jurisdiction represent meaningful potential holder demand?
  High-value jurisdiction (US, UK, EU, UAE): full ×1.05 modifier
  Smaller jurisdiction: ×1.02 (minor but positive)
```

---

## Traditional finance signals

```
SPORTS CLUB STOCK PERFORMANCE — SENTIMENT BRIDGE:

  PUBLICLY LISTED CLUBS WITH ASSOCIATED FAN TOKENS:
    Certain sports clubs are publicly traded (Juventus, Manchester United,
    Borussia Dortmund, Ajax, others). Their stock performance creates a
    parallel sentiment signal for the associated fan token.
    
  WHY THIS MATTERS:
    Institutional and retail equity holders are a related-but-different holder
    segment from fan token holders. Sentiment flows between the two when
    club news affects both simultaneously.
    
  STOCK AT 52-WEEK HIGH:
    positive sentiment signal for fan token
    Apply: stock_high_sentiment_modifier = ×1.03
    Mechanism: club commercial health is signalled; positive media attention;
      holders feel confident about club trajectory
    Duration: while stock remains at or near 52-week high
    
  STOCK AT 52-WEEK LOW:
    negative sentiment signal for fan token
    Apply: stock_low_sentiment_modifier = ×0.96
    Mechanism: club financial health concerns; negative media; holder uncertainty
    Duration: while stock remains near 52-week low
    
  CLUBS CURRENTLY LISTED (as of library state):
    Confirm current listed status before applying — clubs can delist or relist.
    Source: major exchange listings (NYSE, LSE, Euronext) for relevant clubs.
    
  NOTE:
    Stock performance is a correlation signal, not a causation signal.
    Do not assume fan token will mirror stock performance tick for tick.
    Apply the sentiment modifier, not a price correlation modifier.

SPORTS MEDIA M&A:
  Broadcast rights consolidation or media company M&A activity in sports:
    Affects commercial context for clubs with fan tokens (broadcast revenue).
    Apply: broadcast_commercial_modifier — see core/broadcast-media-intelligence.md
    for the full broadcast and media framework.
    This file notes the signal exists; the detail is in the broadcast file.
```

---

## Market maker intelligence

```
MARKET MAKER PRESENCE AND WITHDRAWAL:

  WHY MARKET MAKERS MATTER:
    Professional market makers provide bid-ask liquidity — ensuring there is
    always a buyer and seller near the current price. Without market makers,
    spreads widen significantly, making casual trading expensive.
    
  PROFESSIONAL MARKET MAKER CONFIRMED PRESENT:
    Positive liquidity signal — tighter spreads, lower transaction friction
    Apply: market_maker_presence_signal = ×1.03 to demand signal confidence
    (Not a direct demand modifier — a signal reliability amplifier)
    Mechanism: wider participation is enabled when spreads are tight
    
  MARKET MAKER WITHDRAWAL:
    Negative liquidity signal — wider spreads, higher transaction friction
    Apply: market_maker_withdrawal_signal = ×0.94 sustained until new MM confirmed
    Mechanism: holders face higher costs to enter or exit; casual traders deterred;
      price volatility increases (thin order book)
    
  HOW TO IDENTIFY MARKET MAKER PRESENCE:
    Tight and consistent bid-ask spreads on exchange (below 0.5%)
    Consistent depth on both sides of the order book
    Market maker disclosures (some exchanges publish MM agreements)
    Source: exchange order book data (publicly visible)
    
  CHILIZ OFFICIAL MARKET MAKING:
    Chiliz Group or associated entities may provide market making for fan tokens
    on Socios/FanToken.com. Official ecosystem market making is a positive
    structural signal — apply ×1.03 confidence modifier for officially confirmed cases.
```

---

## Compatibility

**CHZ listing entry:**      `macro/crypto-digital-asset-intelligence.md` (×1.08-1.12 entry)
**Regulatory layer:**       `macro/macro-regulatory-sportfi.md`
**Institutional context:**  `macro/institutional-intelligence.md`
**Broadcast bridge:**       `core/broadcast-media-intelligence.md`
**Token lifecycle:**        `fan-token/fan-token-lifecycle/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Crypto exchange macro intelligence: venue health, liquidity signals, and regulatory status |
| Reasoning | ACTIVE | Exchange intelligence reasoning chain from venue signals to macro liquidity modifier |
| Context | ACTIVE | Exchange context: CEX vs DEX, regulatory status, volume trends, insolvency risk |
| Memory | ACTIVE | Historical exchange failure patterns (FTX, Celsius) and market impact data |
| Judgment | ACTIVE | Judgment on exchange signal materiality — regulated vs unregulated exchange risk differs |
| Attention | ACTIVE | Maximum attention for exchange insolvency signals and regulatory enforcement actions |
| Communication | ACTIVE | Exchange output with venue health, regulatory status, and macro liquidity modifier |
| Verification | ACTIVE | Exchange solvency signals require official regulatory filings — social media insufficient |
| Learning | ACTIVE | Exchange failure pattern calibration from historical insolvency event data |
| Integration | ACTIVE | Integrates with crypto-digital-asset-intelligence and fan token exchange intelligence |
| Calibration | ACTIVE | Exchange risk modifiers calibrated from historical venue failure-to-market impact data |
| Adaptation | ACTIVE | Exchange intelligence adapts as regulated markets expand and offshore venues decline |
| Ethics | ACTIVE | Exchange insolvency signals affect user funds — accuracy is a safety-relevant ethics requirement |
| Transparency | ACTIVE | Exchange venue, regulatory status, and risk classification always explicit in output |


---

*SportMind v3.97.40 · MIT License · sportmind.dev*
*Confirm all listing/delisting events via official exchange announcement (Tier 1 source)*
