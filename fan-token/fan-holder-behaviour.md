---
name: fan-holder-behaviour
description: >
  Enduring patterns in fan token holder behaviour — how holders act around
  match events, tournament windows, supply events, and governance participation.
  Covers pre-match accumulation, post-tournament-exit decay, claim period
  behaviour, governance participation patterns, supply event response, World Cup
  behaviour, and agent reasoning guidance. Reference cases from $BELG FTO (June
  2026) and UCL Final 2026. Library Rule: PASSES — enduring behaviour patterns,
  not specific data.
---

# Fan Holder Behaviour — Enduring Patterns

**Scope:** How fan token holders act around match events, tournament windows, supply events, and governance.
**Calibration basis:** Chiliz ecosystem operational data, FTP PATH_2 records, FTO participation records.

---

## Overview

Fan token holders are not passive investors. Their behaviour is event-driven,
emotionally linked to club performance, and follows predictable patterns that
agents reasoning about fan token demand must understand.

```
CORE INSIGHT:
  Fan token demand is not driven by fundamental valuation.
  It is driven by emotional proximity to competitive events.
  The holder who accumulates before a UCL final is not calculating
  intrinsic value — they are expressing identity and anticipation.

  An agent that treats fan tokens like financial instruments
  will misread the demand signal.

  An agent that understands holder behaviour can:
    · Anticipate accumulation windows before high-demand fixtures
    · Model post-elimination decay rates by club tier
    · Identify governance disengagement before price signals confirm it
    · Separate genuine demand from tournament-amplified noise
```

---

## Pre-Match Accumulation Windows

```
PATTERN:
  Holders typically accumulate in the 48-72 hour window before
  high-demand fixtures. Accumulation velocity increases as kickoff approaches.

HIGHEST-DEMAND FIXTURES (accumulation triggers):
  UCL Final:              ×2.00 occasion weight — strongest accumulation signal
  Domestic cup final:     ×1.60
  UCL semi/quarter:       ×1.60 / ×1.40
  Derby match:            ×1.35
  National team knockout: varies by nation tier (see World Cup section)
  UCL group stage:        ×1.40 — less dramatic but still elevated

TIMING PATTERN:
  T-72h: accumulation begins for major fixtures
  T-48h: pre-liquidation events confirm demand (FTP PATH_2 activation)
          The act of pre-liquidation at T-48h IS a demand signal to the market
          — it confirms holder expectation of outcome
  T-24h: accumulation accelerates with lineup confirmation
  T-2h:  final demand surge, lineup confirmed
  Post-kickoff: demand settles based on match flow

PRE-LIQUIDATION AS DEMAND SIGNAL:
  When FTP PATH_2 activates and pre-liquidation fires at T-48h:
    · Pool size reflects aggregate holder expectation of outcome
    · Larger pool = more holders expecting result-driven supply change
    · Pool size is a revealed preference signal, not a survey

AGENT RULE:
  Pre-match accumulation patterns are directional, not precise.
  Use as a demand confirmation signal alongside sport domain analysis —
  not as a standalone signal.
```

---

## Post-Tournament-Exit Decay

```
PATTERN:
  When a club or national team is eliminated from a tournament,
  demand drops sharply within 24-48 hours of elimination.

DECAY TIMELINE BY TIER:
  Tier A clubs ($PSG, $BAR, $AFC, $CITY):
    Recovery: 2-4 weeks
    Mechanism: league activity maintains holder engagement
    Floor: above pre-tournament baseline (UCL run generated awareness)

  Tier B clubs ($GAL, $ATM, $JUV):
    Recovery: 4-6 weeks
    Mechanism: slower — fewer alternative engagement drivers
    Floor: returns approximately to pre-tournament baseline

  Tier C clubs and lower:
    Recovery: 6-12 weeks
    Mechanism: limited holder base, limited engagement alternatives
    Risk: extended decay can trigger stop-loss mechanics

  National team tokens ($SNFT, $ARG, $BRA equivalents):
    Recovery: 3-6 months
    Mechanism: no league matches to sustain demand between tournaments
    This is the deepest decay pattern in the ecosystem
    Floor: may not return to tournament-peak for 18-24 months (next tournament)

COMPOUND DECAY RISK:
  Elimination in early round (group stage) produces deeper and faster decay
  than elimination in semi-final or final.
  Reason: early elimination removes months of anticipated demand;
  late elimination has already delivered most of the tournament demand.

AGENT RULE:
  Apply exit decay modifier when club/nation is eliminated:
    Within 48h of elimination: ×0.70–0.80 on demand signals
    Week 2-4: ×0.85–0.90
    Return to baseline: full CDI framework resumes
  Do not apply tournament occasion weights after elimination.
```

---

## Claim Period Behaviour

```
PATTERN:
  Fan Token Offering (FTO) claim periods show predictable participation
  patterns across wave structures.

GENERAL CLAIM PERIOD MECHANICS:
  Wave 1 (typically limited cap per user):
    · Fills faster than Wave 2 in high-demand partnerships
    · Scarcity mechanic drives early participation
    · Loyalty bonus (if applicable) incentivises early claim

  Wave 2 (open participation):
    · Lower urgency — no cap pressure
    · Attracts broader but less engaged holders
    · Participation rate typically 60-80% of Wave 1 rate

TYPICAL CLAIM COMPLETION RATE:
  60-80% of subscription window participants claim during the open period
  Unclaimed airdrop (post-claim-period): creates a small supply distribution
  event as tokens distribute to non-claiming participants

REGULATORY EXCLUSIONS:
  Some FTO events exclude jurisdictions due to regulatory compliance.
  This reduces effective holder base in excluded regions.
  UK exclusion: documented in $BELG FTO (June 2026)
  Any exclusion reduces total addressable participant pool — apply discount
  to demand forecasts for that holder segment.

REFERENCE CASE — $BELG FTO (June 2026):
  Royal Belgian Football Association fan token
  FTO date: 2026-06-03
  Format: two-wave FTO (first documented two-wave FTO in SportMind registry)
  Claim period: June 4-9
  UK users: excluded from loyalty bonus due to regulatory compliance
  Total supply: 20,000,000 (STANDARD tier)
  FTO tranche: 2,000,000 (10% of total supply)
  Loyalty bonus: 10% (non-UK participants)
  Contract: 0xfaB24366503Eb0fa8CB8FB7d1311159FD4283657

AGENT RULE:
  During an FTO claim period for a tracked token:
    · Expect elevated on-chain activity and wallet creation
    · Wave 1 completion rate signals community enthusiasm level
    · Unclaimed tokens at claim period end = minor supply distribution event
    · Regulatory exclusions narrow the effective demand pool
```

---

## Governance Participation Patterns

```
PATTERN:
  Governance participation is a leading indicator of community health —
  declining participation signals holder disengagement before price does.

PARTICIPATION TRIGGERS (highest to lowest):
  1. High-stakes decisions (naming rights, squad selection):
     Highest participation — holders perceive real influence
  2. Tournament and World Cup windows:
     Highest governance participation of the year
     Match anticipation drives platform engagement generally
  3. Commercial decisions (kit sponsor, kit design):
     Moderate participation — tangible but not emotionally critical
  4. Low-stakes votes (kit colour detail, mascot vote):
     Lowest participation — holders see no material impact

PARTICIPATION LIFECYCLE:
  Early token (Phase 1-2): high participation — novelty and identity
  Established token (Phase 3): stable participation, engaged core
  Mature token (Phase 4+): participation concentrates in engaged minority
  Declining community: participation drops across all vote types simultaneously

GOVERNANCE AS LEADING INDICATOR:
  Price and volume signals lag community health.
  Governance participation leads it.
  If poll participation drops 30%+ across consecutive votes:
    · Flag CHI reduction
    · Reassess demand trajectory
    · Check if other engagement signals (social, on-chain) confirm decline

QUORUM CONSIDERATIONS:
  Low quorum votes that still pass are not necessarily weak signals —
  the fan token governance model does not require full participation.
  Concentrated voting by engaged minority is normal for Phase 3+ tokens.

AGENT RULE:
  Track governance participation trends, not just outcomes.
  A vote that passes 95-5 with 10% participation is a different signal
  from a vote that passes 55-45 with 45% participation.
  Both pass. Only the second one tells you the community is engaged.
```

---

## Supply Event Response Patterns

```
AFTER A WIN BURN EVENT (FTP PATH_2):
  Supply effect:   tokens removed from circulation (deflationary)
  Holder response: short-term demand spike as market perceives scarcity
  Duration:        24-72 hours typically
  Magnitude:       proportional to occasion weight of the match
    UCL Final WIN: maximum demand × maximum burn = peak positive compound
    Standard domestic WIN: limited occasion weight × moderate burn = muted
  Key signal:      burn amount confirms pre-liquidation pool size was accurate

AFTER A LOSS MINT EVENT (FTP PATH_2):
  Supply effect:   tokens added to treasury (inflationary)
  Holder response: compounded negative sentiment
    Team lost (negative sporting signal) AND
    Supply increased (negative tokenomics signal) simultaneously
  Worst case pattern:
    High-demand fixture (×2.00) + LOSS at 90 mins = mint event
    Maximum negative compound: elevated demand anticipation + supply increase
    Example: UCL Final → Arsenal LOSS at 90 mins would have been this pattern
             (actual: DRAW at 90 mins → no supply event)

AFTER A DRAW (no FTP event):
  Supply effect:   unchanged (0 burned, 0 minted)
  Holder response: neutral from FTP supply perspective
  Demand effect:   determined entirely by match occasion weight and context
  Note:            In knockout matches, a DRAW at 90 minutes may still lead to
                   a winner via extra time/penalties — but FTP does not care.
                   Demand may spike if the club advances; supply does not change.

UCL FINAL 2026 REFERENCE CASE ($AFC):
  90-minute score: 1-1 (DRAW)
  FTP PATH_2 outcome: NO SUPPLY EVENT (0 burned, 0 minted)
  Arsenal won on penalties 4-3 in extra time: IRRELEVANT to FTP
  $AFC supply: unchanged after the Final
  Demand effect: neutral from supply perspective; club advanced (won on penalties)
  Source: fantokens.com/fan-token-play (official FTP rule specification)

CONSECUTIVE SUPPLY EVENT EFFECTS:
  Consecutive burns: cumulative scarcity narrative strengthens holder confidence
    April 2026 Arsenal: WIN burn (159,025) then LOSS mint (100,000) then DRAW
    Net: deflationary across the sequence despite the one mint event
  Consecutive mints: cumulative supply narrative erodes holder confidence
    Three consecutive LOSS results → three consecutive mints → sentiment deteriorates
```

---

## World Cup Holder Behaviour

```
PATTERN:
  Major international tournaments produce distinct holder behaviour cycles
  distinct from club token patterns. World Cup 2026 (June 11 – July 19,
  North America) is the reference tournament for this framework.

ACCUMULATION CYCLE:
  T-2 weeks before tournament: accumulation begins for known participant nations
  Group stage: elevated but not peak demand — outcome still uncertain
  Round of 16: first major demand surge for surviving nations
  Quarter-final: peak demand window — four remaining nations at maximum
  Semi-final/Final: demand concentrates in surviving nation tokens
  Exit at any stage: sharp decay within 48h (see Post-Tournament-Exit Decay)

PEAK DEMAND WINDOWS:
  Quarter-final through Final stage tokens carry ×1.60–×2.00 occasion weight
  Host nation tokens: additional ×1.10–×1.20 commercial premium
    Local commercial activation, domestic media amplification
  Surprise qualifier nations: elevated demand if unexpected — story premium

DECAY DEPTH BY STAGE OF EXIT:
  Group stage exit:     deepest decay (3-6 months recovery, expectations unmet)
  Round of 16 exit:     deep decay (2-4 months)
  Quarter-final exit:   moderate decay (6-8 weeks)
  Semi-final exit:      shallow decay (4-6 weeks, holders feel tournament value was delivered)
  Runner-up:            minimal decay — narrative of "nearly won" sustains engagement
  Winner:               minimal or positive — championship narrative sustains demand

FRAUD RISK WINDOW:
  The 4 weeks before and during any major tournament represent the highest
  risk period for unofficial tokens claiming national team affiliation.
  Pattern: unofficial tokens launch with national team branding just before
  major tournaments when search volume for national team tokens is at peak.
  Apply four-source verification to ALL new national team token signals
  in this window before any library addition or SMI recommendation.
  Reference: fan-token/fraud-risk-intelligence.md

AGENT RULE:
  Apply tournament demand modifiers only to officially verified tokens
  in the SportMind registry.
  An unverified national team token during a World Cup window is a
  fraud risk signal, not a demand opportunity.
```

---

## Agent Reasoning Guidance

Before reasoning about fan token demand for any fixture, apply this sequence:

```
STEP 1: IDENTIFY OCCASION WEIGHT
  What competition and stage is this?
  Apply occasion weight (×1.00 to ×2.00) before any other modifier.
  Reference: core/pre-match-signal-framework.md — STEP 1

STEP 2: CHECK FTP STATUS AND 90-MINUTE SCENARIOS
  Is FTP PATH_2 active for either club token?
  Map the three 90-minute outcome scenarios:
    Scenario A: Home win at 90 mins  → supply event A
    Scenario B: Away win at 90 mins  → supply event B
    Scenario C: Level at 90 mins     → DRAW → NO SUPPLY EVENT
  Note: Knockout match with extra time possible — 90-minute result still governs.
  Reference: fan-token/ftp-path2.md — 90-MINUTES PLAY RULE

STEP 3: ASSESS TOURNAMENT CONTEXT
  Is either club/nation in an active tournament?
    Group stage: elevated but uncertain
    Knockout: apply knockout demand premium
    Already eliminated: apply exit decay modifier — do not apply tournament weight
  Is this the World Cup window? Apply fraud risk verification threshold.

STEP 4: CHECK HOLDER BASE CHARACTERISTICS
  What is the supply tier?
    ULTRA_LOW supply tokens (< 5M): price impact per trade is larger
    STANDARD supply tokens (10-30M): standard demand framework applies
    LARGE supply tokens (> 30M): demand moves more slowly, deeper liquidity
  Check recent supply event history — consecutive burns vs consecutive mints
  affect holder sentiment trajectory before price confirms it.

STEP 5: INTEGRATE WITH SPORT DOMAIN SIGNAL
  Holder behaviour amplifies the sport domain signal — it does not replace it.
  A strong sport domain signal with high occasion weight and pre-match
  accumulation activity is the highest-confidence compound signal.
  A weak sport domain signal with holder accumulation activity deserves
  higher skepticism — emotional demand does not override poor sporting signal.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Fan holder behaviour intelligence: accumulation patterns, decay rates, governance signals, supply event responses |
| Reasoning | ACTIVE | Five-step agent reasoning guidance from occasion weight through sport domain integration |
| Context | ACTIVE | Context-dependent patterns — club tier, tournament stage, supply tier, governance phase all affect behaviour |
| Memory | ACTIVE | Historical pattern recognition: pre-match accumulation windows, post-exit decay timelines, governance trends |
| Judgment | ACTIVE | Judgment gates at each step — verified token vs unverified, genuine demand vs tournament noise |
| Attention | ACTIVE | Elevated attention during FTO claim periods, tournament knockout stages, and World Cup fraud risk window |
| Communication | ACTIVE | Demand signal outputs include holder behaviour context: accumulation signal, decay stage, governance health |
| Verification | ACTIVE | Four-source verification required for new national team tokens in World Cup window |
| Learning | ACTIVE | Behaviour patterns calibrated from FTP PATH_2 records, $BELG FTO data, and governance participation data |
| Integration | ACTIVE | Integrates with ftp-path2.md, fraud-risk-intelligence.md, fan-token-lifecycle, pre-match-signal-framework |
| Calibration | ACTIVE | Decay timelines and accumulation windows calibrated from Chiliz ecosystem operational data |
| Adaptation | ACTIVE | Behaviour framework adapts as new token types (national team, FTO formats) and mechanics emerge |
| Ethics | ACTIVE | Fraud risk section flags deceptive tokens during World Cup window — holder protection is an ethics function |
| Transparency | ACTIVE | Reference cases ($BELG FTO, UCL Final 2026) cited explicitly — behaviour patterns are traceable to real events |

---

## Compatibility

**Occasion weights:**       `core/pre-match-signal-framework.md` — STEP 1
**FTP mechanics:**          `fan-token/ftp-path2.md` — 90-MINUTES PLAY RULE
**Fraud risk:**             `fan-token/fraud-risk-intelligence.md`
**Lifecycle phases:**       `fan-token/fan-token-lifecycle/fan-token-lifecycle.md`
**$BELG registry:**         `fan-token/registry/complete-registry.md`
**Governance framework:**   `fan-token/governance-intelligence.md`
**World Cup intelligence:** `fan-token/world-cup-2026-intelligence/`

---

*SportMind v3.97.116 · MIT License · sportmind.dev*
*Holder behaviour is event-driven, emotionally linked, and predictable.*
*All 14 Mind dimensions mapped.*
