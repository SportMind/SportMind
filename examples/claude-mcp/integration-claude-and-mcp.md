# SportMind — Claude / Claude Code Integration

> **v2.1.0:** SportMind now has five layers. Full loading order:
> Layer 5 (macro) → Layer 4 (market) → Layer 1 (sport domain) → Layer 2 (athlete) → Layer 3 (fan token).
> The examples below show Layers 1–2. Prepend `macro/macro-overview.md` and
> `market/market-{sport}.md` for complete five-layer intelligence.

SportMind skills can be loaded into Claude agents via MCP (Model Context Protocol)
or directly via system prompt. This example covers both approaches.

---

## Option A — System prompt (simplest, works everywhere)

Copy the skill content you need into your Claude system prompt.
Works in Claude.ai, Claude Code, Claude Desktop, and any API call.

```python
import anthropic

# Load the skills you need
with open("sports/football/sport-domain-football.md") as f:
    football_domain = f.read()

with open("athlete/football/athlete-intel-football.md") as f:
    football_athlete = f.read()

with open("core/core-signal-weights-by-sport.md") as f:
    signal_weights = f.read()

system_prompt = f"""
You are a football sports intelligence agent.

{football_domain}

{football_athlete}

{signal_weights}

When evaluating any football match:
1. Score match importance using the domain model
2. Apply athlete modifier based on player availability and form
3. Weight signals using football-specific weights
4. Select and apply the most relevant event playbook
5. Output a clear adjusted_signal_score with recommendation
"""

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "PSG are playing UCL tonight. Mbappé is confirmed starting, in HOT form. Whale sell_ratio is 0.685. Base signal score is 68. What's your recommendation?"}
    ]
)
print(message.content[0].text)
```

---

## Option B — Claude Code MCP server

Run SportMind as a local MCP server that Claude Code can connect to.

### Setup

```bash
# Clone SportMind
git clone https://github.com/SportMind/SportMind
cd sportmind

# Install the MCP server package (when available)
npm install @sportmind/mcp-server

# Add to Claude Code
claude mcp add sportmind npx @sportmind/mcp-server
```

### What the MCP server exposes

Once connected, Claude Code gains these tools:

| Tool | Description |
|---|---|
| `sportmind_get_sport_skill` | Load a sport domain skill by name |
| `sportmind_get_athlete_skill` | Load an athlete skill by sport |
| `sportmind_apply_modifier` | Compute athlete modifier given player data |
| `sportmind_get_playbooks` | Get event playbooks for a sport |
| `sportmind_get_signal_weights` | Get recommended signal weights for a sport |
| `sportmind_get_result_matrix` | Get result impact ranges for a sport |
| `sportmind_list_skills` | List all available skills and their status |

### Example Claude Code session

```
User: I'm building a football prediction agent. Load the SportMind football skills
      and tell me how to evaluate a Champions League match.

Claude: [calls sportmind_get_sport_skill(sport="football")]
        [calls sportmind_get_athlete_skill(sport="football")]
        [calls sportmind_get_signal_weights(sport="football")]

        Based on the SportMind football domain skill, here's how to evaluate
        a Champions League match:

        Match importance:
        - UCL = Tier 1 competition (highest token impact)
        - Knockout round: apply 1.25× sizing vs standard
        - Group stage: standard sizing applies

        Athlete modifier workflow:
        1. get_key_player_availability — check who's confirmed vs doubtful
        2. get_player_form_score — last 5 match rolling average
        3. get_goalkeeper_rating — GK is highest single-player modifier
        4. apply_athlete_modifier — composite score

        Signal weighting for football:
        - Sports catalyst: 30% (most important)
        - Whale flows: 25%
        - Social: 20%
        - Price trend: 15%
        - Macro: 10%

        Most relevant playbook: Playbook 3 — Champions League Knockout Catalyst
        [details...]
```

---

## Option C — Claude.ai with file upload

Upload skill files directly as context documents in Claude.ai:

1. Open a new Claude.ai conversation
2. Click the attachment icon
3. Upload the skill files you need:
   - `sports/football/sport-domain-football.md`
   - `athlete/football/athlete-intel-football.md`
   - `core/core-signal-weights-by-sport.md`
4. Start your conversation — Claude has full skill context

This is the quickest way to use SportMind without any code.

---

## Best practices for Claude integration

**Be explicit about the task.** Start your conversation with:
```
"You have SportMind sports intelligence skills loaded. I need you to evaluate
[event] for [token/market]. Apply the football domain model and athlete
modifier system to give me an adjusted recommendation."
```

**Ask for structured output.** Claude can output structured modifier breakdowns:
```
"Give me the response as a JSON object with:
- base_signal_score
- athlete_modifier (and breakdown by component)
- adjusted_signal_score
- signal_direction
- recommendation
- key_risks (array)"
```

**Use the athlete/meta orchestrator for multi-token analysis:**
```
"I have upcoming matches for PSG, BAR, and NAVI tonight.
Run the full SportMind modifier pipeline for each and rank them
by adjusted_signal_score."
```
