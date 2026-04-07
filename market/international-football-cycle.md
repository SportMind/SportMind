# International Football Cycle — SportMind Intelligence Framework

**The perpetual cycle model for international football signals.**
The World Cup is not the destination — it is one peak in a continuous cycle that
never ends. This document defines the full cycle, its signal weights, post-tournament
transition behaviour, and the NCSI hierarchy across all competition types.

---

## Why a cycle model, not an event model

SportMind's existing documents treat international football events individually:
`world-cup-2026.md` covers the World Cup, and the football token intelligence skill
mentions the Euros. This creates a gap: agents know how to analyse a World Cup
quarter-final but not what the signal environment looks like the week after the
final whistle.

The reality is a perpetual cycle:

```
PERPETUAL INTERNATIONAL FOOTBALL CYCLE

League season          ←─────────────────────────────────────────────┐
  (Aug–May, annual)                                                    │
       ↓                                                               │
International breaks   ← September, October, November, March breaks   │
  (friendlies +                                                        │
   qualification)                                                      │
       ↓                                                               │
UEFA Nations League    ← Group stage Sept–Nov, Finals June            │
  (2-year cycle)                                                       │
       ↓                                                               │
Major tournament       ← World Cup (4-year, even years)               │
  (June–July)             Euros (4-year, even years, offset by 2)     │
       ↓                                                               │
Post-tournament        ← Transfer window opens immediately            │
  transition                                                           │
       ↓                                                               │
League season restart  ← Pre-season, kit reveals, first match        ─┘
  (July–August)
```

The cycle has no start and no end. An agent reasoning about fan tokens must know
where in the cycle the current date sits — not just which match is next.

---

## The three-tier international signal hierarchy

All international football events sit in one of three tiers. This is the NCSI
weight table that governs club token spillover for every international event.

### Tier 1 — Maximum international signal (NCSI weight: 1.00)

**FIFA World Cup**
- 32-team format (2026: 48 teams, first expansion)
- Every 4 years (2022, 2026, 2030...)
- Highest single tournament signal in the library
- National team tokens: direct reaction
- Club tokens: NCSI spillover via ATM calculation
- Transfer window follows immediately: World Cup performances = transfer market catalyst

**UEFA European Championship (Euros)**
- 24-team format; purely European nations
- Every 4 years (2024, 2028, 2032...) — offset by 2 years from World Cup
- For European club tokens: equal to World Cup in signal weight
  Reason: ALL players in the Euros come from European clubs. The national team–club
  token connection is tighter than the World Cup (which dilutes across global clubs).
- $BAR, $PSG, $JUV, $CITY token holders are primarily European. Their national team
  identities are mostly in the Euros, not the World Cup group stage.
- Club spillover: highest per-player of any tournament because player identity is
  concentrated in a smaller pool of clubs

```
EURO vs WORLD CUP — TOKEN SIGNAL COMPARISON:

  World Cup (Tier 1):
    National tokens: highest absolute signal
    Club tokens: spread across global clubs → individual club NCSI lower per player
    Duration: 32 days (2022) / 39 days (2026 with 48 teams)
    
  Euros (Tier 1, equal weight):
    National tokens: European only
    Club tokens: concentrated in top European clubs → individual club NCSI HIGHER
    Duration: 31 days
    
  AGENT RULE: For European club tokens ($BAR, $PSG, $JUV, $CITY, $RM etc.),
  apply Euros NCSI at 1.10× the World Cup NCSI because player concentration is higher.
  A French player at PSG generates more $PSG token signal at the Euros than the World Cup
  because the Euros audience is more concentrated in European fan token holders.
```

### Tier 2 — Significant international signal (NCSI weight: 0.55–0.75)

**UEFA Nations League**
- 55 UEFA nations in 4 leagues (A, B, C, D)
- Played September–November (group stage) + June (Finals)
- League A Finals: 4 nations, single venue weekend — equivalent to a minor tournament
- Provides competitive fixtures between international breaks
- Signal weight: League A matches = 0.75; League B = 0.55; League C/D = 0.30

**World Cup Qualification (European)**
- Played March, June, September, October, November
- Group stage + playoffs
- High-stakes matches (last qualifying places) = elevated NCSI
- Signal weight: decisive qualifier = 0.70; early group match = 0.45

**Euro Qualification**
- Played March, June, September, October, November (2 years before each Euros)
- Structure similar to World Cup qualification
- Signal weight: same as World Cup qualification

**Copa América, Africa Cup of Nations, Asian Cup**
- Continental tournaments for non-European national tokens
- Copa América: every 4 years (also temporary expansion cycles) — ARG, BRA tokens
- AFCON: every 2 years — CAF nations, limited active fan tokens currently
- Signal weight: Copa América = 0.80 (ARG/BRA token signal); others = 0.50

### Tier 3 — Low international signal (NCSI weight: 0.10–0.25)

**International Friendlies**
- Played during every international break (September, October, November, March)
- Normally low signal — but with specific high-value exceptions:

```
WHEN FRIENDLIES HAVE REAL SIGNAL VALUE:

1. INJURY COMEBACK:
   Player returning from significant injury plays in a friendly
   → Clears injury_warning flag for their club token
   → Signal: positive for club token; confirms player available for club season
   NCSI weight: 0.20 (single match) but strategic importance is HIGH

2. SQUAD SELECTION SIGNAL:
   Manager selects/drops a key player from national squad for friendly window
   → Dropped: potential form or fitness concern for their club
   → Selected after period out: rehabilitation confirmed
   NCSI weight: 0.15 per match but directional information is valuable

3. PRE-TOURNAMENT PREPARATION:
   Friendlies in the 2-3 windows before a major tournament
   → Tactical system signals: what formation/system is the manager testing?
   → Squad hierarchy signals: who is starting vs rotating?
   NCSI weight: 0.20 + tournament proximity modifier (×1.5 if tournament is <3 months away)

4. HIGH-PROFILE NEUTRAL VENUE:
   "Prestige friendlies" (e.g. England at Wembley vs Brazil, France at Stade de France
   vs Argentina) have elevated engagement but not elevated signal weight
   NCSI weight: 0.25 maximum — never more regardless of occasion

STANDARD FRIENDLY:
   NCSI weight: 0.10
   Agent default: load domain skill only; do not load full fan token intelligence stack
   Exception: activate full stack only if one of the four conditions above applies
```

---

## Post-tournament transition model

This is the undocumented territory. After every Tier 1 tournament ends, the signal
environment transitions through four phases before returning to the league baseline.

### Phase 1 — Immediate post-tournament (Week 1–2 after final)

```
WHAT HAPPENS:
  Tournament narrative completes: winner token peaks, loser tokens have bottomed
  Player fatigue sets in: clubs managing returning players carefully
  Transfer speculation begins: tournament standouts = instant transfer targets
  Media saturation: tournament remains in cycle for 1–2 weeks

SIGNAL BEHAVIOUR:
  National tokens: winner holds for 3–5 days then decays toward league baseline
  Club tokens: NCSI spillover completes; tokens begin normalising
  Transfer-linked tokens: tokens of clubs connected to transfer targets = elevated
  
TOKEN RECOMMENDATION FOR AGENTS:
  Week 1 post-tournament: do not act on residual tournament signal
  It is narrative momentum, not new sporting signal
  Load core/core-narrative-momentum.md — post-tournament decay section
  
APS NOTE:
  Transfer window opens immediately post-tournament
  Agents should load fan-token/transfer-signal/ — APS becomes primary signal
  Players with World Cup/Euro spotlight = elevated transfer probability
  Their club's token = APS calculation required urgently
```

### Phase 2 — Transfer window peak (Week 3–6 after final)

```
WHAT HAPPENS:
  Major transfers announced: clubs buying tournament stars
  Fee records sometimes broken: World Cup winners command premium
  Squad disruption: clubs that sell tournament stars lose key NCSI drivers
  
SIGNAL BEHAVIOUR:
  Buying club token: positive signal (+5–20% depending on player ATM)
  Selling club token: short-term negative, medium-term neutral to positive
    (transfer fee received → reinvestment signal)
  Player token (if exists): peak ATM moment immediately post-tournament
  
TRANSFER PRIORITY AFTER TOURNAMENTS:
  1. World Cup Golden Boot winner: maximum ATM; maximum club token disruption if sold
  2. Tournament best XI players: high ATM; significant disruption
  3. Breakout tournament performers: elevated ATM for 6–12 months
  4. Tournament injured players: flag for clubs — reduced ATM; monitor recovery

AGENT RULE:
  After every Tier 1 tournament, run APS calculation for all clubs with tokens
  whose players featured prominently.
  Load fan-token/transfer-intelligence/ for full TVS + DLVS assessment.
```

### Phase 3 — Pre-season and league restart (July–August)

```
WHAT HAPPENS:
  Club pre-season tours begin: club identity reasserts
  Kit reveals: annual positive engagement event (+2–5% HAS spike)
  New signings announced: fresh from post-tournament transfer window
  First competitive match back: league season opener
  
SIGNAL BEHAVIOUR:
  Club tokens: return to domestic/European competition drivers
  National token signal: dormant until September international break
  NCSI: resets to league-level weighting; no sustained national team signal
  
CLUB SEASON RESTART SEQUENCE:
  Day 1 of pre-season: squad announced → APS/TVS updated
  Kit reveal: engagement spike → positive HAS signal
  First pre-season friendly: fitness signals, new signing integration
  Community Shield / Supercopa / equivalent: first competitive match
  Gameweek 1 of league: full club token signal resumes
  
AGENT RULE:
  From the first day of pre-season: shift from international cycle to club cycle.
  Disable NCSI calculations until September international break.
  Primary signal drivers: UCL draw (July/August), transfer window deadline,
  squad depth for new season.
```

### Phase 4 — Return to normal cycle (September onwards)

```
WHAT HAPPENS:
  September international break: first post-tournament international window
  Nations League or qualification resumes (depending on cycle year)
  Club and international signals run in parallel again
  
SIGNAL HIERARCHY:
  Club match week: primary signal (as always)
  International break week: NCSI activates for 10 days, then resets
  
POST-TOURNAMENT SEPTEMBER SIGNAL IS WEAKER THAN NORMAL:
  Players physically tired from long tournament summer
  Squads rotating more heavily than normal
  Nations League group stage has lower stakes than pre-tournament qualification
  
  Apply ×0.85 to all NCSI calculations in September following a Tier 1 tournament.
  This is the tournament fatigue modifier — documented here for the first time.
```

---

## The full NCSI weight table (all competition types)

This supersedes and extends the NCSI table in `fan-token/football-token-intelligence/`.

| Competition | NCSI weight | Notes |
|---|---|---|
| FIFA World Cup | 1.00 | Maximum; global national + club tokens |
| UEFA European Championship | 1.00 (×1.10 for European clubs) | Higher concentration per European club |
| Copa América | 0.80 | ARG, BRA tokens; limited other national tokens active |
| UEFA Nations League Finals | 0.75 | League A, Final 4 format |
| World Cup qualification (decisive) | 0.70 | Last qualifying places; high stakes |
| Euro qualification (decisive) | 0.70 | Same structure as WC qualification |
| Africa Cup of Nations | 0.65 | Limited active club token connections currently |
| Nations League group stage (League A) | 0.60 | Competitive but non-eliminating |
| World Cup / Euro qualification (group) | 0.45 | Early stage; lower stakes |
| Asian Cup | 0.45 | Growing relevance as Korean/Japanese clubs get tokens |
| Nations League (League B) | 0.40 | Below top tier nations |
| Pre-tournament friendly (< 3 months) | 0.20 | With proximity modifier ×1.5 |
| Prestige friendly | 0.25 | Never higher regardless of occasion |
| Standard friendly | 0.10 | Default; special cases documented above |
| Post-tournament period (Phase 1) | 0.00 | Narrative only; do not act on residual signal |

---

## Euro 2028 — planning framework

```
EURO 2028 OVERVIEW:
  Host: Netherlands and Germany (awarded 2024)
  Dates: June–July 2028
  Teams: 24
  Format: group stage + knockout, same as 2024
  
SIGNIFICANCE FOR FAN TOKENS:
  This is the next Tier 1 European club token event after World Cup 2026.
  For European club tokens, Euro 2028 is as important as World Cup 2026.
  
SIGNAL CALENDAR (working backwards from June 2028):
  2026 (September–November): Euro 2028 qualification begins
  2026 (March): first qualification matches
  2027 (September–November): qualification decisive stage
  2027 (November): playoff draws
  2028 (March): final playoffs
  2028 (April–May): Euro 2028 squad naming signals
  2028 (June): Euro 2028 tournament

KEY MONITORING TARGETS FOR EURO 2028:
  Which clubs provide players to qualification group leaders?
  (Germany, France, Spain, England, Portugal typically = highest club NCSI)
  Any new European clubs launching tokens before 2028?
  Nations League 2026-27 results → Euro 2028 seeding implications
  
AGENT NOTE:
  Euro 2028 qualification begins September 2026 — just 2 months after World Cup 2026 ends.
  The post-tournament transition from World Cup 2026 flows directly into Euro 2028
  qualification without a gap. September 2026 international break = first post-WC2026
  AND first Euro 2028 qualifying window simultaneously.
```

---

## International break management for agents

The ten international windows per year each require a consistent agent protocol:

```
INTERNATIONAL BREAK PROTOCOL (apply every September, October, November, March window):

PRE-BREAK (T-7 days):
  1. Which club players are going on international duty?
     Load athlete/football/ — national team data for key ATM players
  2. Determine NCSI weight for their competition:
     Nations League or qualification? Apply appropriate tier weight from table above
  3. Set lineup_unconfirmed for club matches surrounding the break
  4. Check injury_warning for players with recent injuries

DURING BREAK:
  1. Monitor international results for NCSI-relevant players
  2. Apply NCSI calculation per match result
  3. Track injuries (critical — international injury = club availability concern)
  4. Friendly exceptions: check four special-case conditions above

POST-BREAK (T+1 to T+7 after return to clubs):
  1. International injury log: which players returned injured?
     Activate injury_warning for their club token
  2. Fatigue assessment: Nations League Finals players need 1-week recovery
  3. NCSI reset: clear international signal; return to club signal drivers
  4. Tournament fatigue modifier: apply ×0.85 if break follows Tier 1 tournament (Phase 4)

MONITORING RULE:
  The three most important international break signals for club tokens:
  1. Star player injury (immediate negative impact)
  2. Star player return from injury (immediate positive)
  3. Decisive qualification result (sustained positive/negative depending on outcome)
```

---

## Relationship to other SportMind documents

| Document | Relationship |
|---|---|
| `market/world-cup-2026.md` | Specific tournament; this document provides the cycle context |
| `fan-token/football-token-intelligence/` | NCSI mechanism; this document provides the weights |
| `fan-token/transfer-signal/` | APS and TVS; activated in Phase 2 post-tournament |
| `core/temporal-awareness.md` | Freshness tiers; international breaks are Tier 3 events |
| `core/core-narrative-momentum.md` | Post-tournament narrative decay model |
| `macro/macro-geopolitical.md` | Tournament hosting context; geopolitical signals |
| `athlete/football/` | ATM calculations for NCSI |

---

## Agent loading instruction

```
WHEN TO LOAD THIS DOCUMENT:

Always load when:
  - Analysing international break signal for a club token
  - Assessing post-tournament club token behaviour
  - Planning token intelligence for Euro 2028 window
  - Determining NCSI weight for any non-World Cup competition

Do not replace with:
  - world-cup-2026.md (that covers the specific tournament; this covers the cycle)
  - football-token-intelligence (that covers the mechanism; this covers the weights)

LOAD SEQUENCE when international cycle is relevant:
  1. This document (cycle context + NCSI weights)
  2. market/world-cup-2026.md (if tournament is active or imminent)
  3. fan-token/football-token-intelligence/ (NCSI mechanism + ATM)
  4. athlete/football/ (player-specific ATM values)
  5. core/temporal-awareness.md (freshness tier for each data type)
```

---

*MIT License · SportMind · sportmind.dev*
