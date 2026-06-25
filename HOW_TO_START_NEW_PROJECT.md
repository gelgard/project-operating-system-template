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
- implementation-only Cursor prompts, with planning/architecture/validation ownership kept in agent chat
- manager-facing summaries for current and next implementation steps
- hard task-closure gates and validation artifact cleanup
- controlled Change Request intake before new functionality or functional changes
- Stage feature-branch workflow using `develop` and `feature/stage-<stage-number>-<stage-name-kebab-case>`

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

## Context JSON Archive Rule

The created project may retain:

- historical `contextJSON/json_spec.md`
- historical `contextJSON/json_<timestamp>.json`

These files are frozen external informational exports only.

New populated JSON files are not generated during architecture sync, context restore, task issue, or task closure unless a future explicit architecture decision reintroduces an export mechanism.
