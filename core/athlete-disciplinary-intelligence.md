# Athlete Disciplinary Intelligence — SportMind Core

**The framework for modelling disciplinary events, sanctions, and their cascading
effects across sporting performance, fan sentiment, commercial value, and fan token signals.**

Disciplinary events are categorically different from injury or form signals. A ban
has a defined return date. A criminal charge has no defined resolution timeline. A
red card affects one match. A governance sanction can affect a club for years.
Standard athlete availability models treat all absences identically. They do not.

This skill models the full disciplinary signal chain: the offence → the regulatory
response → the performance impact → the multi-axis sentiment cascade.

---

## Why disciplinary intelligence is a distinct layer

```
WHAT STANDARD AVAILABILITY MODELS SEE:
  Player X: SUSPENDED → availability modifier ×0.72
  Return date: 3 matches
  
WHAT DISCIPLINARY INTELLIGENCE ADDS:
  Offence type: violent conduct (elbow, high force, off-ball)
  Regulatory body: World Rugby citing commissioner
  Process stage: cited → hearing scheduled → verdict pending
  Precedent: similar offence = 6–10 week ban in past 12 months
  Character context: first offence vs. repeat offender
  Fan reaction: polarised (42% defending player, 58% condemning)
  Commercial reaction: sponsor issued holding statement
  Token impact: -4.2% in 24h post-citation, recovering as verdict pending
  
  THESE ARE DIFFERENT SIGNALS WITH DIFFERENT DOWNSTREAM EFFECTS
```

---

## Disciplinary event taxonomy

### Tier 1 — On-field technical offences
Low severity. Routine sporting regulation.

| Type | Examples | Typical consequence | Sentiment impact |
|---|---|---|---|
| Yellow card / sin bin | Cynical foul, time-wasting, dissent | 10-min sin bin or caution | Minimal — routine |
| Technical infringement | Forward pass, knock-on, offsides | Free kick / penalty | None |
| Deliberate knock-on | Preventing try / goal | Yellow/red card + penalty try | Minor — specific context |
| Dissent (minor) | Verbal protest to referee | Yellow card | Minor — supporter sympathy |

**Agent rule:** Tier 1 events within normal match context → no disciplinary modifier beyond
standard availability. Apply only if accumulation triggers suspension (e.g. 5 yellows = 1-match ban).

---

### Tier 2 — On-field conduct offences
Moderate severity. Typically triggers citing / charge process.

| Type | Examples | Typical ban range | Sentiment impact |
|---|---|---|---|
| Dangerous play | Dangerous tackle, high contact | 2–6 weeks | Moderate — depends on injury caused |
| Foul play | Stamping, raking, biting | 4–12 weeks | High — deliberate intent |
| Violent conduct | Punching, elbowing, headbutt | 6–20 weeks | High to severe |
| Red card + citing | Sent off AND cited by citing commissioner | Added to red-card ban | High |
| Abuse of match official | Verbal abuse of referee | 3–8 matches | High — fan polarisation |

**Agent rule:** Tier 2 events → apply DSM (Disciplinary Sentiment Modifier) at MODERATE level.
Performance modifier: ×0.72 (SUSPENDED) for absence duration.
Sentiment modifier: see DSM framework below.

---

### Tier 3 — Off-field conduct offences
High severity. Extends beyond the sporting moment.

| Type | Examples | Typical consequence | Sentiment impact |
|---|---|---|---|
| Social media misconduct | Discriminatory post, inflammatory content | 3–8 match ban + fine | Severe — brand damage |
| Betting violations | Betting on own matches or sport | Season ban or lifetime | Catastrophic |
| Doping violation | Failed drugs test | 2–4 year ban | Catastrophic |
| Bringing game into disrepute | Public intoxication, brawl | Variable | High |
| Failure to cooperate | Non-disclosure, refused test | Extended ban | Severe |

**Agent rule:** Tier 3 events → apply DSM at SEVERE level regardless of playing absence.
Commercial cascade is primary signal. Fan token agents must flag COMMERCIAL_RISK_ACTIVE.

---

### Tier 4 — Criminal and legal proceedings
Maximum severity. Unresolved timeline. Highest uncertainty.

| Type | Examples | Regulatory response | Sentiment impact |
|---|---|---|---|
| Criminal charge (non-violent) | Fraud, financial crime | Club suspension pending outcome | High to severe |
| Criminal charge (violent) | Assault, domestic violence | Immediate contract suspension likely | Catastrophic |
| Conviction | Any criminal conviction | Contract termination risk | Catastrophic |
| Civil proceedings | Civil lawsuit, restraining order | Variable by jurisdiction | Moderate to severe |

**Agent rule:** Tier 4 events → ABSTAIN from commercial recommendations until resolution.
Apply uncertainty flag: LEGAL_PROCEEDINGS_ACTIVE. Do not model outcome.
Timeline: unknown until verdict. Check for new information before each signal cycle.

---

## Sport-specific disciplinary frameworks

### Football — FA / UEFA / FIFA structure

```
ON-FIELD PROCESS:
  Referee decision → Yellow/red card at match level
  Match report submitted within 24h
  For sending-off: automatic 1-match ban minimum
  For additional misconduct: referee report triggers FA review
  
CITING / CHARGE PROCESS:
  FA Regulatory Commission: domestic offences
  UEFA Control, Ethics and Disciplinary Body (CEDB): European competitions
  FIFA Disciplinary Committee: international matches and World Cup

KEY THRESHOLDS:
  5 yellow cards (domestic league) = 1-match ban
  10 yellow cards = 2-match ban
  Violent conduct red card = minimum 3-match ban
  Assault on referee = minimum 12-match ban
  Discriminatory conduct = minimum 5-match ban + education programme

APPEAL PROCESS:
  Appeal to: FA Appeal Board / UEFA Appeals Body / FIFA Appeal Committee
  Typical timeline: 7-21 days from charge to verdict
  Interim period: if ban NOT suspended on appeal, player misses matches during process

OFF-FIELD STRUCTURE:
  FA Regulation E1(b): bringing the game into disrepute
  Scope: social media, public conduct, criminal proceedings, betting
  Timeline: unpredictable — can run for months
  
AGENT INSTRUCTION: Check FA Disciplinary Procedures document for current season
thresholds — they are reviewed annually. Accumulation thresholds may vary by competition.
```

---

### Rugby Union — World Rugby citing commissioner process

```
ON-FIELD PROCESS:
  Referee: yellow card (10-min sin bin) or red card (dismissal)
  Red card: automatic citing commissioner review within 24h
  
CITING COMMISSIONER PROCESS:
  Any incident can be cited within 48h of match (even if not red-carded)
  Citing commissioner reviews footage independently
  Decision: cited (to judicial hearing) or not cited
  
JUDICIAL HEARING:
  Independent judicial officer (not World Rugby employee)
  Timeline: typically within 7-10 days of incident
  Standard of proof: balance of probabilities
  
ENTRY POINT BANS (World Rugby Regulation 17):
  Low end: 2 weeks
  Mid-range: 6 weeks
  Top end: 12 weeks
  For most serious (intentional, severe injury): 52+ weeks
  
AGGRAVATING FACTORS (increase ban):
  - Vulnerability of victim
  - Degree of force
  - Nature of foul play (deliberate vs. reckless)
  - Existence of prior offences (doubling of entry point possible)
  - Targeting the head
  
MITIGATING FACTORS (reduce ban):
  - Clear and early guilty plea (up to 50% reduction)
  - Remorse and good character
  - First offence
  - Interference of play (contact was incidental)

AGENT INSTRUCTION: Entry point + aggravating/mitigating factors determines actual ban.
An agent should not model the outcome — it should flag CITING_PENDING and apply
AVAILABILITY: UNCERTAIN until verdict. Post-verdict: apply full calculated absence.
```

---

### MMA — Athletic Commission and UFC structure

```
EXISTING SPORTMIND SIGNAL: weight_miss_modifier already covers pre-fight signals
DISCIPLINARY ADDS: post-fight and between-fight conduct

IN-COMPETITION:
  Referee stoppage for illegal blow: point deduction or DQ
  Groin shot, eye poke, late hit: variable (referee discretion)
  
POST-FIGHT TESTING:
  USADA (UFC Anti-Doping): year-round testing
  State athletic commissions: post-fight testing
  Timeline from failure to sanction: 3-6 months
  
UFC CODE OF CONDUCT:
  Covers: criminal charges, social media, public conduct
  Consequence: suspension, fine, removal from rankings
  Extreme cases: contract termination

AGENT INSTRUCTION: For active USADA investigations → flag DOPING_REVIEW_ACTIVE.
This suppresses signal (do not generate commercial recommendations during review).
For criminal charges: flag LEGAL_PROCEEDINGS_ACTIVE.
```

---

### Cricket — ICC and domestic board structure

```
ICC CODE OF CONDUCT:
  Level 1: Minor offences (send-off, abuse of equipment) — fine, 1 demerit point
  Level 2: Serious offences (excessive appealing, contact with umpire) — fine + 2-4 points
  Level 3: Major offences (intimidation of umpire) — ban + 4-5 points
  Level 4: Most serious (physical assault) — ban from all cricket
  
DEMERIT POINT ACCUMULATION:
  4 points in 24 months → 2 Test / 4 ODI / 4 T20I ban
  8 points in 24 months → 4 Test / 8 ODI / 8 T20I ban
  
SPIRIT OF CRICKET INCIDENTS:
  Not subject to formal ICC process but generate significant sentiment signal
  Examples: ball tampering, Mankad dismissals (pre-law-change debates), sledging
  Agent rule: Spirit of Cricket incidents → apply SENTIMENT_CONTROVERSY_ACTIVE flag
  No availability modifier (no ban), but fan/commercial sentiment affected
  
BALL TAMPERING: Tier 4-equivalent. Career-damaging. Apply full DSM SEVERE.

AGENT INSTRUCTION: ICC charges are public within 24h of incident.
Demerit point history is published and verifiable.
```

---

### Formula 1 — FIA stewards and sporting regulations

```
RACE INCIDENT PROCESS:
  FIA stewards: real-time investigation during/after race
  Penalties: time penalty, grid penalty, drive-through, stop-go, DQ, race ban
  
SPORTING CODE:
  Article 12: disrepute and bringing sport into disrepute
  Covers: public statements, social media, conduct toward officials
  
SUPER LICENCE PENALTY POINTS:
  Points accumulate on super licence (equivalent to driving licence penalty points)
  12 points in 12 months = 1-race ban
  Most penalties: 2-3 points; serious incidents: 5-10 points
  
FIA ETHICS AND DIVERSITY COMMISSION:
  Covers: discriminatory conduct, political statements
  
AGENT INSTRUCTION: Super licence point total is public. Track accumulation.
A driver on 9+ points entering a high-incident circuit → flag SUSPENSION_RISK.
This is a pre-event signal not available in standard form models.
```

---

### Rugby League — Rugby League International Federation (RLIF) / NRL / Super League

```
Similar to Rugby Union but with differences:
  Sin bin: 10 minutes (same)
  Grade system: Grade A, B, C (low to high severity)
  Match review committee: reviews all send-offs and incidents
  Early guilty plea: significant sentence reduction (equivalent to World Rugby mitigation)
  
NRL SPECIFIC:
  NRL Integrity Unit: handles off-field conduct
  Supplements testing: strict liability
  
AGENT INSTRUCTION: Same framework as Rugby Union. CITING_PENDING flag applies.
Check competition-specific thresholds (NRL vs. Super League differ).
```

---

## The Disciplinary Sentiment Modifier (DSM) framework

The DSM quantifies how a disciplinary event affects the five sentiment dimensions
that SportMind tracks for fan token and commercial analysis.

```
FIVE SENTIMENT DIMENSIONS:

1. FAN_SENTIMENT        — How do existing fans react?
2. SOCIAL_SENTIMENT     — How does the broader public / social media react?
3. COMMERCIAL_SENTIMENT — How do sponsors and brand partners react?
4. COMPETITION_SENTIMENT — How does governing body / competition react?
5. BROADCAST_SENTIMENT  — How does media coverage change?
```

### DSM severity levels

#### DSM MINIMAL (Tier 1 offences — routine)
```
FAN_SENTIMENT:          No measurable change
SOCIAL_SENTIMENT:       No measurable change (normal match noise)
COMMERCIAL_SENTIMENT:   No change
COMPETITION_SENTIMENT:  Standard process, no escalation
BROADCAST_SENTIMENT:    Match commentary only
TOKEN_IMPACT:           None

AGENT ACTION: No DSM modifier. Standard availability modifier only if ban triggered.
```

#### DSM MODERATE (Tier 2 — on-field conduct offences)
```
FAN_SENTIMENT:          Polarised response (30-40% defend player, 60-70% condemn)
                        IF no injury caused: less severe condemnation
                        IF significant injury caused: majority condemn strongly
SOCIAL_SENTIMENT:       Elevated negative volume +200-400% above baseline for 48-72h
                        Decays quickly if no ongoing process (citing dropped)
                        Sustains if citing proceeds to hearing
COMMERCIAL_SENTIMENT:   Sponsor monitoring — no public statement at this stage
                        Club PR active — likely internal statement
COMPETITION_SENTIMENT:  Citing process active — potential ban forthcoming
                        Referee match report filed
BROADCAST_SENTIMENT:    Incident replayed extensively (24-48h)
                        Pundit debate — framing affects fan polarisation

TOKEN_IMPACT:           Immediate: -2 to -5% in 24h post-incident
                        Recovery: gradual if verdict is lenient OR player exonerated
                        Sustained: -3 to -8% if ban confirmed and player is key asset
                        
MODIFIER:               DSM_MODERATE = 0.88 applied to commercial signal
                        Duration: until verdict + 2 weeks post-verdict
AGENT ACTION: Apply DSM_MODERATE. Flag CITING_ACTIVE or BAN_CONFIRMED.
```

#### DSM SEVERE (Tier 3 — off-field conduct)
```
FAN_SENTIMENT:          Significant negative shift across majority
                        Exceptions: clubs with strong tribal loyalty may defend strongly
                        Long-term: fan base fractures along values lines
SOCIAL_SENTIMENT:       Viral negative coverage — extends beyond sports media
                        Duration: 2-4 weeks sustained (longer if ongoing process)
                        Re-ignites at each process milestone (charge, verdict, appeal)
COMMERCIAL_SENTIMENT:   Sponsor public statement likely (distancing or condemnation)
                        Activation hold on player-linked campaigns
                        Kit sale impact: measurable decline if player is key commercial asset
COMPETITION_SENTIMENT:  Investigation active — player potentially suspended pending outcome
                        Governing body may issue own statement
BROADCAST_SENTIMENT:    Dominates sports news cycle for 1-2 weeks minimum
                        Non-sports media pick-up (betting violations, doping, discrimination)
                        
TOKEN_IMPACT:           Immediate: -5 to -15% in 24-48h post-disclosure
                        Recovery: only begins when process resolves AND outcome is lenient
                        No recovery: if conviction/ban confirmed — establishes new baseline
                        
MODIFIER:               DSM_SEVERE = 0.72 applied to commercial signal
                        Duration: until full resolution of process
AGENT ACTION: Flag COMMERCIAL_RISK_ACTIVE. Reduce commercial signal weighting.
Do not generate fan token ENTER recommendation while COMMERCIAL_RISK_ACTIVE.
```

#### DSM CATASTROPHIC (Tier 4 — criminal / legal / doping)
```
FAN_SENTIMENT:          Majority negative for violent/sexual offences
                        Split/complex for non-violent (financial crime, drug use)
                        Club association: some fan distancing from club identity
SOCIAL_SENTIMENT:       Cross-media viral — national / international coverage
                        Sustained for months with each legal milestone
                        Cannot be managed by club PR alone
COMMERCIAL_SENTIMENT:   Sponsor contract review / suspension / termination
                        Major kit sponsors may activate morality clauses
                        Broadcast rights holders may restrict player content
COMPETITION_SENTIMENT:  Player may be suspended from competition pending legal outcome
                        Club may face secondary investigations (knowledge, conduct)
BROADCAST_SENTIMENT:    Player name becomes search term associated with offence
                        Coverage tone permanently altered (context follows all future coverage)

TOKEN_IMPACT:           Immediate: -10 to -35% depending on player prominence and offence type
                        Long-term: baseline reset (token may never recover to pre-incident level)
                        Timeline uncertainty: token price volatility elevated until resolution
                        
MODIFIER:               DSM_CATASTROPHIC: ABSTAIN from commercial recommendations
                        Flag: LEGAL_PROCEEDINGS_ACTIVE
AGENT ACTION: ABSTAIN. Do not model outcome. Generate no commercial signal.
Monitor: check for resolution at each agent cycle.
```

---

## Multi-axis sentiment cascade by offence type

### Case study A — Rugby: violent conduct red card + citing

```
EVENT: Starting prop cited for elbow to opponent's jaw. No injury. First offence.
Expected ban: 8–12 weeks (mid-range entry point + no prior offence mitigation)

T+0h  (incident in match):
  FAN_SENTIMENT:       Initial shock → polarisation begins online
  SOCIAL_SENTIMENT:    Clip circulates. Rugby community split.
  COMMERCIAL:          No immediate reaction
  BROADCAST:           Match punditry focuses on incident (30-min coverage)
  TOKEN:               -1.5% in first 4 hours (minor signal)

T+24h (citing confirmed):
  FAN_SENTIMENT:       Majority view: "had to be cited" — condemnation builds
  SOCIAL_SENTIMENT:    Peak volume day. #[PlayerName] trending in rugby circles.
  COMMERCIAL:          Sponsor monitoring. No statement.
  COMPETITION:         Citing commissioner confirms: referred to judicial hearing
  TOKEN:               -3.5% cumulative. CITING_ACTIVE flag.
  
T+7 days (judicial hearing):
  FAN_SENTIMENT:       Hearing date creates renewed focus. Defensive fans rally.
  SOCIAL_SENTIMENT:    Secondary peak. Pre-hearing character witness pieces.
  COMMERCIAL:          Sponsor issues ambiguous "aware of process" statement
  BROADCAST:           Pre-hearing analysis — ban length prediction debate
  TOKEN:               -2.5% (slight recovery from early shock, now pricing in process)

T+10 days (verdict: 8-week ban):
  FAN_SENTIMENT:       If ban = expected: acceptance. If ban > expected: outrage.
  SOCIAL_SENTIMENT:    Verdict spike (±) then rapid decay
  COMMERCIAL:          Sponsor releases brief supportive statement (if good character history)
  COMPETITION:         Ban confirmed, dates published
  TOKEN:               Ban duration priced in. Recovery begins if player not KEY_ASSET.
                       -4% sustained if STARTING_PLAYER in key competition phase.
                       
DSM applied: DSM_MODERATE throughout process. Remove on return + 2 weeks.
```

---

### Case study B — Football: off-field social media discrimination charge

```
EVENT: Midfielder posts discriminatory content on social media. Immediately deleted.
Club: Top-6 Premier League. Player: Key XI, significant commercial profile.

T+0h (post made):
  If not viral: incident may be contained for 24-48h
  If viral (most likely): immediate avalanche begins
  FAN_SENTIMENT:       Majority condemnation. Fans distancing publicly.
  SOCIAL_SENTIMENT:    Non-sports media pick-up within 6 hours
  COMMERCIAL:          Shirt sponsor legal review. Activation hold.
  BROADCAST:           Top of sports news within 12 hours
  TOKEN:               -8 to -12% within first 12 hours (major commercial asset)

T+24h (club statement):
  IF club acts quickly (condemns, player removed from squad):
    FAN_SENTIMENT: Majority approve club response. Slight recovery.
    TOKEN: Partial recovery (-5 to -8% from baseline)
  IF club acts slowly / defends player:
    FAN_SENTIMENT: Anger extends to club.
    TOKEN: Continued decline (-12 to -18%)

T+48–72h (FA charge):
  Charged: E1(b) — bringing the game into disrepute
  Minimum ban: 5 matches + education
  FAN_SENTIMENT: Process acceptance. Waiting for verdict.
  COMMERCIAL: Sponsor suspends all player activations pending resolution
  TOKEN: COMMERCIAL_RISK_ACTIVE flag. DSM_SEVERE applied.

T+3-6 weeks (verdict):
  IF conviction + ban: DSM_SEVERE sustained for ban duration + 6 weeks
  IF education + fine (no ban): DSM_MODERATE (residual commercial damage)
  
DSM: DSM_SEVERE throughout. DSM_MODERATE for 6 weeks post-verdict.
COMMERCIAL_RISK_ACTIVE until: charge dropped or verdict served + 6 weeks.
```

---

### Case study C — National team player: Tier 4 criminal charge (non-violent)

```
EVENT: National team captain charged with financial fraud. Not detained.
World Cup 2026: 8 weeks away.

IMMEDIATE (charge announced):
  FAN_SENTIMENT:       Deep complexity. Identity crisis for fans. "Captain" = club/country symbol.
  SOCIAL_SENTIMENT:    Global coverage (national team = broader audience than club)
  COMMERCIAL:          National FA reviews captain status. Major sponsors issue holding statements.
  COMPETITION:         FA/governing body: may remove captaincy. May suspend from squad.
  BROADCAST:           Dominates all sports media. Non-sports media lead story.
  TOKEN (if applicable): -20 to -35% immediate. LEGAL_PROCEEDINGS_ACTIVE.

WORLD CUP CONTEXT:
  IF player cleared before tournament: partial recovery, scrutiny remains
  IF proceedings unresolved at tournament start: governing body decision point
    → Player participates: controversy sustained throughout tournament
    → Player excluded: absence signal + commercial void
  IF convicted during tournament: catastrophic signal

AGENT ACTION: ABSTAIN from all commercial recommendations.
Do not model outcome. Monitor at each legal milestone.
Timeline unknown. Price in maximum uncertainty.
```

---

## DSM integration with existing SportMind signals

### Connection to athlete modifier system

```
EXISTING: core/core-athlete-modifier-system.md
  Psychological sub-modifier: covers "controversy, morale" at 0.78–1.12
  
DSM EXTENDS THIS:
  Controversy is now typed (Tier 1–4) with specific modifier values
  DSM replaces generic "controversy" with structured disciplinary modifier
  Integration: DSM value feeds INTO psychological sub-modifier
  
  If DSM_MODERATE (0.88): psychological sub-modifier floor = 0.85
  If DSM_SEVERE (0.72): psychological sub-modifier floor = 0.78
  If DSM_CATASTROPHIC: ABSTAIN overrides all sub-modifiers
```

### Connection to fan sentiment intelligence

```
EXISTING: fan-token/fan-sentiment-intelligence/
  Models emotional arc after sporting outcomes
  
DSM EXTENDS THIS:
  Disciplinary events create a NEGATIVE emotional arc
  This follows different phases from win/loss arcs:
  
  DISCIPLINARY EMOTIONAL ARC:
    Phase 1 — SHOCK (0-48h): maximum negative sentiment
    Phase 2 — PROCESS WATCH (48h to verdict): sustained negative, slight stabilisation
    Phase 3 — VERDICT RESPONSE (verdict day): spike up or down depending on outcome
    Phase 4 — INTEGRATION (1-4 weeks post-verdict): sentiment finding new baseline
    Phase 5 — MEMORY (varies): incident becomes part of player/club narrative
    
  IF verdict = lenient/exoneration: arc mirrors positive outcome recovery (Phase 3 upward)
  IF verdict = severe: no recovery arc — new lower baseline established
```

### Connection to brand score

```
EXISTING: fan-token/brand-score/
  Models commercial value of athlete-club brand association
  
DSM EXTENDS THIS:
  Tier 3-4 incidents directly reduce brand score
  DSM_SEVERE: brand score penalty -15 to -35 points
  DSM_CATASTROPHIC: brand score suspended (do not use until resolved)
  
  Recovery timeline:
    Minor (Tier 2, first offence): brand score recovers in 3-6 months
    Moderate (Tier 3): brand score recovers in 6-18 months IF no repeat
    Severe (Tier 4): brand score may permanently reset lower
```

### Connection to fan token signal

```
INTEGRATION POINT:
  Before generating any fan token commercial signal (ENTER/WAIT/ABSTAIN):
  
  Step 1: Check DSM_STATUS for all key squad players
  Step 2: If any key player = DSM_SEVERE or DSM_CATASTROPHIC → flag
  Step 3: Apply relevant commercial modifier or ABSTAIN
  
  RULE: Never generate ENTER recommendation when COMMERCIAL_RISK_ACTIVE
         or LEGAL_PROCEEDINGS_ACTIVE is set on a key commercial asset
```

---

## Agent reasoning protocol — disciplinary events

```
WHEN a disciplinary event is detected:

1. CLASSIFY the offence (Tier 1 / 2 / 3 / 4)
2. IDENTIFY the regulatory framework (sport-specific, see above)
3. DETERMINE process stage (pre-charge / charged / hearing scheduled / verdict)
4. APPLY DSM at appropriate severity level
5. CHECK player prominence (KEY_ASSET / REGULAR_XI / SQUAD / PERIPHERAL)
   — KEY_ASSET: maximum DSM impact on signal
   — PERIPHERAL: minimal token impact even at DSM_SEVERE
6. SET flags:
   — CITING_ACTIVE (Tier 2, on-field, pre-verdict)
   — COMMERCIAL_RISK_ACTIVE (Tier 3+)
   — LEGAL_PROCEEDINGS_ACTIVE (Tier 4)
   — SUSPENSION_RISK (accumulation approaching threshold)
7. GENERATE modified signal OR ABSTAIN

KEY RULE:
  Disciplinary uncertainty is WORSE than negative certainty.
  A confirmed 8-week ban prices into the signal cleanly.
  An unresolved criminal charge cannot be priced — ABSTAIN.
```

---

## Flags introduced by this skill

| Flag | Meaning | Trigger | Agent action |
|---|---|---|---|
| `CITING_ACTIVE` | Player cited, hearing pending | Tier 2 on-field citing confirmed | Apply DSM_MODERATE, reduce availability confidence |
| `BAN_CONFIRMED` | Ban verdict confirmed | Any confirmed suspension | Apply ban duration to availability + DSM |
| `COMMERCIAL_RISK_ACTIVE` | Commercial signal degraded by conduct | Tier 3 offence + active process | Downweight commercial recs, no ENTER |
| `LEGAL_PROCEEDINGS_ACTIVE` | Criminal/civil proceedings active | Tier 4 charge filed | ABSTAIN from commercial recs |
| `SUSPENSION_RISK` | Accumulation approaching ban threshold | N-1 yellow cards, N-1 points | Flag pre-match; lineup watch elevated |
| `CONDUCT_RESIDUAL` | Offence resolved but commercial residual | Post-verdict, Tier 3+ | Apply reduced commercial modifier for defined window |
| `INVESTIGATION_ACTIVE` | Internal investigation or USADA review | Announced investigation | Flag; monitor; no commercial rec |

---

## Cross-sport sentiment comparison

| Sport | Typical fan reaction speed | Commercial reaction speed | Token impact speed | Key driver |
|---|---|---|---|---|
| Football | Hours (social media saturation) | 12-24h (sponsor review) | 2-6h | Player commercial profile |
| Rugby Union | 24-48h (citing process slower) | 48-72h | 6-12h | Match importance |
| MMA | Hours (fight-day intensity) | 24h | 2-4h | Fight proximity |
| Cricket | 24-48h (Spirit of Cricket slower) | 48-72h | 12-24h | Test vs. T20 context |
| Formula 1 | Hours (global audience) | 12-24h | 4-8h | Championship implications |
| Rugby League | 24h (NRL audience density) | 48h | 8-16h | Origin/international context |

---

## Data sources for disciplinary monitoring

### Primary — official regulatory bodies
- **FA Disciplinary Procedures**: thefa.com/football-rules-governance/disciplinary
- **World Rugby Judicial Decisions**: world.rugby/the-game/judicial-decisions
- **UFC Official**: ufc.com (suspension announcements)
- **ICC Code of Conduct**: icc-cricket.com/about/cricket/rules-and-regulations
- **FIA Stewards Decisions**: fia.com/documents/decisions
- **NRL Integrity Unit**: nrl.com/news/integrity

### Secondary — verified aggregators
- **BBC Sport** (fastest mainstream for UK/European sports)
- **ESPN** (fastest for US-centric sports + global MMA)
- **Sky Sports** (Premier League + Rugby Union UK)
- **Rugby Pass** (Rugby Union disciplinary — specialist)
- **MMA Fighting** (UFC/MMA conduct — specialist)

### Social monitoring (sentiment cascade tracking)
- **X (Twitter) API**: real-time hashtag volume post-incident
- **Google Trends**: search spike = public awareness threshold crossed
- **Sponsor social channels**: holding statement detection

### Agent instruction for data sourcing
```
Priority order:
1. Official governing body statement (ground truth for process stage)
2. Club official statement (ground truth for commercial response)
3. BBC Sport / ESPN (mainstream awareness threshold)
4. Social monitoring (sentiment velocity and direction)

Do NOT use:
- Tabloid/gossip sources for unconfirmed allegations
- Anonymous sources for Tier 4 events
- Pre-verdict speculation as signal inputs
```

---

*SportMind v3.32 · MIT License · sportmind.dev*
*Connects to: core/core-athlete-modifier-system.md · fan-token/fan-sentiment-intelligence · fan-token/brand-score · core/core-narrative-momentum.md*
