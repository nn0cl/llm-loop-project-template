# Agent Quickstart

Use this as the first short entry point before coding.

## Session Entry

Each new LLM session starts without prior chat context.

1. Read the task message for the covering design agreement, operating path,
   phase, persona, spec or ADR, issue, and branch.
2. If resuming, read the cited handoff or trace before other documents.
3. Recover progress from repository artifacts, not from assumed chat history:
   agreements, issues, work plans, specs, ADRs, branches, changed files,
   `docs/collaboration/loop-settings.toml`, and prior `Type: review-finding`
   issues that affect the area.
4. Read loop settings when present; write new collaboration record bodies in
   `[docs].language`. If `docs/collaboration/loop-settings.toml` is missing,
   ask the Director to run `scripts/init-loop-settings.sh` before design work.
5. If the covering agreement, path, phase, persona, or authoritative scope is
   missing, stop after design intake and return a reopening request.

For session-entry checklists and resume examples, see
`docs/collaboration/session-start-and-resume.md`.

Also see: `docs/collaboration/loop-settings.md`,
`docs/collaboration/post-hoc-audit.md`,
`docs/collaboration/findings-reuse.md`, `docs/spike/README.md`,
`docs/backlog/README.md`.

## Operating Paths

Select the smallest path that safely fits the request.

### Fast Path

Use for mechanical, local, and low-risk work such as formatting, typo fixes,
file moves, script syntax checks, README clarifications, or deterministic
verification.

Read:

1. this file.
2. directly touched files.
3. `docs/collaboration/definition-of-done.md` before final reporting.

Output a compact design note with scope, omitted context, deterministic checks,
and why Feature Path or Architecture Path is unnecessary.

Do not use Fast Path when the task changes behavior, tests, architecture,
agent instructions, collaboration rules, privacy policy, or accepted specs.

### Feature Path

Use for Phase 1, 2, or 3 feature work.

Read:

1. this file.
2. `docs/at-tdd/process.md`.
3. `docs/collaboration/ai-human-scheme.md`.
4. `docs/architecture/ai-request-routing.md`.
5. target specification under `docs/specs/`.
6. area-specific architecture document.
7. `docs/architecture/implementation-readiness.md`.
8. `docs/architecture/io-reasoning-contracts.md` only when AI/model output is
   involved.

Output the full `[DESIGN CHECK]` scaffold and execute only the requested phase.

### Architecture Path

Use for ADRs, dependency boundaries, privacy-sensitive routing, prompt or
instruction changes, process changes, and conflicts between rules.

Read:

1. this file.
2. `docs/collaboration/ai-human-scheme.md`.
3. `docs/architecture/ai-request-routing.md`.
4. `docs/collaboration/model-tool-capability-matrix.md`.
5. `docs/collaboration/privacy-context-budget-policy.md`.
6. relevant ADRs and touched contract files.
7. `docs/architecture/io-reasoning-contracts.md` when AI/model output is
   involved.

Output the full `[DESIGN CHECK]` scaffold and return a reopening request when a
new architecture or process decision is required that the design agreement does
not settle.

## Design First

Every user request starts with a design note before tests or implementation.
Size the note to the selected operating path.

The design note selects:

- target behavior.
- next AT-TDD phase.
- context to include in AI requests.
- context to omit from AI requests.
- lightweight VO or DTO candidates.
- ports and adapters involved.
- task routing to model, assistant, or deterministic tool.
- input, output, and reasoning evidence contracts when AI or model output is
  involved.

Fast Path may omit non-applicable VO/DTO, ports/adapters, and AI output
contract fields when it explicitly states that they are not involved.

## Phase Rule

Only execute the phase named for the task in the plan under the covering design
agreement.

- Phase 1: failing tests only.
- Phase 2: minimum implementation only.
- Phase 3: refactor and verification gap summary.

Phase transitions within an issue require self-review — the Implementer
reviewing its own phase transition, not a separate context. Do not start
Phase 2 from Phase 1 tests that have not been self-reviewed on the record.
Once every issue in the work plan is self-reviewed and complete, the whole
work plan requires exactly one Reviewer approval from a separate context
before it closes.

Approval is typed and scoped: `Specification conformance`, `Phase
correctness`, `Boundary conformance`, `Evidence sufficiency`. Never infer one
from another. Every approval must satisfy the deterministic precondition and
the falsification burden; the Reviewer's work-plan-level approval must also
satisfy context separation, which self-review is exempt from — see
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
and `docs/collaboration/ai-human-scheme.md`. A proposed ADR is not
implementation authorization.

Return to Architecture Path when a change introduces a subsystem, language,
framework, datastore, concurrency or transaction boundary, authentication or
authorization boundary, deployment boundary, or changes the premise of an
accepted ADR or approved logic.

## Bug Triage

Bug fixes follow the same phase rule as feature work. A minor bug may omit a
separate local issue or work plan only when it is size `S`, within already
approved scope, clear from existing behavior or specification, low risk, and
verified in the same attempt.

Omitting a separate planning artifact does not permit skipping Phase 1, Phase
2, Phase 3, deterministic verification, self-review, or the work-plan-level
Reviewer approval gate.

When a bug is size `M` or larger, needs a second execution attempt, changes
boundaries, or remains ambiguous, record it in a local issue or active work
plan before continuing.

## Core Boundaries

- Domain has no UI framework, DB, file-system, network, or third-party
  provider dependency.
- Use cases depend on domain and ports.
- Adapters implement ports.
- Delivery handlers (UI components, HTTP/RPC handlers, CLI entry points) are
  thin and call use cases only.
- `<Add your project's primary datastore and any settings-gated secondary
  store rules here, e.g. "Postgres is the primary application database" or
  "Analytics writes are gated by a feature flag".>`

## Required Area Documents

- Test placement: `docs/architecture/testing-strategy.md`
- File placement: `docs/architecture/project-structure.md`
- Dependency policy: `docs/architecture/dependency-policy.md`
- AI input/output/reasoning: `docs/architecture/io-reasoning-contracts.md`
- AI-human collaboration: `docs/collaboration/ai-human-scheme.md`
- Design & review perspectives: `docs/collaboration/design-review-perspectives.md`
- `<Add one line per stack-specific architecture document you create, e.g.
  "Backend core: docs/architecture/backend-architecture.md.">`

## Stop Conditions

Stop and return a reopening request, or raise an ADR, when the task requires
choosing something the design agreement does not settle:

- `<Persistence engine or schema details beyond the accepted baseline>`.
- `<Vector DB / embedding model or dimensions>`.
- `<External vault/layout convention>`.
- `<Provider API or SDK>`.
- `<Any other technology choice listed as a "Current Non-Decision" in
  CLAUDE.md>`.
