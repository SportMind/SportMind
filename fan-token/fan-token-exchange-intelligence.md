# Fan Token™ Exchange Intelligence

**Version:** 3.80.0
**Layer:** Fan Token Commercial (Layer 3)
**Scope:** Global exchange delisting lifecycle, liquidity impact, sentiment consequences,
intervention modelling, re-listing signals, and agent decision rules for sports-backed fan tokens.

---

## Why exchange infrastructure is a fan token intelligence layer

Most fan token intelligence frameworks treat exchange listings as stable background
infrastructure — a token is either listed or it is not. This is wrong.

Exchange listing status is a live variable. For fan tokens with significant exposure
to specific regional markets — particularly the Korean exchange cluster, the Turkish
retail market, and Indian mid-tier exchanges — a delisting warning or confirmation is
a primary signal that touches liquidity, sentiment, CDI calculations, and the token's
ability to respond to sporting events with the price behaviour SportMind models.

Fan tokens have a structural property that makes exchange intelligence uniquely valuable:
there is a real entity behind every token that can intervene. A club, a sporting
organisation, or Socios itself can respond to a delisting risk in ways that a DeFi
protocol or memecoin cannot. This creates a predictable intervention probability model
that has no equivalent in general crypto exchange intelligence.

The SPURS case in 2025–2026 — simultaneous warning notices from Bithumb, Coinone, and
Gopax — demonstrates that this is not an edge case. It is a recurring pattern for fan
tokens that rely on a single regional market for a disproportionate share of their
liquidity.

---

## Exchange tier framework for fan tokens

Exchange impact is not equal. The severity of a delisting event depends on which tier
of exchange is involved, and how much of the token's volume flows through that exchange
or region.

### Tier 1 — Global liquidity anchor exchanges

**Exchanges:** Binance, OKX

These exchanges represent the deepest liquidity for any listed token globally.
Binance delisting is the highest-severity liquidity event in the category. When
Binance delisted StaFi (FIS) in December 2025, the token declined 73% over 60 days.
Binance uses a Monitoring Tag system as a warning mechanism — tokens tagged must pass
a quarterly quiz to trade, flagging them as high-risk before any formal delisting action.

**Fan token exposure:** BAR, AFC, PSG, ACM, JUV, CITY, INTER listed on Binance.
Binance maintains a dedicated Fan Token hub, which gives these tokens structural
protection from routine cleanup cycles. However, hub membership does not confer
permanent immunity — low sustained volume remains a delisting trigger.

**Impact profile on delisting confirmation:**
- Immediate liquidity collapse. Binance represents a large share of spot volume for most
  fan tokens — depth disappears and bid-ask spreads widen significantly on remaining exchanges.
- Global price discovery impaired. Other exchanges reprice from a thinner order book.
- Withdrawal deadline pressure triggers forced selling from holders who cannot or will not
  migrate to another exchange within the window (typically 30 days for withdrawals).
- Recovery pathway is long. Re-listing on Binance requires standard listing review with no
  guaranteed outcome.

**OKX profile:** Regular asset reviews, typically 30-day notice before trading suspension.
Deposits suspended before trading halt — agents monitoring deposit suspension as a leading
indicator of imminent OKX delisting have approximately 7–14 days of pre-confirmation signal.

### Tier 2 — Regional dominant exchanges

**Exchanges:** Upbit, Bithumb, Coinone, Korbit, Gopax (Korean DAXA cluster); Bybit, Gate.io,
MEXC, KuCoin (global mid-tier); CoinDCX (Indian mid-tier)

The Korean DAXA cluster is the most consequential tier for fan tokens specifically.
Korea has 16 million crypto account holders — approximately 30–32% of the population —
making it one of the highest per-capita crypto retail markets globally. Fan tokens
with significant Korean exposure (GAL, TRA, SPURS, GOZ, SAM) are structurally dependent
on this cluster for retail bid support.

**DAXA mechanics** (Digital Asset eXchange Alliance):
Upbit, Bithumb, Coinone, Korbit, and Gopax act in coordination through DAXA, a
self-regulatory body. When DAXA designates a token for Investment Warning status,
all five exchanges implement measures simultaneously. This coordination amplifies
impact — there is no Korean fallback exchange when DAXA acts as a bloc.

Korean exchanges are now required to conduct six-monthly reviews of all listed assets,
evaluating trust, security, issuer reliability, and trading activity. This means fan
tokens with declining Socios engagement or falling volume face recurring exposure to
DAXA review cycles, not just one-off events.

**CoinDCX (India):** Delisted ASR (AS Roma), alongside 16 other tokens, in June 2025
citing low trading volume. Indian mid-tier exchanges represent a meaningful secondary
market for European football fan tokens, particularly for clubs with large South Asian
fanbases (Manchester City, Liverpool-adjacent tokens, PSG).

### Tier 3 — Niche and emerging market exchanges

**Exchanges:** Bitget, LBank, XT.com, Indodax (Indonesia), regional Turkish exchanges

These exchanges often represent the final resting place for fan tokens after upper-tier
delistings. Volume is thin and spreads are wide, but they preserve on-chain accessibility.
VATRENI (Croatia) trades on Gate.io and XT.com — this is a Tier 3 liquidity profile
despite the token's World Cup 2026 relevance.

Tier 3 delistings are low-severity events in isolation. However, a cascade — where a
token migrates down through the tiers over time — is a structural liquidity deterioration
signal that feeds directly into the CHI and CDI frameworks.

### Tier 4 — DEX only (FanX / Kayen)

When a fan token is delisted from all CEX venues, on-chain DEX liquidity on FanX
(the native Chiliz Chain AMM, previously Kayen) becomes the sole market. This is a
distinctive state for fan tokens that has no parallel in most crypto assets: the token
remains fully functional for its Socios utility (voting, rewards, exclusive access)
even when CEX liquidity is zero. The token's utility value and its market value
effectively decouple.

This decoupling matters for agents. A token in Tier 4 state should not be modelled
using standard market intelligence — CDI, CHI, and on-chain holder activity are the
primary signals, not price or volume.

---

## The DAXA delisting lifecycle — stage-by-stage intelligence

The Korean DAXA lifecycle is the most structured and predictable delisting pathway
in global crypto markets. Its stages are consistently applied and publicly announced,
giving agents a defined signal timeline.

### Stage 0 — Pre-warning: volume and activity monitoring

Before any formal action, Korean exchanges monitor trading volume, project activity,
and issuer responsiveness. For fan tokens, the observable pre-warning signals are:

- **Volume decay:** Korean trading pair volume declining over 30–60 days without a
  sporting catalyst to explain it.
- **Socios poll absence:** No new polls or governance events published for 30+ days.
- **Chiliz Chain activity:** Declining unique wallet interactions with the token contract.
- **Social silence:** Club's official accounts not mentioning or promoting the fan token.

Any three of these conditions active simultaneously constitutes a pre-warning flag
in SportMind's agent reasoning. This is Stage 0 — no exchange action has occurred
but the conditions for review are present.

**Agent instruction:** Flag token for enhanced monitoring. Do not adjust CDI yet.
Log conditions against EDLI (Exchange Delisting Likelihood Index — see scoring section).

### Stage 1 — Investment Warning issued

DAXA designates the token for Investment Warning (투자유의 종목). The notice is published
simultaneously on all five member exchange sites. Deposit suspension may be implemented
immediately on some exchanges.

**Typical price impact:** −15% to −30% on announcement across all markets, not just Korean.
The global price falls because Korean retail bid support withdraws simultaneously and the
signal is read as a negative fundamental development.

**Review period:** Typically 2–8 weeks. During this window, the project — in a fan token's
case, the club, Socios, or both — can submit a response demonstrating the concerns are
being addressed. DAXA evaluates the response and decides to lift the warning or proceed
to delisting.

**Fan token intervention levers available in this window:**
1. New Socios governance poll published.
2. Club official statement promoting the token.
3. New fan token utility event (exclusive content, ticketing priority, merchandise discount).
4. Visible increase in Chiliz Chain on-chain activity.
5. Volume recovery on Korean pairs — even without intervention, a sporting event can
   provide this (e.g., a cup run during the review window).

**Agent instruction:** Activate Stage 1 protocol. Recalculate EDLI. Assess intervention
probability (see Intervention Probability Model). Adjust CDI downward by the magnitude
specified in the CDI adjustment table. Monitor Socios poll feed and club social accounts
for intervention signals.

### Stage 2a — Warning lifted (positive resolution)

DAXA removes the token from Investment Warning status after determining the concerns
have been addressed. All five exchanges restore full listing with no restriction.

**Price response:** Partial recovery. Typically +10% to +20% as Korean bid support returns
and the resolution signal is processed. The recovery is rarely full because some holders
exited during Stage 1 and are not immediately replaced.

**IoTeX (IOTX) precedent:** Hacked in late 2024, Korean exchanges added to watchlists.
Token dropped 23%. Three weeks after the hack was patched and a full audit submitted,
Upbit, Bithumb, and Coinone simultaneously removed IOTX from their watchlists on
March 15, 2025. Recovery followed. For fan tokens, the equivalent pathway is demonstrable
club engagement within the review window.

**Agent instruction:** Deactivate EDLI flag. Restore CDI baseline. Log resolution details
for pattern library (club response time, intervention type, outcome).

### Stage 2b — Delisting confirmed

DAXA determines the token does not meet the criteria for continued listing. A confirmed
delisting date is set, typically 2–4 weeks from announcement to allow withdrawals.

**Price response:** Second sharp decline on confirmation. The investment warning had
already priced in partial delisting risk — confirmation removes the remaining optionality.
Combined Stage 1 + Stage 2b declines for major tokens historically range from −45% to
−70% from pre-warning levels.

**Korean trading pairs:** Suspended at the designated time. Korean retail volume effectively
goes to zero. All remaining liquidity is on global CEX pairs and DEX pools.

**Fan token-specific consequence:** The token retains full Socios utility. Holders in Korea
can still use the token for governance and rewards within the Socios app — only the
exchange trading functionality is removed. This is a material difference from a standard
crypto delisting. For tokens with high Socios utility activity (frequent polls, active
governance), the functional token survives the exchange delisting intact.

**Agent instruction:** Apply full EDLI impact. CDI adjustment at confirmed-delisting
magnitude. Activate DEX liquidity monitoring via FanX/Kayen. Note that Socios utility
functionality is unaffected — flag for holder archetype analysis (Loyalist holders
retain, Speculator holders exit, outcome diverges by archetype composition).

### Stage 3 — Post-delisting stabilisation

After delisting from Korean exchanges, the token stabilises at a new liquidity floor
determined by global CEX pairs and DEX volume. This floor is typically 30–50% below
pre-warning levels for tokens that were Korean-volume-dependent.

The stabilisation period reveals the token's true utility holder base. Loyalist and
Governance Participant archetypes (from the CHI framework) remain. Speculator and
Yield Farmer archetypes have largely exited. The post-stabilisation CHI reading is
the baseline from which any recovery or re-listing pathway must be assessed.

---

## Global CEX delisting patterns — beyond Korea

### Binance Monitoring Tag system

Binance places tokens on a Monitoring Tag when they show significantly higher volatility
or risk than standard listings. Tagged tokens require users to pass a quiz every 90 days
to continue trading. The tag is visible on the trading interface and functions as a
public delisting warning.

**Fan token exposure:** Any Binance-listed fan token can receive a Monitoring Tag if
volume falls below Binance's review thresholds. The Fan Token hub provides partial
protection but is not absolute. The November 2024 and April 2025 batch delisting
rounds showed that Binance uses cluster-based cleanup, removing 5–10 tokens at once
during downmarket periods.

**Agent monitoring instruction:** Watch for Monitoring Tag assignment on Binance-listed
fan tokens. Tag assignment is a weaker signal than DAXA Investment Warning but carries
the same directional implication. EDLI score increases by 15 points on Monitoring Tag
assignment (see scoring section).

### OKX 30-day notice pattern

OKX follows a transparent review process with typically 30-day advance notice before
delisting. Deposits are suspended approximately 7 days before the delisting date.
The deposit suspension is the leading indicator — it appears in exchange announcements
before the trading suspension date.

**Agent monitoring instruction:** Monitor OKX announcements for deposit suspension
notices on fan token pairs. Deposit suspension without accompanying re-listing news
is a confirmed delisting signal with approximately 7-day lead time.

### Mid-tier cascade pattern

When a fan token loses upper-tier exchange support, the volume concentrates on
mid-tier venues (Gate.io, MEXC, KuCoin). These exchanges tolerate lower volume
but also conduct periodic reviews. The pattern observed across multiple tokens is:

1. Tier 1 exit (Binance or OKX) → volume concentrates on Tier 2.
2. Tier 2 regional exit (DAXA) → volume concentrates on global mid-tier.
3. If no recovery catalyst, Tier 3 mid-tier reviews trigger in 6–12 months.
4. Token reaches DEX-only state.

This cascade is not inevitable. Sporting catalysts — a cup run, a major transfer,
a World Cup — can arrest the cascade at any stage by regenerating volume and community
attention that satisfies exchange review criteria.

---

## The fan token intervention model

Fan tokens have a structural advantage over generic crypto assets in exchange
delisting scenarios: there is a real-world entity — the club — whose actions
directly affect the token's exchange viability. This creates an intervention
probability model that SportMind can calculate.

### Intervention Probability Score (IPS)

The IPS is a 0–100 score estimating the probability that a DAXA Stage 1 warning
will be resolved without delisting.

**IPS components:**

| Component | Weight | Signal |
|---|---|---|
| Recent Socios poll activity | 25% | Polls published in last 30 days |
| Club social media token mentions | 20% | Official club accounts in last 14 days |
| CHI trajectory | 20% | Rising, flat, or declining over 30 days |
| Korean volume trend | 15% | Volume 7-day vs 30-day average |
| Sporting calendar position | 10% | Active competition window vs off-season |
| Historic intervention record | 10% | Club's prior response to platform concerns |

**IPS thresholds:**

| Score | Interpretation | Agent action |
|---|---|---|
| 70–100 | High intervention probability | Hold CDI adjustment at Stage 1 level. Monitor for resolution. |
| 40–69 | Moderate — outcome uncertain | Apply graduated CDI adjustment. Set 14-day review checkpoint. |
| 0–39 | Low — delisting likely | Apply full Stage 2b CDI adjustment pre-emptively. |

**IoTeX precedent applied to fan tokens:** IoTeX scored high on the equivalent of
a technical intervention (patch + audit + exchange engagement). A fan token equivalent
would be: new poll published + club statement + increased on-chain activity within
the review window. If all three are present within 7 days of a Stage 1 warning,
IPS is pushed toward the high band regardless of other factors.

**SPURS contextual note:** The simultaneous Bithumb/Coinone/Gopax warnings on SPURS
are consistent with a DAXA coordination action. Given SPURS' +83% rally during the
2025 Europa League run — demonstrating that sporting performance directly generates
Korean volume — a strong European competition result during a review window would
constitute a natural volume intervention even without explicit club action.

---

**Academic grounding: Assaf, Demir & Ersan (2024), *International Review of Economics & Finance* — GSADF-based bubble detection in fan tokens confirms periods of exuberance precede sharp corrections. Vidal-Tomás (2023), *Journal of Economic Studies* — bubble phenomenon and Chiliz ecosystem dynamics documented. Lubian (2023), *Journal of Quantitative Finance and Economics* — asymmetric downside volatility confirmed: negative moves exceed positive moves in magnitude. All three inform the EDLI risk calibration below.**

## Exchange Delisting Likelihood Index (EDLI)

The EDLI is a 0–100 score for any fan token in the registry, calculated by agents
as a standing risk monitor. Higher scores indicate higher delisting risk across
the token's exchange portfolio.

### EDLI input factors

**Volume signals (40% weight):**
- 30-day volume trend on primary CEX pairs: declining = +10 to +20 points
- Korean pair volume share below 5% of prior 90-day average: +15 points
- Single exchange accounts for >70% of total volume: +10 points (concentration risk)

**Activity signals (30% weight):**
- No Socios poll published in 45+ days: +15 points
- No club social media token mention in 30+ days: +10 points
- On-chain active addresses declining for 4+ consecutive weeks: +5 points

**Exchange status signals (30% weight):**
- Binance Monitoring Tag active: +15 points
- DAXA Investment Warning active: +25 points
- Regional exchange deposit suspension active: +20 points
- Any exchange delisting confirmed: +30 points (triggers cascade risk assessment)

### EDLI interpretation

| Score | Status | CDI adjustment | Agent action |
|---|---|---|---|
| 0–20 | Normal | 0% | Standard monitoring |
| 21–40 | Elevated | −5% | Flag for 30-day watch |
| 41–60 | Warning | −10% | Activate Stage 1 protocol |
| 61–80 | Critical | −20% | IPS assessment, cascade risk check |
| 81–100 | Severe | −30% | Full exchange intelligence report |

---

## Sentiment and community impact layers

Exchange delistings do not affect only price and liquidity. They propagate through
the fan token ecosystem via sentiment channels that SportMind's existing intelligence
layers already model.

### Fan Sentiment Intelligence (CDI decay)

A delisting warning is the most severe negative sentiment event in the fan token
lifecycle outside of club relegation or a star departure. The CDI (Commercial Duration
Index) from `fan-sentiment-intelligence` normally decays toward baseline following
a result. A DAXA Investment Warning overrides this model.

**CDI override rule:** When EDLI > 60, CDI is capped at its current value even
if a positive sporting event (win, cup run) would normally extend it. The reason:
positive sporting sentiment partially offsets exchange risk in the community, but
does not eliminate it. Holders who are exchange-dependent (Speculators, Yield Farmers)
are exiting regardless of the next match result. Only structural resolution — warning
lifted, volume recovered, new utility events — restores normal CDI behaviour.

**Sentiment asymmetry:** Research confirms fan token losses generate stronger negative
sentiment than wins generate positive sentiment (loss-effect asymmetry, Ante et al.
2024). This asymmetry compounds during exchange delisting events: holders who exit
are more vocal about their negative experience than new holders who might enter at
lower prices. Social media sentiment monitoring will show net negative signal for
weeks after a warning even if the underlying token remains functional.

### Holder archetype impact (CHI consequences)

The four holder archetypes from `fan-holder-profile-intelligence` respond differently
to exchange delisting events:

**Loyalist fans (40–60% of typical holder base):**
Exit rate during delisting: low. These holders use the token for Socios utility
and are not exchange-dependent for their primary experience. CHI impact: moderate
short-term decline, recovery follows if club engagement continues. The Loyalist
cohort is the stable foundation that sustains a token through an exchange delisting.

**Governance Participants (10–20% of holder base):**
Exit rate: very low. These holders are specifically motivated by voting rights
and are unlikely to exit due to exchange-only pressure. CHI impact: minimal.
They may increase governance activity during a delisting period as they attempt
to signal the token's health.

**Speculators (20–30% of holder base):**
Exit rate during delisting: very high. Speculators are exchange-dependent —
they entered via exchange pairs and exit the same way. The DAXA warning and
subsequent price decline trigger automatic exit for this cohort. CHI impact:
large short-term negative. However, Speculator exit is not inherently negative
for the token's long-term health — it concentrates ownership in utility-motivated
holders who are more likely to sustain the CHI floor.

**Yield Farmers / DeFi participants (5–15% of holder base):**
Exit rate: very high. Liquidity pool withdrawals often precede or accompany
exchange delisting events as these holders seek to redeploy to higher-liquidity
venues. CHI impact: DEX liquidity declines, increasing slippage on remaining
on-chain trades. Cross-reference with `defi-liquidity-intelligence` for LP
withdrawal signals.

**Post-delisting CHI floor:**
After a Tier 1 or full DAXA delisting, the remaining holder base is predominantly
Loyalists and Governance Participants. The CHI floor for this concentrated base
is typically higher per-holder than the pre-delisting CHI, even though total
holders have declined. This matters for agents assessing re-listing potential
— a smaller but more committed holder base is a stronger re-listing argument
than a large but disengaged one.

### Governance activity as a health signal

During and after exchange delisting events, Socios governance activity becomes
an important counter-signal. Clubs that respond to delisting pressure with new
polls and fan engagement events are demonstrating the token's utility is intact.
This is directly observable and should be monitored.

**Governance activity signal classification:**

| Activity | Signal interpretation |
|---|---|
| New poll published within 7 days of DAXA warning | Positive intervention signal — feeds IPS |
| Poll participation rate higher than 90-day average | Community rallying — reduces EDLI |
| No poll activity for 30+ days post-warning | Passive response — negative IPS factor |
| Club deletes or ignores fan token social content | Partnership risk flag — separate alert |

---

## Re-listing intelligence

Re-listing of a delisted fan token is rare but documented and commercially significant.
WEMIX was delisted from all DAXA exchanges in December 2022 and re-listed beginning
with Coinone in February 2023, followed by other members. The driver was demonstrated
resolution of the original disclosure concerns combined with sustained community activity.

For fan tokens, the re-listing pathway is more predictable than for general crypto assets
because sporting performance and club engagement provide natural volume catalysts.

### Re-listing Readiness Score (RRS)

The RRS is a 0–100 score for tokens in post-delisting state, estimating re-listing
probability within a 90-day window.

| Component | Weight | Positive signal |
|---|---|---|
| DEX volume trend | 25% | Rising 30-day DEX volume without price decline |
| Socios poll activity | 20% | 2+ polls published in last 30 days |
| CHI trajectory | 20% | Rising post-delisting floor |
| Sporting calendar | 15% | Major competition imminent (cup run, WC qualifier) |
| Global CEX tier | 10% | At least one Tier 2 exchange still listed |
| Club social engagement | 10% | Active fan token content on club channels |

**RRS thresholds:**

| Score | Interpretation |
|---|---|
| 70–100 | Re-listing conditions present. Flag for exchange outreach monitoring. |
| 40–69 | Re-listing possible but conditions not yet sufficient. |
| 0–39 | Re-listing unlikely within 90-day window. |

**Empirical basis: Saggu, Ante & Demir (2024), *Research in International Business and Finance*. Documented anticipatory price gains before FIFA World Cup fixtures; event-driven losses post-elimination exceed advancement gains (asymmetry confirmed).**

**World Cup 2026 re-listing amplifier:**
For national team tokens (ARG, POR, ITA, SNFT, BFT, VATRENI) and club tokens
with high WC2026 exposure, the tournament window (June–July 2026) represents a
structural re-listing opportunity. Exchange commercial teams are aware of the
increased fan interest and may accelerate review timelines for tokens that have
resolved underlying concerns. Apply NCSI WC2026 multiplier as a +15-point
RRS bonus during the 60-day pre-tournament window.

---

## DEX liquidity as a fallback signal

When CEX liquidity deteriorates, FanX (the native Chiliz Chain AMM) and Kayen
become the primary price discovery venues. The DeFi liquidity intelligence framework
in `defi-liquidity-intelligence` covers LP mechanics in detail. The exchange-specific
additions are:

**DEX volume growth after CEX delisting:**
A token that loses a Tier 2 CEX exchange but shows rising DEX volume is demonstrating
that utility holders are migrating to on-chain trading rather than exiting. This is
a positive signal for IPS and RRS calculation.

**LP withdrawal timing:**
LP providers typically withdraw ahead of CEX delisting confirmation, not after.
A sudden increase in LP withdrawals from FanX/Kayen pools, without a sporting
catalyst, is a leading indicator that a CEX delisting is anticipated by
sophisticated market participants. This signal typically precedes public
exchange announcements by 3–7 days.

**Slippage as a health metric:**
Post-delisting, slippage on FanX/Kayen for typical fan token purchase sizes ($50–$500)
is a direct readability of the remaining community health. Slippage below 2% on a
$200 purchase suggests functional liquidity. Slippage above 5% suggests thin pools
and likely Loyalist-only activity. Cross-reference with CHI to confirm.

---

## Cross-layer integration with SportMind

Exchange intelligence integrates with the following existing SportMind frameworks:

**Fan Token Commercial (Layer 3):**
- `fan-token-lifecycle.md` — Exchange delisting maps to Phase 4 (Utility Plateau) or
  Phase 5/6 (Non-Contractual Token). EDLI > 60 is a Phase 4 indicator. Full delisting
  from all CEX venues is a Phase 5 indicator.
- `fan-holder-profile-intelligence.md` — CHI calculation should incorporate EDLI score
  as a negative modifier when EDLI > 40.
- `fan-sentiment-intelligence` — CDI cap rule applies when EDLI > 60.
- `defi-liquidity-intelligence` — LP withdrawal monitoring as leading indicator.
  Slippage tracking as health proxy.
- `gamified-tokenomics-intelligence` — FTP PATH_2 events cannot counteract
  DAXA-warning-level price pressure. A WIN supply burn during a DAXA review window
  will reduce the decline rate but will not reverse the liquidity withdrawal. Agents
  should not model FTP events as sufficient to offset EDLI > 60 conditions.
- `fan-token-partnership-intelligence` — Expired or weakening partnerships increase
  EDLI baseline score. The ESRPLE adoption matrix from Part 6 maps directly to IPS
  calculation.

**Platform layer:**
- `fraud-signal-intelligence.md` — The MRS (Manipulation Risk Score) is elevated
  during DAXA warning windows. Wash trading is a documented exchange-compliance
  concern. Agents should increase MRS monitoring frequency when EDLI > 40.
- `chiliz-chain-address-intelligence.md` — On-chain address activity is an EDLI
  input. Declining unique address interactions are a Stage 0 pre-warning signal.

**Macro layer:**
- `macro-regulatory-sportfi.md` — MiCA authorisation for Socios (granted September 2025)
  reduces European exchange delisting risk for MiCA-compliant listings. US SEC/CFTC
  joint guidance (March 2026) classifying fan tokens as digital collectibles reduces
  US exchange regulatory delisting risk. These macro developments provide a partial
  structural offset to exchange-level delisting pressures.

---

## Korean market concentration — fan token exposure map

Korean market exposure varies significantly across the registry. Agents must
calibrate EDLI scoring to reflect actual Korean volume dependency.

**High Korean exposure (Korean pairs account for estimated >30% of total volume):**
GAL (Galatasaray), TRA (Trabzonspor), SPURS, GOZ, SAM, IBFK

These tokens carry elevated structural EDLI sensitivity to DAXA actions. A DAXA
Investment Warning for any of these tokens represents a larger proportional liquidity
event than for European-focused tokens.

**Moderate Korean exposure (estimated 10–30%):**
BAR, ACM, JUV, ATM, PSG, CITY, INTER, EFC, CPFC

**Low Korean exposure (estimated <10%):**
MENGO, FLU, SPFC, SACI, GALO, VERDAO (Brazilian-dominant volume)
BUFC, JDT, PERSIB, PRSJ (Southeast Asian-dominant volume)

**Note on concentration risk:**
Single-exchange dependency — regardless of which exchange — is an EDLI risk factor
independent of Korean exposure. A Brazilian fan token where >70% of volume flows
through one regional exchange is exposed to that exchange's review cycle with the
same structural fragility, even though the delisting mechanism differs from DAXA.

---

## Agent decision rules

```
EXCHANGE_DELISTING_INTELLIGENCE_PROTOCOL:

  // Stage 0 monitoring (always active)
  IF volume_decay_30d AND socios_poll_absence_30d AND on_chain_activity_declining:
    SET edli_pre_warning = TRUE
    INCREASE monitoring_frequency TO daily
    LOG conditions_to_edli_tracker

  // Stage 1 — Investment Warning received
  IF daxa_investment_warning_published OR binance_monitoring_tag_assigned:
    CALCULATE edli_score
    CALCULATE ips_score
    APPLY cdi_adjustment(stage_1)
    IF ips_score >= 70:
      SET intervention_window = ACTIVE
      MONITOR socios_poll_feed EVERY 6h
      MONITOR club_social_accounts EVERY 6h
      MONITOR korean_volume_trend EVERY 12h
    ELIF ips_score < 40:
      PRE_APPLY cdi_adjustment(stage_2b)
      ALERT "Low intervention probability — pre-positioning for delisting"
    CHECKPOINT 14_days

  // Stage 2a — Warning lifted
  IF investment_warning_removed AND no_delisting_confirmed:
    RESTORE cdi_baseline
    DEACTIVATE edli_flag
    LOG resolution_to_pattern_library(club_response_time, intervention_type)
    GENERATE intervention_success_report

  // Stage 2b — Delisting confirmed
  IF delisting_date_confirmed:
    APPLY cdi_adjustment(confirmed_delisting)
    ACTIVATE dex_liquidity_monitoring
    SEGMENT holders_by_archetype
    NOTE "Socios utility unaffected — flag for loyalist retention analysis"
    CALCULATE rrs_score
    SET_ALERT rrs_threshold_70

  // Re-listing detection
  IF exchange_relisting_signal_detected AND rrs_score >= 70:
    GENERATE relisting_opportunity_brief
    APPLY wc2026_bonus IF tournament_window_active
    ALERT "Re-listing conditions present for [TOKEN]"

  // Cross-layer updates
  ALWAYS:
    UPDATE chi_with_edli_modifier IF edli > 40
    CAP cdi IF edli > 60
    INCREASE mrs_monitoring IF edli > 40
    CROSS_REFERENCE ftp_events "FTP WIN events do not offset EDLI > 60 conditions"
```

---

## Output schema

```json
{
  "ticker": "SPURS",
  "exchange_intelligence": {
    "edli_score": 72,
    "edli_status": "CRITICAL",
    "active_warnings": ["BITHUMB_INVESTMENT_WARNING", "COINONE_INVESTMENT_WARNING", "GOPAX_INVESTMENT_WARNING"],
    "korean_exposure_tier": "HIGH",
    "ips_score": 58,
    "ips_interpretation": "MODERATE — outcome uncertain",
    "intervention_window_active": true,
    "intervention_signals_detected": ["socios_poll_published_3d_ago"],
    "cdi_adjustment": -0.20,
    "cdi_cap_active": true,
    "dex_monitoring_active": false,
    "rrs_score": null,
    "flags": {
      "daxa_warning_active": true,
      "binance_monitoring_tag": false,
      "ftp_override_blocked": true,
      "loyalist_retention_watch": false,
      "wc2026_relisting_bonus_eligible": false
    },
    "sporting_calendar_note": "Europa League active — sporting event during review window is natural volume intervention",
    "recommended_action": "HOLD_AND_MONITOR — IPS moderate, sporting calendar favourable, 14-day checkpoint"
  }
}
```

---

## Aggregator trust signal framework

CoinGecko and CoinMarketCap are not live data sources for SportMind agents —
they are platforms. Their published methodologies encode stable analytical frameworks
that agents apply as reasoning scaffolding without any API dependency.

### CoinGecko Exchange Trust Score → EDLI calibration

CoinGecko rates exchanges on a 1–10 Trust Score based on traffic, trading
legitimacy, API quality, and regulatory standing. The Trust Score distribution
of a fan token's listing venues is more informative than raw venue count:

| Trust Score | Tier | EDLI implication |
|---|---|---|
| 9–10 | Tier 1 (Binance, OKX, Coinbase) | Delisting = maximum EDLI severity event |
| 7–8 | Tier 1–2 boundary (Bybit, Kraken) | Significant but not global anchor |
| 5–6 | Tier 2 (Gate.io, MEXC, KuCoin) | Important for regional volume |
| 3–4 | Tier 3 (XT.com, LBank, niche regional) | Delisting is low-severity |
| 1–2 | Tier 4 (DEX-equivalent CEX) | On-chain signal preferred over volume |

A token listed on 10 Trust Score 3 exchanges is more fragile than a token
listed on 3 Trust Score 8 exchanges. Apply this distribution test before
calculating concentration risk in EDLI volume signals.

### CoinMarketCap Liquidity Score as EDLI leading indicator

CMC's Liquidity Score normalises order book depth and spread across venues.
A declining Liquidity Score trend without a sporting catalyst is an EDLI
Stage 0 pre-warning signal. It is a leading indicator because it reflects
institutional market maker withdrawal — market makers reduce depth before
volume collapses in headline figures.

**Rule:** A 30% Liquidity Score decline over 60 days with flat headline
volume is a higher-risk configuration than low volume with a stable score.
The flat volume is being maintained by retail activity without market maker
depth — a fragile liquidity structure that collapses under any selling pressure.

---

## Institutional flow signals

### OTC and professional market making

Large fan token transactions and club treasury management route through OTC
desks rather than spot markets. An institutional buy of 500,000 AFC tokens
OTC does not appear in spot volume but reduces circulating supply available
to retail. Agents should not interpret low spot volume as low institutional
interest — OTC activity is systematically invisible to aggregators.

**Observable institutional signal:** Bid-ask spread on major token pairs
tightening from 0.5%+ to below 0.2% without a volume explanation. This is
professional market making entering the token. When Galaxy Digital or Cumberland
begins quoting tight spreads on a fan token pair, the token has reached
institutional viability. This reduces EDLI baseline by 10 points versus default.

**Coinbase Prime:** The primary institutional onramp for US sports investors
post-SEC/CFTC guidance (March 2026). Custody announcements in quarterly
Coinbase Prime disclosures are early signals of institutional accumulation
before any spot volume change.

### Neobank distribution as lifecycle signal

Revolut (50M+ European users), Crypto.com, and eToro represent mainstream
distribution channels that expand fan token reach to non-crypto-native sports
fans. A confirmed neobank listing is a Phase 2→3 lifecycle acceleration signal:

- Neobanks conduct due diligence before listing — confirmation validates
  the token's commercial standing.
- Audience expansion to mainstream sports fans (core Revolut demographic
  is 25–35 European, matching fan token holder profile).
- Volume uplift is typically short-term (6–12 weeks) followed by baseline
  stabilisation as the new audience becomes the installed base.
- Neobank volumes are typically not reflected in CoinGecko or CMC rankings —
  distribution value is fan acquisition, not trading depth.

**Agent instruction:** Neobank listing is a positive IPS factor (suite
expanding) and a negative EDLI factor (reduced concentration risk). Advance
lifecycle phase signal toward Phase 3 confirmation on neobank listing.


## New listing intelligence

A CEX listing is the structural inverse of a delisting — but it is not simply
the reverse signal. The mechanics of a new listing are distinct and generate
predictable price and sentiment patterns that SportMind agents can model.

### The listing price pattern

New CEX listings follow a consistent three-phase pattern across fan tokens:

**Empirical basis: Mazur & Vega (2023), *The Journal of Alternative Investments*. Analysis of fan token listing events. 150% average first-day returns documented; long-run underperformance follows announcement spike. Confirms the three-phase pattern modelled here.**

**Phase 1 — Pre-announcement accumulation (T-7d to T-1d):**
Sophisticated holders accumulate ahead of the public announcement. On-chain
wallet activity increases. DEX volume rises without a sporting catalyst.
Observable signal: rising DEX volume + flat or declining Socios poll activity
(sport-agnostic buyers entering). This is a leading indicator of an imminent
listing announcement.

**Phase 2 — Announcement to listing day (T-0 to T+2d):**
Retail FOMO spike. Price typically rises 40–80% for Tier 1 exchange listings,
20–40% for Tier 2. Volume surges. New wallet addresses enter the registry.
Critical agent rule: do not apply FTP or sporting modifiers during this window.
The price signal is exchange-driven, not sport-driven. Applying sport modifiers
to an announcement-phase token overstates commercial signal.

**Phase 3 — Post-listing normalisation (T+3d to T+30d):**
"Sell the news" correction. Retail profit-taking reduces the announcement gain
by 20–50%. The token finds a new baseline above its pre-announcement price
if the listing was geographically aligned with the fanbase. If the listing was
purely speculative (exchange with no fanbase overlap), the token typically
returns to pre-announcement levels or below within 30 days.

**Upbit post-listing exception:** Upbit has the strongest post-listing 30-day
performance of any major exchange (67% of newly listed tokens remain in the
green at 30 days, vs ~50% for Binance and OKX). An Upbit listing of a Korean-
market-relevant fan token (GAL, TRA, SPURS) carries materially stronger 30-day
signal durability than a listing on a global general-purpose exchange.

### Geographic alignment signal

**Academic grounding: Marques, Sousa & Barbosa (2026), *International Journal of Sports Marketing and Sponsorship* — fan token purchase intent study. Club loyalty and perceived governance influence are the two strongest predictors of token acquisition intent, significantly outweighing financial return expectations. This empirically confirms that aligned listings — those reaching fans who already follow the club — generate durable Loyalist-archetype holders, while misaligned listings attract Speculator-archetype buyers with no loyalty anchor.**

The most important listing intelligence variable for fan tokens is whether the
exchange serves the token's actual fanbase geography.

**Aligned listing (high commercial signal):**
- GAL listed on a Turkish exchange → Turkish Galatasaray fanbase accessible
- MENGO listed on a Brazilian exchange → core Flamengo supporters
- SPURS listed on a Korean exchange → Korean football fan base (already large)

An aligned listing expands the Loyalist and Governance Participant archetypes —
fans who hold for utility, not speculation. CDI durability increases. CHI is
likely to improve over the 60-day post-listing window as new utility holders
enter the suite.

**Misaligned listing (low commercial signal):**
A listing on an exchange with no overlap with the token's actual fanbase
geography attracts Speculator archetype buyers only. Price spikes but CHI
does not improve. CDI extension does not persist beyond the announcement window.

**Agent instruction:** Cross-reference the exchange's primary user geography
against the club's fanbase geography from `market/market-football.md` (or
relevant sport market file) before classifying listing commercial signal strength.

### Listing tier → EDLI reduction table

| Listing tier | Exchange examples | EDLI reduction |
|---|---|---|
| Tier 1 (global anchor) | Binance, OKX | −25 points |
| Tier 1 regional dominant | Upbit (Korea) | −20 points (Korean-heavy tokens) |
| Tier 2 mid-tier global | Gate.io, MEXC, KuCoin | −10 points |
| Tier 2 regional | Bitget, XT.com, regional CEX | −5 points |
| Neobank distribution | Revolut, Crypto.com, eToro | −5 points + Phase 3 signal |

Apply EDLI reduction on confirmed listing date, not on announcement. Announcement
triggers the price response but the listing only reduces structural fragility once
the new liquidity venue is operational.

### Listing as lifecycle signal

| Listing event | Lifecycle implication |
|---|---|
| Tier 1 CEX listing | Phase 2 confirmation or Phase 3 recovery signal |
| Tier 1 listing of previously DEX-only token | Phase 2 launch event — treat as new token for CDI purposes |
| Regional CEX aligned with fanbase | Phase 3 commercial expansion — CDI positive |
| Multiple Tier 2 listings within 30 days | Phase 2 momentum signal |
| Listing on exchange with no fanbase overlap | Speculative-only — do not extend CDI |

### Re-listing as the highest-value listing signal

A token that was delisted and subsequently re-listed carries the strongest
combined signal in this framework. The re-listing confirms:
- The underlying issues that caused the delisting have been resolved
- The club or Socios has actively engaged to restore exchange support
- The holder base has been quality-filtered (Speculators exited at delisting)
- The remaining holders are predominantly Loyalists and Governance Participants

Re-listing on a Tier 1 or Tier 2 exchange after a confirmed delisting is a
STRONG_POSITIVE classification across CDI, CHI, and EDLI simultaneously.
Apply full RRS score reassessment and confirm community activity before entering
the signal chain.

### Agent listing rules

```
NEW_LISTING_PROTOCOL:

  // Pre-announcement detection
  IF dex_volume_rising_7d AND no_sporting_catalyst AND no_socios_poll_7d:
    FLAG potential_listing_accumulation
    SET enhanced_monitoring = TRUE
    DO NOT apply FTP or sport modifiers to DEX volume signal

  // Announcement phase
  IF cex_listing_announced:
    CLASSIFY exchange_tier
    ASSESS geographic_alignment (exchange_primary_market vs club_fanbase_geography)
    SET phase = ANNOUNCEMENT_WINDOW
    HOLD sport modifiers — price signal is exchange-driven
    NOTE: Do not apply FTP WIN modifier during announcement window
    LOG announcement_date, exchange, tier, alignment_classification

  // Listing day
  IF listing_day_confirmed:
    CALCULATE edli_reduction (from tier table)
    APPLY edli_reduction immediately
    IF geographic_alignment == ALIGNED:
      SET cdi_extended = TRUE
      SET chi_improvement_watch = 60_days
    ELIF geographic_alignment == MISALIGNED:
      SET cdi_extended = FALSE
      NOTE "Speculative listing — monitor for 30d normalisation"

  // Post-listing (T+30d)
  IF days_since_listing >= 30:
    ASSESS normalisation: price_above_pre_announcement?
    IF aligned AND price_holds: CONFIRM Phase 3 commercial signal
    IF misaligned AND price_reverts: CONFIRM speculative-only classification
    RESUME normal sport + FTP modifier application

  // Re-listing (strongest signal)
  IF relisting_after_confirmed_delisting:
    CLASSIFY as STRONG_POSITIVE
    RECALCULATE rrs_score
    CONFIRM community_activity_before_signal_entry
    ADVANCE lifecycle_phase_signal
```

---



- `fan-token/fan-token-lifecycle/fan-token-lifecycle.md` — Phase 4/5/6 mapping
- `fan-token/fan-holder-profile-intelligence.md` — CHI and archetype framework
- `fan-token/fan-sentiment-intelligence/fan-sentiment-intelligence.md` — CDI model
- `fan-token/defi-liquidity-intelligence/defi-liquidity-intelligence.md` — LP monitoring
- `fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md` — FTP interaction
- `fan-token/fan-token-partnership-intelligence/fan-token-partnership-intelligence.md` — IPS inputs
- `platform/fraud-signal-intelligence.md` — MRS elevation protocol
- `platform/chiliz-chain-address-intelligence.md` — On-chain EDLI inputs
- `macro/macro-regulatory-sportfi.md` — Structural exchange risk offsets
- `market/sports-equity-intelligence.md` — Cross-instrument equity signals, CHZ macro layer
