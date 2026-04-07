# Skill Registry — SportMind Platform

**The queryable catalogue of all SportMind skills.** Agents and developers use
the registry to discover available skills, understand their capabilities, and
select the right skill set for any use case without reading every file.

---

## Registry format

Each skill entry has a standardised metadata block:

```
SKILL_ID:        unique identifier (used in platform/api-contracts.md)
TYPE:            domain | athlete | fantoken | core | market | macro | platform
SPORT:           sport identifier or "all"
TIER:            1-4 (fan token readiness) or "all"
STATUS:          stable | beta | stub
LAYERS:          which layers this skill covers [1,2,3,4,5]
KEY_METRICS:     named metrics this skill produces
REQUIRES:        skills that should be loaded before this one
OUTPUTS:         what the skill gives an agent
CONTRACT:        platform contract identifier (from api-contracts.md)
```

---

## Layer 1 — Sport domain skills

### Stable (28 skills)

| Skill ID | Sport | Key differentiator | Contract |
|---|---|---|---|
| `domain.football` | Football / Soccer | Competition tier model; derby multiplier; NCSI | `signal.domain` |
| `domain.basketball` | Basketball | Player-centric NBA + club-centric EuroLeague | `signal.domain` |
| `domain.mma` | MMA | Weigh-in binary signal; fight card hierarchy; CRI | `signal.domain` |
| `domain.esports` | Esports | Patch/meta cycle; multi-game org architecture | `signal.domain` |
| `domain.american-football` | NFL | Weekly injury report cadence; QB criticality | `signal.domain` |
| `domain.cricket` | Cricket | Format-first; DLS; dew factor; India-Pakistan ×2 | `signal.domain` |
| `domain.formula1` | Formula 1 | Qualifying-first; regulation cycles; constructor | `signal.domain` |
| `domain.ice-hockey` | NHL | Goaltender as primary variable; GSAx; B2B | `signal.domain` |
| `domain.baseball` | MLB | Pitcher-first; Statcast; park factors; rotation | `signal.domain` |
| `domain.motogp` | MotoGP | Hardware tier; wet specialists; crash probability | `signal.domain` |
| `domain.afl` | AFL | Dual scoring; kicking accuracy; MCG context | `signal.domain` |
| `domain.handball` | Handball | GK save%; financial tier gap; EHF Final4 | `signal.domain` |
| `domain.kabaddi` | Kabaddi | Star raider model; All Out dynamics; PKL | `signal.domain` |
| `domain.nascar` | NASCAR | Track type taxonomy; Championship 4 | `signal.domain` |
| `domain.rugby` | Rugby Union | Set piece; kicker zones; Six Nations | `signal.domain` |
| `domain.rugby-league` | Rugby League | State of Origin disruption; NRL/Super League | `signal.domain` |
| `domain.tennis` | Tennis | Surface splits; H2H; Grand Slam structure | `signal.domain` |
| `domain.golf` | Golf | Strokes gained; cut line; course history | `signal.domain` |
| `domain.boxing` | Boxing | Belt fragmentation; weigh-in risk; promotional | `signal.domain` |
| `domain.cycling` | Cycling | Grand Tour fatigue curves; DNF; Classics | `signal.domain` |
| `domain.athletics` | Athletics | Olympic cycle; wind legal; record proximity | `signal.domain` |
| `domain.horse-racing` | Horse Racing | Going conditions; draw bias; trainer language | `signal.domain` |
| `domain.darts` | Darts | 9-dart signal; PDC; Ally Pally | `signal.domain` |
| `domain.snooker` | Snooker | Crucible effect; Triple Crown; 147 | `signal.domain` |
| `domain.netball` | Netball | World Cup cycle; Commonwealth Games | `signal.domain` |
| `domain.winter-sports` | Winter Sports | Olympic cycle; Crystal Globe; crash risk | `signal.domain` |
| `domain.swimming` | Swimming | Olympic peak model; world record proximity | `signal.domain` |
| `domain.rowing` | Rowing | Boat Race; Olympic; weather dominance | `signal.domain` |

### Stubs — community contributions welcome (14 skills)

`domain.badminton` `domain.volleyball` `domain.table-tennis` `domain.sailing`
`domain.triathlon` `domain.field-hockey` `domain.squash` `domain.curling`
`domain.gymnastics` `domain.weightlifting` `domain.judo` `domain.taekwondo`
`domain.fencing` `domain.swimming-open-water`

---

## Layer 2 — Athlete intelligence skills (29 skills)

| Skill ID | Sport | Primary modifier variable | Contract |
|---|---|---|---|
| `athlete.football` | Football | xG form + GK rating + lineup confirmation | `modifier.athlete` |
| `athlete.mma` | MMA | Striking/grappling + weight cut + fight camp | `modifier.athlete` |
| `athlete.esports` | Esports | Roster stability + HLTV + meta readiness | `modifier.athlete` |
| `athlete.nfl` | NFL | QB CPOE + O-line health + injury designations | `modifier.athlete` |
| `athlete.nba` | NBA | Load management + on/off splits + clutch | `modifier.athlete` |
| `athlete.nhl` | NHL | GSAx + goaltender start + special teams | `modifier.athlete` |
| `athlete.cricket` | Cricket | Batter/bowler H2H + pitch + toss | `modifier.athlete` |
| `athlete.tennis` | Tennis | Surface splits + serve metrics + H2H | `modifier.athlete` |
| `athlete.rugby` | Rugby Union | Set piece + kicker accuracy + halfback | `modifier.athlete` |
| `athlete.golf` | Golf | Strokes gained + course history + cut line | `modifier.athlete` |
| `athlete.boxing` | Boxing | Weigh-in + belt status + fight camp | `modifier.athlete` |
| `athlete.cycling` | Cycling | GC standing + DNF risk + course fit | `modifier.athlete` |
| `athlete.athletics` | Athletics | Form score + WR proximity + doping status | `modifier.athlete` |
| `athlete.horse-racing` | Horse Racing | Going preference + C&D record + jockey | `modifier.athlete` |
| `athlete.snooker` | Snooker | Crucible record + pressure stats | `modifier.athlete` |
| `athlete.darts` | Darts | 3-dart average + checkout % + Ally Pally | `modifier.athlete` |
| `athlete.baseball` | MLB | PQS (pitcher) + BQS (batter) + Statcast | `modifier.athlete` |
| `athlete.rugby-league` | Rugby League | PAS + PIS + State of Origin modifier | `modifier.athlete` |
| `athlete.formula1` | Formula 1 | Qualifying delta + wet weather rating | `modifier.athlete` |
| `athlete.afl` | AFL | Kicking accuracy + contested possession | `modifier.athlete` |
| `athlete.motogp` | MotoGP | Hardware tier + wet specialist + crash prob | `modifier.athlete` |
| `athlete.handball` | Handball | GK save rate + position-specific | `modifier.athlete` |
| `athlete.kabaddi` | Kabaddi | Raider rating + All Out dynamics | `modifier.athlete` |
| `athlete.nascar` | NASCAR | Track type specialisation | `modifier.athlete` |
| `athlete.netball` | Netball | Shooter accuracy + centre pass | `modifier.athlete` |
| `athlete.rowing` | Rowing | Split time + taper + course conditions | `modifier.athlete` |
| `athlete.swimming` | Swimming | PB proximity + taper timing | `modifier.athlete` |
| `athlete.winter-sports` | Winter Sports | Course fit + snow conditions | `modifier.athlete` |
| `athlete.meta` | All sports | Cross-sport modifier orchestrator | `modifier.athlete` |

---

## Layer 3 — Fan token intelligence skills (21 skills)

### Foundation
| Skill ID | Purpose | Contract |
|---|---|---|
| `fantoken.why` | Foundational value thesis — read first | Reference only |
| `fantoken.pulse` | On-chain baseline: HAS, TVI | `signal.full` |

### Intelligence chain
| Skill ID | Key metrics | Contract |
|---|---|---|
| `fantoken.performance-on-pitch` | PI | `intelligence.commercial` |
| `fantoken.performance-off-pitch` | DTS, TAI, PS | `intelligence.commercial` |
| `fantoken.athlete-social-lift` | AELS | `intelligence.commercial` |
| `fantoken.athlete-social-activity` | SHS, AGI | `intelligence.commercial` |
| `fantoken.transfer-signal` | APS, TSI | `intelligence.commercial` |
| `fantoken.transfer-intelligence` | TVS, DLVS | `intelligence.commercial` |
| `fantoken.brand-score` | ABS | `intelligence.commercial` |
| `fantoken.sponsorship-match` | AFS | `intelligence.commercial` |
| `fantoken.sports-brand-sponsorship` | Market rate | `intelligence.commercial` |

### Sport bridge skills (Tier 1)
| Skill ID | Sport | Key metrics | Contract |
|---|---|---|---|
| `fantoken.football-bridge` | Football | FTIS, NCSI, ATM | `signal.full` |
| `fantoken.formula1-bridge` | Formula 1 | FTIS, CTI, DTM | `signal.full` |
| `fantoken.mma-bridge` | MMA | FighterTIS, FTM, CRI | `signal.full` |
| `fantoken.esports-bridge` | Esports | OrgTIS, GRM, PRS, RSI | `signal.full` |
| `fantoken.basketball-bridge` | Basketball | NBATIS | `signal.full` |
| `fantoken.cricket-bridge` | Cricket | CricTIS | `signal.full` |

### Lifecycle and infrastructure
| Skill ID | Key concept | Contract |
|---|---|---|
| `fantoken.lifecycle` | Six-phase model; LTUI | `intelligence.lifecycle` |
| `fantoken.partnership-intel` | PHS + VSI | `intelligence.partnership` |
| `fantoken.validator-intel` | VSI; PSG dual-layer | `intelligence.validator` |
| `fantoken.defi-liquidity` | TVL; slippage; LP signals | `modifier.defi` |

---

## Layer 4 — Market intelligence (35 files)

| Skill ID | Sport | Tier | Key insight |
|---|---|---|---|
| `market.overview` | All | — | Tier system framework |
| `market.key-findings` | All | — | 12 cross-sport insights |
| `market.world-cup-2026` | Football | — | WC2026 signal calendar |
| `market.womens-sports` | All | 2→1 | Demographic advantage |
| `market.football` | Football | 1 | $50B+; 40+ tokens; WC2026 |
| `market.basketball` | Basketball | 1 | $10.5B NBA; Top Shot precedent |
| `market.mma` | MMA | 1 | UFC $1.3B; most volatile |
| `market.esports` | Esports | 1 | CS2 skin economy; publisher gate |
| `market.formula1` | F1 | 1 | Drive to Survive; constructor tokens |
| `market.cricket` | Cricket | 1/2 | IPL gap; India regulation |
| *(Tier 2–4 files)* | 28 sports | 2-4 | See market-overview.md |

---

## Layer 5 — Macro intelligence (8 files)

| Skill ID | Category | Key signal |
|---|---|---|
| `macro.overview` | All | Bifurcated model; event taxonomy |
| `macro.pandemic` | Acute | Physical ×0.30 / Digital ×1.15 |
| `macro.geopolitical` | Acute/Structural | Sanctions ×0.60 |
| `macro.crypto-cycles` | Cyclical | CHZ/BTC ~0.80; bear ×0.75 |
| `macro.broadcast` | Structural | RSN collapse; streaming shift |
| `macro.economic` | Cyclical | Recession ×0.85–0.92 |
| `macro.climate` | Structural | Outdoor sport disruption |
| `macro.governance` | Acute | Corruption/doping ×0.70 |

---

## Core skills (20 files)

| Skill ID | Purpose |
|---|---|
| `core.athlete-modifier` | The modifier pipeline (0.55–1.25) |
| `core.signal-weights` | Component weights by sport (30 sports) |
| `core.result-matrices` | Price impact by result type |
| `core.confidence-schema` | Standard output format (v1.1) |
| `core.sportmind-score` | Unified cross-sport quality metric |
| `core.calibration` | Framework for improving modifier accuracy |
| `core.officiating` | Referee/judge tendency modifiers |
| `core.weather` | Match-day condition modifiers |
| `core.congestion` | Fixture pile-up modifiers |
| `core.draft-intel` | Draft event signal framework |
| `core.narrative` | Narrative momentum modifiers |
| `core.injury-master` | Injury taxonomy and pipeline |
| `core.data-sources` | Live data source directory |
| `core.context-window` | Token budget management |
| `core.multi-agent` | Session and routing patterns |
| `core.live-signals` | Static vs live input boundary |

---

## Registry query patterns

```python
# Find all skills for a specific sport
def get_skills_for_sport(sport: str, tier: int = None) -> list:
    """Returns skill IDs covering a given sport."""
    skills = []
    skills.append(f"domain.{sport}")          # Layer 1
    skills.append(f"athlete.{sport}")         # Layer 2
    if tier == 1:
        skills.append(f"fantoken.{sport}-bridge")  # Layer 3 bridge
        skills.append("fantoken.pulse")
    skills.append(f"market.{sport}")          # Layer 4
    skills.append("macro.overview")           # Layer 5
    return [s for s in skills 
            if s in SKILL_REGISTRY]  # filter to existing

# Find all skills by type
def get_skills_by_type(skill_type: str) -> list:
    types = {
        "domain": [s for s in SKILL_REGISTRY if s.startswith("domain.")],
        "athlete": [s for s in SKILL_REGISTRY if s.startswith("athlete.")],
        "fantoken": [s for s in SKILL_REGISTRY if s.startswith("fantoken.")],
        "macro": [s for s in SKILL_REGISTRY if s.startswith("macro.")],
        "core": [s for s in SKILL_REGISTRY if s.startswith("core.")],
    }
    return types.get(skill_type, [])

# Get minimum viable skill set for use case
MINIMUM_VIABLE_SETS = {
    "domain_query":        ["domain.{sport}", "core.confidence-schema"],
    "pre_match":           ["domain.{sport}", "athlete.{sport}", 
                            "core.athlete-modifier", "core.confidence-schema"],
    "fan_token_tier1":     ["fantoken.why", "macro.overview", "market.{sport}",
                            "domain.{sport}", "athlete.{sport}", "fantoken.pulse",
                            "fantoken.{sport}-bridge", "core.athlete-modifier",
                            "core.confidence-schema"],
    "commercial_brief":    ["fantoken.why", "fantoken.pulse", 
                            "fantoken.performance-on-pitch",
                            "fantoken.athlete-social-activity",
                            "fantoken.brand-score", "fantoken.sponsorship-match",
                            "fantoken.lifecycle", "core.confidence-schema"],
    "defi_check":          ["fantoken.defi-liquidity", "fantoken.lifecycle",
                            "core.confidence-schema"],
}
```

---

## Registry metadata standard (for contributors)

When submitting a new skill, include this metadata block at the top of the file:

```yaml
---
skill_id: domain.volleyball
type: domain
sport: volleyball
tier: 3
status: stable
layers: [1]
key_metrics: []
requires: []
outputs: "Competition structure, event playbooks, signal weights, agent reasoning prompts"
contract: signal.domain
version: 1.0.0
contributor: "@github-handle"
---
```

---

*MIT License · SportMind · sportmind.dev*
