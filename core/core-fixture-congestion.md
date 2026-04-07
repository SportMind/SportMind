# Fixture Congestion Intelligence — SportMind Core

Fixture congestion — multiple high-intensity matches within a short window — creates
fatigue, rotation pressure, and squad depth requirements that standard form analysis
misses entirely. This skill gives AI agents a universal congestion framework with
sport-specific parameters.

---

## The congestion signal

```
WHAT CONGESTION MEASURES:
  Days since last match × match intensity × travel distance × squad depth available

WHAT IT PREDICTS:
  → Performance degradation (covered by athlete modifier fatigue component)
  → Rotation likelihood (key player availability becomes uncertain)
  → Recovery variance (older players, injury returnees more affected)
  → Tactical shift (managers change formations under congestion)

KEY INSIGHT: Congestion affects the TEAM more than any single player modifier
can capture. The athlete modifier pipeline handles individual fatigue. This
skill handles the systemic team-level congestion effect.
```

---

## Universal congestion tiers

```
TIER 1 — SEVERE CONGESTION (≥3 competitive matches in 7 days):
  Modifier: × 0.88 on full-strength signal
  Rotation very likely for some positions
  Injury risk elevated: +15% above normal for soft tissue injuries
  Examples: Champions League + weekend Premier League + midweek cup
            NBA back-to-back-to-back (3 in 3)
            NRL clubs during State of Origin period (reduced squads)

TIER 2 — HIGH CONGESTION (3 matches in 8–12 days):
  Modifier: × 0.93
  Rotation likely in cup competitions or weakest opponents
  Key players managed: 70–80 minutes likely for high-mileage players
  Examples: Standard European double-gameweek
            NBA back-to-back
            AFL clubs with interstate travel mid-week

TIER 3 — MODERATE CONGESTION (3 matches in 13–18 days):
  Modifier: × 0.97
  Minor rotation expected; core XI largely unchanged
  Watch: minutes load for players returning from injury

TIER 4 — STANDARD (2 matches per week, normal rest):
  Modifier: × 1.00 (baseline — no congestion adjustment)

TIER 5 — EXTENDED REST (8+ days since last match):
  Modifier: × 1.03 (well-rested; may also indicate match rustiness)
  Watch: First match back after international break or enforced rest
```

---

## Football / Soccer — congestion specifics

```
KEY CONGESTION WINDOWS (annual calendar):
  December (Premier League/La Liga/Bundesliga): Holiday fixture pile-up
  → Premier League clubs can play 6+ matches in December
  → Spanish/German clubs have fewer matches; significant advantage in European competition
  
  February/March (Champions League + domestic): European teams under highest load
  February/March (FA Cup + Premier League): Domestic cup adds a match per week
  
  International breaks: Club matches interrupted; players return fatigued from travel
  → Some players return with 1–2 days' preparation; applies Tier 2 modifier

ROTATION PATTERNS BY MANAGER:
  Rotation-heavy managers (Pep Guardiola, Jurgen Klopp historically):
  Rotate significantly in cups and weaker league matches under congestion
  → Increase uncertainty on XI prediction; widen confidence intervals
  
  Rotation-light managers (often lower-table managers with thinner squads):
  Play same XI regardless; fatigue accumulates in key players
  → Apply player-level fatigue modifier (athlete skill) to high-minute players

TRAVEL FATIGUE AMPLIFIER:
  Away matches 500+ km from home base: Add Tier +1 congestion modifier
  Example: Russian clubs in European competition before 2022 bans
  Example: Australian clubs in AFC Champions League
  Transatlantic travel (pre-season tours): Apply Tier 1 regardless of fixture count

SQUAD DEPTH INTERACTION:
  Rich squads (Manchester City, Real Madrid): Congestion less punishing
  Apply congestion modifier at 70% strength for squads ranked top-5 in depth
  
  Thin squads (promoted clubs, financially restricted clubs): Congestion more punishing
  Apply congestion modifier at 130% strength for squads ranked bottom-5 in depth
```

---

## Basketball (NBA) — back-to-back framework

```
NBA CONGESTION IS DOCUMENTED AND MEASURABLE:

Back-to-back (B2B): Two games on consecutive days
  → Teams play 15–20 B2Bs per season
  → Second night of B2B: documented −3.2 points per 100 possessions on average
  → Apply: × 0.93 modifier for second game of B2B

B2B on road: Second game on road after road game
  → More severe: documented −4.5 points per 100 possessions
  → Apply: × 0.90 modifier

Load management / rest decisions:
  NBA teams rest star players on B2Bs → immediate availability uncertainty
  Agent rule: When B2B identified, load athlete modifier FIRST
  (star player rested = severe modifier) before applying congestion modifier
  Do not double-count: Apply the larger of the two modifiers, not both

3-in-4 nights (3 games in 4 days):
  → Rare but occurs; most severe NBA congestion
  → Apply: × 0.87 modifier for third game

DATA SOURCE:
  NBA.com schedule, Basketball-Reference.com game logs
```

---

## Rugby League (NRL / Super League) — State of Origin congestion

```
STATE OF ORIGIN CONGESTION (NRL — highest severity rugby league congestion):

During Origin window:
  → Queensland and NSW players return from Origin series with 0–2 days' recovery
  → Clubs playing the Origin players at full intensity: Tier 1 congestion applies
  → Clubs without Origin players: potential advantage; apply × 1.04 reverse benefit

Origin game played Wednesday → NRL club game Sunday:
  → 4 days' recovery for Origin players
  → Apply Tier 2 modifier to clubs fielding 3+ Origin players

Origin disruption modifier (from athlete-intel-rugby-league.md):
  This core skill's congestion framework stacks with that modifier
  Combined: Apply athlete modifier first, then congestion modifier

SUPER LEAGUE MAGIC WEEKEND:
  All Super League clubs play once in a single weekend
  → No congestion created but unusual travel and conditions
  
WORLD CUP INTERRUPTIONS:
  International windows remove key players; returning players have travel fatigue
  Apply Tier 2 modifier for first NRL match after extended international window
```

---

## American Football (NFL) — short week framework

```
NFL CONGESTION OCCURS WHEN:
  Short week (Thursday Night Football after Sunday game):
  → 4 days' recovery instead of standard 7
  → Historical data: TNF teams average −1.8 points vs spread on short rest
  → Apply: × 0.94 modifier for Thursday Night Football team on short week
  → Exception: Bye week before TNF — no modifier needed

CONSECUTIVE AWAY GAMES:
  3+ consecutive away games: Documented −2.1 points per game vs home baseline
  Apply: × 0.95 for third consecutive away game

LATE-SEASON CUMULATIVE FATIGUE (Weeks 14–17):
  Teams with 0 or 1 losses managing playoff seeding: may rest key players
  → Monitor depth chart reports carefully in final 4 weeks

DATA SOURCE:
  NFL.com schedule, Pro-Football-Reference.com rest data, 
  OddsShark injury/rest database
```

---

## Cricket — tour fatigue and congestion

```
INTERNATIONAL TOUR CONGESTION:
  Modern cricket schedules are the most congested in sport history
  Test match → T20 series → ODI series with days between

DAYS BETWEEN FORMATS:
  0–1 days between Test and limited-overs: Severe mental/physical fatigue
  2–3 days: Significant; apply Tier 2 modifier
  4+ days: Normal; no congestion modifier

IPL PLAYER AVAILABILITY CONGESTION:
  IPL players return from international duty mid-tournament
  → New arrivals need 1 match adaptation; apply × 0.95 for first IPL match
  
TEST SERIES DEEP INTO LONG SERIES:
  By Test 4–5 of a 5-match series, fast bowlers are significantly fatigued
  → Leading quick bowlers: Apply Tier 2 modifier from Test 4 onward
  → Batting is less affected by physical congestion

DATA SOURCE: ESPNcricinfo schedule, Cricket.com.au
```

---

## MMA — fight camp congestion (fight frequency)

```
FIGHT FREQUENCY SIGNAL:
  Unlike team sports, MMA congestion is measured across months not days

OPTIMAL CAMP LENGTH: 8–12 weeks
  Fighters competing more frequently: progressive camp quality decline
  Fighters with >3 fights in 12 months: Flag for review (injury/exhaustion risk)

SHORT NOTICE REPLICATIONS:
  <2 weeks notice: Partial camp; apply Tier 1 congestion equivalent
  2–4 weeks notice: Partial camp; apply Tier 2 congestion equivalent
  4+ weeks with full camp: No congestion modifier

This overlaps with injury-intel-mma.md — cross-reference for late replacement protocol
```

---

## Cycling — Grand Tour fatigue curve

```
GRAND TOUR CONGESTION IS PROGRESSIVE:
  This is covered in detail in:
  - sports/cycling/sport-domain-cycling.md (stage-level fatigue)
  - core/injury-intelligence/injury-intel-cycling.md (DNF prediction)
  
  For GC riders: Apply congestion modifier from Stage 15 onward
  For sprinters: Apply from Stage 18 onward (different fatigue profile)
  For domestiques: Apply from Stage 12 onward (higher daily workload)
```

---

## Agent integration

```
LOADING INSTRUCTION:
  Load AFTER athlete modifier (Layer 2) and BEFORE final signal output
  Apply to the signal AFTER individual athlete modifiers are calculated
  
  Order of modifier application:
  1. Base signal score (from platform)
  2. Athlete modifier (Layer 2) — individual player adjustments
  3. Congestion modifier (this file) — team-level fatigue
  4. Officiating modifier (core-officiating-intelligence.md)
  5. Weather modifier (core-weather-match-day.md)
  6. Macro modifier (Layer 5)
  → Final adjusted signal score

CONGESTION MODIFIER DOES NOT APPLY:
  Individual sports (tennis, golf, athletics, snooker, darts)
  → Use athlete modifier fatigue component only
  → These sports have sport-specific fatigue frameworks in athlete skills
  
SPECIAL CASE — ROTATION:
  If confirmed rotation (team fielding B team / resting stars):
  → Do not apply congestion modifier; apply direct availability modifier instead
  → Confirmed rotation is captured by athlete modifier (Phase 2 lineup confirmation)
  → Congestion modifier is for UNCERTAINTY phase before lineup confirmation
```

*MIT License · SportMind · sportmind.dev*
