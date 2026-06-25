# AGENTS.md

agent_contract_version: 2.0
last_synced_with_architecture: 2026-06-25T00:00:00+03:00
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
- contextJSON/json_<timestamp>.json -> frozen historical external informational snapshots only; no new snapshots are generated
- code -> validation only

---

## SOURCE OF TRUTH PRIORITY (STRICT)

1. project_recovery/*
2. AGENTS.md
3. docs/architecture/*
4. docs/plans/*
5. ai_tasks/*
6. contextJSON/json_<timestamp>.json archive
7. code

Violation = invalid execution

---

## EXECUTION MODEL

restore -> validate -> locate -> execute -> update -> sync

Execution responsibility split (mandatory):
- Cursor is used only for code writing and directly code-related implementation work
- architecture definition/update is performed here by the agent, not by Cursor
- planning / next-step planning is performed here by the agent, not by Cursor
- validation strategy and closure-gate evaluation are performed here by the agent, not by Cursor
- manual test orchestration and user-side validation instructions are performed here by the agent, not by Cursor
- Prompt for Cursor must exclude work the agent already performs here
- duplicated content between chat-side execution package and Prompt for Cursor is forbidden

Manager-facing step summary rule (mandatory):
- every current/next AI step must include a short manager-facing summary
- summary must explain what will be done and why from the user/product perspective
- summary must avoid programming jargon and low-level implementation language
- summary must be brief, clear, and understandable to a non-technical manager

---

## ARCHITECTURE BOUNDARIES

- recovery = factual state
- architecture = rules
- plans = future
- ai_tasks = execution
- contextJSON = external informational projection for a third-party application

Rules:
- code cannot redefine architecture
- JSON cannot override recovery
- JSON cannot define or redefine architecture, development methodology, validation strategy, testing rules, or execution process
- AGENTS/AGEND do not override recovery

---

## CONTEXT JSON CONTRACT

Last frozen JSON:
contextJSON/json_<timestamp>.json

Rules:
- frozen historical external informational export only
- no longer regenerated or updated unless a future project explicitly reintroduces an export mechanism
- must not be treated as an architecture, process, methodology, testing, or decision source for this repository
- UI must NOT parse markdown
- markdown paths used only for display
- architecture sync must not create a new populated contextJSON snapshot
- if a contextJSON file conflicts with recovery, AGENTS, architecture, plans, or ai_tasks, the markdown source-of-truth wins

---

## RESTORATION MODES

Fast:
- AGENTS.md + recovery + plan validation

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
  - `обнови полный контест` => Full restore (forced, typo alias)
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
- необходимо внести изменения
- обнови контекст
- обнови полный контекст
- обнови полный контест

Semantic command equivalence (mandatory):
- Command matching is intent-based, not literal-only.
- The following user phrasings must be treated as equivalent to `дай следующую AI task`:
  - `дай следующую аи таск`
  - `следущую аи таск`
  - `следущую задачу`
- For all equivalents above, agent must apply the same next-task response format gate.
- The following user phrasings must be treated as equivalent to `необходимо внести изменения`:
  - `вносим изменения`
  - `надо внести изменения`
  - `нужно внести изменения`
  - `необходимо внести правки`
  - `внеси изменения`
  - any close phrasing with the same meaning
- For all equivalents above, agent must start Change Request Intake from `docs/architecture/change-management-process.md`.
- Change Request Intake must return the required "Добавить Change Request" questions first and must not start implementation or create an AI task until the user's answers are analyzed and required source-of-truth updates are made.

---

## ARCHITECTURE UPDATE TRIGGERS

Update architecture when:

- current/completed/next task changes
- implementation status changes
- source-of-truth command model changes
- execution model changes
- AGENTS.md changes

---

## DO / DO NOT

Do:
- restore before acting
- validate AGENTS with recovery
- treat contextJSON as frozen historical export only, never as architecture/process authority
- follow task sequence strictly
- provide testing instructions in short explicit steps with exact commands/actions and expected results
- for AI tasks that include UI scope, always provide detailed manual visual testing instructions with exact UI actions and expected visible results
- for AI tasks with UI scope, always run Playwright-based visual validation by the agent and report executed visual steps, observed result per step, and detected visual mismatches
- keep user-side manual visual steps in parallel; do not replace them with agent-only checks
- keep refinements inside the current AI task unless the user explicitly asks for a new task
- save the ai_task markdown file when issuing the next AI task
- include a short manager-facing summary for every current/next step in plain non-technical language
- for new functionality or functional changes, enforce `docs/architecture/change-management-process.md` before implementation
- when the user triggers change intake, ask the mandatory "Добавить Change Request" questions before changing plans, tasks, or code
- keep Cursor prompts development-only: code changes, refactors, and code-level tests directly tied to implementation
- when user asks `дай следующую AI task`, respond in strict copy-ready format:
  - do not paste full AI task body into chat if task file is already created/saved
  - provide the saved ai_task file path
  - provide a short manager-facing summary
  - provide Prompt for Cursor in one separate fenced block
  - provide Test/Verification as step-by-step actions
  - provide each terminal command in its own separate fenced block for 1:1 copy
  - include `Self-check: path ✅ | cursor prompt ✅ | test steps ✅ | command blocks ✅`
- provide commit message automatically after full validation of the current AI task
- resolve any in-scope validation gap inside the same current AI task before marking it complete
- after closing each AI task, automatically delete temporary files created only for testing/validation unless they are intentional evidence artifacts
- enforce mandatory Task Closure Hard Gate Checklist before marking any AI task complete:
  - context/restore gate passed for the required restore mode
  - Goal Alignment + Requirement IDs present and valid
  - scope/baseline gate passed
  - agent validation passed
  - user manual validation passed for required steps
  - no open in-scope validation gaps remain
  - temporary validation-only artifacts are deleted unless intentionally kept
  - commit message is provided only after all gates pass
- announce explicitly when a new Stage starts
- follow mandatory Stage branch flow:
  - every Stage must have its own branch named `feature/stage-<stage-number>-<stage-name-kebab-case>`
  - all Stage work is committed only to that Stage feature branch
  - when the Stage is complete, merge that feature branch into `develop`
  - create the next Stage feature branch from updated `develop`
  - do not implement Stage work directly on `main` or `develop`

Do Not:
- invent tasks
- skip numbering
- override architecture
- implement a new functional change before Change Request Intake and impact analysis are complete
- treat code as truth
- parse markdown for runtime
- treat contextJSON as architecture/process authority
- use vague testing instructions when a concrete step/result pair can be provided
- create a new ai_task just to refine prompt or testing for the current task
- start a new Stage on an old branch without merging the completed Stage into `develop` and creating the next Stage feature branch
- implement Stage work directly on `main` or `develop`
- mark any AI task complete when at least one Task Closure Hard Gate checklist item is not satisfied
- duplicate manual validation, planning, architecture reasoning, or next-step orchestration inside Prompt for Cursor
- use Cursor as the owner of planning, architecture, validation strategy, closure gates, or response formatting

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
