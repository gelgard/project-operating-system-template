# Lean Operating Mode

## Status
Mandatory for chat responses, task issuance, restore reports, validation summaries, and architecture synchronization.

## Direct Response Mode
- Be direct.
- Prefer 1-3 short sentences when the task permits.
- Report only new, changed, failed, blocked, or actionable information.
- Do not repeat unchanged rules, task history, full task bodies, full Cursor reports, or full successful test output.
- Do not add background, summaries, caveats, or follow-up offers unless required for correctness.
- If code is requested in chat, provide only the code and one short note unless explanation is explicitly requested.

## Token-Control Rules
- Keep task files complete; keep chat delta-only.
- Run and report focused validation by default. Run one full regression when task risk, dependency/runtime changes, shared contracts, Stage closure, or the task explicitly requires it.
- Do not repeat a successful full regression for status, restore, or architecture-only work when no code/runtime/test/dependency/generated asset changed.
- Report counts once; do not repeat historical pass counts.
- Repeat complete credential instructions in chat only when credential setup or credential-backed live validation is the next required action.

Lean mode changes reporting density only. It never weakens restore, source-of-truth priority, Goal Alignment, engineering discipline, security, design, testing, branch workflow, or closure gates.
