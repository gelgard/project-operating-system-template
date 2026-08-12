# Full Template Technology-Neutral Governance Audit — 12.08.2026

Status: completed on branch `docs/template-governance-v3-20260812`.

## Audit goal

Ensure a new project with any architecture or technology inherits the proven
development/context operating method without inheriting source-product details.

## Findings and corrections

| ID | Severity | Finding | Correction |
|---|---|---|---|
| TPL-001 | critical | Fast/Full Restore had no single current-state manifest and did not reconcile actual repository/worktree facts. | Added manifest-first Full Restore contract, state_id projections and validator. |
| TPL-002 | critical | “Archive-first” encouraged archives to outrank an available live workspace and allowed stale history to compete with current facts. | Changed to workspace/manifest-first with archive fallback and archive non-authority. |
| TPL-003 | high | Commands existed only as prose; automatic event triggers and accepted-CR activation were not mechanically checked. | Added JSON command/event/rule registry plus structural validator. |
| TPL-004 | high | “Small tasks only”, universal option comparison and broad manual UI checks could create meta-work, invisible layers and repeated corrections. | Replaced with vertical Outcome Slice, practical DoR, material option analysis and milestone OWNER UI. |
| TPL-005 | high | Validation was not explicitly risk-classed and could force either too little or repeated full regression. | Added Standard/Sensitive/Integration-Release gates and lower-gate stop. |
| TPL-006 | high | Cursor was hardcoded rather than configuring an implementation agent and transport authority. | Added implementation-agent plus OWNER_MEDIATED/DIRECT_ALLOWED project binding and independent audit. |
| TPL-007 | high | No two-correction budget or invalid-transport semantics. | Added maximum two valid passes; truncated/no-edit transport consumes none. |
| TPL-008 | medium | Producer PASS, delivery, Requirement acceptance, milestone and release state were not clearly separated. | Added task state/closure semantics and separate traceability projections. |
| TPL-009 | medium | OWNER was asked for manual UI validation on every UI task. | OWNER now validates only ready milestone UI directly in running app/device; agents own automation. |
| TPL-010 | medium | CR propagation did not require a trigger binding. | Accepted register and trigger binding must match before implementation. |
| TPL-011 | medium | Stage merge lacked isolated candidate and post-merge canary. | Added normal merge candidate/canary/Full Restore sequence. |
| TPL-012 | medium | No explicit architecture/technology portability mapping. | Added bootstrap mapping for build, scenario, storage, UI/device, external state, release and evidence. |
| TPL-013 | critical | Template traceability imposed dashboard/alerts/history/UI product IDs on every derived project. | Replaced them with project-populated product IDs plus only universal governance IDs; non-UI is explicit N/A. |
| TPL-014 | high | A derived project could omit part of the operating-system file set while the structural validator still passed. | Added a required OS file manifest in the validator and a project inheritance acceptance checklist. |
| TPL-015 | high | Trigger prose required evidence, but the machine registry did not, and accepted-CR bindings lacked a complete-row validator. | Trigger schema v2 now requires evidence on commands/events and complete fail-closed accepted-rule bindings. |
| TPL-016 | high | Optional `.cursor/commands` could initiate small/post-hoc work without the active task, DoR, transport authority or independent closure. | Converted adapters into guarded technology-neutral entry points and added them to the required OS file set. |
| TPL-017 | critical | Context projection still required an archive upload and ranked all recovery history above the live manifest; specialized recovery prompts bypassed the common restore. | Made live workspace/manifest authoritative, added state_id to project context, and routed GTM/brand/visual modes through Fast/Full Restore. |

## Inherited universal mechanisms

- source-of-truth priority and conflict stop;
- current-state manifest and actual version-control reconciliation;
- command/event trigger registry and accepted-CR bindings;
- architecture-first planning and controlled CR propagation;
- one vertical Outcome Slice and practical DoR;
- selected-entity identity preservation;
- risk-proportional independent validation;
- configurable implementation-agent transport;
- maximum two valid corrective passes;
- direct ready-product OWNER walkthrough only when applicable;
- credential/external/destructive authority, budgets and rollback;
- commit/push/merge/canary/restore closure;
- archive non-authority and frozen historical exports;
- delivery versus acceptance versus release separation.

## Technology-neutral inheritance test

A derived project passes only when it can map the universal concepts to its
actual architecture without deleting them. Valid examples include:

- browser/UI scenario, native-device scenario, CLI behavior, API contract,
  background worker, data pipeline, infrastructure deployment or firmware
  observation;
- SQL, document, object, memory, file, queue or device persistence with its own
  rollback semantics;
- monorepo, multi-repo or explicitly accepted alternative to Stage branches,
  provided isolation, normal integration, exact identity, canary and recovery
  remain.

The template must not force a language, framework, cloud, database, provider,
chart library, domain, screen set, task number, Requirement ID or live service.

## Validation

Run in the template:

```bash
python3 scripts/validate_governance_contract.py
```

When synchronizing from a real source project, add repeated `--forbid TOKEN`
arguments for source identity, provider, product, branch/task and technology
names. After bootstrap set `template_mode=false`, replace required
placeholders, populate CR bindings and run the same validator again.

The structural validator does not replace stack-specific builds/tests,
security analysis, runtime proof or human milestone acceptance.
