---
name: signal-confidence-framework
description: >
  When signals are actionable and when they are not. How confidence degrades as
  uncertainty increases. When to recommend HOLD regardless of direction. Layer
  conflict resolution hierarchy. Load before producing any SportMind output.
---

# Signal Confidence Framework

**When to act and when to hold. How certainty degrades with missing information.**

> Load as the final check before producing any SportMind signal output.
> Load alongside: core/agent-reasoning-chains.md · core/agent-onboarding.md

---

## Confidence levels

```
HIGH CONFIDENCE — ENTER or EXIT:
  ALL of the following must be confirmed:
  ✓ Starting lineup confirmed (official club announcement or T-2h sources)
  ✓ Key player availability confirmed (not just rumoured)
  ✓ Weather conditions confirmed (T-2h weather station, not T-72h forecast)
  ✓ Referee appointment confirmed (if applying officiating modifier)
  ✓ No active macro override flag
  ✓ Adjusted score above 65 OR below 35 (clear directional signal)
  ✓ Composite modifier within ×0.85–×1.15 range (no extreme outlier)
  
  Recommended action: ENTER or EXIT based on direction
  Signal class: EXECUTION

MEDIUM CONFIDENCE — MONITOR:
  One or more of the following are unconfirmed:
  · Lineup not yet announced (T-24h or earlier)
  · One key player availability is unclear or unverified
  · Weather forecast but not yet confirmed at T-2h
  · Referee not yet announced for this match
  · Adjusted score is 55-65 or 35-45 (moderate directional signal)
  
  Recommended action: MONITOR — position, do not execute
  Signal class: PLANNING
  Note: T-2h will upgrade this to HIGH or downgrade to LOW

LOW CONFIDENCE — HOLD:
  Two or more of the following conditions present:
  · Lineup unconfirmed
  · Multiple key player availabilities unclear
  · Significant weather uncertainty (storm risk, venue uncertain)
  · Macro override recently triggered or under evaluation
  · Adjusted score is 45-55 (effectively a coin flip)
  
  Recommended action: HOLD — wait for T-2h execution quality signal
  Signal class: MONITOR (not PLANNING or EXECUTION)
```

---

## Uncertainty stacking

```
UNCERTAINTY ACCUMULATION RULE:

  Each unconfirmed variable reduces confidence by one tier:
    3 confirmed variables, 1 unconfirmed → MEDIUM
    2 confirmed, 2 unconfirmed → LOW
    Any combination of 3+ unconfirmed → automatic LOW regardless of score
    
  AUTOMATIC HOLD — three or more unconfirmed variables:
    Do not proceed to signal output.
    Return: signal_class = MONITOR, recommended_action = HOLD
    Reason: compound uncertainty means the signal has insufficient reliability
      to justify any directional position.
```

---

## Override conditions — always HOLD

```
THESE CONDITIONS TRIGGER AUTOMATIC HOLD REGARDLESS OF ADJUSTED SCORE:

  1. ACTIVE MACRO OVERRIDE FLAG:
     If macro/macro-regulatory-sportfi.md or macro/macro-crypto-market-cycles.md
     has flagged macro_override_active = true:
     → HOLD entire signal
     → Macro override is the highest-priority flag in the system
     
  2. THREE OR MORE KEY ABSENCES UNCONFIRMED:
     If 3+ key players have unclear availability (not confirmed absent OR present):
     → HOLD — too much athlete uncertainty
     → Wait for T-2h official confirmation
     
  3. FTP PATH_2 WITH LINEUP UNCONFIRMED ($AFC):
     For PATH_2 tokens: supply event magnitude depends on exact lineup.
     If lineup is unconfirmed: supply event estimate is too imprecise to size.
     → HOLD PATH_2 sizing — proceed with directional signal only
     → Confirm at T-2h before any supply-event-dependent positioning
     
  4. ADJUSTED SCORE BETWEEN 48-52:
     This range represents a coin flip — neither side has a reliable edge.
     → HOLD regardless of composite modifier
     → Small modifier shifts within this range are not reliable signals
     
  5. COMPOUND WEATHER MODIFIER BELOW ×0.75:
     Extreme conditions create unpredictable outcomes — even the weather model
     is unreliable at this level of severity.
     → HOLD directional signal; flag EXTREME_CONDITIONS
```

---

## Confidence decay by time

```
SIGNAL RELIABILITY BY TIME BEFORE KICKOFF:

  T-72h and earlier:
    Confidence: LOW — planning only
    Issues: lineup unknown, weather unknown, late news possible
    Use for: tournament/season-level planning; never for execution
    
  T-48h:
    Confidence: LOW-MEDIUM — team news beginning to emerge
    Issues: likely lineup still uncertain; weather unreliable
    Use for: position planning; not execution sizing
    
  T-24h:
    Confidence: MEDIUM — squad usually announced; weather more reliable
    Issues: late injuries possible; weather still has variance
    Use for: provisional positioning
    
  T-2h:
    Confidence: HIGH — lineup confirmed; weather confirmed; referee confirmed
    Use for: execution quality signal
    The T-2h signal is the primary execution signal for all SportMind chains
    
  Post-kickoff:
    All pre-match signals are deprecated.
    In-match reasoning (if applicable): see chain steps for in-match modifiers
    Do not use pre-match adjusted score post-kickoff for new positions
```

---

## Conflicting layer resolution hierarchy

```
LAYER CONFLICT RESOLUTION:

  When two layers produce contradictory signals, apply this hierarchy
  in strict order — higher priority always supersedes lower:

  PRIORITY 1 — MACRO OVERRIDE (highest authority):
    Source: macro/macro-regulatory-sportfi.md or macro/macro-crypto-market-cycles.md
    If macro_override_active = true: HOLD regardless of all other signals
    Macro override can only be removed by the macro layer itself, not by sport signals
    
  PRIORITY 2 — FTP PATH_2 SUPPLY MECHANICS:
    Source: fan-token/ftp-path2.md
    For $AFC only: supply signal adds a second independent dimension to the direction
    signal. This does not override direction — it adds supply event probability.
    Conflict resolution: supply and direction are independent; report both
    
  PRIORITY 3 — CONFIRMED ATHLETE ABSENCES:
    Source: athlete/[club].md + tier-a-clubs-framework.md
    Confirmed key absence: apply modifier before finalising direction assessment
    If absence modifier shifts adjusted score from one confidence tier to another:
      Upgrade confidence level check before output
    Unconfirmed absence: flag as LINEUP_UNCERTAINTY; do not apply modifier
    
  PRIORITY 4 — SPORT DOMAIN BASE SIGNAL:
    Source: sports/[sport]/[competition].md
    The primary adjusted score and direction source.
    All other modifiers stack on top of this foundation.
    Never skip this layer — it is the signal foundation.
    
  PRIORITY 5 — VENUE AND WEATHER:
    Source: core/venue-intelligence.md + core/weather-intelligence.md
    Apply as the final modifier stack before confidence check.
    Weather at T-2h: full weight | Weather forecast at T-48h: ×0.60 weight
    
  PRIORITY 6 — PSYCHOLOGICAL AND HISTORICAL PATTERNS:
    Source: core/psychological-intelligence.md + core/historical-pattern-intelligence.md
    Apply ONLY when:
      Confirmed pattern with minimum five comparable situations
      Pattern is enduring (spans different squads AND managers)
    Do not apply psychological or historical modifiers without sample qualification.
    These are the lowest-priority modifiers — they refine, not determine, the signal.
```

---

## Required output structure

```
EVERY SPORTMIND SIGNAL MUST INCLUDE THESE FIELDS:

  {
    "direction":           "HOME" | "AWAY" | "DRAW",
    "adjusted_score":      [0-100],
    "sms":                 [0-100],
    "recommended_action":  "ENTER" | "EXIT" | "HOLD" | "MONITOR",
    "composite_modifier":  [decimal, e.g. 1.10],
    "modifiers_applied": {
      "athlete_modifier":     [decimal],
      "venue_modifier":       [decimal],
      "weather_modifier":     [decimal],
      "officiating_modifier": [decimal],
      "psychological_modifier":[decimal]
    },
    "flags": {
      "lineup_unconfirmed":    [bool],
      "macro_override_active": [bool],
      "ftp_path2_active":      [bool],
      "supply_event_type":     "REDUCTION" | "MINT" | "NONE",
      "weather_override_active":[bool],
      "hold_recommended":      [bool]
    },
    "confidence_level":    "HIGH" | "MEDIUM" | "LOW",
    "signal_class":        "EXECUTION" | "PLANNING" | "MONITOR"
  }
  
  FIELDS THAT MAY NOT BE OMITTED:
    direction, adjusted_score, recommended_action, confidence_level, signal_class
    All other fields may be null if not applicable but must be present.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches what makes a signal actionable versus what triggers a HOLD — the threshold framework that prevents agents from acting on insufficient evidence.

**Reasoning:** Provides the structured output schema and confidence level classification system that every SportMind analysis must produce before being acted upon.

**Context:** Applies to every analysis at the output stage — confidence level and HOLD conditions must be assessed after all modifiers are applied, before any output is finalised.

**Memory:** Draws on calibration tier data (from calibration-feedback-loop.md) to assign appropriate confidence levels — a signal built on Tier 0 modifiers cannot be HIGH confidence.

**Judgment:** This file IS the Judgment framework at the output level — knowing when to say HOLD rather than forcing a LOW confidence output is the core Judgment function.

**Attention:** Confidence level determines how much agent attention the output deserves — HIGH confidence warrants action, MEDIUM warrants monitoring, LOW warrants explicit uncertainty communication, HOLD warrants stopping.

**Learning:** Each confirmed HIGH confidence signal that was correct reinforces the confidence threshold calibration. Each incorrect HIGH confidence signal triggers review of what elevated it prematurely.

**Integration:** Confidence assessment must account for all simultaneously active modifiers — a signal may be HIGH on sport domain alone but LOW when macro uncertainty and missing lineup data are integrated.

---

## Compatibility

**Reasoning chains:**   `core/agent-reasoning-chains.md`
**Loading order:**      `core/agent-onboarding.md`
**Macro override:**     `macro/macro-crypto-market-cycles.md`
**PATH_2 mechanics:**   `fan-token/ftp-path2.md`

---

*SportMind v3.97.38 · MIT License · sportmind.dev*
*The T-2h signal is the primary execution signal. Earlier signals are planning only.*
