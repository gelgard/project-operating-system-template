# How To Start A New Project

## Main Idea

This repository is used to reproduce the **way a project is run**.
It is not used to copy the content of any one project.

A new project may differ substantially:
- in technologies
- in architecture
- in product type
- in complexity
- in deployment model

What must remain the same is the operating method.

## What Must Be Reproduced

After creating a new project from this template and executing the prompt sequence from `README.md`, the new project must receive:
- architecture-first startup
- source-of-truth files
- implementation plan
- recovery system
- AI task workflow
- response format rules
- detailed terminal testing discipline
- architecture / plan / recovery synchronization logic

## What Must Not Be Carried Over

The template must not carry over:
- project-specific domain entities
- project-specific stages
- project-specific AI task numbering
- project-specific product architecture
- project-specific product content

## Current Project Commands You Should Use After Project Startup

Once a new project is created from this template and the prompt sequence has been executed, the working project should support commands like:

### 1. `обнови архитектурные файлы`
Use this to safely synchronize architecture, plan, and recovery files with the current real implementation state.

### 2. `восстанови контекст проекта`
Use this to restore the project state in a new chat from source-of-truth files and current code.

### 3. `дай следующую AI task`
Use this to continue implementation strictly in the established AI task format.

These are project-level operating commands, not template-maintenance commands.

## How To Start

1. create a new repository from this template
2. execute prompts in the order defined in `README.md`
3. get the foundation first
4. then the plan
5. then the recovery layer
6. only then begin implementation
