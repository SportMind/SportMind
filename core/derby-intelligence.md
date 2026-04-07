# Derby Intelligence

**Specific signal characteristics for the highest-stakes rivalry matches across sport.**
The general derby framework (reduce form differential 40%, apply rivalry multiplier)
exists in `core/core-narrative-momentum.md`. This document extends it with the specific
characteristics of the 30 highest-signal derbies globally, plus the cross-sport
rivalry template.

---

## Why derby-specific intelligence matters

The general 40% form discount and rivalry multiplier are correct as defaults. But they
miss what makes each derby distinctive:

- **Some derbies have conduct risk far above the average.** The Superclásico (Boca vs River)
  has a different red card and incident probability than the Manchester derby.
- **Some derbies are genuinely coin-flip regardless of form distance.** India-Pakistan in
  cricket is functionally unpredictable in a way that Barcelona-Real Madrid is not.
- **Some derbies have one-sided historical dominance that changes the form discount.**
  Tottenham vs Arsenal is a rivalry. Arsenal's dominance in recent decades changes
  how that rivalry's form discount should be applied differently than a genuinely balanced one.
- **Some derbies have specific token signal characteristics.** El Clásico generates $BAR
  and $RM signals that behave differently from standard matches — the dual-token dynamic
  requires specific handling.

---

## The Derby Signal Model (DSM)

```
DSM = competition_tier_weight × rivalry_intensity × form_compression × conduct_risk

rivalry_intensity: How much does this derby override standard form?
  Maximum (0.90): Result is nearly unpredictable regardless of form differential
  High (0.75):    Form differential compressed significantly
  Moderate (0.60): Form still matters but rivalry effect is real
  Low (0.45):     Recognised rivalry but form is primary signal

form_compression (what % of form differential is discounted):
  Maximum intensity derbies:  50% discount (not 40% default)
  High intensity:             40% discount (library default)
  Moderate intensity:         25% discount
  Low intensity:              15% discount

conduct_risk modifier (red card / incident probability vs league average):
  Very high (> 2× average): × 0.92 on any modifier requiring clean game
  High (1.5–2× average):    × 0.95
  Average:                   × 1.00
  Low (< 0.75× average):    × 1.03 (clean game more likely)
```

---

## The 30 highest-signal football derbies

### Global Tier 1 — Maximum signal (rivalry_intensity 0.85–0.90)

**El Clásico — FC Barcelona vs Real Madrid**

```
Form compression:   50% — form differential is almost irrelevant
Conduct risk:       Average — well-managed by elite referees
Token dynamic:      DUAL TOKEN — $BAR and $RM both respond
  Both teams active: load multi-token event protocol
  $BAR holder base: Spain + Latin America + global
  $RM holder base:  Spain + Middle East + Latin America
  Pre-match (T-48h): social volume 10-15× normal; HAS spike both tokens
  Post-match: winning token +8-18%; losing token -6-12%
  Draw: modest positive for both (engagement event regardless)
Frequency:        2-4 times per season (La Liga x2, Copa del Rey if paired, Supercopa)
Best signal window: La Liga matches with title implications
ATM note:         Messi era generated $BAR maximum ATM — successor dynamics apply
```

**Superclásico — Boca Juniors vs River Plate (Argentina)**

```
Form compression:   50% — purest rivalry_intensity 0.90 in world football
Conduct risk:       VERY HIGH — 2× Argentine league average
  Red card probability: elevated; controversial decisions common
  Apply × 0.92 conduct modifier to any signal involving clean game assumption
Token dynamic:      No active Socios tokens currently
  Monitoring: Boca/River tokens would be highest-commercial Argentine sports tokens
  If tokens launch: this derby = maximum Argentine token signal event
Frequency:        2-3 times per season (Argentine Primera + Copa matches)
NCSI note:        Players from Boca/River in national squad: elevated
                  Argentine football identity is deeply Superclásico-linked
```

**Derby della Madonnina — AC Milan vs Inter Milan**

```
Form compression:   45% — high intensity, some form residual
Conduct risk:       High — heated, European club conduct risk elevated
Token dynamic:      DUAL TOKEN if both active
  Milan city pride + European pedigree = sustained holder engagement
  Champions League seasons: each derby amplified by European narrative
Frequency:        2 times per season (Serie A) + cup if drawn
Signal note:      Derby result can shift Champions League qualification
                  in tight Serie A seasons — apply stakes multiplier
```

**Manchester Derby — Manchester City vs Manchester United**

```
Form compression:   40% — high but City's sustained dominance affects
  NOTE: When form differential > 30 points: apply only 35% compression
  (City's structural superiority is real even in derbies in recent seasons)
Conduct risk:       Average
Token dynamic:      $CITY active (check $MUFC status)
  $CITY holder base: globally distributed; Premier League premium
  Derby week: HAS spike $CITY; social volume 5-8× normal
Frequency:        2 times per season + cups if drawn
```

**North London Derby — Arsenal vs Tottenham**

```
Form compression:   40%
Conduct risk:       Average to high
Token dynamic:      No active Socios tokens for either club currently
Historical note:    Arsenal's recent dominance (2020s) changes form compression:
  When Arsenal form differential > 25 points: apply 30% compression only
  Tottenham have won this derby against strong Arsenal sides historically
Frequency:        2 times per season + cups
```

**Celtic vs Rangers — The Old Firm (Scotland)**

```
Form compression:   50% — rivalry_intensity 0.88 — genuine 50/50 regardless
Conduct risk:       Very high — highest incident probability in British football
  Red card probability: 2.5× Scottish Premiership average
  Apply × 0.90 conduct modifier
Cultural context:   Religious/cultural dimensions create maximum emotional intensity
  Form becomes almost irrelevant — apply 50% compression without exception
Token dynamic:      No active tokens; strong case for both — loyal domestic fanbases
Frequency:        3-6 times per season (league x2 + cup appearances)
```

---

### Global Tier 1 — High signal (rivalry_intensity 0.75–0.85)

**El Clásico Colombiano — Millonarios vs América de Cali**
**Fenerbahçe vs Galatasaray (Turkey)**
**Boca Juniors vs San Lorenzo / Independiente**
**Dortmund vs Schalke — Revierderby (Germany)**
**Marseille vs PSG — Le Classique (France)**
**Roma vs Lazio — Derby della Capitale (Italy)**

```
MARSEILLE vs PSG — LE CLASSIQUE:
  French football's primary rivalry signal
  Token: $PSG active; OM token monitoring
  Form compression: 45% — PSG structural dominance but Le Classique equalises
  PSG away at Marseille: apply ×1.20 home atmosphere modifier (Vélodrome)
  Pre-match H48h: $PSG HAS spike; OM community engagement peak
  
DORTMUND vs SCHALKE (Revierderby):
  Most attended German derby — Ruhr industrial identity
  Token: Track Bundesliga club token launches
  Currently suspended: Schalke's relegation/return cycle disrupts rivalry continuity
  Restoration signal: when both clubs in same division → Revierderby resumes full weight
```

---

### Premier League secondary derbies

```
MERSEYSIDE — Liverpool vs Everton:
  Form compression: 40%; Liverpool structural dominance recent decades
  Conduct risk: Average; typically well-managed
  Everton relegation risk (recent): check competitive status before analysis

WEST MIDLANDS — Aston Villa vs Birmingham / Villa vs Wolves:
  Form compression: 35%; clear quality gaps in recent years
  Signal weight depends on competitive proximity in table

LONDON DERBIES (general):
  Chelsea vs Arsenal, Chelsea vs Spurs, West Ham vs various:
  Apply standard 40% compression + conduct modifier by specific pairing
  All qualify for ×1.15-1.20 rivalry multiplier
```

---

### La Liga secondary derbies

```
SEVILLE DERBY — Sevilla vs Real Betis:
  Form compression: 45% — genuinely balanced historically
  Conduct risk: High — passionate; apply × 0.94
  Token: Monitor both clubs for Socios activity (both have commercial relationships)

MADRID DERBY — Atlético vs Real Madrid:
  Form compression: 42%
  Token: $RM active; Atlético token monitoring
  Tactical note: Atlético's defensive style means lower-scoring outcomes more likely
                 Adjust expected-goals-based analysis accordingly
```

---

### Other major European derbies

```
AMSTERDAM DERBY — Ajax vs Feyenoord (Klassieker, Netherlands):
  Strongest Dutch rivalry; form compression 40%
  Conduct risk: High historically
  
PORTO vs BENFICA vs SPORTING (O Clássico Português):
  Three-way Portuguese rivalry; each pairing has its own characteristics
  Porto-Benfica: rivalry_intensity 0.80
  
GLASGOW DERBY covered above (Old Firm)
BELGRADE (Crvena zvezda vs Partizan): rivalry_intensity 0.82, conduct risk very high
```

---

## Cross-sport derby intelligence template

The derby concept applies across all major team sports. Use this template for
any sport not individually documented above.

```
CROSS-SPORT DERBY TEMPLATE:

STEP 1 — CLASSIFY THE RIVALRY:
  Continental (e.g., State of Origin): maximum intensity (0.88-0.90)
  City/regional (e.g., Manchester derby): high intensity (0.75-0.85)
  League/historical (e.g., historic rivals): moderate (0.60-0.75)
  Competitive (two good teams often meeting): low-moderate (0.45-0.60)

STEP 2 — IDENTIFY SPORT-SPECIFIC FORM COMPRESSION:
  Combat sports (MMA, boxing): form compression NOT applied — individual skill dominates
  Team sports with high individual variance (basketball): 25-35% compression
  Team sports with tactical systems (football, rugby): 35-50% compression
  Cricket: format-dependent (Test: 30%, T20: 20% — T20 variance too high for large compression)

STEP 3 — CONDUCT RISK ASSESSMENT:
  Sport-specific average card/incident rates from core/core-officiating-intelligence.md
  Derby-specific elevation: typically 1.5-2.5× sport average for Tier 1 rivalries

STEP 4 — TOKEN DUAL-SIGNAL PROTOCOL:
  If both clubs have active tokens: load multi-token event protocol
  Signal direction: winning team's token rises; losing team's falls
  Draw: engagement event — modest positive for both (rare outcome narrative)
  
SPORT-SPECIFIC RIVALRY EXAMPLES:
  NRL: Storm vs Broncos, Roosters vs Rabbitohs
  AFL: Collingwood vs Carlton (highest VIC attendance), Collingwood vs Essendon
  NBA: Lakers vs Celtics (historical; geography-divided now), Knicks vs Nets
  NHL: Maple Leafs vs Canadiens (Original Six), Penguins vs Capitals (Crosby vs Ovechkin era)
  MLB: Yankees vs Red Sox, Dodgers vs Giants
  Cricket: India vs Pakistan (×2.00 — see cricket cycle), Ashes
  Rugby: Bledisloe Cup (Australia vs NZ), Calcutta Cup (England vs Scotland)
```

---

## Derby signal flag

```
NEW FLAG: derby_active

Activate when: this match is a recognised derby (Tier 1 or 2 from this document,
  or cross-sport template classification)

Effect on confidence output:
  adjusted_score uncertainty band: widened by ±5 points
  recommended_action: never STRONG_ENTER in a derby (maximum: ENTER)
  reasoning_summary: must note derby compression applied and percentage used
  
  "Derby signal active: El Clásico form differential compressed 50%.
   Adjusted_score 68.4 should be treated as 65-72 range rather than point estimate."

AGENT RULE: In a derby, always present adjusted_score as a range, never a point.
The form compression introduces genuine uncertainty that a point estimate misrepresents.
```

---

## Compatibility

**Narrative momentum:** `core/core-narrative-momentum.md` — general rivalry framework
**Football token bridge:** `fan-token/football-token-intelligence/` — dual token protocol
**Officiating intelligence:** `core/core-officiating-intelligence.md` — conduct risk data
**Manager intelligence:** `core/manager-intelligence.md` — managers' derby records
**International cycles:** `market/international-football-cycle.md` — national team rivalries

*MIT License · SportMind · sportmind.dev*
