# Context Projection Layer

## Purpose

Context Projection Layer historically converted project state into populated machine-readable JSON bundles.

Existing outputs are retained as frozen historical external informational exports only.
They are no longer active architecture synchronization deliverables by default.

It is an external informational projection only. It must not define or redefine the repository's
architecture, process, methodology, testing rules, validation strategy, or execution model.

## Historical Outputs

1. contextJSON/json_spec.md
2. contextJSON/json_<timestamp>.json

## Core Rule

Existing JSON files are archive artifacts only and must not override active source-of-truth files.

If a future project explicitly reintroduces JSON export generation, generated JSON must be populated, not skeletal, and may contain:
- architecture file tree
- file purposes
- file update rules
- architecture graph
- file usage order
- plan summary
- task status summary
- roadmap summary
- system explanation for management
- current project status for customer reporting
- last-iteration summary
- timestamp for history tracking

## External Archive Rule

Existing timestamped JSON snapshots are external visual/reporting archive inputs only.
They are not internal project authority and cannot override recovery, AGENTS, architecture, plans, or AI tasks.

External tools may read historical JSON for:
- architecture tree rendering
- file-purpose and update-rule rendering
- architecture dependency graph rendering
- plan rendering
- AI task status rendering
- roadmap rendering
- management summary rendering
- customer status summary rendering
- last-iteration rendering

Markdown files may still be opened by file path for raw content display,
but they must not be required to compute project structure, status, roadmap, or summaries.

## Future Generation Inputs

If a future project explicitly reintroduces JSON export generation, the
populated JSON generation pipeline must use sources in this order:

1. `project_recovery/00_CURRENT_STATE_MANIFEST.md` and matching current projections;
2. `AGENTS.md` and the governance trigger registry;
3. active `docs/architecture/*`;
4. active `docs/plans/*` and accepted CR addenda;
5. the one active task/closure and manifest-linked evidence;
6. frozen context JSON for prior projection metadata only;
7. code/runtime for validation only.

## Future Full Structured Snapshot Rule

If generation is reintroduced, JSON may be treated as a full structured snapshot of the current project state for external reporting only.

This means it must contain enough structured data for the visual application
to reconstruct project state without markdown parsing.

This does not mean the JSON must embed the full raw contents of all markdown files.

## Update Rule

Whenever "обнови архитектурные файлы" is executed:
- run Full Restore against the live workspace and current-state manifest
- reconcile actual version-control facts and preserve dirty user changes
- use an explicitly supplied archive only as comparison evidence when the live
  workspace is unavailable or the OWNER names that archive as the audit source
- do not regenerate populated JSON snapshots
- do not update json_spec.md unless a future architecture decision explicitly reintroduces JSON export generation
- no contextJSON artifact is required for architecture sync completion
- keep repository decisions governed by the source-of-truth priority, not by JSON contents

## Human Summary Rule

The JSON must contain concise, human-readable summaries for:
- system purpose
- how the system works
- what is already implemented
- what is in progress
- what is next
- approximate completion percentage
- what changed during the last iteration

These summaries must be suitable for management and customer-facing reporting.
