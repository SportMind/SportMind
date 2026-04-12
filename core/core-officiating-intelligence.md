# Officiating Intelligence — SportMind Core

Referees, umpires, and judges are consistent, measurable signal inputs that most
prediction models ignore entirely. This skill gives AI agents the framework to
incorporate officiating tendencies as a first-class pre-match variable.

---

## Why officiating is a signal, not noise

Officiating tendencies are:
- **Documented** — statistics are publicly available or derivable from match data
- **Persistent** — individual referee tendencies are stable across seasons
- **Material** — high-card referees in football increase game flow disruption;
  lenient MMA judges shift optimal fighter strategy; strict baseball umpires
  with small strike zones change pitcher/hitter approach
- **Underpriced** — retail prediction markets rarely adjust for officiating;
  the edge is available to agents that do

```
OFFICIATING INTELLIGENCE FRAMEWORK:

Pre-match input:
  1. Identify the assigned official(s)
  2. Load their documented tendency profile
  3. Apply sport-specific officiating modifiers to the base signal

The modifier is SMALL but CONSISTENT — typically ±3–8% on relevant metrics.
Accumulated across many events, this edge compounds significantly.
```

---

## Football / Soccer — Referee intelligence

### Core metrics to track per referee

```
CARDS:
  Yellow cards per game (YPG): league average ~3.5–4.5; high = >5.0; low = <2.5
  Red cards per game (RPG): league average ~0.15; high = >0.25
  Card differential (home vs away): positive = home-favouring referee
  
PENALTIES:
  Penalties awarded per 100 games: league average ~20–25
  Home/away penalty split: benchmark is 60/40 home-favoured
  VAR referral rate (where VAR exists): high referral = less decisive on-pitch
  
GAME MANAGEMENT:
  Injury time added (average minutes per half)
  Advantage played rate (vs stopping for foul)
  
DATA SOURCES:
  WhoScored.com, TransferMarkt referee stats, FBref referee logs,
  FootyStats referee pages
```

### Football officiating modifiers

```
CARD-HEAVY REFEREE (YPG > 5.0):
  → Increase probability of key player suspension risk
  → Reduce confidence in teams relying on physical pressing styles
  → Increase value of technically clean, less physical teams
  Signal modifier: Physical pressing teams −5%

LOW-CARD REFEREE (YPG < 2.5):
  → Physical teams gain relative advantage
  → Long matches more likely (less disruption)
  Signal modifier: Physical teams +3%

HOME-FAVOURING PENALTY SPLIT (>65% home):
  → Home team advantage amplified beyond standard home field
  Signal modifier: Home token/team +4%

HIGH INJURY TIME REFEREE (avg >5 min per half):
  → Games more open; late goals more frequent
  → Trailing teams gain marginal time value
  
DERBY ASSIGNMENTS:
  Top referees assigned to derbies/finals — check appointment tier
  UEFA appoints Category 1 referees to Champions League knockout stages
  Lower tier referee in a big match = uncommon; flag for investigation
```

---

## MMA / Combat Sports — Judge intelligence

### Why judge tendencies matter in MMA

Judges determine 60–70% of UFC outcomes (most fights go to decision). Individual
judge tendencies — who they favour (striker vs grappler), how they score rounds
(10-point must system applied strictly vs loosely), their history of controversial
decisions — directly affect fighter strategy and outcome probability.

```
JUDGE TENDENCY PROFILES:

STRIKER-FAVOURING JUDGE:
  Values: Visible strikes, aggression, forward pressure
  Impact: Grapplers with control time but less visible damage get less credit
  Agent action: When striker-favouring judge on panel, +3–5% to striker probability
  
GRAPPLING-FAVOURING JUDGE:
  Values: Takedowns, control time, submission attempts
  Impact: Pure strikers who win standing exchanges may lose rounds on this judge
  Agent action: When grappling-favouring judge on panel, +3–5% to grappler probability
  
CLOSE-ROUND JUDGE (conservative scorer):
  Rarely scores 10-8 rounds even in dominant performances
  Impact: Reduces probability of judge favouring one fighter by wide margin
  
DOMINANT-PERFORMANCE JUDGE:
  Willing to score 10-8; rewards clear dominance more than conservative judges
  
DATA SOURCES:
  MMADecisions.com — judge-level breakdown of every decision fight
  Tapology.com — judge scoring records
  ESPN MMA judge statistics database
```

### Boxing judge intelligence

```
BOXING-SPECIFIC CONSIDERATIONS:

Home judge bias: Documented in world title fights hosted in fighter's country
  → When two of three judges are from home fighter's nation: discount away fighter +8%

Promoter influence history: Some sanctioning bodies have documented scorer relationships
  → WBC/WBA/IBF/WBO each have different judge pools; research which judges on card
  
CompuBox-alignment rate: Judges who score consistently with CompuBox punch stats
  vs judges who reward "ring generalship" (harder to quantify)
  
DATA SOURCES:
  BoxRec.com judge records
  CompuBox statistics (correlation analysis)
```

---

## Cricket — Umpire intelligence

```
CRICKET UMPIRE SIGNALS:

LBW RATE:
  Umpires vary in LBW willingness; some give benefit of doubt to batters
  High LBW rate umpires: favour spin and swing bowlers on helpful surfaces
  Low LBW rate umpires: batters gain marginal advantage
  
DRS PRESSURE:
  International umpires whose decisions are overturned by DRS at high rates
  = less reliable decision-making; DRS reviews become more valuable
  → Monitor: umpire DRS overturning rate (available from ESPNcricinfo data)
  
SLOW OVER RATE TOLERANCE:
  Some umpires apply slow over rate rules strictly (financial penalties for captains)
  → Affects captain decision-making in the field
  
DATA SOURCES:
  ESPNcricinfo statsguru — match-level umpire data
  CricketArchive — career umpire statistics
```

---

## American Football — Officiating crew intelligence

```
NFL OFFICIATING CREW SIGNALS:

PENALTY RATE:
  Crews vary from ~7 to ~12 penalties per game (league average ~9.5)
  High-penalty crews: disrupt rhythm teams; favour disciplined schemes
  Low-penalty crews: physical play normalised; less stoppage time
  
PASS INTERFERENCE TENDENCIES:
  Some crews call PI at high rates → benefit passing offences
  Some crews allow more contact → benefit physical defensive backs
  
HOME ADVANTAGE CORRELATION:
  Some crews have documented home team penalty split above neutral
  (Subtle but trackable over multi-season sample)
  
CREW EXPERIENCE:
  New crew members in important games = higher variance in officiating
  
DATA SOURCES:
  NFL.com/officials — crew assignments and statistics
  FootballPerspective.com — penalty rate analysis by crew
  NFLRefScores.com — crowd-sourced crew tendency tracking
```

---

## Horse Racing — Stewards intelligence

```
HORSE RACING STEWARDS SIGNALS:

PHOTO FINISH TENDENCY:
  Stewards at different racecourses vary in how they call tight finishes
  Some stewards are quick to call objections; others let result stand
  
GOING REPORT RELIABILITY:
  Individual racecourse clerks of the course vary in how accurately
  they assess and report going conditions
  Some known to understate softness (Ground: "Good to Soft" = actually "Soft")
  
OBJECTION UPHOLD RATE:
  At tracks with high objection uphold rates, horses who finish strongly
  from disadvantaged positions deserve slightly more credit
  
DATA SOURCES:
  Racing Post stewards reports
  Racingresearch.co.uk — track-level stewards analysis
```

---

## Tennis — Chair Umpire and Line Call intelligence

```
TENNIS OFFICIATING SIGNALS:

TIME VIOLATION CALLS:
  Umpires who call time violations at higher rates disrupt rhythm servers
  Players with slow service routines (Djokovic historically) affected more
  
FOOT FAULT CALLING:
  Rare but some umpires/line judges have documented higher foot fault rates
  
HAWK-EYE LIVE COURTS:
  Courts with automated calling remove human line call variance entirely
  → On Hawk-Eye Live courts, officiating intelligence is primarily chair umpire only
  
CLAY COURT MARK REVIEWS:
  On clay, players can request mark inspection; chair umpire decides
  Some chairs more willing to overrule electronic marks
```

---

## Agent integration — how to apply officiating intelligence

```
LOADING INSTRUCTION:
  Load core-officiating-intelligence.md AFTER sport domain skill (Layer 1)
  and BEFORE athlete modifier computation (Layer 2)

  1. Identify assigned official(s) from fixture data
  2. Look up their tendency profile from data source
  3. Apply the relevant modifier to the pre-modifier signal score
  4. Document the officiating modifier separately from the sport modifier
     (so it can be tracked and calibrated independently)

OFFICIATING MODIFIER SIZING GUIDANCE:
  Never apply an officiating modifier > ±8% without large sample evidence
  Minimum sample for reliable officiating tendency: 25+ matches/fights
  Recency weight: last 20 events count 60%, previous history 40%
  
OFFICIATING MODIFIER STACKS WITH:
  Athlete modifier (Layer 2)
  Macro modifier (Layer 5)
  
OFFICIATING MODIFIER DOES NOT STACK WITH:
  Venue intelligence (separate modifier — see core-venue-intelligence when available)
  
AGENT RULE: If assigned official is unknown at time of analysis,
  use zero modifier — do not assume average. Unknown = neutral.
```

---

## Technology-assisted officiating — VAR, Hawk-Eye, TMO

```
THE FUNDAMENTAL CHANGE:
  Technology-assisted officiating does not remove human bias — it changes
  WHERE bias operates and WHEN commercial signals are confirmed.
  
  WITHOUT TECHNOLOGY:
    Controversial red card → immediate commercial event (confirmed in-match)
    CDI event fires at match time
    
  WITH VAR / TMO:
    Controversial red card → PROVISIONAL commercial event (unconfirmed)
    Review period: 2–8 minutes of uncertainty
    Outcome A (upheld): CDI event confirmed, delayed
    Outcome B (overturned): CDI event cancelled, signal reversal

LEAGUE-LEVEL VAR PRESENCE:
  
  VAR ACTIVE (as of 2026):
    UEFA Champions League, Europa League, Conference League
    Premier League, Bundesliga, La Liga, Serie A, Ligue 1
    MLS, Brazilian Série A
    FIFA World Cup, UEFA Euros
    
  NO VAR (significant leagues):
    Championship (England), League One/Two
    Scottish Premiership
    Eredivisie (Netherlands) — VAR introduced then paused
    Many lower-tier European leagues
    
  AGENT RULE: Always check whether VAR is active in the competition being
  analysed. The officiating modifier applies differently per league.

HOW VAR CHANGES THE OFFICIATING MODIFIER:

  CARD EVENTS WITH VAR:
    First 3 minutes post-decision: apply provisional modifier only (×0.70)
    After VAR upholds: full modifier applies
    After VAR overturns: reverse modifier, flag CDI_REVERSAL
    
  PENALTY DECISIONS WITH VAR:
    Penalty awarded: treat as provisional until VAR completes
    Expected VAR review duration: 90–180 seconds
    Overturn rate for penalties (EPL data): ~15% of reviewed penalties reversed
    Apply: ×0.85 provisional modifier until confirmed
    
  OFFSIDE DECISIONS (automated offside lines):
    Semi-automated offside (SAOT) in UCL/World Cup:
    No review delay — decision made at same speed as play
    Marginal offside calls will now be confirmed faster
    Commercial signal: no change to timing, but accuracy increases
    
  GOAL-LINE TECHNOLOGY:
    No review delay. Decision instant. Signal fires immediately.
    Overrides all other decision uncertainty.

SPORTS WITH TMO (Rugby Union / League):
    
  TMO REVIEW CHARACTERISTICS:
    Duration: 3–10 minutes for complex decisions
    Try awarded → commercial event provisional for duration of TMO
    TMO overturn rate: approximately 12–18% of reviewed decisions
    Apply: ×0.82 provisional modifier during TMO review
    After TMO decision: full modifier applies or reversal
    
  YELLOW/RED CARD REVIEWS:
    Rugby citing (post-match): CDI event confirmed in-match but can be
    extended post-match. See core/post-match-signal-framework.md.

MMA INSTANT REPLAY:
  Post-fight instant replay review (rare, judges overriding):
  Apply uncertainty flag until result confirmed.
  Duration: typically resolved within 30 minutes of bout end.

HAWK-EYE CHALLENGE SYSTEM (Tennis, Cricket):
  
  TENNIS:
    Line challenge: 30-second delay. Overturn rate ~28%.
    Apply: provisional hold on point-sequence-dependent signal during review.
    Commercial implication: very low (individual points rarely move token signals)
    
  CRICKET (DRS — Decision Review System):
    Umpire decision reviewed on appeal.
    Key wickets: wicket of star player → apply provisional ×0.80 until DRS completes
    Overturn rate for LBW DRS appeals: ~30% successful.
    
ALGORITHMIC OFFICIATING (emerging, 2026+):
  AI-assisted judge systems being trialled in MMA (UFC) and boxing.
  If AI scoring replaces or supplements human judges:
    Judge-bias modifier from MMA section REDUCES in weight
    Shot accuracy and compuStrike data becomes primary signal
    Current status: advisory only (no competitions with binding AI judging yet)
    Monitor: UFC, WBO announcements on AI judging programme
```

## Contribution guidance

Officials statistics are available publicly for most major sports. Contributors with
access to structured officiating databases can calibrate the modifier ranges above
with historical validation. The current ranges are based on documented tendency
analysis but are not ML-calibrated (v3.0 roadmap item).

*SportMind v3.62 · MIT License · SportMind · sportmind.dev*
*See also: core/tactical-matchup-intelligence.md · core/post-match-signal-framework.md*
