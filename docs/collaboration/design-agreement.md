# Design Agreement

The design agreement is the first of two gates a human signs per work plan in
this repository. It marks the end of the design phase and the start of the
closed execution loop for exactly one work plan; the second gate is the
work-plan close (see "Closing a work plan" below).

Before it, the Director is present: stating direction, and building the plan
with the Planner through dialogue. After it, the Director is not present
inside the work plan — no phase approval, no test review, no per-issue
sign-off. Phase transitions within an issue are self-reviewed by the
Implementer; the Director's next contact with the work is at its close.

Because these two gates carry the weight the removed per-phase gates used to
carry, a vague agreement produces a loop that runs confidently in the wrong
direction, and there is no per-phase reviewer downstream to notice — only the
work-plan-level Reviewer, once, at the end.

## What the design phase produces

1. A direction stated by the Director for one work plan: what is to be built,
   under which constraints, and what would count as it being wrong. Per
   `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
   (ADR 0016) Rule 2, this direction may be stated once, at
   `docs/backlog/item-NNNN-*.md` approval, rather than freshly for each work
   plan the item eventually produces — see "Backlog-item-level agreement"
   below.
2. A plan built with the Planner — through dialogue with the Director at
   backlog-item approval, or autonomously by the Design & Review group
   within that approved item's stated scope, per ADR 0016 Rule 2 — covering
   scope, decomposition, sequencing, and the persona assigned to each task
   in that work plan.
3. Acceptance specifications written by the Specifier, at the level of detail a
   test can be written from.
4. A design agreement document recording all of the above as agreed.

An agreement covers exactly one work plan. A second work plan reaches its own
agreement, even when it follows directly from the first at the work-plan
close.

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

### Backlog-item-level agreement

Per ADR 0016 Rule 2, the Director's agreement statement above may be given
at `docs/backlog/item-NNNN-*.md` approval, in advance of the specific work
plan it authorizes, instead of through a fresh live dialogue turn for that
work plan. When this applies:

- the Design & Review group produces the plan, the specifications, and this
  record's contents autonomously, within the scope the approved backlog
  item states;
- the record's "Agreement" section cites the backlog item's approval as the
  basis for the Director's agreement statement, rather than a fresh
  transcript of a live turn for this specific work plan;
- the AI's own executability statement is still made fresh, by the Design &
  Review group, against the actual plan and specifications it produced —
  ADR 0016 does not, and cannot, pre-approve the AI's half of "Reaching
  agreement" before the plan exists to be judged executable.

This does **not** weaken "Silence is not agreement" above. Backlog-item
approval is itself an explicit, on-the-record act by the Director — not
silence, and not proceeding without objection — and it is scoped strictly to
what the backlog item states. A work plan that goes beyond the approved
backlog item's stated scope is not covered by backlog-item-level agreement;
it requires its own reopening request, per "Reopening the agreement" below,
the same as any other decision the agreement does not settle.

### Intervention-gated provisional records

Per ADR 0016 Rule 4, if the Director sends a chat message directly into
either group's session while a design-agreement record is being produced or
amended, the specific in-flight item is gated to per-step Director approval
until a resolving instruction. Any design-agreement content touched while
that gate is active is **provisional**: the record must state that it is
provisional and name the gate, and it does not count as reached agreement
under "Reaching agreement" above until the Director's resolving instruction
confirms it. A provisional record is not silently promoted to an agreed
record by the gate simply lapsing or being forgotten — the resolving
instruction is what removes the provisional marking.

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

## Review Summary Packet

Before the work-plan-level Reviewer pass — after Preflight Validation
passes, per `CLAUDE.md`'s "Work-Plan Review" — the work plan's own
"Review Summary Packet" section (`docs/templates/work-plan.md`) is
filled in as the Reviewer's canonical review input. Per item-0012 facet 6
("Review records as summary packets"): making the Reviewer read every
trace in full raises cognitive load without a matching audit benefit for
what changed since the last review. A Reviewer session should read the
packet first, and treat detailed traces, self-reviews, and issue Work
Notes as linked evidence to consult for falsification, not as the
review's own entry point.

This does not weaken the Reviewer's own falsification burden or the
deterministic-precondition/context-separation constraints in
`CLAUDE.md`'s "Constraints" — a Reviewer that finds the packet's own
claims insufficient, or needs to verify a specific detail, still reads
the underlying trace or issue file directly, the same way it would
independently re-run a deterministic check rather than trust a pasted
claim (per `docs/collaboration/design-review-perspectives.md`'s
"Re-verify state that could have changed underneath you"). The packet
changes where the review *starts*, not how rigorously it must actually
search.

## Closing a work plan

The second gate, per
`docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.
It happens once, after every issue in the work plan has reached self-reviewed
completion, passed Preflight Validation, and been approved by the
work-plan-level Reviewer in a separate context.

Closing is one combined action, not two:

- the Director reads the Reviewer-approved result, and
- states the next direction — opening a new design agreement for the next
  work plan — or ends the engagement,

in the same turn. It is not satisfied by reading alone with no stated next
step, and it is not two separate acts performed at different times by
default.

This specific work plan's own successor does not start without this — the
Director's next-direction statement, which opens the next work plan's
agreement, is part of the same combined close action. Per
`docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
Rule 3, this does not block unrelated, concurrently in-flight work plans in
either group — only the one work plan being closed, and what directly
follows from closing it, wait on this action. A work plan that has not
closed is not superseded by a new direction stated mid-plan — that is a
reopening request against the current agreement, not the start of a new one.

## Related documents

- `docs/collaboration/personas.md` — who does what on each side of these
  gates.
- `docs/collaboration/ai-human-scheme.md` — the full loop and approval model.
- `docs/templates/design-agreement.md` — the record template.
- `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
  — the decision that defines these two gates and what runs between them.
