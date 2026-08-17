# Backlog

The backlog holds candidates that are **not yet promised** under a design
agreement. It is a planning ledger, not an execution queue.

## Location and naming

```text
docs/backlog/
├── README.md
├── .gitkeep
└── item-NNNN-short-slug.md
```

Numbering:

- Use four digits: `item-0001`, `item-0002`, …
- Do not reuse numbers.
- Create a file by copying `docs/templates/backlog-item.md`.

## What belongs here

- Feature or improvement ideas not yet on a work plan
- Spike candidates (uncertainty known, not yet investigated)
- Deferred follow-ups from a work-plan close
- Options parked after a spike chose "backlog / drop" (with link)

## What does not belong here

- Work already covered by an active design agreement and work plan
- Acceptance specifications (those live under `docs/specs/`)
- Accepted ADRs
- Review findings (`Type: review-finding` under `docs/issues/`)

## Status values

| Status | Meaning |
| --- | --- |
| `captured` | Written down; no commitment |
| `ready-for-planning` | Enough detail to discuss in a design dialogue |
| `promoted` | Moved onto a work plan / design agreement; link the plan |
| `spiked` | A spike case was opened; link `docs/spike/case-…` |
| `dropped` | Explicitly not doing; keep the reason |

## Rules

1. **No execution from backlog alone.** Do not start Red/Green/Refactor
   against a backlog item until it is promoted into a covering design
   agreement and work plan (or an explicitly covered spike case).
2. **Promotion is a design-phase act.** Planner + Director dialogue, then
   the agreement and work plan name the item.
3. **Spike when uncertain.** If size would be `TBD` or options are open,
   open `docs/spike/case-NNNN-…` and set status `spiked` with the case link.
4. **Close hygiene.** At work-plan close, the Director's next direction may
   promote, spike, drop, or leave items `captured`.
5. **Cost posture.** Prefer options that need no mandatory paid spend when
   quality and fit allow — same judgment bar as spikes
   (`docs/spike/README.md`).
6. **Bulk design-phase gate.** Once the Director approves a backlog item for
   promotion (status `promoted`), that approval is the design-phase human
   gate for the work it authorizes — see
   `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
   Rule 2 and `docs/collaboration/design-agreement.md`'s "Backlog-item-level
   agreement". The Design & Review group may then proceed autonomously,
   within the approved item's stated scope, without a further live
   per-work-plan Planner-Director dialogue turn.
7. **Compliance boundary.** Autonomous progress after backlog approval
   remains bounded by the project's operational rules (this repository's own
   contract documents) and applicable law — a standing constraint, not
   satisfied implicitly or checked once and forgotten. A backlog item that
   would require exceeding either boundary is a reopening request, per
   `docs/collaboration/design-agreement.md`'s "Reopening the agreement", not
   a judgment call the Design & Review or Implementation group resolves on
   its own. See ADR 0016 Rule 5.

## Relationship to issues and spikes

```text
backlog item
  → (optional) spike case     docs/spike/case-NNNN-…
  → promoted to work plan
  → LISS implementation issue + Spec
  → or ADR path when structural
  → or decision issue when only a human can close it
```
