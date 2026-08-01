# AI Work Trace

## Request

- Date: 2026-08-02
- User request: Rewrite the operating contract documents to remove the human
  from every execution loop; have AI perform its own review and approval under
  task-appropriate personas; keep human involvement to initial direction,
  dialogic detailed planning, and a mandatory documented design agreement
  closing the design phase; stop fine-grained human approval; preserve the
  invariants that every decision is documented, every executed fact leaves
  evidence, and every claim states its grounds.
- Active persona: Planner and Specifier (design phase, in dialogue with the
  Director). This change defines the contract; it is not loop execution.
- Covering design agreement: none — this change *creates* the design agreement
  mechanism. The Director's instruction in session is the authority, and ADR
  0013 is its record.
- Current phase: Architecture Path.
- Canonical issue or work plan: none; direct Director instruction.
- AI planning record: not applicable.

## Context Ledger

- Included: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md`, `.cursor/rules/*.mdc`, `docs/collaboration/*.md`,
  `docs/architecture/*.md`, `docs/architecture/adr/0003`, `docs/at-tdd/*.md`,
  `docs/templates/*.md`, `docs/templates/examples/*.md`,
  `.github/workflows/ci.yml`, `.github/pull_request_template.md`,
  `scripts/*.sh`, `scripts/lib/*.sh`, `README.md`, `README.ja.md`,
  `QUICKSTART.md`, `QUICKSTART.ja.md`.
- Omitted: `docs/collaboration/traces/*` and `docs/collaboration/reviews/*`
  (historical records of work actually performed under the superseded model —
  rewriting them would falsify the record); `docs/issues/LISS-*` (same);
  ADRs 0001-0012 (superseded where applicable by 0013, not edited).
- Assumptions:
  - "Persona" means a scoped operating role with admissible inputs and required
    outputs, not a stylistic voice. Recorded in
    `docs/collaboration/personas.md`.
  - The bounded execution-batch mechanism existed only to reduce human approval
    overhead. With no human approval inside the loop it has no remaining
    function, so it was retired rather than adapted.
  - Contract-file changes remain a design-phase decision requiring the
    Director, because changing the contract changes the rules the experiment
    runs under. This is not a reintroduced deliverable gate.
- Open decisions:
  - Whether the Reviewer must run on a different model from the Implementer.
    Currently recommended, not required (Director's selection).
  - `docs/collaboration/adoption-guide.md:158` still names an Adjudicator
    approval dated 2026-07-16. Left as a historical fact about LISS-0015.
  - `docs/architecture/adr/0012` links a `docs/research/` file that no longer
    exists after the Director's deletion request. Left unedited as an accepted
    ADR; flagged to the Director.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; deterministic checks via
  `bash -n`, `python3`, `grep`, and a local run of the CI copy smoke test.
- Reason: contract-wide semantic rewrite across 40+ interdependent documents;
  mechanical replacement alone would have produced incoherent gates.
- Privacy constraints: none; repository-local documentation only.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone of `llm-loop-project-template`, branch
  `process/director-model-contract-rewrite`
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
- Scope: ADR 0013; new persona and design-agreement documents; full rewrite of
  `ai-human-scheme.md`; the nine agent operating contract files; the normative
  collaboration, architecture, and at-tdd documents; templates; scripts; CI;
  both READMEs.
- Result: complete. No `Adjudicator` reference remains in any normative
  document; the one remaining occurrence is a dated historical fact.
- Attempt boundary: single continuous session.
- Notes: `docs/research/` (24 files) was deleted on Director instruction during
  this session; three dangling references were found and two were repaired.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: the contract set, the normative document set, CI, scripts, and
  both READMEs. Historical record directories were listed but not read in full.
- Context intentionally omitted: trace, review, and issue history under
  `docs/collaboration/traces/`, `docs/collaboration/reviews/`, `docs/issues/`.
- Deterministic checks used: `bash -n` on all four shell scripts; a Python
  existence check over the CI `required_files` list; a local execution of the
  CI template-copy smoke test including the exclusion and placeholder
  assertions; repository-wide `grep` for residual `Adjudicator` references and
  for dangling `docs/research` links.
- Escalation reason: the change alters the governing collaboration model, which
  is Architecture Path by definition.
- Avoided LLM work: mechanical replacements were applied with `perl`/`sed`
  rather than regenerating whole files, and were verified by `grep` afterwards.
- Rework caused by AI output: line-wrap damage from two multi-line
  substitutions, and one ADR filename that pushed reference lines past the
  80-column convention. Both were detected by a width check and repaired.

## Decisions Carried

- Director decisions from the covering design agreement: human role renamed to
  `Director`; personas defined as a fixed core set plus a documented extension
  rule; AI approval constrained by context separation, a deterministic
  precondition, and a falsification burden; the whole normative document set
  rewritten in one pass; `docs/research/` deleted; no commits made.
- Reviewer decisions, with the failure scenarios searched for: none. This
  change has not been reviewed by a separate context. It was produced under the
  model it defines and has not yet been subjected to it.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  - `bash -n scripts/copy-ai-collaboration-files.sh
    scripts/update-ai-collaboration-files.sh scripts/init-llm-context.sh
    scripts/lib/collaboration-template-paths.sh`
  - Python existence check over the 62 entries in the CI `required_files` list.
  - Local run of the CI template-copy smoke test into a temporary repository,
    asserting required files present, excluded paths absent, retired files
    absent, and placeholders filled.
  - `grep -rn 'Adjudicator'` across all normative documents, contracts,
    templates, scripts, CI, and READMEs.
  - `grep -rIn 'docs/research'` for dangling references after deletion.
- Result:
  - `bash -n`: OK, all four scripts.
  - `required_files`: 62 entries, 0 missing.
  - Smoke test: all assertions passed, including
    `docs/collaboration/agreements/.gitkeep` present,
    `docs/templates/design-agreement.md` and `review-record.md` present,
    agreement/review/trace/LISS files excluded from the copy, retired
    `adjudicator-review.md`, `execution-batch-review.md`, and
    `check-execution-batch-reviews.py` absent, and placeholders filled.
  - Residual `Adjudicator` references: 1, at
    `docs/collaboration/adoption-guide.md:158`, a dated historical fact about
    LISS-0015 and intentionally preserved.
  - Dangling `docs/research` references: 3 found, 2 repaired in
    `QUICKSTART.md` and `QUICKSTART.ja.md`, 1 left in accepted ADR 0012.
- Not verified: CI itself was not executed — the workflow requires GitHub
  Actions. Only its individual steps were reproduced locally. No commit or push
  was made, per Director instruction.

## Changed Files

- Added: `docs/architecture/adr/0013-director-centered-planning-and-closed-loop.md`,
  `docs/collaboration/personas.md`, `docs/collaboration/design-agreement.md`,
  `docs/collaboration/agreements/.gitkeep`,
  `docs/templates/design-agreement.md`, `docs/templates/review-record.md`.
- Removed: `docs/templates/adjudicator-review.md`,
  `docs/templates/execution-batch-review.md`,
  `scripts/check-execution-batch-reviews.py`, `docs/research/` (24 files).
- Rewritten: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md` (3), `.cursor/rules/*.mdc` (3),
  `docs/collaboration/ai-human-scheme.md`.
- Updated: the remaining normative documents under `docs/collaboration/`,
  `docs/architecture/`, `docs/at-tdd/`, `docs/templates/`,
  `.github/workflows/ci.yml`, `.github/pull_request_template.md`,
  `scripts/init-llm-context.sh`, `scripts/update-ai-collaboration-files.sh`,
  `scripts/lib/collaboration-template-paths.sh`, `README.md`, `README.ja.md`,
  `QUICKSTART.md`, `QUICKSTART.ja.md`.

## Next Safe Action

Have a Reviewer persona, in a separate context, review this change against the
contract it introduces — the first real exercise of the model. Then reach a
design agreement with the Director for the first execution task, using
`docs/templates/design-agreement.md`, and record it under
`docs/collaboration/agreements/`.

## Notes

This change was produced by the design-phase personas and has not been reviewed
by a separate context. Under the contract it introduces, that means it is not
approved — only agreed in direction. The gap is recorded here rather than
papered over, since the first thing a closed loop must be able to do is notice
that its own founding change skipped the gate it defines.
