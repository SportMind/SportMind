# Injury Intelligence — Cycling

Sport-specific injury intelligence for road cycling. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to cycling's unique dynamics.
Load both files for full cycling injury intelligence.

---

## What makes cycling injury intelligence different

Cycling has two injury dynamics that no other sport in this library replicates at
the same scale:

**1. Crashes are structurally inevitable, not random** — Road cycling races involve
200+ riders on narrow roads at speeds of 50–80km/h. Crashes don't happen because
of unusual circumstances — they happen in every major race at predictable moments.
An agent that understands when and where crashes are most likely can pre-assess
injury probability before a race even starts.

**2. Cumulative fatigue is a form of soft injury** — A Grand Tour (Tour de France,
Giro d'Italia, Vuelta a España) runs for 21 stages over 23 days. The physical toll
is so extreme that a GC (General Classification) leader in Week 3 is a genuinely
different athlete from the same rider in Week 1. This degradation is measurable,
predictable, and impactful — but it is never described as "injury" because the
rider is still racing.

---

## Crash probability by race type and moment

### Stage types and crash risk

```
FLAT STAGES (sprint finishes):
  Crash probability: HIGH in final 3km
  Why: 200 riders converging at 60km/h+ on tight city streets
  Typically affected: sprinters, lead-out trains, riders caught in final surge
  GC contenders: usually protected by team behind first 10 rows in sprint finishes
  
  High-crash moments:
    Final kilometre (sprint position fighting): peak risk
    Technical corners in final 5km
    Roundabouts / road furniture in sprint finish town
    
MOUNTAIN STAGES:
  Crash probability: MODERATE
  Typical crash moments: technical descents (not climbs)
  Particularly dangerous: wet roads, high-speed descents after summits
  GC contenders: exposed on technical descents if unable to descend well
  
TIME TRIALS:
  Crash probability: LOW (solo effort, no peloton)
  Exception: wet conditions; technical courses; tired riders near end of stage race
  Typically not a crash-risk stage
  
COBBLED CLASSICS (Paris-Roubaix, Tour of Flanders):
  Crash probability: VERY HIGH throughout
  Cobbles create constant crash risk, not just at finish
  Specialist event — non-cobbled specialists are higher crash risk
  
CRITERIUMS / CIRCUIT RACES:
  Crash probability: HIGH (tight corners, repeated laps)
  
GRAND TOUR PROLOGUE / STAGE 1–3:
  Historically highest crash stages in any Grand Tour
  Reason: nervous peloton, everyone is fresh and fighting for position
  GC riders sometimes deliberately avoid exposure until peloton settles (Stage 3+)
```

### Pre-race crash risk assessment

```
ELEVATED CRASH RISK CONDITIONS:
  Wet roads: × 1.5 crash probability multiplier
  Narrow roads in final 30km of flat stage: × 1.3
  Technically complex finish (sharp corners, barriers): × 1.4
  Cross-winds (echelons form, peloton splits violently): × 1.6
  Very hot conditions (concentration lapses, heat-related): × 1.2
  Cobbled sections: × 2.0 for unspecialised riders
  
  Agent rule: On stages with multiple elevated risk conditions,
  apply pre-emptive × 0.90 to GC leader completion probability.
```

---

## Grand Tour cumulative fatigue curve

The most important and unique concept in cycling injury intelligence. The "soft
injury" of Grand Tour fatigue changes the physical capability of every rider in
a three-week race.

```
GRAND TOUR FATIGUE TIMELINE (21 stages over 23 days):

WEEK 1 (Stages 1–7):
  Physical state: Fresh. Riders at 95–100% of season-peak capacity.
  GC riders: Protecting position, avoiding risk.
  Crash risk: Highest (nervous peloton).
  Prediction reliability: High — form data is still accurate.
  
WEEK 2 (Stages 8–14):
  Physical state: Accumulating fatigue. GC riders at 85–92%.
  Form players vs GC specialists: GC specialists start to assert.
  Domestiques (team workers): Progressively more fatigued than protected leaders.
  Crash risk: Moderate — peloton is settled, but fatigue adds error.
  Prediction reliability: Good — form data still useful with week-2 adjustment.
  
WEEK 3 (Stages 15–21):
  Physical state: Deep fatigue. GC leaders at 75–85%.
  Recovery ability: Heavily impaired. An illness or crash at this point = likely DNF.
  Breakaway success: Higher (peloton conserving energy for GC protection).
  Time trial (often Stage 20): Tests who has managed fatigue best — important signal.
  Prediction reliability: Moderate — past form data less predictive;
                          current race data (within Tour) more predictive.
```

### Applying the fatigue modifier

```
GRAND TOUR FATIGUE MODIFIER:

Stage 1–7:     × 1.00 (no fatigue adjustment)
Stage 8–10:    × 0.97 (early Week 2 fatigue)
Stage 11–13:   × 0.94 (mid-Tour — fatigue establishing)
Stage 14–16:   × 0.90 (significant fatigue for most riders)
Stage 17–18:   × 0.86 (only GC specialists still competitive)
Stage 19–21:   × 0.82 (extreme fatigue — character and tactical awareness over power)

REST DAY ADJUSTMENT:
  After each rest day (typically Days 8 and 15): add × 0.04 recovery bonus
  (Partial but not complete recovery; muscle damage accumulates)
  
GC LEADER vs DOMESTIQUE DIFFERENTIAL:
  Protected GC leader: receives full fatigue modifier above
  Domestique (team worker): apply additional × 0.90 from Stage 10 onwards
  (Riders protecting their leader expend more effort; fatigue faster)
  
PREVIOUS GRAND TOUR WITHIN 45 DAYS:
  Any rider who completed another Grand Tour in same season:
  Apply × 0.94 from Stage 1 (pre-existing fatigue entering the race)
```

---

## Injury types specific to cycling

### Contact injuries (crash-related)
```
ROAD RASH (abrasions): Tier C
  Recovery: 1–7 days depending on extent
  Performance impact during recovery: painful but manageable
  Impact on riding: minimal in long races (adrenaline and tape)
  
COLLARBONE FRACTURE: Tier B
  Recovery: 4–8 weeks
  Very common crash injury (instinctive arm extension)
  Typically ends Grand Tour immediately
  Return modifier: × 0.88 first 3 races (shoulder strength and confidence)
  
WRIST / HAND FRACTURE: Tier B
  Recovery: 3–8 weeks
  Affects handlebar grip, braking, time trial position
  Return modifier: × 0.90 first 3 races
  
KNEE LIGAMENT (MCL from crash): Tier B
  Recovery: 4–8 weeks
  Affects power output and pedalling biomechanics
  Return modifier: × 0.85 (significant — cycling requires knee stability)
  
CONCUSSION: Tier B minimum
  Cycling has elevated concussion awareness post-2020
  Strict return protocols in UCI events
  Agent rule: "In concussion protocol" = treat as out until official clearance
  
HEAD TRAUMA (severe): Tier A
  Rare but career-defining
  Any confirmed serious head injury requires complete reassessment
```

### Overuse and chronic injuries
```
KNEE PAIN (patellofemoral / iliotibial band):
  Very common in professional cycling; often managed across a season
  Signals: reduced cadence, changed position, fewer long climbs in training
  Performance impact: × 0.93 on climbing output if chronic
  
SADDLE SORES AND SKIN CONDITIONS:
  Not serious in isolation but compound with Grand Tour fatigue
  A rider dealing with saddle sores in Week 3 of a Grand Tour has reduced
  motivation to push in time trials and key mountain stages
  Signal: rider stands on pedals more than usual (relieving saddle pressure)
  
TENDINITIS (Achilles, patellar):
  Common from training load; manageable at low intensity
  Time trials and steep gradients amplify pain and reduce output
  Apply: × 0.90 on time trial and mountain stage performance
  
RESPIRATORY ILLNESS:
  High-risk in peloton (shared hotel corridors, team buses, podium exposure)
  "Something going through the team bus" → apply × 0.88 to all riders on that team
  Grand Tour respiratory: compound effect with fatigue = very serious by Week 3
```

---

## GC leader vulnerability windows

Grand Tour GC leaders are protected by their team but have specific vulnerability moments
that create the most significant injury and performance risk:

```
HIGH VULNERABILITY MOMENTS:

1. Crosswind stages (echelon formation):
   Peloton splits into groups; protection breaks down
   GC leader can be "caught out" and lose significant time
   Not injury per se but team protection failure = exposure to crash and isolation
   
2. Technical descents post-summit:
   Most descending crashes happen here
   "Poor descenders" (identified trait in form databases) face higher risk
   
3. Intermediate sprint in flat stage:
   Team wastes energy on intermediate sprint = less protection in finale
   GC leader more exposed in chaotic final kilometres
   
4. Final kilometre of flat stage (if lead-out fails):
   GC leader caught without protection in sprint chaos
   Crash probability highest here
   
5. Week 3 mountain stages (fatigue + attacks):
   GC leader defending overall lead under sustained attack
   Combined fatigue + effort = highest injury probability from crashes
   One attack too many can cause catastrophic collapse (bonking) or increase crash risk
```

---

## DNF prediction — the most unique cycling metric

In no other sport does "Did Not Finish" carry the predictive complexity it does in
cycling. A DNF is not just a bad result — it is often preceded by signals that
give 12–24 hours of advance warning.

```
PRE-DNF SIGNAL PATTERN (watch for in live monitoring):

Day before potential DNF:
  Rider finishing "on the limit" when usually comfortable
  Rider not visible in breakaway attempts or team work (not pulling)
  Social media: no post-stage posts (too exhausted even to post)
  
Day of potential DNF:
  Rider not in start list warm-up (teams sometimes scratch overnight)
  Rider looks "empty" in peloton (not responding to attacks)
  Team car repeatedly pulling alongside (feeding recovery product / concern)
  
During race (live):
  Rider dropped from peloton on a moderate gradient (not a hard climb)
  Rider sitting up (hands on top of bars, no racing position)
  Team car following rider who is minutes behind peloton
  
  Agent rule: If monitored rider shows 2+ pre-DNF signals on consecutive stages,
  apply × 0.75 to completion probability for that stage and reduce overall position.
```

---

## Data sources

- **ProCyclingStats / CyclingArchives**: Race results, DNF records, team rosters
- **VeloNews / CyclingNews**: Race reports with crash and injury detail
- **UCI official results**: Official timing, DNF classifications
- **Strava / Garmin segments**: Training data where public (some pros share)
- **Team social media**: Rider condition updates, team news
- **TV broadcast**: Commissaire radio and team car radio commentary
- **cycling-info.com / Procyclingstats**: Historical head-to-head and course performance

---

*MIT License · SportMind · sportmind.dev*
