# Design Agreement

The design agreement is the single gate a human signs in this repository. It
marks the end of the design phase and the start of the closed execution loop.

Before it, the Director is present: stating direction, and building the plan
with the Planner through dialogue. After it, the Director is not in the loop —
no phase approval, no test review, no sign-off on deliverables.

Because it is the only gate, it carries the weight the removed gates used to
carry. A vague agreement produces a loop that runs confidently in the wrong
direction, and there is no human downstream to notice.

## What the design phase produces

1. A direction stated by the Director: what is to be built, under which
   constraints, and what would count as it being wrong.
2. A plan built with the Planner through dialogue, covering scope,
   decomposition, sequencing, and the persona assigned to each task.
3. Acceptance specifications written by the Specifier, at the level of detail a
   test can be written from.
4. A design agreement document recording all of the above as agreed.

## Reaching agreement

Agreement is explicit and mutual. Neither side reaches it alone:

- The **Director** agrees that the plan and specifications describe what they
  actually want built, and that the stated boundaries are the right ones.
- The **AI** agrees that the plan and specifications are executable without
  further interpretation — that nothing in them requires guessing at a rule
  that was never stated.

If the AI cannot make the second statement, the design phase is not finished,
regardless of the Director's readiness to proceed. Silence is not agreement,
and neither is proceeding without objection.

## What the record must contain

Use `docs/templates/design-agreement.md`. The record must state:

- **Direction**: the Director's framing, in the Director's terms.
- **Scope**: what is in, and what is explicitly out.
- **Plan**: tasks, sequencing, and the persona assigned to each.
- **Specifications**: the specification files this agreement covers.
- **Boundaries**: architecture and dependency constraints the loop must not
  cross without reopening this agreement.
- **Settled ambiguities**: each question raised during planning and the answer
  agreed, with who decided it.
- **Deferred questions**: each question left open, and the condition that will
  settle it. A deferral with no condition is not a deferral.
- **Verification**: the deterministic checks that gate approval for this work.
- **Falsification criteria**: what observable result would show this design was
  wrong. Without this the experiment has no negative case.
- **Agreement**: the Director's agreement and the AI's executability statement,
  both explicit.

Store records under `docs/collaboration/agreements/` as
`YYYY-MM-DD-<slug>.md`.

## Running against the agreement

Inside the loop, the agreement is the authority. Personas read it, do not
amend it, and do not work around it.

A task may only run if a design agreement covers it. Work with no covering
agreement is not started — it is returned to the design phase.

## Reopening the agreement

The loop stops and the agreement reopens when:

- a task requires a decision the agreement does not settle.
- a boundary named in the agreement would have to be crossed.
- a deferred question's settling condition is reached.
- deterministic verification contradicts an assumption the agreement rests on.
- the Arbiter finds neither side of a dispute is grounded, which means the
  contract or the agreement is underspecified.
- a falsification criterion is met.

Reopening is a documented request to the Director naming what is unsettled and
what the loop needs in order to continue. It is not a request for approval of
work already done, and it must not be used as a way to reintroduce
deliverable-level review through the back door.

The loop does not guess past an unsettled question, and it does not stop
quietly. Either the agreement covers the case, or the agreement is reopened
with the gap named.

## Related documents

- `docs/collaboration/personas.md` — who does what on each side of this gate.
- `docs/collaboration/ai-human-scheme.md` — the full loop and approval model.
- `docs/templates/design-agreement.md` — the record template.
