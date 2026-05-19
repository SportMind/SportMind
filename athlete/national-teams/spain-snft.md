---
name: spain-snft
description: >
  Spain national team ($SNFT) athlete intelligence reasoning framework.
  Covers tactical identity, position modifier weights by role, squad depth
  reasoning, World Cup 2026 context, long-term absence impact framework,
  and $SNFT fan token demand signal interaction. Enduring framework only —
  no named player current status, no injury logs, no specific return dates.
---

# Spain National Team ($SNFT) — Athlete Intelligence

**Enduring tactical identity, position modifiers, and squad depth reasoning.**

> No named player current status. No injury logs. No specific return dates.
> Q4 2026 used as outer reasoning horizon for extended absence modelling only.

---

## Tactical identity

```
SYSTEM: High possession, positional play, aggressive press off the ball
  Spain's national team identity is built on:
  · Technical superiority in midfield — the system's engine
  · Full-back involvement in build-up — not traditional wide defenders
  · Fluid positional interchanges — players are system-first, not role-fixed
  · Winning the ball high when pressed — press triggers are system-embedded

EUROPEAN CHAMPIONSHIP 2024: CONFIRMED WINNERS
  Pedigree signal: ×1.08 applied to $SNFT demand baseline.
  Spain have won 4 of the last 7 major tournaments — ingrained winning culture.
  This is an enduring multi-season trajectory signal — does not expire.
```

---

## Position modifier weights

```
MIDFIELD — HIGHEST MODIFIER POSITION:
  Spain's system is more midfield-dependent than most major national teams.
  The midfield controls tempo, triggers press, and connects defence to attack.

  Creative / progressive midfielder (8 role):
    Absence modifier: ×0.88 — system coherence significantly reduced
    This is Spain's highest single-position modifier.
    The 8 role in Spain's system carries both defensive and creative responsibility —
    no other position combines both at this weight.

  Defensive midfielder / anchor (6 role):
    Absence modifier: ×0.92
    Spain can adapt more easily here than at the 8 — multiple profiles fit.

  Box-to-box midfielder (second 8):
    Absence modifier: ×0.94
    Rotation and depth here is typically deeper than the creative 8.

ATTACK:
  Left forward / wide attacker:
    Absence modifier: ×0.92 — Spain's left side has historically been a primary
    attacking vector; right side is more rotation-tolerant.

  Right forward / wide attacker:
    Absence modifier: ×0.94

  Centre forward:
    Absence modifier: ×0.92
    Spain's system has functioned without a traditional striker — but the
    absence of the primary goal threat still requires tactical adaptation.

DEFENCE:
  Right back:
    Absence modifier: ×0.93 — Spain's right back carries significant attacking load
  Left back:
    Absence modifier: ×0.92 — historically Spain's most attacking fullback position
  Centre backs:
    Absence modifier: ×0.95 per CB — depth is historically strong
  Goalkeeper:
    Absence modifier: ×0.96 — depth is strong; less system-dependent than field positions
```

---

## Long-term absence reasoning framework

```
EXTENDED ABSENCE DEFINITION: 4+ months unavailable

  MIDFIELD KEY PLAYER (8 role) — EXTENDED ABSENCE:

  IMMEDIATE IMPACT (matches 1-5 without player):
    Apply: ×0.90 system coherence modifier
    Squad adaptation required — available options assessed for role fit.

  ADAPTATION PERIOD (matches 6-15):
    If adaptation solution identified: ×0.96 sustained (modified system)
    If no clear solution: ×0.91 sustained (ongoing coherence deficit)

  MULTI-COMPETITION IMPACT:
    Key midfield absence affects all competitions simultaneously.
    Apply ×0.88 squad depth modifier across full competition calendar.

  WORLD CUP 2026 SPECIFIC REASONING (Q4 2026 horizon):
    If player unavailable through Q4 2026 (outer reasoning horizon):
    World Cup squad inclusion probability: LOW
    Spain tactical adjustment required — position gap must be filled.
    Two adaptation paths:
      Path A: Like-for-like replacement (technical 8): system maintained
        → Apply ×0.96 Spain adjusted score (minor coherence loss)
      Path B: System adjustment (deeper block, wider press triggers):
        → Apply ×0.92 Spain adjusted score (structural adaptation)
    Agent cannot determine which path until squad announcement.
    Apply: ×0.94 uncertainty weight until Spain manager confirms approach.

  $SNFT DEMAND IMPACT OF KEY ABSENCE:
    Immediate: ×0.95 demand signal (uncertainty about World Cup performance)
    If Path A confirmed (strong replacement): ×0.98 (minimal impact)
    If Path B confirmed (system change): ×0.92 sustained
    World Cup participation itself maintains tournament demand premium —
    Spain's participation signal outweighs any single player absence.
    Apply ×1.20 World Cup participation baseline regardless of squad gaps.
```

---

## World Cup 2026 demand framework

```
WORLD CUP 2026 — $SNFT SIGNAL WEIGHTS:
  (Applies to all Spain national team token signals during tournament)

  Pre-tournament confirmed participation: ×1.20 demand baseline
  Favourable group draw:                  ×1.25
  Difficult group draw:                   ×1.15 (still positive — Spain favoured)
  Group stage win:                        ×1.05 per win (stacking to cap)
  Group stage exit:                       −35 to −45% — Spain always favoured
  Round of 16:                            ×1.15 baseline from this stage
  Quarter-final:                          ×1.25
  Semi-final:                             ×1.35
  Final:                                  ×1.50
  World Cup victory:                      ×1.80 to ×2.20

  DEFENDING EUROPEAN CHAMPION MODIFIER:
    Spain enter World Cup 2026 as reigning European champions.
    Apply: ×1.08 pedigree premium to all World Cup demand signals.
    This compounds with tournament progression signals.

  Spain HISTORICAL PEDIGREE:
    4 major tournament wins in 7 tournaments (2008-2024).
    Apply: sustained ×1.08 pedigree modifier to $SNFT demand baseline.
    This is a multi-season enduring signal — not contingent on current results.
```

---

## $SNFT demand signal framework

```
COMPETITION MODIFIERS (non-World Cup):
  Nations League:          ×1.08 (meaningful but below major tournament)
  Nations League Final:    ×1.20
  Friendly:                ×1.00 baseline — no significant modifier

SQUAD ANNOUNCEMENT SIGNALS:
  Full-strength squad confirmed:      ×1.05
  Key position gap confirmed:         ×0.94 (uncertainty about system adaptation)
  Surprise inclusion (young talent):  ×1.03 excitement signal
  Captain confirmed available:        ×1.02 leadership stability signal

DEMAND FLOOR:
  Spain's global fanbase and reigning European champion status provide
  structural demand floor.
  Apply minimum ×0.90 demand floor — Spain fan token cannot collapse
  regardless of squad absences.
```

---

## Compatibility

**Barcelona connection:**    `athlete/football/barcelona-bar.md`
**Coaching intelligence:**   `core/coaching-intelligence.md`
**Seasonal patterns:**       `core/seasonal-intelligence.md`
**$SNFT token:**             `fan-token/national-team-tokens.md`
**World Cup framework:**     `core/fan-token-reasoning-chains-extended.md` (Chain C)

---

*SportMind v3.97.61 · MIT License · sportmind.dev*
*Spain's creative 8 role carries the highest single-position modifier: ×0.88.*
*World Cup participation signal always outweighs any single player absence.*
