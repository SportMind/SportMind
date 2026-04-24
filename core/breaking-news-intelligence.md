# Breaking News Intelligence

**The framework for how SportMind agents reason about breaking sports news —
the taxonomy of event types, their signal impact, and the correct agent
response protocol when news arrives before, during, or after analysis.**

Breaking news is the most operationally challenging input a sports intelligence
agent handles. A well-computed pre-match signal can be invalidated in seconds
by a manager sacking, a key player injury in warm-up, or a match postponement.
Agents that do not have a principled response framework either miss the signal
entirely or overreact to noise.

This document defines the framework. The temporal awareness model
(`core/temporal-awareness.md`) defines data freshness tiers. The real-time
integration patterns (`platform/realtime-integration-patterns.md`) define
how to connect live data. This document defines what to *do* with it when it arrives.

---

## Breaking news taxonomy

Eight categories of breaking sports news, ordered by signal impact:

```
CATEGORY 1 — MATCH PERSONNEL (Highest impact)
  Event types:
    Key player injury in warm-up / confirmed absent (T-0)
    Manager sacking within 72h of match
    Multiple player absences confirmed simultaneously
    Goalkeeper change from confirmed starter to backup
    Mass injury event (training ground accident, illness outbreak)

  Signal impact: CRITICAL
  Agent response: RELOAD (discard previous analysis, rebuild from scratch)
  Position size: 0% until reload complete
  Flag activated: injury_warning + lineup_unconfirmed + reload_required

CATEGORY 2 — MATCH STATUS (Highest impact)
  Event types:
    Match postponed (weather, stadium, political)
    Match abandoned mid-game
    Match moved to neutral venue
    Significant kick-off time change (> 2h)
    Behind-closed-doors confirmation (no crowd)

  Signal impact: CRITICAL
  Agent response: VOID (signal is no longer applicable)
  Position size: 0% — signal is moot
  Flag activated: match_status_void

CATEGORY 3 — DISCIPLINARY / REGULATORY
  Event types:
    Red card in first 15 minutes (numerical disadvantage for 75+ minutes)
    Points deduction confirmed during season
    Club placed into administration
    Transfer embargo imposed
    Player banned (doping, misconduct — confirmed)
    VAR/TMO review reversing a major decision

  Signal impact: HIGH
  Agent response: MODIFY (adjust signal; do not void entirely)
  Position size: Reduce to 50% pending modifier recalculation
  Flag activated: sport-specific flag (e.g., red_card_early, admin_risk)

CATEGORY 4 — TRANSFER AND CONTRACT
  Event types:
    Star player transfer completed overnight before a match
    Player publicly refuses to play (contract dispute)
    Release clause triggered (player departing)
    Pre-contract agreement announced for key player
    Agent publicly confirms player seeking transfer

  Signal impact: HIGH
  Agent response: MODIFY for current match; RELOAD APS/NCSI projections
  Position size: Reduce to 65% for current match signal
  Flag activated: transfer_signal_active + ats_reload_required

CATEGORY 5 — COACHING AND MANAGEMENT
  Event types:
    Manager press conference reveals unexpected tactical change
    Assistant manager/key staff departure announced
    Club ownership change confirmed
    Major boardroom dispute becomes public

  Signal impact: MODERATE
  Agent response: MODIFY (apply manager intelligence framework)
  Position size: 75% pending modifier recalculation
  Flag activated: manager_instability or tactical_uncertainty
  See: core/manager-intelligence.md for the full manager signal model

CATEGORY 6 — EXTERNAL EVENTS
  Event types:
    Extreme weather confirmed (stadium evacuation risk, waterlogged pitch)
    Political protest / security incident near stadium
    Transport infrastructure failure (team delayed in transit)
    Pandemic-level public health restriction (see macro/macro-pandemic-public-health.md)
    Natural disaster affecting a venue city

  Signal impact: MODERATE to CRITICAL (depends on severity)
  Agent response: ESCALATE to human + MODIFY based on available information
  Position size: Reduce to 50%; human approves any action
  Flag activated: external_event_active

CATEGORY 7 — COMMERCIAL AND TOKEN EVENTS
  Event types:
    Fan token platform outage
    Smart contract exploit affecting token
    Major exchange delisting announcement
    Token liquidity crisis (TVL drops > 40% in < 1h)
    Governance vote manipulation detected

  Signal impact: HIGH for token signal; neutral for match signal
  Agent response: SEPARATE match signal from token signal; pause token recommendations
  Position size: Pause token signal entirely; match analysis continues
  Flag activated: liquidity_critical or platform_risk

CATEGORY 8 — MACRO BREAKING NEWS
  Event types:
    Central bank emergency rate decision
    Crypto exchange collapse (FTX-scale event)
    Geopolitical escalation affecting match country
    Regulatory announcement (ban on sports tokens in major market)

  Signal impact: LIBRARY-WIDE (affects all active signals)
  Agent response: MACRO_OVERRIDE — suspend all token recommendations
  Position size: 0% for all token signals until macro reassessment
  Flag activated: macro_override_active (see core/temporal-awareness.md Tier 0)
  See: macro/macro-overview.md + macro/macro-geopolitical.md
```

---

## Agent response protocols

```
PROTOCOL 1 — RELOAD

When to use: Category 1 (key player absent at T-0), Category 2 (match status)
             when match is confirmed to continue at new time

Steps:
  1. Set position_size = 0% immediately
  2. Activate reload_required flag
  3. Log the breaking news event with timestamp
  4. Re-run full SportMind reasoning chain from Step 1
  5. Do NOT use any modifier values from the previous analysis
  6. Output new signal with fresh timestamp and breaking_news_reload = true

Time to reload: < 5 minutes for a standard pre-match signal
               < 2 minutes for a simplified signal (macro + domain only)

Example — goalkeeper substitution at T-0:
  Previous signal: sms 78, ENTER standard
  Breaking news: starter goalkeeper injured in warm-up, backup confirmed
  Action: RELOAD with backup_quality_delta applied
  New signal: sms 71, position_size 65% (reduced confidence from roster change)


PROTOCOL 2 — MODIFY

When to use: Categories 3, 4, 5 (disciplinary, transfer, coaching news)
             when existing signal is still valid but a specific modifier changes

Steps:
  1. Identify which modifier is affected
  2. Apply the relevant breaking news modifier (see table below)
  3. Recalculate composite_modifier and SMS
  4. Note the modification in the signal output
  5. Flag as modified_post_news = true

Breaking news modifiers:
  Early red card (first 15 min): × 0.70 for affected team's signal
  Player refuses to play: × 0.80 (confirmed; motivation compromised)
  Manager sacked within 48h: × 0.88 (tactical uncertainty; new caretaker)
  Transfer confirmed (star departure): × 0.85 for club token
  Unexpected tactical system change (press conference): × 0.92

Threshold: if modified signal SMS drops > 15 points: escalate to human
           regardless of original signal quality


PROTOCOL 3 — VOID

When to use: Category 2 when match is postponed or abandoned
             Category 7 when token platform is non-operational

Steps:
  1. Set signal_status = VOID
  2. Set position_size = 0%
  3. Log void reason and timestamp
  4. Do NOT generate a new signal until event is rescheduled with confirmed details
  5. Alert operator with void notification

Void is permanent for the original event.
When rescheduled: treat as a completely new event — do not carry over signals.


PROTOCOL 4 — ESCALATE

When to use: Category 6 (external events), Category 8 (macro breaking)
             Any breaking news where the correct response is unclear

Steps:
  1. Pause autonomous action immediately
  2. Generate escalation brief (full context, current signal state, what changed)
  3. Send to human review channel
  4. Continue monitoring; do not act until human responds
  5. Log escalation in audit trail

Escalation brief format:
  BREAKING NEWS ESCALATION
  Event: [what happened]
  Category: [1-8]
  Current signal state: [sms, position_size, flags before news]
  Impact assessment: [what changes and why]
  Recommended response: [RELOAD / MODIFY / VOID]
  Confidence in recommendation: [HIGH / MEDIUM / LOW]
  What human needs to decide: [specific question]
  Timeout: [when agent will act without response — default 30 minutes]
```

---

## Signal invalidation rules

```
A pre-computed signal is INVALIDATED (must be discarded) when:

HARD INVALIDATION (always discard):
  → Match postponed or abandoned
  → Key player confirmed absent AFTER signal was generated
    (lineup_unconfirmed flag was active AND player is now confirmed out)
  → Manager change within 24h of match
  → Match moved to neutral venue (home advantage signal no longer applies)
  → Platform outage (token signal cannot be acted on)

SOFT INVALIDATION (modify, not discard):
  → New injury information for non-key players
  → Weather forecast update (apply weather modifier to existing signal)
  → Minor tactical news (press conference quotes)
  → Odds movement > 15% (market has new information; check source)

NOT INVALIDATION (do not modify):
  → Social media rumours without official confirmation
  → Journalist speculation (Category 1 sources only)
  → Historical news that does not affect the current match
  → Token price movement alone (price follows signal; price is not signal)

SOURCE TIER FOR BREAKING NEWS:
  Tier 1 (always act on): Official club announcement, league/federation statement,
          player confirmed absent by manager in press conference
  Tier 2 (apply with modifier): Tier 1 journalist (Sky Sports, ESPN, L'Équipe),
          club official source with track record
  Tier 3 (flag for monitoring, do not modify): Social media reports,
          unverified accounts, aggregator sites
  Tier 4 (ignore): Anonymous sources, forum speculation, price-based inference

AGENT RULE: Only Tier 1 and Tier 2 sources trigger Protocol actions.
  Tier 3 activates monitoring mode only.
  Tier 4 is logged but produces no signal change.
```

---

## Sport-specific breaking news patterns

```
FOOTBALL:
  Most impactful: Manager sacking within 48h of match (MODIFY × 0.88)
  Most common: Injury confirmation at T-2h (RELOAD if key player)
  Watch for: VAR/referee controversy post-match affecting next fixture narrative
  Token signal: Any news involving a club's next match directly affects HAS

CRICKET:
  Most impactful: DLS interruption confirmation (match interrupted by rain)
  Most common: Toss result + pitch report at T-1h
  Watch for: Dew forecast update at T-4h (evening T20s in South Asia)
  Breaking news window: Toss result is the final critical pre-match signal

MMA:
  Most impactful: Weigh-in result (weight miss → RELOAD with × 0.72)
  Most common: Injury in final camp (camp injury reports, 1-2 weeks out)
  Watch for: Post-weigh-in confrontation (motivation signal)
  Protocol: Weight miss is always Category 1 RELOAD regardless of fighter tier

FORMULA 1:
  Most impactful: Grid penalty confirmed (FIA stewards, post-qualifying)
  Most common: Weather forecast update (wet race signal)
  Watch for: Red flag in FP3 (car damage signal before qualifying)
  Breaking news window: Post-qualifying grid penalties are Category 3 MODIFY

NHL:
  Most impactful: Morning skate goaltender absence (RELOAD with backup modifier)
  Most common: Day-to-day designation changed to OUT on game day
  Watch for: Backup confirmed on the ice at morning skate (positive signal)
  Protocol: No goaltender confirmation = lineup_unconfirmed regardless of time

BASKETBALL (NBA):
  Most impactful: Star player DNP-rest confirmed (RELOAD with × 0.70)
  Most common: Load management designation on back-to-back day
  Watch for: Pre-game injury report change (Q → D → O designations)
  Protocol: Injury designations change until 30 minutes before tip-off
```

---

## Integration with autonomous agents

```
BREAKING NEWS IN THE AGENT LIFECYCLE:

During MONITORING state:
  Agent subscribes to news feeds for monitored events
  News arrives → evaluate against taxonomy (Category 1-8)
  Category 1-2: immediate transition to ANALYSING (Protocol RELOAD/VOID)
  Category 3-6: flag for next cycle OR immediate if time-sensitive
  Category 7-8: immediate ESCALATING transition

During WAITING_FOR_HUMAN state:
  Breaking news still processed
  Category 1: override wait — reload and escalate new situation
  Category 2: void signal; notify human that original escalation is moot
  Category 3-6: add to escalation brief; do not restart wait timer

Signal bus publication on breaking news:
  When breaking news triggers RELOAD or VOID, publish invalidation signal to bus:
  {
    "source_agent": "prematch-001",
    "event_id": "ucl-qf-psg-arsenal",
    "signal_type": "signal_invalidation",
    "reason": "key_player_absent_confirmed",
    "protocol": "RELOAD",
    "previous_sms": 78,
    "timestamp": "..."
  }
  All agents subscribed to this event receive the invalidation.
  See: examples/agentic-workflows/multi-agent-coordination.md

ESCALATION COMPLETENESS (Safety Principle 4):
  Breaking news escalations must include:
  1. The news event itself (what happened, source tier, timestamp)
  2. The previous signal state (SMS, action, key modifiers)
  3. The protocol assessment (RELOAD / MODIFY / VOID / ESCALATE)
  4. The specific question for the human to answer
  5. A timeout after which the agent will act autonomously (default 30 min)
  Partial escalations with just "breaking news received" are not acceptable.
```

---


## Autonomous Execution

**Trigger conditions — when this skill should self-invoke:**
- Any Category 1 or Category 2 breaking news event confirmed from Tier 1 source
  for a monitored token's associated club, athlete, or competition
- Category 7/8 (governance / regulatory) breaking news for any monitored token
- Signal invalidation required (RELOAD or VOID protocol triggered)

**Execution at autonomy Level 2:**
- Category 1: immediately trigger RELOAD protocol. Halt position signals.
  Notify operator. Recalculate from scratch once trigger is processed.
- Category 2: apply defined modifier. Flag "CATEGORY_2_ACTIVE" in signal output.
  Recalculate and notify operator.
- Category 7/8: escalate immediately to human. Do not proceed with signal.
- Publish signal invalidation to agent bus for all subscribed agents.

**Execution at autonomy Level 3–4:**
- Auto-process Category 2-6 events within defined response times
- Auto-recalculate and dispatch updated signals for Category 2-6 events
- Category 1 and 7/8 always escalate even at Level 4 — no exception
- Auto-log all breaking news events with category, source tier, and protocol applied

**Hard boundaries:**
- Category 1 events (key player injury, manager sacking) always escalate to human.
  Even at Level 4 autonomy, Category 1 requires human confirmation before action.
- Tier 2 or lower source confirmation is insufficient for Category 1 RELOAD protocol.
  Must be confirmed from official club/federation (Tier 1) before RELOAD triggers.
- VOID protocol (signal discarded entirely) must be logged with explicit reason.
  Never void a signal silently — the void reason is part of the audit trail.
- Response time targets are maximums — earlier is always better.

---

## Compatibility

**Temporal awareness:** `core/temporal-awareness.md` — Tier 4-5 data (match day)
**Manager intelligence:** `core/manager-intelligence.md` — Category 5 detail
**Reasoning patterns:** `core/reasoning-patterns.md` — six-step chain (Step 3: athlete availability)
**Real-time patterns:** `platform/realtime-integration-patterns.md` — live data connections
**Agent framework:** `core/autonomous-agent-framework.md` — Safety Principles 4 and 6
**Multi-agent coordination:** `examples/agentic-workflows/multi-agent-coordination.md` — signal invalidation bus

*MIT License · SportMind · sportmind.dev*
