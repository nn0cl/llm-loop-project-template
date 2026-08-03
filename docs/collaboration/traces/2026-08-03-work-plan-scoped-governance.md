# AI Work Trace

## Request

- Date: 2026-08-03
- User request: change the execution-loop governance so that within an
  ISSUE's Red/Green/Refactor, review and approval happen in self-context;
  work-plan review and resolution happen AI-to-AI, in a separate context;
  the post-work-plan-completion review and the decision to proceed to the
  next work plan are one combined human action; fixes remain AI work. Reached
  through several turns of dialogue, confirmed with "はい。進めて".
- Active persona: Specifier, then Implementer, executing the agreed model.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (DA-2026-08-03-01).
- Current phase: Architecture Path.
- Canonical issue or work plan: none; direct Director instruction, recorded
  as the agreement above.
- AI planning record: the Plan table in that agreement.

## Context Ledger

- Included: `docs/architecture/adr/0001`, `0006`, `0012`, `0013`; the nine
  agent operating contract files; `docs/collaboration/ai-human-scheme.md`,
  `personas.md`, `design-agreement.md`, `definition-of-done.md`,
  `local-issue-planning.md`, `branch-commit-pr-discipline.md`,
  `model-tool-capability-matrix.md`, `project-start-guide.md`,
  `template-benefits.md`; `docs/at-tdd/process.md`;
  `docs/architecture/agent-quickstart.md`, `implementation-readiness.md`,
  `ai-request-routing.md`, `README.md`; `docs/templates/work-plan.md`,
  `examples/adoption-prompts.md`; both project READMEs and QUICKSTART files;
  `.github/workflows/ci.yml`, `pull_request_template.md`;
  `scripts/check-contract-consistency.py`.
- Omitted: `docs/specs/preflight-validation.feature.md` and
  `review-issue-and-minor-fix-path.feature.md` — read only to confirm they
  describe mechanisms (Preflight, Minor Fix Path, review-finding lifecycle)
  that ADR 0014 reuses rather than redefines, so they needed no edits;
  historical records under `docs/collaboration/traces/`, `reviews/`,
  `agreements/` (dated 2026-08-02 and earlier), `docs/issues/`,
  `docs/work-plans/`.
- Assumptions:
  - Self-review waives context separation only — the deterministic
    precondition and falsification burden remain required. Confirmed
    explicitly with the Director during dialogue.
  - The work-plan close is one combined action, not two. Confirmed explicitly
    with the Director during dialogue, after a clarifying exchange.
  - ADR 0006 (contract-file change control) is untouched: self-review must
    never apply to changes to the agent operating contract itself, since that
    would validate the rule using the context that is changing it. This
    change itself is therefore reviewed under the pre-change contract, not
    under the model it introduces — the same bootstrapping discipline this
    repository used for its own founding rewrite.
  - Version bump is major (`v2.0.0` candidate) per `CHANGELOG.md`'s own rule:
    this changes the meaning of a rule adopting projects rely on.
- Open decisions: the two rows in the agreement's Deferred Questions —
  whether work-plan size should be bounded, and whether the Arbiter role
  needs to change under this model.

## Routing

- Model/assistant/tool: Claude Opus 5 via Claude Code; deterministic checks
  via `scripts/check-contract-consistency.py`, `bash -n`, targeted `grep`
  sweeps, and the copy-script smoke test.
- Reason: the change is a foundational governance rewrite spanning an ADR,
  two collaboration-scheme documents, all nine contract files, and a dozen
  supporting documents — Architecture Path by definition, and the largest
  single change to the execution-loop model since ADR 0001 itself.
- Privacy constraints: none; repository-local documentation only.

## AI Execution Records

### Attempt 1

- Agent: Claude Code
- Environment: local clone of `llm-loop-project-template`, branch
  `process/work-plan-scoped-governance`, based on `main` at `e445936`
  (tag `v1.1.0-4-ge445936`)
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
- Scope: ADR 0014; propagation into `ai-human-scheme.md`, `personas.md`,
  `design-agreement.md`, all nine contract files, `at-tdd/process.md`,
  `definition-of-done.md`, `work-plan.md`, `local-issue-planning.md`,
  `agent-quickstart.md`, `implementation-readiness.md`, both READMEs, both
  QUICKSTART files, `docs/architecture/README.md`,
  `branch-commit-pr-discipline.md`, `model-tool-capability-matrix.md`,
  `project-start-guide.md`, `template-benefits.md`,
  `.github/pull_request_template.md`, `.github/workflows/ci.yml`;
  new `EXTRA_MIRRORED_RULES` entries in the consistency checker for
  self-review, work-plan-level Reviewer, and work-plan close; ADR 0001's
  Status marked partially superseded.
- Result: complete. All checks below pass.
- Attempt boundary: single continuous session.
- Notes: the propagation surfaced a genuine drift risk in the ADR-numbering
  bump itself — adding ADR 0014 moves the process-ADR count from thirteen to
  fourteen and the adopter-start number from `0014` to `0015` everywhere
  those are stated. That is exactly the defect class
  `scripts/check-contract-consistency.py` was built to catch, and it did:
  after the first full pass the checker still reported clean, which was the
  signal to widen the sweep by hand rather than trust the green run — the
  checker's own disclosure says a green run means "no mechanical drift
  found," not "the contract is consistent," and several genuine gaps
  (`model-tool-capability-matrix.md`, `project-start-guide.md`,
  `template-benefits.md`, `agent-quickstart.md`,
  `implementation-readiness.md`, `branch-commit-pr-discipline.md`,
  `.github/pull_request_template.md`) were found only by manual `grep` sweeps
  the checker does not run.

## Cost / Reasoning Control

- Operating path: Architecture Path.
- Files read: as listed in the Context Ledger.
- Context intentionally omitted: as listed in the Context Ledger.
- Deterministic checks used: recorded under Verification below.
- Escalation reason: rewrites the execution-loop governance model; Architecture
  Path by `docs/collaboration/prompt-instruction-change-control.md` and by
  the scale of the change itself.
- Avoided LLM work: the ADR-range bump (0013→0014, adopter start 0014→0015)
  was verified by `grep` for exact prior strings rather than re-read line by
  line; the nine contract files were edited with matching surgical patches
  per file rather than regenerated whole.
- Rework caused by AI output: none within this attempt — the manual sweep
  found gaps before they were committed, not after.

## Decisions Carried

- Director decisions from the covering design agreement: self-review inside
  a work plan, waiving only context separation; work-plan-level AI review,
  once, in a separate context; a combined human close; fixes remain AI work;
  major version bump.
- Planner/Specifier decisions inside that scope: ADR 0006 is untouched and
  this change is reviewed under it; ADR 0001's Status is marked partially
  superseded rather than the ADR being deleted or its body rewritten,
  matching this repository's established pattern for ADR 0003 and 0012.
- Reviewer decisions, with the failure scenarios searched for: none yet. This
  change has not been reviewed by a separate context. It is reviewed under
  the pre-change contract, per the bootstrapping discipline recorded in the
  covering agreement.
- Arbiter decisions, if any: none.

## Verification

- Commands/checks:
  - `python3 scripts/check-contract-consistency.py --repo .` on the working
    tree.
  - The same, inside a fresh `scripts/copy-ai-collaboration-files.sh` target.
  - A negative test injecting one defect of each claimed class (unregistered
    `AGENTS.md` section, dangling reference, stale ADR range, missing mirror
    section) into a disposable copy.
  - `grep` sweeps for the superseded per-phase phrasing across every `.md`
    and `.mdc` file, excluding historical record directories.
  - `grep` for the ADR-count/range strings (`thirteen`, `0001-0013`,
    `0001–0013`, `0014 and up`, `13 件`, `0014 以降`) to confirm every
    instance was bumped.
  - CI `required_files` existence check; ADR existence loop `0001`-`0014`;
    `bash -n` on all four scripts; conflict-marker scan.
- Result:
  - Consistency checker: passes on the working tree and inside a fresh
    target.
  - Negative test: 4 failures injected, 4 reported, non-zero exit.
  - Phrasing sweep: 0 occurrences of the superseded per-phase language
    outside historical records.
  - ADR-count sweep: 0 occurrences of the stale count/range strings.
  - `required_files`: 69 entries, 0 missing. ADR loop `0001`-`0014`: passes.
    `bash -n`: OK. Conflict markers: none.
- Not verified: CI itself, which requires GitHub Actions; and independent
  review, which is the next step, deliberately run under the pre-change
  contract.

## Changed Files

- Added: `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
  the covering design agreement, this trace.
- Rewritten: `docs/collaboration/ai-human-scheme.md`, `personas.md`,
  `design-agreement.md`; the nine agent operating contract files'
  Prime Directive, Phase Discipline, and Approval Model sections.
- Updated: `docs/at-tdd/process.md`, `definition-of-done.md`,
  `local-issue-planning.md`, `branch-commit-pr-discipline.md`,
  `model-tool-capability-matrix.md`, `project-start-guide.md`,
  `template-benefits.md`; `docs/templates/work-plan.md`,
  `examples/adoption-prompts.md`; `docs/architecture/README.md`,
  `agent-quickstart.md`, `implementation-readiness.md`; `README.md`,
  `README.ja.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`;
  `.github/workflows/ci.yml`, `pull_request_template.md`;
  `scripts/check-contract-consistency.py`;
  `docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
  (Status only).

## Next Safe Action

Submit for independent Reviewer review, in a separate context, under the
pre-change (ADR 0001) contract — the model this change has not yet altered.
On approval: tag `v2.0.0`, since this changes the meaning of a rule adopting
projects rely on.

Two deferred questions from the covering agreement remain open after
approval: whether work-plan size should be bounded, and whether the Arbiter
role needs adjustment under this model. Neither blocks this change; both are
named so a future reader does not mistake the silence for an oversight.

## Notes

The empirical argument against self-review that this change accepts as a
tradeoff is not abstract in this repository: it is the six-round review
history of `scripts/check-contract-consistency.py`, four of whose rounds
found the checker claiming a coverage it did not have — findings the
producing context could not have made about itself. ADR 0014 records that
this tradeoff is accepted with that history in view, not overlooked.

The same pattern showed up once more while building this very change: the
first full propagation pass reported clean, and the real gaps were found only
by widening the sweep by hand. A checker that verifies presence of a phrase
is not the same as a reader verifying the phrase is where it needs to be —
the distinction this whole repository exists to keep visible.
