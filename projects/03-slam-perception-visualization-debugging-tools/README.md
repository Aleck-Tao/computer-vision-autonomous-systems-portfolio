# UAV Multisensor and Trajectory Diagnostics

A Python analysis of camera, LiDAR and IMU logs alongside an estimated and reference trajectory. The included 30-second synthetic benchmark compares a baseline with injected drift, timing jitter, missing samples and reordering.

## Results

| Scenario | ATE RMSE | RPE RMSE, 1 s | Camera–LiDAR mismatch, p95 | LiDAR dropout | Failed checks |
|---|---:|---:|---:|---:|---:|
| Baseline | 0.0370 m | 0.0440 m | 2.206 ms | 0.00% | 0 |
| Degraded | 0.2119 m | 0.1525 m | 18.314 ms | 2.67% | 11 |

<p>
  <img src="results/baseline/dashboard.svg" alt="Baseline diagnostic dashboard" width="49%">
  <img src="results/degraded/dashboard.svg" alt="Degraded diagnostic dashboard" width="49%">
</p>

Average sampling rate is a weak acceptance test here. The degraded camera reports 29.99 Hz, but its jitter is 4.716 ms and one timestamp reversal occurs. Its 0.89% dropout remains below the configured limit while the timing checks fail. Sequence loss, timing regularity and trajectory error therefore need separate decisions.

The trajectory analysis removes a fixed XY rotation/translation and vertical offset before computing residuals. ATE describes the aligned position difference; one-second RPE describes local motion error. The degraded case changes several faults together, so it demonstrates detection without identifying an individual fault's causal contribution.

The nearest-frame synchronization metric describes temporal proximity. With periodic sampling, different clock shifts can lead to similar nearest-frame distances. A low p95 also leaves the worst 5% outside the summary; it should be read alongside gap, order and loss statistics.

Reports: [baseline](results/baseline/report.md) · [degraded](results/degraded/report.md). Definitions and assumptions: [methodology](docs/methodology.md).

## Run

From this directory:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m uavdiag benchmark
```

Expected decisions: `baseline: PASS (0 failed gates)` and `degraded: FAIL (11 failed gates)`. The command regenerates data, JSON metrics, reports and SVG dashboards. The root CI compares those files with the committed versions.

## Analyze another log

Put `sensor_timestamps.csv`, `reference_trajectory.csv` and `estimated_trajectory.csv` in one directory, then run:

```bash
python -m uavdiag analyze path/to/log path/to/report --label flight-07
```

Timing columns are `sensor,sequence,timestamp_s`; trajectory columns are `timestamp_s,x_m,y_m,z_m,yaw_rad`. The current timing model uses camera/LiDAR/IMU nominal rates of 30/10/100 Hz. Exit code `0` means all configured checks passed and `2` requests review.

The [thresholds](config/quality_gates.json) belong to this benchmark's policy. Using them on a physical experiment requires a documented reference and a justification for the task's timing and accuracy limits. For package installation and the same analysis, see [uav-multisensor-diagnostics](https://github.com/Aleck-Tao/uav-multisensor-diagnostics).
