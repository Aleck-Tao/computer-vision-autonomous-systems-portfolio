# SLAM and Perception Visualization Debugging Tools

**Status:** Research-supporting workflow / project development  
**Keywords:** SLAM, LiDAR, stereo vision, trajectory plotting, timing diagnostics, perception debugging, autonomous systems, safety-critical validation

---

## Project Overview

This project presents visualization and diagnostic tools for autonomous-system perception and SLAM-style navigation debugging. The main idea is that autonomous systems should not be treated as black boxes. When failures occur, the researcher should be able to inspect trajectories, timestamps, sensor intervals, feature stability and logs.

This approach is relevant to autonomous driving and VLA research because safety-critical systems require interpretable validation and failure-mode analysis, not only aggregate benchmark scores.

---

## Repository Contents

| File | Purpose |
|---|---|
| `docs/debugging_checklist.md` | Practical checklist for SLAM/perception debugging |
| `docs/failure_mode_taxonomy.md` | Failure taxonomy for autonomous perception systems |
| `scripts/plot_trajectory_from_csv.py` | Plot trajectory data from CSV |
| `scripts/timing_diagnostics.py` | Analyse sensor timestamp intervals and jitter |
| `scripts/feature_track_debug_template.py` | OpenCV-style feature tracking template with graceful fallback |
| `sample_data/synthetic_trajectory.csv` | Synthetic trajectory data |
| `sample_data/sensor_timestamps.csv` | Synthetic sensor timestamp data |

---

## Example Debugging Questions

- Is trajectory drift increasing over time?
- Are sensor timestamps stable?
- Is one sensor stream delayed relative to another?
- Are perception failures linked to lighting or texture variation?
- Do failure cases occur before unsafe actions?
- Are logs sufficient to reproduce the issue?

---

## Relevance to VLA Systems

A VLA model may output an action, but a researcher still needs to understand why the action succeeded or failed. This project supports that need by emphasizing:

- interpretable trajectory analysis,
- timing diagnostics,
- failure-mode classification,
- reproducible plotting,
- safety-oriented validation.
