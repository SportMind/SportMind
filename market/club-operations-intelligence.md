# Club Operations Intelligence

**The intelligence framework for the off-pitch dimensions of a sports club.**
Clubs make decisions about academy investment, financial sustainability, community
engagement, stadium development, and ownership structure that directly affect their
fan token lifecycle, commercial partnerships, and long-term token holder base.

This skill covers the club operations signals that existing SportMind skills do not:
the institutional health of a club beyond its on-pitch performance.

---

## Club Health Index (CHI)

```
CHI = (Financial_Stability × 0.30) + (Academy_Pipeline × 0.20)
    + (Community_Engagement × 0.20) + (Ownership_Quality × 0.20)
    + (Infrastructure × 0.10)

FINANCIAL_STABILITY:
  Profitable, low debt, UEFA/domestic compliance: 1.00
  Break-even, moderate debt, compliant:           0.80
  Loss-making, high debt, monitoring required:    0.55
  Financial crisis (administration risk):         0.20

ACADEMY_PIPELINE:
  High production (3+ first-team regulars from academy): 1.00
  Good pipeline (1-2 regulars):                          0.80
  Some development (occasional breakthrough):            0.60
  Weak academy (rarely produces first-team players):     0.35

COMMUNITY_ENGAGEMENT:
  Deep local ties, fan trust, CSR active:        1.00
  Moderate engagement:                           0.75
  Low engagement:                                0.45
  Disconnected (corporate/foreign ownership gap): 0.25

OWNERSHIP_QUALITY:
  Stable, commercially ambitious, fan-aligned:   1.00
  Stable but passive:                            0.75
  Financially stretched:                         0.55
  Toxic (ownership disputes, legal issues):      0.20

INFRASTRUCTURE:
  Modern stadium, training ground, data capability: 1.00
  Adequate:                                         0.75
  Below tier peers:                                 0.50
  Significantly deficient:                          0.30
```

---

## Academy intelligence

```
WHY ACADEMY PRODUCTION IS A FAN TOKEN SIGNAL:

Academy players create the deepest fan emotional connections.
A player who joined a club at age 9 and makes his debut at 18 generates
a narrative that signed players cannot replicate. This translates directly
to fan token engagement — hometown hero narratives drive HAS spikes.

ACADEMY SIGNAL EVENTS:

First-team debut of academy player:
  Academy player first-team debut: narrative_active flag
  Apply × 1.12 to AELS for that player's first 5 matches
  Token holder response: strong positive — future narrative seeded

Academy player sold to elite club:
  Positive: academy quality signal (produced talent worth elite fee)
  Negative: squad depth reduced; community connection weakened
  Net signal: neutral to slightly negative LTUI (quality confirmed but departed)

Academy player progresses to national team:
  Maximum academy narrative signal
  Club credited with "producing" national team player
  LTUI positive sustained — fan identity reinforced

ACADEMY TIER ASSESSMENT:
  Elite (Manchester City academy, Ajax, Barcelona La Masia):
    CHI Academy_Pipeline = 1.00
    Systematic production; regular first-team supply
    LTUI premium: +8-10 sustained from academy identity
    
  Developing:
    CHI = 0.60-0.80
    Occasional breakthrough; investment visible
    
  Struggling:
    CHI < 0.50
    Budget cuts signal; development pipeline broken
    Negative LTUI signal if academy was previously a club identity pillar

MONITORING SIGNALS:
  Academy director departure: flag for pipeline disruption
  Academy budget reduction (from financial reports): negative signal
  UEFA Youth League performance: independent quality signal for European clubs
```

---

## Financial sustainability intelligence

```
WHY FINANCIAL HEALTH AFFECTS FAN TOKENS:

Fan tokens are long-duration commercial relationships. A token holder committing
to Phase 2 (Active Utility) is implicitly assuming the club will be commercially
active for years. Financial instability breaks this assumption.

FINANCIAL DISTRESS PROGRESSION:

Stage 1 — Overspending (commercial monitoring):
  Transfer spend consistently > income; wage/revenue ratio elevated
  Signal: minor LTUI concern; monitor closely
  UEFA/domestic financial monitoring: apply × 0.92 to commercial partnership signals

Stage 2 — Compliance investigation:
  UEFA FFP / domestic PSR investigation active
  Confirmed monitoring: LTUI negative signal × 0.85
  Transfer embargo risk: squad quality signal depressed

Stage 3 — Points deduction / sanction:
  Points deduction (Everton 2023-24 Premier League model):
  Immediate LTUI collapse: -25 to -40 points
  Relegation risk activated: lifecycle disruption flag

Stage 4 — Administration / insolvency:
  Club enters administration
  Fan token effectively Phase 6 (Dormant/Defunct) immediately
  Token liquidity crisis: holders rush for exit
  CHI = 0.10 (minimum)

POSITIVE FINANCIAL SIGNALS:
  New stadium announcement (with funding secured):
    Long-term revenue signal + community asset signal
    CHI Infrastructure: upgrade; LTUI +5-10

  Profitable club year (published accounts):
    Financial stability confirmation
    CHI Financial_Stability upgrade

  Strategic investor with clear commercial plan:
    New ownership with capital injection: LTUI +8-15 if credible
    Trophy hunting investment (short-term, unsustainable): neutral to negative

WAGE/REVENUE RATIO BENCHMARKS (football):
  Healthy: < 60% of revenue spent on wages
  Concerning: 60-80%
  Distress: > 80%
  
  Premier League wage disclosure (end of season) is a Tier 1 data event.
  Apply CHI Financial_Stability update immediately when published.
```

---

## Community engagement intelligence

```
COMMUNITY ENGAGEMENT AS LTUI SIGNAL:

Deep community connection creates fan token holders who hold for identity reasons,
not just speculation. These holders are more stable, more engaged in governance,
and more likely to participate in token-gated experiences.

COMMUNITY ENGAGEMENT TIER SIGNALS:

High engagement club (LTUI premium):
  Foundation active in local schools, hospitals, grassroots football
  Ticket pricing accessible to working-class families
  Away end accessible; fan dialogue active
  Community stake (supporter trust with real influence)
  CHI Community = 0.85-1.00
  LTUI premium: +5-8 sustained

Medium engagement:
  Some community activity; commercially focused
  Standard fan engagement (meet-and-greets, social media Q&A)
  CHI Community = 0.55-0.80

Low engagement (LTUI risk):
  Club-community disconnect (corporate ownership, price hikes)
  Fan protests, boycotts, or widespread disaffection
  CHI Community < 0.50
  LTUI negative: -5 to -15 sustained

SPECIFIC COMMUNITY SIGNAL EVENTS:
  Ticket price freeze announcement:
    Rare in modern football; strong community signal
    Apply LTUI +3 to +6 for clubs with significant working-class holder base

  Fan walkout / organised protest:
    Governance quality concern; LTUI risk signal
    Sustained protests (3+ consecutive matches): CHI Community downgrade

  Community ownership stake (German 50+1, Spanish socios model):
    Structural community alignment; highest CHI Community possible
    Tokenisation-natural: community owners are primed for token governance

  Superleague / breakaway proposal (like April 2021 ESL):
    Immediate fan backlash; community signal collapse
    Apply LTUI × 0.70 immediately on announcement
    Reversal: partial recovery (LTUI × 0.88 restored) — trust takes time to rebuild
```

---

## Stadium and infrastructure intelligence

```
STADIUM DEVELOPMENT SIGNALS:

New stadium announcement:
  Funded and approved:
    Long-term revenue signal
    Infrastructure upgrade: CHI × 1.10
    LTUI +5-10 (generational investment = long-term fan commitment)
    
  Approved but funding unclear:
    Positive narrative only; flag as unconfirmed
    
  Planning rejected:
    Club revenue ceiling maintained; negative signal for growth clubs

Stadium naming rights deal:
  Phase 2 commercial activation
  Revenue injection + brand partner signal
  LTUI +3-5; PHS positive if naming partner quality is high
  
  NEGATIVE: naming rights deal that feels misaligned with fan identity
  (a working-class club naming stadium after crypto/gambling brand):
  Fan backlash risk; monitor community engagement metrics

Training ground upgrade:
  Weaker fan token signal but genuine quality commitment indicator
  Signals: long-term squad development investment
  CHI Infrastructure upgrade

DATA AND ANALYTICS INFRASTRUCTURE:
  Club with advanced analytics capability:
    Better player recruitment (lower APS errors)
    Better injury management (lower TAI volatility)
    Neutral for token signal but positive for sustained competitive quality

ARENA ECONOMICS (multi-sport/multi-use):
  Club investing in arena for events beyond sport:
    Revenue diversification signal
    Phase 5 RWA potential: arena revenue can eventually be tokenised
    CHI Infrastructure = 1.00 when arena fully operational
```

---

## Ownership structure intelligence

```
OWNERSHIP MODELS AND TOKEN IMPLICATIONS:

FAN OWNERSHIP (50+1, supporter trust):
  Highest CHI Ownership_Quality
  Token governance is an extension of existing culture
  LTUI premium: holders identify with ownership model
  Challenge: may resist external commercial partnerships
  
PRIVATE EQUITY (CVC in rugby, RedBird, etc.):
  Commercial acceleration; short-term financial optimisation
  Token-positive if PE has digital/tech strategy
  Risk: exit horizon (3-7 years) may not align with token LTUI
  
SOVEREIGN WEALTH (Qatar/Saudi/UAE):
  Geopolitical dimension: load macro/macro-geopolitical.md
  Financial firepower → star player acquisition potential → LTUI uplift
  Risk: geopolitical events can override sporting signals (PSG example)
  
CORPORATE MULTI-CLUB (City Football Group, Red Bull):
  Revenue sharing across clubs
  Player loan network: academy players move between clubs
  Token signal: main club tokens benefit from pipeline; satellite club tokens lower
  
LEVERAGED BUYOUT (debt-financed acquisition):
  Financial distress risk elevated
  Watch: interest payments vs operating income; debt/EBITDA ratio
  High leverage + poor results = administration risk
  
AGENT RULE:
  Check ownership model before CHI calculation.
  Ownership model determines the baseline for financial stability expectations.
  Same debt level = different CHI depending on whether owner is SWF or LBO.
```

---

## Club operations monitoring framework

```
MONTHLY MONITORING TARGETS:

Financial:
  Regulatory announcements (UEFA, Premier League PSR)
  Annual accounts publication (key: wage/revenue ratio)
  Stadium/infrastructure announcements

Ownership:
  Investment announcements
  Boardroom changes (chairman, CEO)
  Fan trust / supporter group statements

Academy:
  Academy manager changes
  U18/U21 league performance (quality proxy)
  First-team debut of academy players

Community:
  Ticket pricing announcements (season ticket renewal window)
  Community foundation programmes
  Fan sentiment (organised groups, supporter trust votes)

FRESHNESS TIER: Monthly (Tier 1 — slow change, high impact when it happens)
```

---

## Compatibility

**Fan token lifecycle:** `fan-token/fan-token-lifecycle/` — CHI affects LTUI projection
**Financial intelligence:** `core/athlete-financial-intelligence.md` — wage data connection
**Manager intelligence:** `core/manager-intelligence.md` — ownership and manager relationship
**Broadcaster intelligence:** `market/broadcaster-media-intelligence.md` — stadium as revenue
**Governance:** `fan-token/sports-governance-intelligence/` — fan ownership + token governance

*MIT License · SportMind · sportmind.dev*
