# Context Window Management — SportMind

SportMind contains 185+ files totalling ~750KB of structured intelligence.
No LLM context window can load everything simultaneously. This guide tells agents
and developers exactly what to load, when, and in what order — for every use case.

---

## The core problem

A fully loaded SportMind context (all five layers for a single sport + all core files)
requires approximately 40,000–80,000 tokens depending on the sport. Modern LLM context
windows support this, but loading everything for every query is:

- **Expensive** — unnecessary API cost for simple queries
- **Slow** — time-to-first-token increases with context size
- **Dilutive** — irrelevant context reduces the signal quality of relevant context
- **Fragile** — approaching context limits causes truncation of earlier context

The solution is **progressive loading** — load the minimum necessary context for
the specific query, then load additional layers only when their signal is needed.

---

## Token budget estimates per file category

```
APPROXIMATE TOKEN COUNTS (for planning):

Layer 5 — Macro files:
  macro-overview.md:              ~2,500 tokens
  Each macro event file:          ~2,000–3,000 tokens
  Full macro layer (8 files):     ~18,000 tokens

Layer 4 — Market files:
  Each market-{sport}.md:         ~1,500–2,500 tokens
  market-overview.md:             ~2,000 tokens
  market-key-findings.md:         ~2,500 tokens

Layer 1 — Sport domain files:
  Tier 1 sport skills (football, cricket, etc.): ~4,000–8,000 tokens
  Standard sport skills: ~2,500–4,000 tokens

Layer 2 — Athlete files:
  Most athlete skills:            ~2,000–4,000 tokens
  Injury intelligence (full):     ~8,000 tokens (7 files)

Layer 3 — Fan token files:
  fan-token-why.md:               ~3,500 tokens
  fan-token-pulse:                ~2,500 tokens
  Each bridge skill:              ~2,500–4,000 tokens
  defi-liquidity-intelligence:    ~4,500 tokens

Core files:
  core-athlete-modifier-system:   ~1,800 tokens
  confidence-output-schema:       ~2,500 tokens
  core-signal-weights-by-sport:   ~2,000 tokens
  glossary.md:                    ~4,000 tokens

ROOT FILES:
  sportmind-overview.md:          ~8,000 tokens  ← reference doc; rarely load in full
  README.md:                      ~1,200 tokens  ← onboarding only; load once
```

---

## Minimum viable loading sets by use case

### Use case A — Quick sport domain question

```
Estimated tokens: 4,000–8,000
Files to load:
  1. sports/{sport}/sport-domain-{sport}.md  ← the only required file

Skip:
  All layers — not needed for a simple domain question
  
Example query: "How does the Duckworth-Lewis system work in cricket?"
Load: sports/cricket/sport-domain-cricket.md only
```

### Use case B — Pre-match prediction (no active tokens)

```
Estimated tokens: 10,000–18,000
Files to load:
  1. sports/{sport}/sport-domain-{sport}.md
  2. athlete/{sport}/athlete-intel-{sport}.md
  3. core/core-athlete-modifier-system.md
  4. core/confidence-output-schema.md        ← for structured output

Conditional loads (add only if relevant):
  + macro/macro-overview.md                  IF recent macro event
  + core/core-fixture-congestion.md          IF 3+ matches in 10 days
  + core/core-weather-match-day.md           IF outdoor sport + weather concern
  + core/injury-intelligence/{sport}.md      IF injury doubt on key player

Skip:
  market/{sport} — not needed unless token decisions involved
  fan-token/* — no active tokens; not applicable
```

### Use case C — Fan token signal (Tier 1 sport, full intelligence)

```
Estimated tokens: 25,000–45,000
Files to load (in order):
  1. fan-token/fan-token-why.md              ONCE (foundation; skip if already loaded)
  2. macro/macro-overview.md                 CHECK macro state first
  3. market/{sport}/market-{sport}.md        Commercial tier confirmation
  4. sports/{sport}/sport-domain-{sport}.md
  5. athlete/{sport}/athlete-intel-{sport}.md
  6. fan-token/fan-token-pulse/              On-chain baseline
  7. fan-token/{sport}-token-intelligence/   Sport bridge skill
  8. core/core-athlete-modifier-system.md
  9. core/confidence-output-schema.md

Conditional loads:
  + fan-token/defi-liquidity-intelligence/   IF TVL check needed
  + fan-token/fan-token-lifecycle/           IF token lifecycle assessment needed
  + fan-token/blockchain-validator-intel/    IF validator club (PSG etc.)
  + core/core-narrative-momentum.md         IF high-narrative fixture (rivalry, final)

Skip:
  macro event files beyond overview          UNLESS active event identified
  All other market files                     Only load the relevant sport
  Glossary                                   Developer reference; not needed in agent
```

### Use case D — Commercial intelligence brief (clubs/agents/brands)

```
Estimated tokens: 30,000–50,000
Files to load:
  1. fan-token/fan-token-why.md
  2. fan-token/fan-token-pulse/
  3. fan-token/performance-on-pitch/
  4. fan-token/athlete-social-activity/
  5. fan-token/athlete-social-lift/
  6. fan-token/brand-score/
  7. fan-token/sponsorship-match/
  8. fan-token/sports-brand-sponsorship/
  9. fan-token/fan-token-lifecycle/          Partnership phase assessment
  10. fan-token/fan-token-partnership-intel/ PHS calculation
  11. core/confidence-output-schema.md

Skip:
  sport domain skills — not needed for commercial analysis
  athlete modifier files — not needed for brand/commercial work
  macro files — not needed unless macro override active
```

### Use case E — DeFi/liquidity check only

```
Estimated tokens: 6,000–10,000
Files to load:
  1. fan-token/defi-liquidity-intelligence/
  2. fan-token/fan-token-lifecycle/          Phase identification only
  3. core/confidence-output-schema.md

Skip: everything else — pure execution check
```

---

## Progressive loading strategy

For production agents handling multiple queries across a session:

```
PROGRESSIVE LOADING PATTERN:

Session start:
  → Load: README.md + fan-token-why.md (foundation; low token cost; load once)
  → Load: macro/macro-overview.md (macro state check; stays relevant all session)
  → Cache: Do not reload these within a session

Per-query loading:
  → Identify: sport + use case + token tier
  → Load: minimum viable set for this specific query (see above)
  → Extend: add conditional files only when their signal is needed

Context pressure management:
  → When approaching 75% of context limit:
    1. Summarise and compress already-processed context
    2. Unload files not relevant to current query thread
    3. Priority load order if forced to choose: modifier system > domain skill >
       athlete skill > market context > macro event files > glossary

NEVER load at session start:
  → sportmind-overview.md in full (8,000 tokens; reference doc only)
  → glossary.md in full (4,000 tokens; query on demand)
  → All macro event files (load only what's currently active)
  → All market files (load only the relevant sport)
```

---

## File priority ranking — when forced to choose

If context window pressure forces loading fewer files, use this priority order:

```
ALWAYS LOAD (foundation):
  1. core/core-athlete-modifier-system.md     How to compute the core modifier
  2. core/confidence-output-schema.md         How to structure the output
  3. sports/{sport}/sport-domain-{sport}.md   How this sport works

LOAD IF AVAILABLE:
  4. athlete/{sport}/athlete-intel-{sport}.md Who is playing and how
  5. core/core-signal-weights-by-sport.md     How to weight signal components
  6. macro/macro-overview.md                  Macro override check

LOAD IF USE CASE REQUIRES:
  7. fan-token/fan-token-pulse/               On-chain baseline (only Tier 1)
  8. fan-token/{sport}-token-intelligence/    Sport bridge (only Tier 1)
  9. market/{sport}/market-{sport}.md         Commercial context
  10. core/core-fixture-congestion.md         Only if congestion flag set

LOAD LAST (lowest priority):
  11. Injury intelligence files               Only if specific injury concern
  12. Narrative momentum                      Only for high-narrative fixtures
  13. Officiating intelligence                Only for major matches
  14. Weather intelligence                    Only for outdoor sports with weather
```

---

## Token-saving techniques

### Technique 1: Numbers over prose

When loading SportMind context into a limited window, extract and pass numbers rather
than prose explanations:

```
INSTEAD OF loading the full signal weights file (2,000 tokens):
  Pass: "Football weights: catalyst 30%, whale 25%, social 20%, price 15%, macro 10%"
  Saves: ~1,900 tokens with full signal information preserved

INSTEAD OF loading the full modifier system (1,800 tokens):
  Pass: "Modifier range: key player out=×0.70, doubt=×0.85, confirmed+hot form=×1.15"
  Saves: ~1,700 tokens with core modifier logic preserved

INSTEAD OF loading a full market file (2,000 tokens):
  Pass: "Football: Tier 1. 40+ active tokens. WC2026 catalyst. CHZ correlation 0.80."
  Saves: ~1,900 tokens with tier and key context preserved
```

### Technique 2: Conditional loading with query routing

```python
# Route to minimum viable skill set based on query classification
def get_skill_set(query: str, sport: str, has_token: bool) -> list[str]:
    base = [f"sports/{sport}/sport-domain-{sport}.md",
            "core/core-athlete-modifier-system.md",
            "core/confidence-output-schema.md"]
    
    if "injury" in query.lower():
        base.append(f"core/injury-intelligence/injury-intel-{sport}.md")
    if "weather" in query.lower() or sport in OUTDOOR_SPORTS:
        base.append("core/core-weather-match-day.md")
    if has_token and sport in TIER_1_SPORTS:
        base.extend([
            "fan-token/fan-token-pulse/",
            f"fan-token/{sport}-token-intelligence/"
        ])
    
    return base
```

### Technique 3: Summary mode for reference files

For large files loaded as background context, instruct the agent to treat them as
reference (query only when needed) rather than loading into active reasoning:

```
System prompt pattern:
  "The following SportMind files are available as reference context.
   Do not process them exhaustively. Only consult the relevant section
   when a specific question requires it:
   [sportmind-overview.md — query only when asked about library structure]
   [glossary.md — query only when a term needs definition]"
```

---

## Context window budgets by model

```
MODEL              | CONTEXT  | FULL L1+L2+L3 | RECOMMENDED USE CASE
-------------------|----------|---------------|---------------------
GPT-4o (128k)      | 128,000  | YES (2 sports)| Full 5-layer; multi-query sessions
Claude 3.5 Sonnet  | 200,000  | YES (3 sports)| Full 5-layer; commercial briefs
Claude 3 Opus      | 200,000  | YES (3 sports)| Deep analysis; research agent
Gemini 1.5 Pro     | 1,000,000| YES (all)     | Full library; multi-sport simultaneously
GPT-4 Turbo        | 128,000  | YES (2 sports)| Full 5-layer for single sport
Llama 3 (70B)      | 8,000    | Minimum set   | Domain skill + modifier only
Mistral Large      | 32,000   | L1 + L2 only  | No fan token layer; prediction only
Local models       | 4,000    | Domain only   | Single sport-domain-{sport}.md
```

---

## What to do when context overflows

If a SportMind session exceeds context limits mid-conversation:

```
OVERFLOW RECOVERY PROTOCOL:

Step 1: Identify what triggered the overflow
  → Was it loading too many files? (reduce to minimum viable set)
  → Was it a long conversation history? (summarise prior turns)
  → Was it a single very large file? (use summary mode)

Step 2: Restart with compressed context
  → Summarise the prior analysis in <500 tokens
  → Keep: final modifier values, confidence tier, key flags
  → Drop: full file content that generated those values

Step 3: Continue from compressed state
  → Agent can continue reasoning from the summary
  → Re-load specific files only if a new question requires them

WHAT TO PRESERVE IN SUMMARY:
  base_score, composite_modifier, confidence_tier, recommended_action
  Active flags (injury_warning, liquidity_critical, macro_override_active)
  The single primary signal driver
  Any critical risks identified

WHAT TO DROP:
  Full file contents already processed
  Intermediate reasoning steps
  Reference content not cited in final analysis
```

---

## Compatibility

**Closely related:**
- `core/multi-agent-coordination.md` — session state and multi-agent patterns
- `core/confidence-output-schema.md` — structured output (always load)
- `agent-prompts/agent-prompts.md` — ready-to-deploy prompts with appropriate loading

*MIT License · SportMind · sportmind.dev*
