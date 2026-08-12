---
name: football-[home-slug]-vs-[away-slug]-[competition-slug]-[YYYY-MM-DD]
status: COMPLETE — post-match verified
contributor: [Name or handle, e.g. Internal submission · @AltcoinDaddy]
contributor-type: INTERNAL
# contributor-type: EXTERNAL for community submissions
issue: n/a — internal calibration record
# issue: [GitHub issue number] for external contributions
description: >
  Pre-match calibration record for [COMPETITION] · [ROUND].
  [HOME] v [AWAY]. [VENUE], [CITY]. [DATE].
  Signal generated [DATE TIME UTC]. MCP server v[X.X.X].
  Library v[X.X.X]. CHZ [REGIME] [MODIFIER] active.
  [SINGLE-TOKEN / DUAL-TOKEN] record.
  Direction: [HOME/AWAY/DRAW]. Result: [SCORE]. Direction [CORRECT ✓ / INCORRECT ❌]. [GATE NOTE if applicable]. Record [N].
---

# Calibration Record — [COMPETITION] · [ROUND]
## [HOME] v [AWAY] · [DATE]

---

## Match details

```
Match:        [Home team] v [Away team]
Competition:  [Full competition name] — [Round / Stage]
Season:       [YYYY or YYYY/YY]
Venue:        [Venue name] · [City] · [Country]
Venue type:   HOME / AWAY / NEUTRAL / SHARED / TEMPORARY
              [Add note for shared/neutral: e.g. "neither club's home ground"]
Date:         [YYYY-MM-DD]
Kickoff UTC:  [YYYY-MM-DDTHH:MM:00Z]
Kickoff BST:  [YYYY-MM-DD HH:MM BST]
Fan tokens:   Home — $[TOKEN] ([Club] · [Chain] · verified ✓)  OR  null
              Away — $[TOKEN] ([Club] · [Chain] · verified ✓)  OR  no fan token
Token type:   SINGLE-TOKEN / DUAL-TOKEN
              [Note if single-token: "no dual-token modifier applicable"]
Submitted by: [Internal submission / @handle]
Recorded at:  [YYYY-MM-DD HH:MM UTC]
Series:       [e.g. Libertadores Last 16 · August 2026]  OR  n/a

# OPTIONAL — national tokens in PTG-eligible tournaments only
PTG status:   N/A  OR  [ACTIVE — $[TOKEN] Burn to Glory participant]
BTG burn rate: [N/A]  OR  [Current round burn rate: X%]
```

---

## Pre-match signal

*Generated: [DATE TIME UTC] · MCP server v[X.X.X] · Library v[X.X.X]*

```
DIRECTION:          [HOME / AWAY / DRAW]
RAW SCORE:          [0.0–100.0]
CHZ MODIFIER:       [CAPITULATION ×0.70 / ANXIETY ×1.00 / BULL ×1.15]
ADJUSTED SCORE:     [RAW × MODIFIER, e.g. 38.5]
CONFIDENCE:         [HIGH / MEDIUM / LOW]
ACTION:             [ENTER / HOLD] ([reason if HOLD, e.g. CHZ regime gate applied])
SMS:                [0–100] · [HIGH_QUALITY / GOOD / PARTIAL / INSUFFICIENT] · [N/5 layers loaded]
MACRO MODIFIER:     [NEUTRAL ×1.0 / etc.]
COMPOSITE MODIFIER: [×X.XX e.g. ×0.70]

# OPTIONAL — for Finals and knockout rounds
OCCASION WEIGHT:    [×X.XX (e.g. ×2.00 UCL Final · ×1.60 UCL knockout)]

# OPTIONAL — for HOME fixtures with non-STANDARD venue tier
VENUE MODIFIER:     [FORTRESS +0.12 / STANDARD +0.06 / WEAKENED +0.02]

FLAGS:
  CHZ_CAPITULATION_ACTIVE:     [Include if CAPITULATION regime active]
  NEGATIVE_FORM_ARC:           [Include if home/away side on losing run]
  H2H_RECENCY_FLAG:            [Include if H2H recency signal material]
  LINEUP_CHECK_REQUIRED:       [Standard — manual check at T-2h]
  DSM_CHECK_REQUIRED:          [Standard — manual check pre-kickoff]
  NO_AWAY_TOKEN:               [Include for single-token records — away side]
  NO_HOME_TOKEN:               [Include for single-token records — home side]
  BRAZIL_REGULATORY_LOADED:    [Include if Brazilian club/holders involved]
  ITALY_REGULATORY_LOADED:     [Include if Italian club/holders involved]
  TURKEY_REGULATORY_LOADED:    [Include if Turkish club/holders involved]
  RUSSIA_ACCESS_RESTRICTION:   [Include if Russian holder segment relevant]
  PTG_NOT_APPLICABLE:          [Include for non-PTG competitions]
  PTG_ACTIVE:                  [Include for PTG-eligible tournaments — see section 7]
  PATH2_NOT_APPLICABLE:        [Include when $AFC not involved]
  PATH2_ACTIVE:                [Include for $AFC fixtures — see section 8]
  BTG_BURN_MOMENTUM:           [Include if token is on a PTG burn run]

PRE-MATCH NOTE:
  [2–4 sentences. Summarise: why this direction? What are the key uncertainties?
  What does the macro regime do to the signal? Any special mechanics active?
  Example: "Fluminense enter as home favourites at the Maracanã but carry a
  negative form arc and a credible H2H recency signal from Rivadavia's group-
  stage hold at the same venue. CHZ CAPITULATION ×0.70 active — adjusted score
  38.5, HOLD gate triggered."]
```

---

## Score derivation

```
Base score (SportMind pre-match):         [X.X]
[Macro modifier (NEUTRAL ×1.0)]:          ×1.00  → [X.X]
[CHZ CAPITULATION modifier (×0.70)]:      ×0.70  → [X.X]
[Occasion weight if applicable (×1.60)]:  ×1.60  → [X.X]
[Venue modifier if applicable (+0.06)]:   +0.06  → [X.X]
Composite modifier applied:               ×[X.XX]

Final adjusted score:                     [X.X]
ENTER threshold:                          [50.0 / state if different]
Threshold comparison:                     [X.X] [> or <] [threshold]

Action gate outcome:
  Raw direction signal: [ENTER / HOLD] ([DIRECTION])
  [CAPITULATION gate: ACTIVE — suppresses to HOLD]  [if applicable]
  Final action output: [ENTER / HOLD]
  Reason: [e.g. adjusted score X.X falls below ENTER threshold
           and CAPITULATION regime gate is non-negotiable]
```

---

## Primary signal drivers

```
DIRECTION CHOSEN: [HOME / AWAY / DRAW]

POSITIVE DRIVERS:
  · [Key reason 1 — e.g. home advantage · Maracanã venue · crowd factor]
  · [Key reason 2 — e.g. competition tier · knockout weight]
  · [Key reason 3 — e.g. quality gap · CDI gate · form momentum]
  [Add/remove as appropriate — minimum 2 positive drivers for HOME or AWAY call]

DAMPENERS / SIGNAL SUPPRESSORS:
  · [Suppressor 1 — e.g. NEGATIVE FORM ARC — X matches without win]
  · [Suppressor 2 — e.g. H2H RECENCY — away side held home side at this venue]
  · [Suppressor 3 — e.g. CHZ CAPITULATION ×0.70 — macro override; HOLD not ENTER]
  · [Suppressor 4 — e.g. SINGLE-TOKEN — no opposing signal to cross-reference]
  [Include at least the CHZ modifier as a suppressor whenever CAPITULATION is active]
```

---

## Signal layers applied

```
LAYER 1 — MACRO:
  CHZ regime: [CAPITULATION / ANXIETY / BULL]
  Modifier: [×0.70 / ×1.00 / ×1.15]
  Verdict: [HOLD gate triggered / ENTER eligible]

LAYER 2 — SPORT DOMAIN:
  File: sports/football/sport-domain-football.md
  Competition occasion weight: [×X.XX (e.g. ×1.30 Libertadores knockout)]
  Venue: [type · tier · capacity note]
  Venue modifier: [STANDARD +0.06 / FORTRESS +0.12 / WEAKENED +0.02]

LAYER 3 — FORM:
  [Home side] form: [POSITIVE / NEGATIVE / MIXED]
  [Recent record summary — e.g. last 5: 4W 1D]
  Form modifier: [POSITIVE / NEGATIVE / NEUTRAL] — [description]
  [Away side] form: [summary if relevant to signal]

LAYER 4 — H2H:
  H2H record: [summary of relevant meetings]
  Recency weight: [0.85 / 1.00 / etc.]
  H2H score: [HOME DOMINANCE / HOME LEAN / BALANCED / AWAY LEAN / AWAY DOMINANCE]
  H2H confidence tier: [LOW / MODERATE / HIGH / VERY HIGH]
  Gate: [PASS (N conditions met) / FAIL — state reason / INSUFFICIENT SAMPLE]

LAYER 5 — REGIME:
  [Regulatory file loaded if applicable — e.g. brazil.md · italy.md · turkey.md]
  [MP/Law reference if applicable]
  [Holder friction note]
  Regime output: [summary — e.g. CAPITULATION ×0.70 dominant; Brazil regulatory noted]

# OPTIONAL
LAYER 6 — CDI:
  [Include if CDI file exists for token]
  File: market/club-intelligence/[token].md
  CDI gate: [GROWTH / CONSOLIDATION / TRANSITION / EMERGING / DORMANT]
  Competition modifier: [note]

# OPTIONAL
LAYER 7 — REGULATORY:
  [Include if specific regulatory framework materially affects signal]
  [Note jurisdiction, law reference, holder friction modifier]
```

---

## PTG / Burn to Glory status

*[OPTIONAL SECTION — include for national tokens in PTG-eligible tournaments only.
Remove this section entirely for club tokens or non-PTG competitions.]*

```
PTG ROUND:          [Round of X · burn rate X%]
WINNER BURN:        [X% of $[TOKEN] treasury holdings burned permanently]
LOSER OUTCOME:      [PTG run ends · no burn · token continues without supply event]

$[TOKEN] BTG HISTORY (pre-match):
  [e.g. Group stage ×3 + R32 ×1 = 4 confirmed burns]
  [Tournament burn leader status if applicable]

RESULT:
  [$TOKEN burn #N triggered at X% rate]  OR  [Burn not triggered — team eliminated]
  [Advance to next round / Eliminated]
  Verify burn: chiliscan.com

CHZ REGIME INTERACTION:
  Burns execute regardless of CHZ macro regime.
  Demand signal suppressed [×X.XX] under [REGIME].
  Supply reduction is structural — price impact dampened by macro.
```

---

## FTP PATH_2 status

*[OPTIONAL SECTION — include only when PATH_2 is active. $AFC is the only confirmed
PATH_2 token. Remove this section entirely for all other tokens.]*

```
TOKEN:            $AFC (Arsenal Fan Token)
STATUS:           ACTIVE — Model 2 (Prediction Market / PATH_2)
PRE-LIQUIDATION:  [CONFIRMED at T-Xh / PENDING]
  $AFC: [amount confirmed / estimated]
  USDC: [amount confirmed / estimated]

SUPPLY EVENT TRIGGER:
  WIN (Arsenal):  $AFC tokens repurchased from market → burn/treasury split
  LOSS (Arsenal): $AFC tokens minted to treasury (supply increases)
  DRAW:           No supply event (PATH_2 settles on 90-minute result only)

RESULT:
  $AFC PATH_2 outcome: [WIN — burn triggered / LOSS — mint triggered / DRAW — no event]
  Tokens [burned / minted / unchanged]: [amount]
  Verify: fantokens.com/fan-token-play
```

---

## Pre-match engagement layer

*[OPTIONAL SECTION — include if Champion Call, Livestream Trading Battle,
or other demand mechanics are active in the pre-match window.]*

```
CHAMPION CALL:    [ACTIVE / NOT ACTIVE]
  [Description if active — e.g. "Champion Call active for $[TOKEN] — deadline [date]"]

LIVESTREAM TRADING BATTLE:
  [ACTIVE / NOT ACTIVE]
  [Description if active]

OTHER MECHANICS:
  [Any additional fan engagement or supply mechanics active pre-match]
```

---

## Result — verified

```
ACTUAL RESULT:    [Home team] [score] [Away team]
WINNING TEAM:     [Winner / None (draw)]
SCORE:            [X–Y (full time / AET)]
EXTRA TIME:       [YES / NO]
PENALTIES:        [YES — [Home] X–Y [Away] / NO]

DIRECTION CORRECT:    [YES — CORRECT ✓ / NO — INCORRECT ❌]
  SportMind predicted: [HOME / AWAY / DRAW]
  Actual result:       [outcome]
  Direction verdict:   [CORRECT / INCORRECT]

ACTION OUTCOME:       [ENTER — position taken / HOLD — gate behaviour CORRECT ✓]
  [Note if HOLD prevented an incorrect ENTER]

CALIBRATION VERDICT:  [CORRECT / INCORRECT] · [GATE BEHAVIOUR note if applicable]
```

---

## Supply event outcome

*[OPTIONAL SECTION — include when PTG burn or PATH_2 supply event was possible.
Remove if PTG N/A and PATH_2 N/A.]*

```
$[TOKEN] SUPPLY EVENT:
  Outcome: [BURN TRIGGERED / MINT TRIGGERED / NO EVENT / NOT APPLICABLE]
  [Burn number and rate for PTG: e.g. "Burn #5 at 2.5% R16 rate"]
  [Cumulative history: e.g. "5 confirmed burns — tournament burn leader"]
  Verify: chiliscan.com
```

---

## Post-match notes

```
MATCH CHARACTER:
  [2–5 sentences. Was it comfortable? Tight? Dramatic comeback? Set piece heavy?
  Describe how the match unfolded and what affected the result.
  Example: "Disciplined, low-scoring first leg. Rivadavia defended compactly and
  frustrated Fluminense throughout. The match never generated the attacking fluency
  a Maracanã home crowd expectation implies."]

WHAT THE SIGNAL GOT RIGHT:
  · [e.g. CAPITULATION gate correctly blocked ENTER on wrong call]
  · [e.g. H2H recency signal validated — away side held home side again]
  · [e.g. MEDIUM confidence appropriate — not HIGH]

WHAT THE SIGNAL GOT WRONG:
  · [e.g. Direction call HOME — result was DRAW]
  · [e.g. Home advantage slightly overstated given H2H and form dampeners]
  [Write "N/A — direction correct" if signal was correct on all counts]
```

---

## Signal quality note

```
CONFIDENCE CALIBRATION: [WELL-CALIBRATED ✓ / OVERCONFIDENT / UNDERCONFIDENT]

[2–4 sentences assessing confidence tier in retrospect.
  Was the tier appropriate for the uncertainty in this fixture?
  Example: "MEDIUM confidence was correct for this fixture context — 5-match
  negative form arc, H2H recency flag active, single-token record, CAPITULATION
  regime active. HIGH confidence would have been wrong."]

HOLD GATE ASSESSMENT: [WORKING AS DESIGNED ✓ / N/A — gate not triggered]
  [If HOLD was triggered: assess whether it was the correct outcome.]

FUTURE CALIBRATION NOTE:
  [1–3 sentences on what this record teaches for future calibrations of this
  token, competition, or signal context.
  Example: "For Copa Libertadores first-leg fixtures with H2H recency flags
  active, consider a modest draw probability premium for base score."]
```

---

## Flags resolved

```
FLAG: [FLAG_NAME]
  Pre-match status: [ACTIVE / PENDING / CONFIRMED]
  Post-match resolution: [How it resolved — e.g. VALIDATED · CONFIRMED · NOT TRIGGERED]

FLAG: [FLAG_NAME]
  Pre-match status: [status]
  Post-match resolution: [resolution]

[Repeat for every flag raised in Pre-Match Signal section]
[Minimum flags to resolve: CHZ regime · form arc if raised · H2H flag if raised ·
 LINEUP_CHECK · DSM_CHECK · TOKEN STATUS · PTG status · PATH_2 status]
```

---

## Agent rules engaged

```
TFM6 Gate 1:              Pre-kickoff submission ✓ ([HH:MM UTC] vs [HH:MM UTC] KO)
CHZ regime applied:       [REGIME] [MODIFIER] applied before output ✓
Token verified active:    $[TOKEN] verified on [Chain] before signal ✓
[Single/dual] token flag: Applied — [no dual-token modifier / dual-token amplification checked] ✓
No named players:         Record contains no named players ✓
[brazil.md loaded:]       Brazil regulatory context loaded ✓  [include if applicable]
[italy.md loaded:]        Italy regulatory context loaded ✓   [include if applicable]
[turkey.md loaded:]       Turkey regulatory context loaded ✓  [include if applicable]
[PTG N/A confirmed:]      [Competition] is not PTG-eligible ✓  [include if applicable]
[PTG verified:]           PTG burn verified on chiliscan.com ✓  [include if applicable]
[PATH_2 N/A confirmed:]   $[TOKEN] is not a PATH_2 token ($AFC only) ✓  [include if applicable]
[PATH_2 verified:]        PATH_2 supply event verified on fantokens.com/fan-token-play ✓
[HOLD gate:]              Triggered correctly under [REGIME] regime ✓  [include if applicable]
[H2H framework:]          Gate run — [PASS/FAIL] · [notes] ✓  [include if applicable]
[DSM checked:]            Disciplinary signal checked pre-kickoff ✓  [include if applicable]
[Lineup confirmed:]       Lineup confirmed at T-2h ✓  [include if applicable]
```

---

## Mind dimensions

| Dimension | Sub-dimension | Status |
|---|---|---|
| 2. Reasoning | 2b Probabilistic · 2d Temporal | ACTIVE |
| 6. Attention | 6a Signal Detection | ACTIVE |
| 8. Verification | 8a Source Tier Assessment | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration | ACTIVE |
| 12. Adaptation | 12a Regime Detection | ACTIVE |
| 14. Transparency | 14b Modifier Disclosure | ACTIVE |

*[Add additional rows for dimensions engaged beyond the core six.
  Common additions: 2c Multi-Signal (dual-token) · 3b Event Context (Finals/knockouts) ·
  5a Uncertainty Weighting (HOLD gate decisions) · 9c Pattern Reinforcement (series records)]*

---

## Source and verification

```
Signal source:    SportMind MCP · sportmind_pre_match
MCP server:       v[X.X.X]
Signal generated: [YYYY-MM-DD HH:MM UTC]
Library version:  v[X.X.X]
Match date:       [YYYY-MM-DD]
Kickoff:          [YYYY-MM-DD HH:MM UTC] / [HH:MM BST]
Submitted by:     [Internal submission / @handle]
Result source:    [e.g. CONMEBOL / FIFA.com / UEFA.com / ESPN — verified post-match]
Result verified:  [YYYY-MM-DD (post-match)]
Record number:    [N]

[PTG verification:    N/A]  OR  [chiliscan.com — $[TOKEN] burn #N confirmed]
[PATH_2 verification: N/A]  OR  [fantokens.com/fan-token-play — supply event confirmed]

NOTE — SINGLE TOKEN RECORD:  [Include if applicable]
  [Away/Home] side has no fan token.
  Direction signal applies to $[TOKEN] only.
  No opposing signal · no dual-token modifier applicable.
```

---

*SportMind v[X.X.X] · MIT License · sportmind.dev*
*STATUS: COMPLETE — direction [CORRECT ✓ / INCORRECT ❌] · [HOLD gate CORRECT ✓ if applicable] · Record [N]*
*[PTG: N/A]  OR  [$[TOKEN] burn #N triggered at X%]*
*[PATH_2: N/A]  OR  [$AFC PATH_2 — [outcome]]*

---

*Template produced Chat 8 · 2026-08-11*
*Synthesised from: UCL Final · WC2026 series (8 records) · $VASCO · $FLU*
*Use for all future football calibration records in community/calibration-data/football/*
*For calibration/2026/ records (WC · UCL only) adapt as needed*
