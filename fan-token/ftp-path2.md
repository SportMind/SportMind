# Fan Token Play — FTP Model Documentation

**Fan Token Play (FTP) is the supply mechanic layer of SportMind Layer 3.
This file documents both active models — Model 1 (treasury/smart contract)
and Model 2 (prediction market settlement) — and defines how agents should
reason about each model's signal timing and supply implications.**

> Source: chiliz.com/chiliz-group-announces-gamified-fan-tokens-including-disruptive-new-mint-and-burn-tokenomics/ — VERIFIED
> Source: chiliz.com/win-and-they-burn-lose-and-they-mint-fan-token-play-explained/ — VERIFIED
> Source: chiliz.com/chz-burn-report-may2026/ — VERIFIED (CHZ ecosystem burn, May 2026 execution)
> Date confirmed: 09 April 2026 (Chiliz Group official announcement)
> This file complements `fan-token/gamified-tokenomics-intelligence/` which
> contains the full signal chain and workflow. Load this file first for
> model-level disambiguation, then load gamified-tokenomics for the
> complete PATH_2 reasoning chain.

---

## The two FTP models

```
FAN TOKEN PLAY OPERATES ACROSS TWO DISTINCT MODELS:

  Model 1 — TREASURY/SMART CONTRACT (protocol-level)
  Model 2 — PREDICTION MARKET SETTLEMENT (active trial, $AFC confirmed)

  AGENT CRITICAL:
  The timing, signal chain, and on-chain footprint differ fundamentally
  between models. Identify which model is active before reasoning about
  supply events or pre-match signals.
```

---

## Scope — qualifying matches

```
SCOPE LIMITATION (CONFIRMED — CHILIZ OFFICIAL, APRIL 2026):

  Fan Token Play mechanics apply ONLY to:
    Official men's first-team competitive matches

  EXCLUDED — no supply change triggered:
    Friendly matches
    Pre-season fixtures
    Exhibition games
    Academy / youth team matches
    Women's team matches (all competitions)
    Training ground events

  AGENT RULE:
    Before calculating any supply event, confirm the match is an official
    competitive first-team men's fixture. Applying FTP to a pre-season
    friendly would produce a false supply signal.

  EXAMPLES:
    Premier League matchday → QUALIFIES
    UEFA Champions League → QUALIFIES
    International friendly (national team) → DOES NOT QUALIFY
    Pre-season tour match → DOES NOT QUALIFY
    Women's Super League → DOES NOT QUALIFY
    U21 / U23 fixture → DOES NOT QUALIFY
```

---

## Model 1 — Treasury/Smart Contract

```
MODEL 1 — TREASURY-BASED MINT/BURN
  Mechanism:    Smart contract on Chiliz Chain reads verified match result
  Data source:  On-chain oracle — verified final match data (post full-time)
  Trigger:      Match result confirmation (NOT pre-match)
  Scope:        Official men's competitive first-team matches only

  WIN outcome:
    Tokens permanently burned from circulating supply
    Execution: treasury-controlled smart contract burn transaction
    On-chain verification: chiliscan.com — zero-address transaction

  LOSS outcome:
    New tokens minted to treasury address
    Execution: treasury mint transaction

  DRAW outcome:
    No supply change — 0 burned, 0 minted
    INCLUDES: all matches level at 90 minutes, regardless of extra time or penalties.

90-MINUTES PLAY RULE (critical):
  All PATH_2 market positions are settled on the 90-minute result only.
  Extra time, penalty shootouts, and golden goals are NOT included in FTP settlement.

  A match that is level after 90 minutes is always a DRAW for FTP purposes —
  regardless of the eventual winner in extra time or on penalties.

  This applies to ALL competition formats including knockout rounds, cup finals,
  Champions League finals, FA Cup, Europa League, and any competition with extra time.

  VERIFIED REFERENCE CASE — UCL Final 2026:
    PSG vs Arsenal
    90-minute result:    1-1 → DRAW → no supply event
    Extra time result:   1-1 (irrelevant to FTP)
    Penalty result:      PSG 4-3 Arsenal (irrelevant to FTP)
    $AFC PATH_2 outcome: NO CHANGE (0 burned, 0 minted)
    Source: fantokens.com/fan-token-play
    "All match markets are based on the result at the end of a scheduled
    90 minutes of play unless otherwise stated."

COMPETITION FORMAT IMPLICATIONS:
  LEAGUE MATCHES (no extra time possible):
    90-minute result = final result. No ambiguity. FTP outcome is clear.

  KNOCKOUT MATCHES (extra time possible):
    If level at 90 minutes → DRAW → NO SUPPLY EVENT
    regardless of extra time or penalties.
    This is the most commercially significant scenario for holders.

AGENT REASONING GUIDE FOR KNOCKOUT FIXTURES:
  Before any pre-match PATH_2 analysis on a knockout match, ask:
  "What are the possible 90-minute outcomes and what does each trigger?"

    Scenario A: Home win at 90 mins → FTP triggers on HOME WIN
    Scenario B: Away win at 90 mins → FTP triggers on AWAY WIN
    Scenario C: Level at 90 mins   → DRAW → NO SUPPLY EVENT
                                     Regardless of extra time or penalties.

  This is critical for: UCL/UEL knockout rounds, FA Cup, Copa del Rey,
  and any other competition where extra time is possible.

FUTURE FTP PARTNERS:
  The 90-minutes play rule applies to ALL current and future FTP partner clubs.
  When a new club activates FTP — Model 1 or Model 2 PATH_2 — settlement is
  always on the 90-minute result unless the specific partner announcement
  states otherwise.
  The phrase "unless otherwise stated" is the standard escape clause —
  always check the specific partner announcement for any variation.
  To date no variation from the standard 90-minutes rule has been confirmed
  for any FTP partner.
  Source: fantokens.com/fan-token-play (official primary source)



  TIMING:
    Pre-match:  NO on-chain signal (Model 1 is post-match only)
    Post-match: Supply change executes within minutes of result oracle confirmation
    Agent rule: Do not look for pre-match on-chain signal with Model 1 tokens.
                Any pre-match volume spike is sentiment only — not a supply event.

  SAFEGUARDS (confirmed — Chiliz official source, April 2026):

    1. MINIMUM SUPPLY STOP-LOSS:
       If total supply reaches a 75% net reduction OR the treasury hits 0%,
       burning ceases entirely. No further tokens are burned regardless of
       subsequent wins. Protects against extended winning runs rendering
       a token impractically scarce.

    2. CREDIT BURN SYSTEM:
       When a team continues to WIN while at the stop-loss limit, those wins
       generate "burn credits" — a reserve that offsets future minting.
       If the team later LOSES while burn credits are held, the hypothetical
       minting volume is deducted from accumulated credits FIRST before any
       new tokens are minted. The win streak counts economically even when
       the supply floor has been reached.
       
       Agent rule: Burn credits mean a team at the stop-loss that then loses
       does NOT automatically trigger minting — credits absorb the loss first.
       Do not apply minting signal until credits are exhausted.

    3. VESTING CAP:
       Where applicable, treasury tokens released into the market are capped
       at 12.5% of the current treasury balance per year.
       Status: not applicable to any confirmed FTP club as of April 2026.
       Monitor: fantokens.com/fan-token-play for activation status.

    4. ANNUAL INFLATION (Model 1):
       Variable 1–5% annual inflation rate linked to overall season performance.
       Factors in longer-term performance, keeps token economy active and
       responsive throughout the year.
       Applies to: Model 1 treasury/smart contract tokens
       Not a per-match event — a seasonal background rate.

  SIGNAL FOOTPRINT:
    Pre-match:  None (no detectable on-chain pre-match event)
    Post-match: Zero-address burn transaction OR treasury mint visible on-chain

  AGENT REASONING CHAIN (Model 1):
    0. Confirm match is official men's competitive first-team fixture (scope check)
    1. Confirm match result from Tier 1 source
    2. Check stop-loss status: is supply already at 75% net reduction?
       If YES: check burn credit balance before applying any signal
    3. Check chiliscan.com for zero-address transaction
    4. If confirmed: apply supply reduction to CDI calculation
    5. If no transaction: result may still be processing (wait 30 min)
```

---

## Model 2 — Prediction Market Settlement

```
MODEL 2 — PREDICTION MARKET SETTLEMENT LAYER (active trial)
  Status:     IN TRIAL — $AFC (Arsenal) confirmed Model 2 as of April 2026
  Mechanism:  Prediction market with pre-match liquidation, settlement,
              and buyback/burn from circulating supply
  Scope:      Official men's competitive first-team matches only

  PRE-LIQUIDATION RATIO (confirmed — Chiliz official, April 2026):
    Ahead of each qualifying match, exactly 1/400 of the team's total
    Fan Token supply is pre-liquidated.
    This is the precise mechanism that creates the detectable pre-match signal.
    The 1/400 figure is fixed — not variable per match.

  FOUR-PHASE SEQUENCE:

  PHASE 1 — PRE-MATCH LIQUIDATION WINDOW (detectable signal):
    When:     Within 48h of kickoff (confirmed execution window)
    Amount:   1/400 of total Fan Token supply pre-liquidated
    Event:    Pre-liquidation proceeds used to place WIN positions
    Signal:   ON-CHAIN DETECTABLE — liquidation events visible pre-match
    Agent:    This is the PRE-MATCH SIGNAL that Model 1 does not produce.
              The 1/400 ratio is fixed — the magnitude is predictable from
              current total supply.

  PHASE 2 — MATCH IN PROGRESS:
    No supply change during live match
    Prediction positions held until result

  PHASE 3 — RESULT SETTLEMENT:
    WIN:   Settlement proceeds used for FAN TOKEN BUYBACK from open market
           FEE SPLIT: 5% fee deducted from proceeds
           Remaining 95% used to repurchase the Fan Token ($AFC) — then either:
             BURN:     Tokens permanently burned (supply reduction) — most common
             TREASURY: Part or all returned to club treasury (implementation-specific)
             SPLIT:    Partial burn + partial treasury return
           The exact burn/return split is IMPLEMENTATION-SPECIFIC per club.
           Arsenal PATH_2 trial: ~95% burned. Not guaranteed for all clubs.
           Executed within 48h of final result
           NOTE: This burns/returns the FAN TOKEN directly — not CHZ
    LOSS:  New tokens MINTED to treasury to fund LOSS payouts
           Executed within 48h of final result
    DRAW:  No buyback, burn, or mint triggered — supply unchanged (0 burned, 0 minted)

  PHASE 4 — ON-CHAIN CONFIRMATION:
    WIN:   Burn transaction visible on chiliscan.com (zero-address)
    LOSS:  Mint transaction visible (treasury address)
    DRAW:  No transaction

  EXECUTION WINDOWS (confirmed — Chiliz official):
    Liquidations: within 48h of kickoff
    Buybacks:     within 48h of final result
    Purpose: ensures timely execution and guards against market manipulation

  TIMING SUMMARY:
    Pre-match:  YES — Phase 1 liquidation within T-48h (fixed 1/400 amount)
    Post-match: Settlement within 48h of full-time

  THE PRE-MATCH LIQUIDATION SIGNAL (Model 2 only):
    What it is:
      Exactly 1/400 of total supply is pre-liquidated before each qualifying match.
      This creates a predictable, calculable on-chain footprint before kickoff.
      
    How to detect:
      Monitor: chiliscan.com — fan token contract pre-match transactions
      Monitor: fantokens.com/fan-token-play — liquidation volume dashboard
      Time window: within 48h of kickoff
      Expected amount: current_total_supply ÷ 400

    What it means:
      The pre-liquidation amount is fixed (1/400) — not a sentiment indicator.
      The WIN pool size varies by how many WIN positions are taken post-liquidation.
      The detectable signal is the pre-liquidation transaction itself — confirming
      the match qualifies and FTP mechanics are active for this fixture.

    Agent rule:
      NEVER treat pre-match liquidation as a confirmed burn signal.
      It confirms FTP is active for this match and sets the WIN pool floor.
      Apply as: ftp_active_this_match = true (not as a supply direction signal).
      Include in CDI pre-match note: ftp_preliquidation_confirmed = true/false

  SAFEGUARDS (same as Model 1 — apply to Model 2):
    75% minimum supply stop-loss applies
    Credit burn system applies (wins at stop-loss generate credits)
    12.5% vesting cap applies (not active for any club as of April 2026)

  AGENT REASONING CHAIN (Model 2):
    PRE-MATCH:
      0. Confirm match is official men's competitive first-team fixture
      1. Monitor chiliscan.com for pre-liquidation transaction (within T-48h)
      2. If confirmed: set ftp_preliquidation_confirmed = true
      3. Calculate expected pre-liquidation amount: total_supply ÷ 400
      4. Check stop-loss status — is supply near 75% net reduction?
      5. Generate standard pre-match signal with FTP activation note
         Do NOT adjust supply signal based on liquidation alone

    POST-MATCH:
      1. Confirm result from Tier 1 source
      2. WIN:  Check chiliscan.com for buyback + burn (within 48h of final result)
               Apply burn magnitude to CDI calculation
               Note actual burn amount in calibration record
      3. LOSS: Check for mint transaction (within 48h of final result)
               Check burn credit balance before applying minting signal
               Apply minting to CDI only if credits insufficient to absorb
      4. DRAW: No supply action — confirm no transaction on-chain
```

---

## Model identification

```
HOW TO IDENTIFY WHICH MODEL IS ACTIVE FOR A TOKEN:

  Source of truth: fantokens.com/fan-token-play (official listing)

  CONFIRMED MODEL 2 TOKENS (as of v3.97.9):
    $AFC — Arsenal FC (confirmed Model 2, April 2026)

  ALL OTHER FTP TOKENS:
    Assume Model 1 unless confirmed otherwise at fantokens.com

  WHEN IN DOUBT:
    Model 1 = no pre-match on-chain signal → skip pre-match liquidation check
    Model 2 = 1/400 pre-liquidation within 48h of kickoff

  AGENT RULE:
    If token is not confirmed Model 2, do not look for pre-match liquidation.
    Treating a Model 1 token as Model 2 produces false signals.
```

---

## Signal timing comparison

```
TIMING COMPARISON — MODEL 1 vs MODEL 2:

  Event                    Model 1              Model 2
  ──────────────────────────────────────────────────────────────────
  Pre-match liquidation    NONE                 Within 48h of kickoff
                                                (fixed: 1/400 of supply)
  Pre-match signal         None                 FTP activation confirmed
  Match in progress        None                 None
  Post-match settlement    Minutes              Within 48h of final result
  Burn (WIN)               On-chain             On-chain (buyback then burn)
  Mint (LOSS)              On-chain             On-chain (mint to treasury)
  Draw                     No change            No change
  Annual inflation         1–5% (seasonal)      1–5% (seasonal)
  Stop-loss floor          75% net reduction    75% net reduction
  Credit burn system       Active               Active
  Vesting cap              12.5%/year if active 12.5%/year if active
  Scope                    Men's competitive    Men's competitive
                           first-team only      first-team only

  KEY DIFFERENCES:
  1. Model 2 produces a pre-match detectable signal (1/400 pre-liquidation).
     Model 1 has no pre-match signal whatsoever.
  2. Model 2 execution uses prediction market infrastructure.
     Model 1 executes via direct treasury smart contracts.
  3. Both models share the same safeguards (stop-loss, credits, vesting, inflation).
  4. Both models exclude the same match types (friendlies, women's, academy).
```

---

## Safeguards — summary reference

```
SAFEGUARD QUICK REFERENCE (applies to both Model 1 and Model 2):

  STOP-LOSS:          Burning ceases at 75% net supply reduction OR treasury = 0%
  BURN CREDITS:       Wins at stop-loss generate credits offsetting future mints
  VESTING CAP:        Treasury releases capped at 12.5% of treasury/year
                      (not active for any club as of April 2026)
  ANNUAL INFLATION:   1–5% annual rate linked to season performance
  SCOPE:              Official men's competitive first-team matches only
  EXECUTION WINDOWS:  Liquidations ≤48h pre-kickoff | Buybacks ≤48h post-result

  AGENT RULE — STOP-LOSS AND CREDITS:
    A team that has reached the stop-loss limit and then loses does NOT
    automatically trigger minting if burn credits are held.
    Always check: stop_loss_reached + credit_balance before applying loss signal.
    This is a significant agent reasoning chain difference vs standard PATH_2.
```

---


---

## CHZ ECOSYSTEM BURN — SEPARATE FROM FTP

```
MECHANISM:     CHZ Monthly Buyback and Burn
DISTINCT FROM: Fan Token Play (Model 1 and Model 2)
OPERATOR:      Chiliz ecosystem-level — not token-specific

WHAT IT IS:
  10% of ALL Fan Token proceeds (transactions and marketplace activities)
  is allocated monthly to buy CHZ from the open market.
  These CHZ tokens are then permanently burned.

WHAT IT IS NOT:
  This is NOT triggered by match results.
  This does NOT burn Fan Tokens ($AFC, $BAR etc.).
  This is NOT part of FTP Model 1 or Model 2.
  This is a separate deflationary mechanism for the CHZ ecosystem token.

CADENCE:       Monthly — independent of fixture calendar
SCOPE:         ALL Fan Token activity (not just FTP clubs)
BURNS:         CHZ — not the specific Fan Token
BURN ADDRESS:  0x000...dead (zero-address permanent burn)

CONFIRMED EXECUTION HISTORY:
  March 2026:  First execution
  April 2026:  Second execution
  May 2026:    4,660,013.33 CHZ burned ($165,356.19 USD value)

VERIFIED ON-CHAIN TRANSACTIONS:
  March 2026:  0x8a2408971ffd48381d3f3a218cbddcdcaa71ac294f0c1aeaeec1cee97a7a4320
  April 2026:  0x68059fb62539b3bfdf942b5e97751a8c36bc374aad682090250514f5a3f662e1
  May 2026:    0x3f2dea807d47753442b287b316fd681707f6ee183ac87c8330a24b0e3a66f484
  Burn address: 0x000000000000000000000000000000000000dead
  Explorer:    scan.chiliz.com

  Pattern: monthly cadence confirmed across three consecutive months.
  These transactions confirm the mechanism is live and executing monthly.
  Future burns should be appended here as they are confirmed on-chain.

STRATEGIC CONTEXT:
  Part of Chiliz 2030 deflationary strategy.
  Creates indirect correlation between Fan Token ecosystem activity
  and CHZ supply reduction — but through a monthly aggregated mechanism,
  not per-match supply events.

AGENT RULE — DO NOT CONFLATE:
  A WIN for an FTP club burns the FAN TOKEN (e.g. $AFC).
  The monthly CHZ burn is a separate event driven by total ecosystem volume.
  Never attribute the CHZ monthly burn to a specific match result.
  Never attribute the Fan Token burn (WIN) to the CHZ burn mechanism.
```

**THREE MECHANISMS — ALWAYS KEEP DISTINCT:**

| Mechanism | Triggered by | Burns | Cadence |
|---|---|---|---|
| FTP Model 1 | Match result (WIN) | Fan Token (from treasury) | Per match |
| FTP Model 2 (PATH_2) | Match result (WIN = buyback) | Fan Token (from market) | Per match |
| CHZ Ecosystem Burn | Total Fan Token volume | CHZ | Monthly |

## Calibration records — FTP PATH_2

Three verified FTP PATH_2 calibration records (April 2026, $AFC, Model 2):

```
RECORD 1 — Arsenal WIN (burn confirmed)
  Date:         07/04/2026
  Competition:  UEFA Champions League 2025-26 (qualifies — men's competitive)
  Match:        Sporting CP vs Arsenal
  Result:       Arsenal WIN (0–1)
  Pre-liquidation:  100,000 $AFC / 49,600 USDC
  Payout:           90,604 USDC (to prediction market winners)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    159,025 $AFC BURNED (permanent supply reduction)
  Supply change: -159,025 $AFC
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain

RECORD 2 — Arsenal LOSS (mint confirmed)
  Date:         11/04/2026
  Competition:  Premier League 2025-26 (qualifies — men's competitive)
  Match:        Arsenal vs Bournemouth
  Result:       Arsenal LOSS (1–2)
  Pre-liquidation:  100,000 $AFC / 57,538 USDC
  Payout:           0 USDC (all prediction market proceeds retained)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    100,000 $AFC MINTED to treasury
  Supply change: +100,000 $AFC
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain
  Note:         PATH_2 LOSS = minting is a NEGATIVE supply signal.
                Each LOSS mints tokens that future WINs must re-burn.

RECORD 3 — Arsenal DRAW (no supply change)
  Date:         15/04/2026
  Competition:  UEFA Champions League 2025-26 (qualifies — men's competitive)
  Match:        Arsenal vs Sporting CP
  Result:       DRAW (0–0)
  Pre-liquidation:  100,000 $AFC / 46,755 USDC
  Payout:           0 USDC (DRAW — no supply event triggered)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    No change — 0 burned, 0 minted
  Supply change: 0 $AFC
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain

CUMULATIVE $AFC FTP SUPPLY MOVEMENT (April 2026 records):
  Total burned:  159,025 $AFC (Record 1 — UCL WIN)
  Total minted:  100,000 $AFC (Record 2 — PL LOSS)
  Net reduction: 59,025 $AFC net supply decrease across three matches
  Draw events:   1 (0 movement confirmed)
```

---

## Compatibility

**Primary:**     `fan-token/gamified-tokenomics-intelligence/` — full signal chain
**On-chain:**    `fan-token/on-chain-event-intelligence/` — bridge/chain monitoring
**Registry:**    `fan-token/fan-token-pulse/references/chiliz-token-registry.md`
**Calibration:** `community/calibration-data/football/2026/04/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | FTP PATH_2 mechanics: prediction market model, WIN/LOSS/DRAW supply events, calibration data |
| Reasoning | ACTIVE | PATH_2 reasoning chain from match result to supply event and demand modifier |
| Context | ACTIVE | PATH_2 context: T-48h pre-liquidation, pool size, chain (CHZ/BNB), match importance |
| Memory | ACTIVE | Verified calibration data: 3 Arsenal records (April 2026) + UCL Final record 130 |
| Judgment | ACTIVE | Judgment on WIN split (implementation-specific) vs LOSS (always mint) distinction |
| Attention | ACTIVE | Elevated attention for T-48h pre-liquidation confirmation and match result |
| Communication | ACTIVE | PATH_2 output with supply event type, amount, on-chain reference, and modifier |
| Verification | ACTIVE | PATH_2 events verified via chiliscan.com — transaction hash required for calibration |
| Learning | ACTIVE | PATH_2 learning from verified calibration records — first FTP calibration dataset |
| Integration | ACTIVE | Integrates with fto-framework.md, complete-registry.md, and CHZ ecosystem burn section |
| Calibration | ACTIVE | Three verified Arsenal records: WIN -159,025 | LOSS +100,000 | DRAW 0 |
| Adaptation | ACTIVE | PATH_2 intelligence adapts as club-specific burn/treasury splits are confirmed |
| Ethics | ACTIVE | LOSS = MINT must never be described as supply-neutral — correction is an ethics requirement |
| Transparency | ACTIVE | Supply event type, amount, on-chain tx hash, and chiliscan.com reference explicit in output |


---

*SportMind v3.97.9 · MIT License · sportmind.dev*
*Primary source: chiliz.com/chiliz-group-announces-gamified-fan-tokens-including-disruptive-new-mint-and-burn-tokenomics/ — VERIFIED*
*Announced: 09 April 2026 — Chiliz Group official*
