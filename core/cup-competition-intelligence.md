# Cup Competition Intelligence

**Signal models for domestic and continental cup competitions across sport.**
Cup competitions have distinct signal characteristics that differ from league
formats: variable opponent quality, upset probability curves, squad rotation
as a systematic signal, and single-elimination pressure that affects both
form predictions and narrative momentum differently.

---

## Why cups need their own intelligence model

League football produces consistent, predictable signal windows. Cup football
does not — for three structural reasons:

**1. Opponent quality variance is extreme.** A Champions League group match
pits two top-10 European clubs. An FA Cup third round match pits a Premier League
club against a League Two club. The same club, the same squad, the same token —
but the signal environment is completely different.

**2. Squad rotation is systematic and predictable.** Elite clubs routinely
field weakened squads in cup competitions when league priority is clear. This
is not an injury signal or a form signal — it is a tactical decision that agents
must account for before applying athlete modifiers.

**3. Upsets have a different signal architecture than league surprises.**
When a lower-division club beats a top-flight club in a cup, the narrative
is simultaneously positive for the lower club and negative for the upper club
in ways that differ from a standard form-based upset.

---

## The Cup Signal Framework (CSF)

```
CSF = competition_prestige × round_weight × opponent_quality_gap × rotation_risk

competition_prestige (how much does this cup matter for token purposes?):
  UCL (not strictly a cup but single-elimination from QF): 1.00
  UEL, UECL (semi-final onwards): 0.70-0.85
  FA Cup, Copa del Rey (semi-final+): 0.65-0.75
  DFB-Pokal, Coppa Italia, Coupe de France (semi+): 0.55-0.65
  League Cup (Carabao Cup / EFL Trophy): 0.40-0.50
  Lower-tier domestic cups: 0.25-0.35

round_weight (escalates through the competition):
  Final:              1.00
  Semi-final:         0.80
  Quarter-final:      0.65
  Round of 16:        0.50
  Round of 32 (R32):  0.40
  Early rounds (R64+): 0.25

opponent_quality_gap (difference in competitive tiers):
  Same tier (UCL R16, both top clubs): 1.00 × standard form model
  1-tier gap (PL vs Championship):     0.70 × standard form (upset risk +15%)
  2-tier gap (PL vs League One):       0.55 × standard form (upset risk +25%)
  3+ tier gap (PL vs non-league):      0.40 × standard form (upset risk +35%)
  
  UPSET PROBABILITY TABLE:
  1-tier gap: 18% upset probability (actual historical FA Cup data)
  2-tier gap: 8% upset probability
  3+ tier gap: 3% upset probability (but narrative impact is very high when it happens)

rotation_risk (probability that top team fields weakened squad):
  HIGH (0.75+): Fixture congestion, league priority clear, next league match < 4 days
  MEDIUM (0.45-0.74): Some rotation expected; 4-5 key players rested
  LOW (0.20-0.44): Competitive squad; minor rotation only
  MINIMAL (< 0.20): Full squad; cup is priority
  
  Apply: adjusted_score × (1 - rotation_risk × 0.25)
  At HIGH rotation risk: adjusted_score confidence band widens ±8 points
```

---

## European competition intelligence

### UEFA Champions League (knockout rounds)

```
UCL KNOCKOUT SIGNAL MODEL:

Two-legged ties (R16 through SF):
  First leg: CSF applies; home advantage standard
  Second leg: aggregate score context modifies everything
    → Team leading on aggregate: apply ×0.92 conservative modifier (protecting lead)
    → Team trailing: apply narrative_active flag; upset risk elevates
    
  Away goals rule ABOLISHED (since 2021-22): 
    Both legs equal weight; only aggregate determines outcome
    This reduced the first-leg signal complexity (no longer need to track
    "away goals" in tied aggregate situations)
    
  Quarter-final and beyond: CSF × 1.00 (full prestige weight)
  
  ROTATION IN UCL:
    Champions rest players for league: almost never (UCL is priority 1)
    Rotation_risk = MINIMAL for top UCL clubs at QF onwards
    Exception: clubs with unassailable league leads in April may rotate for R16

UCL GROUP STAGE:
  CSF: 0.55-0.70 (lower than knockout; qualification implications grow over 6 matches)
  Matchday 6 (decisive group stage): CSF 0.80 if qualification at stake
  Rotation_risk: MEDIUM in early group stage; MINIMAL if qualification uncertain

UCL FINAL:
  Neutral venue; both fanbases represented
  Token dual-signal: if both finalists have active tokens → load multi-token protocol
  Highest single-event signal in European club football calendar
  Token signal: winning club +15-30%; losing club -8-20%
```

### UEFA Europa League / Conference League

```
UEL SIGNAL MODEL:
  Lower prestige than UCL; higher prestige than domestic cups
  R16 onwards: CSF 0.65-0.75
  UEL Final: CSF 0.80 (below UCL but significant — European trophy + qualification)
  
  TOKEN SIGNAL DISTINCTION:
    Clubs with large international fan bases: UCL > UEL significantly
    Clubs with strong domestic fan bases: UEL Final ≈ domestic cup final
    
  CONFERENCE LEAGUE (UECL):
    CSF: 0.50-0.65 (semi-final+); 0.35-0.50 early rounds
    UECL is meaningful for clubs new to European competition
    First European Final for a club = narrative_active flag → apply ×1.15

COPA LIBERTADORES (South America):
  CSF: 0.90 at Final (highest club competition outside UEFA)
  Boca vs River in Libertadores: multiply by derby_active flag
  Argentine/Brazilian clubs: Libertadores = UCL equivalent for token purposes
```

---

## Domestic cup intelligence by country

### FA Cup (England) — detailed model

```
PRESTIGE AND HISTORY:
  Oldest national football cup competition in world (since 1871)
  Any club from any tier (National League South to Premier League) can enter
  "Magic of the Cup" — culturally embedded upset expectation

ROUND STRUCTURE AND SIGNAL:
  Rounds 1-2 (November-December): Non-league/lower league only; no PL clubs yet
    Signal: Very low for fan token purposes
    
  Round 3 (January — "FA Cup weekend"):
    PL and Championship clubs enter for first time
    Biggest upset window: non-league clubs vs PL clubs
    CSF: 0.30 for comfortable ties; 0.45 for high-profile pairings
    
  Round 4 (late January): Top 32; PL clubs still face upset risk
    CSF: 0.35-0.45
    
  Round 5 (February): Last 32; upset probability reducing
    CSF: 0.45-0.55
    
  Quarter-Finals (March): Last 8; elite clubs dominant
    CSF: 0.60-0.70
    
  Semi-Finals (Wembley, April): CSF 0.70-0.75; Wembley atmosphere signal active
  
  Final (Wembley, May): CSF 0.75
    → Adds LTUI positive for clubs with UK-dominant token holder bases
    → For $CITY/$CHELC type clubs: UCL > FA Cup in signal weight
    → For Championship clubs reaching FA Cup Final: maximum narrative signal

ROTATION INTELLIGENCE:
  PL clubs routinely rotate in Rounds 3-5 if league is priority
  Indicators of heavy rotation:
    Manager quotes: "We respect the competition but..." = rotation coming
    Squad announcement: checking for absence of 4+ first-choice players
  At heavy rotation (HIGH rotation_risk): reduce adjusted_score confidence band to ±8

GIANT-KILLING SIGNAL:
  Non-league beats PL: narrative_active ×1.25 for winning club
    (small club with token or high social following → maximum engagement event)
  Championship beats top-6 PL: narrative_active ×1.10
  Token impact for beaten PL club: -5 to -12% (embarrassment premium)
```

### Copa del Rey (Spain)

```
Higher signal than FA Cup for Spanish club tokens.
Reason: Real Madrid and Barcelona always involved until they are eliminated.
Any Copa del Rey Semi-Final involving Real or Barcelona: CSF 0.75
Copa del Rey Final: CSF 0.75-0.80
  Often held in neutral venue; historically chosen in non-Madrid/Barcelona cities.
  
COPA vs LEAGUE PRIORITY:
  Real/Barça: UCL >> Copa in squad rotation decisions
  Mid-tier La Liga clubs: Copa = significant achievement; full squad more likely
  Copa draw upset potential: lower than FA Cup (Spanish lower leagues less competitive)
```

### DFB-Pokal (Germany)

```
CSF: 0.55-0.65 at semi-final+; lower in early rounds.
ROTATION: Bayern typically field competitive squads at all stages.
  Exception: if Bayern secured Bundesliga early → Cup = primary remaining objective.
Final (Berlin, May): CSF 0.65.
TOKEN SIGNAL: Bundesliga club tokens benefit from any European qualification the cup provides.
```

### Coppa Italia (Italy)

```
CSF: 0.55-0.65 at semi-final+.
Two-legged semi-finals: aggregate context applies.
Final: CSF 0.65.
Serie A derbies in Coppa: load core/derby-intelligence.md regardless of round.
```

### Coupe de France

```
CSF: 0.50-0.60 at semi-final+.
PSG dominance: $PSG token signal from Coupe is lower than UCL equivalent.
Amateur clubs in early rounds: France has strong amateur football participation.
```

---

## Token-gated cup access — the utility event

```
TOKEN-GATED CUP EXPERIENCES (Phase 2 utility):

Fan tokens increasingly used as access mechanism for cup match experiences:
  Priority ticket access: token holders get first access to cup final allocations
  Ticket discount: token holders receive reduced cup ticket prices
  Exclusive pre-match access: token holders invited to stadium tours, meet-and-greets
  
SIGNAL FOR TOKEN LIFECYCLE:
  Club announces token-gated cup final ticket access:
    → LTUI positive signal: concrete utility event added to Phase 2
    → HAS spike: holders re-engage to claim benefit
    → Apply × 1.10 to LTUI projection for next 12 months
    
  FA Cup / Copa del Rey Final qualification announcement + token utility:
    → Combined signal: competitive achievement + commercial activation
    → Strongest short-term LTUI uplift in domestic cup context
    
MEMORY TICKETS (blockchain-native collectibles):
  PSG Concorde platform: digital tokens tied to stadium attendance
  Cup finals as memory ticket events: special edition commemorative tokens
  Signal: positive for Phase 4-5 transition (collectibles as continued engagement)
  Load fan-token/rwa-sportfi-intelligence/ for memory ticket framework
```

---

## Cup competition calendar — annual overview

```
ANNUAL CUP SIGNAL CALENDAR:

August:
  Champions League qualifying (R1-R3): clubs entering at qualifying stage
  DFB-Pokal R1: German lower vs higher division
  
September-October:
  FA Cup R1-R2: Pre-PL entry; monitoring only
  Carabao Cup (EFL) R2-4: PL clubs enter; minor signal
  
November:
  UCL Group Matchday 4-5: qualification picture forming
  
December:
  FA Cup R3 draw announced: signal for pairings
  
January:
  FA Cup R3 (first January weekend): "Cup weekend" — highest domestic cup signal
  FA Cup R4: follow-on from R3 results
  Carabao Cup Semi-Finals: two-legged; moderate signal
  
February:
  FA Cup R5: Last 32; upset probability declining
  UCL R16 first legs: first UCL knockout signal of year
  Copa del Rey R16/QF: Spanish cup overlap
  
March:
  UCL R16 second legs + QF draw
  FA Cup QF
  Copa del Rey SF first legs
  
April:
  UCL QF both legs
  UCL SF draw + first legs
  FA Cup SF (Wembley)
  DFB-Pokal SF
  
May:
  UCL SF second legs
  Domestic cup Finals (FA Cup, Copa, Coppa, DFB, Coupe)
  UCL Final
  
June:
  Europa League Final, Conference League Final
```

---

## Compatibility

**Football leagues:** `market/football-leagues-advanced.md` — prize window context
**Derby intelligence:** `core/derby-intelligence.md` — cup derby fixtures
**Football token bridge:** `fan-token/football-token-intelligence/` — CSF inputs to FTIS
**RWA/SportFi:** `fan-token/rwa-sportfi-intelligence/` — memory ticket collectibles
**Lifecycle:** `fan-token/fan-token-lifecycle/` — token-gated cup access as utility

*MIT License · SportMind · sportmind.dev*
