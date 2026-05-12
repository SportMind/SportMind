---
name: vitality-vit
description: >
  Team Vitality ($VIT) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Multi-title organisation: CS2 and Valorant primary.
  Franchised VCT participant — stability modifier applies. Covers title-specific
  demand weighting, roster change impact, and French identity premium signals.
---

# Team Vitality ($VIT) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $VIT.**
**Multi-title organisation: CS2 + Valorant primary titles.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `sports/esports-framework.md` · `sports/esports-cs2.md` · `sports/esports-moba-tactical.md`

---

## Organisation context

```
TEAM VITALITY PROFILE:
  Organisation type: multi-title esports organisation
  Primary titles: CS2 (Counter-Strike 2), Valorant
  Secondary presence: League of Legends, other titles
  Notable: one of Europe's largest and most commercially developed esports organisations
  French identity: Paris-headquartered; strong French and European fanbase
  
FRANCHISE STATUS:
  Valorant (VCT EMEA): CONFIRMED FRANCHISED PARTICIPANT
    Franchised stability modifier: ×1.05 on $VIT demand baseline
    Applies: permanent roster slot means no relegation/promotion risk
    Effect: more stable demand curve vs non-franchised esports organisations
    
  CS2: NOT FRANCHISED (CS2 has no franchise system)
    Standard esports volatility applies in CS2
    Roster changes have full impact (no protected slot stability)
```

---

## Multi-title demand weighting

```
$VIT DEMAND — TITLE WEIGHTING:

  CS2 demand weight:       0.50 (primary title; established fanbase; Major-driven)
  Valorant demand weight:  0.35 (growing; franchised; Champions-driven)
  Other titles:            0.15 (supplementary; limited individual demand impact)
  
  HOW TO APPLY MULTI-TITLE WEIGHTING:
    Do not treat $VIT as a single-title token.
    Calculate demand signal for CS2 performance AND Valorant performance separately.
    Apply title weights and sum for net $VIT demand signal.
    
    Example: CS2 Major victory (+40%) at CS2 weight 0.50 = +20% net $VIT demand
    Example: VCT Champions win (+50%) at Valorant weight 0.35 = +17.5% net
    Combined: both in same window (rare) = compound demand peak
    
  TITLE PERFORMANCE INDEPENDENCE:
    CS2 and Valorant rosters are separate — one title's poor result does not
    necessarily affect the other.
    But: a strong simultaneous performance across both titles creates a
    compounding brand narrative premium.
    Apply: dual_title_strong_performance_modifier = ×1.05 when BOTH titles
      are performing at playoff/knockout level simultaneously.
```

---

## CS2 performance reasoning

```
$VIT CS2 DEMAND FRAMEWORK:

  TOURNAMENT HIERARCHY (apply from esports-cs2.md):
    CS Major: signal weight ×1.80 | IEM Katowice: ×1.60 | ESL/BLAST: ×1.20
    
  VITALITY-SPECIFIC CS2 NOTES:
    French/European identity: European fanbase creates regional demand concentration.
    Apply: european_cs_identity_modifier = ×1.05 at CS2 events with strong European audiences
      (IEM Katowice especially — large European crowd; Vitality as a top European team
       receives crowd support signal beyond pure performance)
    
  CS2 ROSTER CHANGE IMPACT FOR $VIT:
    Apply standard esports-framework.md roster modifiers.
    CS2 is not franchised — Vitality can lose players to competitors freely.
    Star CS2 player departure: ×0.80 (primary role × standard carry modifier)
    AWPer-specific departure: apply ×0.82 modifier from esports-cs2.md
    
  MAJOR PERFORMANCE = PRIMARY CS2 DEMAND CATALYST:
    CS Major qualification: ×1.05 demand signal
    Major group stage appearance: ×1.15
    Major playoff bracket: ×1.25
    Major victory: +40-60% spike
```

---

## Valorant performance reasoning

```
$VIT VALORANT DEMAND FRAMEWORK:

  TOURNAMENT HIERARCHY (apply from esports-moba-tactical.md):
    Champions: ×1.80 | Masters: ×1.40 | Regional league: ×1.00
    
  FRANCHISED STABILITY ADVANTAGE:
    Vitality's permanent VCT EMEA slot means:
      No qualifier anxiety (no risk of missing the league)
      More consistent presence → more consistent demand signals
      Lower demand volatility than non-franchised esports organisations
    Apply: vct_franchised_stability_modifier = ×1.05 on all Valorant demand signals
    
  VITALITY EMEA IDENTITY:
    VCT EMEA is Vitality's home league — French/European supporters dominant.
    Apply: emea_home_league_modifier = ×1.03 for VCT EMEA matches
    (Regional audience concentration — similar concept to Spurs' Korean fanbase modifier)
    
  VALORANT ROSTER IMPACT:
    Franchised structure reduces roster churn slightly vs non-franchised.
    Apply departure modifier ×0.90 factor (10% lower impact than non-franchised)
    i.e.: Duelist departure: standard ×0.83 × 0.90 = ×0.747 effective modifier
    Note: this is a small adjustment reflecting lower churn probability,
      not a change to the base role departure values.
```

---

## French identity and demand signal

```
FRENCH IDENTITY — $VIT DEMAND MODIFIER:

  VITALITY'S FRENCH BRAND:
    Team Vitality is headquartered in Paris and has a strong French national identity.
    This creates geographic demand concentration in France and EMEA.
    
  FRENCH MARKET MODIFIER:
    Apply: french_market_modifier = ×1.05 for events with strong French media coverage
      or French national tournament context (French national league events, Paris events)
    This is the same demographic concentration pattern as $ALPINE (French F1 team)
    
  EVENTS WITH ELEVATED FRENCH SIGNAL:
    CS2 or Valorant events hosted in France: french_market_modifier = ×1.08
    Paris-specific events: ×1.10 (hometown factor)
    International events (neutral location): no French modifier — standard
    
  COMBINED EUROPEAN IDENTITY:
    European esports events more broadly: apply ×1.03 European identity modifier
    (Vitality is a flagship European esports org — recognised beyond France)
```

---

## Off-season roster change framework

```
OFF-SEASON ROSTER CHANGES — $VIT SPECIFIC:

  CS2 OFF-SEASON (November-January typically):
    CS2 roster changes are more frequent and impactful than Valorant.
    Monitor: any primary CS2 player contract expiry or transfer.
    Apply standard esports-framework.md off-season volatility flag.
    
  VALORANT OFF-SEASON (October-December after Champions):
    Franchised structure moderates Valorant roster churn.
    Vitality more likely to retain core Valorant roster than CS2 roster.
    Off-season demand volatility: LOWER in Valorant than CS2 for $VIT.
    
  PATCH CYCLE IMPACT:
    Apply patch recency modifiers from esports-framework.md for both titles.
    CS2 patches: moderate frequency; AWP/rifle meta changes most impactful for $VIT.
    Valorant patches: frequent; agent meta shifts affect roster's draft flexibility.
```

---

## Compatibility

**Esports base:**     `sports/esports-framework.md`
**CS2 framework:**    `sports/esports-cs2.md`
**Valorant:**         `sports/esports-moba-tactical.md`
**CDI:**              `fan-token/esports-token-intelligence/`
**Tier A:**           `athlete/football/tier-a-clubs-framework.md` (demand curve framework)

---

*SportMind v3.97.31 · MIT License · sportmind.dev*
*Multi-title: CS2 weight 0.50 | Valorant weight 0.35. Franchised VCT stability ×1.05*
