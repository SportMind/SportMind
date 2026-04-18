---
name: post-match-signal-framework
description: >
  Structured post-match analysis workflow for SportMind agents. Use when a match
  result has just been confirmed and an agent needs to assess the commercial impact
  on fan tokens, update signal state, and determine whether ENTER/WAIT/ABSTAIN
  recommendations have changed. Covers the 4h, 24h, and 72h post-result windows,
  result-type commercial modifiers, and the transition from pre-match to post-match
  signal mode. Complements core/core-result-impact-matrices.md (which has the base
  impact values) with a structured agent workflow for applying them.
---

# Post-Match Signal Framework — SportMind

**What an agent does in the hours after a result.**

Every SportMind skill focuses on pre-match analysis. Post-match is the period
when fan token price movements are most predictable and most measurable — a win
creates a documented 24-72 hour elevation window, a loss creates a documented
decline, and the magnitude and duration of both are well-modelled.

This framework defines the post-match agent workflow: what to check, in what
order, at what time intervals, and what signals emerge from result analysis that
were not available pre-match.

---

## Why post-match has a distinct signal structure

```
PRE-MATCH:
  Signal quality is limited by uncertainty (lineup, form, conditions)
  Agent outputs direction and confidence with multiple unknowns
  SMS typically 60-80 (some uncertainty always present)

POST-MATCH:
  All pre-match uncertainties resolved
  Actual performance data available (goals, assists, minutes, GSAx)
  On-chain holder behaviour observable (did prediction materialise?)
  NCSI calculation can begin immediately (was key ATM player impactful?)
  Transfer signal emerges (did breakout performance change APS?)
  
  THE KEY INSIGHT:
  Post-match is not the end of analysis — it is the start of the next cycle.
  A win post-match generates a 24-72h commercial window.
  An unexpected win generates a longer window than a predicted win.
  A loss after pre-match ENTER = immediate position review required.
```

---

## Post-match time windows

```
T+0 to T+2h — IMMEDIATE WINDOW:
  Purpose: Signal confirmation and first response
  
  Checklist:
  □ Confirm result via Tier 1 source (BBC Sport, official league app)
  □ Check for post-match steward/referee decisions (F1, rugby citing, VAR)
  □ Note: were key ATM players involved? Goals, assists, standout performances?
  □ Check token price reaction (chiliscan or fantokens.com)
  □ Calculate: did result match pre-match signal direction?
    → YES: signal confirmed — note for calibration
    → NO: note as potential calibration record (wrong predictions equally valuable)
  □ Update Memory MCP: result + pre-match direction + outcome match
  
  AGENT BEHAVIOUR:
    Do not generate new commercial signal in T+0 to T+2h
    This is confirmation and data collection, not new signal generation
    Exception: dramatic result (massive upset) → immediate position review

T+2h to T+24h — PRIMARY COMMERCIAL WINDOW:
  Purpose: Main post-match commercial signal generation
  
  Checklist:
  □ Run sportmind_sentiment_snapshot — has composite signal changed?
  □ Check LunarCrush Galaxy Score (via social-intelligence-connector.md)
    → Win: is Galaxy Score elevated vs pre-match baseline?
    → Loss: is Galaxy Score declining?
  □ Calculate NCSI if national team players were involved
  □ Check on-chain velocity (address intelligence — transfer rate spike?)
  □ Apply result impact from core/core-result-impact-matrices.md
  □ Generate updated commercial signal for token
  □ Set CDI clock: start Commercial Duration Index from T+2h, not T+0
  
  WHY T+2h NOT T+0:
    First 2 hours are price discovery — volatile, high spread, low signal reliability
    T+2h onwards: price stabilises, on-chain activity patterns emerge, signal is actionable

T+24h — CONFIRMATION WINDOW:
  Purpose: Verify elevation/decline is sustained or reverting
  
  Checklist:
  □ Check token price vs T+0 baseline
  □ Check Galaxy Score trend (rising/falling/stable)
  □ Check holder count vs pre-match (address intelligence S3)
  □ Assess: is elevation sustainable or mean-reverting?
  □ Update CDI estimate based on actual observed decay vs expected
  □ Flag: unexpected elevation (win was predicted → standard CDI)
             vs dramatic elevation (win was upset → extended CDI)

T+72h — DECAY ASSESSMENT:
  Purpose: Assess CDI trajectory and plan next pre-match window
  
  Checklist:
  □ Is elevation still above pre-match baseline by >5%?
    → YES: sustained signal — hold or add
    → NO: CDI expired or accelerated — reassess position
  □ Upcoming match scan: next high-FTIS event for this token?
  □ Update Memory MCP: CDI delivered vs CDI estimated
    → This data improves future CDI estimates
```

---

## Result-type commercial modifiers

These extend `core/core-result-impact-matrices.md` with the timing architecture.

```
WIN (expected — predicted by pre-match signal):
  Immediate impact (T+0 to T+2h): +3-8% typical
  T+2h signal: ENTER if SMS ≥ 60 and macro clear
  CDI: Standard (see fan-token/fan-sentiment-intelligence/ for sport-specific values)
  Galaxy Score expected: +8-15 points
  Decay pattern: steady; half-life ~1-2 days (standard win)

WIN (unexpected — pre-match signal was WAIT or predicted AWAY):
  Immediate impact (T+0 to T+2h): +8-18% typical (upset premium)
  T+2h signal: ENTER — upset creates stronger and longer commercial window
  CDI: Extended (×1.3-1.5 vs standard win)
  Galaxy Score expected: +15-25 points (high social volume)
  Decay pattern: fast initial spike, plateau, then standard decay
  
  NARRATIVE NOTE:
    Upset win creates narrative that standard win does not.
    "PSG beat Arsenal despite pre-match WAIT signal" = media story.
    Media story = CDI extension (see core/media-intelligence.md velocity model).

LOSS (expected):
  Immediate impact (T+0 to T+2h): -2-8% typical
  T+2h signal: WAIT — wait for stabilisation window (T+24h minimum)
  CDI: Negative CDI — commercial suppression window, not commercial opportunity
  Galaxy Score expected: -5-12 points
  
  WHEN TO CONSIDER ENTERING POST-LOSS:
    Only after: (a) full CDI negative window has elapsed AND (b) next fixture
    creates new positive signal AND (c) Galaxy Score has recovered to pre-loss baseline

LOSS (unexpected — pre-match signal was ENTER or predicted HOME win):
  Immediate impact (T+0 to T+2h): -8-18% typical
  T+2h signal: ABSTAIN — unexpected loss requires full signal reassessment
  
  MANDATORY POST-UNEXPECTED-LOSS CHECKLIST:
  □ Was this a data quality issue? (lineup wrong, injury not captured)
  □ Was this a model gap? (new opponent tactic not in domain skill)
  □ Was this within normal variance? (SMS 65, 35% chance of wrong direction)
  □ Update calibration record — unexpected losses are the most valuable records

DRAW (in sport where draws are rare):
  Treat as minor loss signal for betting-adjacent tokens
  Treat as neutral for fan tokens in sports where draws are expected (football league)
  
  SPORT-SPECIFIC DRAW HANDLING:
    Football (league): draw common → minimal commercial impact
    Football (cup/knockout): draw forces replay/extra time → neutral to slight negative
    Rugby: draw very rare → significant narrative signal regardless of pre-match expectations

DOMINANT WIN (e.g. 5-0, 4-0 football; shutout NHL; UCL winning margin ≥3):
  Apply dominant_win_multiplier (×1.20-1.35 on standard win CDI)
  Galaxy Score spike typically +20-35 points
  Smart wallet activity expected: monitor S2 signal (address intelligence)
  NCSI amplification: dominant win amplifies ATM player spillover by ×1.15-1.25
```

---

---

## Loss-effect asymmetry — empirical finding

**Source: Ante, Schellinger & Demir (2024), intraday event study, 8 fan tokens / 325 matches.
Synthesised in Zhou et al. (2026), *Frontiers in Psychiatry* thematic review.**

Fan token markets do not respond symmetrically to wins and losses.

```
EMPIRICAL FINDING:
  Fan token returns decline on average −0.8% DURING matches
  Fan token returns decline a further −0.7% POST-MATCH
  
  LOSS EFFECT (asymmetry): losses trigger larger negative market reactions
  than wins create positive reactions.
  
  IMPLICATION: The market prices in expected wins partially in advance
  (pre-match narrative, lineup confirmation, form) — so a confirmed WIN
  is less surprising than a LOSS. A loss is a greater information shock.

AGENT CALIBRATION RULES:

  POST-WIN SIGNAL:
    Expected WIN (pre-match direction was HOME/AWAY, confirmed): 
      Market reaction is MODERATE — partly priced in
      Apply standard win modifier
      CDI extension: standard window
      
    Unexpected WIN (pre-match said WAIT or opposite direction):
      Market reaction is ELEVATED — genuine information shock
      Apply upset premium modifier (see result-type modifiers above)
      CDI extension: extended window
      
  POST-LOSS SIGNAL:
    Expected LOSS (pre-match predicted this outcome):
      Market reaction is STILL SIGNIFICANT — loss effect > win effect
      Apply loss modifier at FULL strength (not discounted for being expected)
      CDI compression begins immediately
      
    Unexpected LOSS (pre-match said ENTER or predicted WIN):
      Market reaction is SEVERE — maximum information shock
      Apply full loss modifier + unexpected_loss_premium
      LTUI trajectory: immediate downgrade review
      
  PATH_2 INTERACTION:
    PATH_2 LOSS = supply-neutral (pre-liquidated amount minted back)
    But market sentiment reaction is NOT neutral
    On-chain supply is restored; off-chain price still reflects loss sentiment
    Agent rule: PATH_2 LOSS → supply-neutral signal + loss_sentiment_discount
    These are TWO SEPARATE SIGNALS — do not conflate

PRACTICAL IMPLICATION:
  Do not assume a draw is symmetric between win and loss for sentiment.
  Research shows the baseline return drift is already −0.8% during matches.
  A DRAW produces less negative sentiment than a LOSS but is not neutral
  relative to the pre-match expectation of a WIN.
  
  Recommended: apply draw_disappointment_discount = 0.92 if pre-match
  signal was ENTER (investor expected a win, DRAW is a negative surprise).
  If pre-match was WAIT, draw_modifier = 1.00 (no expectation violated).
```

## Post-match NCSI calculation

```
IMMEDIATE NCSI CALCULATION (T+2h):

Step 1: Identify ATM players who participated in the match
  Source: official match stats (FBref for football, UFC Stats for MMA, etc.)
  
Step 2: Assess performance tier
  DOMINANT: goals/assists + man of match + >7.5 rating = Tier 1 NCSI
  GOOD: contributed to win + positive rating = Tier 2 NCSI
  AVERAGE: played, no standout contribution = Tier 3 NCSI
  POOR: played, negative impact = negative NCSI applied

Step 3: Apply ATM multiplier
  Use ATM value from fan-token/football-token-intelligence/ for football
  For other sports: use sport-specific ATM equivalent

Step 4: Apply competition amplifier
  UCL match: ×1.00 base
  World Cup match: ×3.5-4.0 (see world-cup-2026-intelligence/)
  Standard league: ×0.65

Step 5: Calculate club token impact
  club_token_impact = ATM × performance_tier × competition_amplifier
  Apply to fan-token-pulse HAS baseline

EXAMPLE:
  Player scores hat-trick in UCL quarter-final (ATM 0.35):
    Performance tier: DOMINANT (Tier 1 NCSI)
    Competition amplifier: ×1.00 (UCL)
    Impact: 0.35 × 1.00 × 1.0 = 0.35
    Commercial modifier: +12-18% on club token T+2h
```

---

## Post-match calibration record generation

```
EVERY MATCH IS A CALIBRATION OPPORTUNITY.

Standard workflow:
  1. Before match: generate pre-match signal → save to memory
     {direction, sms, adjusted_score, modifiers_applied, flags}
  
  2. After match: record actual outcome
     {result, direction_correct, actual_token_movement, unexpected_factors}
  
  3. Calculate calibration value:
     direction_correct = (pre_match_direction == actual_result_direction)
  
  4. Identify what to calibrate:
     If wrong AND unexpected: flag for modifier review
     If wrong AND expected (close game): normal variance, note only
     If right AND dramatic: positive calibration confirmation

SUBMITTING AS COMMUNITY RECORD:
  See: community/calibration-data/CONTRIBUTING.md
  Format: core/calibration-framework.md
  Value: wrong predictions are AS VALUABLE as correct ones
  Priority: records for WC2026, modifiers with <10 records, new sports
```

---

## Post-match agent sequence

```
RECOMMENDED SEQUENCE (applies within 4h of result):

1. sportmind_verifiable_source(query_type="match_result", sport=...)
   → Confirm result from Tier 1 source

2. Wait T+2h from final whistle before generating commercial signal

3. sportmind_macro()
   → Macro conditions may have changed since pre-match analysis

4. sportmind_sentiment_snapshot(token=..., use_case=...)
   → Check if composite signal has shifted

5. [Optional] LunarCrushConnector.get_token_galaxy_score(ticker)
   → Observe Galaxy Score change vs pre-match baseline

6. [Optional] ChilizAddressIntelligence.get_transfer_velocity(contract)
   → Check on-chain reaction (velocity spike = strong reaction)

7. Apply result-type commercial modifier (this file)

8. Update Memory MCP:
   → signal_history: add post-match result + outcome
   → dsm_history: no change unless new disciplinary event post-match
   → upcoming_events: refresh next fixture date

9. Generate post-match commercial signal for T+2h to T+24h window

10. Schedule next analysis:
    → T+24h: CDI confirmation check
    → T+72h: decay assessment
    → Next pre-match T-48h: standard pre-match chain
```

---

## Integration with SportMind skills

```
FEEDS INTO:
  fan-token/fan-sentiment-intelligence/   → CDI calculation inputs
  fan-token/fan-token-pulse/              → HAS update post-result
  fan-token/on-chain-event-intelligence/  → smart wallet post-match behaviour
  core/core-narrative-momentum.md         → post-win narrative signal
  core/core-result-impact-matrices.md     → base result impact values

USES:
  core/verifiable-sources-by-sport.md     → Tier 1 result confirmation
  platform/memory-integration.md          → storing and retrieving result history
  platform/social-intelligence-connector.md → Galaxy Score post-match check
  platform/chiliz-chain-address-intelligence.md → on-chain reaction measurement
  community/calibration-data/             → contributing post-match records
```

---

*SportMind v3.43 · MIT License · sportmind.dev*
*See also: core/core-result-impact-matrices.md · fan-token/fan-sentiment-intelligence/*
*platform/memory-integration.md · community/calibration-data/CONTRIBUTING.md*
