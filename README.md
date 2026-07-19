# Computer Vision and Autonomous Systems Research Portfolio

I am **Yuanyuan Tao (Alec)**, an MSc Electronic Engineering candidate at Durham University. My current work connects physical UAV experimentation with multi-sensor perception, mission-level language interfaces and reproducible safety/diagnostic tooling.

This repository is organized around public evidence rather than broad skill claims: runnable code, deterministic experiments, tests, machine-readable results and field-test media. Ongoing dissertation material that cannot be released is marked explicitly.

## Featured work

### 1. UAV multi-sensor integrity and trajectory diagnostics

A complete Python research tool that detects timestamp jitter, frame loss, out-of-order samples, Camera–LiDAR synchronization error and trajectory degradation. It includes controlled fault injection, SE(2)-aligned ATE/RPE analysis, configurable quality gates, SHA-256 provenance, four unit tests and GitHub Actions reproducibility.

| Scenario | Verdict | ATE RMSE | RPE RMSE | Camera–LiDAR sync p95 | Failed gates |
|---|:---:|---:|---:|---:|---:|
| Baseline | **PASS** | 0.0370 m | 0.0440 m | 2.206 ms | 0 |
| Degraded | **FAIL** | 0.2119 m | 0.1525 m | 18.314 ms | 11 |

<p>
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/baseline/dashboard.svg" alt="Baseline diagnostic dashboard" width="49%">
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/degraded/dashboard.svg" alt="Degraded diagnostic dashboard" width="49%">
</p>

[`Open the project →`](projects/03-slam-perception-visualization-debugging-tools/)

### 2. AI-agent-assisted UAV system and field testing

An ongoing MSc system project connecting LiDAR/stereo perception, structured mission contracts, deterministic safety checks, flight-control interfaces and post-flight validation. Two outdoor flight-test videos (3:43 total) provide public evidence of the physical platform; the repository carefully avoids treating video as proof of autonomy.

<p>
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_a.jpg" alt="Outdoor UAV field test A" width="49%">
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_b.jpg" alt="Outdoor UAV field test B" width="49%">
</p>

[`Open the project →`](projects/01-ai-agent-assisted-autonomous-uav/)

## Research evidence map

| Claim | Public evidence | Boundary |
|---|---|---|
| Built and tested a physical UAV platform | Two outdoor MP4 clips, extracted frames, metadata and SHA-256 manifest | Footage does not prove autonomous operation |
| Implemented safety-aware mission handling | Typed mission JSON and deterministic validation scripts | Parser is rule-based, not presented as a VLA model |
| Built reproducible sensor/trajectory diagnostics | Importable package, CLI, tests, benchmark data, reports and CI | Included accuracy values are controlled simulation results |
| Audited real field-test video quality | 224 decoded samples, per-frame CSV, summary JSON and SVG timeline | Image-quality metrics do not imply autonomous-flight success |
| Understand experimental failure analysis | Fault injection covers drift, disturbance, jitter, loss, reordering and clock offset | Real-log thresholds must be platform-specific |

## Reproduce the main result

```bash
cd projects/03-slam-perception-visualization-debugging-tools
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m uavdiag benchmark
```

Expected output:

```text
Ran 4 tests ... OK
baseline: PASS (0 failed gates)
degraded: FAIL (11 failed gates)
```

### 3. Real flight-video quality audit

A reproducible data-quality pipeline over the two released MP4 clips. It decodes frames at 1 Hz, measures exposure/clipping, Laplacian sharpness and temporal luminance change, and writes per-frame CSV, provenance JSON, a report and an SVG timeline.

The committed audit covers **224 real frames**; it found two low-sharpness outliers in Clip B and no widespread black-frame or highlight-clipping failure at the sampled instants.

[`Open the project →`](projects/02-uav-flight-video-quality-audit/)

## Research direction

I am interested in PhD work involving computer vision, multimodal perception, autonomous systems and Vision–Language–Action research, especially where real-world deployment demands explicit validation, interpretable failure analysis and safe interfaces between learned components and control systems.

## Contact

**Yuanyuan Tao (Alec)**  
MSc Electronic Engineering Candidate, Durham University  
[yuanyuan.tao@durham.ac.uk](mailto:yuanyuan.tao@durham.ac.uk)
