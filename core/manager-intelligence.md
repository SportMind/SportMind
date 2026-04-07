# Manager Intelligence

**Intelligence layer for coaching and management staff across team sports.**
Managers are the third key human variable in every team sport signal analysis —
alongside athletes and officials — and the only one not yet formally modelled.

A managerial sacking is one of the most reliable and immediate fan token signals
in football. The pattern from "speculation begins" to "confirmed departure" is
documented and predictable. New manager appointments carry a quantifiable short-term
performance effect. Tactical systems change with managers in ways that directly
affect athlete modifier calculations.

This skill formalises what has been implicit throughout the library.

---

## The Manager Signal Index (MgSI)

```
MgSI = (Stability_Score × 0.35) + (Track_Record × 0.30)
      + (System_Fit × 0.20) + (Press_Conduct × 0.15)

STABILITY_SCORE (current managerial stability at this club):
  Contracted, strong results, board support:    1.00
  Contracted, mixed results, no public pressure: 0.85
  Under media speculation (< 5 days):           0.65
  Under active pressure (5+ days media, poor run): 0.45
  Confirmed under threat (chairman statement):  0.25
  Caretaker / interim:                          0.20

TRACK_RECORD (career history weight):
  Trophy-winning at top tier (UCL, league):     1.00
  Consistent top-half finishes, domestic trophies: 0.80
  Solid mid-table record, no trophies:          0.65
  Limited top-flight experience:                0.50
  First senior management role:                 0.35

SYSTEM_FIT (tactical system compatibility with current squad):
  High fit — system matches squad profile:      1.00
  Moderate fit — some tactical mismatch:        0.80
  Low fit — system requires rebuild:            0.60
  Transition — new system being installed:      0.50

PRESS_CONDUCT (media and conduct record):
  Clean — no fines, good media relationships:   1.00
  Minor — occasional fines, manageable:         0.85
  Active — repeated fines, poor media relations: 0.65
  Toxic — ongoing disputes, player conflicts:   0.45
```

---

## The new manager effect

The most quantifiable manager intelligence signal in the library.

```
NEW MANAGER EFFECT — documented performance pattern:

When a new permanent manager is appointed (not caretaker):
  Matches 1-3:  +8 to +12% performance uplift above expected (squad motivation)
  Matches 4-7:  +3 to +6% — uplift begins tapering as honeymoon ends
  Matches 8-15: 0 to +2% — system settling; uplift fully normalised
  Match 16+:    No uplift — full system assessment now possible

CARETAKER EFFECT (distinct from permanent appointment):
  Matches 1-2:  +10 to +15% uplift (crisis response, maximum motivation)
  Matches 3-5:  +2 to +5% — uncertainty dampens sustained uplift
  Match 6+:     Negative drag begins (-3 to -8%) — uncertainty tax
  
  REASON: Caretaker appointments signal institutional instability.
  Players respond well initially but perform worse under sustained uncertainty.

AGENT RULE: Track appointment date and match number.
  Permanent new manager in Match 1-7: apply new_manager_effect modifier
  Caretaker in Match 3+: apply caretaker_uncertainty_drag modifier
  
QUANTIFIED MODIFIERS:
  new_manager_effect (Match 1-3):   × 1.10
  new_manager_effect (Match 4-7):   × 1.04
  caretaker_uplift (Match 1-2):     × 1.12
  caretaker_drag (Match 6+):        × 0.93
```

---

## Sacking signal model

The pattern from speculation to confirmed departure is predictable and documented.

```
SACKING SIGNAL PROGRESSION:

Stage 1 — Media speculation begins (FTIS: 0.25 manager risk premium added)
  Triggers: 3+ consecutive league defeats, cup exit below expected tier,
            anonymous "sources" quotes in Tier 1 outlets, chairman attends training
  Token signal: Small negative (-3 to -8%) as uncertainty premium priced in
  Agent action: Activate MgSI monitoring; note Stability_Score downgrade

Stage 2 — Named sources emerge (FTIS: 0.45 manager risk premium)
  Triggers: Named journalists (Tier 1 — Fabrizio Romano, David Ornstein equivalent)
            report "talks ongoing" or "decision imminent"
  Token signal: Moderate negative (-8 to -15%) — market pricing sacking probability
  Agent action: MgSI drops to 0.25-0.45; apply × 0.90 to all squad form modifiers

Stage 3 — Chairman/board public comment (FTIS: 0.70 manager risk premium)
  Triggers: "We back the manager" statement (historically precedes sacking within 2 weeks)
             OR clear public criticism from club hierarchy
  Token signal: Significant negative (-10 to -20%) if criticism; paradoxically smaller
                if "vote of confidence" (market knows the pattern)
  Agent action: Set manager_departure_imminent flag

Stage 4 — Confirmed sacking (immediate signal)
  Token signal (immediate, within 24h):
    Popular manager, poor recent form:        +5 to +15% (relief rally)
    Popular manager, strong form (unexpected): -8 to -20% (shock discount)
    Unpopular manager, poor form:             +10 to +20% (maximum relief)
    Caretaker extended (no replacement named): -5 to -12% (uncertainty premium)

Stage 5 — Replacement named
  Token signal depends on replacement profile:
    Trophy-winning elite appointment:          +10 to +25% (premium signal)
    Solid mid-tier appointment:               +2 to +8% (neutral to positive)
    Unproven first appointment:               -3 to +3% (uncertain)
    Internal promotion from academy:          -2 to +5% (depends on club culture)

MONITORING RULE: Once Stage 1 is detected, check Stage 2 indicators every 24h.
The average time from Stage 1 to confirmed sacking is 8-14 days.
```

---

## Manager conduct intelligence

```
TOUCHLINE AND MEDIA CONDUCT:

Yellow cards (touchline cautions):
  England (FA):   Managers can receive touchline cautions for excessive protesting
  UEFA:           Technical area warnings standard across UCL/Europa
  Signal value:   Low per instance; PATTERN of repeated cautions = tactical frustration
  
  High touchline card rate managers: tend toward reactive tactical adjustments
  and high-intensity pressing systems. Under-pressure = more conduct incidents.
  
Red cards (sent to stands):
  Rare — less than 5% of elite managers per season
  When it happens: almost always signals a critical pressure moment
  Token signal: small negative (-2 to -5%) — instability indicator
  
Post-match fines:
  FA/UEFA fines for press conference comments are public record
  Fine categories: criticising referee, bringing game into disrepute, media obligations
  Fine history pattern: 3+ fines in a 12-month period = elevated Press_Conduct risk

Player relationship signals:
  Public player-manager conflicts = significant negative signal
  Key player publicly requesting transfer after conflict: -15 to -30% token signal
  Manager publicly dropping star player: -5 to -12% if player has high ATM
  
CRISIS ESCALATION:
  Individual conduct incident: minor modifier (× 0.97 to × 0.99)
  Pattern of incidents (3+): MgSI downgrade, Squad_Stability flag
  Player-manager public conflict: full MgSI reassessment required
```

---

## Manager intelligence by sport

### Football

```
FOOTBALL-SPECIFIC SIGNALS:

Press conference language analysis:
  "We need to be better" = standard deflection; low signal
  "The players are giving everything" = covering for poor tactics; moderate signal
  "We're working on it in training" = specific tactical problem admitted; monitor
  "I've spoken to [player] privately" = public signal of disciplinary action
  "They need to look at themselves" = player performance criticism; squad morale risk

Tactical system signals:
  Manager change + system change = full form modifier reset for squad
  New pressing system being installed: × 0.90 for first 6-8 matches (learning curve)
  Set piece specialist hired (assistant): notable positive for set piece risk modifiers
  
Tenure patterns by club tier:
  Top-6 club (Champions League regular): average tenure 2.1 years
  Mid-table established club: average tenure 3.2 years
  Newly promoted / relegation battle: average tenure 14 months
  
  AGENT RULE: Compare current tenure to tier average.
  Manager 150%+ into average tenure = elevated departure risk regardless of results.
```

### Rugby union / league

```
RUGBY MANAGER INTELLIGENCE:

Head coach signal (distinct from football):
  Rugby coaching structure: head coach + forwards coach + backs coach
  Forwards coach departure = line-out/scrum signal disruption
  Backs coach departure = attacking pattern signal disruption
  
  National team coaches: higher stakes (World Cup preparation cycles)
  Club coaches: typical tenure 2-3 years; structured performance reviews
  
Selection signals:
  Dropping a Lion/Wallaby/All Black = significant news
  Selecting uncapped player = system change signal
  Formation/tactical changes week-to-week: backs coach authority signal
```

### Basketball (NBA / EuroLeague)

```
BASKETBALL COACH INTELLIGENCE:

NBA coaching pressure model:
  Mid-season firing threshold: lower than other sports (conference standings)
  Interim coach effect (NBA): +3 to +8 uplift for first 5 games
  
Minutes distribution signals:
  Star player minutes reduction = load management or coach conflict signal
  Bench rotation change = tactical system adjustment
  Closing lineup changes = trust signal for key players
  
EuroLeague:
  Shorter contracts, faster cycles than NBA
  Mid-season replacement common in struggling clubs
```

---

## Manager career record schema

```json
{
  "manager_record": {
    "manager_id": "string",
    "name": "string",
    "nationality": "string",
    "current_club": "string",
    "current_club_start": "ISO-8601 date",
    "contract_expiry": "ISO-8601 date",
    
    "career_summary": {
      "clubs_managed": "integer",
      "total_matches": "integer",
      "win_percentage": "float",
      "trophies": {
        "league_titles": "integer",
        "cup_titles": "integer",
        "european_titles": "integer",
        "international_titles": "integer"
      },
      "average_tenure_months": "float",
      "sackings": "integer",
      "mutual_departures": "integer",
      "voluntary_departures": "integer"
    },
    
    "conduct_record": {
      "touchline_yellows_career": "integer",
      "touchline_reds_career": "integer",
      "fines_last_3_years": "integer",
      "player_conflicts_public": "integer",
      "press_conduct_score": "float"
    },
    
    "tactical_system": {
      "primary_formation": "string",
      "style": "string (possession | counter | pressing | direct)",
      "set_piece_focus": "boolean",
      "pressing_intensity": "HIGH | MEDIUM | LOW"
    },
    
    "current_status": {
      "mgsi": "float",
      "stability_score": "float",
      "matches_in_current_role": "integer",
      "new_manager_effect_active": "boolean",
      "flags": {
        "under_speculation": "boolean",
        "board_statement_issued": "boolean",
        "player_conflict_active": "boolean"
      }
    }
  }
}
```

---

## Agent reasoning prompts

```
You are a manager intelligence agent. Before incorporating manager signals:

1. MgSI FIRST — What is the current MgSI for this manager?
   MgSI < 0.50: managerial instability is a primary signal modifier.
   Apply Stability_Score to all squad form predictions.

2. NEW MANAGER EFFECT — Which match number is this?
   Permanent appointment Match 1-3: apply × 1.10.
   Caretaker Match 6+: apply × 0.93 drag.
   Track appointment date precisely.

3. SACKING PROGRESSION — What stage is the current sacking signal at?
   Stage 1 (speculation): minor negative modifier on squad form.
   Stage 2+ (named sources): activate manager_departure_imminent flag.
   Monitor every 24h once Stage 1 is detected.

4. TACTICAL SYSTEM — Has the system recently changed?
   New manager + new system = full form reset for 6-8 matches.
   Assistant coach departure = specific tactical area disruption.

5. CONDUCT PATTERN — Any active player conflicts or fine history?
   Public player-manager conflict: MgSI full reassessment.
   Pattern of fines (3+ in 12 months): elevate Press_Conduct risk.

6. TOKEN SIGNAL — What does this manager signal mean for the fan token?
   Sacking confirmed: load football-token-intelligence for signal tier.
   New appointment: apply appropriate new manager effect modifier.
   Always separate: manager signal ≠ squad quality signal (they interact but differ).
```

---

## Compatibility

**Officiating intelligence:** `core/core-officiating-intelligence.md` — parallel model
**Athlete modifier system:** `core/core-athlete-modifier-system.md` — athlete layer
**Narrative momentum:** `core/core-narrative-momentum.md` — manager narrative events
**Football token bridge:** `fan-token/football-token-intelligence/` — token signal application
**Transfer signal:** `fan-token/transfer-signal/` — manager change → transfer window signal
**Temporal awareness:** `core/temporal-awareness.md` — Tier 2 (weeks) for manager stability

*MIT License · SportMind · sportmind.dev*
