# $AFC — Arsenal FC Fan Token Intelligence

**Single-token reference file for $AFC (Arsenal FC Fan Token).
Consolidates supply intelligence, FTP PATH_2 mechanics, competition standing,
and agent reasoning for the most intelligence-rich token in the SportMind library.**

> Cross-references: `fan-token/league-football-token-intelligence.md` (PL/UCL context)
> Cross-references: `fan-token/ftp-path2.md` (FTP Model 2 mechanics)
> Cross-references: `fan-token/supply-intelligence.md` (supply template)

---

## Token overview

```
TOKEN:            $AFC
CLUB:             Arsenal FC
LEAGUE:           Premier League (England)
CHAIN:            Chiliz Chain (native) | Solana + Base (via LayerZero, BRIDGE_LIVE)
CONTRACT:         Post-April 27, 2026 (18-decimal migration — verify at chiliscan.com)
FTP MODEL:        Model 2 — Prediction Market Settlement (CONFIRMED, April 2026)
PATH_2:           CONFIRMED — WIN burns | LOSS mints | DRAW neutral
SUPPLY STATUS:    BRIDGE_LIVE + MULTICHAIN_ACTIVE
TIER:             Tier A — Fan Token Active
```

---

## Supply intelligence

```
SUPPLY INTELLIGENCE — $AFC (Arsenal FC Fan Token)
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
    breakdown: −159,025 burned (Apr 7 UCL WIN) + 100,000 minted (Apr 11 PL LOSS)
    Status: DEFLATIONARY — net burn > net mint this period ✓

  pre_liquidation_pool:    ~111,500 tokens
    calculation: 44,600,000 ÷ 400 = 111,500
    this is the fixed 1/400 pre-liquidated before each qualifying match

  stop_loss_status:        CLEAR
    floor: 75% net supply reduction
    current reduction: well below floor
    credit_balance: 0 (stop-loss not reached)

  ftp_model:               Model 2 (confirmed)
  ucl_standing:            FINALIST (2025-26) | opponent: PSG
  ucl_final:               30 May 2026 · Puskás Aréna, Budapest
```

---

## FTP PATH_2 signal chain

```
$AFC PATH_2 — AGENT REASONING CHAIN:

  STEP 0 — SCOPE CHECK:
    Is the match an official men's first-team competitive fixture?
    YES → proceed | NO → no FTP event; supply signal = none

  STEP 1 — PRE-MATCH (within T-48h):
    Monitor chiliscan.com for pre-liquidation transaction
    Expected amount: ~111,500 tokens (circulating_supply ÷ 400)
    If confirmed: set ftp_preliquidation_confirmed = true
    If not observed by T-2h: flag for investigation (may be processing)

  STEP 2 — RESULT CONFIRMATION:
    Confirm result from Tier 1 source (UEFA/PL official, BBC Sport, etc.)

  STEP 3 — SUPPLY EVENT:
    WIN:   Check chiliscan.com for buyback + burn within 48h of full-time
           Apply actual burn amount to CDI calculation
           Update circulating_supply (decrease) and last_ftp_event
    LOSS:  Check for mint transaction within 48h of full-time
           Confirm credit_balance = 0 before applying mint signal
           Apply mint amount to CDI (negative supply signal)
           Update circulating_supply (increase) and last_ftp_event
    DRAW:  Confirm no on-chain transaction
           No supply change — last_ftp_event unchanged

  STEP 4 — UPDATE SUPPLY BLOCK:
    After each event: update circulating_supply, last_ftp_event, net_ftp_change_ytd
    Recalculate: pre_liquidation_pool = new_circulating_supply ÷ 400

UCL FINAL CONTEXT (30 May 2026):
  Largest potential $AFC burn in library history if Arsenal WIN
  Estimated: 250,000–500,000 $AFC burned (finals pool larger than standard match)
  Arsenal LOSS estimate: 120,000–180,000 $AFC minted
  Pre-liquidation window: within 48h of kickoff (by ~16:00 CEST 30 May)
  Probability-weighted expected supply change: −108,000 $AFC (per v3.97.7 signal)
```

---

## Competition standing

```
CURRENT COMPETITION STANDING:
  Premier League 2025-26:         Active (season in progress)
  UEFA Champions League 2025-26:  FINALIST
    Opponent:   PSG ($PSG)
    Date:       30 May 2026
    Venue:      Puskás Aréna, Budapest, Hungary
    Context:    Arsenal's first UCL Final since 2006 (19-year wait)

UCL ROUTE TO FINAL:
  QF Leg 2: Sporting CP vs Arsenal — WIN (0–1) → PATH_2 burn 159,025 ✓
  QF Leg 1: Arsenal vs Sporting CP — DRAW (0–0) → no supply change ✓
  SF:       Arsenal vs Atlético Madrid — WIN 2–1 on aggregate → PATH_2 burn (unrecorded)

FTP CALIBRATION RECORDS (April 2026):
  UCL 07/04: Sporting CP vs Arsenal → Arsenal WIN → −159,025 burned ✓
  PL  11/04: Arsenal vs Bournemouth → Arsenal LOSS (1–2) → +100,000 minted ✗
  UCL 15/04: Arsenal vs Sporting CP → DRAW (0–0) → 0 supply change ✗
```

---

## Key athlete flags

```
KEY PLAYER FLAGS (library state May 8, 2026):
  Bukayo Saka (RW):        ⚠ FLAG — monitor at T-48h before UCL Final
    Saka FIT → ATM ×1.10 for Arsenal signals (+4–6 adjusted score points)
    Saka ABSENT → ATM ×0.85 (−8–10 adjusted score points)
  
  William Saliba (CB):     EXPECTED FIT — outstanding UCL run
  Declan Rice (CM):        EXPECTED FIT — engine of Arsenal's press
  Martin Ødegaard (CAM):   MONITOR — late season load management
  Kai Havertz (CF):        EXPECTED FIT

  LOAD agents: athlete/football/athlete-intel-football.md for full commands
```

---

## CDI signal weights — $AFC

```
$AFC CDI WEIGHTS (football domain + PATH_2 active):

  Component           Weight   Notes
  ──────────────────────────────────────────────────────
  Sports catalyst      30%     Match result + PATH_2 supply event combined
  Supply mechanics     25%     PATH_2 burn/mint magnitude (unique to $AFC)
  Market/whale flows   20%     On-chain accumulation pre-match (Model 2 signal)
  Social sentiment     15%     Arsenal global fan base + PATH_2 community awareness
  Macro               10%     CHZ/BTC cycle backdrop

  NOTE: $AFC has a dedicated supply mechanics weight (25%) not present in
  standard football CDI. This reflects the confirmed Model 2 mechanics that
  create a distinct on-chain signal layer before and after each match.

SIGNAL AMPLIFIERS:
  UCL Final match:     CDI × 1.25 (highest match importance)
  PATH_2 active:       WIN signal amplified (supply burn confirmed)
  BRIDGE_LIVE:         CDI ceiling +5% (expanded liquidity pathways)
  Pre-liquidation high: ftp_pool_elevated flag in CDI output
```

---

## Regulatory context — UK and US

```
UK ($AFC primary domestic market):
  SI 2026/102 — STATUTORY_REGIME_ENACTED
  No new compliance barriers for UK $AFC holders before 30 May 2026.
  FCA gateway opens 30 September 2026 — Arsenal FC planning required.
  UK holders can trade on Solana/Base (post-omnichain) without friction.

US:
  LEGALLY_DEFINED / NON_SECURITY (SEC/CFTC March 2026)
  $AFC tradeable on Solana and Base — accessible to US holders directly.
  First-mover advantage window active for US market entry.
```

---

## Compatibility

**League context:** `fan-token/league-football-token-intelligence.md`
**FTP mechanics:** `fan-token/ftp-path2.md`
**Supply template:** `fan-token/supply-intelligence.md`
**Athlete:**        `athlete/football/athlete-intel-football.md`
**Sport domain:**   `sports/football/sport-domain-football.md`
**Calibration:**    `community/calibration-data/football/2026/04/`
**UCL signal:**     `examples/calibration/ucl-final-2026-psg-arsenal-signal.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Arsenal-specific fan token intelligence: $AFC profile, FTP PATH_2 mechanics, CDI |
| Reasoning | ACTIVE | Arsenal token reasoning chain from club signal to $AFC modifier |
| Context | ACTIVE | Arsenal context: PL Champions 2025/26, UCL Final 2026, FTP PATH_2 active |
| Memory | ACTIVE | Arsenal token history: three verified PATH_2 calibration records (April 2026) |
| Judgment | ACTIVE | Judgment on Arsenal-specific signal materiality — FTP PATH_2 adds supply event layer |
| Attention | ACTIVE | Elevated attention for Arsenal match results — all trigger PATH_2 supply events |
| Communication | ACTIVE | Arsenal token output: CDI modifier, PATH_2 status, supply event type |
| Verification | ACTIVE | Arsenal PATH_2 events verified via chiliscan.com on-chain confirmation |
| Learning | ACTIVE | Arsenal calibration data — three PATH_2 records provide verified supply baseline |
| Integration | ACTIVE | Integrates with ftp-path2.md, complete-registry.md, and athlete/football/arsenal-afc.md |
| Calibration | ACTIVE | Arsenal PATH_2 calibration: WIN burn (159,025), LOSS mint (100,000), DRAW (0) verified |
| Adaptation | ACTIVE | Arsenal intelligence adapts as PATH_2 pool sizes and club performance evolves |
| Ethics | NOT APPLICABLE | Arsenal token intelligence is sports/crypto analysis — no ethical dimension |
| Transparency | ACTIVE | PATH_2 supply event outcome and on-chain source explicit in all Arsenal outputs |
| Execution | ACTIVE | Signal generation workflow, event playbooks, and structured output templates defined |
| Collaboration | ACTIVE | Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer |


---

*SportMind v3.97.10 · MIT License · sportmind.dev*
*$AFC supply data verified: 2026-05-08*
*Source: fantokens.com/trade/arsenal-fan-token*
