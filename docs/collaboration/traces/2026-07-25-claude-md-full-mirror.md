# AI Work Trace

## Request

- Date: 2026-07-25
- User request: review and, on confirmation, implement a third-adopter
  (qpex) process-feedback finding as a new local issue (LISS-0018) in
  `llm-project-template`.
- Current phase: process/docs, Architecture Path (revises an Accepted ADR).
- Canonical issue or work plan:
  `docs/issues/LISS-0018-third-adopter-claude-md-full-mirror.md`.
- AI planning record: this trace; see Cost / Reasoning Control below.

## Context Ledger

- Included: this repo's `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`,
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/definition-of-done.md`,
  `docs/collaboration/process-gap-register.md`,
  `docs/issues/LISS-0005-adopter-feedback-process-hygiene-improvements.md`
  (structural precedent), `docs/research/README.md` and
  `docs/research/2026-07-06-rationale-evidence-based-process-design.md`
  (citation/evidence discipline); two Anthropic official Claude Code
  documentation pages, fetched live 2026-07-25.
- Omitted: the qpex repository itself (not accessible from this session; the
  incident was relayed by the Adjudicator in chat and treated as a factual
  record, not independently re-verified against qpex's own trace/ADR files).
- Assumptions: the qpex incident report is accurate as relayed. Anthropic's
  fetched documentation reflects current (2026-07-25) product behavior and
  may change in future Claude Code releases.
- Open decisions: see LISS-0018's "Adjudicator Decision Points" (causal
  mechanism unconfirmed; PreToolUse-hook enforcement deferred; Claude Code's
  supported-agent status question deferred).

## Routing

- Model/assistant/tool: Claude Sonnet 5 (Claude Code), interactive session.
- Reason: process/docs Architecture Path work requiring live web verification
  (Anthropic docs) and multi-file consistency editing across the agent
  operating contract; not a candidate for a deterministic tool.
- Privacy constraints: none — no private/user data involved, only this
  repository's own documentation and public Anthropic documentation.

## AI Execution Records

### Attempt 1

- Agent: Claude Code (Claude Sonnet 5), interactive session, plan mode then
  execution.
- Environment: local clone of `llm-project-template`, branch
  `process/liss-0018-claude-md-full-mirror`.
- Model as displayed: Claude Sonnet 5.
- Reasoning setting as displayed: not applicable (interactive, no explicit
  reasoning-effort control surfaced to the trace).
- Estimated token range: not tracked.
- Estimated token midpoint: not tracked.
- Actual tokens: not available in this environment.
- Token metric: not applicable.
- Token source: not applicable.
- Token attribution boundary: not applicable.
- Actual token unavailable reason: interactive CLI session without a
  token-usage export in scope for this task.
- Estimate variance: not applicable.
- Variance reason: not applicable.
- Scope: draft and revise `docs/issues/LISS-0018-*.md`; revise
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`; rewrite
  `CLAUDE.md` as a full mirror; add this trace.
- Result: completed, pending Adjudicator PR review.
- Attempt boundary: single interactive session, no retries.
- Notes: scope changed twice during the session (original two-item draft
  dropped in full; a branch/PR-granularity sub-topic also dropped) before
  converging on this issue's actual scope. See LISS-0018 Context for the
  final scope rationale.

## Optional Reference Total

- Value: not tracked.
- Metric: not applicable.
- Source: not applicable.
- Compatibility statement: not applicable.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: see Context Ledger above.
- Context intentionally omitted: qpex repository contents (not accessible;
  see Assumptions).
- Deterministic checks used: `wc -l` for CLAUDE.md/AGENTS.md/copilot-instructions.md
  line counts; `git log`/`git show` history checks (during earlier,
  since-dropped scope) to verify LISS-0005 precedent.
- Escalation reason: Architecture Path work revising an Accepted ADR requires
  full design-check-level rigor, not Fast Path.
- Avoided LLM work: none applicable — this is inherently a
  judgment/synthesis task (reconciling contradictory documentation, honest
  evidence weighing).
- Rework caused by AI output: none yet; this is the first attempt.

## Adjudicator Decisions

- Confirmed scope should drop the original two-item draft (branch/PR
  granularity, cross-reference-register sync) entirely; current
  ISSUE-unit-PR practice is not a problem.
- Confirmed the real topic is the `@AGENTS.md` import / behavioral-adherence
  finding from qpex.
- Confirmed proceeding with the qpex-style full-mirror fix now, without
  first resolving the causal-mechanism uncertainty or building
  `PreToolUse`-hook enforcement; both deferred to LISS-0018's Adjudicator
  Decision Points.
- Confirmed proposal + implementation land in the same PR, left unmerged for
  explicit Adjudicator review before merge.

## Verification

- Commands/checks: `wc -l CLAUDE.md AGENTS.md .github/copilot-instructions.md`
  (245 / 179 / 173 lines); manual read-through of the rewritten `CLAUDE.md`
  against the prior `CLAUDE.md` and `AGENTS.md` to confirm no rule was
  silently dropped, only reorganized/de-duplicated (the old `CLAUDE.md`'s
  "Claude Code Reading Sequence" and "Implementation Entry Point" sections
  were near-duplicates of each other and of `AGENTS.md`'s "Expected
  Workflow," and are merged into one section in the rewrite). An initial
  231-line draft collapsed the itemized collaboration/architecture document
  list into prose; that was reverted after review because it dropped
  concrete filenames, landing at 245 lines.
- Result: CLAUDE.md line count (245) exceeds Anthropic's documented ~200-line
  adherence guidance; recorded as a deliberate, noted trade-off in LISS-0018
  (fidelity over brevity) rather than force-trimmed to hit the number. CI
  docs/markdown lint not yet run in this trace — expected to run in the PR.

## Changed Files

- `CLAUDE.md` (rewritten as full mirror, `@AGENTS.md` import removed).
- `docs/architecture/adr/0006-prompt-instruction-change-control.md` (new
  2026-07-25 decision round; updated Decision/Consequences/Enforcement
  file-by-file descriptions).
- `docs/issues/LISS-0018-third-adopter-claude-md-full-mirror.md` (new).
- `docs/collaboration/traces/2026-07-25-claude-md-full-mirror.md` (this
  file, new).

## Next Safe Action

- Open a pull request from `process/liss-0018-claude-md-full-mirror` to
  `main`, left unmerged, requesting explicit Adjudicator review per
  `docs/collaboration/prompt-instruction-change-control.md`. Do not merge
  without that review.

## Notes

- `.grok/rules/*.md` and `.cursor/rules/*.mdc` were checked for relevant
  mirrored content and require no edits: neither previously referenced
  `@AGENTS.md` for Claude Code's mechanism, so this change does not
  introduce new inconsistency there.
