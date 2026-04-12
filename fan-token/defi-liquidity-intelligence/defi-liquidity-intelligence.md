# DeFi and Liquidity Intelligence — SportMind Layer 3

DeFi (Decentralised Finance) is the financial infrastructure layer beneath fan tokens
in their mature form. This skill gives AI agents and developers the framework to reason
about fan tokens as DeFi-native assets — not just as prediction instruments.

**Scope:** DeFi concepts as they apply specifically to sports assets and fan tokens.
This is not a general DeFi education. It covers the mechanics that directly affect
how agents should reason about fan token signals, liquidity, yield, and prediction markets.

---

## Why DeFi context changes agent reasoning

Without DeFi context, an agent treats a fan token signal as binary — bullish or bearish
based on sporting events, social sentiment, and macro conditions.

With DeFi context, the agent also asks:

```
DEFI INTELLIGENCE QUESTIONS:
  1. Is there sufficient liquidity to execute this signal without adverse slippage?
  2. Is LP activity signalling accumulation or distribution ahead of this event?
  3. Is this token generating on-chain yield — and does that change the exit calculus?
  4. Is this token in a prediction market pool — and what does pool liquidity say
     about market conviction?
  5. Is this token in Phase 5/6 (non-contractual, DEX-primary) — and what does
     that mean for price discovery mechanics?

These are not optional refinements. For tokens with thin liquidity or DEX-primary
trading, they are the MOST important questions an agent can ask.
```

---

## 1. Liquidity pools — what they are for sports assets

### The mechanics

```
AUTOMATED MARKET MAKER (AMM):
  Most DEX trading uses AMM protocols (Uniswap v2/v3, PancakeSwap, Chiliz DEX)
  Instead of an order book, price is set by a constant formula:
    x × y = k  (reserves of Token A × reserves of Token B = constant)
  
  This means: price moves with every trade proportional to pool size
  A $10,000 buy in a $100,000 pool moves price more than the same buy
  in a $10,000,000 pool

LIQUIDITY POOL (LP):
  Two assets locked in a smart contract, e.g. $PSG / USDC
  LP providers deposit both assets and receive LP tokens representing their share
  Traders swap against the pool; LP providers earn a % of fees on each swap
  
FAN TOKEN POOLS IN PRACTICE:
  Most fan tokens trade primarily on Binance (CEX) for major tokens
  DEX pools exist on:
    - Chiliz DEX (chiliz.net/dex) — native Chiliz Chain DEX
    - Uniswap (via Chiliz Chain bridge or wrapped tokens)
    - PancakeSwap (some tokens bridged to BNB Chain)
  
  For non-contractual Phase 6 tokens: DEX becomes the PRIMARY or ONLY venue
  
SOURCES:
  DeFiLlama (defillama.com) — TVL and pool data for most major DEXs
  GeckoTerminal (geckoterminal.com) — real-time DEX pool data
  Dune Analytics (dune.com) — custom dashboards for Chiliz DEX activity
  Chiliz DEX (chiliz.net/dex) — native pool data
```

### TVL (Total Value Locked) as a signal

```
TVL = Total value of assets locked in a liquidity pool
    = (Token A reserve × Token A price) + (Token B reserve × Token B price)

TVL SIGNAL INTERPRETATION FOR FAN TOKENS:

TVL > $5M:          Deep liquidity — agents can act on signals without slippage concern
                    Large buys/sells absorbed without significant price impact
                    
TVL $500k–$5M:      Moderate liquidity — standard position sizes workable
                    Large positions require splitting across time to avoid slippage
                    
TVL $100k–$500k:    Thin liquidity — signal is valid but execution is constrained
                    Apply: LIQUIDITY_WARNING flag; reduce position size to 40%
                    
TVL < $100k:        Very thin liquidity — even moderate positions move price significantly
                    Apply: LIQUIDITY_CRITICAL flag; do not act on signals > 0.5× standard size
                    Prediction accuracy is irrelevant if execution cost exceeds signal value

AGENT PRE-EXECUTION RULE:
  Check TVL BEFORE applying any SportMind signal modifier
  If TVL_WARNING or TVL_CRITICAL flags are active:
  → Adjust position size DOWN regardless of signal confidence
  → High confidence + thin liquidity = reduced size, not full entry
```

---

## 2. Slippage — the hidden execution cost

```
SLIPPAGE DEFINITION:
  The difference between the expected price of a trade and the executed price.
  Caused by moving along the AMM price curve during execution.

SLIPPAGE ESTIMATION FOR FAN TOKENS:

For a trade of size S in a pool with TVL of P:
  Estimated price impact ≈ S / (P/2) × 100%
  
  Example: $10,000 trade in a $200,000 TVL pool
  Impact ≈ $10,000 / $100,000 × 100% = 10% price impact
  (You move the price 10% against yourself just by trading)

PRACTICAL SLIPPAGE THRESHOLDS:
  < 0.5% impact: Clean execution — trade normally
  0.5–1.0% impact: Acceptable — slight degradation vs signal value
  1.0–3.0% impact: Meaningful — split into smaller tranches over time
  > 3.0% impact: Significant — execution cost may exceed signal value; REDUCE or ABSTAIN

SLIPPAGE CALCULATOR FOR AGENTS:
  trade_size_usd = [position in dollars]
  pool_tvl_usd = [from GeckoTerminal or DeFiLlama]
  estimated_impact_pct = (trade_size_usd / (pool_tvl_usd / 2)) × 100
  
  if estimated_impact_pct > 3.0:
    apply LIQUIDITY_CRITICAL flag
    recommended_action = ABSTAIN or dramatically reduced size
```

---

## 3. LP activity as an on-chain signal

LP additions and removals are detectable on-chain and carry signal value distinct
from price action.

```
LP ADDITION SIGNALS:

Large LP addition from new wallet cluster:
  → Institutional or informed accumulation signal
  → NEW money entering the pool = expectation of upcoming positive catalyst
  → Cross-reference with: upcoming sporting event, partnership announcement,
    transfer window, major competition
  → Expected signal: POSITIVE; moderate weight (not definitive alone)

LP addition from known club/partner wallet:
  → Very strong positive signal — insider confidence
  → Validator clubs adding to their own token pool = deepest conviction signal

Gradual LP additions over multiple days:
  → Patient accumulation; likely pre-event positioning
  → Less urgent than single large addition

LP REMOVAL SIGNALS:

Large LP removal ahead of major event:
  → Can mean: profit-taking, hedging before uncertain outcome, liquidity needs
  → Do NOT automatically interpret as bearish — could be neutral
  → Cross-reference with: current price trend, recent social signals, club news

Complete LP removal (pool draining):
  → Significant warning signal — large holder exiting entirely
  → If combined with declining utility events: potential Phase 4→5 transition
  → Apply: PHS reassessment immediately

MONITORING TOOL:
  Dune Analytics — custom query: track LP add/remove events by pool address
  GeckoTerminal — pool transaction history
  Chiliz Explorer — wallet-level LP position tracking
```

---

## 4. DEX vs CEX price discovery — what agents need to know

```
CEX (CENTRALISED EXCHANGE) PRICE DISCOVERY:
  Set by order book matching (Binance, Bybit, etc.)
  Deep liquidity; low slippage for most fan tokens
  Subject to: wash trading, spoofing, coordinated manipulation
  Source of truth for: most Tier 1 active tokens ($BAR, $PSG, $CHZ)
  
DEX (DECENTRALISED EXCHANGE) PRICE DISCOVERY:
  Set by AMM formula — purely algorithmic
  No order book; price is a function of pool reserves
  Subject to: sandwich attacks, MEV, thin liquidity price manipulation
  Source of truth for: Phase 6 non-contractual tokens; newer/smaller tokens

WHEN PRICE DIVERGES BETWEEN CEX AND DEX:
  CEX price > DEX price: Arbitrageurs will buy DEX and sell CEX until equalised
  DEX price > CEX price: Reverse arbitrage
  
  Persistent divergence (>2%) without arbitrage closure:
    → Signals a breakdown in arbitrage mechanism
    → Usually means: CEX has delisted or restricted trading
    → For fan tokens: this is a Phase transition signal (CEX → DEX-primary)
    → Cross-reference with: Socios/Binance announcements

AGENT RULE:
  For Tier 1 active tokens: use CEX price as primary source
  For Phase 5/6 non-contractual tokens: use DEX price as primary source
  For any token showing persistent CEX/DEX divergence: 
    apply lifecycle reassessment immediately
```

---

## 5. On-chain yield — sports assets as yield-generating instruments

Fan tokens can generate yield through multiple DeFi mechanisms. An agent that
understands yield sources reasons differently about token holding incentives.

```
YIELD SOURCES FOR SPORTS ASSETS:

1. LIQUIDITY PROVISION (LP YIELD):
   By providing liquidity to a fan token pool, holders earn:
   - Trading fees (typically 0.2–0.3% of each swap)
   - Incentive tokens (some protocols pay additional rewards for fan token LPs)
   
   Yield calculation:
   APR = (Annual trading fees for pool) / TVL × 100%
   
   High-volume pools (e.g. $CHZ/USDC during Champions League): 5–15% APR
   Low-volume pools (off-season, non-contractual tokens): <1% APR
   
   RISK: Impermanent loss — if token price moves significantly vs pair asset,
   LP position loses value vs simply holding the token

2. STAKING YIELD (VALIDATOR REWARDS):
   Covered in blockchain-validator-intelligence.md
   PSG earns CHZ rewards from securing Chiliz Chain
   Staking APY varies with: total staked CHZ, network activity, tokenomics
   
3. PREDICTION MARKET LIQUIDITY PROVISION:
   Protocols like Azuro, Polymarket operate prediction markets
   Liquidity providers stake funds into prediction pools
   Earn yield from the spread between prediction prices and actual outcomes
   
   For sports: providing liquidity to a match outcome pool earns fees
   regardless of the sporting result — but LPs bear risk if outcomes are
   heavily one-sided (they effectively take the other side of all bets)

4. LENDING PROTOCOL COLLATERAL:
   Some DeFi protocols accept fan tokens as collateral for loans
   Token holder borrows USDC/ETH against their $BAR position
   Enables leverage without selling; also generates interest for lenders
   Currently limited to CHZ on major protocols; fan tokens primarily niche
   
YIELD AS A HOLDING INCENTIVE:
  An agent should model yield when reasoning about holder behaviour.
  A holder earning 8% APR from LP provision has a different exit calculus
  than a holder earning 0%.
  Higher yield → higher stickiness → lower sell pressure in bear conditions
  This modifies the HAS (Holder Activity Score) interpretation:
    High HAS + high LP yield: holders are engaged AND economically locked in
    High HAS + zero yield: engagement without economic alignment (more fragile)
```

---

## 6. Prediction markets as DeFi infrastructure

```
WHAT PREDICTION MARKET PROTOCOLS ARE:
  Smart contract systems where participants bet on real-world outcomes
  Outcomes are settled on-chain using oracle data (Chainlink, UMA, etc.)
  No central counterparty — the protocol is the house
  
KEY PROTOCOLS FOR SPORTS:
  Azuro (azuro.org): 
    Sports prediction market infrastructure protocol
    Enables any dApp to build prediction markets using Azuro's liquidity
    Backed by Chiliz-adjacent investors; sports focus
    Sports data: Chainlink sports oracle
    
  Polymarket (polymarket.com):
    General prediction market; significant sports coverage
    USDC-settled; real-money predictions
    High profile events (World Cup, major boxing, Wimbledon) have deep pools
    
  Betswap.gg / BookiePro: 
    On-chain sports betting infrastructure

WHAT PREDICTION MARKET POOL DATA TELLS AGENTS:
  Pool size = market conviction
    Large pool on a match outcome: many participants have studied this event
    → More reliable odds signal than thin pool
    
  Odds movement in pool = informed betting activity
    Pool odds moving away from market consensus: watch for information asymmetry
    → Could precede injury news, weather changes, selection surprises
    
  Pool TVL growing rapidly before event: increased engagement signal
    → Positive for related fan token (narrative momentum + engagement)
    → Cross-reference with: social volume, athlete social lift (AELS)

AGENT RULE: When operating in prediction market contexts, treat pool TVL as an
additional signal confidence multiplier. Deep pools = higher reliability odds.
Thin pools = wider uncertainty; treat with same caution as thin LP liquidity.
```

---

## 7. The DeFi lifecycle — how fan tokens move through DeFi phases

```
PHASE 1 (Active partnership, CEX-primary):
  DeFi role: minimal; small DEX pools exist but CEX dominates
  Agent approach: ignore DEX data; use CEX price and volume
  Liquidity check: TVL check is precautionary only

PHASE 2 (Partnership plateau, CEX beginning to reduce):
  DeFi role: DEX pool activity beginning to grow
  Agent approach: monitor both CEX and DEX; check for divergence
  Liquidity check: TVL check is material; flag if < $500k

PHASE 3 (Post-partnership, transitioning to DEX-primary):
  DeFi role: DEX becomes primary price discovery venue
  Agent approach: DEX price is source of truth; LP activity = primary signal
  Liquidity check: TVL check is CRITICAL; slippage calculation required before any signal action
  Yield signal: LP yield may be primary holder incentive now; check APR

PHASE 4 (Non-contractual, DEX-primary):
  DeFi role: full DEX-primary; prediction market utility emerging
  Agent approach: DEX data only; prediction market pool data valuable
  Liquidity check: ALWAYS run before any action; position size governed by TVL
  Yield signal: Holders are primarily LP yield earners or prediction market participants
  
AGENT LOADING RULE:
  For Phase 1/2 tokens: load DeFi skill as supplementary context
  For Phase 3/4 tokens: load DeFi skill BEFORE fan-token-pulse
  Phase identification: see fan-token/fan-token-lifecycle/
```

---

## 8. DeFi signal modifier — how to apply to confidence output

```
DEFI MODIFIERS TO ADD TO CONFIDENCE OUTPUT SCHEMA:

New flag: liquidity_warning
  Set TRUE when pool TVL < $500k for the primary trading venue
  → Triggers: position size reduction regardless of signal confidence

New flag: liquidity_critical  
  Set TRUE when pool TVL < $100k OR estimated slippage > 3%
  → Triggers: ABSTAIN or maximum 20% standard position

New context field: defi_context
  {
    "primary_venue": "CEX|DEX",
    "pool_tvl_usd": 0,
    "estimated_slippage_pct": 0.0,
    "lp_activity_signal": "ACCUMULATION|NEUTRAL|DISTRIBUTION|UNKNOWN",
    "yield_apr_pct": 0.0,
    "prediction_market_pool_usd": 0,
    "lifecycle_phase": 1-6
  }

DEFI-ADJUSTED SIZING RULES:
  TVL > $5M: No adjustment to standard sizing
  TVL $500k–$5M: Max 80% standard position
  TVL $100k–$500k: Max 40% standard position (liquidity_warning active)
  TVL < $100k: Max 20% standard position (liquidity_critical active)
  Slippage > 3%: Override all other sizing; REDUCE or ABSTAIN
```

---

## 9. Developer integration guidance

```
DEFI DATA SOURCES FOR DEVELOPERS:

Real-time pool data:
  GeckoTerminal API (geckoterminal.com) — pool TVL, price, volume, transactions
  DeFiLlama API (defillama.com/api) — TVL across all protocols
  Chiliz DEX subgraph — native Chiliz Chain pool data
  Dune Analytics (dune.com) — custom SQL queries on on-chain data

LP activity monitoring:
  The Graph Protocol (thegraph.com) — index and query Chiliz Chain LP events
  Moralis (moralis.io) — multi-chain LP position tracking
  Covalent (covalenthq.com) — historical LP transaction data

Prediction market data:
  Azuro SDK (azuro.org/docs) — integration with Azuro liquidity pools
  Polymarket CLOB API (docs.polymarket.com) — conditional token markets
  
Yield calculation:
  DeFiLlama yields (defillama.com/yields) — APR/APY across all protocols
  Revert Finance (revert.finance) — Uniswap v3 LP analytics

DEVELOPER BUILD PRIORITIES (DeFi context):
  1. Pre-execution liquidity check: query GeckoTerminal before any agent action
  2. LP activity monitor: subscribe to pool contract events via The Graph
  3. CEX/DEX divergence detector: compare Binance price vs Chiliz DEX price
  4. Slippage estimator: calculate expected impact before position entry
  5. Yield dashboard: track APR for fan token pools as holder incentive signal
```

---

## Glossary additions

| Term | Definition |
|---|---|
| **AMM** | Automated Market Maker — algorithm that sets DEX price using pool reserve ratios |
| **TVL** | Total Value Locked — total dollar value of assets in a liquidity pool |
| **LP** | Liquidity Provider — wallet that deposits assets into a pool and earns fees |
| **LP token** | Receipt token representing a share of a liquidity pool |
| **Impermanent loss** | Loss incurred by LP providers when token price moves relative to pair asset |
| **Slippage** | Price impact of a trade — difference between expected and executed price |
| **DEX** | Decentralised Exchange — exchange operating via smart contracts without a central authority |
| **CEX** | Centralised Exchange — traditional exchange with a central operator (Binance, Coinbase) |
| **Sandwich attack** | MEV strategy where attacker buys before and sells after a detected pending DEX trade |
| **MEV** | Maximal Extractable Value — profit extracted by reordering blockchain transactions |
| **Prediction market** | Protocol where participants bet on outcomes settled by on-chain oracles |
| **Oracle** | Service that brings real-world data (match results, prices) on-chain for smart contracts |

---

## 10. Algorithmic market feedback — how automated systems respond to burn events

```
WHAT THIS COVERS:
  When a PATH_2 WIN burn is confirmed on-chain, the supply reduction is real
  and permanent. But the market price response is mediated by automated
  systems — market makers, arbitrage bots, and liquidity rebalancers — before
  human traders can act. Understanding this layer prevents agents from
  over-interpreting the immediate post-burn price movement.

THE AUTOMATED RESPONSE SEQUENCE (T+0 to T+30 minutes post-WIN):

  T+0 — Burn confirmed on-chain:
    Transaction visible on Chiliscan. Total supply decreases.
    Smart wallets monitoring contract events detect this first.
    
  T+0 to T+5 — Automated market maker (AMM) rebalancing:
    If token is in a liquidity pool (KAYEN/Uniswap-compatible):
    AMM automatically adjusts pool ratio to reflect reduced supply.
    Price increases algorithmically without any human buying.
    This is NOT organic demand — it is mechanical pool rebalancing.
    
  T+5 to T+15 — Arbitrage bots:
    Price difference between DEX (post-rebalance) and CEX (Binance/Bybit):
    Arbitrage bots buy on lower-priced exchange, sell on higher.
    This closes the spread but creates confusing volume signal.
    Bot-driven arbitrage volume should NOT be counted as organic demand.
    
  T+15 to T+60 — Human market response:
    Retail holders see Chiliscan notification or social media coverage.
    First organic buying pressure begins.
    This is the signal SportMind's commercial modifiers capture.

AGENT IMPLICATIONS:

  DO NOT apply the PATH_2 WIN modifier to the T+0 to T+15 price move.
  That price move is algorithmic, not commercial signal.
  
  APPLY the WIN modifier starting from T+15 onward.
  The sustained price above pre-match baseline after T+30 is the real signal.
  
  RULE: If price spikes immediately post-burn but reverts within 15 minutes,
  this is likely AMM rebalancing + arbitrage, not genuine demand uplift.
  
  RULE: If price sustains above pre-match baseline at T+60, organic demand
  signal is confirmed. Apply FTP WIN modifier at full weight.

LIQUIDITY DEPTH EFFECT:
  Low liquidity pools: algorithmic price impact is LARGER
    (same burn creates bigger price move with less liquidity to absorb it)
  High liquidity pools: algorithmic price impact is SMALLER
    (burn absorbed across deeper pool; organic signal cleaner)
  
  Check: TVL before applying burn commercial modifier.
  TVL < $100k: high algorithmic noise. Reduce WIN modifier weight by 30%.
  TVL $100k–$1M: moderate noise. Reduce by 10%.
  TVL > $1M: low noise. Full modifier applies.

BURN SIGNAL CLASSIFICATION:
  GENUINE COMMERCIAL SIGNAL: price sustained T+60, organic volume, TVL adequate
  ALGORITHMIC REBALANCE ONLY: spike and revert within 15 min, no organic volume
  MANIPULATED SIGNAL: wash trading detected (see platform/fraud-signal-intelligence.md)
```

## Compatibility

**Prerequisites:**
- `fan-token/fan-token-why.md` — foundational value thesis (read first)
- `fan-token/fan-token-lifecycle/` — lifecycle phases; DEX transition timing
- `fan-token/fan-token-pulse/` — on-chain holder data (HAS, TVI)

**Closely related:**
- `fan-token/blockchain-validator-intelligence/` — validator rewards as DeFi yield
- `core/confidence-output-schema.md` — output schema (add DeFi flags)
- `platform/fraud-signal-intelligence.md` — manipulation detection for DEX signals

**Data sources:**
- `core/data-sources.md` — Layer 3 on-chain sources section

---

*SportMind v3.62 · MIT License · SportMind · sportmind.dev*
