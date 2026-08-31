# Computer Vision and Autonomous Systems Research Portfolio

[![Reproducibility](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

I am **Yuanyuan Tao (Alec)**, an MSc Electronic Engineering candidate at Durham University. My work connects physical UAV experimentation, multimodal perception, safety-constrained mission interfaces, and reproducible sensing/diagnostic workflows.

This repository is the permanent overview for my research portfolio. It keeps the physical evidence and integrated system narrative in one place, while the specialist repositories below provide focused packages, tests, data, and CI for individual research questions.

## Research map

| Specialist repository | Research question | Reproducible evidence | Boundary |
|---|---|---|---|
| [UAV multisensor diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) | Can timing and trajectory failures be detected before a camera/LiDAR experiment is accepted? | Python package, CLI, five tests, controlled fault injection, ATE/RPE and synchronization reports | Accuracy values are synthetic benchmark results, not field-performance claims |
| [Safety-constrained UAV mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) | How should language-level intent cross into a safety-critical UAV stack? | Typed contract, JSON Schema, fail-closed policy, threat model, seven tests | The parser is rule-based and is not presented as a trained VLA model |
| [Runtime evidence assurance for UAV telemetry](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) | Can changing telemetry evidence update a bounded assurance argument and produce reproducible fallback recommendations? | Executable claim/monitor mapping, deterministic replay checks, source/data/result manifests, v0.1.0 release and six-job CI | Synthetic open-loop replay with demonstrator thresholds and a separately configured synthetic oracle; no vehicle command, recovery, or flight-safety claim |
| [Safe neural control certificates](https://github.com/Aleck-Tao/safe-neural-control-certificates) | Can an arbitrary finite neural action be projected into an analytically feasible robust interval for a declared uncertain plant? | In-repository separate-code-path certificate recomputation, five-controller comparison, explicit negative controls, 90 simulated scalar-model closed-loop runs, 36,012 implementation checks, v0.1.0 and six-job CI | Exact only for the scalar sampled-data model and assumptions; no MIMO, continuous-time, physical-system, HIL, or intrinsic-neural-stability claim |
| [Decentralized learning stress test](https://github.com/Aleck-Tao/decentralized-learning-stress-test) | How do peer-local aggregation rules behave under non-IID scarcity, malicious deltas, local synthetic augmentation, and a loss-based membership audit? | Pinned UCI Adult archive, 8 simulated peers, 54 CPU runs, 19 tests, per-peer train/holdout hashes, three result manifests, v0.1.0 and Windows/Linux CI | Synchronous single-process simulation; no network deployment, DP, secure aggregation, BFT theorem, LLM, or fairness/compliance claim |
| [Wireless TSN deadline lab](https://github.com/Aleck-Tao/wireless-tsn-deadline-lab) | How do wireless loss bursts and imperfect clock synchronization affect deadline-aware scheduling at a wired-to-wireless boundary? | C++20 simulator, right-censor-safe cohort, independent evaluator, GCC/Clang/CTest/ASan/UBSan, 240 CI runs, 725 hashed result files and v0.1.0 | Packet/slot abstraction only; no IEEE 802.1Qbv/802.1AS conformance, ns-3, PHY/MAC, FPGA/SDR, openwifi, or hardware evidence |
| [UAV flight-video quality audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) | Is released field footage usable as traceable visual evidence? | Two MP4 clips, SHA-256 manifest, 224 sampled frames, per-frame CSV, JSON and SVG | Image quality does not prove autonomous-flight success |
| [Multichannel thermal validation toolkit](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) | How can protocol integrity, status semantics, and channel consistency form one validation decision? | Fictional public protocol, seeded simulator, nine tests, versioned gates and reports | All data are synthetic; no commercial protocol, client data, or product specification is published |

## Integrated UAV system and physical evidence

The MSc system project connects LiDAR/stereo perception, structured mission contracts, deterministic safety checks, flight-control interfaces, and post-flight validation. Two outdoor field-test videos provide evidence that the physical platform was assembled and tested; they are deliberately not used as proof of autonomous behavior.

<p>
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_a.jpg" alt="Outdoor UAV field test A" width="49%">
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_b.jpg" alt="Outdoor UAV field test B" width="49%">
</p>

- [Integrated system project](projects/01-ai-agent-assisted-autonomous-uav/)
- [Field-media provenance and evidence notes](projects/01-ai-agent-assisted-autonomous-uav/docs/flight_test_evidence.md)
- [Standalone safety interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface)
- [Standalone real-video audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit)

## Selected reproducible results

### Multisensor diagnostic benchmark

| Scenario | Verdict | ATE RMSE | RPE RMSE | Camera–LiDAR sync p95 | Failed gates |
|---|:---:|---:|---:|---:|---:|
| Baseline | **PASS** | 0.0370 m | 0.0440 m | 2.206 ms | 0 |
| Degraded | **FAIL** | 0.2119 m | 0.1525 m | 18.314 ms | 11 |

<p>
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/baseline/dashboard.svg" alt="Baseline diagnostic dashboard" width="49%">
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/degraded/dashboard.svg" alt="Degraded diagnostic dashboard" width="49%">
</p>

The degraded case injects drift, disturbance, timestamp jitter, loss, reordering, and clock offset. Its expected failure demonstrates the quality gates; it is not a failed field deployment.

### Real field-video audit

The committed video pipeline decodes 224 samples at 1 Hz, measures exposure/clipping, Laplacian sharpness, and temporal luminance change, then emits per-frame CSV, provenance JSON, a report, and an SVG timeline. Two low-sharpness samples were flagged in Clip B; no widespread black-frame or highlight-clipping condition was found at the sampled instants.

### Multichannel thermal validation

The separate thermal toolkit demonstrates a status-first acquisition-to-decision workflow. Its synthetic baseline passes with a 0.3026 °C p95 channel spread and zero issues; the controlled degraded run produces a 1.1843 °C p95 spread and eight coded issues. These are simulator regression results, not hardware accuracy specifications.

### Decentralized learning robustness

The 54-run Adult benchmark retains both useful and adverse outcomes. Under peer-mean aggregation, the non-IID scarce synthetic mix reached 0.729 mean balanced accuracy, while the configured sign-flip attack reduced it to 0.484; trimmed mean reached 0.677 under that attack. These values describe one public dataset, topology, model, attack, and three-seed design. They are not a privacy or Byzantine-resilience guarantee.

### Wireless deadline scheduling

The 240-run C++ matrix likewise avoids a winner-only narrative. Clock-aware EDF improved on FIFO in the bursty-channel and retry/replication cases, but fell below FIFO during the configured synchronization holdover; strict priority was strongest in several stress cases. The full event/metadata/metric chain and negative overload control are committed, while standards and hardware claims remain explicitly out of scope.

## Reproduce this repository

```bash
# Multisensor benchmark
cd projects/03-slam-perception-visualization-debugging-tools
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m uavdiag benchmark

# Mission-contract checks
cd ../01-ai-agent-assisted-autonomous-uav
python -m unittest discover -s tests -v

# Real-video audit
cd ../02-uav-flight-video-quality-audit
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m videoaudit
```

The root [GitHub Actions workflow](.github/workflows/reproducibility.yml) runs all three paths and rejects changes when committed results cannot be regenerated.

## Evidence and disclosure policy

Every quantitative statement should be traceable to a result file and regeneration command. Simulation results and field evidence are labelled separately. Confidential dissertation logs, third-party data, commercial identifiers, proprietary communication maps, calibration algorithms, and unpublished hardware details are intentionally excluded.

- [Reviewer-oriented evidence index](PROJECTS_OVERVIEW.md)
- [PhD research-fit map](docs/research_fit_map.md)
- [Asset and provenance index](ASSETS_INDEX.md)

## Research direction

I am interested in PhD work on computer vision, multimodal perception, autonomous systems, safe learning-based control, trustworthy decentralized AI, time-sensitive wireless systems, and Vision–Language–Action research, especially where deployment requires explicit validation, interpretable failure analysis, and safe interfaces between learned components, networks, and control systems. My embedded sensing work provides a complementary experimental foundation: defensible acquisition, status-aware decoding, and traceable quality decisions.

## Contact

**Yuanyuan Tao (Alec)**  
MSc Electronic Engineering Candidate, Durham University  
[yuanyuan.tao@durham.ac.uk](mailto:yuanyuan.tao@durham.ac.uk)
