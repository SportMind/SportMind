# Fan Token Play — FTP Model Documentation

**Fan Token Play (FTP) is the supply mechanic layer of SportMind Layer 3.
This file documents both active models — Model 1 (treasury/smart contract)
and Model 2 (prediction market settlement) — and defines how agents should
reason about each model's signal timing and supply implications.**

> Source: fantokens.com/fan-token-play — VERIFIED
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

## Model 1 — Treasury/Smart Contract

```
MODEL 1 — TREASURY-BASED MINT/BURN
  Mechanism:    Smart contract on Chiliz Chain reads verified match result
  Data source:  On-chain oracle — verified final match data (post full-time)
  Trigger:      Match result confirmation (NOT pre-match)
  
  WIN outcome:
    Tokens permanently burned from circulating supply
    Execution: treasury-controlled smart contract burn transaction
    On-chain verification: chiliscan.com — zero-address transaction
    
  LOSS outcome:
    New tokens minted to treasury address
    Execution: treasury mint transaction
    
  DRAW outcome:
    No supply change — 0 burned, 0 minted
    
  TIMING:
    Pre-match:  NO on-chain signal (Model 1 is post-match only)
    Post-match: Supply change executes within minutes of result oracle confirmation
    Agent rule: Do not look for pre-match on-chain signal with Model 1 tokens.
                Any pre-match volume spike is sentiment only — not a supply event.
    
  SAFEGUARDS (confirmed):
    75% net reduction floor on cumulative burns
    12.5% vesting cap per event
    1–5% annual inflation fee tied to seasonal Win% (fallback model)
    
  SIGNAL FOOTPRINT:
    Pre-match:  None (no detectable on-chain pre-match event)
    Post-match: Zero-address burn transaction OR treasury mint visible on-chain
    
  AGENT REASONING CHAIN (Model 1):
    1. Confirm match result from Tier 1 source
    2. Check chiliscan.com for zero-address transaction
    3. If confirmed: apply supply reduction to CDI calculation
    4. If no transaction: result may still be processing (wait 30 min)
```

---

## Model 2 — Prediction Market Settlement

```
MODEL 2 — PREDICTION MARKET SETTLEMENT LAYER (active trial)
  Status:     IN TRIAL — $AFC (Arsenal) confirmed Model 2 as of April 2026
  Mechanism:  Prediction market with pre-match liquidation, settlement,
              and buyback/burn from circulating supply
  
  FOUR-PHASE SEQUENCE:
  
  PHASE 1 — PRE-MATCH LIQUIDATION WINDOW (detectable signal):
    When:     T-12h to T-2h before kickoff
    Event:    Losing-side prediction positions liquidated pre-match
    Effect:   Proceeds flow into WIN prediction pool
    Signal:   ON-CHAIN DETECTABLE — liquidation events visible pre-match
    Agent:    This is the PRE-MATCH SIGNAL that Model 1 does not produce.
              Elevated pre-match liquidation volume = elevated WIN pool = 
              elevated potential burn magnitude if WIN occurs.
    
  PHASE 2 — MATCH IN PROGRESS:
    No supply change during live match
    Prediction positions held until result
    
  PHASE 3 — RESULT SETTLEMENT:
    WIN:   Prediction market settles WIN positions
           Settlement proceeds used for $AFC BUYBACK from open market
           Purchased tokens immediately BURNED (permanent supply reduction)
    LOSS:  LOSS prediction positions receive settlement payout
           New tokens MINTED to treasury to fund LOSS payouts
    DRAW:  No supply change — market settles at no-movement
    
  PHASE 4 — ON-CHAIN CONFIRMATION:
    WIN:   Burn transaction visible on chiliscan.com (zero-address)
    LOSS:  Mint transaction visible (treasury address)
    DRAW:  No transaction
    
  TIMING:
    Pre-match:  YES — Phase 1 liquidation events are detectable pre-match
    Post-match: Settlement and burn/mint execute post-result confirmation
    
  THE PRE-MATCH LIQUIDATION SIGNAL (Model 2 only):
    This signal does not exist in Model 1.
    
    What it is:
      Elevated liquidation volume in the pre-match window indicates large
      prediction positions being closed before kickoff. This creates:
      a) A larger WIN pool (more proceeds available for buyback/burn)
      b) A measurable pre-match on-chain footprint for agents monitoring
      c) An indicator of community conviction about the match outcome
    
    How to detect:
      Monitor: chiliscan.com — fan token contract pre-match transactions
      Monitor: fantokens.com/fan-token-play — liquidation volume dashboard
      Time window: T-12h to T-2h (liquidation window per fantokens.com)
      Signal threshold: liquidation volume > 2× baseline = elevated signal
    
    What it means:
      High pre-match liquidation → large potential burn if WIN occurs
      Low pre-match liquidation → smaller burn even on WIN
      Pre-match liquidation spike without WIN = MINTING on LOSS
      
    Agent rule:
      NEVER treat pre-match liquidation as a confirmed burn signal.
      It is a POTENTIAL MAGNITUDE indicator — the WIN must still occur.
      Apply pre-match liquidation as a modifier to the WIN scenario only.
      Include in CDI pre-match note as: liquidation_pool_elevated = true/false
      
  AGENT REASONING CHAIN (Model 2):
    PRE-MATCH:
      1. Check liquidation volume at T-12h and T-2h windows
      2. If elevated: flag liquidation_pool_elevated = true
      3. Include in pre-match CDI note — do NOT yet adjust supply signal
      4. Generate standard pre-match signal with liquidation context note
      
    POST-MATCH:
      1. Confirm result from Tier 1 source
      2. WIN:  Check chiliscan.com for buyback + burn transaction
               Apply burn magnitude to CDI calculation
               Note actual burn amount in calibration record
      3. LOSS: Check for mint transaction
               Apply minting to CDI (negative supply signal)
      4. DRAW: No supply action — confirm no transaction on-chain
```

---

## Model identification

```
HOW TO IDENTIFY WHICH MODEL IS ACTIVE FOR A TOKEN:

  Source of truth: fantokens.com/fan-token-play (official listing)

  CONFIRMED MODEL 2 TOKENS (as of v3.97.2):
    $AFC — Arsenal FC (confirmed Model 2, April 2026)

  ALL OTHER FTP TOKENS:
    Assume Model 1 unless confirmed otherwise at fantokens.com
    
  WHEN IN DOUBT:
    Model 1 = no pre-match on-chain signal → skip pre-match liquidation check
    Model 2 = pre-match liquidation signal → run Phase 1 check at T-12h
    
  AGENT RULE:
    If token is not confirmed Model 2, do not look for pre-match liquidation.
    Treating a Model 1 token as Model 2 produces false signals.
```

---

## Signal timing comparison

```
TIMING COMPARISON — MODEL 1 vs MODEL 2:

  Event                    Model 1         Model 2
  ─────────────────────────────────────────────────
  Pre-match liquidation    NONE            T-12h to T-2h (DETECTABLE)
  Pre-match signal         None            Liquidation pool magnitude
  Match in progress        None            None
  Post-match settlement    Minutes         Minutes
  Burn (WIN)               On-chain        On-chain (buyback then burn)
  Mint (LOSS)              On-chain        On-chain (mint to treasury)
  Draw                     No change       No change

  KEY DIFFERENCE:
  Model 2 produces a pre-match detectable signal via liquidation events.
  This changes the agent reasoning chain — pre-match intelligence is
  available for Model 2 tokens that does not exist for Model 1 tokens.
  The pre-match signal does not guarantee a burn; it indicates potential
  burn magnitude IF a WIN occurs.
```

---

## Calibration records — FTP PATH_2

Three verified FTP PATH_2 calibration records (April 2026, $AFC, Model 2):

```
RECORD 1 — Arsenal WIN (burn confirmed)
  Date:         07/04/2026
  Competition:  UEFA Champions League 2025-26
  Match:        Sporting CP vs Arsenal
  Result:       Arsenal WIN (0–1)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    159,025 $AFC BURNED (permanent supply reduction)
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain
  Signal:       PATH_2 WIN burn confirmed. Largest verified $AFC burn record.
  
RECORD 2 — Arsenal LOSS (mint confirmed)
  Date:         11/04/2026
  Competition:  Premier League 2025-26
  Match:        Arsenal vs Bournemouth
  Result:       Arsenal LOSS (1–2)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    100,000 $AFC MINTED to treasury
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain
  Signal:       LOSS = supply INCREASE. Negative supply signal for $AFC.
                MINTING reduces the deflationary effect of PATH_2 for this
                match period. CDI: apply as negative supply signal.
  Note:         PATH_2 LOSS = minting is a NEGATIVE signal — not neutral.
                Each LOSS mints tokens that future WINs must re-burn.
  
RECORD 3 — Arsenal DRAW (no supply change)
  Date:         15/04/2026
  Competition:  UEFA Champions League 2025-26
  Match:        Arsenal vs Sporting CP
  Result:       DRAW (0–0)
  FTP model:    Model 2 — prediction/mint/burn
  FTP event:    No change — 0 burned, 0 minted
  Source:       fantokens.com/fan-token-play — VERIFIED on-chain
  Signal:       DRAW = supply neutral. No on-chain transaction expected.
                Confirm absence of transaction on chiliscan.com.

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

---

*SportMind v3.97.2 · MIT License · sportmind.dev*
*Source: fantokens.com/fan-token-play — VERIFIED*
