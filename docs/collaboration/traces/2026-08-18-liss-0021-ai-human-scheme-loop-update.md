# AI Work Trace: LISS-0021 — Update the collaboration loop for backlog-gated, non-blocking, two-group execution

## Request

- Date: 2026-08-18
- User request: Design & Review group handoff (via `SendMessage`) assigning
  WP-0002's LISS-0020 through LISS-0026 to this Implementation-group session.
- Active persona: Implementer
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
  (`DA-2026-08-18-01`)
- Current phase: Architecture Path, single-phase contract-file edit
  (process-only issue; no Red/Green/Refactor)
- Canonical issue or work plan: LISS-0021;
  `docs/work-plans/WP-0002-two-group-send-message-loop.md`
- AI planning record: `AIP-0021-001` (in LISS-0021 itself; planning size `M`)

## Context Ledger

- Included: `docs/collaboration/ai-human-scheme.md`,
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
  the Director's intervention-semantics clarification recorded in
  `DA-2026-08-18-01`'s Settled Ambiguities, LISS-0021's own issue text.
- Omitted: application-level specs (none apply; process-only change).
- Assumptions: `docs/collaboration/cross-session-messaging.md` (LISS-0022's
  own target) does not yet exist at the time of this edit; this document's
  new cross-references to it are forward references, expected to resolve
  once LISS-0022 lands later in this same work-plan pass, not a defect in
  this issue's own change.
- Open decisions: none.

## Routing

- Model/assistant/tool: Claude Sonnet 5 via Claude Code CLI
- Reason: process/contract document edit within an existing standing session
- Compatibility state: N/A (no dependency/version claim)
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
- Estimated token range: 2,500-6,000 (per AIP-0021-001)
- Estimated token midpoint: 4,000 (per AIP-0021-001)
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not surfaced by this harness
- Estimate variance: N/A
- Variance reason: token usage not surfaced by this harness
- Scope: rewrote "The Loop" diagram and surrounding prose, added
  "Non-blocking concurrency across work plans" and "Intervention channel"
  subsections, updated "Human agreement (Director)" and "Decision Gates" in
  `docs/collaboration/ai-human-scheme.md`
- Result: landed
- Attempt boundary: single cohesive edit
- Notes: none

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: `docs/collaboration/ai-human-scheme.md`, ADR 0016, LISS-0021,
  WP-0002, `DA-2026-08-18-01`
- Context intentionally omitted: application-level specs (none apply)
- Deterministic checks used: `python3 scripts/check-contract-consistency.py`;
  read-through of the Reviewer three-constraints and Three Invariants
  sections to confirm they were not touched
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
- Next action: continue to LISS-0022
- Independent Reviewer still required: yes

## Decisions Carried

- Director decisions from the covering design agreement: the intervention
  channel's precise effect — gates the specific in-flight item to per-step
  approval, not a session halt, per the Director's refinement quoted
  verbatim in `DA-2026-08-18-01`'s Direction section — is restated in the
  new "Intervention channel" subsection using the same effect, not a
  paraphrase that could drift from it.
- Reviewer decisions, with the failure scenarios searched for: none yet —
  this issue awaits the work-plan-level Reviewer pass.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks: `python3 scripts/check-contract-consistency.py`;
  read-through against ADR 0016's Decision section (Rules 1-6)
- Result: consistency checker shows 4 failures, all of the same kind as the
  baseline (references to `docs/collaboration/cross-session-messaging.md`,
  not yet created) — 2 pre-existing from ADR 0016 itself, plus 2 new from
  this file's own new cross-references to the same not-yet-created file.
  No other failure category appeared. Read-through confirms every element
  of ADR 0016 Rules 2, 3, and 4 that this issue's Acceptance Notes require
  is present in the diagram or prose, and that the Reviewer's three
  constraints, the Implementer's self-review requirements, and the Three
  Invariants sections are unchanged from the pre-edit file.

## Changed Files

- `docs/collaboration/ai-human-scheme.md`

## Next Safe Action

- Proceed to LISS-0022 (`docs/collaboration/cross-session-messaging.md`,
  new file) — its landing resolves all 4 currently-expected reference
  failures above.

## Notes

- Reason for the change: ADR 0016 relocated the design-phase gate to
  backlog-item approval, introduced non-blocking concurrency across work
  plans, and introduced the Director's intervention channel.
  `ai-human-scheme.md` (an ADR 0006 contract file) is the primary loop
  description in this repository and previously showed only the
  single-session, per-work-plan-blocking model; leaving it unchanged would
  make it contradict ADR 0016 and `personas.md` (LISS-0020).
- Expected agent behavior change: an agent reading `ai-human-scheme.md` now
  sees the backlog-item gate as the loop's entry point, the two-group
  handoff points inside the loop, that more than one work plan can be
  in-flight without one blocking another, and the intervention channel's
  precise per-item (not per-group) effect.
