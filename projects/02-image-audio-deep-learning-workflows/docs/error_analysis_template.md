# Error Analysis Template

This template can be used after model evaluation.

## Experiment Information

- Model:
- Dataset:
- Date:
- Training setting:
- Validation/test split:
- Main metric:

## Failure Categories

| Category | Description | Example |
|---|---|---|
| Visual ambiguity | Object or scene is difficult to interpret | low light, occlusion, blur |
| Label ambiguity | Label itself may be uncertain | multi-label scene assigned one class |
| Rare scenario | Uncommon class or environment | unusual viewpoint, novel object |
| Preprocessing issue | Failure caused by resizing/cropping/normalization | object cropped out |
| Model bias | Systematic confusion between classes | road vs pavement |
| Data shift | Test data differs from training data | different sensor/camera |

## VLA-Specific Notes

For VLA systems, errors should also record:

- whether the perception error caused an unsafe action,
- whether the language instruction was misunderstood,
- whether long-horizon reasoning failed,
- whether the action could be explained with visual evidence,
- whether the failure was caused by latency or communication constraints.
