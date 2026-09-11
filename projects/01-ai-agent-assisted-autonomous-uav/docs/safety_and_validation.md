# Static limits and runtime stopping margin

The public contract validator checks a requested clearance and speed category. A runtime decision also needs a model of how far the vehicle can move before it stops.

For a one-dimensional approach toward a stationary obstacle with speed `v >= 0`, total observation/actuation delay `tau >= 0`, and constant braking deceleration `a > 0`, assume speed stays constant during the delay. The stopping distance is

```text
d_stop = v * tau + v^2 / (2 * a).
```

With an allowance `e >= 0` for clearance uncertainty, the corresponding margin is `d_measured - e - d_stop`. This is a kinematic analysis under the stated assumptions, not a measured braking result. It shows why one fixed clearance threshold cannot apply equally at every speed:

```text
partial d_stop / partial tau = v
partial d_stop / partial v   = tau + v / a.
```

Delay consumes distance linearly; speed also increases the braking term quadratically. A vehicle-specific check would need a conservative deceleration estimate, documented latency and an uncertainty allowance. The [runtime replay project](https://github.com/Aleck-Tao/runtime-safety-assurance-uav) explores a related stopping-margin monitor under its synthetic model.

## What to record in an integrated test

Log the request and parsed contract, timestamped state used at the decision, policy result, recommendation, executed action and reference measurements. Keeping recommendation and execution separate allows three failures to be distinguished: incorrect interpretation, inadequate constraints, and a correctly requested action that was not carried out.

The [synthetic diagnostic pipeline](../../03-slam-perception-visualization-debugging-tools/) checks timing and reference/estimate alignment. The [field-video audit](../../02-uav-flight-video-quality-audit/) identifies visually weak segments. These checks determine whether a recording supports the quantity being evaluated; thresholds should be chosen for that quantity and platform.
