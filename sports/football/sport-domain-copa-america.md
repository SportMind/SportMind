---
name: sport-domain-copa-america
description: >
  Copa América reasoning framework. Structural differences from the World Cup.
  Covers CONMEBOL format, CONCACAF guest teams, altitude/climate modifiers,
  and impact on $ARG and Brazilian fan token demand signals.
---

# Copa América — Sport Domain Reasoning

**Structural differences from the World Cup framework. Load with:**
`sports/football/sport-domain-football-world-cup.md` (base tournament framework)

> Enduring reasoning framework. No specific player names, scores, or expiring data.

---

## Domain Model

Copa América is the continental championship of CONMEBOL (South American Football Confederation). It is the oldest international football tournament in the world and typically includes invited CONCACAF guest nations. Held every four years (with irregular editions), it typically overlaps with the European close season — meaning European-based South American players arrive significantly fresher than they would for AFCON.

Key distinctions from the World Cup:
- CONMEBOL-only nations + invited CONCACAF guests
- Rotating host system — altitude and climate vary dramatically by host
- European-based players arrive post-season (less fatigued than AFCON)
- Primary fan tokens: $ARG | No confirmed Brazil token currently
- CONCACAF guest teams introduce non-CONMEBOL reasoning requirements

---

## Event Playbooks

### Playbook 1: Copa América Group Stage
```
trigger: Copa América group stage match
entry:   T-48h with altitude and climate check
exit:    T+24h
filter:  altitude_modifier + climate_modifier + CONMEBOL_vs_CONCACAF_check
sizing:  signal × 1.00 base; altitude compounds significantly at high-altitude venues
```

### Playbook 2: Copa América Knockout Match
```
trigger: Copa América knockout match
entry:   T-48h
exit:    T+24h post-result
filter:  accumulated_fatigue × host_nation_check × altitude_acclim status
sizing:  signal × stage_weight (same scale as WC framework)
```

### Playbook 3: CONMEBOL vs CONCACAF Guest Match
```
trigger: Match between CONMEBOL and CONCACAF guest team
entry:   Apply quality_gap_modifier before signal generation
exit:    T+24h
filter:  Guest team motivation (often playing for qualification tournaments, not Copa)
sizing:  Apply quality_tier_differential — CONMEBOL teams statistically stronger
note:    CONCACAF guest motivation is typically lower; dead rubber logic may apply
         earlier than standard — check group context carefully
```

### Playbook 4: $ARG Token — Copa América Signal
```
trigger: Argentina fan token with confirmed tournament participation
entry:   Phase 3 (group draw) or earlier if available
exit:    Exit decay curve on elimination
filter:  PATH_2 not confirmed for $ARG — demand-only signals apply
sizing:  Apply national-team-tokens.md demand cycle; Copa year premium
```

---

## Signal Weight Adjustments

| Factor | Copa América | World Cup | Rationale |
|---|---|---|---|
| Altitude modifier | CRITICAL | Significant | Some venues at 2,500m+ — extreme effect |
| CONCACAF guest quality | Lower | N/A | Quality gap is significant modifier |
| Player fatigue on arrival | LOW (post-European season) | VARIES | South American players fresh from seasons |
| Fan token primary signal | $ARG dominant | Multiple | Limited active CONMEBOL fan tokens |
| Tournament rarity | Moderate | High | More frequent than WC; less rare signal |
| Crowd culture | Intense, partisan | Varies | South American stadiums extreme atmosphere |

---

## CONMEBOL format and qualification

```
FORMAT (standard Copa América):
  12 CONMEBOL teams + invited CONCACAF guests (typically 2-4)
  Group stage → knockout (quarterfinals → semis → final)
  Qualification: CONMEBOL members automatically qualify
  CONCACAF guests: invited by CONMEBOL (not via qualification — motivation issue)

QUALIFICATION REASONING:
  All 10 CONMEBOL nations automatically qualify → no qualification risk to model
  $ARG ($ARG token) has no qualification risk signal — Argentina always participates
  CONCACAF guests: their presence is political/commercial, not qualification-earned
  
  AGENT RULE:
    Copa América has no qualification risk discount for CONMEBOL nations.
    Skip the Phase 1 qualification check from national-team-tokens.md for CONMEBOL.
    Apply Phase 2 (squad announcement) as the first relevant signal.
```

---

## Altitude and climate modifiers

```
ALTITUDE — COPA AMERICA CRITICAL MODIFIER:

  CONMEBOL hosts rotating. Some historic and potential venues are at
  extreme altitude — Bolivia (La Paz ~3,600m), Colombia (Bogotá ~2,600m),
  Peru (Cusco ~3,400m), Ecuador (Quito ~2,850m).

  ALTITUDE MODIFIER TABLE:
    Sea level venues (0–500m):       no modifier
    Moderate altitude (500–1,500m):  altitude_modifier = ×0.96 (first match only)
    High altitude (1,500–2,500m):    altitude_modifier = ×0.90 (matches 1–2)
    Extreme altitude (>2,500m):      altitude_modifier = ×0.82 (matches 1–2)

  ACCLIMATISATION EXEMPTIONS:
    Teams based in the host nation's altitude zone: no modifier
    Teams that held pre-tournament camp at similar altitude: reduce modifier by half
    After 2+ matches at altitude: assume acclimatisation, restore to baseline

  COMPOUND ALTITUDE + HEAT:
    Some CONMEBOL venues combine altitude with tropical heat (Manaus-type conditions).
    Apply both modifiers if confirmed: altitude + heat compound (multiply, not add).
    Document both modifiers explicitly in signal output.

SOUTH AMERICAN CLIMATE CONTEXT:
  Copa América timing (June–July): South American winter in southern cone nations
  (Argentina, Chile, Uruguay) but tropical summer in northern nations (Colombia, Brazil).
  Check host city climate zone before every match — do not assume uniform conditions.
```

---

## CONCACAF guest team reasoning

```
CONCACAF GUESTS — SIGNAL IMPLICATIONS:

  Copa América regularly invites CONCACAF nations (USA, Mexico, others).
  These teams are NOT qualifying — they are invited guests.

  MOTIVATION DIFFERENTIAL:
    CONMEBOL teams: Copa América is the pinnacle of South American football
    CONCACAF guests: playing for experience, preparation, prestige — not titles
    Motivation modifier: CONCACAF_guest_motivation = ×0.88 (against CONMEBOL)

  QUALITY DIFFERENTIAL:
    CONMEBOL top-4 (Argentina, Brazil, Uruguay, Colombia): World Cup-level quality
    CONCACAF guests: typically World Cup qualification-tier quality
    Apply: quality_tier_gap_modifier when CONMEBOL top-4 faces CONCACAF guest
      quality_tier_gap_modifier = ×1.12 for CONMEBOL top-4

  EXCEPTION — CONCACAF STRONG TEAMS:
    USA, Mexico are competitive at international level.
    Do not apply full quality gap vs USA or Mexico — they are competitive.
    Apply standard match signal; no quality_tier modifier vs USA/Mexico.

  DEAD RUBBER NOTE:
    CONCACAF guest teams with no realistic Copa title ambition may rotate
    more heavily than CONMEBOL opponents in group stage.
    Apply partial dead rubber logic if guest team's progress is already secured
    or mathematically impossible.
```

---

## $ARG and Brazilian fan token demand

```
COPA AMERICA FAN TOKEN SIGNALS:

  PRIMARY ACTIVE TOKEN:
    $ARG — Argentina Fan Token
    Copa América is the primary national tournament signal for $ARG.
    Every Copa América is a demand cycle event for $ARG.
    Apply national-team-tokens.md demand phases — no Copa-specific modifications needed.
    PATH_2 NOT confirmed for $ARG — demand-only signals apply.

  BRAZIL:
    No confirmed Brazil fan token as of current library state.
    Brazil's Copa América performance generates demand for $FLU and $MENGO
    as the highest-profile Brazilian club tokens — partial national proxy effect.
    Apply: brazil_proxy_modifier = ×1.03 per knockout round for $FLU/$MENGO
    if Brazil advances, assuming the narrative associates.

  MONITORING:
    Watch for any CONMEBOL national token launches before Copa América.
    A Brazil national token launch = highest-value unserved Copa América token.
    If launched: apply national-team-tokens.md Phase 1 immediately.
```

---

## European-based player fatigue context

```
PLAYER ARRIVAL FATIGUE — COPA AMERICA ADVANTAGE:

  Copa América is played in June–July.
  European domestic seasons end in May–June.
  European-based South American players are released post-season.

  Contrast with AFCON:
    AFCON: January — mid-season for European leagues; African players miss
      club matches and return fatigued from tournament + travel
    Copa América: June — post-season; no club matches missed; players fresh

  FATIGUE MODIFIER — COPA AMERICA:
    For South American players based in European clubs:
      No post-season fatigue modifier (arrived fresh after domestic season)
      Exception: players who participated in long cup runs into May/June
      (UCL Final participants, cup final participants) — apply ×0.95 match 1

  NET EFFECT:
    Copa América generally has fewer compounding fatigue factors than AFCON.
    Apply World Cup base fatigue framework without additional AFCON-style
    European-season disruption modifiers.
```

---

## Agent Reasoning Prompts

```
COPA AMERICA-SPECIFIC QUESTIONS (supplement World Cup framework):

  1. What is the altitude of the venue?
     → Mandatory before every Copa match — some venues are extreme altitude
  2. Is this a CONMEBOL vs CONCACAF guest match?
     → Apply quality_tier and motivation modifiers for guest teams
  3. Is the guest team USA or Mexico?
     → Do NOT apply quality gap modifier — they are competitive
  4. Is $ARG involved? Is this a Copa demand cycle signal?
     → Apply national-team-tokens.md Phase 4 (progression) signal
  5. Are European-based South American players fatigued?
     → Copa starts post-European season (June) — typically fresh on arrival
     → Exception: UCL Final or cup final participants in May/June
  6. Does Brazil have an active fan token?
     → Currently no — route Brazil sentiment through $FLU and $MENGO proxy
```

---

## Key Commands

```
get_copa_altitude_modifier(venue_city)
  → Returns: altitude_modifier based on venue elevation

get_conmebol_vs_concacaf_modifier(team_type)
  → Returns: quality_tier or motivation modifier for guest team matches

get_arg_copa_demand_signal(tournament_phase)
  → Returns: $ARG demand phase signal per national-team-tokens.md framework

check_copa_path2_applicable(match)
  → Returns: "PATH_2 not confirmed for $ARG — demand only"
```

---

## Data Sources

```
CONMEBOL official (conmebol.com)  — fixtures, results, squads
Transfermarkt.com                 — nationality data for squad analysis
Goal.com / Infobae (Spanish)      — South American coverage
Terra Sports (Portuguese)         — Brazilian coverage
fantokens.com                     — $ARG supply and FTP status
```

---

## Compatibility

**Base framework:** `sports/football/sport-domain-football-world-cup.md`
**National tokens:** `fan-token/national-team-tokens.md`
**Tournament macro:** `macro/tournament-macro.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Copa America-specific signal intelligence: CONMEBOL dynamics, altitude, and squad signals |
| Reasoning | ACTIVE | Copa America reasoning chain from squad composition and venue conditions to outcome prediction |
| Context | ACTIVE | Copa America context: altitude venues, South American press style, squad fatigue from MLS/European season |
| Memory | ACTIVE | Historical Copa America outcome patterns and altitude impact data |
| Judgment | ACTIVE | Judgment on Copa America signal hierarchy — altitude and squad freshness are primary |
| Attention | ACTIVE | Elevated attention for altitude venues and squad confirmation signals |
| Communication | ACTIVE | Copa America signal output with altitude modifier, squad context, and direction |
| Verification | ACTIVE | Copa America data from CONMEBOL official sources |
| Learning | ACTIVE | Copa America modifier calibration from historical tournament outcome data |
| Integration | ACTIVE | Integrates with sport-domain-football.md and national team framework |
| Calibration | ACTIVE | Copa America altitude modifiers calibrated against historical venue outcome data |
| Adaptation | ACTIVE | Copa America intelligence adapts as CONMEBOL format and venue rotation evolve |
| Ethics | NOT APPLICABLE | Copa America sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Altitude context, venue data source, and modifier basis explicit in output |


---

*SportMind v3.97.24 · MIT License · sportmind.dev*
*Enduring framework — applies to every future Copa América*
