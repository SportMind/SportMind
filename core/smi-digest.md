# SportMind Intelligence State Digest

> **Designed for SMI agent reference context.**
> Load this file as a lightweight state summary before loading full layer skills.
> Tells agents what is current, what is complete, and where the gaps are.
> Updated after every versioned release.

**Last updated:** v3.97.5 — May 2026

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
  - Saudi Pro League: no dedicated sport domain file; coverage via football
    domain only — thin signal for SPL-specific variables
  - MLS: covered via american-football domain; club-level intelligence thin

Modifiers needing update: none flagged

Source: core/sport-tiers.md (quarterly review: Jan/Apr/Jul/Oct)
```

---

## LAYER 2 — ATHLETE INTELLIGENCE

```
Coverage:        29 sports

Known gaps:
  - Saudi Pro League: athlete profiles sparse (Ronaldo, Benzema era intelligence
    built; broader SPL roster intelligence thin)
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

Known gaps:
  - Model 2 pre-liquidation signal timing: calibration records needed
    (T-12h to T-2h liquidation window — only $AFC records exist so far)
  - Middle East fan token market: thin; no Gulf/Saudi-specific intelligence
  - Women's football fan tokens: not modelled
  - Esports fan tokens: intelligence exists but thinner than football tier

Active tokens tracked (Tier A — BRIDGE_LIVE confirmed):
  $AFC   $ACM   $ARG   $ASR   $ATM   $BAR
  $CITY  $FLU   $GAL   $INTER $JUV   $MENGO
  $NAP   $OG    $POR   $PSG   $SPURS $VCF
  + $CHZ (native chain token) + $PEPPER

FTP PATH_2 live data source: fantokens.com/fan-token-play
UCL 2025-26 context:
  $AFC ucl_standing: FINALIST | opponent: PSG
  $PSG ucl_standing: FINALIST | opponent: Arsenal
  UCL Final: 30 May 2026, Puskás Aréna, Budapest
  
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
  - Saudi Pro League: commercial tier not assessed; SPL TV deal and
    sponsorship structure not modelled
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
```

---

## KNOWN LIBRARY GAPS — PRIORITY ORDER

```
1. Saudi Pro League — sport domain, athlete, and market layers all thin
   Action: community contribution priority; stub files exist in sports/
   
2. Middle East regulatory framework — macro layer missing
   Action: monitor UAE VARA and Saudi SAMA for classification guidance
   
3. MLS — market and athlete layers thin
   Action: US fan token regulatory clarity now confirmed; MLS intelligence
   can be built with LEGALLY_DEFINED / NON_SECURITY foundation
   
4. Esports — sport domain playbook incomplete
   Action: game-title-specific playbooks needed (CSGO, LoL, Dota 2, Valorant)
   
5. Latin America regulatory status — macro layer thin
   Action: Brazil partial; Argentina, Colombia, Mexico not covered
   
6. FanToken.com Model 2 pre-liquidation calibration records needed
   Action: T-12h to T-2h liquidation window records for $AFC; expand to
   other Model 2 tokens when confirmed
   
7. Women's football market and fan tokens — not modelled
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

MACRO EVENTS PROCESSED:
  SI 2026/102 enacted — UK STATUTORY_REGIME_ENACTED (February 2026)
  Chiliz Bridge LIVE — 18 tokens MULTICHAIN_ACTIVE + BRIDGE_LIVE
  Decimal migration — all Fan Tokens 0 → 18 decimal (April 27, 2026)
  $AFC PATH_2 Model 2 confirmed — April 2026
  UCL 2025-26 Final confirmed — PSG vs Arsenal, May 30, Budapest
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
  UCL/competition:      Update on confirmed results — check league-football-token-intelligence.md
  Gap priority order:   Reassess quarterly (aligns with tier review schedule)
```

---

*SportMind v3.97.5 · MIT License · sportmind.dev*
*SMI Digest — agent reference state summary*
