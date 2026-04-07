#!/usr/bin/env python3
"""
SportMind macro state updater.
Refreshes platform/macro-state.json with current market data.
Called by .github/workflows/macro-monitor.yml after signal checks.

The macro-state.json file is the lightweight session-start macro check
that agents read instead of loading full macro skill files.

See platform/live-signals.md (Category 1) for what agents do with this data.
See platform/monitoring-alerts.md for the full alert specification.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

MACRO_STATE_FILE = Path("platform/macro-state.json")


def update_timestamp() -> None:
    """Update the updated_at timestamp in macro-state.json."""
    try:
        with open(MACRO_STATE_FILE) as f:
            state = json.load(f)

        state["macro_state"]["updated_at"] = datetime.now(timezone.utc).isoformat()

        with open(MACRO_STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)

        print(f"macro-state.json updated at {state['macro_state']['updated_at']}")
        print(f"Current phase: {state['macro_state']['crypto_cycle'].get('phase', 'NEUTRAL')}")
        print(f"Current modifier: {state['macro_state']['crypto_cycle'].get('macro_modifier', 1.00)}")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"ERROR: Could not update macro-state.json: {e}")
        sys.exit(1)


if __name__ == "__main__":
    update_timestamp()
