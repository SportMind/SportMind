# Cross-Sport Meta Orchestrator — Athlete Intelligence

Cross-sport athlete context layer. Applies to all fan tokens regardless of sport. Covers availability, fatigue, weather, psychological signals, lineup timing, and the master signal modifier pipeline. This is the orchestration layer that all sport-specific skills feed into.

**Applicable tokens:** All active Chiliz fan tokens (see fan-token-pulse/references/chiliz-token-registry.md)

---

## Commands

`get_athlete_signal_modifier` — master command; routes to sport-specific modifier


| Command | Description | Auth |
|---|---|---|
| `get_global_availability_feed` | All tokens — injury/suspension flags in one call | Yes |
| `get_fatigue_index` | Travel, rest days, schedule density per token | Yes |
| `get_weather_impact` | Weather overlay for outdoor sport events | Yes |
| `get_psychological_signals` | Controversy, morale, momentum, streak data | Yes |
| `get_lineup_timing_alert` | Webhook trigger when official lineup confirmed | Yes |
| `get_head_to_head_context` | Team vs team historical context for any sport | Yes |
| `apply_athlete_modifier` | Master pipeline: applies all sub-modifiers to a signal | Yes |
| `get_athlete_adjusted_scores` | All tokens ranked by athlete-adjusted signal scores | Yes |
| `subscribe_athlete_alerts` | Push alerts for key player status changes | Yes |

---

## Command reference

### `get_global_availability_feed`

Single call returning athlete risk flags for all active signals. Designed to be called first in any agent loop.

**Parameters:**
- `min_signal_score` (optional, default: 50) — only return tokens with signal above threshold
- `hours_ahead` (optional, default: 48) — only tokens with events in this window

**Returns:**
```json
{
  "generated_at": "2026-04-06T08:00:00Z",
  "tokens_with_events": 7,
  "availability_flags": [
    {
      "token": "BAR",
      "match": "Barcelona vs Atletico",
      "kickoff_hours": 12,
      "base_signal_score": 72,
      "availability_risk": "MEDIUM",
      "key_flags": ["Gavi DOUBT", "De Jong OUT"],
      "athlete_modifier": 0.83,
      "adjusted_score": 60,
      "action": "HOLD — wait for lineup confirmation"
    },
    {
      "token": "PSG",
      "match": "PSG vs Lyon",
      "kickoff_hours": 36,
      "base_signal_score": 68,
      "availability_risk": "LOW",
      "key_flags": [],
      "athlete_modifier": 1.12,
      "adjusted_score": 76,
      "action": "BUY — full strength, Mbappé HOT form"
    },
    {
      "token": "NAVI",
      "match": "IEM Katowice — Group Stage",
      "kickoff_hours": 8,
      "base_signal_score": 61,
      "availability_risk": "LOW",
      "key_flags": ["Full roster confirmed"],
      "athlete_modifier": 1.15,
      "adjusted_score": 70,
      "action": "CONSIDER — meta aligned, s1mple in form"
    }
  ]
}
```

---

### `get_fatigue_index`

**Parameters:**
- `token` (required)
- `include_international` (optional, default: true) — include international duty travel

**Returns:**
```json
{
  "token": "BAR",
  "fatigue_assessment": {
    "matches_last_7_days": 2,
    "matches_last_14_days": 4,
    "avg_squad_minutes_last_7_days": 186,
    "international_returnees": ["Gavi", "Pedri", "Lewandowski"],
    "avg_travel_km_international_returnees": 7400,
    "days_rest_since_last_match": 3,
    "fixture_congestion_flag": true,
    "rotation_likelihood": "HIGH"
  },
  "fatigue_index": 0.81,
  "fatigue_label": "HIGH",
  "rotation_impact_modifier": 0.88,
  "signal_modifier": 0.91,
  "notes": "3 international returnees with long travel — expect rotation or reduced performance"
}
```

---

### `get_weather_impact`

**Parameters:**
- `token` (required)
- `match_id` (optional)
- `hours_ahead` (optional, default: 24)

**Returns:**
```json
{
  "token": "SPURS",
  "match": "Tottenham vs Arsenal",
  "venue": "Tottenham Hotspur Stadium (Open sections)",
  "weather_forecast": {
    "kickoff_time": "2026-04-06T16:30:00Z",
    "temperature_c": 8,
    "wind_speed_kph": 28,
    "wind_direction": "NW",
    "precipitation_mm": 4.2,
    "precipitation_probability_pct": 72,
    "conditions": "RAINY_WINDY"
  },
  "sport_impact": {
    "long_ball_accuracy_reduction_pct": 18,
    "crossing_accuracy_reduction_pct": 22,
    "set_piece_delivery_reduction_pct": 15,
    "pace_advantage_neutral": true,
    "high_press_effectiveness_reduction_pct": 12
  },
  "weather_modifier": 0.94,
  "signal_modifier": 0.94,
  "notes": "Wind disrupts long ball game and set piece delivery — low-scoring match more likely"
}
```

**Weather impact by sport:**
- Football: wind affects crossing, long balls, set pieces
- Rugby: wind affects kicking (major modifier)
- Cricket: dew affects ball swing, toss decision, run rates
- Tennis: wind affects serve accuracy and consistency
- NFL: wind affects passing, field goals
- Esports: no weather modifier (indoor, always 1.0)

---

### `get_psychological_signals`

**Parameters:**
- `token` (required)
- `days` (optional, default: 14)

**Returns:**
```json
{
  "token": "JUV",
  "psychological_signals": {
    "win_streak": 0,
    "loss_streak": 2,
    "recent_red_cards": 1,
    "recent_controversy": {
      "flag": true,
      "description": "Manager public criticism of squad after last defeat",
      "severity": "MODERATE"
    },
    "contract_dispute_flags": ["Player X contract talks stalled"],
    "home_crowd_advantage": true,
    "post_international_break": true,
    "post_international_break_historical_win_rate": 0.42,
    "fan_sentiment_score": 38,
    "dressing_room_cohesion_estimate": "LOW"
  },
  "psychological_modifier": 0.82,
  "signal_modifier": 0.82,
  "notes": "Loss streak + manager controversy + poor post-intl break record = significant negative modifier"
}
```

---

### `get_lineup_timing_alert`

Register for webhook push when lineup is confirmed for a token's upcoming match.

**Parameters:**
- `token` (required)
- `webhook_url` (required)
- `match_id` (optional — defaults to next match)
- `trigger_at` (optional) — `official_release` (default), `press_conference`, `rumour`

**Returns:**
```json
{
  "subscription_id": "lta_psg_20260405",
  "token": "PSG",
  "match": "PSG vs Lyon",
  "kickoff": "2026-04-07T20:00:00Z",
  "expected_release": "2026-04-07T18:45:00Z",
  "trigger": "official_release",
  "webhook_url": "https://your-agent.endpoint.com/lineup",
  "payload_preview": {
    "token": "PSG",
    "lineup_confirmed": true,
    "key_players_starting": 5,
    "athlete_modifier": "WILL_BE_COMPUTED",
    "adjusted_signal_score": "WILL_BE_COMPUTED",
    "recommendation": "WILL_BE_COMPUTED"
  }
}
```

**Webhook payload on trigger:**
```json
{
  "event": "LINEUP_CONFIRMED",
  "token": "PSG",
  "match": "PSG vs Lyon",
  "minutes_to_kickoff": 74,
  "athlete_modifier": 1.18,
  "base_signal_score": 68,
  "adjusted_signal_score": 80,
  "action": "BUY — full strength lineup confirmed, Mbappé starting",
  "confidence": 0.84,
  "expires_at": "2026-04-07T20:00:00Z"
}
```

---

### `apply_athlete_modifier`

Master pipeline. Runs all applicable sub-skills and returns composite modifier.

**Parameters:**
- `token` (required)
- `sport` (optional — auto-detected if omitted)
- `match_id` (optional)
- `include_weather` (optional, default: true)
- `include_psychological` (optional, default: true)

**Returns:**
```json
{
  "token": "BAR",
  "sport": "football",
  "match": "Barcelona vs Atletico Madrid",
  "base_signal_score": 72,
  "pipeline_results": {
    "availability_modifier": 0.83,
    "form_modifier": 1.05,
    "goalkeeper_modifier": 1.02,
    "fatigue_modifier": 0.91,
    "weather_modifier": 0.97,
    "psychological_modifier": 0.96,
    "set_piece_modifier": 1.00,
    "lineup_confirmation_modifier": 0.95,
    "head_to_head_modifier": 1.04
  },
  "composite_modifier": 0.77,
  "adjusted_signal_score": 55,
  "adjusted_direction": "NEUTRAL",
  "confidence": 0.71,
  "key_risks": [
    "Gavi DOUBT — press confirmation pending",
    "De Jong OUT — midfield depth reduced",
    "High fatigue index — international returnees",
    "Lineup not confirmed — using interim modifier"
  ],
  "agent_recommendation": "HOLD — score drops from BULLISH to NEUTRAL after athlete layer. Re-evaluate at lineup confirmation (-1h).",
  "re_evaluate_at": "2026-04-05T19:00:00Z"
}
```

---

### `get_athlete_adjusted_scores`

All tokens with upcoming events, ranked by athlete-adjusted signal score.

**Parameters:**
- `hours_ahead` (optional, default: 48)
- `min_adjusted_score` (optional, default: 60)
- `direction` (optional) — `long`, `short`, `all`

**Returns:**
```json
{
  "generated_at": "2026-04-06T08:00:00Z",
  "ranked_tokens": [
    {
      "token": "PSG",
      "match": "PSG vs Lyon",
      "kickoff_hours": 36,
      "base_score": 68,
      "athlete_modifier": 1.18,
      "adjusted_score": 80,
      "direction": "BULLISH",
      "confidence": 0.87,
      "top_factor": "Mbappé confirmed starting, HOT form (5G last 5)"
    },
    {
      "token": "NAVI",
      "match": "IEM Group Stage",
      "kickoff_hours": 8,
      "base_score": 61,
      "athlete_modifier": 1.15,
      "adjusted_score": 70,
      "direction": "BULLISH",
      "confidence": 0.79,
      "top_factor": "Full roster, s1mple rating 1.38 last event"
    },
    {
      "token": "ATM",
      "match": "Atletico vs Barcelona",
      "kickoff_hours": 12,
      "base_score": 58,
      "athlete_modifier": 1.10,
      "adjusted_score": 64,
      "direction": "BULLISH",
      "confidence": 0.72,
      "top_factor": "Full defensive unit confirmed, Atletico home fortress"
    }
  ]
}
```

---

## Master modifier reference

| Signal modifier range | Meaning | Agent action |
|---|---|---|
| 1.20+ | Elite conditions — full strength, HOT form, favourable matchup | Strong entry signal |
| 1.10–1.19 | Strong conditions — most key players fit, good form | Entry with normal sizing |
| 1.00–1.09 | Neutral — no major boosts or concerns | Follow team signal as-is |
| 0.90–0.99 | Minor concerns — some fatigue, unconfirmed lineup | Reduce size or wait |
| 0.80–0.89 | Significant concerns — key doubt, high fatigue, weather | Strong caution, likely skip |
| 0.70–0.79 | Major degradation — key player out, multiple absences | Skip unless whale signal overrides |
| Below 0.70 | Severe — multiple outs, backup GK, crisis conditions | Do not enter |

---

## Autopilot template

```json
{
  "template_id": "athlete_aware_matchday",
  "description": "Matchday momentum strategy with athlete-layer signal adjustment",
  "params": {
    "entry_timing": "-2h_before_kickoff",
    "exit_timing": "fulltime",
    "min_athlete_adjusted_score": 68,
    "require_lineup_confirmed": true,
    "max_fatigue_index": 0.85,
    "min_key_player_availability_pct": 80,
    "weather_veto_threshold": 0.88,
    "psychological_veto_threshold": 0.80,
    "recheck_at_lineup_confirmation": true,
    "position_size_scaling": "proportional_to_modifier"
  },
  "risk_level": "moderate",
  "expected_trade_frequency": "1-3 per matchday",
  "note": "Combine with sell_ratio_brackets check — athlete layer does not override whale distribution signals"
}
```
