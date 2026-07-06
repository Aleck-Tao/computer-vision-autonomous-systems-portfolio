# Failure-Mode Taxonomy for Autonomous Perception

| Failure category | Description | Example diagnostic signal |
|---|---|---|
| Timing mismatch | Sensors are not synchronized | high timestamp jitter or offset |
| Trajectory drift | Pose estimate gradually diverges | increasing path deviation |
| Feature instability | Visual features are not consistent | low feature-track length |
| Sparse depth / point data | Depth or LiDAR signal is insufficient | reduced point count |
| Lighting variation | Perception degrades under lighting changes | failure near overexposed region |
| Texture variation | Low-texture surface causes visual failure | few stable keypoints |
| Communication delay | Remote command/logging delay affects system | high latency or packet loss |
| Safety-policy gap | No clear action under uncertain perception | missing stop/return trigger |

## Research Use

For VLA/autonomous-driving research, this taxonomy can support systematic analysis of rare or novel scenarios. Rather than reporting only success/failure, each case can be mapped to a failure category and linked to sensor evidence.
