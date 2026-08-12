# Full Context Restore Contract

Status: mandatory and read-only.

## Outcome

After `обнови полный контекст`, the agent has one coherent, current,
evidence-linked project picture before planning, issue or validation. Restore
does not edit files, issue work, run external/live actions, accept tasks or
regenerate context exports unless the same OWNER message explicitly requests a
separate authorized action.

## Canonical input order

1. `AGENTS.md` and the governance trigger registry.
2. `project_recovery/00_CURRENT_STATE_MANIFEST.md`.
3. Stage/status projections carrying the same `state_id`.
4. Actual git worktrees, branches, HEADs, staging and dirty state named by the
   manifest.
5. Active architecture, design, security and delivery contracts.
6. Accepted CR register, implementation plan, traceability, delivery health
   and milestone plan when present.
7. The one active task and closure record plus manifest-linked recent evidence.
8. Baseline specification/source hashes and validators when drift is possible.
9. Scope-selected product/domain/provider/credential authorities.

Historical recovery evidence is pointer-driven. Reading every archive file is
not a current-state selection algorithm.

## Reconciliation

1. Capture `state_id`, `as_of`, task state, correction count and external/live
   budget from the manifest.
2. Verify every current projection agrees.
3. Compare recorded repositories/worktrees with actual version-control state.
   Preserve and report dirty changes; never reset/stash/delete during restore.
4. Verify active task/closure/evidence pointers and that no later accepted
   closure supersedes them.
5. Verify every accepted CR has a trigger binding.
6. Separate delivery, Requirement acceptance, milestone and release readiness.
7. Run `python3 scripts/validate_governance_contract.py`.
8. Same-priority conflicts return `BLOCKED / CONTEXT_CONFLICT`.

## Completeness certificate

Report:

- state ID and freshness;
- Stage, branch/worktree/HEAD and dirty/staged state;
- completed/current/next tasks and valid correction count;
- active Outcome Slice, production path and unavailable scope;
- Requirement/TEST delivery and acceptance;
- accepted CR/trigger coverage;
- design, security, credential, external/live and destructive boundaries;
- automated evidence and human walkthrough state;
- retry/run budget and pending OWNER actions;
- drift, contradictions and missing pointers;
- current-task, next-task, Stage and release readiness separately;
- final `READY/BLOCKED` and next authorized action.

## Automatic Full Restore triggers

- explicit Full Restore or architecture-update command;
- accepted CR propagation;
- Stage/major integration merge or transition;
- suspected drift or conflicting task report;
- agent handoff or context compaction;
- new calendar day or inactivity of at least four hours.

Fast Restore is sufficient before task issue only when none applies and the
manifest was verified in the same fresh session.
