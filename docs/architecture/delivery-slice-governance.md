# Delivery Slice Governance

Status: mandatory and technology-neutral.

## Outcome Slice

The default implementation unit is one observable vertical outcome:

`user/system entry -> production boundary -> processing/persistence -> observable result`

The first slice of a capability is its walking skeleton. A task may cross UI,
API, service, storage, worker, device, infrastructure or other required layers.
Split only when outcomes are independently demonstrable, not to satisfy a file
or line limit.

Target task size is advisory: normally 80–180 specification lines and no more
than 20 directly related files. A larger indivisible slice needs one concise
reason. These numbers never override correctness or the visible outcome.

## Practical Definition of Ready

Before issue, record:

- user/system outcome and Requirement/Journey/Surface mapping;
- authoritative input and exact selected identity;
- real production entry point and end-to-end path;
- measurable acceptance and automated observable proof;
- risk class and applicable hostile/partial/restart/concurrency conditions;
- applicable design/accessibility contract;
- external prerequisite and authority to use it now;
- rollback for destructive or persistent change;
- explicitly unavailable scope.

Unknown critical external uncertainty may use one bounded Feasibility Spike.
Ordinary implementation uncertainty stays inside the Outcome Slice.

## Risk-proportional validation

- `Standard`: focused behavior tests, static/type/format checks, relevant build,
  one real scenario, diff and secret/path scan.
- `Sensitive`: Standard plus adversarial boundary tests, affected-subsystem
  regression, persistence/ownership/security checks, cleanup and rollback, and
  relevant native/live proof.
- `Integration/Release`: fresh deploy/package, full applicable regression,
  cumulative journeys, security/accessibility, rollback and merge/deploy
  canaries.

Universal 100% coverage is not required. Existing thresholds may not regress;
critical security/data/domain branches need positive and negative evidence.
Failed lower gates block higher-cost gates. `NOT RUN` never means PASS.

## Human and automated acceptance

Every UI Outcome Slice receives automated browser/device/UI proof. A human
OWNER walkthrough is required only at capability milestones, UX decision
gates, Stage merge and release unless the project explicitly requires more.

The OWNER validates only ready functionality through direct actions in the
running application. Screenshots/videos/traces are supporting evidence, not a
substitute. Instructions identify exact candidate, prerequisites, launch,
actions, expected results, failure criteria, cleanup and verdict. All
automatable tests/logs/hashes/API/DB/security checks remain agent-owned.

For non-UI work record `OWNER UI walkthrough: not applicable`.

## Handoff and correction

The implementation agent returns a criterion-by-criterion self-review. Its
`DONE/PASS` is untrusted producer input until independent manager validation of
the actual branch/worktree, authorized diff and gates.

Maximum two valid corrective implementation passes. Consolidate all first
audit blockers into one correction. A truncated or misrouted prompt that made
no authorized edit is invalid transport and consumes no implementation pass.
After two failed valid corrections, stop and recompose, change implementer,
defer or return to OWNER; never create an unauthorized third pass.

## Evidence and closure

One append-only task closure record normally contains handoff, corrections,
validation, visual artifact, delivery/acceptance delta, commit and push.
Separate evidence is reserved for external live, security, rejected, Stage or
release events.

Delivery, Requirement acceptance, milestone availability and release readiness
are distinct states. A runnable slice does not automatically complete every
mapped Requirement.
