---
name: womens-football
description: >
  Women's football reasoning framework. No active women's football fan tokens
  confirmed — this framework prepares SportMind for when they launch. Covers
  structural differences from men's football, key competition reasoning,
  fan token launch readiness assessment, and World Cup timing specifics.
  All enduring reasoning — these structural differences persist indefinitely.
---

# Women's Football — Reasoning Framework

**Prepares SportMind for women's football fan token intelligence.**
No confirmed active women's football fan tokens in current library state.
This file contains the enduring reasoning framework for when they launch.

> Library Rule: structural differences between women's and men's football
> are enduring characteristics of the sport. True and useful beyond six months.

---

## Structural differences from men's football

```
COMPETITION CALENDAR:
  WSL (England): September to May — same seasonal structure as men's
    but without the volume and density of competition
  NWSL (USA): Spring to Fall (March-November) — different calendar to European leagues
  Liga F (Spain): September to June
  Frauen-Bundesliga (Germany): September to May
  Women's Champions League: September to May (group stage through final)
  
  KEY DIFFERENCE vs MEN'S:
    International windows are more frequent and longer for women's football.
    Women's World Cup camps can be 4-6 weeks vs men's 2-3 weeks.
    International duty therefore disrupts domestic clubs MORE than in men's football.
    Apply: international_disruption_modifier ×1.20 for women's football clubs
      (20% larger disruption than equivalent men's modifier)

TRANSFER FEES AND VALUATIONS:
  Women's football transfer fees are significantly lower than men's equivalents.
  The modifier framework requires recalibration:
    
    Women's Marquee signing threshold: above €500k (vs men's €50M+)
    Women's Notable signing threshold: above €100k
    Women's Squad depth signing: below €100k
    
  Apply the SAME tier framework as men's (see transfer-window-intelligence.md)
  but with the recalibrated fee thresholds above.
  
  TRAJECTORY NOTE:
    Women's football transfer fees are growing rapidly.
    The €500k marquee threshold should be reviewed annually.
    If the market has grown significantly, recalibrate thresholds upward.

ATTENDANCE AND BROADCAST REVENUE:
  Women's football attendance and broadcast revenue are growing fast.
  Signal implications:
    Current state (growing but lower than men's): base CDI modifiers should be
      scaled relative to women's market, not men's market
    Trajectory matters as much as current state:
      Clubs with fastest-growing attendance are more valuable fan token prospects
      than clubs with large but stagnant audiences
    Apply: growth_trajectory_modifier = ×1.05 for clubs with documented
      3+ consecutive seasons of attendance growth
```

---

## Key competition reasoning

```
UEFA WOMEN'S CHAMPIONS LENGTH:
  Highest prestige European competition — knockout psychology similar to UCL.
  Competition structure (group stage → knockout) mirrors men's format.
  
  Signal implications when women's tokens exist:
    UWCL qualification: demand premium ×1.10 (same framework as men's UCL)
    UWCL knockout stages: demand premium ×1.15-1.40 depending on round
    UWCL final appearance: peak demand event (same pattern as men's UCL final)
    
  CLUB BRAND ALIGNMENT:
    Clubs with both men's and women's UCL appearances simultaneously have
    amplified brand signal — both squads in Europe = elevated commercial profile.
    Apply: dual_ucl_brand_modifier = ×1.05 on any associated fan token

FIFA WOMEN'S WORLD CUP:
  Quadrennial — same cycle as men's World Cup.
  Offset from men's by 4 years (Women's WC in the year between two men's WCs).
  
  Timing: July-August (distinct from men's November-December historically,
    and also distinct from men's June-July in recent editions)
  
  Signal framework:
    Apply national-team-tokens.md demand cycle framework if women's national tokens exist.
    If no women's national tokens: route sentiment through associated club tokens
      (same proxy mechanism as Euros — see sport-domain-euros.md)
    Tournament demand premium: apply same 300-1,000% historical range framework
      BUT with lower base market cap → smaller absolute demand in early market
      
  LESS DOMESTIC DISRUPTION:
    Women's World Cup (July-August) overlaps with domestic close season in Europe.
    European domestic leagues are suspended during summer.
    Less club disruption than men's equivalents — no mid-season absences.

WSL / NWSL / LIGA F — DOMESTIC REASONING:
  Most likely first home for women's fan tokens (domestic league clubs).
  Apply standard football sport domain reasoning with these adjustments:
    Home advantage: similar to men's (+0.10) but crowd composition is growing
    Derby matches: apply derby modifier (see acmilan-acm.md framework for model)
    International windows: elevated disruption modifier ×1.20 (see above)
```

---

## Fan token launch readiness

```
WHICH CLUBS ARE MOST LIKELY TO LAUNCH WOMEN'S FAN TOKENS:

  TIER 1 CANDIDATES (strongest launch readiness):
    Clubs with:
      Existing men's fan token on Chiliz (infrastructure already in place)
      Strong women's team with sustained domestic/European success
      Large women's fan base with documented growth
    Primary candidates in this tier:
      Arsenal ($AFC exists — Women's Arsenal token most likely from English clubs)
      Barcelona ($BAR exists — Barça Women are European powerhouse)
      Manchester City ($CITY exists — City Women have strong domestic profile)
      Chelsea (no current men's token but women's team highly successful)
      Lyon (no men's token but Lyon Women are most decorated European women's club)
      
  TIER 2 CANDIDATES (good readiness, less immediate):
    Clubs with existing men's token but women's program less developed:
      PSG Women (PSG men's token exists)
      Juventus Women (JUV men's token exists)
      AC Milan Women (ACM men's token exists)
      
  HOW WOMEN'S TOKEN INTERACTS WITH EXISTING MEN'S TOKEN:
    Same club, different tokens:
      Men's token: established holder base, club-level CDI established
      Women's token: launches into an existing club fan base
      Cross-promotion: women's token launch benefits from men's holder base awareness
      Apply: existing_club_token_launch_bonus = ×1.15 to new women's token launch CDI
        (Club community already engaged; acquisition cost lower than from scratch)
        
  DEMAND SIZING ON LAUNCH:
    Expected launch market cap: significantly below men's equivalents
    BUT growth trajectory expected to be faster than men's equivalent at same age
    Apply: women_token_growth_premium = ×1.10 on demand trajectory projections
      for first 2 years post-launch (faster growth expected relative to men's pace)

HOW WOMEN'S TOKENS WILL DIFFER FROM MEN'S:
  No confirmed FTP PATH_2 mechanic for any women's football at current state.
  Until confirmed: treat all potential women's tokens as demand-only.
  If PATH_2 extends to women's teams: update this file and apply arsenal-afc.md
    framework adapted for women's match schedule and supply pool sizing.
```

---

## Women's World Cup timing

```
WOMEN'S WORLD CUP — CALENDAR CONTEXT:

  TIMING (July-August):
    Runs AFTER European domestic seasons conclude.
    Less domestic season disruption than men's World Cup (which sometimes ran
    during or after club seasons with varied timing).
    European players: released post-season, arrive fresh (similar to Copa América).
    
  PLAYER FATIGUE PROFILE:
    Players from major European leagues: season ends May/June → 2-3 month off-season
    before July Women's World Cup.
    Apply: women_world_cup_fatigue_modifier = ×0.99 match 1 only (minimal fatigue)
    (Far less than AFCON ×0.96 mid-season disruption)

  NATIONAL TOKEN OR CLUB PROXY:
    No confirmed women's national tokens in current library state.
    Route national tournament sentiment through:
      (a) Associated women's club tokens if they exist at time of tournament
      (b) Men's club tokens of clubs strongly associated with participating nations
          (same proxy mechanism as Euros — see sport-domain-euros.md)
          
  DEMAND SIGNAL WHEN NO WOMEN'S TOKENS EXIST:
    Women's World Cup generates brand signal for clubs with strong women's programs.
    If Arsenal Women reach World Cup final → $AFC men's token receives marginal benefit
    through club brand amplification.
    Apply: women_wc_club_brand_modifier = ×1.02 for clubs with Women's WC finalists
    Duration: 1-2 weeks around tournament climax only
```

---

## Compatibility

**Euros proxy mechanism:** `sports/football/sport-domain-euros.md`
**National token cycles:** `fan-token/national-team-tokens.md`
**Transfer framework:**    `core/transfer-window-intelligence.md`
**Tournament macro:**      `macro/tournament-macro.md`
**AFCON comparison:**      `sports/football/sport-domain-afcon.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Women's football signal intelligence: WSL, NWSL, UEFA Women's Championship signals |
| Reasoning | ACTIVE | Women's football reasoning chain from squad composition and form to outcome prediction |
| Context | ACTIVE | Women's football context: competition tier growth, depth of squad, FIFA Women's World Cup |
| Memory | ACTIVE | Historical women's football outcome patterns and tournament baselines |
| Judgment | ACTIVE | Judgment on women's football signal differences from men's — squad depth is more impactful |
| Attention | ACTIVE | Elevated attention during FIFA Women's World Cup and UEFA Women's EURO |
| Communication | ACTIVE | Women's football signal output with competition context and direction |
| Verification | ACTIVE | Women's football data from FIFA/UEFA official sources |
| Learning | ACTIVE | Women's football calibration growing as data availability improves |
| Integration | ACTIVE | Integrates with sport-domain-football.md for shared framework with women's-specific overrides |
| Calibration | EMERGING | Women's football calibration is emerging — growing dataset |
| Adaptation | ACTIVE | Women's football intelligence adapts as professional standards and competition depth evolve |
| Ethics | NOT APPLICABLE | Women's football sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Competition context and women's-specific signal differences noted in output |


---

*SportMind v3.97.28 · MIT License · sportmind.dev*
*No active women's football fan tokens confirmed — framework ready for when they launch*
