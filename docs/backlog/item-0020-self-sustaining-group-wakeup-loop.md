# Backlog item: item-0020-self-sustaining-group-wakeup-loop

## Metadata

- Item ID: item-0020
- Title: Design & Review and Implementation groups do not actually watch
  their own queues — the Backlog thread currently relays every wake-up
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: medium
- Suggested planning size: M
- Owner/agent (optional): unassigned

## Summary

The Director's original intent for this model (stated directly, verbatim):
the Implementation group should always be looping/waiting; the Design &
Review group should wait on the backlog and start once something is
approved; the Implementation group should start on a Design-&-Review
-approved work plan once one exists. In short: each group self-sustains a
watch loop over its own queue (backlog for Design & Review, approved work
plans for Implementation), with no third party needed to wake it up.

**Gap found by direct comparison against both the written contract and
today's actual operation:**

- ADR 0016 (`docs/architecture/adr/0016-*.md`) and
  `docs/collaboration/cross-session-messaging.md` describe the two groups
  as "standing," "started once and kept alive," and "autonomous" — but
  neither document specifies an actual self-sustaining watch/poll
  mechanism. They define *who messages whom and how* (`SendMessage`/
  `ListAgents`), not *what triggers a dormant standing session to check its
  own queue without being told*.
- In practice, throughout this session, a Design & Review sub-agent's turn
  simply ended when it ran out of immediate work, becoming unreachable
  (`ListAgents` reporting "no reachable agents"). The Backlog thread had to
  notice this (by checking `ListAgents` or by the user asking for a status
  update) and explicitly `SendMessage` it to resume — repeatedly, dozens of
  times this session. This is a Backlog-thread-mediated relay, not a
  self-driven loop the two groups sustain on their own.

## Why it might matter

The documented model implies more autonomy than actually exists — a later
reader (human or agent) could reasonably expect the standing sessions to
notice new backlog items or completed dependencies on their own, and be
surprised when nothing happens until the Backlog thread manually intervenes.
This also means the Backlog thread's attention is a hidden bottleneck the
contract doesn't disclose.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes.
- Boundaries or non-goals:
  - Do not assume a literal infinite-polling loop is technically available
    to a spawned sub-agent session in this environment — that needs to be
    investigated, not presumed. (The Backlog thread itself has access to a
    self-pacing wakeup mechanism for its own use; whether an equivalent
    exists for a spawned Design & Review or Implementation sub-agent is
    the open question this item's spike must answer.)
  - If true self-sustaining polling turns out not to be available, the
    fallback is to document the Backlog-thread-relay pattern *honestly* as
    the actual mechanism (correcting ADR 0016/cross-session-messaging.md's
    implied autonomy) rather than leaving the documentation overstating
    what happens automatically.
  - Do not weaken ADR 0016 Rule 2's actual autonomy (Design & Review still
    doesn't need Director dialogue once a backlog item is promoted) — this
    item is specifically about the *wake-up* mechanism, not the *judgment*
    autonomy, which already works as intended.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      determine what wake-up/self-scheduling primitives are actually
      available to a spawned sub-agent session in this environment (does
      an equivalent of the Backlog thread's own scheduled-wakeup capability
      exist for sub-agents? can a sub-agent re-invoke itself after a delay?
      is there any event-driven "something changed" signal short of
      another session's `SendMessage`?), then design the closest achievable
      approximation of the Director's intended model, and update ADR
      0016/`cross-session-messaging.md` to state the real mechanism
      precisely — whichever it turns out to be.
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  (existing, this item corrects/completes its wake-up-mechanism gap);
  related: `docs/collaboration/cross-session-messaging.md`

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread ("はい"), after the
  Director directly compared their original intent against the actual
  documented and observed behavior. Per ADR 0016 Rule 2, Design & Review
  proceeds autonomously from here, starting with the spike.
- Reason: Real, evidenced gap between stated intent, written contract, and
  observed operation; ready to run starting with investigation.
