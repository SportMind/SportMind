# Saudi Pro League — SportMind Sport Domain Intelligence

**Supplementary domain file. Load alongside `sports/football/sport-domain-football.md`
for Saudi Pro League specific signal intelligence.**

---

## Overview

```
LEAGUE:           Saudi Pro League (SPL)
COUNTRY:          Kingdom of Saudi Arabia
CLUBS:            18 (2025-26 season)
PRIMARY OWNERS:   Public Investment Fund (PIF) — directly owns Al Nassr,
                  Al Hilal, Al Ittihad, Al Ahli (the "PIF Four")
                  Remaining clubs: privately owned
SEASON FORMAT:    August to May (overlaps with European season)
COMMERCIAL TIER:  Emerging Tier 1 — PIF investment elevating rapidly
                  Legacy tier: Regional Tier 2 (pre-2023)
FAN TOKEN STATUS: No confirmed active fan tokens as of v3.97.8
                  Near-term probability: HIGH (PIF clubs most likely first movers)
CHILIZ PIPELINE:  Monitor — Tier B (Fan Token Adjacent)
```

---

## Domain Model

### Season Rhythm

```
SPL SEASON CALENDAR (distinct from European rhythm):

  Phase               Months    Token/Signal Behaviour
  ───────────────────────────────────────────────────────────
  Pre-season          Jul–Aug   Transfer window peak — signal dominated by
                                summer signings; fan anticipation driven by
                                European star acquisitions
  Early season        Aug–Oct   High engagement post-transfer; new signings
                                making debut; attendance and social peaks
  Winter window       Jan–Feb   Second transfer window — secondary signal spike
  Title run-in        Mar–May   Domestic title race dominates; Ramadan window
                                creates fixture compression and form volatility
  Summer window       Jun–Aug   HIGHEST SPL signal period — summer transfers from
                                Europe dominate global sports media

  AGENT NOTE: The summer transfer window (June–August) is THE primary SPL signal
  event. European player acquisitions create larger global media events than SPL
  match results for fan token purposes. A signing announcement from a PIF club
  outperforms most match-day signals in media reach.
```

### Match Importance Scoring

```
SPL MATCH IMPORTANCE (MIS) — ADJUSTED SCALE:

  PIF Derby (Al Hilal vs Al Nassr):      MIS 9.5 — highest domestic fixture
  Al Ittihad vs Al Hilal:                MIS 8.5
  Al Ahli vs Al Nassr:                   MIS 8.0
  PIF club vs major private club:        MIS 7.0
  Standard SPL fixture:                  MIS 5.0

  NOTE: SPL MIS is compressed vs European Tier 1. A standard SPL fixture
  is equivalent to a mid-table PL fixture in fan token signal terms.
  PIF derby matches approach EPL top-6 fixture weight.
```

---

## Signal Variables — Saudi Pro League Specific

```
PRIMARY SIGNAL VARIABLES:

1. SUMMER TRANSFER WINDOW ACTIVITY (highest weight — 35%)
   Weight: 35% of SPL pre-season signal
   
   Star acquisition announcement:
     European Tier 1 player (Ballon d'Or calibre): CDI amplification ×2.0–3.0
     European Tier 1 player (top-20 world): CDI amplification ×1.5–2.0
     European Tier 2 player: CDI amplification ×1.2–1.5
     
   Signal timing:
     Rumour (Tier 3 source):    Low confidence — do not act
     Negotiation confirmed:     Tier 2 — monitor
     Club official announcement: Tier 1 — execute
     
   Why this is SPL's dominant signal:
     Global media coverage of SPL signings far exceeds match coverage.
     Fan token holders respond to star power narratives, not domestic results.
     A Neymar, Benzema, or Ronaldo signing creates multi-week CDI elevation.

2. HIGH-PROFILE PLAYER PERFORMANCE (25%)
   Performance modifier for named high-profile players only.
   SPL domestic records (goals, assists) have limited global signal weight.
   Performance that generates European media pickup = signal.
   Performance seen only on regional broadcast = low signal.

3. MATCH RESULT — PIF DERBY (20%)
   Only PIF derby matches generate signal equivalent to European mid-tier fixtures.
   Standard SPL results: low global media reach; limited fan token signal.

4. CLUB FINANCIAL NEWS / PIF ANNOUNCEMENTS (12%)
   PIF investment decisions, stadium projects, sponsorship deals.
   Vision 2030 milestone announcements.
   Any signal that positions SPL clubs as global commercial entities.

5. INTERNATIONAL TOURNAMENT PERFORMANCE — Saudi NT (8%)
   Saudi Arabia national team reaching knockout stages.
   WC2026: Saudi Arabia in Group C (vs Argentina/Mexico/Poland cluster).
   Saudi NT token (if launched): NCSI ×2.5 for WC knockout stage progression.
```

---

## Risk Variables

```
RISK VARIABLE 1 — EXTREME HEAT (HIGHEST OPERATIONAL RISK)

  Context: Riyadh summer temperatures regularly exceed 45°C (113°F).
  SPL summer matches (August kick-off): played 21:00+ local time to reduce heat.
  
  Signal implications:
    Physical load: European players unaccustomed to heat show performance decline
    in weeks 1–8 of the season (acclimatisation period).
    Injury rates for European signings: elevated in first full season.
    Late kick-off times: reduce live viewership in European time zones.
    
  Modifier: Apply heat_risk_modifier = 0.90 for European signings in Aug–Sep.
  After full acclimatisation (10+ matches): return to baseline modifier.
  
  Extreme heat match conditions:
    If match played in temperatures >40°C: apply fatigue_modifier = 0.92 to
    second-half performance; particularly relevant for older signings (30+).

RISK VARIABLE 2 — RAMADAN FIXTURE SCHEDULING

  Context: Ramadan falls in different months each year (lunar calendar).
  Players observing Ramadan fast during daylight hours (including training).
  SPL has significant proportion of practising Muslim players.
  
  Signal implications:
    Performance variance for fasting players: typically 5–15% output reduction
    in matches played near Iftar (breaking of fast at sunset).
    Late Ramadan matches (night kick-offs, post-Iftar): performance normalises.
    European non-Muslim signings: unaffected physically; affected by team cohesion.
    
  Modifier: ramadan_modifier applies only to practising Muslim players.
  Default: ramadan_modifier = 0.92 (daytime training and pre-Iftar matches)
  Night matches (post-Iftar): ramadan_modifier = 1.00 (no impact)
  
  AGENT RULE: Check match kick-off time relative to Iftar before applying.
  Iftar time varies by date and city — check for accurate application.

RISK VARIABLE 3 — TRAVEL FATIGUE FOR EUROPEAN SIGNINGS

  Context: Most SPL players travel to Europe during international breaks.
  Round trip London/Madrid to Riyadh: ~6,500km, 6–8h flight.
  International break travel + acclimatisation = 7–10 day performance dip.
  
  Modifier: post_international_break_modifier = 0.92 for European-born players.
  Applies to first 2 SPL matches after international break.
  
  High-risk players: those with international duty (Ronaldo — Portugal,
  Benzema — retired France, Neymar — Brazil if fit).
  
RISK VARIABLE 4 — BROADCAST REACH LIMITATION

  Context: SPL broadcast deals heavily weighted toward MENA region.
  Global broadcast reach significantly below EPL, La Liga, Bundesliga.
  Match results generate limited signal in European fan bases.
  
  Signal implication: SPL match outcomes have reduced CDI impact vs European
  equivalents. Apply broadcast_reach_modifier = 0.75 to SPL match result signals
  (vs European Tier 1 equivalents at 1.00).
  Exception: PIF derby — broadcast_reach_modifier = 0.90 (global media pickup).
```

---

## Event Playbooks

### Playbook 1 — SPL Star Signing Announcement

```
TRIGGER: PIF club confirms signing of European Tier 1 or Tier 2 player.
FILTER:  Tier 1 source only. SPL rumours have high false-positive rate.
ENTRY:   On Tier 1 official announcement confirmation.
EXIT:    T+72h post-announcement (peak decay); or debut match completion.
SIZING:  Full signal weight on Ballon d'Or calibre; scale down for Tier 2.

PRE-ANNOUNCEMENT (rumour phase):
  Signal weight: LOW — do not act on unverified transfer rumours.
  Monitor Tier 2 sources only. Flag for T-1h preparation.

ANNOUNCEMENT (Tier 1 confirmed):
  CDI spike: immediate. Duration 48–72h peak.
  Token signal: associated club fan token (when live) or nearest proxy.
  Apply: star_signing_modifier × tier_weight
    Ballon d'Or calibre: ×2.5
    Top-20 European player: ×1.75
    Top-50 European player: ×1.35
  
POST-SIGNING (debut match):
  CDI elevation: moderate (debut anticipation 24–48h pre-match).
  Debut match: apply debut_modifier = 1.20 to match importance score.
  Post-debut decay: 7–10 days return to baseline (unless debut performance elite).
```

### Playbook 2 — PIF Derby Match

```
TRIGGER: Al Hilal vs Al Nassr (or other PIF club derby fixture).
FILTER:  Confirm Ronaldo and Neymar availability before signal generation.
ENTRY:   T-48h with confirmed key player availability.
EXIT:    T+24h post-match (result sentiment decay).
SIZING:  MIS 9.0–9.5 applied; broadcast_reach_modifier = 0.90.

PRE-MATCH (T-48h):
  Check: High-profile player availability (Ronaldo, Neymar availability is
  the dominant variable — confirm fitness before signal generation).
  Signal: Elevated vs standard SPL fixture. Apply MIS 9.0–9.5.
  Social volume: global spike expected from Ronaldo/Neymar fan bases.

MATCH DAY:
  Apply standard football signal chain with SPL-adjusted weights.
  Broadcast reach: 0.90 (global pickup for PIF derbies).

POST-MATCH:
  High-profile player performance narrative dominates signal.
  Ronaldo goal → global media loop → extended CDI elevation (12–24h).
  Result secondary to narrative for global fan base.
```

### Playbook 3 — Ramadan Window Compression

```
TRIGGER: Multiple SPL fixtures scheduled in Ramadan period.
FILTER:  Check match kick-off time relative to Iftar before applying.
ENTRY:   Standard match entry; modified by Ramadan context.
EXIT:    Standard match exit.
SIZING:  Reduced for daytime/pre-Iftar matches; standard for night matches.

PRE-TOURNAMENT CHECK:
  Identify matches: daytime training + pre-Iftar kick-offs vs night matches.
  Apply ramadan_modifier to Muslim player contingent per team.
  
SIGNAL ADJUSTMENT:
  Pre-Iftar matches: reduce expected performance output for domestic players.
  Night matches (post-Iftar): standard modifiers apply.
  
NOTE: European signings (Ronaldo, Benzema, Neymar era) are unaffected
physiologically but team cohesion disruption applies to mixed squads.
```

---

## Fan Token Clubs — Saudi Pro League

```
FAN TOKEN STATUS (as of v3.97.8):
  No confirmed active SPL fan tokens on Chiliz Chain or FanToken.com.

HIGH PROBABILITY FIRST MOVERS (PIF Four — all state-owned, PIF control):

  AL HILAL:
    Commercial scale: largest club in MENA by revenue and titles
    Global following: 10M+ social media (Arabic + international)
    FT probability: HIGHEST — PIF commercial mandate + Neymar era global reach
    Likely token: $HILAL or $ALH
    Signal window: any official announcement triggers immediate CDI event

  AL NASSR:
    Commercial scale: elevated globally due to Ronaldo signing (2023)
    Global following: 15M+ post-Ronaldo (largest SPL following internationally)
    FT probability: VERY HIGH — Ronaldo era transformed global brand
    Likely token: $NASSR or $ANS
    Signal window: strongest FT launch signal if Ronaldo still active at launch

  AL ITTIHAD:
    Commercial scale: historically strongest Saudi domestic brand
    Global following: 8M+ social media
    FT probability: HIGH — PIF ownership + Benzema era momentum
    Likely token: $ITTIHAD or $ALI

  AL AHLI:
    Commercial scale: growing rapidly post-PIF acquisition
    Global following: 5M+ social media
    FT probability: MEDIUM-HIGH — PIF playbook applied systematically

AGENT RULE:
  When any PIF club announces a fan token (Tier 1 source required):
    1. Reclassify SPL from Tier B → Tier A (sport-tiers.md update required)
    2. Run Phase 1 CDI baseline protocol within 72h
    3. Apply ×1.40 first-mover CDI launch modifier (US-equivalent first-mover)
    4. Load fan-token/fan-token-lifecycle/ Phase 1 immediately
```

---

## Agent Reasoning Prompts

```
WHEN ANALYZING AN SPL MATCH OR TOKEN EVENT:

1. "Is this signal driven by a star player narrative or a match result?"
   SPL signals are predominantly narrative-driven (signing, debut, milestone).
   Match results carry 30–40% of the signal weight of equivalent European fixtures.

2. "Is the high-profile player (Ronaldo/Neymar/Benzema) confirmed available?"
   SPL star availability is the single highest-weight variable.
   Ronaldo availability: treat as ATM modifier ×1.25–1.50 for Al Nassr signals.
   Neymar availability: historically unreliable — apply strict Tier 1 confirmation.

3. "What is the thermal and scheduling context?"
   August–September: apply heat_modifier = 0.90 to European signings.
   Ramadan window: check kick-off vs Iftar time before applying modifiers.
   International break aftermath: apply travel_modifier = 0.92 for 2 matches.

4. "Is this a PIF club or a privately-owned club?"
   PIF clubs: higher commercial ceiling, faster token probability, global brand.
   Private clubs: regional focus, lower global signal weight.

5. "What is the broadcast reach for this match?"
   Standard SPL: broadcast_reach_modifier = 0.75 vs European Tier 1.
   PIF derby: broadcast_reach_modifier = 0.90.
   Never apply 1.00 to an SPL fixture (EPL/UCL reserved tier).
```

---

## Calibration Notes

```
HOW SPL DIFFERS FROM EUROPEAN LEAGUES FOR SIGNAL WEIGHTING:

  EUROPEAN TIER 1 (EPL, La Liga, Bundesliga, Serie A, Ligue 1):
    Match result dominates signal: 60–70% of CDI weight
    Star player contribution: 20–30%
    Transfer/commercial news: 10–20%

  SPL (current calibration — pre-fan-token):
    Transfer/star signing: 35% of CDI weight (primary signal)
    Match result: 20% (below European equivalent)
    Star player availability: 25% (Ronaldo/Neymar factor outsized)
    Commercial/PIF news: 12%
    Broadcast-limited reach: reduces all weights by 0.75 vs European

  CALIBRATION RECORDS STATUS:
    SPL calibration records: ZERO (as of v3.97.8)
    PRIORITY: Submit SPL records before any European expansion
    Starting point: PIF derby match outcomes + transfer announcement CDI spikes
    Target: 10 records before any SPL modifier values are treated as confirmed

  KNOWN CALIBRATION UNCERTAINTIES:
    No fan token exists for SPL clubs → CDI/FTP signal is theoretical
    All SPL modifiers are constructed from first principles and analogy
    Once a SPL fan token launches: treat first 30 days as Phase 1 calibration
    Do not apply European fan token historical modifiers to SPL until 20+ records
```

---

## Data Sources

```
PRIMARY SOURCES:
  Arab News Sport (arabnews.com/sport)       — SPL fixtures, results, signings
  Saudi Pro League official (spl.com.sa)     — Official standings, schedules
  Goal.com MENA edition                      — Transfer coverage, squad news
  PIF official (pif.gov.sa)                  — Investment decisions, announcements
  Transfermarkt (spl section)                — Valuations, contract data

SECONDARY SOURCES:
  Soccerway (soccerway.com)                  — Results, statistics
  BBC Sport (when SPL reaches international coverage)
  UEFA / FIFA for international fixture context

SOCIAL MONITORING:
  Twitter/X: @AlNassrFC_EN, @alhilal_EN, @AlIttihad, @AlAhliSC
  YouTube: SPL official channels (highlights, press conferences)
  Instagram: Ronaldo @cristiano (Nassr content signals broader audience reach)

AGENT NOTE: SPL media coverage is heavily Arabic-language.
English-language sources are secondary. For transfer intelligence,
supplement with Spanish (Marca, AS) and English (The Athletic, Fabrizio Romano)
for European player perspective.
```

---

### Playbook 4 — Fan Token Launch Event (SPL)

```
TRIGGER: PIF club officially announces fan token launch on Chiliz/FanToken.com
FILTER:  Tier 1 source required (official club + Chiliz press release).
ENTRY:   On announcement confirmation — reclassify SPL to Tier A immediately.
EXIT:    T+30 days (Phase 1 CDI decay to baseline).
SIZING:  Apply ×1.40 first-mover modifier; maximum Phase 1 CDI engagement.

PRE-LAUNCH (announcement to TGE):
  Load: fan-token/fan-token-lifecycle/ Phase 1 protocol immediately.
  Signal: highest CDI window for any SPL fan token event.
  Apply: US first-mover ×1.40 equivalent (largest unserved GCC market).

TGE (Token Generation Event):
  CDI peak: 24–48h around TGE.
  Monitor: on-chain holder count growth (chiliscan.com).
  Benchmark: first 72h holder count vs Phase 1 projections.

POST-LAUNCH (first 30 days):
  Match performance begins contributing to CDI signal.
  Apply: debut_modifier = 1.20 to first home match post-TGE.
  Calibration records: collect immediately — priority for library.
```

---

## Signal Weight Adjustments

For Saudi Pro League, apply these weight adjustments (vs standard football):

| Component | SPL Weight | Standard Football | Rationale |
|---|---|---|---|
| Transfer/signing news | 35% | 15% | SPL defined by star acquisitions |
| Star player availability | 25% | 15% | Ronaldo/Neymar factor outsized |
| Match result | 20% | 35% | Broadcast reach limited globally |
| PIF/commercial news | 12% | 5% | Sovereign ownership adds signal type |
| Macro | 8% | 10% | Standard weight |

*Apply broadcast_reach_modifier = 0.75 to all SPL result signals (0.90 for PIF derbies).*

---

## Key Commands

```
get_spl_star_availability(club)
  → Returns availability and ATM modifier for high-profile players
  → Priority: Ronaldo (Al Nassr), Neymar (Al Hilal), Benzema (Al Ittihad)

get_spl_transfer_signal(club, player_tier)
  → Calculates CDI impact of confirmed signing
  → tier: "ballon_dor" | "top_20" | "top_50"

get_spl_match_signal(home_club, away_club, match_type)
  → Returns adjusted match signal with SPL broadcast modifier
  → match_type: "pif_derby" | "pif_vs_private" | "standard"

get_heat_modifier(month, player_origin)
  → Returns heat and acclimatisation modifier
  → month: 1–12 | player_origin: "european" | "south_american" | "saudi"
  
get_ramadan_modifier(kickoff_time, player_religion)
  → Returns Ramadan performance modifier
  → kickoff_time: local time | player_religion: "muslim" | "non_muslim"
```

---

## Compatibility

**Extends:** `sports/football/sport-domain-football.md`
**Market:**  `market/market-saudi-pro-league.md`
**Athlete:** `athlete/football/athlete-intel-saudi-pro-league.md`
**Tiers:**   `core/sport-tiers.md` — Tier B (Fan Token Adjacent)


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Saudi Pro League-specific signal intelligence: mega-signing impact, development trajectory |
| Reasoning | ACTIVE | SPL reasoning chain from squad composition and commercial context to outcome prediction |
| Context | ACTIVE | SPL context: mega-signing motivation signals, league development phase, Asian Champions League |
| Memory | ACTIVE | Historical SPL outcome patterns and mega-signing performance data |
| Judgment | ACTIVE | Judgment on SPL signal uniqueness — motivation of elite players is a primary signal |
| Attention | ACTIVE | Elevated attention for player motivation signals and club commercial announcements |
| Communication | ACTIVE | SPL signal output with motivation modifier, squad context, and direction |
| Verification | ACTIVE | SPL data from Saudi Pro League official sources |
| Learning | ACTIVE | SPL modifier calibration from historical mega-signing performance data |
| Integration | ACTIVE | Integrates with sport-domain-football.md, CDI framework, and KSA regulatory intelligence |
| Calibration | ACTIVE | SPL motivation modifiers calibrated against historical player performance data |
| Adaptation | ACTIVE | SPL intelligence adapts as league development phase and player acquisition evolve |
| Ethics | NOT APPLICABLE | SPL sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Player motivation context, source, and modifier basis explicit in output |


---

*SportMind v3.97.8 · MIT License · sportmind.dev*
*Saudi Pro League intelligence — Layer 1 Sport Domain*
*Calibration records: 0 — PRIORITY collection required*
