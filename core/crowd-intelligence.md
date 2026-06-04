---
name: crowd-intelligence
description: >
  Enduring crowd dynamics reasoning framework extending core/venue-intelligence.md.
  Covers statistically verified crowd effects on referee decisions, capacity and
  atmosphere modifiers, crowd composition signals, and fan token holder crowd
  engagement signals. Load alongside venue-intelligence.md.
---

# Crowd Intelligence

**Crowd dynamics as a signal modifier — extending venue-intelligence.md.**
Do not re-read venue-intelligence.md — this file adds the crowd-specific reasoning layer.

> Related: `core/venue-intelligence.md` (base venue modifiers, sell-out ×1.05).
> Related: `core/referee-intelligence.md` (home/away bias in officiating).
> This file covers crowd composition, capacity dynamics, and specific crowd signals.

---

## Crowd noise and referee decisions

```
STATISTICALLY VERIFIED CROWD EFFECTS ON OFFICIATING:

  WHY THIS BELONGS IN THE LIBRARY:
    The relationship between crowd noise and referee decisions is one of the
    most statistically replicated findings in sports science. It is not
    contested — it is enduring structural fact.

  PENALTY AWARD RATE — HOME ADVANTAGE:
    Home teams receive approximately 15% more penalties than away teams
    across large samples (10,000+ match databases).
    This is partly explained by playing style, partly by crowd pressure.
    The crowd pressure component: approximately 40% of the differential.
    
    Signal implication: home team's goal threat via penalties is structurally
    elevated beyond technical skill alone.
    Apply: this is already partially captured in the home advantage baseline
      modifier from venue-intelligence.md. Do not double-count.
      Apply only when a referee has a confirmed additional home penalty bias
      beyond the average — see referee-intelligence.md penalty modifier.

  YELLOW CARD DISTRIBUTION — AWAY TEAM BIAS:
    Away teams receive approximately 12% more yellow cards than equivalent
    behaviour by home teams would receive.
    Crowd noise amplifies referee perception of foul severity for away players.
    
    Signal implication:
      Away teams with aggressive pressing or physical style face elevated
      booking risk — apply: away_booking_risk_modifier = ×1.05 for
      confirmed physical away teams in hostile atmospheres
      
  VAR PARTIAL MITIGATION:
    VAR reduces crowd effect on goal and penalty decisions significantly.
    VAR does NOT reduce crowd effect on non-reviewable decisions:
      Yellow cards: not VAR reviewable in most competitions
      Foul calls: not VAR reviewable
      Free kick placement: not VAR reviewable
    Result: crowd noise retains full effect on moment-to-moment foul decisions
    even with VAR present.
    Apply: retain crowd pressure modifier for non-VAR decisions;
      reduce only for decisions that VAR covers (goals, penalties, red cards)
    
  HIGH-NOISE VENUES — AMPLIFIED EFFECT:
    Venues with enclosed roof structures, lower capacity but high density,
    and traditionally vocal crowds amplify the crowd noise effect.
    Apply: high_noise_venue_modifier = ×1.05 amplifier on crowd pressure signals
    Confirm via: historical attendance and ground characteristics data.
    Examples: Celtic Park, Anfield, Türk Telekom Stadium, Galatasaray context.
```

---

## Capacity and atmosphere modifiers

```
CAPACITY UTILISATION — ATMOSPHERE SIGNAL:

  This section EXTENDS venue-intelligence.md which covers the sell-out modifier.
  Do not duplicate the sell-out ×1.05 modifier — reference it.

  CAPACITY UTILISATION TABLE (extending venue-intelligence.md):

  Utilisation              Atmosphere modifier     Notes
  ──────────────────────────────────────────────────────────────────────
  Below 60% capacity       ×0.88                  Sparse; minimal atmosphere
  60-80% capacity          ×0.95                  Reduced vs baseline
  80-95% capacity          ×1.00 (standard)       Normal home advantage applies
  95-100% (near sell-out)  ×1.03                  Elevated atmosphere
  100% confirmed sell-out  ×1.05                  From venue-intelligence.md

  HOW TO COMBINE WITH HOME ADVANTAGE:
    Apply: capacity modifier × home advantage baseline = combined home signal
    Example: 70% capacity × standard home +0.10 = +0.095 effective home signal
    
  EMPTY OR CLOSED-DOORS STADIUM:
    When matches are played without fans (no public attendance):
      Remove home advantage baseline entirely.
      Apply: neutral_venue_modifier from venue-intelligence.md instead.
      Historical reference: COVID-era research confirmed home advantage
        dropped to near-zero without fans — the crowd effect is real
        and quantifiable. This is enduring reasoning, not current context.
```

---

## Crowd composition signals

```
AWAY END ALLOCATION — AWAY SUPPORT MODIFIER:

  AWAY ALLOCATION CONFIRMED SOLD OUT:
    Away team receives measurable support boost when away allocation is full.
    Apply: away_support_modifier = ×1.02 to away team adjusted score
    Mechanism: vocal away support creates a micro-home-advantage for the
      away team within the larger hostile environment
    Confirm via: official club ticket information (away allocation)
    
  AWAY ALLOCATION EMPTY / VERY LOW:
    No modifier — absence of away fans is already the default assumption
    in a standard hostile away environment.

NEUTRAL VENUE CROWD COMPOSITION (extending venue-intelligence.md):

  CROWD SPLIT ASSESSMENT:
    ≥60% crowd supporting Team A:  crowd_proxy_modifier = ×1.03 for Team A
    ≥75% crowd supporting Team A:  crowd_proxy_modifier = ×1.05 for Team A
    50/50 split:                   no modifier — true neutral
    
    Assess split via: geographic proximity, ticket allocation, national fan base data
    See: venue-intelligence.md neutral venue section for full proxy framework.
    
  MIXED-NATIONALITY CROWD AT INTERNATIONAL NEUTRAL VENUES:
    Large international tournaments at neutral venues often attract mixed crowds.
    Assessment method:
      1. Identify each team's global fan base size
      2. Identify the venue's geographic proximity to each fan base
      3. Estimate ticket allocation where available
    Apply the relevant ×1.03 or ×1.05 modifier based on resulting crowd split estimate.

FIRST MATCH AT A NEW STADIUM:

  ATMOSPHERE UNCERTAINTY:
    Crowd unfamiliar with acoustic properties; new routines not yet established;
    emotional connection to new ground not yet built.
    Apply: new_stadium_atmosphere_modifier = ×0.98 for first match
    Duration: first home match only — remove immediately after
    Note: this is a small modifier; the novelty factor partially offsets it
```

---

## Fan token holder crowd engagement signals

```
FAN TOKEN HOLDER EVENTS — COMMUNITY HEALTH SIGNALS:

  STADIUM-BASED HOLDER EVENTS:
    Fan token holder events at the stadium (pitch side access, exclusive
    meet and greet, pre-match holder zones) create positive community
    health signals.
    Apply: holder_event_demand_modifier = ×1.03 for 48-72h around the event
    Mechanism: reinforces holder identity; generates social media content;
      attracts attention from non-holders who see the exclusivity
      
  HOW TO IDENTIFY:
    Official club or Socios announcement of holder-specific stadium events.
    Apply only when confirmed via official channels — not rumoured events.

STADIUM NAMING RIGHTS — FAN TOKEN CONNECTION:

  NAMING RIGHTS CONNECTED TO FAN TOKEN ECOSYSTEM:
    When the stadium naming rights deal is connected to a crypto, fan token,
    or blockchain brand — it creates a positive commercial signal for
    the associated token.
    Apply: naming_rights_ecosystem_modifier = ×1.05 sustained demand modifier
    Mechanism: brand association; commercial partnership credibility;
      signals mainstream commercial integration of fan tokens
    Duration: sustained for the duration of the naming rights contract
    
  HOW TO IDENTIFY:
    Official stadium naming announcement from club or partner.
    Confirm the naming partner has a direct fan token ecosystem connection.

NEW STADIUM OPENING:

  STADIUM OPENS (club moves to a new or significantly upgraded ground):
    Phase 1 — opening event: demand spike ×1.20 (48-72h around opening)
    Phase 2 — first season: sustained ×1.08 demand modifier
    Mechanism: increased match day revenue; elevated media attention;
      new visual identity associated with the club; new holder narrative
      
  QUALIFICATION TO APPLY:
    Applies to: brand-new stadium opening, or major capacity expansion
      where the fan experience is fundamentally upgraded
    Does NOT apply to: routine stadium renovations, minor capacity additions
    
  INTERACTION WITH FAN TOKEN PATH_2 ($AFC):
    If $AFC Arsenal were to open a new stadium, the increased attendances
    would not directly affect PATH_2 mechanics (supply events are based on
    match results, not attendance). However: elevated demand for $AFC from
    the stadium narrative would amplify the demand dimension of PATH_2 events.
    Note this interaction rather than applying a direct PATH_2 modifier.
```

---

## Compatibility

**Base venue modifiers:**   `core/venue-intelligence.md` (sell-out ×1.05, home advantage by sport)
**Referee bias:**           `core/referee-intelligence.md` (penalty and card bias)
**Psychological impact:**   `core/psychological-intelligence.md` (derby amplification)
**Social sentiment:**       `core/social-sentiment-intelligence.md`
**Broadcast amplification:**`core/broadcast-media-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Crowd dynamics, home advantage signals, and atmosphere impact intelligence |
| Reasoning | ACTIVE | Crowd reasoning chain from attendance and atmosphere to performance modifier |
| Context | ACTIVE | Context: neutral venue, crowd capacity, rivalry status, home vs away |
| Memory | ACTIVE | Historical crowd-performance correlation data by sport and venue type |
| Judgment | ACTIVE | Judgment on crowd signal materiality — not all home advantages are equal |
| Attention | ACTIVE | Elevated attention for unusual crowd conditions — reduced attendance, neutral venue |
| Communication | ACTIVE | Crowd signal output with home advantage modifier and venue context |
| Verification | ACTIVE | Crowd restrictions or bans require official confirmation before modifier adjustment |
| Learning | ACTIVE | Home advantage calibration from historical outcome data across sports |
| Integration | ACTIVE | Integrates with venue intelligence, neutral venue modifier, and match conditions |
| Calibration | ACTIVE | Home advantage modifiers calibrated against historical home vs away outcome data |
| Adaptation | ACTIVE | Crowd intelligence adapts as behind-closed-doors policies change |
| Ethics | NOT APPLICABLE | Crowd signals are factual environmental data — no ethical dimension |
| Transparency | ACTIVE | Home advantage modifier and crowd conditions explicit in output |


---

*SportMind v3.97.37 · MIT License · sportmind.dev*
*Crowd effect on referee decisions is verified scientific consensus — not speculation*
