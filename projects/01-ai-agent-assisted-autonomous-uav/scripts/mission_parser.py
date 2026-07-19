"""Deterministic adapter from constrained mission language to a typed contract.

This parser is the transparent public adapter used to exercise the downstream
safety interface.  It is deliberately not presented as a trained VLA model: a
learned parser can replace it later without changing the validated contract.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass(frozen=True)
class MissionPlan:
    mission_type: str = "inspection"
    target_area: str = "unknown"
    speed_mode: str = "normal"
    min_obstacle_clearance_m: float = 1.0
    return_to_home_on_link_loss: bool = False
    stop_on_low_lidar_confidence: bool = False
    report_required: bool = False
    source_instruction: str = ""


def parse_clearance(text: str) -> float:
    """Extract a clearance value such as '1.5 metres' from text."""
    match = re.search(r"(\d+(?:\.\d+)?)\s*(?:m|meter|metre|meters|metres)", text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return 1.0


def parse_instruction(text: str) -> MissionPlan:
    lower = text.lower()
    mission_type = "inspection"
    target_area = "unknown"
    speed_mode = "normal"
    min_obstacle_clearance_m = 1.0
    return_to_home_on_link_loss = False
    stop_on_low_lidar_confidence = False
    report_required = False

    if "corridor" in lower:
        target_area = "corridor"
    elif "target area" in lower:
        target_area = "target_area"
    elif "indoor" in lower or "test area" in lower:
        target_area = "indoor_test_area"

    if "search" in lower:
        mission_type = "search"
    elif "inspect" in lower:
        mission_type = "inspection"
    elif "move" in lower:
        mission_type = "navigation"

    if "low speed" in lower or "slow" in lower:
        speed_mode = "low"
    elif "fast" in lower:
        speed_mode = "high"

    if "avoid" in lower or "obstacle" in lower:
        min_obstacle_clearance_m = parse_clearance(text)

    if "link" in lower or "communication" in lower or "starlink" in lower:
        if "unstable" in lower or "loss" in lower or "lost" in lower:
            return_to_home_on_link_loss = True

    if "low lidar confidence" in lower or "confidence is low" in lower:
        stop_on_low_lidar_confidence = True

    if "report" in lower or "describe" in lower or "generate" in lower:
        report_required = True

    return MissionPlan(
        mission_type=mission_type,
        target_area=target_area,
        speed_mode=speed_mode,
        min_obstacle_clearance_m=min_obstacle_clearance_m,
        return_to_home_on_link_loss=return_to_home_on_link_loss,
        stop_on_low_lidar_confidence=stop_on_low_lidar_confidence,
        report_required=report_required,
        source_instruction=text,
    )


def main() -> None:
    input_file = Path(__file__).resolve().parents[1] / "sample_data" / "sample_mission_commands.txt"
    output_file = Path(__file__).resolve().parents[1] / "sample_data" / "parsed_mission_examples.json"

    commands = [line.strip() for line in input_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    parsed = [asdict(parse_instruction(command)) for command in commands]

    output_file.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
    print(f"Parsed {len(parsed)} mission command(s). Output written to {output_file}")


if __name__ == "__main__":
    main()
