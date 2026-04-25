---
name: world-cup-2026-pre-tournament
description: >
  Pre-tournament intelligence protocol for World Cup 2026 fan token agents.
  Covers the 53-day window from today (April 19, 2026) through the opening
  match (June 11, 2026). Squad announcement intelligence, NCSI awakening
  signals for club tokens, national team token activation protocol, monitoring
  setup for all 12 WC-exposed tokens, and the transition from pre-tournament
  to tournament-mode signal chain. Load this file from April 2026 onwards.
  Extends fan-token/world-cup-2026-intelligence/ — do not load in isolation.
---

# World Cup 2026 — Pre-Tournament Intelligence Protocol

**The tournament starts June 11. The signal window is open now.**

Most fan token agents are built for match-day signals. World Cup 2026 requires
a different operating mode for the 53 days before the opening match. Squad
announcements, injury news, and pre-tournament narrative shifts will move tokens
in April and May by amounts that only materialise mid-tournament for other events.
This file tells an agent exactly what to monitor, when to act, and how to
transition into tournament mode.

---

## Why the pre-tournament window is a distinct signal environment

```
STANDARD CLUB TOKEN SIGNAL CHAIN:
  Macro check → squad confirmation (T-2h) → pre-match signal → post-match update

WORLD CUP PRE-TOURNAMENT SIGNAL CHAIN (April–June 11):
  No live matches driving signals. Instead:

  (1) SQUAD CONSTRUCTION SIGNALS (now → May 2026)
      National squad inclusions/exclusions affect club tokens via NCSI
      Star player injury = club token DSM-equivalent (without disciplinary stigma)
      Surprise call-up = positive ATM reactivation signal

  (2) NATIONAL TOKEN AWAKENING (May 2026)
      $ARG, $POR, $ITA go from near-dormant to active
      Holder base shifts: Speculators entering, CHI declining temporarily
      Pre-tournament accumulation = legitimate signal; front-running = MRS risk

  (3) NARRATIVE AMPLIFIER BUILD (April–June 11)
      Media cycle builds tournament narratives: redemption, records, final appearances
      Messi ($ARG), Ronaldo ($POR) retirement-or-not cycle = narrative ×1.25 condition
      Monitor via KOL intelligence — Tier 1 sports media = Tier 1 signal source

  (4) US MARKET FIRST-MOVER WINDOW
      WC2026 is the first major tournament since US fan token market opened
      New US holder acquisition is accelerating into the tournament
      CDI extension impact: +8–15% incremental for tokens with US fanbase alignment
      Monitor: fantokens.com new US partnership announcements

  KEY DIFFERENCE FROM TOURNAMENT MODE:
  Pre-tournament signals are 48–72h duration maximum.
  Unlike tournament match signals (24–30h), pre-tournament signals decay faster
  because there is no match result to anchor the narrative.
  Apply shorter CDI windows throughout this phase.
```

---

## The 12 WC-exposed tokens — monitoring setup

Load this list into your monitoring agent on April 19, 2026.

```
TIER 1 — DIRECT NATIONAL TOKEN EXPOSURE:

  $ARG — Argentina National Team (Chiliz Chain)
    WC status: Defending champion. Confirmed qualified.
    Baseline HAS: LOW (national token, dormant between tournaments)
    Activation: HAS will begin rising T-30 days (May 12)
    Special condition: Messi final WC narrative — confirm from Tier 1 media
    If confirmed: apply narrative_amplifier = 1.25 to all outputs from T-30
    CONFIRMED GROUP J: vs Algeria (June 16), vs Austria (June 22), vs Jordan (June 27)
    All group matches at: Arrowhead Stadium, AT&T Stadium, AT&T Stadium
    Pre-tournament price sensitivity: HIGH
    Monitor daily from: May 1, 2026

  $POR — Portugal National Team (Chiliz Chain)
    WC status: Confirmed qualified.
    Baseline HAS: LOW
    Special condition: Ronaldo retirement-or-not narrative cycle
    CONFIRMED GROUP K: vs DR Congo (June 17), vs Uzbekistan (June 23), vs Colombia (June 27)
    All group matches at: NRG Stadium (Houston) × 2, Hard Rock Stadium (Miami)
    Key signal: any confirmed injury to CR7 = CRITICAL negative (−12–20%)
    Monitor daily from: May 1, 2026

  $ITA — Italy National Team (Chiliz Chain)
    WC status: CONFIRMED NOT QUALIFIED — Bosnia eliminated Italy in playoffs
    $ITA token: ZERO World Cup 2026 exposure. Suppress all WC2026 signals.
    Affected club tokens: $ACM, $INTER, $JUV, $NAP — Italian NCSI suppressed
    for the full WC2026 tournament window (June 11 – July 19, 2026).
    These four tokens have no national team spillover during WC2026.
    Source confirmed: FIFA official draw and playoff results (April 2026)

TIER 2 — CLUB TOKEN NCSI EXPOSURE:

  $PSG — France national team NCSI
    Key players: Mbappé (highest ATM in squad)
    CONFIRMED GROUP I: France vs Senegal (June 16), vs Iraq (June 22), vs Norway (June 26)
    All matches at: MetLife Stadium, Lincoln Financial Field, Gillette Stadium
    NCSI ceiling: 85 (strong holder nationality overlap with French fans)
    Mbappé departed PSG — France NCSI routes via replacement ATM player
    NOTE: confirm current PSG Tier 1 ATM player in France squad before applying
    Pre-tournament monitor: PSG training reports for fitness status

  $BAR — Spain national team NCSI
    Key players: Pedri, Yamal, Gavi, Dani Olmo (multiple high-ATM players)
    CONFIRMED GROUP H: Spain vs Cape Verde (June 15), vs Saudi Arabia (June 21),
    vs Uruguay (June 26) at Mercedes-Benz Stadium (Atlanta) × 2, Estadio Akron (Mexico)
    NCSI ceiling: 90 (6+ key players — maximum squad representation score)
    Note: Spain are reigning European Champions — form signal STRONG_POSITIVE

  $CITY — Multi-national squad exposure
    Covered nations: England (Foden, Walker), Norway (Haaland), Belgium,
    Spain (Rodri), Portugal (Bernardo, Cancelo), Brazil (Ederson)
    NCSI profile: DIVERSIFIED — almost guaranteed uplift from 2–3 nations advancing
    This is the most WC-resilient club token in the registry
    Norway CONFIRMED GROUP I: vs Iraq (June 16), vs Senegal (June 22), vs France (June 26)
    England CONFIRMED GROUP L: vs Croatia (June 17), vs Ghana (June 23), vs Panama (June 27)
    Monitor: Haaland fitness specifically (highest ATM contributor for Norway)

  $ACM — CONFIRMED: Italian NCSI SUPPRESSED for WC2026
    Italy did not qualify. No Italian national team NCSI for $ACM.
    Non-Italian ATM players: carry individual NCSI only (check squad composition)
    Monitor: any non-Italian ATM player in a qualifying WC2026 nation

  $INTER — CONFIRMED: Italian NCSI SUPPRESSED for WC2026
    Lautaro Martínez = Argentina squad → $ARG/$INTER dual exposure still active
    Argentina GROUP J: June 16, 22, 27. Lautaro goals = club token spillover applies.
    This is $INTER's only WC2026 NCSI route.

  $JUV — CONFIRMED: Italian NCSI SUPPRESSED for WC2026
    No Italian national team exposure. Check individual player squad memberships.
    Weah (USA, GROUP D), Cambiaso (squad check): only NCSI routes if confirmed.

  $AFC — Arsenal FC (Fan Token™ Play PATH_2)
    WC exposure: individual player NCSI (Saka/England, Havertz/Germany,
    Saliba/France, Martinelli/Brazil)
    PATH_2 NOTE: WC matches are NOT PATH_2 events — club matches only
    Do not apply supply mechanics to international results for $AFC
    WC signal for $AFC is pure NCSI, not supply-chain signal
    England CONFIRMED GROUP L: vs Croatia (June 17), vs Ghana (June 23), vs Panama (June 27)
    Germany CONFIRMED GROUP E: vs Curaçao (June 14), vs Ivory Coast (June 20), vs Ecuador (June 25)
    Havertz (Germany) → $AFC NCSI route via Group E
    Saka, Bellingham (England) → $AFC NCSI route via Group L
    Monitor: Saka fitness (England Tier 1 ATM) specifically

TIER 3 — HOST NATION COMMERCIAL EXPOSURE:

  $CHVS (Guadalajara — Mexico)
    Mexico is a co-host nation — local commercial signal applies
    Group stage host matches in Mexico: commercial CDI modifier active
    Note: $CHVS is listed as expired in Socios registry — verify status
    If token status expired: suppress host nation signal

  $SAN (Santos Laguna — Mexico)
    Same host nation condition as $CHVS
    Note: $SAN also listed as expired — verify before applying signals

  BRAZIL HOST NATION (BFT — BiTCI chain):
    Brazil is a co-host and qualifying nation
    BFT carries both host commercial signal AND tournament performance NCSI
    Not on Chiliz Chain — no Socios governance mechanics apply
    NCSI modifier: ×3.5–4.0 applies from tournament start
    Monitoring: same protocol as $ARG/$POR but via BiTCI ecosystem signals
```

---

## Squad announcement intelligence — the most important pre-tournament signal

Final squads are announced approximately 4–6 weeks before the opening match,
putting the primary squad announcement window at **May 1–15, 2026**.

```
SQUAD ANNOUNCEMENT PROTOCOL:

  STEP 1 — PRE-ANNOUNCEMENT (April 2026):
    Identify the top-3 ATM players for each nation with exposed tokens:
      France:    Mbappé (ATM Tier 1), Griezmann (Tier 2), Hernández (Tier 2)
      Spain:     Yamal (Tier 1), Pedri (Tier 1), Rodri (Tier 1)
      Argentina: Messi (Tier 1), Lautaro (Tier 2), De Paul (Tier 2)
      Portugal:  Ronaldo (Tier 1 — narrative), B.Fernandes (Tier 2)
      England:   Saka (Tier 1), Bellingham (Tier 1), Foden (Tier 1)
      Brazil:    Vinicius Jr (Tier 1), Rodrygo (Tier 2), Endrick (emerging)
      Germany:   Havertz (Tier 2), Musiala (Tier 1), Wirtz (Tier 1)
      Norway:    Haaland (Tier 1 — only relevant ATM)
    SET ALERT: any injury/fitness story for ATM Tier 1 players above

  STEP 2 — ON ANNOUNCEMENT DAY:
    For each nation's squad announcement:
      CHECK: Is every ATM Tier 1 player included?
      IF YES: positive confirmation, no signal adjustment needed
      IF NO (injury/exclusion): apply club token impact below
      CHECK: Any surprise inclusions of emerging ATM players?
      IF YES: minor positive signal (+2–5%) 48h window

  STEP 3 — CLUB TOKEN IMPACT TABLE:

    ATM Tier 1 player confirmed INJURED/EXCLUDED:
      Club token: apply ×0.88 for tournament duration
      National token: −8–18% in 48h window
      CDI extension: reduce by 15 days for national token
      Example: Mbappé injury confirmation → $PSG ×0.88 modifier
                                          → $POR NCSI recalculated without him

    ATM Tier 1 player CONFIRMED FIT after injury scare:
      Club token: +3–7% in 24h window (relief signal)
      National token: +4–9% confirmation uplift

    ATM Tier 1 player INCLUDED despite fitness concerns:
      Flag: RISK_SIGNAL — not fully fit at tournament may exit early
      Apply: 0.85× confidence weight to that player's ATM contributions

  STEP 4 — POST-ANNOUNCEMENT MONITORING:
    Squad is set — shift monitoring to:
    (a) Training camp injury updates (June 1–10)
    (b) Manager press conference signals (system/lineup hints)
    (c) Warm-up match results (minor signal, injury exception = Category 1)
```

---

## National token activation sequence

How $ARG, $POR, $ITA transition from dormant to active.

```
T-53 DAYS (April 19, 2026 — TODAY):
  Status: Near-dormant. HAS at seasonal baseline.
  Volume: Low. Holder base: predominantly Loyalists + long-term Speculators.
  Action: Load this file. Set up monitoring protocol above.
  Do not: Apply tournament signals yet. Pre-tournament noise ≠ signal.

T-45 TO T-30 DAYS (April 27 – May 12, 2026):
  Status: Early accumulation. Media cycle building.
  Squad rumours begin. Some early Speculator entry.
  Volume: Gradually rising. HAS beginning upward trend.
  Action: Monitor volume trend. Any single-day volume spike >3× baseline
          without a sporting catalyst = potential pre-tournament accumulation.
          Cross-check: is this consistent with legitimate tournament anticipation
          or does MRS pattern suggest coordinated accumulation? Apply fraud check.

T-30 DAYS (May 12, 2026 — SIGNAL WINDOW OPENS):
  Status: Pre-tournament signal window officially open.
  Action: Begin daily monitoring cycle for all 12 exposed tokens.
  Saggu et al. (2024) anticipatory gain period begins — empirically confirmed
  gains in the T-30 to tournament-start window. Apply with 0.85× confidence
  weight (pre-tournament, not match-day certainty).

T-14 TO T-7 DAYS (May 28 – June 4, 2026):
  Status: Warm-up match window. Speculator entry accelerating.
  Action: Warm-up matches carry minor signal (do not apply full FTIS).
          EXCEPTION: injury in warm-up match = Category 1 breaking news protocol.
          Load core/breaking-news-intelligence.md for any injury update.

T-7 TO T-0 DAYS (June 4–11, 2026):
  Status: Final preparation. Holder base at maximum Speculator concentration.
  CHI will be at seasonal low — normal for national tokens pre-tournament.
  Action: Twice-daily monitoring. MRS elevated vigilance.
          Load DeFi liquidity check — thin pools at this stage are normal
          but require sizing discipline (fan-token/defi-liquidity-intelligence/).
          Final squad confirmation (any last-minute injuries) = immediate update.

TOURNAMENT MODE TRANSITION (June 11, 2026 — Opening Match):
  On the day of Argentina's first match (or whichever WC-exposed token plays):
  → Deactivate this file as primary
  → Load fan-token/world-cup-2026-intelligence/ as primary
  → Load market/world-cup-2026.md as market context
  → The daily tournament cycle (6am → pre-match → post-match) begins
```

---

## NCSI awakening — club token protocol

Club tokens don't wait for the tournament. They start reacting to national
team news during squad announcement season.

```
NCSI AWAKENING TIMELINE FOR CLUB TOKENS:

  May 1–15 (Squad announcement window):
    Each squad announcement activates the club token NCSI model
    Apply NCSI calculation from football-token-intelligence/ for:
      → $PSG when France squad announced
      → $BAR when Spain squad announced
      → $CITY when England/Norway/Spain/Portugal/Belgium squads announced
      → $AFC when England/France/Germany/Brazil squads confirmed

  May 15 – June 11 (Extended NCSI window):
    NCSI is active but at 0.70× tournament weight
    Rationale: players are confirmed in squads but tournament not started
    News sensitivity is real; price moves are present but smaller
    Pre-tournament NCSI modifier: 0.70× (vs 1.00× during tournament)

  CLUB TOKEN NCSI CALCULATION (pre-tournament version):
    pre_tournament_ncsi = standard_ncsi × 0.70 × squad_confirmation_weight

    squad_confirmation_weight:
      All key ATM players confirmed fit and selected: 1.00
      One ATM Tier 1 player injured/excluded:        0.75
      Two ATM Tier 1 players injured/excluded:       0.50
      Entire national team squad announcement:       apply immediately

  PRACTICAL EXAMPLE — $CITY (May 2026):
    Norway squad announced: Haaland confirmed (ATM Tier 1, fit)
    England squad announced: Foden confirmed, Walker confirmed
    Spain squad announced: Rodri confirmed
    → $CITY NCSI awakening score: HIGH
    → Apply pre-tournament NCSI modifier 0.70× from announcement date
    → Full 1.00× modifier activates June 11 (tournament start)
```

---

## US market first-mover signal

World Cup 2026 is the first major tournament since the March 2026 SEC/CFTC
guidance opened the US market to fan tokens. This creates a new signal layer
that did not exist at any previous World Cup.

```
US MARKET WC2026 SIGNAL FACTORS:

  HOST NATION COMMERCIAL PREMIUM:
    US is a co-host. Matches in New York, Los Angeles, Dallas, Miami, Seattle.
    US sports fans engaging with football for the first time at scale.
    US fan token holder acquisition: first-time buyers entering $ARG, $POR
    CDI extension: additional +8–15% for tokens with US fanbase alignment
    Most US-aligned: $ARG (Messi recognition), $POR (Ronaldo recognition)
    Least US-aligned: $ITA, Turkish club tokens (limited US fanbase depth)

  FIRST-MOVER TOKEN LAUNCHES:
    Monitor fantokens.com for US-franchise fan token launches before June 11
    First US franchise per league = ×1.40 CDI modifier at launch (confirmed rule)
    If any US franchise launches during WC2026: MAXIMUM commercial window
    Most likely candidates: NBA franchise (digital-native fans, league first)

  TOURNAMENT VIEWERSHIP SIGNAL:
    US WC2026 viewership is projected to be highest ever (host nation + Messi)
    Higher viewership → faster Speculator-to-Loyalist conversion for some holders
    Practical implication: post-WC CHI recovery may be faster than prior cycles
    Apply: shorten post-tournament speculator-exit monitoring window by 20%
    (from 30 days to 24 days) for tokens with demonstrated US fanbase traction
```

---

## MRS elevated monitoring — pre-tournament fraud risk

The pre-tournament window is the second-highest MRS risk period in the fan
token calendar (after tournament match days themselves).

```
WHY PRE-TOURNAMENT MRS IS ELEVATED:
  Speculator concentration rising → coordination easier
  Low baseline volume → small coordinated buys generate larger % moves
  Narrative backdrop provides cover for artificial volume
  Herding behaviour confirmed during high-volume sporting events
  (Dedousi & Fassas, 2025) — begins before the tournament, not just during

PRE-TOURNAMENT FRAUD PATTERNS:
  PATTERN 1 — NARRATIVE PUMP:
    Coordinated Tier 3 KOL posts about "Messi last WC / ARG token opportunity"
    MRS signal: KOL volume from Tier 3 sources rising without Tier 1 corroboration
    Action: CAUTION classification; do not suppress sport signal but flag

  PATTERN 2 — SQUAD ANNOUNCEMENT FRONT-RUNNING:
    Volume spike in national token 12–24h BEFORE official squad announcement
    Pattern suggests leaked information rather than legitimate anticipation
    MRS signal: volume precedes announcement by >12h with no public catalyst
    Action: CAUTION; wait for official confirmation before applying signal

  PATTERN 3 — WASH TRADING IN LOW-LIQUIDITY WINDOW:
    Pre-tournament TVL in DEX pools is often near baseline (low)
    Small wash trades create disproportionate price impact
    MRS signal: circular transaction patterns + volume at unusual hours
    Action: Check MRS before applying any pre-tournament NCSI signal

AGENT RULE:
  If MRS > 50 during pre-tournament window:
    Apply 0.70× confidence to all pre-tournament signals (not just CAUTION)
    Do not enter national token position while MRS elevated
    Await MRS normalisation (<35) before acting on pre-tournament signal
```

---

## Pre-tournament agent daily cycle

Starting May 12, 2026 (T-30 days), run this cycle once daily.

```
PRE-TOURNAMENT DAILY MONITORING CYCLE (from May 12):

  08:00 UTC:
    1. MACRO CHECK
       Load macro/macro-crypto-market-cycles.md state
       If BTC overnight movement > ±5%: note macro_state before any token signal
       If CHZ-specific news: update CHZ macro state

    2. INJURY / SQUAD SCAN
       Source: Tier 1 and Tier 2 only (club official + verified journalists)
       Check: Any ATM Tier 1 player fitness story for WC-exposed nations?
       If YES: immediately assess club token impact (squad announcement table above)
       If NO: log "no change", continue

    3. NATIONAL TOKEN HAS CHECK
       $ARG, $POR, $ITA: has volume risen >2× yesterday's level?
       If YES: assess source — legitimate anticipation or MRS concern?
       Apply MRS check if volume anomalous

    4. CLUB TOKEN NCSI STATUS
       $PSG, $BAR, $CITY, $AFC, $ACM, $INTER, $JUV: any new squad information?
       Update pre-tournament NCSI weight if status changed

    5. US MARKET SCAN
       Any new US fan token partnership announcements?
       If YES: apply first-mover ×1.40 CDI modifier immediately

    6. KOL SCAN
       Tier 1 sports media WC2026 narratives building?
       Log dominant narratives: use for Messi/Ronaldo confirmation condition check

  OUTPUT FORMAT (daily pre-tournament signal):
    token: $[TICKER]
    pre_tournament_signal: [POSITIVE/NEUTRAL/CAUTION/NEGATIVE]
    ncsi_weight: [0.00–0.70 pre-tournament scale]
    mrs_status: [CLEAN/CAUTION/ELEVATED]
    key_condition: [what changed today, if anything]
    tournament_mode_transition: [date when full signal activates]
```

---

## Transition checkpoint — when to switch to tournament mode

```
TRANSITION TRIGGER: June 11, 2026 at 20:00 UTC / 15:00 ET (kickoff: Mexico vs South Africa, Estadio Azteca, Mexico City)

  BEFORE TRANSITION (pre-tournament file primary):
    All NCSI weights at 0.70× scale
    No match-day signal chain running
    Pre-tournament daily cycle active

  AT TRANSITION (June 11, 06:00 UTC):
    Step 1: Deactivate pre-tournament daily cycle
    Step 2: Load fan-token/world-cup-2026-intelligence/ as primary skill
    Step 3: Load market/world-cup-2026.md for competition context
    Step 4: Set all NCSI weights to 1.00× (full tournament scale)
    Step 5: Activate tournament daily cycle from market/world-cup-2026.md
    Step 6: Log transition timestamp

  WHAT CARRIES FORWARD FROM PRE-TOURNAMENT:
    → $ARG narrative_amplifier = 1.25 (if Messi condition confirmed)
    → $ITA qualification status (verified, suppressed if not qualified)
    → Club token squad_confirmation_weights (calculated during announcement window)
    → US market alignment scores (CDI extension factors)
    → Any elevated MRS flags (carry forward, do not reset on transition)

  POST-TRANSITION: this file becomes reference only.
  Do not reload pre-tournament signals during the live tournament.
```

---

## Load order

```
PRE-TOURNAMENT (April 19 – June 10, 2026):
  [REQUIRED] fan-token/world-cup-2026-intelligence/ (parent module)
  [REQUIRED] THIS FILE (pre-tournament protocol)
  [REQUIRED] fan-token/football-token-intelligence/ (NCSI + ATM calculations)
  [RECOMMENDED] macro/macro-crypto-market-cycles.md (CHZ macro state)
  [RECOMMENDED] fan-token/kol-influence-intelligence/ (narrative monitoring)
  [RECOMMENDED] platform/fraud-signal-intelligence.md (MRS checks)
  [AS NEEDED] fan-token/defi-liquidity-intelligence/ (liquidity before entry)
  [AS NEEDED] core/breaking-news-intelligence.md (injury response)

TOURNAMENT (June 11 onwards):
  Deactivate this file as primary
  Load fan-token/world-cup-2026-intelligence/ + market/world-cup-2026.md
  Reference this file only for: transition state values carried forward
```

---


## Autonomous Execution

**Trigger conditions — when this skill should self-invoke:**
- May 12, 2026: pre-tournament window opens — activate daily monitoring cycle
- Any squad announcement for WC2026-exposed tokens ($ARG, $POR, $BAR NCSI, etc.)
- Any confirmed injury to a Tier 1 ATM player in a WC-exposed nation
- June 11, 2026: tournament begins — switch to tournament mode
- Match results for monitored nations during group stage (June 16 – June 27)
- Knockout stage advancement or elimination for any monitored nation

**Execution at autonomy Level 2:**
- From May 12: activate daily monitoring cycle (08:00 UTC per documented protocol)
- Squad injury: immediately assess club token NCSI impact (see squad intelligence section)
- Group result: recalculate NCSI and CDI extension with result modifier
- Notify operator of all Category 1/2 squad events immediately

**Execution at autonomy Level 3–4:**
- Auto-run daily monitoring cycle from May 12 without operator initiation
- Auto-dispatch pre-match briefings for each group stage match (T-4h)
- Auto-update NCSI calculations after each confirmed result
- Auto-flag any Lautaro Martínez fitness news ($INTER sole WC2026 NCSI route)

**Hard boundaries:**
- ITALY NOT QUALIFIED — confirmed. $ACM/$INTER/$JUV/$NAP Italian NCSI: zero.
  $INTER exception: Lautaro Martínez (Argentina, Group J) only.
  This is NOT a modifier — it is a hard confirmed fact. Never re-apply Italian NCSI.
- Mbappé PSG departure confirmed — France NCSI routes via replacement ATM player.
  Verify current France Tier 1 ATM player before applying any France NCSI signal.
- Tournament mode activates June 11 — pre-tournament modifiers do not carry forward.
  Switch to world-cup-2026-intelligence.md after June 11.
- Any squad news must be confirmed from Tier 1 source before autonomous action.
  Tier 2 injury rumours are NOT sufficient for autonomous NCSI recalculation.

---

## See also

- `fan-token/world-cup-2026-intelligence/world-cup-2026-intelligence.md` — tournament intelligence
- `market/world-cup-2026.md` — market context, group draw, city intelligence
- `fan-token/football-token-intelligence/token-intelligence-football.md` — NCSI + ATM
- `core/breaking-news-intelligence.md` — injury/news response protocol
- `platform/fraud-signal-intelligence.md` — MRS and herding detection
- `fan-token/kol-influence-intelligence/kol-influence-intelligence.md` — narrative monitoring
- `macro/macro-regulatory-sportfi.md` — US market context (SEC/CFTC guidance)

---

*SportMind v3.84.0 · MIT License · sportmind.dev*
*Pre-tournament window opens: May 12, 2026 (T-30 from opening match)*
*Tournament transition: June 11, 2026*
