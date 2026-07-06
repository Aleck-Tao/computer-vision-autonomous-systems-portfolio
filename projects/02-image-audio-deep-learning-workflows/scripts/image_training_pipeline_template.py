"""
Image training pipeline template.

This file is a professional template for organising a PyTorch image-classification
experiment. It is intentionally lightweight so it can be adapted to real datasets
without exposing ongoing dissertation code or restricted data.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ExperimentConfig:
    data_dir: Path
    output_dir: Path
    epochs: int = 10
    batch_size: int = 16
    learning_rate: float = 1e-3
    seed: int = 42


def parse_args() -> ExperimentConfig:
    parser = argparse.ArgumentParser(description="Image training pipeline template")
    parser.add_argument("--data-dir", type=Path, default=Path("data/images"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/image_experiment"))
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    args = parser.parse_args()
    return ExperimentConfig(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
    )


def main() -> None:
    cfg = parse_args()
    cfg.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        import torch  # noqa: F401
        import torchvision  # noqa: F401
    except Exception:
        print("PyTorch/torchvision not available in this environment.")
        print("This script is a template. Install torch and torchvision to adapt it to a real dataset.")
        print(f"Experiment configuration: {cfg}")
        return

    print("PyTorch detected. Add dataset loading, model definition, training and evaluation here.")
    print(f"Experiment configuration: {cfg}")

    # Recommended structure for real experiments:
    # 1. set random seed
    # 2. create train/val/test transforms
    # 3. load datasets using ImageFolder or custom Dataset
    # 4. define model
    # 5. train with validation loop
    # 6. save checkpoints and metrics
    # 7. run error analysis


if __name__ == "__main__":
    main()
