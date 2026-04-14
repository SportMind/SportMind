---
name: tournament-elimination-intelligence
description: >
  Intelligence framework for the commercial and FTP supply impact when a
  team is eliminated from a competition — particularly UEFA Champions League
  and major cup competitions where FTP PATH_2 is active. Covers three
  elimination scenarios: group stage exit, knockout round exit, and final
  defeat. Quantifies the projected supply reduction that will NOT happen
  (cancelled burn events), the NCSI collapse, the LTUI trajectory reset,
  and the correct agent classification of each event. Includes second-leg
  aggregate score context — Arsenal vs Sporting UCL QF Leg 2 (aggregate
  1-0) is the canonical worked example. Critical for any agent monitoring
  a fan token for a club with an active FTP PATH_2 path through a cup
  competition. Distinct from core/cup-competition-intelligence.md (which
  covers on-pitch signal mechanics) — this skill covers the commercial
  and supply cascade that follows elimination.
---

# Tournament Elimination Intelligence — SportMind

**When a team is eliminated from a competition, the on-pitch result is one
signal. The commercial cascade is a different, larger signal that agents
must reason about separately.**

For standard fan tokens, elimination is a negative CDI event. For tokens
with an active FTP PATH_2, elimination has a permanent supply trajectory
impact — all future WIN burn events in that competition are cancelled.
This skill models both.

---

## The elimination cascade

```
WHEN A TEAM IS ELIMINATED FROM A COMPETITION:

  1. IMMEDIATE (T+0 to T+60 min):
     Standard loss result impact applies (see core/core-result-impact-matrices.md)
     CDI negative event fires
     For Leg 2 two-legged ties: aggregate score determines whether
       this is actually an elimination or just a loss

  2. COMPETITION CALENDAR COLLAPSE (T+60 min onwards):
     All future matches in this competition are removed from the calendar
     Each cancelled match = one less WIN burn opportunity (FTP PATH_2)
     Each cancelled match = one less NCSI amplification event
     The competition tier weight is permanently removed from the season forecast

  3. LTUI TRAJECTORY RESET:
     LTUI was forecasted on the assumption of continued competition
     Elimination triggers a downward revision to the LTUI trajectory
     Severity depends on: how many rounds remain, competition tier, PATH_2 status

  4. AGENT ACTION:
     Do not classify as a single-event signal
     Classify as CALENDAR_COLLAPSE — a structural change to the season outlook
     Apply revised LTUI trajectory going forward
     Flag: COMPETITION_EXIT_[COMPETITION_NAME]
```

---

## Arsenal vs Sporting — UCL QF Leg 2 (canonical example)

```
MATCH CONTEXT:
  Arsenal (home) vs Sporting CP (away)
  UEFA Champions League Quarter-Final — Leg 2 of 2
  Aggregate: Arsenal 1–0 up going into Leg 2
  Venue: Emirates Stadium, London
  FTP PATH_2: active for $AFC

AGGREGATE SCORE RULES (critical for agent classification):
  Arsenal need: WIN or DRAW → advance to semi-finals
  Arsenal eliminated if: LOSE by 2+ goals (Sporting win aggregate 2-1+)
  Arsenal eliminated if: LOSE by 1 goal (1-1 aggregate) → extra time → penalties

SCENARIO A — ARSENAL WIN OR DRAW (advance, aggregate ≥ 1-0):
  Signal: Standard WIN or DRAW result
  FTP PATH_2: WIN = burn event fires at full-time. DRAW = no burn (loss in previous rounds)
  Agent action: HOLD pre-match, re-assess at full-time
  NCSI: UCL semi-final path confirmed — competition weight maintained

SCENARIO B — ARSENAL LOSE (e.g. 1-0 to Sporting, aggregate 1-1):
  Extra time / penalties required
  FTP: no supply change until 90 minutes confirmed result
  Signal: uncertain — hold until extra time result

SCENARIO C — ARSENAL ELIMINATED (e.g. lose 2-0, Sporting win 2-1 aggregate):
  Immediate: standard loss CDI event fires
  Then: CALENDAR_COLLAPSE triggers

CALENDAR COLLAPSE CALCULATION for $AFC in UCL:
  Remaining UCL matches if Arsenal reach semi-final:  ~2–3 more matches
  PATH_2 burns per UCL WIN:                           ~0.24% circulating supply
  Projected burns now cancelled:                      0.48–0.72% supply reduction lost
  That lost reduction is permanent — it will never happen in this season

  NCSI impact:
    UCL QF weight ×0.75 (knockout)
    UCL SF weight ×0.88 (semi-final)
    UCL Final weight ×1.00
    All of these events are now cancelled
    Season NCSI forecast drops materially

  LTUI revision:
    Pre-elimination LTUI trajectory: Phase 2 (rising, UCL run)
    Post-elimination: Phase 3 (plateau, domestic competition only)
    LTUI trajectory resets to domestic-only outlook

  TOKEN SIGNAL POST-ELIMINATION:
    T+0 to T+4 hours:   emotional sell pressure (sentiment-driven)
    T+4 to T+48 hours:  rational reassessment (domestic league position re-evaluated)
    T+48h onwards:      new baseline established (domestic-only LTUI)

  $AFC AGENT RULE — ELIMINATION NIGHT:
    Do NOT apply the single-event loss modifier and stop there
    Load full CALENDAR_COLLAPSE assessment
    Revise season supply trajectory
    If domestic league form remains strong: partial LTUI recovery possible
    Arsenal in a title race = significant LTUI offset to UCL elimination
```

---

## Elimination by competition type and round

```
UCL GROUP STAGE EXIT:
  Remaining cancelled matches: 3–4 per season (group stage remainder)
  + entire knockout round path
  PATH_2 burn events lost: 4–6 (conservative estimate for deep run)
  NCSI impact: HIGH — UCL is the highest commercial tier
  Typical token impact: -8 to -15% vs pre-tournament baseline
  Recovery driver: EL/ECL qualification (partial NCSI offset)

UCL ROUND OF 16 EXIT:
  Remaining cancelled matches: QF + SF + Final = up to 5 matches
  PATH_2 burn events lost: 2–4 (based on expected win rate in remaining rounds)
  NCSI impact: HIGH
  Typical token impact: -6 to -12%
  Recovery driver: domestic league position

UCL QUARTER-FINAL EXIT (Arsenal/Sporting scenario):
  Remaining cancelled: SF (1 match) + Final (1 match) = up to 2 matches
  PATH_2 burn events lost: 1–2 burns (0.24–0.48% supply reduction lost)
  NCSI impact: MEDIUM-HIGH — QF is a premium window
  Typical token impact: -4 to -8%
  Recovery driver: domestic title race, EL/ECL consolation if applicable

UCL SEMI-FINAL EXIT:
  Remaining cancelled: Final only = 1 match
  PATH_2 burn events lost: 0–1 (one final burn opportunity lost)
  NCSI impact: MEDIUM — semi-final run already delivered most commercial value
  Typical token impact: -2 to -5%
  Recovery driver: runner-up narrative, next season UCL seeding

UCL FINAL DEFEAT:
  No cancelled matches — entire run completed
  PATH_2: all burn events fired throughout the run
  NCSI: full tournament NCSI delivered
  Token impact: negative CDI for defeat but not CALENDAR_COLLAPSE
  Special classification: FINAL_DEFEAT — separate from elimination
  Narrative: runner-up for season narrative arc (see core/core-narrative-momentum.md)

DOMESTIC CUP EXIT:
  Impact depends on PATH_2 status — most domestic cups are not UCL-tier
  FA Cup: lower NCSI weight; token impact typically -2 to -4%
  Copa del Rey / DFB-Pokal: similar range
  EFL Cup: minimal token impact for UCL-tier clubs
```

---

## Two-legged tie classification rules

```
AGENT CLASSIFICATION — SECOND LEG RESULTS:

RULE 1: Always check aggregate before classifying an elimination
  A loss in Leg 2 is NOT automatically an elimination
  Arsenal lose 1-0 in Leg 2 + led 1-0 from Leg 1 = ADVANCE (0-0 aggregate tie)
  Arsenal lose 2-0 in Leg 2 + led 1-0 from Leg 1 = ELIMINATED (Sporting win 2-1)

RULE 2: Extra time / penalty scenario
  1-1 aggregate after 90 min → UNCERTAIN until extra time / penalties conclude
  Do not apply CALENDAR_COLLAPSE until result is confirmed at full-time
  Apply: RESULT_UNCERTAIN flag; wait for confirmation

RULE 3: Away goals rule (note: removed from UEFA competitions 2021)
  Away goals rule NO LONGER APPLIES in UEFA competitions
  Aggregate tied after 90 min → extra time regardless of away goals
  Legacy documents may reference away goals — do not apply to current UEFA matches

RULE 4: Pre-match second-leg context
  Leg 2 pre-match signal must incorporate:
    Current aggregate score
    Arsenal leading: priority = AVOID LOSING by 2+
    Arsenal trailing: must score AND not concede
  Load: core/cup-competition-intelligence.md for second-leg tactical framework
  TMAS may shift based on tactical approach (defending lead vs attacking deficit)
```

---

## Output schema

```json
{
  "elimination_brief": {
    "club":          "Arsenal",
    "token":         "AFC",
    "competition":   "UEFA Champions League",
    "round":         "Quarter-Final",
    "result":        "ELIMINATED",
    "aggregate":     "Sporting CP 2-1 Arsenal"
  },

  "calendar_collapse": {
    "matches_cancelled":        2,
    "competition_flag":         "COMPETITION_EXIT_UCL",
    "path2_burns_lost":         1.5,
    "supply_reduction_lost_pct": 0.36,
    "ncsi_events_cancelled":    2
  },

  "ltui_revision": {
    "pre_elimination_trajectory": "RISING (UCL semi-final path)",
    "post_elimination_trajectory": "PLATEAU (domestic only)",
    "recovery_drivers": [
      "Arsenal 2nd in Premier League — title race active",
      "Europa League consolation path possible via UEFA coefficient"
    ]
  },

  "token_signal": {
    "immediate_t0_t4h":         "NEGATIVE CDI — emotional sell pressure",
    "medium_t4h_t48h":          "REASSESSMENT — domestic league re-priced",
    "new_baseline":             "Domestic-only LTUI trajectory",
    "recommended_action":       "WAIT",
    "sms":                      44
  },

  "plain_english": "Arsenal going out of the Champions League tonight is more than a bad result — it removes 1–2 future burn events from the PATH_2 supply schedule and collapses the UCL commercial calendar for the rest of the season. The token will likely sell off over the next few hours as the emotional reaction works through, then stabilise as the market re-prices around the Premier League position. If Arsenal are still in a title race, that significantly limits the downside.",

  "sportmind_version": "3.64.0"
}
```

---

*SportMind v3.64 · MIT License · sportmind.dev*
*See also: fan-token/gamified-tokenomics-intelligence/ · core/cup-competition-intelligence.md*
*core/core-result-impact-matrices.md · core/core-narrative-momentum.md*
*fan-token/fan-token-lifecycle/ · fan-token/football-token-intelligence/*
