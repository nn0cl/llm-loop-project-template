# LISS-0040: Copy-exclusion exemption for check-contract-consistency.py's reference check

## Metadata

- Local issue ID: LISS-0040
- GitHub issue: none
- Status: review
- Phase: phase-0-design
- Type: bug-fix
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/copy-target-refs-and-branch-cleanup

## Summary

- `scripts/check-contract-consistency.py`'s `check_references` reports a
  dangling reference for any target that does not exist, with no exception
  for a target this template intentionally excludes from adopter copies
  (`scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths`). Against a scratch copy produced
  by `scripts/copy-ai-collaboration-files.sh`, ADRs 0016-0019,
  `docs/collaboration/cross-session-messaging.md`, and
  `docs/collaboration/design-review-perspectives.md` all cite excluded
  paths as evidence (correctly, per Invariant 3), producing 26 false-
  positive failures — the exact class CI's "Repository sanity" job reported
  on run
  https://github.com/nn0cl/llm-loop-project-template/actions/runs/32248215256.
- Fix: add a third "expected-absent" exemption to `check_references`,
  alongside the existing `TEMPLATE_ONLY_FILES` and
  `OPTIONAL_INIT_CREATED_FILES` ones — a target that does not exist, but
  matches a pattern in `collaboration_template_exclude_paths`
  (`scripts/lib/collaboration-template-paths.sh`), is not a dangling
  reference. Reuse that list via a small parser (regex over the `.sh`
  file's array literal) and `fnmatch.fnmatchcase`, rather than a second,
  independently maintained pattern list.

## Acceptance Notes

- Real scratch-copy reproduction (not a synthetic fixture): copy this
  repository into a scratch target using the same selection
  `scripts/copy-ai-collaboration-files.sh` uses (or the script itself, if
  runnable against a scratch destination), then run
  `python3 scripts/check-contract-consistency.py --repo <scratch>`.
- Red: before the fix, the scratch-copy run reports dangling-reference
  failures for paths matching `collaboration_template_exclude_paths` (the
  same class the linked CI run reported).
- Green: after the fix, the same scratch-copy run passes with no failures
  in the "references" category attributable to excluded-pattern paths.
- `python3 scripts/check-contract-consistency.py --repo .` (against this
  repository itself, not a copy) stays a clean pass throughout — the
  exemption must never suppress a target that genuinely exists.
- Module docstring's "What this cannot check" section discloses the new
  exemption's own residual gap (a genuinely broken reference to an
  excluded-shaped path, in this repository's own tree, is now also
  silently accepted).
- Self-review recorded (short form — planning size S).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0011-copy-target-references-and-branch-cleanup.md`,
  `scripts/lib/collaboration-template-paths.sh`,
  `scripts/copy-ai-collaboration-files.sh`

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0011-*.md`, `DA-2026-08-19-04`,
  `scripts/check-contract-consistency.py` (whole file),
  `scripts/lib/collaboration-template-paths.sh` (whole file),
  `scripts/copy-ai-collaboration-files.sh` (copy-selection logic only).
- Omitted: unrelated checker functions not touched by this issue
  (`check_mirror_parity`, `check_adr_range`, etc. — read for context, not
  modified).
- Assumptions: bash `case` glob matching and Python's
  `fnmatch.fnmatchcase` are equivalent for every pattern currently in
  `collaboration_template_exclude_paths` (all use only `*` and literal
  path segments; no `?`, `[...]`, or other glob metacharacters that could
  diverge between the two implementations) — verified by direct inspection
  of the pattern list, not assumed.

## AI Planning Records

### AIP-0040-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code, Design & Review group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not displayed in this environment)
  - N/A reason: this environment does not surface a reasoning-effort label
- Created at: 2026-08-19
- Planning size: S
- Intended execution route: direct edit, single function plus one new
  helper and one docstring addition
- Compatibility state: Verified — `fnmatch.fnmatchcase` behavior for `*`
  confirmed against the exact patterns present in
  `collaboration_template_exclude_paths` today
- Intended scope: `scripts/check-contract-consistency.py` only
- Estimated token range: low thousands
- Estimated token midpoint: N/A (not tracked in this environment)
- Token metric: N/A
- Estimation basis: single-file, single-function scope, no new dependency
- Assumptions: see Context above
- Confidence: high
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `scripts/lib/collaboration-template-paths.sh` (this repository, read
  directly — the pattern list being reused).

## Work Notes

- Persona: Implementer.
- Fix: added `_copy_exclusion_patterns` (parses
  `collaboration_template_exclude_paths` out of
  `scripts/lib/collaboration-template-paths.sh` with a regex over the array
  literal, degrading to `[]` when the file is absent/unreadable, mirroring
  `read_optional`'s degrade shape) and `_is_copy_excluded_reference`
  (matches a target against those patterns with `fnmatch.fnmatchcase`) in
  `scripts/check-contract-consistency.py`. Wired the exemption into
  `check_references` alongside the existing `TEMPLATE_ONLY_FILES` /
  `OPTIONAL_INIT_CREATED_FILES` checks, same shape: only a target that does
  not exist and matches an exclude pattern is treated as expected-absent.
  Added the disclosed residual gap to the module docstring's "What this
  cannot check" section, and a short clause to the `Checks:` list's item 3.
- No second, independently maintained pattern list was created —
  `_copy_exclusion_patterns` reads `collaboration_template_exclude_paths`
  directly from `scripts/lib/collaboration-template-paths.sh` every call.

### Self-review (short form, planning size S)

Phase / finding: Red then Green, reproducing the CI "Repository sanity"
smoke test locally (`.github/workflows/ci.yml`'s "Check template copy smoke
test" step), against a real scratch copy — not a synthetic fixture — per
this issue's own Acceptance Notes.

Command run (Red, before the fix, on this repository's own HEAD prior to any
code change in this issue):

```
tmp="$(mktemp -d)"; mkdir -p "$tmp/target"; git init -q "$tmp/target"
scripts/copy-ai-collaboration-files.sh --target "$tmp/target" \
  --project-name "Smoke App" --domain-summary "template smoke test" \
  --stack "test stack"
python3 "$tmp/target/scripts/check-contract-consistency.py" --repo "$tmp/target"
```

Result (Red — actual pasted output, 26 failures, every one a path matching
`collaboration_template_exclude_paths`):

```
references:
  docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:6 names 'docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md', which does not exist
  docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:23 names 'docs/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
  docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:80 names 'docs/backlog/item-0004-two-group-send-message-loop.md', which does not exist
  docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md:6 names 'docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md', which does not exist
  docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md:14 names 'docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md', which does not exist
  docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md:18 names 'docs/backlog/item-0007-multi-agent-tool-loop-portability.md', which does not exist
  docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md:36 names 'docs/backlog/item-0007-multi-agent-tool-loop-portability.md', which does not exist
  docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:6 names 'docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md', which does not exist
  docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:8 names 'docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md', which does not exist
  docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:29 names 'docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md', which does not exist
  docs/architecture/adr/0019-loop-ledgers.md:6 names 'docs/collaboration/agreements/2026-08-19-adr-loop-ledgers.md', which does not exist
  docs/architecture/adr/0019-loop-ledgers.md:9 names 'docs/work-plans/WP-0010-adr-loop-ledgers.md', which does not exist
  docs/architecture/adr/0019-loop-ledgers.md:13 names 'docs/backlog/item-0002-adr-loop-ledgers.md', which does not exist
  docs/collaboration/cross-session-messaging.md:77 names 'docs/backlog/item-0008-coordinator-message-hallucination-correction.md', which does not exist
  docs/collaboration/design-review-perspectives.md:58 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md', which does not exist
  docs/collaboration/design-review-perspectives.md:64 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-3.md', which does not exist
  docs/collaboration/design-review-perspectives.md:65 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md', which does not exist
  docs/collaboration/design-review-perspectives.md:66 names 'docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
  docs/collaboration/design-review-perspectives.md:88 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md', which does not exist
  docs/collaboration/design-review-perspectives.md:92 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md', which does not exist
  docs/collaboration/design-review-perspectives.md:115 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review.md', which does not exist
  docs/collaboration/design-review-perspectives.md:117 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md', which does not exist
  docs/collaboration/design-review-perspectives.md:120 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-3.md', which does not exist
  docs/collaboration/design-review-perspectives.md:126 names 'docs/collaboration/reviews/2026-08-02-contract-consistency-review-4.md', which does not exist
  docs/collaboration/design-review-perspectives.md:169 names 'docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
  docs/collaboration/design-review-perspectives.md:181 names 'docs/backlog/item-0008-coordinator-message-hallucination-correction.md', which does not exist

contract consistency: 26 failure(s)
```

Command run (Green, after the fix, on a fresh scratch copy — new `mktemp -d`,
same steps as above):

Result (Green — actual pasted output):

```
contract consistency: all checks passed
```

Command run (this repository's own `HEAD`, not a copy — before and after the
fix): `python3 scripts/check-contract-consistency.py --repo .`

Result (both before and after the fix): `contract consistency: all checks
passed` (one transient, self-caused exception during this issue's own work:
after editing this issue's own `Status:` field to `in_progress` without yet
syncing `WP-0012`'s Issue Graph row, the "issue status sync" check correctly
flagged the mismatch — expected, not a defect in this fix, and resolved by
updating the work plan's Issue Graph in the same change).

Risks considered:
- The fix swallows a genuinely broken reference in this repository's own
  tree that happens to be shaped like an excluded pattern (the exact
  falsification criterion DA-2026-08-19-04 names).
- The fix hardcodes a second exclude-pattern list instead of reusing
  `collaboration_template_exclude_paths`.
- `fnmatch.fnmatchcase` diverges from bash `case` glob matching for some
  pattern currently in the list, producing a false exemption or a missed
  one.

Why each does not occur:
- Verified directly: added a scratch file at
  `docs/collaboration/scratch-liss0040-negative-check.md` (deleted after the
  check, never committed) naming a genuinely nonexistent, non-excluded-shaped
  target (`docs/collaboration/definitely-does-not-exist-anywhere.md`), ran
  `python3 scripts/check-contract-consistency.py --repo .`, and got a
  "references" failure naming exactly that file:line and target — the
  exemption did not swallow it. Command and full output:
  ```
  $ python3 scripts/check-contract-consistency.py --repo .
  references:
    docs/collaboration/scratch-liss0040-negative-check.md:3 names 'docs/collaboration/definitely-does-not-exist-anywhere.md', which does not exist

  contract consistency: 1 failure(s)
  ```
  Deleted the scratch file afterward; a follow-up run returned to `contract
  consistency: all checks passed`.
- `_copy_exclusion_patterns` reads `collaboration_template_exclude_paths`
  directly from `scripts/lib/collaboration-template-paths.sh` with a regex
  over the array literal (`collaboration_template_exclude_paths=\((.*?)\)`)
  and extracts every quoted string inside it — no second list is written or
  maintained anywhere in `check-contract-consistency.py`.
- Confirmed by direct inspection (not assumed) that every pattern currently
  in `collaboration_template_exclude_paths` (`docs/collaboration/traces/*.md`,
  `docs/collaboration/agreements/*.md`, `docs/collaboration/reviews/*.md`,
  `docs/issues/LISS-*.md`, `docs/specs/*.md`, `docs/spike/case-*`,
  `docs/backlog/item-*.md`, `docs/work-plans/WP-*.md`,
  `docs/collaboration/loop-settings.toml`) uses only literal path segments
  and `*`, with no `?`, `[...]`, or other glob metacharacter that could
  diverge between bash `case` matching and `fnmatch.fnmatchcase` — both
  treat `*` as matching any run of characters, including `/`, for every one
  of these patterns.

## Verification

- Red: reproduced CI's own smoke-test flow against a real scratch copy;
  26 dangling-reference failures, all matching
  `collaboration_template_exclude_paths` — pasted above.
- Green: same reproduction on a fresh scratch copy, after the fix;
  `contract consistency: all checks passed` — pasted above.
- This repository's own `HEAD` stayed a clean pass throughout (transient
  self-caused status-sync mismatch noted and resolved above).
- Negative case: a genuinely broken, non-excluded-shaped reference is still
  caught — pasted above.
