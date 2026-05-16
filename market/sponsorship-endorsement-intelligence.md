---
name: sponsorship-endorsement-intelligence
description: >
  Enduring reasoning framework for sponsorship and endorsement activity as signals
  affecting club commercial health, fan token demand, and CDI modifiers. Covers
  sponsorship tier classification, sponsorship event signals, individual athlete
  endorsement frameworks, athlete sponsorship as club/fan token signal, tournament
  sponsorship signals, and FTP PATH_2 interaction. Enduring frameworks only —
  not current sponsors or active deal details.
---

# Sponsorship and Endorsement Intelligence

**How sponsorship and endorsement activity signals commercial health and fan token demand.**
Sponsorship is one of the most reliable leading indicators of commercial trajectory.
Commercial trajectory directly affects fan token demand signals through CDI modifiers.

---

## Sponsorship tier framework

```
TIER 1 — GLOBAL BRAND SPONSOR (Fortune 500 or equivalent):
  Examples of tier type: major automotive, technology, financial services, luxury goods.
  Signal: maximum commercial health indicator.
  CDI modifier: ×1.08 sustained | Duration: full contract period

TIER 2 — REGIONAL BRAND SPONSOR (strong regional presence, not global):
  Signal: solid commercial health.
  CDI modifier: ×1.04 sustained

TIER 3 — LOCAL OR SECTOR SPONSOR (local business or niche sector):
  Signal: standard commercial baseline.
  CDI modifier: ×1.00 — no adjustment

TIER 4 — NO FRONT OF SHIRT SPONSOR:
  Two possible causes — assess which applies:
  Financial difficulty confirmed: CDI modifier ×0.92
  Deliberate strategy (charitable or brand positioning): neutral — no modifier
```

---

## Sponsorship event signals

```
NEW SHIRT SPONSORSHIP ANNOUNCED:
  Tier 1: ×1.08 announcement week | ×1.05 sustained for contract duration
  Tier 2: ×1.04 announcement week | ×1.02 sustained
  Tier 3: no significant signal

SHIRT SPONSORSHIP TERMINATED MID-CONTRACT:
  COMMERCIAL_RISK_FLAG
  CDI modifier: ×0.85 sustained until new sponsor announced.
  Sponsors do not break contracts without significant cause — this is a serious signal.

STADIUM NAMING RIGHTS DEAL — NEW:
  Long-term commercial stability signal.
  CDI modifier: ×1.08 sustained (typically 5-15 year duration)

STADIUM NAMING RIGHTS — LOSS:
  Uncertainty signal: ×0.94 until new deal announced.

KIT MANUFACTURER — GLOBAL TIER (Nike/Adidas/Puma equivalent):
  CDI modifier: ×1.05 sustained.
  Signals global commercial reach and merchandising revenue capacity.

KIT MANUFACTURER — TIER DOWNGRADE:
  Negative commercial signal: ×0.94.
  Suggests global brands are not competing for the club's business.

CHILIZ OR SOCIOS AS DIRECT SPONSOR:
  When Chiliz or Socios sponsors a club event, stadium, or competition directly:
  Ecosystem signal: ×1.10 for all fan tokens associated with that event or competition.
  Direct ecosystem investment by the platform operator signals market confidence.
```

---

## Individual athlete endorsement framework

```
ENDORSEMENT PORTFOLIO DEPTH (relevant for future individual athlete token modelling):
  Global tier endorsements (3+):
    Personal brand depth signal: ×1.15 ceiling applied to demand estimates.
    Athlete has broad appeal beyond sport-specific audience.
  No major endorsements:
    ×0.90 to demand ceiling estimates for individual athlete token modelling.

ENDORSEMENT TERMINATION (mid-contract brand drop):
  Integrity or performance concern signal.
  Apply: ×0.88 to athlete-linked demand signals for 4-8 weeks.
  Distinct from contract expiry — termination signals active brand concern.

CRYPTO OR WEB3 ENDORSEMENT:
  Athlete publicly endorses a crypto or Web3 project:
  Positive: ×1.05 digital asset openness signal for any associated fan token.
  Risk: if endorsed project subsequently found fraudulent:
  Apply: ×0.88 credibility discount to all athlete-linked demand signals.
```

---

## Athlete sponsorship as club and fan token signal

```
KEY PLAYER GLOBAL BOOT OR APPAREL DEAL:
  Club commercial visibility signal.
  CDI modifier: ×1.04 sustained for deal duration.
  Signals the club's global reach justifies major brand investment.

KEY PLAYER LUXURY OR LIFESTYLE BRAND DEAL:
  CDI modifier: ×1.03 sustained.
  Signals crossover appeal beyond sport — expands club's addressable audience.

MULTIPLE MAJOR ENDORSEMENTS FOR SAME PLAYER:
  Positive CDI: ×1.06
  Risk signal: commercial concentration.
  If player holds above 40% of club's individual sponsorship commercial value:
  Apply departure modifier ×1.15 weighting versus standard player departure.
  The commercial cliff is steeper than the athletic loss alone.

ATHLETE ENDORSEMENT TERMINATION (mid-contract brand drop):
  Apply: ×0.88 to athlete performance and availability confidence.
  Fan token demand impact: ×0.90 sustained for 4-6 weeks.
  Cross-reference: core/anti-doping-intelligence.md and
    core/psychological-intelligence.md for cause assessment.

ATHLETE AS FAN TOKEN AMBASSADOR:
  Official named ambassador or personal channel promotion:
    Tier 1 global athlete (contracted): ×1.15 announcement week | ×1.06 sustained
    Organic personal support (not contracted): ×1.10 — higher credibility than contracted
  Ambassador contract ends or athlete stops promoting:
    Mild negative: ×0.96 for 2-3 weeks as their audience attention shifts.

ATHLETE ADVERTISING IN NEW GEOGRAPHY:
  Key player appears in major campaigns in a new market:
  Club fanbase expansion signal for that geography.
  Apply: ×1.04 to demand signals from that geographic region.
  Particularly relevant when the new geography has significant fan token holder potential.

ATHLETE ADVERTISING CONFLICT (personal vs club sponsor):
  Player's personal sponsor is direct competitor to club's official sponsor:
  Commercial tension signal: ×0.95 commercial harmony modifier until resolved.
  Resolution confirmed: ×1.00 restored immediately.

WORLD CUP ATHLETE ADVERTISING:
  Key players prominent in global tournament advertising campaigns:
  Compound signal — tournament visibility × advertising presence.
  Apply: ×1.08 to fan token demand signals for clubs with key players
  featured prominently in tournament advertising.
```

---

## Tournament and competition sponsorship

```
CLUB AS OFFICIAL TOURNAMENT SPONSOR:
  Fan token club sponsors the competition they participate in:
  Commercial depth signal — commercially significant enough to sponsor their own competition.
  CDI modifier: ×1.06 sustained for tournament duration.

FAN TOKEN PLATFORM AS OFFICIAL TOURNAMENT PARTNER:
  Socios or Chiliz becomes official partner of major tournament or governing body:
  Ecosystem legitimacy signal: ×1.12 applied to all active fan tokens in that competition.
  Duration: partnership period.

COMPETING SPONSOR CONFLICTS (sleeve branding restrictions):
  Club shirt sponsor in direct commercial conflict with tournament official sponsor:
  Reduced commercial visibility: ×0.96 on commercial exposure metrics.
```

---

## FTP PATH_2 sponsorship interaction

```
SPONSORSHIP AFFECTS THE DEMAND SIDE OF FTP PATH_2 — NOT THE SUPPLY MECHANIC:

  Strong sponsorship portfolio → higher CDI baseline → larger demand premium on WIN.
  The burn fires regardless of sponsorship.
  Commercial health determines how the holder community responds to the supply event.

  STRONG CDI + WIN BURN = maximum demand amplification.
  WEAK CDI + WIN BURN = supply event fires but demand response is muted.

  Think of it as:
    Supply mechanics create the event.
    Commercial health determines the community's response to it.
```

---

## Compatibility

**Marketing signals:**    `market/marketing-advertising-intelligence.md`
**Partnership signals:**  `market/commercial-partnership-intelligence.md`
**Ecosystem health:**     `fan-token/ecosystem-health-intelligence.md`
**FTP PATH_2:**           `fan-token/ftp-path2.md`
**Context bridge:**       `fan-token/fan-token-context-bridge.md`

---

*SportMind v3.97.59 · MIT License · sportmind.dev*
*Sponsorship signals affect CDI (demand side). They do not affect PATH_2 supply mechanics.*
