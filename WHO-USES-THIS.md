# Who Uses SportMind — Find Your Path

**Read this before anything else. Under 5 minutes to your starting point.**

SportMind is a large library. This document maps each type of person who
uses it to exactly the files they need — nothing more. Skip everything else
until you are confident in your starting point.

---

## Who are you?

---

### 🏗 I am a developer building a fan token application

**Your goal:** Connect SportMind intelligence to an application that reads
fan token signals and does something useful with them (dashboard, alerts,
trading UI, token-gated content, governance brief).

**Start here — in this order:**

1. **`examples/starter-pack/README.md`** — Pick your complexity level (01 through 06).
   Start with 01-simple-signal.py. You will have a working signal in under 10 minutes.

2. **`platform/skill-bundles.md`** — Find the named bundle that matches your use case.
   `ftier1-football` for football tokens, `governance-brief` for governance, etc.
   This tells you exactly which skills to load and in what order.

3. **`platform/data-connector-templates.md`** — Copy-paste code for the three data
   sources you need most: lineup data, fan token market data, and macro state.

4. **`platform/chiliz-agent-kit-integration.md`** — If you need to execute on-chain
   (trades, governance votes, staking), this is the execution layer connection.

**You do not need to read:** WHO-WE-ARE.md, sport domain skills, or calibration data.
Those are background context. You need working code first.

---

### 🤖 I am building an autonomous AI agent

**Your goal:** An agent that runs continuously, monitors signals, escalates to humans
appropriately, and improves over time.

**Start here — in this order:**

1. **`core/sportmind-purpose-and-context.md`** — 600 tokens. Load this into your agent's
   system prompt first. It gives the agent everything it needs to operate correctly.

2. **`core/autonomous-agent-framework.md`** — The full lifecycle model, safety principles,
   and decision matrix. Your agent architecture should implement this.

3. **`examples/agentic-workflows/README.md`** — Seven workflow patterns. Pick the one
   that matches your use case (portfolio monitor, pre-match chain, tournament tracker, etc.)

4. **`core/agent-goal-framework.md`** — If your agent needs to adapt its plan over time
   rather than execute a fixed schedule, read this for the goal-directed extension.

5. **`platform/skill-bundles.md`** — What to load at agent initialisation.

**You do not need to read:** Individual sport domain files at first — use bundles.
Individual calibration records — those are for modifier improvement, not deployment.

---

### 📊 I am a sports analyst or club commercial professional

**Your goal:** Understand what SportMind produces and use the intelligence outputs
to inform decisions about athletes, tokens, transfers, or commercial partnerships.

**Start here — in this order:**

1. **`WHO-WE-ARE.md`** — What SportMind is and what it produces. The commercial context.

2. **`agent-prompts/agent-prompts.md`** — Prompts 11, 12, and 13 are specifically for
   club commercial directors and sports agents. These are ready to copy into Claude or
   any LLM and get structured commercial intelligence immediately.

3. **`examples/applications/`** — Browse the 11 application blueprints. Find the one
   that matches your use case (talent scouting, athlete commercial, governance brief, etc.)

4. **`core/sportmind-purpose-and-context.md`** — Load this into any LLM conversation
   to give it the complete SportMind context in one 600-token block.

**You probably do not need:** The platform layer, scripts, or CI/CD documentation.
Those are developer infrastructure. You need intelligence frameworks and prompts.

---

### 🔬 I am a researcher or want to understand the methodology

**Your goal:** Understand how SportMind works, how the modifiers are calibrated,
what the evidence base looks like, and whether the library's claims are credible.

**Start here — in this order:**

1. **`core/calibration-framework.md`** — The methodology for how modifiers improve over time.

2. **`core/modifier-recalibration-v5.md`** — The most recent recalibration. Shows what
   was tested, what was confirmed, what was updated, and what was wrong and why.

3. **`community/calibration-data/CONTRIBUTING.md`** — The evidence methodology:
   how outcome records are structured, what counts as valid evidence, what does not.

4. **`core/reasoning-patterns.md`** — The six-step reasoning chain that SportMind
   agents use. This is the core methodology.

5. **`core/agent-intelligence-model.md`** — Honest assessment of what kind of
   intelligence SportMind provides and where its boundaries are.

**Specific claims to verify:**
- 96% calibration accuracy: see `community/calibration-data/` — all 126 records are there
- Zero wrong-direction records outside European football draws: verifiable in the records
- Named metrics (HAS, NCSI, ATM, etc.): each has a definition in the relevant skill file

---

### 🌍 I want to contribute to SportMind

**Your goal:** Submit calibration records, translate skills, or improve the library.

**Start here — in this order:**

1. **`FIRST-RECORD-CHALLENGE.md`** — The simplest path to your first contribution.
   Read this first. You can submit a calibration record with zero coding required.

2. **`community/calibration-data/CONTRIBUTING.md`** — The full contribution process:
   templates, quality criteria, how records are reviewed, what gets credit.

3. **`community/CONTRIBUTORS.md`** — Recognition tiers and what each level means.

4. **`i18n/README.md`** — If you want to add or improve a language translation.

**What the community needs most right now:**
- Football calibration records (we need athlete_modifier football records specifically)
- Cricket records (dew_factor, India-Pakistan matches)
- Any records from sports currently underrepresented (rowing, netball)
- External records — all 100 current records were submitted by the founding team

---

### 🚀 I just want to see SportMind work in 5 minutes

**Your goal:** See a real output before committing to anything.

```bash
# 1. Clone the repository
git clone https://github.com/sportmind/sportmind.git
cd sportmind

# 2. Install requirements
pip install aiohttp --break-system-packages

# 3. Start the local API
python scripts/sportmind_api.py

# 4. In another terminal — your first signal
python examples/starter-pack/01-simple-signal.py
```

If you do not want to run anything locally, paste the contents of
`core/sportmind-purpose-and-context.md` + `sports/football/sport-domain-football.md`
into any Claude or GPT-4 conversation and ask:

> "PSG are playing Arsenal tomorrow in the UCL. PSG are top of Ligue 1, 
> full squad available. Arsenal have a key forward injured. Paris home.
> Using the SportMind framework you have loaded, generate a pre-match signal."

You will see SportMind working immediately.

---

## Quick reference card

| You are | Start with | Skip |
|---|---|---|
| App developer | starter-pack + skill-bundles | WHO-WE-ARE, sport domains, calibration |
| Agent builder | purpose-and-context + agent-framework | Individual sport files (use bundles) |
| Analyst / commercial | WHO-WE-ARE + agent-prompts | Platform layer, scripts |
| Researcher | calibration-framework + recalibration reports | Agentic workflows, i18n |
| Contributor | FIRST-RECORD-CHALLENGE + CONTRIBUTING | Everything else until first record |
| Just curious | 5-minute quickstart above | Everything |

---

*MIT License · SportMind · sportmind.dev*
