# Product Goal Traceability Matrix

## Purpose
Guarantee that every AI task directly contributes to canonical product goals and can be audited.

## Canonical Product Goal
Define and deliver the intended end-state product behavior with architecture-first control, measurable acceptance, and recoverable execution.

## UI Target (End-State)
- User-facing dashboard/surfaces reflect real system state from runtime truth.
- Key status, progress, alerts, and history are visible and testable.
- Localization and UX consistency are preserved across screens.

## Constraint Baseline (Non-Negotiable)
- Architecture-first workflow
- Recovery layer is mandatory
- Source-of-truth priority is strict
- Git Stage branch workflow is mandatory: Stage work happens on `feature/stage-<stage-number>-<stage-name-kebab-case>`, completed Stages merge into `develop`, and next Stage branches are created from updated `develop`
- contextJSON is a frozen historical external export only and is no longer generated during sync
- contextJSON must not define architecture, process, methodology, testing, validation, or execution rules
- AI tasks are executable units with deterministic acceptance and test evidence
- Cursor prompts are implementation-only; planning, architecture, validation strategy, manual-test orchestration, closure gates, and response packaging remain agent-owned
- every current/next AI step includes a brief manager-facing summary
- task closure is forbidden until the Task Closure Hard Gate Checklist passes
- every task follows engineering edge-condition analysis and real option comparison
- lean/token-controlled reporting cannot reduce validation quality
- credential/platform work follows the mandatory credential-security process
- accepted Change Requests are effective-specification addenda propagated to every affected source-of-truth layer
- successful task closure automatically commits task-scoped changes on the Stage feature branch

## Requirement IDs
- PG-RT-001 Runtime truth and projection integrity
- PG-OV-001 User-visible operational overview
- PG-AR-001 Alerting and risk/status visibility
- PG-HI-001 History/timeline visibility
- PG-UX-001 UX/i18n consistency
- PG-EX-001 Execution discipline and recoverability
- PG-CTX-001 Historical contextJSON archive integrity and no-new-generation policy
- PG-CHANGE-001 Controlled change intake, impact analysis, traceability, and plan insertion process
- PG-SEC-001 Credential, secret, dependency, and public-runtime security discipline
- PG-DESIGN-001 Approved-design and agent/user visual-validation discipline

## Stage Coverage Map
| Requirement ID | Stage | Implementing AI Tasks | Current Coverage |
| --- | --- | --- | --- |
| PG-RT-001 | Stage X | AI Task XXX | pending |
| PG-OV-001 | Stage X | AI Task XXX | pending |
| PG-AR-001 | Stage X | AI Task XXX | pending |
| PG-HI-001 | Stage X | AI Task XXX | pending |
| PG-UX-001 | Stage X | AI Task XXX | pending |
| PG-EX-001 | Stage X | AI Task XXX | pending |
| PG-CTX-001 | All architecture syncs | AI Task XXX | pending |
| PG-CHANGE-001 | All stages | architecture process active | pending |
| PG-SEC-001 | All affected stages | AI Task XXX | pending |
| PG-DESIGN-001 | Every UI stage | AI Task XXX | pending |

## AI Task Alignment Protocol (Mandatory)
- Every AI task must map to one or more Requirement IDs from this file.
- Missing mapping => task is BLOCKED.
- Acceptance must include measurable checks/evidence for each mapped Requirement ID.
- Every AI task must include a manager-facing summary explaining the user/product value in non-technical language.
- Prompt for Cursor must stay development-only and must not duplicate agent-owned planning, architecture, validation strategy, manual testing, closure, or response-format work.
- UI-scope tasks require both Playwright visual validation by the agent and manual user-side visual validation steps.
- Any new functionality or functional change must pass `docs/architecture/change-management-process.md` before implementation.
- Change requests must map to existing Requirement IDs or create a new Requirement ID before implementation.
- Every task includes `Анализ частностей и выбор решения`.
- Credential and UI tasks include PG-SEC-001 / PG-DESIGN-001 when applicable.

## Current Task Anchor
- Current AI task: AI Task XXX
- Requirement IDs:
  - PG-EX-001

## Audit Checklist
1. Current stage/task in recovery matches plan and ai_tasks.
2. Every active/completed AI task has Goal Alignment mapping.
3. Acceptance evidence exists for mapped Requirement IDs.
4. contextJSON is not regenerated and is treated only as a frozen historical archive.
5. No drift between architecture rules and response format rules.
6. Stage branch flow was respected when Stage changed.
7. Task-scoped changes automatically committed after successful closure validation.
8. Context Restore Policy is respected:
   - Fast restore before each new AI task
   - Full restore after architecture sync / merge/stage transition / desync / long pause / `обнови полный контекст`
   - typo alias `обнови полный контест` also forces Full restore
9. Task Closure Hard Gate Checklist fully passed before completion.
10. Temporary validation-only files deleted unless intentionally kept as evidence.
11. Change Request process was enforced for any new functionality or functional change.
12. Accepted Change Requests were recorded in accepted_change_requests.md and fully propagated.
13. Credential/design/engineering/lean contracts were applied where relevant.
