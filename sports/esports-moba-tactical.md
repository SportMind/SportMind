---
name: esports-moba-tactical
description: >
  League of Legends and Valorant reasoning framework. No active Chiliz tokens
  confirmed for either title — framework prepares SportMind for future launches.
  Covers Worlds/MSI/VCT tournament structures, regional dominance patterns,
  franchised system advantages, and demand frameworks for when tokens launch.
---

# League of Legends and Valorant — MOBA and Tactical Shooter Framework

**No active Chiliz fan tokens confirmed for LoL or Valorant organisations.**
Framework prepares SportMind for when they launch.
Load alongside `sports/esports-framework.md` (base framework).

---

## League of Legends — reasoning framework

### Tournament structure and signal weights

```
LOL TOURNAMENT HIERARCHY:

  WORLDS (annual world championship — October/November):
    Signal weight: ×2.00
    The primary annual demand event for any LoL organisation token.
    Regional champions + qualifying teams from global leagues.
    Format: play-in stage → group stage → knockout (Bo3/Bo5)
    Timing: October/November — follows regional summer splits
    
  MSI — MID-SEASON INVITATIONAL (May):
    Signal weight: ×1.50
    Second-largest international event. One team per region (regional champions).
    
  REGIONAL LEAGUES:
    LCK (Korea):          Signal weight ×1.20 — highest domestic prestige globally
    LPL (China):          Signal weight ×1.20 — largest viewership globally
    LEC (Europe):         Signal weight ×1.10
    LCS (North America):  Signal weight ×1.05 (declining regional significance)
    
  INTERNATIONAL vs REGIONAL WEIGHT:
    For any LoL token, Worlds/MSI carry 0.70 demand weight; regional play 0.30.
    Even strong regional teams have limited global demand without Worlds success.
```

### Regional dominance reasoning

```
LOL REGIONAL DOMINANCE — ENDURING PATTERNS:

  KOREAN (LCK) AND CHINESE (LPL) STRUCTURAL ADVANTAGES:
    Historically dominate Worlds — multiple consecutive victories from both regions.
    Foundation: longer professional infrastructure, bootcamp culture, player development.
    
  INTERNATIONAL MODIFIER TABLE:

  Matchup                           Modifier for LCK/LPL team
  ─────────────────────────────────────────────────────────────────────
  LCK vs LEC at Worlds              ×1.10 for LCK team
  LCK vs LCS at Worlds              ×1.12 for LCK team
  LPL vs LEC at Worlds              ×1.10 for LPL team
  LCK vs LPL at Worlds              No modifier — evenly matched historically
  LEC vs LCS at Worlds              ×1.05 for LEC team (LEC stronger internationally)

  WESTERN TEAM INTERNATIONAL MODIFIER:
    LEC and LCS teams at international events vs LCK/LPL:
    Apply: western_lol_international_modifier = ×0.85 vs Korean/Chinese opponents
    This reflects documented historical results — not a permanent ceiling but a structural pattern.

  REGIONAL META IDENTITY (enduring signals):
    LCK: methodical, macro-focused, objective control, slow-build victories
      Implication: favours longer-game strategies; struggles in high-tempo meta
    LPL: aggressive, skirmish-focused, early game pressure
      Implication: thrives in high-tempo patch meta; higher variance
    LEC: flexible, experimental, willing to play unorthodox strategies
      Implication: benefits in fresh patch environments (faster adaptation)
    LCS: import-heavy (many Korean/European players); volatile performance
      Implication: higher roster change frequency = more integration modifiers

  PATCH META INTERACTION WITH REGIONAL IDENTITY:
    Fresh patch (0-14 days):
      LCK teams: apply slow_meta_adaptor_discount = ×0.96 (methodical identity)
      LEC teams: apply fast_adaptor_bonus = ×1.04 (experimental identity)
    Stable patch (30+ days):
      LCK teams: full modifier restored (macro and discipline shine)
      LEC: no special modifier in stable meta
```

### LoL role importance and roster impact

```
ROLE IMPORTANCE — LEAGUE OF LEGENDS:

  CARRY ROLES (primary damage output):
    AD Carry (ADC): primary late-game damage; highest mechanical skill demand
    Mid laner: early-game tempo and cross-map influence
    
    Star carry departure: ×0.80 (slightly higher than CS2 AWPer ×0.82 for absence;
      LoL carry is less singular than CS2 AWPer — two carry positions exist)
      
  SUPPORT AND UTILITY ROLES:
    Support: enables carry; lower individual visibility
    Jungler: cross-map control; can carry but more utility-focused
    Top laner: often isolated; important for split-push and teamfight tanking
    
  IGL EQUIVALENT — SHOTCALLER:
    In LoL, the primary shotcaller (often support or jungler) organises team decisions.
    Shotcaller departure: ×0.88 (higher than general support departure — strategic voice lost)
    
  ROSTER INTEGRATION IN LOL:
    Apply standard esports-framework.md integration timeline (0-30d ×0.88, 31-60d ×0.94, etc.)
    Additional LoL note: champion pool coordination takes longer to establish than individual skill.
    For duo lane (ADC + support): new pairing needs 5-10 additional matches for synergy.
    Apply: duo_integration_modifier = ×0.96 for first 5 matches of new ADC/Support pairing.
```

### LoL token demand framework

```
DEMAND FRAMEWORK FOR ANY LOL ORGANISATION TOKEN:

  PRESTIGE TIERS:
    Worlds winner: ×1.20 permanent prestige floor
    MSI winner: ×1.10 prestige floor
    Worlds finalist: ×1.08 prestige floor
    Worlds semi-finalist (consistent): ×1.05 prestige floor
    Regional champion (no international presence): ×1.00 baseline

  KOREAN ORGANISATION PREMIUM:
    Korean LCK organisations carry additional international recognition.
    Apply: korean_org_international_modifier = ×1.10 at international events
    This reflects both sporting prestige and the global Korean esports brand.
    
  DEMAND CALENDAR:
    Off-season (Jan): lowest demand; roster change signals dominate
    Spring split (Feb-Apr): building
    MSI (May): first international peak
    Summer split (Jun-Aug): stable
    Worlds (Oct-Nov): annual peak — primary demand event
    Post-Worlds (Nov-Dec): decay to new baseline
    
  WORLDS DEMAND CURVE:
    Pre-Worlds (3 weeks out): ×1.10 build
    Play-in stage: ×1.15 (if team progressing)
    Group stage: ×1.20
    Knockout rounds: per-round premium (esports-framework.md schedule)
    Worlds victory: +60-80% spike (highest annual demand event)
```

---

## Valorant — reasoning framework

### Tournament structure

```
VALORANT TOURNAMENT HIERARCHY:

  VCT VALORANT CHAMPIONS TOUR — FRANCHISED STRUCTURE:
    Three international leagues: Americas, EMEA, Pacific
    All 30 franchised organisations play in regional leagues
    
  CHAMPIONS (annual world championship — August-September):
    Signal weight: ×1.80
    Primary annual demand event for any Valorant organisation token.
    
  MASTERS (two per year — mid-season internationals):
    Signal weight: ×1.40
    One Masters in spring, one in summer
    International competition between regional league champions
    
  REGIONAL LEAGUE SEASON:
    Signal weight: ×1.00 baseline
    Higher than non-franchised league equivalents due to franchise stability
    
  INTERNATIONAL TOURNAMENT CADENCE:
    Unlike LoL (one Worlds), Valorant has more frequent international touchpoints.
    This creates more evenly distributed demand throughout the year.
    Valorant demand curve is flatter (less extreme peak/trough) than LoL or Dota 2.
```

### Franchised system advantages

```
FRANCHISED STRUCTURE — DEMAND SIGNAL IMPLICATIONS:

  WHAT FRANCHISING CREATES:
    Roster stability: organisations cannot be relegated; cannot lose their slot.
    Less pressure to roster-cycle: teams can invest in long-term builds.
    Investor confidence: permanent slots attract commercial partners.
    
  DEMAND SIGNAL IMPLICATIONS OF FRANCHISING:
    Roster stability modifier: ×1.05 applied to demand baseline versus equivalent
      non-franchised esports organisation token at same achievement level.
    Reason: lower roster change frequency = more stable demand signals.
    
  TOKEN DEMAND CURVE RELIABILITY:
    Franchised Valorant tokens will have more predictable demand curves than:
      Dota 2 (non-franchised; high roster churn)
      CS2 (non-franchised with some exceptions)
    Lower variance = more reliable signal; can weight Valorant token CDI more heavily.
    Apply: valorant_cdl_reliability_modifier = reduce confidence interval by ×0.90
      (tighter prediction range due to more stable underlying signals)
      
  HOW FRANCHISED STABILITY AFFECTS DEPARTURE SIGNALS:
    Franchised organisations are more likely to retain key players (incentive alignment).
    Star player departure from a franchised team: apply ×0.90 modifier to standard
      esports departure impact (less likely = carries partial surprise premium when it occurs)
```

### Valorant role importance and regional patterns

```
VALORANT ROLE DYNAMICS:

  VALORANT AGENT ROLES (analog to CS2 roles but with unique mechanics):
    Duelist: primary fragger; high individual impact (similar to CS2 AWPer in role weight)
      Duelist departure: ×0.83 modifier (close to CS2 AWPer ×0.82)
    Sentinel: defensive anchor; enables structure
      Sentinel departure: ×0.90 modifier
    Controller: map control via smokes; enables team play
      Controller departure: ×0.88 (strategic vision lost; similar to shotcaller)
    Initiator: creates entry opportunities
      Initiator departure: ×0.92 modifier

VALORANT REGIONAL PATTERNS:
  EMEA: strongest international results in early Valorant history
    Apply: emea_valorant_modifier = ×1.05 at international events (modest advantage)
    
  Pacific/Americas: competitive and closing the gap
    No structural modifier yet established — apply standard signal weights
    
  VALORANT REGIONAL MODIFIER CONFIDENCE:
    Much lower confidence than LoL or CS2 regional patterns (newer title).
    Apply: ×0.90 confidence level to any Valorant regional modifier.
    As Valorant international tournament sample grows: recalibrate confidence upward.

PATCH META IN VALORANT:
  Agent meta shifts with patches — some agents become non-viable.
  Apply standard esports-framework.md patch recency modifier.
  Valorant agent pool is smaller than LoL champion pool → patches are more decisive.
  Teams with wide agent pool across all roles: apply flexibility_modifier = ×1.05.
```

### MOBA and tactical token demand framework

```
DEMAND FRAMEWORK — LOL AND VALORANT TOKENS (when they launch):

  COMPARISON TO DOTA 2 AND CS2:
    LoL: larger global audience ceiling — higher potential demand vs Dota 2
    Valorant: younger, growing audience — faster demand growth trajectory but smaller base
    CS2: established audience with strong regional concentration
    Dota 2: smaller total audience but deep engagement and prestige (TI prize pool)

  DEMAND SIZING ON LAUNCH:
    LoL organisation token from Worlds-contending team: would rival $OG baseline
    Valorant organisation token: smaller initial market but higher growth trajectory
    Apply: valorant_growth_trajectory_modifier = ×1.10 on demand projections (faster growth)

  WHICH ORGANISATIONS WOULD PRODUCE HIGHEST DEMAND:
    LoL: Korean LCK champions with Worlds pedigree (T1, Gen.G, established Korean orgs)
      Korean org + Worlds history = highest LoL token launch potential
    Valorant: EMEA franchised teams with Champions pedigree
      Franchised stability + Champions success = highest Valorant token launch potential
      
  MONITORING:
    Watch: chiliz.com and fantokens.com for any LoL or Valorant partnership announcements
    A Riot Games / Chiliz partnership at title level would unlock multiple tokens simultaneously
    Apply: title_partnership_announcement_modifier = ×1.30 to any confirmed Riot partnership
      (multiple launches simultaneously; ecosystem-level signal)
```

---

## Compatibility

**Base framework:**  `sports/esports-framework.md`
**Dota 2:**          `sports/esports-dota2.md`
**CS2:**             `sports/esports-cs2.md`
**CDI:**             `fan-token/esports-token-intelligence/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | MOBA and tactical shooter cross-genre signal framework |
| Reasoning | ACTIVE | MOBA/tactical reasoning chain from team composition to genre-specific outcome prediction |
| Context | ACTIVE | Genre context: MOBA (Dota 2, LoL) vs tactical shooter (CS2, Valorant) signal differences |
| Memory | ACTIVE | Historical genre-specific outcome patterns and team composition baselines |
| Judgment | ACTIVE | Judgment on genre-specific signal applicability — MOBA draft vs tactical economy differ |
| Attention | ACTIVE | Elevated attention for genre-defining events (TI for MOBA, Major for tactical) |
| Communication | ACTIVE | MOBA/tactical signal output with genre identifier and relevant signal framework |
| Verification | ACTIVE | Genre-specific data from official tournament and game operator sources |
| Learning | EMERGING | MOBA/tactical calibration is developing across titles |
| Integration | ACTIVE | Integrates with esports-framework.md, esports-dota2.md, and esports-cs2.md |
| Calibration | EMERGING | Genre-level calibration is emerging |
| Adaptation | ACTIVE | Genre framework adapts as new titles emerge and existing titles evolve |
| Ethics | NOT APPLICABLE | MOBA/tactical sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Genre type, game title, and signal framework identifier explicit in output |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |


---

*SportMind v3.97.30 · MIT License · sportmind.dev*
*No active LoL or Valorant tokens on Chiliz — framework ready for when they launch*
*Korean LoL organisations carry ×1.10 international prestige modifier*
