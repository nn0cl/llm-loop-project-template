# AI Work Trace

## Request

- Date: 2026-07-25
- User request: review and, on confirmation, implement an adopter-feedback
  (qpex) process-feedback finding as a new local issue (LISS-0018) in
  `llm-project-template`.
- Current phase: process/docs, Architecture Path (revises an Accepted ADR).
- Canonical issue or work plan:
  `docs/issues/LISS-0018-another-adopter-claude-md-full-mirror.md`.
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
  `docs/architecture/adr/0006-prompt-instruction-change-control.md`;
  rewrite `CLAUDE.md` as an effective-content mirror of `AGENTS.md`
  (condensed restatement, not a literal splice — see LISS-0018 Acceptance
  Note 1); add this trace.
- Result: local edits and commit completed; no pull request opened.
- Attempt boundary: single interactive session, no retries.
- Notes: scope changed twice during the session (original two-item draft
  dropped in full; a branch/PR-granularity sub-topic also dropped) before
  converging on this issue's actual scope, per user redirection rather than
  AI error. Separately, the `CLAUDE.md` draft itself was revised once within
  this attempt (an initial 231-line condensed version was replaced with the
  245-line version actually committed, after self-review found it had
  dropped concrete document filenames — see LISS-0018 Acceptance Note 1).
  See LISS-0018 Context for the final scope rationale.

### Attempt 2 (Adjudicator review pass)

- Agent: Claude Code (Claude Sonnet 5), same interactive session.
- Environment: same branch, after Attempt 1's commit.
- Scope: Adjudicator-driven correction pass on Attempt 1's output. Six
  errors found on review, three specific to the ADR text and three
  inherited into both the ADR and LISS-0018:
  1. A `PreToolUse`-hook quote was misattributed to *Automate actions with
     hooks* (hooks-guide) when both sentences are actually from *How Claude
     remembers your project* (memory page).
  2. One of those misattributed sentences ("Hooks execute as shell commands
     at fixed lifecycle events and apply regardless of what Claude
     decides to do.") does appear verbatim, but on the memory page's
     troubleshooting section, not hooks-guide — the ADR's citation pointed
     to the wrong URL.
  3. "literal full mirrors" / "literal text for CLAUDE.md,
     copilot-instructions.md, and .grok/rules/*.md" overstated actual file
     structure (compare headings across the three files — they differ) and
     directly contradicted this same change's own LISS-0018 text, which
     correctly describes the `CLAUDE.md` rewrite as "a condensed,
     Claude-native restatement... not a literal splice."
  4. "third adopter" collided with LISS-0006, which already uses "a third
     adopter round" for an unrelated project (a rhythm/music-learning
     game). Renamed throughout (including the issue filename) to "another
     adopter (qpex)".
  5. "`@import` and literal duplication load identically" overstated
     Anthropic's actual text, which says imported content still loads into
     context at launch but does not claim the two mechanisms are
     equivalent in all respects.
  6. Bullet-point phrasing made it ambiguous whether both failure modes (A:
     design-check omission, B: decision-gate skip) were repeated, when only
     A was recorded as repeated and B as a single occurrence.
- Result: all six corrected in `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  and `docs/issues/LISS-0018-another-adopter-claude-md-full-mirror.md`
  (renamed from the `...third-adopter...` filename); this trace updated to
  record the correction.
- Attempt boundary: same session, second commit.
- Notes: items 1–3 were not present in LISS-0018 itself (it already cited
  the hooks-guide permission-mode quote correctly and already described the
  `CLAUDE.md` rewrite as non-literal) — they were introduced only when
  drafting the ADR revisit section. Items 4–6 were inherited into both
  files from Attempt 1's initial drafting and required fixes in both.

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
- Rework caused by AI output: two distinct kinds, do not conflate them.
  (a) Within Attempt 1, before any external review: scope was narrowed twice
  at the user's direction (not AI error), and the `CLAUDE.md` draft was
  revised once by self-review (231→245 lines, restoring dropped filenames) —
  self-caught, not Adjudicator-triggered. (b) Attempt 2 is genuine
  Adjudicator-triggered rework: it corrected six accuracy issues in Attempt
  1's ADR/issue text (citation misattribution, an overstated "literal
  mirror" claim, an issue-numbering collision with LISS-0006, an overstated
  "load identically" claim, and an ambiguous repetition claim) — caught by
  Adjudicator review, not self-caught.

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

- `CLAUDE.md` (rewritten as an effective-content mirror of `AGENTS.md`,
  condensed restatement, `@AGENTS.md` import removed).
- `docs/architecture/adr/0006-prompt-instruction-change-control.md` (new
  2026-07-25 decision round; updated Decision/Consequences/Enforcement
  file-by-file descriptions).
- `docs/issues/LISS-0018-another-adopter-claude-md-full-mirror.md` (new).
- `docs/collaboration/traces/2026-07-25-claude-md-full-mirror.md` (this
  file, new).

## Next Safe Action

- The branch is committed locally only; the Adjudicator explicitly declined
  to push or open a PR in this session. When the Adjudicator decides to
  proceed, open a pull request from
  `process/liss-0018-claude-md-full-mirror` to `main`, left unmerged,
  requesting explicit Adjudicator review per
  `docs/collaboration/prompt-instruction-change-control.md`. Do not merge
  without that review.

## Notes

- `.grok/rules/*.md` and `.cursor/rules/*.mdc` were checked and require no
  edits for this specific change: neither previously referenced
  `@AGENTS.md` as *Claude Code's* import mechanism, so this change does not
  introduce a *new* inconsistency there. This is a narrow claim — it does
  not mean the five contract files are fully consistent with each other in
  general. Pre-existing gaps such as `.github/copilot-instructions.md` and
  `.grok/rules/*.md` lacking a dedicated "Approval Model" section (present
  in `AGENTS.md` and now in `CLAUDE.md`) were neither introduced nor
  resolved by this change and are out of scope here.
