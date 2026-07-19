# Public Evidence and Claim Boundaries

This page is a reviewer-oriented index of what can be verified in the repository.

## Strongest public evidence

1. **Reproducible diagnostics package** — source code, CLI, deterministic benchmark, quality-gate configuration, tests, reports, SVG dashboards and CI workflow.
2. **Physical UAV field-test media** — two original MP4 files, representative frames, media metadata and SHA-256 hashes.
3. **Real-video quality audit** — decoded image metrics over both released clips, with per-frame CSV and input hashes.
4. **Safety-aware mission interface** — structured mission output and a deterministic validator that rejects missing fail-safe behavior.

## Evidence policy

Every quantitative statement should be traceable to a committed result file and a command that regenerates it. Simulated values are labelled as benchmark results. Field-test media are described only as evidence of physical platform testing, not as proof of autonomous performance.

## Project status

| Project | Public maturity | Recommended reviewer entry point |
|---|---|---|
| UAV multi-sensor integrity and trajectory diagnostics | Reproducible software project | `projects/03-.../README.md` |
| AI-agent-assisted UAV system | Ongoing MSc work with field-test evidence | `projects/01-.../README.md` |
| UAV field-test video quality audit | Reproducible analysis of released real media | `projects/02-uav-flight-video-quality-audit/README.md` |

Confidential dissertation logs, third-party data and unpublished hardware details are intentionally excluded. Where those materials are necessary for a claim, the claim is marked as ongoing rather than implied by a public placeholder.
