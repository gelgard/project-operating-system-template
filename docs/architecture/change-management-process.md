# Change Management Process

## Status
Mandatory.

## Purpose
Projects created from this template can accept new functionality, refinements, corrections, and plan changes without breaking the approved technical specification, design contract, implementation plan, Stage branch workflow, or final product goal.

No material functionality or authority change may go directly into
implementation until it passes this Change Request process. In-scope defects
and clarifications use bounded TASK-AMENDMENT under the current task.

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

After the user answers, the agent must perform analysis and update all necessary source-of-truth files before issuing or changing implementation tasks.

## Change Classification
Every requested change must be classified as one or more:
- `Refinement` - clarifies or improves the current AI task without changing architecture.
- `Scope Addition` - adds planned behavior inside an existing Requirement ID.
- `Requirement Extension` - adds product behavior not covered by current Requirement IDs.
- `Design Delta` - changes or extends UI/UX beyond the approved design contract.
- `Architecture Change` - affects data flow, persistence, security, integrations, rules, protection, API, WebSocket, runtime flow, or isolation boundaries.
- `Defect Fix` - corrects a bug or mismatch in accepted functionality.
- `Reprioritization` - changes the order of Stage or AI task execution.

## TASK-AMENDMENT

No full CR is needed for an in-scope defect or clarification that preserves the
accepted outcome and boundaries: missing implied edge test, parser/schema
hardening without public-contract change, approved-design correction,
cleanup/lifecycle fix or implementation simplification. Record cause, exact
delta, files and validation in the current closure record; it consumes the
normal correction budget.

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

If the change touches credentials, platform accounts, secrets, env vars, API
keys, database/cache URLs, authentication, deployment variables, RPC endpoints,
monitoring tokens, or integration access, also apply
`docs/architecture/credential-security-process.md`.

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

The project-populated design authority is
`docs/design/approved-design-contract.md` plus its approved source references
and `docs/design/design-tokens.json`.

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

## Source-Of-Truth Propagation Rule
Every accepted Change Request is a technical-specification addendum and must be
recorded in `docs/plans/accepted_change_requests.md`.

It must also have one matching `rule_bindings` entry in
`docs/architecture/governance-trigger-registry.json` defining when the accepted
decision executes. Approval without both projections is not effective
propagation.

Update every affected layer:
- baseline/effective specification and spec-alignment gap plan;
- architecture, system overview, data flow, and assumptions;
- implementation/release/testing plans;
- Requirement IDs and traceability;
- recovery/current status;
- design and user-behavior documentation;
- credential/security process;
- AI tasks/templates and response/process rules.

If a layer needs no change, record that as an explicit impact-analysis result.
Missing propagation blocks implementation and closure.

`обнови архитектурные файлы` must audit recent accepted CRs against every
applicable layer and apply missing deltas without full rewrites.

Before the propagation commit, run
`python3 scripts/validate_governance_contract.py` plus affected
traceability/spec/source checks. Product implementation is a later task/commit.

Rules retained only in a proposed CR or historical recovery file do not
control implementation.

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

The configured implementation agent owns only authorized code implementation
and directly related tests after the change is accepted and packaged.

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
- Do not issue credential-affecting work without complete acquisition and safe
  storage instructions.
- Do not expose secrets in source, markdown, tests, logs, screenshots, or
  committed examples.
- Do not break isolation boundaries.
- Do not turn short visible increments into long invisible backend phases.
- Do not implement Stage work on `master`, `main`, or `develop`.
- Do not generate new populated contextJSON snapshots.
- Do not mark tasks complete while closure gates are open.
