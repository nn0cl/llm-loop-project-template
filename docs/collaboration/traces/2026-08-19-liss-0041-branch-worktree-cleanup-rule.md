# AI Work Trace: LISS-0041 — self-directed branch/worktree cleanup rule

## Request

- Date: 2026-08-19
- User request: Design & Review group handoff assigning WP-0012's LISS-0040
  and LISS-0041 to this Implementation-group session.
- Active persona: Implementer
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-copy-target-refs-and-branch-cleanup.md`
  (`DA-2026-08-19-04`)
- Current phase: Architecture Path, single-phase contract-file edit
  (process-only issue; no Red/Green/Refactor)
- Canonical issue or work plan: LISS-0041;
  `docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md`
- AI planning record: `AIP-0041-001` (in LISS-0041 itself; planning size `S`)

## Context Ledger

- Included: `docs/backlog/item-0011-copy-target-references-and-branch-cleanup.md`,
  `DA-2026-08-19-04` in full, `docs/collaboration/branch-commit-pr-discipline.md`
  in full (the file changed), `docs/collaboration/prompt-instruction-change-control.md`
  in full (the Traceability Rule and Review Rule this trace and the change
  itself must satisfy), `docs/collaboration/cross-session-messaging.md` in
  full (read to judge whether a cross-reference from the new subsection
  improves the document, per the task's own instruction to read it first).
- Omitted: the full WP-0002-WP-0011 history of which specific worktrees
  existed — the backlog item's own count (11 worktrees, over a dozen
  branches) was treated as sufficient grounding for a forward-looking rule,
  per LISS-0041's own Context section.
- Assumptions: none beyond what LISS-0041's own Summary states.
- Open decisions: whether to cross-reference `cross-session-messaging.md`
  from the new subsection — resolved below under Decisions Carried.

## Routing

- Model/assistant/tool: Claude Sonnet 5 via Claude Code CLI
- Reason: contract-document edit within an existing Implementation-group
  worktree session
- Compatibility state: N/A (no dependency/version claim)
- Privacy constraints: none; public template repository, no secrets involved

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI (Implementation-group session)
- Environment: local git worktree,
  `/Users/nn0cl/Documents/git/llm-loop-project-template/.claude/worktrees/agent-a0f06d6c248b5a9ed`,
  branch `process/copy-target-refs-and-branch-cleanup`, created from the tip
  of `process/wp-0012-item-0011-copy-target-refs-branch-cleanup` (commit
  `291a414`, "docs: design agreement + work plan for item-0011 (WP-0012)").
  The worktree this session was originally spawned into was on a stale
  branch tip that predated WP-0012's own files entirely; recovered the
  correct base by inspecting `git branch -a` and `git log --oneline` on the
  branches present locally, per this repository's own Session Entry
  artifact-recovery rule.
- Model as displayed: claude-sonnet-5
- Reasoning setting as displayed: N/A (not surfaced to this session)
- Estimated token range: 6,000-14,000 (per AIP-0041-001's "low thousands"
  estimation basis, read against a single-contract-file, bounded-addition
  scope)
- Estimated token midpoint: N/A (not tracked in this environment)
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not surfaced by this harness
- Estimate variance: N/A
- Variance reason: token usage not surfaced by this harness
- Scope: extended `docs/collaboration/branch-commit-pr-discipline.md`'s
  existing "Implementation-group worktree, per work plan" subsection's
  "When removed" bullet with a new "Who removes it, and when" bullet,
  stating that the session whose content the worktree/branch held removes
  both, immediately, as its own completion step, once it confirms its
  content actually landed upstream — not deferred to a later sweep.
  Added a new subsection, "Self-directed branch and worktree cleanup at
  merge time", generalizing the same rule to any session in the two-group
  topology whose branch merges into whatever it was feeding
  (Implementation into Design & Review's branch; Design & Review's own
  working branch into the shared `process/*` branch), citing ADR 0016 for
  the topology and cross-referencing `cross-session-messaging.md` for the
  full handoff protocol. Did not change the existing merge-timing
  constraint (worktree/branch removed after merge or work-plan close,
  whichever is first; never while issues in that plan are still in
  progress) — both new additions restate it rather than altering it.
- Result: landed
- Attempt boundary: single cohesive edit to one file (plus this trace and
  the issue/work-plan status updates in separate, matching commits).
- Notes: none.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: see Context Ledger above; also
  `docs/templates/self-review.md`, `docs/templates/ai-work-trace.md`,
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`.
- Context intentionally omitted: see Context Ledger above.
- Deterministic checks used:
  `python3 scripts/check-contract-consistency.py --repo .`.
- Escalation reason: N/A (single attempt).
- Avoided LLM work: none.
- Rework caused by AI output: none.

## Preflight Validation

- Required: yes (work-plan-level, covering both LISS-0040 and LISS-0041)
- Result: N/A at this per-file trace level — see
  `docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md`'s own
  Preflight Validation section for the whole-plan result.
- Checks and command output: see Verification below.
- Scope result: N/A at this level.
- Next action: N/A at this level.
- Independent Reviewer still required: yes

## Decisions Carried

- Director decisions from the covering design agreement: placement of the
  rule (`branch-commit-pr-discipline.md`, extending the existing
  Implementation-group worktree subsection and adding a new subsection for
  the Design & Review group) settled by `DA-2026-08-19-04`'s Settled
  Ambiguities, "Where does the branch-cleanup rule go?" row — applied
  exactly as specified.
- Reviewer decisions, with the failure scenarios searched for: none yet —
  pending the work-plan-level Reviewer pass, which per LISS-0041's own
  Acceptance Notes must independently confirm the new rule against
  `prompt-instruction-change-control.md`'s Traceability Rule and Review
  Rule.
- Arbiter decisions, if any: none.
- Own judgment call (per this repository's Invariant 3, stating its own
  grounds): whether to cross-reference `cross-session-messaging.md` from
  the new subsection, left to this session's own judgment by the parent
  task. Read that file in full: it documents the `SendMessage`/`ListAgents`
  handoff protocol and the two-group topology's message-triggers, but does
  not itself discuss branch or worktree cleanup. Decision: add one
  cross-reference sentence at the end of the new subsection, pointing
  readers to it for the full handoff protocol the branch-merge
  relationship (Implementation -> Design & Review -> shared `process/*`)
  is grounded in — a single sentence, not a restatement of its content, so
  it adds a pointer rather than indirection a reader must follow to
  understand the rule itself (the rule is fully stated without needing to
  open that file).

## Verification

- Read-through against `prompt-instruction-change-control.md`'s
  Traceability Rule: this trace states which contract file changed
  (`docs/collaboration/branch-commit-pr-discipline.md`), why the change was
  needed (branches/worktrees left behind after merge across WP-0002 through
  WP-0011, per `docs/backlog/item-0011-*.md`), and what agent behavior is
  expected to change (a session removes its own merged branch/worktree
  immediately, as part of its own completion step, instead of leaving it
  for a later manual sweep).
- Commands/checks:
  ```
  $ python3 scripts/check-contract-consistency.py --repo .
  contract consistency: all checks passed
  ```
- Result: passes cleanly, including mirror parity and references — expected,
  since `branch-commit-pr-discipline.md` is referenced by, not literally
  mirrored into, `AGENTS.md`/`CLAUDE.md`/etc.
  (`FULL_MIRRORS`/`MIRRORED_SECTIONS`/`EXTRA_MIRRORED_RULES` in
  `scripts/check-contract-consistency.py` do not name this file), confirmed
  by running the check rather than assuming it, per this issue's own
  Acceptance Notes.

## Changed Files

- `docs/collaboration/branch-commit-pr-discipline.md`
- `docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md` (this file)

## Next Safe Action

- LISS-0040 and LISS-0041 both self-reviewed complete; run whole-work-plan
  Preflight Validation, then hand off to the Design & Review group's
  separate-context Reviewer pass, per direction 3 (Trigger B) in
  `docs/collaboration/cross-session-messaging.md`.

## Notes

- LISS-0040's fix to `scripts/check-contract-consistency.py` does not
  require its own trace: confirmed against
  `prompt-instruction-change-control.md`'s exact Agent Operating Contract
  Files list, which does not include `scripts/*.py`, matching
  `DA-2026-08-19-04`'s own Spike Result finding and WP-0011/LISS-0039's
  prior precedent for the same script.
