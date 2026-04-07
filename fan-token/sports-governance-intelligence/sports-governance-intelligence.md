# Sports Governance Intelligence

**The intelligence framework for on-chain sports governance — DAO patterns,
fan token voting mechanics, club decision-making, and the emerging model of
fan participation in sports organisations.**

---

## Why governance intelligence matters now

Fan token governance has existed since 2019 (Juventus $JUV on Socios) but has
largely been limited to cosmetic decisions — kit colours, training music, charity
donations. The commercial case for deeper governance is now being made by multiple
stakeholders simultaneously:

- **Clubs** are realising that engaged governance participants are more loyal
  commercial consumers than passive fans
- **Token platforms** are building infrastructure for more meaningful votes
- **Regulators** (EU MiCA, UK FCA) are clarifying the legal framework for
  tokenised participation rights
- **Web3 sports projects** (DAO-based clubs, fan-owned football experiments)
  are demonstrating that fan governance can extend beyond cosmetics

SportMind's governance intelligence framework covers all of these dimensions —
from the current Socios governance model through to the emerging DAO-based
club ownership structures.

---

## Governance Signal Index (GSI)

```
GSI = (Participation_Rate × 0.30) + (Decision_Weight × 0.30)
    + (Transparency_Score × 0.25) + (Execution_Track_Record × 0.15)

PARTICIPATION_RATE (what % of eligible holders vote?):
  > 30% participation:   1.00 — highly engaged governance community
  15-30%:                0.80 — healthy engagement
  5-15%:                 0.55 — moderate; improvement possible
  < 5%:                  0.25 — governance fatigue or disengagement signal

DECISION_WEIGHT (how meaningful are the decisions being voted on?):
  Structural (manager appointment, stadium naming, equity):  1.00
  Commercial (major partnership, shirt sponsor):             0.80
  Competitive (player signing input, tactical preference):   0.65
  Operational (training location, kit design):              0.45
  Cosmetic (travel playlist, warmup music):                 0.15

TRANSPARENCY_SCORE (how visible is the governance process?):
  On-chain, auditable, results published immediately:        1.00
  Off-chain but publicly reported:                          0.75
  Results announced but process opaque:                     0.50
  Results not consistently published:                       0.20

EXECUTION_TRACK_RECORD (does the club act on vote results?):
  Always executes vote outcomes:                            1.00
  Usually executes (>80%):                                  0.80
  Sometimes executes (<80%):                                0.50
  Rarely/never executes:                                    0.10
  
  WARNING: Governance where the club does not execute on outcomes
  is not governance — it is theatre. GSI < 0.40 with low execution
  track record = governance_theatre flag; LTUI impact negative.
```

---

## Current governance model — Socios/Chiliz

```
THE SOCIOS GOVERNANCE MODEL (2019-present):

How it works:
  Token holders vote on predefined club decisions via the Socios app
  One token = one vote (typically weighted by token holding)
  Vote window: usually 48-72 hours
  Results: announced on app and club social channels
  
Decision categories in practice:
  Most common: design/aesthetic choices (kit, bus livery, locker room music)
  Growing: commercial preferences (preferred charity, community initiatives)
  Emerging: meaningful input on club decisions (player signing preference polls)
  
  NOTE: Socios governance is currently predominantly cosmetic (Decision_Weight 0.15-0.45).
  This is a deliberate platform choice — lower legal/regulatory complexity.
  The trajectory is toward more meaningful decisions as the regulatory framework clarifies.

GSI FOR TYPICAL SOCIOS GOVERNANCE:
  Participation_Rate: 0.55-0.75 (variable by club; major clubs higher)
  Decision_Weight: 0.25-0.45 (mostly cosmetic to operational)
  Transparency_Score: 0.75 (off-chain but publicly reported)
  Execution_Track_Record: 0.85 (clubs generally execute on Socios decisions)
  
  Typical GSI range: 0.50-0.70 (moderate governance quality)

GOVERNANCE TOKEN vs GOVERNANCE MECHANISM:
  The fan token IS the governance token (no separate governance token)
  This means commercial activity and governance participation use the same instrument
  Holding for governance = holding for speculation (same token)
  This alignment is commercially useful but creates governance distortion:
  Whales (large holders) dominate votes regardless of fan authenticity
```

---

## DAO-based sports governance — the emerging model

```
SPORTS DAO STRUCTURES (2024-2026):

TYPE 1 — DAO-owned clubs:
  Fans collectively own and govern a football club via DAO
  Example: Wrexham pre-Hollywood (fan trust model, not DAO but conceptually similar)
  
  True DAO club governance:
    Tokenised shares → each token = governance rights + economic rights
    Major decisions (manager appointment, transfer budget): on-chain vote
    Day-to-day operations: delegated to professional management
    
  SIGNAL FOR SPORTMIND:
    DAO ownership = Decision_Weight 0.80-1.00 (meaningful structural decisions)
    If club achieves promotion: governance token = equity value event
    Apply LTUI × 1.25 for structural decision governance vs cosmetic

TYPE 2 — DAO fan councils:
  Advisory body to club board; no binding authority but formal consultation rights
  Growing model: gives fans voice without transferring control
  
  Example: Real Madrid's socios model (traditional membership, not blockchain)
  Blockchain adaptation: on-chain fan council with formal advisory rights
  
  SIGNAL: Fan council decisions with genuine advisory weight =
  GSI Decision_Weight 0.50-0.65 (above cosmetic, below structural)

TYPE 3 — Specific decision DAOs:
  One-off governance events for specific high-stakes decisions
  Example: "Should we accept this naming rights offer for the stadium?"
  Token holders vote; result is binding
  
  This is the near-term most likely expansion of Socios governance
  Compatible with current regulatory framework
  LTUI impact: each binding decision vote = engagement spike + utility confirmation

TYPE 4 — Multi-club governance:
  A DAO governing a group of clubs across tiers or countries
  City Football Group model adapted to DAO structure
  Complex but emerging in lower-tier football
```

---

## On-chain voting mechanics

```
VOTING MECHANISM INTELLIGENCE:

SIMPLE MAJORITY (most common):
  50%+ wins
  Risk: low participation can produce unrepresentative outcomes
  Mitigation: quorum requirements (minimum % must vote for result to be valid)
  Signal: clubs with quorum requirements = higher governance maturity

QUADRATIC VOTING:
  Votes cost proportional to the square of the number of votes cast
  Prevents whale dominance (holding 10× tokens doesn't give 10× influence)
  More equitable for minority holders
  SportMind flag: quadratic_voting_active → lower whale dominance risk

CONVICTION VOTING:
  Votes accumulate strength over time (longer-held positions carry more weight)
  Rewards long-term holders; reduces governance mercenaries
  LTUI signal: conviction voting = structural incentive for long-term holding

DELEGATED VOTING:
  Token holders delegate votes to trusted representatives
  Reduces governance fatigue (not every holder needs to vote on everything)
  Risk: delegate capture (small group controls voting outcomes)
  
AGENT RULE: For any governance analysis, identify the voting mechanism first.
Simple majority + no quorum + high whale concentration = governance_theatre risk.
Quadratic or conviction voting = higher governance quality signal.
```

---

## Governance and the fan token lifecycle

```
GOVERNANCE AS LIFECYCLE SIGNAL:

PHASE 1 (Launch):
  Governance votes are marketing events — drive awareness of the token
  High participation expected (novelty effect)
  Decision_Weight typically low (cosmetic only)
  GSI diagnostic: if participation is high but Decision_Weight is 0.15-0.30,
  this is a healthy Phase 1 pattern, not governance theatre

PHASE 2 (Active Utility):
  Governance votes are utility events — they prove the token does something
  Participation stabilises; Decision_Weight should increase gradually
  Target GSI for healthy Phase 2: 0.60-0.75
  
  WARNING SIGNAL: Phase 2 with declining participation + no Decision_Weight increase
  → Phase 3 governance fatigue approaching

PHASE 3 (Plateau):
  Governance fatigue is a primary Phase 3 driver
  Holders stop voting because decisions feel meaningless
  Participation_Rate declines systematically
  
  INTERVENTION OPTIONS:
  1. Introduce meaningful decision (structural vote): spike in participation
  2. Reduce vote frequency: fewer votes = each vote feels more significant
  3. Introduce binding decisions: execution track record improvement
  4. Quadratic voting: restores holder confidence in fairness

PHASE 4-5 (RWA/SportFi):
  Governance transforms: token holders vote on financial decisions
  Revenue distribution, treasury management, capital allocation
  Decision_Weight 0.80-1.00 by Phase 5
  GSI target for mature sports DAO: 0.75+

LTUI IMPACT OF GOVERNANCE QUALITY:
  High GSI (0.75+): LTUI +8-12 per governance cycle (sustained utility)
  Medium GSI (0.50-0.74): LTUI +3-7 (moderate utility)
  Low GSI (0.25-0.49): LTUI neutral to -2 (governance fatigue risk)
  Governance theatre (< 0.25): LTUI -5 to -10 (trust erosion)
```

---

## Club governance intelligence for agents

```
BEFORE ANY GOVERNANCE VOTE ANALYSIS:

1. IDENTIFY DECISION TYPE:
   Cosmetic → Decision_Weight 0.15
   Operational → 0.45
   Commercial → 0.65-0.80
   Structural → 0.80-1.00
   
2. CHECK PARTICIPATION HISTORY:
   What was participation rate in last 3 votes?
   Declining trend = governance fatigue signal
   Spike = meaningful decision or campaign driving participation
   
3. EXECUTION TRACK RECORD:
   Has the club executed on the last 5 vote outcomes?
   < 80% execution rate = governance_theatre risk flag
   
4. VOTING MECHANISM:
   Simple majority / quadratic / conviction / delegated?
   Identify whale concentration risk
   
5. REGULATORY CONTEXT:
   EU club (MiCA applies): governance token = financial instrument if economic rights
   UK club (FCA framework): check promotion/restriction rules
   USA club (SEC): most cautious jurisdiction for governance tokens
   
6. LTUI PROJECTION:
   Model the vote outcome for LTUI (same framework as app-08-governance-intelligence.md)
   Add GSI context: high-GSI governance makes LTUI projections more reliable

GOVERNANCE BRIEF TEMPLATE:
  Vote: [Decision]
  Decision Weight: [Cosmetic/Operational/Commercial/Structural]
  GSI: [Score] / [Tier]
  Historical Participation: [%] (trend: [rising/stable/declining])
  Execution Track Record: [%]
  Voting Mechanism: [Type]
  LTUI YES: [projection]
  LTUI NO: [projection]
  Governance Quality Assessment: [brief note]
```

---

## Governance signal flags

```
NEW FLAGS:

governance_theatre:
  Activated when: GSI < 0.35 OR execution_track_record < 0.60
  Effect: LTUI projection reliability reduced; note in output
  Warning: "Governance may not represent genuine holder influence"

governance_fatigue:
  Activated when: participation_rate declining for 3+ consecutive votes
  Effect: LTUI stability concern; Phase 3 proximity signal
  Warning: "Declining engagement in governance suggests lifecycle transition"

structural_vote_active:
  Activated when: Decision_Weight ≥ 0.80 (meaningful structural decision)
  Effect: × 1.15 to LTUI projection; elevated engagement expected
  Positive signal: "Meaningful governance event — maximum holder engagement expected"

whale_dominance_risk:
  Activated when: top 10 addresses hold > 40% of voting tokens
  Effect: governance outcome may not represent median holder preference
  Note: less severe with quadratic voting (apply × 0.75 reduction)
```

---

## Compatibility

**App 8 (Governance Intelligence):** `examples/applications/app-08-governance-intelligence.md`
**Fan token lifecycle:** `fan-token/fan-token-lifecycle/` — governance as Phase signal
**RWA/SportFi:** `fan-token/rwa-sportfi-intelligence/` — Phase 5 governance evolution
**Manager intelligence:** `core/manager-intelligence.md` — manager appointment votes
**Broadcaster intelligence:** `market/broadcaster-media-intelligence.md` — governance for media decisions

*MIT License · SportMind · sportmind.dev*
