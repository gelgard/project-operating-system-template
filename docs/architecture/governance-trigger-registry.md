# Governance Trigger Registry

Status: mandatory process architecture.

Machine-readable projection: `governance-trigger-registry.json`.

Every executable rule needs a unique trigger, action, authority, evidence and
fail-closed result. Rule-like text without this binding is guidance or
historical evidence, not an active execution rule.

Trigger precedence:

1. safety/authority stops;
2. restore and integrity events;
3. task/CR/merge/release state transitions;
4. explicit commands;
5. reporting.

Apply all compatible higher-priority triggers first. Conflicts are `BLOCKED`,
never silently resolved by convenience, file number, mtime or chat recency.

Exact phrases in the JSON registry are guaranteed aliases. Intent-equivalent
phrases are allowed only when unambiguous. The longer Full Restore command must
not be shadowed by the Fast Restore phrase.

## Archive activation

Numbered recovery evidence, closed task records, rejected branches, proposed
CR sources and historical snapshots are evidence only. A historical rule is
active only after projection into `AGENTS.md` or active architecture, the
machine trigger registry and every affected plan/test/design/security layer.

An unprojected normative-looking archive statement is `GOVERNANCE_DRIFT` and
blocks task issue until projected or explicitly classified historical.

## Configurable project bindings

At bootstrap the project must populate:

- project response prefix, if any;
- implementation-agent transport mode (`OWNER_MEDIATED` or `DIRECT_ALLOWED`);
- requirement registry and accepted CR IDs;
- Stage/branch strategy or an explicitly approved equivalent;
- UI/device/manual acceptance surfaces;
- external/live/destructive authority boundaries.

Technology, product, provider and domain rules belong in project overlays, not
in this universal template.

Every accepted-CR `rule_bindings` row contains `id`, `source`, `when`,
`action`, `authority`, `evidence` and `fail_closed: true`. The CR ID alone does
not activate a rule; the condition and observable proof must be explicit.
