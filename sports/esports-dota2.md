---
name: esports-dota2
description: >
  Dota 2 specific reasoning framework for AI agents. Covers tournament structure
  signal weights (TI, Majors, DPC), hero meta patch reasoning, carry player
  dominance, draft flexibility modifier, and specific $OG and $ALL token demand
  frameworks. Load alongside sports/esports-framework.md.
---

# Dota 2 — Esports Reasoning Framework

**Title-specific. Load alongside `sports/esports-framework.md` (base framework).**

---

## Active fan tokens

```
CONFIRMED DOTA 2 TOKENS:
  $OG   OG Esports — BRIDGE_LIVE (Chiliz Chain + Solana + Base)
        Demand-only — no FTP PATH_2
        OG's brand is built on TI victories — the strongest esports prestige modifier
        in the library.
        
  $ALL  Alliance — verify current Chiliz partnership status before applying
        Demand-only — no FTP PATH_2
        Alliance historic TI victory creates permanent prestige baseline.

AGENT RULE: Verify both tokens at fantokens.com before every analysis cycle.
Esports partnership statuses change more frequently than traditional sports.
```

---

## Tournament structure and signal weights

```
DOTA 2 TOURNAMENT HIERARCHY:

  The International (TI) — ANNUAL WORLD CHAMPIONSHIP:
    Signal weight multiplier: ×2.0 versus standard tournament baseline
    Prize pool: the largest annual prize pool in esports (community-funded component)
    Timing: typically August/September
    Qualification: regional DPC points + direct invites
    Stage structure: group stage → double-elimination main event bracket
    
    TI IS THE SINGULAR EVENT for Dota 2 token demand:
      A team's entire annual demand narrative centres on TI performance.
      DPC results matter for qualification and prestige but carry far less
      demand weight than TI itself.
      TI demand build: begins 3-4 weeks before group stage
      
  DOTA PRO CIRCUIT (DPC) REGIONAL LEAGUE:
    Signal weight: ×1.00 (baseline)
    Purpose: builds points for Major/TI qualification
    Demand impact: moderate — qualification secured or at risk are the key signals
    
  DPC MAJORS (3 per season):
    Signal weight: ×1.50
    Highest ranked international events outside TI
    Major victory: significant demand spike +20-35%
    Major final appearance: +10-20% demand during bracket
    
  ONLINE LEAGUES vs LAN EVENTS:
    DPC regional league: often online → apply ×0.92 online modifier (from esports-framework.md)
    Majors and TI: always LAN → full signal weight
```

---

## Dota 2 specific modifiers

### Hero meta and patch reasoning

```
DOTA 2 HERO META INTELLIGENCE:

  WHY HERO META MATTERS MORE IN DOTA 2 THAN MOST ESPORTS:
    Dota 2 has 120+ heroes with complex interactions. Patch changes can make
    entire playstyle strategies obsolete — not just individual heroes.
    The meta in Dota 2 is more complex and shifts more dramatically than CS2.
    
  HERO POOL (DRAFT FLEXIBILITY) MODIFIER:
    Teams with larger competent hero pools have strategic advantages:
      They can threaten more picks, making them harder to draft against.
      They adapt faster to meta shifts.
      
    Draft flexibility modifier:
      Teams with documented wide hero pool (documented across tournaments):
        flexibility_modifier = ×1.05 on adjusted match signal
      Teams known for narrow hero pool / signature heroes:
        If their signature heroes are nerfed: apply hero_nerf_modifier = ×0.90
        If their signature heroes are buffed: apply hero_buff_modifier = ×1.08
        
  PATCH RECENCY IN DOTA 2:
    Apply the standard patch recency framework from esports-framework.md.
    Additional Dota 2 note: major Dota 2 patches can shift the entire game
    meta, not just balance. Full ×0.85 confidence modifier applies for 0-7 days.
    Some teams have documented stronger meta-read ability — identify and apply
    patch_adapter_modifier = ×1.06 for confirmed fast-adapter teams.
```

### Carry player dominance

```
CARRY PLAYER DOMINANCE — DOTA 2 SPECIFIC:

  WHY CARRY MATTERS MORE IN DOTA 2 THAN OTHER ESPORTS:
    Dota 2 has a more pronounced carry role dependency than most esports titles.
    In the late game, the primary carry player is the team's primary win condition.
    
  CARRY PLAYER MODIFIER:
    Primary carry player modifier weight in Dota 2:
      Carry weight: ×1.15 versus ×1.00 baseline in other esports titles
      
    This means carry player absence/replacement has 15% more impact in Dota 2
    than the equivalent star player change in CS2 or LoL.
    
    Carry departure: apply ×0.75 from esports-framework.md AND amplify by 1.15:
      Effective modifier: ×0.75 × 1.15 impact weight = carry is the most critical position
    
    Elite carry replacement (same tier): ×0.90 (not ×0.75 — quality preserved)
    Downgrade replacement: ×0.78 (×0.75 floor with small quality premium)
    
  SUPPORT PLAYER IN DOTA 2:
    Support roles are critical for carry enablement — but less individually visible.
    Support departure: ×0.92 base modifier (matches esports-framework.md)
    Support pair disruption (both supports changed): ×0.88 compound
```

---

## $OG token demand framework

```
$OG DEMAND CYCLE — BUILT AROUND TI:

  OG'S BRAND IDENTITY:
    OG are the only organisation to win The International twice consecutively.
    This creates a permanent prestige modifier that distinguishes $OG from all
    other esports tokens — including other Dota 2 tokens.
    
  PERMANENT PRESTIGE MODIFIER:
    og_prestige_modifier = ×1.10 applied to $OG baseline demand at all times
    This reflects OG's sustained global recognition beyond any single tournament result.
    
  ANNUAL DEMAND CYCLE:

  Period                      Demand level    Notes
  ────────────────────────────────────────────────────────────────────────
  Off-season (Oct-Mar)        ×1.00 base      Prestige modifier applies throughout
  DPC league season (Mar-Jun) ×1.05           Results signal TI qualification trajectory
  Pre-TI build (Jun-Aug)      ×1.10           Anticipation; TI narrative builds
  TI group stage (Aug)        ×1.15           OG in TI = peak engagement begins
  TI main event bracket       ×1.20           Each round adds demand
  TI victory                  ×1.60-2.00      Maximum event; unprecedented in $OG history
  Post-TI 4-6 weeks           Decaying        Returns to prestige-elevated baseline
  
  TI IS SINGULAR FOR $OG:
    DPC Major results carry significant less demand weight than TI for $OG.
    A DPC Major victory for OG: +15-25% spike (strong but not TI-scale)
    TI victory for OG: +60-100% spike (generational event for this token)
    
  OG ROSTER STABILITY PREMIUM:
    OG have historically maintained roster cores over multiple seasons.
    When OG roster is stable (same core for 12+ months):
      Apply: og_roster_stability_modifier = ×1.05 to demand signals
    Major OG roster change: apply standard esports roster disruption modifiers
      (×0.75-0.92 depending on role) — prestige modifier maintained but signal disrupted
```

---

## $ALL (Alliance) token demand framework

```
$ALL DEMAND CYCLE:

  ALLIANCE BRAND IDENTITY:
    Alliance won TI3 — an iconic victory in Dota 2 history.
    Their brand carries historical prestige, though not as sustained as OG's
    (OG won TI7 AND TI8 consecutively; Alliance's last TI win is older).
    
  PRESTIGE BASELINE:
    alliance_prestige_modifier = ×1.05 (lower than OG's ×1.10 — older historical win)
    Apply at all times as structural demand floor.
    
  REGIONAL DEMAND:
    Alliance is a Scandinavian organisation. Regional esports events in
    Northern Europe carry additional demand weight for $ALL:
      Scandinavian/Nordic audience concentration
      Apply: scandinavian_regional_modifier = ×1.05 for events with strong
        Scandinavian coverage or audience penetration
    
  ROSTER STABILITY SIGNAL:
    Alliance historically shows higher roster turnover than OG.
    This creates more frequent roster change demand disruptions.
    Apply standard esports-framework.md roster modifiers on each change.
    More frequent roster changes = less stable demand baseline = higher volatility.
    Apply: alliance_roster_volatility_flag during any rebuild period.
    
  TI DEMAND CYCLE:
    Same structure as $OG annual cycle, scaled to Alliance's lower prestige tier:
      Pre-TI: ×1.05 build
      TI main event: ×1.10 per round (vs $OG ×1.20)
      TI victory: ×1.40-1.60 (vs $OG ×1.60-2.00 — lower prestige multiplier)
```

---

## Compatibility

**Base framework:**  `sports/esports-framework.md`
**CS2:**             `sports/esports-cs2.md`
**LoL/Valorant:**    `sports/esports-moba-tactical.md`
**CDI:**             `fan-token/esports-token-intelligence/`

---

*SportMind v3.97.30 · MIT License · sportmind.dev*
*$OG prestige modifier ×1.10 — only two-time consecutive TI winner in Dota 2 history*
