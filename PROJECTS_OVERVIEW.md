# Project and result index

Use this page to move from a result to the code and assumptions behind it. Each specialist README links its experiment configuration, outputs and reproduction command.

| Project | Result to inspect | Question to follow through the implementation |
|---|---|---|
| [Multisensor diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) | Baseline and degraded reports: average sensor rate remains close to nominal while timing and trajectory checks fail | Which failures are visible in sequence gaps, timestamp differences and aligned pose error? |
| [Flight-video audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) | Per-frame metrics and timeline for 224 samples from two released clips | Does a sharpness outlier reflect blur, a change in scene texture, or an exposure change? |
| [Mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) | Example contracts and accepted/rejected policy decisions | Which constraints can be checked from structured fields, and which depend on interpretation or current vehicle state? |
| [Runtime evidence assurance](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) | Replay comparisons between immediate monitoring and persistence-qualified recommendations | How much decision delay does persistence introduce, and what happens when required evidence becomes stale? |
| [Neural control certificates](https://github.com/Aleck-Tao/safe-neural-control-certificates) | Five-controller simulation comparison and analytic certificate | How do uncertainty, actuator limits and the contraction target determine the feasible action interval? |
| [Decentralized learning](https://github.com/Aleck-Tao/decentralized-learning-stress-test) | Adult clean/poisoned comparisons across three aggregation rules | What does coordinate trimming discard when benign peers already disagree because of non-IID data? |
| [Wireless scheduling](https://github.com/Aleck-Tao/wireless-tsn-deadline-lab) | Six-scenario report, paired seed comparisons and per-run event traces | When do estimated deadlines become less useful than a simple queue order? |
| [Thermal validation](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) | Baseline/degraded channel metrics and status-fault reports | Can cross-channel agreement detect a common offset, or is an independent reference needed? |

## Analyses included here

- [Mission contracts](projects/01-ai-agent-assisted-autonomous-uav/): parser, policy checks, sample commands and interface design.
- [Field-video analysis](projects/02-uav-flight-video-quality-audit/results/report.md): measured image properties, with [per-frame values](projects/02-uav-flight-video-quality-audit/results/frame_metrics.csv).
- [Synthetic baseline](projects/03-slam-perception-visualization-debugging-tools/results/baseline/report.md) and [fault-injected case](projects/03-slam-perception-visualization-debugging-tools/results/degraded/report.md): timing and trajectory comparisons using the same checks.
- [Flight-media record](projects/01-ai-agent-assisted-autonomous-uav/docs/flight_test_evidence.md): original outdoor clips, stills, metadata and hashes.

## Reading the results

The field-video metrics describe the released MP4 files. The multisensor and thermal fixtures, telemetry replays, scalar-control runs and wireless cases use declared synthetic models. The decentralized study uses the public Adult dataset with simulated peers and controlled attacks. Mission handling is executable parsing and validation code.

This distinction determines how to use a result: a model comparison tests an algorithm under its assumptions; field accuracy requires measurements and a reference for the physical quantity being claimed. Theory and mechanism explanations are identified in the project notes, with open questions collected in the [research map](docs/research_fit_map.md).
