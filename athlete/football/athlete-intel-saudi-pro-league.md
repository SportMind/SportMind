# Saudi Pro League — Athlete Intelligence

**Supplementary athlete intelligence for Saudi Pro League.
Load alongside `athlete/football/athlete-intel-football.md` for SPL-specific
player modifier context.**

---

## Applicable tokens

```
ACTIVE TOKENS:      None confirmed as of v3.97.8
ANTICIPATED TOKENS: $HILAL (Al Hilal), $NASSR (Al Nassr),
                    $ITTIHAD (Al Ittihad), $AHLI (Al Ahli)

This file provides athlete modifier intelligence for when SPL fan tokens
launch and for existing European fan tokens whose players move to the SPL.
Example: $PSG or $BAR holders tracking Neymar/Messi-era transfers.
```

---

## Commands

| Command | Description |
|---|---|
| `get_key_player_availability` | Check availability for Ronaldo, Neymar, Benzema |
| `get_athlete_signal_modifier` | SPL-specific composite modifier for named players |
| `get_player_form_score` | Form rating adjusted for SPL conditions |
| `get_physical_load` | Heat and travel fatigue assessment |

---

## Command reference

See `athlete/football/athlete-intel-football.md` for base command implementations.
This file provides SPL-specific parameter overrides and modifier values.

### `get_key_player_availability` (SPL override)

```json
{
  "player": "Cristiano Ronaldo",
  "club": "Al Nassr",
  "available": true,
  "atm_modifier": 1.50,
  "flags": ["heat_acclimatised", "age_load_managed"],
  "confidence": "medium",
  "source_required": "tier1_confirmation_T48h"
}
```

### `get_athlete_signal_modifier` (SPL)

```json
{
  "club": "Al Hilal",
  "player": "Neymar",
  "condition": "unconfirmed",
  "modifier": 0.85,
  "note": "Assume unavailable until Tier 1 confirmation. Injury history applies."
}
```

---

## High-Profile Player Profiles

### Cristiano Ronaldo — Al Nassr

```
TOKEN RELEVANCE:    $NASSR (anticipated) | Proxy: Portuguese national token $POR
STATUS:             Active (2023–present at Al Nassr)
CONTRACT:           Extended through 2025-26 season

SIGNAL PROFILE:
  Global following:    600M+ across social platforms (largest individual sports
                       following globally)
  Media reach:         Any Ronaldo SPL content generates European media pickup
  SPL impact:          Ronaldo signing in 2023 transformed Al Nassr's global brand
                       from regional to international overnight

ATM MODIFIER (Ronaldo at Al Nassr):
  Ronaldo fit + scoring form:     ×1.50 (unique — no other SPL player applies this)
  Ronaldo fit, not scoring:       ×1.25 (presence value exceeds output)
  Ronaldo doubtful / absent:      ×0.65 for Al Nassr token signals
  Ronaldo injury confirmed:       ×0.55 — significant brand signal reduction
  
  NOTE: Ronaldo's ATM modifier range (0.55–1.50) is the widest in the
  SPL. His presence alone, regardless of performance, carries significant
  brand value. His absence affects token signals more than any comparable
  European player absence (except Messi-era equivalents).

FORM CONTEXT:
  Age factor (2026): 41 years old — elevated injury monitoring required
  Physical load management: SPL schedule is lighter than European Tier 1
  Heat acclimatisation: 3+ seasons in Saudi Arabia — no longer a risk factor
  
AVAILABILITY HISTORY (SPL):
  2023-24: Highly available (40+ appearances across competitions)
  2024-25: Some absences (load management + minor injuries)
  2025-26: Monitor closely — age-related load management standard expectation

AGENT RULE — RONALDO AVAILABILITY:
  For any Al Nassr signal, check Ronaldo availability FIRST.
  Ronaldo absent → ATM modifier floor 0.55 → signal downgrade automatic.
  Ronaldo confirmed fit → apply ×1.50 ceiling modifier to match importance.
  Ronaldo milestone near (e.g. 900 career goals): apply ×1.30 narrative modifier.

EUROPEAN TOKEN CROSS-IMPACT:
  $POR (Portugal fan token): Ronaldo international performance still drives $POR.
  SPL performance does not directly affect $POR CDI.
  Ronaldo retirement announcement (future): Tier 1 signal for $POR
  (negative supply demand shock on retirement vs positive legacy narrative).
```

### Karim Benzema — Al Ittihad

```
TOKEN RELEVANCE:    $ITTIHAD (anticipated) | Proxy: None (French NT retired)
STATUS:             Active at Al Ittihad (2023–present)
BALLON D'OR:        2022 winner — highest-pedigree signing in SPL history to date

SIGNAL PROFILE:
  Global following:    50M+ social media
  Media reach:         Strong European coverage (French and Spanish language)
  SPL impact:          Benzema signing elevated Al Ittihad to global awareness;
                       first Ballon d'Or winner to sign for SPL

ATM MODIFIER (Benzema at Al Ittihad):
  Benzema fit + scoring form:     ×1.35
  Benzema fit, inconsistent form: ×1.10
  Benzema doubtful / managing:    ×0.80
  Benzema absent:                 ×0.70

FORM CONTEXT:
  Age factor (2026): 38 years old — fitness management is primary variable
  Injury history: significant — multiple muscle and knee issues across career
  Heat acclimatisation: 3 seasons in Saudi Arabia — adapted
  Peak form SPL: shown in flashes; no longer the sustained excellence of
  Real Madrid prime, but single-match performances remain elite level

AVAILABILITY HISTORY:
  2023-24: Inconsistent — multiple absences for injury and personal reasons
           Left the club temporarily in disputed circumstances (2024)
  2024-25: Returned and stabilised; availability improved
  2025-26: Moderate availability expected; manage load expectations

AGENT RULE — BENZEMA AVAILABILITY:
  More volatile than Ronaldo — do not assume availability without confirmation.
  Benzema confirmed: ×1.35 for Al Ittihad signals.
  Benzema absent: ×0.70 — significant reduction vs Ronaldo (smaller global base).
  Benzema controversy/dispute with club: apply ATM floor ×0.60 (narrative risk).
```

### Neymar Jr — Al Hilal (context — injury history)

```
TOKEN RELEVANCE:    $HILAL (anticipated) | Proxy: None (Brazilian national retired)
STATUS:             Contracted to Al Hilal; severely limited by injury (2023–present)
SIGNING CONTEXT:    World-record wage; expected to transform Al Hilal globally

SIGNAL PROFILE:
  Global following:    210M+ social media (third largest individual sports following)
  Media reach:         Extremely high — any Neymar content is global news
  SPL actual impact:   SEVERELY LIMITED — Neymar played fewer than 7 matches
                       for Al Hilal across 2023-24 and 2024-25 due to ACL injury

ATM MODIFIER (Neymar at Al Hilal):
  CRITICAL NOTE: Neymar's modifier framework must begin with injury assessment.
  
  Neymar fit + match active:          ×1.45 (highest $HILAL signal amplifier)
  Neymar in rehabilitation / unknown: ×0.85 (uncertainty premium)
  Neymar confirmed absent:            ×0.75 (significant but $HILAL has depth)
  Neymar return announced (Tier 1):   ×1.35 (pre-return anticipation)
  
  IMPORTANT: Neymar's RETURN is itself a signal event, not just availability.
  Even a training ground appearance after extended absence generates media spike.
  Apply return_anticipation_modifier = ×1.20 for 2 weeks preceding confirmed return.

INJURY HISTORY (SPL-relevant):
  August 2023: Signed for Al Hilal; global media event
  October 2023: ACL rupture — entire 2023-24 season missed
  2024-25: Return delayed; limited appearances; further setbacks
  2025-26: Status uncertain — treat as unavailable until Tier 1 confirmation

AGENT RULE — NEYMAR:
  NEVER assume Neymar available. Always require T-48h Tier 1 confirmation.
  Neymar is the highest single-player CDI uncertainty factor in the library.
  His availability probability (pre-confirmation): apply 30% weight only.
  Al Hilal signals without Neymar: use squad-depth modifier ×0.90 (strong squad).

EUROPEAN TOKEN CROSS-IMPACT:
  $PSG: Neymar departure from PSG was long-completed. No $PSG CDI link.
  Brazil NT ($BRA if launched): career likely over for international duty.
```

---

## Form Modifier Context — European Stars in SPL Conditions

```
EUROPEAN STAR PERFORMANCE TRANSLATION TO SPL:

  The SPL is a lower competitive intensity league than EPL/La Liga/UCL.
  European stars typically register better raw statistics (goals, assists)
  in the SPL, but the signal value of those statistics is lower.

  TRANSLATION TABLE:
  
  European Tier 1 stat (EPL/UCL)        SPL equivalent
  ───────────────────────────────────────────────────
  10 goals in EPL                        ~14–18 goals in SPL
  Champions League goal                  2–3 SPL goals (media coverage equivalent)
  Assists in EPL                         ~1.3× assists in SPL
  
  IMPLICATION FOR AGENTS:
  Do not treat SPL statistical milestones the same as European equivalents.
  A Ronaldo hat-trick in the SPL generates European media coverage.
  A Ronaldo hat-trick in the UCL would generate 5× more.
  Apply SPL_stats_weight = 0.65 when translating SPL performance to global signal.

  EXCEPTION — SPECIFIC HIGH-VISIBILITY MILESTONES:
  Ronaldo 900 career goals: full signal (milestone is cumulative, not league-specific)
  Benzema 500 career goals: full signal (legacy achievement)
  Individual records that are career-level, not league-level: no discount.
```

---

## Availability Modifier — Injury Patterns

```
SPL-SPECIFIC INJURY RISK FACTORS:

  HEAT-RELATED INJURY ELEVATION:
    Risk window: August–September (pre-acclimatisation)
    Players at risk: first-season European signings, players 30+
    Elevated risk: muscle injuries (hamstring, calf) — heat affects muscle fibres
    Modifier: heat_injury_risk_modifier = ×1.15 (15% elevated injury probability)
              applies to all European signings in first August–September in SPL
    
  POST-ACCLIMATISATION:
    After full season in SPL: return to baseline injury risk
    3+ seasons in SPL (Ronaldo): no heat modifier applied

  LOAD MANAGEMENT — HIGH-WAGE SIGNINGS:
    PIF clubs have incentive to protect high-value contracts.
    Rotation and rest are more common than in European clubs under pressure.
    Modifier implication: high-profile SPL signings have lower match availability
    % than equivalent European players, but lower season-ending injury risk.
    Apply load_management_modifier = 0.90 availability to signings 30+.

  TRAVEL FATIGUE:
    International break travel: Riyadh to Europe/South America = 7–12h flight.
    Post-international break dip: 2 SPL matches.
    Modifier: post_international_break_modifier = 0.92 (consistent with global norm).

COMPOSITE MODIFIER RANGE — SPL ATHLETE INTELLIGENCE:

  Elite European signing, fully fit, peak form:    1.40–1.50 (Ronaldo ceiling)
  Elite European signing, fit, good form:          1.20–1.35
  Elite European signing, fit, moderate form:      1.00–1.20
  Elite European signing, managing load:           0.85–1.00
  Elite European signing, heat/travel risk:        0.80–0.92
  Elite European signing, injury doubtful:         0.70–0.82
  High-profile signing absent (confirmed):         0.55–0.75

  BASELINE (no high-profile European signing in squad): 1.00
  SPL domestic player contribution: no modifier adjustment above 1.05
  (domestic SPL players do not drive global fan token signals)
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| High-profile signing fully fit, top form (Ronaldo/Neymar calibre) | ×1.40–1.50 |
| High-profile signing fit, good form | ×1.20–1.35 |
| High-profile signing fit, moderate form | ×1.00–1.20 |
| High-profile signing managing load | ×0.85–1.00 |
| Heat/travel risk window (Aug–Sep, first season) | ×0.80–0.92 |
| High-profile signing doubtful / injury concern | ×0.70–0.82 |
| High-profile signing confirmed absent | ×0.55–0.75 |
| No high-profile European signing in squad | 1.00 |

---

## Integration example

### Pre-match workflow — PIF Derby (Al Nassr vs Al Hilal)

```
1. Load: sports/football/sport-domain-football.md           (base domain)
2. Load: sports/football/sport-domain-football-saudi-pro-league.md (SPL context)
3. Load: athlete/football/athlete-intel-football.md         (base commands)
4. Load: athlete/football/athlete-intel-saudi-pro-league.md (this file)

5. get_key_player_availability(Al Nassr)
   → Check Ronaldo availability first
   → If Ronaldo FIT: ATM = ×1.50
   → If Ronaldo ABSENT: ATM = ×0.65

6. get_key_player_availability(Al Hilal)
   → Check Neymar availability (assume unavailable until Tier 1 confirmed)
   → If Neymar FIT: ATM = ×1.45
   → If Neymar ABSENT: ATM = ×0.90 (Al Hilal squad depth modifier)

7. get_athlete_signal_modifier(both_clubs)
   → Apply composite SPL modifier
   → Apply heat_risk_modifier if Aug–Sep
   → Apply ramadan_modifier if applicable

8. Generate pre-match signal with SPL-adjusted weights
   broadcast_reach_modifier = 0.90 (PIF derby)
```

---

## get_athlete_signal_modifier

```
COMMAND: get_athlete_signal_modifier(club, player_name, condition)

USAGE:
  get_athlete_signal_modifier("Al Nassr", "Ronaldo", "fit")     → 1.50
  get_athlete_signal_modifier("Al Nassr", "Ronaldo", "absent")  → 0.65
  get_athlete_signal_modifier("Al Hilal", "Neymar", "unconfirmed") → 0.85
  get_athlete_signal_modifier("Al Ittihad", "Benzema", "fit")   → 1.35
  get_athlete_signal_modifier("Al Nassr", "squad", "baseline")  → 1.00

NOTE: SPL domestic players do not have named modifier entries.
Apply squad_baseline = 1.00 for non-high-profile player analysis.
```

---

## Compatibility

**Extends:** `athlete/football/athlete-intel-football.md`
**Sport:**   `sports/football/sport-domain-football-saudi-pro-league.md`
**Market:**  `market/market-saudi-pro-league.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Saudi Pro League athlete intelligence: star player signals, acclimatisation, and PIF acquisition context |
| Reasoning | ACTIVE | SPL reasoning chain from player signals to APS modifier in Saudi context |
| Context | ACTIVE | SPL context: heat conditions, playing standard adjustment, star player motivation signals |
| Memory | ACTIVE | Historical SPL player performance patterns post-transfer from European leagues |
| Judgment | ACTIVE | Judgment on SPL signal — motivation and acclimatisation are primary SPL-specific signals |
| Attention | ACTIVE | Elevated attention for star player form signals and match fitness declarations |
| Communication | ACTIVE | SPL athlete output with APS modifier, acclimatisation stage, and motivation signal |
| Verification | ACTIVE | SPL data from Saudi Football Federation official sources |
| Learning | ACTIVE | SPL APS calibration developing — limited data on post-transfer performance baselines |
| Integration | ACTIVE | Integrates with market-saudi-pro-league and sports/football/sport-domain-football-saudi-pro-league |
| Calibration | EMERGING | SPL APS modifier calibration is developing — limited pre-2023 data |
| Adaptation | ACTIVE | SPL athlete intelligence adapts as playing standards and star player profiles evolve |
| Ethics | NOT APPLICABLE | SPL athlete intelligence is sports analysis — no ethical dimension |
| Transparency | ACTIVE | APS modifier, acclimatisation stage, and motivation signal source explicit in output |


---

*SportMind v3.97.8 · MIT License · sportmind.dev*
*Saudi Pro League Athlete Intelligence — Layer 2*
