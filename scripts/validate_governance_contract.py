#!/usr/bin/env python3
"""Validate template-derived governance structure without knowing its stack."""

from __future__ import annotations

import json
import re
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_OS_FILES = (
    ".cursor/commands/implement-feature.mdc",
    ".cursor/commands/plan-stage.mdc",
    ".cursor/commands/prepare-release.mdc",
    ".cursor/commands/review-current-module.mdc",
    ".cursor/commands/write-tests.mdc",
    ".env.example",
    ".gitignore",
    "AGENTS.md",
    "AI_CONTEXT.md",
    "AI_PROJECT_MAP.md",
    "README.md",
    "HOW_TO_START_NEW_PROJECT.md",
    "ai_tasks/000_ai_task_template.md",
    "docs/architecture/change-management-process.md",
    "docs/architecture/context-projection-layer.md",
    "docs/architecture/core/execution_model.md",
    "docs/architecture/credential-security-process.md",
    "docs/architecture/delivery-slice-governance.md",
    "docs/architecture/engineering-discipline.md",
    "docs/architecture/full-context-restore-contract.md",
    "docs/architecture/git-branch-workflow.md",
    "docs/architecture/governance-trigger-registry.json",
    "docs/architecture/governance-trigger-registry.md",
    "docs/design/approved-design-contract.md",
    "docs/plans/accepted_change_requests.md",
    "docs/plans/product_goal_traceability_matrix.md",
    "docs/plans/release-plan.md",
    "docs/plans/system-implementation-plan.md",
    "docs/plans/testing-strategy.md",
    "project_recovery/00_CURRENT_STATE_MANIFEST.md",
    "project_recovery/01_PROJECT_CONTEXT.txt",
    "project_recovery/02_DEV_PROCESS_RULES.txt",
    "project_recovery/03_ARCHITECTURE_RULES.txt",
    "project_recovery/04_RECOVERY_PROMPT.txt",
    "project_recovery/05_TESTING_RULES.txt",
    "project_recovery/06_STAGE_PROGRESS.txt",
    "project_recovery/07_GTM_RECOVERY_PROMPT.txt",
    "project_recovery/08_BRAND_RECOVERY_PROMPT.txt",
    "project_recovery/08_VISUAL_IDENTITY_IMPLEMENTATION_PROMPT.txt",
    "project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt",
    "project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt",
    "project_recovery/11_RESPONSE_FORMAT_RULES.txt",
    "project_recovery/12_ARCHITECTURE_UPDATE_COMMAND.txt",
    "project_recovery/12_TEMPLATE_REPO_UPDATE_COMMAND.txt",
    "project_recovery/13_CANONICAL_TEMPLATE_REPO_BUILD_COMMAND.txt",
    "scripts/validate_governance_contract.py",
    "template_governance/01_TEMPLATE_SYNC_RULES.md",
    "template_governance/02_METHOD_CHANGE_CRITERIA.md",
    "template_governance/03_TEMPLATE_COMMANDS.md",
    "template_governance/04_PROMPT_SEQUENCE_GOVERNANCE.md",
    "template_governance/05_TEMPLATE_AUDIT_2026-08-12.md",
    "template_governance/06_INHERITANCE_ACCEPTANCE_CHECKLIST.md",
    *(f"prompts/{number:02d}_{name}.txt" for number, name in (
        (1, "PROJECT_INTAKE"),
        (2, "ARCHITECTURE_FOUNDATION"),
        (3, "PLAN_DECOMPOSITION"),
        (4, "RECOVERY_SETUP"),
        (5, "START_IMPLEMENTATION"),
        (6, "STANDARD_WORKING_MODE"),
        (7, "RECOVERY_IN_NEW_CHAT"),
    )),
)


def require_file(relative: str, errors: list[str]) -> str:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"missing required file: {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def extract_state_id(text: str) -> str | None:
    match = re.search(r"(?m)^-?\s*state_id:\s*(.+)$", text)
    return match.group(1).strip() if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forbid", action="append", default=[], help="source-project token forbidden in universal contracts")
    args = parser.parse_args()
    errors: list[str] = []
    for relative in REQUIRED_OS_FILES:
        require_file(relative, errors)
    registry_text = require_file("docs/architecture/governance-trigger-registry.json", errors)
    manifest = require_file("project_recovery/00_CURRENT_STATE_MANIFEST.md", errors)
    accepted = require_file("docs/plans/accepted_change_requests.md", errors)
    agents = require_file("AGENTS.md", errors)
    if errors:
        return report(errors)

    try:
        registry = json.loads(registry_text)
    except json.JSONDecodeError as exc:
        return report([f"invalid trigger registry JSON: {exc}"])

    if registry.get("schema_version") != 2:
        errors.append("trigger registry schema_version must be 2")
    if not isinstance(registry.get("template_mode"), bool):
        errors.append("trigger registry template_mode must be boolean")

    rows = registry.get("commands", []) + registry.get("events", []) + registry.get("rule_bindings", [])
    ids = [row.get("id") for row in rows]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        errors.append("trigger/rule ids must be present and unique")

    for row in registry.get("commands", []):
        if not row.get("phrases") or not row.get("action") or not row.get("authority") or not row.get("evidence") or row.get("fail_closed") is not True:
            errors.append(f"incomplete command trigger: {row.get('id')}")
    for row in registry.get("events", []):
        if not row.get("when") or not row.get("action") or not row.get("authority") or not row.get("evidence") or row.get("fail_closed") is not True:
            errors.append(f"incomplete event trigger: {row.get('id')}")
    for row in registry.get("rule_bindings", []):
        required = ("source", "when", "action", "authority", "evidence")
        if any(not row.get(key) for key in required) or row.get("fail_closed") is not True:
            errors.append(f"incomplete accepted-rule binding: {row.get('id')}")

    expected = {"обнови контекст", "обнови полный контекст", "обнови архитектурные файлы", "дай следующую аи таск", "готово", "необходимо внести изменения"}
    phrases = {phrase for row in registry.get("commands", []) for phrase in row.get("phrases", [])}
    phrase_list = [phrase for row in registry.get("commands", []) for phrase in row.get("phrases", [])]
    if len(phrase_list) != len(set(phrase_list)):
        errors.append("command aliases must be unique")
    if expected - phrases:
        errors.append(f"missing command aliases: {sorted(expected - phrases)}")

    for row in rows:
        for authority in row.get("authority", []):
            if not (ROOT / authority).is_file():
                errors.append(f"{row.get('id')} missing authority: {authority}")

    accepted_ids = set(re.findall(r"(?m)^## (CR-[A-Za-z0-9_-]+)\b", accepted))
    bound_ids = {row.get("source") for row in registry.get("rule_bindings", [])}
    if accepted_ids != bound_ids:
        errors.append(f"accepted CR / trigger binding mismatch: accepted={sorted(accepted_ids)} bound={sorted(bound_ids)}")

    state_id = extract_state_id(manifest)
    if not state_id:
        errors.append("current-state manifest missing state_id")
        state_id = "UNKNOWN"
    template_mode = bool(registry.get("template_mode"))
    if not template_mode and "{{" in manifest:
        errors.append("project manifest still contains template placeholders")
    if not template_mode:
        unresolved_bindings = [
            key
            for key, value in registry.get("project_bindings", {}).items()
            if not isinstance(value, str) or not value or "{{" in value
        ]
        if unresolved_bindings:
            errors.append(f"project trigger bindings still contain placeholders: {sorted(unresolved_bindings)}")
        transport = registry.get("project_bindings", {}).get("transport_mode")
        if transport not in {"OWNER_MEDIATED", "DIRECT_ALLOWED"}:
            errors.append("project transport_mode must be OWNER_MEDIATED or DIRECT_ALLOWED")

    state_projection_paths = (
        "project_recovery/01_PROJECT_CONTEXT.txt",
        "project_recovery/06_STAGE_PROGRESS.txt",
        "project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt",
        "project_recovery/10_CURRENT_IMPLEMENTATION_STATUS.txt",
        "docs/plans/product_goal_traceability_matrix.md",
    )
    for relative in state_projection_paths:
        content = require_file(relative, errors)
        projected_state_id = extract_state_id(content)
        if projected_state_id != state_id:
            errors.append(f"{relative} state_id mismatch: {projected_state_id!r} != {state_id!r}")
        if not template_mode and "{{" in content:
            errors.append(f"{relative} still contains template placeholders")

    for required in ("governance-trigger-registry.json", "full-context-restore-contract.md", "00_CURRENT_STATE_MANIFEST.md", "delivery-slice-governance.md"):
        if required not in agents:
            errors.append(f"AGENTS missing governance reference: {required}")

    full_prompt = require_file("project_recovery/09_FULL_PROJECT_RECOVERY_PROMPT.txt", errors)
    if re.search(r"read all (?:project_recovery|recovery)", full_prompt, re.IGNORECASE):
        errors.append("Full Restore still selects state by reading all recovery files")

    populated = sorted(path.name for path in (ROOT / "contextJSON").glob("json_*.json"))
    if len(populated) > 1:
        errors.append(f"template has more than one historical context snapshot: {populated}")

    universal_paths = [ROOT / "AGENTS.md", ROOT / "docs/architecture/governance-trigger-registry.md", ROOT / "docs/architecture/full-context-restore-contract.md", ROOT / "docs/architecture/delivery-slice-governance.md"]
    for path in universal_paths:
        text = path.read_text(encoding="utf-8")
        for token in args.forbid:
            if token in text:
                errors.append(f"source-project leakage in {path.relative_to(ROOT)}: {token}")

    if errors:
        return report(errors)
    print(f"GOVERNANCE_CONTRACT=PASS mode={'template' if template_mode else 'project'} state_id={state_id} triggers={len(rows)} accepted_crs={len(accepted_ids)}")
    return 0


def report(errors: list[str]) -> int:
    print("GOVERNANCE_CONTRACT=FAIL")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
