# AI Work Trace: LISS-0022 — Define the cross-session messaging (send_message/ListAgents) handoff protocol

## Request

- Date: 2026-08-18
- User request: Design & Review group handoff (via `SendMessage`) assigning
  WP-0002's LISS-0020 through LISS-0026 to this Implementation-group session.
- Active persona: Implementer
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
  (`DA-2026-08-18-01`)
- Current phase: Architecture Path, single-phase contract-file creation
  (process-only issue; no Red/Green/Refactor)
- Canonical issue or work plan: LISS-0022;
  `docs/work-plans/WP-0002-two-group-send-message-loop.md`
- AI planning record: `AIP-0022-001` (in LISS-0022 itself; planning size `M`)

## Context Ledger

- Included: ADR 0016, the `SendMessage`/`ListAgents` tool descriptions
  available in this session, `docs/collaboration/ai-human-scheme.md`
  Invariant 1, LISS-0022's own issue text (five handoff directions, the
  trigger/content/record requirement, the "message is a trigger" rule, the
  `ListAgents`-failure requirement).
- Omitted: application-level specs (none apply; process-only change).
- Assumptions: `SendMessage` and `ListAgents` are available in this
  environment (confirmed directly — both tools are present in this
  session's own deferred/available tool list, used earlier in this same
  session to receive the handoff message this trace documents). The new
  file states this as a precondition rather than silently assuming a target
  adopting project always has them.
- Open decisions: exact message text templates are left to Implementer
  discretion per `DA-2026-08-18-01`'s Deferred Questions; this document
  states required content, not exact wording, matching that deferral.

## Routing

- Model/assistant/tool: Claude Sonnet 5 via Claude Code CLI
- Reason: process/contract document creation within an existing standing
  session
- Compatibility state: Verified — this session's own receipt of a
  `SendMessage`-delivered handoff (documented in this same session's
  transcript) is a live worked example of direction 2 in the new document
- Privacy constraints: none; public template repository, no secrets involved

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI (standing Implementation group session)
- Environment: local git worktree,
  `/Users/nn0cl/Documents/git/llm-loop-project-template/.claude/worktrees/agent-a2450968f458bbc6f`,
  branch `worktree-agent-a2450968f458bbc6f` fast-forwarded onto
  `process/two-group-send-message-loop-design`
- Model as displayed: claude-sonnet-5
- Reasoning setting as displayed: N/A (not surfaced to this session)
- Estimated token range: 3,000-7,000 (per AIP-0022-001)
- Estimated token midpoint: 4,500 (per AIP-0022-001)
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not surfaced by this harness
- Estimate variance: N/A
- Variance reason: token usage not surfaced by this harness
- Scope: new file `docs/collaboration/cross-session-messaging.md`; no code
  changes
- Result: landed
- Attempt boundary: single cohesive new-document draft
- Notes: none

### Attempt 2 (real-failure follow-up)

- Agent: Claude Code CLI (standing Implementation group session)
- Environment: same worktree/branch as Attempt 1
- Model as displayed: claude-sonnet-5
- Reasoning setting as displayed: N/A (not surfaced to this session)
- Estimated token range: N/A
- Estimated token midpoint: N/A
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not surfaced by this harness
- Estimate variance: N/A
- Variance reason: unplanned follow-up, prompted by a peer message asking
  for firsthand confirmation of a real `SendMessage`/`ListAgents` failure
  this session hit while trying to reply to its own WP-0002 handoff sender
- Scope: added "Confirmed failure mode: `ListAgents` absent, and a guessed
  reply address" subsection to `docs/collaboration/cross-session-messaging.md`
- Result: landed
- Attempt boundary: single follow-up edit, distinct from Attempt 1's
  original draft
- Notes: the facts recorded (two `to: "general-purpose"` failures, an
  absent `ListAgents` tool, one successful `to: "main"`) are this session's
  own firsthand, live tool-call results in this same conversation, not a
  relay of another session's account.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: ADR 0016, `docs/collaboration/ai-human-scheme.md`,
  LISS-0022, WP-0002, `DA-2026-08-18-01`
- Context intentionally omitted: application-level specs (none apply)
- Deterministic checks used: `python3 scripts/check-contract-consistency.py`
- Escalation reason: N/A
- Avoided LLM work: none
- Rework caused by AI output: none

## Preflight Validation

- Required: yes (work-plan-level Preflight runs once, after all seven
  issues in this batch land — not per issue)
- Result: N/A at this issue level; see WP-0002's own Preflight Validation
  section for the work-plan-level run
- Checks and command output: see this issue's own Work Notes / self-review
- Scope result: N/A at this issue level
- Next action: continue to LISS-0023
- Independent Reviewer still required: yes

## Decisions Carried

- Director decisions from the covering design agreement: the "message is a
  trigger, not a record" rule (`DA-2026-08-18-01` Boundaries: "A
  `SendMessage` payload is never itself the deterministic record of a
  decision") is stated as this document's own governing rule, in its own
  named section, cross-referencing Invariant 1 directly.
- Reviewer decisions, with the failure scenarios searched for: none yet —
  this issue awaits the work-plan-level Reviewer pass.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks: `python3 scripts/check-contract-consistency.py`;
  read-through confirming every one of the five handoff directions states
  trigger, message content, and record file(s)
- Result: `contract consistency: all checks passed` — this is the first
  point in the work-plan pass where the checker returns zero failures,
  because the two previously-expected `cross-session-messaging.md`
  reference failures (from ADR 0016) and the two added by LISS-0021's own
  forward references now resolve against this newly-created file.

## Changed Files

- `docs/collaboration/cross-session-messaging.md` (new in Attempt 1; the
  "Confirmed failure mode" subsection added in Attempt 2)

## Next Safe Action

- Commit this work-plan pass locally (no push/PR/merge), per the
  Implementation-group worktree rule LISS-0024 documents, and report the
  branch name back to the requesting session.

## Notes

- Reason for the change: ADR 0016 introduced a standing two-group topology
  connected by `SendMessage`/`ListAgents`, but named no document stating the
  concrete message contract between the groups. Without this document,
  Invariant 1 ("every decision produces a document") would be at risk of
  being satisfied only informally, by convention, rather than by a stated
  contract a later reader or agent can check a given handoff against.
- Expected agent behavior change: a Design & Review group session handing
  off a design agreement, or an Implementation group session handing off a
  Preflight pass or a Reviewer decision, now has a concrete content
  requirement to follow (trigger, message content, record file) instead of
  improvising wording per handoff; and both groups now have an explicit,
  reopening-request-worthy rule for what to do when `ListAgents` cannot find
  the expected target session, instead of silently proceeding or guessing.
