# AI_CONTEXT.md

Internal architecture name: PropAgent
Public product name: Disciplia
Public domain: https://disciplia.trade

Identity rule:
- PropAgent is the internal engineering / repository / architecture identity.
- Disciplia is the public-facing product / brand / GTM identity.

Disciplia is a discipline analytics platform for traders.

Implemented analytics slice:
RuleResults
→ DisciplineScoreEngine
→ DisciplineScoreExplanation
→ DisciplineAnalyticsEngine
→ DisciplineTrendBuilder
→ StrategyBehaviorEngine
→ DisciplineProfileEngine
→ TraderDisciplineState
→ DisciplineStateSummary
→ DisciplineStateContractBuilder
→ GET /discipline-state

Implemented real-time slice:
live snapshot
→ LiveRuleEvaluationEngine
→ RealTimeAlertEngine
→ AccountRiskState
→ LiveDisciplineMonitor
→ LiveDisciplineMonitorContractBuilder
→ GET /live-discipline-monitor
→ automated endpoint tests
→ stabilized route structure

Current project stage:
- Stage 6 — Real-Time Discipline Guard

Current next task:
- 063_context_json_generator_design_or_runtime_stub

Context Projection Layer rule:
- Context Projection Layer is part of the architecture set.
- Architecture synchronization must maintain:
  - contextJSON/json_spec.md
  - a new populated contextJSON/json_<timestamp>.json
- The latest timestamped JSON snapshot is the authoritative runtime source for the external visual application.
- Markdown files are opened by path only for raw content display and must not be required to compute project structure, status, roadmap, graph, or summaries.

Archive-first architecture sync workflow:
When architecture files need updating:
1. first inform that architecture sync is needed
2. user uploads the current project archive
3. full project sync is performed against the uploaded archive
4. only after that the command "обнови архитектурные файлы" is executed

Critical rule:
Architecture sync is incomplete unless contextJSON artifacts are regenerated, included in the update archive,
and the newest timestamped JSON becomes the current authoritative visual-app snapshot.
