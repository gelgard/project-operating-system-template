# CURRENT STATE MANIFEST

state_schema: 1

state_id: {{UNIQUE_MONOTONIC_STATE_ID}}

as_of: {{ISO_8601_WITH_TIMEZONE}}

authority: current factual projection only

## Repository

- canonical repository: {{REPOSITORY_PATH_OR_URL}}
- integration/publishing strategy: {{BRANCH_STRATEGY}}
- active branch/worktree/HEAD: {{ACTIVE_BRANCH_WORKTREE_HEAD}}
- dirty/staged state: read actual version-control state during restore

## Stage and task

- current Stage/capability: {{CURRENT_STAGE_OR_CAPABILITY}}
- active task: {{TASK_ID_OR_NONE}}
- chain ID: {{CHAIN_ID_OR_NONE}}
- state: {{PLANNED_ISSUED_HANDOFF_AUDIT_ACCEPTED_CLOSED_OR_BLOCKED}}
- task contract: {{ACTIVE_TASK_PATH_OR_NONE}}
- closure record: {{CLOSURE_RECORD_PATH_OR_NONE}}
- valid corrective implementation passes: {{COUNT}}/2
- next authorized action: {{ONE_ACTION}}

## Delivery and authority

- Outcome Slice: {{VISIBLE_OR_SYSTEM_OUTCOME}}
- risk: {{STANDARD_SENSITIVE_OR_INTEGRATION_RELEASE}}
- Requirement/TEST delivery: {{DELIVERY_STATE}}
- Requirement/TEST acceptance: {{ACCEPTANCE_STATE}}
- milestone/release state: {{MILESTONE_AND_RELEASE_STATE}}
- external/live/destructive budget: {{BUDGET_OR_NONE}}
- pending OWNER action: {{ACTION_OR_NONE}}

## Evidence pointers

- current implementation plan: `docs/plans/system-implementation-plan.md`
- traceability: `docs/plans/product_goal_traceability_matrix.md`
- accepted CR register: `docs/plans/accepted_change_requests.md`
- active evidence: {{CURRENT_EVIDENCE_PATHS_OR_NONE}}

## Archive boundary

Unlisted recovery records and superseded/rejected materials are historical
evidence only. They cannot override this manifest or activate a rule. Actual
repository drift blocks work and requires factual synchronization; restore
never stashes, resets or deletes user changes.
