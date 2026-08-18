# AI Work Trace: LISS-0032 — `definition-of-done.md` hook/coverage criteria

## Request

- Date: 2026-08-18
- User request: Design & Review group handoff assigning WP-0006's LISS-0032
  and LISS-0033 to this Implementation-group session.
- Active persona: Implementer
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- Current phase: Architecture Path, single-phase contract-file edit
  (process-only issue; no Red/Green/Refactor)
- Canonical issue or work plan: LISS-0032;
  `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`
- AI planning record: `AIP-0032-001` (in LISS-0032 itself; planning size `M`)

## Context Ledger

- Included: `DA-2026-08-18-05`, `docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md`
  (this issue's own new ADR), the prior text of `definition-of-done.md`.
- Omitted: application-level specs (none apply; process-only change);
  `docs/collaboration/design-review-perspectives.md` (LISS-0033's own
  deliverable, not yet written when this file was edited).
- Assumptions: none beyond the design agreement's own settled points.
- Open decisions: none.

## Routing

- Model/assistant/tool: Claude Sonnet 5 via Claude Code CLI
- Reason: process/contract document edit within an existing standing session
- Compatibility state: N/A (no dependency/version claim)
- Privacy constraints: none; public template repository, no secrets involved

## AI Execution Records

### Attempt 1

- Agent: Claude Code CLI (Implementation-group session)
- Environment: local git worktree,
  `/Users/nn0cl/Documents/git/llm-loop-project-template/.claude/worktrees/agent-af7587091e1cec4ac`,
  branch `process/quality-gate-hooks-and-coverage-policy`, created from
  commit `57af72e`.
- Model as displayed: claude-sonnet-5
- Reasoning setting as displayed: N/A (not surfaced to this session)
- Estimated token range: 8,000-18,000 (per AIP-0032-001, covering the ADR
  plus all four LISS-0032 file edits together)
- Estimated token midpoint: 12,000
- Actual tokens: N/A
- Token metric: N/A
- Token source: N/A
- Token attribution boundary: N/A
- Actual token unavailable reason: not surfaced by this harness
- Estimate variance: N/A
- Variance reason: token usage not surfaced by this harness
- Scope: added a hook-wiring qualification to Universal Done's
  "deterministic verification was run" criterion (a wired, commit-blocking
  hook is what "run" means once ADR 0018 applies, not a manually-run
  equivalent); added a branch/route coverage anti-gaming criterion to
  Phase 2 Done; added a hook-wiring qualification and a coverage-preserved
  criterion to Phase 3 Done. No existing criterion's wording was removed or
  weakened — all changes are additive bullets or additive clauses appended
  to an existing bullet.
- Result: landed
- Attempt boundary: single cohesive edit, alongside the ADR and the three
  non-contract-file edits (`tooling.md`, `testing-strategy.md`,
  `emit-tooling-setup-prompt.sh`) in the same LISS-0032 commit set.
- Notes: this file is an ADR-0006 contract file
  (`docs/collaboration/*.md`, not a record directory), so this trace is
  required per `docs/collaboration/prompt-instruction-change-control.md`.

## Optional Reference Total

- Value: N/A
- Metric: N/A
- Source: N/A
- Compatibility statement: N/A

## Cost / Reasoning Control

- Operating path: Architecture Path
- Files read: `CLAUDE.md`, `docs/architecture/agent-quickstart.md`,
  `DA-2026-08-18-05`, `docs/work-plans/WP-0006-*.md`, LISS-0032, LISS-0033,
  `docs/architecture/tooling.md`, `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`, `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/source-code-quality.md`, a representative sample of
  `docs/collaboration/reviews/*.md`, `docs/templates/adr.md`,
  `docs/templates/self-review.md`, `docs/templates/ai-work-trace.md`,
  `docs/collaboration/prompt-instruction-change-control.md`, ADR 0006, ADR
  0008, ADR 0016, `docs/architecture/agent-quickstart.md`.
- Context intentionally omitted: full text of every `docs/collaboration/reviews/*.md`
  file beyond the ones named as the representative sample; other
  in-progress branches' uncommitted work.
- Deterministic checks used: `python3 scripts/check-contract-consistency.py --repo .`;
  `bash scripts/init-loop-settings.sh --prompt-only`.
- Escalation reason: N/A (single attempt).
- Avoided LLM work: none; all four LISS-0032 files plus the ADR required
  direct, careful editing to stay consistent with the ADR's exact wording
  rather than being safely delegable.
- Rework caused by AI output: one self-inflicted defect, caught and fixed
  before commit — unescaped backticks inside
  `scripts/lib/emit-tooling-setup-prompt.sh`'s heredoc (delimiter `PROMPT`,
  unquoted) caused the shell to attempt command substitution on the new
  table's backtick-quoted paths when `init-loop-settings.sh --prompt-only`
  was run, producing "command not found" noise and a mangled table in the
  emitted prompt. Fixed by removing the inline backticks from the new
  table cells (matching the existing convention elsewhere in this same
  heredoc, e.g. `\`docs/architecture/tooling.md\`` uses an escaped
  backtick, never a bare one) and re-verifying the prompt output cleanly.

## Preflight Validation

- Required: yes (work-plan-level, covering both LISS-0032 and LISS-0033;
  see `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`)
- Result: N/A at this per-file trace level — see the work plan's own
  Preflight Validation section for the whole-plan result.
- Checks and command output: see Verification below for this file's own
  contribution.
- Scope result: N/A at this level.
- Next action: N/A at this level.
- Independent Reviewer still required: yes

## Decisions Carried

- Director decisions from the covering design agreement: numeric-floor
  non-decision and no-retroactive-`scripts/`-application decision, both
  applied to `definition-of-done.md`'s new criteria exactly as reasoned in
  `DA-2026-08-18-05`'s Settled Ambiguities (no floor number appears in any
  Done criterion; no criterion requires `scripts/` coverage work).
- Reviewer decisions, with the failure scenarios searched for: none yet —
  pending the work-plan-level Reviewer pass (Task 10).
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  ```
  $ python3 scripts/check-contract-consistency.py --repo .
  references:
    docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:50 names 'docs/collaboration/design-review-perspectives.md', which does not exist
  contract consistency: 1 failure(s)
  ```
  (Expected at this point in the work plan: LISS-0033's own deliverable,
  `docs/collaboration/design-review-perspectives.md`, is created later in
  the same work plan and this reference resolves once it lands — see the
  work plan's own final Preflight Validation section for the whole-tree
  passing result.)
- Result: `definition-of-done.md`'s own edit introduces no new failures
  beyond the expected, already-known pending reference above (confirmed by
  running the checker immediately after this file's edit, before
  LISS-0033's file existed).

## Changed Files

- `docs/collaboration/definition-of-done.md`

## Next Safe Action

- Continue LISS-0032 with the remaining non-contract-file edits
  (`tooling.md`, `testing-strategy.md`, `emit-tooling-setup-prompt.sh`),
  then LISS-0032 self-review, then LISS-0033.

## Notes

- This trace covers `definition-of-done.md` only. `CLAUDE.md` and the new
  `docs/collaboration/design-review-perspectives.md` (both also ADR-0006
  contract files, touched under LISS-0033) are covered by a separate trace,
  `docs/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md`.
