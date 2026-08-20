# LISS-0054: Interactive prompting for `scripts/copy-ai-collaboration-files.sh`

## Metadata

- Local issue ID: LISS-0054
- GitHub issue: none
- Status: ready
- Phase: phase-0-design
- Type: feature
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (Implementer persona)
- Related branch: process/interactive-copy-script (Implementation-group
  worktree branch, merged into the shared branch
  `process/promote-item-0015`)

## Summary

- `scripts/copy-ai-collaboration-files.sh` is flag-driven only: a new
  adopter must know `--target`, `--project-name`, `--domain-summary`, and
  `--stack` up front. `scripts/update-ai-collaboration-files.sh` already has
  a working interactive-prompt precedent (`is_interactive_tty()`, an
  explicit stated default per prompt, `--non-interactive` override) that
  this issue mirrors.
- Add: an `is_interactive_tty()` helper identical in shape to the one in
  `scripts/update-ai-collaboration-files.sh` (checks
  `[ "$non_interactive" != true ] && [ -t 0 ] && [ -t 1 ]`); a new
  `--non-interactive` flag; and, when interactive and a value was not
  supplied as a flag, a prompt for each of `--target` (required — loops on
  an empty response, since no default is possible), `--project-name`,
  `--domain-summary`, and `--stack` (each optional — a single prompt,
  stating the field is optional, empty response accepted and treated
  exactly as if the flag were omitted).
- `--force` and `--dry-run` stay flag-only, never prompted (see the design
  agreement's Settled Ambiguities for the grounds).
- Exact prompt text, flow placement, and every scenario this must satisfy:
  `docs/specs/interactive-copy-script.feature.md`.
- Deterministic verification: a new Python test file driving the script
  through a real pseudo-terminal via the standard-library `pty` module
  (test-only infrastructure; the shipped script stays bash-only). Add it as
  a new CI step alongside the existing "Check template copy smoke test"
  step in `.github/workflows/ci.yml`, so the interactive behavior is
  actually exercised in CI, not only exercised by a flag-driven smoke test
  that never engages the TTY-gated code path.

## Acceptance Notes

- Every Gherkin scenario in `docs/specs/interactive-copy-script.feature.md`
  has a passing, deterministic test exercising it (pty-based for the
  TTY-gated scenarios; a plain non-TTY invocation is sufficient for the
  "non-interactive shell skips all prompting" scenario, since the existing
  CI runner already provides that condition for free).
- `bash -n scripts/copy-ai-collaboration-files.sh` passes.
- The existing "Check template copy smoke test" CI step continues to pass
  unmodified — this is additive, not a replacement for flag-driven use.
- `python3 scripts/check-contract-consistency.py --repo .` passes (this
  issue touches no contract file, so this is a regression check, not an
  expected-change check).
- `scripts/copy-ai-collaboration-files.sh --help` documents `--non-interactive`
  and states that missing values are prompted for interactively.
- Self-review recorded at each phase transition (Red to Green, Green to
  Refactor), per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`;
  full-form self-review per `docs/architecture/adr/0015-review-cost-discipline.md`
  (planning size `M`).

## Review Finding Record

N/A — `Type` is `feature`, not `review-finding`.

## Dependencies

- Parent: docs/work-plans/WP-0018-interactive-copy-script.md
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0015-interactive-copy-script.md`,
  `scripts/update-ai-collaboration-files.sh` (the interactive-prompt
  precedent mirrored here), `docs/collaboration/adoption-guide.md` (read
  for context, not changed — see spec's Out of Scope)

## Decisions Not Settled by the Design Agreement

- None identified — both judgment calls the backlog item flagged
  (`--force`/`--dry-run` prompting; empty-optional-prompt behavior) are
  settled in `DA-2026-08-20-01`'s Settled Ambiguities, and the exact prompt
  contract is pinned down in the spec referenced above. If the Implementer
  finds a case the spec does not cover, that is a reopening request, not a
  judgment call to resolve unilaterally.

## Context

- Included: `docs/backlog/item-0015-interactive-copy-script.md` (whole
  file), `scripts/copy-ai-collaboration-files.sh` (whole file, current
  state), `scripts/update-ai-collaboration-files.sh` (whole file, as the
  precedent — specifically `is_interactive_tty()` and
  `ask_restore_or_keep_deleted()`), `.github/workflows/ci.yml`'s "Check
  template copy smoke test" step, `docs/specs/interactive-copy-script.feature.md`.
- Omitted: `scripts/lib/collaboration-template-paths.sh` and
  `scripts/init-llm-context.sh` (unrelated to prompting; not touched),
  `docs/collaboration/adoption-guide.md`'s full body (only its two lines
  naming the copy script were checked, per the spec's Out of Scope).
- Assumptions: `python3` is available in every environment this script
  already runs in, since `scripts/check-contract-consistency.py` already
  requires it and CI already invokes `python3` directly — using it for
  test-only pty driving adds no new environment requirement.

## AI Planning Records

### AIP-0054-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code (Design & Review group session)
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not surfaced by this harness)
  - N/A reason: this environment does not display a separate reasoning-effort
    label to the session itself.
- Created at: 2026-08-20
- Planning size: M
- Intended execution route: Implementation-group subagent, isolated git
  worktree, branch `process/interactive-copy-script`, merged back into the
  shared branch `process/promote-item-0015` on completion.
- Compatibility state: Verified — `is_interactive_tty()`'s shape and the
  pty-driving approach (`python3 -c` with `pty.fork()`) were both smoke-
  tested directly in this session before this plan was written.
- Intended scope: `scripts/copy-ai-collaboration-files.sh`,
  `.github/workflows/ci.yml` (one new step), one new pty-based Python test
  file under `scripts/tests/`.
- Estimated token range: 40,000-90,000
- Estimated token midpoint: 65,000
- Token metric: cumulative input+output tokens across the Implementer
  subagent's Red+Green+Refactor turns, as reported by that session's own
  usage accounting.
- Estimation basis: comparable in surface area to WP-0016's
  drift-prevention CI-check issues (new script logic plus one new CI step
  plus a dedicated test artifact), scaled down since no new architecture
  document is involved.
- Assumptions: single execution attempt; no dependency-adoption note
  needed (python3's `pty` module is standard library, not a new
  dependency).
- Confidence: medium — the prompt-flow design itself is fully pinned down
  by the spec, but pty-based test flakiness (timing-sensitive reads) is a
  known general risk class for this approach and could require a second
  attempt at the test file specifically.
- Revises: N/A
- Revision reason: N/A
- Superseded by: N/A

## References

- `scripts/update-ai-collaboration-files.sh` (this repository, current
  branch) — the interactive-prompt precedent mirrored by this issue.
- Python standard library `pty` module documentation
  (https://docs.python.org/3/library/pty.html) — used for the pseudo-
  terminal test harness; standard library only, no external package.

## Work Notes

- 2026-08-20: Issue created by the Design & Review group (Planner/Specifier
  persona) under `DA-2026-08-20-01`, following ADR 0016 Rule 2 autonomous
  planning from `docs/backlog/item-0015-interactive-copy-script.md`'s
  promotion.

## Verification

- To be recorded by the Implementer at each phase transition, and by this
  work plan's Preflight Validation section before the separate-context
  Reviewer pass.
