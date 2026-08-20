# LISS-0063: Document the check-and-spawn wake protocol in ADR 0016 and cross-session-messaging.md

## Metadata

- Local issue ID: LISS-0063
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Architecture Path
- Type: architecture
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. Size `M` because it edits
  two agent operating contract files (ADR 0006 governance: separate-
  context Reviewer required, plus a mandatory AI work trace) even though
  the actual content added is narrowly scoped and fully specified below.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`)
- Related branch: process/promote-item-0020 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`'s own spike
(`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`) found
that ADR 0016 and `docs/collaboration/cross-session-messaging.md` describe
the Design & Review and Implementation groups as "standing" and
"autonomous" without ever specifying an actual wake-up mechanism, and that
no primitive in this environment lets a fully-dormant session revive
itself unprompted. `docs/issues/LISS-0062-...md`'s own settled decision
(Director-approved, recorded in that issue's Work Notes) resolves this
with a **check-and-spawn / queue-continuation protocol**, quoted there
verbatim, that reassigns responsibility for waking the next layer to the
event that produces new approved work, rather than to the dormant session
itself. This issue documents that protocol precisely in both contract
files, replacing the vague language with the concrete mechanism.

## Acceptance Notes

### 1. `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`

Add a new `### Rule 7` immediately after the existing `### Rule 6 — What
is unchanged` section (currently ending at line ~227, immediately before
`## Supersession, precisely`), with this exact content:

```markdown
### Rule 7 — Check-and-spawn wake protocol

Neither standing session is expected to revive itself from full dormancy
with no external trigger — no primitive in this environment provides
that (confirmed by direct investigation,
`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`).
Instead, responsibility for waking the next layer moves to the event that
produces new approved work:

1. **Backlog approval -> Design & Review.** When the Backlog thread
   approves a backlog item (`docs/backlog/item-NNNN-*.md` moves to
   `Status: promoted`), the Backlog thread checks, via `ListAgents`,
   whether a Design & Review session is already running. If one is
   found, it sends the new item to that session via `SendMessage`. If
   none is found, it spawns one (Agent-tool, worktree-isolated, per the
   existing convention this repository already uses for Implementation-
   group dispatch) with the approved item as its task.
2. **Work-plan approval -> Implementation.** When the Design & Review
   group has a work plan ready for implementation (a freshly built plan
   from the Planner, or a Reviewer-approved plan awaiting execution), the
   Design & Review group itself checks, via `ListAgents`, whether an
   Implementation session is already running. If one is found, it sends
   the work plan to that session via `SendMessage`. If none is found, it
   spawns one.
3. **Queue continuation before going idle.** Inside each standing loop
   (Design & Review, Implementation), before going idle after finishing a
   task, the loop checks its own queue for other already-approved-but-
   unstarted work — promoted backlog items not yet picked up, for Design
   & Review; Reviewer-approved work plans not yet implemented, for
   Implementation — and proceeds directly to the next one if any exists.
   A loop goes idle only when its own queue is genuinely empty.
4. **Resume before duplicate-spawn.** Before any party spawns a new
   session for a role (Backlog thread spawning Design & Review, Design &
   Review spawning Implementation, or any session recovering after an
   error), it first checks whether a session already exists for that
   role — including one that has just failed or errored, since its git
   worktree and branch survive the failure and may hold uncommitted or
   unpushed work. If a prior worktree/branch for that role's in-flight
   task exists and has not been merged or cleaned up, the spawning party
   resumes it (`SendMessage` to its `agentId` once reachable, or a new
   session re-pointed at the same worktree/branch) rather than spawning a
   fresh session that would duplicate the worktree or strand the earlier
   content.

This closes the gap
`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md` named: ADR
0016 and `docs/collaboration/cross-session-messaging.md` previously
described the two groups as "standing" and "autonomous" without
specifying a concrete wake-up mechanism. It does not claim full
self-revival from dormancy is achieved — no primitive in this
environment delivers that (per the spike). The one residual case is
brand-new work arriving while both loops are fully idle and no session
exists to check `ListAgents` on either's behalf; that case still needs
the Backlog thread (or whatever originates the first approval) to
perform rule 1's own check-and-spawn, which is the natural entry point,
not a gap this protocol fails to close.
```

Update the ADR's own **Status** section (top of file) to add, after the
existing `Follow-up issues: LISS-0020 through LISS-0026...` sentence, a
new sentence: "Rule 7 (the check-and-spawn wake protocol) is covered by a
separate, later design agreement, `DA-2026-08-20-06`, following
`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`'s own
promotion and the required-first spike
(`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`);
Rules 1-6 remain covered by `DA-2026-08-18-01` as before." Do not remove
or alter any existing Status-section sentence.

Add one new bullet to the **Enforcement** section (at the end of the
file) after the existing bullets:

```markdown
- a spawning party creating a duplicate session/worktree for a role
  without first checking, via `ListAgents`, whether one already exists
  (Rule 7) — including a role recovering from a session that just failed
  or errored, whose worktree/branch may hold undiscovered work.
- a standing loop going idle while its own queue still has
  already-approved-but-unstarted work it did not check for (Rule 7,
  point 3).
```

### 2. `docs/collaboration/cross-session-messaging.md`

Update **direction 1** ("Backlog approval -> Design & Review group",
currently at line ~141-153) — replace its current "Message" bullet
(which currently reads "none needed... If the Director's own workflow
does use `SendMessage`...") with:

```markdown
- **Message**: required, per ADR 0016 Rule 7. On approving a backlog
  item, the Backlog thread checks via `ListAgents` whether a Design &
  Review session is already running. If found, it sends the approved
  item to that session via `SendMessage`; the message still carries no
  content beyond pointing at the backlog item file (the governing rule
  above is unchanged). If no Design & Review session is found — including
  the case where a candidate session exists but is unreachable because it
  just failed or errored, per Rule 7 point 4 — the Backlog thread spawns
  one (Agent-tool, worktree-isolated) with the approved item as its task,
  rather than spawning a fresh one when a resumable worktree/branch for
  an in-flight Design & Review task already exists.
```

Update **direction 2** ("Design agreement recorded -> Implementation
group", currently at line ~155-174) by adding, immediately after the
existing "Message content" bullet and before "Record", a new bullet:

```markdown
- **Wake mechanic**: per ADR 0016 Rule 7, the Design & Review group
  checks via `ListAgents` whether an Implementation session is already
  running before sending this handoff. If found, it sends the work plan
  to that session via `SendMessage`. If not found — including when a
  prior Implementation session for a related, unfinished task just failed
  or errored, leaving a resumable worktree/branch behind, per Rule 7
  point 4 — it spawns one (Agent-tool, worktree-isolated), rather than
  duplicating a worktree that already holds in-flight or uncommitted
  work.
```

Add one new top-level section, placed immediately before `## Handling a
missing or malformed handoff` (currently at line ~247):

```markdown
## Queue continuation and resume-before-duplicate-spawn (ADR 0016 Rule 7)

Two rules apply inside every standing session, independent of which
specific handoff direction triggered its current work, restated here for
this tool's own concrete `SendMessage`/`ListAgents` mechanics (ADR 0016
Rule 7 is the authoritative statement; this section does not add new
substance beyond stating it in terms of this environment's own tools):

- **Before going idle, check the queue.** A standing session finishing
  one task does not simply end its turn — it checks whether other
  already-approved-but-unstarted work exists in its own queue (promoted
  backlog items not yet picked up, for Design & Review; Reviewer-approved
  work plans not yet implemented, for Implementation) and proceeds
  directly to the next one if so. Only a genuinely empty queue is a
  reason to go idle.
- **Before spawning, check for a resumable session.** Before creating a
  new Agent-tool worktree-isolated session for a role, the spawning party
  calls `ListAgents` to check whether a session for that role already
  exists — including one that just failed or errored. A failed session's
  git worktree and branch survive the failure and may hold real,
  committed-but-unpushed work with no other session aware of it. If a
  prior worktree/branch for that role's in-flight task exists and has not
  been merged or cleaned up, resume it — `SendMessage` to its `agentId`
  once it is reachable again, or point a new session at the same
  worktree/branch — rather than spawning a fresh session that would
  duplicate the worktree or strand the earlier content. Per Invariant 1,
  a session's own local commits are real evidence the moment they exist,
  regardless of whether they have been pushed; losing track of a worktree
  that holds them is a process failure this rule exists to prevent, not
  an acceptable cost of a session ending unexpectedly.
```

## Dependencies

- Parent: `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`
- Depends on: `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`
  (`Status: done` — Director's settled decision recorded there)
- Blocks: none
- Related: `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
  `docs/collaboration/cross-session-messaging.md`,
  `docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`

## Decisions Not Settled by the Design Agreement

- None — this issue's scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md`
  (`DA-2026-08-20-06`) and by LISS-0062's own recorded Director decision.

## Context

- Included: `docs/issues/LISS-0062-...md`'s full text (the Director's own
  verbatim decision), ADR 0016's full text, `cross-session-messaging.md`'s
  full text, `docs/spike/case-0003-...md`'s full text.
- Omitted: nothing else — this is a fully bounded, fully specified
  documentation change.
- Assumptions: none. Every inserted sentence above is given verbatim in
  this issue's own Acceptance Notes; the Implementer is not asked to
  paraphrase, summarize, or interpret the Director's decision.

## Trace Requirement

**Mandatory** — both edited files are agent operating contract files
under `docs/collaboration/prompt-instruction-change-control.md`'s own
"Agent Operating Contract Files" list (`docs/architecture/adr/*.md` is
not itself on that list as a blanket pattern, but ADR 0016 specifically
is the ADR this same contract document's own governance already treats
as covering the topology `cross-session-messaging.md` implements — treat
both as requiring a trace here, matching this session's own established
practice for ADR-0016-adjacent contract work). Create
`docs/collaboration/traces/2026-08-20-check-and-spawn-wake-protocol.md`
using `docs/templates/ai-work-trace.md`, per
`docs/collaboration/prompt-instruction-change-control.md`'s Traceability
Rule: which contract file(s) changed, why, and what agent behavior is
expected to change as a result (a spawning party now performs a
`ListAgents` check before spawning; a standing session now checks its own
queue before going idle).

## References

- `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`
- `docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`
- `docs/collaboration/prompt-instruction-change-control.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0023, scoped per the design agreement. Every inserted
  sentence is specified verbatim above. Not yet dispatched.

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `grep -n "Rule 7" docs/architecture/adr/0016-...md` confirms the new
  section landed with the exact heading.
- `git diff` shows the change confined to the two named contract files,
  the new trace file, and this issue's own tracking file.
- The new trace file exists and states the required three facts (which
  files, why, what behavior changes).
