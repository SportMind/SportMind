---
name: anti-doping-intelligence
description: >
  Enduring reasoning framework for anti-doping signals as they affect athlete
  availability, match outcomes, and fan token demand. Covers suspension tier
  classification, whereabouts failures as leading indicators, CAS appeal timeline
  reasoning, return from suspension modifiers, and fan token demand impact including
  community sentiment and club-level integrity signals. Frameworks only — no named
  athletes or specific case records.
---

# Anti-Doping Intelligence

**How to reason about anti-doping signals for availability, outcomes, and fan token demand.**

> IMPORTANT FRAMING:
> SportMind does not speculate about specific athletes or make doping accusations.
> This framework applies to confirmed official signals from WADA, USADA, or national
> anti-doping authorities that are publicly announced through Tier 1 sources.
> No modifier is applied from unconfirmed or media-only reports.

---

## Suspension tier classification

```
TIER FRAMEWORK — suspension length as availability and demand signal:

  TIER 1 — SHORT SUSPENSION (under 6 months):
    Likely whereabouts failure or minor procedural violation.
    Return timeline predictable within contract period.
    Athlete modifier on return: ×0.94 for first three matches
    Fan token demand impact: minimal if club squad depth is sufficient

  TIER 2 — STANDARD SUSPENSION (1-2 years):
    Confirmed prohibited substance.
    Significant availability gap — return within contract period likely but not certain.
    Athlete modifier on return: ×0.88 for first five matches
    Fan token demand impact: −8 to −15% sustained for duration of suspension
      if athlete is a key squad member

  TIER 3 — LONG SUSPENSION (2-4 years):
    Serious violation or confirmed aggravating circumstances.
    Career disruption significant — return to previous performance level uncertain.
    Athlete modifier on return: ×0.82 for first ten matches
    Fan token demand impact: −15 to −25% sustained
      Treat as season-ending absence for modelling purposes

  TIER 4 — LIFETIME BAN:
    Career ending.
    Treat identically to retirement for all SportMind signal purposes.
    Fan token demand impact: same as marquee player permanent departure
```

---

## Whereabouts failures as leading indicators

```
Whereabouts failures are publicly recorded and precede positive tests.
Three failures within 12 months = same consequence as a positive test.

  ONE CONFIRMED FAILURE:
    FLAG only — no modifier applied. Monitor for subsequent failures.

  TWO CONFIRMED FAILURES:
    LOW RISK signal.
    Apply: ×0.97 to athlete availability confidence.
    Not a suspension but elevated risk profile.

  THREE CONFIRMED FAILURES:
    EQUIVALENT TO POSITIVE TEST.
    Apply Tier 1 suspension framework immediately —
    even before official suspension is confirmed.
```

---

## Appeal timeline reasoning

```
Anti-doping suspensions are frequently appealed to CAS (Court of Arbitration for Sport).
Appeals create availability uncertainty that must be reasoned about explicitly.

  APPEAL FILED — OUTCOME PENDING:
    Apply: ×0.50 weight to suspension modifier
    Flag as: AVAILABILITY_UNCERTAIN_APPEAL
    Do not treat athlete as available or unavailable — uncertainty in both directions.

  APPEAL SUCCESSFUL — SUSPENSION REDUCED:
    Recalculate return timeline.
    Apply reduced tier modifier based on new suspension length.

  APPEAL UNSUCCESSFUL — UPHELD:
    Apply full tier modifier. Reset return timeline calculation.

  PROVISIONAL SUSPENSION (before hearing):
    Athlete unavailable immediately.
    Apply: Tier 2 modifier as default until hearing outcome confirmed.
```

---

## Return from suspension

```
Return from suspension is distinct from return from injury.
The athlete has been training throughout — unlike injured players.

  PHYSICAL READINESS:
    Physical conditioning typically maintained during suspension.
    Apply lower return modifier than equivalent injury duration.

  PSYCHOLOGICAL READINESS:
    Public scrutiny, squad reintegration, and competitive match sharpness all require time.
    Matches 1-3 on return:  ×0.92
    Matches 4-8 on return:  ×0.96
    Match 9+:               full performance modifier restored

  TEAM REINTEGRATION SIGNAL:
    Manager public support of returning athlete: ×1.02 to return modifier
    Manager ambiguous about returning athlete:   ×0.90 to return modifier
```

---

## Fan token demand impact of doping signals

```
COMMUNITY SENTIMENT DIMENSION:
  Doping violations create community trust damage beyond pure availability.
  Distinct from injury — holders may sell on principle, not just performance grounds.

  KEY PLAYER CONFIRMED VIOLATION:
    Apply: demand_suppressor = ×0.85 immediately
    Duration: until return to play confirmed AND community sentiment stabilises
    Typical stabilisation window: 8-16 weeks

  CLUB-LEVEL DOPING CULTURE SIGNAL:
    Multiple confirmed violations from same club within 24 months:
    Apply: club_integrity_modifier = ×0.88 sustained on all demand signals for that club
    This is an enduring institutional signal — not a temporary modifier.

  GOVERNING BODY INVESTIGATION (club or competition):
    Apply: ×0.90 to all tokens associated with that competition
    Duration: until investigation is formally resolved by Tier 1 source

  NATIONAL TEAM DOPING SIGNALS:
    Multiple confirmed violations in an Olympic or World Cup cycle:
    Apply: ×0.88 to national team token demand for duration of that cycle
```

---

## Competition integrity interaction

```
Anti-doping signals interact with the sports integrity framework.

  TIER 3 COMPETITION + ACTIVE DOPING INVESTIGATION OF PARTICIPATING CLUB:
    Apply: HOLD to all directional signals
    Integrity uncertainty too high for reliable signal production.

  AGENT RULE:
    Do not compound doping modifiers with injury modifiers if the athlete is
    suspended and unavailable — only the absence modifier applies.
    Doping-specific demand modifiers (community sentiment) apply separately
    from the standard athlete availability modifier.
```

---

## Compatibility

**Integrity framework:**   `core/sports-integrity-intelligence.md`
**Athlete intelligence:**  `athlete/[club].md`
**Confidence framework:**  `core/signal-confidence-framework.md`
**Press conference:**      `core/press-conference-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Anti-doping regulatory landscape, test schedules, and violation patterns |
| Reasoning | ACTIVE | Reasoning chain from anti-doping event to athlete availability and performance modifier |
| Context | ACTIVE | Competition-specific anti-doping context — testing frequency varies by event tier |
| Memory | ACTIVE | Violation history and suspension records for athlete profile |
| Judgment | ACTIVE | Judgment on materiality — not all violations are equal in impact |
| Attention | ACTIVE | Elevated attention when anti-doping news breaks near competition |
| Communication | ACTIVE | Signal communication: provisional suspension vs confirmed ban distinction |
| Verification | ACTIVE | Source verification — only WADA/national agency announcements are Tier 1 |
| Learning | EMERGING | Pattern learning from historical violation-performance correlation |
| Integration | ACTIVE | Integrates with athlete availability, APS modifier, and competition intelligence |
| Calibration | EMERGING | Limited calibration data for anti-doping impact on fan token signals |
| Adaptation | ACTIVE | Modifier adapts as anti-doping case progresses through stages |
| Ethics | ACTIVE | Anti-doping violations are factual signals — no editorialising |
| Transparency | ACTIVE | Distinction between alleged, provisional, and confirmed violations must be visible |


---

*SportMind v3.97.58 · MIT License · sportmind.dev*
*Applies to confirmed official anti-doping authority announcements only — not media reports.*
