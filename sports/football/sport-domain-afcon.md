---
name: sport-domain-afcon
description: >
  Africa Cup of Nations (AFCON) reasoning framework — HIGHEST PRIORITY regional
  tournament file. January timing disrupts European club season at its peak.
  Documents which fan token clubs are exposed, squad depth modifiers, and the
  predictable cyclical impact on club CDI signals.
---

# Africa Cup of Nations (AFCON) — Sport Domain Reasoning

**HIGHEST PRIORITY regional tournament file. January timing is the defining
structural characteristic — it disrupts European club seasons at their peak.**

Load with: `sports/football/sport-domain-football-world-cup.md` (base framework)

> Enduring reasoning framework. No specific player names or current standings.
> Applies to every future AFCON edition (biennial — every two years, January).

---

## Domain Model

AFCON is the African continental championship organised by the Confederation
of African Football (CAF). Unlike all other major international tournaments,
AFCON is played in January–February — in the middle of the European football season.

This is the defining structural difference from every other tournament in the library:
- **European clubs lose African international players mid-season**
- Affected clubs must play competitive league and cup matches without key players
- The disruption window is 4–6 weeks
- This is predictable, cyclical, and patterned — agents can pre-flag affected clubs

---

## Event Playbooks

### Playbook 1: AFCON Match
```
trigger: AFCON match confirmed (note: January — European season is live)
entry:   T-48h with squad confirmation
exit:    T+24h
filter:  Standard WC group stage logic; altitude/climate check for host country
sizing:  signal × 1.00 (standard); host nation modifier applies
note:    AFCON matches have limited global broadcast reach — apply
         broadcast_reach_modifier = 0.75 vs European Tier 1 equivalent
```

### Playbook 2: European Club Match During AFCON Window
```
trigger: Fan token club match while AFCON is live (January–February)
entry:   T-48h with AFCON-absence squad check
exit:    T+24h
filter:  afcon_absence_check: which key players are at AFCON?
sizing:  Apply AFCON squad depth modifier (see below)
note:    This is the PRIMARY signal for fan token CDI during AFCON
         Most of the AFCON signal flows through club tokens, not national tokens
```

### Playbook 3: Club Fan Token — AFCON Exposure Assessment
```
trigger: Start of AFCON window (pre-tournament)
entry:   Assess which clubs lose key African players
exit:    Player return — typically 2 matches after AFCON conclusion
filter:  Count African international starters per club; assess position criticality
sizing:  Apply appropriate AFCON depth modifier (see framework below)
```

### Playbook 4: AFCON National Token Signal (if applicable)
```
trigger: African national fan token confirmed (none currently)
entry:   Apply national-team-tokens.md demand cycle
exit:    Exit decay curve on elimination
filter:  No confirmed African national tokens — monitor for launches
sizing:  Demand-only signals; broadcast reach moderate (African + diaspora market)
```

---

## Signal Weight Adjustments

| Factor | AFCON | World Cup | Rationale |
|---|---|---|---|
| European club disruption | MAXIMUM | None (post-season) | Mid-season timing = clubs lose players NOW |
| Fan token primary signal | CLUB tokens | National tokens | Signal flows through $AFC, $PSG etc. |
| Broadcast reach | Moderate (regional) | Very high (global) | AFCON has African + diaspora coverage |
| Predictability | VERY HIGH | High | Biennial, always January — pre-plan |
| National token availability | None confirmed | Some | No active African national tokens |
| Climate at host venue | Tropical/subtropical | Varies | African hosts often high heat/humidity |

---

## European club exposure — which clubs are affected

```
IDENTIFYING AFCON-EXPOSED CLUBS:

  HIGHEST EXPOSURE (consistent African international presence):
    Premier League clubs: historically lose most players to AFCON
      Arsenal: has had Ivorian, Ghanaian, Nigerian, Egyptian players at AFCON
      Chelsea, Liverpool, Arsenal, Man City: regular AFCON contributors
    Ligue 1 clubs: France has large African diaspora player base
      PSG, Lyon, Marseille, Monaco: regular AFCON contributors
    Other leagues: Bundesliga, Serie A — fewer but notable African internationals

  MEDIUM EXPOSURE:
    Spanish La Liga: some African internationals; typically fewer than EPL/Ligue 1
    Italian Serie A: growing African international presence
    Portuguese Liga: significant African diaspora; key for Cape Verde, Angola

  LOW EXPOSURE:
    Bundesliga: fewer African internationals than EPL or Ligue 1
    Netherlands, Belgium: moderate exposure

  HOW TO ASSESS EXPOSURE FOR A SPECIFIC CLUB:
    1. Identify starting XI players with African international eligibility
    2. Confirm AFCON squad selection (T-4 weeks from AFCON start)
    3. Count confirmed absent players and their positional criticality
    4. Apply appropriate AFCON depth modifier
```

---

## AFCON squad depth modifier framework

```
AFCON DEPTH MODIFIER — FAN TOKEN CLUBS:

  The AFCON modifier is the key CDI adjustment for European club tokens
  during the AFCON window. It applies to club competitive matches, not AFCON matches.

  MODIFIER TABLE:
    0 key players at AFCON:              no modifier (×1.00)
    1 key player at AFCON:               ×0.96 per match in AFCON window
    2 key players at AFCON:              ×0.92 per match in AFCON window
    3+ key players at AFCON:             ×0.88 per match in AFCON window
    Star player (team's highest ATM) at AFCON: apply ATM absent modifier additionally

  DEFINITION OF "KEY PLAYER":
    Regularly starts (>60% of matches)
    Positionally important (not a squad player)
    The club would need to adjust their system without them

  POSITION CRITICALITY AMPLIFICATION:
    Goalkeeper at AFCON: club must use backup GK — apply additional ×0.96
    Defensive partnership broken (both CBs): additional ×0.94
    Central midfielder or playmaker: additional ×0.97
    Striker (if only one regular striker): additional ×0.96

  FTP PATH_2 INTERACTION:
    If a PATH_2 club (e.g. $AFC Arsenal) loses key players to AFCON:
      Apply AFCON depth modifier to the PATH_2 WIN probability calculation
      Fewer key players = lower win probability = lower expected PATH_2 burn
      Do not suppress PATH_2 — adjust the win probability input, not the mechanic

  RETURN TIMELINE:
    Player typically returns 1–2 weeks after AFCON conclusion
    First 2 matches post-return: apply return_acclimatisation_modifier = ×0.97
    (fitness reconditioning after 4-6 week tournament)
    After match 3: remove return modifier; assume full fitness
```

---

## AFCON cyclical pre-flagging

```
AFCON PREDICTABILITY — AGENT PRE-PLANNING:

  AFCON is uniquely predictable among all international tournaments:
    Fixed timing: January–February (biennial)
    Fixed affected leagues: EPL, Ligue 1, and others consistently lose players
    Known exposure: African international presence is a stable club characteristic

  PRE-TOURNAMENT PROTOCOL (T-4 weeks):
    1. Identify which fan token clubs have key African internationals
    2. Monitor squad announcement (typically 3-4 weeks before AFCON)
    3. Once squad confirmed: lock in AFCON depth modifier for club CDI
    4. Flag: which club matches fall during AFCON window?
    5. Apply modifier to all club matches during 4–6 week AFCON window

  BIENNIAL CYCLE:
    Agents should maintain a "AFCON exposure register" for each fan token club —
    which clubs historically lose key players, and for which competitions.
    This register is largely stable from tournament to tournament (player eligibility
    changes slowly; national associations are consistent).

  WHEN AFCON IS NOT IN PROGRESS:
    Remove all AFCON modifiers.
    Return player ATM to baseline.
    No AFCON signal in non-AFCON years.
```

---

## No confirmed African national tokens

```
AFRICAN NATIONAL TEAM TOKENS:

  As of the library's current knowledge state, no African national team
  has a confirmed active fan token on Chiliz or FanToken.com.

  WHERE THE AFCON SIGNAL FLOWS:
    AFCON demand flows through EUROPEAN CLUB tokens as proxies.
    Fans of Senegal, Nigeria, Ivory Coast, Morocco, Egypt etc. support those
    nations — but access fan tokens through their clubs (Arsenal, PSG, etc.)
    
  IF AFRICAN NATIONAL TOKENS LAUNCH:
    Apply national-team-tokens.md demand cycle immediately.
    African national token launch during AFCON = maximum first-mover event.
    Apply ×1.40 first-mover CDI modifier (largest unserved African market).
    Morocco, Egypt, Nigeria, Senegal are highest-probability first launchers
    given their fan bases and diaspora commercial networks.
```

---

## Agent Reasoning Prompts

```
AFCON-SPECIFIC QUESTIONS — MANDATORY PRE-MATCH CHECKS:

  FOR AFCON MATCHES:
  1. Which nation is this and what is the climate zone at the host venue?
     → Apply heat/humidity modifier if tropical conditions confirmed
  2. What is the quality tier of each nation?
     → Significant variance in AFCON field — check CAF ranking
  3. Is any active fan token club's key player involved in this AFCON match?
     → No direct CDI signal — route through club token absence framework

  FOR EUROPEAN CLUB MATCHES DURING AFCON WINDOW (PRIMARY USE):
  1. Which key players from this club are at AFCON?
     → Check squad announcement (T-4 weeks from AFCON start)
  2. How many key players absent, and what positions?
     → Apply AFCON depth modifier table (1 player: ×0.96, 2: ×0.92, 3+: ×0.88)
  3. Is this club's PATH_2 token active?
     → Adjust win probability input for PATH_2 burn calculation
     → Do not suppress PATH_2 — adjust the probability, not the mechanic
  4. When do the players return?
     → Typically 1-2 weeks post-AFCON; apply ×0.97 for first 2 matches back
  5. Is this AFCON year predictable for next season pre-planning?
     → YES — biennial, January, same leagues affected; pre-flag early
```

---

## Key Commands

```
get_afcon_exposure(club_token)
  → Returns: count of key players at AFCON, positions, depth modifier to apply

get_afcon_depth_modifier(key_players_absent, position_criticality)
  → Returns: depth modifier value for this club's AFCON window

get_afcon_path2_adjustment(club_token, win_probability)
  → Returns: AFCON-adjusted win probability for PATH_2 burn calculation

afcon_return_timeline(player, afcon_exit_date)
  → Returns: estimated return date, matches before full fitness assumed
```

---

## Data Sources

```
CAF official (cafonline.com)     — AFCON fixtures, results, squads
BBC Sport Africa                 — English-language coverage
Goal.com Africa edition          — Squad news, results
Club official channels           — Player release and return confirmation
Transfermarkt.com                — African international profiles per club
```

---

## Compatibility

**Base framework:** `sports/football/sport-domain-football-world-cup.md`
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`
**Club CDI:** `fan-token/league-football-token-intelligence.md`

---

*SportMind v3.97.24 · MIT License · sportmind.dev*
*Enduring framework — applies to every future AFCON edition (biennial, January)*
*HIGHEST PRIORITY regional tournament file — January timing disrupts European club season*
