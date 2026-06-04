---
name: rugby-union-specific
description: >
  Rugby union extended reasoning framework and fan token intelligence.
  Structural differences from base sport domain. Covers set piece dominance
  as the primary signal, kicking game intelligence, competition structure,
  and specific reasoning for $SARRIES token. Load alongside
  sports/rugby/sport-domain-rugby-union.md.
---

# Rugby Union — Extended Reasoning Framework

**Extends `sports/rugby/sport-domain-rugby-union.md`. Do not re-read base content.**
Load the base file first, then this file for extended intelligence.

---

## Fan token context

```
ACTIVE RUGBY UNION FAN TOKENS:
  $SARRIES  — Saracens (Premiership Rugby)
  $SHARKS   — Sharks (South Africa / URC)
  $QUINS    — Harlequins (Premiership Rugby)
  $SFP      — Stade Français Paris (Top 14)

ALL DEMAND-ONLY:
  No confirmed FTP PATH_2 mechanic for any rugby union token.
  Athlete availability → match outcome probability → demand signal only.
  Do not apply PATH_2 supply chain to any rugby union token.
```

---

## Set piece dominance as primary signal

```
SET PIECE — THE PRIMARY SIGNAL IN ELITE RUGBY:

  WHY SET PIECE DOMINATES:
    Unlike football, rugby union's set piece (scrum and lineout) is a
    structured possession contest that directly determines territory,
    field position, and scoring opportunity.
    
    A team that dominates the set piece controls:
      Possession quality (clean ball vs disrupted ball)
      Field position (forward pressure creates territory)
      Momentum (set piece dominance demoralises opponents)
      Penalty opportunity (scrum infringements = kickable penalties)
      
  SCRUM SIGNAL:
    Set piece dominance assessment: identify which team has the stronger scrum pack.
    Scrum-dominant team in wet conditions: amplified advantage (ball slippery = set piece control more valuable)
    
    scrum_dominance_modifier:
      Clear scrummaging advantage: ×1.08 to adjusted score
      Marginal advantage: ×1.03
      Evenly matched: no modifier
      
  LINEOUT SIGNAL:
    Lineout accuracy predicts clean possession rates.
    lineout_accuracy_modifier:
      Confirmed lineout dominant team: ×1.05
      Lineout uncertainty (hooker form issue): ×0.95
      
  COMBINED SET PIECE:
    Team with both scrum AND lineout dominance:
      set_piece_dominance_modifier = ×1.12 (compound)
      This is one of the strongest single modifiers in rugby union.
```

---

## Kicking game intelligence

```
TERRITORY AND FIELD POSITION — KICKING GAME:

  KICKING GAME AS PRIMARY ATTACKING MECHANISM:
    In elite rugby union (particularly international and European level),
    the kicking game is not a fallback — it is often the primary attacking
    mechanism. Teams use tactical kicking to establish territory, create
    pressure, and force errors.
    
  KICKING GAME MODIFIER FRAMEWORK:
    Kicking-dominant team WITH an elite goal kicker:
      kicking_game_modifier = ×1.08
      Rationale: every turnover or penalty conceded becomes a scoring opportunity
      
    Kicking-dominant team WITHOUT an elite goal kicker:
      kicking_game_modifier = ×1.02 (territorial benefit without conversion certainty)
      
    Non-kicking team facing kicking-dominant opponent:
      chase_and_defend_pressure = elevated; apply ×0.97 to defending modifier
      
  WIND INTERACTION (see weather-intelligence.md):
    Kicking game in strong wind: kicking_game_modifier reduced to ×0.92 against wind
    Kicking game with wind: kicking_game_modifier elevated to ×1.15 with wind
    This is the largest wind modifier in the library — kicking sports are most affected.
    
  HIGH ALTITUDE KICKING:
    At altitude (1,500m+): ball travels further, kicks go longer than sea level.
    Kicking teams at altitude: kicking_game_modifier = ×1.05 additional
    (longer kicks = better field position from same kick quality)
```

---

## Home advantage and fortress venues

```
HOME ADVANTAGE — RUGBY UNION:

  BASELINE: +0.12 to adjusted score (above football +0.10)
  Reasoning: crowd noise at lineouts affects throw accuracy;
    scrum calls benefit from crowd noise disruption of opposition;
    referee interpretation influenced by partisan crowd.

FORTRESS VENUES:
  Some rugby grounds have documented fortress characteristics.
  Apply fortress_modifier = ×1.15 (above baseline ×1.12) when:
    Home team win% at this venue exceeds 70% in last 5 seasons
    Crowd atmosphere is documented as elite-level hostile
    Examples: Loftus Versfeld, Principality Stadium (closed roof), Eden Park
    
  CLOSED ROOF STADIUMS:
    Some rugby venues have retractable roofs.
    Closed roof: amplifies crowd noise significantly; apply ×1.05 to home advantage
    Open roof in rain: apply wet conditions modifier (see weather file)
```

---

## Competition structure reasoning

```
PREMIERSHIP RUGBY (England):
  Regular season: home and away; apply standard home advantage modifier
  Playoff format: top 4 qualify; semi-finals at top seeds' grounds
    → Home advantage applies in semi-finals for top seeds
  European qualification: league position affects European Champions Cup entry
    → Demand signal elevated when European qualification is at stake
    Apply: european_stakes_modifier = ×1.05 to demand signal in final 5 matches
      when European qualification is uncertain

UNITED RUGBY CHAMPIONSHIP (URC):
  Cross-border competition (Ireland, Scotland, Wales, Italy, South Africa):
    Significant travel fatigue modifier for South African clubs:
    URC matches in Europe for South African teams: apply ×0.95 match 1 of European tour
    (Long-haul travel + time zone adjustment; see general travel modifier)
  Conference structure: conference position affects playoff seeding
  
EUROPEAN CHAMPIONS CUP:
  Highest prestige European rugby competition.
  Fan token demand responds strongly to European progress:
    European Champions Cup match: demand_premium = ×1.10 (higher than Premiership match)
    Knockout stage: demand_premium = ×1.20
    Final appearance: demand_premium = ×1.40
    
  Token-specific: $SARRIES demand is most sensitive to European Champions Cup
  as Saracens' brand is strongly associated with European pedigree.
    
SUPER RUGBY (Southern Hemisphere):
  Travel fatigue signal is the primary differentiator from Northern Hemisphere:
    Trans-Tasman travel (Australia ↔ New Zealand): ×0.97 first match (significant time zone)
    Southern Hemisphere to South Africa: ×0.95 first match (combined travel + altitude)
    Apply: super_rugby_travel_modifier per fixture — do not assume domestic conditions.
```

---

## $SARRIES token reasoning

```
SARACENS ($SARRIES) — TOKEN-SPECIFIC REASONING:

  BRAND IDENTITY:
    Saracens' brand is built on European Champions Cup success and Premiership dominance.
    Their token demand is more sensitive to European progress than domestic results.
    
  DEMAND SIGNAL PRIORITIES:
    1. European Champions Cup knockout stage matches (highest demand trigger)
    2. Premiership playoff matches
    3. Regular season Premiership matches (lower demand weight)
    
  DEMAND MODIFIER FRAMEWORK:
    European Champions Cup knockout: demand_weight = ×1.30 vs standard match
    Premiership final: demand_weight = ×1.20
    Premiership semi-final: demand_weight = ×1.10
    Regular season: demand_weight = ×1.00
    
  STONEX STADIUM (home ground):
    Saracens' StoneX Stadium has a noted home advantage.
    Relatively smaller capacity for a top club — full capacity is intimate and loud.
    Apply: stonex_sellout_modifier = ×1.08 when confirmed sell-out
    (Higher than average home advantage — intimate ground amplifies atmosphere)
```

---

## Compatibility

**Base file:**         `sports/rugby/sport-domain-rugby-union.md`
**Referee framework:** `core/referee-intelligence.md`
**Weather:**           `core/weather-intelligence.md`
**Travel fatigue:**    `sports/football/sport-domain-football-world-cup.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Rugby union cross-competition framework: URC, Premiership, and European Cup signals |
| Reasoning | ACTIVE | Rugby union cross-competition reasoning with competition-specific override hierarchy |
| Context | ACTIVE | Cross-competition context: shared set piece signals vs competition-specific modifiers |
| Memory | ACTIVE | Cross-competition rugby union outcome patterns |
| Judgment | ACTIVE | Judgment on cross-competition rugby signal applicability |
| Attention | ACTIVE | Attention allocation across simultaneous rugby union competitions |
| Communication | ACTIVE | Cross-competition output with competition identifier and framework version |
| Verification | ACTIVE | Rugby union cross-competition data from World Rugby and competition operators |
| Learning | ACTIVE | Cross-competition calibration from accumulated rugby union outcome data |
| Integration | ACTIVE | Integrates with sport-domain-rugby-union.md and all competition-specific files |
| Calibration | ACTIVE | Cross-competition rugby union calibration consistent with sport-domain framework |
| Adaptation | ACTIVE | Rugby union framework adapts as competition formats and law changes evolve |
| Ethics | NOT APPLICABLE | Rugby union framework is analytical — no ethical dimension |
| Transparency | ACTIVE | Competition type and applied framework explicit in output |


---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*Set piece dominance is the primary signal in elite rugby union*
