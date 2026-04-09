# Memory MCP Integration — SportMind

**What a SportMind agent should remember across sessions — and how to
structure persistent memory for fan token portfolio intelligence.**

Memory MCP gives an agent persistent storage that survives beyond a single
conversation. For SportMind, this transforms one-shot analysis into
compounding intelligence — each session builds on the last, and patterns
that only emerge over time (a token's seasonal sentiment arc, a player's
repeated disciplinary risk, a macro cycle's effect on a specific sport's
tokens) become visible and actionable.

---

## Why memory matters for fan token intelligence

```
WITHOUT MEMORY:
  Session 1: PSG analysis → WAIT (macro override)
  Session 2: PSG analysis → agent has no memory of previous state
             Repeats macro check, repeats signal generation from scratch
             Cannot detect: "macro has now recovered since last WAIT"
             Cannot detect: "this is the third consecutive WAIT on PSG"

WITH MEMORY:
  Session 1: PSG analysis → WAIT (macro override 0.68)
             Memory stores: {PSG: last_signal=WAIT, macro_at_analysis=0.68, date=...}
  Session 2: PSG analysis → agent retrieves memory
             Detects: macro has recovered to 0.92 since last session
             Detects: PSG has had three consecutive WAITs — investigate pattern
             Produces: "Macro recovery noted since last analysis. Re-running full chain."
```

---

## Memory schema — what to store

### Token memory record

```json
{
  "entity_type": "fan_token",
  "ticker": "PSG",
  "name": "Paris Saint-Germain",
  "sport": "football",
  "last_updated": "2026-04-08T10:00:00Z",
  
  "signal_history": [
    {
      "date": "2026-04-08T10:00:00Z",
      "recommendation": "WAIT",
      "sms": 72,
      "macro_modifier": 0.92,
      "adjusted_score": 50.6,
      "reason": "CITING_ACTIVE — key striker pending judicial hearing",
      "dsm_level": "MODERATE",
      "flags": ["CITING_ACTIVE"]
    }
  ],
  
  "dsm_history": [
    {
      "date": "2026-04-06T00:00:00Z",
      "player": "Key striker",
      "sport": "football",
      "dsm_level": "MODERATE",
      "flag": "CITING_ACTIVE",
      "process_stage": "CITED_OR_CHARGED",
      "expected_resolution": "2026-04-15",
      "resolved": false
    }
  ],
  
  "macro_at_last_analysis": 0.92,
  "consecutive_waits": 1,
  "consecutive_enters": 0,
  "lifecycle_phase": 3,
  
  "upcoming_events": [
    {
      "event": "UCL Quarter-Final leg 2",
      "date": "2026-05-07T20:00:00Z",
      "competition_tier": 1,
      "ftis_estimate": 88
    }
  ],
  
  "notes": "Citing expected resolved by 2026-04-15. Re-run full chain on verdict."
}
```

---

### Macro memory record

```json
{
  "entity_type": "macro_state",
  "last_updated": "2026-04-08T06:00:00Z",
  "crypto_cycle_phase": "NEUTRAL",
  "macro_modifier": 1.00,
  "btc_vs_200d_ma": "above",
  "previous_modifier": 0.92,
  "modifier_direction": "recovering",
  "phase_since": "2026-03-15",
  "active_overrides": [],
  "notes": "Recovered from BEAR phase (0.68) over 3 weeks. Now NEUTRAL."
}
```

---

### Player disciplinary memory record

```json
{
  "entity_type": "player_disciplinary",
  "player": "Player name",
  "club": "Club name",
  "sport": "football",
  "token_association": ["PSG"],
  "last_updated": "2026-04-06T00:00:00Z",
  
  "current_status": {
    "dsm_level": "MODERATE",
    "flag": "CITING_ACTIVE",
    "process_stage": "CITED_OR_CHARGED",
    "offence_type": "On-field conduct — dangerous play",
    "tier": 2,
    "expected_resolution": "2026-04-15",
    "regulatory_source": "world.rugby/the-game/judicial-decisions"
  },
  
  "history": [
    {
      "date": "2025-11-10",
      "dsm_level": "MODERATE",
      "flag": "BAN_CONFIRMED",
      "ban_weeks": 4,
      "resolved": true,
      "resolved_date": "2025-12-08"
    }
  ],
  
  "repeat_offender": true,
  "prior_offences": 1,
  "notes": "Second citing in 12 months — aggravating factor in current hearing."
}
```

---

### Portfolio summary record

```json
{
  "entity_type": "portfolio_summary",
  "last_updated": "2026-04-08T10:00:00Z",
  "tokens_monitored": ["PSG", "BAR", "CITY", "ACM", "JUV"],
  "current_recommendations": {
    "PSG":  "WAIT",
    "BAR":  "ENTER",
    "CITY": "ENTER",
    "ACM":  "WAIT",
    "JUV":  "ENTER"
  },
  "active_flags": {
    "PSG": ["CITING_ACTIVE"],
    "ACM": ["SUSPENSION_RISK"]
  },
  "macro_modifier_at_analysis": 1.00,
  "next_high_ftis_events": [
    {"token": "BAR", "event": "El Clásico", "date": "2026-04-26", "ftis": 95},
    {"token": "PSG", "event": "UCL QF leg 2", "date": "2026-05-07", "ftis": 88}
  ]
}
```

---

## Memory MCP configuration

```python
# claude_desktop_config.json — add Memory MCP server

{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sportmind": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

---

## Memory operations — what the agent does

### At session start (retrieve)

```
1. Retrieve portfolio_summary → what was last recommended per token?
2. Retrieve macro_state → has macro_modifier changed since last session?
3. For each token in scope:
   a. Retrieve fan_token record → last signal, consecutive waits, lifecycle
   b. Retrieve player_disciplinary records → any unresolved flags?
   c. Check upcoming_events → any high-FTIS events since last session?

4. Surface changes:
   "Since last session (3 days ago):
    — PSG: CITING_ACTIVE still unresolved (expected resolution 2026-04-15)
    — Macro: recovered from 0.92 to 1.00 (NEUTRAL phase)
    — BAR: El Clásico in 18 days (FTIS 95) — highest upcoming event
    — ACM: SUSPENSION_RISK player on 4 yellow cards (1 from 5-match ban)"
```

---

### At session end (store)

```
For each token analysed this session:
  → Update signal_history with today's recommendation
  → Update dsm_history if any disciplinary change occurred
  → Update consecutive_waits / consecutive_enters count
  → Update upcoming_events list
  → Add any notes from this session's reasoning

Update macro_state record with current modifier

Update portfolio_summary with all current recommendations
```

---

## Memory-informed reasoning patterns

### Pattern 1 — Macro recovery detection

```
Memory: macro_at_last_analysis = 0.68 (BEAR — was overriding all signals)
Current: macro_modifier = 1.00 (NEUTRAL — recovery complete)

Agent reasoning:
  "Macro has recovered from BEAR (0.68) to NEUTRAL (1.00) since last analysis.
   Previous WAITs driven by macro override may now be actionable.
   Re-running full sequential chain for all WAIT-flagged tokens."
   
Value: Without memory, agent would not know previous WAITs were macro-driven
       and might give a different (wrong) reason for the previous WAIT.
```

---

### Pattern 2 — Repeat disciplinary signal

```
Memory: player_disciplinary history shows prior offence (BAN 4 weeks, Nov 2025)
Current: new CITING_ACTIVE for same player (April 2026)

Agent reasoning:
  "This is a repeat offence within 12 months. World Rugby Regulation 17
   treats prior offences as an aggravating factor — expected ban range
   increases from 8-12 weeks (first offence) to potentially 12-20 weeks.
   Extend DSM_MODERATE duration estimate accordingly."
   
Value: Without memory, agent applies standard first-offence estimate.
       Memory enables the correct (higher) ban estimate for repeat offenders.
```

---

### Pattern 3 — Consecutive WAIT detection

```
Memory: PSG signal_history shows 3 consecutive WAITs over 6 weeks

Agent reasoning:
  "PSG has generated WAIT for three consecutive analyses.
   Review: Was this consistently disciplinary? Consistently macro?
   Or a pattern suggesting structural concern with this token?
   
   History:
   — WAIT 1: macro_override (0.68) — macro-driven
   — WAIT 2: CITING_ACTIVE — disciplinary-driven
   — WAIT 3: lifecycle Phase 4 signal emerging — structural?
   
   Pattern: macro has recovered. Citing resolved. Lifecycle Phase 4
   signal needs investigation — check fan-token/fan-token-lifecycle/."
   
Value: Three WAITs from three different causes = different meaning than
       three WAITs from the same cause. Only visible with memory.
```

---

### Pattern 4 — Pre-event memory preparation

```
Memory: upcoming_events shows UCL QF leg 2 in 29 days (FTIS 88)

Agent proactive trigger:
  "UCL Quarter-Final leg 2 approaches in 29 days (FTIS 88 — high signal).
   Recommended preparation timeline:
   T-14 days: Run full sequential chain — establish baseline
   T-7 days:  Check disciplinary status for key players
   T-48h:     Verify lineup source (club official X account)
   T-2h:      Final confirmation and signal generation
   
   Store: pre_event_preparation_started = true for this event"
   
Value: Memory enables proactive rather than reactive analysis.
```

---

## What NOT to store in memory

```
DO NOT STORE:
  Live prices — these change by the minute; memory would be stale immediately
  Live TVL or liquidity data — same reason
  Specific score predictions — SportMind generates structural signals, not scores
  Personal fan opinions or sentiment expressed in conversation
  Unverified rumours or non-Tier-1 source reports
  
STORE:
  SportMind-generated signals and recommendations (your outputs)
  DSM status and flags (from authoritative sources)
  Macro modifier at each analysis point (from macro-state.json)
  Upcoming events with FTIS estimates (structural calendar data)
  Pattern observations (consecutive WAITs, repeat disciplinary)
  Resolution timelines for active processes (citing, legal)
```

---

## Memory decay — when to clear or archive

```
CLEAR after resolution:
  DSM records: clear CITING_ACTIVE when verdict confirmed
  SUSPENSION_RISK: clear at season start (yellow card accumulation resets)
  MACRO_OVERRIDE: clear when macro_modifier returns above 0.75

ARCHIVE after 6 months:
  Signal history older than one full season
  Resolved disciplinary records (keep for repeat offender detection)
  Pre-event records after event has passed

NEVER clear:
  Repeat offence history (permanent for aggravating factor calculation)
  Lifecycle phase transitions (pattern of Phase 3→4→5 is long-term signal)
  Portfolio performance tracking (for calibration record generation)
```

---

*SportMind v3.35 · MIT License · sportmind.dev*
*See also: platform/sequential-thinking-integration.md · platform/fetch-mcp-disciplinary.md*
*core/athlete-disciplinary-intelligence.md · fan-token/fan-token-lifecycle/*
