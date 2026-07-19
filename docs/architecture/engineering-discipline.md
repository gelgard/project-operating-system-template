# Engineering Discipline Protocol

## Status
Mandatory for every implementation, architecture, test, script, runtime, and UI task.

## Required Decision Protocol
Before implementation:
1. State the exact requirement, invariants, and out-of-scope behavior.
2. Mark these edge-condition groups `applicable` or `not applicable`: zero/one/many/duplicates, arbitrary selected entity, all entry points, delayed/repeated/out-of-order events, concurrency, restart/deploy, partial failure, invalid/hostile input, and hidden `latest/first/current/default` assumptions.
3. Compare at least two real solution options by correctness, security, performance, and code simplicity.
4. Choose only an option that handles every applicable condition.
5. Record remaining assumptions in `docs/architecture/assumptions.md` and guard them in code or validation.

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
Every new `ai_tasks/*.md` file must contain `Анализ частностей и выбор решения` with task understanding, edge conditions, at least two options, the chosen solution, rejected alternatives, and assumptions.

Skipping this protocol is invalid execution.
