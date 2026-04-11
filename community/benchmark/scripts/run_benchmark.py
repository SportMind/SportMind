#!/usr/bin/env python3
"""
SportMind Benchmark Runner
Compares SportMind + LLM vs Vanilla LLM on 40 standardised historical scenarios.

Usage:
    python run_benchmark.py
    python run_benchmark.py --sport football
    python run_benchmark.py --sport all --config both --model claude-sonnet-4-20250514

Requires:
    pip install anthropic aiohttp
    export ANTHROPIC_API_KEY=your_key
"""

import asyncio
import json
import os
import sys
import argparse
import time
from pathlib import Path
from datetime import datetime, timezone

ROOT      = Path(__file__).parent.parent.parent.parent  # SportMind repo root
BM_DIR    = Path(__file__).parent.parent
SCENARIOS = BM_DIR / "scenarios"
RESULTS   = BM_DIR / "results"
RESULTS.mkdir(exist_ok=True)
(RESULTS / "history").mkdir(exist_ok=True)

try:
    import anthropic
except ImportError:
    print("ERROR: pip install anthropic")
    sys.exit(1)

MODEL    = "claude-sonnet-4-20250514"
MAX_TOKENS = 1000

VANILLA_SYSTEM = """You are a sports analyst. Answer sports prediction questions 
based on your knowledge. Predict the direction (HOME/AWAY/DRAW for match outcomes, 
or ENTER/WAIT/ABSTAIN for fan token signals) and explain your key reasoning variables.
Be concise — 150 words maximum."""

SPORTMIND_SYSTEM_TEMPLATE = """You are a SportMind-powered sports intelligence agent.
You have been loaded with the following SportMind skill files:

{skill_content}

Using the SportMind framework above, predict the direction for the scenario provided.
Output format:
DIRECTION: [HOME/AWAY/DRAW or ENTER/WAIT/ABSTAIN]
KEY_VARIABLE: [primary modifier or signal variable — use SportMind named metrics where applicable]
REASONING: [2-3 sentences maximum]
SMS: [estimated SportMind Score 0-100]"""


def load_skill_content(skill_paths: list, root: Path) -> str:
    """Load and concatenate skill file contents for SportMind context."""
    content_parts = []
    for skill_path in skill_paths:
        full_path = root / skill_path
        if full_path.exists():
            text = full_path.read_text(encoding="utf-8")
            # Use compressed version if available and file is large
            compressed_path = root / "compressed" / "README.md"
            # Truncate very long files to first 3000 chars to manage context
            if len(text) > 4000:
                text = text[:3800] + "\n\n[TRUNCATED FOR BENCHMARK CONTEXT]"
            content_parts.append(f"--- {skill_path} ---\n{text}")
        else:
            content_parts.append(f"--- {skill_path} ---\n[FILE NOT FOUND]")
    return "\n\n".join(content_parts)


def build_scenario_prompt(scenario: dict) -> str:
    """Build the user prompt from a scenario."""
    event   = scenario.get("event", {})
    context = scenario.get("context", {})

    lines = [
        f"SPORT: {scenario['sport'].upper()}",
        f"EVENT: {event.get('name', '')}",
        f"DATE: {event.get('date', '')}",
        f"COMPETITION: {event.get('competition', '')}",
        f"VENUE: {event.get('venue', '')}",
        "",
    ]

    if scenario.get("signal_type") == "fan_token_commercial":
        lines += [
            f"TOKEN: {context.get('token', '')}",
            f"LIFECYCLE PHASE: {context.get('lifecycle_phase', '')}",
        ]
    else:
        lines += [
            f"HOME/TEAM A: {context.get('home_team', '')}",
            f"AWAY/TEAM B: {context.get('away_team', '')}",
        ]

    lines += [
        "",
        f"CONTEXT: {context.get('pre_match_notes', '')}",
        "",
        f"QUESTION: {scenario.get('question', '')}",
    ]

    return "\n".join(lines)


def parse_response(response_text: str) -> dict:
    """Extract direction, key variable, and SMS from model response."""
    lines      = response_text.upper()
    direction  = None
    key_var    = None
    sms        = None

    for line in response_text.split("\n"):
        line_upper = line.upper().strip()
        if line_upper.startswith("DIRECTION:"):
            val = line.split(":", 1)[-1].strip().upper()
            for d in ["HOME", "AWAY", "DRAW", "ENTER", "WAIT", "ABSTAIN"]:
                if d in val:
                    direction = d
                    break
        elif line_upper.startswith("KEY_VARIABLE:"):
            key_var = line.split(":", 1)[-1].strip()
        elif line_upper.startswith("SMS:"):
            try:
                sms = float(line.split(":", 1)[-1].strip().split()[0])
            except:
                pass

    # Fallback: scan full text for direction
    if not direction:
        for d in ["HOME", "AWAY", "DRAW", "ENTER", "WAIT", "ABSTAIN"]:
            if d in lines:
                direction = d
                break

    return {
        "direction":    direction,
        "key_variable": key_var,
        "sms":          sms,
        "raw":          response_text,
    }


def score_response(parsed: dict, scenario: dict) -> dict:
    """Score a parsed response against the verified outcome."""
    scoring         = scenario.get("scoring", {})
    verified        = scenario.get("verified_outcome", {})
    correct_dir     = scoring.get("direction_correct_if", "")
    keywords        = [k.lower() for k in scoring.get("key_variable_keywords", [])]

    direction_correct = (parsed.get("direction") == correct_dir)

    key_var_text = (parsed.get("key_variable") or "") + " " + parsed.get("raw", "")
    key_var_text = key_var_text.lower()
    key_var_identified = any(kw in key_var_text for kw in keywords) if keywords else None

    return {
        "direction_correct":      direction_correct,
        "predicted_direction":    parsed.get("direction"),
        "correct_direction":      correct_dir,
        "key_variable_identified": key_var_identified,
        "sms":                    parsed.get("sms"),
    }


async def run_scenario(client, scenario: dict, config: str, root: Path) -> dict:
    """Run a single scenario for one configuration (sportmind or vanilla)."""
    prompt = build_scenario_prompt(scenario)

    if config == "sportmind":
        skill_content  = load_skill_content(
            scenario.get("sportmind_skills", []), root
        )
        system_prompt  = SPORTMIND_SYSTEM_TEMPLATE.format(
            skill_content=skill_content
        )
    else:
        system_prompt  = VANILLA_SYSTEM

    try:
        response = client.messages.create(
            model      = MODEL,
            max_tokens = MAX_TOKENS,
            system     = system_prompt,
            messages   = [{"role": "user", "content": prompt}],
        )
        response_text = response.content[0].text
    except Exception as e:
        response_text = f"ERROR: {str(e)}"

    parsed = parse_response(response_text)
    scored = score_response(parsed, scenario)

    return {
        "scenario_id":  scenario["scenario_id"],
        "sport":        scenario["sport"],
        "difficulty":   scenario.get("difficulty", "standard"),
        "signal_type":  scenario.get("signal_type", "match_outcome"),
        "config":       config,
        "response":     response_text,
        "parsed":       parsed,
        "scored":       scored,
    }


def load_scenarios(sports_filter: str) -> list:
    """Load all scenarios, optionally filtered by sport."""
    scenarios = []
    for sport_dir in sorted(SCENARIOS.iterdir()):
        if not sport_dir.is_dir():
            continue
        if sports_filter != "all" and sport_dir.name != sports_filter:
            continue
        for scenario_file in sorted(sport_dir.glob("*.json")):
            try:
                s = json.loads(scenario_file.read_text())
                scenarios.append(s)
            except Exception as e:
                print(f"  WARNING: Could not load {scenario_file}: {e}")
    return scenarios


async def run_benchmark(sport: str = "all", config: str = "both",
                         model: str = MODEL) -> dict:
    """Main benchmark runner."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client    = anthropic.Anthropic(api_key=api_key)
    scenarios = load_scenarios(sport)
    configs   = ["sportmind", "vanilla"] if config == "both" else [config]

    print(f"\nSportMind Benchmark")
    print(f"  Scenarios:   {len(scenarios)}")
    print(f"  Configs:     {', '.join(configs)}")
    print(f"  Model:       {model}")
    print(f"  Started:     {datetime.now(timezone.utc).isoformat()}")
    print(f"{'─'*52}\n")

    all_results = []
    total_runs  = len(scenarios) * len(configs)
    completed   = 0

    for cfg in configs:
        print(f"Running config: {cfg.upper()}")
        for i, scenario in enumerate(scenarios):
            print(f"  [{i+1}/{len(scenarios)}] {scenario['scenario_id'][:55]}",
                  end="... ", flush=True)
            result = await run_scenario(client, scenario, cfg, ROOT)
            all_results.append(result)
            completed += 1
            correct = "✓" if result["scored"]["direction_correct"] else "✗"
            print(correct)
            # Small delay to avoid rate limits
            await asyncio.sleep(0.5)
        print()

    # Compile results
    run_meta = {
        "run_at":    datetime.now(timezone.utc).isoformat(),
        "model":     model,
        "scenarios": len(scenarios),
        "configs":   configs,
        "version":   "3.47.0",
    }

    output = {
        "meta":    run_meta,
        "results": all_results,
    }

    # Save results
    out_path = RESULTS / "latest.json"
    out_path.write_text(json.dumps(output, indent=2))

    # Archive
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    archive = RESULTS / "history" / f"run-{ts}.json"
    archive.write_text(json.dumps(output, indent=2))

    print(f"Results saved to {out_path}")
    return output


def print_summary(results: dict):
    """Print accuracy summary table to stdout."""
    from collections import defaultdict

    by_sport_config = defaultdict(lambda: {"correct": 0, "total": 0})
    overall         = {"sportmind": {"c": 0, "t": 0}, "vanilla": {"c": 0, "t": 0}}

    for r in results["results"]:
        sport  = r["sport"]
        cfg    = r["config"]
        c      = r["scored"]["direction_correct"]
        key    = f"{sport}_{cfg}"
        by_sport_config[key]["total"]   += 1
        by_sport_config[key]["correct"] += int(c)
        overall[cfg]["t"] += 1
        overall[cfg]["c"] += int(c)

    # Get all sports
    sports = sorted(set(r["sport"] for r in results["results"]))

    print(f"\n{'─'*68}")
    print(f"{'Sport':<18} {'SportMind':>14} {'Vanilla':>14} {'Delta':>10}")
    print(f"{'─'*68}")

    for sport in sports:
        sm = by_sport_config[f"{sport}_sportmind"]
        vn = by_sport_config[f"{sport}_vanilla"]
        sm_acc = sm["correct"] / sm["total"] * 100 if sm["total"] else 0
        vn_acc = vn["correct"] / vn["total"] * 100 if vn["total"] else 0
        delta  = sm_acc - vn_acc
        delta_str = f"+{delta:.0f}%" if delta > 0 else f"{delta:.0f}%"
        print(f"{sport:<18} {sm['correct']}/{sm['total']} ({sm_acc:.0f}%){'':<3}"
              f"{vn['correct']}/{vn['total']} ({vn_acc:.0f}%){'':<3}"
              f"{delta_str:>8}")

    print(f"{'─'*68}")
    sm_o   = overall["sportmind"]
    vn_o   = overall["vanilla"]
    sm_acc = sm_o["c"] / sm_o["t"] * 100 if sm_o["t"] else 0
    vn_acc = vn_o["c"] / vn_o["t"] * 100 if vn_o["t"] else 0
    delta  = sm_acc - vn_acc
    delta_str = f"+{delta:.0f}%" if delta > 0 else f"{delta:.0f}%"
    print(f"{'OVERALL':<18} {sm_o['c']}/{sm_o['t']} ({sm_acc:.0f}%){'':<3}"
          f"{vn_o['c']}/{vn_o['t']} ({vn_acc:.0f}%){'':<3}"
          f"{delta_str:>8}")
    print(f"{'─'*68}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SportMind Benchmark Runner")
    parser.add_argument("--sport",    default="all",
                        help="Sport to test (football/cricket/mma/formula1/all)")
    parser.add_argument("--config",   default="both",
                        choices=["sportmind", "vanilla", "both"])
    parser.add_argument("--model",    default=MODEL)
    parser.add_argument("--output",   default=None,
                        help="Custom output path for results JSON")
    args = parser.parse_args()

    results = asyncio.run(run_benchmark(
        sport  = args.sport,
        config = args.config,
        model  = args.model,
    ))

    print_summary(results)
    print(f"Full results: {RESULTS / 'latest.json'}")
    print(f"Run: python score_results.py  to generate the report\n")
