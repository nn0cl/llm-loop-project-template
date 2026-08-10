# Collaboration Scheme: Work-Plan-Scoped Design, Self-Reviewed Execution

This document defines how the human and the AI personas collaborate in this
repository. It does not define application internals.

The governing decisions are
`docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
(design phase, personas, the invariants) and
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
(execution-loop granularity, which supersedes ADR 0001 on this point).

The shape: a human is present for a work plan's initial direction and for one
combined checkpoint at its close. Inside a work plan, an issue's phase
transitions are validated by the Implementer itself — self-review, not a
separate-context Reviewer. Once every issue in the work plan is
self-reviewed and complete, exactly one separate-context Reviewer pass runs
over the whole work plan before it can close.

## Roles

### Director

The human. Present at the start and the close of each work plan, not inside
it.

Responsibilities:

- state the direction for a work plan: what is to be built, under which
  constraints, and what would count as it being wrong.
- build the detailed plan with the Planner through dialogue.
- reach the design agreement covering that work plan, explicitly and on the
  record.
- decide on a reopening request when the loop returns one.
- **close the work plan**: after the work-plan-level Reviewer approves, read
  the result and state the next direction — or end the engagement — in the
  same action. This is the combined checkpoint per ADR 0014, not two separate
  acts.

Explicitly **not** Director responsibilities:

- approving an issue's individual phase transitions (Red, Green, Refactor) —
  those are self-reviewed by the Implementer.
- reviewing tests before implementation.
- signing off on deliverables inside a work plan, before it closes.
- any other per-artifact approval inside the loop.

Between a work plan's start and its close, the Director is not a gate. If they
want to inspect in-progress output, they read the artifacts; reading is not a
gate and the loop does not wait on it. The close is the one point where
reading is mandatory, not optional.

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

Before or during planning, unpromised candidates may live under
`docs/backlog/`, and uncertainty may be closed via spikes under
`docs/spike/case-NNNN-…` (internet research allowed; prefer zero mandatory
paid spend when quality allows). Spikes and backlog items are not substitute
design agreements. Session language and audit/findings flags live in
`docs/collaboration/loop-settings.toml` (see `loop-settings.md`,
`post-hoc-audit.md`, `findings-reuse.md`).

```text
Director states direction for one work plan
  -> Planner <-> Director dialogue          [human present]
  -> Specifier writes acceptance specs      [human present]
  -> DESIGN AGREEMENT (Director + AI)       [human present, gate, documented]
  ============================================================
  for each issue in the work plan:
    -> Phase 0 Design Intake    (Implementer)
    -> Phase 1 Red              (Implementer)
    -> Deterministic verification
    -> Self-review              (Implementer, same context)
    -> Phase 2 Green            (Implementer)
    -> Deterministic verification
    -> Self-review              (Implementer, same context)
    -> Phase 3 Refactor         (Implementer)
    -> Deterministic verification
    -> Self-review              (Implementer, same context)
  ============================================================
  -> Preflight Validation        (Implementer / deterministic tool, work-plan level)
  -> fail -> Implementer correction and repeat Preflight
  -> pass
  -> Review                     (Reviewer, separate context, whole work plan)
       |
       +-- findings -> review-finding local issues -> Minor Fix Path / re-open issue
       +-- approved
  -> WORK PLAN CLOSE (Director: read result + state next direction) [human present, gate]
       |
       +-- next direction -> new design agreement for the next work plan
       +-- no further work -> engagement ends
       |
       +-- deadlock -> Arbiter
       +-- unsettled question / boundary crossing -> reopen design agreement
```

Between the two double lines, the loop runs without human presence. It stops
only for a reopening request, never for approval of work already done. The
work-plan close is not "inside" that stretch — it is the second of the two
human gates this model has, matched to the design agreement at the start.

Preflight Validation is a submission check, not an approval, run at the
work-plan level before the Reviewer sees the plan's result. It may reject a
change for missing evidence or mechanical inconsistency, but it cannot approve
specification conformance, set `wont_do`, or close an ISSUE.

## Approval Model

### Human agreement (Director)

Two gates per work plan: the **design agreement**, at the start, and the
**work-plan close**, at the end — one combined action, not two. Both are
mutual and explicit:

- At the start, the Director agrees the plan describes what they want built,
  and the AI agrees it is executable without further interpretation. Recorded
  under `docs/collaboration/agreements/`. See
  `docs/collaboration/design-agreement.md`.
- At the close, the Director reads the Reviewer-approved result and states
  the next direction (or ends the engagement) in the same turn.

There is no per-phase and no per-issue human gate. Do not create one.

### Self-review (Implementer, inside a work plan)

Every phase transition inside an issue — Red to Green, Green to Refactor — is
validated by the Implementer that did the work, in its own context. Self-review
requires:

- **Deterministic precondition.** Recorded deterministic verification output,
  same as any approval.
- **Falsification burden.** The failure scenarios looked for and why each does
  not occur, same as any approval.

It does **not** require context separation — the Implementer reviews its own
work at this layer. This is the one constraint ADR 0014 waives here, and only
here.

### AI approval (Reviewer, once per work plan)

Issued once, over the whole work plan, after Preflight Validation passes.
Typed and scoped:

- `Specification conformance`: the work plan's issues satisfy their acceptance
  specifications.
- `Phase correctness`: each issue's artifacts belong to the phase that
  produced them, with no later phase's work leaked in.
- `Boundary conformance`: the changes respect the dependency rule, the port
  boundaries, and the boundaries named in the design agreement.
- `Evidence sufficiency`: deterministic verification was run throughout, its
  output is recorded, and every claim states its grounds.

Each is a separate decision. Granting one does not grant another.

### Three constraints on the Reviewer's approval

An approval that fails any of these does not count, regardless of what the
record says:

1. **Context separation.** The Reviewer runs in a context separate from the one
   that produced the work, and receives only artifacts, specifications,
   contract documents, and deterministic output. The Implementer's reasoning is
   not admissible as justification. This constraint is not waived at the
   work-plan level — only the Implementer's own self-review, inside a work
   plan, is exempt from it.
2. **Deterministic precondition.** No approval without recorded deterministic
   verification output. AI judgment is additive, never a substitute.
3. **Falsification burden.** The Reviewer names the failure scenarios it
   searched for and the grounds on which each does not occur. "No problems
   found" is not an approval.

Running the Reviewer on a different model or tool than the Implementer is
recommended to reduce shared systematic bias, but is not required.

Changes to the agent operating contract files themselves are never
self-reviewed, at any granularity. ADR 0006 requires a separate-context
Reviewer for those regardless of work-plan scope, because self-review would
validate the rule using the context that is changing it.

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
- self-review record: failure scenarios looked for, and why each does not
  occur.

Phase 2 Green:

- minimal implementation.
- unchanged specifications and tests.
- deterministic verification output.
- self-review record.

Phase 3 Refactor:

- refactor summary with behavior-preservation grounds.
- deterministic verification output.
- verification gap statement.
- self-review record.

Work-plan close:

- Preflight Validation record, work-plan scoped.
- Reviewer's review record naming searched failure scenarios, grounds, and
  decision, stored under `docs/collaboration/reviews/`.
- the Director's next-direction statement, or a stated end of the engagement.

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
- Phase 2 work built on Phase 1 output with no self-review record — no
  deterministic output, or no named failure scenarios.
- a work plan reported closed with no work-plan-level Reviewer approval from a
  separate context.
- a contract-file change approved by self-review instead of under ADR 0006's
  separate-context requirement.
- an approval with no deterministic verification output, at either layer.
- an approval stating "no problems found" with no searched scenarios, at
  either layer.
- broad context dumping.
- hidden assumptions.
- modifying specifications or tests to make implementation pass.
- turning AI prose into accepted design without an ADR or a design agreement.
- dense or multi-responsibility source code that is hard to review.
- a design agreement spanning more than one work plan.
- treating the work-plan close as satisfied by reading alone, with no
  recorded next-direction statement.
- introducing a human approval gate inside a work plan (per-phase or
  per-issue) without an ADR superseding ADR 0014.
