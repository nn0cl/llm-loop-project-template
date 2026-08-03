# Implementation Readiness Checklist

Use this checklist before starting a coding task.

## Required Inputs

- A target EARS or Gherkin specification exists under `docs/specs/` for
  Feature Path work.
- A design note identifies target behavior, included context, omitted context,
  task routing, and any applicable VO/DTO candidates or ports/adapters.
- AI-assisted tasks identify input envelope, output schema, and reasoning
  evidence contract.
- A recorded design agreement under `docs/collaboration/agreements/` covers
  this task.
- The plan under that agreement names the current phase and the active
  persona.
- The touched area has a matching architecture rule document.
- Unknown provider, DB, model, or folder decisions are listed as ambiguities or
  captured in an ADR.
- New dependencies have a lightweight adoption note covering vulnerability
  posture, version-specific examples, troubleshooting depth, minimal real-file
  testing, POC feasibility, and Clean Architecture boundary fit.
- Settings tasks separate normal settings, validation, and secrets.
- Optional local infrastructure tasks (e.g. containerized services) keep that
  infrastructure outside domain and use-case unit test requirements.

## Ready for Phase 1 Red

- The scenario has clear `Given`, `When`, and `Then` clauses.
- External resources can be represented as ports.
- Expected results are observable.
- The test location is selected from `docs/architecture/testing-strategy.md`.

## Ready for Phase 2 Green

- Phase 1 tests were self-reviewed by the Implementer that wrote them — the
  self-review record and deterministic verification output are on file. Per
  `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
  this is not a separate-context Reviewer approval; that happens once, over
  the whole work plan, at its close.
- The implementation location follows `docs/architecture/project-structure.md`.
- Business logic belongs in domain or application modules.
- Delivery handlers, UI components, and adapters remain thin.
- Source code remains readable, appropriately split, and reviewable — by a
  reviewing persona, a future agent, or the Director inspecting artifacts.

## Ready for Phase 3 Refactor

- Tests are green.
- Refactoring does not change assertions or behavior.
- Remaining risks are stated in the verification gap summary.
- Self-reviewed, same terms as Phase 1 and Phase 2.

## Ready to Close the Work Plan

- Every issue in the work plan is self-reviewed and complete.
- Preflight Validation is recorded over the whole work plan and returned
  `pass`; a Preflight pass is not Reviewer approval.
- The Reviewer persona, running in a context separate from the one that
  produced the work, has approved the work plan, naming the failure scenarios
  it tried to falsify.
- The Director has read the approved result and recorded the next direction,
  or the end of the engagement, in the same action.

## Not Ready If

- The task starts tests, implementation, migrations, or UI without the
  path-appropriate design intake.
- The proposed AI request payload includes unrelated files, full private
  documents, secrets, or provider data not required by the task.
- AI output is accepted as trusted data without structured validation, source
  evidence, confidence or uncertainty, and review status.
- The task requires choosing a datastore, vector DB, embedding model, external
  layout, or provider API that neither an ADR nor the design agreement settles.
- A new dependency is adopted without checking known vulnerability reports for
  the intended version, version-matched examples, troubleshooting evidence, a
  minimal real-file test path, and POC feasibility when architecture risk is
  present.
- Saving settings triggers side-effecting external calls (writes, provider
  calls, projections) that the feature does not require.
- Domain or use-case unit tests require optional infrastructure (containers,
  external services) to be installed.
- The proposed code puts business policy in UI components, delivery handlers,
  or adapters.
- Tests require a real external service, network call, or provider for core
  behavior.
- The proposed code is dense, multi-responsibility, or split into speculative
  abstractions that increase the cognitive load of reviewing it.
