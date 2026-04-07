# Netball — Token Intelligence

Bridge skill connecting netball events to fan token and prediction market signals.
Netball has the strongest gender demographics of any sport in the library (75%+
female fanbase), the most concentrated commercial infrastructure of any Commonwealth
sport outside cricket, and is undergoing the fastest Tier 2→1 commercial
transition of any sport tracked in SportMind.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 transitioning → Tier 1
  No active Socios tokens at time of writing — but fastest-moving Tier 2 sport
  75%+ female fanbase = unique audience not well-served by existing fan tokens
  Caitlin Clark halo effect: women's sport commercial momentum across all codes
  Netball World Cup 2027 (Australia): catalyst window aligning with AFL/RWC 2027

SIGNAL CHARACTERISTICS:
  Most commercially significant: ANZ Premiership (NZ) + SSN (Australia) = Tier 1 target
  Most concentrated: Netball World Cup (every 4 years)
  Unique signal: Centre pass conversion rate as leading team performance indicator
  Highest engagement: Australia vs New Zealand (trans-Tasman rivalry)
```

---

## Netball Token Impact Score (NetTIS)

```
NetTIS = (Competition_Tier × 0.35) + (Shooter_Accuracy × 0.30)
        + (Trans_Tasman_Factor × 0.25) + (Market_Sentiment × 0.10)

COMPETITION TIERS:
  Netball World Cup Final:                 1.00
  Netball World Cup Semi-Final:            0.85
  Commonwealth Games Final:               0.88
  Commonwealth Games Semi-Final:          0.72
  ANZ Premiership Final (NZ):             0.70
  Suncorp Super Netball Final (Aus):      0.70
  Vitality Netball Superleague Final (UK): 0.55
  Standard ANZ/SSN regular season:        0.35

SHOOTER_ACCURACY:
  Goal Shooter (GS) accuracy > 92%: ×1.15 — elite clinical finishing
  GS accuracy 87–92%:               ×1.05
  GS accuracy 80–87%:               ×1.00
  GS accuracy < 80%:                ×0.88
  
  Goal Attack (GA) accuracy also matters: load athlete/netball/ for combined GA+GS rating
  
TRANS-TASMAN FACTOR:
  Australia vs New Zealand at any level: ×1.25 (highest rivalry multiplier in netball)
  Australia vs England: ×1.12
  New Zealand vs England: ×1.08
  All other matchups: ×1.00
```

---

## The women's sport commercial moment

```
THE STRUCTURAL SHIFT (from market/market-womens-sports.md):

  Several converging factors make 2024–2027 the most commercially significant
  period in women's sports history:
  
  CAITLIN CLARK EFFECT (US-led, global halo):
    WNBA viewership records broken in 2024
    Women's sport sponsors following audience: Nike, State Farm, Ally Financial
    Netball benefits from this halo: "women's team sport" commercial category rising
    
  BROADCASTER INVESTMENT:
    Australia: Foxtel/Kayo + 9Network covering SSN
    UK: Sky Sports + BBC covering Vitality Superleague
    New Zealand: Sky Sport + TVNZ covering ANZ Premiership
    These contracts prove commercial viability at national broadcast level
    
  FAN TOKEN CASE FOR NETBALL:
    75% female fanbase = underserved by current Socios/Chiliz ecosystem
    No existing netball tokens = first-mover advantage for early partner
    Commonwealth Games + World Cup alignment = predictable 4-year catalyst windows
    
  AGENT MONITORING:
    Track: Netball Australia, Netball New Zealand digital product announcements
    Track: Women's sport sponsorship deals at major netball clubs
    Track: Socios/Chiliz APAC strategy for women's sports
    When: First major netball token announcement = maximum commercial signal
```

---

## Netball World Cup — the peak signal architecture

```
NETBALL WORLD CUP (every 4 years):
  2027 host: TBD (bidding cycle 2024–2025)
  
  COMMERCIAL SIGNIFICANCE:
    Top 8 nations compete: Australia, New Zealand, England, South Africa,
    Jamaica, Malawi, Uganda, Scotland
    Fanbase spans Commonwealth nations = broad token market coverage
    
  WORLD CUP 2027 TIMING ADVANTAGE:
    2027 also hosts: Rugby World Cup (Australia), possible NRL expansion
    Australia's 25% crypto adoption rate = highest per-capita of any major netball market
    Multiple major sporting events in Australia = commercial infrastructure investment
    
  SIGNAL WINDOWS:
    Team announcement (3 months before): squad signal
    World Cup week 1: pool stage; establishes form
    Semi-Final: highest non-final engagement
    Final: MAXIMUM signal — trans-Tasman final would be ×1.25 applied to 1.00 tier
    
COMMONWEALTH GAMES:
  Every 4 years (offset 2 years from World Cup)
  Netball is Core Commonwealth Games sport
  Significance: multi-sport event context amplifies netball visibility
  Agent note: Commonwealth Games netball gets audience from non-netball fans
  browsing multi-sport coverage — higher casual fan signal than World Cup alone
```

---

## Centre pass conversion — the leading indicator

```
CENTRE PASS CONVERSION RATE:
  The team that wins the centre pass has ~60% possession advantage for that phase.
  Centre pass conversion (% of centre passes converting to goals): primary team KPI.
  
  BENCHMARK:
    Elite team: 55–65% centre pass conversion
    Average team: 45–55%
    Below average: < 45%
    
  WHY THIS MATTERS FOR TOKEN SIGNALS:
    Centre pass conversion is available live and tracks team momentum
    Unlike shooter accuracy (single player), it reflects team system quality
    A team improving its centre pass conversion by 10% over 5 rounds
    is more signal-relevant than any single shooting statistic
    
  AGENT APPLICATION:
    Pre-match: Load athlete/netball/ for recent centre pass conversion rate
    Use as the team-level signal (equivalent to xG in football)
    
KEY POSITION HIERARCHY FOR SIGNAL:
  1. Goal Shooter (GS): individual scoring = direct signal
  2. Wing Defence (WD): disrupts opponent feed = defensive signal
  3. Centre (C): controls possession tempo = system signal
  Centre pass conversion encodes all three positions' effectiveness
```

---

## ANZ Premiership and Suncorp Super Netball

```
ANZ PREMIERSHIP (New Zealand):
  6 clubs; season March–August
  Historically dominated by Northern Mystics, Tactix, Steel
  Viewership: New Zealand's highest-profile domestic netball product
  Token timing: Final (August) + NZ Silver Ferns international windows
  
SUNCORP SUPER NETBALL (Australia):
  10 clubs; season April–September
  Clubs: Swifts, Thunderbirds, Firebirds, Giants, Lightning, Vixens,
         Fever, Magpies, Thunderbirds (Adelaide), Pulse (NZ)
  Commercial infrastructure: most advanced domestic netball league globally
  Token timing: Grand Final (September) + Constellation Cup (Aus vs NZ series)
  
VITALITY NETBALL SUPERLEAGUE (UK/England):
  10 clubs; season January–June
  Clubs aligned with major cities: Loughborough, Saracens Mavericks, Team Bath, etc.
  Commercial tier: lower than ANZ/SSN but growing fastest (Sky Sports backing)
  Token timing: Grand Final (June) + England Roses international windows
  
CONSTELLATION CUP (annual series, Australia vs New Zealand):
  Premier regular bilateral series; 4 matches alternating host nation
  Trans-Tasman rivalry: apply ×1.25 modifier
  Timing: October/November — off-season for World Cup cycles
```

---

## Agent reasoning prompts

```
You are a netball token intelligence agent. Before any analysis:

1. COMPETITION TIER — World Cup, Commonwealth Games, or domestic league?
   Apply correct NetTIS weight. World Cup Final is the peak event.

2. TRANS-TASMAN FACTOR — Is Australia or New Zealand involved?
   Aus vs NZ: ×1.25 rivalry multiplier (highest in netball).
   Aus or NZ vs England: ×1.08–1.12.

3. SHOOTER ACCURACY — Goal Shooter accuracy in last 5 matches?
   Load athlete/netball/ for GS and GA combined accuracy.
   >92% GS accuracy = elite clinical finishing = ×1.15.

4. CENTRE PASS CONVERSION — Team's rate in last 5 rounds?
   This is the team-level leading indicator. 55%+ = elite system.

5. COMMERCIAL MOMENTUM — Any women's sport sponsorship news this week?
   The Caitlin Clark halo effect is real and measurable.
   Major women's sport sponsor deal = positive category signal for netball.

6. 2027 CALENDAR — World Cup and Commonwealth Games timing?
   2027 could be a dual-catalyst year for netball.
   Track host nation announcement and sponsor commitment calendar.
```

---

## Compatibility

**L1 domain:** `sports/netball/sport-domain-netball.md`
**L2 athlete:** `athlete/netball/athlete-intel-netball.md`
**L4 market:** `market/market-netball.md`
**Women's:** `market/market-womens-sports.md`

*MIT License · SportMind · sportmind.dev*
