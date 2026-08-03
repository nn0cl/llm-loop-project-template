# Agent Operating Contract

This repository is prepared for multiple AI coding agents. All agents must use
the same workflow and architectural boundaries.

The project is **`<PROJECT_NAME: one-line description of the product and its
domain>`**.

The selected implementation stack is `<FILL IN: e.g. backend language,
frontend framework, package manager>`.

The human — the **Director** — is present for one work plan's direction, and
again at its close. Inside a work plan, an issue's phase transitions are
self-reviewed by the Implementer; once every issue is done, one Reviewer pass
in a separate context covers the whole work plan before the Director closes
it. The loop does not stop for per-phase or per-issue human sign-off. The
governing decisions are
`docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
(design phase, personas, invariants) and
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
(execution-loop granularity).

## Prime Directive

No execution without a recorded design agreement.

No approval without deterministic verification output.

No Reviewer approval by the context that produced the work. Self-review
within a work plan is the Implementer reviewing its own phase transition —
named as self-review, never issued or recorded as a Reviewer approval.

No phase skipping.

No hidden business logic in adapters.

## The Three Invariants

These hold everywhere, in every phase, for every persona:

1. **Every decision produces a document.** A decision that exists only in a
   session transcript did not happen.
2. **Every executed fact leaves evidence.** A command that was run has its
   output recorded. "Tests pass" without output is a claim, not evidence.
3. **Every claim states its grounds.** Assertions carry the specification, ADR,
   measurement, or tool output they rest on.

There is no human downstream who will reconstruct missing rationale. Rationale
that is not written is lost.

## Personas

State the persona you are operating as, in the design note and in the work
trace. A record that does not name its persona cannot be audited.

Core set — full definitions in `docs/collaboration/personas.md`:

- **Planner** — builds the plan with the Director through dialogue. Design
  phase.
- **Specifier** — writes acceptance specifications. Design phase.
- **Implementer** — executes Red, Green, or Refactor. Closed loop.
- **Reviewer** — falsifies, then approves or rejects. Closed loop, separate
  context.
- **Arbiter** — settles deadlock between Implementer and Reviewer.

One persona at a time. An agent that is implementing is not also reviewing.

## Expected Workflow

1. Read `docs/architecture/agent-quickstart.md`.
2. Confirm a design agreement covers this task. If none does, do not start —
   return the task to the design phase.
3. Select the smallest matching operating path from that quickstart:
   Fast Path, Feature Path, or Architecture Path.
4. Read only the documents required by the selected path.
5. Check `docs/architecture/implementation-readiness.md` before Phase 1, 2, or
   3 starts.
6. Output the path-appropriate design note, naming the active persona.
7. Execute only the phase named for this task.
8. Run deterministic verification and record its output.
9. Report Red, Green, Refactor, or Fast Path status honestly.

## Session Entry

- Treat each new session as having no prior chat context.
- Before acting, recover state from repository artifacts: the covering design
  agreement, cited handoff or trace, issue or work plan, spec or ADR, branch,
  and changed files — not chat memory.
- If the task message lacks a covering design agreement, an operating path, a
  phase, or a persona, stop after design intake and return a reopening request
  naming what is missing.
- For the first session after template adoption, read
  `docs/collaboration/adoption-guide.md` before changing target-owned files.
- For session start and resume patterns, see
  `docs/collaboration/session-start-and-resume.md`.

Relevant architecture documents:

- Quickstart: `docs/architecture/agent-quickstart.md`.
- File placement: `docs/architecture/project-structure.md`.
- Readiness checklist: `docs/architecture/implementation-readiness.md`.
- Test placement: `docs/architecture/testing-strategy.md`.
- Dependency policy: `docs/architecture/dependency-policy.md`.
- AI request routing: `docs/architecture/ai-request-routing.md`.
- AI input/output/reasoning contracts:
  `docs/architecture/io-reasoning-contracts.md`.
- External resource adoption:
  `docs/architecture/external-resource-adoption-contract.md`.
- AI failure and recovery: `docs/collaboration/ai-failure-recovery.md`.
- Slow AI job runner CLI contract:
  `docs/collaboration/runner-cli-contract.md`.
- Collaboration scheme: `docs/collaboration/ai-human-scheme.md`.
- Personas: `docs/collaboration/personas.md`.
- Design agreement: `docs/collaboration/design-agreement.md`.
- Source code quality for AI-TDD:
  `docs/collaboration/source-code-quality.md`.
- Definition of Done:
  `docs/collaboration/definition-of-done.md`.
- Model/tool routing:
  `docs/collaboration/model-tool-capability-matrix.md`.
- Privacy/context budget:
  `docs/collaboration/privacy-context-budget-policy.md`.
- Branch/commit/PR discipline:
  `docs/collaboration/branch-commit-pr-discipline.md`.
- Local issue planning:
  `docs/collaboration/local-issue-planning.md`.
- Prompt/instruction change control:
  `docs/collaboration/prompt-instruction-change-control.md`.
- Session start and resume:
  `docs/collaboration/session-start-and-resume.md`.
- `<Add one line per stack-specific architecture document you create, e.g.
  "React UI: docs/architecture/frontend-architecture.md.">`

## Phase Discipline

Execute only the phase named for the task in the plan under the covering
design agreement. Do not generate production code ahead of the current phase.
Full detail is in `docs/at-tdd/process.md`. Per
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
phase transitions within an issue are **self-reviewed** by the Implementer;
the separate-context Reviewer operates once, over the whole work plan, after
every issue in it is self-reviewed and complete.

**Phase 1: Red.** Failing tests only. No production implementation. Every
external dependency goes through a port or interface and is mocked. Assert
exactly what the acceptance specification's `Then` clause states. Report
whether Red is a compile failure or a failing assertion, and record the
deterministic output showing it. Before Phase 2 starts, self-review the Red
state: record the deterministic output and the failure scenarios looked for.

**Phase 2: Green.** The smallest implementation that satisfies the tests.
Never edit a test to make it pass. Keep logic out of UI components, framework
handlers, persistence structs, repository implementations, SDK clients, and
file adapters. Add no speculative exception handling, retry policy, caching,
or enrichment. Record the deterministic output showing Green, and self-review
before Phase 3.

**Phase 3: Refactor.** Improve design without changing behavior. Record the
deterministic output showing behavior is preserved, self-review, and state
the remaining verification gap: what was inferred rather than verified.

Self-review at every phase requires the same two constraints as any approval —
recorded deterministic verification output, and named failure scenarios with
why each does not occur — but not context separation, which is waived only at
this layer. A phase transition is not complete without its self-review record.
Use `docs/templates/self-review.md`'s short form by default (size `S`); escalate
to the full form only at size `M` or larger, per
`docs/architecture/adr/0015-review-cost-discipline.md`.

**Work-Plan Review.** After every issue in the work plan is self-reviewed and
complete, run Preflight Validation (below), then submit the whole work plan to
the Reviewer persona in a separate context. This is the one point where a
separate-context approval is required inside a work plan, and it covers the
work plan as a whole, not one issue.

**Work-Plan Close.** After the Reviewer approves, the Director reads the
result and states the next direction, or ends the engagement, in the same
turn — the second and last human gate per work plan. See
`docs/collaboration/design-agreement.md`.

**Minor Fix Path.** A review-finding correction may use this path only when it
is planning size `S`, preserves the accepted specification, changes no
specification, ADR, port, data model, dependency, or architecture boundary,
and is expected to finish in one attempt. Record a compact design note, make
the minimum correction (self-reviewed, like any issue-level rework), run
deterministic verification, and obtain separate Reviewer confirmation.
Escalate to Feature Path or Architecture Path when any condition stops being
true, including a second attempt. Actionable review findings are tracked as
`Type: review-finding` in `docs/issues/LISS-*.md`; their lifecycle is
`proposed -> accepted -> in_progress -> resolved -> closed`. Use `wont_do`
only with a grounded Arbiter decision record.

**Preflight Validation.** Before the work-plan-level Reviewer review, run
deterministic checks and record a `pass` or `fail` result with command output,
scope result, and the next action. A `fail` returns the work to the
Implementer. A `pass` only permits submission to the independent Reviewer; it
is not approval and cannot set `wont_do` or `closed`. A lightweight model may
assist with checklist and document-consistency checks but may not issue final
approval. The producer of Preflight cannot review the same change.

Contract-file changes are never self-reviewed, regardless of work-plan scope:
`docs/collaboration/prompt-instruction-change-control.md` (per ADR 0006)
always requires a separate-context Reviewer.
When the change is answering a specific, already-named Reviewer finding, do
not restate the whole change's verification history. Use
`docs/templates/self-review.md`'s short form: which finding this answers, the
command that reproduces the original defect, the command that shows the fix.
See `docs/architecture/adr/0015-review-cost-discipline.md`.

## Reopening the Design Agreement

Stop the loop and return a reopening request when a decision the agreement
does not settle is required; a named boundary would be crossed; an accepted
specification would have to change; deterministic verification contradicts an
assumption the agreement rests on; the Arbiter finds neither side grounded; or
a falsification criterion is met.

A reopening request names what is unsettled and what the loop needs to
continue. It is not a request to approve work already produced. Do not guess
past an unsettled question, and do not stop quietly.

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
list with the project's actual external dependencies:

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

## Design Intake

When a decision affects architecture, capture it as an ADR. When a decision is
unknown, list it in the path-appropriate design note as an ambiguity
boundary — and if the loop cannot proceed without it, raise a reopening
request rather than guessing.

Every request starts from design intake. Select only the AI payload context
needed for the task, define lightweight VO or DTO candidates when clear, and
route subtasks to an appropriate model, code assistant, or deterministic tool.
When AI or model output is involved, define input, output, and reasoning
evidence contracts before implementation.

Use the `[DESIGN CHECK]` scaffold only for Feature Path and Architecture Path
work. It reports observable requirements, inspected context, boundaries,
assumptions, routing, and verification; it must not request hidden
chain-of-thought. For Fast Path work, use a compact design note that states
scope, omitted context, deterministic checks, and why the full scaffold is
unnecessary.

The common scaffold is:

```markdown
[DESIGN CHECK]
- Active persona:
- Covering design agreement:
- Scope and expected behavior:
- Specifications and files inspected:
- Component boundaries, ports/adapters, and VO/DTO candidates when applicable:
- Applicable constraints:
- Decisions, assumptions, and unresolved ambiguities:
- Included and omitted AI context:
- Task routing (model/assistant/tool):
- Input/output evidence contract when AI output is involved:
- Verification plan:
```

## Approval Model

### The two human gates, per work plan

The **design agreement**, reached before the work plan's loop starts, and the
**work-plan close**, reached after the Reviewer approves the completed work
plan. Both are mutual and explicit:

- At the start: the Director agrees the plan describes what they want built,
  and the AI agrees it is executable without further interpretation. Recorded
  under `docs/collaboration/agreements/` using
  `docs/templates/design-agreement.md`.
- At the close: the Director reads the Reviewer-approved result and states the
  next direction — or ends the engagement — in the same action.

There is no per-phase and no per-issue human gate. Do not create one, and do
not use a reopening request as a disguised request for deliverable review.

### Self-review, inside a work plan

The Implementer validates its own phase transitions (Red to Green, Green to
Refactor) in the same context that did the work. Self-review requires a
deterministic precondition and a falsification burden, same as any approval,
but not context separation — see "Three constraints" below for which apply.

### AI approval, once per work plan

Issued by the Reviewer persona, in a separate context, over the whole
completed work plan — not per phase, per issue. Typed and scoped — treat these
as distinct and never infer one from another:

- `Specification conformance`: the work plan's issues satisfy their acceptance
  specifications.
- `Phase correctness`: each issue's artifacts belong to the phase that
  produced them, with no later phase's work leaked in.
- `Boundary conformance`: the changes respect the dependency rule, the port
  boundaries, and the boundaries named in the design agreement.
- `Evidence sufficiency`: deterministic verification was run throughout, its
  output is recorded, and every claim states its grounds.

### Three constraints

An approval failing any of these does not count, whatever the record says.
Self-review satisfies (2) and (3); only the Reviewer's work-plan-level
approval must satisfy all three, including (1):

1. **Context separation.** The Reviewer runs in a context separate from the one
   that produced the work, and receives only artifacts, specifications,
   contract documents, and deterministic output. The Implementer's reasoning is
   not admissible as justification. Waived only for Implementer self-review
   within a work plan — never for the Reviewer's own approval, and never for
   contract-file changes, which ADR 0006 governs independently.
2. **Deterministic precondition.** No approval without recorded deterministic
   verification output. AI judgment is additive, never a substitute.
3. **Falsification burden.** The failure scenarios searched for and the
   grounds on which each does not occur. "No problems found" is not an
   approval, at either layer.

Running the Reviewer on a different model or tool than the Implementer is
recommended to reduce shared systematic bias, but is not required.

Record reviews with `docs/templates/review-record.md`, stored under
`docs/collaboration/reviews/`. When handing off or stopping before completion,
use `docs/templates/agent-handoff.md`.

## Source Code Quality

Generated source code must minimize cognitive load for whoever reads it next —
a reviewing persona, a future agent, or the Director inspecting artifacts.
Prefer clear responsibility boundaries, small functions, straightforward names,
and reviewable tests. Do not compress implementation into dense code just to be
minimal.

## Completion

Before reporting completion, check `docs/collaboration/definition-of-done.md`.
Create AI work traces under `docs/collaboration/traces/` when the trace policy
requires it. Use feature-unit branches for feature work. For feature work,
identify local issue or GitHub issue dependencies before creating the branch.

## Project Boundaries

`<Describe the project's runtime and trust boundaries here: whether it is
local-first, cloud-native, or hybrid; which external systems are optional and
replaceable; which datastore is primary; which migration tool is used. Do not
invent full schemas before accepted behavior, reviewed Red tests, or an ADR
require them.>`

## Current Non-Decisions

Technology and design choices intentionally deferred to an ADR rather than
assumed by an agent. Treat these as ADR topics, not assumptions.

- `<Provider/vendor choice>`.
- `<Data store or schema detail>`.
- `<Model/embedding choice>`.
