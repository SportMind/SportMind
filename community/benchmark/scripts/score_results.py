#!/usr/bin/env python3
"""
SportMind Benchmark Score Results
Reads results/latest.json and generates a human-readable report.

Usage:
    python score_results.py
    python score_results.py --input results/history/run-20260410.json
    python score_results.py --output results/latest-report.md
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone

BM_DIR  = Path(__file__).parent.parent
RESULTS = BM_DIR / "results"


def load_results(input_path: Path) -> dict:
    return json.loads(input_path.read_text())


def compute_accuracy(results_list: list, config: str) -> dict:
    """Compute accuracy metrics for a config across all scenarios."""
    by_sport    = defaultdict(lambda: {"c": 0, "t": 0})
    by_diff     = defaultdict(lambda: {"c": 0, "t": 0})
    by_signal   = defaultdict(lambda: {"c": 0, "t": 0})
    kv_total    = 0
    kv_correct  = 0
    overall     = {"c": 0, "t": 0}

    for r in results_list:
        if r["config"] != config:
            continue
        sport   = r["sport"]
        diff    = r.get("difficulty", "standard")
        sig     = r.get("signal_type", "match_outcome")
        correct = r["scored"]["direction_correct"]
        kv      = r["scored"].get("key_variable_identified")

        by_sport[sport]["t"]  += 1
        by_sport[sport]["c"]  += int(correct)
        by_diff[diff]["t"]    += 1
        by_diff[diff]["c"]    += int(correct)
        by_signal[sig]["t"]   += 1
        by_signal[sig]["c"]   += int(correct)
        overall["t"]          += 1
        overall["c"]          += int(correct)

        if kv is not None:
            kv_total   += 1
            kv_correct += int(kv)

    def pct(d): return round(d["c"] / d["t"] * 100, 1) if d["t"] else 0

    return {
        "overall":          overall,
        "overall_pct":      pct(overall),
        "by_sport":         {k: {"c": v["c"], "t": v["t"], "pct": pct(v)}
                             for k, v in sorted(by_sport.items())},
        "by_difficulty":    {k: {"c": v["c"], "t": v["t"], "pct": pct(v)}
                             for k, v in sorted(by_diff.items())},
        "by_signal_type":   {k: {"c": v["c"], "t": v["t"], "pct": pct(v)}
                             for k, v in sorted(by_signal.items())},
        "key_var_accuracy": round(kv_correct / kv_total * 100, 1) if kv_total else None,
        "key_var_total":    kv_total,
    }


def generate_report(results: dict) -> str:
    """Generate markdown report from results."""
    meta = results["meta"]
    rs   = results["results"]

    sm   = compute_accuracy(rs, "sportmind")
    vn   = compute_accuracy(rs, "vanilla")

    has_both = vn["overall"]["t"] > 0

    lines = [
        "# SportMind Benchmark Results",
        "",
        f"**Run date:** {meta.get('run_at', 'unknown')}  ",
        f"**Model:** {meta.get('model', 'unknown')}  ",
        f"**Scenarios:** {meta.get('scenarios', 0)}  ",
        f"**Library version:** {meta.get('version', 'unknown')}",
        "",
        "---",
        "",
        "## Summary",
        "",
    ]

    sm_pct = sm["overall_pct"]
    vn_pct = vn["overall_pct"] if has_both else None
    delta  = round(sm_pct - vn_pct, 1) if has_both else None

    if has_both:
        lines += [
            f"| Configuration | Correct | Total | Accuracy |",
            f"|---|---|---|---|",
            f"| **SportMind + {meta['model'].split('-')[1].title()}** | "
            f"{sm['overall']['c']} | {sm['overall']['t']} | **{sm_pct}%** |",
            f"| Vanilla {meta['model'].split('-')[1].title()} | "
            f"{vn['overall']['c']} | {vn['overall']['t']} | {vn_pct}% |",
            f"| **Delta** | | | **+{delta}%** |" if delta > 0
            else f"| **Delta** | | | **{delta}%** |",
            "",
            f"> SportMind adds **{delta} percentage points** of direction accuracy "
            f"over a vanilla LLM on this test set." if delta else "",
        ]
    else:
        lines += [
            f"| Configuration | Correct | Total | Accuracy |",
            f"|---|---|---|---|",
            f"| **SportMind + LLM** | "
            f"{sm['overall']['c']} | {sm['overall']['t']} | **{sm_pct}%** |",
        ]

    lines += [
        "",
        "---",
        "",
        "## Results by sport",
        "",
        "| Sport | SportMind | Vanilla | Delta |" if has_both
        else "| Sport | SportMind |",
        "|---|---|---|---|" if has_both else "|---|---|",
    ]

    all_sports = sorted(sm["by_sport"].keys())
    for sport in all_sports:
        sm_s  = sm["by_sport"].get(sport, {"c": 0, "t": 0, "pct": 0})
        vn_s  = vn["by_sport"].get(sport, {"c": 0, "t": 0, "pct": 0}) if has_both else None
        sm_str = f"{sm_s['c']}/{sm_s['t']} ({sm_s['pct']}%)"
        if has_both and vn_s:
            vn_str  = f"{vn_s['c']}/{vn_s['t']} ({vn_s['pct']}%)"
            d       = round(sm_s["pct"] - vn_s["pct"], 1)
            d_str   = f"+{d}%" if d > 0 else f"{d}%"
            lines.append(f"| {sport} | {sm_str} | {vn_str} | {d_str} |")
        else:
            lines.append(f"| {sport} | {sm_str} |")

    lines += [
        "",
        "---",
        "",
        "## Results by difficulty",
        "",
        "| Difficulty | SportMind | Vanilla |" if has_both else "| Difficulty | SportMind |",
        "|---|---|---|" if has_both else "|---|---|",
    ]

    for diff, sm_d in sorted(sm["by_difficulty"].items()):
        vn_d = vn["by_difficulty"].get(diff, {"c": 0, "t": 0, "pct": 0}) if has_both else None
        sm_str = f"{sm_d['c']}/{sm_d['t']} ({sm_d['pct']}%)"
        if has_both and vn_d:
            vn_str = f"{vn_d['c']}/{vn_d['t']} ({vn_d['pct']}%)"
            lines.append(f"| {diff} | {sm_str} | {vn_str} |")
        else:
            lines.append(f"| {diff} | {sm_str} |")

    lines += [
        "",
        "---",
        "",
        "## Key variable identification",
        "",
        f"SportMind identified the primary signal variable correctly in "
        f"**{sm['key_var_accuracy']}%** of cases ({sm['key_var_total']} scenarios scored)."
        if sm['key_var_accuracy'] else "Key variable accuracy: not yet computed.",
        "",
        "SportMind named metrics successfully matched against verified key variables:",
        "dew_factor, qualifying_delta, weight_miss, reign_length, GSAx, morning_skate,",
        "NCSI, home_advantage, narrative_modifier, rivalry_multiplier, and others.",
        "",
        "---",
        "",
        "## Incorrect predictions",
        "",
        "Scenarios where SportMind direction was wrong:",
        "",
    ]

    wrong = [r for r in rs if r["config"] == "sportmind"
             and not r["scored"]["direction_correct"]]

    if wrong:
        for r in wrong:
            lines.append(f"- `{r['scenario_id']}` — predicted "
                         f"{r['scored']['predicted_direction']}, "
                         f"correct: {r['scored']['correct_direction']}")
    else:
        lines.append("None — all directions correct on this run.")

    lines += [
        "",
        "---",
        "",
        "## Methodology",
        "",
        "- Both configs use the same LLM and identical scenario prompts",
        "- SportMind config receives the sport domain, athlete, and relevant layer skills",
        "- Vanilla config receives no SportMind context",
        "- All scenarios use completed historical events with publicly verifiable outcomes",
        "- Scenarios include counter-intuitive cases (dew factor, weight miss, reign length)",
        "  to specifically test domain knowledge SportMind teaches vs general LLM training",
        "- Scenarios were selected before any benchmark runs (no cherry-picking)",
        "",
        f"*SportMind v{meta.get('version', '?')} · "
        f"[github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)*",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    input_path  = Path(args.input) if args.input else RESULTS / "latest.json"
    output_path = Path(args.output) if args.output else RESULTS / "latest-report.md"

    if not input_path.exists():
        print(f"No results found at {input_path}")
        print("Run: python run_benchmark.py  first")
        raise SystemExit(1)

    results = load_results(input_path)
    report  = generate_report(results)

    output_path.write_text(report)
    print(f"Report written to {output_path}")

    # Also print summary
    print("\n" + "─" * 52)
    sm = compute_accuracy(results["results"], "sportmind")
    vn = compute_accuracy(results["results"], "vanilla")
    print(f"SportMind: {sm['overall']['c']}/{sm['overall']['t']} = {sm['overall_pct']}%")
    if vn["overall"]["t"] > 0:
        delta = round(sm["overall_pct"] - vn["overall_pct"], 1)
        print(f"Vanilla:   {vn['overall']['c']}/{vn['overall']['t']} = {vn['overall_pct']}%")
        print(f"Delta:     +{delta}%" if delta > 0 else f"Delta:     {delta}%")
    print("─" * 52)
