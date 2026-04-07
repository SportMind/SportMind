#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 02: Claude Conversation
=========================================================
SportMind loaded as Claude context via MCP.

What this demonstrates:
  - Connecting SportMind as a Claude MCP tool
  - Claude using SportMind intelligence to reason about a sporting event
  - Structured output from the conversation
  - The LLM-as-reasoning-engine pattern

What you need:
  pip install anthropic mcp
  export ANTHROPIC_API_KEY=your_key_here
  python scripts/sportmind_mcp.py --port 3001  # in another terminal

What to change first:
  USER_QUERY — ask about any sport or event
  MCP_URL    — if hosting SportMind MCP remotely

SportMind's role here:
  Claude is the reasoning engine.
  SportMind is the domain knowledge context (loaded as an MCP tool).
  You get Claude's natural language reasoning PLUS SportMind's structured intelligence.
"""

import os
import anthropic

# ── Configuration ─────────────────────────────────────────────────────────────

MCP_URL    = os.environ.get("SPORTMIND_MCP_URL", "http://localhost:3001/mcp")
API_KEY    = os.environ.get("ANTHROPIC_API_KEY", "")
USER_QUERY = """
Analyse tonight's UCL quarter-final between PSG and Arsenal.
PSG are at home. Arsenal have been in strong form away in Europe.

Please:
1. Check the macro state first
2. Generate a pre-match signal using SportMind
3. Explain what the key modifiers are and why
4. Tell me what would change your assessment
"""

# ── The system prompt ─────────────────────────────────────────────────────────
# This tells Claude how to use SportMind correctly.
# It enforces the reasoning chain from core/reasoning-patterns.md.

SYSTEM_PROMPT = """You are a sports intelligence analyst powered by SportMind.

You have access to SportMind MCP tools. For any sports analysis:

1. ALWAYS call sportmind_macro FIRST — the macro modifier gates all fan token signals
2. Then call sportmind_signal for the specific event
3. Apply the six-step SportMind reasoning chain:
   Step 1: Macro check (you just did this)
   Step 2: Competition classification (what tier is this event?)
   Step 3: Athlete availability (is lineup confirmed?)
   Step 4: Signal computation (what does the evidence say?)
   Step 5: DeFi/liquidity check (if fan token application)
   Step 6: Confidence output (SMS, tier, recommended_action)

Output format:
  - State the macro phase and modifier
  - State the competition tier and its signal weight
  - List the key modifiers applied and their values
  - State the SMS and what it means
  - State the recommended_action with reasoning
  - Note what information would change your assessment

Remember: SportMind provides intelligence. You provide reasoning. 
Never recommend specific financial decisions — provide intelligence context only.
"""

# ── Run the conversation ───────────────────────────────────────────────────────

def run_sportmind_conversation(query: str) -> str:
    """Run a Claude conversation with SportMind as MCP context."""

    if not API_KEY:
        print("ERROR: Set ANTHROPIC_API_KEY environment variable")
        return ""

    client = anthropic.Anthropic(api_key=API_KEY)

    print(f"Query: {query[:80]}...")
    print("Calling SportMind via Claude MCP...\n")

    response = client.beta.messages.create(
        model      = "claude-sonnet-4-20250514",
        max_tokens = 2000,
        system     = SYSTEM_PROMPT,
        mcp_servers= [
            {
                "type": "url",
                "url":  MCP_URL,
                "name": "sportmind"
            }
        ],
        messages   = [
            {"role": "user", "content": query}
        ]
    )

    # Extract the text response
    full_response = ""
    for block in response.content:
        if hasattr(block, "text"):
            full_response += block.text

    return full_response


if __name__ == "__main__":
    result = run_sportmind_conversation(USER_QUERY)
    print("── Claude + SportMind Analysis ──────────────")
    print(result)

# ── Extending this example ────────────────────────────────────────────────────
#
# Multi-turn conversation (maintain history):
#
#   history = []
#   while True:
#       user_input = input("You: ")
#       history.append({"role": "user", "content": user_input})
#
#       response = client.beta.messages.create(
#           model=..., mcp_servers=[...],
#           messages=history
#       )
#       assistant_msg = response.content[0].text
#       history.append({"role": "assistant", "content": assistant_msg})
#       print(f"SportMind: {assistant_msg}")
#
# Structured JSON output (for downstream processing):
#   Add to system prompt: "Always end your response with a JSON block tagged
#   ```json containing: {sms, macro_modifier, recommended_action, key_flags[]}"
#
# See: platform/sportmind-mcp-server.md for all five MCP tool definitions
# See: core/reasoning-patterns.md for the full six-step chain
