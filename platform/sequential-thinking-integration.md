# Sequential Thinking Integration — SportMind

**How to use Sequential Thinking MCP to make SportMind's reasoning chain
explicit, auditable, and error-resistant.**

Sequential Thinking MCP gives an agent the ability to reason step-by-step
through a problem — completing each phase before moving to the next, with
each step informed by the results of the previous one. For SportMind, this
transforms a flat context-load into a structured reasoning chain where every
decision is traceable and every signal layer is applied in the correct order.

---

## Why sequential thinking matters for SportMind

```
WITHOUT SEQUENTIAL THINKING:
  Agent loads all five layers simultaneously
  Reasoning is implicit — cannot be audited
  Macro override may be missed if agent jumps to signal
  Disciplinary flags may not surface before commercial recommendation
  Errors are hard to diagnose — was it the wrong skill or wrong reasoning?

WITH SEQUENTIAL THINKING:
  Agent completes Phase 1 before starting Phase 2
  Each phase produces a named output used by subsequent phases
  Macro override stops the chain at Phase 1 — nothing wasted
  Disciplinary flag in Phase 3 prevents ENTER in Phase 5
  Any error is traceable to the exact phase where it occurred
```

---

## The SportMind sequential reasoning chain

SportMind has a natural five-phase reasoning sequence. Sequential Thinking
maps directly onto it.

```
PHASE 1 — MACRO GATE
  Tool: sportmind_macro
  Question: Is the macro environment safe to proceed?
  Output: macro_modifier, macro_phase, active_override
  
  IF macro_modifier < 0.75: STOP → output WAIT_MACRO_OVERRIDE
  IF macro_modifier >= 0.75: PROCEED to Phase 2
  
  Why this is Phase 1:
    The macro modifier gates everything. A crypto bear market (×0.55)
    makes all fan token analysis unreliable regardless of sporting signals.
    There is no point running Phases 2-5 under a macro override.

PHASE 2 — EVENT CONTEXT
  Tool: sportmind_pre_match (or sportmind_signal for simple cases)
  Question: What is the base sporting signal for this event?
  Input: macro_modifier from Phase 1
  Output: direction, adjusted_score, sms, layers_loaded
  
  Apply macro_modifier to adjusted_score immediately.
  IF sms < 40: flag INSUFFICIENT_COVERAGE — note but continue
  Capture: competition tier, use_case, skill_stack loaded

PHASE 3 — DISCIPLINARY CHECK
  Tool: sportmind_disciplinary (for each key player)
  Question: Are any disciplinary flags active for key players?
  Input: event context from Phase 2
  Output: DSM level, active flags, commercial_modifier
  
  IF LEGAL_PROCEEDINGS_ACTIVE: STOP → output ABSTAIN_DISCIPLINARY
  IF COMMERCIAL_RISK_ACTIVE: flag — continue with reduced commercial signal
  IF CITING_ACTIVE: apply DSM_MODERATE (×0.88) to commercial signal
  IF clean: proceed with full commercial signal

PHASE 4 — FAN TOKEN CONTEXT
  Tool: sportmind_fan_token_lookup + sportmind_sentiment_snapshot
  Question: What is the current token state and sentiment vector?
  Input: DSM status from Phase 3
  Output: token tier, lifecycle phase, macro_sentiment, composite_signal
  
  IF COMMERCIAL_RISK_ACTIVE from Phase 3: do not generate ENTER
  IF token in lifecycle Phase 4/5: apply reduced commercial expectation
  Capture: chiliscan verification link, fantokens market reference

PHASE 5 — SIGNAL SYNTHESIS
  Question: What is the final recommendation?
  Input: All outputs from Phases 1-4
  Output: ENTER / WAIT / ABSTAIN + reasoning trace
  
  ENTER conditions (ALL must be true):
    ✓ macro_modifier >= 0.75
    ✓ sms >= 60
    ✓ No LEGAL_PROCEEDINGS_ACTIVE or COMMERCIAL_RISK_ACTIVE
    ✓ Token in active lifecycle phase (Phase 2 or 3)
    ✓ adjusted_score (macro-adjusted) supports direction
    
  WAIT conditions (ANY true):
    → sms 40-59 (partial coverage)
    → CITING_ACTIVE (process pending)
    → Lineup unconfirmed within T-2h
    → Token in lifecycle Phase 4 (plateau)
    
  ABSTAIN conditions (ANY true):
    → macro_modifier < 0.75
    → LEGAL_PROCEEDINGS_ACTIVE
    → sms < 40
    → Token in lifecycle Phase 5/6 (post-partnership)
```

---

## Implementation — Sequential Thinking MCP configuration

```python
# How to configure Sequential Thinking MCP for SportMind
# Add to your claude_desktop_config.json or MCP setup

{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "sportmind": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"]
    }
  }
}
```

---

## System prompt — sequential SportMind agent

Use this system prompt to configure an agent that applies the full
SportMind sequential reasoning chain:

```
You are a SportMind analysis agent. When asked to analyse a fan token
or sporting event, you MUST follow the SportMind sequential reasoning
chain in this exact order:

PHASE 1 — Call sportmind_macro. Check macro_modifier.
  If macro_modifier < 0.75: output WAIT_MACRO_OVERRIDE and stop.
  
PHASE 2 — Call sportmind_pre_match with the event details.
  Apply macro_modifier from Phase 1 to the adjusted_score.
  
PHASE 3 — Call sportmind_disciplinary for each key player mentioned.
  If LEGAL_PROCEEDINGS_ACTIVE: output ABSTAIN and stop.
  If COMMERCIAL_RISK_ACTIVE: flag and reduce commercial signal.
  
PHASE 4 — Call sportmind_fan_token_lookup and sportmind_sentiment_snapshot
  for the relevant token.
  
PHASE 5 — Synthesise all phase outputs into a final recommendation.
  Apply ENTER / WAIT / ABSTAIN rules from core/sequential-thinking-integration.md.
  Show your reasoning for each phase in the output.

Never skip phases. Never generate ENTER if COMMERCIAL_RISK_ACTIVE or
LEGAL_PROCEEDINGS_ACTIVE was set in Phase 3.

Format your output as:
  Phase 1 result: [macro status]
  Phase 2 result: [signal + SMS]
  Phase 3 result: [disciplinary status]
  Phase 4 result: [token context]
  Phase 5 recommendation: ENTER / WAIT / ABSTAIN
  Reasoning: [one sentence per phase explaining the decision]
```

---

## Sequential chain for complex failure analysis

When a signal fails — a WAIT or ABSTAIN — Sequential Thinking provides
structured diagnosis rather than a flat "do not enter" response.

```
FAILURE ANALYSIS SEQUENCE:

Phase 1 — Identify the trigger
  Which phase caused the stop?
  What was the specific value or flag?
  Example: "Phase 3 — CITING_ACTIVE for key striker"

Phase 2 — Assess severity and timeline
  Is this temporary (citing process = 7-14 days) or open-ended (legal)?
  What is the expected resolution window?
  Example: "Judicial hearing in 7 days — resolution by [date]"

Phase 3 — Define the monitoring condition
  What specific change would unlock ENTER?
  What source to monitor?
  Example: "Monitor world.rugby/the-game/judicial-decisions —
            ENTER unlocked if citing dropped or ban < 2 weeks"

Phase 4 — Set the re-analysis trigger
  At what point should the full chain be re-run?
  Example: "Re-run on verdict day. Re-run if ban confirmed > 6 weeks
            (triggers DSM_MODERATE for remainder of season)"
```

---

## Multi-token sequential analysis

When managing a portfolio of fan tokens across multiple clubs and sports,
sequential thinking prevents cascade errors where one token's analysis
bleeds into another.

```
PORTFOLIO SEQUENTIAL PATTERN:

Step 1: sportmind_macro (once — applies to all tokens)
Step 2: For each token:
  a. sportmind_fan_token_lookup → get token context
  b. sportmind_sentiment_snapshot → get current state
  c. sportmind_disciplinary → check key players
  d. sportmind_pre_match → get upcoming event signal (if applicable)
  e. Synthesise → ENTER / WAIT / ABSTAIN for this token

Step 3: Portfolio synthesis
  Compare all token recommendations
  Flag: tokens with conflicting signals
  Flag: tokens where macro-adjusted signal changes recommendation
  Output: ranked portfolio by conviction level

KEY RULE: Each token analysis is independent within the sequential chain.
A WAIT on PSG does not affect the BAR analysis.
A COMMERCIAL_RISK_ACTIVE on one token does not flag others.
```

---

## Integration with existing SportMind tools

```
SEQUENTIAL THINKING CONNECTS TO:

sportmind_pre_match     → Phase 2 primary tool
sportmind_macro         → Phase 1 gate
sportmind_disciplinary  → Phase 3 check
sportmind_fan_token_lookup → Phase 4 resolution
sportmind_sentiment_snapshot → Phase 4 state
sportmind_verifiable_source → Source check at any phase

SKILL FILE REFERENCES:
  core/core-athlete-modifier-system.md — modifier application order
  core/athlete-disciplinary-intelligence.md — Phase 3 DSM values
  fan-token/fan-token-lifecycle/ — Phase 4 lifecycle assessment
  fan-token/fan-sentiment-intelligence/ — Phase 4 sentiment arc
  core/confidence-output-schema.md — Phase 5 output format
```

---

*SportMind v3.35 · MIT License · sportmind.dev*
*See also: platform/memory-integration.md · platform/fetch-mcp-disciplinary.md*
*MCP-SERVER.md for server setup · core/athlete-disciplinary-intelligence.md for DSM values*
