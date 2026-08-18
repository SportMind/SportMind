# Source Registry

Domain: intelligence/source-registry.md
Version: v4.6.0
Library Rule: Six-Month Test PASSES · Proper Noun Test PASSES
Scope: Canonical registry of all sources scanned during SMI
briefings. Defines tier classification, split rules, scan
frequency, failure mode rules, and standing protocols per
source. Load before any briefing to confirm correct source
tier before acting on any signal. Companion to
intelligence/country-scan/ (all files) ·
fan-token/holder-tax-framework.md · macro/regulatory/ (all) ·
core/compound-signal-framework.md.

---

TIER DEFINITIONS

TIER 1 — Primary confirmed source. Official. Direct. No aggregation.
  Library action permitted on Tier 1 signals without cross-reference.
  Always cite the specific Tier 1 source in any library action.

TIER 2 — Reliable secondary source. Editorial standards confirmed.
  Library action requires cross-reference with one other Tier 1
  or Tier 2 source before committing. Never act on Tier 2 alone.

AGGREGATOR — Aggregates from multiple sources without independent
  verification. FM1 applies to all price and sentiment content.
  FM2 applies to all speculation and rumour content.
  No library action without Tier 1 or Tier 2 confirmation.

SPLIT RULE — applies when a single source produces both
  library-quality content AND noise. Agent must classify content
  type before applying tier. Never apply the higher tier to the
  lower content type. Format:
  [Source]: [content type A] = Tier [N] ·
    [content type B] = FM[N] (no library action)

---

SECTION 1 — CHILIZ ECOSYSTEM SOURCES

chiliz.com (primary newsroom)
  Tier: 1 · Scan: every briefing
  Content: partnership announcements · token launches · regulatory
    filings · OFT confirmations · white paper releases ·
    Greenhouse programme updates
  Split rule: newsroom articles = Tier 1 ·
    price or market commentary = FM1 (perishable · no action)
  Library action: YES on partnership and structural announcements
  Key use: HP flag confirmation · OFT verification ·
    eu-mica.md updates · complete-registry.md updates

chiliz.com/blog (separate from newsroom — check both)
  Tier: 1 · Scan: every briefing
  Content: product announcements · ecosystem updates ·
    releases sometimes appear here before newsroom
  Note: check newsroom AND blog — they are separate endpoints
  Library action: YES on structural announcements

socios.com
  Tier: 1 · Scan: every briefing
  Content: Fan Token Play announcements · FTP · governance votes ·
    PTG burn confirmations · engagement mechanic updates ·
    new token launch announcements
  Library action: YES on FTP · PTG · governance — these are supply
    events. Cross-reference chiliz.com for confirmation.
  Key use: fan-token-play.md · burn-to-glory-framework.md

chiliscan.com
  Tier: 1 · Scan: every briefing
  Content: on-chain verification · $PEPPER buy-back volumes ·
    PTG burn transaction confirmations · OFT bridge movements ·
    18-decimal migration tracking · token supply changes ·
    large wallet movements · token velocity data
  Library action: YES on confirmed on-chain supply events
  Key use: HP-3 $PEPPER buy-back · defi-integration-intelligence.md ·
    on-chain intelligence (Section 4)

Chiliz Chain Explorer (explorer.chiliz.com)
  Tier: 1 · Scan: when supply event suspected or chiliscan.com
    signal requires verification
  Content: raw on-chain data · transaction verification ·
    token contract events · holder count changes
  Library action: YES as cross-reference for chiliscan.com signals
  Note: raw data requires interpretation — confirm via chiliscan.com

fantokens.com (newsroom articles)
  Tier: 2 (confirmed news) · Aggregator (price/sentiment)
  Scan: every briefing
  Split rule: confirmed news and partnership articles = Tier 2 ·
    price ranges · market sentiment · named individual performance
    = FM1 (no library action)
  Library action: Tier 2 content only · always cross-reference
    Tier 1 before library action
  Note: often surfaces signals before chiliz.com — treat as alert
    mechanism · confirm via Tier 1 before committing

---

SECTION 2 — CRYPTO REGULATORY AND MACRO SOURCES

CoinDesk (coindesk.com)
  Tier: 2 (regulatory/institutional) · Aggregator (price/sentiment)
  Scan: every briefing
  Split rule:
    Regulatory analysis · jurisdiction reporting · institutional
    adoption · MiCA/ESMA coverage · legislative updates ·
    confirmed exchange listings = TIER 2 ·
    cross-reference with official regulatory body before
    library action
    Price commentary · market sentiment · token price ranges
    · speculative analysis = FM1 (no library action)
  Library action: Tier 2 regulatory content only
  Key use: MiCA updates · jurisdiction signals · CHZ macro layer ·
    Russia · Brazil · Turkey regulatory monitoring ·
    HP flag tracking · exchange intelligence

CoinTelegraph (cointelegraph.com)
  Tier: 2 (regulatory/legislative) · Aggregator (price/sentiment)
  Scan: every briefing
  Split rule:
    Regulatory reporting · legislative analysis · jurisdiction
    updates · confirmed crypto legal status changes = TIER 2
    Price predictions · market sentiment · altcoin speculation
    = FM1 (no library action)
  Library action: Tier 2 regulatory content only
  Key use: jurisdiction updates · regulatory HP flags ·
    South Korea · UAE · Saudi Arabia monitoring ·
    global crypto legislative tracker

The Block (theblock.co)
  Tier: 2 (institutional reporting and research) · Aggregator (price)
  Scan: every briefing
  Split rule:
    Institutional adoption · research reports · confirmed data ·
    on-chain analytics · regulatory developments ·
    venture capital flows into sports tech/fan tokens = TIER 2
    Price analysis · market commentary = FM1
  Library action: Tier 2 content · especially institutional
    adoption signals relevant to CHZ market cycle framework
  Key use: macro/chz-market-cycle-framework.md ·
    institutional crypto adoption · competitor intelligence ·
    DeFi intelligence · sports tech investment signals

Decrypt (decrypt.co)
  Tier: 2 (consumer crypto and regulatory) · Aggregator (price)
  Scan: every briefing
  Split rule:
    Regulatory news · confirmed product launches · exchange
    listings · legislative developments · confirmed ecosystem
    events = TIER 2
    Price movement commentary · speculation = FM1
  Library action: Tier 2 content only
  Key use: Russia daily scan · general regulatory monitoring ·
    consumer crypto product signals · US regulatory coverage

DL News (dlnews.com)
  Tier: 2 · Scan: every briefing
  Specialism: EU regulatory reporting · MiCA · FCA · ESMA ·
    European crypto legislation in depth
  Split rule: all regulatory analysis = Tier 2 ·
    price/market content = FM1
  Library action: YES on EU and UK regulatory signals
  Key use: eu-mica.md monitoring · FCA gateway monitoring ·
    MiCA individual white paper registration tracking ·
    ESMA Q&A signals · MiCA review December 2027

OECD (oecd.org)
  Tier: 1 · Scan: monthly · escalate immediately on CARF signal
  Content: Crypto-Asset Reporting Framework (CARF) implementation
    updates · global tax information exchange framework ·
    country-by-country CARF adoption timelines
  Library action: YES on CARF implementation confirmations —
    affects holder anonymity and demand behaviour in every
    jurisdiction simultaneously
  Key use: every Tier A country scan · global tax intelligence ·
    cross-border holder behaviour modelling
  Note: CARF is a global macro signal — when any country confirms
    CARF implementation, flag in that country's scan file AND
    in the briefing as a cross-jurisdictional signal

---

SECTION 3 — REGULATORY BODY SOURCES (by jurisdiction)

GLOBAL / EU:
  esma.europa.eu (ESMA) — Tier 1 · weekly scan
    MiCA implementation · fan token white paper registry ·
    Q&A publications · individual token ESMA filings
    Escalate: any fan token white paper confirmation or
    classification guidance
  Source: eu-mica.md

  europa.eu (European Commission) — Tier 1 · on signal
    Digital Finance Package · MiCA legislative updates ·
    EU AI Act (SportMind commercial relevance) ·
    EU competition law applied to football
    Escalate: any digital finance legislation affecting crypto assets

  ecb.europa.eu (European Central Bank) — Tier 1 · on signal
    Crypto stance statements · digital euro developments ·
    payment token classifications

ITALY:
  consob.it (CONSOB) — Tier 1 · weekly
  bancaditalia.it (Banca d'Italia) — Tier 1 · monthly
  agenziaentrate.gov.it (Tax authority) — Tier 1 · on signal

BRAZIL:
  congress.leg.br — Tier 1 · daily (MP 1.303 active)
  bcb.gov.br (Banco Central do Brasil) — Tier 1 · weekly
  cvm.gov.br (CVM — securities) — Tier 1 · monthly

TURKEY:
  spk.gov.tr (SPK — Capital Markets Board) — Tier 1 · weekly
  masak.gov.tr (MASAK — financial intelligence) — Tier 1 · monthly
  tcmb.gov.tr (TCMB — Central Bank) — Tier 1 · monthly

UK:
  fca.org.uk (FCA) — Tier 1 · weekly
    Crypto asset gateway · MARC framework · fan token classification
    Escalate: any fan token classification update or
    MARC timeline change

GERMANY:
  bafin.de (BaFin) — Tier 1 · weekly
    German crypto regulation · MiCA implementation ·
    consumer crypto guidance

JAPAN:
  fsa.go.jp (FSA — Financial Services Agency) — Tier 1 · weekly
    Crypto exchange licensing · token classification ·
    HP-2 Tokyo Verdy regulatory context

USA:
  sec.gov (SEC) — Tier 1 · weekly · ESCALATE on any fan token mention
    Securities classification risk · enforcement actions ·
    any crypto asset ruling with fan token implications
  cftc.gov (CFTC) — Tier 1 · monthly
    Commodity classification · derivatives on fan tokens
  ftc.gov (FTC) — Tier 1 · on signal
    Consumer protection · fan token marketing claims

PORTUGAL:
  cmvm.pt (CMVM) — Tier 1 · monthly
    MiCA implementation · securities regulation
  at.gov.pt (Autoridade Tributária) — Tier 1 · on signal
    CGT status · holding period rules (currently 0% after 365 days)

ARGENTINA:
  bcra.gob.ar (BCRA) — Tier 1 · weekly
    Crypto stance · exchange controls · peso volatility context
  cnv.gob.ar (CNV — securities) — Tier 1 · monthly

SOUTH AFRICA:
  sars.gov.za (SARS) — Tier 1 · daily until August 31 (HP active)
  fsca.co.za (FSCA) — Tier 1 · monthly

RUSSIA:
  cbr.ru (Bank of Russia) — Tier 1 · daily from September 1
    Eligible asset list · crypto regulatory guidance ·
    HP-11 fan token eligibility
    Escalate: immediately on any fan token eligibility announcement

MALTA (Chiliz regulatory home):
  mfsa.mt (MFSA) — Tier 1 · monthly
    Chiliz MiCA notification gateway · individual fan token
    white paper filings · CASP licensing
    Note: MFSA is the EU gateway for all Chiliz MiCA filings —
    more important than most Tier 1 regulatory sources for
    direct Chiliz ecosystem intelligence

---

SECTION 4 — SPORTS INTELLIGENCE SOURCES

UEFA.com — Tier 1 · every briefing
  Competition calendar · UCL/UEL/UECL draws · results ·
  trophy records · squad registration · coefficient rankings ·
  financial fair play rulings · club licensing decisions
  Library action: YES on competition structure changes and
  financial fair play rulings (CDI signals)
  Key use: competition-calendar-framework.md · trophy verification ·
    trophy-premium-framework.md · rivalry fixture confirmation

FIFA.com — Tier 1 · every briefing
  World Cup calendar · national team competitions ·
  PTG tournament triggers · FIFA rankings · transfer windows ·
  governance decisions · competition format changes
  Library action: YES on tournament structure and PTG triggers
  Key use: WC calendar · national token PTG burns ·
    burn-to-glory-framework.md · fan-base-intelligence.md

CONMEBOL.com — Tier 1 · every briefing (ACTIVE — Libertadores R16)
  Copa Libertadores · Copa Sudamericana · results ·
  match schedules · venue confirmations · fixture changes
  Library action: YES on competition results and structural changes
  Key use: Brazilian cluster calibration records ·
    Libertadores occasion weight · $FLU/$VERDAO/$MENGO/$SCCP

BBC Sport (bbc.co.uk/sport) — Tier 2 · every briefing
  Split rule: confirmed managerial appointments and departures ·
    confirmed injuries · confirmed squad news · official results
    · confirmed transfer completions = TIER 2
    Transfer speculation · opinion · predictions · rumours = FM2
  Library action: Tier 2 confirmed news only (no named individuals)
  Key use: UK club CDI signals ($AFC · $SPURS · $CITY) ·
    $SFA national team · coaching succession framework

ESPN (espn.com) — Tier 2 · every briefing
  Split rule: confirmed results · official roster moves ·
    confirmed managerial changes · confirmed card announcements
    ($UFC/$PFL) = TIER 2
    Trade rumours · speculation · opinion = FM2
  Library action: Tier 2 confirmed news only
  Key use: Brazilian cluster CDI · US College HP-7 ·
    MMA ($UFC/$PFL confirmations) · $MENGO/$VERDAO/$FLU/$SCCP

Sky Sports (skysports.com) — Tier 2 · every briefing
  Split rule: confirmed transfers · confirmed appointments ·
    confirmed results = Tier 2 · speculation = FM2
  Library action: Tier 2 confirmed news only
  Key use: UK club CDI signals · transfer window (confirmed only) ·
    Premier League structural news

Goal.com — Tier 2 · every briefing
  Split rule: confirmed results and schedules = Tier 2 ·
    speculation = FM2
  Library action: Tier 2 confirmed content only
  Key use: South American football schedules · return leg timing ·
    Brazilian cluster · general football calendar

Globo Esporte (ge.globo.com) — Tier 2 · every briefing
  Content: Brasileirão · Copa do Brasil · Brazilian national team ·
    CDI signals for all 9 Brazilian cluster tokens
  Split rule: confirmed news = Tier 2 · speculation = FM2
  Library action: Tier 2 confirmed news only
  Key use: Brazilian cluster CDI signals ($MENGO $VERDAO $FLU
    $SCCP $SPFC $GALO $SACI $VASCO $BAHIA)

TRT Spor (trtspor.com.tr) — Tier 2 · every briefing
  Content: Süper Lig · Turkish cup · Turkish national team
  Split rule: confirmed news = Tier 2 · speculation = FM2
  Library action: Tier 2 confirmed news only
  Key use: $GAL · $TRA · Turkish cluster CDI signals

beIN Sports (beinsports.com) — Tier 2 · every briefing
  Content: Middle East · North Africa · global sports
  Library action: Tier 2 confirmed content
  Key use: South American football · $FLU/$VERDAO etc

MMA Fighting (mmafighting.com) — Tier 2 · every briefing
  Split rule: confirmed card announcements · confirmed results ·
    confirmed weigh-in results = Tier 2 ·
    rankings speculation · fight predictions = FM2
  Library action: Tier 2 confirmed content
  Key use: $UFC/$PFL card confirmations · weigh-in results ·
    MMA calibration records · mma-intelligence-framework.md

MMA Junkie (mmajunkie.com) — Tier 2 · every briefing
  Same split rule as MMA Fighting · use as cross-reference
  Key use: UFC/PFL card tier confirmation (PPV vs Fight Night)

ESPN MMA (espn.com/mma) — Tier 2 · every briefing
  Same split rule · ESPN MMA cross-reference for card confirmations

Record.pt / A Bola (record.pt · abola.pt) — Tier 2 · every briefing
  Content: Portuguese football primary · FPF national team ·
    $POR CDI signals · Portuguese league news
  Split rule: confirmed news = Tier 2 · speculation = FM2
  Key use: $POR national token CDI · Portuguese sporting landscape

ESPN Argentina / TyC Sports — Tier 2 · every briefing
  Content: Argentine football primary · AFA national team ·
    $ARG CDI signals
  Split rule: confirmed news = Tier 2 · speculation = FM2
  Key use: $ARG national token · Copa signals · WC2030 qualifying

MLS.com — Tier 2 · on signal
  Content: Major League Soccer · US soccer landscape ·
    any Chiliz MLS partnership signals
  Library action: Tier 2 confirmed content · escalate any
    Chiliz MLS partnership to Strategy & Brainstorm
  Key use: US sporting landscape · HP-7 US College context

---

SECTION 5 — ON-CHAIN INTELLIGENCE SOURCES

chiliscan.com — Tier 1 (see Section 1)
Chiliz Chain Explorer — Tier 1 (see Section 1)

Dune Analytics (dune.com)
  Tier: 2 · Scan: weekly
  Content: Chiliz Chain dashboards · fan token holder analytics ·
    trading volume by token · wallet concentration analysis ·
    on-chain activity metrics
  Split rule: on-chain data analysis = Tier 2 ·
    price commentary = FM1
  Library action: Tier 2 on-chain data · cross-reference
    chiliscan.com before any library action
  Key use: holder behaviour patterns · fan-base-intelligence.md ·
    fan-holder-behaviour.md · liquidity pool intelligence

Kayen Finance on-chain (kayen.finance)
  Tier: 1 · Scan: every briefing (for $PEPPER buy-back signal)
  Content: DEX volume data · $PEPPER buy-back confirmation ·
    liquidity pool depth · trading pair availability
  Library action: YES on $PEPPER buy-back confirmation (HP-3)
  Key use: HP-3 · defi-integration-intelligence.md ·
    $PEPPER governance intelligence

FanX on-chain (app.fanx.xyz)
  Tier: 1 · Scan: every briefing (testnet status monitor)
  Content: DEX live volume · prediction market status ·
    mainnet launch signal
  Library action: YES on mainnet launch confirmation (HP-1)
  Note: TESTNET ONLY as of v4.6.0 · Sept 12 2026 HP-1 expiry

---

SECTION 6 — EXCHANGE INTELLIGENCE SOURCES

CoinMarketCap (coinmarketcap.com)
  Tier: 2 (exchange listings only) · Aggregator (all else)
  Scan: every briefing
  Split rule: confirmed new exchange listings for fan tokens
    or $CHZ · confirmed delistings · new trading pairs = TIER 2
    Price data · market cap rankings · sentiment = FM1 (no action)
  Library action: Tier 2 listing changes only
  Key use: fan token accessibility by jurisdiction ·
    $CHZ exchange coverage · new market access signals
  Note: a new $CHZ listing in a Tier B country = demand signal ·
    escalate to Strategy & Brainstorm

CoinGecko (coingecko.com)
  Tier: 2 (exchange listings) · Aggregator (all else)
  Scan: every briefing · cross-reference CoinMarketCap
  Same split rule as CoinMarketCap
  Key use: fan token listing verification · exchange coverage map

OKX Blog (okx.com/learn)
  Tier: 2 · Scan: weekly
  Content: OKX exchange announcements · new listing confirmations ·
    CHZ/fan token trading pair updates · OKX DEX developments
  Split rule: confirmed listings/product announcements = Tier 2 ·
    market commentary = FM1
  Key use: OKX DEX (Agentic Finance execution layer future) ·
    fan token trading pair availability

Binance Blog (binance.com/en/blog)
  Tier: 2 · Scan: weekly
  Content: Binance listing announcements · fan token availability ·
    CHZ trading pairs · regulatory compliance updates by region
  Split rule: confirmed announcements = Tier 2 · commentary = FM1
  Key use: largest exchange · CHZ/fan token global accessibility

---

SECTION 7 — SOCIAL INTELLIGENCE PROTOCOL

NOTE: Social sentiment = FM1 always. This section covers
STRUCTURED social intelligence only — not price sentiment.

WHAT QUALIFIES AS STRUCTURED SOCIAL INTELLIGENCE:
  · Official club or Socios account governance vote announcement
  · Confirmed FTP or PTG event announced via official channel
  · Chiliz/Socios product launch announced via official social
  · Official competition authority draw or result confirmation
  · Confirmed managerial/ownership change via official club channel

WHAT DOES NOT QUALIFY (FM1 or FM2 applies):
  · Price commentary · "to the moon" · buy/sell signals
  · Fan token price predictions · market sentiment
  · Transfer rumours from social accounts (even large ones)
  · Unverified competition results

SOURCES (when accessible):
  @Chiliz (X/Twitter) — BLOCKED via automated access ·
    monitor manually when possible · flag as UNVERIFIED
    until confirmed via Tier 1/2 source
  @FanTokens (X/Twitter) — BLOCKED · same restriction
  @Socios (X/Twitter) — BLOCKED · same restriction
  Official club social accounts — monitor manually for
    governance announcements · confirm via Tier 1 before action

Socios.com platform (app.socios.com)
  Tier: 1 · Scan: every briefing
  Content: active governance votes · fan polls · FTP rewards ·
    engagement mechanics · token-specific announcements
  Library action: YES on confirmed governance/FTP events

Reddit (reddit.com/r/socios · r/chiliz)
  Aggregator · Scan: weekly
  Split rule: community reports of confirmed announcements
    (cross-reference with Tier 1 before any action) = alert only ·
    all price/sentiment content = FM1
  Library action: NEVER direct from Reddit ·
    use only as signal to check Tier 1/2 sources

---

SECTION 8 — COMPETITOR INTELLIGENCE SOURCES

The Block research (theblock.co/research)
  Tier: 2 · Scan: weekly
  Content: sports tech investment reports · fan engagement
    platform analysis · blockchain sports ecosystem mapping
  Key use: competitor landscape · market positioning ·
    structural sports tech signals

CoinDesk features (coindesk.com/business)
  Tier: 2 · Scan: weekly
  Content: sports blockchain ecosystem reporting ·
    competitor platform analysis
  Key use: any new fan token platform launch ·
    competitor failure signals (validates Chiliz positioning)

Fan token competitor platforms to monitor:
  Bitci.com — Tier 2 · on signal ·
    Former competitor · monitor for any reactivation
  Rally (rally.io) — Tier 2 · on signal ·
    Declined significantly · monitor for lessons
  Any new entrant — flag as UNCLASSIFIED SIGNAL ·
    escalate to Strategy & Brainstorm immediately

---

SECTION 9 — MACROECONOMIC INTELLIGENCE SOURCES

Federal Reserve (federalreserve.gov) — Tier 1 · on signal
  Content: interest rate decisions · risk appetite signals ·
    any crypto asset statements
  Key use: macro/chz-market-cycle-framework.md ·
    risk-on/risk-off assessment for CHZ regime

ECB (ecb.europa.eu) — Tier 1 · on signal
  Content: European monetary policy · digital euro ·
    crypto asset stance
  Key use: EU Tier A country scans · CHZ macro regime

BTC price and cycle (CoinDesk aggregator — FM1 for price)
  Note: BTC cycle POSITION (halving proximity · cycle stage) is
  structural context — not a price signal. Load as directional
  context only. Never quote BTC price in SMI output.
  BTC cycle stage = macro context for CHZ regime assessment.

G20 crypto framework
  Tier: 2 · on signal · track via CoinDesk/The Block
  Content: G20 crypto regulatory harmonisation ·
    global stablecoin framework · FATF recommendations
  Key use: global regulatory macro · multi-jurisdiction signals

---

SECTION 10 — TECHNOLOGY AND PRODUCT INTELLIGENCE SOURCES

Chiliz GitHub (github.com/chiliz)
  Tier: 1 · Scan: weekly
  Content: Chiliz Chain release notes · smart contract updates ·
    SDK releases · network upgrades · hard fork announcements
  Library action: YES on network upgrades and new mechanics
  Key use: defi-integration-intelligence.md · staking-intelligence ·
    OFT bridge intelligence

Chiliz Developer Docs (docs.chiliz.com)
  Tier: 1 · Scan: monthly
  Content: token contract addresses · developer API updates ·
    integration documentation changes
  Library action: YES on contract address changes or new tokens
  Key use: complete-registry.md verification ·
    fan-token/registry/ updates

SportMind GitHub (github.com/SportMind/SportMind)
  Tier: 1 · Scan: every Build Chat session
  Content: CHANGELOG · file updates · version tracking
  Key use: internal library state verification ·
    CHANGELOG cross-reference for TO-DO updates

---

SECTION 11 — INTERNAL SPORTMIND STATE CHECK

Run at start of every briefing. Confirms internal state
before external intelligence scan begins.

CHECK 1 — LIBRARY VERSION:
  Confirm current library version from CHANGELOG ·
  State in briefing header: Library state: v[X.X.X]
  If unknown: check github.com/SportMind/SportMind/CHANGELOG.md

CHECK 2 — SMI PROMPT VERSION:
  Confirm SMI prompt version from Drive doc header ·
  State in briefing: SMI prompt: v[X.X.X]
  If stale: flag for Strategy & Brainstorm to bump

CHECK 3 — OPEN CALIBRATION RECORDS:
  Any pre-match records submitted but not yet closed? ·
  Any return leg results due that need post-match filing? ·
  Flag all open records in briefing

CHECK 4 — HP FLAG EXPIRY CHECK:
  Any HP flags within 14 days of 90-day expiry clock? ·
  Any HP flags that should be retired (Tier 1 confirmed negative)? ·
  Flag for Strategy & Brainstorm

CHECK 5 — REGULATORY DEADLINE CHECK:
  Any T-30 or closer regulatory deadlines? ·
  List all active countdown timers ·
  Escalate any T-7 or closer

CHECK 6 — TO-DO ALIGNMENT:
  Does the briefing header match the current TO-DO library state? ·
  If discrepancy: note and flag for Strategy & Brainstorm

---

SECTION 12 — SCAN FREQUENCY SCHEDULE

EVERY BRIEFING:
  Chiliz ecosystem: chiliz.com · chiliz.com/blog · socios.com ·
    chiliscan.com · Kayen Finance · FanX · fantokens.com
  Crypto regulatory: CoinDesk · CoinTelegraph · The Block ·
    Decrypt · DL News
  Sports: UEFA.com · FIFA.com · CONMEBOL.com · BBC Sport ·
    ESPN · Sky Sports · Goal.com · Globo Esporte · TRT Spor ·
    beIN Sports · MMA Fighting · MMA Junkie · ESPN MMA ·
    Record.pt · ESPN Argentina / TyC Sports
  Exchange: CoinMarketCap · CoinGecko
  Social: Socios.com platform (app.socios.com)
  Internal: SportMind state check (Section 11)

DAILY (active protocols):
  sars.gov.za — until August 31 (T-30 SARS active)
  congress.leg.br — MP 1.303 monitoring
  cbr.ru — from September 1 (HP-11 Russia provisions)

WEEKLY:
  fca.org.uk · esma.europa.eu · bafin.de · fsa.go.jp ·
  mfsa.mt · Dune Analytics · OKX Blog · Binance Blog ·
  Chiliz GitHub · The Block research ·
  OECD (CARF monitoring) · competitor intelligence scan ·
  Reddit r/socios (alert only — no direct library action) ·
  MLS.com (on signal threshold)

MONTHLY:
  bancaditalia.it · cvm.gov.br · masak.gov.tr · tcmb.gov.tr ·
  cmvm.pt · cnv.gob.ar · fsca.co.za · bcb.gov.br ·
  Chiliz Developer Docs · ecb.europa.eu · G20 framework scan

ON SIGNAL (when HP flag or known trigger active):
  Chiliz Chain Explorer · specific regulatory bodies ·
  country-scan Tier C/D triggers · competitor new entrant alert

ANNUAL:
  Global scan protocol (see Section 18)

---

SECTION 13 — FAILURE MODE REFERENCE

FM1 — PRICE AND SENTIMENT NOISE:
  Never file: price ranges · market sentiment · surge headlines ·
    fan token price predictions · BTC price ·
    "10% fan token market surge" style headlines
  Apply to: all aggregator price content · social sentiment ·
    fantokens.com price ranges · CoinDesk market commentary

FM2 — SPECULATION AND RUMOUR:
  Never file: transfer rumours · unconfirmed managerial moves ·
    "sources claim" reporting · analyst predictions
  Apply to: Sky Sports transfer speculation ·
    ESPN rumours · unnamed source reporting

FM3 — NAMED INDIVIDUAL VIOLATION:
  Library Rule FAILS on named athletes · managers · executives ·
    named referees · named arbitrators
  Encode as structural archetype only ·
    "confirmed head coach departure" not "[Name] sacked"
  Apply to: all sports reporting involving named individuals

FM4 — MISLEADING GROUPING:
  Never group tokens that share a category but not a status ·
  Example: $ITA grouped with WC-qualified national tokens ·
    $ITA = zero PTG burns · NEVER group with $SPAIN/$ARG/$POR
  Apply to: fantokens.com comparative articles ·
    aggregator national token roundups

FM5 — STALE SIGNAL RETENTION:
  HP flags expire after 90 days without Tier 1 confirmation ·
  Apply to: any HP flag approaching 90-day clock ·
  Flag in briefing 14 days before expiry ·
  Bring to Strategy & Brainstorm for retirement decision

FM6 — CDI GATE MISAPPLICATION:
  Never apply full compound signal to a TRANSITION gate token ·
  Never produce high-confidence output for TRANSITION ·
  Never upgrade CDI gate without Strategy & Brainstorm review
  Apply to: all pre-match analysis and briefing demand signals

FM7 — SUPPLY EVENT CONFUSION:
  Never conflate PTG burns (supply reduction) with demand signals ·
  Never apply $AFC PATH_2 mechanics to any other token ·
  Never assume symmetry in dual-token supply events
  Apply to: all national token and $AFC fixture analysis

---

SECTION 14 — NEW COUNTRY DETECTION PROTOCOL

Any of the following triggers automatic new country assessment.
Flag in briefing as: NEW COUNTRY SIGNAL — [Country] —
assess for tier placement — escalate to Strategy & Brainstorm

TRIGGERS:
  · Chiliz announces any partnership in a country not in Tier A/B/C
  · A fan token reports significant holder activity in a new
    jurisdiction (via chiliscan.com or Dune Analytics)
  · Any regulatory body in any country makes a statement
    specifically about fan tokens
  · CoinDesk/CoinTelegraph reports a country-level crypto
    development that explicitly mentions fan tokens or Socios
  · A new national team token launches for any country
  · A new club token launches for a club in a country not yet
    in the scan architecture
  · Any country confirms CARF implementation (OECD signal)

ON TRIGGER:
  Step 1: Flag in briefing as UNCLASSIFIED COUNTRY SIGNAL
  Step 2: Note: potential tier placement [A/B/C/D]
  Step 3: Note: which existing library files may need updating
  Step 4: ESCALATE TO STRATEGY & BRAINSTORM before any
    library action or tier assignment

---

SECTION 15 — UNKNOWN UNKNOWNS OPEN SCAN PROTOCOL

Weekly open scan — no predefined topic. Asks:
"What has happened in the last 7 days at the intersection of
sports, blockchain, and fan engagement that SportMind does
not currently track?"

SEARCH TERMS (run each independently):
  "fan token" · "Chiliz" · "Socios" · "sports blockchain" ·
  "football token" · "sports NFT regulation" · "fan engagement
  blockchain" · "$CHZ" · any active token cashtag

SOURCES: CoinDesk · CoinTelegraph · The Block · Decrypt ·
  Google News (sports + blockchain filter)

ON UNCLASSIFIED RESULT:
  Flag in briefing as:
  UNCLASSIFIED SIGNAL:
    Source: [source · tier]
    Signal: [structural description — no names · no prices]
    Why flagged: [relevance reasoning]
    Potential impact: [which SportMind domain]
    Action: ESCALATE TO STRATEGY & BRAINSTORM
    Priority: [HIGH / MEDIUM / LOW]

  Never discard an unclassified signal silently.
  Never classify without Strategy & Brainstorm review.
  The flag is the deliverable — not the classification.

---

SECTION 16 — ATHLETE AND MANAGEMENT INTELLIGENCE PROTOCOL

Named individuals ALWAYS fail the Library Rule (FM3).
But structural signals from the same events often PASS.

PASSES LIBRARY RULE (structural · 6-month test · file in CDI):
  Confirmed head coach departure (mid-season or end of season)
  Confirmed new head coach appointment
  Confirmed key player season-ending injury (archetype only:
    "first-choice goalkeeper confirmed out for season")
  Confirmed new sporting director / ownership change
  Confirmed club administration / financial restructuring
  Confirmed points deduction or sporting sanction

FAILS LIBRARY RULE (named individual · FM3 applies):
  "[Name] sacked" — encode as: "confirmed head coach departure"
  "[Name] scores" — never file match scorer names
  "[Name] injured" — encode as archetype if season-ending confirmed
  "[Name] signs" — encode as: "confirmed [position] acquisition"

HOW TO FILE CDI SIGNALS FROM THESE EVENTS:
  Load the relevant CDI file (market/club-intelligence/[token].md) ·
  Encode structurally · no named individuals ·
  Flag for CDI gate reassessment if change is material ·
  Bring to Strategy & Brainstorm for CDI gate update if warranted

---

SECTION 17 — PARTNERSHIP AND COMMERCIAL INTELLIGENCE PROTOCOL

Commercial developments that constitute CDI signals:

PASSES LIBRARY RULE (structural):
  Confirmed new shirt sponsor (major commercial deal)
  Confirmed stadium naming rights deal
  Confirmed new broadcast deal for league with active tokens
  Confirmed club acquisition by new ownership
  Confirmed club financial distress or administration
  Confirmed significant player acquisition or departure
    (encode as position and fee bracket — not named individual)

SOURCES FOR COMMERCIAL INTELLIGENCE:
  BBC Sport (confirmed deals only — no speculation)
  Sky Sports (confirmed only — FM2 for all speculation)
  Official club announcements via club websites (Tier 1)
  UEFA/FIFA official (financial fair play decisions)
  The Athletic (confirmed only · when accessible)

HOW TO FLAG:
  If commercial signal may change CDI gate:
  Flag in briefing as: CDI SIGNAL — $[TOKEN] —
    [structural description] — assess for gate impact —
    escalate to Strategy & Brainstorm

---

SECTION 18 — SPORTS GOVERNANCE INTELLIGENCE PROTOCOL

Sports governance changes that affect fan token signals:

MONITOR:
  League expansion or format changes (new clubs · playoff format)
  Financial fair play ruling against active token club
  Competition disqualification or points deduction
  Player strikes or lockouts affecting competition calendar
  Competition format changes (UCL expansion was structural)
  Match-fixing investigations involving active token clubs
  La Liga/FIFA governance dispute — Tier 2 only · escalate on
    any ruling that could affect token club participation

SOURCES:
  UEFA.com (Tier 1 · governance decisions)
  FIFA.com (Tier 1 · governance decisions)
  BBC Sport (Tier 2 · confirmed governance news)
  CoinDesk (Tier 2 · crypto/sports intersection governance)

HOW TO FLAG:
  Flag as: GOVERNANCE SIGNAL — [competition/body] —
    [structural description] — [affected tokens] —
    assess for occasion weight or CDI impact

---

SECTION 19 — ANNUAL GLOBAL SCAN PROTOCOL

Run once per year (recommend: start of each calendar year).

PURPOSE: catch drift — countries that have become relevant
without triggering a specific detection signal.

PROCEDURE:
  Step 1: Load fan-token/registry/complete-registry.md
  Step 2: For every active token, identify primary holder
    jurisdiction (via fan-base-intelligence.md register)
  Step 3: Cross-reference against Tier A/B/C/D registers
  Step 4: Any jurisdiction with 2+ active tokens and no
    country scan file = assess for tier placement
  Step 5: Any jurisdiction with a materially changed regulatory
    environment since last scan = reassess tier
  Step 6: Any new token with an untracked primary jurisdiction
    = immediate tier assessment
  Step 7: Bring all findings to Strategy & Brainstorm

OUTPUT: annual global scan report in briefing format ·
  list of tier changes proposed · list of new entries needed ·
  list of any retired entries (no longer relevant)

---

MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a 1b 1c 1d | ACTIVE |
| 2. Reasoning | 2a 2b 2c 2d | ACTIVE |
| 3. Context | 3a 3b 3c | ACTIVE |
| 4. Memory | 4a 4b 4c | ACTIVE |
| 5. Judgment | 5a 5b 5c 5d | ACTIVE |
| 6. Attention | 6a 6b 6c | ACTIVE |
| 7. Communication | 7a 7b 7c | ACTIVE |
| 8. Verification | 8a 8b 8c 8d | ACTIVE |
| 9. Learning | 9a 9b 9c | ACTIVE |
| 10. Integration | 10a 10b | ACTIVE |
| 11. Calibration | 11a 11b 11c 11d | ACTIVE |
| 12. Adaptation | 12a 12b 12c 12d | ACTIVE |
| 13. Ethics | 13a 13b 13c 13d | ACTIVE |
| 14. Transparency | 14a 14b 14c 14d | ACTIVE |
| 15. Execution | 15a 15b 15d | ACTIVE |
| 16. Collaboration | 16a 16b 16c 16d | ACTIVE |

COMPATIBILITY: all SportMind files · SMI prompt v4.4.9+ ·
  intelligence/country-scan/ (all) · macro/regulatory/ (all) ·
  fan-token/holder-tax-framework.md · core/compound-signal-framework.md ·
  market/fan-base-intelligence.md · market/rivalry-intelligence.md ·
  market/trophy-premium-framework.md ·
  market/dual-fan-token-match-dynamics.md

LAST VERIFIED: 2026-08-18
Version: v4.6.0
© 2026 SportMind
