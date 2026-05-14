---
name: legislation-process-intelligence
description: >
  Enduring reasoning framework for how legislation moves from proposal to enacted
  law and how each stage affects market access and modifier weights. Applies to
  any jurisdiction and any bill affecting fan tokens or digital assets. The
  framework is permanently true; specific bill status is expiring data.
---

# Legislation Process Intelligence

**How to reason about legislation at each stage of its journey.**
The framework is enduring. Scheduled dates and current vote counts are expiring data.

> Load alongside: `macro/clarity-act-complete-framework.md` (CLARITY Act application)
> Load alongside: `macro/macro-regulatory-sportfi.md` (enacted jurisdiction status)

---

## The Library Rule for legislation

```
ENDURING vs EXPIRING in legislative context:

  ENDURING (belongs in library):
    How each stage of a bill's journey affects modifier weights
    How enforcement versus existence changes signal reliability
    Which jurisdictions to monitor and why
    Cross-jurisdictional conflict resolution principles

  EXPIRING (does not belong):
    Specific vote counts or vote dates
    Named politicians and their positions
    Committee hearing schedules
    Current bill status updates

  AGENT RULE:
    When a legislation signal arrives, apply the stage framework below.
    Fetch the current status at query time from primary sources.
    Apply the enduring modifier weight for that stage.
```

---

## Legislative stage framework

```
EIGHT-STAGE SIGNAL WEIGHT FRAMEWORK:

  Stage               Signal description                     Modifier weight
  ─────────────────────────────────────────────────────────────────────────
  1. Discussion draft  Direction signalled, nothing stable    ×0.25
  2. Formally introduced Bill in the system; monitored       ×0.40
  3. Committee markup  Provisions becoming more stable       ×0.60
  4. Committee passage Higher enactment probability          ×0.75
  5. Full chamber pass Near-confirmed modifiers applicable   ×0.85
  6. Both chambers     Enactment highly probable             ×0.95
  7. Enacted into law  Confirmed modifier values             ×1.00
  8. Implementation    Varies by rulemaking progress         see below

  HOW TO APPLY:
    Identify the current stage from primary sources at query time.
    Multiply the relevant modifier value by the stage weight.
    Example: CLARITY Act joint rulemaking modifier (×0.94) at committee passage stage:
      Effective weight = ×0.94 × ×0.75 = ×0.705 on US market signals

  IMPLEMENTATION STAGE (Stage 8) — RULEMAKING UNCERTAINTY:
    Laws take effect through implementing regulations (rulemakings).
    Until implementing regulations are effective:
      Apply: rulemaking_uncertainty_modifier = ×0.85 to enacted law modifiers
    When regulations become effective:
      Apply full enacted modifier (×1.00 × regulation stage = full effect)
      
  BIPARTISAN SIGNAL:
    Legislation with confirmed bipartisan support crosses stages faster.
    Bipartisan bill at Stage 3: upgrade signal weight to ×0.70 (not ×0.60).
    Historical reference: GENIUS Act passed Senate 68-30 — indicates
      bipartisan crypto legislation is achievable in current US Senate.
```

---

## Cross-jurisdictional conflict resolution

```
WHEN TWO JURISDICTIONS HAVE CONFLICTING FRAMEWORKS:

  SCENARIO: Token is accessible in both Jurisdiction A and B.
    A has permissive framework (positive modifier).
    B has restrictive framework (negative modifier).
    
  RESOLUTION PRINCIPLE:
    Apply the more restrictive framework as the binding signal for the
    specific holder-platform combination.
    
  EXAMPLE:
    USDT unrestricted in UAE (×1.00)
    USDT restricted for retail in EU for certain use cases (×0.95 modifier)
    An EU-based holder on an EU-regulated platform: apply ×0.95.
    A UAE-based holder on a UAE-regulated platform: apply ×1.00.
    
  IRRECONCILABLE CONFLICT:
    If two enacted frameworks directly contradict each other for the same
    holder-platform combination with no clear resolution:
    Apply: HOLD signal for the affected jurisdiction.
    Reason: conflicting regulatory signals make directional assessment unreliable.
    
  AGENT RULE:
    Always assess holder-platform combination, not just the token or jurisdiction
    in isolation. The binding framework is determined by both factors together.
```

---

## Enforcement versus existence

```
THREE ENFORCEMENT STATES — SIGNAL RELIABILITY:

  LAW ENACTED, ENFORCEMENT ACTIVE:
    Apply: full modifier weight (×1.00 on the stage modifier)
    This is the baseline for all enacted law signals.
    
  LAW ENACTED, ENFORCEMENT APPROACH UNCLEAR:
    Apply: enforcement_uncertainty_modifier = ×0.75
    Common in early implementation phases before agency guidance is issued.
    
  LAW ENACTED, ENFORCEMENT ABSENT OR CONFIRMED SUSPENDED:
    Apply: enforcement_absent_modifier = ×0.50
    Law exists but is not being applied — signals are unreliable.
    Example: enforcement moratorium during implementation period.
    
  HOW TO ASSESS ENFORCEMENT LEVEL:
    Primary signals: agency enforcement actions, published guidance, staff statements
    Source: regulator's official enforcement tracker or press release section
    Secondary signals: industry compliance behavior — are platforms self-complying?
    
  PROVISIONAL COMPLIANCE PERIOD:
    Many digital asset laws include a provisional compliance period during which
    existing operators can continue operating while obtaining registration.
    During provisional period: treat as ENFORCEMENT_ACTIVE for compliant platforms,
    ENFORCEMENT_UNCLEAR for non-compliant platforms.
```

---

## Missing jurisdictions to monitor

```
JURISDICTIONS WITH MATERIAL FAN TOKEN EXPOSURE BUT NOT YET DOCUMENTED:

  INDIA (HIGH PRIORITY — not modelled):
    One of the largest potential fan token markets globally.
    Complex evolving crypto legislation — GST on crypto, TDS requirements.
    Primary regulators: RBI (Reserve Bank of India), SEBI (Securities regulator)
    Fan token angle: cricket fan token potential enormous (IPL fanbase ~400M)
    Monitor: RBI circulars, SEBI crypto consultation papers, Finance Ministry budgets
    Gap severity: HIGH — India absence from framework underestimates global demand
    
  NIGERIA (MEDIUM PRIORITY — not modelled):
    Largest crypto market in Africa by volume.
    Significant football fan token interest — PSG, Barcelona among most held.
    Primary regulator: CBN (Central Bank of Nigeria), SEC Nigeria
    Monitor: CBN crypto policy statements, SEC Nigeria virtual assets framework
    
  INDONESIA (MEDIUM PRIORITY — not modelled):
    Active Chiliz market — Bali United has had token presence.
    OJK (Financial Services Authority) framework for digital assets evolving.
    Monitor: OJK digital asset licensing updates
    
  AUSTRALIA (MEDIUM PRIORITY — not modelled):
    Active sports market; significant crypto user base.
    ASIC crypto regulatory framework exists and is relatively clear.
    Monitor: ASIC digital asset guidance; federal Treasury consultations
    
  Note: Oman and Kuwait ARE now documented in macro-regulatory-sportfi.md
    (added v3.97.37). The GCC is now fully mapped.
```

---

## Compatibility

**CLARITY Act application:**  `macro/clarity-act-complete-framework.md`
**Jurisdiction status:**      `macro/macro-regulatory-sportfi.md`
**Government strategy:**      `macro/government-intelligence.md`
**Exchange implications:**    `macro/exchange-intelligence.md`

---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Stage framework is enduring — specific vote counts and dates are expiring data*
