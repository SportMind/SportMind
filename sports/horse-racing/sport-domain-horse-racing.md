# Horse Racing — SportMind Domain Skill

Sport-specific intelligence for horse racing prediction markets and fan tokens.
Covers Flat racing, Jump racing (National Hunt), and the major international festivals.

---

## Overview

Horse racing is the most data-rich individual prediction sport. Unlike athlete tokens, horse racing markets focus on individual horse and jockey combinations — the two are inseparable. The UK has the most sophisticated horse racing betting suite in the world; Cheltenham Festival and Royal Ascot are cultural events that generate enormous market liquidity. Key variables include going (ground conditions), trainer form, jockey booking, and draw bias — none of which have equivalents in other sports.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| Flat turf season opens | Late Mar / Apr | Spring Classics begin (2,000 Guineas, 1,000 Guineas) |
| Royal Ascot | Jun | Premium flat meeting — international fields |
| Glorious Goodwood | Jul–Aug | Major summer flat meeting |
| St Leger / Arc de Triomphe | Sep–Oct | Autumn Classics; Arc is richest European flat race |
| Jump season peak | Oct–Apr | NH racing dominates autumn through spring |
| Cheltenham Festival | Mar (4 days) | Highest-impact jump racing event of the year |
| Grand National | Apr | Most watched UK race — global audience |
| Flat season closes | Nov | All-weather / winter programme less significant |

### Going (Ground Condition) as Signal Variable

Going is unique to horse racing — no equivalent in any other sport:

| Going | Meaning | Horses affected |
|---|---|---|
| Firm | Hard, fast ground | Favours certain horses; can cause injuries |
| Good to Firm | Ideal fast ground | Broadest range of runners |
| Good | Standard | General purpose |
| Good to Soft | Slightly cut-up | Soft ground specialists emerge |
| Soft | Holding ground | Stamina test — "mudlarks" thrive |
| Heavy | Very soft, energy-sapping | Only specialist stayers/jumpers perform |

**Agent rule:** Always check going at declaration time (Tuesday for Cheltenham). A horse with a Going Preference of "Good or Faster" is significantly disadvantaged in Heavy going.

### Result Impact Matrix

| Result | Token / Market impact |
|---|---|
| Cheltenham Gold Cup win | +25–50% |
| Grand National win | +20–40% |
| Champion Hurdle win | +15–30% |
| Arc de Triomphe win | +20–40% (flat) |
| Royal Ascot Group 1 win | +10–20% |
| Favourite beaten at odds-on | -10–20% |
| Training setback announced | -8–18% |
| Injury withdrawal | -15–30% |
| Horse retired | -40–70% (token collapse) |

---

## Sport-Specific Risk Variables

### Going Change Risk

Ground conditions can change dramatically overnight with rain:

| Event | Impact |
|---|---|
| Overnight rain on Firm going | Favourite on Firm = significant disadvantage shift |
| Unexpected drying in Heavy conditions | Switch in going preference hierarchy |
| Watered ground (artificial) | Course management can stabilise conditions |

### Draw Bias (Flat Racing)

Starting stall position (draw) creates structural advantage/disadvantage at specific courses:

| Venue / condition | Draw bias |
|---|---|
| Chester (tight oval) | Low draws heavily favoured — high draws nearly unwinnable |
| Ascot (straight 5f) | High draws (stands side) historically favoured |
| Newmarket (straight) | Variable — check recent going side |
| York | Low draws favoured in sprints |

**Agent rule:** At Chester especially, a horse drawn high in a sprint is a structural disadvantage regardless of form.

### Ante-Post Risk (Betting Before Declarations)

Ante-post markets (predicting weeks ahead) carry non-runner risk:

| Risk | Impact |
|---|---|
| Horse declared non-runner (injury) | Full loss of ante-post position if no Rule 4 |
| Horse switched to different race | Position becomes void |
| Going changes unfavourably | Horse scratched — ante-post loses |

---

## Event Playbooks

### Playbook 1: Cheltenham Festival Grade 1
```
trigger:  Cheltenham Festival begins (Tuesday of Festival week)
entry:    Morning of race day (after going report)
exit:     Race result
filter:   Horse has course and distance winners (C&D) on similar going
          Trainer in form at Festival (check trainer statistics)
          Jockey booking confirmed (leading jockey retained)
sizing:   1.0× per race; 1.5× for Champion Hurdle / Gold Cup
note:     Cheltenham is the pinnacle of jump racing. Market confidence
          is highest here — ante-post markets start months before.
          Check going on Tuesday morning — can shift overnight.
```

### Playbook 2: Grand National — Specialised Approach
```
trigger:  Grand National week (Aintree, early April)
entry:    Morning of National (Saturday) after going confirmed
exit:     Race result
filter:   Horse with National course experience (top-weight horses rarely win)
          Going preference matches declared going
          Age profile: 9–11 years old most successful historically
sizing:   0.5× — highest variance race in the calendar (40 runners)
note:     National is the most unpredictable race in the world.
          Reduce position size accordingly. Focus on proven course
          performers and avoid horses making their National debut.
```

### Playbook 3: Group 1 Flat Classic
```
trigger:  Classic race week (Guineas, Derby, Oaks, St Leger, Arc)
entry:    Monday–Tuesday of Classic week
exit:     Race result + 1h
filter:   Horse is unbeaten at the trip or has won at Group 1 level
          Jockey retains ride (no last-minute jockey change)
sizing:   1.25× for Arc de Triomphe (richest, most international)
note:     Jockey changes in the week before a Classic are a significant
          bearish signal — check daily until declarations close.
```

### Playbook 4: Trainer Form Catalyst
```
trigger:  Trainer on exceptional form at festival (10%+ strike rate above normal)
entry:    From Day 2 of festival onwards
exit:     End of festival
filter:   Trainer has 3+ winners already at the meeting
sizing:   0.7× — trainer form indicator, not individual horse signal
note:     Some trainers "train for the festival" — their horses peak
          specifically at Cheltenham. This is a real and recurring signal.
```

### Playbook 5: Non-Runner / Injury Exit
```
trigger:  Horse declared non-runner or injury announced
action:   EXIT immediately if holding ante-post position
note:     No equivalent of "playing through injury" in horse racing.
          A non-runner is a full stop. Exit immediately.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 40% | Race result is everything |
| Market / whale flows | 25% | Horse racing has the most sophisticated betting market |
| Social sentiment | 15% | Grand National and Cheltenham have huge public interest |
| Price trend | 15% | Course form is highly predictive |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
You are a horse racing intelligence agent. Before evaluating any race:

1. Going is the single most important variable after the horse's ability.
   Always check going at declaration time — going changes can make or break a favourite.

2. Course and distance winners (C&D) are the most predictive past performance filter.
   A horse that has won at the course and distance in similar conditions is the primary signal.

3. Draw bias is structural at certain courses. At Chester especially, a high draw in a sprint
   is a near-disqualifying factor — the track geometry makes it nearly impossible to overcome.

4. Trainer form at festivals is a real and trackable signal.
   Some trainers "train for Cheltenham" — their horses peak specifically there.

5. Non-runner = full exit. Horse racing has no equivalent of a player coming on injured.
   A withdrawn horse is a complete position close, no exceptions.

6. Grand National requires maximum variance discount. 40 runners over unique fences —
   reduce position size to 0.5× maximum regardless of favourite status.
```

---

## Data Sources

- Race schedules and results: Racing Post (racingpost.com)
- Going reports: Official course going reports (British Horseracing Authority)
- Form and statistics: Racing Post, Timeform
- Trainer/jockey statistics: Racing Post trainer/jockey profiles

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/horse-racing/sport-domain-horse-racing.md` | Every analysis |
| Athlete modifier | `athlete/horse-racing/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-horse-racing.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/horse-racing`
**Recommended:** `signal-scores`, `oracle-signals`, `athlete/meta`

*MIT License · SportMind · sportmind.dev*

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-horse-racing.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

