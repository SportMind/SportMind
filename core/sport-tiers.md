# Sport Tiers — SportMind Intelligence Classification

**The tier system classifies every sport in the SportMind library by its
relationship to the fan token suite and the depth of intelligence maintained.
Tier determines calibration priority, monitoring cadence, and agent signal
weighting. Tier classification is reviewed every quarter.**

---

## Tier A — Fan Token Active

Sports with live fan tokens on Chiliz Chain or FanToken.com. Full
intelligence stack maintained at all layers. Active calibration programme.
Priority SportMind Intelligence (SMI) monitoring — changes in these sports
propagate directly to CDI, FTP, and NCSI signals for listed tokens.

```
TIER A DEFINITION:
  Condition:   Active fan token confirmed on Chiliz Chain or FanToken.com
  Intelligence: Full — all five layers loaded for signal generation
  Calibration:  Active — new records submitted and processed continuously
  Monitoring:   Priority — breaking news, squad updates, macro events
  Agent rule:   Always load Layer 1 domain skill + fan token layer for
                any query involving a Tier A sport or its fan tokens

CURRENT TIER A SPORTS (6):
  football          — Layer 1 FULL | Fan token: 37+ active tokens
  basketball        — Layer 1 FULL | Fan token: NBA teams via Chiliz
  mma               — Layer 1 FULL | Fan token: UFC fighters/events
  formula1          — Layer 1 FULL | Fan token: constructor tokens
  motogp            — Layer 1 FULL | Fan token: team tokens active
  cricket           — Layer 1 FULL | Fan token: IPL and national teams

TIER A PRIORITY WITHIN TIER:
  Football > MMA > Formula 1 > Cricket > Basketball > MotoGP
  (Ranked by volume of active fan tokens and CDI signal frequency)
```

---

## Tier B — Fan Token Adjacent

Sports with no current fan token but with a credible near-term prospect of
one launching, or with strong structural alignment to the fan token model
(large addressable fanbases, existing digital engagement, or commercially
active clubs in the Socios / Chiliz partner pipeline). Existing domain
intelligence is maintained and updated. Monitor for new token launches.

```
TIER B DEFINITION:
  Condition:   No active fan token — but strong launch probability
  Intelligence: Full domain skill maintained (Layer 1 + Layer 2)
  Calibration:  Maintained — existing records valid; no active expansion
  Monitoring:   Standard — token launch watch active
  Agent rule:   Load Layer 1 domain skill for sport signals.
                If a new fan token launches, immediately reclassify to
                Tier A and run Phase 1 CDI baseline protocol within 72h.

CURRENT TIER B SPORTS (5):
  rugby-union       — Large global fanbase, premiership clubs Chiliz-adjacent
  tennis            — ATP/WTA commercial scale; individual player tokens possible
  athletics         — World Athletics; national federation token potential
  esports           — Multiple game titles with existing token activity via Chiliz
  rugby-league      — Super League; regional fanbase with digital engagement

TIER B PROMOTION TRIGGERS:
  Any confirmed fan token announcement from Chiliz, Socios, or FanToken.com
  for a Tier B sport → immediately reclassify to Tier A
  Apply new_fan_token event type in Intelligence Listener:
    event_type: "new_fan_token" → tier_upgrade: "B → A"
  Load fan-token-lifecycle.md Phase 1 protocol within 72h of launch
```

---

## Tier C — Stub Sports

Sports with minimal fan token connection and no credible near-term launch
prospect. Stub files are maintained in the library to ensure complete
sports coverage and to support future community contributions. No active
calibration priority. No SMI monitoring for fan token signals.

```
TIER C DEFINITION:
  Condition:   No active fan token and low near-term launch probability
  Intelligence: BASIC stub maintained (see BASIC tier spec in templates/)
  Calibration:  None — calibration records accepted but not prioritised
  Monitoring:   None — no SMI monitoring for token signals
  Agent rule:   Load Layer 1 domain skill for sport-specific signals only.
                Do not load fan token layer — no relevant intelligence.
                Flag any fan token news as Tier 2 for human review.

CURRENT TIER C SPORTS (32):
  afl               american-football   badminton
  baseball          boxing              curling
  cycling           darts               fencing
  field-hockey      golf                gymnastics
  handball          horse-racing        ice-hockey
  judo              kabaddi             nascar
  netball           rowing              sailing
  snooker           squash              swimming
  swimming-open-water  table-tennis     taekwondo
  triathlon         volleyball          weightlifting
  winter-sports

TIER C PROMOTION TRIGGERS:
  Same as Tier B → any confirmed fan token launch triggers immediate
  promotion to Tier A (bypassing Tier B if already at full launch).
  Long-term commercial pipeline signals may warrant Tier C → B upgrade
  at quarterly review — requires Tier 2 confirmation from a credible source.
```

---

## Quarterly tier review

```
REVIEW SCHEDULE:
  Frequency: Every quarter (January, April, July, October)
  Trigger:   Also triggered by any confirmed fan token launch or termination

PROMOTION CRITERIA (upgrade to higher tier):
  Tier C → B:  Confirmed commercial pipeline signal from Chiliz/Socios
               (e.g. partnership announcement, pilot programme confirmed)
               OR sport reaches 1M+ active digital engagement milestone
  Tier B → A:  Confirmed live fan token on Chiliz Chain or FanToken.com
               (Tier 1 source only — official announcement required)
  
DEMOTION CRITERIA (downgrade to lower tier):
  Tier A → B:  Fan token confirmed delisted or expired with no replacement
               confirmed. Suppress fan token signals; maintain domain skill.
  Tier B → C:  No fan token launch signal in 12+ months; commercial pipeline
               explicitly abandoned or no update for 4 consecutive quarters.

REVIEW AUTHORITY:
  Tier changes are recorded in CHANGELOG.md as a ### Changed entry.
  Tier A ↔ B changes require a Tier 1 source confirmation.
  Tier B ↔ C changes require a Tier 2 source and a rationale note.
  No tier change is ever applied automatically — human confirmation required.
```

---

## Integration with Intelligence Listener

```
INTELLIGENCE LISTENER ROUTING BY TIER:

  Tier A events:    Always Tier 1 (act immediately)
    new_fan_token:  Tier 2 sport → Tier A reclassification required
    path2_activation, cdi_spike, governance_proposal: standard routing
    injury_confirmed for Tier A sport: Tier 2 (high signal for CDI)

  Tier B events:    Tier 2 (review required)
    new_fan_token:  IMMEDIATE — triggers B → A reclassification
    token_partnership: Tier 2 — confirm before acting

  Tier C events:    Tier 3 (context only)
    new_fan_token:  Tier 2 — unexpected; requires verification
    All others:     Log only; no CDI or FTP impact
```

---

## SMI monitoring cadence

```
SPORTMIND INTELLIGENCE (SMI) MONITORING SCHEDULE:

  Tier A (Priority):
    Breaking news check:    Every 1h during active season
    Squad/athlete updates:  Daily at 08:00 UTC
    Fan token CDI check:    Every 4h (macro + on-chain)
    WC2026 window (June–July 2026): Every 1h for all Tier A national tokens

  Tier B (Standard):
    Token launch watch:     Daily
    Domain skill freshness: Monthly check
    No CDI monitoring:      Tier B sports have no active token signal

  Tier C (Minimal):
    Stub file review:       Quarterly only
    Token launch watch:     Monthly scan only
    No active monitoring:   Tier C sports are community contribution territory
```

---

## Compatibility

**Extends:** `core/external-intelligence-intake.md` — three-tier intake system
**Used by:** `scripts/sportmind_listener.py` — event routing by sport tier
**Related:** `fan-token/fan-token-layer-overview.md` — fan token skill map
**Templates:** `templates/template-new-sport-skill.md` — for Tier C expansion

---

*SportMind v3.96.9 · MIT License · sportmind.dev*
*Tier classification reviewed quarterly — January, April, July, October.*
