---
name: referee-pool-depth
description: >
  Deep competition-specific referee pool profiles for competitions with active fan
  token clubs. Extends core/referee-pool-intelligence.md with pool size, selection
  methodology, card rate data, home bias statistics, and the six-step referee pool
  reasoning chain. Covers UCL, Premier League, Bundesliga, La Liga, Serie A, Ligue 1,
  and cross-competition confidence weight table.
---

# Referee Pool — Deep Profiles

**Extends `core/referee-pool-intelligence.md` with deeper competition-specific data.**
Individual tendencies must always be assessed within pool context.
Load this file together with `core/referee-intelligence.md`.

---

## UCL referee pool — deep profile

```
SELECTION: UEFA Elite category only.
  Nationality rotation strictly enforced.
  No referee from same country as either competing club.
  Pool size: approximately 20 Elite referees active per UCL season.
  Each official: 4-6 UCL matches per season.

CARD RATE:
  UCL yellow card rate 12% below equivalent domestic matches.
  Referees allow more physical contact in UCL vs domestic.
  Apply: ×0.88 to card-based modifier signals in UCL context.

ADVANTAGE PLAY:
  UCL referees prefer playing advantage over stopping play.
  Apply: ×0.92 reduction to any modifier based on defensive foul frequency.

CROWD PRESSURE:
  Elite referees manage crowd pressure more effectively than domestic officials.
  Apply: ×0.92 to crowd pressure home advantage modifier.

UCL FINAL SPECIFIC:
  Most experienced Elite referee not from either finalist's nation,
  who has not officiated a major final in the last 2 seasons.
  Extra conservative officiating standard — career-defining match.
  Apply: ×0.97 to card threshold (referees more cautious in finals).

CONFIDENCE WEIGHT: ×1.00
```

---

## Premier League referee pool — deep profile

```
POOL STRUCTURE:
  14 Select Group 1 referees — full-time professional officials.
  380 matches per season. Algorithm-based PGMOL rotation assignment.
  High familiarity between referees and clubs across a full season.

CARD RATE:
  Higher than UCL — one of the highest in European top-flight leagues.
  Interventionist style — referees stop play more readily.

HOME PENALTY BIAS:
  Statistically verified: home team receives approximately 15% more
  penalty decisions than away teams in Premier League.
  This is a pool-level structural tendency — not individual referee bias.
  Apply: ×1.03 home team advantage modifier specific to penalty/foul decisions.

LATE MATCH CARD RATE:
  Card rate increases in final 20 minutes.
  Fatigue, desperation, and crowd noise combine.
  If match is close in final 20 minutes: apply ×1.08 to card probability.

HIGH PRESS MATCHES:
  More fouls called in first 15 minutes of high-press tactical matches.
  Apply: ×1.05 to early foul probability in matches where both teams press.

CONFIDENCE WEIGHT: ×1.00
```

---

## Bundesliga referee pool — deep profile

```
POOL STRUCTURE:
  24 DFB Elite referees. Fittest referees in Europe by documented standards.
  Annual fitness and sprint tests required for pool membership.

FITNESS ADVANTAGE:
  Fewer late-match errors than PL — fitness reduces fatigue-related decisions.
  Apply: no late-match card amplifier (unlike PL above).

ADVANTAGE PLAY:
  Above-average advantage calls — referees allow play to continue.
  Apply: ×0.95 to foul frequency modifiers.

VAR RECORD:
  Lowest error rate in VAR review of any major European league.
  Bundesliga adopted VAR in 2017/18 — longest track record.
  VAR overturns fewer correct calls than any other major league.
  Apply: ×1.00 confidence to VAR-related outcome predictions.

CONFIDENCE WEIGHT: ×1.00
```

---

## La Liga referee pool — deep profile

```
POOL STRUCTURE:
  18 Primera División referees. RFEF oversight.

CARD RATE:
  Highest card rate of major European leagues.
  Apply: ×1.10 to card probability modifiers vs European average baseline.

SIMULATION CALLING:
  Inconsistent simulation (diving) detection — varies significantly
  by individual referee. Individual tendency profiling is more important
  than pool average for La Liga.
  Rule: apply individual file at full weight before pool context for La Liga.

EL CLÁSICO PROTOCOL:
  RFEF deliberately appoints conservative, experienced referees for El Clásico.
  Apply: ×0.95 confidence to card predictions specifically for El Clásico.
  Historical pattern: card rate in El Clásico is below La Liga average.

CONFIDENCE WEIGHT: ×0.95
```

---

## Serie A referee pool — deep profile

```
POOL STRUCTURE:
  20 AIA (Associazione Italiana Arbitri) referees. FIGC oversight.
  VAR since 2017/18 — alongside Bundesliga as early adopters.

HISTORICAL CONTEXT:
  Historically highest controversy rate of major European leagues.
  VAR has improved consistency materially since 2017/18.
  Individual variance remains higher than PL or Bundesliga.

OFFSIDE CALLS:
  Italian VAR culture is particularly rigorous on offside.
  Offside calls reversed by VAR more common in Serie A than other leagues.
  Apply: ×1.05 to offside-related prediction uncertainty.

CONFIDENCE WEIGHT: ×0.95
  Slightly reduced due to higher individual variance and historical controversy.
```

---

## Ligue 1 referee pool — deep profile

```
POOL STRUCTURE:
  20 FFF (Fédération Française de Football) referees.
  Fewest UEFA Elite appointments of any major European league.

HOME ADVANTAGE:
  Higher home team advantage in decisions than European average.
  Apply: ×1.10 to home advantage modifier versus European average baseline.
  (vs PL where home advantage is ×1.03 specific to penalties — Ligue 1 is broader)

DATA LIMITATION:
  Fewer independently validated individual tendency profiles than other leagues.
  Lower international profile means less external analysis available.
  Apply: ×0.85 confidence weight to all Ligue 1 individual referee tendency signals.

CONFIDENCE WEIGHT: ×0.85
```

---

## Cross-competition confidence weights

```
COMPETITION               CONFIDENCE WEIGHT
UCL:                      ×1.00
Premier League:           ×1.00
Bundesliga:               ×1.00
La Liga:                  ×0.95
Serie A:                  ×0.95
Ligue 1:                  ×0.85
MLS:                      ×0.80
Lower tier domestic:      ×0.75
International (FIFA):     ×0.90 — neutral pool, variable data per referee
International (UEFA):     ×0.95 — quality standard, smaller per-referee sample
Asian competitions:       ×0.85

INDIVIDUAL VS POOL WEIGHTING (when they conflict):
  Individual tendency:    ×0.60 weight
  Pool average:           ×0.40 weight
  Individual tendency wins — pool context provides floor/ceiling constraints only.
```

---

## REASONING CHAIN — REFEREE POOL

```
STEP 1 — Identify competition:
  Load confidence weight from the table above.

STEP 2 — Load individual referee profile:
  From core/referee-intelligence.md.
  Apply individual tendency with ×0.60 weight.

STEP 3 — Apply pool context:
  Card rate, advantage play, crowd pressure reduction, home advantage.
  Apply pool characteristics with ×0.40 weight.

STEP 4 — Stack with match context:
  Final or major derby: apply ×0.97 to card threshold.
  High-press match: apply early foul probability modifier.
  Close match in final 20 minutes (PL): apply ×1.08 late card modifier.

STEP 5 — Multiply by competition confidence weight:
  All referee modifiers × competition confidence weight from table.

STEP 6 — Integrate into adjusted score stack:
  Referee is a Level 3 standard modifier.
  Apply after macro and athlete intelligence.
  Referee modifier is never the lead signal — it refines, not drives.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches the specific characteristics of each competition's referee pool — card rates, advantage play tendency, crowd pressure response, home team bias — as calibrated modifier inputs for six major competitions.

**Reasoning:** Provides the six-step referee pool reasoning chain from competition identification through individual/pool weighting to adjusted score integration.

**Context:** Applies to every fixture where a referee appointment is known — competition context determines which pool profile and confidence weight apply. Crossing competition tiers requires applying the lower confidence weight.

**Memory:** Draws on documented pool statistics across multiple seasons — PL home penalty rate (15% bias) and UCL card rate reduction (12%) are empirically established patterns with multi-season evidence base.

**Judgment:** Do not apply individual tendency modifiers from a previous domestic season when the referee is operating in a different competition tier — pool context changes with competition. Apply the lower confidence weight when any uncertainty exists about pool assignment.

**Attention:** Referee pool intelligence is a Level 3 standard modifier — it should not dominate the analysis. Macro and athlete intelligence take priority. Referee is the final modifier in the stack, not the lead signal.

**Learning:** Pool characteristics should be updated when multiple calibration records from the same competition reveal systematic deviations from documented pool behaviour. Card rate and home bias tendency should be reviewed after each calibration cycle.

**Integration:** Referee pool integrates simultaneously with psychological intelligence (crowd pressure), venue intelligence (neutral vs home), and athlete intelligence (tactical fouls, card accumulation). All four interact — load them together and apply compound modifiers.

---

## Compatibility

**Pool overview:**          `core/referee-pool-intelligence.md`
**Individual profiles:**    `core/referee-intelligence.md`
**Psychological:**          `core/psychological-intelligence.md`
**Venue intelligence:**     `core/venue-intelligence.md`
**Signal confidence:**      `core/signal-confidence-framework.md`

---

*SportMind v3.97.73 · MIT License · sportmind.dev*
*Individual tendency ×0.60 weight | Pool average ×0.40 weight. Individual wins.*
*Referee is Level 3 — it refines the analysis, it does not drive it.*
