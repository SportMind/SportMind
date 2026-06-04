# World Cup — Football Sport Domain Reasoning Framework

**Enduring reasoning framework for AI agents analysing World Cup matches.
Not specific to any edition — applicable to every future World Cup.
Load alongside `sports/football/sport-domain-football.md` for tournament context.**

> SportMind Library Rule check: every element in this file is true and
> useful beyond six months. No specific dates, named players, current prices,
> or expiring operational data. This file teaches agents how to think
> about World Cup football — not what is true right now.

---

## Domain Model

The World Cup is a single-elimination tournament following a group stage,
played every four years between national teams. The 48-team format (current
and future editions) uses 16 groups of three teams, with the top two from
each group advancing to a 32-team knockout bracket.

Key domain distinctions from club football:
- National team form diverges from club form (separate reasoning required)
- No FTP PATH_2 supply mechanics for national team matches (club token only)
- Tournament fatigue compounds across 4–7 matches over 4–6 weeks
- Dead rubber matches are structurally more common in 3-team groups
- Host continent advantage creates measurable performance modifiers

---

## Event Playbooks

### Playbook 1: Group Stage Match
```
trigger: World Cup group stage match confirmed
entry:   T-48h (with squad and dead rubber assessment)
exit:    T+24h post match
filter:  dead_rubber_check first; goal_difference_check; travel_modifier_check
sizing:  signal × stage_weight (1.00 for group stage)
```

### Playbook 2: Knockout Round Match
```
trigger: World Cup knockout match (R32 through Final)
entry:   T-48h (with accumulated fatigue and rest assessment)
exit:    T+24h post match (or post-penalties if applicable)
filter:  fatigue_modifier × bracket_position × previous_round_ET_check
sizing:  signal × stage_weight (1.15–1.50 depending on round)
```

### Playbook 3: Dead Rubber Detection
```
trigger: Group stage match where tournament positions may already be decided
entry:   Simulation run before any signal generation
exit:    Dead rubber modifier applied throughout; never removed mid-match
filter:  goal_difference_override_check (GD in play = not dead rubber)
sizing:  signal × 0.55 (full) or × 0.75 (partial); FTP still fires
```

### Playbook 4: National Team Token Tournament Signal
```
trigger: National team fan token with confirmed tournament participation
entry:   Phase-appropriate (see fan-token/national-team-tokens.md)
exit:    Exit decay curve applied immediately on elimination
filter:  qualification confirmed; active token confirmed; PATH_2 = NO
sizing:  demand-only signal; scale with round and underdog premium
```

---

## Tournament structure reasoning

### 48-team format and dead rubber identification

```
48-TEAM FORMAT SIGNAL IMPLICATIONS:

  The 48-team World Cup uses a group stage of 16 groups of three teams.
  Each team plays two group-stage matches. The top two from each group advance.
  One match per group is played simultaneously in the final group round.

  DEAD RUBBER IDENTIFICATION FRAMEWORK:

  A dead rubber occurs when one or more teams in a group has no possibility
  of advancing or has already secured advancement before their final match.

  Dead rubber signals to check before any group-stage match:
    1. Can the team mathematically qualify regardless of this result?
       → If YES for both teams: both may rotate — reduce signal weight
    2. Can the team mathematically be eliminated regardless of this result?
       → If YES for both teams: motivation signal severely reduced
    3. Is one team already through and one team already out?
       → Extreme dead rubber — maximum signal reduction
    4. Does one team need a specific result (not just a win)?
       → Goal difference scenarios remain high motivation

  DEAD RUBBER MODIFIER:
    Full dead rubber (both teams' fates decided): signal_weight × 0.55
    Partial dead rubber (one team's fate decided): signal_weight × 0.75
    Standard group match (both teams' fates open): signal_weight × 1.00

  EXCEPTION — FTP PATH_2:
    A dead rubber match still triggers PATH_2 supply mechanics for any
    Fan Token club involved, if the match qualifies under FTP scope
    (official men's competitive — international tournaments qualify).
    Dead rubber ≠ no supply event. The supply mechanics fire regardless
    of motivational context. Never suppress FTP signals for dead rubbers.

  EXCEPTION — REPUTATION MATCHES:
    Some dead rubbers have reputational stakes (e.g. a nation playing
    their last-ever World Cup match, or a manager's final game). These
    generate media signals that partially offset the dead rubber reduction.
    Apply reduced dead rubber modifier (×0.80) rather than full (×0.55).
```

### Three-team simultaneous final round reasoning

```
THREE-TEAM GROUP — SIMULTANEOUS FINAL ROUND:

  The 48-team format's final group round plays both remaining matches
  simultaneously. This creates specific signal dynamics:

  WHY SIMULTANEITY MATTERS:
    Teams cannot adjust their strategy based on the other match's live result.
    Pre-match signals are based on what each team needs — but actual
    behaviour may shift intra-match as score updates arrive via sideline staff.
    
  SIGNAL IMPLICATIONS:
    1. Pre-match motivation signals are cleaner (no inter-match dependency)
    2. Intra-match momentum signals are less reliable (teams may shift
       formation or intensity in response to other match scores)
    3. Post-match signal: always check BOTH matches before interpreting result

  GOAL DIFFERENCE SCENARIOS:
    In tight three-team groups, goal difference can determine progression.
    If goal difference is in play: dead rubber logic is suspended — both
    teams remain highly motivated even if win/loss outcome is irrelevant.
    A team that needs to win by three goals plays differently to a team
    that only needs a draw. Identify goal difference scenarios explicitly.

  AGENT RULE:
    Before any final group-stage match, check:
      (a) What does each team need to advance?
      (b) Does goal difference apply?
      (c) What is happening in the simultaneous match?
    Only then apply motivation signal weights.
```

### Knockout bracket positioning

```
KNOCKOUT BRACKET POSITIONING REASONING:

  World Cup draw position determines the path to the final.
  Path difficulty varies significantly by bracket half.

  SIGNAL IMPLICATIONS BY ROUND:
    Round of 32 (last 32):   Standard knockout signal — winner advances
    Round of 16 (last 16):   Signal elevated — single elimination, no second chance
    Quarter-final:            High signal — top-8 status at stake
    Semi-final:               Maximum pre-final signal
    Third-place play-off:     Reduced signal — motivation frequently questioned
    Final:                    Maximum signal of the tournament

  BRACKET HALF ANALYSIS:
    Agents should identify which bracket half a team is in and whether
    they face a path of stronger or weaker opponents.
    Favourable bracket half → demand trajectory elevated for associated tokens
    Difficult bracket half → demand trajectory compressed (earlier exit risk)

  PATH DIFFICULTY MODIFIER:
    Favourable half (weaker projected opponents): demand_multiplier × 1.15
    Standard half: demand_multiplier × 1.00
    Difficult half (stronger projected opponents): demand_multiplier × 0.90

  THIRD-PLACE PLAY-OFF:
    Treat as a partial dead rubber unless specific factors apply:
    - Home nation in play-off (elevated crowd motivation)
    - Individual player milestone at stake (golden boot, caps record)
    Apply signal_weight × 0.70 for standard third-place play-off.
    Third-place play-off DOES trigger FTP supply mechanics — not exempt.
```

### Extra time and penalty reasoning

```
EXTRA TIME AND PENALTY PROBABILITY:

  Knockout matches may extend to extra time (30 minutes) and penalties.
  This affects pre-match signal confidence and FTP timing.

  SHOOTOUT PROBABILITY CONTEXT:
    Historically, approximately 20–25% of knockout matches go to extra time.
    Of those, approximately 50–60% reach a penalty shootout.
    Base probability of a knockout match reaching penalties: ~10–15%.

  SIGNAL IMPLICATIONS:
    Pre-match: reduced directional confidence for closely matched teams
    Apply: direction_confidence_reduction = 0.85 for evenly matched knockout ties
    
    Extra time / penalties are unpredictable at signal level — do not attempt
    to predict shootout outcomes beyond historical baseline (coin-flip territory).
    
    POST-EXTRA-TIME FTP:
    FTP supply event timing: if a match goes to extra time, the result
    confirmation is delayed by 30+ minutes. Buyback/burn execution window
    (≤48h post-result) is unaffected but begins later.
    If penalties decide the winner: the result is the penalty shootout outcome
    — not the 90-minute or 120-minute score. Confirm which result triggers FTP.
    
  AGENT RULE:
    For evenly matched knockout ties: apply confidence_haircut = 0.85.
    Never attempt to predict penalty shootout outcome directionally.
    Flag "extra time possible" in pre-match signal notes.
```

---

## Host nation reasoning

### Home continent advantage modifier

```
HOME CONTINENT ADVANTAGE — WORLD CUP:

  Teams playing a World Cup in their own confederation have measurable
  advantages beyond standard home advantage:

  FACTORS:
    Crowd familiarity: local fans, familiar stadium atmospheres
    Travel distance: no long-haul travel, same time zone
    Climate familiarity: teams practise year-round in similar conditions
    Food, culture, language: team support staff operates in home conditions
    Media and psychological environment: home country media narrative

  MODIFIER FRAMEWORK:
    Host nation (playing in their own country): home_modifier × 1.20
    Same confederation (e.g. CONCACAF team in CONCACAF-hosted tournament):
      confederation_modifier × 1.10
    Adjacent confederation (e.g. European team in US, short travel):
      proximity_modifier × 1.05
    Intercontinental travel (e.g. Asian team travelling to Americas):
      travel_penalty × 0.92 (first 1–2 matches only, until acclimatised)

  EXCEPTION:
    These modifiers apply at match level, not at campaign level.
    A team still needs quality to advance — the modifier represents
    a marginal structural advantage, not a performance guarantee.
```

### Neutral venue modifier

```
NEUTRAL VENUE AND TRAVEL FATIGUE:

  A World Cup hosted in a region foreign to most participants creates
  compounded fatigue signals for travelling teams.

  INTERCONTINENTAL TRAVEL SIGNALS:
    Flight distance > 8,000km → apply travel_fatigue_modifier = 0.92
      (first match only — teams typically arrive 7–10 days early)
    Multiple long-haul group stage trips → acclimatisation disrupted
    
  CLIMATE ZONE MISMATCH:
    Teams moving between climatic zones face performance risk in first match:
      Temperate → tropical heat: heat_acclimatisation_modifier = 0.90 (match 1)
      Cold climate → high humidity: humidity_modifier = 0.92 (match 1)
      After match 1: assume acclimatisation complete, return to baseline

  ALTITUDE:
    Matches played at altitude (>1,500m above sea level) affect aerobic capacity.
    Low-altitude teams playing at altitude: altitude_modifier = 0.88 (match 1)
    High-altitude national teams (e.g. Bolivia, Peru) at altitude: no modifier
    Note: all World Cup venues should be checked for altitude before signal generation.

  AGENT RULE:
    Check travel origin → venue city → climate zone before every match.
    Apply modifiers to match 1 only unless evidence suggests ongoing adjustment.
    After match 2: remove travel/climate modifiers unless ongoing evidence.
```

### Time zone fatigue modifier

```
TIME ZONE DISRUPTION — WORLD CUP:

  Teams travelling across multiple time zones face disruption to sleep
  patterns, training schedules, and match-day readiness.

  TIME ZONE MODIFIER TABLE:
    0–2 hours difference:   No modifier — within adaptation threshold
    3–5 hours difference:   time_zone_modifier = 0.96 (match 1)
    6–8 hours difference:   time_zone_modifier = 0.92 (matches 1–2)
    9+ hours difference:    time_zone_modifier = 0.88 (matches 1–2)

  HIGH-RISK COMBINATIONS:
    European team playing in Americas (6–9h difference): apply ×0.92–0.88
    Asian team playing in Americas (12–15h difference): apply ×0.88
    These teams face maximum time zone disruption in early group stage.

  MITIGATION SIGNALS:
    Long pre-tournament camp in destination time zone: reduce modifier by half
    Late kick-off times (22:00+ local): partial mitigation for jet-lagged teams
    Check: did the team arrive early? → key signal that mitigates time zone risk

  AGENT RULE:
    Identify each team's home time zone and the venue time zone before match 1.
    Apply modifier to match 1 (and match 2 for 9+ hour differences).
    After 10+ days in destination: assume adaptation, remove modifier.
```

---

## Tournament fatigue reasoning

### Match cadence modelling

```
WORLD CUP MATCH CADENCE VERSUS CLUB FOOTBALL:

  World Cup group stage: matches every 4–7 days
  World Cup knockout stage: matches every 4–5 days with travel between venues
  Club football (EPL): matches every 3–4 days in busy periods
  
  NET EFFECT: World Cup cadence is similar to club congested periods
  BUT with significantly more travel, higher intensity, and no rotation
  of player depth (squads of 26, but star players rarely rested).

  ACCUMULATED FATIGUE FRAMEWORK:
    Match 1 (group): fresh — no modifier
    Match 2 (group): mild fatigue — apply fatigue_modifier = 0.97
    Match 3 (group): moderate fatigue — apply fatigue_modifier = 0.94
    Round of 16:     fatigue from 3 group matches + travel — ×0.92
    Quarter-final:   accumulated fatigue — ×0.90
    Semi-final:      peak fatigue window — ×0.88
    Final:           rest period often longer (3–4 days) — ×0.93

  FATIGUE SIGNAL INTERACTIONS:
    Teams that played extra time in previous round: apply additional ×0.95
    Teams that played penalties: apply additional ×0.97 (psychological cost)
    Teams with 4+ day rest before match: remove one fatigue layer

  AGENT RULE:
    Track matches played per team through the tournament.
    Apply cumulative fatigue modifier for knockout rounds.
    Adjust when rest period is confirmed longer than standard.
```

### Squad rotation signals

```
SQUAD ROTATION AS A SIGNAL:

  Managers who rotate heavily in the group stage preserve fresher squads
  for the knockout rounds. This creates a distinct signal:

  ROTATION SIGNAL IDENTIFICATION:
    Indicators of heavy rotation:
      Named lineup shows 4+ changes from previous match
      Key players rested (goal-scorer, playmaker, #1 goalkeeper)
      Tactical experiment evident (different formation)
    
    Indicators of minimal rotation:
      Same XI as previous match
      Only injury/suspension-forced changes
      High-intensity pressing system maintained

  SIGNAL IMPLICATIONS:
    Heavy group-stage rotators → enter knockouts fresher
      Apply knockout_freshness_modifier = ×1.05 for heavily rotated team
    Minimal group-stage rotators → may be fatigued entering knockouts
      No additional modifier — fatigue framework already captures this

  CAVEAT:
    Rotation only benefits if the rotated players are genuine quality
    alternatives. Squads with thin depth cannot rotate without losing quality.
    Check squad depth profile alongside rotation signal.

  DEAD RUBBER ROTATION:
    Teams that secured qualification early frequently rotate for the dead rubber
    group match. This is predictable — apply motivation_modifier reduction AND
    expect rotation to increase.
    FTP reminder: PATH_2 still fires on the rotated team's result.
```

### Climate acclimatisation

```
CLIMATE ACCLIMATISATION — TOURNAMENT CONTEXT:

  See also: Neutral venue modifier (above) for per-match application.

  TOURNAMENT-LEVEL IMPLICATIONS:
    A team that acclimatises poorly in match 1 but adapts by match 2
    enters the knockout rounds at full capacity — do not carry climate
    modifiers beyond the acclimatisation window.

  COMPOUND EFFECTS:
    Team from temperate climate → playing in heat AND at altitude:
      Apply BOTH heat and altitude modifiers to match 1 (×0.90 × 0.88 = ×0.79)
      This is a significant compound signal — flag prominently.

  PRE-TOURNAMENT CAMP SIGNAL:
    Teams that hold pre-tournament camp in a climate-similar environment
    to the host city are explicitly reducing their acclimatisation risk.
    This is a Tier 2 signal worth monitoring — it indicates coaching staff
    awareness and proactive preparation.
```

---

## National team versus club reasoning

### Why national team form diverges from club form

```
NATIONAL TEAM FORM VERSUS CLUB FORM — DIVERGENCE FRAMEWORK:

  National team form and club form are frequently uncorrelated.
  Agents should never directly port club-level ATM modifiers to national team.

  REASONS FOR DIVERGENCE:

  1. TACTICAL SYSTEM:
     A player dominant in their club's system may be used differently
     by the national team manager. Midfield playmaker at club →
     defensive midfielder for national team = different performance context.

  2. PARTNERSHIP CHEMISTRY:
     Club players train with their team-mates daily. National players
     meet for 10–14 days before a tournament. New partnerships take time.
     First tournament match often sees lower chemistry than later rounds.

  3. MOTIVATION CALIBRATION:
     Some players raise their level for international duty (particularly
     players from nations with strong football identity). Others underperform
     due to pressure or fatigue from club season.

  4. PHYSICAL CONDITION:
     End-of-season tournaments (World Cup in June–July): some players arrive
     fatigued from long club seasons. Others arrive fresh if their club
     exited competitions early.

  NATIONAL TEAM ATM MODIFIER RULE:
    Do not use club ATM modifier directly for national team signal.
    Apply independent assessment based on:
      (a) Player's current role in the national team system
      (b) Recent international form (last 3–5 international matches)
      (c) End-of-season fatigue status
      (d) Whether the manager typically uses this player as a starter

  WORLD CUP YEAR CLUB IMPACT:
    Players who go deep in the World Cup (semi-final, final) may return
    to clubs 6–8 weeks later than non-tournament players.
    This creates a delayed start to the following club season — relevant
    for fan token athlete modifiers in August/September post-World Cup.
    Apply post_world_cup_delay_modifier = ×0.92 for the first 3–4 club
    matches after a player returns from deep tournament run.
```

### International break disruption signal

```
INTERNATIONAL BREAK DISRUPTION — WORLD CUP PREPARATION:

  The World Cup requires a 6–8 week break from domestic leagues.
  Pre-tournament preparation camps run 2–4 weeks before the tournament.

  CLUB FORM DISRUPTION SIGNALS:
    Final club matches before World Cup break: players may be managed (rested)
    by club managers to ensure tournament fitness — reduce club ATM temporarily.
    
    Post-World Cup return: players return at different fitness levels.
      Semi-finalists/finalists: typically 4–6 weeks behind standard pre-season
      Early exits (group stage): closer to standard pre-season timeline
    
  FAN TOKEN CLUB IMPLICATIONS:
    Clubs that lose many players to deep tournament runs face a delayed
    return to form in the first 6–8 weeks of the following season.
    Apply squad_disruption_modifier for clubs losing 5+ players to deep runs:
      5–7 players lost to QF+: modifier = ×0.94 for first 4 club matches
      8+ players lost to SF+:  modifier = ×0.90 for first 6 club matches

  WORLD CUP YEAR SUSPENSION FROM CLUB SIGNAL:
    During the World Cup itself (6–8 weeks), club token CDI signals shift
    to tournament mode. Club match results are irrelevant — the tournament
    performance of the club's national team players is the primary signal.
    Load `fan-token/national-team-tokens.md` during this period.
```

---

## Dead rubber reasoning — summary

```
DEAD RUBBER QUICK REFERENCE:

  DEFINITION:
    A dead rubber is any match where the result cannot affect the advancement
    or elimination of either team. Both teams' fates are already determined.

  IDENTIFICATION STEPS:
    1. Check current group standings (points, goal difference)
    2. Simulate all possible results for remaining matches
    3. If result of THIS match cannot change either team's ranking: dead rubber

  SIGNAL WEIGHTS:
    Full dead rubber:    signal × 0.55 | motivation × 0.55
    Partial dead rubber: signal × 0.75 | motivation × 0.75
    Standard match:      signal × 1.00

  NEVER SUPPRESS FTP:
    FTP PATH_2 supply events fire on dead rubbers.
    A 0-0 dead rubber still produces a DRAW = no supply change.
    A 3-0 dead rubber win still produces a BURN event.
    Motivation context does not affect supply mechanics — result does.

  GOAL DIFFERENCE EXCEPTION:
    If goal difference is mathematically relevant for either team's
    advancement or seeding, the match is NOT a dead rubber even if
    win/loss is irrelevant. Apply standard signal weight.
```

---

## Signal Weight Adjustments

For World Cup matches, apply these interpretive weights (adjustments on top of base football weights):

| Modifier | Condition | Weight Adjustment |
|---|---|---|
| Stage weight | Group stage | ×1.00 base |
| Stage weight | Round of 16/32 | ×1.15 |
| Stage weight | Quarter-final | ×1.25 |
| Stage weight | Semi-final | ×1.35 |
| Stage weight | Final | ×1.50 |
| Dead rubber | Full dead rubber (both fates decided) | ×0.55 |
| Dead rubber | Partial dead rubber (one team's fate decided) | ×0.75 |
| Travel fatigue | Flight >8,000km, match 1 only | ×0.92 |
| Time zone | 6–8h difference, match 1 | ×0.92 |
| Time zone | 9+ hour difference, matches 1–2 | ×0.88 |
| Heat acclimatisation | Temperate→tropical, match 1 | ×0.90 |
| Altitude | Low-altitude team at altitude, match 1 | ×0.88 |
| Home continent | Same confederation as host | ×1.10 |
| Host nation | Playing in own country | ×1.20 |
| Accumulated fatigue | Quarter-final | ×0.90 |
| Accumulated fatigue | Semi-final | ×0.88 |
| Previous round ET | Extra time in previous match | additional ×0.95 |
| Underdog premium | Giant-killing WIN | ×1.5–2.0 on WIN signal |
| Third-place play-off | Standard (no special factors) | ×0.70 |

*FTP PATH_2: dead rubber ≠ no supply event. PATH_2 fires regardless of dead rubber status.*

---

## Key Commands

```
WORLD CUP SPECIFIC COMMANDS:

get_dead_rubber_status(team_a, team_b, group_standings)
  → Returns: dead_rubber_type (full / partial / none), modifier to apply
  → Also returns: goal_difference_in_play (true/false)

get_tournament_fatigue_modifier(team, matches_played, previous_round_ET)
  → Returns: fatigue_modifier value and rationale

get_travel_modifier(origin_country, venue_city, match_number)
  → Returns: travel_modifier, time_zone_modifier, climate_modifier
  → Checks: altitude, climate zone, time zone difference

get_bracket_position_signal(team, bracket_half, projected_path)
  → Returns: path_difficulty (favourable / standard / difficult)
  → Returns: demand_multiplier for associated token

get_tournament_phase(current_date, tournament_schedule)
  → Returns: current phase (pre-tournament / group / knockout / final / post)
  → Returns: applicable macro overlay from macro/tournament-macro.md

check_ftp_scope(match_type)
  → For international: returns "PATH_2 does NOT apply to club tokens in international matches"
  → For dead rubber: returns "PATH_2 still applies — dead rubber ≠ no supply event"
```

---

## Agent Reasoning Prompts

```
WHEN ANALYSING A WORLD CUP MATCH — LOAD ORDER AND KEY QUESTIONS:

1. Load: sports/football/sport-domain-football.md (base football domain)
2. Load: sports/football/sport-domain-football-world-cup.md (this file)
3. Load: fan-token/national-team-tokens.md (if national token involved)
4. Load: macro/tournament-macro.md (tournament macro overlay)

KEY QUESTIONS BEFORE ANY WORLD CUP MATCH:

  TOURNAMENT STRUCTURE:
  → What stage is this match? (group / R32 / QF / SF / Final)
  → Is this a dead rubber? (check both teams' mathematical positions)
  → Is goal difference in play? (may override dead rubber logic)
  → Is this a simultaneous final group round? (intra-match strategy shifts)

  TRAVEL AND FATIGUE:
  → What is the travel distance and time zone difference for each team?
  → Is this match 1, 2, or 3? (fatigue accumulation)
  → Did either team play extra time in the previous round?
  → What is the rest period between previous and current match?

  CLIMATE AND VENUE:
  → What is the altitude of the venue?
  → What is the climate zone vs each team's home environment?
  → Did either team hold a pre-tournament acclimatisation camp?

  NATIONAL TEAM SPECIFICS:
  → What is each player's role in the national team vs club role?
  → Has there been recent international form (last 3–5 international matches)?
  → Are star players confirmed in squad and expected to start?

  FTP SUPPLY:
  → Is either national team's corresponding fan token involved?
  → Does any involved club token have confirmed PATH_2? (Club matches only)
  → Is this match a dead rubber? (PATH_2 still fires — never suppress)

OUTPUT FORMAT:
  Generate structured signal with all tournament modifiers applied.
  Note each modifier applied and its rationale.
  Flag any high-uncertainty elements (extra time risk, dead rubber exception).
```

---

## Data Sources

```
PRIMARY SOURCES FOR WORLD CUP REASONING:

  Tournament structure and results:
    FIFA official (fifa.com)            — official results, squads, draw
    UEFA.com                            — for European national teams
    CONMEBOL.com                        — for South American national teams
    AFC (the-afc.com)                   — Asian teams
    CAF online (cafonline.com)          — African teams
    CONCACAF (concacaf.com)             — North/Central American and Caribbean

  Squad and player data:
    Club official websites              — player fitness and availability
    Transfermarkt.com                   — squad values and profiles
    Soccerway.com                       — results and historical records

  Tournament host city and venue:
    FIFA official venue listings        — city, altitude, climate zone
    Wunderground / weather APIs         — climate zone confirmation

  National token data:
    fantokens.com                       — active national tokens
    chiliscan.com                       — on-chain verification
    chiliz.com official                 — partnership announcements

AGENT NOTE:
  National team data is more frequently updated and less predictable
  than club data. Apply stricter Tier 1 confirmation requirements for
  national team signals (injury, squad selection, tactical changes).
```

---

## Playbook 1 — Group stage analysis

```
TRIGGER: World Cup group stage match
FILTER:  Confirm both teams' tournament positions before signal generation
ENTRY:   Apply dead rubber check first. If dead rubber: reduce signal weight.
EXIT:    T+24h (group stage results absorb quickly)
SIZING:  Scale with stage importance and dead rubber status.

STEPS:
  1. Check both teams' mathematical positions (dead rubber test)
  2. Check simultaneous match context (final group round only)
  3. Apply travel, time zone, climate modifiers for early rounds
  4. Apply fatigue modifier (match 2 or 3 in group stage)
  5. Check FTP scope — does PATH_2 apply? (national team = no PATH_2 for club tokens)
  6. Generate signal with all modifiers documented
```

## Playbook 2 — Knockout match analysis

```
TRIGGER: World Cup knockout round match
FILTER:  Bracket position, rest days, previous round extra time
ENTRY:   T-48h with confirmed team news
EXIT:    T+24h (knockout signal resolves quickly post-match)
SIZING:  Scale with round (QF > R16 > SF > Final)

STEPS:
  1. Identify round and bracket position
  2. Apply stage-appropriate signal magnitude
  3. Apply accumulated fatigue modifier (QF, SF, Final)
  4. Apply extra time haircut if previous round went to ET
  5. Apply penalty probability note if teams are evenly matched
  6. Check FTP scope (national team matches — no PATH_2 for club tokens)
  7. Load national-team-tokens.md for demand signal on national tokens
```

## Playbook 3 — Dead rubber identification

```
TRIGGER: Approaching World Cup group stage match where fates may be decided
FILTER:  Run mathematical simulation before signal generation
ENTRY:   Only after confirming dead rubber status
EXIT:    Apply reduced signal weight throughout; do not revert to standard
SIZING:  signal × 0.55 (full dead rubber) or × 0.75 (partial)

STEPS:
  1. Simulate all possible results for all remaining group matches
  2. Determine if THIS match's result can change either team's fate
  3. If NO → full dead rubber → apply signal × 0.55
  4. Check goal difference — if GD in play, override dead rubber logic
  5. CHECK FTP: dead rubber ≠ no PATH_2 supply event. Still apply FTP.
  6. Document dead rubber status explicitly in signal output
```

## Playbook 4 — National team token tournament signal

```
TRIGGER: National team token with confirmed tournament participation
FILTER:  Confirm nation has qualified and has an active fan token
ENTRY:   Begin with Phase 2 (squad announcement) or earlier if available
EXIT:    Apply appropriate exit decay curve on elimination
SIZING:  Scale with tournament round and underdog premium

STEPS:
  1. Load fan-token/national-team-tokens.md
  2. Load macro/tournament-macro.md (apply tournament macro overlay)
  3. Confirm qualification and active token status
  4. Apply tournament demand phase (1–5) based on current moment
  5. Apply host nation modifier if applicable
  6. Apply cross-token confederation correlation
  7. Generate demand signal (demand only — no PATH_2 for national tokens)
```

---

## Compatibility

**Extends:** `sports/football/sport-domain-football.md`
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`
**Existing WC intelligence:** `fan-token/world-cup-2026-intelligence/`

---

*SportMind v3.97.18 · MIT License · sportmind.dev*
*Enduring framework — applicable to every future World Cup*
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`
**Existing WC intelligence:** `fan-token/world-cup-2026-intelligence/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | FIFA World Cup signal intelligence: 48-team format, group dynamics, host effects, and squad signals |
| Reasoning | ACTIVE | World Cup reasoning chain from squad composition, group draw, and conditions to outcome prediction |
| Context | ACTIVE | World Cup context: 2026 North America hosts, 48-team format, extended squad size |
| Memory | ACTIVE | Historical World Cup outcome patterns and tournament stage baselines |
| Judgment | ACTIVE | Judgment on World Cup signal hierarchy — squad depth and tournament form are primary |
| Attention | ACTIVE | Maximum attention during World Cup — highest demand amplifier in SportMind |
| Communication | ACTIVE | World Cup signal output with tournament phase, group context, and direction |
| Verification | ACTIVE | World Cup data from FIFA official sources |
| Learning | ACTIVE | World Cup modifier calibration from historical tournament outcome data |
| Integration | ACTIVE | Integrates with sport-domain-football.md, national team tokens, and World Cup 2026 fan token framework |
| Calibration | ACTIVE | World Cup modifiers calibrated against historical stage and format outcome data |
| Adaptation | ACTIVE | World Cup intelligence adapts for 2026 48-team format changes |
| Ethics | NOT APPLICABLE | World Cup sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Tournament stage, group context, and format change implications explicit in output |


---

*SportMind v3.97.18 · MIT License · sportmind.dev*
*Enduring framework — applicable to every future World Cup*
