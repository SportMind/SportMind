# Fan Token Supply Intelligence — Template and Framework

**Structured supply data template for active Fan Tokens™. Load alongside
CDI signal chain for supply-aware analysis. Updated per versioned release.**

> Used by: all Tier A fan token intelligence files
> Maintained by: fan-token/ftp-path2.md (mechanics) and this file (data)

---

## Supply intelligence template

```
SUPPLY INTELLIGENCE BLOCK — [TOKEN_SYMBOL] ([CLUB_NAME])
Last verified:   [YYYY-MM-DD]
Source:          [URL]

  circulating_supply:      [N] tokens
  total_supply:            [N] tokens
  circulation_ratio:       [N]%
    (circulating / total — higher = more in public hands)

  last_ftp_event:
    amount:    [+/- N] tokens
    direction: [BURN / MINT / NONE]
    date:      [YYYY-MM-DD]
    match:     [match description]

  net_ftp_change_ytd:     [+/- N] tokens (since season start / Jan 1)
    (negative = net burn / deflationary  |  positive = net mint / inflationary)

  pre_liquidation_pool:   ~[N] tokens
    (calculated: circulating_supply ÷ 400 — per FTP Model 2 confirmed mechanics)

  stop_loss_status:        [CLEAR / APPROACHING / REACHED]
    (APPROACHING = within 10% of 75% net reduction floor)
    (REACHED = burning ceases; credit burn system active)

  credit_balance:          [N] tokens  (if applicable)
    (accrued burn credits from wins at stop-loss — offsets future mints)

  chain_support (Fan Tokens V2.0 — confirmed April 2026):
    chiliz_chain:  ACTIVE (native — settlement anchor, FTP supply events)
    solana:        ACTIVE (via LayerZero bridge — Jupiter/Raydium DEXs)
    base:          ACTIVE (via LayerZero bridge — Aerodrome/Uniswap Base DEXs)
    bridge_status: BRIDGE_LIVE
    decimal_standard: 18 (V2.0 — upgraded from 0-decimal legacy)
    contract_note: Verify current addresses at chiliscan.com (post-April 27, 2026)
```

---

## How to use this template

```
AGENT LOADING RULE:
  Load this template block before running any CDI signal that involves
  supply mechanics. Supply state changes the signal weight applied to
  WIN/LOSS/DRAW outcomes.

  Key calculations:

  1. PRE-LIQUIDATION POOL (Model 2 tokens only):
     pre_liquidation_pool = circulating_supply ÷ 400
     This is the fixed amount pre-liquidated before each qualifying match.
     Agents should confirm this calculation matches the observed on-chain event.

  2. STOP-LOSS CHECK:
     Reduction so far = (original_total_supply - circulating_supply) / original_total_supply
     If reduction > 75%: stop_loss_reached = true → no further burn signal
     If 65–75%: stop_loss_approaching = true → flag in CDI output

  3. NET FTP YTD CONTEXT:
     Negative value: token is deflationary this period (more burns than mints)
     Positive value: token is inflationary this period (more mints than burns)
     Use as a context modifier for holder sentiment (deflationary = positive signal)

  4. CIRCULATION RATIO CONTEXT:
     Below 40%: treasury holds majority — minting events have less relative impact
     40–70%:    typical range — standard signal weights apply
     Above 70%: most supply in public hands — burn events have higher impact per unit

DATA FRESHNESS RULE:
  Supply data should be verified within 7 days for active tokens.
  Stale data (>14 days) should be flagged as potentially outdated.
  After any FTP event (WIN/LOSS), update circulating_supply and last_ftp_event.
  Source: fantokens.com/trade/[token-slug] or chiliscan.com
```

---

## Populated supply blocks — active tokens

### $AFC — Arsenal FC Fan Token

```
SUPPLY INTELLIGENCE BLOCK — $AFC (Arsenal FC)
Last verified:   2026-05-08
Source:          fantokens.com/trade/arsenal-fan-token

  circulating_supply:      ~44,600,000 tokens
  total_supply:            ~84,100,000 tokens
  circulation_ratio:       53%

  last_ftp_event:
    amount:    −159,025 tokens
    direction: BURN (permanent)
    date:      2026-04-07
    match:     Sporting CP vs Arsenal — UCL QF Leg 2 (Arsenal WIN 0–1)

  net_ftp_change_ytd:      −59,025 tokens
    (2026 YTD: −159,025 burned + 100,000 minted = net −59,025)
    Status: DEFLATIONARY — net burn > net mint this period

  pre_liquidation_pool:    ~111,500 tokens
    (44,600,000 ÷ 400 = 111,500 — per FTP Model 2 confirmed ratio)

  stop_loss_status:        CLEAR
    (current net reduction from original supply is well below 75% floor)

  credit_balance:          0 (stop-loss not reached; no credits accrued)

  ftp_model:               Model 2 — Prediction Market Settlement (confirmed)
  path2_confirmed:         true
  ucl_standing:            FINALIST (2025-26) | opponent: PSG | final: 30 May 2026

  chain_support (Fan Tokens V2.0):
    chiliz_chain:  ACTIVE (FTP supply events settle here — chiliscan.com)
    solana:        ACTIVE (Jupiter/Raydium — BRIDGE_LIVE)
    base:          ACTIVE (Aerodrome/Uniswap Base — BRIDGE_LIVE)
    bridge_status: BRIDGE_LIVE
    decimal_standard: 18 (V2.0 — upgraded April 27, 2026)
    binance_status: UNAFFECTED (not in May 2026 Binance CAP20 migration list)
```

---

## Signal implications by supply state

```
SUPPLY STATE → SIGNAL WEIGHT ADJUSTMENT:

  HIGH CIRCULATION RATIO (>70%):
    Burn events: higher CDI impact per token (larger % of public float affected)
    Mint events: lower CDI impact per token (treasury absorption smaller)
    $AFC current (53%): standard signal weights apply

  STOP-LOSS APPROACHING (65–75% net reduction):
    Flag: stop_loss_approaching = true in CDI output
    Apply: reduced WIN signal confidence (burn may not execute)
    Watch: credit burn system may activate before stop-loss confirmed

  STOP-LOSS REACHED:
    WIN signal: supply signal PAUSED — no burn executes
    Credit burn system active — credits accumulate
    LOSS signal: check credit balance before applying mint signal

  DEFLATIONARY YTD (net_ftp_change_ytd negative):
    Positive holder sentiment context
    Applied as: supply_trend = "deflationary" in signal notes
    $AFC current: −59,025 YTD — deflationary ✓

  PRE-LIQUIDATION POOL SIZE:
    Larger pool = larger WIN burn potential (when WIN pool exceeds floor)
    $AFC current: ~111,500 tokens per qualifying match
    UCL Final pool: likely larger (elevated prediction market participation)
```

---

## Update protocol

```
WHEN TO UPDATE SUPPLY DATA:
  After every confirmed FTP event (WIN burn or LOSS mint)
  At minimum: monthly verification for active tokens
  Before any UCL/major tournament signal generation
  After decimal migration events or contract address changes

FIELDS TO UPDATE AFTER FTP EVENT:
  circulating_supply:     adjust by event amount
  last_ftp_event:         new amount, direction, date, match
  net_ftp_change_ytd:     running total (sum of all +/- events this year)
  pre_liquidation_pool:   recalculate from new circulating_supply
  stop_loss_status:       re-evaluate after significant burn series

DATA SOURCES (priority order):
  1. fantokens.com/trade/[token-slug]  — official supply dashboard
  2. chiliscan.com                     — on-chain verification (Chiliz Chain)
  3. fantokens.com/fan-token-play      — FTP event confirmation
  4. birdeye.so / Jupiter.ag           — Solana chain data (post-V2.0)
  5. basescan.org / Aerodrome          — Base chain data (post-V2.0)

CROSS-CHAIN NOTE (Fan Tokens V2.0 — active April 2026):
  All confirmed BRIDGE_LIVE tokens operate on Chiliz Chain, Solana, and Base.
  Supply figures always refer to TOTAL supply across all three chains combined.
  FTP supply events (burns/mints) settle on Chiliz Chain regardless of where
  the token is currently held. Bridging does not change supply — it moves tokens.
  See fan-token/registry/bridge-supported.md for full chain support details.
```

---

## Compatibility

**Mechanics:**    `fan-token/ftp-path2.md` — Model 1 and Model 2 definitions
**Calibration:**  `community/calibration-data/football/2026/04/`
**On-chain:**     `fan-token/on-chain-event-intelligence/`
**Bridge:**       `fan-token/registry/bridge-supported.md` — V2.0 multi-chain registry
**Token files:**  `fan-token/arsenal.md` · (see fan-token/ registry for additional token files)


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan token supply intelligence: TVS, circulating supply, burn/mint events, and supply modifiers |
| Reasoning | ACTIVE | Supply reasoning chain from supply data to TVS modifier and demand signal adjustment |
| Context | ACTIVE | Supply context: total supply, circulating supply, FTP burn/mint events, staking lock-up |
| Memory | ACTIVE | Historical supply change patterns and their price correlation data |
| Judgment | ACTIVE | Judgment on supply signal materiality — FTP burn events always material, minor burns less so |
| Attention | ACTIVE | Maximum attention for FTP supply events — LOSS = MINT is highest supply risk signal |
| Communication | ACTIVE | Supply output with TVS value, circulating supply, and active supply modifiers |
| Verification | ACTIVE | Supply data from on-chain chiliscan.com — not aggregator estimates |
| Learning | ACTIVE | Supply calibration from verified PATH_2 records: WIN -159,025 | LOSS +100,000 | DRAW 0 |
| Integration | ACTIVE | Integrates with ftp-path2.md, staking intelligence, and gamified tokenomics |
| Calibration | ACTIVE | TVS modifier calibrated from verified PATH_2 supply event records |
| Adaptation | ACTIVE | Supply intelligence adapts as FTP mechanics and token issuance evolve |
| Ethics | ACTIVE | LOSS = MINT must never be described as supply-neutral — accuracy is an ethics requirement |
| Transparency | ACTIVE | Supply event type, amount, source, and TVS modifier always explicit in output |


---

*SportMind v3.97.22 · MIT License · sportmind.dev*
*Supply data verified: 2026-05-08*
*Source: fantokens.com/trade/arsenal-fan-token*
