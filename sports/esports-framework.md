---
name: esports-framework
description: >
  Overarching esports reasoning framework for AI agents. Core differences from
  traditional sports: patch meta intelligence, roster change impact, LAN vs online
  variance, regional dominance patterns, prize pool motivation, and annual demand
  cycle. All demand-only — no FTP PATH_2 confirmed for any esports token.
  Load before any title-specific esports file.
---

# Esports — Core Reasoning Framework

**Overarching framework for esports signal reasoning. Load before title-specific files.**
Extends: `sports/esports/sport-domain-esports.md` (base domain) and
`fan-token/esports-token-intelligence/` (CDI framework).
Do not duplicate base content — this file adds deep reasoning layers.

---

## Confirmed active esports tokens on Chiliz Chain

```
BRIDGE_LIVE (active partnership, multi-chain):
  $OG    OG Esports — Dota 2 primary title
  $ALL   Alliance — Dota 2 primary title (verify current partnership status)

ACTIVE — Chiliz Chain (partnership status: verify before applying):
  $TH    Team Heretics — multi-title
  $VIT   Vitality — multi-title (CS2, LoL, others)
  $DOJO  DOJO — verify title affiliation before applying
  $MIBR  MIBR — CS2 — DORMANT (verify before applying demand signals)

LEGACY — DO NOT TREAT AS ACTIVE PARTNERSHIP:
  $NAVI  Natus Vincere — Partnership no longer active.
         Token exists as legacy on-chain contract only.
         Do not apply demand signal from active partnership intelligence.

NO ACTIVE CHILIZ TOKEN CONFIRMED:
  League of Legends organisations
  Valorant organisations
  (Framework built for future launches — see esports-moba-tactical.md)

AGENT RULE:
  Before applying any esports token demand signal: verify current partnership
  status at fantokens.com or chiliz.com official channels.
  Partnership statuses change more frequently in esports than in traditional sports.
  Never assume a token is active based on on-chain existence alone.
```

---

## Patch meta intelligence — unique to esports

```
PATCH META — THE PRIMARY ESPORTS SIGNAL MODIFIER:

  WHY PATCHES MATTER:
    Game developers release patches that change hero/weapon/character balance,
    mechanics, and strategic viability. A patch can make entire strategies
    obsolete within 24 hours. This has no equivalent in traditional sports.
    
  PATCH RECENCY MODIFIER TABLE:

  Patch age             Signal confidence modifier    Notes
  ───────────────────────────────────────────────────────────────────────
  0-7 days (fresh)      ×0.85 on all historical data  High variance; teams adapting
  8-30 days (settling)  ×0.93 on historical data      Patterns emerging; moderate confidence
  31+ days (stable)     ×1.00 (full weight)            Historical patterns reliable

  HOW TO APPLY:
    Identify the most recent significant patch date.
    Calculate days since patch release.
    Apply confidence modifier to ALL historical performance data for both teams.
    The modifier applies to win rates, style preferences, map/hero tendencies.
    
  MAJOR vs MINOR PATCHES:
    Major patches (full rebalance, new season, significant mechanic changes):
      Apply full recency modifier framework regardless of days since release
      Even a 45-day-old major patch may still have fresh modifier if it was extreme
      
    Minor patches (individual adjustments, bug fixes):
      Apply reduced recency modifier:
        0-7 days minor patch: ×0.94 (not ×0.85) — less systemic disruption
        8-30 days minor: ×0.97
        31+ days minor: ×1.00

  PATCH SPECIALIST ADVANTAGE:
    Some teams are documented faster meta-adapters — they perform better in
    fresh patch environments than slower-adapting teams.
    Adaptor premium: ×1.06 for confirmed fast-adapter teams in 0-14 day fresh patch windows
    Apply: check historical win rate in first 2 weeks of major patches vs settled patches.
```

---

## Roster change intelligence

```
ROSTER CHANGE IMPACT — MAGNITUDE COMPARISON TO TRADITIONAL SPORTS:

  ESPORTS vs TRADITIONAL SPORTS ROSTER CHANGE IMPACT:
    Traditional sports (football): key player departure = −3-8% win probability impact
    Esports: star carry player departure = −20-40% win probability impact
    
    Esports roster changes have larger individual impact because:
      Small team size (5 players) → each player is 20% of the team
      Role specialisation is extreme — one player cannot cover another's role
      Chemistry and communication are critical and take time to rebuild
      
  ROLE-SPECIFIC DEPARTURE MODIFIERS:

  Role                  Departure modifier    Notes
  ─────────────────────────────────────────────────────────────────────
  Star carry/fragger    ×0.75               Primary damage output lost
  Secondary carry       ×0.85               Support damage lost; system disrupted
  IGL (in-game leader)  ×0.82               Strategic caller lost; system disruption
  Support player        ×0.92               Less visible but critical for system
  Coach departure       ×0.94               Preparation and strategic identity affected

  ROSTER INTEGRATION TIMELINE — PERFORMANCE MODIFIER:

  Days since change     Performance modifier   Notes
  ─────────────────────────────────────────────────────────────────────
  0-30 days             ×0.88                 Chemistry building; communication rough
  31-60 days            ×0.94                 Settling; improvement visible
  61-90 days            ×0.97                 Nearing full integration
  91+ days              ×1.00                 Full modifier restored

  HOW TO APPLY:
    On any roster change announcement: apply departure modifier immediately.
    Begin integration timeline from the player's first official match with new roster.
    Track each changed player independently if multiple changes occur simultaneously.
    Multiple simultaneous changes: apply compound (multiply) integration modifiers.
    
  REBUILD vs REFRESH SIGNAL:
    Full roster rebuild (3+ players changed): treat as a new team; reset all historical data
    Apply: new_team_confidence_modifier = ×0.75 on all historical performance data
    Timeline: 6+ months for full historical data reliability to re-establish
    
    Partial roster refresh (1-2 players): apply individual role modifiers; preserve other history
```

---

## LAN versus online performance

```
LAN VS ONLINE VARIANCE:

  LAN EVENTS (highest signal reliability):
    Players compete in person at a physical venue.
    Eliminates internet connection variables, reduces technical issues.
    Higher psychological pressure — crowd present.
    Largest tournaments are exclusively LAN.
    Signal reliability: HIGHEST — use LAN performance as primary baseline.
    
  ONLINE EVENTS (lower signal reliability):
    Teams compete remotely from home/bootcamp.
    Subject to connection quality, ping differences, technical issues.
    Lower crowd pressure — home environment.
    
  ONLINE PERFORMANCE MODIFIER:
    Apply: online_performance_modifier = ×0.92 versus LAN baseline for same teams.
    This means a team's online win rate is a less reliable predictor of LAN performance.
    Reverse: do not apply LAN-calibrated expectations to online matches at full weight.
    
  LAN SPECIALISTS vs ONLINE SPECIALISTS:
    Some teams consistently perform above their online baseline at LAN events.
    LAN specialist signal: historical LAN win rate significantly above online win rate.
    Apply: lan_specialist_modifier = ×1.05 for confirmed LAN specialists at LAN events.
    
    Conversely, some teams perform better online (home environment, less pressure).
    Online specialist: historical online win rate above LAN win rate.
    Apply: online_specialist_modifier = ×1.03 for confirmed online specialists at online events.
    
  TOURNAMENT WEIGHT BY FORMAT:
    Major LAN events: highest signal weight (see title-specific files for multipliers)
    Minor LAN events: moderate signal weight
    Online league season: apply ×0.92 modifier to all historical pattern reliability
    Online qualifiers: lowest signal weight — high technical variance
```

---

## Regional performance patterns

```
ENDURING REGIONAL DOMINANCE — REASONING FRAMEWORK:

  These patterns are enduring structural characteristics of the esports ecosystem.
  They are not current form — they are persistent structural advantages.

  CS2 / COUNTER-STRIKE:
    CIS and Eastern European heritage: historically dominant in CS titles
    Apply: cis_cs_heritage_modifier = ×1.08 for confirmed CIS-heritage CS2 organisations
      in international competition (vs Western European or North American opponents)
    Foundation: deep talent pipeline, culture of individual fragging skill

  LEAGUE OF LEGENDS:
    Korean (LCK) and Chinese (LPL) teams: historically dominate Worlds international
    Apply: kor_chn_lol_international_modifier = ×1.10 vs Western/other region opponents
    Western teams (LEC, LCS) at international events:
      Apply: western_lol_international_modifier = ×0.85 vs Korean/Chinese opponents
    Foundation: superior infrastructure, longer professional history in the region

  DOTA 2:
    Chinese teams: historical dominance at TI (The International)
    Eastern European teams: consistent podium presence
    Western and SEA teams: more volatile — higher variance at international events
    Apply: chn_dota_international_modifier = ×1.08 for confirmed Chinese Dota 2 orgs at TI
    
  VALORANT:
    EMEA region has shown strongest performance in early Valorant history
    Pacific and Americas are competitive; no dominant structural pattern yet established
    Valorant regional modifiers should be applied with lower confidence than older titles
    Apply: ×0.90 confidence to any regional modifier in Valorant until pattern is established

  INTER-REGIONAL MATCH VARIANCE:
    When teams from different regions meet with limited historical sample:
    Apply: inter_regional_variance_modifier = ×0.90 on signal confidence
    This reflects limited head-to-head data — patterns are less reliable.
    Exception: well-documented international records (Worlds, TI, Majors) with
      5+ historical meetings allow standard confidence.
```

---

## Prize pool motivation

```
PRIZE POOL AS MOTIVATION SIGNAL:

  WHY PRIZE POOL MATTERS:
    In esports, prize pools vary enormously — from $10,000 at minor events
    to $40M+ at The International. This creates measurable performance motivation.
    Traditional sports have more uniform financial incentives.

  PRIZE POOL MODIFIER TABLE:
    World championship level (top-5 all-time prize pool for this title): ×1.20
    Major tournament level (top-20% of annual prize pools for this title): ×1.10
    Regular season / league play: ×1.00 (baseline motivation)
    Minor events / qualifiers: ×0.95 (lower motivation for established teams)
    
  PRIZE POOL COMPOUND WITH ROSTER QUALITY:
    High prize pool × high roster quality = maximum motivation signal
    Apply: compound_modifier = prize_pool_modifier × roster_quality_modifier
    
  CROWD-FUNDED PRIZE POOLS (Dota 2 TI model):
    Some events use community funding that grows over time.
    Rising prize pool as tournament approaches = increasing motivation signal.
    Apply: rising_prize_pool_momentum_modifier = ×1.03 per week of community funding
    growth in the month before the event.
```

---

## Esports token demand cycle

```
ANNUAL ESPORTS TOKEN DEMAND CYCLE (universal — all titles):

  MAJOR TOURNAMENT ANNOUNCEMENT (2-6 months before event):
    Demand builds 2-4 weeks after announcement
    Build modifier: ×1.05 to ×1.08 approaching event

  PRE-TOURNAMENT QUALIFIER PERIOD:
    If team must qualify (non-direct invite): qualification risk discount applies
    Qualified: remove discount; demand builds
    Failed qualification: demand cliff (apply departure decay framework levels)

  TOURNAMENT GROUP STAGE:
    Demand holds or builds depending on team performance
    Strong group stage (top performance): ×1.10 during stage

  TOURNAMENT KNOCKOUT STAGE (per round survived):
    Round of 16 / top 16: ×1.05
    Quarter-final / top 8:  ×1.10
    Semi-final / top 4:     ×1.15
    Grand Final:            ×1.25

  TOURNAMENT VICTORY:
    Major title: +30-50% demand spike (48-72h peak)
    World championship: +60-100% demand spike
    Victory baseline: 10-15% permanently above pre-tournament baseline

  POST-TOURNAMENT DECAY:
    Decay over 3-6 weeks to new (elevated) baseline
    Losing finalist: −10-15% immediate drop; recovers to near baseline in 2-3 weeks

  OFF-SEASON:
    Minimum demand period; roster change signals dominate
    Roster speculation creates brief demand spikes
    Apply: off_season_volatility_flag — roster moves are the primary CDI events

ESPORTS vs TRADITIONAL SPORTS DEMAND COMPARISON:
  Higher peak spikes: esports ×1.60-2.00 at World Championship vs football UCL ×1.40
  Longer off-seasons with lower baseline: typically 3-4 months vs 1-2 months football
  Patch cycle volatility: additional CDI events not present in traditional sports
  Roster change impact: 2-5× the demand impact of equivalent player move in football
  All esports tokens: DEMAND ONLY — no FTP PATH_2 confirmed for any esports token
```

---

## Compatibility

**Base domain:**        `sports/esports/sport-domain-esports.md`
**CDI framework:**      `fan-token/esports-token-intelligence/`
**Dota 2:**             `sports/esports-dota2.md`
**CS2:**                `sports/esports-cs2.md`
**LoL / Valorant:**     `sports/esports-moba-tactical.md`

---

*SportMind v3.97.30 · MIT License · sportmind.dev*
*All esports tokens are demand-only — no FTP PATH_2 confirmed for any esports token*
*Verify partnership status before applying any token demand signal*
