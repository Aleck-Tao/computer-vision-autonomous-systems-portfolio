"""
Safety-check module for structured UAV mission plans.

The goal is to demonstrate safety-aware mission validation before action execution.
This is a representative template for research discussion and is not flight-control software.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


SAFETY_LIMITS = {
    "min_clearance_m": 0.75,
    "max_clearance_m": 5.0,
    "allowed_speed_modes": {"low", "normal"},
}


def validate_mission(plan: Dict[str, Any]) -> List[str]:
    issues: List[str] = []

    clearance = float(plan.get("min_obstacle_clearance_m", 0.0))
    if clearance < SAFETY_LIMITS["min_clearance_m"]:
        issues.append(f"Obstacle clearance too low: {clearance:.2f} m")
    if clearance > SAFETY_LIMITS["max_clearance_m"]:
        issues.append(f"Obstacle clearance value unrealistic: {clearance:.2f} m")

    speed_mode = plan.get("speed_mode", "normal")
    if speed_mode not in SAFETY_LIMITS["allowed_speed_modes"]:
        issues.append(f"Unsafe or unsupported speed mode: {speed_mode}")

    if not plan.get("return_to_home_on_link_loss", False):
        issues.append("No return-to-home behaviour specified for communication link loss")

    if not plan.get("stop_on_low_lidar_confidence", False):
        issues.append("No stop behaviour specified for low LiDAR confidence")

    return issues


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_file = base / "sample_data" / "sample_mission_output.json"
    plan = json.loads(input_file.read_text(encoding="utf-8"))
    issues = validate_mission(plan)

    if issues:
        print("Mission requires review:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Mission passed the example safety checks.")


if __name__ == "__main__":
    main()
