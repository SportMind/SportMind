# Weather and Match-Day Conditions — SportMind Core

Match-day weather is a pre-match signal variable for outdoor sports. This skill gives
AI agents a unified framework for interpreting weather conditions as prediction inputs,
distinct from the structural long-term climate disruption covered in
`macro/macro-climate-weather.md`.

**Scope:** This file covers weather as a tactical pre-match variable.
For structural climate risk (season cancellations, long-term venue viability), see
`macro/macro-climate-weather.md`.

---

## The weather signal hierarchy

Not all weather affects all sports equally. Load only the section relevant to
the sport being analysed.

```
SPORTS MOST AFFECTED BY WEATHER (highest to lowest):
  1. Cricket           — rain, dew, pitch moisture, humidity, light
  2. Horse racing      — going (ground conditions), visibility, temperature
  3. Cycling           — rain, wind, temperature extremes
  4. Athletics         — wind (legal limit ±2.0 m/s for records), heat, rain
  5. Golf              — wind, rain, temperature (ball flight physics)
  6. Rugby (all codes) — rain, wind (kicking and handling)
  7. American football — rain, wind, extreme cold (ball handling, kicking)
  8. Football/soccer   — heavy rain (surface), wind (long ball game)
  9. Tennis (outdoor)  — wind, heat, rain (suspension)
  10. Baseball         — wind direction/speed (park-specific), rain
  
SPORTS LESS AFFECTED:
  MMA, esports, snooker, darts, basketball, ice hockey — indoor; no weather effect
  Formula 1, MotoGP — significant effect (wet race specialist framework exists
  in sport domain skills; cross-reference those files)
```

---

## Cricket — the most weather-sensitive sport

```
RAIN AND REDUCED OVERS:
  DLS (Duckworth-Lewis-Stern) method recalculates targets in reduced-over games
  DLS favours chasing teams in short formats when rain interrupts mid-innings
  DLS disadvantages batting teams who lose overs from their first innings
  
  AGENT RULE: Check weather forecast for T20 and ODI matches 24h in advance
  Rain probability >40% for a T20 = DLS scenario possible; load DLS probability
  modifier for chasing team. Chase-friendly conditions = +4–6% to chasing team.

DEW FACTOR (day-night matches):
  Dew settles on the outfield from ~20:00 local time in tropical climates
  Wet ball = swing and spin dramatically reduced in second innings
  Batting second (chasing) = significant advantage in dew conditions
  
  Most affected: IPL (India), PSL (Pakistan), BPL (Bangladesh), CPL (Caribbean)
  Least affected: Northern hemisphere day games, early-season cold weather venues
  
  DEW MODIFIER:
  High dew probability (tropical venue, evening match): Batting second +8–12%
  Low dew probability (cold venue, day match): No modifier

PITCH MOISTURE AND MORNING CONDITIONS:
  Early-morning moisture assists swing bowling and seam movement
  As day progresses, pitch dries → batting becomes easier
  
  COIN TOSS SIGNAL: In high-moisture conditions, toss winner who fields first
  gains tactical advantage. Monitor toss result for morning matches.
  
  OVERCAST CONDITIONS:
  Cloud cover retains moisture; assists swing bowling throughout day
  Clear bright conditions: Pitch dries faster; batting conditions improve

HUMIDITY:
  High humidity (>70%): Ball swings more; reverse swing more likely later
  Low humidity (<40%): Ball loses condition faster; less swing
```

---

## Horse Racing — going conditions

```
GOING REPORT FRAMEWORK:
  (UK/Ireland scale)
  Firm → Good to Firm → Good → Good to Soft → Soft → Heavy
  
  Each horse has a preferred going range documented in form guides
  Going preference is one of the strongest single-horse modifiers available
  
  GOING MODIFIER CALCULATION:
  Horse's preferred going vs today's going:
    Ideal going: × 1.10 modifier
    Adjacent going: × 1.00 (no change)
    One step off preferred: × 0.93
    Two steps off preferred: × 0.85
    Extreme mismatch: × 0.75
  
  DATA SOURCE: Racing Post form guide, Timeform going preference ratings

GOING VARIABILITY:
  Going can change between the morning report and race time
  Rain overnight: goes softened 0.5–1.0 steps toward heavy
  Bright sun + wind: firms up 0.5 steps toward firm
  
  AGENT RULE: For afternoon races, check both morning going report AND
  actual weather that day. The going at race time may differ from the
  official morning report.

TEMPERATURE EXTREMES:
  Very cold (<5°C): Horses from warmer stables may underperform
  Very hot (>28°C): Horses with heavy coats or from cooler climates at risk
  
VISIBILITY:
  Fog/mist: Some races abandoned above threshold; check racecourse weather
```

---

## American Football — weather modifiers

```
WIND (the dominant factor in American football):
  Wind speed (mph) → Passing/kicking impact:
  0–5 mph:   No modifier — standard conditions
  6–15 mph:  Mild headwind on certain drives; minimal passing effect
  16–25 mph: Significant effect on deep passing, field goals >45 yards
             → −5% to high-passing offences; −10% to field goal probability >45 yards
  >25 mph:   Major effect; run-heavy offences gain relative advantage
             → −12% to passing offences; +5% to run-heavy teams
  
  Wind direction matters: Crosswind most disruptive to accuracy
  Swirling/variable wind: Highest variance — avoid over-confidence

RAIN:
  Ball handling impaired → increased fumble risk for both teams
  Wet ball → reduced passing accuracy, receiver drops
  Rain modifier: −5% to high-passing, low-turnover teams

COLD (temperature °F):
  Above 20°F: No significant modifier
  10–20°F: Kicking range reduced (ball loses elasticity); passing slightly affected
  Below 10°F: Significant — run-heavy teams gain advantage; home cold-weather teams
  vs warm-weather visitors: +4% to home team

DATA SOURCES:
  Weather.com, National Weather Service, ESPN weather feature (pre-game)
  Vegas weather correlation studies (documented in sports betting literature)
```

---

## Football / Soccer — weather modifiers

```
HEAVY RAIN:
  Wet pitch: Ball moves faster; reduces technical passing accuracy
  Tends to level playing fields between technical and direct teams
  Direct/physical style teams gain relative advantage in heavy rain
  High-pressing technical teams slightly disadvantaged
  
  Rain modifier: Technical passing teams −3%; physical/direct teams +2%

STRONG WIND (>20 mph):
  Long-ball/aerial teams gain advantage
  Short passing, possession teams disrupted
  Set pieces (corners, free kicks) become more variable
  
  Wind modifier: Aerial/long-ball teams +3%; possession teams −3%

EXTREME HEAT (>32°C / 90°F):
  High-intensity pressing teams fatigue faster
  Water breaks introduced at 32°C+ (international rules)
  Teams with deeper squads gain late-game advantage
  
  Heat modifier: High-press teams −4% over 90 minutes; deep squads +2%

COLD (<0°C / 32°F):
  Pitches may be frozen or borderline playable
  Grounds staff heat pitches; check pitch inspection reports
  Generally low modifier once pitch is confirmed playable
```

---

## Golf — weather modifiers

```
WIND (primary factor in golf):
  Wind speed → scoring impact (per round):
  0–5 mph:   Normal scoring expected
  6–15 mph:  Scoring average rises ~1–2 strokes per round
  16–25 mph: Scoring average rises ~3–5 strokes per round; low scores rare
  >25 mph:   Links specialist advantage; scoring unpredictable
  
  Wind modifier: In high wind (>20 mph), increase weight of:
  → Links course experience
  → Shot-shaping ability over raw distance
  → Previous performance at this course in wind
  
  Scoring projection: Every 5 mph wind above 10 mph = approximately +0.5 strokes
  to field average per round; adjust cut line projections accordingly

RAIN:
  Soft fairways: Less roll; distance decreases
  Wet greens: Ball checks up faster; aggressive play rewarded
  Umbrella/waterproof conditions: Comfort factor; some players impaired

TEMPERATURE:
  Cold air is denser: Ball flies shorter (approximately 2% per 10°F drop below 70°F)
  Hot/thin air: Ball flies further (altitude + temperature compound)
  
DATA SOURCES:
  Weather.com golf-specific forecasts
  European Tour/PGA Tour weather app data
  Shot Scope conditions tracking (community data)
```

---

## Rugby — weather modifiers

```
RAIN:
  Ball handling impaired → reduced handling error tolerance
  Wet conditions favour: Kicking games, forward dominance, set piece teams
  Wet conditions disfavour: Wide expansive game, off-load heavy teams
  
  Rain modifier: Wide/expansive style teams −5%; set piece/kicking teams +4%

STRONG WIND:
  Kicking accuracy reduced → territory game becomes harder
  Conversions and penalties from wide positions become unreliable
  
  Wind modifier: Kicking-dependent teams (fly-half accuracy teams) −5%
  Particularly applies to rugby union where kickers are primary scorers

COLD AND MUDDY:
  Heavy mud: Scrum dominance amplified; mobile forward advantage reduced
  Mud modifier: Heavy scrum teams +3%
```

---

## Athletics — legal wind limits

```
WIND LEGAL LIMITS FOR RECORDS:
  Sprints and horizontal jumps: ±2.0 m/s maximum (tailwind only for records)
  Wind assistance: >+2.0 m/s = performance cannot count for world/national record
  
AGENT IMPLICATIONS:
  In strong tailwind conditions: expect faster sprint times; more likely PBs
  but these cannot count as records — affects narrative value and token signal
  In headwind conditions: slower times likely; upset probability increases
  
HEAT POLICY:
  >35°C WBGT (Wet Bulb Globe Temperature): Events may be shortened or postponed
  Marathon/distance events most vulnerable
  Check forecast before any outdoor athletics position

RAIN:
  Jumps (triple jump, long jump): Wet runway impairs grip; results typically slower
  Throws (discus, hammer): Generally unaffected except in extreme conditions
```

---

## Weather monitoring — agent workflow

```
STANDARD PRE-MATCH WEATHER CHECK:

For outdoor sports: run this check 24h and 3h before event start

1. Identify: Is this sport weather-sensitive? (see hierarchy above)
   → If indoor or low-sensitivity: skip weather check
   → If outdoor and medium/high sensitivity: proceed

2. Get forecast: Wind speed/direction, rain probability, temperature, humidity
   → Sources: Weather.com, BBC Weather, Dark Sky API, venue-specific reports

3. Apply sport-specific modifier from this file

4. Check for extreme conditions:
   → Abandonment risk: Check racecourse/ground weather policy
   → Event modification risk: (DLS in cricket, water breaks in football)
   → Postponement risk: (golf, outdoor athletics, horse racing most vulnerable)

5. If abandonment/postponement probability > 15%: Reduce position size
   → Cancellation confirmed: Exit all positions; await rescheduled date

WEATHER MODIFIER STACKS WITH:
  Athlete modifier (Layer 2)
  Officiating modifier (core-officiating-intelligence.md)
  Macro modifier (Layer 5)

WEATHER MODIFIER DOES NOT DUPLICATE:
  macro/macro-climate-weather.md — that file covers structural long-term risk
  This file covers match-day tactical weather only
```

*MIT License · SportMind · sportmind.dev*
