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
- machine-readable context projection
- predictable project governance

---

## Main Goal of This Template

Using this repository and the prompt sequence described below, you must be able to create a new project that works according to the same principles, rules, process discipline, and execution model as the reference workflow — **without inheriting the specific architecture of any one project**.

In other words:
- reuse the methodology
- do not reuse project-specific content

---

## Context Projection Layer

Projects created from this template must also support a machine-readable context projection layer.

That layer must produce:

- `contextJSON/json_spec.md`
- `contextJSON/json_<timestamp>.json`

The JSON snapshot must be populated, not skeletal.

It must contain enough aggregated information for an external application to visualize:

- architecture file tree
- file purposes
- file update rules
- architecture dependencies
- plan structure
- AI task statuses
- roadmap with current position
- management summary
- customer-facing current status summary
- last-iteration summary

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

### Prompt 02 — Architecture Foundation
File:
- `prompts/02_ARCHITECTURE_FOUNDATION.txt`

### Prompt 03 — Plan Decomposition
File:
- `prompts/03_PLAN_DECOMPOSITION.txt`

### Prompt 04 — Recovery Setup
File:
- `prompts/04_RECOVERY_SETUP.txt`

### Prompt 05 — Start Implementation
File:
- `prompts/05_START_IMPLEMENTATION.txt`

### Prompt 06 — Standard Working Mode
File:
- `prompts/06_STANDARD_WORKING_MODE.txt`

### Prompt 07 — Recovery In A New Chat
File:
- `prompts/07_RECOVERY_IN_NEW_CHAT.txt`

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
- context projection rules

## What Must Not Be Universal

The template must not preserve:
- project-specific domain entities
- project-specific stages
- project-specific task numbering
- project-specific architecture content
- project-specific branding
- project-specific code structure unless universally reusable
