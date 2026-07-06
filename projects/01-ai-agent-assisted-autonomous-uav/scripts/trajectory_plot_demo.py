"""
Synthetic trajectory-plot demonstration for UAV perception/navigation debugging.

This script generates a simple trajectory and obstacle map. It is intended to show
how trajectory visualization can support failure analysis in autonomous systems.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    asset_dir = base / "assets"
    asset_dir.mkdir(exist_ok=True)

    t = np.linspace(0, 1, 200)
    x = 10 * t
    y = 2.0 * np.sin(2 * np.pi * t) + 0.2 * np.sin(12 * np.pi * t)

    obstacles = np.array([[2.5, 1.1], [5.5, -1.2], [7.8, 0.9]])

    plt.figure(figsize=(7, 4.5))
    plt.plot(x, y, label="synthetic UAV trajectory")
    plt.scatter(obstacles[:, 0], obstacles[:, 1], marker="x", s=80, label="obstacles")
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.title("Synthetic UAV Trajectory Debug Plot")
    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.legend()
    out = asset_dir / "synthetic_uav_trajectory_debug_plot.png"
    plt.tight_layout()
    plt.savefig(out, dpi=180)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
