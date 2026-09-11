# UAV Field-Video Quality Audit

An analysis of the two outdoor UAV clips stored in this portfolio. The pipeline samples frames at 1 Hz, resizes them to 180 pixels wide and measures luma, clipping, Laplacian variance and temporal luma change.

![Video quality timeline](results/timeline.svg)

## Results

| Clip | Duration | Samples | Mean luma | Median sharpness | Low-sharpness samples | Max dark pixels | Max clipped pixels |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 91.33 s | 91 | 128.62 | 254.5 | 0 | 4.41% | 0.55% |
| B | 132.90 s | 133 | 133.41 | 216.7 | 2 | 1.94% | 1.09% |

The 224 samples contain two within-clip sharpness outliers in Clip B. Large dark or clipped regions are absent at the sampled instants. Use the [frame metrics](results/frame_metrics.csv) to locate the changes and the original footage to interpret them.

A Laplacian response depends on texture as well as blur. The rule `max(20, Q1 - 1.5 * IQR)` marks low values relative to each clip, so a consistently low-detail clip can have few outliers. Similarly, a 1 Hz audit can miss a short defect between samples. These choices make this a first pass for selecting segments to inspect.

## Run

From this directory:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m videoaudit
```

The command reads the original MP4 files in [Test Video](../../Test%20Video/) and regenerates [frame metrics](results/frame_metrics.csv), [summary and provenance](results/summary.json), [report](results/report.md) and [timeline](results/timeline.svg).

Luma uses Rec. 709 RGB weights; dark/clipped fractions use thresholds of 16/240 on a 0–255 scale. Sharpness uses the variance of a four-neighbour Laplacian, and temporal change compares consecutive samples without motion compensation. These metrics describe the video files. Evaluating localization or task success additionally requires synchronized reference measurements.

The [standalone package](https://github.com/Aleck-Tao/uav-flight-video-quality-audit) contains the same audit with installation metadata and method notes.
