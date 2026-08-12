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
    - project_recovery/00_CURRENT_STATE_MANIFEST.md
    - AGENTS.md
    - docs/architecture/governance-trigger-registry.json
    - docs/plans/system-implementation-plan.md
    - docs/plans/product_goal_traceability_matrix.md
- Full restore:
  - required after `обнови архитектурные файлы`
  - required after merge/stage transition
  - required on suspected desync
  - required after long pause
  - required on explicit command `обнови полный контекст`
  - follows docs/architecture/full-context-restore-contract.md
  - reconciles actual version-control state against the current manifest
  - reads archive evidence only through current pointers/conflict audit
- Command mapping:
  - `обнови контекст` => Fast restore (default)
  - `обнови полный контекст` => Full restore (forced)
  - `обнови полный контест` => Full restore (forced, typo alias)
- Long pause:
  - inactivity >= 4 hours OR new calendar day OR context handoff
  - Full restore required
- Failure gate:
  - skipped restore, projection conflict, manifest/repository drift or failed
    governance validation => BLOCKED

Governance trigger gate:
- every executable command/event rule and accepted CR has a unique binding in
  docs/architecture/governance-trigger-registry.json
- archive evidence is non-normative until projected into active architecture
- run scripts/validate_governance_contract.py after architecture/CR
  propagation, before post-Full-Restore task issue and before Stage merge

ContextJSON archive rule:
- existing contextJSON files are frozen historical external exports only
- no new populated contextJSON snapshots are generated during architecture sync, context restore, task issue, or task closure
- contextJSON cannot override recovery, AGENTS, architecture, plans, or ai_tasks

Change management rule:
- material changes pass the CR process; in-scope defects use TASK-AMENDMENT
- task issue also requires docs/architecture/delivery-slice-governance.md

Delivery rule:
- one task normally equals one vertical Outcome Slice
- pass practical DoR and classify Standard/Sensitive/Integration-Release risk
- implementation handoff is independently audited against actual diff/gates
- maximum two valid corrective implementation passes
- delivery, Requirement acceptance, milestone and release remain separate
