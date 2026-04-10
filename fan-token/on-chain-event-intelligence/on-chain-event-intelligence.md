# On-Chain Event Intelligence

**The framework for interpreting on-chain *events* as pre-match and
commercial signals — smart money wallet behaviour, LP activity ahead
of sporting events, governance execution patterns, and staking ratio changes.**

This skill is distinct from the DeFi liquidity intelligence skill
(`fan-token/defi-liquidity-intelligence/`). That skill covers *state*:
current TVL, spread, pool depth, and liquidity tier. This skill covers
*events*: changes in on-chain behaviour that signal information asymmetry,
smart money positioning, or governance intentions before they are reflected
in price.

The core thesis: on-chain data is transparent. When large wallets move,
when liquidity is added before a match, when governance votes are queued —
these actions are visible on-chain before their consequences appear in price.
A well-instrumented agent can read these signals and incorporate them into
its pre-match and commercial intelligence.

---

## Signal categories

```
CATEGORY 1 — LARGE WALLET MOVEMENTS (Smart Money)

Definition: Transactions involving wallets holding ≥ 0.5% of circulating supply
            OR wallets in the top-50 by token holdings

Signal types:
  Accumulation (large wallet buys): pre-event confidence signal
  Distribution (large wallet sells): pre-event concern signal
  Wallet clustering: multiple large wallets moving in same direction

Monitoring window: T-72h to T-2h before a significant match or event

Accumulation thresholds:
  > 0.5% supply moved in 24h: MODERATE signal
  > 1.0% supply moved in 24h: HIGH signal
  > 2.0% supply moved in 24h: STRONG signal (flag for immediate analysis)

Modifier formula:
  accumulation_signal = min(1.15, 1.00 + (pct_supply_moved × 0.10))
  distribution_signal = max(0.85, 1.00 - (pct_supply_moved × 0.12))

CAUTION: Large wallet movement is a signal, not a guarantee.
  Whales can be wrong. Apply as modifier × 0.70 (partial confidence).
  Large wallet accumulation + high SMS + clean macro = strongest combined signal.
  Large wallet accumulation alone (without SMS support) = flag only; do not act.


CATEGORY 2 — LP ADDITIONS / REMOVALS (Liquidity Provision)

Pre-match LP additions:
  Sophisticated liquidity providers often add to pools before high-signal events.
  They do this because high-volume events generate more fees.
  Signal: LP addition in 24-48h before a major match = liquidity_depth improving.
  Modifier: TVL_tier may upgrade (THIN → MODERATE) if LP addition is significant.

Pre-match LP removals:
  LP removal before a match = liquidity provider expects volatility they do not
  want exposure to. This is a bearish signal for the match outcome.
  Applies when: > 15% of pool liquidity removed within 24h of event.
  Modifier: TVL_tier may downgrade; apply liquidity_warning flag.

Post-match LP activity:
  LP additions after a win: confidence in sustained price support.
  LP removals after a win: profit-taking by LPs; not necessarily bearish
  (they provided liquidity during the spike and are now reducing exposure).

MONITORING IMPLEMENTATION:
  Track pool TVL every 15 minutes (Platform 3 real-time pattern)
  Calculate rate of change, not just level
  Alert on: 15%+ change in either direction within any 2-hour window


CATEGORY 3 — GOVERNANCE VOTE EXECUTION

On-chain governance events are transparent and trackable.
Before a vote is publicly announced (pre-announcement window), governance
contract state changes on-chain — a proposal is submitted, vote weights
are set, quorum parameters are defined.

Pre-vote signals (detectable before announcement):
  Governance contract: new proposal submitted → vote incoming
  Vote weight delegation: major holders delegating before announcement
  These signals are typically 24-72h ahead of public announcement.

Vote execution confirmation:
  On-chain: vote results are immutable once executed.
  Timing: execution often happens before club publicly announces outcome.
  Signal: on-chain execution = confirmed vote outcome, regardless of announcement.

Governance execution as commercial signal:
  Meaningful vote executed (Decision_Weight ≥ 0.65): LTUI +3 to +5
  Cosmetic vote executed (Decision_Weight ≤ 0.30): LTUI neutral
  Vote executed but result not publicly communicated within 48h:
    governance_theatre risk — track execution vs communication gap


CATEGORY 4 — STAKING RATIO CHANGES

Staking ratio = % of circulating supply currently staked
Higher staking ratio = fewer tokens available for trading = lower sell pressure

Staking ratio signals:
  Rising staking (> 5% increase in 7 days): positive signal
    Holders are locking tokens, reducing sell pressure
    Modifier: × 1.04 to LTUI stability
    
  Falling staking (> 5% decrease in 7 days): concern signal
    Holders are unstaking — may be preparing to sell
    Modifier: × 0.96 to LTUI stability
    Apply liquidity_warning if > 10% decrease

  Staking threshold events:
    Staking ratio crosses 40% for first time: structural positive signal
    Staking ratio drops below 20%: structural concern signal


CATEGORY 5 — CROSS-CHAIN BRIDGE ACTIVITY

Chiliz Chain / Socios tokens can bridge to Ethereum and other chains.
Unusual bridge activity can signal:
  Mass bridging out: holders moving tokens to sell on other platforms
  Bridging in: new holders entering via other chains (growth signal)

Signal thresholds:
  > 2% supply bridged in 48h: significant movement, monitor direction
  Consistent net outflow over 7 days: negative structural signal
  Net inflow (more bridging in than out): positive growth signal


CATEGORY 6 — WALLET AGE AND HOLDER RETENTION

Average wallet age = average time holders have held their tokens.
This is a loyalty and conviction proxy.

Rising average wallet age: long-term holders not selling — conviction signal
Falling average wallet age: turnover increasing — speculative vs holder shift

New wallet acquisition rate:
  Spike in new wallets (> 100 new holders in 24h): outreach working
  Post-match new wallet spike: outcome converting new fans to holders
  Off-season new wallet spike: organic growth or marketing activation
```

---

## On-chain event monitoring implementation

```python
# on_chain_monitor.py
"""
Monitor Chiliz Chain / Socios on-chain events for fan token signals.
Extends Platform realtime-integration-patterns.py Pattern 3 (token monitor).
"""
import asyncio
from datetime import datetime, timezone

KAYEN_API   = "https://api.kayen.finance/v1"
CHILIZ_RPC  = "https://rpc.ankr.com/chiliz"  # Public Chiliz Chain RPC

class OnChainEventMonitor:
    """
    Monitors Chiliz Chain events for smart money signals.
    Runs every 15 minutes; alerts on Category 1-6 events.
    """

    def __init__(self, token_address: str, token_symbol: str):
        self.token_address  = token_address
        self.token_symbol   = token_symbol
        self.baseline_tvl   = 0.0
        self.baseline_stake = 0.0
        self.large_wallet_threshold = 0.005  # 0.5% of supply

    async def check_wallet_movements(self) -> list:
        """
        Detect large wallet movements in the last 24h.
        Returns list of detected signals.
        """
        # Fetch recent transactions from KAYEN or Chiliz Chain explorer
        # Filter for transfers involving top-50 wallets by holdings
        # Calculate % of supply moved
        
        signals = []
        
        # STUB: Replace with live Chiliz Chain transaction data
        # In production:
        #   1. Get top-50 wallets for this token from KAYEN
        #   2. Fetch last 24h transactions for those wallets
        #   3. Calculate net movement (buy/sell direction)
        #   4. Apply thresholds and build signals
        
        return signals

    async def check_lp_activity(self, pool_address: str,
                                  hours_to_event: float = 999) -> dict:
        """
        Check liquidity pool activity for pre-event signals.
        Returns LP signal with direction and magnitude.
        """
        import aiohttp

        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{KAYEN_API}/pools/{pool_address}") as r:
                    pool = await r.json()

            current_tvl = pool.get("tvl_usd", 0)
            tvl_24h_ago = pool.get("tvl_24h_ago_usd", current_tvl)

            if tvl_24h_ago == 0: return {"signal": "NO_DATA"}

            pct_change  = (current_tvl - tvl_24h_ago) / tvl_24h_ago
            is_pre_event = hours_to_event <= 48

            if pct_change > 0.15 and is_pre_event:
                return {
                    "signal":       "LP_ADDITION_PRE_EVENT",
                    "magnitude":    pct_change,
                    "modifier":     1.03,
                    "note":         f"LP added {pct_change:.0%} in 24h before event — liquidity depth improving"
                }
            elif pct_change < -0.15 and is_pre_event:
                return {
                    "signal":       "LP_REMOVAL_PRE_EVENT",
                    "magnitude":    abs(pct_change),
                    "modifier":     0.94,
                    "flag":         "liquidity_warning",
                    "note":         f"LP removed {abs(pct_change):.0%} in 24h before event — liquidity concern"
                }

            return {"signal": "STABLE", "modifier": 1.00}

        except Exception as e:
            return {"signal": "ERROR", "note": str(e)}

    async def check_staking_ratio(self) -> dict:
        """Check staking ratio trend for conviction signal."""
        try:
            import aiohttp
            async with aiohttp.ClientSession() as s:
                async with s.get(
                    f"{KAYEN_API}/tokens/{self.token_address}/staking"
                ) as r:
                    data = await r.json()

            current  = data.get("staking_ratio", 0.0)
            week_ago = data.get("staking_ratio_7d_ago", current)

            if week_ago == 0: return {"signal": "NO_DATA"}

            change = current - week_ago

            if change > 0.05:
                return {
                    "signal":   "STAKING_RISING",
                    "current":  current,
                    "change":   change,
                    "modifier": 1.04,
                    "note":     f"Staking ratio +{change:.0%} in 7d — holders locking tokens"
                }
            elif change < -0.05:
                return {
                    "signal":   "STAKING_FALLING",
                    "current":  current,
                    "change":   change,
                    "modifier": 0.96,
                    "note":     f"Staking ratio {change:.0%} in 7d — holder conviction declining"
                }

            return {"signal": "STABLE", "modifier": 1.00}

        except Exception as e:
            return {"signal": "ERROR", "note": str(e)}

    async def get_composite_on_chain_signal(self,
                                             pool_address: str,
                                             hours_to_event: float = 999) -> dict:
        """
        Composite on-chain signal combining all categories.
        Returns overall on-chain modifier and active signals.
        """
        lp_signal      = await self.check_lp_activity(pool_address, hours_to_event)
        staking_signal = await self.check_staking_ratio()
        wallet_signals = await self.check_wallet_movements()

        # Build composite
        modifiers  = [
            lp_signal.get("modifier", 1.00),
            staking_signal.get("modifier", 1.00),
        ]
        for w in wallet_signals:
            modifiers.append(w.get("modifier", 1.00))

        # Geometric mean of modifiers
        composite = 1.00
        for m in modifiers:
            composite *= m
        composite = composite ** (1 / len(modifiers))

        active_signals = [
            s["signal"] for s in [lp_signal, staking_signal] + wallet_signals
            if s.get("signal") not in ("STABLE", "NO_DATA", "ERROR")
        ]

        flags = []
        if lp_signal.get("flag") == "liquidity_warning":
            flags.append("liquidity_warning")
        if staking_signal.get("signal") == "STAKING_FALLING" and \
           staking_signal.get("current", 1.0) < 0.20:
            flags.append("low_staking_ratio")

        return {
            "token":            self.token_symbol,
            "on_chain_modifier": round(composite, 4),
            "active_signals":   active_signals,
            "flags":            flags,
            "components": {
                "lp":      lp_signal,
                "staking": staking_signal,
            },
            "generated_at": datetime.now(timezone.utc).isoformat()
        }
```

---

## Integration with SportMind signal chain

```
STEP 5b (OPTIONAL) — On-chain event check:

This is an optional step in the six-step reasoning chain, inserted between
Step 5 (DeFi/liquidity check) and Step 6 (confidence output).

When to include:
  - Fan token Tier 1 analysis (full stack)
  - When liquidity context is critical (DeFi prediction markets)
  - When large wallet activity has been detected in the 24h pre-event window

When to skip:
  - Pure match analysis (no token context)
  - Bandwidth-constrained agents
  - When on-chain data is unavailable

Example — on-chain modifier incorporation:
  Base signal SMS: 76
  DeFi TVL tier: MODERATE (modifier 1.00)
  On-chain signals detected:
    LP addition +18% in 24h pre-event: modifier × 1.03
    Staking ratio rising +7%: modifier × 1.04
    No large wallet signals detected
  
  On-chain composite modifier: 1.035 (geometric mean)
  
  Final adjusted score: 76 × 1.035 = 78.7
  Note: "On-chain signals positive — LP and staking confirm holder confidence"
```



CATEGORY 6 — WALLET AGE AS CONVICTION PROXY

  Long-held wallets (12+ months) that begin actively trading:
  Signal: Dormant long-term holders reactivating = strong conviction shift
  Accumulation by old wallets: STRONG_BULL_SIGNAL (conviction accumulation)
  Distribution by old wallets: STRONG_BEAR_SIGNAL (conviction distribution)
  
  Wallet age tiers:
    < 3 months: Recent entrant — low conviction signal value
    3-12 months: Established — moderate conviction signal
    12-24 months: Long-term — high conviction signal
    24+ months: OG holder — maximum conviction signal weight


CATEGORY 7 — FAN TOKEN PLAY EVENTS (Path 2, April 2026+)

  Fan Token Play Path 2 creates PROTOCOL-DRIVEN on-chain events that are
  detectable before and after every match. These are distinct from organic
  whale activity — they are scheduled, attributable, and follow a precise pattern.
  
  Misreading Fan Token Play events as organic activity is a significant agent error.
  
  EVENT 1: PRE-LIQUIDATION (T-48h before match)
    What happens: Treasury wallet sells 1/400th of circulating supply → USDT
    On-chain signature: Treasury wallet, exact 0.25% supply amount, T-48h timing
    Detection method:
      1. Identify treasury wallet for the token (via KAYEN or chiliscan token metadata)
      2. Monitor for treasury sells in the T-72h to T-24h window
      3. If sell size = ~0.25% of supply AND sender = treasury wallet: FAN TOKEN PLAY
      4. Confirm via fantokens.com or chiliscan token page
    
    Signal value: Confirms Fan Token Play is ACTIVE for this specific match
    Modifier: None to pre-match signal (it is confirmation, not directional)
    Flag: set fan_token_play_active = true for this match
    
    AGENT ERROR TO AVOID:
      Do NOT treat this as a large whale sell signal (Category 1)
      Do NOT apply distribution_signal modifier (this is not bearish)
      Do NOT set liquidity_warning (this is protocol mechanics, not organic exit)
  
  EVENT 2: POST-WIN BUYBACK AND BURN (within T+48h of WIN)
    What happens: Win proceeds → 95% used to buy back tokens → burned to zero address
    On-chain signature: Buy from KAYEN pool → tokens sent to 0x0000...0000
    Detection method:
      1. After a WIN result is confirmed
      2. Monitor for burn transactions from the token contract
      3. Burns to 0x0000000000000000000000000000000000000000 = permanent burn
      4. Attribute to Fan Token Play if timing matches T+48h window
    
    Signal value: Confirms WIN + supply reduction — reinforces post-match ENTER
    Modifier: Apply gamified_win_modifier from gamified-tokenomics-intelligence/
    
  EVENT 3: POST-LOSS RE-MINT (within T+48h of LOSS)
    What happens: Pre-liquidated amount minted back to treasury wallet
    On-chain signature: New tokens appear in treasury wallet (not to market)
    Detection method:
      1. After a LOSS result is confirmed
      2. Monitor for mint transactions to treasury wallet
      3. Amount should match pre-liquidation amount (~0.25% of supply)
      4. Supply returns to pre-match level (neutral, not expanded)
    
    Signal value: Confirms LOSS + supply neutral — Path 2 LOSS is less negative than Path 1
    Modifier: No negative modifier beyond standard loss sentiment
    
  MONITORING IMPLEMENTATION:
    Query: chiliscan.com/token/{contract}/transfers
    Filter: from_address = treasury_wallet OR to_address = 0x0000...0000
    Window: T-72h to T+72h around each match
    Alert conditions:
      Treasury sell ~0.25% supply at T-48h: FAN_TOKEN_PLAY_DETECTED
      Burn to zero address post-match: FAN_TOKEN_PLAY_WIN_CONFIRMED
      Treasury mint ~0.25% post-match: FAN_TOKEN_PLAY_LOSS_CONFIRMED
  
  CHZ ECHO SIGNAL:
    Fan Token Play WIN burns also contribute to CHZ buyback via the 10% ecosystem rule.
    A confirmed Fan Token Play WIN generates TWO deflationary signals:
      1. Fan token supply burn (this category)
      2. CHZ supply burn (see macro/macro-crypto-market-cycles.md — virtuous cycle)
    Note both in signal output. They are different assets but connected mechanics.


---

## Caution notes

```
ON-CHAIN SIGNAL LIMITATIONS:

1. CORRELATION NOT CAUSATION
   Large wallet accumulation before a win does not prove the wallet had
   advance information. Some wallets are simply better at analysis.
   Never assume manipulation without additional evidence.

2. SIGNAL LAG
   On-chain transactions take time to be indexed and discoverable.
   There is typically a 5-15 minute lag between transaction and detection.
   Not suitable for T-0 signals (match has started).

3. WASH TRADING RISK
   Some on-chain activity is artificial (wash trading to inflate volume).
   Cross-reference on-chain volume with off-chain exchange volume.
   If on-chain volume >> off-chain volume: potential wash trading flag.

4. PROTOCOL-SPECIFIC BEHAVIOUR
   Chiliz Chain (Socios) fan tokens behave differently from
   ERC-20 tokens on Ethereum. KAYEN AMM mechanics differ from Uniswap.
   Always use Chiliz-specific data sources (KAYEN API, Chiliz explorer).

5. REGULATORY CONSIDERATION
   In some jurisdictions, acting on wallet movement data to trade tokens
   may be subject to market manipulation regulations.
   SportMind provides intelligence for analysis; legal compliance is
   the responsibility of the application layer.
```

---

## Compatibility

**DeFi liquidity intelligence:** `fan-token/defi-liquidity-intelligence/` — TVL state (complement)
**Sports governance:** `fan-token/sports-governance-intelligence/` — governance vote signals
**Real-time patterns:** `platform/realtime-integration-patterns.md` — Pattern 3 (base token monitor)
**RWA/SportFi:** `fan-token/rwa-sportfi-intelligence/` — Phase 5 on-chain mechanics
**Breaking news:** `core/breaking-news-intelligence.md` — Category 8 (token platform events)
**Fan Token Play:** `fan-token/gamified-tokenomics-intelligence/` — Path 1/2 mechanics detail
**CHZ macro:** `macro/macro-crypto-market-cycles.md` — virtuous cycle and CHZ burn signal

*SportMind v3.44 · MIT License · sportmind.dev*
*Category 7 (Fan Token Play events) added April 2026*
