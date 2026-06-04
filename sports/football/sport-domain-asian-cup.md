---
name: sport-domain-asian-cup
description: >
  AFC Asian Cup reasoning framework. Structural differences from the World Cup.
  January–February timing (similar to AFCON) but affects different clubs.
  Documents Southeast Asian fan token market engagement and the lighter
  European club disruption compared to AFCON.
---

# AFC Asian Cup — Sport Domain Reasoning

**Structural differences from the World Cup framework. Load with:**
`sports/football/sport-domain-football-world-cup.md` (base tournament framework)

> Enduring reasoning framework. No specific player names or current standings.
> Applies to every future AFC Asian Cup edition.

---

## Domain Model

The AFC Asian Cup is the continental championship of the Asian Football Confederation.
It is played every four years, typically in January–February. Like AFCON, it disrupts
the European football season — but Asian internationals are less prevalent in European
Tier 1 clubs than African internationals, making the club disruption lighter.

Key distinctions:
- January–February timing — mid-European-season (similar to AFCON)
- 24-team format — larger field than previous editions
- Asian playing conditions: extreme heat possible in Gulf states hosts
- Southeast Asian fan token markets show elevated engagement during Asian Cup
- European club exposure is lighter than AFCON (fewer Asian starters in Tier 1)

---

## Event Playbooks

### Playbook 1: Asian Cup Match
```
trigger: Asian Cup match confirmed
entry:   T-48h with climate/altitude check
exit:    T+24h
filter:  climate_modifier (Gulf heat or extreme conditions); quality tier check
sizing:  signal × 1.00 base; Gulf host heat compounds significantly
note:    Broadcast reach: moderate (Asian + diaspora); lower than Euros/WC
```

### Playbook 2: European Club Match During Asian Cup Window
```
trigger: Fan token club match while Asian Cup is live (January–February)
entry:   T-48h with Asian-absence squad check
exit:    T+24h
filter:  asian_absence_check: which key players are at Asian Cup?
sizing:  Apply Asian Cup depth modifier (lighter than AFCON for most clubs)
```

### Playbook 3: Southeast Asian Fan Token Market Engagement
```
trigger: Asian Cup knockout rounds (significant SEA audience events)
entry:   Monitor regional fan token market signals during tournament
exit:    T+2 weeks post-tournament
filter:  Which fan tokens have significant SEA holder bases?
sizing:  Apply regional_engagement_modifier for relevant tokens
```

### Playbook 4: Asian Cup National Token (if applicable)
```
trigger: Asian national fan token with confirmed tournament participation
entry:   Apply national-team-tokens.md demand cycle
exit:    Exit decay curve on elimination
filter:  Check fantokens.com for active Asian national tokens
sizing:  Demand-only; Asian diaspora market reach
```

---

## Signal Weight Adjustments

| Factor | Asian Cup | AFCON | World Cup |
|---|---|---|---|
| European club disruption | LIGHTER | MAXIMUM | None |
| Asian fan token market engagement | HIGH | Moderate | Very high |
| Gulf host heat modifier | Extreme (if Gulf host) | Moderate | Varies |
| Broadcast reach | Moderate (Asian + diaspora) | Moderate (African) | Very high |
| Quality level | High (Japan, Korea, Iran, Australia) | High (Morocco, Senegal, Egypt) | Highest |
| Fan token club exposure | Lower than AFCON | Higher than Asian | N/A |

---

## European club disruption — lighter than AFCON

```
ASIAN INTERNATIONAL PRESENCE IN EUROPEAN CLUBS:

  Asian internationals play in European leagues but in smaller numbers
  than African internationals. The clubs most affected differ significantly.

  HIGHEST EXPOSURE (Asian international presence in European leagues):
    Japanese internationals: growing presence in Bundesliga, EPL, Serie A
    South Korean internationals: Premier League (Son Heung-min etc.), Bundesliga
    Australian internationals: EPL, Championship, other European leagues
    Iranian internationals: Some Bundesliga, Austrian Bundesliga presence

  CLUBS MOST LIKELY TO LOSE ASIAN PLAYERS:
    Smaller European clubs with specific Asian player concentrations
    EPL clubs (South Korean connections): Spurs primarily (historically)
    Bundesliga clubs with Japanese connections: several mid-table clubs

  ASIAN CUP DEPTH MODIFIER SCALE:
    Apply ×0.97 (not ×0.92) as the typical starting point.
    Asian internationals are generally fewer and lower in positional criticality
    at European Tier A clubs than African internationals.

    0 key players at Asian Cup: no modifier
    1 key player at Asian Cup:  ×0.97 per match in window
    2 key players at Asian Cup: ×0.94 per match in window
    3+ key players:             ×0.91 per match in window

  EXCEPTION — STAR PLAYER CASE:
    If the club's highest ATM player is at Asian Cup (e.g. team's #1 striker):
    Apply the standard ATM absent modifier from athlete-intel-football.md
    This overrides the generic Asian Cup depth modifier for that player.
```

---

## Gulf host climate modifier

```
GULF HOST CONDITIONS (when applicable):

  Asian Cup is sometimes hosted in Gulf states (Qatar, Saudi Arabia, UAE).
  Gulf conditions in January–February are moderate compared to summer —
  temperatures 20–28°C, no extreme heat issue for winter tournament.

  STANDARD GULF WINTER CONDITIONS:
    January in Gulf states: 18–28°C — COMFORTABLE for football
    No heat modifier required for January Gulf hosting
    Contrast: summer Gulf conditions (35–45°C) would require full heat modifier

  EXCEPTION — UNEXPECTED HEAT EVENT:
    If a specific match has confirmed temperatures >30°C: apply ×0.95 match 1
    This is unusual for January Gulf conditions but possible in some venues

  HUMIDITY MODIFIER (Gulf winter):
    Gulf humidity in January: 50–70% — moderate; no humidity modifier unless >75%

  NON-GULF HOSTS:
    Asian Cup has been hosted across Asia: Japan, South Korea, China, Qatar,
    Indonesia (proposed), India (proposed).
    For non-Gulf hosts: apply climate modifier based on host city conditions.
    January in East Asia (Japan, South Korea): cold; no heat issue; standard conditions.
```

---

## Southeast Asian fan token market engagement

```
SOUTHEAST ASIAN FAN TOKEN MARKET:

  Southeast Asia is a significant and growing fan token market.
  The Asian Cup drives engagement in SEA markets that have lower engagement
  at other times of the year.

  SEA MARKET CHARACTERISTICS:
    High mobile penetration; active crypto adoption in Vietnam, Thailand, Philippines
    Strong football fan culture (EPL particularly popular in SEA)
    Asian Cup participation of SEA nations drives local engagement
    $CHZ and fan tokens have real-world holder bases in this region

  ASIAN CUP ENGAGEMENT SIGNAL:
    When SEA nations (Vietnam, Thailand, Indonesia, Philippines, Malaysia)
    participate in the Asian Cup: regional engagement elevated.
    This correlates with broader fan token market volume spikes in the region.
    Apply: sea_engagement_modifier = ×1.03 to volume expectations during Asian Cup.

  FAN TOKEN CLUBS WITH SEA HOLDER PRESENCE:
    $BAR (Barcelona) — very large SEA following
    $ACM (AC Milan) — significant SEA following
    $JUV (Juventus) — SEA following
    Global fan token volume from SEA contributes meaningful aggregate.

  LOCAL TOKENS:
    Johor Darul Ta'zim ($JDT) is cited as an example of regional token activity.
    Monitor fantokens.com for any confirmed SEA club or national tokens.
    A Malaysian or Thai national token during Asian Cup = regional first-mover event.
```

---

## Agent Reasoning Prompts

```
ASIAN CUP-SPECIFIC QUESTIONS (supplement World Cup framework):

  1. What is the venue and is it a Gulf state host?
     → Check climate — Gulf in January is moderate (no heat modifier needed)
     → Non-Gulf Asian host: check climate zone; cold in East Asian January
  2. Is this a Tier 1 Asian nation (Japan, Korea, Iran, Australia) vs lower tier?
     → Apply quality tier check — significant variance in Asian Cup field
  3. Which fan token clubs lose key Asian players during this window?
     → Lighter disruption than AFCON; apply ×0.97 depth modifier
  4. Is a Southeast Asian nation in the tournament?
     → Apply sea_engagement_modifier = ×1.03 for regional fan token volume
  5. Is there a confirmed Asian national fan token?
     → Check fantokens.com — none confirmed as of library state
     → If launched: apply national-team-tokens.md immediately
  6. What is the broadcast reach for this match?
     → MODERATE (Asian + diaspora); not global scale of World Cup
```

---

## Key Commands

```
get_asian_cup_exposure(club_token)
  → Returns: Asian international players at Asian Cup, depth modifier

get_gulf_climate_modifier(venue_city, month)
  → Returns: climate modifier (typically none for January Gulf)

get_sea_engagement_signal(tournament_phase)
  → Returns: SEA market engagement level; applicable club tokens

check_asian_national_token(confederation)
  → Returns: confirmed active Asian national tokens (if any)
```

---

## Data Sources

```
AFC official (the-afc.com)       — Asian Cup fixtures, results, squads
Goal.com Asian edition           — Regional coverage
J-League official                — Japanese international updates
K League official                — South Korean international updates
fantokens.com                    — Asian national token launches
```

---

## Compatibility

**Base framework:** `sports/football/sport-domain-football-world-cup.md`
**AFCON comparison:** `sports/football/sport-domain-afcon.md`
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Asian Cup-specific signal intelligence: AFC qualification, host nation advantage, squad signals |
| Reasoning | ACTIVE | Asian Cup reasoning chain from squad composition and AFC context to outcome prediction |
| Context | ACTIVE | Asian Cup context: host nation advantage, Middle East tournaments, J.League and K-League player base |
| Memory | ACTIVE | Historical Asian Cup outcome patterns and host nation advantage data |
| Judgment | ACTIVE | Judgment on Asian Cup signal hierarchy — host nation advantage is significant |
| Attention | ACTIVE | Elevated attention for squad announcements and group stage draw |
| Communication | ACTIVE | Asian Cup signal output with host context, squad status, and direction |
| Verification | ACTIVE | Asian Cup data from AFC official sources |
| Learning | ACTIVE | Asian Cup modifier calibration from historical tournament outcome data |
| Integration | ACTIVE | Integrates with sport-domain-football.md and national team framework |
| Calibration | ACTIVE | Asian Cup modifiers calibrated against historical tournament data |
| Adaptation | ACTIVE | Asian Cup intelligence adapts as AFC tournament format evolves |
| Ethics | NOT APPLICABLE | Asian Cup sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Host nation context and squad source explicit in output |


---

*SportMind v3.97.24 · MIT License · sportmind.dev*
*Enduring framework — applies to every future AFC Asian Cup*
