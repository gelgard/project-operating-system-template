# How To Start A New Project

## Main Idea

This repository is used to reproduce the **way a project is run**.
It is not used to copy the content of any one project.

A new project may differ substantially:
- in technologies
- in architecture
- in product type
- in complexity
- in deployment model

What must remain the same is the operating method.

## What Must Be Reproduced

After creating a new project from this template and executing the prompt sequence from `README.md`, the new project must receive:
- architecture-first startup
- source-of-truth files
- implementation plan
- recovery system
- AI task workflow
- response format rules
- detailed terminal testing discipline
- architecture / plan / recovery synchronization logic
- frozen historical contextJSON archive handling; no new populated contextJSON snapshots by default
- implementation-only prompts for the configured implementation agent, with
  planning/architecture/validation ownership kept in manager-agent chat
- manager-facing summaries for current and next implementation steps
- hard task-closure gates and validation artifact cleanup
- controlled Change Request intake before new functionality or functional changes
- Stage feature-branch workflow using `develop` and `feature/stage-<stage-number>-<stage-name-kebab-case>`
- mandatory engineering edge-case analysis and comparison of solution options
- lean/token-controlled delta-only reporting without weaker validation
- credential acquisition/storage/rotation instructions when secrets are needed
- automatic task commit after every successful closure gate
- selected-entity integrity across multi-step flows
- Outcome Slice delivery and practical DoR
- Standard/Sensitive/Integration-Release risk validation
- current-state manifest plus actual version-control reconciliation
- machine-checked command/event/CR triggers and archive non-authority
- independent implementation-handoff audit and two-correction budget

## Current Project Commands You Should Use After Project Startup

Once a new project is created from this template and the prompt sequence has been executed, the working project should support commands like:

### 1. `обнови архитектурные файлы`
Use this to safely synchronize architecture, plan, and recovery with the current implementation state.

This command must not generate a new populated `contextJSON/json_<timestamp>.json`.

### 2. `обнови контекст`
Use this for default Fast restore before each new AI task.

### 3. `обнови полный контекст`
Use this to run forced Full restore after architecture sync, stage/merge transition, suspected desync, long pause, or explicit full-context request.

Typo alias:
- `обнови полный контест` must behave the same way.

### 4. `дай следующую AI task`
Use this to continue implementation strictly in the established AI task format.

Equivalent user phrasings such as `дай следующую аи таск`, `следущую аи таск`, and `следущую задачу` should trigger the same next-task response format.

### 5. `необходимо внести изменения`
Use this when new functionality, refinements, defect fixes, design deltas, architecture changes, or reprioritization are requested.

Equivalent user phrasings such as `вносим изменения`, `надо внести изменения`, `нужно внести изменения`, `необходимо внести правки`, and `внеси изменения` must start Change Request Intake.

### 6. `готово`
Aliases `таск выполнен`, `задача выполнена`, `задача готова`, and `готово`
must run every validation required by the current task. Successful closure
automatically commits task-scoped changes on the current Stage feature branch.

### 7. `проверь лог`
When the project defines a canonical persisted operational audit, inspect that
evidence against the effective specification and documented user behavior. If
the project has no such audit contract, return a precise blocker instead of
inventing one.

## Project Bootstrap Obligations

When copying this template:
- replace identity and product placeholders without deleting process contracts;
- register the baseline specification and accepted-CR addendum files;
- populate the approved design contract before UI implementation;
- initialize Requirement IDs, Stage 1, no completed/current task, and logical next tasks;
- create `.env.example` placeholders only; never copy real `.env` values;
- keep contextJSON historical/frozen unless export generation is explicitly reintroduced.
- populate current-state `state_id`, branch/worktree/HEAD, active task, risk,
  correction count, evidence pointers and external/live budget;
- set implementation agent and transport mode (`OWNER_MEDIATED` or
  `DIRECT_ALLOWED`);
- replace stack placeholders with project commands while preserving risk-class
  meaning and closure semantics;
- run `python3 scripts/validate_governance_contract.py` before the initial
  project commit.
- complete `template_governance/06_INHERITANCE_ACCEPTANCE_CHECKLIST.md` and
  retain its project-mode validator result as bootstrap evidence;
- during template sync, pass source-specific identities/providers/technologies
  as repeated `--forbid TOKEN` arguments to prove no leakage into universal
  contracts.

## Technology-Neutral Mapping Audit

Before implementation, confirm the derived project maps all universal concepts:

- “build” to its actual compiler/bundler/package step or explicit N/A;
- “real scenario” to browser, device, CLI, API, worker, data pipeline, firmware
  or infrastructure behavior appropriate to the product;
- persistence/rollback to its actual storage and deployment model;
- UI walkthrough to a running product surface, or explicit non-UI N/A;
- external/live authority to real providers/accounts/devices/environments;
- branch/canary model to the chosen version-control/release architecture;
- requirement IDs and evidence to the project specification.

Do not copy a source project's framework, provider, screen, task number,
Requirement ID, branch name, credential, URL or live evidence.

## Context JSON Archive Rule

The created project may retain:

- historical `contextJSON/json_spec.md`
- historical `contextJSON/json_<timestamp>.json`

These files are frozen external informational exports only.

New populated JSON files are not generated during architecture sync, context restore, task issue, or task closure unless a future explicit architecture decision reintroduces an export mechanism.
