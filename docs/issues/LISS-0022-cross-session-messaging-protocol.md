# LISS-0022: Define the cross-session messaging (send_message/ListAgents) handoff protocol

## Metadata

- Local issue ID: LISS-0022
- GitHub issue: none
- Status: review
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  created `docs/collaboration/cross-session-messaging.md` defining the
  governing "message is a trigger, not a record" rule, `ListAgents` usage
  and not-found handling (reopening-request-worthy blocker), and the five
  handoff directions (backlog approval; design agreement recorded; issue
  self-review complete / work-plan Preflight passes; Reviewer approval or
  rejection; Director intervention), each stating trigger, message content,
  and the record file(s). Also added a "Handling a missing or malformed
  handoff" section extending the same treatment to a message naming a file
  that does not exist or does not match its claimed content. This landing
  is itself a live worked example of direction 2 (design agreement recorded
  -> Implementation group): this session received exactly such a
  `SendMessage` handoff naming WP-0002 and `DA-2026-08-18-01`.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md`.
- 2026-08-18, real-failure follow-up (Implementer, same session): this
  session's own attempt to reply to the peer that sent its WP-0002 handoff
  hit exactly the failure this document warns about. Firsthand, confirmed
  facts: `SendMessage` with `to: "general-purpose"` (the label shown in the
  incoming message's own `from` attribute) failed twice, verbatim retry
  included — `"No agent named 'general-purpose' is reachable."`;
  `ListAgents` was searched for directly and was not present as a callable
  tool in this session at all, despite `SendMessage`'s own description
  naming it as the discovery mechanism; `SendMessage` with `to: "main"`
  succeeded on the first attempt (`"Message queued for the main
  conversation's next turn."`), confirming this session is itself a
  background subagent of its sender, and that address was the fix. Added
  "Confirmed failure mode: `ListAgents` absent, and a guessed reply
  address" to `docs/collaboration/cross-session-messaging.md`, stating this
  precisely and the resulting rule: a `from=` display label is not proof of
  a resolvable `SendMessage` address; try `to: "main"` first for a direct
  spawn parent/child reply; a handoff sender should give its own
  `ListAgents`-verified name or agent ID in the message body rather than
  relying on the receiver to infer one.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form (per this session's explicit
instruction, notwithstanding this issue's `M` planning size).

```text
Phase / finding: Architecture Path design note -> new file
  docs/collaboration/cross-session-messaging.md

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

Risks considered:
  1. One of the five handoff directions is missing trigger, message
     content, or record file.
  2. The "message is a trigger, not a record" rule is stated only
     implicitly (e.g. buried in one direction's bullet) rather than as a
     named, cross-referenced constraint.
  3. `ListAgents` failure handling is left as an implicit judgment call
     rather than stated as a reopening-worthy blocker.
  4. The document leaves the checker's reference check newly broken (a
     dangling link to a file that still does not exist).
  5. The document duplicates content that already lives in
     `docs/collaboration/ai-human-scheme.md` or ADR 0016 instead of
     cross-referencing it.

Why each does not occur:
  1. Read-through of "The five handoff directions": each of the five
     numbered subsections (1. Backlog approval, 2. Design agreement
     recorded, 3. Issue self-review / Preflight, 4. Reviewer approval or
     rejection, 5. Director intervention) has its own "Trigger"/"Message
     content"/"Record" (or equivalently labeled) bullets naming a concrete
     file path or explicit "none needed" with reasoning.
  2. The rule has its own top-level section, "The governing rule: a message
     is a trigger, not a record," stated before any handoff direction, and
     explicitly cites Invariant 1 by name ("This follows directly from
     Invariant 1: a decision that exists only in a session transcript did
     not happen").
  3. The "`ListAgents` — locating the other group's session" section states
     plainly: "this is a blocker, not a judgment call," lists four things
     not to do (guess, retry indefinitely, assume pickup, treat absence as
     'no work in flight'), and directs the reader to
     `docs/collaboration/design-agreement.md`'s "Reopening the agreement"
     rules by name.
  4. Ran the checker after creating the file (output above): zero
     failures, meaning every reference this new file makes (to ADR 0016,
     `ai-human-scheme.md`, `session-start-and-resume.md`,
     `design-agreement.md`, `docs/backlog/README.md`) resolves, and the two
     previously-pending references from ADR 0016 itself now resolve too.
  5. The document states protocol-specific content only (the five handoff
     directions, the trigger rule, `ListAgents` handling) and points to
     ADR 0016 for the topology/rules it implements and to
     `ai-human-scheme.md` for the loop and Invariant 1, via a "Related
     documents" section, rather than restating either.
```
