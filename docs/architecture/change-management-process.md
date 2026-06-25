# Change Management Process

## Status
Mandatory.

## Purpose
Projects created from this template can accept new functionality, refinements, corrections, and plan changes without breaking the approved technical specification, design contract, implementation plan, Stage branch workflow, or final product goal.

No new functionality or functional change may go directly into implementation until it passes the Change Request process in this file.

## Trigger Commands
The following user commands start Change Request Intake:
- `необходимо внести изменения`
- `вносим изменения`
- `надо внести изменения`
- `нужно внести изменения`
- `необходимо внести правки`
- `внеси изменения`
- any close phrasing with the same meaning

Command matching is intent-based, not literal-only.

## Required First Response
When a trigger command is received, the agent must not start coding and must not create an AI task immediately.

The agent must first return this intake form:

```text
Добавить Change Request:
1. Название изменения:
2. Что нужно добавить или изменить:
3. Почему это нужно пользователю или продукту:
4. К какому экрану, модулю, сценарию или Stage относится:
5. Это уже есть в ТЗ или это расширение ТЗ:
6. Это уже есть в утвержденном дизайне или требует design delta:
7. Влияет ли на integrations, credentials, rules, protection, persistence, account isolation, API/WebSocket, security, or runtime flow:
8. Срочность: сейчас / текущий Stage / позже:
9. Есть ли ограничения, примеры, ссылки, скриншоты или желаемое поведение:
```

After the user answers, the agent must perform analysis and update the necessary source-of-truth files before issuing or changing implementation tasks.

## Change Classification
Every requested change must be classified as one or more:
- `Refinement` - clarifies or improves the current AI task without changing architecture.
- `Scope Addition` - adds planned behavior inside an existing Requirement ID.
- `Requirement Extension` - adds product behavior not covered by current Requirement IDs.
- `Design Delta` - changes or extends UI/UX beyond the approved design contract.
- `Architecture Change` - affects data flow, persistence, security, integrations, rules, protection, API, WebSocket, runtime flow, or isolation boundaries.
- `Defect Fix` - corrects a bug or mismatch in accepted functionality.
- `Reprioritization` - changes the order of Stage or AI task execution.

## Impact Analysis Gate
Before implementation, the agent must analyze impact on:
- canonical product goal
- technical specification
- approved design / UX references
- Requirement IDs and traceability
- current Stage and current AI task
- next task sequence
- security and credential boundaries
- data model and isolation boundaries
- runtime flow and integration boundaries
- validation strategy and closure gates
- git Stage branch workflow
- manager-facing delivery story

The decision must be one of:
- `fits current task`
- `new AI task in current Stage`
- `future AI task`
- `plan update required`
- `blocked`

## Design Alignment Gate
If a change affects UI:
- if it already exists in the approved design contract, implement strictly from that contract
- if it is not in the approved design, record it as a design delta before implementation
- if it contradicts the approved design, block implementation until a new approved design or explicit architecture exception exists

Temporary UI shapes are forbidden.

## Traceability Gate
Every accepted change must map to existing Requirement IDs or create a new Requirement ID in `docs/plans/product_goal_traceability_matrix.md`.

Missing Requirement ID mapping blocks implementation.

## Plan Recomposition Rule
If a change affects order, scope, Stage boundaries, or delivery sequence:
- preserve the final product goal
- preserve short visible increments where applicable
- update affected architecture, plan, recovery, and task files
- state what moved and why
- state how quality and final scope remain protected

Plan changes must be controlled deltas, not informal task drift.

## Task Packaging Rule
After analysis, an accepted change must be packaged as exactly one of:
- refinement inside the current AI task
- new numbered AI task in the current Stage
- future numbered AI task
- architecture update package before implementation
- blocked decision with required fix

No change may be implemented as an untracked side effect.

## Implementation Ownership
The agent owns:
- change classification
- impact analysis
- architecture and plan updates
- Requirement ID mapping
- validation strategy
- manual test strategy
- closure gate evaluation
- task packaging

Cursor owns only code implementation after the change is accepted and packaged.

## Required Response After User Answers
After receiving a completed Change Request, the agent must respond with:

```text
Change classification:
Impact analysis:
Requirement IDs:
Design impact:
Architecture impact:
Plan impact:
Decision:
Required architecture/source-of-truth updates:
Proposed task placement:
Readiness: ready/blocked
```

If ready, the agent then updates all necessary source-of-truth files and commits the architecture/plan changes. Only after that may a current-task refinement or next AI task package be issued.

## Non-Negotiable Boundaries
- Do not bypass the approved design contract.
- Do not weaken integration/security boundaries.
- Do not store credentials insecurely.
- Do not break isolation boundaries.
- Do not turn short visible increments into long invisible backend phases.
- Do not implement Stage work on `main` or `develop`.
- Do not generate new populated contextJSON snapshots.
- Do not mark tasks complete while closure gates are open.
