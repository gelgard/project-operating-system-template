# AGENTS.md

agent_contract_version: 2.0
last_synced_with_architecture: 2026-03-24T13:28:00+02:00
compatible_with_template_os: v1

## PURPOSE
This file defines the operational contract for any agent working in this project.

The agent:
- does NOT design the system
- executes strictly inside architecture-first system

---

## AUTHORITATIVE SOURCES MATRIX

- project_recovery/* -> factual state
- AGENTS.md -> execution contract
- docs/architecture/* -> rules and constraints
- docs/plans/* -> roadmap
- ai_tasks/* -> execution units
- contextJSON/json_<latest>.json -> runtime snapshot (UI/reporting)
- code -> validation only

---

## SOURCE OF TRUTH PRIORITY (STRICT)

1. project_recovery/*
2. AGENTS.md
3. docs/architecture/*
4. docs/plans/*
5. ai_tasks/*
6. contextJSON/json_<latest>.json
7. code

Violation = invalid execution

---

## EXECUTION MODEL

restore -> validate -> locate -> execute -> update -> sync

---

## ARCHITECTURE BOUNDARIES

- recovery = factual state
- architecture = rules
- plans = future
- ai_tasks = execution
- contextJSON = runtime projection

Rules:
- code cannot redefine architecture
- JSON cannot override recovery
- AGENTS does not override recovery

---

## CONTEXT JSON CONTRACT

Latest JSON:
contextJSON/json_<timestamp>.json

Rules:
- authoritative runtime source for visual app
- contains full structured snapshot
- UI must NOT parse markdown
- markdown paths used only for display

---

## RESTORATION MODES

Fast:
- AGENTS.md + contextJSON + recovery validation

Full:
- full traversal of all layers

Archive-first:
- required before architecture update

Context Restore Policy:
- Before every new AI task, run Fast restore (key files only).
- Full restore is mandatory after:
  - command `обнови архитектурные файлы`
  - merge/stage transition
  - suspected desync (recovery/architecture/plan/task mismatch)
  - long pause
  - explicit command `обнови полный контекст`
- Command mapping:
  - `обнови контекст` => Fast restore (default)
  - `обнови полный контекст` => Full restore (forced)
- Long pause rule:
  - session inactivity >= 4 hours OR
  - new calendar day since last restore OR
  - context handoff between agents/users
  => Full restore required
- Fast restore key files:
  - project_recovery/06_STAGE_PROGRESS.txt
  - project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt
  - AGENTS.md
  - docs/plans/system-implementation-plan.md
  - docs/plans/product_goal_traceability_matrix.md
  - contextJSON/json_<latest>.json (metadata + plan + traceability sections)
- Fast restore required outputs:
  - current stage/current task/next tasks
  - gate status (Goal Alignment / Requirement mapping)
  - readiness: ready/blocked
- Full restore required outputs:
  - complete state reconstruction
  - drift/conflict audit
  - architecture/plan/recovery sync status
  - explicit blockers and required fixes (if any)
- Failure/blocked conditions:
  - required restore type not executed
  - source priority violated
  - task missing Goal Alignment mapping when gate is active
  - Full restore trigger occurred but only Fast restore was done
  - blocked response format:
    - BLOCKED: Context restore policy violation.
    - REQUIRED FIX: Run <Fast|Full> restore and resync required files.

---

## COMMAND MODEL

Allowed commands:

- обнови архитектурные файлы
- обнови template-repo
- собери canonical template-repo
- дай следующую AI task
- обнови контекст
- обнови полный контекст

---

## ARCHITECTURE UPDATE TRIGGERS

Update architecture when:

- current/completed/next task changes
- implementation status changes
- contextJSON schema changes
- execution model changes
- AGENTS.md changes

---

## DO / DO NOT

Do:
- restore before acting
- validate AGENTS with recovery
- use JSON as runtime source
- follow task sequence strictly
- provide testing instructions in short explicit steps with exact commands/actions and expected results
- keep refinements inside the current AI task unless the user explicitly asks for a new task
- save the ai_task markdown file when issuing the next AI task
- provide commit message automatically after full validation of the current AI task
- resolve any in-scope validation gap inside the same current AI task before marking it complete
- announce explicitly when a new Stage starts
- follow stage branch flow: merge current work into `development`, then create/use `feature/stage<stageNum>`

Do Not:
- invent tasks
- skip numbering
- override architecture
- treat code as truth
- parse markdown for runtime
- use vague testing instructions when a concrete step/result pair can be provided
- create a new ai_task just to refine prompt or testing for the current task
- start a new Stage on an old branch without the required merge + stage-branch creation

---

## FAILURE CONDITIONS

Invalid if:

- recovery ignored
- AGENTS ignored
- architecture bypassed
- tasks reordered
- logic invented

---

## STOP RULE

After restore -> STOP

Wait for:
"дай следующую AI task"
