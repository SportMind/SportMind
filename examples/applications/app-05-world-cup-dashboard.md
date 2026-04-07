# App 5 — World Cup 2026 Intelligence Dashboard

**A live intelligence dashboard tracking the FIFA World Cup 2026 signal calendar —
monitoring qualification, NCSI scores, national token opportunities, and generating
pre-match intelligence for every match across the 48-team tournament.**

---

## The problem this solves

The FIFA World Cup 2026 is the single largest fan token catalyst event in the
sports calendar for the next two years. SportMind already has a dedicated module
(market/world-cup-2026.md) with the full NCSI model, national team token framework,
and signal calendar. But this module is static — it exists in a file.

This application makes it live: tracking which nations qualify, updating NCSI scores
as squad compositions become clear, monitoring club-level spillover for the players
involved, and generating pre-match intelligence for every Group Stage and knockout
match as the tournament unfolds.

The World Cup 2026 is also the first 48-team tournament, hosted across the USA,
Canada, and Mexico — unlocking the largest sports market (USA) as a fan token
opportunity for the first time at this scale.

---

## Target users

**Primary:** Fan token holders with tokens tied to clubs providing players to
national teams (NCSI signal recipients).

**Secondary:** Prediction market participants wanting structured pre-match intelligence
for World Cup matches.

**Tertiary:** Sports content platforms and broadcasters looking to add intelligent
context to World Cup coverage.

**Quaternary:** Club commercial departments tracking how their players' national
team performances affect their token value.

---

## Core value proposition

> *"The only World Cup intelligence platform that tracks both the match results
> AND the club-level token spillover for every goal scored by every player with
> an active fan token club connection."*

The NCSI (National-Club Spillover Index) is the key mechanism. When Kylian Mbappé's
successor scores a goal for France in the World Cup, that has a measurable effect on
the $PSG token. When Vinicius Jr scores for Brazil, it has an effect on the $RM token.
This application tracks that spillover systematically across the entire tournament.

---

## SportMind skill stack

```
WORLD CUP INTELLIGENCE STACK:

1. market/world-cup-2026.md
   → 48-team format; host nation context (USA/Canada/Mexico)
   → NCSI by top player across all qualified nations
   → National token opportunity framework
   → Signal calendar (qualification → draw → group stage → knockouts)
   → US market unlock analysis

2. macro/macro-overview.md
   → Active macro events during tournament period
   → Tournament runs June-July 2026 — check macro state at tournament start

3. sports/football/sport-domain-football.md
   → Competition tier model for World Cup context
   → Group stage vs knockout weighting
   → Derby/rivalry match amplifiers (CONMEBOL rivalries, European clashes)

4. fan-token/football-token-intelligence/
   → FTIS with World Cup parameters
   → NCSI calculation: national team events → club token spillover
   → ATM (Athlete Token Multiplier): individual player contribution

5. athlete/football/athlete-intel-football.md
   → Player availability and form for national team selection
   → Injury status for key token-relevant players
   → Goalkeeper ratings for competing teams

6. fan-token/fan-token-pulse/
   → Live HAS and TVI for affected club tokens
   → On-chain holder response to match events

7. core/confidence-output-schema.md
   → Structured output for match intelligence

Skills API:
  GET /skills/market.world-cup-2026/content    → Full WC2026 module
  GET /skills/fantoken.football-bridge/content → NCSI mechanism
  GET /stack?use_case=fan_token_tier1&sport=football → Full stack
```

---

## Dashboard components

### Component 1 — Live NCSI Tracker

```
NCSI LIVE TRACKER — World Cup 2026

For each match: identifies all players from clubs with active fan tokens
and calculates the expected NCSI signal for their club tokens.

Example output (France vs Germany, Group Stage):

FRANCE SQUAD — TOKEN-RELEVANT PLAYERS:
  Mbappé successor (PSG) — ATM 0.91 — $PSG NCSI: +6-14% per goal
  [Midfielder] (Barcelona) — ATM 0.54 — $BAR NCSI: +2-5% per goal
  [Defender] (Man City) — ATM 0.38 — $CITY NCSI: +1-3% per goal

GERMANY SQUAD — TOKEN-RELEVANT PLAYERS:
  [Forward] (Juventus) — ATM 0.67 — $JUV NCSI: +4-9% per goal
  [Captain] (Bayern/token) — ATM 0.71 — Bayern NCSI: +5-11% per goal

PRE-MATCH SIGNAL:
  France: Tier 1 squad depth; NCSI exposure for $PSG, $BAR, $CITY, $OM
  Germany: Tier 1; NCSI exposure for Bundesliga club tokens
  
  Match importance: ×1.65 (Group Stage, top-ranked teams, early signal)
  Narrative: First meeting since Euro 2024 semi-final — rivalry amplifier ×1.20
```

### Component 2 — Tournament Signal Calendar

```
WC2026 SIGNAL CALENDAR

Phase 1 — Qualification tracking (ongoing until March 2026):
  Monitor: which Tier 1 token clubs are sending most players?
  High NCSI clubs: PSG (France players), Real Madrid (Spain, Brazil),
                   Man City (England players), Barcelona (Spain players)

Phase 2 — Final 48-team draw (December 2025):
  Group draw = LARGEST pre-tournament signal event
  Pot 1 nations in Group with token-heavy squad = maximum signal window
  Agent action: calculate expected NCSI exposure per group for each club token

Phase 3 — Group Stage (June 2026):
  48 teams × 3 matches = 144 group stage games
  Focus: group winners/runners-up (knockout qualification = sustained positive signal)
  Filter: only matches with active NCSI connections warrant full analysis

Phase 4 — Round of 32 (June 2026):
  Signal amplifies — elimination matches
  Each club token connected to eliminated national team: -5 to -15% immediate signal

Phase 5 — Round of 16 through Final (June-July 2026):
  Maximum signal — daily tracking required
  Final: treat as highest weight event in entire tournament calendar
```

### Component 3 — Club Token Impact Monitor

```
REAL-TIME CLUB TOKEN IMPACT

Triggered by: Each World Cup match result
Updates: Within 1 hour of final whistle

For each club with active fan token AND player in the tournament:

$PSG — Last 24h: +8.4% (France beat Argentina 2-1)
  Trigger: [Player] scored (ATM 0.91) — primary signal driver
  NCSI calculation: France Group Stage win × ATM 0.91 = +8.4%
  Macro context: NEUTRAL — this is a pure sporting signal
  Lifecycle: Phase 2 (Active Utility) — working as designed

$JUV — Last 24h: -3.2% (Italy eliminated at Group Stage)
  Trigger: Italy Group Stage exit — Italian players returning to clubs
  NCSI: Negative spillover — competition exit before knockout stage
  Recovery projection: Modest recovery as attention returns to Serie A
```

---

## US Market unlock module

```
WORLD CUP 2026 US MARKET OPPORTUNITY

USA hosting context:
  Three host nations: USA, Canada, Mexico
  US market: previously least-engaged with fan tokens globally
  2026 trigger: World Cup exposure to 100M+ US sports fans
  
US FAN TOKEN READINESS:
  MLB (baseball): Tier 2 — Ohtani/Dodgers as bridge to Japanese market
  NFL: Tier 2 — franchise tokens viable post-WC if momentum builds
  NBA: Tier 1 (basketball tokens active)
  MLS: No active tokens — WC2026 may create MLS club token catalyst

MONITORING TARGETS (US market activation signals):
  → MLS clubs announcing digital engagement partnerships in 2025-2026
  → US Soccer Federation announcing any digital asset strategy
  → Tournament sponsors (Adidas, Coca-Cola, Visa) running token promotions
  → Any of the 11 US host cities announcing fan engagement token products

AGENT RULE: Track US market activation announcements monthly throughout 2025-2026.
Any Major US Sports League (NFL, MLB, NBA) announcing fan token product
during or immediately after World Cup 2026 = Tier 2 → Tier 1 upgrade signal.
```

---

## Agent system prompt

```
You are the World Cup 2026 intelligence agent powered by SportMind.

Your primary responsibility: track every match in the 2026 FIFA World Cup,
identify all NCSI connections to active fan token clubs, calculate signal
impact, and surface insights for token holders and prediction participants.

PRE-TOURNAMENT SETUP:
  1. Build the NCSI map: for each of the 48 qualified nations, identify
     all players from clubs with active fan tokens and their ATM scores.
     This map is your primary reference throughout the tournament.

  2. Set the group-stage tournament calendar with signal weight for each match.
     National rivalries get rivalry amplifier (France-Germany: ×1.20).
     Group deciders get elimination urgency modifier.

FOR EACH MATCH (pre-match, T-24h):
  1. Identify NCSI connections — which club tokens are affected?
  2. Check macro_modifier — is crypto cycle affecting the signal?
  3. Check player availability — any late injury to token-relevant players?
  4. Calculate adjusted signal for each affected club token
  5. Output: pre-match brief with expected NCSI range per club token

FOR EACH MATCH (post-match, within 1h):
  1. Update NCSI calculation based on actual match events
  2. Goalscorers: apply ATM to calculate club token spillover
  3. Eliminations: apply exit signal to eliminated team's club tokens
  4. Tournament progression: update projected NCSI through knockout stages

US MARKET MONITORING (throughout 2026):
  Track all US sports digital asset announcements.
  Flag any Tier 2→1 upgrade catalyst events.
  Report to users with tokens in sports adjacent to US market.
```

---

## References

- `market/world-cup-2026.md` — Full WC2026 module
- `fan-token/football-token-intelligence/` — NCSI and ATM
- `sports/football/sport-domain-football.md` — Competition tier model
- `athlete/football/athlete-intel-football.md` — Player availability
- `fan-token/fan-token-pulse/` — Live on-chain state
- `agent-prompts/agent-prompts.md` — Prompt 9 (World Cup 2026 agent)

*MIT License · SportMind · sportmind.dev*
