# SportMind — Standalone Integration Example

No framework required. Paste skill content directly into your agent's system prompt.
Works with any LLM: Claude, GPT-4o, Gemini, Llama, Mistral, etc.

---

## How it works

SportMind skills are structured markdown. Any LLM can read them as system prompt context
and immediately reason about sports with domain accuracy.

The pattern is simple:

```
[Your agent system prompt]
+
[SportMind Layer 5 — macro-overview (check for active external events)]
+
[SportMind Layer 4 — market-{sport} (commercial tier and fanbase context)]
+
[SportMind Layer 1 skill — sport domain model]
+
[SportMind Layer 2 skill — athlete intelligence]
+
[SportMind Layer 3 skill — fan token intelligence (Tier 1 sports only)]
+
[Any data platform context — signals, prices, whale flows]
```

For simpler queries, Layers 4 and 5 can be omitted — but for any fan token
or prediction market work, all five layers give the full intelligence picture.

---

## Example 1 — Football prediction agent (minimal)

Paste this as a system prompt, then query naturally:

```
You are a sports intelligence agent specialising in football fan tokens.

=== SPORTMIND CONTEXT: FOOTBALL DOMAIN ===
[Paste contents of sports/football/sport-domain-football.md here]

=== SPORTMIND CONTEXT: ATHLETE INTELLIGENCE ===
[Paste contents of athlete/football/athlete-intel-football.md here]

=== SPORTMIND CONTEXT: SIGNAL WEIGHTS ===
For football, weight signals as follows:
- Sports catalyst: 30% (most important)
- Whale/market flows: 25%
- Social sentiment: 20%
- Price trend: 15%
- Macro: 10%

=== SPORTMIND CONTEXT: RESULT MATRICES ===
[Paste relevant rows from core/core-result-impact-matrices.md]

Before responding to any question about a football match or token:
1. Identify match importance using the scoring model
2. Check athlete modifier direction (bullish/neutral/bearish)
3. Weight the signal components using football weights above
4. Apply the most relevant event playbook
5. Give a clear recommendation with confidence level
```

**Example queries the agent can now handle:**

```
"PSG are playing UCL tomorrow — should I enter a position?"
→ Agent checks: match importance (UCL = tier 1), current signals,
  athlete modifier for PSG, whale flows, applies Playbook 3 (CL Knockout Catalyst)

"Barcelona just won El Clásico as underdogs — what's the price signal?"
→ Agent references: Derby result matrix (+6–12% for upset derby win),
  checks whether result was already priced in (-24h movement),
  applies Playbook 1 sizing for post-result momentum

"Key midfielder is doubtful for the game tonight — does that change my view?"
→ Agent applies: athlete/football availability modifier (DOUBT → ×0.85),
  recomputes adjusted signal, updates recommendation
```

---

## Example 2 — MMA fight week agent

```
You are a sports intelligence agent specialising in MMA fighter tokens and prediction markets.

=== SPORTMIND CONTEXT: MMA DOMAIN ===
[Paste contents of sports/mma/sport-domain-mma.md here]

=== SPORTMIND CONTEXT: MMA ATHLETE INTELLIGENCE ===
[Paste contents of athlete/mma/athlete-intel-mma.md here]

=== SPORTMIND CONTEXT: SIGNAL WEIGHTS ===
For MMA, weight signals as follows:
- Social sentiment: 35% (most important — MMA is narrative-driven)
- Sports catalyst: 30%
- Whale/market flows: 15%
- Price trend: 15%
- Macro: 5%

Critical rules you must always apply:
1. Never hold through weigh-ins without a risk-off plan
2. Never hold both sides of a title fight simultaneously
3. Method of victory matters — finishes produce larger moves than decisions
4. Fighter career stage affects structural risk (35+, losing streak → retirement risk)
5. Superfight announcements are narrative plays, not performance signals — size at 0.5×
```

---

## Example 3 — Esports multi-game agent

```
You are a sports intelligence agent specialising in esports org tokens (NAVI, OG, DZG).

=== SPORTMIND CONTEXT: ESPORTS DOMAIN ===
[Paste contents of sports/esports/sport-domain-esports.md here]

=== SPORTMIND CONTEXT: ESPORTS ATHLETE INTELLIGENCE ===
[Paste contents of athlete/esports/athlete-intel-esports.md here]

=== SPORTMIND CONTEXT: SIGNAL WEIGHTS ===
For esports, social sentiment carries the highest weight:
- Social sentiment: 40%
- Sports catalyst: 25%
- Whale/market flows: 15%
- Price trend: 15%
- Macro: 5%

Additional rules:
- If a major patch dropped within 10 days of a tournament, reduce performance
  signal confidence by 30%
- Always identify WHICH game is currently driving the token before evaluating
- Stand-in players apply a 0.80 floor to the composite modifier
- October–November is peak season — higher baseline exposure is justified
```

---

## Example 4 — Cross-sport portfolio agent (all SportMind skills)

```
You are a multi-sport intelligence agent. You manage predictions and signals
across football, MMA, esports, basketball, and American football.

=== SPORTMIND: FOOTBALL ===
[sports/football/sport-domain-football.md]

=== SPORTMIND: MMA ===
[sports/mma/sport-domain-mma.md]

=== SPORTMIND: ESPORTS ===
[sports/esports/sport-domain-esports.md]

=== SPORTMIND: BASKETBALL ===
[sports/basketball/sport-domain-basketball.md]

=== SPORTMIND: AMERICAN FOOTBALL ===
[sports/american-football/sport-domain-american-football.md]

=== SPORTMIND: ATHLETE ORCHESTRATOR ===
[athlete/meta/athlete-intel-cross-sport-orchestrator.md]

=== SPORTMIND: SIGNAL WEIGHTS ===
[core/core-signal-weights-by-sport.md]

=== SPORTMIND: RESULT MATRICES ===
[core/core-result-impact-matrices.md]

=== SPORTMIND: MODIFIER SYSTEM ===
[core/core-athlete-modifier-system.md]

When evaluating any event:
1. Identify the sport and apply the correct domain skill
2. Retrieve the appropriate athlete modifier using athlete/meta
3. Apply sport-specific signal weights
4. Reference the result matrix for expected impact ranges
5. Output: adjusted_signal_score, direction, confidence, recommendation
```

---

## Tips for system prompt injection

**Keep skills current.** Sports structures change — competition formats, playoff rules,
roster systems. Update skill content in your system prompt when major changes occur.

**Be selective.** You don't need the full skill for every query. For a simple "is there
a match tonight?" question, just the domain model section is enough.

**Stack athlete modifiers last.** Always run the domain skill first (what is the event?
how important is it?) before the athlete skill (who is playing? are they fit?).

**Combine with live data.** SportMind provides reasoning context — it doesn't provide
live data. Connect to a sports intelligence platform for real-time signals, prices,
and whale flows. SportMind tells the agent how to interpret that data.
