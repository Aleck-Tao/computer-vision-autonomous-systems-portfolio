# Research questions

The projects share an interest in decisions made with imperfect information. These are the next questions suggested by their current implementations and results; they are proposed comparisons, not additional experiment results.

## How should measurement quality change a decision?

The [multisensor benchmark](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) shows why normal average sampling rate is insufficient for accepting a log. The [runtime monitor](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) takes the next step by making recommendations from changing telemetry evidence. A useful comparison would vary fault duration and monitor persistence together: longer persistence suppresses short excursions but delays the response to a sustained fault.

For visual inputs, the [video audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) identifies within-clip sharpness changes. A next study would compare those flags with independently measured tracking or detection errors. That would test whether the quality metric predicts a task-relevant failure, rather than merely a change in image texture.

## How much model uncertainty can a control constraint absorb?

The [scalar control project](https://github.com/Aleck-Tao/safe-neural-control-certificates) makes the feasible action interval explicit. Its derivation exposes a tradeoff between stronger contraction, disturbance tolerance and actuator authority. Extending the state dimension would require checking how conservative the chosen constraint becomes and whether the optimization remains feasible near the boundary.

The [mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) raises a related question at a slower timescale: a contract can satisfy static speed and clearance limits while depending on stale state. Connecting contract acceptance to a current stopping-margin estimate would allow that difference to be evaluated directly.

## When does robust aggregation suppress useful disagreement?

In the [decentralized Adult study](https://github.com/Aleck-Tao/decentralized-learning-stress-test), peer disagreement arises from both non-IID data and malicious updates. Coordinate trimming reduces the effect of the configured sign-flip attack, but can also change how benign minority distributions influence the model. Varying partition skew and attacker strength separately would help locate where that tradeoff changes. The current membership audit provides a separate diagnostic; a privacy guarantee would require a mechanism with an explicit privacy analysis.

## When is a deadline estimate accurate enough to schedule with?

The [wireless simulation](https://github.com/Aleck-Tao/wireless-tsn-deadline-lab) produces a useful reversal: clock-aware EDF improves delivery under bursty loss, yet loses to FIFO in the configured holdover case. This motivates varying synchronization interval, measurement noise and deadline slack separately. A comparison of the current drift estimate with a windowed estimate would test whether more stable clock estimation improves the scheduling decision, at the cost of slower adaptation.

## Which sensing faults need an external reference?

The [thermal toolkit](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) separates channel spread, reference error, drift and status flags. If all channels share the same offset, their spread can remain small: agreement alone cannot identify that error. A follow-up could vary common and channel-specific errors independently to determine what each acceptance metric can detect.

The [project index](../PROJECTS_OVERVIEW.md) links the current results behind these questions.
