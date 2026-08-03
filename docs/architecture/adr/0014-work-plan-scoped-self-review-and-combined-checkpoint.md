# ADR 0014: Work-Plan-Scoped Self-Review and a Combined Human Checkpoint

## Status

Accepted. Covered by `DA-2026-08-03-01`. Supersedes the execution-loop
portions of ADR 0001 (the per-phase, separate-context Reviewer requirement,
and the single-gate model). ADR 0001's Director/Planner/Specifier design
phase, and its Approval Model's three constraints on any approval that does
occur in a separate context, are unchanged.

## Context

ADR 0001 established one human gate — the design agreement, before the loop —
and required every phase transition inside the loop (Red, Green, Refactor) to
be approved by the Reviewer persona in a context separate from the one that
produced the work. That granularity means a Reviewer invocation, in a
separate context, at every phase boundary of every issue.

The Director requested a coarser granularity: review and approval within a
single issue's Red/Green/Refactor cycle should happen in the same context
that did the work, and the separate-context Reviewer should operate once, at
the level of a completed work plan, rather than once per phase per issue.
Correspondingly, the Director's own involvement should be scoped to a work
plan rather than to individual deliverables: state the direction once at the
start, and once at the end, read the AI-approved result and state the next
direction in the same action.

This repository's own recent history is the direct evidence for what this
trades away. `scripts/check-contract-consistency.py` went through six rounds
of separate-context review before approval; four of those rounds found the
checker claiming coverage it did not have, and every one of those findings
was invisible to the context that produced the checker, because that context
cannot see its own blind spots by construction. Self-review does not remove
that risk. It relocates it: instead of being caught at the next phase
boundary, a self-review blind spot now survives until the work plan's
completion, where it either surfaces at the work-plan-level Reviewer pass or
does not surface until the Director's own read of the result.

The Director accepted this tradeoff explicitly, in exchange for fewer
separate-context invocations per issue and a human touchpoint scoped to work
plans rather than to every deliverable. This ADR records the acceptance, not
just the mechanism, so a future reader does not mistake the reduced review
frequency for an oversight.

## Decision

1. **A design agreement covers exactly one work plan.** The design-agreement
   boundary and the execution-loop boundary are the same thing. Starting a
   new work plan means reaching a new design agreement — the Director's
   initial-direction dialogue with the Planner, as under ADR 0001, unchanged.

2. **Within a work plan, an issue's Red/Green/Refactor phase transitions are
   validated by the Implementer itself — self-review, not a separate-context
   Reviewer.** Self-review still requires:
   - recorded deterministic verification output (the deterministic
     precondition), and
   - a named statement of the failure scenarios looked for and why each does
     not occur (the falsification burden).

   Only context separation is waived at this layer. An Implementer that
   records neither of the other two has not self-reviewed; it has skipped
   the phase gate.

3. **Once every issue in a work plan reaches self-reviewed completion, the
   work plan as a whole goes through Preflight Validation (per ADR 0013) and
   then exactly one independent Reviewer pass, in a separate context, over
   the work plan's full result.** This Reviewer pass is unchanged from ADR
   0001 in every other respect: it must satisfy all three constraints
   (context separation, deterministic precondition, falsification burden),
   and it is the only approval in the loop that counts as an AI approval of
   record.

4. **Findings from the work-plan-level review become review-finding local
   issues, resolved through the existing Minor Fix Path or an escalation to
   Feature/Architecture Path**, per ADR 0012, unchanged. Rework inside an
   issue during resolution is self-reviewed the same way the original
   execution was.

5. **Closing a work plan is one combined human action, not two.** Once the
   work-plan-level Reviewer approves, the Director reads the result and
   states the next direction — starting a new design agreement, or ending
   the engagement — in the same turn. This is a required checkpoint, not
   optional reading: the next work plan does not start without it. It
   replaces both "review the deliverable" and "decide whether to continue"
   as separate acts.

6. **There is no per-phase and no per-issue human gate.** There are exactly
   two human touchpoints per work-plan cycle: the initial-direction dialogue
   that produces the design agreement, and the combined closing checkpoint
   that ends one work plan and, in the same action, may open the next.

7. **This ADR does not apply to changes to the agent operating contract
   itself.** ADR 0006 governs those independently, requires a separate-context
   Reviewer regardless of work-plan granularity, and is not superseded here.
   Self-review of a contract-file change would validate the rule using the
   context that is changing it — the same unsoundness this ADR exists to
   accept as a tradeoff elsewhere, not to introduce here by accident.

## Consequences

Positive:

- Fewer separate-context Reviewer invocations per unit of work — one per work
  plan instead of one per phase per issue.
- Human involvement is scoped to work-plan boundaries, matching what the
  Director asked for, and is measurably lower-frequency than ADR 0001's model
  in the common case of a work plan with more than one issue.
- The mechanisms this reuses (Preflight, Minor Fix Path, review-finding
  lifecycle) already existed and did not need to be redesigned, only
  re-scoped.

Negative:

- Self-review cannot catch what the producing context cannot see about
  itself. A defect introduced in Phase 1 of an early issue in a large work
  plan is not independently examined until the work-plan-level review, which
  may be many issues later.
- The severity of the negative above scales with work-plan size. This ADR
  does not itself bound work-plan size; that risk is named as a Deferred
  Question in the covering design agreement, not solved here.
- A work plan that fails the work-plan-level review returns a larger unit of
  rework than a phase-level rejection would have, proportional to how much of
  the plan was built on the defect before it was caught.
- The empirical basis for treating context separation as load-bearing (six
  review rounds in this repository's own history, four of which found real
  defects self-review structurally could not have found) applies with equal
  force to the layer this ADR removes it from. That evidence is not
  contradicted by this decision — the tradeoff is accepted with it in view.

## Enforcement

Code review should reject:

- an issue's phase transition (Red to Green, Green to Refactor) validated
  with no self-review record — no deterministic output, or no named failure
  scenarios.
- a work plan's completion reported without a work-plan-level Reviewer
  approval from a separate context.
- a contract-file change approved by self-review rather than under ADR 0006's
  separate-context requirement.
- the Director's closing checkpoint treated as satisfied by "reading" alone,
  with no recorded next-direction statement, or split into two separate
  actions where one is silently skipped.
- a design agreement that spans more than one work plan, or a work plan
  executed with no covering design agreement.
