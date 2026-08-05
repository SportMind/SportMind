---
name: american-football-nfl
description: >
  NFL-specific sport domain intelligence framework. Covers season structure,
  QB dominance modifier, home field advantage, short-week performance, dome vs
  outdoor modifiers, bye week signal, salary cap intelligence, draft intelligence,
  and playoff format. Post-CLARITY Act the US is the largest addressable fan token
  market — NFL intelligence is strategically important.
---

# American Football — NFL Sport Domain Intelligence

**How to reason about NFL matches and signals for AI agent use cases.**
The NFL is the highest revenue sports league globally and the largest potential
fan token market post-CLARITY Act regulatory clarity.

---

## Season structure

```
REGULAR SEASON:
  18 weeks | September to January
  17 games per team | 32 teams total
  Conference structure: AFC and NFC, 4 divisions each

PLAYOFFS:
  Wild Card → Divisional → Championship → Super Bowl
  January to February
  Single elimination from Wild Card onwards

SUPER BOWL:
  Highest single-event viewership in US sports.
  Signal weight: ×2.50 — highest of any single event in SportMind.
  For any future NFL fan tokens: Super Bowl = equivalent of UCL Final
    for European football tokens — maximum single event demand spike.
```

---

## Core match modifiers

```
HOME FIELD ADVANTAGE:
  NFL has the highest documented home field advantage in major team sports.
  Home team wins approximately 57% of regular season games.
  Apply: ×1.08 home advantage modifier.
  (Compare: Premier League ×1.04 | NBA ×1.06)
  Rationale: crowd noise creates false start penalties, affects QB communication.

QUARTERBACK DOMINANCE:
  QB is the highest single-position impact role in team sports globally.
  Starting QB absent (season-ending injury or suspension):
    Apply: ×0.72 — highest position absence modifier in SportMind.
  Backup QB starting (known, game-experience):
    Apply: ×0.78
  Third-string QB or emergency starter:
    Apply: ×0.65
  Rationale: no other position in any other sport has this asymmetric impact.
  The gap between a franchise QB and backup is larger than any other sport.

SHORT WEEK — THURSDAY NIGHT FOOTBALL:
  Teams playing on 4 days rest (Thursday Night Football).
  Apply: ×0.94 to both teams.
  Teams travelling across time zones for TNF specifically:
    Apply: ×0.91 to the travelling team.

DOME vs OUTDOOR CONDITIONS:
  Teams based in domes playing outdoor in cold weather:
    Apply: ×0.93 to dome-based visiting team.
  Outdoor cold weather teams playing at home in winter:
    Apply: ×1.04 — structural advantage, acclimatised.
  Below freezing conditions (confirmed forecast):
    Dome-based visiting team: ×0.94 additional modifier (stacks with above).

BYE WEEK ADVANTAGE:
  Team coming off bye week (extra preparation, full rest):
    Apply: ×1.04.
  Week after a bye, opponent is not rested: baseline.
```

---

## Salary cap intelligence

```
SALARY CAP CONTEXT:
  NFL hard salary cap creates unique squad-building constraints.
  Unlike European football transfers, NFL cap management is a primary
  competitive signal — not secondary.

SIGNIFICANT CAP SPACE:
  Teams entering summer with substantial cap space:
    Squad upgrade probability HIGH.
    Positive signal for future fan token commercial trajectory.

AT CAP CEILING:
  Teams at or above cap ceiling:
    Squad maintenance only — no significant additions possible.
    Neutral-to-negative CDI signal.

DEAD CAP SIGNAL:
  Dead cap = money owed to released players counting against current cap.
  Dead cap above 15% of total cap:
    Apply: ×0.94 to squad quality modifier.
    Rationale: team is structurally constrained by past decisions.

FRANCHISE TAG:
  Player placed on franchise tag = club values player, cannot afford long-term deal.
  Signals: negotiation ongoing, player may be unhappy.
  Apply: ×1.10 departure probability modifier for following offseason.
```

---

## Draft intelligence

```
NFL DRAFT CONTEXT:
  Primary squad-building mechanism — unlike European football where transfers dominate.
  7 rounds. Top picks receive 4-year rookie contracts (team-controlled).

TOP 5 DRAFT PICK:
  Generational talent signal.
  For future NFL fan tokens: franchise QB prospect = highest long-term demand driver.
  Apply: ×1.15 to 3-year trajectory signal.

HIGH DRAFT POSITION (top 10):
  High pick = poor previous season = squad rebuild phase.
  Apply: ×0.92 to current season performance modifier.
  Apply: ×1.08 to 3-year trajectory (squad building, not immediate return).

LATE DRAFT SELECTION (rounds 4-7):
  Depth players. Individually minimal signal.
  Multiple late-round picks from a position group: depth being rebuilt.

TRADE UP IN DRAFT:
  Club sacrifices future picks to move up: signals urgency.
  Usually for a specific player — if QB, maximum positive trajectory signal.
```

---

## Playoff format intelligence

```
SINGLE ELIMINATION:
  From Wild Card onwards — one bad game ends the season.
  Variance much higher than league football playoff formats.
  Apply: ×1.15 uncertainty modifier to all NFL playoff predictions.

SEEDING SIGNAL:
  #1 seed in each conference: bye week in Wild Card round.
  Apply: ×1.06 performance modifier for #1 seeds in Divisional.
  Extra rest advantage is measurable in NFL playoffs.

HOME FIELD THROUGH PLAYOFFS:
  #1 and #2 seeds host all games until Super Bowl (neutral site).
  Home field in playoffs: ×1.10 (elevated from regular season ×1.08).
  Crowd noise at championship round level is materially higher.

SUPER BOWL (neutral site):
  No home field advantage.
  Return to base modifiers only — no venue premium.
  Signal weight: ×2.50 event modifier for any connected fan token signals.
```

---

## Fan token pipeline context

```
NO NFL FAN TOKENS CURRENTLY CONFIRMED ON CHILIZ CHAIN (as of library compilation).

US FAN TOKEN MARKET CONTEXT:
  Post-CLARITY Act regulatory clarity makes the US the largest addressable
  fan token market.
  NFL franchises represent the highest commercial value sports organisations
  in the world — Dallas Cowboys, New England Patriots, Los Angeles Rams etc.
  exceed the commercial value of most European football clubs.

WHEN NFL FAN TOKENS LAUNCH — apply:
  US regulatory framework from macro/macro-regulatory-sportfi.md
  First mover premium: ×1.30 CDI (largest market, no competition)
  Super Bowl signal: ×2.50 (highest single event modifier in SportMind)
  Quarterback-centric demand: key QB news has higher CDI impact than any
    other position-based signal in any other sport

PIPELINE SIGNAL MONITORING:
  Monitor: Socios.com partnership announcements with NFL franchises.
  Monitor: CLARITY Act implementation and its effect on fan token legality.
  See: fan-token/emerging-sports-pipeline.md
```

---

## Compatibility

**Market intelligence:**   `market/market-american-football.md`
**Sport tiers:**           `core/sport-tiers.md`
**Salary cap reference:**  `core/financial-sustainability-intelligence.md`
**Emerging pipeline:**     `fan-token/emerging-sports-pipeline.md`
**CLARITY Act:**           `macro/clarity-act-complete-framework.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | NFL-specific signal playbook: salary cap, injury designation system, and draft intelligence |
| Reasoning | ACTIVE | NFL reasoning chain with injury designation integration and playoff probability |
| Context | ACTIVE | NFL context: AFC/NFC conference, Wild Card vs Division seeds, bye week advantages |
| Memory | ACTIVE | Historical NFL outcome patterns and injury designation accuracy baselines |
| Judgment | ACTIVE | Judgment on NFL injury designation materiality — Doubtful vs Questionable differ significantly |
| Attention | ACTIVE | Elevated attention for Friday/Saturday practice reports — final designation indicators |
| Communication | ACTIVE | NFL signal output with designation history, playoff context, and modifier |
| Verification | ACTIVE | NFL injury reports from official NFL.com release — beat reporter observations Tier 2 |
| Learning | ACTIVE | NFL injury designation calibration: historical designation-to-actual-play accuracy rates |
| Integration | ACTIVE | Integrates with injury-intel-nfl.md and fan-token/nfl-token-intelligence/ |
| Calibration | ACTIVE | NFL injury designation accuracy calibrated — most structured injury signal in library |
| Adaptation | ACTIVE | NFL intelligence adapts as salary cap rules and playoff formats evolve |
| Ethics | NOT APPLICABLE | NFL sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | NFL injury designation source and historical accuracy explicit in output |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |


---

*SportMind v3.97.71 · MIT License · sportmind.dev*
*QB absence modifier ×0.72 is the highest single-position modifier in SportMind.*
*Super Bowl signal weight ×2.50 is the highest single event weight in SportMind.*
