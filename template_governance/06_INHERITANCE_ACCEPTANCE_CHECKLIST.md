# Technology-Neutral Inheritance Acceptance Checklist

Use this checklist before the first implementation task in every repository
created from this template. A copied directory is not an inherited operating
system until every applicable row is `PASS` or explicitly justified `N/A`.

## 1. Project identity and authority

- [ ] Product identity, repository, owners and message prefix are populated.
- [ ] The effective specification and requirement register are named.
- [ ] Source priority is explicit; conflicts stop work instead of being guessed.
- [ ] Historical archives, rejected CRs and superseded tasks are non-authoritative.

## 2. Current-state restoration

- [ ] `project_recovery/00_CURRENT_STATE_MANIFEST.md` has a unique `state_id`.
- [ ] Branch, worktree, HEAD and dirty/staged facts are read from version control.
- [ ] Stage, active task, correction count, next action and evidence are populated.
- [ ] The same `state_id` appears in Stage, status, Full Restore and traceability projections.
- [ ] Fast Restore and Full Restore have distinct triggers and bounded read sets.
- [ ] Compaction, handoff, long pause, merge and suspected drift force Full Restore.

## 3. Trigger reachability

- [ ] Every supported user command maps to one exact action.
- [ ] Every automatic lifecycle event maps to one fail-closed action.
- [ ] Every accepted CR has an active `rule_bindings` row.
- [ ] No active rule exists only in archive prose.
- [ ] `python3 scripts/validate_governance_contract.py` passes in project mode.

## 4. Delivery and task quality

- [ ] The next task is one observable Outcome Slice, not an isolated technical layer.
- [ ] DoR identifies production path, consumer, data/evidence and rollback.
- [ ] Requirement delivery, acceptance, milestone and release are separate states.
- [ ] The implementation-agent transport mode is explicit and enforceable.
- [ ] Implementer reports are independently audited against the actual diff and gates.
- [ ] Maximum two valid corrective passes is enforced; truncated/no-edit prompts do not consume one.

## 5. Architecture and technology mapping

- [ ] Build/package/start commands are mapped to the actual stack or explicit N/A.
- [ ] A real scenario is mapped to the product surface: UI, device, CLI, API,
  worker, pipeline, firmware or infrastructure.
- [ ] Persistence, migration, rollback and recovery match the chosen architecture.
- [ ] External providers/accounts/devices/environments have authority and run budgets.
- [ ] Version-control isolation, integration, canary and rollback match the repository model.
- [ ] No source project's domain, provider, technology, task ID, branch or evidence leaked in.

## 6. Validation and acceptance

- [ ] Risk is classified as Standard, Sensitive or Integration/Release.
- [ ] The smallest sufficient lower gates run before expensive/live gates.
- [ ] Security, secret, identity, cleanup and changed-scope checks are explicit.
- [ ] OWNER performs only applicable ready-product milestone UI/device walkthroughs.
- [ ] Non-UI projects explicitly mark human visual acceptance N/A and provide runtime evidence.
- [ ] Commit/push/merge occur only after closure and are followed by a canary and Full Restore.

## 7. Portability canary

Create a disposable copy, set `template_mode=false`, populate its project
bindings and current-state projections, then run the validator. The canary must
pass without deleting governance contracts or adding a source-specific
exception. Finally run stack-specific validation defined by the derived project.

Failure in sections 1–7 blocks the first implementation task. Fix the template
mapping or record an approved CR; do not silently weaken the inherited rule.
