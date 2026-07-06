"""
Plot trajectory data from a CSV file.

Expected columns:
    timestamp_s, x_m, y_m, z_m, yaw_rad, confidence
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def parse_args() -> argparse.Namespace:
    base = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Plot trajectory from CSV")
    parser.add_argument("--csv", type=Path, default=base / "sample_data" / "synthetic_trajectory.csv")
    parser.add_argument("--out", type=Path, default=base / "assets" / "trajectory_plot_from_csv.png")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.csv)
    args.out.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(7, 4.5))
    scatter = plt.scatter(df["x_m"], df["y_m"], c=df["confidence"], s=14, label="trajectory")
    plt.plot(df["x_m"], df["y_m"], linewidth=0.8, alpha=0.6)
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.title("Trajectory Debug Plot with Confidence")
    plt.colorbar(scatter, label="perception confidence")
    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(args.out, dpi=180)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
