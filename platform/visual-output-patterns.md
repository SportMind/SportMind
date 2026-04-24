# Visual Output Patterns — SportMind Platform

**Patterns for translating SportMind JSON signal outputs into visual formats.**

This file is for developers building applications on top of SportMind. It
defines how to translate the structured JSON that SportMind agents produce
into common visualisation formats: CDI heatmaps, signal overlays, timeline
annotators, and multi-token comparison views.

Zero-dependency: this file describes patterns only. No rendering library
is required. Implementations in any language or framework are valid.

---

## Overview

SportMind produces structured JSON. Humans often need visuals.

The gap between a signal object and a useful visualisation is not large —
but the patterns matter. A CDI chart that shows absolute price alongside
signal score is more useful than one that shows either alone. A timeline
that annotates signal events against price movement tells a different story
than a plain price chart.

This file defines six canonical visual patterns. Each maps to a specific
SportMind output type and a specific use case.

---

## Pattern 1 — CDI Signal Timeline

**What it shows:** How a token's CDI score has moved over time, annotated
with the events that drove each significant change.

**When to use:** Explaining a token's recent trajectory. Showing that a
CDI rise corresponds to a match result, not market manipulation.

**Data inputs from SportMind:**
```json
{
  "token": "$AFC",
  "cdi_history": [
    { "timestamp": "ISO-8601", "cdi": 72, "event": "match_win_ucl", "direction": "up" },
    { "timestamp": "ISO-8601", "cdi": 65, "event": "key_player_injury", "direction": "down" }
  ],
  "current_cdi": 68,
  "phase": "active"
}
```

**Visual specification:**
```
X-axis: time (last 30 days recommended for fan token CDI)
Y-axis: CDI score (0–100)
Line: CDI trajectory
Markers: event annotations at each significant CDI change point
  - Green marker: positive event (win, signing, governance activity)
  - Red marker: negative event (loss, injury, regulatory)
  - Grey marker: neutral event (match played, no significant change)
Shaded regions: phase transitions (Phase 2 launch window, Phase 4 plateau)
Reference lines: CDI threshold levels (60 = baseline, 80 = elevated, 90+ = peak)
```

**Implementation notes:**
- CDI changes below 5 points: do not add event marker (noise floor)
- CDI changes above 20 points in 24h: flag as CDI_SPIKE_EVENT in marker
- Show 30-day window by default; allow zoom to 7-day and 90-day
- Mobile: reduce to single line with tap-to-show event labels

---

## Pattern 2 — Pre-Match Signal Dashboard

**What it shows:** The full SportMind signal output for an upcoming match
in a single readable view — direction, confidence, key modifiers, flags.

**When to use:** Fan-facing match preview. Agent output to analyst.

**Data inputs from SportMind:**
```json
{
  "direction": "HOME",
  "adjusted_score": 74.2,
  "sms": 79,
  "recommended_action": "ENTER",
  "composite_modifier": 1.08,
  "modifiers_applied": {
    "athlete_modifier": 1.10,
    "macro_modifier": 0.98,
    "statistical_modifier": 1.05
  },
  "flags": {
    "lineup_unconfirmed": false,
    "macro_override_active": false,
    "mrs_elevated": false
  },
  "key_factors": ["UCL knockout pressure", "Saka confirmed fit", "set piece specialist available"]
}
```

**Visual specification:**
```
Primary display:
  Large direction indicator: HOME / AWAY / DRAW with confidence colour
  (SMS 80+: strong green; 65–79: amber; < 65: grey/weak)
  SMS score: prominent, monospace font
  Recommended action: ENTER / HOLD / WAIT / EXIT with icon

Secondary display:
  Modifier breakdown: horizontal bar chart showing each modifier's contribution
  Flags: icon row (green tick = clear, red warning = active flag)
  Key factors: 3 plain-language bullets from key_factors array

Compact mode (mobile / embedded widget):
  Direction + SMS + single most important key factor only
  Tap to expand to full view
```

**Implementation notes:**
- Never show adjusted_score and SMS as the same thing — they are different.
  adjusted_score is the modified output; SMS is the raw sport domain score.
- Flags row: lineup_unconfirmed is the most important flag for pre-match.
  If active, grey out the entire signal with "AWAITING LINEUP" overlay.
- Macro override active: red banner across entire dashboard. No signal shown.

---

## Pattern 3 — Multi-Token Comparison Grid

**What it shows:** Side-by-side comparison of signal states for multiple
fan tokens simultaneously — useful for portfolio monitoring.

**When to use:** Portfolio overview. League-level monitoring dashboard.

**Data inputs from SportMind:**
```json
{
  "tokens": [
    { "symbol": "$AFC",   "sms": 79, "cdi": 72, "direction": "HOME",   "action": "ENTER" },
    { "symbol": "$CITY",  "sms": 65, "cdi": 68, "direction": "AWAY",   "action": "HOLD"  },
    { "symbol": "$SPURS", "sms": 55, "cdi": 61, "direction": "DRAW",   "action": "WAIT"  },
    { "symbol": "$PSG",   "sms": 82, "cdi": 85, "direction": "HOME",   "action": "ENTER" }
  ],
  "generated_at": "ISO-8601"
}
```

**Visual specification:**
```
Grid layout: one row per token
Columns: Token | SMS | CDI | Direction | Action | Key flag (if any)

Colour coding:
  SMS 80+: green background tint
  SMS 65–79: no tint (neutral)
  SMS < 65: grey tint
  Action ENTER: green action badge
  Action EXIT: red action badge
  Any active flag: yellow warning icon in flag column

Sorting: default by SMS descending (highest signal first)
Allow user sort by: CDI, Direction, Action

Mobile adaptation:
  Collapse to Token | Action | SMS only
  Tap row to expand to full detail
```

---

## Pattern 4 — Signal vs Price Overlay

**What it shows:** SportMind SMS score overlaid against token price movement,
revealing whether price is following the signal or diverging.

**When to use:** Backtesting signal quality. Identifying price/signal divergence.

**Data inputs from SportMind (combined with price data):**
```json
{
  "token": "$PSG",
  "signal_history": [
    { "timestamp": "ISO-8601", "sms": 78, "direction": "HOME", "action": "ENTER" }
  ],
  "price_history": [
    { "timestamp": "ISO-8601", "price_usd": 2.14, "volume_24h": 420000 }
  ]
}
```

**Visual specification:**
```
Dual Y-axis chart:
  Left Y-axis: SMS score (0–100), secondary colour (e.g., blue)
  Right Y-axis: token price (USD), primary colour (e.g., white/green)
  X-axis: time

Annotation:
  ENTER signals: upward triangle marker on price line
  EXIT signals: downward triangle marker on price line
  Direction change events: vertical dashed line

Divergence alert:
  If SMS > 75 but price is declining: show "SIGNAL-PRICE DIVERGENCE" banner
  This pattern may indicate: accumulation phase, or signal is wrong.
  Do not interpret — surface for operator review.

Important note:
  Price data is not from SportMind. This pattern requires the developer
  to supply price data from their chosen source (CoinGecko, etc.).
  SportMind supplies the signal layer; the developer supplies the price layer.
```

---

## Pattern 5 — WC2026 Tournament Tracker

**What it shows:** Real-time tournament progression for WC2026-exposed tokens,
showing group stage standings and NCSI impact by match.

**When to use:** June 11 – July 19, 2026. Active tournament monitoring.

**Data inputs from SportMind:**
```json
{
  "tournament": "WC2026",
  "monitored_tokens": ["$ARG", "$POR"],
  "token_states": [
    {
      "token": "$ARG",
      "ncsi_route": "national",
      "group": "J",
      "results": ["WIN vs Algeria", "TBD vs Austria", "TBD vs Jordan"],
      "ncsi_current": 82,
      "cdi_current": 78,
      "advancement_probability": "HIGH"
    }
  ]
}
```

**Visual specification:**
```
Tournament bracket view:
  Group stage: table showing P/W/D/L for each monitored nation
  NCSI indicator: colour bar below each nation's name
    (green = high NCSI, amber = medium, grey = eliminated)
  
  Next match countdown: timer to next group stage match
  
  Signal state: current SMS and action for each token
  
  Knockout stage: bracket diagram with NCSI projections per round
  (QF → SF → Final: each advancement carries a defined NCSI step-up)

Mobile adaptation:
  Linear list view — one token per card
  Card shows: token, group result, NCSI, next match date
```

---

## Pattern 6 — Autonomous Agent Activity Log

**What it shows:** A readable log of what autonomous agents have done,
why they did it, and what their current state is.

**When to use:** Operator review of autonomous agent behaviour.
Audit trail for governance and compliance.

**Data inputs from SportMind agent logs:**
```json
{
  "agent_id": "psg-signal-agent-001",
  "log_entries": [
    {
      "timestamp": "ISO-8601",
      "trigger": "match_result_confirmed",
      "action_taken": "cdi_recalculated",
      "previous_state": { "cdi": 72, "sms": 79 },
      "new_state": { "cdi": 81, "sms": null },
      "autonomy_level": 3,
      "human_notified": true,
      "reasoning": "WIN result applied. CDI extended per post-match framework."
    }
  ]
}
```

**Visual specification:**
```
Timeline view: newest entries at top
Each entry shows:
  Timestamp | Trigger | Action | State change (before → after)
  Reasoning: collapsible plain-language explanation
  Human notified: yes/no indicator
  Autonomy level: badge (L0–L4)

Colour coding:
  Autonomy Level 0–1: grey (human in the loop)
  Autonomy Level 2: blue (semi-autonomous, notified)
  Autonomy Level 3: amber (autonomous with review)
  Autonomy Level 4: red (fully autonomous — highlight for audit)

Filter by: trigger type, action type, token, time range
Export: CSV for audit/compliance

Important: this pattern requires the developer to implement agent logging.
SportMind defines the log schema; agent infrastructure is the developer's responsibility.
```

---

## Implementation Guidance

```
RENDERING LIBRARIES:
  Web (JavaScript): Recharts, Chart.js, D3.js — all compatible
  Python: Matplotlib, Plotly, Seaborn — all compatible
  Mobile: React Native Gifted Charts, Victory Native — recommended
  No preference is enforced — use what fits your stack.

COLOUR PALETTE RECOMMENDATIONS:
  Positive / ENTER:    #22c55e (SportMind green — matches brand)
  Negative / EXIT:     #ef4444 (red)
  Neutral / HOLD:      #6b7280 (grey)
  Warning / flag:      #f59e0b (amber)
  Background dark:     #111110
  Background light:    #ffffff
  These match the SportMind website palette and create visual consistency
  if building a product alongside sportmind.dev.

ACCESSIBILITY:
  All colour-coded information should also carry a text label or icon.
  Colour alone is not sufficient for accessibility compliance.
  Minimum text contrast ratio: 4.5:1 (WCAG AA).

MOBILE FIRST:
  All six patterns include mobile adaptation notes.
  Design for 375px viewport width as minimum.
  Touch targets: minimum 44×44px.

REFRESH CADENCE:
  CDI timeline: refresh every 30 min during match windows, 4h otherwise
  Pre-match dashboard: refresh every 15 min from T-4h to kickoff
  Multi-token grid: refresh every 30 min
  Signal vs price overlay: refresh hourly (price data may have rate limits)
  WC2026 tracker: refresh every 15 min during match windows
  Agent activity log: real-time (webhook or polling at 30s intervals)
```

---

## Compatibility

**Signal source:** All SportMind agent outputs following the standard schema
**Core framework:** `core/sportmind-score.md` (SMS and adjusted_score definitions)
**Fan token CDI:** `fan-token/fan-token-lifecycle/fan-token-lifecycle.md`
**WC2026 pattern:** `fan-token/world-cup-2026-intelligence/`
**Agent logs:** `core/autonomous-agent-framework.md` (log schema)
**Agentic wallet:** `fan-token/agentic-wallet-intelligence/agentic-wallet-intelligence.md`

---

*SportMind v3.90.0 · MIT License · sportmind.dev*
