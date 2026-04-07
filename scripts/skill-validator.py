#!/usr/bin/env python3
"""
SportMind skill validator.
Checks all sport-domain and athlete-intel skill files against required structure.
Run: python scripts/skill-validator.py
Used by CI on every PR touching skills.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Required sections for sport domain skills — accepts common name variants
SPORT_REQUIRED_SECTIONS = [
    # (canonical name, [accepted variants])
    ("## Domain Model",         ["## Domain Model"]),
    ("## Event Playbooks",      ["## Event Playbooks"]),
    ("## Signal Weight",        ["## Signal Weight", "## Signal Weighting", 
                                  "## Signal Weight Adjustments", "## Signal Weights"]),
    ("## Key Commands",         ["## Key Commands", "## Commands", "## Fan Token Layer",
                                  "## Fan Token Notes", "## Fan Token Compatibility",
                                  "## Key Token Commands", "## Token Commands"]),
    ("## Agent Reasoning",      ["## Agent Reasoning Prompts", "## Agent Reasoning",
                                  "## Agent Reasoning Rules", "## Agent Rules"]),
    ("## Data Sources",         ["## Data Sources", "## Sources", "## Data Source"]),
    ("## Compatibility",        ["## Compatibility"]),
]

# Required sections for athlete skills — accepts common name variants
ATHLETE_REQUIRED_SECTIONS = [
    ("## Commands",             ["## Commands", "## Command list", "## Key Commands"]),
    ("## Command reference",    ["## Command reference", "## Command Reference",
                                  "## Commands reference"]),
    ("## Modifier reference",   ["## Modifier reference", "## Modifier Reference",
                                  "## Modifier table", "## Master modifier reference",
                                  "## Cricket modifier table", "## NBA modifier table",
                                  "## NFL modifier table", "## NHL modifier table",
                                  "## Key Player Composite Modifier"]),
    ("## Integration example",  ["## Integration example", "## Integration Example",
                                  "## Agent integration", "## Autopilot template",
                                  "## Integration"]),
]

# Accepted variants for each required playbook field
PLAYBOOK_FIELD_VARIANTS = {
    "trigger": ["trigger:"],
    "entry":   ["entry:", "action:", "signal:", "position:", "trade:"],
    "exit":    ["exit:", "close:", "take_profit:", "stop:"],
    "filter":  ["filter:", "condition:", "requires:", "pre_condition:"],
    "sizing":  ["sizing:", "size:", "position_size:", "scale:"],
}
PLAYBOOK_FIELDS = list(PLAYBOOK_FIELD_VARIANTS.keys())  # kept for reference

PLACEHOLDERS = [
    "[PLACEHOLDER]",
    "[Sport Name]",
    "[sport name]",
    "<!-- INSTRUCTIONS FOR CONTRIBUTORS",
    "TODO",
    "[Your GitHub handle]",
    "[Date]",
]

STUB_MARKER = "Status: 🔜"


def is_stub(content: str) -> bool:
    return STUB_MARKER in content or len(content.strip().split('\n')) <= 25


def has_section(content: str, variants: list) -> bool:
    """Return True if content contains any of the section name variants."""
    return any(v in content for v in variants)


def check_sport_skill(path: Path) -> list[str]:
    content = path.read_text()
    if is_stub(content):
        return []
    errors = []

    for canonical, variants in SPORT_REQUIRED_SECTIONS:
        if not has_section(content, variants):
            errors.append(f"Missing required section: {canonical} "
                          f"(checked variants: {', '.join(variants[:3])}{'...' if len(variants) > 3 else ''})")

    playbook_count = content.count("### Playbook")
    if playbook_count < 4:
        errors.append(f"Only {playbook_count} playbooks found — minimum 4 required")

    for i, block in enumerate(content.split("### Playbook")[1:], 1):
        if "```" in block:
            code_block = block.split("```")[1] if "```" in block else ""
            cb_lower = code_block.lower()
            missing = []
            for field, variants in PLAYBOOK_FIELD_VARIANTS.items():
                if not any(v in cb_lower for v in variants):
                    missing.append(field)
            if missing:
                errors.append(f"Playbook {i} missing fields: {', '.join(missing)}")

    return errors


def check_athlete_skill(path: Path) -> list[str]:
    content = path.read_text()
    if is_stub(content):
        return []
    errors = []

    for canonical, variants in ATHLETE_REQUIRED_SECTIONS:
        if not has_section(content, variants):
            errors.append(f"Missing required section: {canonical}")

    if "## Command reference" in content or any(v in content for v in 
       ["## Command Reference", "## Commands reference"]):
        ref_idx = max(content.find("## Command reference"),
                      content.find("## Command Reference"),
                      content.find("## Commands reference"))
        ref_section = content[ref_idx:]
        if "```json" not in ref_section:
            errors.append("Command reference must include JSON return examples (```json blocks)")

    if "get_athlete_signal_modifier" not in content:
        errors.append("Missing required command: get_athlete_signal_modifier")

    return errors


def check_placeholders(path: Path) -> list[str]:
    content = path.read_text()
    if is_stub(content):
        return []
    found = [p for p in PLACEHOLDERS if p in content]
    return [f"Unreplaced placeholder: {p}" for p in found]


# Required sections for fan-token bridge skills
BRIDGE_REQUIRED_SECTIONS = [
    ("## At a glance",      ["## At a glance", "## Overview", "## At a Glance"]),
    ("## Agent reasoning",  ["## Agent reasoning prompts", "## Agent reasoning",
                              "## Agent Reasoning Prompts", "## Agent Reasoning Rules",
                              "## Key agent reasoning rules", "## Key Agent Reasoning Rules"]),
    ("## Compatibility",    ["## Compatibility"]),
]


def check_bridge_skill(path: Path) -> list[str]:
    content = path.read_text()
    if is_stub(content):
        return []
    errors = []
    for canonical, variants in BRIDGE_REQUIRED_SECTIONS:
        if not has_section(content, variants):
            errors.append(f"Missing required section: {canonical}")
    # Must have at least one token impact score or metric defined
    has_score = any(term in content for term in [
        "TIS", "Score", "NASCARTIS", "PKLTIS", "NetTIS", "RLTIS",
        "HandTIS", "NFLTIS", "AFLTIS", "RugbyTIS", "MLBTIS", "NHLTIS",
        "MotoTIS", "FighterTIS", "FTIS", "OrgTIS", "NBATIS", "CricTIS",
    ])
    if not has_score:
        errors.append("Missing token impact score definition (e.g. NASCARTIS, PKLTIS)")
    return errors


def validate_all() -> bool:
    all_passed = True
    errors_by_file: dict = {}

    for skill_file in sorted(ROOT.glob("sports/*/sport-domain-*.md")):
        errors = check_sport_skill(skill_file) + check_placeholders(skill_file)
        if errors:
            errors_by_file[str(skill_file.relative_to(ROOT))] = errors

    for skill_file in sorted(ROOT.glob("athlete/*/athlete-intel-*.md")):
        errors = check_athlete_skill(skill_file) + check_placeholders(skill_file)
        if errors:
            errors_by_file[str(skill_file.relative_to(ROOT))] = errors

    for skill_file in sorted(ROOT.glob("fan-token/*/*-token-intelligence.md")):
        errors = check_bridge_skill(skill_file) + check_placeholders(skill_file)
        if errors:
            errors_by_file[str(skill_file.relative_to(ROOT))] = errors

    total_files = (
        len(list(ROOT.glob("sports/*/sport-domain-*.md"))) +
        len(list(ROOT.glob("athlete/*/athlete-intel-*.md"))) +
        len(list(ROOT.glob("fan-token/*/*-token-intelligence.md")))
    )
    error_count = sum(len(e) for e in errors_by_file.values())

    print(f"\nSportMind skill validation")
    print(f"{'=' * 50}")
    print(f"Files checked: {total_files}")
    print(f"Files with errors: {len(errors_by_file)}")
    print(f"Total errors: {error_count}")

    if errors_by_file:
        print("\nErrors found:")
        for file_path, errors in errors_by_file.items():
            print(f"\n  {file_path}")
            for error in errors:
                print(f"    ✗ {error}")
        all_passed = False
    else:
        print("\n✓ All skills passed validation")

    return all_passed


if __name__ == "__main__":
    passed = validate_all()
    sys.exit(0 if passed else 1)
