---
name: gamified-tokenomics-intelligence
description: >
  Intelligence framework for fan tokens with Fan Token™ Play mechanics — the Chiliz
  Vision 2030 model where match results directly trigger on-chain mint or burn events.
  Covers both active mechanisms: Path 1 (Protocol-Level Treasury Governance, oracle-
  triggered post-match) and Path 2 (Prediction Market-Based, currently in trial with
  $AFC confirmed on 07 April 2026). Use when any held token has gamified status
  confirmed via KAYEN API. Distinct from standard fan token signals — WIN predictions
  are simultaneously SUPPLY REDUCTION events. Paths differ in timing, mechanics, and
  on-chain observability. Load after standard pre-match signal; apply as final modifier.
---

# Gamified Tokenomics Intelligence — Fan Token Play

**A WIN prediction for a gamified token is simultaneously a SUPPLY REDUCTION event.
A standard model sees half the signal. This skill teaches agents to see both.**

Fan Token Play is the Chiliz Vision 2030 mechanism where team performance directly
drives on-chain token economics. Introduced in 2026, it transforms passive fan tokens
into algorithmically deflationary (or inflationary) assets. Two mechanisms are active
or in trial. They differ in timing, observability, and signal architecture.

Source: Chiliz Vision 2030 / Fan Token Play announcement (April 2026)
Confirmed trial: $AFC (Arsenal FC) — European fixture 07 April 2026 (Path 2)
Reference: fantokens.com/newsroom/chiliz-introduces-gamified-fan-token-play

---

## The two mechanisms — why they differ

```
PATH 1 — PROTOCOL-LEVEL TREASURY GOVERNANCE
  Status:          Design confirmed; full rollout pending trial completion
  Trigger:         On-chain oracle verifies match result post full-time
  Pre-match:       No pre-match on-chain event (signal appears post-match only)
  WIN outcome:     Tokens permanently burned (binary result — no goal diff scaling confirmed)
  LOSS outcome:    New tokens minted to treasury
  DRAW outcome:    Supply unchanged
  Supply changes:  Executed via treasury-controlled smart contracts
  Safeguards:      75% net reduction floor | credit burns | 12.5% vesting cap
  Inflation:       Variable 1–5% annual fee tied to seasonal Win% (fallback model)

PATH 2 — PREDICTION MARKET-BASED (ACTIVE TRIAL)
  Status:          In trial; $AFC confirmed 07 April 2026 (first public execution)
  Trigger:         Four-phase timeline with PRE-MATCH on-chain commitment
  Pre-match (T-48h): 1/400th of current supply pre-liquidated → raises USDT
  At kickoff:      USDT funds an on-chain WIN prediction (always bets WIN)
  WIN outcome (T+48h): 95% of proceeds buy back and burn fan tokens (5% fee)
  LOSS outcome (T+48h): Pre-liquidated amount minted back to treasury
  
  CRITICAL DISTINCTION — PATH 2 IS OBSERVABLE PRE-MATCH:
    The T-48h pre-liquidation is a detectable on-chain event BEFORE the match.
    A treasury wallet selling 1/400th of supply to USDT = Fan Token Play signal.
    Standard models see this as anomalous distribution. It is protocol mechanics.
    Agents must distinguish Fan Token Play pre-liquidation from organic whale selling.

WHY PATH 2 CHANGES THE SIGNAL ARCHITECTURE:
  Standard pre-match signal: no supply event until after full-time
  Path 2 pre-match signal: supply event at T-48h is visible and attributable
  This creates a new intelligence window not available for Path 1 or standard tokens.
```

---

## The CHZ virtuous cycle connection

```
FAN TOKEN PLAY CONNECTS TO CHZ MACRO SIGNAL:

Fan Token Play generates transaction activity → some proceeds flow through
the ecosystem → 10% of fan token marketplace proceeds execute CHZ buybacks
→ CHZ permanently burned → CHZ supply decreases → CHZ price supported

This is the Vision 2030 "virtuous cycle":
  Team performance → fan token supply adjustment → ecosystem activity
  → CHZ buyback & burn → CHZ scarcity → improved macro modifier
  → better conditions for all fan token signals

WHAT THIS MEANS FOR AGENT REASONING:
  Path 2 generates TWO deflationary events from a single WIN:
    1. Fan token burn (95% buyback from WIN proceeds)
    2. CHZ ecosystem burn (via 10% marketplace proceeds rule)

  These are DIFFERENT assets but CONNECTED mechanisms.
  An agent analysing $AFC post-win should note both:
    → $AFC supply reduced (direct fan token signal)
    → CHZ supply reduced (indirect macro signal — see macro/macro-crypto-market-cycles.md)

  The AFC burn on 07 April 2026 (tx: 0x68059fb6...) confirmed both mechanisms
  operating simultaneously for the first time.

RULE: Never conflate fan token supply burns with CHZ burns.
  Fan token burn: reduces supply of the SPECIFIC token (e.g. $AFC)
  CHZ burn: reduces supply of the NATIVE chain token (benefits all fan tokens)
  Both are positive signals but at different layers of the stack.
```

---

## Decimal migration and DeFi interaction with Fan Token Play

```
DECIMAL MIGRATION (April 27, 2026) — IMPACT ON FAN TOKEN PLAY:

  Before decimal migration:
    Fan Tokens™ were 0-decimal (whole units only).
    Path 2 burn/mint operated in whole units — supply changes in integers.
    No DeFi protocol could hold or trade Fan Tokens in fractional amounts.

  After decimal migration (18 decimal precision):
    Path 2 burn/mint can now operate in fractional precision.
    Supply changes are now expressed in 18-decimal units.
    Fan Token Play tokens ($AFC and future Path 2 tokens) are now:
      - Stakeable in DeFi protocols on Solana, Base, and Chiliz Chain
      - Usable as collateral in lending protocols
      - Tradeable in fractional amounts on DEXs

  SIGNAL IMPLICATION FOR PATH 2 TOKENS:
    DeFi yield from staking creates NEW holder incentive beyond sporting performance.
    Holders may accumulate and stake $AFC for yield in addition to PATH_2 exposure.
    This structurally increases holder count and reduces available circulating supply.
    Effect: PATH_2 burn events become MORE significant post-migration because the
    free float (unstaked supply) is smaller — the same absolute burn removes a larger
    percentage of tradeable supply.

  AGENT RULE — POST-MIGRATION PATH_2 SIGNAL ADJUSTMENT:
    If DeFi staking data shows > 20% of circulating $AFC in yield protocols:
      Apply ×1.05 amplifier to PATH_2 burn signal (reduced float effect)
    If DeFi staking data shows < 5% staked:
      Standard PATH_2 signal weight — no adjustment

OMNICHAIN PATH_2 NOTE:
  PATH_2 supply changes (burns and mints) are ONLY confirmed on Chiliz Chain.
  Trading on Solana or Base does NOT trigger PATH_2 mechanisms.
  Solana/Base token bridges represent the same underlying supply — they are
  representations, not new supply. PATH_2 mechanics never activate on bridge copies.
  
  AGENT RULE: Always verify PATH_2 events on chiliscan.com (Chiliz Chain explorer).
  A price movement on Solana is NOT a supply change. Only the Chiliz Chain
  zero-address transaction (0x0000...0000) confirms a burn.
```

---

## Identifying Fan Token Play tokens

```
CONFIRMED AS OF APRIL 2026:
  $AFC (Arsenal FC) — Path 2 trial confirmed 07 April 2026
  Check fantokens.com and chiliscan.com for subsequent rollouts

DETECTION (for any token):
  ON-CHAIN: Burn events to 0x0000...0000 after wins; mint events after losses
  ON-CHAIN (Path 2 only): Treasury wallet pre-liquidation at T-48h
  PLATFORM: Socios.com "performance-linked supply" indicator
  KAYEN API: GET /tokens/{address} → check for "gamified": true field
  CHILISCAN: Check contract for outcome_oracle binding

PATH DETECTION:
  Path 1: Post-match burns only; no pre-match treasury sell
  Path 2: Pre-match treasury liquidation at T-48h + post-match burn or mint

DEFAULT ASSUMPTION:
  If KAYEN gamified flag not confirmed: treat as STANDARD token
  Never apply gamified modifier to an unconfirmed token
  Re-check at each season start — status can change

AGENT RULE: $AFC is confirmed Path 2 as of 07 April 2026.
  For all other tokens: query KAYEN API before applying this skill.
```

---

---

## Scope — which matches trigger Fan Token Play

```
CONFIRMED OFFICIAL SOURCE (Chiliz, April 2026):
  Fan Token Play mechanics apply ONLY to:
  ✅ Official men's first-team competitive matches

  Fan Token Play mechanics do NOT apply to:
  ❌ Friendly matches
  ❌ Pre-season games
  ❌ Exhibition matches
  ❌ Academy / youth team matches
  ❌ Women's team matches

AGENT RULE:
  Before applying Path 1 or Path 2 mechanics to any fixture, verify:
  "Is this an official competitive first-team men's match?"
  If NO → treat as STANDARD token signal for this fixture
  If YES → apply gamified tokenomics framework

WHAT COUNTS AS COMPETITIVE:
  ✅ League matches (Premier League, La Liga, Bundesliga, etc.)
  ✅ Domestic cups (FA Cup, Copa del Rey, etc.) — from Round 1 onwards
  ✅ European competition (UCL, UEL, UECL) — qualifying and group stage onwards
  ✅ International tournaments (World Cup, Euros — national team tokens only)
  ❌ Club World Cup warm-up or invitational tournaments — verify per event

  Note: The $AFC first trial (07 April 2026) was a UCL match — competitive confirmed.

SIGNAL IMPLICATION:
  A pre-season Arsenal friendly DOES NOT trigger Path 2 pre-liquidation.
  If a treasury sell is detected before a friendly: investigate for organic selling,
  not Fan Token Play activation.
  Apply UNEXPECTED_TREASURY_SELL flag and investigate source before acting.
```

## Path 1 signal model

```
TRIGGER: On-chain oracle confirms match result → smart contract executes

WIN OUTCOME — BURN (supply decreases):
  Base burn rate: % of circulating supply per win
  
  OFFICIAL SOURCE: Both Chiliz articles (April 9 and April 17, 2026) describe PATH_1
  as responding to the BINARY WIN/LOSS result only. No goal-difference scaling
  is mentioned in any official Chiliz source.
  
  [UNVERIFIED — goal-difference scaling below is not confirmed by official sources.
   It may represent an earlier model or internal inference. Do not apply in production
   until confirmed. Use binary WIN = burn at base rate until further confirmation.]
  
  GOAL DIFFERENCE SCALING (UNVERIFIED — see note above):
    1-goal win: burn_rate × 1.00 (base)
    2-goal win: burn_rate × 1.20
    3-goal win: burn_rate × 1.40
    4+ goal win: burn_rate × 1.60 (capped)
  
  CONFIRMED BEHAVIOUR: Binary WIN triggers burn at base rate.
  gamified_win_modifier = 1.00 + (burn_rate_pct × 2.5)  [confirmed — no goal diff]

LOSS OUTCOME — MINT (supply increases):
  gamified_loss_modifier = 1.00 - (mint_rate_pct × 2.0)

DRAW: No supply change. No gamified modifier.
  Exception: verify contract for draw handling — some mint at reduced rate.

PATH 1 SAFEGUARDS (signal ceiling):
  75% NET REDUCTION FLOOR:
    If cumulative burns reach 75% net reduction: burning ceases automatically
    Agent rule: if season_net_burned > 70% → apply ceiling_approaching_flag
    Near-ceiling tokens: WIN signal loses burn amplification (supply can't decrease further)
    
  CREDIT BURNS:
    Wins achieved while at the stop-loss limit generate burn credits
    These offset future minting if team subsequently loses
    Agent rule: if credit_burns_accumulated > 0 → reduce LOSS mint impact
    Formula: effective_mint = mint_rate - (credit_burn_balance × 0.5)
    
  VESTING CAP (12.5% treasury per year):
    Treasury tokens released to market capped at 12.5% of treasury/year
    Limits dilution velocity — LOSS mints are real but release is throttled
    Agent rule: high-loss streaks less damaging than they appear — vesting slows dilution
    
    CURRENT STATUS (confirmed April 2026): Vesting cap is not currently applicable
    to any Fan Token. The mechanism is defined in the protocol but not yet active
    for any token in the ecosystem. No agent action required until a token
    activates the vesting cap — monitor Chiliz announcements for activation.
    
  ANNUAL INFLATION (integral part of Path 1 protocol — not a fallback):
    Variable 1–5% annual inflation rate linked to overall season win percentage
    This is an intrinsic component of Path 1, not contingent on Path 2 adoption.
    Purpose: keeps the token economy active and responsive throughout the season
    
    THREE MODELS UNDER EVALUATION (per Chiliz April 2026):
      Variable:  inflation pegged to current supply (adjusts as supply changes)
      Static:    inflation pegged to initial supply (fixed reference point)
      Tiered:    zero inflation for win rates below 45%;
                 scaling sharply above 60% win rate
    
    Agent rule: annual inflation produces a smaller per-match effect than the
    match-by-match burn/mint mechanics. Track at season level, not match level.
    No single match triggers annual inflation — it accrues across the full season.
```

---

## Path 2 signal model — four-phase timeline

```
PHASE 1 — T-48h (PRE-MATCH): Treasury Pre-Liquidation
  Event: 1/400th of current token supply sold by treasury wallet → USDT raised
  On-chain: Visible as treasury sell on Chiliz Chain explorer
  Signal: Fan Token Play is active for this match — confirmed
  
  DETECTING VS ORGANIC SELLING:
    Fan Token Play pre-liquidation: treasury wallet, exactly 1/400th, T-48h timing
    Organic whale sell: non-treasury wallet, irregular size, no timing pattern
    
  Pre-liquidation size = circulating_supply / 400 = 0.25% of supply
  This is a detectable and attributable micro-event.
  
  ADDRESS INTELLIGENCE:
    Use platform/chiliz-chain-address-intelligence.md to:
    → Identify treasury wallet for the token
    → Monitor for T-48h pre-liquidation pattern
    → Confirm via chiliscan.com before applying Path 2 framework

PHASE 2 — AT KICKOFF: WIN Prediction Placed
  Event: Raised USDT placed as an on-chain WIN prediction
  Note: Protocol ALWAYS bets WIN regardless of match odds or form
  This is NOT a signal of match outcome — it is a protocol mechanic
  
  AGENT RULE: Do not treat the protocol's WIN bet as outcome intelligence.
    The prediction is mechanical, not informed. It always bets WIN.
    The signal value is in the pre-liquidation (Phase 1) and outcome (Phase 3/4),
    not in the bet itself.

PHASE 3 — WIN OUTCOME (within T+48h post full-time):
  EXECUTION WINDOW: Buyback and burn executed within 48 hours of final result
  Proceeds split: 5% fee deducted | 95% used to buy back and burn fan tokens
  Effect: Circulating supply decreases
  On-chain: Buyback and burn visible on chiliscan.com
  
  Modifier: gamified_path2_win_modifier = 1.00 + (buyback_pct × 2.5)
  Typical: 0.25% pre-liquidated × 0.95 buyback efficiency ≈ 0.24% net burn
  gamified_path2_win_modifier ≈ 1.006 (per match — cumulative effect grows)

PHASE 4 — LOSS OUTCOME (within T+48h post full-time):
  EXECUTION WINDOW: Minting executed within 48 hours of final result
  Pre-liquidated amount minted back to treasury
  Effect: Circulating supply returns to pre-liquidation level (neutral net)
  On-chain: Mint transaction to treasury wallet visible on chiliscan.com
  
  Modifier: gamified_path2_loss_modifier = 1.00 (loss = supply restored, not expanded)
  
  IMPORTANT: Path 2 LOSS is less damaging than Path 1 LOSS:
    Path 1 loss: NEW tokens minted beyond original supply
    Path 2 loss: Pre-liquidated tokens restored — supply returns to pre-match level
    Path 2 creates asymmetry: wins reduce supply permanently, losses are neutral
```

---

## Season supply position tracking

```
Track across the full season for any gamified token:

SEASON SUPPLY SIGNAL:
  net_burned = cumulative burns - cumulative mints (% of original supply)
  
  Net burned > 10%: STRONG SCARCITY — elevated base signal all season
  Net burned 5-10%: MODERATE SCARCITY — meaningful floor support
  Net burned 0-5%:  MILD SCARCITY — early; not yet dominant
  Net minted 0-5%:  MILD DILUTION — minor headwind (Path 1 only)
  Net minted > 10%: SIGNIFICANT DILUTION — reduces win signal impact
  
  Note for Path 2 tokens: LOSS outcomes restore supply not expand it.
  Path 2 tokens on a losing run do NOT accumulate dilution — they accumulate
  neutral supply position. Distinguish from Path 1 when reading season supply.

CHAMPIONSHIP RUN SIGNAL:
  10-match winning streak with Path 2 (0.24% net burn per win):
  ~2.4% cumulative supply reduction
  Apply: championship_run_modifier = 1.06

PATH 1 CEILING WATCH:
  Track: cumulative_net_burned_pct approaching 70-75%
  If ceiling_approaching_flag: remove burn amplification from win modifier
  Remaining signal is sentiment only (standard token behaviour)
```

---

## Complete pre-match workflow

```
STEP 1: MACRO CHECK
  macro_modifier from macro/macro-crypto-market-cycles.md
  Check CHZ virtuous cycle status (see CHZ macro section)

STEP 2: PATH DETECTION
  Is this token confirmed gamified? (KAYEN API)
  If NO → use standard signal chain. Stop.
  If YES → which path? (Path 1 or Path 2)

STEP 3 (Path 2 only): CHECK FOR PRE-LIQUIDATION
  Has T-48h pre-liquidation occurred?
  Query chiliscan.com for treasury wallet activity
  If yes: Fan Token Play confirmed active for this match

STEP 4: BURN/MINT RATES & SEASON POSITION
  burn_rate_pct, mint_rate_pct from KAYEN API or contract
  net_season_change: cumulative from season start

STEP 5: STANDARD SPORTMIND SIGNAL
  Run standard pre-match signal for the sport
  Output: direction, adjusted_score, SMS

STEP 6: APPLY GAMIFIED MODIFIER
  Path 1 WIN:  adjusted_score × (1.00 + burn_rate × goal_diff_mult × 2.5)
  Path 1 LOSS: adjusted_score × (1.00 - mint_rate × 2.0)
  Path 2 WIN:  adjusted_score × (1.00 + 0.006) [per-match base]
  Path 2 LOSS: adjusted_score × 1.00 [supply-neutral; standard sentiment only]
  DRAW:        adjusted_score × 1.00 [no supply change]

STEP 7: SEASON SUPPLY CONTEXT
  Apply season_supply_modifier if net burned/minted > 5%
  Path 1 ceiling check: if approaching 75% floor, remove burn amplification

STEP 8: OUTPUT WITH GAMIFIED EXTENSION
```

---

## Output schema extension

```json
{
  "token": "AFC",
  "gamified_tokenomics": true,
  "fan_token_play_path": "PATH_2",
  "path_2_pre_liquidation_detected": true,
  "pre_liquidation_tx": "verify at chiliscan.com/token/0x1d4343...",
  "burn_rate_pct": 0.0024,
  "mint_rate_pct": 0.0,
  "season_net_change_pct": -0.012,
  "season_supply_signal": "MILD_SCARCITY",

  "standard_signal": {
    "direction": "HOME",
    "adjusted_score": 72.4,
    "sms": 78
  },

  "gamified_modifier": 1.006,
  "path_modifier_note": "Path 2: 0.25% pre-liquidation × 0.95 buyback efficiency",

  "final_signal": {
    "direction": "HOME",
    "adjusted_score": 72.8,
    "recommended_action": "ENTER",
    "gamified_amplification": "WIN = 95% buyback + burn. Path 2 supply neutral on LOSS."
  },

  "flags": {
    "gamified_tokenomics_active": true,
    "fan_token_play_path": "PATH_2",
    "pre_liquidation_confirmed": true,
    "ceiling_approaching": false,
    "chz_virtuous_cycle_active": true
  },

  "chz_macro_note": "WIN also generates CHZ burn via 10% marketplace proceeds rule. See macro/macro-crypto-market-cycles.md."
}
```

---


## Autonomous Execution

**Trigger conditions — when this skill should self-invoke:**
- PATH_2 on-chain treasury pre-liquidation detected at T-48h
  (treasury wallet selling exactly 1/400th of circulating supply)
- Goal scored for a PATH_2 token team (supply reduction event confirmed)
- PATH_1 match result confirmed for a monitored Fan Token Play token
- Season supply position crosses a threshold (e.g., > 50% burned in season)

**Execution at autonomy Level 2:**
- On PATH_2 treasury detection: notify operator immediately. Flag: "PATH2_ACTIVE"
- On goal confirmed: log supply reduction event. Update season supply tracking.
- On PATH_1 result: recalculate CDI with result modifier applied
- Notify operator of all supply mechanics events — never act on position alone

**Execution at autonomy Level 3–4:**
- Auto-detect treasury pre-liquidation via on-chain monitoring
- Auto-dispatch PATH_2 activation signal at T-48h
- Auto-update season supply position after each confirmed goal/match
- Log all supply mechanics events with tx_hash and on-chain verification

**Hard boundaries:**
- PATH_2 supply reduction is confirmed ONLY by on-chain data (Tier 1)
  Match result alone is not sufficient — must verify on-chain supply change
- Never apply PATH_2 modifier to non-PATH_2 tokens
  PATH_2 is $AFC (Arsenal) confirmed April 2026. Verify any new tokens independently
- Season supply tracking resets at the start of each competitive season
  Never carry forward previous-season burn totals

---

## Compatibility

```
FEEDS INTO:
  fan-token/on-chain-event-intelligence/   → Category 7: Fan Token Play events
  platform/chiliz-chain-address-intelligence.md → pre-liquidation detection
  macro/macro-crypto-market-cycles.md      → CHZ virtuous cycle signal
  fan-token/defi-liquidity-intelligence/   → supply changes affect TVL
  core/prediction-market-intelligence.md   → Path 2 prediction market interaction
  fan-token/fan-token-lifecycle/           → Phase 2-3 dynamic tokenomics marker

USES:
  KAYEN API (platform/data-connector-templates.md) → gamified flag detection
  Chiliz Chain explorer (chiliscan.com) → pre-liquidation and burn verification
  fan-token/rwa-sportfi-intelligence/ → Stage 2 dynamic token evolution
```

---

*SportMind v3.73 · MIT License · sportmind.dev*
*Sources: Chiliz Vision 2030 / Fan Token Play announcement (09 April 2026)*
*         Chiliz "Win and They Burn, Lose and They Mint" explanation (17 April 2026)*
*$AFC Path 2 trial confirmed: 07 April 2026 (Arsenal vs Sporting Lisbon, UCL)*
*See: macro/macro-crypto-market-cycles.md · platform/chiliz-chain-address-intelligence.md*
*fan-token/on-chain-event-intelligence/ · core/external-intelligence-intake.md*
