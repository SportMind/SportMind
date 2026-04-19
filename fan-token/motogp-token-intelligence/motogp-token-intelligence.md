# MotoGP — Token Intelligence

Bridge skill connecting MotoGP events to fan token and prediction market signals.
MotoGP's token model is structurally distinct from every other motorsport in the library:
rider-centric rather than constructor-centric, governed by a single commercial entity
(Dorna Sports), and with its strongest markets in Spain, Italy, and Southeast Asia —
three of the highest crypto-adoption regions in the world.

---

## At a glance

```
TOKEN ECOSYSTEM STATUS: Tier 2 — high credibility, near-term
  No active fan tokens at time of writing
  Dorna Sports: centralised commercial authority (one deal covers full championship)
  Rider-centric model: Márquez, Bagnaia, Binder — individual rider tokens viable
  Southeast Asia: Indonesia (80M+ fans), Thailand, Malaysia = crypto-native markets

SIGNAL CHARACTERISTICS:
  Most predictive: Hardware tier (manufacturer advantage) + circuit fit
  Most volatile: Wet race sessions (completely different hierarchy emerges)
  Most concentrated: Mugello (Italian GP), Barcelona (Spanish GP), Sepang (Malaysia)
  Unique signal: Crash probability by circuit type is quantifiable and persistent

STRUCTURE NOTE: 21 race calendar + sprint races (since 2023).
  Sprint races (Saturdays): 50% points of full race; separate signal event.
  Each race weekend has three signal moments: qualifying, sprint, grand prix.
```

---

## MotoGP Token Impact Score (MotoTIS)

```
MotoTIS = (Race_Importance × 0.30) + (Hardware_Tier × 0.35)
         + (Circuit_Fit × 0.25) + (Market_Sentiment × 0.10)

RACE IMPORTANCE:
  Season finale (Valencia, Valencia decider):    1.00
  Title decider (any round when championship decided): 0.95
  Italian GP (Mugello — cultural peak):          0.85
  Spanish GP (Barcelona/Jerez — Márquez home):  0.85
  Sepang (Malaysia) / Mandalika (Indonesia):     0.80
  Losail (Qatar, season opener):                 0.72
  Standard round:                                0.50
  Sprint Race:                                   0.40 (half-distance; separate signal)

HARDWARE TIER (most persistent signal in MotoGP):
  Tier 1 (factory works team, current champion manufacturer):  ×1.15
  Tier 2 (factory works team, second manufacturer):            ×1.05
  Tier 3 (satellite team with current-spec bike):              ×0.98
  Tier 4 (satellite team with older-spec bike):                ×0.88
  
  AGENT RULE: Hardware tier is structural — it does not change race-to-race.
  Update hardware tier at season start and after major technical regulation changes.
  Mid-season engineering developments can shift a team 0.5 tier levels.
```

---

## The Dorna commercial model — the single-deal advantage

```
WHY DORNA MATTERS FOR TOKEN PRODUCTS:

In F1: commercial rights held by Formula One Management (FOM/Liberty Media)
  Team-level tokens require individual team commercial agreements
  Multi-stakeholder complexity = slower token product development

In MotoGP: Dorna Sports holds ALL commercial rights for the championship
  One conversation with Dorna = potential coverage of all teams AND riders
  This is the single largest structural commercial advantage in motorsport
  outside of F1 for token product deployment.

DORNA DIGITAL STRATEGY:
  VideoPass: subscription streaming product — proven digital audience
  MotoGP app: 5M+ registered users
  Gaming (MotoGP official game): Milestone partnership — existing digital fans
  
  Token pathway: Dorna has all the commercial prerequisites in place.
  Monitor: Dorna Sports digital product partnership announcements.
  Any announcement about "fan engagement", "digital collectibles", or
  "blockchain" from Dorna = Tier 2→1 upgrade signal.

RIDER-CENTRIC vs CONSTRUCTOR-CENTRIC:
  F1 tokens: constructor-level (Ferrari, Alpine, Aston Martin)
  MotoGP natural model: RIDER-level (Márquez, Bagnaia, Binder)
  
  WHY: Riders switch teams frequently; team identities are weaker than in F1
  A Marc Márquez token carries more commercial weight than a Ducati token
  because Márquez is the primary fan attachment point regardless of team.
  
  If MotoGP tokens launch: expect rider tokens first, then manufacturer tokens.
```

---

## Wet race signal — the complete hierarchy reversal

```
WET RACE MODEL — the most dramatic hierarchy change in any motorsport:

In dry conditions: hardware tier dominates (×1.15 for Tier 1 factory team)
In wet conditions: riding skill + wet weather specialisation overrides hardware

WET RACE SPECIALISTS (historical):
  Marc Márquez: elite wet rider — upgrade from any hardware tier in wet
  Valentino Rossi era: wet races = 30-40% increase in upset probability

WEATHER CHECK PROTOCOL:
  1. Check circuit location and weather forecast T-24h before race
  2. Check qualifying session conditions (may differ from race day)
  3. If >60% rain probability: wet_race_probability = HIGH
     → Apply wet specialist modifier (load athlete/motogp/)
     → Reduce hardware tier modifier by 50%
     → Increase upset probability estimate by 25-30%

FLAGS:
  weather_risk: activate when >40% rain probability
  lineup_unconfirmed: applicable if wet/dry call uncertain (tyre choice signal)
  
  Tyre compound selection: Michelin supplies all teams; compound choice by rider
  Hard tyre on wet track: signal of rider confidence in conditions
  Rain tyre selection: rain expected; straightforward
  Intermediate: marginal conditions — highest variance scenario
```

---

## Southeast Asia — the core growth market

```
SOUTHEAST ASIA MARKET PROFILE:

Indonesia:
  80M+ MotoGP fans (officially reported by Dorna)
  Mandalika circuit (Lombok): opened 2022; massive local engagement
  Mobile-first market: high smartphone penetration, growing crypto adoption
  Indonesian government has expressed interest in blockchain-based fan products

Thailand:
  Chang International Circuit (Buriram): capacity 70,000+
  Strong Moto2/Moto3 Thai riders = national engagement
  Thai crypto adoption: growing; ByBit and Binance active in market

Malaysia:
  Sepang International Circuit: one of MotoGP's most attended events
  Malaysian Petronas sponsorship: deep institutional connection to MotoGP

WHY SOUTHEAST ASIA MATTERS FOR TOKEN TIMING:
  Combined population in these three markets: 500M+
  Mobile-first digital engagement: natural fit for token products
  Lower regulatory complexity than US/EU for sports tokens
  
  MONITORING RULE:
  Any MotoGP commercial partnership with Southeast Asian technology companies
  (Grab, GoTo, Tokopedia) = strong token launch catalyst signal.
```

---

## Marc Márquez — the franchise signal

```
MARC MÁRQUEZ — HIGHEST INDIVIDUAL COMMERCIAL VALUE IN MOTOGP:

Titles: 8 World Championships (6 MotoGP, 1 Moto2, 1 125cc)
Return: after arm surgery (2024+) — recovery trajectory is primary monitoring signal

TOKEN SIGNAL:
  Márquez is to MotoGP what Ronaldo is to football: the primary individual
  commercial driver. Any MotoGP token product will price Márquez's involvement
  into its commercial value.
  
  Ducati signing (2024): Márquez + Ducati Tier 1 hardware = combined peak signal
  
  ACTIVE MONITORING:
  Track: race results, injury status, championship position
  Apply: ×1.10-1.15 individual commercial multiplier for Márquez-related events
  
CAREER RISK (CRI equivalent):
  MotoGP riders face higher career-ending crash risk than any other sport in the library
  A major injury to Márquez = token commercial value impact assessment required
  Load: athlete/motogp/ — career longevity model
```

---

## Sprint race model (since 2023)

```
SPRINT RACES — NEW SIGNAL DIMENSION (2023 onwards):
  Saturday sprint: 50% of race distance; separate points scoring
  Sprint + GP = two independent signal events per race weekend

SPRINT SIGNAL WEIGHT:
  Sprint: 40% of the MLBTIS for the same round
  Sprint result correlates with GP result at ~55% — moderate predictive value
  
  AGENT RULE: Sprint race result is a fresh signal, not a leading indicator.
  A sprint win does not significantly change GP prediction.
  A crash in the sprint: check for injury → potential lineup_unconfirmed for GP.

COMBINED WEEKEND SIGNAL:
  Sprint + GP total signal weight = 1.40 × standard single race
  Calendar rounds with sprint: apply 1.40 multiplier to round importance.
```

---

## Agent reasoning prompts

```
You are a MotoGP token intelligence agent. Before any analysis:

1. HARDWARE TIER — What tier is this rider's motorcycle?
   Most persistent signal in MotoGP. Update at season start only.
   Mid-season technical bulletin: update if significant performance shift detected.

2. WEATHER CHECK — Rain probability at circuit?
   >40%: activate weather_risk flag; reduce hardware modifier by 50%
   Wet race: wet specialist advantage overrides hardware tier.

3. CIRCUIT FIT — Does this rider historically perform well here?
   Load athlete/motogp/ for circuit-specific modifier.
   Some riders are strongly circuit-specific (Márquez at COTA).

4. DORNA ANNOUNCEMENT — Any digital product news this week?
   Dorna controls all commercial rights. One announcement = full championship impact.

5. SOUTHEAST ASIA RACE — Is this Sepang, Mandalika, or Buriram?
   Apply ×1.10-1.15 regional market amplifier.
   These circuits generate outsized digital engagement relative to viewership.

6. SPRINT RACE vs GP — Which event is being analysed?
   Sprint: apply 0.40 weight. GP: apply full weight.
   Sprint crash → check injury before GP analysis.
```

---

## Compatibility

**L1 domain:** `sports/motogp/sport-domain-motogp.md`
**L2 athlete:** `athlete/motogp/athlete-intel-motogp.md`
**L4 market:** `market/market-motogp.md`
**Weather:** `core/core-weather-match-day.md`

*MIT License · SportMind · sportmind.dev*
