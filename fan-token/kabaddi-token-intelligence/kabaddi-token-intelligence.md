# Kabaddi (PKL) — Token Intelligence

Bridge skill connecting Pro Kabaddi League events to fan token and prediction market
signals. Kabaddi is the youngest demographic sport in the library (average fan age
well below any other), sits at the intersection of India's explosive mobile-first
sports consumption, and has the most star-player-dependent signal model of any
team sport — a single raider's form can reverse an entire match's trajectory.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — near-term high credibility
  No active Socios tokens at time of writing
  Pro Kabaddi League: Reliance Industries / JioCinema infrastructure ready
  350–400M viewers per season — among the top 3 Indian sports leagues
  Dream11 daily fantasy: 200M+ users, kabaddi is top-3 sport on platform
  Youngest fanbase: average age well below IPL cricket or ISL football

SIGNAL CHARACTERISTICS:
  Most predictive: star raider success rate (>60% = carry potential)
  Most volatile: PKL Finals (December/January)
  Unique signal: All Out event — complete squad elimination creates momentum reset
  Commercial catalyst: JioCinema streaming deal = Reliance digital ecosystem gateway
```

---

## PKL Token Impact Score (PKLTIS)

```
PKLTIS = (Match_Importance × 0.35) + (Raider_Form × 0.35)
        + (Home_Advantage × 0.20) + (Market_Sentiment × 0.10)

MATCH IMPORTANCE:
  PKL Final:                      1.00
  PKL Semi-Final:                 0.85
  PKL Eliminator:                 0.72
  Patna Pirates vs U Mumba:       0.65  (historic rivalry — highest regular match signal)
  Jaipur Pink Panthers vs Bengaluru: 0.60
  Standard PKL match:             0.35
  
RAIDER FORM:
  Raid success rate > 60% (last 5 matches): CARRY POTENTIAL — ×1.25
  Raid success rate 50–60%:                 HOT — ×1.12
  Raid success rate 40–50%:                 AVERAGE — ×1.00
  Raid success rate < 40%:                  COLD — ×0.88
  Star raider ABSENT:                       FLOOR modifier ×0.78
  Both star raiders absent (both teams):    Signal quality DOWN — apply ×0.85 overall
  
HOME_ADVANTAGE: PKL home advantage is among strongest in any league in library
  Home team: ×1.08
  Away team (travelling state): ×0.95
  Neutral venue (finals in major city): ×1.00
```

---

## The All Out event — the defining kabaddi signal

```
WHAT AN ALL OUT IS:
  When the defending team loses all 7 active players, the attacking team scores
  2 bonus points and the eliminated team returns at full strength.
  
  All Out is structurally unlike anything in any other sport in the library:
    - It resets the on-court balance instantly
    - It creates a momentum swing that affects the next 5–8 raids
    - It is partially predictable from defensive formation quality
    
ALL OUT SIGNAL IMPACT:
  Team concedes All Out: momentum reversal; short-term scoring surge for attacker
  Team achieves All Out: +2 bonus points + momentum multiplier for next possession
  
  PRE-MATCH DETECTION:
    Which team has weaker defensive corner (the position that triggers most All Outs)?
    Load athlete/kabaddi/ for corner defender rating
    Corner defender below average + strong raider opponent = high All Out probability
    
  IN-MATCH SIGNAL:
    All Out occurs → recalibrate signal: the achieving team has a 65% win rate
    from the point of All Out in close matches
    
  AGENT RULE: All Out is a live signal only — pre-match analysis cannot predict
  exactly when it occurs, only the probability. Weight All Out probability
  into the defensive fragility component of PKLTIS.
```

---

## PKL calendar and commercial context

```
PKL SEASON (December–January, 22–24 weeks):
  Format: 12 franchise teams; round-robin → Play-offs → Final
  Venue: Host cities rotate (Delhi, Mumbai, Pune, Jaipur, Patna, Bengaluru, etc.)
  
  PEAK SIGNAL WINDOWS:
    Season opener (December): activation; moderate engagement
    PKL Eliminator: highest regular stakes; elimination format
    PKL Semi-Final and Final (January): peak signal
    
  RELIANCE/JIOCINEMA INFRASTRUCTURE:
    Star Sports (linear): primary broadcaster
    JioCinema (OTT): digital streaming; Reliance Jio ecosystem
    JioCinema had 40M+ concurrent viewers during some PKL seasons
    This digital infrastructure is the commercial gateway for fan tokens
    
  DREAM11 SIGNAL:
    Dream11 kabaddi contests: millions of daily entries
    Player ownership percentage in Dream11 = leading indicator of fan interest
    High ownership % + good raider form = positive token signal
    
  TOKEN LAUNCH TIMING:
    Best window: PKL Final week (January)
    Second best: Season opener (December, round 1)
    Reliance announcement timing: JioCinema partnership events
```

---

## Star raider model — the individual player primacy rule

```
KABADDI IS THE MOST INDIVIDUAL-DOMINANT TEAM SPORT IN THE LIBRARY:

  A star raider with >60% raid success rate can carry a below-average team
  to within range of any opponent. No other team sport has this degree of
  individual player dependency in the signal model.
  
  TOP RAIDER TIER (historical reference):
    These players generate ATM-equivalent signals (see fantoken.football-bridge) for PKL:
    - Raider with 100+ raid points per season: max ATM equivalent
    - Multi-season performer with >55% success rate: high ATM equivalent
    
  RAIDER AVAILABILITY KNOCKOUT:
    If a star raider (>55% season average) is ruled out:
      Apply floor modifier ×0.78 (stronger than football's GK absence rule)
      The signal quality drops because kabaddi has fewer substitution options
      than any other sport in the library
      
  TACKLE SPECIALIST NOTE:
    While raiders drive the signal, elite tacklers (corner + cover positions)
    prevent All Out and stabilise extended lead protection.
    Load athlete/kabaddi/ for tackle specialist rating alongside raider rating.
```

---

## India market commercial context

```
WHY KABADDI HAS UNIQUE TOKEN TIMING:

  The IPL token gap (VDA framework — see fan-token/cricket-token-intelligence/)
  means cricket tokens are NOT currently available for the world's largest cricket market.
  
  PKL fills that gap: it is India-native, has comparable digital infrastructure,
  and the regulatory environment for a sports token that is NOT associated with
  cricket (and therefore BCCI) may move faster.
  
  If India's VDA framework clarifies for sports tokens:
    PKL tokens could launch BEFORE IPL tokens (no BCCI approval required)
    Reliance/JioCinema commercial ecosystem ready immediately
    Dream11 audience = existing digital sports consumer base
    
  AGENT MONITORING:
    Track Finance Ministry / SEBI VDA announcements
    Track JioCinema digital product partnership announcements
    PKL token launch would be the first India-native major sports token
    — treat any announcement as a maximum signal event
```

---

## Agent reasoning prompts

```
You are a PKL kabaddi token intelligence agent. Before any analysis:

1. STAR RAIDER STATUS — Raid success rate for the last 5 matches?
   This is the most important single input in kabaddi analysis.
   >60% = CARRY; <40% = avoid; absent = ×0.78 floor modifier.

2. ALL OUT PROBABILITY — Corner defender quality vs opposing raider?
   Load athlete/kabaddi/ for corner defender rating.
   Weak corner + elite raider = high All Out probability = signal uncertainty.

3. HOME ADVANTAGE — Who is the home team?
   PKL home advantage is structurally strong. Always apply.

4. SERIES PHASE — Playoffs vs regular season?
   Apply correct PKLTIS weight. Finals = maximum signal.

5. DREAM11 OWNERSHIP — What is the top raider's ownership % on Dream11?
   High ownership + good form = engagement signal confirmation.
   This is the closest PKL has to on-chain holder activity data.

6. INDIA VDA MONITORING — Any regulatory announcements this week?
   PKL token launch depends on India VDA framework.
   New announcement = maximum signal event regardless of PKL match result.
```

---

## Compatibility

**L1 domain:** `sports/kabaddi/sport-domain-kabaddi.md`
**L2 athlete:** `athlete/kabaddi/athlete-intel-kabaddi.md`
**L4 market:** `market/market-kabaddi.md`
**India regulatory:** `fan-token/cricket-token-intelligence/` (VDA context)

*MIT License · SportMind · sportmind.dev*
