# LISS-0062: Self-sustaining group wake-up mechanism — decision

## Metadata

- Local issue ID: LISS-0062
- GitHub issue: none
- Status: proposed
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: decision
- Priority: medium
- Initial planning size: TBD (this issue records a decision, not
  implementation work; the resulting design agreement/ADR work gets its
  own planning size once opened)
- Current planning size: TBD
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: unassigned — awaiting Director/Backlog-thread response
- Related branch: none — this issue records a decision checkpoint, not
  code or document changes

## Summary

`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`
(`Status: promoted`) asked whether a spawned sub-agent session (Design &
Review or Implementation group) in this environment has access to any
primitive that lets it wake itself up without an external party noticing
and explicitly resuming it. The required-first spike,
`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`
(`Status: closed`, Selection: human-decision), is now closed. Its finding
is not a clean yes/no:

- **No mechanism lets a specific dormant standing session revive itself
  with its own live conversational state and no external trigger.**
  Confirmed directly: `Monitor` and blocking `Bash` sleeps are both
  explicitly scoped to, at most, the current session's own active
  lifetime by their own tool descriptions; neither survives a session
  going fully idle.
- **A real, empirically-confirmed primitive does exist that could reduce
  — not eliminate — the manual-relay burden**: `mcp__scheduled-tasks__*`
  (cron or one-time scheduled tasks) was directly invoked from inside
  this spawned Design & Review session and succeeded, confirming it is
  reachable from a spawned sub-agent context. Each firing starts a fresh,
  stateless session rather than resuming the one that scheduled it — a
  real architectural difference from what "standing session that watches
  its own queue" implies, but one that already fits this repository's own
  `CLAUDE.md` "Session Entry" model (every session, spawned or not,
  already recovers state from repository artifacts, not chat memory).
- A harness-level `Stop` hook (via `.claude/settings.json`) was named as a
  plausible further alternative but was **not independently tested** —
  inferred only from two other skills' own descriptions, per the spike's
  own explicit refusal to presume an unverified capability.
- Background-agent completion notifications (today's actual mechanism)
  are real and already work, but are empirically confirmed insufficient
  on their own: this session went idle and needed an explicit external
  `SendMessage` to resume after every one of the four backlog items
  processed in this thread (0016 batch 1, 0017, 0018, 0019), each time its
  own dispatch queue emptied.

## Acceptance Notes

This issue is resolved when the Director/Backlog thread states a decision
recorded below, and either:

- a follow-up work plan and design agreement are opened to implement the
  chosen mechanism and update ADR 0016/`cross-session-messaging.md`
  accordingly, or
- the Director redirects the approach, and this issue records that
  redirection before any execution work plan opens.

## What is being asked of the Backlog thread

Exactly the question the spike's own Selection reserved:

1. **Adopt candidate B** — scheduled-task-based periodic fresh-session
   polling for one or both standing groups (a cadence and cost/quota
   decision the Backlog thread should weigh in on, since each firing
   consumes model usage even when there is no new work to pick up); or
2. **Accept and honestly document candidate A** — the Backlog-thread-relay
   pattern is the real, permanent mechanism; correct ADR 0016 and
   `cross-session-messaging.md` to state this precisely instead of the
   current implied-but-unspecified "standing"/"autonomous" language, per
   the backlog item's own explicit fallback instruction; or
3. **Authorize a further, narrowly-scoped follow-up spike** specifically
   to test candidate C (a harness `Stop` hook in `.claude/settings.json`)
   before choosing between 1 and 2; or
4. **Hold this item open** for further discussion before any of the above
   proceeds.

## Dependencies

- Parent: `docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`
- Depends on:
  `docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`
  (`Status: closed`)
- Blocks: the follow-up design-agreement/ADR-correction work (not yet
  opened)
- Related:
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
  `docs/collaboration/cross-session-messaging.md`

## Decisions Not Settled by the Design Agreement

- No design agreement covers this item yet beyond the backlog-item-level
  approval (`docs/backlog/item-0020-...md`, `Status: promoted`) — per
  that item's own text, the choice among the spike's named options is
  explicitly reserved as the human-decision point this issue asks for,
  before any execution work plan's own design agreement is produced.

## Context

- Included: item-0020's full text, ADR 0016's and
  `cross-session-messaging.md`'s full text, direct empirical testing of
  this session's own actual tool surface (`mcp__scheduled-tasks__*`,
  `Monitor`, `Bash`), and `CLAUDE.md`'s own Session Entry section.
- Omitted: any actual configuration or testing of a harness `Stop` hook
  (candidate C) — deliberately not attempted in the spike, since doing so
  would itself stand up a real automation surface outside the spike's own
  investigation-only scope.
- Assumptions: the Implementation group's own tool surface is assumed
  equivalent to this Design & Review session's, per both being "standing
  sessions in the same environment" under ADR 0016 — not independently
  confirmed by testing from inside an Implementation-group session
  itself; named as an open risk in the spike's own "Open risks after
  close" section, not silently treated as confirmed.

## Links

- Spike case:
  `docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- ADR: `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  (existing, this item's decision will correct or complete its wake-up
  gap); related: `docs/collaboration/cross-session-messaging.md`

## References

- `docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`
- `docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
- `docs/collaboration/cross-session-messaging.md`
- `CLAUDE.md`, "Session Entry" section

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Spike case-0003
  closed with Selection: human-decision (no clean full-autonomy answer;
  a real but architecturally-different partial mechanism exists and was
  empirically confirmed reachable). This issue opened as the recorded
  check-in point the spike's own Next action names, before any ADR
  correction or new automation is adopted. No `.claude/settings.json` or
  scheduled task was created or modified. Awaiting Director/Backlog-thread
  response before opening the follow-up work plan and design agreement.

## Verification

- N/A — this issue records a decision checkpoint, not executable or
  testable work. Deterministic verification applies to the later
  follow-up work plan once authorized.
