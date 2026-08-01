# AI Work Trace

## Request

- Date: 2026-08-02
- User request: remove the references to `docs/research/`, and tidy dangling
  references generally.
- Active persona: Specifier, executing the plan agreed with the Director.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-dangling-reference-cleanup.md`
  (DA-2026-08-02-02), which settles Deferred Question 1 of DA-2026-08-02-01.
- Current phase: Architecture Path.
- Canonical issue or work plan: none; direct Director instruction.
- AI planning record: the Plan table in that agreement.

## Context Ledger

- Included: `docs/architecture/adr/0003`, `0006`, `0008`, `0012`, `0013`,
  `docs/architecture/README.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/agreements/2026-08-02-post-rewrite-doc-consistency.md`,
  `docs/templates/examples/rust-agent-instructions.md`,
  `frontend-agent-instructions.md`, and the output of a repository-wide link
  and anchor audit over every `.md`, `.mdc`, `.sh`, `.yml`, and `.py` file.
- Omitted: the bodies of historical records under
  `docs/collaboration/traces/`, `docs/collaboration/reviews/`,
  `docs/issues/`, and `docs/work-plans/` — enumerated by the audit, read only
  where a hit needed classifying, and not edited.
- Assumptions:
  - "Remove the references" applies to documents read as current guidance, not
    to dated records. A record of a deletion that cannot name what was deleted
    stops being a record.
  - ADR 0012's replacement note should not reintroduce the path, since the
    instruction was to remove references to it.
- Open decisions: the two rows in the agreement's Deferred Questions — whether
  the audit becomes a CI check, and whether ADR 0006's body is revised.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; deterministic checks via
  two purpose-written Python checkers, `grep`, `bash -n`, and local runs of the
  CI repository-sanity steps.
- Reason: the audit is mechanical and was done mechanically. The reasoning was
  spent on classifying each hit as a defect, a false positive, or a record.
- Privacy constraints: none; repository-local documentation only.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone of `llm-loop-project-template`, branch
  `docs/dangling-reference-cleanup`, based on `main` at commit `81b32dd`
- Model as displayed: Claude Opus 5
- Reasoning setting as displayed: default
- Estimated token range: not recorded
- Estimated token midpoint: not recorded
- Actual tokens: unavailable
- Token metric: unavailable
- Token source: unavailable
- Token attribution boundary: unavailable
- Actual token unavailable reason: the harness does not surface per-session
  token counts to the agent.
- Estimate variance: not applicable
- Variance reason: not applicable
- Scope: ADR 0003 and 0012 status and references; the ADR index in
  `docs/architecture/README.md`; two current documents describing a dropped
  mechanism; the Reopening Log of DA-2026-08-02-01.
- Result: complete. All four plan rows satisfied.
- Attempt boundary: single continuous session.
- Notes: the audit found more than the requested reference. Two current
  documents still described `CLAUDE.md` as using the `@AGENTS.md` import,
  dropped on 2026-07-25 — a dangling reference with no broken path, invisible
  to any link check. ADR 0003 and ADR 0012 both read as `Accepted` with
  nothing saying ADR 0013 had superseded them, and the ADR index stopped at
  0011.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: as listed in the Context Ledger. Historical records were
  enumerated by the checkers rather than read.
- Context intentionally omitted: historical record bodies.
- Deterministic checks used: as recorded under Verification below.
- Escalation reason: the change touches `docs/collaboration/*.md` and accepted
  ADRs, which is Architecture Path by
  `docs/collaboration/prompt-instruction-change-control.md`.
- Avoided LLM work: the audit was two short scripts run over the tree, not a
  document-by-document reading. The scripts are scratch tooling and are not
  added to the repository — see the agreement's Deferred Questions.
- Rework caused by AI output: the first version of ADR 0012's replacement note
  named the deleted path while explaining its absence, which the checker
  correctly flagged as a dangling reference and which read against the
  instruction. Rewritten to describe the directory without naming it.

## Decisions Carried

- Director decisions from the covering design agreement: remove the
  `docs/research/` references; tidy dangling references generally.
- Planner decisions inside that scope: current documents lose the reference
  while dated records keep it; ADR bodies are not rewritten, only Status and
  References; the `docs/templates/examples/` paths are false positives.
- Reviewer decisions, with the failure scenarios searched for: none. This
  change has not been reviewed by a separate context.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  - A link checker resolving every markdown link and backticked path in every
    `.md`, `.mdc`, `.sh`, `.yml`, and `.py` file against the working tree,
    both repo-root-relative and file-relative.
  - An anchor checker resolving every `#fragment` against the target
    document's headings.
  - `grep` for `docs/research`, `@AGENTS.md`, and `Referee`, filtered to
    exclude historical records.
  - Existence check over the CI `required_files` list; ADR existence check
    `0001`-`0013`; `bash -n` on all four scripts; conflict-marker scan; local
    run of the template-copy smoke test.
  - Column-width check over added ASCII lines.
- Result:
  - Link audit before: 7 hits — 1 real defect (ADR 0012), 1 record mention,
    5 false positives. After: 3 hits, all in agreement records that quote the
    instruction or the settled question; 0 defects. The 5 false positives are
    `../docs/architecture/*.md` paths inside
    `docs/templates/examples/*-agent-instructions.md`, which are example
    content for placement inside a target project and resolve there, not here.
  - Anchor audit: 0 dangling anchors, before and after.
  - `@AGENTS.md` as a current claim: 2 occurrences before, 0 after.
  - `required_files`: 63 entries, 0 missing. ADRs 0001-0013: present.
    `bash -n`: OK. Conflict markers: none. Smoke test: passed, including the
    `reviews/` and `agreements/` assertions.
  - Width check: no added ASCII line over 80 columns.
- Not verified: CI itself, which requires GitHub Actions. Its steps were
  reproduced locally.

## Changed Files

- Added:
  `docs/collaboration/agreements/2026-08-02-dangling-reference-cleanup.md`,
  this trace.
- Updated: `docs/architecture/adr/0003-ai-human-collaboration-governance.md`,
  `docs/architecture/adr/0012-rename-referee-to-adjudicator.md`,
  `docs/architecture/README.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/collaboration/adoption-guide.md`,
  `docs/collaboration/agreements/2026-08-02-post-rewrite-doc-consistency.md`
  (Reopening Log entry only).

## Next Safe Action

Decide whether the link and anchor audit becomes a CI step. Run by hand it
found a defect that had survived two prior verification passes; run never, it
will miss the next one. The cost is a script added to what every adopting
project receives, which is a Director decision about the distribution.

Three consecutive contract changes now stand unreviewed by a separate context.

## Notes

The requested reference was one line. The audit that found it also found a
class the previous passes could not have caught by construction: a statement
that is factually stale while every path in it resolves. `grep` for a deleted
name finds the first kind and never the second. What found the second was
reading a current document and asking whether the mechanism it describes still
exists.
