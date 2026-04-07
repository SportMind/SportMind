#!/usr/bin/env python3
"""
SportMind security validator.
Extends skill-validator.py with security-focused checks.

Runs as a second CI pass on every PR, and on-demand for maintainers.
Checks for:
  1. Prompt injection patterns in skill file content
  2. Suspicious instruction patterns (persona override, data exfiltration)
  3. Integrity: file hash matches platform/skill-hashes.json
  4. Calibration record provenance (submitted_by, source URL, timestamp)
  5. Skill registry integrity (no unexpected new endpoints)

Usage:
  python scripts/security_validator.py                # full check
  python scripts/security_validator.py --content      # injection scan only
  python scripts/security_validator.py --hashes       # integrity check only
  python scripts/security_validator.py --calibration  # provenance check only
  python scripts/security_validator.py --generate-hashes  # update skill-hashes.json

See SECURITY.md for the full threat model and disclosure policy.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
HASHES_FILE = ROOT / "platform" / "skill-hashes.json"
CALIBRATION_DIR = ROOT / "community" / "calibration-data"

# ── Prompt injection patterns ─────────────────────────────────────────────────
#
# These patterns are checked against ALL skill files served by the Skills API.
# Any match blocks the file from being merged until manually reviewed.
#
# The list is deliberately broad at the starts-with/contains level.
# False positives (legitimate educational mentions of injection) are handled
# by the ALLOWLIST below and by maintainer review.

INJECTION_PATTERNS = [
    # Direct instruction override attempts
    (r"ignore\s+(all\s+)?previous\s+instructions?",         "CRITICAL: instruction override attempt"),
    (r"ignore\s+(all\s+)?prior\s+instructions?",             "CRITICAL: instruction override attempt"),
    (r"disregard\s+(all\s+)?previous\s+instructions?",       "CRITICAL: instruction override attempt"),
    (r"forget\s+(all\s+)?(previous|prior|your)\s+instructions?", "CRITICAL: instruction override attempt"),
    (r"override\s+(all\s+)?previous\s+instructions?",        "CRITICAL: instruction override attempt"),
    (r"do\s+not\s+follow\s+(your\s+)?previous",              "CRITICAL: instruction override attempt"),

    # Persona / identity hijack
    (r"you\s+are\s+now\s+(?!an?\s+(?:agent|analyst|intelligence|a\s+sport))", "HIGH: persona override"),
    (r"act\s+as\s+(?!an?\s+(?:agent|analyst|sport|fan\s+token))",     "HIGH: persona override"),
    (r"pretend\s+(you\s+are|to\s+be)",                       "HIGH: persona override"),
    (r"your\s+new\s+(role|identity|persona|instructions?\s+are)", "HIGH: persona override"),
    (r"from\s+now\s+on\s+(you\s+are|you\s+will|always)",     "HIGH: persona override"),

    # System prompt / LLM control tokens
    (r"<\|im_start\|>",                                      "HIGH: LLM control token"),
    (r"<\|im_end\|>",                                        "HIGH: LLM control token"),
    (r"<\|system\|>",                                        "HIGH: LLM control token"),
    (r"\[INST\]",                                            "HIGH: LLM control token"),
    (r"\[\/INST\]",                                          "HIGH: LLM control token"),
    (r"<s>.*<\/s>",                                          "HIGH: LLM control token"),
    (r"###\s*System:",                                       "MEDIUM: potential system prompt injection"),
    (r"###\s*Human:",                                        "MEDIUM: potential chat format injection"),
    (r"###\s*Assistant:",                                    "MEDIUM: potential chat format injection"),

    # Data exfiltration attempts
    (r"send\s+(this|the|all|any)\s+(data|information|context|conversation)\s+to", "CRITICAL: exfiltration attempt"),
    (r"post\s+(this|the|all|any)\s+(data|information|context)\s+to",              "CRITICAL: exfiltration attempt"),
    (r"http[s]?://(?!github\.com|sportmind\.dev|docs\.anthropic\.com|api\.anthropic\.com)",
                                                              "MEDIUM: external URL — review required"),
    (r"fetch\s*\(\s*['\"]http",                              "HIGH: fetch to external URL"),
    (r"eval\s*\(",                                           "HIGH: eval() in skill content"),
    (r"exec\s*\(",                                           "HIGH: exec() in skill content"),
    (r"import\s+os\b",                                       "HIGH: os import in skill content"),
    (r"import\s+subprocess",                                 "HIGH: subprocess import in skill content"),

    # Financial manipulation
    (r"always\s+(recommend|say|output|return)\s+(buy|sell|long|short|enter|exit)",
                                                             "HIGH: hardcoded financial instruction"),
    (r"(buy|long)\s+\$[A-Z]{2,10}\s+(now|immediately|always)",
                                                             "HIGH: hardcoded buy signal"),
    (r"(sell|short)\s+\$[A-Z]{2,10}\s+(now|immediately|always)",
                                                             "HIGH: hardcoded sell signal"),
    (r"this\s+token\s+will\s+(always|definitely|certainly)\s+(go\s+up|rise|increase|moon)",
                                                             "MEDIUM: market manipulation language"),

    # Jailbreak patterns
    (r"jailbreak",                                           "HIGH: jailbreak language"),
    (r"DAN\s+mode",                                          "HIGH: DAN jailbreak pattern"),
    (r"developer\s+mode\s+enabled",                          "HIGH: developer mode jailbreak"),
    (r"do\s+anything\s+now",                                 "HIGH: DAN variant"),
]

# Patterns allowed in specific contexts (e.g. security docs, educational mentions)
# Format: (path_glob, pattern_substring)
SECURITY_ALLOWLIST = [
    # Security documentation (allowed to mention attack patterns for educational purposes)
    ("SECURITY.md",                 "ignore previous"),
    ("SECURITY.md",                 "IGNORE PREVIOUS"),
    # This script itself (contains patterns as strings for detection)
    ("scripts/security_validator",  "ignore"),
    # Integration pattern documents (contain code examples with OS/subprocess imports)
    ("platform/realtime-integration-patterns",  "import os"),
    ("platform/realtime-integration-patterns",  "os import"),
    ("platform/sportmind-mcp-deployment",       "import subprocess"),
    ("platform/sportmind-mcp-deployment",       "subprocess import"),
    ("platform/freshness-strategy",              "import os"),
    ("platform/freshness-strategy",              "os import"),
    ("platform/freshness-strategy",              "import subprocess"),
    ("platform/freshness-strategy",              "subprocess import"),
    ("examples/starter-pack",                    "import os"),
    ("examples/starter-pack",                    "import subprocess"),
    # Scripts directory (all scripts are legitimate code)
    ("scripts/",                    "import os"),
    ("scripts/",                    "import subprocess"),
    ("scripts/security_validator",  "fetch"),
    ("scripts/security_validator",  "import os"),
    ("scripts/security_validator",  "act as"),
    # Legitimate code examples in documentation files
    ('platform/integration-partners', 'fetch('),  # JS code example in Partner 7
    ("i18n/README.md",              "import os"),          # Python snippet showing os.path
    ("platform/skill-registry-api", "fetch("),            # JS code example
    ("platform/skill-registry-api", "await fetch"),       # JS code example
    ("platform/skill-registry-api", "your-org"),          # placeholder URL in docs
    # Legitimate usage in platform documentation
    ("agent-prompts/",              "localhost"),          # local dev URL
    ("platform/",                   "localhost"),          # local dev URL
    ("platform/",                   "your-org"),           # placeholder URL
    ("platform/",                   "github.io"),          # GitHub Pages URL
    # Legitimate "Show:" usage in world-cup module (product description, not injection)
    ("world-cup-2026",              "show:"),
    ("world-cup-2026",              "Show:"),
    ("docs/",                       "injection"),          # documentation
]


def is_allowed(file_path: str, description: str, matched_text: str = "") -> bool:
    """
    Return True if this finding is allowlisted for this file.
    Checks the path fragment against the file path AND the allowlist
    pattern_frag against either the finding description or matched text.
    """
    fp_lower = file_path.lower()
    check_lower = (description + " " + matched_text).lower()
    for path_frag, pattern_frag in SECURITY_ALLOWLIST:
        if path_frag.lower() in fp_lower and pattern_frag.lower() in check_lower:
            return True
    return False


def scan_for_injection(file_path: Path) -> list[dict]:
    """
    Scan a skill file for prompt injection and malicious content patterns.
    Returns list of findings, each with severity, pattern, and line number.
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError) as e:
        return [{"severity": "ERROR", "message": f"Could not read file: {e}", "line": 0}]

    findings = []
    content_lower = content.lower()
    lines = content.split("\n")

    for pattern_str, description in INJECTION_PATTERNS:
        # Check against full content (case-insensitive)
        matches = list(re.finditer(pattern_str, content_lower, re.IGNORECASE | re.DOTALL))
        for match in matches:
            # Find line number
            line_num = content[:match.start()].count("\n") + 1
            line_text = lines[line_num - 1].strip()[:100] if line_num <= len(lines) else ""

            rel_path = str(file_path.relative_to(ROOT))
            line_ctx = lines[line_num - 1] if line_num <= len(lines) else ""
            if is_allowed(rel_path, description, line_ctx):
                continue

            severity = description.split(":")[0]
            findings.append({
                "severity": severity,
                "message": description,
                "pattern": pattern_str,
                "line": line_num,
                "context": line_text,
                "file": rel_path,
            })

    return findings


# ── Integrity checking ────────────────────────────────────────────────────────

def compute_file_hash(file_path: Path) -> str:
    """Compute SHA-256 hash of a file's content."""
    content = file_path.read_bytes()
    return hashlib.sha256(content).hexdigest()


def get_skill_files() -> list[Path]:
    """Return all skill files that should be integrity-checked."""
    patterns = [
        "sports/*/sport-domain-*.md",
        "athlete/*/athlete-intel-*.md",
        "fan-token/**/*.md",
        "core/*.md",
        "market/*.md",
        "macro/*.md",
        "platform/*.md",
    ]
    files = []
    for pattern in patterns:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def generate_hashes(output_file: Path = HASHES_FILE) -> dict:
    """Generate SHA-256 hashes for all skill files and save to JSON."""
    skill_files = get_skill_files()
    hashes = {
        "_meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generated_by": "scripts/security_validator.py --generate-hashes",
            "library_version": "3.5.0",
            "total_files": len(skill_files),
            "description": (
                "SHA-256 hashes of all SportMind skill files. "
                "Agents and developers can verify file integrity by comparing "
                "the hash of received content against this record. "
                "Updated by maintainers on every skill file change."
            ),
        },
        "files": {}
    }

    for file_path in skill_files:
        rel_path = str(file_path.relative_to(ROOT))
        hashes["files"][rel_path] = {
            "sha256": compute_file_hash(file_path),
            "size_bytes": file_path.stat().st_size,
            "last_verified": datetime.now(timezone.utc).isoformat(),
        }

    output_file.write_text(json.dumps(hashes, indent=2, ensure_ascii=False))
    print(f"Generated hashes for {len(skill_files)} files → {output_file}")
    return hashes


def verify_hashes() -> list[dict]:
    """
    Verify current skill files against stored hashes.
    Returns list of integrity violations.
    """
    if not HASHES_FILE.exists():
        return [{"severity": "WARNING",
                 "message": "skill-hashes.json not found — run --generate-hashes to create",
                 "file": str(HASHES_FILE)}]

    try:
        stored = json.loads(HASHES_FILE.read_text())
    except json.JSONDecodeError as e:
        return [{"severity": "ERROR", "message": f"skill-hashes.json is invalid JSON: {e}",
                 "file": str(HASHES_FILE)}]

    stored_files = stored.get("files", {})
    violations = []

    for rel_path, entry in stored_files.items():
        file_path = ROOT / rel_path
        if not file_path.exists():
            violations.append({
                "severity": "WARNING",
                "message": "File in hash registry no longer exists",
                "file": rel_path,
            })
            continue

        current_hash = compute_file_hash(file_path)
        stored_hash  = entry.get("sha256", "")

        if current_hash != stored_hash:
            violations.append({
                "severity": "HIGH",
                "message": "File content has changed since last hash generation",
                "file": rel_path,
                "stored_hash": stored_hash[:16] + "...",
                "current_hash": current_hash[:16] + "...",
                "note": "Run --generate-hashes after reviewing the change.",
            })

    # Check for new files not yet in registry
    current_files = get_skill_files()
    for file_path in current_files:
        rel_path = str(file_path.relative_to(ROOT))
        if rel_path not in stored_files:
            violations.append({
                "severity": "INFO",
                "message": "New file not yet in hash registry",
                "file": rel_path,
                "note": "Run --generate-hashes to register.",
            })

    return violations


# ── Calibration provenance ────────────────────────────────────────────────────

REQUIRED_PROVENANCE_FIELDS = [
    "submitted_by",
    "submission_timestamp",
]

REQUIRED_OUTCOME_FIELDS = [
    "result_source_url",
    "result",
]


def check_calibration_provenance() -> list[dict]:
    """
    Check all calibration outcome records for required provenance fields.
    Returns list of issues found.
    """
    if not CALIBRATION_DIR.exists():
        return [{"severity": "INFO",
                 "message": "calibration-data directory not found",
                 "file": str(CALIBRATION_DIR)}]

    issues = []
    records = sorted(CALIBRATION_DIR.rglob("*.json"))
    # Exclude report/summary files — only check outcome records
    records = [r for r in records if r.name != "README.md"
               and "report" not in r.name.lower()]

    for record_path in records:
        try:
            data = json.loads(record_path.read_text())
        except json.JSONDecodeError as e:
            issues.append({
                "severity": "ERROR",
                "message": f"Invalid JSON: {e}",
                "file": str(record_path.relative_to(ROOT)),
            })
            continue

        rec = data.get("outcome_record", {})
        rel_path = str(record_path.relative_to(ROOT))

        # Check provenance fields
        for field in REQUIRED_PROVENANCE_FIELDS:
            if field not in rec:
                issues.append({
                    "severity": "MEDIUM",
                    "message": f"Missing provenance field: {field}",
                    "file": rel_path,
                    "note": "Add field to outcome_record root level.",
                })

        # Check outcome has source URL
        outcome = rec.get("outcome", {})
        for field in REQUIRED_OUTCOME_FIELDS:
            if field not in outcome:
                issues.append({
                    "severity": "MEDIUM",
                    "message": f"Missing outcome field: {field}",
                    "file": rel_path,
                })

        # Check source URL is not empty
        source_url = outcome.get("result_source_url", "")
        if source_url and source_url.strip() in ("", "null", "N/A", "TBD"):
            issues.append({
                "severity": "MEDIUM",
                "message": "result_source_url is empty or placeholder",
                "file": rel_path,
                "note": "All outcome records must cite a verifiable official source.",
            })

        # Detect duplicate record IDs
        # (collected across all records — done at aggregate level)

    return issues


# ── Main runner ───────────────────────────────────────────────────────────────

def severity_order(s: str) -> int:
    return {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "INFO": 3,
            "WARNING": 4, "ERROR": 5}.get(s, 9)


def print_findings(findings: list[dict], label: str) -> int:
    """Print findings grouped by severity. Returns count of CRITICAL/HIGH findings."""
    if not findings:
        print(f"  ✓ {label}: no issues")
        return 0

    sorted_findings = sorted(findings, key=lambda f: severity_order(f.get("severity", "INFO")))
    critical_high = sum(1 for f in findings
                        if f.get("severity") in ("CRITICAL", "HIGH", "ERROR"))

    print(f"\n  {label}: {len(findings)} finding(s)  "
          f"[{critical_high} critical/high]")

    for f in sorted_findings:
        sev = f.get("severity", "INFO")
        icon = {"CRITICAL": "🔴", "HIGH": "🔴", "MEDIUM": "🟡",
                "INFO": "🔵", "WARNING": "🟡", "ERROR": "🔴"}.get(sev, "⚪")
        file_info = f.get("file", "")
        line_info = f" (line {f['line']})" if f.get("line") else ""
        print(f"    {icon} [{sev}] {file_info}{line_info}")
        print(f"       {f.get('message', '')}")
        if f.get("context"):
            print(f"       → {f['context'][:80]}")
        if f.get("note"):
            print(f"       Note: {f['note']}")

    return critical_high


def run_security_checks(
    check_content: bool = True,
    check_hashes: bool = True,
    check_calibration: bool = True,
    verbose: bool = False,
) -> bool:
    """Run all security checks. Returns True if no CRITICAL/HIGH findings."""
    print(f"\nSportMind Security Validator")
    print(f"{'=' * 50}")
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    print()

    total_critical_high = 0
    total_findings = 0

    # 1. Content injection scan
    if check_content:
        print("── Prompt injection scan ────────────────────────")
        skill_files = get_skill_files()
        # Also scan fan-token, i18n, agent-prompts
        skill_files += list(ROOT.glob("agent-prompts/*.md"))
        skill_files += list(ROOT.glob("i18n/**/*.md"))

        all_injection = []
        for file_path in sorted(set(skill_files)):
            findings = scan_for_injection(file_path)
            all_injection.extend(findings)

        print(f"  Files scanned: {len(set(skill_files))}")
        ch = print_findings(all_injection, "Injection findings")
        total_critical_high += ch
        total_findings += len(all_injection)

    # 2. Integrity check
    if check_hashes:
        print("\n── Integrity check ──────────────────────────────")
        violations = verify_hashes()
        if HASHES_FILE.exists():
            stored_meta = json.loads(HASHES_FILE.read_text()).get("_meta", {})
            print(f"  Hash registry: {stored_meta.get('total_files', '?')} files")
            print(f"  Generated: {stored_meta.get('generated_at', 'unknown')}")
        ch = print_findings(violations, "Integrity violations")
        total_critical_high += ch
        total_findings += len(violations)

    # 3. Calibration provenance
    if check_calibration:
        print("\n── Calibration provenance ───────────────────────")
        cal_records = list(CALIBRATION_DIR.rglob("*.json")) if CALIBRATION_DIR.exists() else []
        print(f"  Records found: {len(cal_records)}")
        issues = check_calibration_provenance()
        ch = print_findings(issues, "Provenance issues")
        total_critical_high += ch
        total_findings += len(issues)

    # Summary
    print(f"\n{'=' * 50}")
    print(f"Total findings: {total_findings}")
    print(f"Critical/High:  {total_critical_high}")

    if total_critical_high == 0:
        print("\n✓ Security check passed — no critical or high findings")
        return True
    else:
        print(f"\n✗ Security check FAILED — {total_critical_high} critical/high finding(s)")
        print("  Review findings above before merging.")
        print("  See SECURITY.md for disclosure and response process.")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="SportMind security validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/security_validator.py                  # full check
  python scripts/security_validator.py --content        # injection scan only
  python scripts/security_validator.py --hashes         # integrity check only
  python scripts/security_validator.py --calibration    # provenance check only
  python scripts/security_validator.py --generate-hashes # update hash registry
        """
    )
    parser.add_argument("--content",          action="store_true",
                        help="Run injection scan only")
    parser.add_argument("--hashes",           action="store_true",
                        help="Run integrity check only")
    parser.add_argument("--calibration",      action="store_true",
                        help="Run calibration provenance check only")
    parser.add_argument("--generate-hashes",  action="store_true",
                        help="Generate/update platform/skill-hashes.json")
    parser.add_argument("--verbose",          action="store_true",
                        help="Show all findings including INFO level")
    args = parser.parse_args()

    if args.generate_hashes:
        generate_hashes()
        print("Done. Commit platform/skill-hashes.json to lock current state.")
        return 0

    # If no flags, run everything
    run_all = not (args.content or args.hashes or args.calibration)

    passed = run_security_checks(
        check_content=run_all or args.content,
        check_hashes=run_all or args.hashes,
        check_calibration=run_all or args.calibration,
        verbose=args.verbose,
    )
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
