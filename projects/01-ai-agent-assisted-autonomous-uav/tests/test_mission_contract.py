from __future__ import annotations

import unittest
from dataclasses import asdict

from scripts.mission_parser import parse_clearance, parse_instruction
from scripts.safety_checks import validate_mission


class MissionContractTests(unittest.TestCase):
    def test_parser_extracts_explicit_constraints(self) -> None:
        plan = parse_instruction(
            "Inspect the corridor at low speed, keep 1.5 metres from obstacles, "
            "return if the link is lost, stop if LiDAR confidence is low, and generate a report."
        )
        self.assertEqual(plan.target_area, "corridor")
        self.assertEqual(plan.speed_mode, "low")
        self.assertEqual(plan.min_obstacle_clearance_m, 1.5)
        self.assertTrue(plan.return_to_home_on_link_loss)
        self.assertTrue(plan.stop_on_low_lidar_confidence)
        self.assertTrue(plan.report_required)
        self.assertEqual(validate_mission(asdict(plan)), [])

    def test_unsafe_contract_is_blocked_for_multiple_reasons(self) -> None:
        plan = parse_instruction("Move fast and keep 0.4 m from the obstacle.")
        issues = validate_mission(asdict(plan))
        self.assertTrue(any("clearance too low" in issue for issue in issues))
        self.assertTrue(any("speed mode" in issue for issue in issues))
        self.assertTrue(any("link loss" in issue for issue in issues))
        self.assertTrue(any("LiDAR confidence" in issue for issue in issues))

    def test_clearance_parser_supports_metric_variants(self) -> None:
        self.assertEqual(parse_clearance("maintain 2 metres clearance"), 2.0)
        self.assertEqual(parse_clearance("maintain 0.75 m clearance"), 0.75)


if __name__ == "__main__":
    unittest.main()
