---
name: galatasaray-gal
description: >
  Galatasaray ($GAL) athlete intelligence reasoning framework. Demand-only —
  no confirmed FTP PATH_2. Covers Türk Telekom stadium home fortress reasoning,
  Süper Lig tactical context, Turkish international player dependency, and
  European qualification demand impact on $GAL demand signals.
---

# Galatasaray ($GAL) — Athlete Intelligence

**DEMAND-ONLY. No confirmed FTP PATH_2 mechanic for $GAL.**

> Library Rule: no named players, no current injury status. Reasoning framework only.

Load alongside: `athlete/football/tier-a-clubs-framework.md`

---

## System identity and stadium context

```
GALATASARAY SYSTEM IDENTITY:
  Galatasaray are the most decorated Turkish club — Süper Lig dominance
  and periodic European campaigns define their identity.
  Their system is typically attack-minded with reliance on individual quality
  in attacking positions, supported by a disciplined Turkish defensive base.

TÜRK TELEKOM STADIUM — HOME FORTRESS:
  Galatasaray's home ground is widely documented as one of the most hostile
  atmospheres in European football. The stadium's enclosed design amplifies
  crowd noise significantly.
  
  Home advantage baseline: standard +0.10 (football baseline)
  Türk Telekom fortress modifier: ×1.12 (significantly above average)
  European nights at Türk Telekom: apply ×1.15 (atmosphere amplified by occasion)
  
  Sell-out confirmed modifier: ×1.05 applied on top of fortress ×1.12
    combined: ×1.17 (one of the highest single-venue modifiers in the library)
```

---

## Position reasoning frameworks

### Attacking players — individual quality dependency

```
ATTACKING QUALITY DEPENDENCY:

  ROLE IN SYSTEM:
    Galatasaray's attacking system relies heavily on individual quality in
    the final third. Unlike possession clubs, Galatasaray's attack is
    structured around releasing technically gifted players rather than
    systematic patterns. Individual availability therefore carries more
    weight than at systematically cohesive clubs.
    
  MODIFIER FRAMEWORK:
    PRIMARY STRIKER / ATTACKING THREAT AVAILABLE:
      goal_threat_modifier = ×1.12 (above average — individual dependency)
      
    ABSENT:
      adjusted_score_shift = −5 to −8 points (higher than average)
      Reason: system does not absorb individual attacking absence as well
        as clubs with deep tactical identity (City, Barcelona)
      individual_quality_dependency_modifier = ×0.84

FOREIGN MARQUEE PLAYER PRESENCE:
  Galatasaray periodically attract high-profile foreign signings. When a
  globally recognised player is active in the squad:
    international_profile_modifier = ×1.08 on demand signal
    Their form and availability carry higher global narrative weight
    Absence: apply individual_quality_modifier (see above) × demand_sentiment_weight = 0.9
```

### Defensive organisation

```
DEFENSIVE ORGANISATION:

  ROLE IN SYSTEM:
    Turkish clubs typically build on physical defensive presence. Galatasaray's
    defence is their structural foundation — key Turkish international players
    anchor the defensive line.
    
  TURKISH INTERNATIONAL DEFENDER NOTE:
    Key Turkish international defenders at Galatasaray carry a dual signal:
      Club role: standard individual modifier
      National team role: during Turkish national team qualification periods,
        player visibility elevated → demand signal amplified
    Apply: turkish_national_team_sentiment_modifier = ×1.03 during EURO
      qualification / Nations League high-stakes periods
      (Turkish fans track national team form closely — club token sentiment
       can correlate with national team results in Turkey)
```

---

## Süper Lig tactical context

```
SÜPER LIG TACTICAL CONTEXT:

  COMPETITION CHARACTERISTICS:
    Süper Lig is a competitive but lower-intensity technical league than EPL,
    Bundesliga, or La Liga. However, physicality and intensity are high.
    
  TACTICAL MODIFIERS (Süper Lig vs European competitions):
    Domestic (Süper Lig): apply standard modifiers; home advantage ×1.12
    European (UCL/UEFA): reset to standard European baseline; reduce home modifier
      European away matches: Türk Telekom modifier does not apply away
      
  AFCON EQUIVALENT — TÜRK TELEKOM CUP / NATIONAL TEAM:
    Turkey's national team campaigns do not create the same mid-season disruption
    as AFCON (Turkey national team is not AFCON-eligible; Turkish players are
    released for UEFA qualifiers — standard European windows apply).
    Apply standard international break framework (no AFCON-specific modifier).
```

---

## European qualification and $GAL demand

```
$GAL DEMAND — EUROPEAN SENSITIVITY:

  CHAMPIONS LEAGUE QUALIFICATION:
    Galatasaray's brand is elevated by UCL participation.
    UCL qualification confirmed: demand_premium = ×1.15 (seasonal baseline lift)
    UCL qualification missed: demand_decay = ×0.90 for the season
    
  UCL KNOCKOUT PROGRESS:
    Each UCL knockout round advanced: ×1.10 demand premium
    Istanbul hosts UCL Final (historically): city-level demand amplification
    
  EUROPA LEAGUE:
    Lower than UCL but meaningful: qualification premium ×1.05
    EL knockout stages: ×1.05 per round
    
  AGENT RULE:
    Confirm European competition status at start of each season.
    $GAL demand trajectory for the season is heavily influenced by whether
    UCL football is live. UCL = elevated baseline; no European = depressed baseline.
```

---

## Compatibility

**Base framework:**   `athlete/football/athlete-intel-football.md`
**Tier A framework:** `athlete/football/tier-a-clubs-framework.md`
**Venue fortress:**   `core/venue-intelligence.md`

---

*SportMind v3.97.29 · MIT License · sportmind.dev*
*Türk Telekom fortress: one of the highest home advantage modifiers in the library (×1.12-1.17)*
