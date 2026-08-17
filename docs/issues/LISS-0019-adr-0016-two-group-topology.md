# LISS-0019: Write ADR 0016 — standing two-group session topology and backlog-gated autonomy

## Metadata

- Local issue ID: LISS-0019
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Specifier)
- Related branch: process/adr-0016-two-group-topology

## Summary

- Write `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  using `docs/templates/adr.md`.
- The ADR must state, as a testable rule:
  1. Two standing session groups connected via the `SendMessage` /
     `ListAgents` cross-session tools: the **Design & Review group** (Planner,
     Specifier, Reviewer, Arbiter) and the **Implementation group**
     (Implementer). Persona-to-group mapping is fixed; see LISS-0020.
  2. Director approval is granted at the `docs/backlog/item-NNNN-*.md` level.
     Once a backlog item is approved, the Design & Review group may
     autonomously perform requirement organization, research (including
     spikes under `docs/spike/`), method/approach study, and produce the
     work plan, specifications, and the design-agreement record for that
     item — with no further blocking Planner-Director dialogue per work
     plan. This supersedes ADR 0001's requirement that every design
     agreement is reached through a live Planner-Director dialogue turn by
     turn; the dialogue may now happen once, at backlog-item approval, with
     downstream planning delegated.
  3. Multiple work plans may be in flight concurrently across both groups.
     A work plan awaiting the Director's closing checkpoint (ADR 0014) does
     not block the Design & Review group from continuing design work on the
     next backlog item, nor the Implementation group from continuing
     execution on another already-agreed work plan. This supersedes ADR
     0014 clause 6's "the next work plan does not start without [close]".
  4. **Intervention channel.** At any time, the Director may send a chat
     message directly into either group's standing session. Receipt of such
     a message converts the specific in-flight item being worked at that
     moment — not the group's other concurrent work — into a human-approval
     -gated mode: the group continues its development-loop and review work
     on that item, but each subsequent step requires the Director's explicit
     approval before proceeding. This gated mode persists until the
     Director gives a resolving instruction, which either restores
     autonomous progress on that item or redirects it. Other concurrently
     in-flight work plans or backlog items in either group are unaffected
     and continue under the standing backlog-level authorization.
  5. Autonomous progress under this ADR remains bounded by the project's
     operational rules and applicable law; this is a standing constraint,
     not a per-item checkbox.
  6. The two existing human gates (design agreement, work-plan close) are
     unchanged in kind; only their blocking behavior across concurrent work
     plans, and the backlog-level batching of the design-agreement dialogue,
     change.
- State explicitly which ADR 0001 and ADR 0014 clauses are superseded, and
  which parts remain in force (the three invariants, the Reviewer's three
  constraints, the Implementer's self-review requirements, ADR 0006's
  contract-file governance — none of these are altered).

## Acceptance Notes

- ADR file exists at the path above, `Status: Accepted`, citing the covering
  design agreement (`docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`)
  once recorded.
- Read-through confirms the Decision section states each of the six points
  above as a testable rule, not prose description.
- Status section of ADR 0001 and ADR 0014 updated (or a note added) pointing
  forward to ADR 0016 for the clauses it supersedes, mirroring how ADR 0001's
  own Status section already points to ADR 0014.

## Dependencies

- Parent: WP-0002
- Depends on: none
- Blocks: LISS-0020, LISS-0021, LISS-0022, LISS-0023, LISS-0024, LISS-0025,
  LISS-0026
- Related: docs/architecture/adr/0001, docs/architecture/adr/0014

## Decisions Not Settled by the Design Agreement

- None known. Escalate to a reopening request if ADR drafting surfaces a
  rule the design agreement does not settle.

## Context

- Included: ADR 0001, ADR 0014, `docs/collaboration/personas.md`,
  `docs/collaboration/ai-human-scheme.md`,
  `docs/collaboration/design-agreement.md`, the Director dialogue recorded in
  the covering design agreement's Direction section.
- Omitted: application-level specs (this is a governance/process change with
  no application specification).
- Assumptions: the next available ADR number is 0016 (0001–0015 exist at
  planning time).

## AI Planning Records

### AIP-0019-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A
  - N/A reason: reasoning-effort setting is not surfaced to this session by
    the harness
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Specifier persona, single agent, single attempt
- Compatibility state: N/A (no dependency/version claim)
- Intended scope: one new ADR file; no code changes
- Estimated token range: 3,000–8,000
- Estimated token midpoint: 5,000
- Token metric: output tokens for the ADR draft plus one revision pass
- Estimation basis: comparable to ADR 0014's length and the prior agreement's
  Task 1 scope
- Assumptions: no dependency-adoption evidence section needed (no library
  selection)
- Confidence: medium — the supersession wording for two prior ADRs at once is
  more intricate than a single-ADR supersession
- Revises: none
- Revision reason: n/a
- Superseded by: none

## References

- `docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
- `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
- `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (structural precedent for a governance-superseding ADR plus propagation)

## Work Notes

- 

## Verification

- Read-through against the design agreement's Direction and Settled
  Ambiguities sections.
- `scripts/check-contract-consistency.py` (run after LISS-0020–0011 also
  land, since consistency is a whole-work-plan property).
