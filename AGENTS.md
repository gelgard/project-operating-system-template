# AGENTS.md

agent_contract_version: 3.0
last_synced_with_architecture: 2026-08-12T00:00:00+03:00
compatible_with_template_os: v2

## Purpose

This is the technology-neutral operating contract for every agent in a project
created from this template. Project architecture and domain content are
overlays; they must not replace the operating method silently.

## Source-of-truth priority

1. `project_recovery/00_CURRENT_STATE_MANIFEST.md` and its current projections — factual state only;
2. `AGENTS.md` — execution contract;
3. `docs/architecture/*` — durable rules and constraints;
4. `docs/plans/*` — roadmap, traceability and accepted CR addenda;
5. `docs/design/*` — mandatory UI/experience contract when applicable;
6. project-approved product/domain/user-behavior authorities;
7. active `ai_tasks/*` — execution units;
8. frozen historical exports such as `contextJSON/*`;
9. code/runtime — implementation evidence only.

Recovery facts cannot change requirements. Code, task text, chat and archive
evidence cannot override a higher authority. Same-priority contradiction is
`BLOCKED / CONTEXT_CONFLICT`.

## Execution model

`restore -> validate -> locate -> execute -> update -> sync`

Mandatory universal contracts:

- `docs/architecture/governance-trigger-registry.md` and JSON projection;
- `docs/architecture/full-context-restore-contract.md`;
- `docs/architecture/delivery-slice-governance.md`;
- `docs/architecture/engineering-discipline.md`;
- `docs/architecture/lean-operating-mode.md`;
- `docs/architecture/change-management-process.md`;
- `docs/architecture/credential-security-process.md` when applicable;
- `docs/architecture/git-branch-workflow.md`;
- `docs/design/approved-design-contract.md` for UI/experience work.

The bootstrap must explicitly set the implementation agent and transport mode:

- planning/manager agent owns architecture, task packaging, validation
  strategy, independent audit, closure and next-step orchestration;
- implementation agent owns authorized code and directly related tests;
- `OWNER_MEDIATED` means the manager returns a standalone prompt and OWNER
  transports it manually; the manager must not proxy-send or operate the
  implementer UI;
- `DIRECT_ALLOWED` requires an explicit project rule and still preserves
  independent manager validation.

Every current/next step includes a short non-technical outcome summary.

## Architecture boundaries

- manifest/recovery = current facts;
- architecture = rules;
- plans = future work and accepted addenda;
- tasks = execution units;
- design = mandatory experience behavior;
- runtime/code = evidence;
- archive/export = historical information only.

Runtime must not parse governance Markdown as product configuration unless an
explicit architecture decision designs and validates that behavior.

## Outcome Slice and DoR

One implementation task normally delivers one Outcome Slice:

`entry/action -> production boundary -> processing/persistence -> observable result`.

Before issue, record outcome, Requirement/Journey/Surface mapping,
authoritative input, exact selected identity, production path, acceptance,
risk class, automated observable proof, applicable design, external
prerequisite, rollback and unavailable scope.

Task size is advisory: normally 80–180 specification lines and no more than 20
related files. Split by independently demonstrable outcomes, not arbitrary
layer/file limits.

## Engineering and identity

Analyze only applicable input, zero/one/many/duplicate, selected-identity,
ordering/concurrency, restart, persistence, provider, hostile and partial
failure risks. Compare alternatives only when the choice materially affects
correctness, security, performance, maintainability or approved design. Choose
the minimum sufficient implementation and name a concrete second consumer for
new abstractions.

An explicitly selected record/entity/artifact stays bound to that exact
identity. Never substitute latest/first/default/global state without explicit
confirmation.

## Validation

Classify tasks as Standard, Sensitive or Integration/Release and apply
`delivery-slice-governance.md`. Failed lower gates block higher gates; skipped
is `NOT RUN`. Existing coverage thresholds may not regress; universal 100%
coverage is not a template rule.

An implementer `DONE/PASS`, self-review or pasted log is untrusted input until
the manager verifies actual worktree, authorized diff and mandatory gates.
Maximum two valid corrective implementation passes. Invalid prompt transport
with no authorized edit consumes no pass.

## Human UI audit

The OWNER personally validates only ready functionality that requires direct
actions in a running UI. Before that, the manager completes every automatable
test, log, API, DB, CLI, native/package, security, accessibility, evidence,
cleanup and residual check.

Every required walkthrough gives exact candidate/path, prerequisites, launch,
actions, expected visible results, failure criteria, cleanup and verdict.
Media supports but never replaces direct in-app/device validation. Non-UI work
records `OWNER UI walkthrough: not applicable`.

## Credential, external and destructive authority

Affected tasks document why access is required, acquisition, exact variable or
credential name, ignored local storage, platform secret storage, least
privilege, safe validation, budget/retry, rollback and rotation/revocation.
Secrets never enter source, tasks, logs, screenshots, fixtures or exports.

External/live/destructive actions require explicit authority and a recorded
bounded budget. Absence of authority is `BLOCKED`, not permission by inference.

## Restoration policy

Fast Restore before a new task reads AGENTS, trigger registry, current-state
manifest, Stage/status, implementation plan, traceability and scope overlays.

Full Restore follows `docs/architecture/full-context-restore-contract.md` and
is mandatory after architecture update, accepted CR propagation, Stage/major
merge or transition, suspected drift/conflicting report, agent handoff,
context compaction, new day, inactivity >=4 hours or explicit command.

Full Restore is manifest-first and reconciles actual version control. It never
selects state by reading every historical recovery file. Missing/contradictory
state or failed governance validation blocks issue and closure.

## Command model

Commands and event triggers live in
`docs/architecture/governance-trigger-registry.json`. Guaranteed aliases:

- `обнови контекст` -> Fast Restore;
- `обнови полный контекст` / `обнови полный контест` -> Full Restore;
- `обнови архитектурные файлы` -> Full Restore plus propagation audit;
- `дай следующую AI task` and registered variants -> DoR and task issue;
- `необходимо внести изменения` / `внеси изменения` -> CR intake;
- completion aliases including `готово` -> independent current-task audit;
- `проверь лог` -> inspect canonical persisted audit or return a missing-contract blocker.

The longer/more-specific command wins. Ambiguous intent blocks rather than
silently choosing an action.

Run `python3 scripts/validate_governance_contract.py` after architecture/CR
propagation, before task issue following Full Restore and before Stage merge.

## Change requests

A full CR is required for material product/Requirement, domain rule,
architecture/security/persistence authority, design direction, provider/
license/spend, Stage order, OWNER authority or release/platform changes.

In-scope defect, missing implied edge test, parser hardening, approved-design
correction or lifecycle fix uses `TASK-AMENDMENT` in the current closure record.

An accepted CR is effective only after its accepted-register entry, matching
trigger binding, affected source-of-truth propagation, validation and separate
documentation commit. Implementation is a later task/commit.

## Next-task response gate

Issue only after DoR. Save `ai_tasks/<number>_<name>.md`; return path, manager
summary and one complete copyable implementer prompt. The prompt declares one
Outcome Slice, mappings, production path, risk, criteria, exclusions, focused
commands, automated proof and fill-in self-review. State milestone/manual UI
placement and unavailable scope.

If another task is active, a critical prerequisite is unknown or correction
budget is exhausted, return the exact blocker/recomposition instead of
inventing a task.

## Closure and Git

Closure requires restore, valid mapping, working production outcome,
proportional independent validation, automated observable proof, applicable
OWNER UI PASS, no open in-scope gaps, cleanup, diff/secret checks, traceability
update and task-scoped commit/push unless OWNER explicitly selected local-only.

Producer PASS never closes a task. Commit/push failure blocks closure. Delivery,
Requirement acceptance, milestone and release state are updated separately.

Stage work uses `feature/stage-<number>-<name>` unless the project accepts an
equivalent branch model. Never implement directly on integration/publishing
branches. Stage completion uses isolated candidate validation, normal merge,
post-merge canary and Full Restore. No force/destructive Git action without
explicit approval.

## Archive boundary

Numbered recovery evidence, closed tasks, superseded/rejected branches,
proposed CR sources and historical exports are non-normative. A historical
rule executes only after active architecture plus trigger-registry projection.
Otherwise classify it historical or return `BLOCKED / GOVERNANCE_DRIFT`.

## Stop rule

After restore, stop unless the same OWNER message explicitly requests another
authorized action.
