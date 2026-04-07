# Winter Sports — SportMind Domain Skill

Sport-specific intelligence for winter sports fan tokens and prediction markets.
Covers Alpine Skiing, Biathlon, Cross-Country Skiing, Ski Jumping, Snowboard,
Bobsleigh, Luge, Skeleton, Figure Skating, Speed Skating, Curling, and Ice Hockey (national).

---

## Overview

Winter sports is a collective category covering a wide range of disciplines united by the
Olympic Winter Games cycle. Unlike summer Olympics, winter sports have a smaller but intensely
loyal fan base concentrated in Northern Europe, North America, and East Asia. Fan tokens are
primarily tied to national teams (Norway, Switzerland, Austria, Germany dominate Alpine and
Nordic events) or individual star athletes. The Winter Olympics every four years is the
dominant signal event — outside that cycle, World Cup circuits provide sustained weekly signals
from November through March.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal Behaviour |
|---|---|---|
| World Cup circuit opens | Oct–Nov | Season baseline; early form signals |
| Alpine Skiing World Cup | Nov–Mar | Weekly races across Europe; Crystal Globe standings |
| Biathlon World Cup | Nov–Mar | Weekly events; hugely popular in Northern Europe |
| Ski Jumping World Cup | Nov–Mar | Four Hills Tournament (Dec-Jan) is peak |
| Cross-Country Skiing World Cup | Nov–Mar | Tour de Ski (Jan) is primary circuit event |
| Winter X Games | Jan | Freestyle / snowboard; younger audience |
| World Championships (individual disciplines) | Feb (non-Olympic years) | Tier-2 peak |
| Winter Olympic Games | Feb (every 4 years) | Tier-1 — maximum signal |
| Paralympic Winter Games | Mar (same year) | Following Olympics; growing audience |

### Event Tier System

```
Tier 1: Winter Olympic Games
Tier 2: Winter World Championships (Alpine, Biathlon, Ski Jumping, Nordic)
Tier 3: Crystal Globe / discipline season champions
         Four Hills Tournament (Ski Jumping — Dec-Jan)
         Tour de Ski (Cross-Country — Jan)
         Biathlon World Cup Final
Tier 4: Individual World Cup race wins
Tier 5: National championships, Europa Cup
```

### Discipline-Specific Token Relevance

Different winter disciplines generate different audience profiles:

| Discipline | Token relevance | Key markets |
|---|---|---|
| Alpine Skiing | HIGH — star-driven, global TV | Austria, Switzerland, Norway, France |
| Biathlon | HIGH — Nordic markets, massive fan base | Norway, Germany, France |
| Ski Jumping | MODERATE — niche but passionate | Austria, Germany, Norway, Poland |
| Cross-Country | MODERATE — Nordic specialist | Norway, Sweden, Finland |
| Figure Skating | HIGH in Asia — large East Asian fan base | Japan, South Korea, Russia |
| Speed Skating | MODERATE — Netherlands dominant | Netherlands, South Korea |
| Curling | LOW — niche but vocal | Scotland, Canada, Sweden |
| Bobsleigh / Luge | LOW — limited token ecosystem | Jamaica novelty aside |
| Snowboard | GROWING — younger audience | USA, Canada, Australia |
| Ice Hockey (national) | HIGH in Winter Olympics | Canada, USA, Russia, Finland, Sweden |

### Result Impact Matrix

| Result | Token impact |
|---|---|
| Winter Olympic gold | +25–55% |
| Winter Olympic silver/bronze | +8–18% |
| World Championship gold | +15–30% |
| Crystal Globe (season champion) | +12–25% |
| Four Hills Tournament win | +15–28% |
| Individual World Cup race win | +3–8% |
| Injury during race (DNF) | -10–25% |
| Season-ending injury | -15–30% |
| World record broken (Speed Skating, Alpine) | +15–30% |

---

## Sport-Specific Risk Variables

### Weather and Snow Conditions

Winter sports are uniquely weather-dependent — races can be cancelled, courses can change:

| Condition | Impact |
|---|---|
| Race cancelled due to weather | Neutral to -3% (uncertainty) |
| Icy course (Alpine) | Increases crash risk; variance spikes |
| Heavy snowfall (Ski Jumping) | Cancelled or fair-start protocol applied |
| Warm temperatures (spring races) | Course softening — favours technically different skiers |
| Poor visibility (Biathlon) | Shooting accuracy drops for all — equalises field |

**Agent rule:** Always check forecast for race day. Weather-cancelled race = no result signal
(not a positive or negative — event simply reschedules).

### Four-Year Olympic Cycle Compression

Winter sports athletes structure their careers around four-year cycles:

| Situation | Token impact |
|---|---|
| Star athlete peaks in Olympic year | Maximum token valuation |
| Olympic year injury (athlete misses Games) | -20–40% — four years of preparation lost |
| Athlete skips World Cups to save for Olympics | Short-term signal gap; long-term accumulation play |
| Veteran athlete announces final Olympics | Sentimental rally — often outperforms expectations |

### Alpine Skiing Crash Risk — Unique Injury Profile

Alpine skiing has one of the highest injury rates in sport. Gate crashes and downhill falls can
end seasons or careers:

| Injury event | Token impact |
|---|---|
| Fall in training (precautionary) | -5–10% |
| Race crash with season-ending injury | -15–30% |
| Knee injury (ACL) | -15–30%; 6–12 month recovery minimum |
| Career-ending crash | -40–70% |

---

## Event Playbooks

### Playbook 1: Winter Olympics Gold Run
```
trigger:  Star athlete qualifies for Olympic final / final round
entry:    Morning of event (after qualifying confirmed)
exit:     1h post-result
filter:   Athlete is defending champion or World Cup season leader
          No injury concerns from training runs
sizing:   1.5× — Olympics is tier-1 for all winter disciplines
note:     Enter after qualifying round, not pre-Games.
          Olympic downhill / Super-G: only one run — higher variance.
          Alpine combined (2 runs): lower variance, form more predictive.
```

### Playbook 2: Four Hills Tournament (Ski Jumping)
```
trigger:  Four Hills Tournament begins (Oberstdorf — late Dec)
entry:    After Competition 1 result (Oberstdorf)
exit:     After Competition 4 (Bischofshofen — early Jan)
filter:   Jumper leads overall standings after first 2 hills
          Wind conditions stable (no strong tailwind / headwind)
sizing:   1.0× for series leader; 0.5× pre-tournament
note:     Four Hills is the most prestigious non-Olympic ski jumping event.
          A player leading 2-0 after Garmisch is in a very strong position.
          Monitor wind gates before each competition — wind can invalidate jumps.
```

### Playbook 3: Crystal Globe Season Leader
```
trigger:  Athlete leads Crystal Globe standings by 200+ points with 5 races left
entry:    Point of statistical confirmation
exit:     Globe ceremony (season end, Mar)
filter:   No active injury concerns; remaining races suit athlete's specialty
sizing:   0.8× — gradual accumulation signal
note:     Crystal Globes are awarded for overall and discipline season champions.
          A dominant leader provides a sustained 6–8 week signal window.
```

### Playbook 4: Tour de Ski Run
```
trigger:  Cross-country Tour de Ski enters final stages (final climb)
entry:    After Stage 3 (when leaders become clear)
exit:     Final stage result
filter:   Athlete is top-3 overall with strength in final climb format
sizing:   1.0× — Nordic markets have strong social following
note:     Tour de Ski runs across New Year (Dec 28–Jan 7 approx).
          The final stage's Alpe Cermis climb is the decisive signal point.
```

### Playbook 5: Olympic Injury Fade
```
trigger:  Athlete injured in training or race during Olympic Games period
action:   EXIT immediately on any confirmed training setback during Games
note:     Four-year cycle makes Olympic-year injuries catastrophic for tokens.
          Even "minor" injuries at the Olympics should trigger a reassessment.
          Do not hold through uncertainty — exit and re-enter if cleared.
exit:    hold to event completion
filter:  standard availability and macro checks apply
sizing:  1.0× standard position
```

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Race results and championships dominate |
| Social sentiment | 20% | Olympic moments generate huge social spikes |
| Market / whale flows | 20% | Pre-Olympics accumulation is real |
| Price trend | 15% | Season form is predictive for World Cup circuits |
| Macro | 10% | Weather conditions add unique macro-like uncertainty |

---

## Agent Reasoning Prompts

```
You are a winter sports intelligence agent. Before evaluating any winter sports event:

1. Olympic cycle is everything. Winter Olympics year = maximum signal for all disciplines.
   Non-Olympic years calibrate down by 30–40% for World Championships, more for circuit events.

2. Always check weather forecast before any alpine or outdoor winter event.
   A cancelled race or icy course fundamentally changes the signal.

3. Four Hills Tournament (ski jumping) and Tour de Ski (cross-country) are the
   circuit's two signature non-championship events — treat them at tier-3, not tier-4.

4. Alpine skiing crash risk is real and frequent. Do not hold through significant
   training crashes — exit and reassess medical reports before re-entering.

5. Discipline matters enormously — Norway dominates biathlon and cross-country;
   Austria/Switzerland dominate alpine. Identify which national market drives
   the specific athlete's token before evaluating signal strength.

6. Figure skating has an unusually large East Asian audience. Japanese, Korean,
   and Chinese skaters' tokens react strongly to Asian broadcast events and social.
```

---

## Data Sources

- Race results and standings: FIS (fis-ski.com), IBU (biathlon), ISU (skating)
- World Cup circuits: Official FIS app / website
- Weather: Open-Meteo for race venue forecasts
- Social sentiment: LunarCrush + athlete social handles
- Olympics: Official IOC results

---


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/winter-sports/sport-domain-winter-sports.md` | Every analysis |
| Athlete modifier | `athlete/winter-sports/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-winter-sports.md` | Commercial decisions |

## Compatibility

**Pairs with athlete skill:** `athlete/meta` (weather overlay is critical for winter sports)
**Recommended:** `signal-scores`, `athlete/meta`
**Note:** A dedicated `athlete/winter-sports` skill is planned for v1.1

*MIT License · SportMind · sportmind.dev*
