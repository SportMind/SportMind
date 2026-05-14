# SportMind Intelligence State Digest

> **Designed for SMI agent reference context.**
> Load this file as a lightweight state summary before loading full layer skills.
> Tells agents what is current, what is complete, and where the gaps are.
> Updated after every versioned release.

**Last updated:** 3.97.46 — 2026-05-13
**Library state:** 673 files · 454 markdown · 212 CHANGELOG entries · 181 version cycles

---

## THE SPORTMIND LIBRARY RULE

```
Core question: Will this intelligence still be true and useful in six months?
  YES → belongs in the library
  NO  → does not belong

ENDURING (belongs): reasoning patterns · structural mechanics ·
  regulatory frameworks · calibration records · modifier weights
EXPIRING (does not): injury status · live prices · standings ·
  scheduled dates · transfer rumours · named player current form ·
  pending/unconfirmed transactions · specific match predictions

Three tests: (1) framework or data point? (2) true in six months?
  (3) teaches how to think or tells what is true now?

Load CONTRIBUTING.md for the full rule before submitting any contribution.
Load llms.txt for the agent-facing compact version.
```

---

## MANDATORY LOADING ORDER

```
Before any signal or analysis:
  1. core/smi-digest.md           (this file — library state)
  2. macro/macro-regulatory-sportfi.md
  3. macro/macro-crypto-market-cycles.md
  4. fan-token/ftp-path2.md
  5. sports/[relevant-sport]/sport-domain-[sport].md
  6. athlete/[club].md
  7. core/agent-reasoning-chains.md
  8. core/signal-confidence-framework.md (check before output)

Priority conflict resolution: macro override > PATH_2 supply >
  athlete absences > sport domain > venue/weather > psychological/historical
```

---

## SEVEN INTELLIGENCE DOMAINS — CURRENT STATE

### DOMAIN 1 — Sport Domain (`sports/`)

```
Coverage:          42 sports — 62 markdown files
FULL (200L+):      football (8 files incl. WC/Euros/AFCON/Copa/Saudi PL),
                   cricket (2), basketball (2), formula1 (2), mma (2),
                   esports (6), ice-hockey, kabaddi, handball, tennis,
                   golf, horse-racing, cycling, darts, baseball, afl,
                   motogp, nascar, athletics, boxing, snooker,
                   winter-sports, american-football, womens-football,
                   combat-sports-specific, rugby-union-specific, motorsport-specific

MEDIUM/STUB:       badminton, curling, fencing, field-hockey, gymnastics,
                   judo, netball, rowing, rugby-league, sailing, squash,
                   swimming, swimming-open-water, table-tennis, taekwondo,
                   triathlon, volleyball, weightlifting
                   (all structurally present; 141–199L; not fully calibrated)

Known gaps (not yet actioned):
  - Rugby-league: stub level (183L) despite calibration data and active token file
  - Netball: stub level (175L) despite calibration data and token file
  - Rowing: stub level (178L) despite calibration data
  - Basketball: no NBA-specific or EuroLeague-specific competition file
  - Tennis: no ATP/WTA circuit-specific file; no Grand Slam surface differentiation
  - Cricket: no IPL, BBL, or CPL-specific file (highest future fan token potential)
  - NFL: no playoff/bye-week/draft intelligence despite CLARITY Act opening US market
  - Esports: Valorant missing (VIT $VIT active); LoL missing; mobile esports absent
  - Women's sport: womens-football.md exists; women's cricket, WNBA, WTA, women's rugby absent
```

### DOMAIN 2 — Athlete Intelligence (`athlete/`)

```
Coverage:          29 sports — 45 markdown files
Football clubs:    arsenal-afc (deepest — full PATH_2 integration)
                   mancity-city, psg-psg, barcelona-bar, atletico-madrid-atm,
                   juventus-juv, acmilan-acm, inter-milan-inter, napoli-nap,
                   porto-por, galatasaray-gal, tottenham-hotspur-spurs
                   + tier-a-clubs-framework + athlete-intel-football
                   + athlete-intel-saudi-pro-league
Esports:           vitality-vit, athlete-intel-esports
All other sports:  one generic intelligence file per sport

Key frameworks (enduring):
  Tier A absence modifiers: defined per position per club
  New manager effect: 1-5 matches ×1.06 | 6-15 ×1.02 | 16+ baseline
  Relegation framework (universal Tier A): bottom 3 ×0.83 | relegated ×0.60-0.70
  Left CB / defensive versatility (Arsenal): right-footed at left CB ×0.97 discount

Known gaps:
  - $BAR, $CITY, $PSG, $JUV, $ACM club files less developed than arsenal-afc.md
  - No PATH_2 integration in any club file except arsenal-afc.md (correct — $AFC only)
  - NBA, NFL, NHL — generic intelligence only; no franchise-specific files
  - Agent/representative intelligence: absent (player agent activity as transfer signal)
  - Press conference intelligence: absent (manager language patterns as pre-match signal)
```

### DOMAIN 3 — Fan Token Commercial (`fan-token/`)

```
Coverage:          76 markdown files across 40+ directories
Root:              ftp-path2.md, governance-intelligence.md, portfolio-intelligence.md,
                   supply-intelligence.md, national-team-tokens.md, arsenal.md,
                   ecosystem-health-intelligence.md, emerging-sports-pipeline.md,
                   official-verification-framework.md, fraud-risk-intelligence.md,
                   league-football-token-intelligence.md, tournament-elimination-intelligence.md,
                   fan-holder-profile-intelligence.md, fan-token-exchange-intelligence.md,
                   fan-token-layer-overview.md, fan-token-why.md

FTP PATH_2 status:
  Confirmed:        $AFC (Arsenal) — Model 2 — April 2026
  Mechanics:        Pre-liquidation ratio: 1/400 of circulating supply
                    Stop-loss: 75% net reduction or treasury = 0%
                    Credit burns: wins at stop-loss generate offsetting credits
                    Scope: men's competitive first-team only
                    Execution: liquidations ≤48h pre-kickoff | buybacks ≤48h post-result
  Multiplier:       April 2026 calibration: 1/400 → ×1.59 actual
                    Central estimate: ×1.50 | Range: ×1.40–×2.0
  All other tokens: demand-only signals — no supply mechanics confirmed
  Source:           fan-token/ftp-path2.md | fantokens.com/fan-token-play

Active tokens (BRIDGE_LIVE — Chiliz Chain + Solana + Base via LayerZero):
  $AFC $ACM $ARG $ASR $ATM $BAR $CITY $FLU $GAL $INTER $JUV $MENGO
  $NAP $OG $POR $PSG $SPURS $VCF + $CHZ (native) + $PEPPER

Verification (v3.97.44):
  Confirmed national team tokens: $ARG · $POR · $SNFT · $BFT only
  All other national team claims: UNVERIFIED until four-source verification
  Four-source method: club official → socios.com → chiliscan.com → fantokens.com
  Framework: fan-token/official-verification-framework.md
  Red flags: fan-token/fraud-risk-intelligence.md

Ecosystem health modifier (quarterly assessment):
  Load: fan-token/ecosystem-health-intelligence.md
  Five-dimension maturity: MATURE (8-10) ×1.10 | DEVELOPING standard | EARLY ×0.88

Known gaps:
  fan-token/registry/complete-registry.md — MISSING (HIGH PRIORITY)
    official-verification-framework.md references this file.
    bridge-supported.md exists; complete-registry.md does not.
    Positive match lookups have no reference target.
```

### DOMAIN 4 — Market Intelligence (`market/`)

```
Coverage:          44 markdown files
Per-sport:         Market intelligence for 34 sports
Cross-sport:       broadcaster-media-intelligence, club-operations-intelligence,
                   euroleague-basketball-intelligence, three international cycle files

Known gaps:
  - Women's sport market: not modelled
  - i18n layer (20 files): Arabic, French, Spanish, German, Hindi, Japanese,
    Portuguese translations of selected files. Not maintained since early builds.
    Likely contains stale modifier values from pre-v3.97.20.
    Action needed: systematic update or explicit deprecation notice.
```

### DOMAIN 5 — Macro Intelligence (`macro/`)

```
Coverage:          14 markdown files (COMPLETE — full layer)

Files:             macro-regulatory-sportfi.md (primary — 1162L)
                   macro-crypto-market-cycles.md · crypto-digital-asset-intelligence.md
                   institutional-intelligence.md · exchange-intelligence.md
                   government-intelligence.md · tournament-macro.md
                   macro-broadcast-disruption.md · macro-climate-weather.md
                   macro-economic-cycles.md · macro-geopolitical.md
                   macro-governance-scandal.md · macro-pandemic-public-health.md
                   macro-overview.md

Regulatory status (confirmed):
  UK:   STATUTORY_REGIME_ENACTED — SI 2026/102 — FCA gateway Sep 2026
  US:   LEGALLY_DEFINED / NON_SECURITY (SEC/CFTC March 2026)
        CLARITY Act: DRAFT_RELEASED + LEGISLATIVE_MARKUP_IN_PROGRESS
        Section 404 (DRAFT_STABLE): activity-based rewards PERMITTED
                                    passive yield PROHIBITED
  EU:   MiCA ACTIVE
  UAE:  VARA — HIGH (enacted, comprehensive)
  Qatar: QFC — HIGH (within QFC jurisdiction)
  Bahrain: CBB — HIGH (stablecoin clarity included)
  Saudi: M/121 Unified Sports Law — HIGH (enacted)
  Oman: OIFC Royal Decree 8/2026 — MEDIUM_HIGH (enacted)
  Kuwait: RESTRICTIVE — LOW (FATF grey list February 2026)
  India: not modelled (regulatory position unclear — large fanbase gap)
  Latin America: Brazil partial; Argentina, Colombia, Mexico not covered

Crypto cycle modifiers (load macro-crypto-market-cycles.md for current phase):
  BTC dominance >60%: ×0.88 all tokens | <50%: ×1.15 | alt season: ×1.20
  Bull market: ×1.15 | Bear: ×0.85
  CHZ virtuous cycle (all 3 conditions): ×1.12 | Breakdown: ×0.93

Exchange signals:
  Tier 1 new listing: +20-40% spike | +15-25% new baseline
  CHZ delisting from major exchange: ×0.82 ALL fan tokens
```

### DOMAIN 6 — Blockchain / On-Chain Intelligence (`core/`)

```
Coverage:          core/blockchain-onchain-intelligence.md
Primary source:    chiliscan.com (Chiliz Chain explorer)
Data source:       fantokens.com/fan-token-play (FTP PATH_2 monitoring)

Key modifiers:
  Wallet concentration >50%: ×0.90 confidence | <25%: ×1.05
  Rising tx count + rising unique wallets: ×1.08 (genuine demand)
  Rising tx count + static wallets: ×0.85 (wash trading risk)
  Falling tx count: ×0.92 (disengagement)
  Bridge volume growing: ×1.05 | Pre-match $AFC bridge spike: PATH_2 flag
  Smart contract upgrade window: ×0.95 | Post-completion: ×1.05
  Emergency contract pause: ×0.75 ALL affected tokens — HOLD triggered
  LTH ratio >60%: ×1.05 confidence | <30%: ×0.92
```

### DOMAIN 7 — Agent Reasoning Architecture (`core/`)

```
Coverage:          80 markdown files in core/ (includes injury-intelligence/ 8 files)
Anchor files:
  core/agent-onboarding.md          Entry point — loading order + common mistakes
  core/agent-reasoning-chains.md    5 complete chains (absence/regulatory/PATH2/demand/weather)
  core/signal-confidence-framework.md HOLD triggers + layer conflict hierarchy
  core/fan-token-context-bridge.md   Every layer → fan token signal connection

HOLD trigger conditions (automatic — check before any output):
  1. macro_override_active = true
  2. Three or more key absences unconfirmed
  3. PATH_2 with lineup unconfirmed ($AFC only)
  4. Adjusted score between 48-52 (coin flip)
  5. Compound weather modifier below ×0.75
  6. Emergency contract pause active

Confidence timing: T-72h LOW | T-48h LOW-MEDIUM | T-24h MEDIUM | T-2h HIGH

Required output fields: direction · adjusted_score · sms · recommended_action ·
  composite_modifier · modifiers_applied · flags · confidence_level ·
  signal_class · layers_loaded
```

---

## CALIBRATION BASE

```
Total records:     129 verified pre-event submissions (130 data files; 1 is a report)
Direction accuracy: 96%
Sports covered:    21

Records by sport:
  football:     33  formula1:  10  mma:      11  cricket:   13
  basketball:   15  tennis:     8  ice-hockey: 8 rugby-union: 7
  rugby-league:  6  rowing:     3  netball:    3  athletics:  2
  swimming:      2  winter-sports: 2  handball: 1  kabaddi:  1
  darts:         1  snooker:    1  motogp:     1  nascar:    1

FTP PATH_2 calibration (April 2026 — Model 2 verified):
  UCL 07/04/2026: Sporting CP vs Arsenal → WIN — 159,025 $AFC BURNED ✓
  PL  11/04/2026: Arsenal vs Bournemouth → LOSS — 100,000 $AFC MINTED ✗
  UCL 15/04/2026: Arsenal vs Sporting CP → DRAW — 0 burned / 0 minted ✗
  Net April: 59,025 $AFC net reduction (159,025 burned − 100,000 minted)
  Multiplier calibration: ×1.59 actual | ×1.50 central estimate | ×1.40–2.0 range

PENDING calibration record:
  UCL Final 30 May 2026 — PSG vs Arsenal — Budapest
  Pre-match signal: examples/calibration/ucl-final-2026-psg-arsenal-signal.md
  STATUS: PENDING OUTCOME
  If Arsenal WIN: largest single $AFC PATH_2 burn in history (~250-500k)
  Collect: chiliscan.com T-12h to T-2h pre-liquidation data + post-match burn/mint
  Action: submit calibration record after match; update direction accuracy count
```

---

## ACTIVE MONITORING FLAGS

```
FLAG 1 — fan-token/registry/complete-registry.md MISSING
  official-verification-framework.md references this file for positive match lookups.
  bridge-supported.md exists; complete-registry.md does not.
  Agents cannot complete Step 1 of the verification workflow without this file.
  Status: OPEN — HIGH PRIORITY
  Action: build complete-registry.md listing all confirmed official Fan Tokens™
          with contract addresses, chain status, verification sources

FLAG 2 — i18n layer STATUS UNKNOWN
  20 files across Arabic, French, Spanish, German, Hindi, Japanese, Portuguese.
  Last updated: pre-v3.97.20 (unknown exact version).
  May contain stale modifier values (pre-v3.97.35 psychological and coaching modifiers).
  Status: OPEN — MEDIUM PRIORITY
  Action: systematic review and update OR add explicit deprecation notice to i18n/

FLAG 3 — CLARITY Act final status pending
  Current: DRAFT_RELEASED + LEGISLATIVE_MARKUP_IN_PROGRESS
  Section 404 (Activity-based vs passive yield): DRAFT_STABLE
  Committee markup was scheduled May 14, 2026.
  Update macro/macro-regulatory-sportfi.md when enacted status confirmed.
  Status: MONITORING

FLAG 4 — UCL Final calibration record pending
  Match: PSG vs Arsenal, May 30, Budapest, Puskás Aréna
  Pre-match signal published: examples/calibration/ucl-final-2026-psg-arsenal-signal.md
  Calibration record: collect post-match; submit to calibration base
  $AFC PATH_2 data to collect: T-12h to T-2h on chiliscan.com + post-match supply event
  Status: MONITORING — awaiting outcome

FLAG 5 — Fan token registry research: INITIATED (National Teams priority)
  Research task: compile complete-registry.md from Socios official sources
  Sources: socios.com/club-list + chiliscan.com/tokens + fantokens.com
  Scope: all current and historical official Fan Tokens™ with verified contract addresses
  Priority starting point: national team tokens (highest fraud risk during WC 2026)
  Confirmed so far: $ARG · $POR · $SNFT · $BFT (see official-verification-framework.md)
  Status: RESEARCH_INITIATED — linked to FLAG 1
```

---

## KEY MODIFIER QUICK REFERENCE

```
SPORT DOMAIN:
  New manager 1-5 matches: ×1.06 | 6-15: ×1.02 | caretaker: ×1.02
  Manager stability 2yr: ×1.03 | 4yr: ×1.05 | instability (3+ in 2yr): ×0.94
  Win streak 3: ×1.03 | 5: ×1.06 | 7+: ×1.08 ceiling
  Loss streak 3: ×0.96 | 5: ×0.93 | 7+: ×0.90 floor
  Derby: home advantage ×1.10 | form ×0.80 discount
  Historical pattern min sample: <5 skip | 5-9 ×0.50 weight | 10+ full
  Choking pattern: ×0.92 | Clutch: ×1.08 (both require min 5 situations)
  Cup team overperformance: ×1.06 | Final anxiety: ×0.94

ATHLETE:
  GK absent: ×0.90 | Primary striker: ×0.93 | Left CB (Arsenal): ×0.94
  Right-footed replacement at left CB: ×0.97 positional fit discount
  Star player absent (high-profile): −10-15% demand | standard: −5-10%
  New signing arrival: +15-25% demand (2-4 weeks)

FAN TOKEN / DEMAND:
  Summer window: ×1.20 | Dead period: ×0.85 | Winter window: ×1.10
  Title race: ×1.15 | Relegation battle: ×0.88
  Bull market: ×1.15 | Bear: ×0.85 | Alt season: ×1.20
  CHZ virtuous cycle: ×1.12 | Breakdown: ×0.93
  SWF ownership: ×1.05 | New Tier A club to ecosystem: ×1.05
  Tier 1 exchange listing: +20-40% spike | +15-25% new baseline
  CHZ major exchange delisting: ×0.82 ALL tokens

FINANCIAL:
  FFP investigation: ×0.94 | FFP breach: ×0.88
  PE acquisition phase 1: ×0.95 | phase 2 (growth): ×1.10
  Relegated club demand: −25-40% month 1 | settled 60-70%
  Post-trophy hangover: ×0.96 (within 7 days) | Near-miss motivation: ×1.05

FRAUD RISK:
  Passive yield promise: Tier 1 red flag + CLARITY Section 404 violation signal
  No chiliscan.com contract: Tier 1 red flag — NOT AN OFFICIAL FAN TOKEN™
  Event-timed launch (no prior announcement): Tier 1 red flag
  Two or more Tier 2 flags: UNVERIFIED classification required
```

---

## KNOWN LIBRARY GAPS — PRIORITY ORDER

```
PRIORITY 1 — STRUCTURAL (fix immediately):
  1. fan-token/registry/complete-registry.md — MISSING
     Referenced by official-verification-framework.md (v3.97.44).
     Fraud risk layer has broken positive-match reference.
     Build: full registry of confirmed official Fan Tokens™ with
     contract addresses, chain status (native/bridge), verification sources

  2. core/smi-digest.md — NOW CURRENT (v3.97.44)

  3. Thin sport domain files with active token/calibration data:
     rugby-league (183L), netball (175L), rowing (178L)

PRIORITY 2 — COMMERCIAL IMPORTANCE:
  4. Basketball: no NBA or EuroLeague competition-specific file
  5. Tennis: no ATP/WTA circuit or Grand Slam surface differentiation
  6. Cricket: no IPL/BBL/CPL file (highest future fan token potential)
  7. NFL/American football: no playoff/draft/bye-week intelligence
     (CLARITY Act opens US market — elevated priority)
  8. Esports: Valorant missing (VIT active); LoL missing; mobile esports absent
  9. Women's sport: women's cricket, WNBA, WTA, women's rugby all absent

PRIORITY 3 — INTELLIGENCE LAYERS ABSENT ENTIRELY:
  10. Betting odds as signal input — no framework for line moves, sharp money
      (significant gap for complete Mind for Sports)
  11. Injury classification index — enduring type → timeline → modifier reference
  12. Competition-specific referee pool intelligence
  13. Venue-specific microclimate weather patterns
  14. Anti-doping / drug testing intelligence (positive tests, CAS timelines)
  15. Player agent/representative intelligence (agent activity as transfer signal)
  16. Press conference and manager media intelligence

PRIORITY 4 — COMPLETENESS:
  17. i18n layer (20 files) — likely stale, update or deprecate
  18. India: regulatory position not modelled (large fanbase, zero coverage)
  19. Latin America: Brazil partial; Argentina, Colombia, Mexico absent
  20. Club-specific depth uneven ($BAR, $CITY, $PSG, $JUV, $ACM)
  21. examples/ — some files may contain stale modifier values
```

---

## SOURCES — VERIFIED TIER 1

```
fantokens.com/fan-token-play     FTP PATH_2 official data
fantokens.com                    Fan token registry, supply data
chiliscan.com                    On-chain verification (Chiliz Chain explorer)
socios.com                       Official fan token platform and club listings
legislation.gov.uk               UK SI 2026/102
banking.senate.gov               CLARITY Act — US Senate Banking Committee
fatf-gafi.org                    FATF grey list (Kuwait February 2026)
oifc.gov.om                      Oman OIFC Royal Decree 8/2026
chiliz.com                       Ecosystem announcements + FTP mechanics
vara.ae                          UAE VARA regulatory publications
pif.gov.sa                       Saudi PIF investment decisions
spl.com.sa                       Saudi Pro League official
```

---

## UPDATE INSTRUCTIONS

```
Update after every versioned release:
  · Last updated: version and date (line 8)
  · Library state counts (line 9)
  · Domain coverage counts if files added
  · Known gaps: remove filled, add newly identified
  · Active monitoring flags: add/close/update
  · Calibration base count (check community/calibration-data/)
  · Regulatory status changes (check macro/macro-regulatory-sportfi.md)
  · FTP PATH_2 status (check fan-token/ftp-path2.md)
  · Modifier quick reference if values changed
  · Active HOLD triggers if any new conditions

FIELD PRIORITIES (always keep accurate):
  Calibration count:    community/calibration-data/ — count data files
  Regulatory status:    macro/macro-regulatory-sportfi.md
  FTP PATH_2 tokens:    fan-token/ftp-path2.md
  Active flags:         this file — monitoring flags section
  Gap priority order:   reassess quarterly
```

---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*SMI Digest — agent reference state summary · load this file first*
