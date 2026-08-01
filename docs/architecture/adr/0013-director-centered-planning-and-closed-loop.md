# ADR 0013: Director-Centered Planning and an AI-Closed Execution Loop

## Status

Accepted

Supersedes the governance model of ADR 0003 (AI-Human Collaboration
Governance). ADR 0003 remains in the record as the decision this project is
built to test; it is no longer normative.

Supersedes the role definition of ADR 0012 (Rename Referee to Adjudicator).
The human role is renamed again, to `Director`, because its responsibilities
change rather than only its label.

## Context

This repository is a counter-validation project against the human-intervention
model. Under that model a human is present at two points: the initial framing
decision, and feedback on every deliverable an agent produces. The governance
inherited from ADR 0003 encodes the second point directly — a human Adjudicator
approves each phase transition, reviews Phase 1 tests before implementation,
and signs off on completion.

That design assumes standing human judgment is what keeps generated work
correct. This project exists to test the competing claim: that correctness
comes from the written contract and its verification, and that a human inside
the execution loop is a substitute for contracts that are not yet good enough.

The test is only meaningful if the human is actually removed from the loop. As
long as an approval gate remains, a failing contract is silently repaired by
the human standing at the gate, and the result says nothing about the contract.

At the same time, removing the human from planning would not test that claim —
it would test something else entirely (autonomous goal selection), and it would
discard the part of the conventional model that is not in dispute: that a human
decides what is worth building.

## Decision

Adopt a Director-centered planning model with an AI-closed execution loop.

### Human involvement is bounded to three points, all before execution

1. **Direction.** The Director states what is to be built and under which
   constraints.
2. **Detailed planning.** The Director and the Planner persona produce the plan
   through dialogue. This is a conversation, not a review of a finished
   artifact.
3. **Design agreement.** The design phase completes only on explicit agreement
   between the Director and the AI, recorded as a design agreement document.

The Director does not approve phase transitions, does not review tests before
implementation, and does not sign off on deliverables. Fine-grained human
approval is removed by design, not by omission.

### The execution loop is closed

After the design agreement is recorded, review and approval inside the loop are
performed by AI personas. The loop does not stop for a human. It stops for a
contract violation, a missing ground, or a boundary condition that the design
agreement did not settle — and those stops produce a documented request to
reopen the design agreement, not a request for ad-hoc human approval.

### Personas are assigned per task

Work inside the loop is carried out by named personas with distinct
responsibilities, inputs, outputs, and success criteria. A fixed core set is
defined by contract; task-specific personas may be added in the plan. See
`docs/collaboration/personas.md`.

### AI approval is constrained so it cannot become a rubber stamp

Three constraints apply to every approval issued inside the loop:

- **Context separation.** The Reviewer persona runs in a context separate from
  the one that produced the work, and receives only the artifacts and the
  contract documents. The reasoning that produced the work is not available to
  the reviewer as justification.
- **Deterministic precondition.** No approval may be issued without the
  recorded output of deterministic verification. AI judgment is additive to
  that output and never a substitute for it.
- **Falsification burden.** A Reviewer approves by naming the failure scenarios
  it searched for and the grounds on which each does not occur. "No problems
  found" is not an approval.

Running the Reviewer on a different model or tool than the Implementer is
recommended to reduce shared systematic bias, but is not required.

### Three invariants carry over unchanged

These are inherited from the superseded model and are not weakened by removing
human approval:

1. **Every decision produces a document.**
2. **Every executed fact leaves evidence.**
3. **Every claim states its grounds.**

Removing the human raises the cost of violating these, because there is no
longer a reviewer who reconstructs missing rationale from memory.

## Consequences

Positive:

- The claim under test becomes testable: contract quality is no longer masked
  by human repair inside the loop.
- Throughput stops being bounded by human availability at phase boundaries.
- Failure modes surface in artifacts, where they can be studied, instead of
  being absorbed in real time.
- Human attention concentrates where it is least substitutable — deciding what
  to build and agreeing on the design.

Negative:

- A defect that both the Implementer and the Reviewer miss reaches the end of
  the loop with no human checkpoint to catch it. This is accepted as the cost
  of the experiment, and is the primary thing the traces must make visible.
- Correlated blind spots between personas running on the same model are a real
  risk; context separation and the falsification burden mitigate but do not
  eliminate it.
- The design agreement carries more weight than the old phase gates did. A
  vague agreement produces a loop that runs confidently in the wrong direction.
- Deterministic verification becomes load-bearing. Where a project has weak
  tests, the loop has weak brakes.

## Enforcement

Review and CI should reject:

- an execution phase that ran without a recorded design agreement.
- an approval with no recorded deterministic verification output.
- an approval that does not name searched failure scenarios and their grounds.
- a review performed in the same context that produced the work.
- a decision recorded only in a session transcript rather than a document.
- a claim in any artifact that does not state its grounds.
- reintroduction of a human approval gate inside the execution loop without an
  ADR superseding this one.
