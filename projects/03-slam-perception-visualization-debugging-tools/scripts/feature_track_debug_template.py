"""
OpenCV-style feature tracking template.

This script is a template for future use with real image sequences. It checks
whether OpenCV is available and documents the intended workflow without exposing
ongoing thesis data.
"""

from __future__ import annotations


def main() -> None:
    try:
        import cv2  # noqa: F401
    except Exception:
        print("OpenCV is not available in this environment.")
        print("Install opencv-python to adapt this template to a real image sequence.")
        return

    print("OpenCV detected.")
    print("Suggested workflow:")
    print("1. Load image sequence")
    print("2. Detect features using ORB/SIFT/GFTT")
    print("3. Track features across frames")
    print("4. Compute track length and stability")
    print("5. Save visual overlays and summary statistics")


if __name__ == "__main__":
    main()
