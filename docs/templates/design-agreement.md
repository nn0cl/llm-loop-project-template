# Design Agreement Template

Use this to close the design phase with the Director. This is the only gate a
human signs. After it is recorded, the execution loop runs closed.

Store the completed record at
`docs/collaboration/agreements/YYYY-MM-DD-<slug>.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID:
- Date:
- Director:
- Planner / Specifier personas (model or tool used):
- Supersedes agreement (if any):

## Direction

State the Director's framing in the Director's terms — what is to be built,
under which constraints.

- 

## Scope

- In scope:
- Explicitly out of scope:

## Plan

One row per task. Every task names its persona, acceptance criterion, and
verification method, or the plan is not finished.

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |

Sequencing and dependencies:

- 

## Specifications

Specification files this agreement covers:

- `docs/specs/`

## Boundaries

Architecture and dependency constraints the loop must not cross without
reopening this agreement.

- 

## Settled Ambiguities

Every question raised during planning, and the answer agreed.

| Question | Answer | Decided by |
|---|---|---|
|  |  |  |

## Deferred Questions

A deferral with no settling condition is not a deferral — it is an unsettled
question that will stop the loop.

| Question | Condition that will settle it |
|---|---|
|  |  |

## Verification

Deterministic checks that gate approval for this work. Name the commands.

- 

## Falsification Criteria

What observable result would show this design was wrong. Without this, the
work has no negative case and the loop cannot tell success from momentum.

- 

## Agreement

Both statements are required. Neither side reaches agreement alone.

- [ ] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [ ] **AI**: this plan and these specifications are executable without further
      interpretation. Nothing in them requires guessing at a rule that was
      never stated.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

Append one row each time the loop returns a reopening request against this
agreement.

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
