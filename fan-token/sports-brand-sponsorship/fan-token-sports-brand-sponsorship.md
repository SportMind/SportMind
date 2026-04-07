---
name: sports-brand-sponsorship
description: >
  Full-spectrum sports brand and sponsorship intelligence skill covering athlete-brand
  partnership strategy, deal structure analysis, activation planning, ROI measurement
  frameworks, kit and equipment sponsorship, club commercial partnerships, sponsorship
  market benchmarking, portfolio conflict detection, and emerging brand opportunity
  identification. Use this skill when the user asks about sponsorship deals, wants to
  value or structure a sponsorship agreement, asks what a fair rate for an athlete
  endorsement is, wants to find brand partners for a club or athlete, asks how to
  activate a sponsorship using fan token data, wants to assess whether a current
  sponsorship is delivering ROI, asks about sponsorship conflicts or exclusivity,
  needs a brand partner pitch deck, or wants to understand the commercial sponsorship
  landscape for a sport, league, or territory. More comprehensive than sponsorship-match
  (which focuses on audience-brand alignment from token data) — this skill covers the
  full commercial deal architecture. Feeds brand-score and works alongside
  athlete-social-activity and fan-token-pulse.
---

# Sports Brand & Sponsorship

Full commercial intelligence for sports brand partnerships — from market benchmarking
to deal structure, activation strategy, and ROI measurement.

## What this skill produces

- **Sponsorship Market Rate** — Benchmark fee for this athlete, club, or property
- **Deal Structure Recommendation** — Fee components, KPIs, performance bonuses
- **Portfolio Conflict Audit** — Existing deals that may conflict with new partner
- **Activation Plan** — How to make the partnership visible and measurable
- **ROI Framework** — Pre-agreed measurement criteria for both parties
- **Brand Fit Report** — Values alignment, audience overlap, authenticity score
- **Emerging Opportunity Scan** — Brands actively seeking this type of sponsorship
- **Token-Native Integration** — How to layer fan token ecosystem into traditional deals

---

## Data sources

### Sponsorship market intelligence
- **Nielsen Sports** (commercial): global sponsorship benchmarks
- **Sportspro Media** (public reports): deal announcements and estimates
- **Transfermarkt** (public): player sponsorship history (kit, boots)
- **LinkedIn / company news** (public): brand marketing budget signals, campaign launches
- **Companies House / SEC filings** (public): brand marketing spend context
- **Forbes / Business of Sport** (public): disclosed deal values for top athletes

### Brand intelligence
- **Brandwatch / Mention.com**: brand social sentiment and sports engagement
- **SimilarWeb**: brand website traffic and audience demographics
- **Statista**: brand market share, category spending data
- **Web search**: recent brand marketing news, campaign activity, sports investment signals

### Fan token commercial data
- From `fan-token-pulse`: holder geography, HAS, token velocity
- From `athlete-social-activity`: audience demographics, engagement rates
- From `brand-score`: ABS and AELS as deal-value inputs

---

## Sponsorship market rate framework

### Athlete endorsement rate benchmarks

Rate is primarily driven by: social reach × engagement rate × category demand × exclusivity

**Tier classification:**
```
GLOBAL ELITE      (ABS 85+, 50M+ combined following):   £8M–£50M+ per year
PREMIUM           (ABS 70–84, 10–50M following):         £1M–£8M per year
MID-MARKET        (ABS 55–69, 2–10M following):          £150K–£1M per year
DEVELOPING        (ABS 40–54, 500K–2M following):        £20K–£150K per year
EMERGING          (ABS 25–39, <500K following):          £2K–£20K per year
```

**Category multipliers** (apply to base tier rate):
```
Sportswear / footwear (primary kit):    × 1.4  (highest category premium)
Automotive (global car brand):          × 1.3
Watch / luxury goods:                   × 1.5  (exclusivity premium)
Financial services:                     × 1.2
Food & beverage:                        × 0.9
Crypto / Web3:                          × 1.1  (but audience must have crypto affinity)
Travel / hospitality:                   × 0.8
```

**Exclusivity premium:**
- Category exclusive: + 40% to base rate
- Full exclusivity: + 80% to base rate
- Non-exclusive: base rate

**Tournament window uplift:**
- World Cup / Olympics year: + 25–50% for participating national team players
- Champions League finalist: + 15–30%

### Club sponsorship rate benchmarks

```
SHIRT FRONT (primary):
  Champions League clubs:     £20M–£120M per season
  Top 6 Premier League:       £25M–£60M per season
  Mid-Premier League:         £8M–£20M per season
  Championship:               £2M–£6M per season

SLEEVE PATCH:                 15–25% of front shirt rate
KIT MANUFACTURER:             £3M–£100M+ (based on club size and performance)
TRAINING KIT:                 20–35% of match kit rate
STADIUM NAMING RIGHTS:        £5M–£25M+ per year (top-tier)
```

---

## Workflow

### Step 1 — Define sponsorship property and objective
Accept: athlete/club name + optional (specific brand / category / deal type)

Classify:
```
"athlete_endorsement"    → individual player deal
"club_partnership"       → club-level commercial deal
"event_sponsorship"      → tournament or specific event
"kit_sponsorship"        → kit manufacturer or shirt sponsor
"activation_planning"    → making an existing deal work harder
"deal_valuation"         → what is a fair rate for X?
"roi_assessment"         → is an existing deal delivering value?
```

### Step 2 — Sponsorship Market Rate
1. Identify ABS tier (from brand-score if available, else estimate)
2. Apply category multiplier for the specific brand vertical
3. Apply exclusivity modifier
4. Apply tournament/season window uplift if applicable
5. Return: estimated range (low / mid / high) with reasoning

### Step 3 — Portfolio Conflict Audit
Check existing sponsorships for the athlete/club:
1. Pull known sponsorships from public sources (Transfermarkt, sports media)
2. Map each to brand category
3. Flag: direct competitor conflicts (same category)
4. Flag: brand value conflicts (e.g., fast food brand + health/nutrition brand)
5. Flag: territory exclusivity overlaps

```
CONFLICT LEVELS:
  🔴 Hard conflict:    Same category, same territory — deal is blocked
  🟡 Soft conflict:    Adjacent category or different territory — negotiable
  🟢 No conflict:      Clear path to partnership
```

### Step 4 — Brand Fit Assessment

Beyond audience demographics (handled by sponsorship-match), assess:

**Values alignment:**
```
athlete_values  = from athlete-social-activity brand voice profile
brand_values    = derived from brand's own marketing language, campaigns, CSR activity
alignment_score = semantic similarity of values × controversy overlap check
```

**Authenticity signal:**
- Has this athlete genuinely used/mentioned this brand category organically?
- Is the brand's existing ambassadors similar in profile to this athlete?
- Will the target audience believe this partnership?
- Authenticity score: 0–100 (high = audience will accept this partnership)

**Controversy risk check:**
- Has either party had recent PR issues?
- Are there category sensitivities (e.g., alcohol brand + athlete with recovery history)?
- Does the athlete's market overlap with regions where the brand has controversy?

### Step 5 — Deal Structure Recommendation

```
RECOMMENDED DEAL STRUCTURE:

Base fee:           £[X] per year
  ├── Image rights (digital):  40% of base
  ├── Appearances (events):    25% of base
  ├── Social content:          20% of base
  └── Kit/product integration: 15% of base

Performance bonuses:
  + Goal milestone bonus (forwards):  £[X] per 10 goals
  + Trophy bonus:                     £[X] per major trophy
  + Appearance bonus:                 £[X] per 30 starts
  + Social milestone:                 £[X] per 1M new followers

Deliverables (suggested minimum):
  - Social posts: [X] per month (platform breakdown)
  - Brand appearances: [X] per year
  - Campaign shoots: [X] per year
  - Fan token activation: 1 token-native campaign per season
  - Exclusivity: [category] / [territory]
  - Contract length: [X] years

KPI commitments (measurable):
  - Minimum social impressions guarantee
  - Fan token holder activation rate target
  - Brand sentiment lift target (pre/post measurement)
```

### Step 6 — Token-Native Integration Layer
For any sponsorship deal involving an athlete or club with active fan tokens:

**Standard integration package:**
1. Token holder exclusivity window — brand offer available to token holders 48h before general public
2. Athlete milestone trigger — performance event (goal, trophy) triggers automatic token holder reward
3. Co-creation poll — token holders vote on a brand creative element (colourway, tagline, design)
4. Token-gated experience — brand-funded VIP experience accessed via token holding
5. Fan token analytics reporting — brand receives quarterly holder engagement report as proof of impact

**Why brands should request this:**
- Measurable, tamper-proof engagement data from blockchain
- Reach fans who are financially committed to the club (token holders ≠ passive audience)
- First-mover positioning in SportFi commercial space
- Direct link to 2026 World Cup national team token audiences

### Step 7 — ROI Framework

Pre-agree measurement criteria before deal launches:

```
MEASUREMENT FRAMEWORK:

Awareness:
  Social impressions delivered vs. contracted
  Brand mention uplift during campaign periods
  Search volume for brand during activations

Engagement:
  Engagement rate on athlete-brand content vs. brand benchmark
  Fan token holder activation rate (where applicable)
  Event attendance / participation numbers

Commercial:
  Website traffic uplift correlated to campaign periods
  Promo code redemption rate
  E-commerce conversion from athlete-linked landing pages

Sentiment:
  Brand sentiment score pre/post deal period
  Fan token holder sentiment toward brand (via Socios community data)
  Net Promoter Score movement in athlete's key markets
```

### Step 8 — Format output

```
SPORTS BRAND & SPONSORSHIP — [ATHLETE / CLUB NAME]
Deal type: [Athlete endorsement / Club partnership]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MARKET RATE ESTIMATE
  Tier:                  Premium (ABS: 74)
  Category:              Sportswear (× 1.4 multiplier)
  Exclusivity:           Category exclusive (+ 40%)
  Tournament uplift:     World Cup 2026 (+25%)
  Estimated annual rate: £820K – £1.4M
  Mid-point benchmark:   £1.1M per year

PORTFOLIO CONFLICT AUDIT
  Existing deals:        Boot deal (Adidas), grooming brand (UK-only)
  Proposed category:     Mobile technology
  Conflict assessment:   🟢 No conflict — clear path to partnership
  Watch flag:            Adidas contract includes right-of-first-refusal on
                         technology wearables — clarify scope before signing

BRAND FIT
  Values alignment:      84 / 100  [Strong — innovation + dedication themes shared]
  Authenticity score:    71 / 100  [Good — athlete has posted tech content organically]
  Controversy risk:      Low — no flags on either side

DEAL STRUCTURE (recommended)
  Base annual fee:       £1.1M
  Social deliverables:   8 posts/month (4 Instagram, 3 TikTok, 1 YouTube)
  Appearances:           4 per year (2 product launches, 2 market activations)
  Token activation:      1 token-native campaign per season (poll + milestone reward)
  Performance bonus:     +£80K if athlete wins Player of the Season
  Contract term:         2 years + option

TOKEN-NATIVE INTEGRATION (recommended)
  Mechanic: Fan token holders get early access to [Brand]'s new product launch
  + athlete co-designed limited edition announced via token holder poll
  Expected holder activation: 18–24% (based on HAS of 74 and similar campaigns)
  Brand gain: 140,000+ engaged sports fans in target markets for launch

ROI FRAMEWORK
  Primary KPI: 45M impressions across contract year (trackable)
  Secondary: Token holder activation rate ≥18%
  Sentiment target: +6 points brand sentiment in Brazil, Spain, UK markets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run fan-token-pulse for live holder data to strengthen activation proposal
→ Run athlete-social-activity for content deliverable benchmarking
→ Generate pitch deck via docx or pdf skill for brand presentation
```

---

## Emerging opportunity scan

When user asks "what brands are looking for athletes like this?":
1. Identify athlete profile: ABS tier, dominant market, content style, age
2. Scan for brands in the right category that are:
   - Actively expanding in athlete's top holder/follower geographies
   - Not currently represented by a comparable athlete
   - Signalling sports marketing investment (hiring, campaign launches, event presence)
3. Return top 5 brand opportunities with rationale

---

## Club commercial partnership mode

For club-level deals (shirt sponsors, stadium naming, training kit):
1. Benchmark against comparable clubs (league position, global following, token HAS)
2. Assess current partnership portfolio for gaps (e.g., no fintech partner, no travel partner)
3. Identify brands with strategic interest in that club's key geographic markets
4. Structure multi-year deal with token ecosystem integration as differentiator

---

## Reference files

- `references/sponsorship-deal-benchmarks.md` — Disclosed sponsorship values by athlete tier and category
- `references/token-activation-templates.md` — Campaign templates per brand category (shared with sponsorship-match)
- `references/endorsement-contract-clauses.md` — Standard and special clause library for sports endorsement deals
- `references/roi-measurement-tools.md` — Third-party measurement platforms and methodologies *(planned)*
- `references/conflict-matrix.md` — Brand category conflict and exclusivity mapping *(planned)*

---

## Environment variables

```
X_BEARER_TOKEN=<key>          # Social mention monitoring for ROI tracking
BRANDWATCH_API_KEY=<key>      # Optional: brand sentiment tracking
SIMILARWEB_API_KEY=<key>      # Optional: brand traffic/audience data
```
