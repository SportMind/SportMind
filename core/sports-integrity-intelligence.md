---
name: sports-integrity-intelligence
description: >
  Enduring reasoning framework for match fixing, corruption risk, and sports
  integrity signals as pre-match confidence modifiers. Three-tier competition
  integrity classification, match fixing red flags, dead rubber framework, fan
  token integrity signals, and triple integrity flag trigger. Frameworks only
  — not specific match accusations.
---

# Sports Integrity Intelligence

**Enduring red flag reasoning framework for competition integrity signals.**
Not specific match accusations — structural reasoning about documented risk patterns.

> IMPORTANT FRAMING:
> SportMind does not accuse specific matches or individuals of fixing.
> These frameworks provide enduring reasoning about how to weight signals from
> competitions with documented integrity risk patterns.
> Official integrity investigation = immediate HOLD. See below.

---

## Competition integrity tier classification

```
COMPETITION INTEGRITY TIERS — SIGNAL CONFIDENCE WEIGHTS:

  TIER 1 — HIGHEST INTEGRITY (full modifier weight):
    Competitions: UEFA Champions League, FIFA World Cup, Copa America,
      AFCON, Asian Cup, Premier League, Bundesliga, La Liga, Serie A, Ligue 1,
      major national team competitions from Tier 1 footballing nations,
      top domestic leagues across all major established sports
    Signal weight: ×1.00 — full modifier weight; no integrity discount
    Mechanism: robust officiating monitoring, multi-jurisdictional oversight,
      high commercial stakes that incentivise all parties to preserve integrity
      
  TIER 2 — STANDARD INTEGRITY (modest discount):
    Competitions: second tier domestic leagues in major footballing nations,
      established competitions across all major sports with standard monitoring
    Signal weight: ×0.97 — minimal integrity discount
    Note: this is a background discount, not a material signal modifier
    
  TIER 3 — ELEVATED INTEGRITY RISK (significant discount):
    Competitions: competitions in jurisdictions with documented match fixing history,
      lower tier competitions with minimal integrity monitoring,
      competitions without transparent officiating oversight
    Signal weight: ×0.88 — significant integrity confidence discount
    Flag as: INTEGRITY_RISK_ELEVATED in signal output
    Note: signal still produced at ×0.88 weight; not a full HOLD

HOW TO CLASSIFY:
  Primary sources: UEFA/FIFA Integrity Unit, Sportradar Integrity Services,
    INTERPOL Match Fixing Task Force annual reports
  Default: new competition without known integrity track record → Tier 2
  Upgrade to Tier 1: sustained clean record + robust monitoring confirmed
  Downgrade to Tier 3: official investigation history confirmed by primary sources
```

---

## Match fixing red flags

```
ENDURING PATTERNS INDICATING ELEVATED INTEGRITY RISK:

  These are risk signal patterns — not accusations against specific matches or individuals.
  Multiple flags compound. Single flags warrant monitoring, not HOLD.

  FLAG 1 — SUSPICIOUS ODDS MOVEMENT:
    Very large movement on multiple exchanges simultaneously without corresponding news.
    See: core/odds-market-intelligence.md for full odds signal framework.
    
  FLAG 2 — JURISDICTIONAL CONCENTRATION:
    Very large odds movement concentrated in jurisdictions with known fixing risk,
    not reflected on global major markets.
    
  FLAG 3 — COMPETITIVE MOTIVATION ABSENT:
    Team has mathematically eliminated all competitive motivation —
    no relegation risk, no title race, no European qualification impact.
    Combined with Tier 3 competition: significant compound risk signal.
    
  FLAG INTERACTION TABLE:
    
    Flags present               Competition tier    Signal response
    ───────────────────────────────────────────────────────────────────────────
    Flag 3 only                 Tier 1              ×0.92 confidence (dead rubber)
    Flag 3 only                 Tier 2/3            ×0.85 confidence
    Flag 1 + Flag 3             Tier 1              ×0.85 confidence; escalate
    Flag 1 + Flag 2             Tier 2/3            HOLD — INTEGRITY_RISK_HIGH
    Flag 1 + Flag 2 + Flag 3    Any tier            INTEGRITY_TRIPLE_FLAG → HOLD
    Official investigation       Any tier            HOLD immediately — all signals
```

---

## Dead rubber framework

```
DEAD RUBBER — COMPETITIVE MOTIVATION ABSENT:

  DEFINITION:
    A match in which the result has no bearing on the final standing,
    qualification, or relegation position of either team.
    
  DEAD RUBBER + TIER 1 COMPETITION:
    Apply: dead_rubber_motivation_modifier = ×0.93 (from seasonal-intelligence.md)
    Integrity signal: none — Tier 1 competition retains full integrity monitoring
    Net: standard dead rubber discount only
    
  DEAD RUBBER + TIER 3 COMPETITION:
    Apply: HOLD signal regardless of adjusted score
    Rationale: too many confounding factors for reliable signal production
    The combination of zero competitive motivation + elevated integrity risk context
    makes directional signals unreliable regardless of pre-match modifier stack.
    
  AGENT RULE:
    For any dead rubber in Tier 3 competition: output HOLD + INTEGRITY_RISK flag.
    Do not attempt to produce a directional signal.
```

---

## Fan token integrity signal

```
FAN TOKEN INTEGRITY INTERACTION:

  FTP PATH_2 ($AFC) IN INTEGRITY-RISK CONTEXTS:
    $AFC primarily plays in Tier 1 competitions (UCL, Premier League, domestic cups).
    In the normal course, no integrity modifier applies to $AFC supply events.
    
    IF $AFC WERE TO PLAY IN A TIER 3 CONTEXT (friendly tournament, etc.):
      FTP PATH_2 supply events still fire on official results.
      However: apply ×0.85 confidence weight to directional signals.
      The burn/mint mechanism fires regardless — but directional confidence is reduced.
      
  DEMAND-ONLY TOKENS IN TIER 3 COMPETITIONS:
    Apply: ×0.85 confidence weight to all directional demand signals
    Flag: INTEGRITY_RISK_ELEVATED in signal output
    The demand signal still exists — but the confidence in direction is reduced.
    
  INTEGRITY INVESTIGATION CONFIRMED (official source):
    Apply: HOLD to all signals for the affected match
    Remove PATH_2 supply event calculations for that specific match
    Do not produce any directional output until investigation is resolved
    This is the highest-priority override — above all other modifiers
```

---

## Integrity investigation protocol

```
WHEN AN OFFICIAL INTEGRITY INVESTIGATION IS CONFIRMED:

  PRIMARY SOURCES (Tier 1 only):
    UEFA Integrity Unit — official press statements
    FIFA Integrity — official communications
    Sportradar Integrity Services — official alerts (not public; for platforms)
    INTERPOL Match Fixing Task Force — official communications
    National sports authority official communications
    
  CONFIRMATION STANDARD:
    Official statement from one of the above sources is required.
    Media reports, social media, and community sources alone are NOT sufficient
    to trigger the investigation HOLD.
    
  ON CONFIRMATION:
    Apply: HOLD to all signals for affected matches
    Remove: all directional modifier calculations
    Output: INTEGRITY_INVESTIGATION_ACTIVE flag
    Duration: until official resolution or clearance from the primary source

CONNECTION TO ODDS INTELLIGENCE:
  Triple integrity risk signal = INTEGRITY_TRIPLE_FLAG:
    Suspicious odds movement (from odds-market-intelligence.md)
    + Tier 3 competition
    + Dead rubber (no competitive motivation)
    → HOLD signal regardless of any other modifiers
    → INTEGRITY_TRIPLE_FLAG in output
    → Cannot be overridden by any other modifier in the stack
```

---

## Compatibility

**Odds signals:**            `core/odds-market-intelligence.md`
**Dead rubber modifiers:**   `core/seasonal-intelligence.md`
**Confidence framework:**    `core/signal-confidence-framework.md`
**PATH_2 mechanics:**        `fan-token/ftp-path2.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Sports integrity signals: match-fixing patterns, suspicious betting movements, integrity alerts |
| Reasoning | ACTIVE | Integrity reasoning chain from suspicious signal to elevated caution modifier |
| Context | ACTIVE | Integrity context: competition vulnerability, odds movement pattern, reporting source |
| Memory | ACTIVE | Historical integrity incident patterns by competition and region |
| Judgment | ACTIVE | Judgment on integrity signal threshold — false positive risk is high in this domain |
| Attention | ACTIVE | Maximum attention for official integrity alerts from governing bodies |
| Communication | ACTIVE | Integrity signal output with caution flag and confidence — never definitive accusation |
| Verification | ACTIVE | Integrity signals require official governing body alerts — all other sources are Tier 4 |
| Learning | EMERGING | Integrity pattern learning is constrained by limited confirmed case data |
| Integration | ACTIVE | Integrates with odds market intelligence and competition intelligence |
| Calibration | EMERGING | Integrity signal calibration is severely limited — most suspected cases go unconfirmed |
| Adaptation | ACTIVE | Integrity intelligence adapts as governing body detection systems evolve |
| Ethics | ACTIVE | Highest ethics sensitivity: integrity allegations require official confirmation before flagging |
| Transparency | ACTIVE | Source tier and caution flag status always explicit — never present as confirmed corruption |


---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Official investigation confirmed = HOLD immediately. This overrides all other modifiers.*
