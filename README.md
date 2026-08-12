# Universal Project Operating System Template

## Overview

This repository is a reusable operating system for AI-assisted software projects.

It allows you to start any new project (web, mobile, backend, desktop, hybrid) with:

- architecture-first approach
- full source-of-truth documentation
- recovery system (chat-safe)
- strict AI task execution model
- consistent response format
- vertical Outcome Slice delivery with visible/system-observable results
- risk-proportional Standard/Sensitive/Integration-Release validation
- configurable implementation-agent transport with independent manager audit
- manifest-first Fast/Full recovery reconciled against actual version control
- machine-checked command/event/accepted-CR trigger registry
- manager-facing summaries for current and next work
- task state machine, two-correction budget and hard closure gates
- controlled Change Request intake for new functionality or functional changes
- Stage feature-branch workflow using `develop` as the completed-stage integration branch
- mandatory engineering edge-condition analysis and solution comparison
- lean/token-controlled delta-only reporting without weaker quality gates
- credential-security instructions and secret-safety closure checks
- automatic commit after successful task closure
- accepted Change Requests as effective-specification addenda
- archive non-authority: historical evidence cannot silently reactivate rules

---

## What You Get

This template ensures:

- identical project structure across all projects
- no loss of context between chats
- deterministic development workflow
- full architectural visibility
- scalable team onboarding

---

## Repository Structure

### Root Context Files
- AI_CONTEXT.md
- AI_PROJECT_MAP.md
- AI_PRODUCT_STRATEGY_LAYER.md
- AI_GTM_CONTEXT.md
- AI_GTM_PROJECT_MAP.md

### Architecture
- docs/architecture/system-overview.md
- docs/architecture/core-algorithm.md
- docs/architecture/data-flow.md
- docs/architecture/integration-boundaries.md
- docs/architecture/real-time-layer.md
- docs/architecture/engineering-discipline.md
- docs/architecture/lean-operating-mode.md
- docs/architecture/credential-security-process.md
- docs/architecture/change-management-process.md
- docs/architecture/delivery-slice-governance.md
- docs/architecture/governance-trigger-registry.md/.json
- docs/architecture/full-context-restore-contract.md
- docs/architecture/assumptions.md

### Product / Planning / Strategy
- docs/product/*
- docs/plans/*
- docs/plans/accepted_change_requests.md
- docs/plans/spec-alignment-gap-plan.md
- docs/strategy/*

### Brand / Design
- docs/brand/*
- docs/design/*
- docs/design/approved-design-contract.md

### AI Task System
- ai_tasks/000_ai_task_template.md

### Recovery System
- project_recovery/*
- project_recovery/00_CURRENT_STATE_MANIFEST.md
- AGENTS.md

### Governance Validation
- scripts/validate_governance_contract.py

### Implementation-Agent Commands
- .cursor/commands/*

The bundled `.cursor` adapter is optional. Another implementation agent may be
configured at bootstrap without changing the manager/implementer ownership,
independent audit or closure contracts.

---

## Prompt Workflow

### Prompt 1 — Project Intake

Use this to describe your project and extract identity, architecture direction and tech stack.

### Prompt 2 — Architecture Foundation

Generate:
- context files
- architecture files
- planning files
- recovery base

NO CODE at this stage.

### Prompt 3 — Plan Decomposition

Break project into:
- stages
- sub-stages
- AI tasks

Each task must include:
- goal
- acceptance criteria
- test plan

### Prompt 4 — Recovery Setup

Generate:
- full recovery prompt
- recovery files
- status tracking
- response format rules

### Prompt 5 — Start Implementation

Start working strictly via AI tasks with:

- full structured responses
- terminal-based testing
- minimal changes
- architecture preservation

### Prompt 6 — Continuous Execution

Continue:

"Continue with next AI task strictly in defined format"

### Prompt 7 — Recovery in New Chat

Paste recovery prompt + upload repo.

System must:
- reconstruct state
- detect stage
- continue work

---

## Core Rules

- Architecture first, then code
- One observable vertical Outcome Slice per task
- Every task is testable
- Always update architecture
- Recovery must work at any point
- No breaking numbering
- No uncontrolled changes
- Every AI task must include Goal Alignment with Requirement IDs
- Every AI task must include `Анализ частностей и выбор решения`
- Explicitly selected entities must remain bound through every later step
- Every current/next AI step must include a short plain-language manager-facing summary
- Implementation prompts are scope-only and do not duplicate manager-owned
  planning, architecture, validation, closure or orchestration
- UI Outcome Slices require automated proof; OWNER directly validates only
  ready milestone UI in the running application/device
- Task Closure Hard Gate Checklist must pass before a task is marked complete
- Successful task closure automatically commits task-scoped changes on the Stage feature branch
- Temporary validation-only artifacts must be deleted after task closure unless intentionally kept as evidence
- contextJSON is an external informational export for visualization/reporting only; it is not architecture/process authority
- populated contextJSON snapshots are no longer generated during architecture sync, context refresh, task issue, or task closure unless a future project explicitly reintroduces an export mechanism
- every Stage must be developed in `feature/stage-<stage-number>-<stage-name-kebab-case>` and merged into `develop` only after Stage completion
- commands equivalent to `необходимо внести изменения` must start Change Request Intake before plans, tasks, or code are changed
- accepted Change Requests must be recorded in `docs/plans/accepted_change_requests.md` and propagated through every affected source-of-truth layer
- every accepted CR and executable archived rule needs a registered trigger;
  archive evidence alone is non-normative
- credential instructions are repeated in chat only when credential setup/live validation is the next required action
- direct responses are delta-only by default; reporting brevity never reduces validation quality
- Context restore policy:
  - `обнови контекст` => Fast restore (default)
  - `обнови полный контекст` => Full restore (forced)
  - `обнови полный контест` => Full restore (forced typo alias)
- Full Restore is manifest-first, checks actual worktrees/branches/HEAD/dirty
  state and returns a completeness certificate
- maximum two valid corrective implementation passes; implementer PASS is
  untrusted until independent audit

---

## How To Use

1. Copy this repository
2. Replace placeholders
3. Populate the baseline specification, Requirement IDs, approved design, and `.env.example` placeholders
4. Run prompts in order
5. Start implementation via AI tasks
6. Maintain architecture + recovery files

---

## Goal

Make every project:

- structured
- deterministic
- recoverable
- scalable
- understandable by humans and AI

## Template Operating System Inheritance Rule

The uploaded template repository is the **source-of-truth operating system layer** for any new project created from it.

This means the new project must inherit and preserve the template-defined:

- architecture file structure
- recovery structure
- planning structure
- AI task workflow
- response format rules
- architecture update procedure
- workspace/manifest-first sync with archive fallback
- contextJSON rules
- Change Request process
- Stage branch workflow
- command model

The new project may extend the content for its own domain, product, and technology stack, but it must **not replace the template operating system with a different process model** if the template already defines one.

Technology-neutral inheritance means the project chooses its own language,
framework, persistence, UI, deployment and providers. It does not delete the
governance contracts; it maps them to stack-appropriate commands and evidence.

In practical terms:

- the template structure is reused as the baseline
- project-specific architecture is added on top of the baseline
- project-specific planning is added on top of the baseline
- project-specific recovery content is added on top of the baseline
- all future architecture updates must continue to preserve the inherited operating-system rules
