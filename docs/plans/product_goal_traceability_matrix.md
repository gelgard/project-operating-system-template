# Product Goal Traceability Matrix

## Purpose

Guarantee that every task contributes to the canonical project goal and that
delivery, Requirement acceptance, milestone and release state can be audited.

## Project-populated product goal

{{CANONICAL_PRODUCT_OR_SYSTEM_GOAL}}

## Project-populated Requirement IDs

{{PRODUCT_DOMAIN_SECURITY_DATA_UX_OPERATION_REQUIREMENT_IDS}}

Do not inherit product Requirement IDs from the template or source project.
Create IDs from the new project's approved specification. A non-UI project
does not create UI/screen requirements merely because the template supports UI
work.

## Universal governance IDs

- GOV-EX-001 — execution discipline, independent validation and recoverability;
- GOV-CTX-001 — current-state manifest, Full Restore and archive integrity;
- GOV-CHANGE-001 — CR intake, trigger binding and propagation;
- GOV-SEC-001 — credential/external/destructive authority and secret safety;
- GOV-DESIGN-001 — approved design and direct ready-product human validation
  when a user-facing surface exists; otherwise explicitly N/A.

These governance IDs prove process compliance. They do not substitute for the
new project's product requirements.

## Stage / Capability Coverage

| Requirement ID | Stage/Capability | Outcome Slice | Delivery | Acceptance | Evidence |
|---|---|---|---|---|---|
| {{REQ_ID}} | {{STAGE}} | {{TASK_OR_OUTCOME}} | pending | pending | none |
| GOV-EX-001 | all | governance process | active | pending | none |
| GOV-CTX-001 | all | restore/sync | active | pending | none |
| GOV-CHANGE-001 | all | CR process | active | pending | none |
| GOV-SEC-001 | affected work | security authority | pending | pending | none |
| GOV-DESIGN-001 | user-facing work or N/A | design/validation | pending/N/A | pending/N/A | none |

## Task Alignment Protocol

- Every task maps to at least one project Requirement plus applicable GOV IDs.
- Missing mapping blocks issue.
- Each mapped row has measurable evidence and separates delivery/acceptance.
- One task normally equals one vertical Outcome Slice with practical DoR and
  declared Standard/Sensitive/Integration-Release risk.
- Exact selected identity is preserved through the production path.
- Implementation prompts stay implementation-only; manager-agent owns
  planning, independent validation, closure and orchestration.
- UI/device work gets automated proof; OWNER manually checks only ready
  milestone behavior directly in the running product.
- Material changes use CR; in-scope defects use TASK-AMENDMENT.

## Current anchor

- state_id: {{UNIQUE_MONOTONIC_STATE_ID}}
- current Stage/capability: {{CURRENT_STAGE_OR_CAPABILITY}}
- active task: {{TASK_ID_OR_NONE}}
- correction count: {{COUNT}}/2
- current delivery/acceptance: {{SEPARATE_STATES}}

## Audit checklist

1. Manifest, Stage/status, plan and actual repository agree.
2. Active/completed tasks have valid Requirement mappings and evidence.
3. Delivery, acceptance, milestone and release are not conflated.
4. Accepted CR IDs equal trigger bindings and affected propagation passed.
5. Archive/context exports did not activate rules or override current state.
6. Required restore type and governance validator passed.
7. Branch/integration/canary workflow or accepted equivalent was respected.
8. Implementation handoff was independently audited; correction count valid.
9. Applicable credential/design/security contracts passed.
10. Cleanup, diff/secret checks, commit/push and evidence identity passed.
