#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 01: Simple Signal
===================================================
The minimum viable SportMind integration.

What this demonstrates:
  - Loading macro state (always the first step)
  - Loading a sport intelligence stack
  - Generating a pre-match signal
  - Reading the confidence output

What you need:
  pip install requests
  python scripts/sportmind_api.py   # in another terminal

Time to first signal: under 2 minutes.

What to change first:
  SPORT     — change to your sport (football, cricket, basketball, mma, ...)
  EVENT_ID  — describe your event
  HOME/AWAY — the teams or athletes
"""

import json
import requests

# ── Configuration ─────────────────────────────────────────────────────────────

SPORTMIND_API = "http://localhost:8080"
SPORT         = "football"
EVENT_ID      = "ucl-qf-psg-arsenal-2026"
HOME_TEAM     = "PSG"
AWAY_TEAM     = "Arsenal"

# ── Step 1: Always check macro state first ────────────────────────────────────
# The macro modifier gates every fan token signal.
# If it is below 0.75, the entire crypto market is in a bear phase and
# sporting signals lose reliability. Always check this before anything else.

macro    = requests.get(f"{SPORTMIND_API}/macro-state").json()
modifier = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
phase    = macro["macro_state"]["crypto_cycle"]["phase"]

print(f"Macro: {phase} (modifier {modifier})")

if modifier < 0.75:
    print("⚠ Macro override active — signals are less reliable in this market phase")

# ── Step 2: Load the intelligence stack ───────────────────────────────────────
# The stack loads skills in the correct order:
# macro → market → sport domain → athlete → fan token

stack = requests.get(
    f"{SPORTMIND_API}/stack",
    params={"sport": SPORT, "use_case": "fan_token_tier1"}
).json()

print(f"Loaded {stack['total_files']} skill files for {SPORT}")

# ── Step 3: Generate the signal ───────────────────────────────────────────────
# In production this uses the full reasoning chain.
# Here: a simplified version that reads macro modifier + stack coverage.

layers_loaded = set()
for skill in stack.get("stack", []):
    path = skill["skill_id"]
    if path.startswith("macro"):        layers_loaded.add(5)
    elif path.startswith("market"):     layers_loaded.add(4)
    elif path.startswith("sports"):     layers_loaded.add(1)
    elif path.startswith("athlete"):    layers_loaded.add(2)
    elif path.startswith("fan-token"):  layers_loaded.add(3)

sms = round(
    (len(layers_loaded) / 5) * 0.35 * 100 +
    (1.0 if modifier >= 0.75 else 0.6) * 0.25 * 100 +
    0.25 * 100 +
    min(modifier, 1.0) * 0.15 * 100, 1
)

sms_tier = (
    "HIGH_QUALITY" if sms >= 80 else
    "GOOD"         if sms >= 60 else
    "PARTIAL"      if sms >= 40 else
    "INSUFFICIENT"
)

# ── Step 4: Output the signal ─────────────────────────────────────────────────

signal = {
    "event": f"{HOME_TEAM} vs {AWAY_TEAM}",
    "sport": SPORT,
    "sportmind_score": {"sms": sms, "sms_tier": sms_tier},
    "macro": {"phase": phase, "modifier": modifier},
    "layers_loaded": sorted(layers_loaded),
    "recommended_action": "ENTER" if sms >= 60 and modifier >= 0.75 else "WAIT",
    "agent_note": (
        "This signal uses SportMind's structural intelligence. "
        "For full accuracy: integrate live lineup confirmation and current form data. "
        "See platform/live-signals.md and core/temporal-awareness.md."
    )
}

print("\n── SportMind Signal ──────────────────────────")
print(json.dumps(signal, indent=2))

# ── What to build next ────────────────────────────────────────────────────────
# This is the foundation. To improve this signal:
#
# 1. Add lineup confirmation (core/temporal-awareness.md — Tier 4, T-2h window)
# 2. Add weather for outdoor sports (platform/realtime-integration-patterns.md — Pattern 4)
# 3. Add live token data from KAYEN API (Pattern 3 in the same file)
# 4. Run this on a schedule → see 03-single-sport-agent.py
# 5. Add Claude as the reasoning engine → see 02-claude-conversation.py
