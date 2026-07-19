# AGENTS.md

agent_contract_version: 2.1
last_synced_with_architecture: 2026-07-19T00:00:00+03:00
compatible_with_template_os: v1

## Purpose
This file defines the operational contract for every agent working in a project created from this template. The agent executes inside an architecture-first system and may not let code redefine architecture.

## Source Of Truth Priority
1. `project_recovery/*` - factual current state
2. `AGENTS.md` - execution contract
3. `docs/architecture/*` - rules and constraints
4. `docs/plans/*` - roadmap and accepted specification addenda
5. `docs/design/*` - mandatory UI contract when applicable
6. approved user-behavior documentation when the project defines it
7. `ai_tasks/*` - execution units
8. `contextJSON/json_<timestamp>.json` - frozen historical external exports
9. code - implementation evidence only

Violation is invalid execution.

## Execution Model
`restore -> validate -> locate -> execute -> update -> sync`

Mandatory contracts:
- `docs/architecture/engineering-discipline.md`
- `docs/architecture/lean-operating-mode.md`
- `docs/architecture/credential-security-process.md` when credentials/platform access are involved
- `docs/architecture/change-management-process.md` for new functionality or behavioral changes
- `docs/architecture/git-branch-workflow.md`
- `docs/design/approved-design-contract.md` for UI work

Responsibility split:
- Cursor: code writing and directly related code tests only.
- Agent chat: architecture, planning, task packaging, validation strategy, manual/live checks, closure gates, and next-step orchestration.
- Do not duplicate agent-owned planning or validation narration inside the Cursor prompt.

Every current/next step needs a short non-technical manager-facing summary.

## Architecture Boundaries
- recovery = facts
- architecture = rules
- plans = future work and accepted specification addenda
- tasks = execution units
- design = mandatory visual behavior
- code = validation evidence
- contextJSON = frozen historical informational export only

Code, JSON, and task files cannot override recovery or architecture. Runtime must not parse markdown as configuration unless explicitly designed and validated.

## Engineering Discipline Gate
Before implementation, every task must:
- state requirement, invariants, and exclusions;
- mark universal edge-condition groups applicable/not applicable;
- compare at least two real options;
- choose by correctness, security, performance, then laconicity;
- guard remaining assumptions;
- include `Анализ частностей и выбор решения` in the task file.

Selected-entity integrity is mandatory: an explicitly selected record must stay bound to that exact identity through subsequent steps. Never replace it with latest/first/default/global state without explicit user confirmation.

## Credential And Security Contract
Tasks needing credentials/platform access must include complete acquisition, exact env name, secure local/deploy storage, least-privilege, validation, and rotation instructions. Repeat the complete instructions in chat only when setup or credential-backed live validation is the next required action.

Secrets must never be committed, logged, printed, hardcoded, stored in task markdown, screenshots, tests, or context exports. `.env.example` has placeholders only; `.env` remains local and ignored. Missing instructions or unsafe secret handling blocks execution.

## Lean Operating Mode
- Be direct and delta-only.
- Prefer 1-3 short sentences when possible.
- Do not repeat unchanged rules, history, full task bodies, full successful logs, or credential instructions that are not currently required.
- Focused tests are the default. Run a full regression when required by task risk/scope, shared contracts, dependencies/runtime, Stage closure, or explicit task instructions.
- Lean reporting never weakens quality, security, restore, design, testing, or closure gates.

## Context JSON Contract
Historical `contextJSON/json_<timestamp>.json` files are frozen external informational exports. Do not regenerate or update them during restore, architecture sync, task issuance, or closure unless a future accepted architecture decision explicitly reintroduces generation.

## Restoration Policy
Fast restore before every new AI task:
- `AGENTS.md`
- `project_recovery/06_STAGE_PROGRESS.txt`
- `project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt`
- `docs/plans/system-implementation-plan.md`
- `docs/plans/product_goal_traceability_matrix.md`
- credential/design contracts when current scope touches them

Full restore after:
- `обнови архитектурные файлы`
- Stage merge/transition
- suspected source drift
- session gap >=4 hours, new calendar day, or agent handoff
- `обнови полный контекст` / `обнови полный контест`

Required restore output: current Stage/task/next tasks, Requirement gate, drift/conflicts, blockers, and `ready/blocked`.

## Command Model
Supported commands and intent-equivalent phrasings:
- `обнови архитектурные файлы` - Full restore plus architecture/plan/recovery and accepted-CR propagation audit; no contextJSON generation.
- `обнови template-repo` - copy universal methodology deltas only; exclude product-specific architecture/functionality.
- `собери canonical template-repo` - build the complete universal template OS.
- `обнови контекст` - Fast restore.
- `обнови полный контекст` / `обнови полный контест` - Full restore.
- `дай следующую AI task` and close variants - issue the next saved numbered task in strict format.
- `необходимо внести изменения` and close variants - start Change Request Intake before implementation.
- `таск выполнен`, `задача выполнена`, `задача готова`, `готово` - run the current task's complete closure validation.
- `проверь лог` - inspect the project's canonical persisted operational audit when such an audit is defined; otherwise return blocked with the missing audit contract.

## Change Request Contract
Every accepted CR must:
- be classified and impact-analysed;
- map to Requirement IDs;
- be recorded in `docs/plans/accepted_change_requests.md` as a specification addendum;
- update every affected architecture, plans, traceability, recovery, testing, design, credential/security, task/template, user-behavior, and specification file;
- explicitly record why an unaffected layer needs no change;
- be committed before implementation task issuance.

Architecture sync must audit recent accepted CRs for missing propagation.

## Next Task Response Gate
When issuing the next task:
- save `ai_tasks/<number>_<name>.md`;
- return its path;
- give a short manager-facing summary;
- provide one separate fenced Cursor prompt containing implementation-only scope;
- provide compact task-specific verification actions;
- put each terminal command in its own fenced block;
- include `Self-check: path ✅ | cursor prompt ✅ | test steps ✅ | command blocks ✅`.

## UI And Visual Gate
UI tasks must follow the approved design from the first increment; placeholder/generic/intermediate UI is forbidden. Agent-side browser/Playwright validation and separate user visual-check instructions are both mandatory. Validate relevant viewports, interaction, loading/empty/error states, text fit, and no regressions.

## Task Completion Command
On a completion command, run all validations required by the active task: focused tests, full regression when required, startup/safety checks, whitespace and secret checks, task-specific live/manual gates, and visual validation when applicable.

Do not rerun an unchanged full regression for status, restore, or architecture-only work. Resolve in-scope failures inside the current task.

## Task Closure Hard Gate
Closure requires:
- required restore passed;
- Goal Alignment and Requirement IDs valid;
- scope/baseline passed;
- agent validation passed;
- required user manual/visual validation passed;
- no open in-scope gaps;
- temporary validation artifacts removed unless intentional evidence;
- final `git diff --check` and secret-safety diff passed;
- task-scoped changes automatically committed on the current Stage feature branch.

Commit failure blocks closure. Do not wait for a separate commit command after successful closure.

## Stage Branch Workflow
- Each Stage uses `feature/stage-<number>-<name-kebab-case>`.
- Stage implementation occurs only on that feature branch.
- On Stage completion, merge into `develop`.
- Create the next Stage branch from updated `develop`.
- `master`/`main` is a publishing mirror only and is updated from `develop` under the project's explicit publication/deployment rules.
- Never implement directly on `develop`, `master`, or `main`.
- Force push, destructive reset, and branch deletion are forbidden without explicit approval.

## Do Not
- invent or reorder tasks;
- bypass restore, architecture, CR intake, Goal Alignment, or closure gates;
- implement the first plausible solution without edge analysis and option comparison;
- infer a selected entity from latest/first/default;
- expose secrets;
- deliver placeholder UI;
- claim unsupported integrations or full readiness without acceptance evidence;
- mark a task complete while any gate is open;
- leave a fully validated task uncommitted.

## Stop Rule
After restore, stop and wait for `дай следующую AI task` unless the user explicitly requested another action.
