# LISS-0059: `docs/archive/` missing from the copy-exclusion pattern list

## Metadata

- Local issue ID: LISS-0059
- GitHub issue: none
- Status: done
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

- 2026-08-20 — Implementation group (Implementer persona), on branch
  `wp-0021-execution` (created off `process/promote-item-0018`).

  First attempt: `process/promote-item-0018` at commit `95f3eab` did not
  yet contain the WP-0019/archival-batch commits (`81ddf2a`, `dfe5030`,
  only reachable from `process/promote-item-0016`) that create
  `docs/archive/` content, so `docs/archive/` did not exist on that branch
  at all and the pre-fix reproduction genuinely showed zero
  `docs/archive/...` dangling-reference failures (`contract consistency:
  all checks passed`, both against a copied target and against the real
  repository). Per the design agreement's own Falsification Criteria ("The
  reproduction does not actually show the real CI failure shape before the
  fix"), the fix was not applied against that state; the gap was reported
  back instead of guessed past. The coordinating session merged
  `process/promote-item-0016` into `process/promote-item-0018` (merge
  commit `54f73c7`, clean, disjoint files) to bring the archived content
  onto this issue's branch, and this branch was reset onto that merge
  commit before re-attempting.

  Reproduction (before fix), against `wp-0021-execution` at `54f73c7`,
  using the exact CI invocation from `.github/workflows/ci.yml`'s "Check
  template copy smoke test" step (`scripts/copy-ai-collaboration-files.sh
  --target <tmp> --project-name "Smoke App" --domain-summary "template
  smoke test" --stack "test stack"`, then
  `python3 scripts/check-contract-consistency.py --repo <tmp>`):

  ```
  references:
    docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:23 names 'docs/archive/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
    docs/collaboration/design-review-perspectives.md:66 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
    docs/collaboration/design-review-perspectives.md:169 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
    docs/collaboration/restoration-ledger.md:46 names 'docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md', which does not exist
    docs/collaboration/restoration-ledger.md:47 names 'docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md', which does not exist
    docs/collaboration/restoration-ledger.md:48 names 'docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md', which does not exist
    docs/collaboration/restoration-ledger.md:49 names 'docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md', which does not exist
    docs/collaboration/restoration-ledger.md:50 names 'docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md', which does not exist
    docs/collaboration/restoration-ledger.md:51 names 'docs/archive/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
    docs/collaboration/restoration-ledger.md:52 names 'docs/archive/issues/LISS-0019-adr-0016-two-group-topology.md', which does not exist
    docs/collaboration/restoration-ledger.md:53 names 'docs/archive/issues/LISS-0020-personas-group-mapping.md', which does not exist
    docs/collaboration/restoration-ledger.md:54 names 'docs/archive/issues/LISS-0021-ai-human-scheme-loop-update.md', which does not exist
    docs/collaboration/restoration-ledger.md:55 names 'docs/archive/issues/LISS-0022-cross-session-messaging-protocol.md', which does not exist
    docs/collaboration/restoration-ledger.md:56 names 'docs/archive/issues/LISS-0023-session-start-standing-pair.md', which does not exist
    docs/collaboration/restoration-ledger.md:57 names 'docs/archive/issues/LISS-0024-implementation-group-worktree-rule.md', which does not exist
    docs/collaboration/restoration-ledger.md:58 names 'docs/archive/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md', which does not exist
    docs/collaboration/restoration-ledger.md:59 names 'docs/archive/issues/LISS-0026-backlog-readme-bulk-gate.md', which does not exist
    docs/collaboration/restoration-ledger.md:60 names 'docs/archive/issues/LISS-0027-at-tdd-process-adr-0016-qualification.md', which does not exist
    docs/collaboration/restoration-ledger.md:61 names 'docs/archive/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md', which does not exist
    docs/collaboration/restoration-ledger.md:62 names 'docs/archive/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md', which does not exist
    docs/collaboration/restoration-ledger.md:63 names 'docs/archive/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md', which does not exist
    docs/collaboration/restoration-ledger.md:64 names 'docs/archive/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md', which does not exist
    docs/collaboration/restoration-ledger.md:65 names 'docs/archive/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md', which does not exist
    docs/collaboration/restoration-ledger.md:66 names 'docs/archive/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md', which does not exist
    docs/collaboration/restoration-ledger.md:67 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
    docs/collaboration/restoration-ledger.md:68 names 'docs/archive/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md', which does not exist

  contract consistency: 26 failure(s)
  ```

  Exactly 26 failures, all `docs/archive/...` shape, matching PR #21's own
  CI run count.

  Fix applied: added `"docs/archive/*"` as the last entry of
  `collaboration_template_exclude_paths` in
  `scripts/lib/collaboration-template-paths.sh` (`git diff` confirmed
  exactly one line added, nothing else touched).

  Reproduction (after fix), same invocation against a fresh throwaway
  target:

  ```
  contract consistency: all checks passed
  ```

  All 26 `docs/archive/...` dangling-reference failures are gone.
  `find <target> -path '*docs/archive*'` on the post-fix copied target
  returned no output — `docs/archive` remains un-copied, confirming the
  fix did not also touch `collaboration_template_paths`.
  `python3 scripts/check-contract-consistency.py` against the real,
  uncopied worktree (no `--repo` flag) also reported `contract
  consistency: all checks passed` — no regression. All throwaway `$tmp`
  directories and their `git init`-ed contents were removed
  (`rm -rf`) after each reproduction; nothing from either reproduction was
  committed.

  **Self-review (short form, per `docs/templates/self-review.md`)**

  ```
  Phase: Fast Path
  Command run: scripts/copy-ai-collaboration-files.sh --target <tmp>/target \
    --project-name "Smoke App" --domain-summary "template smoke test" \
    --stack "test stack" && python3 scripts/check-contract-consistency.py \
    --repo <tmp>/target
  Result: before fix, "contract consistency: 26 failure(s)", all
    docs/archive/... dangling-reference shape (full output above); after
    fix, "contract consistency: all checks passed" (both the copied
    target and, separately, the real repository with no --repo flag).
  Risks considered:
    1. The `docs/archive/*` exclude pattern could be too broad and start
       exempting a currently-checked reference that should stay flagged as
       genuinely dangling (i.e., masking a real bug elsewhere under
       `docs/archive/`).
    2. The fix could accidentally cause `docs/archive` to start being
       copied to adopter targets (an over-broad change reaching into
       `collaboration_template_paths` instead of, or in addition to,
       `collaboration_template_exclude_paths`).
    3. `_copy_exclusion_patterns()` could fail to parse the new array
       entry (e.g. a quoting/regex mismatch), silently leaving the
       exemption inactive.
  Why each does not occur:
    1. The pattern `docs/archive/*` only ever matches paths that literally
       start with `docs/archive/`. That prefix is populated exclusively by
       this template's own ADR-0020 archival mechanism (Rule 3, in-tree
       moves under `docs/archive/<original-directory>/<original-filename>`)
       — it holds only this template's own superseded/consolidated
       records, never adopter- or feature-specific content, so exempting
       the whole prefix cannot mask a reference to anything outside that
       mechanism's own output.
    2. `git diff scripts/lib/collaboration-template-paths.sh` (recorded
       above and in the commit) shows the one added line lands inside
       `collaboration_template_exclude_paths`, not
       `collaboration_template_paths`; the post-fix
       `find <target> -path '*docs/archive*'` returning empty directly
       confirms `docs/archive` is still never copied.
    3. The post-fix reproduction's clean "all checks passed" result against
       the copied target is itself the direct evidence the array is parsed
       correctly — `_copy_exclusion_patterns()`'s existing regex
       (`collaboration_template_exclude_paths=\((.*?)\)` then
       `"([^"]+)"`) already matches every other quoted, no-special-char
       entry in that array, and the new entry uses the same quoting style
       (`"docs/archive/*"`) with no glob metacharacter the two
       implementations (bash `case` vs Python `fnmatch.fnmatchcase`) could
       diverge on.
  ```

## Verification

- Before-fix reproduction: real `docs/archive/...` dangling-reference
  failures on a copied target (pasted, not summarized).
- After-fix: same reproduction shows zero such failures.
- `docs/archive` confirmed absent from the copied target directory tree.
- `python3 scripts/check-contract-consistency.py` (real repository, no
  `--repo` flag) shows no regression.
- `git diff scripts/lib/collaboration-template-paths.sh` shows exactly one
  added line.
