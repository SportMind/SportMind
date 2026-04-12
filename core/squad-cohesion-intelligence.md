---
name: squad-cohesion-intelligence
description: >
  Intelligence framework for squad cohesion — the collective dynamic of a
  team beyond individual athlete performance. Covers dressing room climate,
  manager-player alignment, leadership structure, internal conflict signals,
  and cohesion trajectory. Produces a Squad Cohesion Index (SCI: 0–100)
  and a cohesion_modifier (0.88–1.10). Fan token commercial connection:
  high cohesion correlates with sustained win rates, LTUI stability, and
  FTP PATH_2 supply reduction pace; low cohesion is a leading indicator of
  performance decline before statistical evidence appears. Load when:
  transfer window activity has disrupted squad balance, a new manager has
  arrived, a public dispute or reported unrest is active, or a major star
  departure has created a void. Cross-sport: most valuable in football,
  NBA, rugby, cricket (Test format). Less applicable to individual sports.
---

# Squad Cohesion Intelligence — SportMind

**The team is not the sum of its individuals. How they combine — and
whether they want to — materially changes what the signal means.**

The LQI (`core/lineup-quality-index.md`) measures player quality aggregated.
This skill measures something different: the quality of the relationships
between those players, and between the players and their manager. Two squads
with identical LQI scores can have radically different outcomes if one is
a cohesive unit and the other is a fractured group of individuals.

---

## Why cohesion is a signal, not noise

```
THREE DOCUMENTED COHESION EFFECTS:

Effect 1 — Pre-performance degradation:
  Cohesion breakdown precedes performance decline by 2–6 weeks.
  Public unrest (journalism, player social media) emerges weeks before
  it appears in results. SportMind agents with cohesion intelligence
  can detect the signal before the market prices it.
  
  Evidence: Multiple documented cases where dressing room reporting
  preceded a run of poor results by 3–5 weeks (Leicester 2022-23,
  Juventus 2022-23, multiple examples in NBA franchise analysis).

Effect 2 — Resilience under adversity:
  High-cohesion squads recover from setbacks (goal conceded, early red card,
  injury to key player) significantly better than low-cohesion squads.
  The comeback rate is partially a cohesion signal.
  
  Implication: In high-stakes matches, cohesion modifies the TAIL RISK —
  it does not change the most likely outcome but it changes how bad the
  bad scenario is likely to be.

Effect 3 — Fan token commercial stability:
  High-cohesion squads produce more consistent utility events — celebrations,
  community content, governance participation — that drive LTUI.
  Low-cohesion squads produce less holder-relevant content and more
  distress-driven social volume, which the library classifies as negative
  rather than positive engagement signal.
```

---

## The Squad Cohesion Index (SCI)

```
SCI = (Manager_Alignment × 0.30)
    + (Leadership_Quality × 0.25)
    + (Recent_Disruption_Inverse × 0.25)
    + (Cultural_Continuity × 0.20)

Scale: 0–100. Modifier applied as per table below.

MANAGER_ALIGNMENT (0–100):
  How aligned are players with the manager's system and authority?
  Signals sourced from: press conferences, journalism, social media tone
  
  90–100: High alignment — players publicly supportive, no dissent signals
  70–89:  Good alignment — standard relationship, minor issues manageable
  50–69:  Moderate — some tension documented; one or two public comments
  30–49:  Low — active speculation, reported cliques or resentment
  10–29:  Very low — open conflict, reported player mutiny signals
  0–9:    Breakdown — confirmed public split (player to media, player walkout)

LEADERSHIP_QUALITY (0–100):
  Strength of captain and senior player leadership within the squad.
  
  85–100: Strong — captain widely respected, senior players unite squad
  65–84:  Good — leadership present but not exceptional
  45–64:  Moderate — captain adequate but not commanding
  25–44:  Weak — leadership vacuum; no clear voice in dressing room
  0–24:   Absent — captain disputed, or captain is part of the conflict

RECENT_DISRUPTION_INVERSE (0–100 — higher = less disruption):
  How much disruption has the squad experienced in the last 8 weeks?
  Disruptions: mass signing window activity, star departure, sacking, major injury,
  public controversy, disciplinary event (DSM Tier 3+)
  
  0 disruptions in 8 weeks:      100
  1 moderate disruption:          75
  2 disruptions or 1 severe:      55
  3+ disruptions:                 30
  Major destabilising event:      10

CULTURAL_CONTINUITY (0–100):
  How stable has the squad's core identity been?
  
  90–100: Stable — largely same core group for 2+ seasons
  70–89:  Good continuity — some turnover but core intact
  50–69:  Some erosion — 3–5 significant departures/arrivals in 12 months
  30–49:  High turnover — manager or ownership change + mass squad change
  0–29:   Identity disruption — full rebuild underway

SCI → MODIFIER CONVERSION:
  SCI 80–100: cohesion_modifier × 1.10  HIGH — squad functions as a unit
  SCI 65–79:  cohesion_modifier × 1.04  GOOD — above baseline
  SCI 50–64:  cohesion_modifier × 1.00  NEUTRAL — no adjustment
  SCI 35–49:  cohesion_modifier × 0.96  MILD CONCERN — monitor
  SCI 20–34:  cohesion_modifier × 0.92  SIGNIFICANT CONCERN
  SCI 0–19:   cohesion_modifier × 0.88  BREAKDOWN — active disruption
```

---

## Cohesion signal detection — verifiable sources

```
TIER 1 SIGNALS (act on immediately):
  → Manager publicly criticises specific player by name
  → Player publicly undermines manager or club policy
  → Confirmed training ground altercation (Tier 1/2 journalism source)
  → Player requests transfer in-season (confirmed by agent or club)
  → Captain stripped of armband mid-season
  → Senior players reported to have met with ownership without manager

TIER 2 SIGNALS (significant weight with corroboration):
  → "Cliques" or "faction" language from Tier 2 journalist
  → Player agent makes public comments about environment
  → Multiple players simultaneously liking social posts critical of club
  → Manager uses noticeably defensive or vague language in press conferences
  → Player dropped for disciplinary reasons without public explanation
  → Player visibly does not celebrate team goals or milestone moments

TIER 3 SIGNALS (background monitoring — alone insufficient):
  → Transfer request rumours (not yet confirmed)
  → Player seen arriving separately or leaving training early
  → Drop in social engagement from player regarding club content
  → Club content team stops featuring specific player regularly
  → Manager rotation patterns inconsistent with form (possible internal reason)

NOISE (do not act on):
  → Anonymous "sources" without named journalist attribution
  → Fan speculation on social media not backed by journalism
  → Player missing from a single training session
  → Single muted celebration (injury, personal circumstance more likely)

AGENT RULE:
  The absence of cohesion signals is itself a signal.
  If a club has had major disruption (star departure, manager sacking,
  mass transfer window activity) and there are zero negative cohesion signals
  after 4 weeks, that is a positive cohesion data point — the squad has
  absorbed the disruption. Upgrade SCI accordingly.
```

---

## Cohesion scenarios and their modifiers

```
SCENARIO 1 — New manager integration (weeks 1–8)
  Phase A (matches 1–3): New manager bounce — high motivation, maximum effort
    Apply from core/manager-intelligence.md: +8–15% uplift
    Cohesion signal: hold neutral — new manager has not yet been tested
  Phase B (matches 4–8): System installation — tactical disruption begins
    Apply cohesion_modifier × 0.96 if system_fit (MgSI) < 0.70
    Players not suited to new system = first cohesion friction window
  Phase C (week 9+): Normalisation or fracture
    Monitor for Tier 2 signals; update SCI based on observed evidence

SCENARIO 2 — Post-transfer-window disruption
  Multiple arrivals in one window: SCI disruption penalty –15 points
  Each ATM-level departure (see core/star-departure-intelligence.md): –10 points
  Star arrival who immediately disrupts team hierarchy: –12 points
  Recovery timeline: 6–10 weeks if no further disruptions

SCENARIO 3 — Disciplinary event (active DSM case)
  DSM Tier 3+ event involving a senior player (core/athlete-disciplinary-intelligence.md):
    First 2 weeks: SCI –20 points (squad distracted, media attention, manager stress)
    If player suspended and team rallies: SCI can recover to –10 by week 4
    If player cleared/resolved: return to pre-event SCI within 2 weeks
    If case drags: sustained SCI penalty until resolution

SCENARIO 4 — Leadership vacuum (captain change)
  Captain removed without obvious external reason (injury, transfer):
    SCI –18 points immediately
    Recovery: depends on quality of replacement captain and narrative
    Interim captain of high LQI/ATM score: –8 net after 2 weeks
    No clear replacement: –18 sustained until new captain established

SCENARIO 5 — Extended bad run (5+ consecutive defeats)
  Bad results reduce cohesion even in previously cohesive squads.
  Baseline SCI deterioration: –3 points per consecutive defeat after 3
  Manager press conference tone is the leading indicator — monitor for
  "character" and "togetherness" language (signals positive cohesion
  being tested) vs short, clipped responses (signals internal concern).
```

---

## Fan token commercial connections

```
HIGH COHESION → FAN TOKEN IMPLICATIONS:

1. LTUI stability
   High-cohesion squads generate consistent utility events — players are
   engaged with the club's digital programme, governance participation is
   higher, commercial partnerships reflect a united brand image.
   Apply: LTUI trajectory positive flag when SCI ≥ 75 for 3+ months.

2. FTP PATH_2 supply trajectory
   High cohesion correlates with sustained win rates.
   Win rates drive supply reduction pace for PATH_2 tokens.
   Formula interaction:
     SCI 80+ → win_probability_baseline × 1.02 uplift (sustained cohesion premium)
     SCI below 40 → win_probability_baseline × 0.95 reduction (pre-decline signal)
   Source: core/star-departure-intelligence.md (departure causes both SCI drop
   and win probability reduction — same mechanism, connected signals)

3. Social engagement quality
   Cohesive squads produce organic, positive social content.
   Fractured squads produce distress-driven volume (negative for HAS).
   Rule: If SCI < 40 AND social volume is high, classify as DISTRESS signal
   rather than POSITIVE ENGAGEMENT signal.
   (Connects to core/star-departure-intelligence.md — social signal classification)

4. Sponsorship and commercial partner confidence
   Sponsors and partners monitor squad harmony. Public conflict = partnership
   termination risk. An active SCI < 30 scenario with media coverage raises
   fan-token/fan-token-lifecycle/ partnership termination risk flag.
```

---

## Cross-sport application

```
FOOTBALL:
  Most applicable sport. Transfer windows, manager pressure, and media coverage
  all create frequent cohesion signal updates.
  Primary signals: Press conferences, The Athletic, Sky Sports insider reporting
  Update frequency: After transfer windows + weekly during active unrest

NBA:
  Highly applicable. "Locker room chemistry" is widely covered in US media.
  Primary signal: The Athletic NBA, ESPN insider reporting, player social media
  Particular signals: star player exit demands, trade requests, coach friction
  Update frequency: Weekly during season

CRICKET (TEST):
  Applicable for long-format cricket where squad dynamics play out over 5 days.
  Less applicable for T20 (too short for cohesion to manifest).
  Primary signal: ESPNcricinfo team reports, dressing room atmosphere pieces
  Key scenario: Captain-coach alignment (Test cricket leadership is dual)

RUGBY (UNION/LEAGUE):
  Applicable. Forward-back divide, captain leadership, coach alignment all matter.
  Less visible cohesion signals than football — sport is more private.
  Primary signal: Post-match press conference, official club communication tone

MMA:
  Not applicable at fighter level (individual sport). Applicable at PROMOTION
  level: if promotion's relationship with its top fighters is fractured,
  card quality and draw-power signals are affected. Rare scenario.

INDIVIDUAL SPORTS (tennis, golf, darts, snooker):
  Not applicable directly. Player-coach relationship is the closest equivalent.
  Do not apply squad cohesion framework to individual sport signals.
  Exception: National team formats (Davis Cup, Ryder Cup) where individual
  players form a temporary team — cohesion framework applies for those events.
```

---

## Cohesion output schema

```json
{
  "cohesion_brief": {
    "club":        "Arsenal",
    "token":       "AFC",
    "assessed_at": "2026-04-12T00:00:00Z"
  },

  "sci_components": {
    "manager_alignment":        88,
    "leadership_quality":       82,
    "recent_disruption_inverse": 70,
    "cultural_continuity":      78
  },

  "sci_score":             80,
  "cohesion_modifier":     1.04,
  "cohesion_label":        "GOOD",

  "active_signals": [
    {
      "tier":   "Tier 2",
      "signal": "Havertz dropped for disciplinary reasons (The Athletic, 2026-03-28)",
      "impact": "Recent_Disruption -10 — partially priced",
      "status": "Resolved — player reintegrated"
    }
  ],

  "ftp_connection": {
    "win_probability_uplift":    0.02,
    "ltui_trajectory":           "STABLE",
    "social_signal_quality":     "POSITIVE — high volume is engagement, not distress"
  },

  "plain_english": "Arsenal's dressing room is in good shape. The manager has the squad behind him, the captain is a genuine leader, and there have been no significant disruptions in the last 8 weeks. Squad harmony is a mild positive for the signal tonight.",

  "sportmind_version": "3.56.0"
}
```

---

*SportMind v3.56 · MIT License · sportmind.dev*
*See also: core/manager-intelligence.md · core/athlete-motivation-intelligence.md*
*core/lineup-quality-index.md · core/star-departure-intelligence.md*
*core/athlete-disciplinary-intelligence.md · fan-token/fan-token-lifecycle/*
