# AI Work Trace

## Request

- Date: 2026-08-20
- User request: Implementer task per the Design & Review group's dispatch
  (`docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`,
  `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`) — insert the
  Director's own settled check-and-spawn / queue-continuation wake protocol
  (quoted verbatim in `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`'s
  Work Notes) into ADR 0016 and
  `docs/collaboration/cross-session-messaging.md`, replacing the previous
  vague "standing"/"autonomous" language that never specified an actual
  wake-up mechanism. LISS-0063 gives every inserted sentence verbatim; this
  attempt inserts it exactly, without paraphrase.
- Active persona: Implementer
- Covering design agreement: `DA-2026-08-20-06`
  (`docs/collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md`)
- Current phase: Architecture Path (per LISS-0063's own Metadata `Phase`
  field), though the content itself is fully specified — no design judgment
  was exercised in this attempt, only precise insertion.
- Canonical issue or work plan: LISS-0063
  (`docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`) / WP-0023
  (`docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`)
- AI planning record: not required beyond WP-0023 and LISS-0063 themselves —
  both already fully specify the plan and the exact text; no further
  planning artifact was produced by this attempt.

## Context Ledger

- Included: `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md` in
  full; `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md` in full
  (the authoritative content spec for both edits, giving every inserted
  sentence verbatim); `DA-2026-08-20-06`
  (`docs/collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md`)
  in full, especially its Boundaries and Falsification Criteria sections;
  `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`'s
  Work Notes, for background on the Director's original decision text (read
  for context only — LISS-0063 already extracted the exact insertion text
  used, so this attempt did not re-derive anything from LISS-0062 directly);
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  in full, to locate the precise insertion points (after Rule 6, before
  "Supersession, precisely"; after the Status section's existing follow-up-
  issues sentence; at the end of Enforcement) and confirm Rules 1-6 were
  otherwise untouched; `docs/collaboration/cross-session-messaging.md` in
  full, to locate direction 1's current "Message" bullet, direction 2's
  existing "Message content" bullet, and the position immediately before
  "## Handling a missing or malformed handoff"; `docs/templates/ai-work-trace.md`;
  `docs/collaboration/prompt-instruction-change-control.md`'s Traceability
  Rule and "Agent Operating Contract Files" list.
- Omitted: nothing else — this is a fully bounded, fully specified
  documentation change, per LISS-0063's own Context section ("Assumptions:
  none. Every inserted sentence above is given verbatim").
- Assumptions: none. Every inserted sentence was copied verbatim from
  LISS-0063's Acceptance Notes fenced code blocks, character for character,
  and confirmed by direct `git diff` comparison against that source text
  (see Verification below).
- Open decisions: none. The one scope question LISS-0063 flagged rather than
  resolved unilaterally (whether an existing code surface should be hooked
  into this protocol) was checked — no such surface was found in `scripts/`
  or `.claude/settings.json` during this attempt; nothing required
  expanding scope or a reopening request.

## Routing

- Model/assistant/tool: Claude Sonnet 5, via Claude Code (background
  subagent in a dedicated worktree)
- Reason: assigned Implementer task per the two-group topology (ADR 0016);
  the task is precise transcription of Director-approved, already-specified
  text into two contract files, not new design content.
- Compatibility state: N/A — no dependency, library, or version claim is
  made by this change.
- Privacy constraints: none beyond the repository's own defaults; no
  external network access was used.

## AI Execution Records

### Attempt 1

- Agent: Claude Code (background subagent)
- Environment: Claude Code CLI, worktree
  `.claude/worktrees/agent-a0833b7243ead35d1`, branch `wp-0023-execution`
  (created from local branch `process/promote-item-0020` at commit
  `954abf1`)
- Model as displayed: Claude Sonnet 5 (model ID `claude-sonnet-5`)
- Reasoning setting as displayed: N/A — not surfaced to this session
- Estimated token range: N/A — not tracked in this environment
- Estimated token midpoint: N/A
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: harness does not surface token counts to
  this session
- Estimate variance: N/A
- Variance reason: N/A
- Scope: insert ADR 0016 Rule 7, its Status-section sentence, and its two
  Enforcement bullets, verbatim per LISS-0063; insert
  `cross-session-messaging.md`'s direction-1 Message bullet replacement,
  direction-2 Wake mechanic bullet, and new "Queue continuation and
  resume-before-duplicate-spawn" section, verbatim per LISS-0063; write this
  trace; update LISS-0063's own Status and Work Notes with a self-review
  record; run `scripts/check-contract-consistency.py`; fill in
  `docs/work-plans/WP-0023-...md`'s own Preflight Validation and Review
  Summary Packet sections.
- Result: success — both contract-file edits independently confirmed
  character-for-character against LISS-0063's own fenced-code-block source
  text via direct `git diff` comparison; no existing sentence in either file
  altered or removed. See Verification below for full command output.
- Attempt boundary: single attempt, no rework.
- Notes: none.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A — single attempt, no cross-attempt token
  aggregation performed.

## Cost / Reasoning Control

- Operating path: Architecture Path (per LISS-0063's own Metadata), though
  narrowly executed as precise insertion — no design judgment was exercised.
- Files read: see Context Ledger above.
- Context intentionally omitted: see Context Ledger above.
- Deterministic checks used: `python3 scripts/check-contract-consistency.py`;
  `git diff` against LISS-0063's own quoted text; targeted `grep` for "Rule
  7" and "Queue continuation and resume-before-duplicate-spawn"; `git diff
  process/promote-item-0020...HEAD --stat` for file-scope confirmation.
- Escalation reason: none — single attempt sufficed; no ambiguity required
  escalation beyond what the design agreement already settled.
- Avoided LLM work: no generative design work performed; both edits
  transcribe already-fully-specified text from LISS-0063's own Acceptance
  Notes rather than composing or paraphrasing new prose.
- Rework caused by AI output: none.

## Preflight Validation

- Required: yes — WP-0023's own Preflight Validation section requires it
  before the work-plan-level Reviewer pass; issuing that section is this
  attempt's own responsibility per WP-0023's text, filled in as a separate
  commit after this one, per the spawning session's instructions.
- Result: see `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s
  own "Preflight Validation" section for the recorded pass/fail result.
- Checks and command output: see Verification below.
- Scope result: pass — only the two contract files, this trace, and the two
  tracking files (`docs/issues/LISS-0063-...md`,
  `docs/work-plans/WP-0023-...md`) are changed (confirmed by `git diff
  process/promote-item-0020...HEAD --stat` below).
- Next action: hand off to the work-plan-level Reviewer pass, in a separate
  context, once Preflight is recorded.
- Independent Reviewer still required: yes.

## Decisions Carried

- Director decisions from the covering design agreement: `DA-2026-08-20-06`'s
  Agreement section has both the Director box (the Director's own verbatim
  protocol text, quoted in `docs/issues/LISS-0062-...md`'s Work Notes) and
  the AI box checked; its Scope, Boundaries, and Settled Ambiguities
  sections fully determine this attempt's content, with no open question
  left to guess at.
- Reviewer decisions, with the failure scenarios searched for: none yet —
  this is the first attempt at LISS-0063, and no Reviewer pass has been
  issued on this work plan. This attempt's own self-review (recorded in
  LISS-0063's Work Notes) searches for text drift from LISS-0063's own
  verbatim specification and accidental alteration of existing sentences;
  the work-plan-level Reviewer's separate-context pass is the next required
  step, not yet performed.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  - `git diff docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
    and `git diff docs/collaboration/cross-session-messaging.md`, each
    compared line-by-line against LISS-0063's own fenced-code-block source
    text.
  - `python3 scripts/check-contract-consistency.py` — regression check.
  - `grep -n "Rule 7" docs/architecture/adr/0016-...md` and `grep -n "Queue
    continuation and resume-before-duplicate-spawn"
    docs/collaboration/cross-session-messaging.md`.
  - `git diff process/promote-item-0020...HEAD --stat` — file-scope check.
- Result: full pasted output recorded in
  `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s own
  Preflight Validation section (filled in as a separate commit after this
  one) and in the final report to the spawning session.

## Changed Files

- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  (edited — added `### Rule 7 — Check-and-spawn wake protocol` immediately
  after Rule 6 and before "Supersession, precisely"; added one Status-
  section sentence after the existing follow-up-issues sentence; added two
  Enforcement bullets at the end of the Enforcement list. Rules 1-6 and all
  other existing content unchanged).
- `docs/collaboration/cross-session-messaging.md` (edited — replaced
  direction 1's "Message" bullet; added direction 2's "Wake mechanic"
  bullet after its "Message content" bullet and before "Record"; added the
  new "Queue continuation and resume-before-duplicate-spawn (ADR 0016 Rule
  7)" section immediately before "## Handling a missing or malformed
  handoff". All other existing content unchanged).
- `docs/collaboration/traces/2026-08-20-check-and-spawn-wake-protocol.md`
  (new, this file).
- `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md` (edited —
  `Status` updated to `done`, Work Notes entry and self-review record
  appended).

**Why the change was needed**: `docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`'s
own spike (`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`)
found that ADR 0016 and `docs/collaboration/cross-session-messaging.md`
described the Design & Review and Implementation groups as "standing" and
"autonomous" without ever specifying an actual wake-up mechanism, and that
no primitive in this environment lets a fully-dormant session revive itself
unprompted. `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`'s
own settled decision (Director-approved, recorded in that issue's Work
Notes) resolves this with a check-and-spawn / queue-continuation protocol
that reassigns responsibility for waking the next layer to the event that
produces new approved work, rather than to the dormant session itself. This
change documents that protocol precisely in both contract files.

**What agent behavior is expected to change as a result**: a spawning party
(the Backlog thread spawning Design & Review; Design & Review spawning
Implementation; or any session recovering after an error) now checks, via
`ListAgents`, whether a session already exists for the target role —
including a session that has just failed or errored, whose worktree/branch
may hold undiscovered committed-but-unpushed work — before spawning a new
one, and resumes an existing/resumable session instead of duplicating it.
Additionally, a standing loop (Design & Review, Implementation) now checks
its own queue for already-approved-but-unstarted work before going idle,
proceeding directly to the next item if any exists, and goes idle only when
its queue is genuinely empty.

## Next Safe Action

- Fill in `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s own
  Preflight Validation section with the actual pasted output of all four
  required checks, and its Review Summary Packet section's Disposition,
  Remaining blockers, and Verification result fields, as a separate commit,
  then hand off to the work-plan-level Reviewer pass in a separate context.

## Notes

- No file other than the two contract files, this trace, and
  `docs/issues/LISS-0063-...md` was changed by the commit this trace
  documents (WP-0023's own Preflight Validation fields are filled in as a
  separate, later commit, per the spawning session's own instructions).
- No new script, helper, scheduled task, or `.claude/settings.json` hook was
  added or found necessary — this is a documentation-only change, per the
  design agreement's own explicit Boundaries. No existing code surface in
  `scripts/` or `.claude/settings.json` was found that should hook into
  this protocol.
- Both edits' factual claims (exact insertion text, insertion points, and
  the "no other content touched" claim) were each independently reproduced
  by direct `git diff` output in this session, not asserted from memory of
  having made the edit.
