# AI Task XXX - {{TASK_NAME}}

Status: {{ISSUED_OR_PLANNED}}

## Stage
{{STAGE}}

## Goal
{{GOAL}}

## Manager-Facing Summary
{{SHORT_NON_TECHNICAL_SUMMARY_OF_WHAT_IMPROVES_AND_WHY}}

## Goal Alignment
- {{REQUIREMENT_ID_1}}
- {{REQUIREMENT_ID_2}}

## Scope
Create:
- {{FILE_TO_CREATE}}

Update:
- {{FILE_TO_UPDATE}}

Do not update:
- {{OUT_OF_SCOPE_BOUNDARY}}
- contextJSON unless an accepted architecture decision explicitly reintroduces generation

## Required Behavior
1. {{BEHAVIOR_1}}
2. {{BEHAVIOR_2}}

## Acceptance Criteria
- {{CRITERION_1}}
- {{CRITERION_2}}
- Applicable edge conditions are tested or guarded.

## Анализ частностей и выбор решения
Task understanding:
- Required: {{EXACT_REQUIREMENT}}
- Invariants: {{INVARIANTS}}
- Out of scope: {{EXCLUSIONS}}

Edge conditions (`applicable` / `not applicable` with reason):
- Zero/one/many/duplicates: {{STATUS_AND_REASON}}
- Explicit non-latest entity selection: {{STATUS_AND_REASON}}
- Entry points/callers: {{STATUS_AND_REASON}}
- Delayed/repeated/out-of-order events: {{STATUS_AND_REASON}}
- Concurrency/redeploy overlap: {{STATUS_AND_REASON}}
- Restart/lost in-memory state: {{STATUS_AND_REASON}}
- Partial failure/retry/idempotency: {{STATUS_AND_REASON}}
- Invalid/boundary/hostile input: {{STATUS_AND_REASON}}

Options:
- Option A: {{OPTION_A_CORRECTNESS_SECURITY_PERFORMANCE_COMPLEXITY}}
- Option B: {{OPTION_B_CORRECTNESS_SECURITY_PERFORMANCE_COMPLEXITY}}

Chosen solution:
- {{CHOICE_AND_WHY}}

Assumptions and guards:
- {{ASSUMPTION_OR_NONE}}

## Credentials And Security Instructions
Include this section only when credentials/platform access are required. State
provider acquisition, exact env names, ignored local storage, deploy-side secret
storage, least privilege, validation, rotation/revocation, and non-commit rules.
If no credentials are needed: `No new credential or platform setup is required.`

## Agent Validation
Focused:
```bash
{{FOCUSED_TEST_COMMAND}}
```

Full regression when required by risk/scope:
```bash
{{FULL_REGRESSION_COMMAND_OR_NOT_REQUIRED}}
```

```bash
git diff --check
```

## Agent Visual Check
Required for UI scope:
- viewports/pages/states: {{CHECKED_SCOPE}}
- result: {{PASS_FAIL}}
- mismatches/fixes: {{NONE_OR_LIST}}

## User Visual Check Instructions
Required for UI scope:
1. {{EXACT_USER_ACTION}}
   Expected: {{EXPECTED_RESULT}}
2. {{NEGATIVE_OR_ERROR_STATE_ACTION}}
   Expected: {{EXPECTED_RESULT}}

## Closure Gate
- Required restore passed: {{YES_NO}}
- Requirement mapping valid: {{YES_NO}}
- Scope/baseline passed: {{YES_NO}}
- Agent validation passed: {{YES_NO}}
- Required user/manual/visual validation passed: {{YES_NO}}
- No open in-scope gaps: {{YES_NO}}
- Temporary artifacts removed/retained as intentional evidence: {{YES_NO}}
- `git diff --check` and secret-safety diff passed: {{YES_NO}}
- Task changes auto-committed on Stage feature branch: {{YES_NO}}

## Cursor Scope
Implement only code and directly related code tests in this task. Do not own
architecture, plans, recovery, manual/live validation, deployment, closure, or
next-task packaging unless explicitly listed as code scope.
