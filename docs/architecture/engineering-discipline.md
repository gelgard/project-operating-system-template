# Engineering Discipline Protocol

## Status
Mandatory for every implementation, architecture, test, script, runtime, and UI task.

## Required Decision Protocol
Before implementation:
1. State Outcome Slice, production path, invariants and unavailable behavior.
2. Analyze only applicable conditions: zero/one/many/duplicates, selected
   identity, entry points, ordering/concurrency, restart/deploy, persistence,
   provider/external state, partial failure and invalid/hostile input.
3. Compare alternatives only when the choice materially affects correctness,
   security, performance, maintainability or approved design.
4. Choose the minimum sufficient option handling every applicable condition.
5. Name a concrete second consumer or mandatory framework reason for each new
   abstraction.
6. Record remaining assumptions and guard them in code or validation.

## Fixed Selection Rule
When a user or caller selects a concrete entity, preserve that exact identity through later input, confirmation, persistence, and response. Never substitute the latest, first, default, or globally inferred entity unless the user explicitly confirms that fallback.

## Quality Rules
- Reuse existing project boundaries and helpers.
- Avoid request-in-loop and repeated external work; use bounded batching, caching, and coalescing where justified.
- Do not block async paths with synchronous I/O.
- Design retries and repeated actions for idempotency.
- Validate ownership, authorization, input bounds, and secret safety at boundaries.
- Add tests or guards for every applicable edge condition.

## AI Task Requirement
Every new `ai_tasks/*.md` contains `Анализ частностей и выбор решения` with
task understanding, applicable conditions, material options when needed,
chosen solution, rejected alternative when material and assumptions.

Skipping this protocol is invalid execution.

## Independent handoff audit

An implementation-agent report is untrusted input. Inspect actual repository,
branch/worktree, authorized diff, staging, task contract and mandatory gates.
Focused green tests or self-declared PASS cannot advance canonical state.

A valid failed correction consumes one of two passes. A truncated/misrouted
prompt that made no authorized change is invalid transport and consumes none.
