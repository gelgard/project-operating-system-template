# AI Task XXX — {{TASK_NAME}}

## Stage
{{STAGE}}

## Substage
{{SUBSTAGE}}

## Goal
{{GOAL}}

## Why This Matters
{{WHY_THIS_TASK_EXISTS}}

## Manager-Facing Summary
{{SHORT_NON_TECHNICAL_SUMMARY_OF_WHAT_IMPROVES_AND_WHY_IT_MATTERS}}

## Goal Alignment
Requirement IDs (from docs/plans/product_goal_traceability_matrix.md):
- {{REQUIREMENT_ID_1}}
- {{REQUIREMENT_ID_2}}

## Files to Create / Update
Create:
- {{FILE_TO_CREATE_1}}

Update:
- {{FILE_TO_UPDATE_1}}

Do not update:
- contextJSON files unless a future architecture decision explicitly reintroduces JSON export generation

## Acceptance Criteria
- {{CRITERIA_1}} (maps to {{REQUIREMENT_ID_1}})
- {{CRITERIA_2}} (maps to {{REQUIREMENT_ID_2}})
- {{CRITERIA_3}}

## Manual Test
{{MANUAL_TEST_SUMMARY}}

## UI Visual Test
Required when task has UI scope:
- User action: {{EXACT_UI_ACTION}}
- Expected visible result: {{EXPECTED_VISIBLE_RESULT}}
- Negative/error-state check: {{EXPECTED_ERROR_OR_EMPTY_STATE_RESULT}}

## Agent Validation
- {{TERMINAL_OR_CODE_TEST_COMMAND_AND_EXPECTED_RESULT}}
- Playwright visual validation required for UI-scope tasks:
  - Step: {{PLAYWRIGHT_VISUAL_STEP}}
  - Observed result: {{PASS_OR_FAIL}}
  - Visual mismatches: {{NONE_OR_LIST}}

## Closure Gate
- Context/restore gate passed for required restore mode: {{YES_NO}}
- Goal Alignment + Requirement IDs present and valid: {{YES_NO}}
- Scope/baseline gate passed: {{YES_NO}}
- Agent validation passed: {{YES_NO}}
- User manual validation passed: {{YES_NO}}
- No open in-scope validation gaps remain: {{YES_NO}}
- Temporary validation-only artifacts deleted or intentionally kept as evidence: {{YES_NO}}
- Commit message provided after all gates pass: {{YES_NO}}
