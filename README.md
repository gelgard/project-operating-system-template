# Universal Project Operating System Template

## Overview

This repository is a reusable operating system for AI-assisted software projects.

Its main purpose is not to store one project's architecture.
Its purpose is to let you create **any future project** — regardless of complexity, architecture, purpose, or technology stack — while preserving the same disciplined operating model.

Projects created from this template may differ substantially from each other.

What must remain the same is the method:

- architecture-first startup
- source-of-truth files
- implementation planning
- staged AI tasks
- recovery across chats
- strict response formats
- safe architecture / plan / recovery synchronization
- predictable project governance

---

## Main Goal of This Template

Using this repository and the prompt sequence described below, you must be able to create a new project that works according to the same principles, rules, process discipline, and execution model as the reference workflow — **without inheriting the specific architecture of any one project**.

In other words:

- reuse the methodology
- do not reuse project-specific content

---

## Prompt Files

Executable prompts are stored in separate files under:

- `prompts/`

`README.md` does not duplicate them as the primary source.
Instead, it defines the required execution order.

---

## Prompt Execution Sequence

Use the prompt files in the exact order below when starting a new project.

### Prompt 01 — Project Intake
File:
- `prompts/01_PROJECT_INTAKE.txt`

Purpose:
- describe the project in plain language
- extract project identity
- propose architecture direction
- propose technology stack
- identify unknowns and risks

### Prompt 02 — Architecture Foundation
File:
- `prompts/02_ARCHITECTURE_FOUNDATION.txt`

Purpose:
- generate the initial source-of-truth foundation
- create architecture, product, planning, and basic recovery files
- no implementation yet

### Prompt 03 — Plan Decomposition
File:
- `prompts/03_PLAN_DECOMPOSITION.txt`

Purpose:
- break the project into stages
- break stages into small AI tasks
- define acceptance criteria and test direction

### Prompt 04 — Recovery Setup
File:
- `prompts/04_RECOVERY_SETUP.txt`

Purpose:
- create the recovery layer
- ensure a new chat can restore the project 1:1

### Prompt 05 — Start Implementation
File:
- `prompts/05_START_IMPLEMENTATION.txt`

Purpose:
- begin implementation using the established AI task structure and response format

### Prompt 06 — Standard Working Mode
File:
- `prompts/06_STANDARD_WORKING_MODE.txt`

Purpose:
- continue the next AI task in the established format

### Prompt 07 — Recovery In A New Chat
File:
- `prompts/07_RECOVERY_IN_NEW_CHAT.txt`

Purpose:
- restore project context after chat loss
- continue from the exact current point

---

## How to Use This Template

### Step 1 — Create a new repository from this template
Use the GitHub template mechanism or clone this repository into a new project repository.

### Step 2 — Run Prompt 01
Describe the project in plain language.

### Step 3 — Run Prompt 02
Generate the foundation layer.

### Step 4 — Run Prompt 03
Generate the full implementation plan and AI task breakdown.

### Step 5 — Run Prompt 04
Generate the recovery system.

### Step 6 — Commit the foundation
Commit the source-of-truth startup state before coding.

### Step 7 — Run Prompt 05
Start implementation with the first open AI task.

### Step 8 — Use Prompt 06
Continue implementation task by task.

### Step 9 — Use Prompt 07 when needed
Restore context in a new chat if required.

---

## What Must Be Universal

The template must preserve:
- structure
- workflow
- governance
- prompts
- recovery logic
- response format
- testing discipline
- update commands

## What Must Not Be Universal

The template must not preserve:
- project-specific domain entities
- project-specific stages
- project-specific task numbering
- project-specific architecture content
- project-specific branding
- project-specific code structure unless universally reusable

---

## Operational Rule

If the methodology changes:
- the template must be updated

If only the project content changes:
- the template must not be updated

---

## Result Rule

The purpose of this template is fulfilled only if a newly created project, after executing the prompt sequence, can operate under the same planning, architecture, recovery, AI task, testing, and response-format discipline as the reference workflow.
