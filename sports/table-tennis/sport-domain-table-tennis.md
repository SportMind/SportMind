# Table Tennis — SportMind Domain Skill

**Status: BASIC** — Core signal framework established. Seeking calibration records.
See GOOD_FIRST_ISSUES.md to contribute additional modifiers or records.

---

## Overview

Table tennis has the world's largest active participant base (est. 875M). China has
dominated the sport for 40+ years — Men's and Women's World Rankings are Chinese-majority
at the top. The ITTF World Tour and WTT (World Table Tennis) circuit provides year-round
competition. Germany (Bundesliga clubs), Korea, Japan, and Sweden have strong non-Chinese
traditions. No current Chiliz tokens, but WTT's aggressive commercial expansion (backed
by ITTF and with digital fan product development) makes table tennis a plausible target.

---

## Primary signal variable

**Chinese dominance adjustment** — When non-Chinese players face Chinese players at
Tier 1 events, the baseline signal requires a Chinese dominance discount:
Top-5 Chinese player vs Top-10 non-Chinese: apply × 0.70 base probability for non-Chinese.
This is not a bias — it reflects 40 years of empirical tournament outcomes.

---

## Event tier system

| Tier | Competition | Signal weight |
|---|---|---|
| 1 | Olympic Games (final) | Maximum |
| 1 | ITTF World Championships (final) | Near-maximum |
| 2 | WTT Champions events | High |
| 2 | Olympic Games (group / earlier rounds) | High |
| 3 | WTT Contender / Star Contender | Moderate |
| 4 | WTT Feeder events | Low |

---

## Key risk variables

```
CHINESE TEAM COMPOSITION CHANGE: Any Chinese selection committee decision
  (players rotate at tournaments) creates uncertainty at Tier 1 events.
  Monitor: CTTA (Chinese Table Tennis Association) selection announcements.

EQUIPMENT RULE CHANGES: ITTF equipment regulation changes (ball size, rubber)
  historically create competitive disruption. Any rule change announcement:
  apply × 0.85 to form-based signals for 3 months post-change.

PLAYING STYLE MATCHUP: Blocker vs attacker, pen-hold vs shake-hand — these
  matchup variables produce more variance than ranking differential.
  H2H at the specific event level is more predictive than season rankings.

MIXED DOUBLES: Highest variance event at Olympic level. Do not apply high-
  confidence signals to mixed doubles without strong H2H data.
```

---


## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal behaviour |
|---|---|---|
| WTT Contender events | Jan–Mar | Tier 3 — lower signal |
| WTT Champions events | Apr–Jun, Sept–Oct | Tier 2 high signal |
| World Table Tennis Championships | Apr/May (biennial) | Tier 1 near-maximum |
| WTT Finals | Nov–Dec | Tier 2 high — season culmination |
| Olympic Games | Every 4 years | Tier 1 maximum |

**Rule:** Chinese selection rotation (CTTA chooses which players represent China at each event) creates uncertainty even at top events. Always check CTTA selection announcement before applying pre-match signal.

### Result Impact Matrix

| Result scenario | Token / market impact |
|---|---|
| Olympic title (non-Chinese) | +20–35% (historic signal — extremely rare) |
| Olympic title (Chinese) | +5–10% (expected; lower surprise value) |
| World Championship title | +8–15% national token potential |
| Equipment rule change announcement | −10–15% on form-based predictions (90-day disruption) |
| Top-3 Chinese player upset loss | +15–25% (winner's nation if token exists) |

---

## Event Playbooks

### Playbook 1: Olympic Table Tennis Final — Non-Chinese Finalist
```
trigger:  Olympic TT final with non-Chinese finalist (rare — major signal event)
entry:    T-4h; verify player form, H2H specifically at this event
exit:     T+72h (extended — historic signal requires longer CDI window)
filter:   Macro gate; note: this is a narrative event as much as a sporting event
sizing:   Full Tier 1 with ×1.20 narrative multiplier (underdog vs China narrative)
note:     Check CTTA selection — if China sent second-tier players, reduce signal
```

### Playbook 2: CTTA Selection Announcement
```
trigger:  Official CTTA announcement of players for Worlds or Olympics
entry:    Immediate assessment on announcement
exit:     Next major event
filter:   Tier 1 source only (CTTA official, Xinhua Sport)
sizing:   Informs pre-event H2H probabilities; not a position event itself
note:     If top-3 Chinese player absent: apply ×0.88 to China's win probability
```

### Playbook 3: WTT Champions Final
```
trigger:  WTT Champions event final (Tier 2 high)
entry:    T-2h; confirm matchup and H2H specifically at WTT level
exit:     T+24h
filter:   Standard pre-match checks
sizing:   Tier 2 sizing — 0.65× vs Tier 1 Olympic
note:     WTT digital platform = most likely future token integration point; monitor
```

### Playbook 4: Equipment Rule Change Response
```
trigger:  ITTF announces equipment/ball rule change (official announcement)
entry:    Immediate — apply 90-day disruption modifier
exit:     After 90 days or 3 major events post-change (whichever first)
filter:   Verify via ITTF official communications only (Tier 1)
sizing:   Apply ×0.85 to all form-based signals during disruption window
note:     Equipment changes historically produce 2–3 unexpected results at major events
```

---

## Signal Weight Adjustments

For table tennis, agents should apply these weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 55% | Individual sport; Chinese dominance factor is primary variable |
| Social sentiment | 12% | Limited global social engagement outside China/Japan/Korea |
| Price trend | 13% | No direct TT tokens; routing via potential future WTT token |
| Market / whale flows | 8% | Minimal institutional involvement currently |
| Macro | 12% | Higher macro weight — Chinese market sensitivity to CHZ state |

---

## Key Commands

| Action | Skill | Command | Use case |
|---|---|---|---|
| Pre-match signal | `core/sportmind-score.md` | SMS calculation | With Chinese dominance adjustment |
| Breaking news | `core/breaking-news-intelligence.md` | Category 2 | CTTA selection, equipment rule |
| Macro gate | `macro/macro-crypto-market-cycles.md` | Macro state | Before any major event |
| H2H framework | `core/historical-intelligence-framework.md` | H2H decay | TT H2H is more predictive than rankings |

---

## Data Sources

- Rankings and draws: [worldtabletennis.com](https://worldtabletennis.com/) — WTT official
- CTTA selection: Xinhua Sport, China Table Tennis Association official (Tier 1)
- Live results: ITTF MyTournament, FlashScore (Tier 2)
- Equipment rules: [ittf.com](https://www.ittf.com/) official rule database

---

## Fan token commercial potential

```
HIGHEST POTENTIAL TOKENS:
  WTT (World Table Tennis): WTT has an existing fan engagement platform and
    digital product roadmap. A WTT × Chiliz partnership is commercially logical.
  Germany: Bundesliga team model (clubs like TTC Neu-Ulm, Borussia Düsseldorf)
    mirrors football token model. German fan governance culture = Governor-ready.
  Japan: T-League professional circuit; strong domestic digital engagement culture.
  
COMMERCIAL NOTE: Table tennis has the largest global participant base of any
  Olympic sport. The barrier to fan token adoption is awareness, not fan culture.
  Any table tennis federation or WTT partnership announcement = monitor for
  first-mover signal. Demographic profile: young, global, digital — ideal token base.
```

---

## Agent Reasoning Prompts

- "Olympic table tennis final — non-Chinese finalist: major signal event. Apply ×0.70 base."
- "Fan token announcement from WTT or any national federation: Phase 1 lifecycle protocol."
- "ITTF equipment rule change: apply ×0.85 to all form signals for 90 days."

---

## Compatibility

**Core frameworks:** `core/sportmind-score.md` · `core/athlete-modifier-system.md`
**Market:** `market/market-table-tennis.md`

---

*SportMind v3.86.0 · MIT License · sportmind.dev*
