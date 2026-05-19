---
name: regional-intelligence-j-league
description: >
  Enduring reasoning framework for J-League fan token adoption, regulatory context,
  competition structure, seasonal demand patterns, and engagement characteristics.
  Covers J-League tier structure, club commercial tiers, annual demand calendar,
  Japanese football culture signals, and how J-League results interact with
  fan token demand signals. Uses Tokyo Verdy MOU as the initial market signal.
---

# J-League Fan Token Regional Intelligence

**How to reason about fan token signals in the J-League ecosystem.**

---

## Competition structure

```
J-LEAGUE TIER STRUCTURE:
  J1 League:    Top flight — 18 clubs. Primary fan token opportunity tier.
  J2 League:    Second tier — 22 clubs. Promotion/relegation with J1.
  J3 League:    Third tier — 18 clubs. Limited fan token commercial viability.

FRANCHISED EQUIVALENT SIGNAL:
  J1 League is not franchised — promotion and relegation apply.
  This creates relegation risk signals analogous to Premier League/La Liga.
  Apply standard relegation modifier framework when J1 clubs face relegation threat.
  See: core/financial-sustainability-intelligence.md for relegation modifier values.

CONTINENTAL COMPETITION:
  AFC Champions League Elite (ACLE): highest prestige for J-League clubs
  Asian competition participation: ×1.15 demand amplifier for any active J-League token
  J1 clubs competing in ACLE signal Tier A commercial status in Japanese context.
```

---

## Club commercial tier framework

```
TIER A — NATIONAL SCALE (largest fanbases, global commercial reach):
  Clubs of this type: historically dominant clubs with national or near-national fanbase
  Commercial characteristics: kit manufacturer partnerships, strong youth academy,
    significant merchandise revenue, pan-Asian fanbase presence
  Fan token demand ceiling: HIGH — comparable to mid-tier European clubs
  CDI modifier baseline: ×1.08

TIER B — REGIONAL SCALE (strong regional fanbase, J1 established):
  Commercial characteristics: regional sponsor portfolio, strong local identity,
    consistent J1 presence, active supporter culture
  Fan token demand ceiling: MEDIUM-HIGH
  CDI modifier baseline: ×1.04

TIER C — CITY/LOCAL SCALE (newer clubs or smaller market):
  Commercial characteristics: primarily local sponsors, developing fanbase,
    growth trajectory rather than established scale
  Fan token demand ceiling: MEDIUM
  CDI modifier baseline: ×1.00

TOKYO VERDY CLASSIFICATION:
  Tier: B-to-A transition — Tokyo market position elevates ceiling above pure size
  Tokyo fanbase + founding club heritage: stronger ceiling than J1 standing alone
  Apply: Tier B baseline with ×1.04 Tokyo market premium
```

---

## Annual demand calendar

```
J-LEAGUE SEASON STRUCTURE:
  Season runs February to December (northern hemisphere winter breaks absent)
  Mid-season break: approximately July (overlaps with summer transfer window)
  This creates a different demand cycle than European clubs.

DEMAND CALENDAR:
  February — Season opener:
    Demand building ×1.08 — new season optimism
    Kit launch and squad announcement signals

  March-May — Season establishes:
    Form signals develop — apply standard form modifier framework
    AFC Champions League group stage (if qualified): ×1.12

  June-July — Mid-season:
    Transfer window activity — J-League has summer window
    International duty (Asian qualifiers, AFC competitions)
    Lower match frequency during break: mild demand dip ×0.97

  August-October — Title race / relegation battle:
    Title contention: ×1.15 demand premium for contending clubs
    Relegation battle: apply relegation modifier framework
    AFC Champions League knockout stages (if present): ×1.20

  November-December — Season conclusion:
    Championship decided — winning club: ×1.25 demand premium
    Relegation confirmed: −25 to −35% demand — same as European framework
    Off-season roster signals dominate from December
```

---

## Japanese football culture signals

```
SUPPORTER CULTURE CHARACTERISTICS:
  Ultra culture: well-organised, loud, visually distinctive supporter sections
  Family attendance: J-League has strong family demographic — broader holder base
  Club identity: strong — local identity often as important as trophy success
  Youth academy pride: Japanese clubs with elite academies command loyalty premium

ENGAGEMENT SIGNAL WEIGHTS:
  J-League club wins J1 title (first or rare):     ×1.30 demand premium
  J-League club wins J1 title (repeat):            ×1.20 demand premium
  AFC Champions League qualification confirmed:    ×1.15
  AFC Champions League title (rare):               ×1.50 — historic signal
  Relegation from J1 to J2:                        −25 to −35% demand
  Promotion from J2 to J1:                         ×1.20 demand premium

RIVALRY SIGNALS:
  Osaka Derby (Gamba v Cerezo): demand amplifier for both clubs ×1.08
  Tokyo Derby (when applicable): ×1.10 demand amplifier
  Classic rivalry fixtures: apply standard derby modifier framework
```

---

## Regulatory and market context

```
FSA FRAMEWORK (Japan Financial Services Agency):
  Digital asset regulation: established licensing regime
  Fan token classification: utility token framing — not securities (enduring)
  Compliance confidence weight: ×1.05 on all Japan demand signals
  SBI Chiliz partnership: institutional credibility signal for entire J-League ecosystem

MARKET ENTRY STAGING:
  Stage 1 — MOU / Partnership signal (current as of library compilation):
    Tokyo Verdy MOU with SBI Chiliz = ecosystem entry confirmed
    Apply: ×1.05 pipeline signal to all active tokens with Japan fanbase presence

  Stage 2 — First live J-League token launch:
    Market validation confirmed
    Apply: ×1.15 to all active tokens in Japan ecosystem

  Stage 3 — Multiple J-League clubs active:
    Market maturity signal — competitive ecosystem
    Apply standard demand framework — no additional multiplier
    Focus shifts to individual club CDI rather than ecosystem signal
```

---

## Fan token demand interaction

```
HOW J-LEAGUE SIGNALS AFFECT EXISTING ACTIVE TOKENS:

  J-League clubs with large European supporter bases (e.g. clubs that have
  produced prominent European transfer alumni): signals may carry demand
  in both Japanese and international holder communities.

  Cross-market signal: when a J-League club's star player moves to a
  European fan token club — monitor for demand transfer:
  Departing club: ×0.90 demand signal (loss of profile player)
  Receiving European club: ×1.04 Japanese market expansion signal

  WINTER TRANSFER WINDOW (January):
    J-League clubs often recruit or release in January
    Acquisition of high-profile returnee (Japanese international):
    ×1.12 demand signal — homecoming narrative resonates strongly
    in Japanese market
```

---

## Compatibility

**Japan market:**             `fan-token/regional-intelligence/japan.md`
**Relegation framework:**     `core/financial-sustainability-intelligence.md`
**Ecosystem health:**         `fan-token/ecosystem-health-intelligence.md`
**Seasonal patterns:**        `core/seasonal-intelligence.md`
**Verification:**             `fan-token/official-verification-framework.md`

---

*SportMind v3.97.59 · MIT License · sportmind.dev*
*Tokyo Verdy MOU = Stage 1 market entry. First live J-League token = Stage 2 validation signal.*
