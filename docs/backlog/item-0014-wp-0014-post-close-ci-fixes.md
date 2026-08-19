# Backlog item: item-0014-wp-0014-post-close-ci-fixes

## Metadata

- Item ID: item-0014
- Title: Fix two post-close CI failures in WP-0014's content
- Status: promoted
- Created: 2026-08-19
- Updated: 2026-08-19
- Priority hint: high
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

PR #17's CI (`Repository sanity` / `Check contract consistency`) found two
genuine defects in WP-0014's already-Director-closed content:

**1. ADR 0020 cites an unresolvable absolute local path.** Line 151 names
`/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`
formatted as a checkable file reference. This path is on one specific
machine's local disk, in a different, unrelated repository — it will never
exist in CI's checkout, in any clone of this repo, or for any adopter.
Fix: rephrase so the citation reads as prose describing an external
project's file, not as a reference the consistency checker's reference
scanner treats as verifiable (matching how the ADR's own earlier, in-repo
citations correctly do use checkable references).

**2. LISS-0044 sits in WP-0014's blocking "Work-Plan Review" findings
table with `Status: proposed`.** `check_open_findings_gate` (item-0009/
WP-0011, working exactly as designed) correctly flags this: a work plan's
own findings table is for Reviewer-found defects that must be resolved
(`closed` or `wont_do`) before the work plan counts as Done — not for a
tracked-but-intentionally-deferred future-work note. LISS-0044 is the
second kind (explicitly "not actionable until a later work plan first
archives something"), so it was placed in the wrong section. Fix: move the
LISS-0044 reference out of WP-0014's Work-Plan Review findings table into
prose (e.g. a Work Notes or "Deferred Follow-ups" mention) — do not close
or reclassify LISS-0044 itself, it remains open and legitimately deferred.

## Why it might matter

Blocks PR #17 (WP-0013 + WP-0014) from merging. Also a useful real example
of the difference between "a Reviewer finding that blocks close" and "a
tracked note for later work" — worth keeping in mind for facet 5
(drift-prevention CI checks, still queued under item-0012) when it reaches
LISS-0044.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - Do not close or change LISS-0044's own status — it stays `proposed`,
    legitimately deferred.
  - Do not weaken `check_open_findings_gate` — it did its job correctly.
  - `docs/architecture/adr/0020-*.md` is not an ADR-0006 contract file, but
    treat it with the same review rigor already established this session
    for every other ADR change.

## Uncertainty

- [x] Spec can be written now
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/work-plans/WP-0014-document-log-lifecycle-model.md`,
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`,
  PR #17 CI run
  (https://github.com/nn0cl/llm-loop-project-template/actions/runs/32262521956)

## Promotion notes

- Date: 2026-08-19
- Decision: Promoted, in the Backlog-layer thread ("承認"). Per ADR 0016
  Rule 2, Design & Review proceeds autonomously from here.
- Reason: Blocking PR #17's merge (CI red on two genuine, narrow defects);
  ready to run.
