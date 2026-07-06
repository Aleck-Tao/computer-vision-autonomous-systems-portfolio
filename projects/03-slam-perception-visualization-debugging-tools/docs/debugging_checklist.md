# SLAM / Perception Debugging Checklist

## 1. Sensor Setup

- Are sensors mounted securely?
- Are camera/LiDAR coordinate frames documented?
- Is calibration available and version-controlled?
- Are time stamps recorded for every sensor frame?

## 2. Timing and Synchronization

- What is the mean update interval for each sensor?
- What is the maximum jitter?
- Are there dropped frames?
- Is there a systematic offset between sensors?

## 3. Trajectory Quality

- Does the trajectory drift over time?
- Are there sudden jumps?
- Does the estimated path match visual inspection?
- Are failures linked to low-texture or reflective regions?

## 4. Feature / Point Stability

- Are tracked features stable across frames?
- Do features disappear during lighting changes?
- Are LiDAR points sparse or noisy in key regions?

## 5. Safety-Related Checks

- Did the system detect obstacles early enough?
- Did perception confidence drop before unsafe behaviour?
- Was an emergency stop or return-to-home condition triggered?
- Was the failure logged clearly?

## 6. Documentation

Each failure case should include:

- date/time,
- environment description,
- sensor configuration,
- software version,
- trajectory plot,
- timing plot,
- short root-cause hypothesis.
