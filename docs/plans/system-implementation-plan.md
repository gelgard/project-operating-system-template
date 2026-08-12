# System Implementation Plan

## Current Stage
{{CURRENT_STAGE}}

## Progress

Completed:
- {{COMPLETED_TASK_RANGE_OR_LIST}}

Current:
- {{CURRENT_AI_TASK}}

Next:
- {{NEXT_AI_TASK_1}}
- {{NEXT_AI_TASK_2}}
- {{NEXT_AI_TASK_3}}

Cross-cutting architecture notes:
- current state originates in project_recovery/00_CURRENT_STATE_MANIFEST.md;
  Stage/status are same-state projections reconciled against actual version control
- executable rules/accepted CRs have bindings in the governance trigger registry
- archives are non-normative evidence and are read only through active pointers
- contextJSON maintenance is no longer part of architecture synchronization
- architecture synchronization is workspace/manifest-first; use an archive
  only when the workspace is inaccessible or explicitly authoritative
- existing timestamped context JSON files are frozen historical external exports only
- no new populated contextJSON snapshots should be generated during architecture sync, context refresh, task issue, or task closure
- contextJSON must not be treated as architecture, process, methodology, testing, validation, or execution authority for the repository
- external reporting/visualization applications must use active source-of-truth files or a future explicitly approved export mechanism
- Fast/Full context restore policy must be enforced before execution
- AI tasks must include Goal Alignment Requirement IDs and evidence-based closure
- every Stage must be implemented on its own branch named `feature/stage-<stage-number>-<stage-name-kebab-case>`
- completed Stage branches merge into `develop`; the next Stage feature branch is created from updated `develop`
- new functionality and functional changes must pass `docs/architecture/change-management-process.md` before implementation
- each task is one vertical Outcome Slice with practical DoR and declared risk
- implementer handoffs are independently audited; maximum two valid corrections
- delivery, Requirement acceptance, milestone and release are separate

Cross-cutting execution responsibility notes:
- configured implementation agent receives only authorized code/refactor and
  directly related test instructions
- planning, architecture reasoning, validation strategy, manual-test orchestration, closure-gate evaluation, next-step planning, and response packaging remain agent-chat responsibilities
- Implementation prompt must not duplicate manual validation, agent-side
  validation plans, architecture ownership or next-step orchestration

Cross-cutting stakeholder summary notes:
- every current/next step must include a short manager-facing summary
- the summary must explain what improves and why it matters in plain non-technical language

Cross-cutting closure notes:
- Task Closure Hard Gate Checklist must pass before any AI task is marked complete
- every UI Outcome gets automated proof; OWNER manually checks only ready
  milestone UI directly in the running app/device
- temporary validation-only artifacts must be deleted after closure unless intentionally kept as evidence
