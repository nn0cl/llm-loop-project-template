# Collaboration Scheme: Director-Bounded Design, AI-Closed Execution

This document defines how the human and the AI personas collaborate in this
repository. It does not define application internals.

The governing decision is
`docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`.

The shape is: a human is present for direction, planning, and the design
agreement. After the design agreement, the execution loop is closed — review
and approval inside it are performed by AI personas, and the loop does not stop
for human sign-off.

## Roles

### Director

The human. Present before the loop, not inside it.

Responsibilities:

- state the direction: what is to be built, under which constraints, and what
  would count as it being wrong.
- build the detailed plan with the Planner through dialogue.
- reach the design agreement, explicitly and on the record.
- decide on a reopening request when the loop returns one.

Explicitly **not** Director responsibilities:

- approving phase transitions.
- reviewing tests before implementation.
- signing off on deliverables.
- any other per-artifact approval inside the loop.

If the Director wants to inspect the loop's output, they read the artifacts.
Reading is not a gate, and the loop does not wait on it.

### Personas

Named AI operating roles with distinct responsibilities, inputs, outputs, and
completion criteria: Planner, Specifier, Implementer, Reviewer, Arbiter. The
core set and the rules for extending it are defined in
`docs/collaboration/personas.md`.

An agent states which persona it is operating as, in the design note and in the
work trace. A record that does not name its persona cannot be audited.

### Deterministic Tool

Non-AI tool: formatter, linter, type checker, dependency checker, test runner,
import-boundary checker, migration checker, container orchestration validator.

Responsibilities:

- verify facts that must not depend on model judgment.
- provide repeatable signals for the loop and for CI.

Its output is a precondition for every approval. No persona may approve past a
failing or absent deterministic signal, and none may reinterpret its output as
passing.

## The Loop

```text
Director states direction
  -> Planner <-> Director dialogue          [human present]
  -> Specifier writes acceptance specs      [human present]
  -> DESIGN AGREEMENT (Director + AI)       [human present, gate, documented]
  ============================================================
  -> Phase 0 Design Intake      (Implementer, per task)
  -> Phase 1 Red                (Implementer)
  -> Deterministic verification
  -> Review                     (Reviewer, separate context)
  -> Phase 2 Green              (Implementer)
  -> Deterministic verification
  -> Review                     (Reviewer, separate context)
  -> Phase 3 Refactor           (Implementer)
  -> Deterministic verification
  -> Review                     (Reviewer, separate context)
  -> Done
       |
       +-- deadlock -> Arbiter
       +-- unsettled question / boundary crossing -> reopen design agreement
```

Everything below the double line runs without human presence. The loop stops
only for a reopening request, never for approval of work already done.

## Approval Model

### Human agreement (Director, before the loop)

One gate: the **design agreement**. Mutual and explicit — the Director agrees
the plan describes what they want built, and the AI agrees it is executable
without further interpretation. Recorded under
`docs/collaboration/agreements/`. See `docs/collaboration/design-agreement.md`.

There is no other human gate. Do not create one.

### AI approval (Reviewer, inside the loop)

Typed and scoped, as before:

- `Specification conformance`: the artifact satisfies its acceptance
  specification.
- `Phase correctness`: the artifact belongs to the phase that was run, and no
  later phase's work leaked into it.
- `Boundary conformance`: the change respects the dependency rule, the port
  boundaries, and the boundaries named in the design agreement.
- `Evidence sufficiency`: deterministic verification was run, its output is
  recorded, and every claim states its grounds.

Each is a separate decision. Granting one does not grant another.

### Three constraints on every AI approval

An approval that fails any of these does not count, regardless of what the
record says:

1. **Context separation.** The Reviewer runs in a context separate from the one
   that produced the work, and receives only artifacts, specifications,
   contract documents, and deterministic output. The Implementer's reasoning is
   not admissible as justification.
2. **Deterministic precondition.** No approval without recorded deterministic
   verification output. AI judgment is additive, never a substitute.
3. **Falsification burden.** The Reviewer names the failure scenarios it
   searched for and the grounds on which each does not occur. "No problems
   found" is not an approval.

Running the Reviewer on a different model or tool than the Implementer is
recommended to reduce shared systematic bias, but is not required.

## The Three Invariants

Carried over unchanged from the superseded model, and not weakened by the
removal of human approval:

1. **Every decision produces a document.** A decision that exists only in a
   session transcript did not happen.
2. **Every executed fact leaves evidence.** A command that was run has its
   output recorded. "Tests pass" without output is a claim, not evidence.
3. **Every claim states its grounds.** Assertions in artifacts carry the
   specification, ADR, measurement, or tool output they rest on.

Removing the human raises the cost of violating these, because no reviewer will
reconstruct missing rationale from memory.

## Required Artifacts

Every task leaves enough evidence for another persona or agent to continue.

Design phase:

- work plan or local issue, with persona assignment per task.
- acceptance specifications.
- design agreement record.

Phase 0 Design Intake:

- design note, naming the active persona.
- included and omitted context.
- assumptions and unresolved ambiguities.
- verification plan.

Phase 1 Red:

- failing tests only.
- statement of whether Red is a compile failure or a failing assertion.
- mocked ports or interfaces for every external dependency.
- deterministic verification output.

Phase 2 Green:

- minimal implementation.
- unchanged specifications and tests.
- deterministic verification output.

Phase 3 Refactor:

- refactor summary with behavior-preservation grounds.
- deterministic verification output.
- verification gap statement.

Every review:

- review record naming searched failure scenarios, grounds, and decision,
  stored under `docs/collaboration/reviews/`.

## Decision Gates

The loop stops and returns a reopening request to the Director when:

- a task requires a decision the design agreement does not settle.
- requirements imply a new architecture decision not covered by an accepted
  ADR.
- a boundary named in the design agreement would have to be crossed.
- an external provider, SDK, model, datastore, or schema convention must be
  chosen and the agreement does not choose it.
- a change would alter an accepted specification.
- deterministic verification contradicts an assumption the agreement rests on.
- a task requires secrets, full private data exports, or context the privacy
  policy does not permit.
- the Arbiter finds neither side of a dispute grounded, meaning the contract or
  the agreement is underspecified.
- a falsification criterion named in the agreement is met.

A reopening request names what is unsettled and what the loop needs to
continue. It is not a request to approve work already produced.

The loop does not guess past an unsettled question, and it does not stop
quietly.

## Context Ledger

Each substantial task maintains a short context ledger in the design note or
final answer:

- `Persona`: the active persona.
- `Included`: files, specs, ADRs, and snippets used.
- `Omitted`: relevant-looking context intentionally excluded.
- `Assumptions`: assumptions made for this phase.
- `Open decisions`: questions for a reopening request or a future ADR.
- `Verification`: deterministic checks run, with output, or explicitly not run.
- `Issue links`: local issue IDs, GitHub issue links, and work plan links.
- `Agreement`: the design agreement record this task runs under.

## Handoff Rule

When stopping before completion, the agent states:

- active persona.
- current phase.
- design agreement this work runs under.
- completed artifacts.
- next safe action.
- blockers, and whether any is a reopening request.
- files changed.
- verification status, with output.

This keeps work resumable by another agent without rereading the entire
repository — which matters more here, since no human is tracking loop state.

## Quality Bar

Acceptable work is:

- covered by a recorded design agreement.
- phase-correct, with the active persona named.
- reviewable in small pieces.
- readable with low cognitive load.
- traceable to specifications, ADRs, or the design agreement.
- verified by deterministic tools, with output recorded.
- honest about ambiguity and unverified claims.

Unacceptable work is:

- execution with no covering design agreement.
- implementation before design intake.
- Phase 2 work built on tests that were never reviewed by a separate context.
- an approval issued by the context that produced the work.
- an approval with no deterministic verification output.
- an approval stating "no problems found" with no searched scenarios.
- broad context dumping.
- hidden assumptions.
- modifying specifications or tests to make implementation pass.
- turning AI prose into accepted design without an ADR or a design agreement.
- dense or multi-responsibility source code that is hard to review.
- reintroducing a human approval gate inside the loop without an ADR
  superseding ADR 0001.
