# Testing Strategy

## Levels
- unit tests for pure behavior and edge conditions;
- integration/contract tests for boundaries;
- focused regression for changed scope;
- one full regression when shared contracts, dependencies/runtime, broad user flows, Stage/release closure, or explicit task requirements justify it;
- bounded sanitized live acceptance when real infrastructure behavior must be proven;
- browser/Playwright plus user visual validation for UI scope.

## Rules
- Every task maps validation to Requirement IDs and applicable engineering edge conditions.
- Focused tests run first.
- Do not rerun an unchanged successful full suite for restore/status/architecture-only work.
- Terminal commands must be exact, copy-ready, and include expected results.
- UI validation covers relevant viewports, interactions, loading/empty/error states, text fit, and the approved design contract.
- Credential/security validation uses fake secrets, redaction checks, dependency review appropriate to exposure, and a staged-diff secret scan.
- Live checks are bounded, reversible, sanitized, and tied to the exact deployed commit.
- Run `git diff --check` before commit.
- Remove temporary validation artifacts unless intentionally retained as evidence.
- Any open in-scope validation gap blocks closure.
