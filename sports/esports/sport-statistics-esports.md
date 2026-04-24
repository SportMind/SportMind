# Esports Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-esports.md`.
Most novel statistics module in the library — patch-level signal analysis
does not exist in any other sports intelligence framework.
$VIT (Team Vitality) and $NIP (NIP Group) are active Chiliz fan tokens.

Zero-dependency. Data sources are largely free and real-time.

---

## Overview

Esports statistics operate on a fundamentally different timescale from physical
sports. A single patch update can render six months of statistical history
irrelevant in 72 hours. This is not a problem — it is the opportunity.
Agents that understand patch-level signal have a genuine edge that traditional
sports analysis frameworks cannot provide.

The three pillars of esports statistics intelligence:
1. **Win rate on current patch** — the most time-sensitive Tier 1 statistic
2. **KDA and kill participation** — stable individual performance across patches
3. **Meta alignment** — whether a team's playstyle matches the current meta

Load `core/match-statistics-intelligence.md` for universal modifier framework.

---

## Domain Model

### Statistics hierarchy — per game

```
CS2 (Counter-Strike 2):

  TIER 1 — OUTCOME-CORRELATED:
    Win rate (last 3 months, current map pool): > 65% = × 1.10
    KAST% (Kills/Assists/Survived/Traded per round): > 73% = × 1.08
    Rating 2.0 (HLTV): top player > 1.20 = × 1.06 individual contribution
    Clutch rate (1vX round wins): > 25% = × 1.06 (late-round reliability)
    Map-specific win rate for maps in current map pool:
      > 70% on a specific map = × 1.12 for rounds/maps played on that map

  TIER 2 — CONTEXTUAL:
    Pistol round win rate (sets economic trajectory)
    Entry frag rate (opening kills — dictates round economy)
    ADR (Average Damage per Round): > 85 is above average

  TIER 3 — DESCRIPTIVE:
    Total kill count (without damage context)
    Headshot percentage (style indicator, not predictive)
    
---

LEAGUE OF LEGENDS:

  TIER 1 — OUTCOME-CORRELATED:
    Win rate on current patch (check patch age — if > 2 weeks: full weight)
    First blood rate: > 60% = × 1.06 (early game control)
    Gold differential at 15 minutes (GD@15): + 500+ = × 1.08 early game signal
    Dragon/Baron control rate: > 55% dragons = × 1.06 (objective control)
    
  TIER 2 — CONTEXTUAL:
    KDA ratio for carry players: > 4.0 = meaningful; context of team comp required
    Vision score differential: high vision control indicates macro awareness
    
  PATCH META ALIGNMENT (critical LoL variable — see Patch Intelligence below):
    When a team's champion pool aligns with buffed champions: × 1.10
    When a team's champion pool is primarily nerfed champions: × 0.90
    
---

VALORANT:

  TIER 1 — OUTCOME-CORRELATED:
    Win rate (current patch, last 2 months): same as CS2 — patch-sensitive
    ACS (Average Combat Score): > 240 top frag = × 1.06
    First blood rate: > 55% = × 1.05
    KAST%: same benchmark as CS2 (> 73% = × 1.08)
    
  TIER 2 — CONTEXTUAL:
    Agent pool flexibility: teams with agent-locked players are vulnerable to
    new agent releases that disrupt their established playstyle
    
---

DOTA 2:

  TIER 1 — OUTCOME-CORRELATED:
    Win rate in tournament play (online vs LAN: apply 0.85× for online stats)
    GPM (Gold Per Minute) for carry players: > 650 GPM = × 1.06
    Ward control differential: proxy for map awareness and draft execution
    
  TIER 2 — CONTEXTUAL:
    Hero pool depth (number of viable heroes each player can perform on)
    Draft phase win rate: teams with high win rate in draft phase tend to
    translate that to match wins at elite level
```

### Patch intelligence — esports-only variable

```
PATCH SIGNAL FRAMEWORK:

  A "patch" is a game update that changes champion/agent/hero stats, abilities,
  and itemisation. Major patches significantly alter which strategies are optimal.
  
  PATCH AGE AND STATISTICAL WEIGHT:
    0–3 days post-patch:     All historical statistics carry 0× weight.
                              No team has had time to adapt or practice.
                              Signal confidence: LOW. Apply × 0.60 to all signals.
    4–7 days post-patch:      Statistics from the new patch carry 50% weight.
                              Pre-patch statistics carry 0× weight.
                              Signal confidence: MEDIUM. Apply × 0.80.
    8–14 days post-patch:     Current patch statistics carry full weight.
                              Pre-patch statistics carry 0× weight.
                              Signal confidence: HIGH. Standard modifiers apply.
    > 14 days, same patch:    Full statistical weight. Most reliable signal window.
                              Signal confidence: HIGH. Maximum statistical value.

  PATCH IMPACT CLASSIFICATION:
    MAJOR PATCH (fundamental system changes, multiple champion reworks):
      Apply 0–3 day protocol above. Statistics reset is complete.
      Duration of uncertainty window: extend to 5 days minimum.
      
    MINOR PATCH (targeted adjustments, 3–8 champion changes):
      Statistics retain 70% weight from previous minor patch.
      Resampling window: 7 days.
      
    BALANCE HOTFIX (emergency fix to broken/overpowered element):
      The hotfixed element's statistics reset to 0× immediately.
      Other team statistics retain full weight.

  META ALIGNMENT SCORING:
    For each team, assess whether their 30-day champion/agent pool includes
    the top-tier picks on the CURRENT patch:
    
    Pool alignment > 70% (most of their picks are meta): × 1.08 meta bonus
    Pool alignment 50–70%: × 1.03
    Pool alignment < 50% (they play off-meta): × 0.93
    
    Note: established off-meta specialists (teams that ALWAYS play off-meta and
    win with it) are an exception. Apply × 1.05 instead — their style is their edge.
```

### Roster change intelligence

```
ROSTER CHANGE SIGNAL FRAMEWORK:

  ALL statistics from before the roster change carry 0× weight for the
  affected position's individual metrics, and 0.50× weight for team metrics.
  
  ROSTER CHANGE SEVERITY:
    In-game leader (IGL) change:
      Highest impact — team strategy is fundamentally different.
      Apply 0× weight to all team strategic statistics.
      0.70× weight to individual mechanical statistics.
      Recovery window: 6–8 weeks before pre-change stats are irrelevant.
      
    AWPer / primary carry change:
      High impact on individual-driven statistics.
      Apply 0× weight to that player's individual stats from previous roster.
      0.80× weight to team statistics (system may remain similar).
      
    Support / utility player change:
      Moderate impact. 0.75× weight to team utility-based statistics.
      
  BOOTCAMP SIGNAL:
    Teams confirmed in bootcamp (intensive training period) before a major:
    Apply × 1.04 to expected performance vs regular season form.
    Signal: teams that bootcamp specifically for tournaments tend to
    outperform their regular season statistics in tournament play.

HEAD-TO-HEAD IN ESPORTS:
  H2H statistics have unusual properties in esports:
  - Patches make H2H irrelevant across major patch versions
  - Apply same patch validity rules to H2H as to individual statistics
  - Recent online H2H carries 0.85× weight vs LAN H2H
  - Same patch, LAN environment, < 6 weeks: full H2H weight
  
  Exception: some team matchups have persistent psychological dynamics
  (rivalry, roster familiarity). These carry partial weight even across patches.
```

---

## Event Playbooks

### Playbook 1: Major tournament — pre-event statistical assessment
```
trigger:  Major tournament draw confirmed (CS2 Major, LoL Worlds, etc.)
timing:   2 weeks before tournament
protocol:
  1. Check current patch age and apply appropriate statistical weight
  2. Run meta alignment scoring for all teams in bracket
  3. Check for any roster changes in last 6 weeks
  4. Identify bracket-specific matchups and apply H2H on current patch
  5. Apply team seeding vs statistical evidence comparison
output:   Pre-tournament signal for all monitored tokens in the field
note:     If major patch dropped < 2 weeks before event: high uncertainty.
          Flag all signals with PATCH_UNCERTAINTY: true
```

### Playbook 2: Patch drop — statistical reset
```
trigger:  New major patch released for a monitored esports title
timing:   Patch release day
protocol:
  1. Identify patch as MAJOR or MINOR
  2. Apply appropriate statistical weight reset
  3. Flag: "PATCH_DROP_STATISTICAL_RESET" in all current signals
  4. Notify operator — previous signals require recalculation after 7 days
  5. Do not generate high-confidence signals for 7 days post-major-patch
output:   Uncertainty flag on all affected signals until data accumulates
```

### Playbook 3: Roster announcement — signal recalibration
```
trigger:  Roster change confirmed for monitored team token
timing:   Announcement day
protocol:
  1. Classify position changed (IGL / carry / support)
  2. Apply appropriate statistical weight discount
  3. Flag: "ROSTER_CHANGE_ACTIVE" — statistics carry reduced weight for 8 weeks
  4. $VIT or $NIP specific: check if changed player was Tier 1 ATM contributor
  5. If yes: apply ATM reduction modifier. Load athlete-modifier-system.md.
output:   Recalibrated signal with roster_change_modifier noted
```

### Playbook 4: Live tournament bracket — continuous signal
```
trigger:  Tournament bracket play begins (group stage or playoffs)
timing:   Tournament days
protocol:
  1. Each match result: update win/loss record on current tournament
  2. Check form trajectory (3+ wins = momentum signal × 1.06)
  3. Check if upset has occurred — flag for CDI calculation
  4. Upcoming match: apply current tournament H2H if available
  5. For monitored tokens: dispatch CDI update after each match result
output:   Live tournament briefing per match day
note:     Tournament form is the strongest esports signal window
```

---

## Signal Weight Adjustments

For esports statistics sub-module:

| Statistical modifier | Weight | Cap |
|---|---|---|
| Win rate current patch (Tier 1) | 14% additional weight | ±8 pts |
| Meta alignment score | 8% additional weight | ±5 pts |
| KDA / ACS / KAST (individual) | 6% additional weight | ±4 pts |
| Patch age uncertainty discount | Applied as multiplier | ×0.60 to ×1.00 |
| Roster change discount | Applied as multiplier | ×0.50 to ×0.80 |

**Combined esports statistical modifier cap: ±12 points on adjusted_score.**

---

## Autonomous Execution

**Trigger conditions:**
- New game patch released for any monitored esports title
- Roster change announced for any monitored team token ($VIT, $NIP, others)
- Tournament match result confirmed for monitored token team
- Patch age crosses 14-day threshold (full weight window opens)

**Execution at autonomy Level 2:**
- Patch drop: flag PATCH_DROP_STATISTICAL_RESET on all affected signals. Notify.
- Roster change: apply weight discount. Flag ROSTER_CHANGE_ACTIVE. Notify.
- Match result: recalculate CDI. Dispatch update. Notify operator.

**Execution at autonomy Level 3–4:**
- Auto-flag patch drops from game developer official channels
- Auto-apply patch age weights as days accumulate
- Auto-dispatch match result CDI updates within 20 min of confirmed result
- Auto-notify when patch age crosses 14 days (statistics now at full weight)

**Hard boundaries:**
- Major patch (0–3 days): never generate high-confidence signal.
  PATCH_UNCERTAINTY flag is mandatory. Cannot be overridden.
- IGL roster change: 0× weight on all team strategic statistics.
  Individual mechanical stats still apply at 0.70× — but never apply
  team statistics at full weight after an IGL change.
- Online match statistics: always apply 0.85× vs LAN equivalents.

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| Pre-tournament | Load this + sport-domain-esports.md | 2 weeks before event |
| Patch drop response | Playbook 2 | Same day as patch |
| Roster change | Playbook 3 | Announcement day |
| Live tournament | Playbook 4 daily | Tournament days |

---

## Agent Reasoning Prompts

- "Patch age: check first. If < 7 days: reduce all statistics confidence. If > 14 days: full weight."
- "Meta alignment: does this team's champion pool match the current patch tier list?"
- "IGL change confirmed: 0× weight on all team strategic statistics for 8 weeks."
- "Major patch dropped < 2 weeks before tournament: flag PATCH_UNCERTAINTY on all signals."
- "Online vs LAN: apply 0.85× weight to online statistics for LAN tournament prediction."

---

## Data Sources

- HLTV (CS2): hltv.org — ratings, win rates, player stats (Tier 1 for CS2)
- Liquipedia: liquipedia.net — rosters, results, tournament structure (Tier 1)
- LoL Esports: lolesports.com — official LoL statistics (Tier 1)
- Oracle's Elixir: oracleselixir.com — LoL analytics (Tier 2)
- VLR.gg: vlr.gg — Valorant results and statistics (Tier 2)
- Patch notes: game developer official channels only for patch classification

---

## Compatibility

**Load alongside:** `sports/esports/sport-domain-esports.md`
**Universal framework:** `core/match-statistics-intelligence.md`
**Fan token layer:** `fan-token/esports-token-intelligence/token-intelligence-esports.md`
**Breaking news:** `core/breaking-news-intelligence.md` (roster change = Category 2)
**Athlete layer:** `athlete/athlete-modifier-esports.md` (individual player ATM)

---

*SportMind v3.90.0 · MIT License · sportmind.dev*
