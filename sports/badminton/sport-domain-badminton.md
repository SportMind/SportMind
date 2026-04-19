# Badminton — SportMind Domain Skill

**Status: BASIC** — Core signal framework established. Seeking calibration records.
See GOOD_FIRST_ISSUES.md to contribute additional modifiers or records.

---

## Overview

Badminton is the world's second-most played sport by participation (after football).
Dominant markets: China, Indonesia, Malaysia, South Korea, India, Denmark.
All World Badminton Federation (BWF) events are relevant; the Thomas Cup (men's teams)
and Uber Cup (women's teams) are the highest-value team competition signals.
No current fan tokens, but the Indonesian market specifically
($PERSIB, $PRSJ are already there) suggests national badminton federation tokens
are commercially plausible — particularly for Indonesia, Malaysia, and India.

---

## Primary signal variable

**Ranking differential and head-to-head** — BWF World Rankings are highly predictive
at Tier 1 events. Top-10 vs top-10 matches are the highest signal events.
The All England Open is the sport's most prestigious tournament outside major championships.

---

## Event tier system

| Tier | Competition | Signal weight |
|---|---|---|
| 1 | Olympic Games (final) | Maximum |
| 1 | BWF World Championships (final) | Near-maximum |
| 2 | Thomas/Uber Cup Final | High |
| 2 | BWF Super 1000 events (All England, Indonesia Open) | High |
| 3 | BWF Super 750/500 events | Moderate |
| 4 | BWF Super 300 events | Low |

---

## Key risk variables

```
INJURY TO RACKET ARM: Wrist, shoulder, elbow injuries are career-defining in badminton.
  Any injury report to a top-10 player: apply × 0.78 to their expected performance.

HOME ADVANTAGE: Very strong in Indonesia and China — crowd intimidation effect real.
  Indonesia Open, China Open: apply × 1.20 home court advantage.

FATIGUE (TOURNAMENT COMPRESSION): BWF Super Series events are consecutive — travel
  and recovery are primary injury risk factors. 3+ events in 5 weeks: × 0.90.

DOUBLES SPECIALIST RISK: Mixed doubles and doubles events are highest variance.
  Do not apply heavy signals to doubles formats without specific pair H2H data.
```

---


## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal behaviour |
|---|---|---|
| BWF Super 1000 circuit | Jan–Nov | Tier 2 high events distributed year-round |
| Thomas/Uber Cup | May (biennial, even years) | Tier 2 high — team competition |
| World Championships | Aug (annual) | Tier 1 near-maximum |
| Olympic Games | Every 4 years (summer) | Tier 1 maximum |
| All England Open | Mar | Premier Tier 2 event — highest prestige outside majors |

**Rule:** Badminton is a year-round sport. Signal quality peaks at All England, Thomas/Uber Cup, Worlds, and Olympics. BWF 300-level events carry base signal only.

### Result Impact Matrix

| Result scenario | Token / market impact |
|---|---|
| Olympic final win | +15–25% (national token, if exists) |
| World Championship title | +10–18% |
| Top-3 ranked player injury | −10–20% (athlete token potential) |
| Indonesia Open win (home favourite) | +8–14% |
| Upset of world No.1 | +12–18% (winner's nation token) |

---

## Event Playbooks

### Playbook 1: Olympic Badminton Final
```
trigger:  Olympic badminton final — nation with token representation
entry:    T-4h; verify player fitness; check H2H at this tournament level
exit:     T+48h
filter:   Macro gate; MRS check
sizing:   Full Tier 1 (no badminton tokens currently — NCSI-only route)
note:     Current relevance is NCSI via $PERSIB/$PRSJ for Indonesian matches
```

### Playbook 2: Indonesia Open — Home Nation Signal
```
trigger:  BWF Super 1000 Indonesia Open (Tier 2 high + ×1.20 home advantage)
entry:    T-2h; verify Indonesian squad health
exit:     T+36h
filter:   Indonesian holder sentiment check; $PERSIB/$PRSJ HAS baseline
sizing:   Tier 2 with ×1.20 home court modifier applied
note:     Indonesian badminton results have documented $PERSIB/$PRSJ NCSI effect
```

### Playbook 3: World No.1 Injury
```
trigger:  Confirmed injury to current world No.1 (any gender) before Worlds/Olympics
entry:    Immediate Category 2 breaking news protocol
exit:     Until return confirmed
filter:   Verify via BWF official or national federation (Tier 1 only)
sizing:   Apply ×0.78 to injured player's expected performance across all analyses
note:     Racket arm injuries: wrist/shoulder/elbow — these are career-length events
```

### Playbook 4: Thomas/Uber Cup Final (Team Format)
```
trigger:  Thomas Cup (men) or Uber Cup (women) final
entry:    T-3h; confirm team lineups; check key singles player availability
exit:     T+24h
filter:   Standard pre-match
sizing:   Tier 2 high — comparable to World Championships knockout round
note:     Indonesia vs China final = maximum badminton commercial signal
```

---

## Signal Weight Adjustments

For badminton, agents should apply these weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 50% | Individual sport — player performance dominant |
| Social sentiment | 18% | Strong in Indonesia/Malaysia; moderate elsewhere |
| Price trend | 12% | No direct badminton tokens; NCSI routing only |
| Market / whale flows | 10% | Low institutional involvement |
| Macro | 10% | Standard CHZ macro applies |

---

## Key Commands

| Action | Skill | Command | Use case |
|---|---|---|---|
| NCSI for Indonesian matches | `fan-token/football-token-intelligence/` | NCSI calculation | $PERSIB/$PRSJ Indonesian sport NCSI |
| Squad availability | `core/pre-match-squad-intelligence.md` | Squad assembly | Player fitness check |
| Breaking news response | `core/breaking-news-intelligence.md` | Category 2 | Injury or withdrawal |
| Macro gate | `macro/macro-crypto-market-cycles.md` | Macro state | Before major events |

---

## Data Sources

- Rankings and draws: [bwfbadminton.com](https://bwfbadminton.com/)
- Player news: National federation sites — PBSI (Indonesia), BAM (Malaysia), BWF (Tier 1)
- Live scores: BWF Tournament Software, FlashScore (Tier 2)
- Indonesian club news: Liga Badminton Indonesia official channels

---

## Fan token commercial potential

```
HIGHEST POTENTIAL TOKENS:
  Indonesia: Largest badminton fan base globally. PBSI (Indonesian federation) = credible
             token issuer. Indonesian market already proven via $PERSIB/$PRSJ.
  Malaysia: National sport level cultural significance. BAM federation known nationally.
  India: Saina Nehwal / PV Sindhu = athlete-token precursors. Growing market.
  China: Highest player quality but restricted digital asset market.
  Denmark: Strongest European market; Viktor Axelsen cultural significance.

ATHLETE TOKEN POTENTIAL (individual):
  Viktor Axelsen (Denmark), PV Sindhu (India), Chen Yufei (China) — all have the
  global profile for individual athlete fan tokens if the regulatory environment allows.
```

---

## Agent Reasoning Prompts

- "Indonesia Open final: apply × 1.20 home advantage; load this file."
- "Top-5 vs Top-5 Olympic final: maximum signal. Full analysis chain."
- "Wrist injury rumour for world No. 2: Category 2 breaking news. Apply × 0.78."

---

## Compatibility

**Core frameworks:** `core/sportmind-score.md` · `core/athlete-modifier-system.md`
**Market:** `market/market-badminton.md`

---

*SportMind v3.86.0 · MIT License · sportmind.dev*
