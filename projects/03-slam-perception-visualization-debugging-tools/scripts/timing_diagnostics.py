"""
Sensor timestamp diagnostics.

This script computes mean update interval, standard deviation, min/max interval
and estimated frequency for each sensor stream.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd


def parse_args() -> argparse.Namespace:
    base = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Analyse sensor timestamps")
    parser.add_argument("--csv", type=Path, default=base / "sample_data" / "sensor_timestamps.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.csv)

    for sensor, group in df.groupby("sensor"):
        timestamps = group["timestamp_s"].sort_values().to_numpy()
        intervals = timestamps[1:] - timestamps[:-1]
        if len(intervals) == 0:
            continue
        mean_dt = intervals.mean()
        print(f"\nSensor: {sensor}")
        print(f"  samples: {len(timestamps)}")
        print(f"  mean interval: {mean_dt:.5f} s")
        print(f"  std interval:  {intervals.std():.5f} s")
        print(f"  min interval:  {intervals.min():.5f} s")
        print(f"  max interval:  {intervals.max():.5f} s")
        print(f"  est. frequency:{1.0 / mean_dt:.2f} Hz")


if __name__ == "__main__":
    main()
