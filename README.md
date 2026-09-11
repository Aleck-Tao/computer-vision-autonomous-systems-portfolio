# Sensing, Control and Autonomous Systems

[![Reproducibility](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

I am Yuanyuan Tao (Alec), an MSc Electronic Engineering candidate at Durham University. These projects examine how sensor timing, uncertain models and incomplete observations affect decisions in autonomous systems.

This repository contains the UAV field media, mission-contract code and two analysis pipelines. The specialist repositories extend the work into runtime monitoring, constrained control, decentralized learning and wireless scheduling.

## Start with the results

**Average sampling rate can hide a damaged log.** In the synthetic multisensor benchmark, the degraded camera stream still averages 29.99 Hz. Yet it contains timestamp reordering, and camera–LiDAR p95 mismatch rises from 2.206 to 18.314 ms. The resulting analysis needs sequence and timing checks alongside the trajectory metrics.

| Synthetic scenario | ATE RMSE | RPE RMSE, 1 s | Sync mismatch, p95 | Failed checks |
|---|---:|---:|---:|---:|
| [Baseline](projects/03-slam-perception-visualization-debugging-tools/results/baseline/report.md) | 0.0370 m | 0.0440 m | 2.206 ms | 0 |
| [Degraded](projects/03-slam-perception-visualization-debugging-tools/results/degraded/report.md) | 0.2119 m | 0.1525 m | 18.314 ms | 11 |

<p>
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/baseline/dashboard.svg" alt="Baseline diagnostic dashboard" width="49%">
  <img src="projects/03-slam-perception-visualization-debugging-tools/results/degraded/dashboard.svg" alt="Degraded diagnostic dashboard" width="49%">
</p>

**Video quality needs a local interpretation.** The audit of two outdoor UAV clips samples 224 frames at 1 Hz and flags two low-sharpness samples in Clip B. Both clips are resized to 180 pixels wide, but texture, scene content and resizing still affect Laplacian variance; changes within a clip are therefore more informative than ranking the two recordings. The [report](projects/02-uav-flight-video-quality-audit/results/report.md) and [timeline](projects/02-uav-flight-video-quality-audit/results/timeline.svg) identify which portions deserve a closer look.

**More selective algorithms introduce tradeoffs.** In the [Adult learning benchmark](https://github.com/Aleck-Tao/decentralized-learning-stress-test), a configured sign-flip attack lowers peer-mean balanced accuracy from 0.729 to 0.484; trimmed mean reaches 0.677 under attack. In the [wireless simulation](https://github.com/Aleck-Tao/wireless-tsn-deadline-lab), clock-aware EDF improves on FIFO under bursty loss but performs worse during clock holdover. The project notes examine the assumptions behind both outcomes.

## Projects

| Area | Repository | Experiment or implementation |
|---|---|---|
| Sensor integrity | [Multisensor diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics) | Simulated timing faults, trajectory alignment and acceptance checks |
| Visual data | [Flight-video audit](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) | Exposure, clipping and sharpness analysis of released field footage |
| Mission handling | [Mission interface](https://github.com/Aleck-Tao/safety-constrained-uav-mission-interface) | Rule-based intent parsing and structured policy checks |
| Runtime monitoring | [Evidence assurance](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) | Synthetic open-loop telemetry replay and fallback recommendations |
| Learning-based control | [Neural control certificates](https://github.com/Aleck-Tao/safe-neural-control-certificates) | Robust action projection and analytic bounds for a scalar sampled-data plant |
| Distributed learning | [Decentralized stress test](https://github.com/Aleck-Tao/decentralized-learning-stress-test) | Eight simulated peers, non-IID Adult partitions and poisoned updates |
| Network timing | [Wireless deadline lab](https://github.com/Aleck-Tao/wireless-tsn-deadline-lab) | Packet/slot simulation of loss, clock uncertainty and scheduling |
| Embedded sensing | [Thermal validation](https://github.com/Aleck-Tao/multichannel-thermal-validation-toolkit) | Synthetic channel faults, reference comparison and a public protocol codec |

The [project index](PROJECTS_OVERVIEW.md) points directly to reports and implementation details. [Research questions](docs/research_fit_map.md) describe the next comparisons suggested by the current results.

## UAV field material

<p>
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_a.jpg" alt="Outdoor UAV test, clip A" width="49%">
  <img src="projects/01-ai-agent-assisted-autonomous-uav/assets/flight_test_clip_b.jpg" alt="Outdoor UAV test, clip B" width="49%">
</p>

Two outdoor flight clips and representative stills document the physical platform. The [media record](projects/01-ai-agent-assisted-autonomous-uav/docs/flight_test_evidence.md) contains the original files, metadata and hashes; the [mission project](projects/01-ai-agent-assisted-autonomous-uav/) describes the contract and control-interface design. The clips support visual inspection of the tests. Localization accuracy and closed-loop autonomy require their own synchronized measurements.

## Run the local analyses

From the repository root:

```bash
# Multisensor benchmark
cd projects/03-slam-perception-visualization-debugging-tools
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m uavdiag benchmark

# Mission-contract checks
cd ../01-ai-agent-assisted-autonomous-uav
python -m unittest discover -s tests -v

# Field-video audit
cd ../02-uav-flight-video-quality-audit
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m videoaudit
```

[CI](.github/workflows/reproducibility.yml) regenerates both analyses and compares the outputs with the committed results. Each specialist repository has its own installation and experiment commands. Methods and input provenance stay with the corresponding reports.

Contact: [yuanyuan.tao@durham.ac.uk](mailto:yuanyuan.tao@durham.ac.uk)
