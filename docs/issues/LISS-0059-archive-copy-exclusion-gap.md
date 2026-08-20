# LISS-0059: `docs/archive/` missing from the copy-exclusion pattern list

## Metadata

- Local issue ID: LISS-0059
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: bug
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`)
- Related branch: process/promote-item-0018 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

PR #21 (WP-0019, item-0016's first ADR-0020 archival batch) fails CI's
"Repository sanity" / "Check template copy smoke test" with 26
dangling-reference failures, all of the shape `docs/archive/...`, which
does not exist` (confirmed directly against the actual CI run,
`https://github.com/nn0cl/llm-loop-project-template/actions/runs/32329294706/job/96306710499`).

Root cause, confirmed by direct reading of the two files involved:

- `scripts/lib/collaboration-template-paths.sh`'s `collaboration_template_paths`
  array (the only list `scripts/copy-ai-collaboration-files.sh` walks when
  building an adopter/test copy) does not list `docs/archive` at all, so
  `docs/archive/` is never copied to the target — correct behavior in
  itself, since archived content is this template's own history, not
  adopter-owned content (matching the treatment `docs/issues/LISS-*.md`,
  `docs/work-plans/WP-*.md`, etc. already get).
- But `scripts/check-contract-consistency.py`'s `_copy_exclusion_patterns()`
  (added by item-0011/LISS-0040) parses its exemption patterns directly
  from that same file's `collaboration_template_exclude_paths` array —
  confirmed by direct reading of `_copy_exclusion_patterns()`'s own
  docstring and regex (`scripts/check-contract-consistency.py` lines
  258-296) — and that array does not have a `docs/archive/*` entry either.
  So a real, correct reference from a still-current document (ADR 0016,
  `docs/collaboration/design-review-perspectives.md`,
  `docs/collaboration/restoration-ledger.md` — all three copied to the
  target, since they live under `docs/architecture`/`docs/collaboration`,
  both listed in `collaboration_template_paths`) to a now-archived file is
  correctly absent on the copy, but not recognized as *expected*-absent,
  so `check_references()` reports it as a genuine dangling reference.

**This is not the same gap `LISS-0044` already closed.** Confirmed by
direct reading of both the current tree and `LISS-0044`'s own file:
`LISS-0044` was `scripts/check-contract-consistency.py`'s `RECORD_DIRS`
constant not exempting `docs/archive/`'s own *outbound* content from
present-tense scanning when the checker runs directly against the real
repository — that was fixed by WP-0016/LISS-0048 (`RECORD_DIRS` already
contains `"docs/archive/",` at line ~328 of the current script, confirmed
directly), and `LISS-0044` is already `Status: closed`, with its own
Verification section recording a real synthetic-file reproduction and
fix confirmation. That fix is a different mechanism (present-tense
outbound-content scanning against the real tree) from this issue's own
gap (the copy-simulation's *inbound*-reference exemption list, checked
against a *copied* target where the file is legitimately absent by
design). `docs/backlog/item-0018-...md`'s own text describes this issue
as "clos[ing] LISS-0044... per the finding's own stated trigger
condition," but that premise does not hold once `LISS-0044`'s own file is
read directly — it is already closed and does not need reopening or
further action. This issue does not touch `LISS-0044`'s own file; no
further edit to it is warranted.

## Acceptance Notes

Add exactly one entry to `collaboration_template_exclude_paths` in
`scripts/lib/collaboration-template-paths.sh`:

```bash
collaboration_template_exclude_paths=(
  "docs/collaboration/traces/*.md"
  "docs/collaboration/agreements/*.md"
  "docs/collaboration/reviews/*.md"
  "docs/issues/LISS-*.md"
  "docs/specs/*.md"
  "docs/spike/case-*"
  "docs/backlog/item-*.md"
  "docs/work-plans/WP-*.md"
  "docs/collaboration/loop-settings.toml"
  "docs/archive/*"
)
```

**Do not** add `docs/archive` to `collaboration_template_paths` (the
copy-inclusion list). Confirmed by direct reading of
`scripts/copy-ai-collaboration-files.sh`'s `copy_path()` function (lines
129-159): only entries in `collaboration_template_paths` are ever visited
by the copy walk at all; `collaboration_template_exclude_paths` is
consulted only *inside* that walk, to skip specific files under an
already-included parent directory. Since `docs/archive` is not, and per
ADR 0020's own Rule 1 (Archive layer holds this template's own historical
record, off the normal reading path) should not become, an included
parent, adding the exclude-pattern alone is sufficient and is the whole
fix on the shell-script side — it has no effect on
`copy-ai-collaboration-files.sh`'s own behavior (the pattern is never
reached, since `docs/archive` is never walked), but is essential for
`scripts/check-contract-consistency.py`'s `_copy_exclusion_patterns()`,
which parses this exact array as its own single source of truth (per that
function's own docstring) for `check_references()`'s copy-exclusion
exemption. No Python code change is required — the exemption is entirely
data-driven from this one array.

### Required reproduction (before and after)

1. Run `scripts/copy-ai-collaboration-files.sh` against a throwaway target
   directory (the same mechanism CI's "Check template copy smoke test"
   step uses — inspect `.github/workflows/ci.yml`'s own step for the exact
   invocation before reproducing, to match it precisely) using the
   **pre-fix** `scripts/lib/collaboration-template-paths.sh`, then run
   `python3 scripts/check-contract-consistency.py --repo <target>` against
   the result. Paste the actual output, confirming real `docs/archive/...,
   which does not exist` dangling-reference failures are produced —
   ideally reproducing the same 26-failure count PR #21's own CI run
   showed, or explaining any difference if the count does not match
   exactly (e.g., if this issue's own branch has a different archive-batch
   history than PR #21's branch at the time it ran).
2. Apply the fix.
3. Re-run the same copy + checker sequence against the same target,
   confirm the `docs/archive/...` dangling-reference failures are gone.
4. Confirm `docs/archive` itself does not appear anywhere under the
   copied target directory (`find <target> -path '*/docs/archive*'`
   returns nothing) — the fix must not accidentally cause `docs/archive`
   to start being copied.
5. Run `python3 scripts/check-contract-consistency.py` (no `--repo` flag,
   against this issue's own real worktree) to confirm no regression on
   the real, uncopied repository.

## Dependencies

- Parent: `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`
- Depends on: none
- Blocks: PR #21 (WP-0019's own merge to `main`) — CI on that PR cannot
  pass until this fix lands on `main`.
- Related: `docs/backlog/item-0018-archive-copy-exclusion-gap.md`,
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (related
  but distinct; already closed, not reopened by this issue),
  `scripts/lib/collaboration-template-paths.sh`,
  `scripts/check-contract-consistency.py`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-archive-copy-exclusion-gap.md`.

## Context

- Included: `docs/backlog/item-0018-...md`'s full text, PR #21's actual CI
  failure log (independently fetched via `gh run view --log`, not taken on
  the backlog item's own description alone), `scripts/lib/collaboration-template-paths.sh`
  and `scripts/check-contract-consistency.py`'s relevant functions in
  full, `docs/issues/LISS-0044-...md`'s full text and current `Status`
  field (independently re-read, not assumed from the backlog item's own
  characterization of it).
- Omitted: the rest of `check-contract-consistency.py`'s other check
  functions (unaffected — this is a pure data/array change, no check
  logic is touched).
- Assumptions: none. The one premise this issue explicitly corrects
  (that this fix "closes LISS-0044") was independently checked against
  the actual current file state before writing this issue, not assumed
  true from the backlog item's own wording.

## References

- `docs/backlog/item-0018-archive-copy-exclusion-gap.md`
- `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`
- `scripts/lib/collaboration-template-paths.sh`
- `scripts/check-contract-consistency.py`
- PR #21: https://github.com/nn0cl/llm-loop-project-template/pull/21
- Failing CI run: https://github.com/nn0cl/llm-loop-project-template/actions/runs/32329294706

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0021, scoped per the design agreement. Not yet dispatched.
  Independently confirmed via `gh run view --log` that PR #21's actual CI
  failure matches the backlog item's own description (26 failures, all
  `docs/archive/...` dangling-reference shape) before writing this issue.
  Independently confirmed `LISS-0044` is already `Status: closed` and its
  own fix (the `RECORD_DIRS` entry) is present in the current tree at
  `scripts/check-contract-consistency.py` line ~328 — the backlog item's
  premise that this issue "closes LISS-0044" does not hold; recorded
  above as a correction, not acted on by reopening that issue.

## Verification

- Before-fix reproduction: real `docs/archive/...` dangling-reference
  failures on a copied target (pasted, not summarized).
- After-fix: same reproduction shows zero such failures.
- `docs/archive` confirmed absent from the copied target directory tree.
- `python3 scripts/check-contract-consistency.py` (real repository, no
  `--repo` flag) shows no regression.
- `git diff scripts/lib/collaboration-template-paths.sh` shows exactly one
  added line.
