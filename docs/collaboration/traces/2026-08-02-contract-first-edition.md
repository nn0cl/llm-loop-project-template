# AI Work Trace

## Request

- Date: 2026-08-02
- User request: tidy the operating contract, in order to make this state the
  first edition. Depth selected by the Director: renumber the ADRs into a
  fresh first-edition set, on top of the consistency and archaeology work.
- Active persona: Specifier, executing the agreed plan.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-02-contract-first-edition.md`
  (DA-2026-08-02-03).
- Current phase: Architecture Path.
- Canonical issue or work plan: none; direct Director instruction.
- AI planning record: the Plan table in that agreement.

## Context Ledger

- Included: the nine agent operating contract files; the ADR set;
  `docs/architecture/README.md`; `docs/collaboration/adoption-guide.md`,
  `ai-human-scheme.md`, `personas.md`,
  `prompt-instruction-change-control.md`; both READMEs; both QUICKSTART
  files; `.github/workflows/ci.yml`; the copy and update scripts.
- Omitted: `docs/templates/examples/` bodies beyond their reference lines;
  `docs/collaboration/` documents no rule in this change touches.
- Assumptions:
  - The governing decision should be `0001` in a first edition, so a reader
    meets the rule that governs the rest before the rest.
  - A superseded ADR is deleted rather than kept with a status banner. Kept,
    it is one careless read away from being followed.
- Open decisions: the two rows in the agreement's Deferred Questions.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; deterministic checks via
  Python link/anchor checkers, `grep`, `bash -n`, and local runs of the CI
  repository-sanity steps.
- Reason: renumbering is mechanical but its blast radius is every document
  that cites an ADR; the judgment was in what to retire and what to preserve
  as grounds.
- Privacy constraints: none; repository-local documentation only.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone of `llm-loop-project-template`, branch
  `process/contract-first-edition`, based on `main` at commit `a650f63`
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
- Scope: ADR renumbering and retirement; archaeology removal; contract-file
  parity; edition declaration.
- Result: complete. All four plan rows satisfied.
- Attempt boundary: single continuous session.
- Notes: the renumbering landed so that only three ADRs changed number
  (`0013→0001`, `0001→0002`, `0002→0003`); `0004`–`0011` kept theirs. That was
  a property of the chosen order, not a plan, and it cut the reference churn
  to a fraction of what a full reshuffle would have caused.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: the contract set, the ADR set, the entry documents, CI, and the
  scripts.
- Context intentionally omitted: as listed in the Context Ledger.
- Deterministic checks used: as recorded under Verification.
- Escalation reason: contract-file and ADR changes are Architecture Path by
  `docs/collaboration/prompt-instruction-change-control.md`.
- Avoided LLM work: the renumbering and the archaeology removal were applied as
  asserted string substitutions in a script — every replacement fails loudly if
  its target text is absent — rather than by regenerating documents. Only ADR
  0006 was rewritten as prose, because its layered narrative could not be
  fixed by substitution.
- Rework caused by AI output: six added lines exceeded the 80-column
  convention, three of them created by rewrapping earlier fixes. Found by a
  width check over added lines and repaired; two required rewrapping the whole
  paragraph rather than the line.

## Decisions Carried

- Director decisions from the covering design agreement: tidy to the deepest of
  the four offered scopes — renumber the ADRs, and declare a version.
- Planner decisions inside that scope: `0001` for the governing decision;
  deletion rather than status-marking for retired ADRs; `v1.0.0` despite
  existing `v0.x` tags.
- Reviewer decisions, with the failure scenarios searched for: none. This
  change has not been reviewed by a separate context.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  - Filename/title agreement across all eleven ADRs.
  - `grep` for `ADR 0012`, `ADR 0013`, `adr/0012`, `adr/0013`, and the
    `0001-0013` ranges.
  - `grep` for `LISS-`, `Adjudicator`, `Referee`, excluding the `LISS-0000`
    and `LISS-NNNN` ID formats.
  - A parity matrix over the nine contract files, checking each for the
    project-name placeholder, stack placeholder, review-record reference,
    personas reference, reopening rule, and phase rules.
  - Link and anchor audits over every `.md`, `.mdc`, `.sh`, `.yml`, `.py`.
  - CI `required_files` existence check; ADR existence loop `0001`-`0011`;
    `bash -n`; conflict-marker scan; copy smoke test.
  - Column-width check over added ASCII lines.
- Result:
  - ADR filenames and titles: all eleven agree.
  - Stale ADR references: 0.
  - `LISS-`/`Adjudicator`/`Referee` outside the ID format: 0.
  - Parity matrix: three real gaps found and closed — `AGENTS.md` had no
    project-name or stack placeholder at all, no phase rules, and no reopening
    section; `.github/copilot-instructions.md` named none of the record
    templates.
  - Link audit: 5 hits, all pre-existing false positives in
    `docs/templates/examples/`; 0 defects. Anchor audit: 0.
  - `required_files`: 63 entries, 0 missing. ADR loop: passes. `bash -n`: OK.
    Conflict markers: none.
  - Copy smoke test: passed; the target's `AGENTS.md` read
    `The project is **Smoke App: template smoke test**` and the version marker
    carried source, ref, and edition.
  - Width check: 6 violations found, all repaired.
- Not verified: CI itself, which requires GitHub Actions. Its steps were
  reproduced locally.

## Changed Files

- Renamed: three ADRs (`0013→0001`, `0001→0002`, `0002→0003`).
- Removed: the superseded governance ADR and the role-rename ADR.
- Added: `CHANGELOG.md`, the covering design agreement, this trace.
- Updated: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/01-quickstart.md`, `.cursor/rules/01-quickstart.mdc`,
  `README.md`, `README.ja.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`,
  `docs/architecture/README.md`, ADRs 0004, 0005, 0006, 0008, 0010, 0011,
  `docs/collaboration/adoption-guide.md`, `ai-human-scheme.md`,
  `personas.md`, `prompt-instruction-change-control.md`,
  `.github/workflows/ci.yml`, `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh`.

## Next Safe Action

Tag `v1.0.0` on the merge commit, so the edition the documents claim is the
edition git can hand out and the version marker can name.

Then have a Reviewer persona, in a separate context, review this edition
against the contract it freezes. Five consecutive contract changes now stand
unreviewed.

## Notes

This is the first record written under the reset repository, and it exists
because the contract requires one — the reset cleared accumulated history, it
did not suspend the rule that new work leaves evidence. It is excluded from
what adopting projects receive, like every record here.

The parity matrix is worth keeping as a habit. It found that `AGENTS.md` —
the file Codex, Cursor, and Grok all read natively, the most widely loaded
contract in the set — never told an adopting project what its own product was.
Every other contract file did. Nothing was broken, nothing was stale, and no
link pointed anywhere wrong; the file simply lacked a sentence, and only
comparing the files against each other made the absence visible.
