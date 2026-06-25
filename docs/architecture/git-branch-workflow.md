# Git Branch Workflow

## Status
Mandatory.

## Core Rule
Every Stage must be developed in its own feature branch.

Branch naming format:

```text
feature/stage-<stage-number>-<stage-name-kebab-case>
```

Examples:
- `feature/stage-1-architecture-foundation`
- `feature/stage-2-core-runtime`
- `feature/stage-3-product-surface`

## Develop Branch
`develop` is the integration branch for completed stages.

When a Stage is complete:
1. finish validation and closure gates for the Stage
2. commit all Stage work on that Stage feature branch
3. merge the Stage feature branch into `develop`
4. create the next Stage feature branch from updated `develop`
5. continue work only on the new Stage feature branch

## Prohibited
- Do not implement Stage work directly on `main`.
- Do not implement Stage work directly on `develop`.
- Do not continue a new Stage on the previous Stage feature branch.
- Do not start a Stage without creating or switching to its corresponding feature branch.
- Do not merge an incomplete Stage into `develop`.

## Authority
This file defines the mandatory git workflow for all future development unless explicitly superseded by a newer architecture rule.
