# json_spec.md

## Purpose

Defines the historical structure, meaning, and generation rules of populated context projection JSON snapshots.

Existing JSON files are frozen historical external informational exports.
They are not active architecture synchronization deliverables by default.

If a future project explicitly reintroduces JSON export generation, generated JSON must not be a schema stub.
It must be a fully populated machine-readable project context bundle.

Markdown files may still be opened by path for raw content display,
but they must not be required to compute project structure, task status, roadmap, graph, or summaries.

## Required Root Sections

- metadata
- architecture_files
- architecture_tree
- architecture_graph
- usage_flow
- project_plan
- ai_task_status
- roadmap
- summaries
- generation_rules

## Key Interpretation Rules

1. Existing json_<timestamp>.json files are frozen historical external informational snapshots.
2. JSON must not override active markdown source-of-truth files.
3. The JSON does not need to embed full markdown text.
4. If JSON export generation is explicitly reintroduced, generated JSON must contain enough structure and summaries for the visual application to operate without markdown parsing.
5. JSON cannot override project_recovery, AGENTS.md, docs/architecture, docs/plans, or ai_tasks.

## Generation Rule

By default:
- do not generate new `contextJSON/json_<timestamp>.json` files during architecture sync, context restore, task issue, or task closure
- do not update `contextJSON/json_spec.md` unless a future architecture decision explicitly reintroduces JSON export generation
- do not overwrite previous snapshots

If a future project explicitly reintroduces JSON export generation:
- current project archive must be uploaded
- a full sync must be performed against the archive
- generated timestamped JSON must be populated with aggregated and structured project information
