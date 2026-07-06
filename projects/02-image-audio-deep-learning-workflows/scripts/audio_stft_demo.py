"""
Synthetic STFT-style audio feature extraction demo.

This script generates a simple synthetic signal and computes a short-time Fourier
transform using NumPy. It avoids external audio dependencies and demonstrates the
feature-extraction logic used in audio/signal deep learning workflows.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def stft(signal: np.ndarray, window_size: int, hop_size: int) -> np.ndarray:
    window = np.hanning(window_size)
    frames = []
    for start in range(0, len(signal) - window_size, hop_size):
        frame = signal[start:start + window_size] * window
        frames.append(np.abs(np.fft.rfft(frame)))
    return np.array(frames).T


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    asset_dir = base / "assets"
    asset_dir.mkdir(exist_ok=True)

    sample_rate = 16000
    duration_s = 1.0
    t = np.linspace(0, duration_s, int(sample_rate * duration_s), endpoint=False)
    signal = 0.7 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 1200 * t)
    signal += 0.02 * np.random.default_rng(42).normal(size=signal.shape)

    spec = stft(signal, window_size=512, hop_size=128)
    spec_db = 20 * np.log10(spec + 1e-8)

    plt.figure(figsize=(7, 4.5))
    plt.imshow(spec_db, origin="lower", aspect="auto")
    plt.xlabel("Frame")
    plt.ylabel("Frequency bin")
    plt.title("Synthetic STFT Feature Demo")
    plt.colorbar(label="Magnitude (dB)")
    plt.tight_layout()
    out = asset_dir / "synthetic_stft_feature_demo.png"
    plt.savefig(out, dpi=180)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
