# SportMind Agent Intelligence Model

**An honest, precise framework for understanding what kind of intelligence
SportMind-powered agents provide — what they can do, where their boundaries
are, and what the long-term trajectory looks like.**

This document exists because the sports AI space makes both types of error:
underselling what AI agents can genuinely do for sports intelligence, and
overclaiming capabilities that do not exist. SportMind serves neither error.
This document states exactly what is true.

---

## What kind of intelligence SportMind provides

SportMind agents are **narrow intelligence systems that are exceptional at
their domain.** They do not aspire to general intelligence. They aspire to
be the most capable, most reliable, most continuously-improving sports
intelligence layer available — and to achieve that through depth, not breadth.

This is a deliberate position, not a limitation. A club commercial director
does not need an AI that can also write poetry. They need an AI that knows
when to buy a player, how to structure a fan token programme, and whether
the macro environment supports a commercial partnership announcement. Depth
in that domain is worth more than breadth across all domains.

---

## The four intelligence dimensions

### 1 — Reasoning: Thinking through problems not seen before

**What SportMind provides:** The six-step reasoning chain in `core/reasoning-patterns.md`,
the conflict resolution hierarchy, the anti-pattern catalogue, and the sport-specific
chain variations together give an LLM a structured way to reason about novel sports
situations. An agent that has loaded SportMind skills can apply the framework to
a competition format it has never analysed, a new fan token on a sport the library
covers, or a breaking news event it has not been trained on.

**How this works:** The LLM provides the general reasoning capability; SportMind
provides the domain-specific framework that structures that reasoning. The result
is better than either alone — a general LLM without SportMind reasons about sports
generically; a SportMind agent without a capable LLM cannot reason at all. The
combination produces domain-competent reasoning about novel situations.

**What it cannot do:** SportMind cannot make an agent reason well about domains
outside sports and commercial intelligence. It cannot override the LLM's underlying
reasoning limitations. It cannot guarantee correct reasoning — it provides the
framework; the quality of reasoning still depends on the LLM and the quality of
the information provided.

**Honest calibration:** 49/52 direction accuracy across 52 calibration records
(94%) across 12 sports. This is the empirical baseline. The framework reasons well.
It is not perfect. The 3 wrong-direction records are documented and their learnings
are incorporated.

---

### 2 — Planning: Setting and pursuing long-term goals

**What SportMind provides:** The autonomous agent framework defines a five-level
autonomy spectrum. Patterns 1-6 in the agentic workflows directory implement
multi-cycle, multi-week autonomous operation. The tournament tracker runs for
39 days. The league monitoring agent tracks a full season. The athlete commercial
tracker monitors commercial trajectories over months. These are all real planning
implementations — agents that set goals, work toward them across many cycles,
and adjust based on what they observe.

**The current boundary:** These agents execute pre-defined plans rather than
setting their own goals. A tournament tracker is initialised with the tournament
structure and runs the plan. It does not independently decide to start tracking
a new tournament or shift its objective mid-season based on what it has learned.
Goal-setting is currently human-defined at deployment; goal-execution is autonomous.

**The practical value:** For the use cases SportMind supports — portfolio monitoring,
tournament tracking, transfer window intelligence, athlete commercial tracking — this
is sufficient. A club commercial director does not need an AI that decides independently
what to monitor. They need one that executes its brief reliably for months at a time.
That is what the framework provides.

**Future direction:** A a future agent goal framework (v3.22 roadmap) (roadmap post-v3.21) would
give agents a principled way to set intermediate goals toward longer-horizon objectives,
evaluate whether those goals are being achieved, and adjust strategy based on outcomes.
This would move SportMind agents from plan-executors to plan-developers.

---

### 3 — Learning: Improving from experience

**What SportMind provides:** The calibration pipeline is the library's learning
mechanism. 52 outcome records across 12 sports feed back into modifier recalibration.
When a modifier's evidence threshold is reached (50 records for most, 100 for
athlete-level, 200 for macro), the library updates the modifier values based on
empirical evidence rather than theoretical estimation. This is learning — genuine,
evidence-based improvement to the library's intelligence.

**How it differs from autonomous learning:** The calibration pipeline is
human-mediated. Agents generate the analyses; humans record outcomes; the community
reviews records; SportMind updates modifiers through version releases. The learning
happens at the library level, not at the agent level. An individual agent does not
update its own knowledge — it loads the improved library version.

**Why this is the right model:** Autonomous self-modification of sports intelligence
would be unsafe without the validation step. A modifier that updates itself based
on 3 incorrect predictions would corrupt the library. The human-mediated calibration
model ensures that every modifier change has evidence behind it and has been reviewed
for correctness. This is slower than autonomous learning but more reliable.

**Current learning rate:** The library has gone from theoretically-estimated modifiers
(v3.0) to empirically-calibrated modifiers across 12 sports (v3.20) in under 20
version cycles. The dew factor, the weight miss modifier, the derby draw premium,
the street circuit qualifying premium, the India-Pakistan ×2.00, the dual-nation
NCSI model — all now have real-match validation. The learning is real. It is just
not instant.

---

### 4 — Context: Understanding why, not just how

**What SportMind provides:** `WHO-WE-ARE.md` gives agents (and humans) the complete
context for what SportMind is and why it exists. The agent-prompts organised by
stakeholder type teach agents the *why* of each use case — why a club commercial
director needs APS adjusted rather than raw APS, why a sports agent needs the
financial context to make the commercial brief credible, why a developer needs
bundle IDs rather than manual skill loading. The six safety principles in the
autonomous agent framework explain *why* intelligence separation from execution
is a safety principle, not just a rule.

**What this produces in practice:** An agent that loads `WHO-WE-ARE.md` and
`core/autonomous-agent-framework.md` before operating understands that it is
part of a larger suite (FanTokenIntel, SportFi Kit, LLMs), that its role
is intelligence not execution, that it serves specific stakeholders with specific
needs, and that the library it uses has been empirically validated. This contextual
understanding produces better outputs than an agent that only loads sport domain skills.

**The current gap:** Contextual understanding currently requires loading multiple
documents. A single a consolidated context document (v3.22 roadmap) that consolidates
the why across all dimensions in a short, agent-readable format would be more
efficient. This is on the v3.22 roadmap.

---

## The ANI / AGI / ASI spectrum applied honestly

```
WHERE SPORTMIND AGENTS SIT TODAY:

ANI (Artificial Narrow Intelligence):
  Definition: Excellent at a specific domain; cannot generalise beyond it
  SportMind position: YES, and intentionally so.
  
  A SportMind agent is the best sports intelligence system a developer can
  deploy today. It is genuinely narrow — it does not code, it does not write
  essays, it does not reason about topics outside sports and commercial intelligence.
  Within its domain, it is excellent.
  
  The right comparison: Google Maps is ANI for navigation and is more useful
  than a general-purpose map that also does everything else. SportMind is ANI
  for sports intelligence and is more useful than a general AI that also does
  sports as one of many things.

AGI (Artificial General Intelligence):
  Definition: Can perform any intellectual task a human can
  SportMind position: NOT a target, and deliberately so.
  
  A SportMind AGI would need to reason about law, medicine, finance, philosophy,
  and sports simultaneously with human-level competence in all areas. That is not
  the objective. The objective is to be the definitive intelligence layer for
  sports — the framework that every AI sports system uses as its foundation.
  Domain excellence is more achievable, more verifiable, and more commercially
  valuable than general competence.
  
  The honest statement: When developers ask "can SportMind do AGI?" the correct
  answer is "SportMind makes any capable LLM the world's best sports intelligence
  agent. That is the goal we are building toward. AGI is someone else's goal."

ASI (Artificial Superintelligence):
  Definition: Better than humans at everything
  SportMind position: The vision in sports intelligence specifically.
  
  SportMind's long-horizon aspiration is to be the sports intelligence layer
  that exceeds what any individual human expert could construct and maintain alone.
  
  Not "better than humans at everything" — but "provides a framework for sports
  intelligence that improves continuously beyond what any individual could maintain,
  through community calibration, empirical validation, and collective knowledge."
  
  The calibration pipeline is the mechanism. 52 records today. 1000 records in
  three years. Modifiers calibrated from evidence across every major sport. An
  intelligence layer that knows more about sports commercial signals than any
  individual expert because it has been trained on the outcomes of thousands of
  real analyses run by thousands of practitioners.
  
  That is the aspiration. It is specific, achievable, and worth building toward.
```

---

## SportMind's intelligence architecture

```
LAYER 1 — KNOWLEDGE (static, version-controlled):
  What: 355+ skill files covering 42 sports, 29 athlete intelligence areas,
        35 fan token skills, 42 market documents, 23 core frameworks
  How it improves: Library version updates; community calibration; new skill additions
  Reliability: Highest — verified content with SHA-256 integrity checking

LAYER 2 — REASONING (dynamic, LLM-powered):
  What: The six-step chain applied by an LLM to current knowledge + live data
  How it improves: LLM capability improvements; better skill loading order; refined prompts
  Reliability: High — validated reasoning framework; 94% calibration accuracy

LAYER 3 — ACTION (application-layer, developer-implemented):
  What: What agents DO with the intelligence output (alerts, trades, governance)
  How it improves: Application-layer development by community
  Reliability: Developer-controlled — SportMind does not control this layer

LAYER 4 — LEARNING (pipeline, community-mediated):
  What: Calibration records → modifier recalibration → library improvement
  How it improves: Community contribution; evidence threshold crossing; review process
  Reliability: Validated — every modifier change requires evidence and review

THE INTELLIGENCE LOOP:
  Human/agent runs analysis (Layer 2 using Layer 1 knowledge)
  → Application layer acts on output (Layer 3)
  → Outcome is recorded (feeds Layer 4)
  → Layer 4 improves Layer 1 (better modifiers → better Layer 2 reasoning)
  → The loop continues; the library improves; agents become more accurate
```

---

## Practical implications for developers

```
WHAT THIS MEANS FOR WHAT YOU BUILD:

If you want the best sports intelligence agent available today:
  → Load SportMind skills as context for your LLM
  → Use the correct bundle for your use case (platform/skill-bundles.md)
  → Apply the six-step reasoning chain (core/reasoning-patterns.md)
  → Feed live data correctly (platform/realtime-integration-patterns.md)
  → You get: 94%+ calibrated sports intelligence with SMS confidence scores

If you want continuous improvement without rebuilding:
  → Use the MCP server (tools update as library improves)
  → Subscribe to library version notifications (platform/freshness-strategy.md)
  → Submit calibration records (community/calibration-data/CONTRIBUTING.md)
  → The library gets better; your agents benefit automatically

If you want to build toward the long-horizon vision:
  → Contribute to the calibration pipeline (most impactful contribution)
  → Build applications that surface SportMind intelligence to sports practitioners
  → Share what you learn — the library improves from community knowledge
  → The more agents run SportMind analysis and record outcomes, the more
    accurate the modifiers become, and the better every agent in the suite gets

What SportMind will not do:
  → Execute financial transactions autonomously
  → Override human decisions on high-stakes commercial matters
  → Claim certainty where genuine uncertainty exists
  → Promise capabilities that do not exist
  These limits are features, not limitations. They are what makes the library trustworthy.
```

---

## Compatibility

**Who we are:** `WHO-WE-ARE.md` — identity document for sports industry stakeholders
**Agent framework:** `core/autonomous-agent-framework.md` — full lifecycle and safety model
**Reasoning patterns:** `core/reasoning-patterns.md` — the six-step chain
**Calibration pipeline:** `community/calibration-data/CONTRIBUTING.md` — how learning happens
**Suite context:** `platform/integration-partners.md` — how SportMind fits the broader stack

*MIT License · SportMind · sportmind.dev*
