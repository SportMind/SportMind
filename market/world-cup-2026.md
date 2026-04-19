# World Cup 2026 — SportMind Module

**FIFA World Cup 2026 · USA / Canada / Mexico · June–July 2026**

The single largest commercial event in fan token history. The first 48-team World Cup.
Hosted across 16 cities in three countries. This module consolidates all World Cup 2026
intelligence from across the SportMind library for agent and developer use.

---

## Tournament overview

```
FORMAT (48-team — first time):
  Phase 1: 12 groups of 4 (top 2 + 8 best third-place = 32 advance)
  Phase 2: Round of 32 → 16 → 8 → 4 → Final
  Total matches: 104 (up from 64 in Qatar 2022)
  
DURATION: ~39 days (June 11 – July 19, 2026)

HOST CITIES AND VENUES (16 cities):
  USA (11): New York/NJ (MetLife), Los Angeles (SoFi), Dallas (AT&T), San Francisco
            (Levi's), Miami (Hard Rock), Seattle (Lumen Field), Boston (Gillette),
            Houston (NRG), Kansas City (Arrowhead), Philadelphia (Lincoln Financial),
            Atlanta (Mercedes-Benz)
  Canada (2): Toronto (BMO Field), Vancouver (BC Place)
  Mexico (3): Mexico City (Estadio Azteca), Guadalajara (Estadio Akron),
              Monterrey (Estadio BBVA)

FINAL: MetLife Stadium, East Rutherford, New Jersey
```

---

## Why this World Cup is different for fan tokens

```
THE 48-TEAM EXPANSION:
  More nations = more fan bases engaged = more token markets activated
  First time: Caribbean, CONCACAF nations have genuine token potential
  Expected: Several new national token launches in 2025–2026 lead-up
  
THE US MARKET UNLOCK:
  World Cup in USA is the primary catalyst for US fan token adoption
  75M+ Latino fans in US who follow football closely
  US regulatory environment (SEC/CFTC clarity) determines whether
  US-based fan token products can fully launch around this tournament
  
  CRITICAL MONITORING:
  If US crypto/utility token regulation clarifies before June 2026:
  → World Cup 2026 becomes the largest single fan token commercial event ever
  If it doesn't: Strong performance still expected but US market limited
  
  See: market/market-american-football.md for US regulatory tracking context
  See: market/market-key-findings.md (Finding 3 — US regulatory gating variable)

THE COMMERCIAL SCALE:
  2022 Qatar World Cup: 5 billion total viewers across tournament
  2026 USA expected viewership: 6–7 billion (USA/Canada primetime + larger format)
  $14B+ in broadcast rights globally
  FIFA commercial revenue target: $11B+ (up from $7.5B in Qatar)
```

---

## National-club token spillover (NCSI) — World Cup edition

```
NCSI AT WORLD CUPS IS THE DOMINANT TOKEN SIGNAL:
  A player's performance for their national team in a World Cup generates
  spillover into their club token price. This effect is 3–4× stronger at
  World Cups than at friendlies or qualifiers.

HIGHEST NCSI IMPACT PLAYERS AND THEIR CLUBS (estimated for 2026):
  
  Kylian Mbappé (France → Real Madrid):
    Real Madrid has $RMFC token
    Mbappé World Cup performance directly impacts $RMFC
    ATM: 0.35–0.42 (highest expected individual ATM in the tournament)
    If Mbappé wins Golden Boot: Expected $RMFC impact +18–25%
    
  Erling Haaland (Norway → Manchester City):
    Norway qualified → $CITY token World Cup NCSI active
    ATM: 0.28 (highest at City)
    Norway early exit: Limited $CITY impact (Haaland returns quickly)
    Norway deep run: Extended narrative; positive NCSI effect
    
  Vinicius Jr (Brazil → Real Madrid):
    Brazil's commercial importance + Real Madrid token = dual impact
    Brazil is highest-engagement single-nation audience globally (200M+ fans)
    $RMFC gets Brazil NCSI AND Vinicius individual ATM
    
  Jude Bellingham (England → Real Madrid):
    England is highest-engagement European nation at World Cups
    England deep run: $RMFC $MUFC and English player tokens all benefit
    England early exit: Immediate negative NCSI for English club tokens
    
  Lamine Yamal (Spain → FC Barcelona):
    Expected to be the tournament's breakthrough star (born 2007)
    $BAR token NCSI: Could be the single largest individual contributor
    Spain tournament performance: Multiple catalysts if they advance far

NATIONAL TOKEN OPPORTUNITIES:
  Tokens that may launch or see peak activity around WC2026:
  → Brazil national token (if launched): Peak commercial window
  → Mexico national token: Host nation; CONCACAF passion; US Latino market
  → USA national token: Home tournament; regulatory clarity dependent
  → Argentina ($ARG): Defending champions; Messi legacy continuation
  → England: Most commercially active European fan token market outside London
```

---

## Competition tier model for World Cup 2026

```
WORLD CUP SPECIFIC TIER WEIGHTS (override standard competition model):

TIER 1 — Maximum signal:
  World Cup Final: importance_score = 1.00 (maximum in all of football)
  World Cup Semi-Finals: 0.92
  World Cup Quarter-Finals: 0.85
  
TIER 2 — Very high signal:
  World Cup Round of 16: 0.72
  World Cup Group Stage (match 3 — deciders): 0.60
  
TIER 3 — Elevated but conditional:
  World Cup Group Stage (match 1–2): 0.45
  Applies standard NCSI calculation
  
SPECIAL MODIFIERS:
  Host nation match (USA/Canada/Mexico): × 1.15 additional on importance
  Rivalry match (Brazil vs Argentina, England vs Germany, etc.): × 1.20 additional
  Defending champion (Argentina) match: × 1.10 additional
  
BRACKET SIGNAL AMPLIFICATION:
  Each round a token-heavy nation advances, their club tokens receive cumulative lift.
  Brazil to semi-final: Four rounds of NCSI × multiplier
  Brazil eliminated in groups: Immediate −8–12% for Brazilian club tokens
```

---

## Pre-tournament signal protocol

The pre-tournament window (now through June 10) requires dedicated monitoring.
Load `fan-token/world-cup-2026-intelligence/world-cup-2026-pre-tournament.md`
alongside this file for the full countdown protocol — squad announcement
intelligence, national token activation sequence, NCSI awakening for club
tokens, and daily monitoring cycle.

---

## Signal calendar for agents

```
PRE-TOURNAMENT WINDOW (Jan–May 2026):
  Monitor: Squad announcements (April–May 2026)
  Signal: Star player inclusion/exclusion → immediate club token effect
  Monitor: Injury news for major ATM players (Mbappé, Haaland, Vinicius)
  Monitor: US regulatory framework announcements
  
  AGENT RULE: Begin World Cup monitoring from January 2026.
  Pre-tournament squad signals can move tokens months before the tournament.

GROUP STAGE (June 11–28, 2026):
  Highest-volume period: First week (all groups playing simultaneously)
  Key signal windows:
    Day 1-2: Opening matches (host nations + defending champions)
    Day 14-16: Group deciders (simultaneous 3rd matches)
  
  AGENT ACTION EACH MATCH DAY:
  1. Identify which Tier 1 token players are in action today
  2. Load their NCSI and ATM values from football-token-intelligence
  3. Apply competition tier importance score (Group Stage Match 1/2/3)
  4. Check DeFi liquidity before any position entry
  
KNOCKOUT STAGE (June 29 – July 19, 2026):
  Signal intensity increases with each round
  
  Round of 32: +40% above Group Stage base signal per round advancement
  Round of 16: +80% vs Group Stage
  Quarter-Finals: +120% vs Group Stage
  Semi-Finals: +160% vs Group Stage
  Final: Peak signal — apply maximum framework
```

---

## Commercial opportunities for developers building around WC2026

```
HIGHEST-VALUE PRODUCTS FOR WORLD CUP 2026:

1. NCSI DASHBOARD:
   Real-time tracker of national team results → club token impact
   Show: Which club tokens are moving and why based on today's match results
   Data: Chiliz explorer + ESPNcricinfo Football + club token prices
   Stack: fan-token-pulse + football-token-intelligence + confidence-output-schema
   
2. BRACKET TOKEN PORTFOLIO:
   Track a portfolio of tokens linked to advancing national teams
   Show: Projected token impact as bracket progresses
   Product: "Build your World Cup token bracket" — gamified commercial tool
   
3. WORLD CUP PREDICTION MARKET:
   Integration with Azuro/Polymarket for on-chain match outcome prediction
   Stack: sports/football + core/core-narrative-momentum + defi-liquidity-intelligence
   
4. NATIONAL TEAM TOKEN SCANNER:
   Identify which national teams are most likely to launch tokens pre-2026
   Stack: market/market-football + fan-token-lifecycle + fan-token-why
   Signal: Monitor Socios/Chiliz partnership announcements with national federations
   
5. ATHLETE COMMERCIAL BRIEF GENERATOR:
   For any World Cup player, generate a commercial brief based on tournament performance
   Stack: fan-token/brand-score + fan-token/athlete-social-activity + fan-token/sponsorship-match
   Trigger: After each match — update briefs with fresh performance data
```

---

## Loading instruction

```
For any World Cup 2026 analysis, load in addition to standard stack:
  1. This file (market/world-cup-2026.md) — tournament context
  2. fan-token/football-token-intelligence/ — NCSI, ATM, FTIS
  3. market/market-football.md — Tier 1 commercial context
  4. Appropriate national team context from macro files if relevant
  
MONITORING CHECKLIST (set up before tournament):
  □ Subscribe to: Chiliz/Socios partnership announcements
  □ Track: US regulatory framework developments (monthly check)
  □ Build: NCSI tracker for top 20 highest-ATM players
  □ Set: Alerts for squad announcements (April/May 2026)
  □ Prepare: DeFi liquidity baseline TVL for all active tokens
```

---

*This module consolidates World Cup 2026 intelligence across the SportMind library.
Individual skill files contain deeper sport-specific and commercial context.*

*Data correct as of Q1 2026. Tournament structure confirmed by FIFA.*



---

## Group stage intelligence framework

```
48-TEAM FORMAT — WHAT CHANGES FOR AGENTS:

The 2026 format introduces mechanics that do not exist in a 32-team World Cup.
Agents need to account for all of them.

12 GROUPS OF 4 — TOP 2 + 8 BEST THIRD-PLACE ADVANCE:
  The "best third-place" rule creates strategic complexity in Group Stage Match 3.
  A third-place team with 4 points (1 win, 1 draw) may qualify.
  This changes tactical motivation in final group matches significantly.

  AGENT RULE: In Match 3, check qualification scenarios for both teams.
  A team already through may rest key players (rotation signal × 0.88).
  A third-place team still competing for best-third-place spot = full effort.

GROUP STAGE MATCH SEQUENCE:
  Match 1 (Group Day 1): Highest uncertainty. No information asymmetry.
                         NCSI weight: 0.35 (lower — both teams fresh start)
  Match 2 (Group Day 2): One result known. Scenarios becoming clearer.
                         NCSI weight: 0.45
  Match 3 (Group Day 3 — SIMULTANEOUS): Maximum stakes information.
                         Qualification/elimination scenarios visible.
                         NCSI weight: 0.60 (decisive — see special modifiers below)

GROUP STAGE DECIDER MODIFIERS (Match 3):
  Both teams must win to guarantee qualification: × 1.20 on standard NCSI
  One team already qualified and other team must win: × 1.15 (asymmetric stakes)
  Both teams already qualified (result irrelevant): × 0.65 (rotation risk HIGH)
  One team eliminated regardless of result: × 0.70 (limited motivation signal)

GOAL DIFFERENCE BATTLES:
  New in 48-team format: goal difference matters for best-third-place spots.
  When a team is running up the score in Match 3: do not flag as anomaly.
  It is rational tournament strategy — teams target GD aggressively.
  For live-match agents: large score lines do not carry standard signal meaning.
```

---

## Host nation intelligence (USA, Canada, Mexico)

```
THREE HOST NATIONS — THREE DISTINCT PROFILES:

UNITED STATES:
  Population: 335M | Latino football fans: 75M+ | 11 venues
  Football context: MLS growing rapidly; USMNT regular FIFA top-20
  Commercial profile:
    Largest potential fan token market globally if US regulation permits
    Drive to Survive effect (DTS): World Cup hosting = DTS for American football fans
    Projected: US football fan base grows 25-35% during/after WC2026
    
  TOKEN SIGNAL:
    No USMNT token currently active on Chiliz
    When launched: hosts receive automatic × 1.30 home tournament bonus
    US Match days in major cities: local fan base engagement unprecedented
    
  HOST CITY PROFILES FOR AGENTS:
    New York/NJ MetLife: Final venue; highest-profile matches
    Los Angeles SoFi: Second-largest market; Latin American diaspora strong
    Dallas AT&T: Mexico diaspora in Texas = de facto Mexico home venue
    Miami Hard Rock: Caribbean + South American diaspora; Spanish-primary crowd
    
  USMNT SQUAD SIGNAL:
    USMNT reaching Round of 16: × 1.10 on all US market token signals
    USMNT reaching Quarter-Final: × 1.25 (unprecedented US football moment)
    USMNT Final: × 2.00 (would be the largest single US sporting event in history)

MEXICO:
  Population: 130M | Football fans: effectively 100M+
  3 venues: Mexico City (Azteca), Guadalajara, Monterrey
  Commercial profile:
    Co-host + most commercially mature Latin American football market
    Mexico City's Estadio Azteca: most historic World Cup venue
    US/Mexico border cities: fans crossing both directions
    
  TOKEN SIGNAL:
    Any Mexico token active: × 1.35 home tournament multiplier
    Mexico at home (Azteca or Guadalajara): crowd = 12th man signal
    Aplicar: rivalry_active flag for USA vs Mexico if they meet
    
  MEXICO SIGNAL CALENDAR:
    Mexican league season suspends around WC2026
    Club tokens (America, Chivas, Cruz Azul) follow NCSI for Mexican players
    Post-tournament: immediate return to Liga MX with WC2026 narrative fresh

CANADA:
  Population: 40M | Football fanbase: rapidly developing
  2 venues: Toronto BMO Field (30k), Vancouver BC Place (54k — dome)
  Commercial profile:
    2022 Qatar was Canada's first World Cup since 1986 — identity moment
    2026 is first time Canada hosts global football at this level
    Toronto: world's most multicultural city — every nation has representation
    Vancouver: Pacific Rim demographic — SE Asian football fans strong
    
  TOKEN SIGNAL:
    Canada NCSI: much smaller than USA/Mexico (lower football ATM base)
    Toronto games involving Caribbean/West African nations: community signal strong
    Vancouver games involving Asian nations: diaspora commercial signal
    
  CANADA-SPECIFIC SIGNAL:
    CanMNT hosting World Cup match at BMO Field: CDI event for Canadian football
    Canada advancing past group stage: first time since 1986 — maximum narrative
```

---

## Group draw intelligence

```
READING THE GROUP DRAW FOR TOKEN SIGNALS:

Pot 1 (highest-ranked nations): Brazil, France, Argentina, England, Spain,
       Portugal, Belgium, Netherlands (approximate — based on FIFA rankings)
       
These nations drive NCSI for the following club tokens:
  Brazil: $RMFC (Vinicius Jr, Militão), $BAR (Raphinha, Ferran Torres)
  France: $RMFC (Mbappé), $BAR (Dembélé), $CITY (pending)
  Argentina: $BAR (de Paul connection), $ATM, various
  England: $MUFC, $CITY, $BAR, $RMFC, various EPL clubs
  Spain: $BAR, $RMFC, $ATM
  Portugal: $RMFC (Bellingham + others)

DREAM DRAW vs DEATH GROUP:
  Pot 1 nation in easy group (Pots 3+4 opponents):
    Expected deep run → NCSI starts accumulating early
    Club token signal: positive from Draw Day onwards (narrative building)
    
  Pot 1 nation in group with multiple Pot 2 nations (death group):
    Early exit risk → uncertainty signal; wider NCSI confidence interval
    Club token: moderate signal; wait for Group Stage results before acting

SAME GROUP AS HOST NATION:
  Any nation in same group as USA/Mexico gets elevated attendance context
  TV audiences larger for matches in USA/Mexico venues
  Apply: × 1.10 NCSI weight for all matches in Mexico City / MetLife

RIVALRY DRAW:
  Brazil vs Argentina in groups: × 1.85 (historical rivals — highest match weight)
  England vs Germany in groups: × 1.60
  Spain vs Portugal in groups: × 1.50 (Iberian derby)
  USA vs Mexico in groups: × 1.55 (CONCACAF's defining rivalry on home soil)
  Any of these rivalries in knockout: add additional × 1.15 (elimination stakes)

AGENT RULE ON DRAW DAY:
  1. Load NCSI mappings for top-32 ATM players
  2. Check which group each player's nation is in
  3. Identify easy vs death group classifications
  4. Update NCSI confidence intervals based on draw outcome
  5. Flag any rivalry matches for highest-priority monitoring
```

---

## City-by-city commercial intelligence

```
HOST CITY DEMOGRAPHICS AND FAN TOKEN RELEVANCE:

NEW YORK / NEW JERSEY (MetLife — Final Venue):
  Demographics: Most diverse metro in USA; 3.4M Latinos
  Key fan bases: Italian, Brazilian, Central American, Colombian
  Token relevance: All finalist nations will have fanbase presence here
  Signal: Highest concentration of overseas fan token holders in USA
  
LOS ANGELES (SoFi Stadium):
  Demographics: 4.9M Latinos; large Mexican and Central American community
  Key nations: Mexico (primary), Guatemala, El Salvador, Brazil
  Token relevance: If Mexico draws LA games → de facto home crowd
  Signal: Largest single-city Latin American diaspora in USA
  
DALLAS (AT&T Stadium):
  Demographics: 1.7M Latinos; largest Mexican diaspora in Texas
  Key nations: Mexico (often treated as home venue), Central America
  Special: Dallas + Houston = Mexico's USA home crowd base
  Signal: Mexico games in Texas cities = × 1.25 crowd intensity signal
  
MIAMI (Hard Rock Stadium):
  Demographics: 70% Latino/Hispanic; large Cuban, Colombian, Venezuelan
  Key nations: Colombia, Venezuela, Argentina, Brazil
  Signal: Most Spanish-language sports media production in USA based here
  Token relevance: Latin American crypto adoption is highest in Miami diaspora

TORONTO (BMO Field):
  Demographics: 50%+ immigrant; Portuguese, Italian, Caribbean, South Asian
  Key nations: Portugal, Italy (if qualified), Trinidad & Tobago, India (diaspora)
  Signal: Portuguese community = $BAR/$RMFC signal through NCSI
  
VANCOUVER (BC Place — Dome):
  Demographics: Large Chinese, Korean, Filipino communities
  Key nations: South Korea, Japan, Australia, China (if qualified)
  Signal: Pacific Rim tournament gateway; different from all other venues

MEXICO CITY (Estadio Azteca — 87,500 capacity):
  Highest capacity venue in tournament
  Mexican fan noise: highest single-venue atmosphere
  El Grito (roar before kick-off): cultural signal of maximum crowd intensity
  Token relevance: If Mexico hosts any Central/South American team here:
    Azteca crowd = 12th man; apply home crowd modifier × 1.15
```

---

## World Cup 2026 agent monitoring framework

```
AUTOMATED MONITORING PROTOCOL FOR WC2026:

PRE-TOURNAMENT (January–June 11, 2026):

  January-March 2026:
    Monitor: National team friendlies — form signals and injury emergence
    Monitor: US regulatory developments (CFTC/SEC clarity)
    Monitor: New token launch announcements by national federations
    Frequency: Weekly scan
    
  April-May 2026 (Squad announcement window):
    CRITICAL: Final 26-man squads announced approximately 4-6 weeks before
    For every top-30 ATM player: check inclusion/exclusion status
    Mbappé/Haaland/Vinicius exclusion due to injury: CRITICAL negative signal
    Surprise inclusion of young ATM player (Lamine Yamal-tier): positive signal
    Frequency: Daily scan from April 1
    
  June 1-10 2026 (Final preparation):
    Training camp injury reports
    Manager press conferences: system signals and lineup hints
    Weather forecasts for venue cities (heat, humidity for US summer)
    Frequency: Twice daily

TOURNAMENT (June 11 – July 19, 2026):

  Daily cycle (6am local tournament time):
    Step 1: Load macro state (crypto market overnight movement)
    Step 2: Check today's match schedule
    Step 3: Identify token-relevant nations playing today
    Step 4: For each: load NCSI calculation with current competition tier weight
    Step 5: Check DeFi liquidity for relevant tokens pre-match
    Step 6: Set pre-match signal; alert if SMS ≥ 70
    
  Post-match (within 30 minutes):
    Step 1: Record result
    Step 2: Update NCSI cumulative tracker
    Step 3: Check for upset (did tournament favourite lose?)
    Step 4: If upset: check which club tokens lose NCSI (star player eliminated)
    Step 5: Generate post-match token signal update
    Step 6: Check CDI: is this a commercially valuable outcome?
    
  Knockout stage escalation:
    As rounds advance, increase monitoring frequency
    QF onwards: real-time monitoring during matches
    Apply fan-sentiment-intelligence.md CDI for each advancing nation

POST-TOURNAMENT (July 2026 onwards):
  Week 1: Tournament CDI peaks — maximum commercial window
  Week 2-4: Transfer window opens — APS recalculations for WC2026 stars
  Month 2-3: Engagement decay (see fan-sentiment-intelligence.md decay curve)
  End of year: Euro 2028 qualification begins — next cycle starts
```

---

## The World Cup 2026 fan token opportunity — consolidated

```
MARKET SIZE ESTIMATE FOR WC2026 FAN TOKEN COMMERCIAL WINDOW:

CURRENT FAN TOKEN MARKET (pre-WC2026):
  Active fan tokens: ~50+ club and national tokens
  Combined market cap: $200-400M range (varies with crypto market cycle)
  Active monthly holders: ~2-3M globally

WC2026 IMPACT PROJECTIONS (sport intelligence estimates):

  Conservative (US regulation not yet clear, moderate crypto market):
    New token holders acquired during tournament: +500k-1M
    Total active tokens: 60-70 (new national tokens launched)
    Market cap increase: +20-30% during tournament peak
    
  Base case (moderate US regulatory progress, neutral crypto market):
    New token holders: +2-4M during 39-day tournament
    New token holders retained 6 months later: 30-40% (DTS-style conversion)
    Market cap increase: +40-60% at tournament peak
    
  Optimistic (US regulation clear, bull crypto market concurrent):
    New token holders: +5-10M (unprecedented scale)
    World Cup = largest single fan token acquisition event in history
    Market cap: potential doubling or more during peak

CDI FOR WC2026 WINNER:
  Winning nation's club tokens:
    CDI = 45 (trophy) × 2.50 (WC outcome tier) × 1.00 (competition weight) = 112.5 days
    LTUI uplift for players on winning team: +8-12 per player
    If winning nation is major token market (Brazil, France, Spain):
      CDI × 1.50 = 168 days of above-baseline commercial engagement

AGENT DEPLOYMENT FOR WC2026:
  Deploy Pattern 3 (Tournament Tracker from agentic-workflows) starting June 1
  Configure with WC2026-specific NCSI weights from this document
  Connect to Pattern 1 (Portfolio Monitor) for daily token signal updates
  Use bundle: tournament-tracker from platform/skill-bundles.md
```

---

## Compatibility

**Full international cycle:** `market/international-football-cycle.md`
**NCSI formula:** `fan-token/football-token-intelligence/`
**Athlete ATM:** `athlete/football/athlete-intel-football.md`
**Fan sentiment CDI:** `fan-token/fan-sentiment-intelligence/`
**Tournament tracker agent:** `examples/agentic-workflows/README.md` — Pattern 3
**App blueprint:** `examples/applications/app-05-world-cup-dashboard.md`

---

## Post-tournament transition (July 2026 onwards)

The World Cup final is not the end of the signal cycle — it is the transition
into the next phase. See `market/international-football-cycle.md` for the full
post-tournament model. Summary for agents:

```
IMMEDIATELY AFTER WORLD CUP 2026 FINAL (July 2026):

Week 1-2:   Tournament narrative completes. Do not act on residual signal.
Week 3-6:   Transfer window peak. Run APS for all token-connected clubs.
             Players who starred at WC2026 = maximum transfer premium.
July-Aug:   Pre-season and league restart. Club signals resume primacy.
September:  FIRST dual event — post-WC2026 recovery + Euro 2028 qualification begins.
             Apply tournament fatigue modifier ×0.85 to all September NCSI calculations.

WHAT COMES AFTER WC2026:
  August 2026:    League season 2026-27 begins
  September 2026: First international break of new cycle
                  AND first Euro 2028 qualifying window
  2026-27:        UEFA Nations League 2026-27
  2027:           Euro 2028 qualification decisive stage
  2028:           UEFA European Championship 2028 (Netherlands + Germany)
  
Euro 2028 is the next Tier 1 European club token event.
For European club tokens, it is equivalent in signal weight to this World Cup.
Reference: market/international-football-cycle.md — Euro 2028 planning framework
```

---

## Cycle context

This document covers the 2026 FIFA World Cup specifically.
For the full international football cycle — NCSI weights across all competition types,
post-tournament transition model, Euro 2028 framework, international break protocol —
see `market/international-football-cycle.md`.

The World Cup is one peak in a perpetual cycle. What comes after is as important
as the tournament itself for long-term fan token intelligence.

*MIT License · SportMind · sportmind.dev*
