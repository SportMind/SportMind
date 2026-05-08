# SportMind Intelligence State Digest

> **Designed for SMI agent reference context.**
> Load this file as a lightweight state summary before loading full layer skills.
> Tells agents what is current, what is complete, and where the gaps are.
> Updated after every versioned release.

**Last updated:** v3.97.9 — 2026-05-08
**Library state:** 610 files · 391 markdown · 178 CHANGELOG entries · Tier B sports: 6

---

## LAYER 1 — SPORT DOMAIN

```
Coverage:        42 sports
Tier A (full):   football, basketball, mma, formula1, motogp, cricket
Tier B (monitored): rugby-union, tennis, athletics, esports, rugby-league
Tier C (stubs):  32 remaining sports

Known gaps:
  - Esports: sport domain playbook incomplete (multiple game titles need
    individual playbooks — CSGO, LoL, Dota 2 not fully differentiated)
  - Saudi Pro League: PARTIALLY FILLED (v3.97.8) —
    sports/football/sport-domain-football-saudi-pro-league.md created.
    Remaining gap: zero calibration records; modifiers unverified.
  - MLS: covered via american-football domain; club-level intelligence thin

Modifiers needing update: none flagged

Source: core/sport-tiers.md (quarterly review: Jan/Apr/Jul/Oct)
```

---

## LAYER 2 — ATHLETE INTELLIGENCE

```
Coverage:        29 sports

Known gaps:
  - Saudi Pro League: PARTIALLY FILLED (v3.97.8) —
    athlete/football/athlete-intel-saudi-pro-league.md created.
    Covers Ronaldo, Benzema, Neymar profiles and heat/load modifiers.
    Remaining gap: composite modifier values unverified (0 calibration records).
  - MLS: athlete modifier profiles thin for non-DP (Designated Player) slots
  - Esports: player-level intelligence at roster level only; individual
    performance modifiers not built for most titles

Modifiers needing update: none flagged
```

---

## LAYER 3 — FAN TOKEN COMMERCIAL

```
Coverage:        65 skills across 41 subdirectories + 7 root files

FTP PATH_2 status:
  Model 1 — Treasury/Smart Contract:    DOCUMENTED (gamified-tokenomics-intelligence/)
  Model 2 — Prediction Market:          DOCUMENTED (fan-token/ftp-path2.md)
  $AFC PATH_2 confirmed:                Model 2 — April 2026
  Mechanics fully confirmed (v3.97.9 — Chiliz official, April 2026):
    Pre-liquidation ratio: 1/400 of total supply per qualifying match
    Stop-loss: burns cease at 75% net reduction or treasury = 0%
    Credit burns: wins at stop-loss generate credits offsetting future mints
    Vesting cap: 12.5%/year of treasury (not active for any club yet)
    Annual inflation (Model 1): 1–5% linked to season performance
    Scope: men's competitive first-team only (no friendlies/pre-season/women's)
    Execution windows: liquidations ≤48h pre-kickoff · buybacks ≤48h post-result
  
  CONFIRMED MECHANICS (v3.97.9 — Chiliz official, April 2026):
    Pre-liquidation ratio:  1/400 of total supply per qualifying match
    Stop-loss floor:        75% net supply reduction OR treasury = 0%
    Credit burn system:     Wins at stop-loss generate credits offsetting future mints
    Vesting cap:            12.5% of treasury/year (not active for any club yet)
    Annual inflation:       1–5% seasonal rate (Model 1, linked to season performance)
    Scope:                  Official men's first-team competitive matches only
                            Friendlies, pre-season, women's, academy — excluded
    Execution windows:      Liquidations ≤48h pre-kickoff | Buybacks ≤48h post-result

Known gaps:
  - Model 2 pre-liquidation mechanics: FILLED (v3.97.9) — 1/400 ratio
    confirmed from Chiliz official. Remaining gap: pre-match liquidation
    volume calibration records (the timing window is now confirmed; actual
    on-chain volume records during the window are still needed)
  - Middle East fan token market: thin; no Gulf/Saudi-specific intelligence
  - Women's football fan tokens: not modelled
  - Esports fan tokens: intelligence exists but thinner than football tier

Active tokens tracked (Tier A — BRIDGE_LIVE confirmed):
  $AFC   $ACM   $ARG   $ASR   $ATM   $BAR
  $CITY  $FLU   $GAL   $INTER $JUV   $MENGO
  $NAP   $OG    $POR   $PSG   $SPURS $VCF
  + $CHZ (native chain token) + $PEPPER

FTP PATH_2 live data source: fantokens.com/fan-token-play
FTP model documentation: fan-token/ftp-path2.md (Model 1 + Model 2)
UCL 2025-26 context:
  $AFC ucl_standing: FINALIST | opponent: PSG
  $PSG ucl_standing: FINALIST | opponent: Arsenal
  UCL Final: 30 May 2026, Puskás Aréna, Budapest
  Pre-match signal: examples/calibration/ucl-final-2026-psg-arsenal-signal.md
  $AFC WIN → ~300–500k burned (largest potential $AFC burn in history)
  $PSG: demand-only signal — no confirmed supply mechanic
  
Omnichain status (confirmed April 2026):
  18 tokens: MULTICHAIN_ACTIVE + BRIDGE_LIVE
  Chains: Chiliz Chain (native) + Solana + Base (via LayerZero)
  Decimal migration: 0 → 18 decimal precision (April 27, 2026)
  All 18 have new post-migration contract addresses
```

---

## LAYER 4 — MARKET INTELLIGENCE

```
Coverage:        43 documents

Known gaps:
  - Saudi Pro League: PARTIALLY FILLED (v3.97.8) —
    market/market-saudi-pro-league.md created.
    Covers PIF structure, fanbase, FT launch probability, transfer impact.
    Remaining gap: KSA regulatory position not fully mapped in macro layer.
  - MLS: fanbase depth thin; US market post-fan-token regulatory
    clarity not fully modelled
  - Middle East market expansion: not modelled (UAE, Qatar, Saudi
    fan token demand not assessed)
  - Women's football market: not modelled

Modifiers needing update: none flagged
```

---

## LAYER 5 — MACRO INTELLIGENCE

```
Coverage:        9 documents

Current regulatory status (confirmed):
  UK:   STATUTORY_REGIME_ENACTED — SI 2026/102 (FSMA 2000 Cryptoassets)
        fca_gateway_date: 2026-09-30 (application period opens)
        Application window: 30 Sep 2026 – 28 Feb 2027
        Regime commencement: 25 October 2027
  US:   LEGALLY_DEFINED / NON_SECURITY
        Joint SEC/CFTC guidance March 17, 2026
        Classification: digital collectibles and digital tools
        Fan Tokens™ not securities — US market open
  EU:   MiCA ACTIVE — Markets in Crypto-Assets Regulation operative
  ASIA: Monitoring — no single confirmed framework

Known gaps:
  - Middle East regulatory framework: not documented
    (UAE VARA, Saudi SAMA positions not modelled)
  - Latin America: regulatory status thin (Brazil partial coverage only)
  - India: regulatory position unclear; not modelled despite large fan base

Modifiers needing update: none flagged

CHZ macro state (current):
  Load macro/macro-crypto-market-cycles.md for live modifier
  CHZ virtuous cycle: buyback/burn programme active
  Omnichain expansion: liquidity amplifier confirmed active
```

---

## LAYER 6 — DEPLOYMENT INTELLIGENCE

```
Coverage:        6 skills (telegram/)

Skills:
  README.md                     Layer overview, OpenClaw/LobsterClawBot compatibility
  sentiment-monitor.md          Community sentiment Tier S/A/B/C/D classification
  price-movement-explainer.md   Five-cause identification protocol
  pre-match-signal.md           T-48h → T+1h delivery timeline
  macro-event-interpreter.md    P1–P6 macro event message templates
  examples/fan-token-trading-bot.md  $AFC PATH_2 worked example

Compatibility: Telegram Bot API 9.6 · OpenClaw · @LobsterClawBot
Known gaps: Only football ($AFC) worked example exists
```

---

## CALIBRATION BASE

```
Total records:   129
Direction accuracy: 96% (across 21 sports)
Calibration format: community/calibration-data/{sport}/{year}/{month}/

Tier A sports priority: ACTIVE
Priority queue: football > mma > formula1 > cricket > basketball > motogp

Last FTP PATH_2 records added (April 2026 — Model 2 verified):
  UCL 07/04/2026: Sporting CP vs Arsenal → Arsenal WIN (0-1)
    FTP: 159,025 $AFC BURNED — direction correct ✓
  PL  11/04/2026: Arsenal vs Bournemouth → Arsenal LOSS (1-2)
    FTP: 100,000 $AFC MINTED — direction wrong ✗
    Note: LOSS = supply INCREASE (negative signal — important calibration)
  UCL 15/04/2026: Arsenal vs Sporting CP → DRAW (0-0)
    FTP: 0 burned / 0 minted — direction wrong ✗

Cumulative $AFC FTP (April 2026):
  Net supply reduction: 59,025 $AFC (159,025 burned − 100,000 minted)

Modifiers flagged for recalibration: none

Upcoming calibration events:
  UCL Final 30 May 2026 — $AFC PATH_2 result (WIN/LOSS/DRAW)
  Expected largest single $AFC PATH_2 record if Arsenal WIN (~300–500k burned)
  Pre-match liquidation data to collect May 30 T-12h to T-2h window
```

---

## KNOWN LIBRARY GAPS — PRIORITY ORDER

```
1. Saudi Pro League — PARTIALLY FILLED (v3.97.8)
   Filled: Layer 1 (sport domain), Layer 2 (athlete intel), Layer 3 (market)
   Remaining: KSA macro regulatory (macro layer), calibration records (0),
   MLS intelligence, esports playbook completion
   Immediate next: submit first 5 SPL calibration records (PIF derby outcomes)
   
2. Middle East regulatory framework — macro layer missing
   Action: monitor UAE VARA and Saudi SAMA for classification guidance
   
3. MLS — market and athlete layers thin
   Action: US fan token regulatory clarity now confirmed; MLS intelligence
   can be built with LEGALLY_DEFINED / NON_SECURITY foundation
   
4. Esports — sport domain playbook incomplete
   Action: game-title-specific playbooks needed (CSGO, LoL, Dota 2, Valorant)
   
5. Latin America regulatory status — macro layer thin
   Action: Brazil partial; Argentina, Colombia, Mexico not covered
   
6. Model 2 pre-liquidation calibration records needed
   Mechanics now fully confirmed (v3.97.9). Remaining gap: empirical records
   documenting actual pre-liquidation amounts on chiliscan.com to verify the
   1/400 ratio in live conditions and build WIN pool size prediction models.
   Action: collect pre-match chiliscan.com data for next $AFC qualifying match.
   
7. UCL Final T-48h, T-24h, T-2h signal updates
   Action: v3.97.7 signal is PLANNING quality (T-22 days). Execution-quality
   signals required at T-48h (lineups emerging), T-24h (team news), T-2h
   (confirmed lineups). Saka availability is the critical athlete flag.
   
8. Women's football market and fan tokens — not modelled
   Action: WSL, NWSL, Liga F fan token pipeline monitoring needed
```

---

## SOURCES ADDED SINCE LAST UPDATE

```
VERIFIED TIER 1 SOURCES (confirmed active):
  fantokens.com/fan-token-play     Official FTP data — Model 1 and Model 2
  fantokens.com                    Fan token registry, supply data
  chiliscan.com                    On-chain verification (Chiliz Chain explorer)
  legislation.gov.uk               UK SI 2026/102 regulatory source
  @Chiliz (official X)             Bridge live confirmation, omnichain launch
  banking.senate.gov/hearings      CLARITY Act — monitoring (UNVERIFIED)
  athlete/football/athlete-intel-football.md   Knockout modifier confirmed
  Arab News Sport (arabnews.com/sport)  SPL fixtures, results, signings — v3.97.8
  spl.com.sa                       Saudi Pro League official standings/schedules — v3.97.8
  pif.gov.sa                       PIF investment decisions and announcements — v3.97.8
  chiliz.com (FTP announcement)    Fan Token Play mechanics — primary source — v3.97.9
  chiliz.com (FTP explainer)       Win-and-burn explainer — secondary source — v3.97.9
  chiliz.com/chiliz-group-announces-gamified-fan-tokens-...  FTP mechanics — v3.97.9
  chiliz.com/win-and-they-burn-lose-and-they-mint-...        FTP explainer — v3.97.9

MACRO EVENTS PROCESSED:
  SI 2026/102 enacted — UK STATUTORY_REGIME_ENACTED (February 2026)
  Chiliz Bridge LIVE — 18 tokens MULTICHAIN_ACTIVE + BRIDGE_LIVE
  Decimal migration — all Fan Tokens 0 → 18 decimal (April 27, 2026)
  $AFC PATH_2 Model 2 confirmed — April 2026
  UCL 2025-26 Final confirmed — PSG vs Arsenal, May 30, Budapest
  CLARITY Act markup — UNVERIFIED/MONITOR (2026-05-08)
  UCL Final pre-match signal published — v3.97.7 (2026-05-08)
  Saudi Pro League intelligence built — Layers 1, 2, 3 — v3.97.8 (2026-05-08)
  FTP PATH_2 seven mechanics confirmed — v3.97.9 (2026-05-08)
  FTP PATH_2 seven confirmed mechanics — Chiliz Group official — v3.97.9 (2026-05-08)
```

---

## UPDATE INSTRUCTIONS

```
This file is updated after every versioned release. Update the following:

  - Last updated: version and date (top of file)
  - Layer coverage counts if changed (new files added to any layer)
  - Known gaps filled by the release (remove from gaps list)
  - New gaps identified in the release (add to priority ordered gaps list)
  - Modifier values changed (recalibration events)
  - New official sources added or verified
  - Calibration base count (update total and add recent records)
  - Regulatory status changes (key macro events)
  - Active token UCL/competition standing if changed
  - FTP PATH_2 status if any new tokens confirmed

FIELD PRIORITIES:
  Calibration count:    Always accurate — check community/calibration-data/
  Regulatory status:    Always current — check macro/macro-regulatory-sportfi.md
  FTP PATH_2 tokens:    Always current — check fan-token/ftp-path2.md
                        Key: 1/400 pre-liquidation ratio now confirmed (calculable)
                        Key: credit burn check required before any loss/mint signal
  UCL/competition:      Update on confirmed results — check league-football-token-intelligence.md
  Gap priority order:   Reassess quarterly (aligns with tier review schedule)
```

---

*SportMind v3.97.9 · MIT License · sportmind.dev*
*SMI Digest — agent reference state summary*
