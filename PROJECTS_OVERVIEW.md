# Public evidence and claim boundaries

This page is a reviewer-oriented index of what can be verified publicly. The portfolio is structured to distinguish integrated physical-system evidence from focused, independently reproducible software repositories.

## Specialist repositories

| Repository | Public maturity | Strongest evidence | Appropriate reviewer use |
|---|---|---|---|
| [Runtime evidence assurance for UAV telemetry](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) | Reproducible synthetic safety-assurance prototype | Bounded STPA-informed model, executable claim graph, six monitors, 70 traces, 30 tests, linked source/data/result manifests and CI | Evaluate hazard-to-evidence traceability, fail-closed state-machine reasoning, exact-action evaluation, and explicit claim boundaries |
| [Safe neural control certificates](https://github.com/Aleck-Tao/safe-neural-control-certificates) | Released scalar robust-control benchmark | Closed-form uncertainty-aware projection, in-repository separate-code-path analytic verifier, five controllers, negative controls, 90 simulated runs, 36,012 corner/grid checks, three linked provenance layers and CI | Evaluate sampled-data derivation, uncertainty handling, counterexample design, classical baselines, and the separation of model guarantee from physical claims |
| [UAV multisensor diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) | Reproducible software project | CLI, five tests, deterministic benchmark, versioned gates, JSON/Markdown/SVG reports and CI | Evaluate sensor-integrity reasoning, trajectory metrics, fault injection, and experiment acceptance |
| [Safety-constrained UAV mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) | Reproducible interface and policy project | Typed contract, schema, parser, fail-closed validation, threat model, seven tests and CI | Evaluate system decomposition and the boundary between language intent and control |
| [UAV flight-video quality audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) | Reproducible analysis of released real media | Two MP4 files, hashes, 224 frame samples, metrics, reports and CI | Evaluate visual-data provenance and evidence-quality analysis |
| [Multichannel thermal validation toolkit](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) | Reproducible synthetic measurement project | Defensive protocol codec, simulator, status-aware analysis, nine tests and CI | Evaluate embedded sensing, experimental validation, and confidentiality-aware public communication |

## Integrated repository evidence

1. **Physical UAV field-test media** — two outdoor MP4 clips, representative stills, media metadata, and SHA-256 hashes.
2. **Integrated system architecture** — a documented connection between perception, mission representation, safety checks, flight-control interfaces, and post-flight validation.
3. **Reproducible diagnostic package** — a local copy of the multisensor benchmark with data, reports, tests, and root CI.
4. **Real-video audit** — a local analysis path over the released field clips.

## Claim matrix

| Claim | Public evidence | Explicit limitation |
|---|---|---|
| Implemented bounded hazard-to-evidence traceability | Machine-readable UCA/constraint/claim links, runtime monitor states, tests, timelines, and integrity manifests | STPA is bounded and not independently reviewed; assumptions and thresholds are unvalidated; no physical recovery is measured |
| Implemented an analytic safety layer around a neural nominal controller | Closed-form robust admissible interval, separate-code-path recomputed margins, uncertainty counterexample, simulated closed-loop regressions and CI | Guarantee is restricted to the declared scalar sampled-data model; the neural network alone and any physical system are not certified |
| Built and tested a physical UAV platform | Outdoor MP4 clips, stills, metadata, and media manifest | Footage does not prove autonomous operation |
| Implemented safety-aware mission handling | Typed mission contract and deterministic validator | Public parser is rule-based, not a trained language/VLA model |
| Built reproducible sensor and trajectory diagnostics | Package, CLI, tests, benchmark data, reports, and CI | Included ATE/RPE values are controlled simulation results |
| Audited real field-video quality | 224 sampled frames with CSV, JSON, report, SVG, and hashes | Quality metrics do not establish task success or autonomy |
| Designed a multichannel validation workflow | Independent public codec, simulator, metrics, gates, and reports | No client data, commercial protocol, chip identity, or proprietary algorithm is included |

## Evidence policy

Every quantitative statement should be traceable to a committed result file and a command that regenerates it. Synthetic values are labelled as benchmarks. Field media are described only as evidence of physical testing. Where confidential or unpublished material would be required to support a stronger claim, the stronger claim is not made.

Start with the [portfolio README](README.md), then choose a specialist repository based on the research area being evaluated.
