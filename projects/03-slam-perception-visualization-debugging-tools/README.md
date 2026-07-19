# UAV Multi-Sensor Integrity and Trajectory Diagnostics

[![reproducibility](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/Aleck-Tao/computer-vision-autonomous-systems-portfolio/actions/workflows/reproducibility.yml)

A small research tool for deciding whether UAV sensor logs and pose estimates are trustworthy enough for downstream perception, mapping or control experiments. It checks three failure surfaces that are easy to miss when only looking at a final trajectory plot:

- per-sensor jitter, dropped samples and out-of-order timestamps;
- Camera–LiDAR nearest-frame synchronization error;
- aligned trajectory accuracy using ATE, one-second RPE, final drift, heading error and path-length error.

The repository contains a deterministic baseline/degraded benchmark, machine-readable quality gates, unit tests, committed reports and an automated reproducibility check. The benchmark uses controlled fault injection so every result can be regenerated without publishing confidential dissertation logs.

## Benchmark result

| Scenario | Verdict | ATE RMSE | RPE RMSE (1 s) | Camera–LiDAR sync p95 | LiDAR dropout rate | Failed gates |
|---|:---:|---:|---:|---:|---:|---:|
| Baseline | **PASS** | 0.0370 m | 0.0440 m | 2.206 ms | 0.00% | 0 |
| Degraded | **FAIL** | 0.2119 m | 0.1525 m | 18.314 ms | 2.67% | 11 |

<p>
  <img src="results/baseline/dashboard.svg" alt="Baseline scenario dashboard" width="49%">
  <img src="results/degraded/dashboard.svg" alt="Degraded scenario dashboard" width="49%">
</p>

The degraded scenario injects localization drift, a temporary pose disturbance, sensor jitter, dropped frames, one timestamp-order violation and a Camera–LiDAR clock offset. The purpose is not to report synthetic accuracy as flight performance; it is to show that the same analysis code accepts a healthy log and rejects a known-bad one.

## Reproduce in one command

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m uavdiag benchmark
```

Expected terminal summary:

```text
baseline: PASS (0 failed gates)
degraded: FAIL (11 failed gates)
```

Generated artifacts are written to `results/<scenario>/`:

- `metrics.json` — complete metrics, gate decisions and SHA-256 input provenance;
- `report.md` — human-readable diagnostic report;
- `dashboard.svg` — dependency-free visual summary.

## Use with an experiment log

Prepare one directory containing:

```text
sensor_timestamps.csv
reference_trajectory.csv
estimated_trajectory.csv
```

Then run:

```bash
python -m uavdiag analyze path/to/log path/to/report --label flight-07
```

The command returns exit code `0` when every configured gate passes and `2` when review is required, so it can be used in an experiment ingestion pipeline.

### Timing schema

```csv
sensor,sequence,timestamp_s
camera,0,0.00000000
camera,1,0.03333333
lidar,0,0.00080000
```

### Trajectory schema

```csv
timestamp_s,x_m,y_m,z_m,yaw_rad
0.000000,0.000000,0.220000,1.450000,0.00000000
```

The reference can come from motion capture, RTK/GNSS, a trusted simulator or another documented reference system. Thresholds in `config/quality_gates.json` are experiment policy, not universal constants; they must be justified for the platform and task.

## Engineering decisions

- **Deterministic data generation:** fixed seeds and stable CSV formatting make reports byte-reproducible.
- **Explicit provenance:** each report records SHA-256 hashes for all input files and the quality-gate configuration.
- **Sequence-aware dropout inference:** frame loss is measured from sequence gaps instead of guessed from irregular timestamps.
- **Rigid trajectory alignment:** a 2D rigid transform and vertical offset remove arbitrary initial frame placement before accuracy metrics are computed.
- **No plotting dependency:** dashboards are generated as SVG using the Python standard library; NumPy is the only runtime dependency.
- **Fail-closed quality gate:** any failed check marks the whole run for review.

See [`docs/methodology.md`](docs/methodology.md) for metric definitions, assumptions and fault-injection design.

## Scope and limitations

This tool diagnoses log integrity and trajectory consistency; it is not a SLAM implementation, flight controller or safety-certified system. The included benchmark is simulated and labelled as such. Real flight accuracy claims require calibrated ground truth, documented sensor mounting and released experimental logs.
