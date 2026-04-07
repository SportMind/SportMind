---
name: esports-token-intelligence
description: >
  Esports-specific fan token intelligence. Use when the user asks about esports org
  token impact from tournament results, roster changes, patch updates, multi-game
  org dynamics, or any on-chain signal tied to esports fan tokens. Esports tokens
  are org-level (not game-level) but price is driven by the org's highest-profile
  active roster. Produces OrgTIS (Organisation Token Impact Score), Game Roster
  Multiplier (GRM), and Patch Risk Score (PRS).
  Load alongside sports/esports and fan-token-pulse.
---

# Esports Token Intelligence

Esports fan tokens are structurally the most complex in the SportMind ecosystem.
Unlike football (club tokens) or MMA (fighter tokens), esports tokens are
**organisation-level** — one token represents an org that may field rosters across
5+ different games simultaneously. The token's price is driven primarily by whichever
of those rosters is currently in the highest-profile active tournament.

This multi-game complexity, combined with the fastest-moving patch/roster environment
in any sport, creates a token intelligence challenge that no generic sports skill can
address adequately.

---

## What this skill produces

- **Organisation Token Impact Score (OrgTIS)** — Tournament × game × org composite (0–100)
- **Game Roster Multiplier (GRM)** — Which game is currently driving the org's token?
- **Patch Risk Score (PRS)** — How exposed is the org to the current meta change?
- **Roster Stability Index (RSI)** — Transfer and squad change risk for the token
- **Multi-Game Calendar Intel** — When multiple org rosters compete simultaneously
- **Peak Season Detection** — October-November stack window identification

---

## Organisation Token Impact Score (OrgTIS)

```
OrgTIS = (
  active_tournament_tier    * 0.35 +  # what competition is the org's best roster in?
  game_audience_weight      * 0.25 +  # CS2 > LoL > Valorant > Dota2 globally
  org_token_health          * 0.20 +  # HAS baseline from fan-token-pulse
  roster_strength_score     * 0.20    # is this their best lineup or a reserve squad?
) * 100
```

| OrgTIS | Label | Agent action |
|---|---|---|
| 85–100 | Maximum | Full chain — Worlds / Major level |
| 70–84 | High | fan-token-pulse + GRM + social monitoring |
| 55–69 | Elevated | Monitor; enter on strong result confirmation |
| 40–54 | Standard | Base signal; standard sizing |
| 25–39 | Low | Skip or minimal |
| 0–24 | Negligible | Ignore |

---

## Game Roster Multiplier (GRM)

The GRM determines which game is driving the org's token at any given moment.
An org's token price is functionally set by:

```
token_price_driver = max(GRM_i × tournament_tier_i) across all active rosters

GRM per game (indicative, varies by org):
  CS2:               0.90–1.40  (highest global viewership, clearest token correlation)
  League of Legends: 0.80–1.30  (Worlds = peak; massive Asian audience)
  Valorant:          0.70–1.15  (fastest growing; Champions = major event)
  Dota 2:            0.65–1.10  (The International = highest prize pool)
  EA FC / FIFA:      0.50–0.80  (football crossover; smaller dedicated audience)
  Rocket League:     0.45–0.70  (growing; unique audience)
  Other titles:      0.30–0.60  (depends on org strength in that game)
```

**Critical rule:** GRM is not fixed — it shifts based on which roster is actively
competing in the highest-tier tournament at that moment.

Example:
```
An org has active CS2 and LoL rosters.
CS2 roster is in IEM Cologne (Tier 2 Major).
LoL roster is in LEC group stage (Tier 3 domestic).
→ GRM_active = CS2 (IEM Cologne × 0.95) > LoL (LEC × 0.60)
→ CS2 roster is driving the token this week.

Next month, LoL enters Worlds (Tier 1 annual peak).
CS2 roster just exited at groups.
→ GRM_active = LoL (Worlds × 1.30) > CS2 (no tournament × 0)
→ LoL roster is now driving the token.
```

**Agent rule:** Always identify the active GRM driver before running any other
analysis. The wrong game's metrics will produce incorrect signals.

---

## Tournament Tier Classification by Game

### CS2 (Counter-Strike 2)

| Event | Tier | OrgTIS base | Signal window |
|---|---|---|---|
| CS2 Major (ESL/FACEIT) | 1 | 88 | Full tournament (2 weeks) |
| IEM Cologne | 1.5 | 82 | Full tournament |
| IEM Katowice | 1.5 | 80 | Full tournament |
| BLAST Premier World Final | 2 | 72 | Finals weekend |
| ESL Pro League (Playoffs) | 2 | 68 | Playoff stage only |
| BLAST Premier Spring/Fall | 2 | 65 | Finals weekend |
| ESL Pro League (Group stage) | 3 | 48 | Limited signal |
| Regional qualifiers | 4 | 25 | Qualification night only |

**CS2 Major note:** The two annual CS2 Majors are the highest-OrgTIS events in the entire
esports token ecosystem. A Major win generates the largest single-tournament token move
of any esports event. Treat CS2 Majors as equivalent to UCL Final in football terms.

### League of Legends

| Event | Tier | OrgTIS base | Signal window |
|---|---|---|---|
| Worlds (World Championship) | 1 | 92 | Full tournament (5 weeks, Oct-Nov) |
| Mid-Season Invitational (MSI) | 1.5 | 80 | Full tournament (3 weeks, May) |
| LEC / LCS Playoffs | 2 | 68 | Playoff series |
| LEC / LCS regular season | 3 | 45 | Win streaks only |
| EMEA Championship | 2 | 65 | Finals |

**LoL Worlds note:** The annual LoL World Championship is the highest-viewership event
in esports, consistently exceeding 70M peak concurrent viewers. For orgs with strong
LoL rosters (NAVI, G2, T1, etc.), Worlds is the annual apex event — equivalent to the
World Cup for national team tokens.

### Valorant

| Event | Tier | OrgTIS base | Signal window |
|---|---|---|---|
| VCT Champions | 1 | 85 | Full tournament (2–3 weeks, Aug-Sep) |
| VCT Masters | 1.5 | 75 | Full tournament |
| VCT EMEA / Americas League | 2 | 58 | Playoff stage |
| VCT regular season | 3 | 40 | Win streaks |

### Dota 2

| Event | Tier | OrgTIS base | Signal window |
|---|---|---|---|
| The International (TI) | 1 | 88 | Full tournament (Oct) |
| ESL One / Majors | 2 | 68 | Tournament run |
| DPC League (regular) | 3 | 42 | Limited |

### EA FC / FIFA Esports

| Event | Tier | OrgTIS base | Signal window |
|---|---|---|---|
| eChampions League | 2 | 60 | Tournament (football crossover audience) |
| ePremier League / eLa Liga | 2 | 55 | Tournament |
| FIFAe World Cup | 1.5 | 70 | Tournament |

---

## Patch Risk Score (PRS)

The patch risk variable is unique to esports — no equivalent exists in any other sport.
A patch update can make a team's strategy obsolete within 24 hours.

```
PRS = (
  days_since_last_patch     * 0.25 +  # recent patch = higher uncertainty
  patch_size_score          * 0.35 +  # major overhaul vs balance tweaks
  team_playstyle_exposure   * 0.25 +  # is this team's style patch-dependent?
  tournament_proximity      * 0.15    # patch dropped close to tournament?
) * 100
```

| PRS | Label | Agent action |
|---|---|---|
| 0–20 | Low | Normal OrgTIS confidence |
| 21–40 | Moderate | Apply 0.90× confidence multiplier to performance signals |
| 41–60 | Elevated | Apply 0.80× multiplier; avoid first-tournament-post-patch entry |
| 61–80 | High | Apply 0.70× multiplier; wait 1 tournament before entering |
| 81–100 | Critical | Performance signals unreliable; base on social/org strength only |

### Patch risk by game

Different games patch at different frequencies and severity:

| Game | Patch frequency | Typical impact | PRS consideration |
|---|---|---|---|
| CS2 | Monthly / as needed | Moderate — map rotations, gun tweaks | PRS usually 20–40 |
| League of Legends | Every 2 weeks | HIGH — champion balance changes strategy | PRS 30–60 regularly |
| Valorant | Every 2 weeks (agents) | Moderate-High — new agent = new meta | PRS 25–55 |
| Dota 2 | Irregular (major updates) | VERY HIGH when updated — sweeping changes | PRS 0–20 normally, 70+ on major update |

**Agent rule for patch proximity:** If a major patch dropped within 14 days of a
Tier 1 or 1.5 tournament, apply PRS confidence reduction regardless of team's historical
performance. Teams that historically adapt quickly earn a patch-resilience premium.

---

## Roster Stability Index (RSI)

RSI measures how stable an org's active roster is. Esports has the highest roster
turnover of any sport — the transfer window never truly closes.

```
RSI = (
  1 - roster_change_probability_90d    # lower change probability = higher stability
) × 100

Roster change probability inputs:
  Contract expiry within 3 months:    +35% probability
  Public player-org dispute signals:  +25% probability
  Team performance decline (3+ losses): +20% probability
  Rival org publicly interested:      +15% probability
  Head coach change:                  +20% probability
  Boot camp cancellation (rumoured):  +10% probability
```

| RSI | Label | Agent interpretation |
|---|---|---|
| 80–100 | Stable | Roster confirmed; performance signals reliable |
| 60–79 | Mostly stable | Minor change possible; moderate confidence |
| 40–59 | Unstable | Significant change likely; reduce position sizing |
| 20–39 | Highly unstable | Roster overhaul probable; base signals unreliable |
| 0–19 | Rebuilding | Treat as new org; historical performance irrelevant |

### RSI impact on OrgTIS

```
OrgTIS_adjusted = OrgTIS × (RSI / 100 × 0.30 + 0.70)

Simplified:
  RSI 80+:  OrgTIS × 1.00 (no adjustment)
  RSI 60:   OrgTIS × 0.94
  RSI 40:   OrgTIS × 0.88
  RSI 20:   OrgTIS × 0.82
  RSI 0:    OrgTIS × 0.76
```

---

## Multi-Game Calendar — October-November Stack Window

October–November is the peak season for multiple reasons simultaneously:
- LoL Worlds (October–November)
- CS2 Major (often October)
- Dota 2 The International (October)
- Valorant Champions (August–September, leading into this window)

When an org is actively competing in 2+ Tier 1 tournaments simultaneously,
the token OrgTIS compounds:

```
MULTI-GAME STACK BONUS:
  2 Tier 1 tournaments simultaneously: OrgTIS × 1.20
  3 Tier 1 tournaments simultaneously: OrgTIS × 1.35
  Advancing in all: compound per-advancement signal

Peak window: October 1 – November 15
  → Identify which orgs are active in multiple Tier 1 events
  → Scale in from October 1 if org is in 2+ Tier 1 events
  → Scale up on each advancement in each tournament
  → Exit after Worlds final (late November)
```

---

## Relegation Risk — Structural Token Event

Tier demotion (relegation from Tier 1 to Tier 2 in a game's circuit) is a
structural negative comparable to football relegation:

| Event | OrgTIS impact | Token impact |
|---|---|---|
| Relegated from LEC / LCS | Permanent GRM reduction for LoL | -15–30% |
| Dropped from VCT partnership | Cannot compete in Tier 1 Valorant | -12–25% |
| Failed to qualify for CS2 Major | Event-specific; not structural | -8–15% |
| Org disbanded a roster (game exit) | GRM for that game goes to zero | -10–20% |

**Key distinction:** Failing to *qualify* for a specific event is temporary.
Being *relegated* from a partnership league is a multi-season structural negative.
Always distinguish between the two.

---

## Star Player Transfer — Token Impact Matrix

| Transfer type | Source org token | Destination org token |
|---|---|---|
| Star player (top 5 global rating) departs | -12–25% | +10–20% |
| Full roster acquisition | -20–35% | +15–28% |
| Head coach departs | -8–15% | +5–12% |
| Roster lock-in (renewal confirmed) | +5–12% | N/A |
| Academy promotion (talent to main roster) | +3–8% | N/A |
| Stand-in player for tournament | -8–15% (uncertainty) | N/A |

---

## Active Esports Org Token Profiles

Approximate token ecosystem profiles for major orgs on Chiliz (Q1 2026):

| Org | Primary game(s) | Key market | CTI equivalent | Peak event |
|---|---|---|---|---|
| Natus Vincere (NAVI) | CS2 | Eastern Europe, Russia | 68–78 | CS2 Major |
| OG Esports | Dota 2, CS2 | Western Europe, global | 58–70 | The International |
| Team Vitality | CS2, LoL | France, Europe | 62–74 | CS2 Major, Worlds |
| Fnatic | CS2, LoL, Valorant | UK, global | 65–76 | CS2 Major, Worlds |
| G2 Esports | LoL, CS2, Valorant | Spain, Europe | 70–82 | Worlds, CS2 Major |
| Cloud9 | CS2, LoL, Valorant | USA | 60–72 | CS2 Major |

*Always verify against live Kayen token registry — org token availability changes.*

---

## Agent Reasoning Prompts

```
You are an esports fan token intelligence agent. Before evaluating any esports event:

1. IDENTIFY THE ACTIVE GRM DRIVER FIRST.
   Which game is currently driving the org's token?
   The org may have 5 rosters — only the one in the highest-tier active tournament matters.

2. CHECK PATCH RISK (PRS) BEFORE TRUSTING PERFORMANCE SIGNALS.
   If a major patch dropped within 14 days of the tournament, reduce confidence
   in historical performance data. Some teams adapt faster than others.

3. OCTOBER-NOVEMBER IS PEAK SEASON.
   Identify which orgs are competing in multiple Tier 1 tournaments simultaneously.
   Scale in from October 1 for multi-tournament orgs; scale up on each advancement.

4. CS2 MAJORS AND LoL WORLDS are the highest-OrgTIS events in the ecosystem.
   Treat them with the same weight as UCL Final (football) or PPV title fight (MMA).

5. STAND-IN PLAYER = IMMEDIATE RSI REASSESSMENT.
   An org fielding a stand-in for a Tier 1 event is the single most negative
   pre-tournament signal in esports. Apply full PRS confidence reduction.

6. RELEGATION IS STRUCTURAL, NOT TEMPORARY.
   A team failing to qualify for one event is an event-level negative.
   A team being relegated from a partnership league is a multi-season negative.
   Distinguish between the two before determining position response.

7. SOCIAL SIGNALS MOVE FASTER IN ESPORTS THAN ANY OTHER SPORT.
   Esports has the youngest, most digitally-native audience. Use -2h and -15m
   prematch windows; the -24h window is less predictive than in other sports.
```

---

## Data Sources

- Tournament brackets and results: HLTV (CS2), Liquipedia (all games), Riot Games circuit feeds
- Player ratings: HLTV player rankings, Liquipedia stats
- Viewership: Esports Charts (esportscharts.com)
- Patch notes: Official game developer changelogs
- Roster news: HLTV, Liquipedia, Twitter/X esports journalists
- Token data: Kayen/FanX API + Socios Connect (via fan-token-pulse)

---

## Compatibility

**Layer 1 companion:** `sports/esports`
**Required Layer 3:** `fan-token-pulse`
**Recommended:** `athlete-social-lift` (esports social moves fastest — high priority)
**Recommended:** `athlete/esports` (roster health and meta readiness)
**Recommended:** `transfer-intelligence` (roster transfer context)

---

*MIT License · SportMind · sportmind.dev*
