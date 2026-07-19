# Template Sync Rules

Transfer only:
- methodology changes
- process changes
- workflow changes
- prompt-sequence changes
- recovery logic changes
- response format changes
- update-command behavior changes
- architecture-governance changes
- engineering-discipline changes
- lean/token-control changes
- credential-security process changes
- Change Request addendum/propagation changes
- task closure and automatic-commit changes
- visual-validation and design-contract changes

Do not transfer:
- project-specific domain logic
- project-specific architecture content
- project-specific roadmap content
- project-specific AI task numbering
- project-specific branding
- project-specific providers, credentials, URLs, deployment configuration,
  branches, requirement IDs, task numbers, or live acceptance evidence

Before commit, scan for source-project identity/functionality leakage and
validate all new cross-references.
