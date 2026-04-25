# NASCAR — SportMind Domain Skill

Sport-specific intelligence for NASCAR — the NASCAR Cup Series, the premier level
of American stock car racing.

---

## Overview

NASCAR is the most popular domestic motorsport in the United States and one of
the highest-attended sporting events in North America. Unlike Formula 1 (road
circuits, constructors championship, aerodynamic engineering) or MotoGP
(motorcycles, rider-centric), NASCAR is defined by oval tracks, door-to-door
racing at 200mph+, drafting dynamics, and a playoff structure unique to motorsport.

The sport's audience is predominantly North American, deeply loyal, and increasingly
digitally engaged. The NASCAR Cup Series currently has no active fan token
but represents a credible expansion target given the sport's massive commercial
infrastructure and the 2026 FIFA World Cup's activation of the North American
sports market.

---

## Domain Model

### Season Calendar

```
NASCAR CUP SERIES (36 regular season + 10 playoff races):

REGULAR SEASON (Feb–Sep, ~26 races):
  Daytona 500 (Feb): Season opener; most prestigious single race
  Superspeedways, short tracks, intermediate ovals, road courses
  
PLAYOFFS / NASCAR CUP PLAYOFFS (Sep–Nov, 10 races):
  16 drivers qualify after regular season
  4 rounds of elimination (each round = 3 races)
  Round of 16 → Round of 12 → Round of 8 → Championship 4
  
CHAMPIONSHIP 4 (Phoenix, Nov):
  4 remaining drivers race for the title at Phoenix Raceway
  Any of the 4 can win regardless of season points — pure race result determines champion
  
SPECIAL EVENTS (non-points or exhibition):
  Clash at the Coliseum (LA Memorial Coliseum): pre-season exhibition
  All-Star Race (variable): mid-season; no points; significant purse
```

### Track Type Classification — the most critical variable

NASCAR tracks are fundamentally different from each other. Track type determines
which cars, setups, and drivers have structural advantages.

```
SUPERSPEEDWAYS (Daytona, Talladega):
  2.5-mile ovals; restricted engine power (restrictor plate racing)
  Speeds: 190–205mph in packs
  DEFINING CHARACTERISTIC: Drafting — cars must draft in packs; single car is slow
  Strategy: position within the pack is everything
  Crash probability: EXTREME (big crashes are structural, not random)
  Driver skill: pack racing awareness; drafting partners matter
  Predictability: LOWEST — any top-30 driver can win; random factors dominant
  
INTERMEDIATE OVALS (1–2 miles: Charlotte, Las Vegas, Atlanta, Michigan):
  Most common track type; ~15 races per season
  Speeds: 170–195mph
  Strategy: tyre management + pit strategy + handling
  Driver skill: balance and smooth driving to preserve tyres
  Predictability: MODERATE — car quality (Chevy vs Ford vs Toyota) matters here
  
SHORT TRACKS (< 1 mile: Bristol, Richmond, Martinsville):
  Slower but highly competitive; door-to-door racing
  Restarts are extremely consequential (inside vs outside lane)
  Crash probability: HIGH (traffic, tight corners)
  Driver skill: restarts, short-run pace, aggression management
  Predictability: MODERATE-LOW — physical driving matters; chaos high
  
ROAD COURSES (Circuit of the Americas, Sonoma, Watkins Glen):
  Left AND right turns; technical driving required
  Specialists: some drivers dramatically outperform on road courses
  Traditional oval drivers sometimes underperform here
  Driver skill: braking points, technical cornering — different from oval
  Predictability: MODERATE — road course specialists identifiable
  
DIRT (Bristol Dirt Race, once per season):
  Only dirt track in the modern Cup schedule
  Extreme variability; limited data history
  Predictability: LOWEST after superspeedways
```

---

## Manufacturer and Team Advantage

```
MANUFACTURER TIER (changes year to year — check current season):
  Chevrolet, Ford, Toyota: the three manufacturers
  Each manufacturer has an alliance of teams sharing data and engines
  
  Toyota historically strongest 2017–2023
  Chevrolet regaining parity 2023–24
  Ford typically third but competitive at specific tracks
  
  TEAM TIER (within manufacturer):
    Hendrick Motorsports (Chevrolet): most resourced; consistent contender
    Joe Gibbs Racing (Toyota): elite team; multiple championships
    Team Penske (Ford): elite team; superspeedway and road course strength
    
    Mid-tier: Trackhouse, Stewart-Haas, 23XI Racing (growing)
    Lower-tier: Smaller teams with fewer resources; rarely win
    
  CHARTER SYSTEM:
    Guaranteed starting positions for chartered teams (top ~30 cars)
    Open teams (non-chartered) must qualify on speed — uncertainty on entry
```

---

## The Playoff Structure — NASCAR's unique format

NASCAR's playoff system is unlike any other motorsport and creates specific
prediction patterns.

```
PLAYOFF MECHANICS:
  Win in regular season: automatic entry to playoffs
  Win in playoffs: automatic advance to next round
  
  ROUND STRUCTURE (each round: 3 races):
    After round 3 races, bottom 4 of remaining drivers are eliminated
    Based on: race wins first, then points
    
  CHAMPIONSHIP 4 (Phoenix):
    4 drivers who survived all elimination rounds race for the title
    PURE RACE RESULT: whoever of the 4 finishes highest wins the championship
    Points are irrelevant for the Championship 4 race
    
  KEY IMPLICATION:
    In the regular season, winning races matters more than points consistency
    A driver can win 3 races and miss the playoffs with bad consistency
    But a driver with 0 wins and consistent top-10s can make the playoffs
    
  CHAMPIONSHIP 4 RACE:
    Phoenix is an intermediate oval — manufacturer and setup matter here
    Driver skill at Phoenix specifically (not general championship form)
    This is the single highest-stakes event in the NASCAR season
```

---

## Drafting — superspeedway-specific intelligence

```
DRAFTING MECHANICS (Daytona and Talladega only):
  Restrictor plate limits engine output; aerodynamic drag is controlling factor
  Cars in packs: lead car pushes air for followers; 2-3 car drafts are faster than solo
  
  DRAFTING PARTNERSHIPS:
    Pre-race drafting alliances are negotiated (same manufacturer usually)
    A driver with a strong drafting partner is at a structural advantage
    Check: who has been pushing whom in practice? (broadcast and team radio give clues)
    
  CRASHES (THE BIG ONE):
    At superspeedways, a single crash can collect 15–20 cars at once
    "The Big One" is a statistical near-certainty at Daytona and Talladega
    Drivers in the back of the pack when "the big one" hits are safer
    
    DAYTONA 500 SPECIFIC:
      Most prestigious race of the year; most watched NASCAR event
      Highest crash probability of any event; unpredictability is structural
      Agent rule: In Daytona 500 predictions, reduce sizing significantly.
      Even the dominant car may not survive to the finish.
```

---

## Pit Strategy — the hidden game

```
PIT STOP INTELLIGENCE:
  4-tyre stop: 11–13 seconds (standard; most common)
  2-tyre stop: 7–8 seconds (saves time; trades tyre quality)
  Fuel-only stop: ~7 seconds (saves tyres; gamble on fuel mileage)
  
  Track position vs tyre quality tradeoff:
    Staying out (not pitting): gain track position; risk worn tyres
    Early pit: fresh tyres; lose track position; need to pass back through traffic
    
  STRATEGY SIGNAL:
    Caution (yellow flag) deployment timing dramatically changes strategy
    Team with tyres vs team without: significant gap under caution
    Final caution timing determines if fuel-only gamble wins or loses
    
RESTARTS — highest leverage moment in short track races:
  Inside lane vs outside lane at restart: inside lane has statistical advantage
  Track-specific: some tracks favour inside lane more strongly than others
  Front row position at restart: the most contested position in NASCAR
```

---

## Event Playbooks

### Playbook 1: Daytona 500 — Narrative Peak
```
trigger:  Daytona 500 race week (annual)
entry:    Days before race (Speedweeks narrative building)
exit:     48h post-race
filter:   No superspeedway prediction for individual winner — too unpredictable
          Focus on: narrative around manufacturers, storylines, returning champions
sizing:   0.85× on any specific winner prediction (reduce for randomness)
note:     The Daytona 500 is the most-watched NASCAR event — Super Bowl equivalent
          for the sport's fans. Winner narrative sustains for weeks. But the race
          itself has the lowest winner predictability in the series.
```

### Playbook 2: Dominating Intermediates — Car Best in Class
```
trigger:  One manufacturer consistently running 1–2 fastest in practice at an
          intermediate oval; confirmed setup advantage
entry:    After happy hour practice (final practice session)
exit:     Race completion
filter:   No weather disruption expected
          Elite team + intermediate oval (not short track or superspeedway)
sizing:   1.10× — car quality at intermediate ovals is the most reliable signal
```

### Playbook 3: Playoff Elimination Race — Win-or-Out
```
trigger:  Driver on the playoff cutline (10th–12th in round) needing a win
entry:    Pre-race (after starting grid set)
exit:     Race completion
filter:   Driver is in a strong car; has won at this track type before
          Not a superspeedway (too random for motivated win prediction)
sizing:   0.95× — desperation can improve performance; also increases risk-taking
note:     Drivers who must win to advance change their approach — more aggressive,
          more willing to make contact. This increases their win probability AND
          their crash probability simultaneously.
```

### Playbook 4: Championship 4 — Phoenix
```
trigger:  NASCAR Championship 4 race at Phoenix Raceway
entry:    Week of championship race (sustained narrative)
exit:     Race result confirmed
filter:   Check Phoenix-specific track record for all 4 remaining drivers
          Manufacturer strength at Phoenix specifically
sizing:   1.25× — single-elimination format; any of 4 can win
note:     Championship 4 is the clearest prediction framework in NASCAR.
          4 known drivers; track history is available for all 4 at Phoenix;
          manufacturer advantage at that specific track is researchable.
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| Daytona 500 win | +25–50% (most prestigious) |
| Regular season win (standard) | +8–18% |
| Playoff round win (advances) | +10–20% |
| Championship win | +30–55% |
| Playoff elimination | -15–30% |
| Championship 4 appearance | +15–25% |

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 40% | Race results and track-type matchup dominant |
| Social sentiment | 15% | Loyal but predominantly North American base |
| Market / whale | 20% | Established US sports betting market |
| Price trend | 20% | Playoff runs create sustained signal windows |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
1. IDENTIFY TRACK TYPE FIRST. Superspeedway, intermediate, short track, road
   course, or dirt — each requires a completely different prediction framework.
   Never apply generic NASCAR form across track types.

2. SUPERSPEEDWAY = REDUCE CONFIDENCE. Daytona and Talladega are genuinely
   unpredictable. Drafting dynamics and crash randomness mean even the
   fastest car has a low win probability. Reduce all sizing here.

3. MANUFACTURER ADVANTAGE at intermediate ovals is the most reliable
   structural signal in the series. Check which manufacturer has the
   fastest cars in practice for those races.

4. CHAMPIONSHIP 4 IS NASCAR'S CLEAREST PREDICTION WINDOW. Four known
   drivers, one track, all points irrelevant — pure race result.
   Research Phoenix-specific track history for all four drivers.

5. RESTART POSITION (inside vs outside lane) at short tracks is a
   decisive moment. Front-row starts at Martinsville and Bristol
   have demonstrably higher win probability than third or fourth.

6. PIT STRATEGY late-race caution timing is the highest-variance
   outcome-determining event at intermediate ovals. This is luck-adjacent
   but teams with aggressive strategists have better historical results.
```

---

## Fan Token™ Notes

No active NASCAR fan token on Chiliz as of Q1 2026. The NASCAR audience is
predominantly North American, deeply loyal, and commercially engaged — exactly
the profile for fan token expansion alongside FIFA World Cup 2026 North American
activation. Highest-value franchise tokens: Hendrick Motorsports, Joe Gibbs Racing,
Team Penske. Daytona 500 week would be the natural launch activation window.

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
NASCAR-specific notes:
- Driver injuries are primarily crash-related: head/neck, ribs, concussion
- HANS device and roll cage have significantly reduced serious injuries post-2000s
- "Driving through pain" is common in NASCAR — drivers often race with undisclosed injuries
- NASCAR allows driver substitutes (a different driver in the same car) for injured drivers

## Data Sources

- **NASCAR official (nascar.com)**: Results, standings, practice times
- **Racing Reference (racing-reference.info)**: Historical data, track records
- **The Athletic NASCAR / NBC Sports**: Race analysis, technical detail
- **Frontstretch.com**: NASCAR news and strategy analysis
- **Weather.com**: Forecast for outdoor tracks (rain can cancel/postpone races)

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Pre-race signal | Load this file + `core/sportmind-score.md` | Apply track type modifier first |
| Qualifying signal | `## Track Type Classification` | NASCAR qualifying sets signal context |
| Playoff race | Playbook 3 or 4 | Elimination urgency modifier applies |
| Manufacturer signal | `## Manufacturer and Team Advantage` | Superspeedway aero package critical |
| Pit strategy | `## Pit Strategy` | Stage racing changes standard pit windows |

---

## Compatibility

**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
