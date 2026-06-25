restore -> validate -> locate -> execute -> update -> sync

restore: recovery + AGENTS
validate: architecture + plan
locate: current task
execute: task only
update: recovery + architecture
sync: architecture + plan + recovery source-of-truth files
stage-transition (when applicable): announce new Stage -> merge completed Stage branch to develop -> create feature/stage-<stage-number>-<stage-name-kebab-case>

Context Restore Policy:
- Fast restore:
  - default mode before each new AI task
  - reads key files only:
    - project_recovery/06_STAGE_PROGRESS.txt
    - project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt
    - AGENTS.md
    - docs/plans/system-implementation-plan.md
    - docs/plans/product_goal_traceability_matrix.md
- Full restore:
  - required after `обнови архитектурные файлы`
  - required after merge/stage transition
  - required on suspected desync
  - required after long pause
  - required on explicit command `обнови полный контекст`
- Command mapping:
  - `обнови контекст` => Fast restore (default)
  - `обнови полный контекст` => Full restore (forced)
  - `обнови полный контест` => Full restore (forced, typo alias)
- Long pause:
  - inactivity >= 4 hours OR new calendar day OR context handoff
  - Full restore required
- Failure gate:
  - if required restore type is skipped => BLOCKED

ContextJSON archive rule:
- existing contextJSON files are frozen historical external exports only
- no new populated contextJSON snapshots are generated during architecture sync, context restore, task issue, or task closure
- contextJSON cannot override recovery, AGENTS, architecture, plans, or ai_tasks

Change management rule:
- new functionality or functional changes must pass docs/architecture/change-management-process.md before implementation
