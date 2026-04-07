# Darts — SportMind Domain Skill

Sport-specific intelligence for darts fan tokens and prediction markets.
Covers PDC (Professional Darts Corporation) — the dominant professional circuit —
including the World Championship, Premier League, World Matchplay, and Grand Slam.

---

## Overview

Professional darts (PDC) has transformed from a pub game into a major televised spectacle.
Alexandra Palace's World Championship is the definitive event — 96,000 fans over 27 days,
sold-out weeks in advance, and a social media reach rivalling mainstream sports. Individual player tokens are the relevant unit.
The sport's unique atmosphere (crowd chanting, walk-on music, 180s) creates social signals
unlike any other sport. Luke Littler's emergence has brought a new generation of global fans.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| World Championship (Ally Pally) | Dec–Jan | Highest impact — 27 nights, global TV audience |
| Premier League Darts | Feb–May | Weekly Thursday night event; 10 rounds + Play-Offs |
| UK Open | Mar | "FA Cup of Darts" — open to all PDC card holders |
| World Matchplay | Jul | Blackpool — summer major |
| World Grand Prix | Oct | Double-in, double-out format; Citywest, Dublin |
| Grand Slam of Darts | Nov | Wolves — PDC vs tour card qualifiers |
| Players Championship Finals | Nov | Season-ending ranking event |
| European Championship | Oct | European venues rotation |

### Event Tier System

```
Tier 1: World Championship (Alexandra Palace)
Tier 2: Premier League (full series), Grand Slam of Darts
Tier 3: World Matchplay, UK Open, European Championship
Tier 4: Players Championship Finals, World Grand Prix
Tier 5: Players Championships (monthly), European Tour events
```

### Result Impact Matrix

| Result | Token impact |
|---|---|
| World Championship win | +25–50% |
| World Championship final (lost) | +10–20% (run narrative) |
| World Championship early exit (pre-QF) | -8–18% |
| Premier League title win | +12–25% |
| World number 1 ranking achieved | +10–20% |
| 9-dart finish (televised) | +8–18% (extremely rare — max achievement) |
| First PDC major win | +10–22% |
| Ranking drop (out of top 32) | -8–15% |

---

## Sport-Specific Risk Variables

### Premier League Format — Weekly Narrative Arc

Premier League Darts runs weekly (Thursdays) across 16 weeks. This creates a sustained signal:

| Event | Impact |
|---|---|
| Player wins 3+ consecutive Premier League nights | +3–7% cumulative momentum |
| Player takes league leaders position | +5–10% |
| Player eliminated in Play-Off semi | -5–10% |
| Player wins Play-Off (Premier League champion) | +12–20% |

### 9-Dart Finish — Rare Catalyst

The perfect leg (nine darts to check out 501) is the rarest achievement in darts:

| Context | Impact |
|---|---|
| 9-darter at World Championship | +15–25% (highest social spike in darts) |
| 9-darter in Premier League (televised) | +8–15% |
| 9-darter in minor event | +3–8% |

**Agent rule:** 9-dart finishes generate immediate social virality regardless of match context. Monitor all PDC televised events.

### Rivalry Matches — Audience and Market Effect

Specific rivalries generate outsized market attention:

| Match | Context |
|---|---|
| Luke Littler vs any top-4 | New generation vs establishment — huge social |
| Phil Taylor legacy matches | Icons attract older audience demographic |
| Michael van Gerwen (MvG) | Dutch market + global recognition |

---

## Event Playbooks

### Playbook 1: World Championship Deep Run
```
trigger:  Player reaches World Championship quarter-final
entry:    QF confirmation evening
exit:     Tournament result
filter:   Player is top-8 seed AND has won a major in the past 2 years
sizing:   1.25× — Ally Pally run creates sustained social narrative
note:     World Championship runs over 27 nights. A player reaching
          the final is 2+ weeks of sustained positive sentiment.
          Scale in: 40% at QF, add at SF, hold through final.
```

### Playbook 2: Premier League Night Win Streak
```
trigger:  Player wins 3+ Premier League nights in succession
entry:    After 3rd consecutive night win
exit:     Premier League Play-Off result OR if player loses 2 nights
filter:   Player is in top-4 league table standings
sizing:   0.8× — momentum play across the series
note:     PL format rewards consistent performers over 16 weeks.
          A player consistently winning is building ranking and token value.
```

### Playbook 3: 9-Dart Finish Alert
```
trigger:  Player completes 9-dart finish in televised event
entry:    Within 1h of completion
exit:     +48h (media cycle)
filter:   Player has on-chain token; event is live on Sky/TNT
sizing:   0.5× — social/narrative play
note:     9-darters at Ally Pally or Premier League get international coverage.
          This is a pure social catalyst — the player may still lose the match.
```

### Playbook 4: First Major Win Breakthrough
```
trigger:  Player wins first PDC major title
entry:    Final confirmation
exit:     +72h
filter:   Player is under-25 or first-time major winner
sizing:   1.0×
note:     First major is career-defining. Luke Littler's first major
          generated sustained multi-week momentum. Check if player
          has been close before — multiple PDC finalist record.
```

### Playbook 5: Tour Card Loss Fade
```
trigger:  Player confirmed to lose PDC Tour Card (drops out of top 64)
action:   Exit position — loss of Tour Card means limited televised access
note:     Without a Tour Card, players cannot compete in major PDC events.
          Token floor collapses as competitive relevance disappears.
          This is a structural exit, not a temporary form dip.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Social sentiment | 35% | Darts is the most atmosphere-driven sport — crowd and social are key |
| Sports catalyst | 30% | Tournament results are primary |
| Market / whale flows | 15% | Pre-Worlds accumulation exists |
| Price trend | 15% | Form correlation is real |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
You are a darts sports intelligence agent. Before evaluating any darts event:

1. Social sentiment leads in darts — more than almost any other sport.
   Walk-on music, crowd chants, and 180 celebrations generate instant viral moments.
   Weight social component at 35% for darts events.

2. World Championship is the only tier-1 event. Alexandra Palace over 27 nights
   is the defining darts event — size at 1.5× maximum vs 1.0× for other events.

3. 9-dart finishes are rare but highly predictable in terms of social impact.
   Any televised 9-darter is an immediate social catalyst regardless of match result.

4. Premier League runs weekly from February to May. This creates a 16-week
   sustained signal opportunity for players in the top 8.

5. Tour Card status determines event access. A player outside the top 64
   has severely restricted access to televised PDC events.

6. Luke Littler effect — the new generation of fans is younger and more
   digitally active than traditional darts audiences. Social signals for
   young players move faster and more amplified than establishment players.
```

---

## Data Sources

- Rankings and results: PDC (pdc.tv)
- Statistics: DartsDatabase (dartsdatabase.co.uk)
- Live: Sky Sports Darts, TNT Sports
- Social: LunarCrush + player social handles

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/darts/sport-domain-darts.md` | Every analysis |
| Athlete modifier | `athlete/darts/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-darts.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/darts`
**Recommended:** `signal-scores` (social component 35%), `oracle-signals`

*MIT License · SportMind · sportmind.dev*
