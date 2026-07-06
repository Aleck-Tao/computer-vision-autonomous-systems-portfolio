"""
Representative text-to-mission parser for an AI-agent-assisted UAV project.

This script is intentionally simple and transparent. It does not claim to be a
trained VLA model. It demonstrates how a natural-language mission instruction can
be converted into a structured mission plan that can later be checked by a safety
module or replaced by an LLM/VLA component.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
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
    plan = MissionPlan(source_instruction=text)

    if "corridor" in lower:
        plan.target_area = "corridor"
    elif "target area" in lower:
        plan.target_area = "target_area"
    elif "indoor" in lower or "test area" in lower:
        plan.target_area = "indoor_test_area"

    if "search" in lower:
        plan.mission_type = "search"
    elif "inspect" in lower:
        plan.mission_type = "inspection"
    elif "move" in lower:
        plan.mission_type = "navigation"

    if "low speed" in lower or "slow" in lower:
        plan.speed_mode = "low"
    elif "fast" in lower:
        plan.speed_mode = "high"

    if "avoid" in lower or "obstacle" in lower:
        plan.min_obstacle_clearance_m = parse_clearance(text)

    if "link" in lower or "communication" in lower or "starlink" in lower:
        if "unstable" in lower or "loss" in lower or "lost" in lower:
            plan.return_to_home_on_link_loss = True

    if "low lidar confidence" in lower or "confidence is low" in lower:
        plan.stop_on_low_lidar_confidence = True

    if "report" in lower or "describe" in lower or "generate" in lower:
        plan.report_required = True

    return plan


def main() -> None:
    input_file = Path(__file__).resolve().parents[1] / "sample_data" / "sample_mission_commands.txt"
    output_file = Path(__file__).resolve().parents[1] / "sample_data" / "parsed_mission_examples.json"

    commands = [line.strip() for line in input_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    parsed = [asdict(parse_instruction(command)) for command in commands]

    output_file.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
    print(f"Parsed {len(parsed)} mission command(s). Output written to {output_file}")


if __name__ == "__main__":
    main()
