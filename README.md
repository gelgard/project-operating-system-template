# Universal Project Operating System Template

## Overview

This repository is a reusable operating system for AI-assisted software projects.

It is designed to let you start any new project — web, mobile, backend, desktop, hybrid, or mixed-stack — with the same disciplined workflow used in a mature architecture-first project.

This template gives you:

- an architecture-first workflow
- source-of-truth project files
- a recovery system for restoring full context in a new chat
- a strict AI task execution model
- a consistent response format
- incremental, testable implementation
- continuous synchronization between architecture, planning, recovery, and execution

The core idea is simple:

1. Define identity
2. Define product
3. Define architecture
4. Define the implementation plan
5. Define recovery and response rules
6. Only then start implementation
7. Continue through small, explicit, testable AI tasks

---

## What You Get

This template ensures:

- identical project structure across projects
- deterministic project workflow
- no loss of context between chats
- clear architecture visibility
- scalable onboarding for tech leads, developers, and AI agents
- stable recovery after interruptions
- consistent project execution regardless of technology stack

---

## Repository Structure

### Root Context Files

These files define the project's core identity and high-level context:

- `AI_CONTEXT.md`
- `AI_PROJECT_MAP.md`
- `AI_PRODUCT_STRATEGY_LAYER.md`
- `AI_GTM_CONTEXT.md`
- `AI_GTM_PROJECT_MAP.md`

### Architecture

These files define the architecture, flow boundaries, and core system shape:

- `docs/architecture/system-overview.md`
- `docs/architecture/core-algorithm.md`
- `docs/architecture/data-flow.md`
- `docs/architecture/integration-boundaries.md`
- `docs/architecture/real-time-layer.md`

### Product / Planning / Strategy

These files define product meaning, roadmap, and execution direction:

- `docs/product/*`
- `docs/plans/*`
- `docs/strategy/*`

### Brand / Design

These files define the public-facing visual system:

- `docs/brand/*`
- `docs/design/*`

### AI Task System

This folder contains the implementation task model:

- `ai_tasks/000_ai_task_template.md`

### Recovery System

These files allow a new chat to restore the full state of the project:

- `project_recovery/*`

### Cursor Commands

These commands support structured execution in Cursor:

- `.cursor/commands/*`

---

## What Is Inside This Repository

This template includes the following categories of files.

### Root-Level Source-of-Truth Files

- `AI_CONTEXT.md`
- `AI_PROJECT_MAP.md`
- `AI_PRODUCT_STRATEGY_LAYER.md`
- `AI_GTM_CONTEXT.md`
- `AI_GTM_PROJECT_MAP.md`

### Architecture Templates

- `docs/architecture/system-overview.md`
- `docs/architecture/core-algorithm.md`
- `docs/architecture/data-flow.md`
- `docs/architecture/integration-boundaries.md`
- `docs/architecture/real-time-layer.md`

### Product / Planning / Strategy Templates

- `docs/product/product-brief.md`
- `docs/product/use-cases.md`
- `docs/product/scope-boundaries.md`
- `docs/plans/system-implementation-plan.md`
- `docs/plans/testing-strategy.md`
- `docs/plans/release-plan.md`
- `docs/strategy/growth-system-overview.md`
- `docs/strategy/brand-integration.md`
- `docs/strategy/positioning.md`

### Brand / Design Templates

- `docs/brand/brand-system.md`
- `docs/design/design-tokens.json`

### AI Task System

- `ai_tasks/000_ai_task_template.md`

### Recovery System

- `project_recovery/01_PROJECT_CONTEXT.txt`
- `project_recovery/02_DEV_PROCESS_RULES.txt`
- `project_recovery/03_ARCHITECTURE_RULES.txt`
- `project_recovery/04_RECOVERY_PROMPT.txt`
- `project_recovery/05_TESTING_RULES.txt`
- `project_recovery/06_STAGE_PROGRESS.txt`
- `project_recovery/07_GTM_RECOVERY_PROMPT.txt`
- `project_recovery/08_BRAND_RECOVERY_PROMPT.txt`
- `project_recovery/08_VISUAL_IDENTITY_IMPLEMENTATION_PROMPT.txt`
- `project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt`
- `project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt`
- `project_recovery/11_RESPONSE_FORMAT_RULES.txt`

### Cursor Command Templates

- `.cursor/commands/plan-stage.mdc`
- `.cursor/commands/implement-feature.mdc`
- `.cursor/commands/review-current-module.mdc`
- `.cursor/commands/write-tests.mdc`
- `.cursor/commands/prepare-release.mdc`

### Additional Files

- `README.md`
- `PROMPT_SEQUENCE.md`

---

## Core Operating Principles

This template is built around several non-negotiable principles.

### 1. Architecture First, Then Code

No implementation starts until:

- product identity is clear
- architecture exists
- implementation plan exists
- recovery files exist
- response format rules exist

### 2. Small AI Tasks Only

Work must move through small, isolated, verifiable tasks.

Each task must be:

- narrow in scope
- architecture-safe
- acceptance-driven
- testable immediately

### 3. Recovery Must Always Work

A new chat must be able to reconstruct the project from source-of-truth files.

### 4. Architecture Must Stay Synchronized

Architecture is not written once and forgotten.

When the project changes, architecture, planning, recovery, and status files must be updated pointwise.

### 5. Numbering Must Remain Stable

AI task numbering should remain linear and stable.

### 6. Terminal-Based Testing Must Be Explicit

When a test is terminal-related, it must be executable step by step from the terminal only, without guesswork.

---

## Recommended Workflow

Use the repository in the following sequence.

### Step 1 — Copy the Template

Create a new repository from this template.

### Step 2 — Replace Placeholders

Fill in:

- internal name
- public name
- domain
- product thesis
- architecture layers
- roadmap
- recovery status

### Step 3 — Generate Foundation Layer

Do not write code yet.

Generate:

- identity files
- architecture files
- product files
- planning files
- recovery rules

### Step 4 — Build the Full Plan

Break the project into:

- stages
- substages
- AI tasks

### Step 5 — Generate Recovery Files

Make sure a new chat can always restore the state of the project.

### Step 6 — Start Implementation

Only after steps 1–5 are complete.

### Step 7 — Continue Through Small Tasks

Never jump into broad implementation without a corresponding AI task.

---

## Prompt Workflow

The sequence below is the intended operating sequence for a new project.

---

## Prompt 1 — Project Intake

Use this prompt after describing your project in your own words.

### Purpose

Use this to describe the project and extract:

- identity
- architecture direction
- technology stack
- operating model
- unknowns and risks

### Prompt

```text
I am starting a new project and want to run it using the same system as my main project.

The work must not be chaotic. It must follow a project operating system with:
- architecture first
- source-of-truth files mandatory
- recovery files mandatory
- implementation only through small AI tasks
- every step must be small, verifiable, and testable
- architecture files must always stay up to date
- a new chat must be able to restore full context 1:1 from the recovery prompt

Based on my project description:
1. extract product identity
2. propose the correct architectural direction
3. propose a suitable technology stack
4. identify the internal engineering name and the public product name if both are needed
5. identify risks and unknowns
6. do not start coding
7. first propose the structure of the source-of-truth files, recovery system, and implementation plan

The response must be structured and professional.
```

### How to Use It

Use this first.  
Do not ask for implementation yet.  
The goal is to get the project correctly framed before any files are generated.

---

## Prompt 2 — Architecture Foundation

Use this after the project has been understood conceptually.

### Purpose

Generate the initial foundation files:

- context
- architecture
- planning
- recovery base

### Prompt

```text
Now generate the foundation layer of the new project using the same system as my current main project.

Prepare in full, ready for 1:1 insertion:

1. AI_CONTEXT.md
2. AI_PROJECT_MAP.md
3. AI_PRODUCT_STRATEGY_LAYER.md
4. AI_GTM_CONTEXT.md
5. AI_GTM_PROJECT_MAP.md
6. docs/architecture/system-overview.md
7. docs/architecture/core-algorithm.md
8. docs/architecture/data-flow.md
9. docs/architecture/integration-boundaries.md
10. docs/architecture/real-time-layer.md
11. docs/product/product-brief.md
12. docs/product/use-cases.md
13. docs/product/scope-boundaries.md
14. docs/plans/system-implementation-plan.md
15. docs/plans/testing-strategy.md
16. docs/plans/release-plan.md
17. project_recovery/03_ARCHITECTURE_RULES.txt
18. project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt
19. project_recovery/11_RESPONSE_FORMAT_RULES.txt

Do not write any code yet.
The full architecture + planning + recovery foundation must be built first.
```

### How to Use It

Run this before implementation planning and long before coding.

---

## Prompt 3 — Plan Decomposition

Use this after the foundation files are generated.

### Purpose

Build the full implementation plan and AI task decomposition.

### Prompt

```text
Now, based on the already created architecture and product files, build the full implementation plan.

Requirements:

- break the project into stages
- break each stage into small AI tasks
- numbering must remain linear
- tasks must be small and verifiable
- for each task include:
    - goal
    - why this matters
    - files to create/update
    - acceptance criteria
    - manual test direction
- start with architecture and foundation tasks
- then implementation tasks
- then API / UI / integration tasks
- if there is a real-time / live / background layer, separate it as an additive branch

Do not start implementation.
First generate only the full roadmap and the list of AI tasks.
```

### How to Use It

This locks in the project execution model before development starts.

---

## Prompt 4 — Recovery Setup

Use this after the plan exists.

### Purpose

Generate the recovery system so the project can survive chat loss and resume 1:1.

### Prompt

```text
Now prepare the recovery system of the new project in full.

Generate ready for 1:1 insertion:

1. project_recovery/01_PROJECT_CONTEXT.txt
2. project_recovery/02_DEV_PROCESS_RULES.txt
3. project_recovery/04_RECOVERY_PROMPT.txt
4. project_recovery/05_TESTING_RULES.txt
5. project_recovery/06_STAGE_PROGRESS.txt
6. project_recovery/07_GTM_RECOVERY_PROMPT.txt
7. project_recovery/08_BRAND_RECOVERY_PROMPT.txt
8. project_recovery/08_VISUAL_IDENTITY_IMPLEMENTATION_PROMPT.txt
9. project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt

Also:

- add recovery files to the active architecture set
- define the rules for updating them
- define the rules for updating implementation status
- define the rules for updating response format rules

Do not start implementing code yet.
```

### How to Use It

This should be done before the first real implementation task.

---

## Prompt 5 — Start Implementation

Use this when the foundation, plan, and recovery system are ready.

### Purpose

Begin actual implementation using the established operating model.

### Prompt

```text
Now continue working strictly according to the established plan / architecture / recovery / response format.

Start from the first open AI task.

The format of every response must be exactly:

1. AI Task XXX — Name
2. Stage / Substage / Goal
3. full ai_tasks/XXX_...md file
4. exact prompt for Cursor
5. expected files
6. detailed testing instructions
7. what to send back
8. completion criteria
9. next step (brief)

If testing is terminal-related:

- describe it in detail
- step by step
- so that everything can be executed fully from the terminal without guessing
- use cat > file <<'EOF' ... EOF if a temporary file is needed

Do not break numbering.
Do not break architecture.
Do not start several large tasks at once.
```

### How to Use It

This is the transition from planning into execution.

---

## Prompt 6 — Standard Working Mode

Use this for normal continuation of the project.

### Purpose

Continue the next AI task without re-explaining the whole workflow.

### Prompt

```text
Continue working strictly according to the established plans, strategy, architecture files, recovery rules, and response format.
Give the next AI task in the full correct format.
```

### How to Use It

This becomes the standard execution prompt once the project is underway.

---

## Prompt 7 — Recovery in a New Chat

Use this when context is lost and a new chat must continue the project.

### Purpose

Restore the full project state before resuming implementation.

### Prompt

```text
If context is lost and a new chat is started, use the following process:

1. upload the project archive
2. paste the recovery prompt from:

project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt

Continue working on the project strictly according to the already established system of rules, formats, and strategy.

First fully restore the project context from the source-of-truth files, recovery files, ai_tasks, and the current code.
Do not start implementation until you restore:

- current project state
- current stage
- completed task list
- next task
- active architecture rules
- AI task response format

After recovery return only:

1. current project state
2. where we are in the plan
3. which tasks are already closed
4. what the next step is
5. which architecture rules are active
6. confirmation that you are ready to continue 1:1 from the current point
```

### How to Use It

This is the critical prompt for continuity across chats.

---

## Practical Sequence For Starting a New Project

Use the prompts in this exact order:

1. Prompt 1 — Project Intake
2. Prompt 2 — Architecture Foundation
3. Prompt 3 — Plan Decomposition
4. Prompt 4 — Recovery Setup
5. Prompt 5 — Start Implementation
6. Prompt 6 — Standard Working Mode
7. Prompt 7 — Recovery in a New Chat

Do not skip steps.

---

## Additional Recommendation

For best results:

- create the new repository from this template
- replace placeholders first
- commit the initial architecture foundation before coding
- update recovery files after every meaningful implementation milestone

---

## Goal

Make every new project:

- structured
- deterministic
- recoverable
- scalable
- understandable by humans and AI
