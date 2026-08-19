# Backlog item: item-0011-copy-target-references-and-branch-cleanup

## Metadata

- Item ID: item-0011
- Title: Fix contract-consistency false positives on copied targets, and
  make branch/worktree cleanup a standard part of work-plan completion
- Status: promoted
- Created: 2026-08-19
- Updated: 2026-08-19
- Priority hint: high
- Suggested planning size: M
- Owner/agent (optional): unassigned

## Summary

Two related end-of-work hygiene gaps, found while attempting to merge PR #16
into `main`:

**1. CI's "Repository sanity" check fails on PR #16 (26 failures).** The
smoke test copies this template into a scratch target (excluding
`docs/collaboration/agreements/*.md`, `docs/collaboration/reviews/*.md`,
`docs/issues/LISS-*.md`, `docs/backlog/item-*.md`, and
`docs/work-plans/WP-*.md`, by design — see
`scripts/lib/collaboration-template-paths.sh`), then runs
`scripts/check-contract-consistency.py --repo` against that copy. New ADRs
0016-0019, `cross-session-messaging.md`, and `design-review-perspectives.md`
all cite specific agreement/work-plan/backlog/review file paths as
supporting evidence (a correct and intentional pattern — Invariant 3, "every
claim states its grounds"), but those exact paths are the ones deliberately
excluded from copies, so the checker reports them as dangling references
against the copied target even though they are legitimate references
against this template's own repository. This is a known, pre-existing gap
class — WP-0005's Implementer found it independently (3 of 4 similar
failures already present before this session's work) and flagged it as a
separate follow-up (`task_cdbaa1ce`, status unknown to this thread — that
task ran in a separate local session this thread cannot query; treat this
item as authorizing the fix regardless of that task's own outcome, and
reconcile/dedupe if it turns out to have already landed).

**2. Branches and worktrees are not cleaned up when a work plan's content is
fully merged.** Across WP-0002 through WP-0011, every Implementation and
Design & Review sub-agent left its own worktree and branch behind after its
content was merged upstream — by the time WP-0011 closed, 11 worktrees and
over a dozen redundant branches had accumulated with nothing but merged,
now-redundant content. The Backlog thread cleaned these up manually, once,
at the very end, rather than as each work plan actually closed. The
Director asked that this become a standing part of "the work loop," not a
one-time manual sweep.

## Why it might matter

(1) blocks merging any PR built from this template's own governance
process, since the CI check that exists specifically to protect contract
consistency now reliably fails on the pattern the process itself
encourages (citing supporting evidence by path). (2) leaves the repository
cluttered with dead branches/worktrees that make it harder to tell what is
actually in flight versus already landed — exactly the kind of drift
`item-0009`'s new checks were built to catch, just at the git/worktree
layer instead of the document layer.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - Do not weaken the copy-exclusion list itself (agreements/reviews/
    issues/backlog-items/work-plans should stay excluded from adopter
    copies — they are this template's own planning history, not
    adopter-owned content).
  - The fix for (1) most likely means teaching
    `check_dangling_references` (or equivalent) to recognize a reference to
    a path matching `collaboration_template_exclude_paths` as expected-absent
    on a copied target, not a defect — reuse
    `scripts/lib/collaboration-template-paths.sh`'s own pattern list rather
    than hardcoding a second one.
  - For (2), decide where the rule belongs —
    `docs/collaboration/branch-commit-pr-discipline.md` (already carries
    the Implementation-group worktree rule, LISS-0024) is the likely home;
    `docs/collaboration/cross-session-messaging.md` may need a
    cross-reference. Both are ADR-0006 contract files.

## Uncertainty

- [x] Spec can be written now — both problems are concretely reproduced
      (CI run linked below; the worktree list before cleanup is in this
      session's own history).
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none yet — related:
  `scripts/check-contract-consistency.py`,
  `scripts/lib/collaboration-template-paths.sh`,
  `docs/collaboration/branch-commit-pr-discipline.md`,
  PR #16 CI run (`Repository sanity`, failed,
  https://github.com/nn0cl/llm-loop-project-template/actions/runs/32248215256)

## Promotion notes

- Date: 2026-08-19
- Decision: Promoted, in the Backlog-layer thread ("承認"). Per ADR 0016
  Rule 2, this approval is the single design-phase gate — the Design &
  Review group proceeds autonomously from here, including the placement
  decision for the branch-cleanup rule and reconciling with `task_cdbaa1ce`
  if it turns out to have already landed independently.
- Reason: Blocking PR #16's merge (CI red) and explicitly requested by the
  Director as a standing process gap; ready to run.
