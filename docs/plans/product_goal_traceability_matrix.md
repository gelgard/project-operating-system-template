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
- Runtime truth comes from latest contextJSON snapshot
- AI tasks are executable units with deterministic acceptance and test evidence

## Requirement IDs
- PG-RT-001 Runtime truth and projection integrity
- PG-OV-001 User-visible operational overview
- PG-AR-001 Alerting and risk/status visibility
- PG-HI-001 History/timeline visibility
- PG-UX-001 UX/i18n consistency
- PG-EX-001 Execution discipline and recoverability

## Stage Coverage Map
| Requirement ID | Stage | Implementing AI Tasks | Current Coverage |
| --- | --- | --- | --- |
| PG-RT-001 | Stage X | AI Task XXX | pending |
| PG-OV-001 | Stage X | AI Task XXX | pending |
| PG-AR-001 | Stage X | AI Task XXX | pending |
| PG-HI-001 | Stage X | AI Task XXX | pending |
| PG-UX-001 | Stage X | AI Task XXX | pending |
| PG-EX-001 | Stage X | AI Task XXX | pending |

## AI Task Alignment Protocol (Mandatory)
- Every AI task must map to one or more Requirement IDs from this file.
- Missing mapping => task is BLOCKED.
- Acceptance must include measurable checks/evidence for each mapped Requirement ID.

## Current Task Anchor
- Current AI task: AI Task XXX
- Requirement IDs:
  - PG-EX-001

## Audit Checklist
1. Current stage/task in recovery matches plan and ai_tasks.
2. Every active/completed AI task has Goal Alignment mapping.
3. Acceptance evidence exists for mapped Requirement IDs.
4. contextJSON latest snapshot aligns with recovery and architecture.
5. No drift between architecture rules and response format rules.
6. Stage branch flow was respected when Stage changed.
7. Commit message provided after full validation of current AI task.
8. Context Restore Policy is respected:
   - Fast restore before each new AI task
   - Full restore after architecture sync / merge/stage transition / desync / long pause / `обнови полный контекст`
