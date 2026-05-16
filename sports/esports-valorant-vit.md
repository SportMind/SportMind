---
name: esports-valorant-vit
description: >
  Valorant-specific intelligence framework using Team Vitality as the reference
  organisation. Covers VCT league structure, Valorant-specific modifiers, dual-title
  demand framework, annual demand cycle, and roster intelligence. Enduring reasoning
  framework applicable to any future Valorant organisation fan token on Chiliz or
  compatible chains. $VIT partnership is currently INACTIVE — see token status block.
---

# Valorant Intelligence Framework — Team Vitality Reference Model

> ⚠️ NOTE: The $VIT (Team Vitality) partnership with Chiliz is no longer active
> as of library compilation. This file provides the enduring Valorant intelligence
> reasoning framework using Vitality as the reference organisation.
> The framework applies to any future Valorant organisation fan token that
> launches on Chiliz or any compatible chain.
> Token status will be updated when the verified fan token registry is complete —
> see `fan-token/registry/complete-registry.md` when available.

---

## Token status

```
$VIT — Team Vitality
  Partnership:      INACTIVE
  On-chain status:  Legacy contract only
  Signal use:       Do not treat as active demand signal
  Framework use:    Reasoning framework is valid for any active Valorant token

$NAVI — Natus Vincere
  Partnership:      INACTIVE
  On-chain status:  Legacy contract only
  Signal use:       Do not treat as active demand signal
  Previously flagged in: sports/esports-cs2.md
```

---

## VCT structure and league framework

```
VCT EMEA LEAGUE — FRANCHISED STRUCTURE:
  Team Vitality competes in VCT EMEA — one of three international franchised leagues.
  Franchised structure means:
    No relegation risk — permanent slot
    Stable roster environment
    Predictable competitive calendar
  Franchised stability modifier: ×1.05 to demand baseline
    versus equivalent non-franchised organisation

VCT EMEA SEASON SIGNAL WEIGHTS:
  Regular split season:               ×1.00 baseline
  Playoff stage:                      ×1.20
  EMEA Champions qualification:       ×1.35

VCT MASTERS (international — two per season):
  EMEA representative qualification:  ×1.50
  Strong performance:                 demand amplifier
  Early elimination:                  demand suppressor

VCT CHAMPIONS (world championship — October/November):
  Highest Valorant prestige event.
  Qualification signal weight:        ×1.80
  Deep run (semi-final+):             ×2.00+
```

---

## Valorant-specific modifiers

```
IGL (IN-GAME LEADER) ROLE:
  Valorant is more tactically dependent on the IGL than CS2.
  IGL absence modifier: ×0.84
  (versus ×0.87 for CS2 AWPer absence)

AGENT POOL FLEXIBILITY:
  Teams with wider agent pools (ability to run multiple compositions)
  have structural strategic advantage.
  Wide pool confirmed: ×1.05 demand baseline

MAP POOL SIGNAL:
  Valorant has a rotating map pool updated each act.
  Favourable map veto confirmed: ×1.04 signal weight

PATCH INTERACTION:
  Valorant patches can shift agent viability, economy mechanics, and map geometry.
  Apply standard fresh patch uncertainty modifier:
  Within 7 days of major patch release: ×0.85 confidence weight on all signals
```

---

## Dual-title demand framework

```
VITALITY IS A DUAL-TITLE ORGANISATION: CS2 + Valorant.
Any active dual-title fan token covers both performance streams.

  BOTH TITLES PERFORMING WELL:
    Compound positive: ×1.12 versus single-title equivalent

  ONE PERFORMING WELL, ONE UNDERPERFORMING:
    Partial offset — apply the stronger signal at ×0.75 weight
    Net effect: muted positive or muted negative

  BOTH TITLES UNDERPERFORMING:
    Compound negative: ×0.88 versus single-title equivalent

  CS2 MAJOR + VALORANT MASTERS CALENDAR OVERLAP (rare):
    Apply peak demand signal for the higher-prestige event
    Apply ×1.05 additional for dual-title calendar alignment
```

---

## Annual demand cycle reference

```
JANUARY — VCT EMEA split begins:
  Demand building: ×1.08

MARCH-APRIL — VCT Masters 1:
  EMEA qualification confirmed: ×1.20
  EMEA elimination:             ×0.95

JUNE — CS2 Major season:
  CS2 Major performance layer adds demand signal
  See: sports/esports-cs2.md for CS2 Major modifier framework

AUGUST — VCT EMEA split 2:
  Holds or builds depending on first-half performance

SEPTEMBER — CS2 Major 2:
  Second Major demand layer

OCTOBER-NOVEMBER — VCT Champions:
  Qualification confirmed:    ×1.35
  Deep run (quarter-final+):  ×1.50
  Victory:                    ×1.70 to ×2.00

DECEMBER — Off-season:
  Roster change signals dominate
  New marquee signing:  ×1.10 (2-3 week demand premium)
  Star player departure: ×0.85
```

---

## Roster intelligence framework

```
STAR PLAYER DEPARTURE MODIFIERS:
  CS2 star player departure:          ×0.80
  Valorant IGL departure:             ×0.82
  Coach departure (either title):     ×0.94
  New marquee signing (either title): ×1.10 for 2-3 weeks

EUROPEAN ORGANISATION DIMENSION:
  For organisations with strong French or Scandinavian heritage:
  European tournament performance carries additional weight for the core holder base.
  European event performance multiplier: ×1.05 additional weight
    versus equivalent result for a non-European organisation
```

---

## Compatibility

**CS2 framework:**         `sports/esports-cs2.md`
**Esports foundation:**    `sports/esports-framework.md`
**MOBA/tactical:**         `sports/esports-moba-tactical.md`
**Fan token verification:** `fan-token/official-verification-framework.md`

---

*SportMind v3.97.58 · MIT License · sportmind.dev*
*$VIT and $NAVI partnerships INACTIVE — framework applies to any future active Valorant token.*
