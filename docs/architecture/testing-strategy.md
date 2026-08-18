# Testing Strategy

Testing follows AT-TDD phase gates.

## Test Levels

### Acceptance Tests

Purpose:

- prove Gherkin scenarios.
- drive Phase 1 Red.

Placement:

- `<FILL IN: where use-case/application acceptance tests live, e.g.
  backend/tests/ or src/core/application/__tests__/>`.
- `<FILL IN: where UI acceptance-style tests live, e.g. frontend/src/features/>`.
- E2E tests only after a runnable shell/deployment exists.

### Domain Unit Tests

Purpose:

- prove pure domain behavior.

Rules:

- no mocks needed for pure logic.
- no framework, DB, network, file-system, or SDK imports.

### Application Use Case Tests

Purpose:

- prove orchestration through ports.

Rules:

- use fake or mock port implementations.
- assert outputs and port interactions specified by Gherkin.
- no real adapters.

### Adapter Integration Tests

Purpose:

- prove concrete provider integration.

Rules:

- must be explicitly requested or covered by an ADR.
- must be separable from normal unit tests.
- must not be required for Phase 1 Red of core behavior.

### Dependency Policy Checks

Purpose:

- catch package dependency, license, advisory, and import-boundary drift.

Rules:

- run the project's chosen dependency-policy tool(s) once configured (see
  `docs/architecture/dependency-policy.md`).
- do not treat these checks as substitutes for Clean Architecture review.

### Front-End Tests

Purpose:

- prove UI behavior and user interaction.

Rules:

- `<FILL IN: your UI test framework, e.g. Vitest + Testing Library, Jest +
  RTL, Playwright component tests>`.
- mock the shared transport/API client boundary.
- do not mock random request strings inside components.

### E2E Tests

Purpose:

- prove the assembled app flow.

Rules:

- `<FILL IN: your E2E framework, e.g. Playwright, Cypress>`, used after the
  runnable shell/deployment exists.
- do not depend on real external providers unless the test is explicitly
  marked as manual or integration.

## Coverage Policy

Per `docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md`.

### Branch/route anti-gaming rule (mandatory, qualitative)

A coverage percentage measures what ran, not what was decided correctly.
This rule is mandatory for every adopting project, independent of whatever
numeric floor (if any) the project chooses under the next section:

- A test that exercises only one side of a conditional branch does not
  count as covering that branch. Every distinct route — both sides of an
  `if`, every case of a multi-way branch — needs its own asserting test.
- A representative subset of routes, chosen only to make a coverage tool
  report a particular percentage, does not satisfy this rule, even when the
  reported number looks acceptable.
- Implementation must not be shaped merely to make a coverage number pass —
  for example, collapsing a real decision into a form a line-coverage tool
  cannot see, or removing a genuine conditional in favor of logic that
  behaves the same way but reads as "covered" by a test that never actually
  exercised the removed decision.

Self-review and Reviewer records should check this rule directly against
the diff — which routes gained their own asserting test — not infer
compliance from a coverage tool's summary percentage alone.

### No universal numeric floor

This template does not mandate one specific numeric coverage floor (for
example, "80% line coverage") for every adopting project's stack. A floor is
a useful backstop against a project that adds no coverage discipline at
all, but it is also exactly the kind of number the anti-gaming rule above
warns against optimizing toward — a fixed target invites shaping tests and
implementation to clear that number rather than to be correct. See ADR
0018's Decision, Rule 3, for the full reasoning.

Each adopting project may choose its own local floor (or decline to set
one) during its own tooling-setup session (see
`scripts/lib/emit-tooling-setup-prompt.sh`), recorded there as a project
decision with its own stated grounds — not fixed by this file or by ADR
0018. The anti-gaming rule above applies regardless of whether a project
adopts a local floor.

## Phase Mapping

Phase 1 Red:

- add failing tests only.
- prefer use-case tests for core behavior.
- prefer UI tests for presentation behavior.

Phase 2 Green:

- add minimum implementation.
- do not edit reviewed tests to pass.

Phase 3 Refactor:

- improve structure.
- keep behavior and assertions stable.

## Mocking Rule

Mock ports, not concrete providers.

Examples:

- mock `<YourExternalServicePort>`, not the SDK client.
- mock `<YourSearchPort>`, not a vector DB client.
- mock `<YourExternalKnowledgePort>`, not an HTTP endpoint.
