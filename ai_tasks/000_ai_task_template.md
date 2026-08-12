# AI Task XXX — {{OUTCOME_SLICE_NAME}}

Status: {{PLANNED_OR_ISSUED}}

Chain ID: {{CHAIN_ID}}

## Stage / Capability

{{STAGE_OR_CAPABILITY}}

## User/System Outcome

{{ONE_OBSERVABLE_OUTCOME_AND_WHY_IT_MATTERS}}

## Manager Summary

{{SHORT_NON_TECHNICAL_VALUE_SUMMARY}}

## Goal Alignment

- Requirement/Journey/Surface: {{IDS}}
- Delivery state at issue: {{STATE}}
- Acceptance state at issue: {{STATE}}

## Practical DoR

- authoritative input: {{INPUT}}
- exact selected identity: {{IDENTITY_OR_NA}}
- production entry/path: {{ENTRY_TO_OBSERVABLE_RESULT}}
- risk: {{STANDARD_SENSITIVE_OR_INTEGRATION_RELEASE}}
- applicable design/accessibility: {{CONTRACT_OR_NA}}
- external prerequisite/authority now: {{READY_OR_BLOCKER}}
- rollback for persistent/destructive change: {{ROLLBACK_OR_NA}}
- automated observable proof: {{SCENARIO}}
- milestone/OWNER walkthrough: {{REQUIRED_NOW_LATER_OR_NA}}

## Scope

Create/update:
- {{AUTHORIZED_PATH_OR_BOUNDARY}}

Do not update/do:
- {{EXCLUSIONS}}
- historical exports/archives unless explicitly authorized
- architecture/plans/recovery unless this is a documentation task

Advisory size: 80–180 task lines and normally <=20 related files.

Indivisibility reason if exceeded: {{REASON_OR_NA}}

## Required Behavior / Acceptance

1. {{CRITERION_WITH_OBSERVABLE_EVIDENCE}}
2. {{CRITERION_WITH_OBSERVABLE_EVIDENCE}}
3. {{NEGATIVE_OR_FAIL_CLOSED_CRITERION}}

## Анализ частностей и выбор решения

- invariants/unavailable scope: {{DETAILS}}
- applicable input/zero-one-many/duplicate risks: {{DETAILS_OR_NA}}
- selected identity/entry points: {{DETAILS_OR_NA}}
- ordering/concurrency/restart/persistence: {{DETAILS_OR_NA}}
- provider/external/partial/hostile failure: {{DETAILS_OR_NA}}
- material options: {{OPTIONS_OR_NO_MATERIAL_CHOICE}}
- minimum sufficient choice: {{CHOICE}}
- new abstraction and second consumer: {{CONSUMERS_OR_NONE}}
- assumptions and guards: {{ASSUMPTIONS_OR_NONE}}

## Credentials / External Authority

{{NO_NEW_CREDENTIAL_OR_COMPLETE_ACQUISITION_STORAGE_LEAST_PRIVILEGE_VALIDATION_BUDGET_ROLLBACK_ROTATION}}

## Implementation-Agent Scope

Implement only the authorized production change and directly related tests.
Do not own architecture, planning, independent validation, live/manual actions,
closure, commits beyond explicit scope or next-task issue.

Transport mode: {{OWNER_MEDIATED_OR_DIRECT_ALLOWED}}.

## Layered Validation

Focused/static/build:

```bash
{{COMMAND}}
```

Affected regression/adversarial/native/live only when required by risk:

```bash
{{COMMAND_OR_NOT_REQUIRED}}
```

Automated observable/UI proof:

```bash
{{COMMAND_OR_NA}}
```

Final diff/secret/cleanup:

```bash
{{COMMAND}}
```

## Required Implementer Handoff

```text
SELF-REVIEW
Outcome and production path: PASS/BLOCKED -> evidence
Criterion matrix: each criterion -> PASS/BLOCKED -> file/test/evidence
Failed or unrun gates: exact list
Allowed/forbidden diff: verdict and actual changed files
Hardcoded/fixture-only success scan: verdict
Secret/identity/raw-error scan: verdict
Cleanup/rollback/residuals: verdict
Abstractions and consumers: list/none
Over-engineering scan: verdict
Staging/commit state: exact
Exact blocker: none or one precise blocker
```

Implementer PASS is handoff input only. Independent manager audit decides the
next canonical state. Maximum two valid corrective implementation passes.

## Closure Gate

- Full/Fast Restore and governance validator passed;
- actual branch/worktree/authorized diff verified;
- production Outcome Slice works;
- risk-proportional validation and automated proof pass;
- applicable direct OWNER UI walkthrough passes;
- no in-scope gap or unsafe residual remains;
- delivery/acceptance traceability updated separately;
- commit/push succeeds unless explicit local-only mode applies.
