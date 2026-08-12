# Testing Strategy

## Risk classes
- Standard: focused behavior/static/build/real-scenario/diff-secret proof;
- Sensitive: Standard plus adversarial boundary, affected regression,
  ownership/security/persistence, cleanup/rollback and relevant native/live;
- Integration/Release: fresh deploy/package, full applicable regression,
  cumulative journeys, security/accessibility, rollback and canaries.

## Rules
- Every task maps validation to Requirement IDs and applicable engineering edge conditions.
- Focused tests run first.
- Do not rerun an unchanged successful full suite for restore/status/architecture-only work.
- Terminal commands must be exact, copy-ready, and include expected results.
- UI validation covers relevant viewports/devices, interactions and applicable
  loading/empty/partial/success/error/offline/forbidden states.
- Credential/security validation uses fake secrets, redaction checks, dependency review appropriate to exposure, and a staged-diff secret scan.
- Live checks are bounded, reversible, sanitized, and tied to the exact deployed commit.
- Run `git diff --check` before commit.
- Remove temporary validation artifacts unless intentionally retained as evidence.
- Failed lower gates block higher gates; skipped is NOT RUN.
- Universal 100% coverage is not required; critical branches need
  positive/negative evidence and existing thresholds may not regress.
- Implementer PASS is untrusted until independent manager verification.
- Any open in-scope validation gap blocks closure.
