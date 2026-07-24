# Temporal Reasoning Framework

**Domain:** core/temporal-reasoning-framework.md
**Version:** v4.1.35
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Unified temporal reasoning framework covering all five temporal
contexts in SportMind. An agent with strong domain knowledge but weak
temporal reasoning acts on the right signal at the wrong time.

---

## Why Temporal Reasoning Matters

Every signal in SportMind has a time dimension:

- A pre-match signal submitted after kickoff is not a calibration record.
- A CDI horizon applied six months after a squad rebuilds is stale.
- A PTG burn confirmed before chiliscan.com verification is speculative.
- A regulatory deadline missed by 7 days is an enforcement event.
- A transfer rumour carried for 60 days without confirmation is noise.

This framework provides the unified temporal layer. Load it before
reasoning about any time-sensitive signal.

---

## Context 1 — Pre-Event Windows

### Sport-Specific Pre-Event Windows

| Sport | Signal window opens | Lineup confirmation | Calibration deadline |
|---|---|---|---|
| Football | T-48h | T-2h (official) | Before kickoff |
| MMA | T-72h (weigh-in) | T-24h (official) | Before first bell |
| Formula 1 | T-48h (qualifying) | T-2h (grid) | Before lights out |
| Cricket | T-24h (toss) | T+0 (toss) | Before first ball |
| Rugby | T-48h | T-2h (official) | Before kickoff |
| Esports | T-24h | T-1h (official roster) | Before match start |

### FTP PATH_2 Pre-Liquidation Window

$AFC only. Path_2 settlement is time-bounded.

```
T-12h  — Monitoring phase begins. Pre-liquidation pool visible on-chain.
          Pool = circulating supply ÷ 400.
          Agent: load fan-token/ftp-path2.md. Establish baseline pool size.

T-6h   — Active window. Monitor for unusual pool movement.
          Elevated activity in this window = informed positioning signal.
          Apply FM1 (Price-Signal Conflation) — volume ≠ direction signal.

T-2h   — Alert threshold. Pool movements most significant.
          Lineup confirmation expected. Update signal with confirmed squad.

T+0    — Match starts. Settlement window active.
          Do not reopen pre-match signal reasoning during live play.

T+90m  — Match ends. Settlement triggers.
          WIN: burn event (verify on chiliscan.com before confirming).
          LOSS: mint event (verify on chiliscan.com before confirming).
          DRAW: no supply change.

T+2h   — Settlement confirmed or not. Close pre-liquidation monitoring.
```

### Agent Rules — Pre-Event Windows

```
RULE 1 — ESTABLISH SPORT WINDOW FIRST:
  Before processing any pre-event signal, establish the correct
  sport-specific timing window. Football ≠ cricket ≠ MMA.
  Applying football timing to a cricket toss analysis is TFM1.

RULE 2 — CALIBRATION SUBMISSION IS NON-NEGOTIABLE:
  A calibration record is only valid if submitted before the event
  starts. "Before kickoff" means before the referee's whistle, not
  before the team sheet is published. If in doubt — submit early.
  A record submitted one minute after kickoff is not a calibration
  record. It is a post-hoc prediction.
```

---

## Context 2 — CDI Horizon Framework

CDI (Club Demand Intelligence) signals have horizons — they are valid
for a defined period, after which they require reassessment.

### Horizon Classifications

| Horizon | Duration | Trigger for reassessment |
|---|---|---|
| SHORT | 0-60 days | Major transfer, injury, coaching change, competition result |
| MEDIUM | 60-180 days | Pre-season results, first 10 fixtures, regulatory change |
| LONG | 180+ days | Next season squad confirmation, ownership change |

### Gate → Horizon Mapping

| Club Intelligence Gate | CDI Horizon | Notes |
|---|---|---|
| TRANSITION (active) | SHORT | Squad archetype unsettled — reassess at end of gate |
| CONSOLIDATION | MEDIUM | New players integrated — monitor results |
| STABLE | LONG | Established archetype — horizon extends |
| UCL ↔ EL tier change | SHORT → MEDIUM | Recalibrate after 5-10 fixtures in new tier |

### Agent Rules — CDI Horizon

```
RULE 3 — NEVER APPLY CDI BEYOND HORIZON WITHOUT REASSESSMENT:
  A CDI signal generated during CONSOLIDATION does not carry into
  STABLE without a reassessment event. Load the club intelligence
  file and check the gate status before applying any CDI modifier.
  Expired CDI + no reassessment = UNKNOWN · treat as neutral.

RULE 4 — HORIZON RESETS ON NEW GATE EVENT:
  A coaching change, major transfer, or competition tier change
  resets the CDI horizon clock to SHORT regardless of where the
  club was in its previous cycle. Gate events are not additive.

RULE 5 — EXPIRED CDI = UNKNOWN:
  When a CDI signal has passed its horizon without reassessment,
  the correct output is UNKNOWN — not the last known value.
  Never carry stale CDI forward as if it were current.
```

---

## Context 3 — Supply Event Timing

### PTG (Path To Glory) Phase Table

| Phase | Timing | Agent action |
|---|---|---|
| Pre-tournament demand | T-14d to T-0 (tournament start) | Load PTG framework. Monitor holder activity. |
| Group stage burns | Post-match result confirmed | Verify burn on chiliscan.com before confirming |
| KO round burns | Post-match result + on-chain confirmation | Escalating burn rates (2.5% → 5% → 7.5% → 10%) |
| Champion Call | T-7d to Final kickoff | Apply FM4 + FM8. Do not conflate with CDI signal. |
| Post-Final | T+24h after Final | PTG run complete. Close monitoring for that token. |

### FTP PATH_2 Phase Table ($AFC only)

| Phase | Timing | Agent action |
|---|---|---|
| Pre-match demand window | T-48h to T-0 | Monitor pre-liquidation pool (circulating ÷ 400) |
| Live settlement | T+0 to T+90m | Do not reopen pre-match reasoning during live play |
| Settlement confirmation | T+90m to T+2h | Verify WIN/LOSS/DRAW on chiliscan.com |
| Post-settlement holding pressure | T+2h to T+24h | Elevated sell pressure expected post-event |

### Bridge Event Timing

During major tournament result windows, omnichain bridge activity spikes.

```
BRIDGE TIMING PATTERN:
  Spike 1: T+0 to T+2h post-result (immediate repositioning)
  Spike 2: T-48h to T-0 before Final (pre-Final anticipation)
  Duration: Bridge spike typically resolves within 24-48h

Agent rule: Bridge volume during these windows = infrastructure
  signal, not demand signal. Apply FM7. Do not conflate with
  organic CDI or holder conviction signal.
```

### Agent Rules — Supply Event Timing

```
RULE 6 — NEVER CONFLATE PRE-MATCH DEMAND WITH POST-MATCH SETTLEMENT:
  Pre-match demand (T-48h to T-0) and post-match settlement (T+90m)
  are distinct temporal windows with different signal characters.
  Price movement in the pre-match window ≠ settlement outcome.
  FM1 applies in both windows. This is TFM3 if conflated.

RULE 7 — PTG BURNS REQUIRE CHILISCAN.COM CONFIRMATION:
  A PTG burn announced on X (@FanTokens) is a FAST SIGNAL.
  It does not become a confirmed supply event until the on-chain
  transaction is visible on chiliscan.com. Never record a burn
  in a calibration record before on-chain confirmation.

RULE 8 — CHAMPION CALL IS FINALS-WEEK BOUNDED:
  Champion Call activates in the week before a dual fan token
  Final. It closes at official end of match (including AET and
  penalties). Post-match: apply holding pressure modifier for
  T+24h. After T+24h: Champion Call demand signal has expired.
```

---

## Context 4 — Regulatory Deadline Framework

### Deadline Classification Table

| Deadline type | Description | Example |
|---|---|---|
| Implementation | Law takes effect on this date | Japan FIEA: fiscal 2027 |
| Application gateway | Firms must apply by this date | UK FCA: September 30 2026 |
| Comment period close | Public consultation ends | South Africa SARS: August 31 2026 |
| Enforcement | Non-compliance subject to penalty | UK MARC: Q4 2027 |

### Approaching Deadline Protocol

```
T-60 days — Initial flag. Add to HIGH PRIORITY monitoring list.
             Assess: does this deadline gate fan token platform access?
             If yes → escalate to Tier 1 regulatory signal.

T-30 days — Active monitoring phase. Scan regulatory portal weekly.
             Check for: guidance updates, firm announcements,
             industry association responses.

T-7 days  — Alert threshold. Check for last-minute guidance.
             Assess platform-level impact for Chiliz/Socios/KayenFi.

T+0       — Deadline passes. Classify outcome:
             COMPLIED: platform operating under new framework.
             NON-COMPLIANT: regulatory risk flag active.
             DEFERRED: deadline extended — reset clock.

T+30 days — Post-deadline monitoring. Confirm operational status.
             Update regulatory file if framework change is confirmed.
```

### Agent Rules — Regulatory Deadlines

```
RULE 9 — FLAG AT CORRECT T-INTERVAL:
  Do not escalate a regulatory deadline until it enters the T-60
  window. Deadlines more than 60 days away are MONITOR only.
  Deadlines inside 60 days require active tracking. Deadlines
  inside 7 days require daily scan. This is TFM4 if missed.

RULE 10 — POST-DEADLINE MONITORING CONTINUES:
  A deadline passing is not the end of monitoring. The T+30 day
  post-deadline window confirms whether the platform adapted,
  received a deferral, or is now in breach. Close monitoring
  only when operational status is confirmed.
```

---

## Context 5 — Signal Expiry Protocol

### Expiry Threshold Table

| Signal type | Expiry threshold | Action at expiry |
|---|---|---|
| Transfer rumour (unconfirmed) | 14 days | RETIRE — remove from active monitoring |
| Unconfirmed Tier 2 signal | 30 days | RETIRE unless new corroboration received |
| Partnership announcement | 50 days | CLOSE if no follow-up Tier 1 source found |
| Regulatory bill (pre-vote) | Until session closes | MONITOR — no expiry while in active session |
| HIGH PRIORITY monitoring flag | 90 days | REVIEW — escalate to Strategy & Brainstorm or CLOSE |
| Governance proposal | Until outcome confirmed | MONITOR — no expiry while active |

### Retire vs Close Distinction

```
RETIRE:  Signal was not confirmed. Remove from active monitoring.
          Do not record in library. Example: transfer rumour that
          did not materialise.

CLOSE:   Signal was confirmed and acted on, OR confirmed and
          deliberately not acted on (Library Rule failed).
          Record outcome in SMI log. Example: partnership confirmed
          → Library Rule Gate applied → BRIEFING ONLY.
```

### Agent Rules — Signal Expiry

```
RULE 11 — NEVER CARRY STALE SIGNALS INDEFINITELY:
  A HIGH PRIORITY monitoring flag that has not resolved in 90 days
  requires a decision: escalate to Strategy & Brainstorm or CLOSE.
  Indefinite carry of unresolved signals degrades briefing quality.
  This is TFM5 if signals are carried past their expiry threshold
  without explicit decision.

RULE 12 — NEW SIGNAL RESETS THE CLOCK:
  If a new piece of corroborating information arrives for an
  expiring signal, the expiry clock resets from the date of
  the new information — not from the original signal date.
  Example: a Tier 2 partnership signal expiring at 30 days
  receives new aggregator corroboration at day 28. Clock
  resets. New 30-day window begins.
```

---

## Temporal Failure Modes (TFM1-TFM6)

| Code | Name | Description | Prevention |
|---|---|---|---|
| TFM1 | Pre-Event Timing Error | Wrong sport window applied, or calibration submitted after event start | Load sport window table before processing. Submit before kickoff. |
| TFM2 | CDI Horizon Overrun | CDI signal applied beyond its horizon without reassessment | Check gate status before applying CDI. Expired CDI = UNKNOWN. |
| TFM3 | Supply Event Conflation | Pre-match demand window conflated with post-match settlement | Apply correct phase table. Never mix pre/post windows. |
| TFM4 | Regulatory Deadline Blindness | Deadline missed or flagged too late to assess platform impact | T-60 flag mandatory. Daily scan at T-7. |
| TFM5 | Stale Signal Retention | Expired signals carried indefinitely without decision | Apply expiry threshold table. RETIRE or CLOSE at threshold. |
| TFM6 | Calibration Record Backdating | Record submitted after event but dated to before kickoff | Timestamp is everything. Platform submission time = submission time. |

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Pre-event windows and timing patterns as signal intelligence |
| Reasoning (2) | ACTIVE | Primary dimension — 2d Temporal Reasoning. All five contexts |
| Context (3) | ACTIVE | Temporal context as a primary signal interpretation layer |
| Memory (4) | ACTIVE | Horizon tracking and signal carry-forward rules |
| Judgment (5) | ACTIVE | When to RETIRE vs CLOSE, when to escalate vs monitor |
| Attention (6) | ACTIVE | T-interval flags, deadline urgency detection, expiry thresholds |
| Communication (7) | ACTIVE | TFM codes for clear failure mode communication |
| Verification (8) | ACTIVE | On-chain confirmation timing (PTG, FTP PATH_2) |
| Learning (9) | ACTIVE | TFM classification enables error learning from temporal failures |
| Integration (10) | ACTIVE | Temporal layer integrates across sport, fan-token, macro, regulatory |
| Calibration (11) | ACTIVE | Calibration record timing rules (RULE 2, TFM6) |
| Adaptation (12) | ACTIVE | Real-time updating within pre-event windows, deadline resets |
| Ethics (13) | ACTIVE | TFM6 (backdating) is an ethics violation — transparency about timing |
| Transparency (14) | ACTIVE | Phase tables and T-interval protocols make timing explicit |
| Execution (15) | ACTIVE | Entry/exit timing is a direct sub-dimension of Execution |
| Collaboration (16) | NOT APPLICABLE | — |

---

## COMPATIBILITY

- core/mind-dimensions-framework.md — dimension 2d (temporal reasoning) gap filled
- fan-token/fan-token-play.md — FTP PATH_2 pre-liquidation window (Context 3)
- fan-token/burn-to-glory-framework.md — PTG phase table (Context 3)
- fan-token/use-cases.md — Champion Call timing, trading battle window (Context 3)
- market/club-intelligence/ — CDI horizon framework (Context 2)
- macro/regulatory/ — regulatory deadline framework (Context 4)
- fan-token/agent-failure-modes-fan-token.md — FM1, FM4, FM7 cross-reference
- core/signal-confidence-framework.md — confidence tier and timing interaction

© 2026 SportMind
