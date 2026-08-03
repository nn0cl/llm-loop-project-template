# Grok Agent Instructions: Architecture Boundaries

## Phase Gate

Only execute the phase named for the task in the plan under the covering design
agreement. If no design agreement covers the task, do not start — return it to
the design phase.

Do not implement ahead of the current phase. Do not "helpfully" generate
production code during Phase 1.

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
phase transitions within an issue are **self-reviewed**; the separate-context
Reviewer operates once, over the whole work plan, after every issue in it is
self-reviewed and complete.

### Phase 1: Red - Failing Tests Only

Generate tests only.

- Do not write production implementation.
- Depend on ports or interfaces for all external resources.
- Mock every external resource listed below under "External Resources Must
  Be Ports".
- Assertions must match the Gherkin `Then` clauses exactly.
- Red is acceptable as compile failure when interfaces or use cases do not
  yet exist, or as test failure when skeletons exist.

Before Phase 2 starts, self-review the Red state: record the deterministic
output and the failure scenarios looked for.

### Phase 2: Green - Minimal Implementation

Generate only the minimum production implementation required to pass the
tests.

- Do not modify tests to make them pass.
- Keep business logic in Domain or UseCase layers.
- Keep UI components, framework request/command handlers, database structs,
  provider clients, and file adapters free of business decisions.
- Do not add behavior not specified by EARS, Gherkin, or reviewed tests.
- Self-review before Phase 3.

### Phase 3: Refactor

Refactor only after Green. Behavior and assertions must not change. Self-review,
and state the remaining verification gap.

After refactoring, output:

```markdown
### 変更の要約 (PR Summary)
- **何を目的として何を変更したか**: ...

### 検証の根拠 (Verification Evidence)
- **実行した決定性チェックとその出力**: ...

### 残存リスク・検証の溝 (Verification Gap)
- **AIが推測で補った部分、またはハルシネーションが発生しやすい箇所**: ...
- **work-plan-level Reviewer が反証を試みるべきポイント**: ...
```

Self-review at every phase requires the same two constraints as any
approval — recorded deterministic verification output, and named failure
scenarios with why each does not occur — but not context separation, which is
waived only at this layer. A phase transition is not complete without its
self-review record.
Use `docs/templates/self-review.md`'s short form by default (size `S`);
escalate to the full form only at size `M` or larger, per
`docs/architecture/adr/0015-review-cost-discipline.md`.

### Work-Plan Review and Close

After every issue in the work plan is self-reviewed and complete, run
Preflight Validation, then submit the whole work plan to the Reviewer persona
in a separate context. After the Reviewer approves, the Director reads the
result and states the next direction, or ends the engagement, in the same
turn — the second and last human gate per work plan.

## Clean Architecture Dependency Rule

Allowed dependencies:

- Domain -> nothing project-specific.
- UseCase -> Domain and Ports.
- Adapter -> UseCase, Ports, framework SDKs, DB SDKs, file system, network.
- UI/Delivery -> application command/query contracts and presentation state.

Forbidden dependencies:

- Domain -> Adapter.
- Domain -> Framework.
- UseCase -> DB schema.
- UseCase -> migration files.
- UseCase -> UI component.
- UseCase -> framework request/command handler.
- UI -> DB.
- UI -> external provider SDK.
- Adapter -> business policy not present in UseCase or Domain.

## External Resources Must Be Ports

Represent these as ports before using concrete implementations. Replace this
list with the project's actual external dependencies (see `AGENTS.md` and
`CLAUDE.md` for the same list kept in sync):

- `<External data source A>`.
- `<External data source B>`.
- `<Primary datastore>`.
- `<Secondary datastore, if any>`.
- Settings storage and validation.
- Secret storage.
- Dependency policy checks.
- `<Optional local runtime services, e.g. Docker-hosted DB>`.
- `<External API / third-party service>`.
- `<LLM or agent provider>`.

## Anti-Hallucination Rules

- Do not invent APIs, model names, vector dimensions, database schemas,
  migrations, or external folder/service conventions.
- Do not include unrelated files, full transcripts/documents, full data
  exports, or secrets in AI request payloads.
- Do not treat free-form AI prose as trusted domain data. Validate output
  schemas, source references, confidence, and review status before use.
- Do not generate dense or multi-responsibility code. Keep source code
  appropriately split and readable for the next reader — a reviewing persona,
  a future agent, or the Director inspecting artifacts.
- If a dependency is unknown, add an interface boundary or an ADR question.
- If a behavior is not in the specification, do not implement it.
