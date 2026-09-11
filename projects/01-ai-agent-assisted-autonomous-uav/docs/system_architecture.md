# Mission and telemetry interfaces

The executable public components are the mission parser, contract checks and offline analysis tools. This page describes the interfaces for connecting them to a vehicle; the full perception-to-flight loop is an integration design.

| Interface | Input and output | Decision it supports |
|---|---|---|
| Mission parser | Constrained English request → mission fields and source text | What has been requested? |
| Contract checks | Fields → accepted/review and specific issues | Does the request satisfy the configured static policy? |
| Perception and navigation adapter | Camera/LiDAR estimates → timestamped state and uncertainty | Is the current scene estimate usable? |
| Runtime monitor | State, evidence age and link status → recommendation | Are the conditions needed for execution still satisfied? |
| Control adapter | Accepted objective and current constraints → vehicle command | Which action is currently feasible? |
| Post-test analysis | Sensor timestamps, estimated/reference trajectories and media → reports | Which parts of the recording support the conclusion? |

## Why keep the contract explicit?

The [parser](../scripts/mission_parser.py) uses keywords and patterns. Its output includes mission type, target, speed mode, clearance, two contingency flags and the source instruction. The [validator](../scripts/safety_checks.py) checks clearance range, allowed speed modes and required contingencies.

Changing a parser should not silently change those policy rules. However, field validity is only one part of acceptance: a correctly typed contract can still encode the wrong interpretation. Retaining the source text makes that mismatch inspectable.

## Where time enters the design

A measurement's value and its age answer different questions. A plausible clearance measured before an obstacle approach can no longer justify the same action after a delay. An integration therefore needs timestamps and freshness limits alongside values, and should record both the recommendation and the action actually taken.

The [multisensor analysis](../../03-slam-perception-visualization-debugging-tools/) checks the input logs. The separate [runtime assurance project](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) studies persistence and stale evidence with synthetic replay. Those results inform the interface design; replay recommendations alone do not measure vehicle recovery.
