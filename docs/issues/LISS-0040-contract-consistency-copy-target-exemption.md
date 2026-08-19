# LISS-0040: Copy-exclusion exemption for check-contract-consistency.py's reference check

## Metadata

- Local issue ID: LISS-0040
- GitHub issue: none
- Status: proposed
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

- 

## Verification

- 
