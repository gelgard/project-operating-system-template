# Credential And Security Process

## Status
Mandatory whenever a task uses credentials, secrets, platform accounts, environment variables, database/cache URLs, API keys, webhooks, RPC endpoints, monitoring DSNs, or deployment access.

## Task Instructions
Every affected AI task must contain a `Credentials And Security Instructions` section that states:
- why each credential is needed;
- where and how to obtain it;
- exact environment-variable name;
- local storage location (`.env`, ignored);
- deployment-side secret storage location;
- least-privilege/read-only settings where applicable;
- safe validation procedure;
- rotation/revocation procedure;
- what must never be committed, logged, pasted into chat, or shown in screenshots.

The complete section must also be repeated in chat when setup or credential-backed live validation is the next required user action. Do not repeat it when existing credentials are already configured and no credential action is required.

## Storage Baseline
- `.env.example` contains placeholders only.
- `.env` and local secret files remain ignored.
- Tests use fake values.
- Source, markdown, task files, fixtures, logs, screenshots, commits, and historical context exports must not contain real secrets.
- Runtime errors and validation reports use sanitized reason codes, never raw URLs, headers, payloads, or exception text containing secrets.

## Security Baseline
- Use least privilege and read-only access unless an explicit accepted architecture decision requires writes.
- Never introduce private keys, signing, custody, destructive production actions, or real-value transactions without explicit architecture and security approval.
- Bound retries, rate limits, caches, concurrency, and provider budgets.
- Provider failure must degrade safely and remain visible; it must not become a false success.
- Public authentication requires rate limiting, secure cookies/session handling, CSRF protection where applicable, and security headers.
- Release validation must include dependency vulnerability review and secret-redaction checks when the project exposes a public runtime.

Missing acquisition/storage instructions block task issuance and closure.
