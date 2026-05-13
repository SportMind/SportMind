---
name: blockchain-onchain-intelligence
description: >
  Enduring reasoning framework for on-chain signals as they affect fan token
  supply, liquidity, and holder behaviour. Covers wallet concentration, transaction
  velocity, bridge activity, smart contract signals, supply event verification,
  and holder behaviour patterns. Load live on-chain data from primary sources
  at query time and apply this framework to interpret it.
---

# Blockchain and On-Chain Intelligence

**How to reason about on-chain signals as fan token modifier inputs.**
Not stored on-chain data — the framework for interpreting it when fetched.

> Primary sources: chiliscan.com (Chiliz Chain) · fantokens.com/fan-token-play
> Load live data at query time. Apply this framework to interpret it.

---

## Wallet concentration framework

```
WALLET CONCENTRATION — SIGNAL RELIABILITY MODIFIER:

  WHY CONCENTRATION MATTERS:
    When a small number of wallets hold a large percentage of supply, a single
    large holder decision can move the price and demand signal significantly.
    High concentration makes individual demand modifiers less reliable.
    
  CONCENTRATION MODIFIER TABLE:

  Top 10 wallets holding     Signal                    Confidence modifier
  ─────────────────────────────────────────────────────────────────────────
  Above 50% of supply       High concentration         ×0.90 confidence weight
  25-50% of supply          Moderate concentration     ×1.00 (standard weight)
  Below 25% of supply       Healthy distribution       ×1.05 confidence weight

  APPLICATION:
    Apply the confidence modifier to ALL demand modifier calculations for this token.
    High concentration (×0.90): each demand signal is less reliable — widen prediction interval.
    Healthy distribution (×1.05): demand signals are more reliable — tighter prediction interval.
    
  HOW TO ASSESS CONCENTRATION:
    Source: chiliscan.com token holder page — shows top wallet distribution.
    Count top 10 wallets vs circulating supply.
    Exclude: confirmed Chiliz/Socios treasury wallets and exchange cold wallets.
      These are structural holdings, not speculative concentration.
    Apply concentration modifier only to organic holder wallets.
    
  CONCENTRATION TREND:
    Concentration decreasing over time: positive distribution signal
    Concentration increasing over time: accumulation signal (institutional or whale)
      → Apply additional monitoring flag: concentration_trending flag
```

---

## On-chain transaction velocity

```
TRANSACTION VELOCITY — DEMAND HEALTH SIGNAL:

  RISING TRANSACTION COUNT WITH RISING UNIQUE WALLETS:
    Genuine demand growth signal — new participants are entering the token
    Apply: genuine_demand_growth_modifier = ×1.08 confidence amplifier
    This is the strongest positive on-chain signal combination.
    
  RISING TRANSACTION COUNT WITH STATIC UNIQUE WALLETS:
    Wash trading risk signal — volume is inflated by existing wallets churning
    Apply: wash_trading_risk_modifier = ×0.85 confidence weight
    Reduce all demand signal weight — the volume is not genuine new demand.
    Flag: wash_trading_risk = true; do not apply volume-based demand modifiers.
    
  FALLING TRANSACTION COUNT:
    Holder disengagement signal
    Apply: holder_disengagement_modifier = ×0.92 confidence weight
    Sustained falling velocity: structural negative signal (beyond single-match variance)
    Define "sustained": 3+ consecutive weeks of declining count
    
  MATCH-DAY TRANSACTION SPIKES:
    Expected on match days for all clubs.
    For $AFC (PATH_2): expect pre-match activity spike from T-12h to T-2h.
    Spike beyond 3× baseline: elevated pre-liquidation engagement signal
      — confirms market is actively engaging with PATH_2 mechanics.
    Spike below 1.5× baseline for $AFC on match day: weak engagement signal;
      expected burn pool may be lower than circulating supply ÷ 400 calculation suggests.
```

---

## Bridge activity signals

```
CROSS-CHAIN BRIDGE VOLUME:

  BRIDGE VOLUME INCREASING (Chiliz Chain ↔ Base or Solana):
    Signal: positive liquidity expansion — holders are accessing multiple chains
    Apply: bridge_growth_modifier = ×1.05 to demand baseline
    Mechanism: cross-chain access increases the total addressable holder base;
      each chain has a different holder segment that the others lack
    Monitor: Chiliz official bridge explorer / LZ (LayerZero) scan for bridge volume
    
  BRIDGE ACTIVITY SPIKE BEFORE $AFC MATCH (T-12h to T-2h):
    Specific signal for FTP PATH_2 mechanics
    Pre-match bridge activity moving tokens to/from Chiliz Chain:
      Signal: holders are positioning for the pre-liquidation window
      Confirms: market engagement with PATH_2 mechanics is active
      Apply: path2_bridge_engagement_flag = true → elevated confidence in burn estimate
      
  BRIDGE VOLUME DECLINING:
    Holders consolidating back to Chiliz Chain (the primary chain)
    Signal: neutral to mildly negative — cross-chain adoption is slowing
    Apply: bridge_decline_flag — note but do not immediately apply a modifier
    Confirm trend (3+ weeks): then apply ×0.97 mild accessibility signal
```

---

## Smart contract signals

```
SMART CONTRACT UPGRADE (official Chiliz announcement):

  UPGRADE ANNOUNCED — PENDING:
    Temporary uncertainty signal during upgrade window
    Apply: contract_upgrade_uncertainty = ×0.95 during active upgrade window
    Duration: from announcement to completion confirmation
    
  UPGRADE COMPLETED SUCCESSFULLY:
    Positive technical progress signal
    Apply: contract_upgrade_completion = ×1.05 for 1-2 weeks post-completion
    Signal: technical infrastructure is improving; team is executing
    Then remove — modifier normalises to baseline
    
  NEW FAN TOKEN CONTRACT DEPLOYED (new token launching):
    Ecosystem growth signal — the platform is expanding
    Apply: new_token_ecosystem_growth = ×1.03 to all EXISTING token demand baselines
    Duration: 2-4 weeks (novelty period); then remove
    Mechanism: new token launch brings new users to the ecosystem who
      may also buy existing tokens

EMERGENCY CONTRACT PAUSE OR EXPLOIT:
  If a smart contract is paused due to an exploit or emergency:
    Apply: emergency_pause_signal = ×0.75 immediately to ALL affected tokens
    This is severe — warrants HOLD on all associated signals
    Duration: until official "all clear" from Chiliz
    Source: Chiliz official channels only (Tier 1) — do not apply based on social media
```

---

## Supply event on-chain verification

```
FTP PATH_2 SUPPLY EVENT VERIFICATION:

  WHY ON-CHAIN VERIFICATION MATTERS:
    Supply events (burns and mints) are permanent and verifiable on-chain.
    Verification confirms the event occurred and the magnitude.
    Source: chiliscan.com — the primary verification source for Chiliz Chain events.

  BURN EVENT VERIFICATION:
    Confirmed burn on-chain:
      → Supply is permanently reduced
      → Verify: burn wallet address received tokens AND tokens were destroyed
      → Burn amount confirmed = circulating supply falls by that amount
    Match against expectation:
      Expected burn range from pre-match analysis vs actual burn amount
      If actual burn significantly exceeds estimate: demand was stronger than expected
      If actual burn significantly below estimate: demand was weaker than expected
      Use to recalibrate future burn estimates for this token.
      
  MINT EVENT VERIFICATION:
    Confirmed mint on-chain:
      → Treasury wallet receives new tokens
      → Circulating supply increases by mint amount
    Match against expectation:
      Similar recalibration logic — actual vs estimated mint amount
      
  PRE-LIQUIDATION MONITORING ($AFC — T-12h to T-2h):
    Monitor chiliscan.com for pre-liquidation transaction patterns:
    Pre-liquidation pool = circulating supply ÷ 400 (theoretical)
    Actual pre-liquidation activity may confirm or diverge from theoretical pool
    Elevated activity: larger potential burn pool → revise estimate upward
    Muted activity: smaller effective pool → revise estimate downward
    Apply: pre_liq_monitoring_flag during the T-12h to T-2h window
```

---

## Holder behaviour patterns

```
LONG-TERM HOLDER RATIO:

  DEFINITION:
    Wallets that have not moved their tokens in 6+ months.
    High ratio = committed community; low ratio = speculative holder base.
    
  RATIO MODIFIER TABLE:

  LTH ratio        Signal               Modifier
  ────────────────────────────────────────────────────────────────────
  Above 60%        Community commitment  ×1.05 confidence amplifier
  30-60%           Mixed / standard      ×1.00 (no modifier)
  Below 30%        Speculative holders   ×0.92 confidence weight

  APPLICATION:
    LTH ratio above 60%: demand signals are more stable and reliable
    LTH ratio below 30%: speculative holders may exit on small negative signals;
      demand signal decay will be faster than average; apply ×0.92 weight
      
  SOURCE: chiliscan.com wallet activity / age analysis

NEW WALLET CREATION RATE AROUND MATCH EVENTS:

  ORGANIC INTEREST SIGNAL:
    New unique wallets acquiring tokens in the 48h before a match:
      Organic interest signal — new participants attracted by the event
      Apply: new_wallet_pre_match_signal = positive engagement flag
      
  EXISTING HOLDER REBALANCING:
    Transaction volume from wallets that already held tokens:
      Not new demand — existing holders repositioning
      Neutral signal — does not indicate new holder base growth
      
  HOW TO DISTINGUISH:
    New wallet creation (first-ever transaction) vs existing wallet activity
    chiliscan.com shows wallet creation date — filter for new vs existing.
```

---

## Compatibility

**Pre-liq calculation:**    `fan-token/ftp-path2.md`
**Bridge V2.0 context:**    `fan-token/fan-token-lifecycle/`
**Ecosystem health:**       `fan-token/ecosystem-health-intelligence.md`
**Exchange signals:**       `macro/exchange-intelligence.md`

---

*SportMind v3.97.41 · MIT License · sportmind.dev*
*Load live on-chain data from chiliscan.com at query time. Apply this framework to interpret it.*
