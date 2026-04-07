#!/usr/bin/env python3
"""
SportMind calibration aggregator.
Processes community outcome records and produces modifier accuracy reports.

Called monthly to assess whether modifier ranges need updating.
Results feed into the 5-step calibration workflow (core/calibration-framework.md).

Usage:
    python scripts/calibration_aggregate.py --sport football
    python scripts/calibration_aggregate.py --all
    python scripts/calibration_aggregate.py --report --output calibration_report.json

See core/calibration-framework.md for the full calibration methodology.
See community/calibration-data/ for outcome record submissions.
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

CALIBRATION_DIR = Path("community/calibration-data")
CALIBRATION_TARGETS = {
    "athlete_modifier": {"direction_accuracy_target": 0.70, "min_events": 100},
    "macro_modifier":   {"direction_accuracy_target": 0.70, "min_events": 200},
    "dew_modifier":     {"direction_accuracy_target": 0.70, "min_events": 50},
    "rivalry_form_discount": {"direction_accuracy_target": 0.65, "min_events": 50},
    "narrative_modifier": {"direction_accuracy_target": 0.65, "min_events": 100},
}

# Confidence tier calibration targets (from calibration-framework.md)
TIER_TARGETS = {
    "HIGH":   0.72,
    "MEDIUM": 0.58,
    "LOW":    0.48,
}


def load_outcome_records(sport: str = None) -> list:
    """Load all outcome records from calibration-data directory."""
    records = []

    if not CALIBRATION_DIR.exists():
        print(f"WARNING: {CALIBRATION_DIR} does not exist.")
        return records

    pattern = "**/*.json"
    for json_file in sorted(CALIBRATION_DIR.glob(pattern)):
        # Filter by sport if specified
        if sport and sport not in str(json_file):
            continue

        try:
            with open(json_file) as f:
                data = json.load(f)
            if "outcome_record" in data:
                data["outcome_record"]["_source_file"] = str(json_file)
                records.append(data["outcome_record"])
        except (json.JSONDecodeError, KeyError) as e:
            print(f"WARNING: Could not parse {json_file}: {e}")

    return records


def calculate_direction_accuracy(records: list) -> dict:
    """Calculate direction accuracy across all records and by sport."""
    total = len(records)
    if total == 0:
        return {"total_records": 0, "message": "No records found"}

    correct = sum(1 for r in records
                  if r.get("outcome", {}).get("direction_correct", False))

    by_sport = defaultdict(lambda: {"correct": 0, "total": 0})
    for r in records:
        sport = r.get("sport", "unknown")
        by_sport[sport]["total"] += 1
        if r.get("outcome", {}).get("direction_correct", False):
            by_sport[sport]["correct"] += 1

    by_tier = defaultdict(lambda: {"correct": 0, "total": 0})
    for r in records:
        tier = r.get("prediction", {}).get("confidence_tier", "UNKNOWN")
        by_tier[tier]["total"] += 1
        if r.get("outcome", {}).get("direction_correct", False):
            by_tier[tier]["correct"] += 1

    return {
        "total_records": total,
        "overall_direction_accuracy": round(correct / total, 3),
        "by_sport": {
            sport: {
                "accuracy": round(v["correct"] / v["total"], 3),
                "correct": v["correct"],
                "total": v["total"]
            }
            for sport, v in by_sport.items()
        },
        "by_confidence_tier": {
            tier: {
                "accuracy": round(v["correct"] / v["total"], 3) if v["total"] > 0 else None,
                "correct": v["correct"],
                "total": v["total"],
                "target": TIER_TARGETS.get(tier),
                "calibrated": (
                    abs((v["correct"] / v["total"]) - TIER_TARGETS.get(tier, 0.6)) < 0.10
                    if v["total"] >= 10 else None
                )
            }
            for tier, v in by_tier.items()
        }
    }


def calculate_modifier_accuracy(records: list) -> dict:
    """Calculate accuracy for each modifier type."""
    modifier_results = defaultdict(lambda: {
        "direction_correct": 0, "total": 0,
        "magnitude_errors": [], "validated": []
    })

    for r in records:
        flags = r.get("calibration_flags", {})
        key_modifier = flags.get("key_modifier_validated")
        if not key_modifier:
            continue

        mr = modifier_results[key_modifier]
        mr["total"] += 1

        if flags.get("modifier_direction_correct"):
            mr["direction_correct"] += 1

        mag_error = flags.get("modifier_magnitude_error")
        if mag_error is not None:
            mr["magnitude_errors"].append(abs(float(mag_error)))

    results = {}
    for modifier, data in modifier_results.items():
        total = data["total"]
        if total == 0:
            continue

        direction_acc = round(data["direction_correct"] / total, 3)
        mean_mag_error = (
            round(sum(data["magnitude_errors"]) / len(data["magnitude_errors"]), 3)
            if data["magnitude_errors"] else None
        )

        target = CALIBRATION_TARGETS.get(modifier, {})
        min_events = target.get("min_events", 100)
        acc_target = target.get("direction_accuracy_target", 0.70)

        results[modifier] = {
            "total_events": total,
            "direction_accuracy": direction_acc,
            "direction_accuracy_target": acc_target,
            "mean_magnitude_error": mean_mag_error,
            "calibrated": direction_acc >= acc_target if total >= min_events else None,
            "min_events_required": min_events,
            "events_until_first_calibration": max(0, min_events - total),
            "status": (
                "CALIBRATED" if (total >= min_events and direction_acc >= acc_target)
                else "BELOW_TARGET" if (total >= min_events and direction_acc < acc_target)
                else f"INSUFFICIENT_DATA ({total}/{min_events} events)"
            )
        }

    return results


def generate_report(records: list) -> dict:
    """Generate a full calibration report."""
    return {
        "report_generated": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "schema_version": "1.0",
        "summary": {
            "total_outcome_records": len(records),
            "sports_covered": list(set(r.get("sport", "unknown") for r in records)),
            "seed_records": sum(1 for r in records if "seed record" in r.get("source", "")),
            "community_records": sum(1 for r in records if "seed record" not in r.get("source", ""))
        },
        "direction_accuracy": calculate_direction_accuracy(records),
        "modifier_accuracy": calculate_modifier_accuracy(records),
        "calibration_actions_needed": [],
        "next_review_date": "Monthly — see core/calibration-framework.md"
    }


def main():
    parser = argparse.ArgumentParser(description="SportMind calibration aggregator")
    parser.add_argument("--sport", help="Filter to specific sport")
    parser.add_argument("--all", action="store_true", help="Process all sports")
    parser.add_argument("--report", action="store_true", help="Generate full report")
    parser.add_argument("--output", help="Save report to file")
    args = parser.parse_args()

    sport = args.sport if not args.all else None
    records = load_outcome_records(sport)

    if not records:
        print(f"No outcome records found in {CALIBRATION_DIR}")
        print("Submit outcome records to build calibration data.")
        print("See community/calibration-data/README.md for instructions.")
        return 0

    print(f"\nSportMind Calibration Aggregator")
    print(f"{'=' * 50}")
    print(f"Records loaded: {len(records)}")

    report = generate_report(records)

    if args.report or args.output:
        report_json = json.dumps(report, indent=2)

        if args.output:
            Path(args.output).write_text(report_json)
            print(f"Report saved to {args.output}")
        else:
            print(report_json)
    else:
        # Summary output
        acc = report["direction_accuracy"]
        print(f"\nDirection accuracy: {acc.get('overall_direction_accuracy', 'N/A')}")
        print(f"\nBy sport:")
        for sport_name, data in acc.get("by_sport", {}).items():
            print(f"  {sport_name}: {data['accuracy']} ({data['correct']}/{data['total']})")

        print(f"\nBy confidence tier:")
        for tier, data in acc.get("by_confidence_tier", {}).items():
            target = data.get("target", "N/A")
            cal = data.get("calibrated")
            status = "✓" if cal else "✗" if cal is False else "?"
            print(f"  {tier}: {data['accuracy']} (target: {target}) {status}")

        mod = report["modifier_accuracy"]
        if mod:
            print(f"\nModifier accuracy:")
            for mod_name, data in mod.items():
                print(f"  {mod_name}: {data['status']}")

    print(f"\nFor calibration workflow: see core/calibration-framework.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
