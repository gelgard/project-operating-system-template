restore -> validate -> locate -> execute -> update -> sync

restore: recovery + AGENTS
validate: architecture + plan
locate: current task
execute: task only
update: recovery + architecture
sync: contextJSON
stage-transition (when applicable): announce new Stage -> merge working branch to development -> create feature/stage<stageNum>

Context Restore Policy:
- Fast restore:
  - default mode before each new AI task
  - reads key files only:
    - project_recovery/06_STAGE_PROGRESS.txt
    - project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt
    - AGENTS.md
    - docs/plans/system-implementation-plan.md
    - docs/plans/product_goal_traceability_matrix.md
    - contextJSON/json_<latest>.json (metadata + plan + traceability sections)
- Full restore:
  - required after `обнови архитектурные файлы`
  - required after merge/stage transition
  - required on suspected desync
  - required after long pause
  - required on explicit command `обнови полный контекст`
- Command mapping:
  - `обнови контекст` => Fast restore (default)
  - `обнови полный контекст` => Full restore (forced)
- Long pause:
  - inactivity >= 4 hours OR new calendar day OR context handoff
  - Full restore required
- Failure gate:
  - if required restore type is skipped => BLOCKED
