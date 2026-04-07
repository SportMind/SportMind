# Boxing — SportMind Domain Skill

Sport-specific intelligence layer for boxing fan tokens and prediction markets.
Covers professional boxing: heavyweight, super-middleweight, light-heavyweight, middleweight,
welterweight, lightweight, and all major world titles (IBF, WBA, WBC, WBO).

---

## Overview

Professional boxing is structurally similar to MMA for token/market intelligence purposes —
individual fighter tokens, event-concentrated price action, and fight week dynamics — but with
critical differences. Boxing has a far more fragmented title structure (four major sanctioning
bodies, each with their own champion), a longer promotional cycle, and the British market
especially follows heavyweight boxing with extraordinary intensity. A Tyson Fury or Anthony Joshua
fight is a national event in the UK, producing token/market moves comparable to major football derbies.

---

## Domain Model

### Event Calendar

Boxing has no fixed season. Events are promoted throughout the year:

| Event type | Frequency | Token impact |
|---|---|---|
| World heavyweight title fight | 3–6 per year | Highest — national event in UK, US |
| Undisputed title fight (all belts) | Rare (1–3 per year) | Exceptional — highest possible impact |
| World title fight (other divisions) | Weekly globally | Moderate — division dependent |
| British/European title (domestic) | Monthly | Low–moderate |
| Undercard bouts | Every fight night | Minimal unless fighter has large token |
| Exhibition / crossover (e.g. vs YouTubers) | Occasional | Narrative play — lower conviction |

**Rule:** Heavyweight division drives the majority of mainstream boxing token/market interest,
especially in the UK, US, and Middle East. Other divisions can produce high-impact events when
an undisputed title or a fan-favourite fighter is involved.

### Fight Night Structure (vs MMA differences)

```
Boxing fight week (differs from MFA):
  Day -7:  Fight announced / promoted — social spike
  Day -5:  Open workout / media day
  Day -2:  OFFICIAL WEIGH-IN — identical binary risk to MMA (see below)
  Day -1:  Final press conference / face-off
  Day 0:   Fight night
           → Undercard (3–6 hours before main event)
           → Main event (prime time — social peak)
  Day +1:  Result digestion, rematch talk, title implications
```

### Title Structure — Critical for Agent Reasoning

Boxing's four sanctioning bodies create a uniquely complex title landscape:

```
IBF — International Boxing Federation
WBA — World Boxing Association (Regular + Super champion tiers)
WBC — World Boxing Council
WBO — World Boxing Organisation

UNDISPUTED = holds all four belts simultaneously (extremely rare, highest value event)
UNIFIED = holds 2-3 of the four belts
LINEAR = "The Man Who Beat The Man" — informal but carries cultural weight
```

**Agent rule:** An undisputed title fight is a tier above any other. A fighter holding
all four belts has the highest token valuation floor — a loss is an existential token event.

### Result Impact Matrix

| Result | Winner token | Loser token |
|---|---|---|
| KO / TKO win | +20–50% | -20–40% |
| Split decision win | +8–20% | -8–18% |
| Unanimous decision win | +12–25% | -10–20% |
| Draw | -5–12% both | |
| No contest / DQ | -10–20% both | |
| Undisputed title won | +30–65% | -25–50% |
| Undisputed title lost | -25–50% | +30–60% |
| Heavyweight title won (major fight) | +25–55% | -20–45% |
| Weigh-in miss | -10–25% (own token) / +3–8% (opponent) | |
| Fight cancelled (injury / dispute) | -15–35% both | |
| Retirement announced | -30–70% (career end) | |

---

## Competition Reference

### Heavyweight Division (Primary — UK market)

Historically the most followed division globally. British heavyweights have dominated the past
decade (Fury, Joshua, Usyk). Key rivalries drive the largest token/market events.

Key fighters with historical token/market relevance:
- Tyson Fury (UK) — lineal champion; entertainment value drives social beyond results
- Anthony Joshua (UK) — multiple reign world champion; huge retail following
- Oleksandr Usyk (Ukraine) — unified/undisputed; technically elite
- Deontay Wilder (US) — KO power; PPV draw

### Super-Middleweight / Light-Heavyweight (Secondary)

Saul "Canelo" Álvarez fights are the second-largest events in boxing — he has the biggest
PPV fanbase globally after the heavyweight division. Any Canelo fight is a tier-1 event
regardless of division.

### Other Notable Divisions

Welterweight, Lightweight — historically rich, fighters like Crawford, Spence Jr., Haney,
Garcia create periodic major events. Divide tracking by individual fighter, not division.

### Promoters (Structural Context)

| Promoter | Key fighters | Distribution |
|---|---|---|
| Top Rank (Bob Arum) | Fury, Lopez, Lomachenko | ESPN, ESPN+ |
| Matchroom Boxing (Eddie Hearn) | Joshua, Whyte, Smith | DAZN, Sky Sports |
| Premier Boxing Champions (PBC) | Wilder, Crawford, Spence | Showtime, Amazon |
| MTK Global / BOXXER | British fighters | Sky Sports, BBC |
| Saudi / Riyadh Season | Undisputed fights | Netflix, PPV |

**Agent note:** Promoter disputes and co-promotional complications are the most common reason
major fights fall through. A confirmed fight is not guaranteed until contracts are signed.

---

## Sport-Specific Risk Variables

### Weigh-In Risk (Same as MMA — Critical)

| Weigh-in outcome | Token impact |
|---|---|
| Makes weight (within limit) | Neutral to +2% |
| Misses weight by < 1lb (fight proceeds, title implications vary) | -5–12% (token holder) |
| Misses weight by > 1lb (title voided even if fight proceeds) | -12–25% |
| Opponent misses weight | +3–8% (cannot win title if opponent misses) |
| Fight cancelled due to weight miss | -20–40% |

### Injury and Late Replacement Risk

Boxing postponements are common. Unlike MMA, boxing has no "fight week" contract deadline:

| Event | Token impact |
|---|---|
| Hand injury announcement (fight off) | -15–30% |
| Training camp injury (postponed 8+ weeks) | -10–20% |
| Same-day withdrawal (rare) | -20–40% |
| Late replacement opponent | -5–15% (reduced opponent quality = narrative deflation) |

### Judging Controversy Risk

Controversial decisions are common in boxing. A hometown judge decision against a British
or American fighter is a significant social sentiment event:

| Event | Token impact |
|---|---|
| Disputed decision (fighter won but fans disagree) | +5–12% (short term but volatile) |
| Robbery call (fighter loses, fans feel cheated) | -8–20% (loser) but +15% rematch talk |
| Immediate rematch clause triggered | +5–10% (both tokens — rematch anticipation) |

**Agent rule:** Always check if rematch clauses exist in title contracts.
A controversial loss with rematch clause is less bearish than a clean loss.

---

## Event Playbooks

### Playbook 1: World Heavyweight Title Fight
```
trigger:  World heavyweight title fight confirmed (all 4 belts or unified)
entry:    Fight week Monday — pre-announcement entry
exit:     Fight night result + 1h
filter:   Fighter holds or is challenging for 2+ belts
          No major injury reports in camp
          Weigh-in clean (post-weigh-in confirmation entry preferred)
sizing:   1.5× standard for undisputed; 1.25× for unified
note:     Wait for weigh-in confirmation if possible — removes binary
          risk. UK heavyweight fights are national events — social
          momentum is unusually strong for 5-7 days pre-fight.
```

### Playbook 2: Weigh-In Confirmation Entry
```
trigger:  Fighter makes weight cleanly at official weigh-ins
entry:    Within 30min of weigh-in confirmation
exit:     Fight result + 30min
filter:   Fighter is favourite or slight underdog (up to +150)
sizing:   1.0× — weigh-in confirmation removes binary risk entirely
note:     Same logic as MMA — this is the highest-conviction entry.
          All weight cut uncertainty is eliminated at this point.
```

### Playbook 3: Undisputed Unification Fight
```
trigger:  Fight confirmed to unify all four major belts in any division
entry:    Fight announcement (2–4 weeks out)
exit:     Fight result + 72h
filter:   Both fighters have liquid tokens on-chain
          No active injury concerns or promotional disputes
sizing:   2.0× on winner; high-stakes event justifies elevated exposure
note:     Undisputed fights are rare and historic. The build-up
          extends over weeks — social momentum sustains.
          Scale in: 40% at announcement, 40% at weigh-in, 20% fight night.
```

### Playbook 4: Rematch Narrative Accumulation
```
trigger:  Controversial split decision or disputed result creates rematch demand
entry:    Night of controversial result (loser's token)
exit:     Rematch announcement confirmed
filter:   Rematch clause exists in contract (check pre-fight)
          Social demand for rematch is strong (track mentions)
sizing:   0.7× — narrative play, not confirmed event yet
note:     Controversial losses generate rematch premium. A fighter
          who "lost" but everyone thinks should have won often sees
          token recovery +10–20% in the week after if rematch is likely.
```

### Playbook 5: Retirement Fade
```
trigger:  Fighter announces retirement or takes career-defining loss at 35+
signal:   Oracle bearish signal + social sentiment sharply negative
action:   Exit position immediately
note:     Boxing career risk is high — repeated KO losses accelerate
          retirement consideration. A fighter taking their second KO
          loss in 3 fights is a structural exit signal, not a dip to buy.
          Do not average down on repeated stoppage losses.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Social sentiment | 30% | Boxing is deeply narrative-driven — hype builds for weeks |
| Sports catalyst | 30% | Fight result is the primary price event |
| Market / whale flows | 20% | Smart money accumulates pre-major fight |
| Price trend | 15% | Form correlation exists but secondary |
| Macro | 5% | Minimal — boxing tokens are fight-event isolated |

---

## Key Commands

| Action | Skill | Command | Use case |
|---|---|---|---|
| Fighter form and recent results | athlete/boxing | `get_fighter_form_score` | Recent fight record and quality of opposition |
| Weigh-in status | athlete/boxing | `get_weigh_in_status` | Binary risk check before fight day entry |
| Physical matchup | athlete/boxing | `get_physical_matchup` | Reach, height, stance, age curve |
| Camp signals | athlete/boxing | `get_fight_camp_signals` | Injury rumours, training partner changes |
| Social momentum | signal-scores | `get_signal_scores` | Fight week hype detection |
| Whale flows | whale-intel | `get_whale_flows` | Pre-fight institutional positioning |

---

## Agent Reasoning Prompts

```
You are a boxing sports intelligence agent. Before evaluating any boxing event:

1. Division matters enormously. Heavyweight fights in the UK are national media events.
   Apply 1.5–2.0× sizing to heavyweight title fights; 0.5–1.0× to other divisions.

2. ALWAYS wait for weigh-in confirmation before full position entry.
   A missed weight cut changes the entire fight narrative.

3. Check the belt situation. Undisputed (all four belts) is a tier-1 catalyst.
   Unified (2-3 belts) is tier-2. A single belt defence is tier-3.

4. Promoter disputes are boxing's unique risk. Confirm fight is fully contracted
   before entering. Rumoured fights fall through frequently.

5. Method of victory matters — a KO win generates a larger move than a decision.
   Check fighter's KO rate and opponent's chin history.

6. Rematch clauses are a real asset. A controversial loss with a rematch clause
   in a major fight is not necessarily a structural exit signal.

7. Career stage awareness. A fighter in their mid-to-late 30s taking a KO loss
   carries retirement risk. Apply structural discount accordingly.
```

---

## Data Sources

- Fight announcements: Matchroom Boxing, Top Rank, PBC, ESPN+, Sky Sports Boxing
- Fighter records and stats: BoxRec (boxrec.com)
- Weigh-in results: ESPN MMA / Boxing, Sky Sports, iFL TV
- Social sentiment: LunarCrush + fighter social handles
- Rankings: IBF, WBA, WBC, WBO official websites

---

## Compatibility

**Pairs with athlete skill:** `athlete/boxing`

**Recommended core skills:**
- `athlete/mma` — fight camp signals are nearly identical to MMA; weigh-in logic is shared
- `signal-scores` — social component is 30% weighted for boxing
- `oracle-signals` — bearish distribution ahead of injury/withdrawal risk

*MIT License · SportMind · sportmind.dev*

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` and
`core/injury-intelligence/injury-intel-boxing.md` for full injury intelligence
specific to this sport — injury taxonomy, modifier pipeline, replacement quality
delta, return-to-play curves, and sport-specific signals.

