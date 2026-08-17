# LISS-0022: Define the cross-session messaging (send_message/ListAgents) handoff protocol

## Metadata

- Local issue ID: LISS-0022
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/cross-session-messaging-protocol

## Summary

- Contract file (new): `docs/collaboration/cross-session-messaging.md`
  (governed by ADR 0006).
- Define the concrete message contract between the Design & Review group and
  the Implementation group, so that Invariant 1 ("every decision produces a
  document") holds across a chat-based handoff:
  - **Backlog approval -> Design & Review group**: no message needed; the
    approved backlog item file is itself the trigger and the document.
  - **Design agreement recorded -> Implementation group**: the Design &
    Review group sends a message naming the work-plan path
    (`docs/work-plans/WP-NNNN-*.md`) and the design-agreement path. The
    message body is not the record; the linked files are. The Implementation
    group acknowledges by starting Phase 0 design intake and recording it in
    the work plan or issue, not by chat reply alone.
  - **Issue self-review complete, or work plan Preflight passes ->
    Design & Review group**: the Implementation group sends a message naming
    the Preflight record and, once all issues in the plan are done, requests
    the work-plan-level Reviewer pass.
  - **Reviewer approval or rejection -> Implementation group**: the Design &
    Review group sends a message naming the review record path
    (`docs/collaboration/reviews/...`) and, on rejection, the resulting
    `Type: review-finding` issue IDs.
  - **Director intervention**: a chat message sent directly into a group's
    session (not through the other group) triggers the gated mode defined in
    ADR 0016; the group records the gate and its resolution in the affected
    issue's Work Notes, not only in chat history.
  - State the `ListAgents` usage: how each group discovers the other's
    current session name/ID before sending, and what to do when the target
    session is not found (do not silently proceed — treat as a blocker
    needing the Director, per the existing "unresolved dependency is a
    reopening request" rule).
- State explicitly: a `SendMessage` payload is never itself the deterministic
  record of a decision. It is a trigger that references a file already
  written to the repository.

## Acceptance Notes

- Every handoff direction listed above states: trigger, message content,
  and the file(s) that carry the actual record.
- The document states the "message is a trigger, not a record" rule as a
  named constraint, cross-referencing Invariant 1.
- `ListAgents` failure handling is stated as a reopening-request-worthy
  blocker, not a judgment call.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0021, LISS-0023

## Decisions Not Settled by the Design Agreement

- Exact message text templates are an implementation detail the Implementer
  may choose; the design agreement settles the required content, not the
  wording.

## Context

- Included: ADR 0016 (from LISS-0019), the `SendMessage`/`ListAgents` tool
  descriptions available in this session, `docs/collaboration/ai-human-scheme.md`
  Invariant 1.
- Omitted: n/a
- Assumptions: `SendMessage` and `ListAgents` are available in the sessions
  that will run each group; if a target project's environment lacks them,
  this document should say so is a precondition, not silently degrade.

## AI Planning Records

### AIP-0022-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A
  - N/A reason: reasoning-effort setting is not surfaced to this session by
    the harness
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementer persona, single agent, single
  attempt
- Compatibility state: Verified — `SendMessage`/`ListAgents` tool
  descriptions read directly from this session's tool list
- Intended scope: one new contract document; no code changes
- Estimated token range: 3,000–7,000
- Estimated token midpoint: 4,500
- Token metric: output tokens for the new document
- Estimation basis: five handoff directions, each needing a short worked
  example
- Assumptions: none beyond tool availability noted above
- Confidence: medium — protocol documents tend to need a second pass once
  the Reviewer exercises an actual handoff scenario
- Revises: none
- Revision reason: n/a
- Superseded by: none

## References

- `SendMessage` / `ListAgents` tool descriptions (this session's tool list)
- `docs/collaboration/ai-human-scheme.md` (Invariant 1)

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through: every handoff direction traces to a file path, not only a
  chat message.
