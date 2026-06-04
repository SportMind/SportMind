---
name: sport-domain-euros
description: >
  UEFA European Championship reasoning framework. Documents structural differences
  from the World Cup framework (v3.97.18). Load alongside sport-domain-football-world-cup.md —
  do not re-read World Cup content, reference it. Covers format differences,
  club fan token impact, European host dynamics, and two-year cycle effects.
---

# UEFA European Championship — Sport Domain Reasoning

**Structural differences from the World Cup framework. Load with:**
`sports/football/sport-domain-football-world-cup.md` (base tournament framework)

> SportMind Library Rule: enduring reasoning framework. No specific player names,
> current standings, or expiring data. Applies to every future Euros edition.

---

## Domain Model

The UEFA European Championship is a 24-team tournament held every four years,
offset two years from the World Cup. It is the second-largest football tournament
by global viewership and the most significant for European fan token club demand.

Key distinctions from the World Cup framework:
- 24-team field (not 48) — fewer dead rubber matches proportionally
- European nations only (no confederation guests)
- Hosted within UEFA's jurisdiction — European crowd proximity for all teams
- Two-year cycle offset from World Cup — European clubs face two major
  international tournament signals per four-year period
- Most European-based players released after domestic season (June start)
  — less fatigued than AFCON window players

---

## Event Playbooks

### Playbook 1: Euros Group Stage Match
```
trigger: Euros group stage match confirmed
entry:   T-48h with dead rubber check
exit:    T+24h
filter:  dead_rubber_check (24-team format reduces dead rubbers vs WC)
sizing:  signal × 1.00 (group) — same framework as World Cup Playbook 1
note:    Refer to sport-domain-football-world-cup.md for dead rubber logic
```

### Playbook 2: Euros Knockout Match
```
trigger: Euros knockout match
entry:   T-48h
exit:    T+24h post-result
filter:  fatigue × bracket position × host proximity modifier
sizing:  signal × stage_weight (same scale as World Cup Playbook 2)
```

### Playbook 3: European Club Fan Token — Euros Impact
```
trigger: Key player from fan token club confirmed in national squad
entry:   Apply Euros_club_impact_modifier for tournament duration
exit:    Player returns to club pre-season (6-8 weeks post-tournament)
filter:  Is player a starter? Is club token PATH_2 active?
sizing:  See European club impact framework below
```

### Playbook 4: Euros Demand Cycle — National Token (if applicable)
```
trigger: European national fan token confirmed (none currently)
entry:   Apply national-team-tokens.md demand cycle framework
exit:    Exit decay curve on elimination
filter:  No confirmed European national tokens — monitor for launches
sizing:  Demand-only (no PATH_2 confirmed for any national token)
```

---

## Signal Weight Adjustments

Euros-specific adjustments relative to World Cup base framework:

| Factor | Euros | World Cup | Rationale |
|---|---|---|---|
| Rarity premium | Lower | Higher | Every 4 years vs every 4 years — but WC is global |
| Dead rubber frequency | Lower | Higher | 24-team format — fewer group surplus matches |
| Host proximity advantage | All European | CONCACAF-specific | All teams in European time zones |
| Time zone fatigue | Minimal for all | Significant for APAC/LATAM | European teams play in European time |
| Club token demand signal | HIGH | MODERATE | European clubs lose far more players to Euros |
| Repeat cycle | 2-year WC offset | 4-year standalone | Two major tournaments per cycle for European fans |

---

## Format differences from World Cup

```
24-TEAM FORMAT (vs 48-team World Cup):

  GROUP STAGE:
    6 groups of 4 teams (not 16 groups of 3)
    Top 2 from each group + 4 best third-placed teams = 16 advance
    Dead rubber calculation: different from WC — use standard 4-team group logic
    Simultaneous final round: yes (within each group, as standard)

  DEAD RUBBER NOTE:
    With 4-team groups, dead rubbers are LESS common than in 3-team WC groups.
    A team in 3rd place can still advance (as one of 4 best third-placed).
    Apply full dead rubber logic only when advancement is mathematically impossible.

  QUALIFICATION FORMAT:
    Groups of nations qualify through UEFA Nations League and playoffs.
    Seeding based on UEFA ranking coefficients — affects group draw signal.
    Host nation(s) automatically qualify — may affect draw dynamics.
```

---

## European host nation reasoning

```
HOST NATION — EUROS CONTEXT:

  Unlike the World Cup, which may be hosted far from most participants,
  Euros host nations are always within the European time zone.
  This reduces travel and time zone modifiers for all teams — including the host.

  HOST ADVANTAGE AT EUROS:
    Same mechanics as World Cup host_nation_modifier (×1.20)
    But the baseline is already elevated — all European teams have
    shorter travel than in a non-European World Cup
    Net additional advantage of being Euros host vs being Euros visitor:
    host_euros_differential = ×1.10 (vs ×1.20 for WC host where others travel far)

  PARTISAN CROWD PROXIMITY:
    Euros often feature several host cities — some may be geographically
    close to specific national fan bases even within the tournament.
    Teams playing "home-adjacent" venues (e.g. German team in Munich)
    receive partial home crowd modifier even as non-host.
    Apply: geographic_proximity_modifier = ×1.05 for teams in their
    home country's regional proximity when confirmed.
```

---

## Euros two-year cycle effect on fan tokens

```
TWO-YEAR CYCLE vs WORLD CUP:

  World Cup and Euros alternate every two years.
  European football seasons therefore face a major international tournament
  signal every two years — alternating between global (WC) and continental (Euros).

  CYCLE DEMAND COMPARISON:
    World Cup year:   global signal — national tokens from all regions affected
    Euros year:       European signal — European club tokens most affected

  EUROPEAN CLUB TOKEN EXPOSURE:
    At Euros, clubs like Arsenal, PSG, Barcelona, Juventus, Inter, City
    lose significant portions of their squads to national duty.
    This creates:
    1. Short-term club signal disruption (squad missing)
    2. National team performance signal overlay (player representing club's nation)
    3. Post-tournament sentiment: how did "our" players do?

  TOKENS DIRECTLY AFFECTED BY EUROS (through key players):
    $AFC  — England players | Arsenal players at Euros
    $SPURS — England players
    $CITY  — England, Germany, Portugal, Spain players at Euros
    $ACM   — Italy players at Euros
    $INTER — Italy players at Euros
    $JUV   — Italy players at Euros
    $PSG   — France players at Euros
    $BAR   — Spain players at Euros
    $ATM   — Spain players at Euros

  AGENT RULE:
    During Euros, European club tokens with major squad contributors at the
    tournament receive a dual signal:
    1. Club performance signal (diminished squad plays club fixtures — none at Euros;
       Euros happens after European domestic season concludes)
    2. National team narrative overlay: "$AFC players powering England to semis"
       or "PSG players eliminated early — sentiment drag"

  TIMING NOTE:
    Euros starts after European domestic seasons conclude (June).
    Club teams do not play competitive matches during Euros.
    There is NO club match CDI signal during Euros — only national team sentiment.
    Exception: FTP PATH_2 does not fire during Euros (no club competitive matches).
    Note for agents: do not expect PATH_2 events from June–July during Euros.
```

---

## No confirmed European national tokens

```
EUROPEAN NATIONAL TEAM TOKENS:

  As of the library's current knowledge state, no European national team
  has a confirmed active fan token on Chiliz or FanToken.com.

  DEMAND SIGNAL FOR EUROS:
    The Euros demand signal flows through CLUB tokens — not national tokens.
    Fans supporting England at Euros may buy $AFC or $SPURS.
    Fans supporting Spain may buy $BAR or $ATM.
    This is an INDIRECT demand pathway — club tokens proxy national sentiment.

  AGENT RULE:
    Do not look for European national tokens — they do not exist (currently).
    Instead: identify which club tokens have the highest national player
    concentration for each team still in the tournament.
    Apply national_sentiment_proxy_modifier = ×1.03 per knockout round
    advanced, for the club token most associated with the leading nation.

  IF EUROPEAN NATIONAL TOKENS LAUNCH:
    Apply national-team-tokens.md demand cycle framework immediately.
    Update this file with confirmed token and source.
```

---

## Key Commands

```
get_euros_club_exposure(club_token)
  → Returns: which national teams have significant representation from this club
  → Returns: tournament phase impact on club token sentiment

get_euros_dead_rubber_status(team, group_standings)
  → Returns: dead_rubber_type (full / partial / none)
  → Note: 4-team groups — third-place teams may still advance

get_euros_host_modifier(team, venue_city)
  → Returns: host or geographic proximity modifier

get_euros_club_token_overlay(national_team, tournament_round)
  → Returns: which club tokens carry the national sentiment proxy signal
```

---

## Agent Reasoning Prompts

```
EUROS-SPECIFIC QUESTIONS (supplement World Cup framework):

  1. Is this competition using the 4-team group format?
     → Apply 4-team dead rubber logic (third-place teams can advance)
  2. What domestic season phase is this? Are club seasons over?
     → Euros starts post-season: no club fixtures, no PATH_2 during Euros
  3. Which club tokens carry the national team sentiment proxy?
     → Identify 2-3 club tokens most associated with each active nation
  4. Are we in a World Cup year or Euros year?
     → Determines which signal is primary: global (WC) or European (Euros)
  5. Is a European national token confirmed?
     → Currently no — route signal through club token proxies
```

---

## Data Sources

```
UEFA official (uefa.com)     — squads, results, draw, format
Transfermarkt.com            — squad nationality data by club
Sofascore / WhoScored        — real-time match intelligence
National federation sites    — injury and availability
Fan token monitoring:
  fantokens.com              — check for European national token launches
  chiliz.com official        — partnership announcements
```

---

## Compatibility

**Base framework:** `sports/football/sport-domain-football-world-cup.md`
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`
**Club tokens:** `fan-token/league-football-token-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | UEFA Euros-specific signal intelligence: tournament structure, host nation, and squad signals |
| Reasoning | ACTIVE | Euros reasoning chain from squad composition and tournament stage to outcome prediction |
| Context | ACTIVE | Euros context: 24-team format, host nation advantage, fatigue after club season |
| Memory | ACTIVE | Historical Euros outcome patterns and tournament stage data |
| Judgment | ACTIVE | Judgment on Euros signal hierarchy — squad form and physical freshness are primary |
| Attention | ACTIVE | Elevated attention for squad news, injury updates, and key group stage fixtures |
| Communication | ACTIVE | Euros signal output with tournament stage modifier, squad context, and direction |
| Verification | ACTIVE | Euros data from UEFA official sources |
| Learning | ACTIVE | Euros modifier calibration from historical tournament outcome data |
| Integration | ACTIVE | Integrates with sport-domain-football.md and national team framework |
| Calibration | ACTIVE | Euros modifiers calibrated against historical tournament stage outcome data |
| Adaptation | ACTIVE | Euros intelligence adapts as UEFA format and tournament structure evolve |
| Ethics | NOT APPLICABLE | Euros sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Tournament stage context and squad source explicit in output |


---

*SportMind v3.97.24 · MIT License · sportmind.dev*
*Enduring framework — applies to every future UEFA European Championship*
