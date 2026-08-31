# PhD research-fit map

This map helps a prospective supervisor identify the shortest path from a research topic to inspectable evidence. It is not a claim that every listed direction is already a completed research contribution; it shows the implemented foundation from which a focused PhD project could begin.

| PhD direction | Demonstrated foundation | Best entry point | Natural next research step |
|---|---|---|---|
| Safety assurance for autonomous systems | Bounded STPA-informed model, UCA-to-claim traceability, persistence-qualified runtime evidence, exact-action and intervention analysis | [Runtime evidence assurance for UAV telemetry](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) | Benign boundary/transient cases, independent review, SITL/HIL telemetry, and closed-loop fallback evaluation |
| Safe AI-based control | Learned nominal policy composed with an exact uncertainty-aware projection; analytic box-invariance and practical-contraction margins; classical and weak baselines; explicit counterexamples | [Safe neural control certificates](https://github.com/Aleck-Tao/safe-neural-control-certificates) | Multi-state nonlinear dynamics, stabilizing physical priors, QC/SDP or CLF/CBF synthesis with solver-margin verification, then HIL evaluation |
| Trustworthy multimodal perception | Camera/LiDAR timing analysis, trajectory evaluation, provenance, controlled sensor faults | [UAV multisensor diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) | Learned uncertainty models, online observability tests, and field-log validation |
| Computer vision for field robotics | Physical UAV media, reproducible frame-quality audit, explicit evidence limits | [UAV flight-video quality audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) | Task-aware visual quality, dataset shift detection, and perception-performance correlation |
| Vision–Language–Action and embodied agents | Typed mission contracts, JSON Schema, fail-closed runtime policy, threat model | [Safety-constrained UAV mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) | Learned intent grounding with formal constraints and closed-loop evaluation |
| Autonomous UAV systems integration | Separation of learned intent, deterministic validation, control boundary, physical-test media, and post-flight evidence | [Integrated UAV project](../projects/01-ai-agent-assisted-autonomous-uav/) | Reachability-informed guards, independently labelled flight logs, and closed-loop evaluation |
| Embedded sensing and experimental instrumentation | Status-first protocol decoding, channel metrics, drift/dropout detection, versioned acceptance gates | [Multichannel thermal validation toolkit](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) | Calibration uncertainty, sensor redundancy, adaptive experiment design, and hardware-in-the-loop validation |
| Reproducible experimental robotics | Deterministic generators, versioned policies, hashes, machine-readable results, and CI across projects | [Public evidence index](../PROJECTS_OVERVIEW.md) | Experiment provenance graphs, benchmark packaging, and multi-site reproducibility |

## Common methodological thread

Across these directions, the central question is the same: **what evidence is required before an autonomous or sensing system's output should be trusted?** The repositories address that question at different layers—packet integrity, sensor validity, temporal alignment, mission semantics, safety policy, and post-experiment reporting.
