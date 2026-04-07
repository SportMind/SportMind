# App 4 — Sports Brand Token Strategy Tool

**A pre-launch due diligence platform for sports clubs, federations, and sports agencies
evaluating whether and how to launch a fan token — using SportMind's commercial stack
to model expected commercial value, lifecycle trajectory, and partnership health.**

---

## The problem this solves

Clubs and federations considering a fan token partnership with Chiliz/Socios or
building their own token product are making a significant commercial decision with
limited analytical tools. Most evaluations are based on: competitor clubs already
having tokens (social proof), projected listing revenue (misleading), and vague
"fan engagement" claims. None of this answers the questions that actually determine
whether a token product succeeds.

SportMind contains the framework to answer those questions rigorously:
- Is this sport at a commercial tier where tokens make sense right now?
- What lifecycle phase would this club's token enter at launch?
- What is the expected LTUI given the club's competition level and fanbase?
- What does a healthy partnership look like — and what are the termination signals?
- Is there a regulatory gating issue in this club's primary market?

---

## Target users

**Primary:** Sports clubs (Tier 2-4) evaluating their first fan token partnership.

**Secondary:** Sports agencies advising clubs on digital asset strategy.

**Tertiary:** Chiliz/Socios partner development teams evaluating potential club partners.

**Quaternary:** Investors evaluating sports token opportunities for their portfolio.

---

## Core value proposition

> *"Before you sign with Chiliz, know exactly what LTUI your token can achieve,
> what your partnership health score will look like in 18 months, and whether
> your primary market's regulatory environment will let your holders participate."*

The PHS (Partnership Health Score) is the core differentiator. Most clubs focus
on launch metrics (listing price, initial holder count). PHS measures the five
indicators that determine whether a partnership is healthy at 12, 24, and 36 months:
utility event frequency, community sentiment, holder count trajectory, token utility
index, and partnership development signals.

---

## SportMind skill stack

```
PRE-LAUNCH DUE DILIGENCE STACK:

1. fan-token/fan-token-why.md
   → Foundational value thesis — why does a fan token make sense at all?
   → Three structural ceilings the token solves (stadium capacity,
     revenue geography, spectator-only model)
   → Five-phase future trajectory (engagement → RWA/SportFi)

2. market/market-{sport}.md
   → What is this sport's fan token readiness tier?
   → Tier 1: proceed to full analysis
   → Tier 2: near-term window; qualified proceed
   → Tier 3: longer horizon; document catalyst conditions needed
   → Tier 4: not recommended at this time

3. market/market-overview.md
   → Tier upgrade/downgrade signals — when does this sport move tiers?
   → Competitor landscape in this sport's token ecosystem

4. macro/macro-economic-cycles.md
   → Current economic cycle — recession risk affects premium sports spending
   → Premium vs mass-market sport vulnerability

5. macro/macro-crypto-market-cycles.md
   → Current crypto phase — not a reason to delay, but affects timing
   → Bear market launch: lower initial price but lower acquisition cost

6. fan-token/fan-token-lifecycle/
   → Six-phase lifecycle model
   → Where would this club enter? Pre-launch through active utility
   → LTUI modelling: what utility event cadence is realistic for this club?

7. fan-token/fan-token-partnership-intelligence/
   → PHS (Partnership Health Score): 5 indicator assessment
   → Termination risk signals — what would a bad partnership look like?
   → Type A/B/C case study context (active partnership; uncertain; post-partnership)

8. fan-token/blockchain-validator-intelligence/
   → VSI (Validator Status Indicator) — if club is a validator node
   → PSG dual-layer model: can this club be both token and validator?

9. core/confidence-output-schema.md
   → Structured output for the due diligence report

Skills API shortcut:
  GET /skills/fantoken.why/content
  GET /skills/fantoken.lifecycle/content
  GET /skills/fantoken.partnership-intel/content
  GET /stack?use_case=commercial_brief
```

---

## Output: Token Launch Due Diligence Report

```
SPORTMIND TOKEN LAUNCH DUE DILIGENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Club: [Club Name]
Sport: [Sport]
Primary Market: [Country/Region]
Report Date: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMMERCIAL TIER ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sport: Football → Tier 1 ✅
  Token ecosystem: Active (40+ clubs, 10+ leagues)
  Precedent: Strong — $BAR, $PSG, $CITY established commercial templates
  
Club tier within sport: Mid-tier domestic (no active European campaign)
  Comparable clubs: Championship-level Premier League equivalents
  Expected initial holder count range: 8,000–25,000 (based on comparables)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LIFECYCLE ENTRY ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projected entry phase: Phase 1 (Launch)
Expected Phase 1 duration: 6–12 months
Transition to Phase 2 (Active Utility): Conditional on:
  - Consistent utility event delivery (minimum 8/year)
  - Holder count stability (< 15% monthly churn)
  - At least 1 major sporting event trigger in Phase 1 window

LTUI PROJECTION (Lifetime Token Utility Index):
  Optimistic (promotion to top flight): 72
  Base case (current division): 54
  Pessimistic (relegation): 38
  
  BASE CASE INTERPRETATION: Score 54 = adequate commercial lifecycle.
  Token remains viable long-term but utility events will be domestic only.
  UCL/Europa events would trigger significant LTUI uplift.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PARTNERSHIP HEALTH INDICATORS (PHS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projected PHS at Month 12 (base case): 68 / 100

Component projections:
  UEF (Utility Event Frequency): 7/10 — domestic club, 6-8 events/year feasible
  CSP (Community Sentiment Projection): 7/10 — fan base engaged, no crisis signals
  HCT (Holder Count Trajectory): 6/10 — mid-tier club; slow organic growth
  TUI (Token Utility Index): 7/10 — Socios infrastructure supports standard utility
  PDS (Partnership Development Signal): 7/10 — no conflict signals identified

TERMINATION RISK: LOW
  No category exit signals. No governance concerns. No competing token interests.
  Primary risk: relegation to lower division (reduces LTUI and UEF projections)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGULATORY ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Primary market: United Kingdom
  UK FCA: Fan tokens regulated as cryptoassets (promotions require FCA approval)
  Recommendation: Confirm FCA cryptoasset promotions approval before UK marketing
  Risk level: MEDIUM — not a blocking issue; requires process compliance

Secondary markets (based on fan demographics): Spain, Germany
  EU MiCA: Fan tokens under monitoring; not currently blocked
  Risk level: LOW

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIMING RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current macro phase: NEUTRAL (macro_modifier: 1.00)
Crypto cycle: Not a blocking issue in either direction

OPTIMAL LAUNCH WINDOW:
  Pre-season (July-August): Highest organic fan engagement
  Derby/rivalry match week: Maximum single-event launch amplifier
  Avoid: January window (attention on transfers); post-relegation

OVERALL RECOMMENDATION: PROCEED with qualifications
  Sport tier: ✅ Tier 1
  Club viability: ✅ Base case LTUI 54 (adequate)
  Regulatory: ⚠️ FCA compliance process required
  Timing: ✅ Summer pre-season launch recommended
```

---

## Agent system prompt

```
You are a sports token strategy agent powered by SportMind.
You conduct pre-launch due diligence for clubs and sports organisations
evaluating whether to launch a fan token product.

DUE DILIGENCE FRAMEWORK:

1. SPORT TIER ASSESSMENT:
   Load market/{sport}.md. State the tier clearly.
   Tier 1: full analysis — proceed
   Tier 2: qualified proceed — document catalyst conditions
   Tier 3-4: not recommended currently — document what would change this

2. LIFECYCLE MODELLING:
   Load fan-token-lifecycle skill. Model LTUI for three scenarios:
   optimistic, base case, pessimistic.
   Be honest about what drives each scenario.

3. PARTNERSHIP HEALTH PROJECTION:
   Load partnership-intel skill. Project PHS at 12 months.
   Identify the top 2 risks to partnership health.
   Name the termination signals that would indicate partnership failure.

4. REGULATORY SCAN:
   Based on the club's primary market, identify relevant regulatory considerations.
   Football clubs in India: SEBI VDA framework (from cricket-token-intelligence)
   UK clubs: FCA cryptoasset promotions
   EU clubs: MiCA monitoring
   US clubs: SEC/CFTC considerations
   Do not provide legal advice — flag for specialist legal review.

5. TIMING RECOMMENDATION:
   Check macro_modifier. Note whether current crypto cycle affects launch timing.
   Identify optimal launch window within the sport's calendar.

TONE: This is a business document. Quantitative where possible.
Clearly separate what SportMind can assess from what requires specialist advice.
Always include an overall recommendation with clear rationale.
```

---

## References

- `fan-token/fan-token-why.md` — Value thesis foundation
- `fan-token/fan-token-lifecycle/` — LTUI and phase modelling
- `fan-token/fan-token-partnership-intelligence/` — PHS framework
- `fan-token/blockchain-validator-intelligence/` — VSI for validator clubs
- `market/market-{sport}.md` — Commercial tier for each sport
- `macro/macro-economic-cycles.md` — Economic cycle context
- `macro/macro-crypto-market-cycles.md` — Crypto cycle timing

*MIT License · SportMind · sportmind.dev*
