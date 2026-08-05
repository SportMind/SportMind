---
name: esports-cs2
description: >
  CS2 (Counter-Strike 2) specific reasoning framework. Covers tournament
  signal weights (Majors, IEM Katowice, ESL Pro League), AWPer role
  dominance, map pool intelligence, pistol round signal, economy reasoning,
  and the framework for any CS2 organisation token that launches.
---

# CS2 (Counter-Strike 2) — Esports Reasoning Framework

**Title-specific. Load alongside `sports/esports-framework.md` (base framework).**

---

## Active CS2 tokens — status note

```
CS2 TOKEN STATUS (as of library compilation):

  $NAVI — Natus Vincere:
    LEGACY CONTRACT ONLY. Partnership no longer active.
    Token exists as legacy on-chain contract.
    DO NOT apply active partnership demand signal to $NAVI.
    If partnership is restored: update this file with confirmed source.
    
  $VIT — Vitality (multi-title, includes CS2):
    Verify current Chiliz partnership status before applying CS2-specific signals.
    Vitality compete in CS2 among other titles.
    
  $MIBR — MIBR (CS2):
    DORMANT status — verify before applying any signal.
    
  NO CONFIRMED ACTIVE CS2-EXCLUSIVE TOKENS.
  
  FRAMEWORK PURPOSE:
    This file provides the enduring CS2 reasoning framework for any CS2 organisation
    token that launches — or for multi-title tokens ($VIT) where CS2 performance
    is part of the demand signal.

AGENT RULE:
  Always verify token status at fantokens.com before applying CS2 demand signals.
  The framework below is the enduring reasoning structure — apply it to any
  confirmed active CS2 token.
```

---

## Tournament structure and signal weights

```
CS2 TOURNAMENT HIERARCHY:

  CS MAJORS (twice yearly — Valve official events):
    Signal weight: ×1.80
    These are the only Valve-sanctioned championships — they carry the highest
    prestige in CS2 and are the primary demand catalyst.
    Prize pool: substantial (Valve-funded); sticker revenue makes these unique events
    
    Major demand cycle:
      Pre-Major qualifier / RMR events: ×1.05
      Major group stage (Swiss or group format): ×1.15
      Major playoff bracket: ×1.25
      Major victory: +40-60% demand spike
      Post-Major: 3-4 week decay to new elevated baseline

  IEM KATOWICE:
    Signal weight: ×1.60 (effectively equivalent to a Major in prestige)
    Katowice is the highest prestige non-Major; crowd atmosphere and history
    make it the benchmark non-Valve event.
    Treat as a near-Major for demand signal purposes.

  ESL PRO LEAGUE:
    Signal weight: ×1.20
    Top tier league — season champions carry meaningful prestige signal.

  BLAST PREMIER:
    Signal weight: ×1.20
    Equivalent tier to ESL Pro League.
    BLAST World Final: signal weight ×1.50 (season-crowning event)

  ONLINE LEAGUES vs LAN EVENTS:
    CS2 has significant online play in regular season — apply ×0.92 online modifier.
    All Majors and IEM Katowice: LAN only — full signal weight.
```

---

## CS2 specific modifiers

### AWPer role — highest individual impact position

```
AWPer ROLE INTELLIGENCE:

  WHY AWPer IS UNIQUE IN CS2:
    The AWPer (primary sniper using the AWP rifle) is the highest individual
    impact role in CS2. A single AWP can determine round outcomes.
    AWPer absence has a larger signal impact than any other role.

  AWPer MODIFIER FRAMEWORK:

  Scenario                          Modifier     Notes
  ────────────────────────────────────────────────────────────────
  Primary AWPer absent              ×0.82        Highest single role modifier in CS2
  Primary AWPer → elite replacement ×0.95        Quality preserved
  Primary AWPer → unproven replace  ×0.85        Significant but not as acute as absence
  Primary AWPer present             ×1.08        Elite AWPer on map that suits AWP

  COMPARISON: Star carry in most esports: ×0.75 departure modifier
  CS2 AWPer: ×0.82 absence modifier (slightly less severe due to team role distribution)
  But on specific AWP-favoured maps: AWPer presence ×1.08 = higher ceiling than other titles

  MAP-AWPer INTERACTION:
    Some CS2 maps are heavily AWP-favoured (long sightlines, open areas).
    On confirmed AWP-favoured maps:
      AWPer present: apply awp_map_premium = ×1.08 (above baseline)
      AWPer absent: apply awp_map_penalty = ×0.80 (worse than standard absence)
    AWP-unfavoured maps (close quarters): reduce AWPer modifier impact by 30%
```

### Map pool intelligence

```
MAP POOL — PRE-MATCH SIGNAL MODIFIER:

  ENDURING MAP STRENGTHS AND WEAKNESSES:
    CS2 teams develop documented strong and weak maps over multiple tournaments.
    These patterns are enduring across years (slow to change without major roster overhaul).
    
  HOW TO APPLY MAP POOL INTELLIGENCE:
    Identify each team's documented strong and weak maps (3+ tournament matches per map).
    On each map in the best-of series:
      Team on documented strong map: ×1.08 map-specific modifier
      Team on documented weak map: ×0.87 map-specific modifier
      
  MAP VETO PROCESS AS SIGNAL:
    The map veto (teams ban maps before play) is itself an intelligence signal.
    Veto signal: team banning their opponent's strongest map = strategic awareness
      Apply: veto_intelligence_modifier = ×1.03 for team making optimal veto decision
    Team forced onto documented weak map by opponent veto:
      Apply: forced_weak_map_modifier = ×0.87 (same as map pool framework)
      
  BEST-OF-3 vs BEST-OF-5:
    Best-of-3: map pool depth matters more (opponent has more bans)
    Best-of-5: wider map pool benefits; fewer bans per side
    For Bo5 (typically only Grand Finals): apply ×1.05 to teams with widest confirmed map pool
```

### Pistol round intelligence

```
PISTOL ROUND WIN RATE:

  WHY PISTOL ROUNDS MATTER:
    Rounds 1 and 16 (second half pistols) are pistol rounds — all players start with
    limited budgets. Pistol round outcomes significantly affect momentum and economy.
    
  PISTOL WIN RATE MODIFIER:

  Win rate              Modifier    Notes
  ──────────────────────────────────────────────────────
  Above 60%             ×1.06       Elite pistol play; consistent early-round advantage
  55-60%                ×1.04       Above average
  45-55% (average)      ×1.00       No modifier — within normal range
  40-45%                ×0.96       Below average; early-round disadvantage
  Below 40%             ×0.94       Consistent pistol weakness

  LEADING INDICATOR USE:
    Pistol round win rate is a forward-looking signal, not just a result.
    Teams with high pistol win rates tend to win economically on both sides.
    Apply as a baseline modifier before match-level adjustments.
```

### Economy reasoning

```
ECONOMY AND COMEBACK PROBABILITY:

  LOSS BONUS SYSTEM:
    After consecutive round losses, teams accumulate more buy-power.
    The loss bonus system creates structural comeback opportunities.
    
  ECONOMY SIGNAL IN PRE-MATCH REASONING:
    Teams that can maintain discipline across economic cycles are more resilient.
    Full-buy round efficiency: confirmed disciplined economic teams ×1.04 on close matches
    Eco-round hit rate (teams that win rounds on reduced buy): ×1.03 bonus
    
  AFTER THREE CONSECUTIVE ROUND LOSSES (in-match signal if tracking live):
    Economy reset probability increases — variance signal ×1.10 for following rounds
    Note: this is primarily an in-match reasoning signal, not a pre-match modifier.
    Pre-match: identify historically disciplined economic teams; apply modifier above.
    
  AGENT RULE FOR CS2 ECONOMY:
    Pre-match: apply pistol win rate and map pool modifiers.
    In-match: track consecutive loss streaks for economic reset signals.
    The loss bonus creates legitimate comeback probability even from deficit.
```

---

## CS2 organisation token demand framework

```
DEMAND FRAMEWORK FOR ANY CS2 ORGANISATION TOKEN:

  TIER 1 ORGANISATIONS — HIGHEST LAUNCH POTENTIAL:
    Organisations with:
      Major victories creating prestige baseline (permanent ×1.08-1.15 floor)
      Global fanbases (not purely regional)
      CIS/Eastern European heritage (highest documented CS engagement density)
    These organisations would produce the highest sustained demand on launch.
    
  DEMAND TIER TABLE BY ACHIEVEMENT:

  Status                                  Baseline modifier
  ──────────────────────────────────────────────────────────────
  Multiple Major winner                   ×1.15 permanent prestige floor
  Single Major winner                     ×1.10 permanent prestige floor
  Major finalist (no win)                 ×1.05 prestige floor
  Top 8 regular contender (no Major win)  ×1.02 prestige floor
  Regional competitive only               ×1.00 (no prestige modifier)

  DEMAND SENSITIVITY TIERS:
    CS Major demand weight: 0.70 | Regular season: 0.30
    (CS2 tokens should be treated as Major-event-sensitive above all else)
```

---

## Compatibility

**Base framework:**  `sports/esports-framework.md`
**Dota 2:**          `sports/esports-dota2.md`
**LoL/Valorant:**    `sports/esports-moba-tactical.md`
**CDI:**             `fan-token/esports-token-intelligence/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | CS2-specific signal intelligence: map pool, economy, AWP usage, and round patterns |
| Reasoning | ACTIVE | CS2 reasoning chain from map pool and economy to match outcome prediction |
| Context | ACTIVE | CS2 context: map veto, pistol round precedence, CT vs T side, economy state |
| Memory | ACTIVE | Historical CS2 outcome patterns by map and team composition |
| Judgment | ACTIVE | Judgment on CS2 signal hierarchy — map veto and economy are primary signals |
| Attention | ACTIVE | Elevated attention during Major championships and qualifying events |
| Communication | ACTIVE | CS2 signal output with map pool context and economy modifier |
| Verification | ACTIVE | CS2 data from official HLTV and Valve tournament sources |
| Learning | EMERGING | CS2 calibration records are limited |
| Integration | ACTIVE | Integrates with sport-domain-esports.md and esports-framework.md |
| Calibration | EMERGING | CS2 calibration is emerging — CS:GO historical data partially applicable |
| Adaptation | ACTIVE | CS2 intelligence adapts as map pool and game updates change meta |
| Ethics | NOT APPLICABLE | CS2 sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Map pool, economy state, and data source explicit in output |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |


---

*SportMind v3.97.30 · MIT License · sportmind.dev*
*AWPer is highest individual role modifier in CS2 (×0.82 absence, ×1.08 AWP-map presence)*
*$NAVI is a legacy on-chain contract — do not treat as active partnership*
