---
name: multi-horizon-reasoning
description: >
  Enduring reasoning framework for reasoning across four time horizons: match (hours),
  season (months), multi-season (years), and market cycle (crypto cycles). Covers
  which horizon is primary for each output type and how Horizon 1 confirmed
  information overrides Horizons 2-4 pattern estimates.
---

# Multi-Horizon Reasoning

**How to reason about signals across four time horizons simultaneously.**

---

## Four time horizons

```
HORIZON 1 — MATCH (hours):
  Window: T-72h to T+2h
  Content: pre-match signal → in-match events → post-match supply event
  Primary reference: core/agent-reasoning-chains.md

HORIZON 2 — SEASON (months):
  Early season (matches 1-10):
    High uncertainty — sample too small; ×0.85 confidence on form modifiers
    Primary signal: pre-season transfer intelligence
  Mid-season (matches 11-25):
    Reliable sample; full confidence on form signals
  Late season (matches 26+):
    Motivation signals dominate — title race, relegation, European spots
    Apply motivation modifier over form in final 10 matches

HORIZON 3 — MULTI-SEASON (years):
  Sustained excellence (3+ consecutive trophies, same competition):
    Apply: ×1.05 pedigree modifier — repeatable winning culture
  Transition period (manager or squad overhaul):
    Suspend historical modifiers for first 10 matches of new era
    New data overrides old patterns
  Structural decline (declining resources, ownership uncertainty, FFP):
    Apply: ×0.85 to form signals — quality below historical baseline

HORIZON 4 — MARKET CYCLE (crypto cycles, 12-36 months):
  Early bull cycle: strongest accumulation signal; new entrants arriving
  Peak bull:        highest demand + highest manipulation risk
  Early bear:       demand decay accelerating; apply bear modifiers
  Deep bear:        only committed holders remain; low manipulation risk
  Accumulation:     smart money signal
  For current phase modifiers: load macro/macro-crypto-market-cycles.md
```

---

## Combining horizons

```
IDENTIFYING THE PRIMARY HORIZON:

  Output type                Primary horizon
  ─────────────────────────────────────────────────────────────────
  Match prediction           Horizon 1 (match)
  Season assessment          Horizon 2 (season)
  Club identity modifier     Horizon 3 (multi-season input)
  Fan token demand baseline  Horizon 4 (market cycle input)
  Full pre-match signal      H1 primary + H2/H3 as context + H4 as baseline

HORIZON CONFLICT RESOLUTION:
  Horizon 1 confirmed information overrides Horizons 2-4 pattern estimates.
  Short-term confirmed information is more reliable than long-term extrapolation.

  EXCEPTION:
    Level 1 override signals (macro override, integrity investigation, CFTC action)
    override all horizons including Horizon 1 in-match signals.
    See: core/signal-interaction-reasoning.md
```


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Multi-horizon reasoning: signals evaluated across short, medium, and long time horizons |
| Reasoning | ACTIVE | Horizon-aware reasoning: different signals have different predictive windows |
| Context | ACTIVE | Horizon context: competition calendar, signal decay rates, planning window |
| Memory | ACTIVE | Horizon baseline patterns: historical signal decay and validity windows by type |
| Judgment | ACTIVE | Judgment on which horizon is primary for a given analysis |
| Attention | ACTIVE | Attention allocation varies by horizon — short-horizon signals require immediate attention |
| Communication | ACTIVE | Multi-horizon output: signals labelled by time horizon and validity window |
| Verification | ACTIVE | Short-horizon signals require more current verification than long-horizon structural signals |
| Learning | EMERGING | Horizon decay rate learning from historical signal validity data |
| Integration | ACTIVE | Multi-horizon reasoning integrates all five layers with time-awareness |
| Calibration | EMERGING | Horizon-specific accuracy calibration is an emerging framework |
| Adaptation | ACTIVE | Horizon framework adapts as competition calendars and signal patterns evolve |
| Ethics | NOT APPLICABLE | Time-horizon analysis is structural — no ethical dimension |
| Transparency | ACTIVE | Time horizon and validity window explicit in all multi-horizon outputs |


---

*SportMind v3.97.52 · MIT License · sportmind.dev*
*Horizon 1 confirmed information overrides Horizons 2-4 pattern estimates.*
