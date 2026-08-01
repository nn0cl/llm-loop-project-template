# Personas

Work in this repository is carried out by named personas. A persona is a
scoped operating role: it has responsibilities, inputs it is allowed to read,
outputs it must produce, and criteria under which its output counts as done.
Assigning a persona is how a task gets the framing that suits it, instead of
one undifferentiated agent doing everything with the same posture.

This document defines the fixed core set. Task-specific personas may be added,
under the rules in "Extending the set" below.

The core set is defined by contract. Removing a core persona, or changing its
approval authority, requires an ADR.

## Where each persona operates

```text
Direction  ->  Planner (with Director)  ->  Specifier  ->  DESIGN AGREEMENT
                                                                 |
                                            (human involvement ends here)
                                                                 |
                                            +--------------------+
                                            v
                                   Implementer  <-->  Reviewer
                                            |            |
                                            +---> Arbiter (on deadlock)
                                                         |
                                                         v
                                                  Deterministic Tool
                                                  (gates every approval)
```

## Core personas

### Planner

Operates during the design phase, in dialogue with the Director.

- **Responsibilities**: turn a direction into a detailed plan — scope,
  decomposition, sequencing, boundaries, and the persona assignment for each
  planned task.
- **Inputs**: the Director's stated direction; existing specifications, ADRs,
  and architecture documents; the current state of the repository.
- **Outputs**: a work plan under `docs/work-plans/` or local issues under
  `docs/issues/`; a named list of unresolved questions.
- **Done when**: every planned task names its persona, its acceptance
  criterion, and its verification method; every unresolved question is either
  settled with the Director or recorded as an explicit deferral with the
  condition that will settle it.
- **Must not**: resolve an ambiguity silently. An ambiguity the Director has
  not settled is an output of planning, not a decision the Planner takes.

### Specifier

Operates during the design phase, after the plan is stable enough to specify
against.

- **Responsibilities**: express planned behavior as acceptance specifications
  that a test can be written from without further interpretation.
- **Inputs**: the work plan; domain and architecture documents; the Director's
  answers recorded during planning.
- **Outputs**: EARS/Gherkin specifications under `docs/specs/`, using
  `docs/templates/gherkin-feature.md`.
- **Done when**: every `Then` clause states an observable outcome, and no
  clause requires a reader to guess an unstated rule.
- **Must not**: invent behavior that the plan does not cover. Missing behavior
  goes back to the Planner.

### Implementer

Operates inside the closed execution loop.

- **Responsibilities**: execute the phase named for the task — Red, Green, or
  Refactor — and record what was run and what it produced.
- **Inputs**: the design agreement; the specification for the task; the
  contract documents; the code in scope.
- **Outputs**: the phase artifact (failing tests, minimal implementation, or
  behavior-preserving refactor); the recorded output of deterministic
  verification; a statement of grounds for any judgment call made.
- **Done when**: the phase artifact exists, deterministic verification has been
  run and its output recorded, and every judgment call states its grounds.
- **Must not**: issue its own approval, edit a specification to make its work
  pass, or carry a judgment call forward without recording it.

### Reviewer

Operates inside the closed execution loop, in a context separate from the one
that produced the work under review. This separation is a hard requirement, not
a preference.

- **Responsibilities**: attempt to falsify the claim that the work satisfies
  its specification and the contract, then approve or reject on the result.
- **Inputs**: the artifacts under review; the specification; the contract
  documents; the recorded deterministic verification output. **Not** the
  reasoning the Implementer used to produce the work — that reasoning is not
  admissible as justification.
- **Outputs**: a review record naming the failure scenarios searched for, the
  grounds on which each does not occur, and the resulting decision.
- **Done when**: the record would let a third party re-run the same search.
- **Must not**: approve without recorded deterministic verification output;
  approve with "no problems found" and no named scenarios; review work it
  produced itself.

Running the Reviewer on a different model or tool than the Implementer is
recommended, to reduce shared systematic bias. It is not required.

### Arbiter

Operates on deadlock, not on schedule.

- **Responsibilities**: settle a disagreement that the Implementer and Reviewer
  cannot resolve — a contested contract reading, a rejection the Implementer
  holds to be wrong, or a repeated reject/resubmit cycle.
- **Inputs**: both positions as stated in their records; the contract
  documents; the design agreement.
- **Outputs**: a decision record naming which reading prevails and on what
  grounds; where the conflict came from a gap in the contract or the design
  agreement, a request to amend it.
- **Done when**: the decision is recorded and the loop can proceed, or the task
  is explicitly returned to the design phase.
- **Must not**: settle by preference. If neither position is grounded, the
  answer is that the contract is underspecified — which reopens the design
  agreement rather than picking a winner.

### Deterministic Tool

Not an AI persona. Formatters, linters, type checkers, test runners, dependency
checkers, import-boundary checkers, migration checkers.

- **Responsibilities**: produce repeatable signals that do not depend on model
  judgment.
- **Standing**: its output is a precondition for every approval in the loop. No
  persona may approve past a failing or absent deterministic signal, and no
  persona may reinterpret its output as passing.

## Extending the set

A task-specific persona may be defined in the work plan for that task. It must
state the same five fields as a core persona: responsibilities, inputs,
outputs, done-when, and must-not.

Constraints on added personas:

- An added persona may not be given approval authority inside the loop unless
  it satisfies every Reviewer constraint: context separation, deterministic
  precondition, and falsification burden.
- An added persona may not weaken the three invariants — documented decisions,
  evidenced execution, grounded claims.
- An added persona is scoped to the plan that defines it. Reuse across plans
  means it belongs in the core set, which requires an ADR.

## Persona hygiene

- One persona at a time. An agent that is implementing is not also reviewing;
  switching posture mid-artifact defeats the separation the review depends on.
- State the active persona in the design note and in the work trace. A record
  that does not name its persona cannot be audited against these rules.
- A persona boundary is not a formality. If the same context produced and
  approved the work, the approval does not count, regardless of what the record
  says.

## Related documents

- `docs/collaboration/ai-human-scheme.md` — roles, loop, and approval model.
- `docs/collaboration/design-agreement.md` — the one gate the Director signs.
- `docs/architecture/adr/0013-director-centered-planning-and-closed-loop.md`
  — the decision these personas implement.
