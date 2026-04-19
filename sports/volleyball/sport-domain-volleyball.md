# Volleyball — SportMind Domain Skill

**Status: BASIC** — Core signal framework established. Seeking calibration records.
See GOOD_FIRST_ISSUES.md to contribute additional modifiers or records.

---

## Overview

Volleyball is an Olympic-cycle sport with a significant year-round professional circuit
(FIVB World League/Nations League, club competitions). Brazil, Italy, Poland, and Japan
have the deepest fan cultures and strongest potential for fan token ecosystems.
No current Chiliz fan tokens — but the demographic profile (young, global, digital) makes
volleyball a plausible future token sport, particularly for national federation tokens.

---

## Primary signal variable

**Team momentum and set-momentum** — volleyball is a high-variance sport within matches
(sets can swing 25-0 to 25-23). Pre-match signal is primarily based on team form and
head-to-head at this competition level. Single set results are NOT sufficient signal — only
match outcomes drive reliable signals.

---

## Event tier system

| Tier | Competition | Signal weight |
|---|---|---|
| 1 | Olympic Games (final) | Maximum |
| 1 | World Championship (final) | Near-maximum |
| 2 | Olympic Games (QF/SF) | High |
| 2 | FIVB Nations League Final | High |
| 3 | FIVB Nations League group | Moderate |
| 3 | European Championship | Moderate |
| 4 | Club competitions (CEV Champions League) | Low-moderate |

---

## Key risk variables

```
HOME ADVANTAGE: Strong in volleyball — crowd noise disrupts serve receive.
  Apply × 1.12 home advantage at major indoor arenas.

SETTER AVAILABILITY: Setter is the most position-critical player in volleyball.
  If starting setter unavailable: apply × 0.82 to signal confidence.

LIBERO AVAILABILITY: Second-most critical position. Absence = defensive fragility.
  If starting libero unavailable: apply × 0.90 to signal confidence.

FATIGUE: Volleyball tournaments (Olympics, World Championships) use compressed schedules.
  3+ matches in 4 days: apply × 0.93 to form-based signals.

ACE/BLOCK SPECIALIST: If opponent has a dominant service ace specialist:
  Apply × 0.88 to expected performance of reception-dependent teams.
```

---


## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal behaviour |
|---|---|---|
| Club season (European) | Sept–May | CEV Champions League Tier 4 signal active |
| FIVB Nations League | May–July | Tier 3 pool play; finals = Tier 2 |
| World Championships | Biennial (odd years) | Tier 1 near-maximum |
| Olympic Games | Every 4 years | Tier 1 maximum |
| Off-season | Aug–Sept | No meaningful signal |

**Rule:** Only Olympic and World Championship knockout matches warrant full signal chain analysis. Pool play requires base signal only.

### Result Impact Matrix

| Result scenario | Token / market impact |
|---|---|
| Olympic final win | +18–28% (national token) |
| World Championship final win | +12–20% |
| Olympic group exit (favourite) | −10–18% |
| Upset win over top-3 ranked team | +8–14% |
| Star player injury (setter) | −12–18% |

---

## Event Playbooks

### Playbook 1: Olympic Volleyball Final
```
trigger:  Olympic final confirmed — both nations have token exposure (direct or NCSI)
entry:    T-6h; load squad availability; confirm setter/libero status
exit:     T+48h post-match
filter:   MRS check; DeFi liquidity check for any relevant tokens
sizing:   Full position — Tier 1 event
note:     Setter absence = apply ×0.82 before any signal calculation
```

### Playbook 2: World Championship Final Entry
```
trigger:  World Championship knockout stage QF onwards
entry:    T-4h; verify squad; check home nation advantage if applicable
exit:     T+36h
filter:   Macro state check; CHZ macro gate
sizing:   0.85× of standard Tier 1 (World Champs < Olympics in holder response)
note:     If defending champion enters: apply ×1.08 narrative modifier
```

### Playbook 3: FIVB Nations League Final
```
trigger:  Nations League final (Tier 2 event)
entry:    T-2h; squad confirmation
exit:     T+24h
filter:   Standard pre-match checks
sizing:   Tier 2 sizing (0.65× vs Tier 1)
note:     Nations League carries less CDI extension than Olympic/WC events
```

### Playbook 4: Star Player Injury (Setter/Libero)
```
trigger:  Confirmed injury to starting setter or libero before major event
entry:    Immediate — Category 2 breaking news protocol
exit:     Until squad replacement confirmed; re-evaluate
filter:   Verify via official team announcement (Tier 1 source only)
sizing:   Reduce position; apply ×0.82 (setter) or ×0.90 (libero) modifier
note:     Warm-up injuries carry same weight as training camp injuries
```

---

## Signal Weight Adjustments

For volleyball, agents should apply these weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 45% | Match results and squad events dominate |
| Social sentiment | 20% | Volleyball has moderate social engagement; less than football |
| Price trend | 15% | Low liquidity in most volleyball-adjacent tokens |
| Market / whale flows | 10% | Limited institutional participation currently |
| Macro | 10% | CHZ macro applies to any Chiliz tokens |

---

## Key Commands

| Action | Skill | Command | Use case |
|---|---|---|---|
| Pre-match signal | `fan-token/football-token-intelligence/` | `sportmind_pre_match` | Adapt FTIS framework to volleyball tier |
| Squad check | `core/pre-match-squad-intelligence.md` | Squad assembly workflow | Setter/libero availability at T-2h |
| Breaking news | `core/breaking-news-intelligence.md` | Category 2 protocol | Injury response |
| Macro gate | `macro/macro-crypto-market-cycles.md` | Macro state check | Before any major match |

---

## Data Sources

- Match results and standings: [volleyballworld.com](https://en.volleyballworld.com/)
- Squad/injury news: Official national federation sites (Tier 1)
- FIVB rankings: [fivb.com/en/volleyball/rankings](https://www.fivb.com/)
- Live scores: FlashScore, SofaScore (Tier 2)

---

## Fan token commercial potential

```
HIGHEST POTENTIAL NATIONAL TOKENS:
  Brazil: Largest volleyball fan base globally; CBV (Brazilian Volleyball Confederation)
          already uses digital fan products. $BRA volleyball token = plausible.
  Italy: Strongest European volleyball market; SuperLega club culture.
  Poland: Reigning world champions (men); passionate national following.
  Japan: Strong domestic market; V.League professional circuit.

MONITORING: fantokens.com for any volleyball federation/club announcements.
Signal on launch: apply standard Phase 1 lifecycle protocol.
```

---

## Agent Reasoning Prompts

- "Olympic volleyball final: load this file + core/pre-match-squad-intelligence.md"
- "Setter injury in warm-up: apply × 0.82 modifier immediately. Category 2 breaking news."
- "Brazil vs Italy pool play: moderate signal. Reserve full analysis for knockout stage."

---

## Compatibility

**Core frameworks:** `core/sportmind-score.md` · `core/athlete-modifier-system.md`
**Market:** `market/market-volleyball.md`

---

*SportMind v3.86.0 · MIT License · sportmind.dev*
